# Dashboard Update Guide

**Version**: v2.2.0
**Last Updated**: 2026-02-05
**Live URL:** https://caio-camargo.github.io/ionwave-dashboard/
**Repo:** https://github.com/caio-camargo/ionwave-dashboard

---

## Architecture (v2 — Dynamic JSON)

The dashboard is now a **multi-page dynamic site** that loads data from JSON files at runtime. Data is never hardcoded in HTML.

```
dashboard/                          ← Working copy (Google Drive)
├── index.html                      ← Mission Control
├── css/styles.css                  ← Shared stylesheet
├── js/
│   ├── data-loader.js              ← Fetches & caches JSON from data/
│   └── renderers.js                ← Auto-renders by data_type
└── views/
    ├── strategic-foundation.html   ← 01 detail view
    ├── market-intelligence.html    ← 02 detail view
    └── customer-research.html      ← 03A + 03B combined view

data/                               ← JSON data layer (source of truth)
├── manifest.json                   ← Master index
├── 01_strategic_foundation/
├── 02_market_intelligence/
├── 03a_customer_research_icp/
└── 03b_customer_research_voc/
```

### How It Works
1. Dashboard pages use `data-loader.js` to fetch JSON files via `fetch()`
2. `renderers.js` auto-renders content based on the `data_type` field in each sheet's `_meta` envelope
3. Data types: `structured_table` → tables, `narrative` → prose blocks, `hybrid` → mixed, `template` → empty state
4. Confidence badges (A/B/C/D) render inline when data points include confidence metadata

---

## How to Update the Dashboard

### Updating Data (most common)

Data updates don't require touching HTML. Just edit the JSON files:

1. Edit files in `data/{file_id}/` (e.g., update quality scores, add data)
2. Update `_meta.json` if sheet metadata changed (quality_score, status, etc.)
3. Update `data/manifest.json` if file-level status changed
4. Deploy (see below)

The dashboard will reflect changes automatically on next page load.

### Adding a New Trade File View

When migrating a new file to JSON:

1. Create `data/{new_file_id}/` directory with `_meta.json` + sheet JSONs
2. Copy an existing view HTML (e.g., `dashboard/views/strategic-foundation.html`)
3. Change the `FILE_ID` constant to the new file ID
4. Add a nav link in `dashboard/index.html` and all view pages
5. Update `data/manifest.json` status to "migrated"
6. Deploy

### Updating Dashboard Code

If you need to change rendering logic, styles, or page structure:
- **Styles:** Edit `dashboard/css/styles.css`
- **Data fetching:** Edit `dashboard/js/data-loader.js`
- **Rendering:** Edit `dashboard/js/renderers.js`
- **Pages:** Edit the relevant HTML file in `dashboard/` or `dashboard/views/`

---

## Deployment

The GitHub Pages repo has a **flat structure** (dashboard contents at root + data/ alongside). Deployment requires assembling this structure.

### Quick Deploy

```bash
# From IonWave Bootstrap directory:

# 1. Create temp deploy directory
mkdir _deploy
cp index.html _deploy/              # CRITICAL: Use ROOT index.html (not dashboard/index.html)
cp -r dashboard _deploy/            # Copy entire dashboard folder
cp -r data _deploy/data
touch _deploy/.nojekyll             # REQUIRED: prevents Jekyll from ignoring _meta.json files

# 2. Init, commit, push
cd _deploy
git init
git remote add origin https://github.com/caio-camargo/ionwave-dashboard.git
git add -A
git commit -m "Update dashboard"
git branch -M main
git push -u origin main --force

# 3. Clean up
cd ..
rm -rf _deploy
```

Site auto-deploys in ~1-2 minutes at https://caio-camargo.github.io/ionwave-dashboard/

### Important: Path Handling

`data-loader.js` auto-detects its base path:
- Pages at root (`index.html`) → fetches from `data/`
- Pages in `views/` → fetches from `../data/`

This means the same JS works in both the local `dashboard/` structure and the flat GitHub Pages structure.

---

## Data Source Mapping

| Dashboard Section | JSON Source |
|---|---|
| Mission Control stats | `data/manifest.json` |
| Trade file grid | `data/manifest.json` → `files` object |
| Dependency chains | `data/manifest.json` → `dependency_chains` |
| Feedback loops | `data/manifest.json` → `feedback_loops` |
| Individual file views | `data/{file_id}/_meta.json` + sheet JSONs |
| Quality scores | Each sheet's `_meta.quality_score` |
| Confidence badges | Inline `{value, confidence, source}` objects in sheet data |

