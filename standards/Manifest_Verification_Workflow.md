# Manifest Verification Workflow
**Purpose:** Daily/periodic check to ensure VERSION_MANIFEST.md is accurate  
**Frequency:** Run daily or when in doubt about file versions  
**Owner:** Danilo (manual process)

---

## QUICK VERIFICATION CHECKLIST

Run through these checks in order:

### 1. Scan for Unversioned Files
**Look for:** Files in project without `_v{x}.{x}.{x}` in filename

**What to check:**
- Architecture docs (*.md files)
- Domain files (01-38 *.xlsx files)
- Master model file

**If found:**
```
Example: Found "02_Market_Intelligence.xlsx" (no version)
Action: Check if versioned copy exists (e.g., "02_Market_Intelligence_v1.0.0.xlsx")
  - If versioned copy exists: Delete the unversioned one
  - If no versioned copy: Rename to add _v1.0.0, update manifest
```

---

### 2. Check for Duplicates
**Look for:** Multiple versions of same file

**What to check:**
```
Example: 
- 02_Market_Intelligence_v1.0.0.xlsx
- 02_Market_Intelligence_v1.0.1.xlsx
- 02_Market_Intelligence_v1.0.2.xlsx
```

**Decision:**
- Keep latest version (v1.0.2 in example)
- Keep 1-2 previous versions for rollback if desired
- Delete older versions if space needed
- Verify manifest shows latest version (v1.0.2)

---

### 3. Compare Manifest to Project Directory
**Look for:** Files in project not listed in manifest, or vice versa

**Process:**
1. List all files in `/mnt/project/`
2. Compare to manifest entries
3. Add any missing files to manifest
4. Mark any deprecated/deleted files in manifest

**If file in project but not in manifest:**
```
Example: Found "40_New_Domain.xlsx" in project, not in manifest
Action: Add to manifest as v1.0.0
```

**If file in manifest but not in project:**
```
Example: Manifest shows "Old_Deprecated.md" but not in project
Action: Add note to manifest: "v1.0.0 | 2026-01-15 | DEPRECATED - removed from project"
```

---

