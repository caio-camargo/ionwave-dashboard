# VERSION MANIFEST
**Last Updated:** 2026-02-03 by Claude  
**Purpose:** Track current version of all versionable files for auto-increment

---

## HOW THIS WORKS

### When Claude Generates Updated File:
1. Claude reads this manifest to find current version
2. Claude auto-increments **patch** version (+0.0.1)
3. Claude generates: `filename_v{major}.{minor}.{patch}.ext`
4. Claude updates this manifest with new version
5. **YOU: Download file, upload to project, swap in the new version, delete old when ready**

### When You Want Major/Minor Bump:
1. Download Claude's output (e.g., `file_v1.0.5.ext`)
2. Rename to desired version (e.g., `file_v1.1.0.ext` or `file_v2.0.0.ext`)
3. Upload renamed file to project
4. Claude will detect new version and continue from there

### Version Increment Rules:
- **Patch (+0.0.1):** Claude auto-increments every time (default)
- **Minor (+0.1.0):** You rename manually for new sections/sheets added
- **Major (+1.0.0):** You rename manually for restructures/breaking changes

### Cleanup:
- Keep 2-3 recent versions in project for rollback
- Delete older versions manually when space needed
- This manifest only tracks current/latest version

---

## ARCHITECTURE DOCUMENTS (31 files)

| File | Current Version | Last Updated | Notes |
|------|----------------|--------------|-------|
| 00_MASTER_CONTROL.md | v1.0.0 | 2026-02-03 | Initial version |
| 00_START_HERE.md | v1.0.0 | 2026-02-03 | Initial version |
| 01_Studio3_Context.md | v1.0.0 | 2026-02-03 | Initial version |
| 02_Glossary.md | v1.0.0 | 2026-02-03 | Initial version |
| 03_What_We_Did.md | v1.0.0 | 2026-02-03 | Initial version |
| 04_Working_Principles.md | v2.0.1 | 2026-02-03 | Added inline grading standard |
| Categorization_And_Order_Of_Work.md | v1.0.0 | 2026-02-03 | Initial version |
| Categorization_Final_Analysis.md | v1.0.0 | 2026-02-03 | Initial version |
| CM_System_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| Deliverable_Structure_Standards.md | v1.0.0 | 2026-02-03 | NEW - Just created |
| DEMO_How_System_Works.md | v1.0.0 | 2026-02-03 | Initial version |
| Dependency_Map.md | v1.0.0 | 2026-02-03 | Initial version |
| Extraction_Execution_Plan.md | v1.0.0 | 2026-02-03 | Initial version |
| Extraction_Progress.md | v1.0.0 | 2026-02-03 | Initial version |
| Extraction_Roadmap.md | v1.0.0 | 2026-02-03 | Initial version |
| FINAL_Categorization.md | v1.0.0 | 2026-02-03 | Initial version |
| Knowledge_Logistics_Audit.md | v1.0.0 | 2026-02-03 | Initial version |
| Market_Landscape_Bootstrap_Plan__1_.md | v1.0.0 | 2026-02-03 | Initial version |
| Master_Index.md | v1.0.0 | 2026-02-03 | Initial version |
| Model_Orchestration.md | v2.0.1 | 2026-02-03 | Added Pattern 6 |
| ODD_System_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| Operator_Management_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| README.md | v1.0.0 | 2026-02-03 | Initial version |
| README_START_HERE.md | v1.0.0 | 2026-02-03 | Initial version |
| README_START_HERE__1_.md | v1.0.0 | 2026-02-03 | Initial version |
| School_System_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| Strategic_Games_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| Trade_Structure_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| TUP_System_Overview.md | v1.0.0 | 2026-02-03 | Initial version |
| Workbook_Generation_Summary.md | v1.0.0 | 2026-02-03 | Initial version |

**Note:** Discrepancy_Register.md is a tracking doc and is NOT versioned per your instruction

---

## DOMAIN FILES (38 files)