---

## Known Issues & Gotchas

### CRITICAL: Dual index.html Files

**Issue**: The project has TWO separate `index.html` files that must be kept in sync:

1. **`dashboard/index.html`** - Working copy in the dashboard directory
2. **`index.html`** (root) - Copy for GitHub Pages deployment

**Why This Exists**:
- GitHub Pages serves from root `index.html` at https://caio-camargo.github.io/ionwave-dashboard/
- Local development works from `dashboard/index.html`
- The root copy uses adjusted paths (`dashboard/css/` instead of `css/`)

**Problem**:
If you update `dashboard/index.html` but forget to update root `index.html`, changes won't appear on GitHub Pages even after deployment completes.

**Solution**:
When updating Mission Control homepage content:
1. Edit `dashboard/index.html` first
2. Copy relevant changes to root `index.html`
3. Adjust paths in root copy:
   - `views/` → `dashboard/views/`
   - `css/` → `dashboard/css/`
   - `js/` → `dashboard/js/`
4. Commit BOTH files
5. Push to GitHub

**Example (Hypotheses System section added 2026-02-05)**:
- Updated `dashboard/index.html` with new section
- Forgot to update root `index.html`
- Result: Changes didn't appear on GitHub Pages for over an hour
- Fix: Added same section to root `index.html` with corrected paths

**Future Prevention**:
Consider consolidating to a single index.html with smart path detection, or document this clearly in session handoffs.

### CRITICAL: Deployment Uses Root index.html

**Issue**: The deployment process requires using the **root `index.html`** file, not `dashboard/index.html`. Using the wrong file causes 404 errors on GitHub Pages.

**Symptoms**:
- Homepage 404s after deployment
- All dashboard views return 404
- CSS and JS files fail to load

**Root Cause**: The root `index.html` has paths like `dashboard/css/styles.css` for GitHub Pages' flat structure, while `dashboard/index.html` has paths like `css/styles.css` for local development.

**Solution**: Always deploy with:
```bash
cp index.html _deploy/              # Use ROOT index.html
cp -r dashboard _deploy/            # Copy entire dashboard folder
```

**NOT**:
```bash
cp -r dashboard/index.html dashboard/css dashboard/js ... _deploy/  # WRONG!
```

**2026-02-05 Example**:
- Deployed using `dashboard/index.html` → entire site 404'd
- Fixed by redeploying with root `index.html` → site loaded correctly

### Jekyll Processing & Underscore Files

**Issue**: GitHub Pages uses Jekyll by default, which **ignores all files starting with underscores** (like `_meta.json`). This causes 404 errors when dashboard tries to fetch data files.

**Symptoms**:
- Dashboard pages show "Loading..." forever
- Console shows `404 (Not Found)` errors for `_meta.json` files
- Mission Control loads fine (doesn't use underscore files) but file views hang

**Solution**: Add a `.nojekyll` file to the repository root

```bash
# From repository root:
touch .nojekyll
git add .nojekyll
git commit -m "Add .nojekyll to serve underscore-prefixed files"
git push origin main
```

**Why This Works**: The `.nojekyll` file tells GitHub Pages to skip Jekyll processing entirely and serve all files as-is, including those starting with underscores.

**Discovered**: 2026-02-05, Session #4 (troubleshooting dashboard view pages)

**Prevention**: The `.nojekyll` file is now committed to the repo. If you ever create a fresh deployment or new repo, remember to add this file immediately.

### GitHub Pages Deployment Lag

**Normal behavior**: Changes appear 2-5 minutes after push
**Large commits**: Can take 10-15 minutes (many files, new directories)
**Caching issues**: Hard refresh (Ctrl+Shift+R) may be needed to see updates

If changes don't appear after 15 minutes:
1. Check that BOTH index.html files were updated (see above)
2. Verify commit was pushed to `main` branch (not `master`)
3. Check GitHub Actions for deployment status
4. Clear browser cache completely
5. Check if `.nojekyll` file exists (required for underscore files)

---

## Legacy Architecture (v1 — Deprecated)

The original dashboard was a single `dashboard.html` file with all data hardcoded inline. That file still exists in the project root but is no longer maintained or deployed. The old approach:
- Single HTML file, all CSS/JS inline, zero dependencies
- Data hardcoded in HTML (not dynamically loaded)
- Required manual editing of HTML to update data
- No connection to the JSON data layer

The old `dashboard.html` can be deleted once the v2 dashboard is stable.