### 4. Check Tracking Docs Aren't Versioned
**Look for:** Tracking docs with version numbers (they shouldn't have them)

**Tracking docs list:**
- Decision_Log.md
- Open_Questions.md
- Discrepancy_Register.md
- Changes_Tracker.md
- All CM_*.md files
- All *_Tracker.md files
- All *_Log.md files

**If found versioned:**
```
Example: Found "Decision_Log_v1.0.0.md"
Action: Rename to "Decision_Log.md" (remove version)
Note: These files should NOT be versioned
```

---

### 5. Validate Version Sequence
**Look for:** Version numbers that don't make sense

**Check for:**
- Skipped versions (v1.0.0 → v1.0.2, missing v1.0.1)
- Backward versions (v1.0.5 exists but manifest shows v1.0.3)
- Malformed version numbers (v1.0 instead of v1.0.0)

**If found:**
```
Example: Manifest shows v1.0.3 but project has v1.0.5
Action: Update manifest to v1.0.5 (project is source of truth)
Note: Skipped versions are OK (maybe you manually bumped)
```

---

## COMMON ISSUES AND FIXES

### Issue 1: File Without Version Number
**Symptoms:** File like `02_Market_Intelligence.xlsx` with no version

**Diagnosis:**
- Check if versioned copy exists elsewhere
- Check manifest - what version should it be?

**Fix:**
```
If versioned copy exists (e.g., v1.0.0):
  → Delete unversioned file
  
If no versioned copy:
  → Rename file to add _v1.0.0 (or current version from manifest)
  → Upload renamed file
```

---

### Issue 2: Multiple Versions Cluttering Project
**Symptoms:** 3+ versions of same file in project

**Diagnosis:**
- Which is latest? (highest version number)
- How many to keep? (usually 2-3 for rollback)

**Fix:**
```
Keep: Latest version + 1-2 previous
Delete: Older versions

Example:
Keep: v1.0.5, v1.0.4, v1.0.3
Delete: v1.0.2, v1.0.1, v1.0.0
```

---

### Issue 3: Manifest Out of Sync
**Symptoms:** Manifest shows v1.0.0 but project has v1.0.5

**Diagnosis:**
- Did you manually update without updating manifest?
- Did Claude generate update but manifest didn't save?

**Fix:**
```
Project is source of truth
→ Update manifest to match project (v1.0.5)
→ Next Claude generation will be v1.0.6
```

---

### Issue 4: Tracking Doc Got Versioned
**Symptoms:** File like `Decision_Log_v1.0.0.md` exists

**Diagnosis:**
- Tracking docs should NOT have versions
- Someone accidentally added version number

**Fix:**
```
→ Rename to remove version: Decision_Log_v1.0.0.md → Decision_Log.md
→ Upload renamed file
→ Delete versioned copy
```

---

### Issue 5: New File Not in Manifest
**Symptoms:** File in project that's not listed in manifest

**Diagnosis:**
- Newly created file
- Forgot to add to manifest

**Fix:**
```
→ Add to appropriate section in manifest
→ If no version number, add as v1.0.0
→ If has version number, record that version
```

---

## DETAILED VERIFICATION PROCESS

### Step-by-Step

**1. Generate file list from project:**
```
In project files, list all:
- *.md files (excluding tracking docs)
- *.xlsx files (all of them)
Count: Should be ~72 files
```

**2. Open VERSION_MANIFEST.md:**
```
Check manifest sections:
- Architecture Documents (should be ~31 files)
- Domain Files (should be 38 files)
- Master Model (should be 1 file)
Total: ~70 files (some may be deprecated)
```

**3. Cross-reference:**
```
For each file in project:
  → Is it in manifest?
  → Does version match?
  → Is it a tracking doc? (shouldn't be versioned)

For each file in manifest:
  → Does it exist in project?
  → Is version accurate?
```

**4. Note discrepancies:**
```
Make list of issues:
- Files without versions
- Duplicate versions
- Manifest mismatches
- Tracking docs with versions
```

**5. Fix issues:**
```
Work through list:
- Rename files to add/fix versions
- Delete duplicate versions
- Update manifest entries
- Remove versions from tracking docs
```

**6. Update manifest timestamp:**
```
At top of VERSION_MANIFEST.md:
**Last Updated:** [today's date] by Danilo
```

---

## AUTOMATION NOTES

**What could be automated (future):**
- Script to scan project and compare to manifest
- Auto-generate list of discrepancies
- Flag files without versions
- Suggest cleanup actions

**What must stay manual:**
- Decision on which versions to keep/delete
- Decision on when to bump minor/major version
- Actual file operations (delete, rename, upload)
- Manifest text updates

---

## FREQUENCY RECOMMENDATIONS

**Daily:** Quick scan for obvious issues
- Any unversioned files?
- Any new files to add?
- Manifest timestamp recent?

**Weekly:** Full verification
- Run all 5 checks
- Clean up old versions
- Verify no tracking docs versioned
- Update manifest notes

**After major work:** Immediate check
- Did Claude update multiple files?
- Are all updates reflected in manifest?
- Any files need manual version bump?

---

## EXAMPLE VERIFICATION SESSION

```
DATE: 2026-02-03
VERIFIER: Danilo

CHECK 1 - UNVERSIONED FILES:
- Found: 04_Working_Principles.md (no version)
- Action: Versioned copy exists (v2.0.1), deleted unversioned
- Result: ✅ Fixed

CHECK 2 - DUPLICATES:
- Found: 02_Market_Intelligence_v1.0.0, v1.0.1, v1.0.2
- Action: Kept v1.0.2 and v1.0.1, deleted v1.0.0
- Result: ✅ Cleaned up

CHECK 3 - MANIFEST COMPARISON:
- Manifest complete, all files accounted for
- Added: Deliverable_Structure_Standards.md v1.0.0
- Result: ✅ Up to date

CHECK 4 - TRACKING DOCS:
- All tracking docs properly unversioned
- Result: ✅ No issues

CHECK 5 - VERSION SEQUENCE:
- All versions sequential and sensible
- Result: ✅ Validated

SUMMARY:
- 2 minor issues fixed
- Manifest updated with new file
- Timestamp updated to 2026-02-03
- Status: ✅ VERIFIED
```

---

**Status:** Workflow defined  
**First verification:** Run after uploading VERSION_MANIFEST.md  
**Owner:** Danilo  
**Cadence:** Daily quick check, weekly full verification