| File | Current Version | Last Updated | Notes |
|------|----------------|--------------|-------|
| 01_Strategic_Foundation.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 02_Market_Intelligence.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 03A_Customer_Research_ICP.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 03B_Customer_Research_VOC.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 04_Planning_Roadmaps.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 05A_Product_Strategy.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 05B_Formulation_Supply.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 06_Unit_Economics.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 07_Offer_Strategy.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 08_Financial_Model.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 09_Brand_Messaging.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 10A_Creative_Strategy.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 11A_Funnel_Strategy.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 11B_Pages_Email.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 12_Media_Acquisition.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 13_Content_SEO.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 14_Community_Engagement.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 15_Operations_Fulfillment.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 16_Team_Organization.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 17_Legal_Compliance.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 18_Analytics_Reporting.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 19_Systems_Automation.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 20_Fundraising.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 21_Expansion_Growth.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 22_Research_Development.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 23_Decision_Support.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 24_Command_Navigation.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 25_Partnerships_Influencers.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 27_Customer_Experience_Journey.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 28_Process_Workflows.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 29_Data_Information_Mgmt.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 30_Risk_Crisis_Management.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 31_Implementation_Execution.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 32_Quality_Standards.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 33_Governance_Structure.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 34_Performance_Optimization.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 35_Training_Enablement.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 36_Reference_Specifications.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 37_Strategic_Initiatives.xlsx | v1.0.0 | 2026-02-03 | Initial version |
| 38_Cross_Functional_Support.xlsx | v1.0.0 | 2026-02-03 | Initial version |

---

## MASTER MODEL (1 file)

| File | Current Version | Last Updated | Notes |
|------|----------------|--------------|-------|
| IonWave_Ops_Model_v10_Organized.xlsx | v10.0.0 | 2026-02-03 | Current master (already has v10 in name) |

**Note:** This file already has v10 in its name. Next update will be v10.0.1 unless you do major restructure.

---

## TRACKING DOCUMENTS (NOT VERSIONED)

The following files are tracking docs and do NOT get versioned per your instruction:
- Decision_Log.md
- Open_Questions.md
- Discrepancy_Register.md
- Changes_Tracker.md
- Execution_Status.md
- Trade_Execution_Tracker.md
- All CM tracking files (CM_Alert_Log.md, CM_KPI_Tracker.md, etc.)
- All operational trackers (AB_Test_Log.md, Budget_Spend_Log.md, etc.)

---

## MANIFEST VERIFICATION WORKFLOW

**Run this daily or when in doubt:**

1. **Manual check:** Scan project directory for files without version numbers
2. **List check:** Compare project files to this manifest - any missing?
3. **Duplicate check:** Are there multiple versions of same file? (cleanup needed)
4. **Tracking doc check:** Are tracking docs accidentally getting versioned? (should not be)
5. **Update manifest:** Add any new files, mark any deprecated files

**Example verification:**
```
Project has: 02_Market_Intelligence.xlsx AND 02_Market_Intelligence_v1.0.1.xlsx
Action: Delete the one without version number, keep v1.0.1
Update: Nothing needed in manifest (already shows v1.0.1)
```

---

## AUTO-INCREMENT EXAMPLE

**Before:**
```
Manifest shows: 02_Market_Intelligence.xlsx = v1.0.0
```

**Claude generates update:**
```
Claude reads manifest: v1.0.0
Claude increments: v1.0.0 + 0.0.1 = v1.0.1
Claude outputs: 02_Market_Intelligence_v1.0.1.xlsx
Claude updates manifest: v1.0.1
Claude tells you: "Download 02_Market_Intelligence_v1.0.1.xlsx, upload to project, swap out v1.0.0"
```

**After you swap:**
```
Project now has: 02_Market_Intelligence_v1.0.1.xlsx
Old v1.0.0 deleted (or kept for rollback)
Manifest shows: v1.0.1
Next generation will be v1.0.2
```

---

## SPECIAL CASES

### New File Created
```
Claude creates: 99_New_Deliverable_v1.0.0.xlsx
Claude adds to manifest: 99_New_Deliverable.xlsx = v1.0.0
```

### You Make Manual Changes
```
You edit v1.0.1 in Excel
You save as: v1.0.2
You upload v1.0.2 to project
Claude sees v1.0.2 in manifest, next will be v1.0.3
```

### Multiple Files in One Session
```
Claude updates 3 files:
- 02_Market_Intelligence.xlsx: v1.0.0 → v1.0.1
- 04_Working_Principles.md: v2.0.1 → v2.0.2
- Model_Orchestration.md: v2.0.1 → v2.0.2

All get new versions, manifest updated once at session end
```

---

**Status:** INITIALIZED  
**Files tracked:** 72 versionable files  
**Next:** Claude will auto-increment on first update
