# classify_tabs.py
import json, re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DUMP_DIR = BASE_DIR / 'ops_model_v10_dump'
MANIFEST = DUMP_DIR / '_manifest.json'
OUTPUT   = DUMP_DIR / '_classification.json'

STRUCTURAL = {
    '0. Start Here', 'S4-Taxonomy', 'Flash Teams Model', 'Directory',
    'Role Rosters', 'Access Model', 'Master Cluster Map',
    'Parallel Execution Map', 'Dependency Graph', 'Role Index',
    'Three-Level Architecture', 'Instructions Spec',
    'S4-Implementation Spec', 'S4-Passet Lifecycle', 'Librarian Role',
    'Launch Narrative', 'Initial Conditions Audit', 'Revised Roles',
    'MC Entertainment Spec',
}

TUP_RE = re.compile(r'^(P|C|IP|V)-(.+)$')

def tup_id(n):
    m = TUP_RE.match(n)
    return m.group(2).strip() if m else None

def classify_cat(n):
    if n.startswith('P-'):  return 'P_tab'
    if n.startswith('C-'):  return 'C_tab'
    if n.startswith('IP-'): return 'IP_tab'
    if n.startswith('V-'):  return 'V_tab'
    if n.startswith('NAV-'): return 'NAV_tab'
    if n in STRUCTURAL: return 'structural'
    return 'content'

def subst(fp, rc):
    if rc <= 3: return False, rc
    try: d = json.loads(fp.read_text(encoding='utf-8'))
    except Exception: return False, 0
    rows = d.get('rows', [])
    ne = sum(1 for r in rows if any(v is not None and str(v).strip() for v in r.values()))
    return ne > 3, ne

def main():
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    sheets, total = manifest['sheets'], manifest['sheet_count']
    print(f'Manifest: {total} sheets')
    for s in sheets:
        s['cat'] = classify_cat(s['name'])
        s['tid'] = tup_id(s['name'])
    cur = None
    for s in sheets:
        c, n = s['cat'], s['name']
        if c == 'P_tab': cur = tup_id(n)
        elif c in ('C_tab','IP_tab'):
            t = tup_id(n)
            if t: cur = t
        s['tup'] = cur if c == 'content' else s['tid']
    print('Checking substance ...')
    for s in sheets:
        if s['cat'] == 'content':
            s['sub'], s['ne'] = subst(DUMP_DIR / s['filename'], s['row_count'])
        else:
            s['sub'], s['ne'] = None, s['row_count']
    cats = {}
    for s in sheets: cats[s['cat']] = cats.get(s['cat'], 0) + 1
    by_tup = {}
    for s in sheets:
        if s['cat'] == 'content':
            k = s['tup'] or '_unassigned'
            by_tup.setdefault(k, []).append({
                'index': s['index'], 'name': s['name'],
                'filename': s['filename'], 'row_count': s['row_count'],
                'is_substantive': s['sub'], 'non_empty_rows': s['ne']})
    empty = [{'index': s['index'], 'name': s['name'],
              'filename': s['filename'], 'row_count': s['row_count'],
              'tup_cluster': s['tup']}
             for s in sheets if s['cat'] == 'content' and not s['sub']]
    depth = {}
    for s in sheets:
        if s['cat'] == 'content' and s['sub']:
            k = s['tup'] or '_unassigned'
            depth[k] = depth.get(k, 0) + s['ne']
    out = {
        'meta': {'source': str(MANIFEST), 'total_sheets': total, 'script': 'classify_tabs.py'},
        'category_counts': cats,
        'content_tabs_by_tup': by_tup,
        'empty_or_template_tabs': empty,
        'content_depth_score_per_cluster': depth,
        'all_sheets': [
            {'index': s['index'], 'name': s['name'], 'category': s['cat'],
             'tup_cluster': s.get('tup'), 'row_count': s['row_count'],
             'is_substantive': s['sub'], 'non_empty_rows': s['ne']}
            for s in sheets],
    }
    OUTPUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Written: {OUTPUT}')
    sep = '=' * 60
    print(); print(sep); print('SUMMARY'); print(sep)
    print(); print('Category counts:')
    for c2, n2 in sorted(cats.items()): print(f'  {c2:15s}  {n2:4d}')
    print(f'  TOTAL            {sum(cats.values()):4d}')
    print(); print(f'Content by TUP ({len(by_tup)} clusters):')
    for t in sorted(by_tup):
        tabs = by_tup[t]
        ns = sum(1 for x in tabs if x['is_substantive'])
        print(f'  {t:20s}  {len(tabs):3d} tabs  ({ns} substantive)')
    print(); print(f'Empty/template tabs: {len(empty)}')
    for e in empty[:20]:
        idx, nm, rc = e['index'], e['name'], e['row_count']
        print(f'  [{idx:4d}] {nm:50s}  rows={rc}')
    if len(empty) > 20: print(f'  ... and {len(empty)-20} more')
    print(); print('Depth scores (top 20):')
    for t, sc in sorted(depth.items(), key=lambda x: -x[1])[:20]:
        print(f'  {t:20s}  depth={sc}')
    print(); print(sep); print('Done.')

if __name__ == '__main__':
    main()
