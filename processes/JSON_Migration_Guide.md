# JSON Migration Guide

**Version:** 1.0.0
**Created:** 2026-02-04
**Purpose:** Step-by-step process for converting Trade XLSX files to the JSON data layer.

---

## Overview

This guide documents how to convert an IonWave Trade XLSX file into the JSON data format used by the dynamic dashboard and Claude's data access layer. Follow this process for each of the remaining 34 files (05A-38).

**Key principle:** We're not doing a mechanical cell-for-cell conversion. We're restructuring the data to be semantically clean — removing spreadsheet artifacts (empty rows, merged cells, formatting-as-data) and producing JSON that is both machine-optimal and renderable by the dashboard.

---

## Architecture

```
data/
├── manifest.json                    # System-level index (update for each file migrated)
├── {file_id}/
│   ├── _meta.json                   # File-level metadata
│   ├── {sheet_id}.json              # One file per sheet
│   └── ...
```

- **One JSON file per sheet** (not per workbook)
- **File IDs** use lowercase with underscores: `05a_product_strategy`
- **Sheet IDs** use lowercase with underscores: `product_strategy_mvp`

---

## Step-by-Step Process

### Step 1: Extract Raw Data

Use Python to read all sheets from the XLSX file:

```python
import openpyxl, sys
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('IonWave/{filename}.xlsx', data_only=True)
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    print(f'=== {sheet_name} ===')
    print(f'Max row: {ws.max_row}, Max col: {ws.max_column}')
    for row in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 100), values_only=False):
        values = []
        for cell in row:
            if cell.value is not None:
                v = repr(cell.value)
                if len(v) > 120:
                    v = v[:120] + '...'
                values.append(f'[{cell.coordinate}] {v}')
        if values:
            print('  ' + ' | '.join(values))
    print()
```

### Step 2: Classify Each Sheet

Determine the `data_type` for each sheet:

| Data Type | Description | When to Use | Dashboard Rendering |
|-----------|-------------|-------------|---------------------|
| `structured_table` | Clean rows/columns with headers | Tables, grids, registries | HTML `<table>` |
| `narrative` | Prose content with sections | Theses, playbooks, guides | Formatted sections |
| `hybrid` | Mix of tables and prose | Analysis sheets, audits | Auto-detected sections |
| `template` | Structure defined but data mostly empty | Monitoring templates, trackers | Structure + empty state |

### Step 3: Create the Directory

```bash
mkdir -p "data/{file_id}"
```

### Step 4: Write `_meta.json`

```json
{
  "file_id": "{file_id}",
  "title": "{Human-readable title}",
  "tier": {1-8},
  "version": "1.0.0",
  "quality_score": "{X/10}",
  "audited": {true/false},
  "audited_session": "{session ref or null}",
  "last_updated": "2026-XX-XX",
  "updated_by": "claude-opus-4.5",
  "sheets": [
    {"id": "{sheet_id}", "title": "{Sheet Title}", "data_type": "{type}", "row_count": {N}}
  ],
  "feeds_into": ["{file_id}", ...],
  "requires": ["{file_id}", ...],
  "feedback_loops": [],
  "key_blockers": "{description}",
  "next_action": "{description}"
}
```

### Step 5: Write Sheet JSON Files

Every sheet file has the same envelope:

```json
{
  "_meta": {
    "sheet_name": "{Original Sheet Name}",
    "parent_file": "{file_id}",
    "version": "1.0.0",
    "last_updated": "2026-XX-XX",
    "updated_by": "claude-opus-4.5",
    "status": "draft",
    "quality_score": "{X/10}",
    "data_type": "{type}",
    "note": "{optional context}"
  },
  "data": { ... }
}
```

#### Confidence Metadata

When a data point has quality/confidence information, use inline metadata:

```json
{
  "annual_revenue": {
    "value": "$60-80M",
    "confidence": "B",
    "source": "Industry triangulation",
    "verified": "2026-01-31",
    "upgrade_path": "SEMrush traffic → conversion estimate"
  }
}
```

Confidence grades:
- **A** = Verified from authoritative source
- **B** = Strong single source or good triangulation
- **C** = Industry benchmark with documented methodology
- **D** = Best guess with documented upgrade path

Simple values that don't need tracking stay as plain values:
```json
{"name": "LMNT", "price_point": "$45/box"}
```

#### Structuring Data by Type

**structured_table:** Put the main data in an array of objects:
```json
{
  "data": {
    "assumptions": [
      {"assumption": "CAC", "current_value": "<$40", "confidence": {...}}
    ]
  }
}
```

**narrative:** Use named sections:
```json
{
  "data": {
    "executive_summary": "...",
    "the_problem": ["bullet 1", "bullet 2"],
    "the_solution": {"description": "...", "differentiation": [...]}
  }
}
```

**template:** Include the expected schema alongside the (possibly empty) data:
```json
{
  "data": { "pain_points": [] },
  "template_structure": {
    "pain_points_schema": {"rank": "number", "pain_point": "string", "frequency": "string"}
  }
}
```

### Step 6: Consolidate Duplicate Sheets

Some XLSX files have duplicate/variant sheets (e.g., "Voice of Customer Database" and "Voice of Customer Database1"). Consolidate into a single JSON file with deduplicated data. Note the consolidation in the `_meta.note`.

### Step 7: Update `manifest.json`

Edit `data/manifest.json`:
1. Change the file's `status` from `"xlsx_only"` to `"migrated"`
2. Update `migrated_count`
3. Update `last_updated`

### Step 8: Create Dashboard View (if needed)

For Tier 1-3 files, create a dashboard view page. Copy an existing view (e.g., `strategic-foundation.html`) and update `FILE_ID`. For files that naturally group (like 03A + 03B), combine into a single view.

### Step 9: Verify

```bash
# Validate JSON syntax
python -m json.tool data/{file_id}/*.json > /dev/null

# Check dashboard renders
# Open dashboard/views/{file-id}.html in browser
```

### Step 10: Commit

```bash
git add data/{file_id}/ dashboard/views/{file-id}.html
git commit -m "Migrate {file_id} to JSON data layer"
```

### Step 11: Archive XLSX

```bash
mv IonWave/{filename}.xlsx archive/
```

---

## Checklist for Each File

- [ ] Extract raw data with Python
- [ ] Classify each sheet's data_type
- [ ] Create directory `data/{file_id}/`
- [ ] Write `_meta.json`
- [ ] Write each `{sheet_id}.json` with envelope
- [ ] Consolidate duplicate sheets
- [ ] Map confidence levels (High→A, Medium→B, Low→C, None→D)
- [ ] Add inline confidence metadata where applicable
- [ ] Update `manifest.json` (status, migrated_count)
- [ ] Create/update dashboard view page
- [ ] Validate JSON syntax
- [ ] Test dashboard rendering
- [ ] Git commit
- [ ] Archive XLSX file

---

## Completed Migrations

| File | Sheets | Date | Notes |
|------|--------|------|-------|
| 01_Strategic_Foundation | 5 | 2026-02-04 | First migration, established patterns |
| 02_Market_Intelligence | 10 | 2026-02-04 | Good variety of table/template/hybrid |
| 03A_Customer_Research_ICP | 5 (from 6) | 2026-02-04 | ICP Analysis merged into _meta |
| 03B_Customer_Research_VOC | 7 (from 9) | 2026-02-04 | Duplicate sheets consolidated |
