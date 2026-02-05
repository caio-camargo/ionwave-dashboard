# DOCUMENT METADATA STANDARDS
**Version**: v1.0.0  
**Author**: Claude (with Caio)  
**Date Created**: 2026-02-03  
**AI Model**: claude-sonnet-4.5-20250929  
**Purpose**: Establish metadata standards for all Studio 3 documents  
**Status**: Draft - Awaiting Approval  
**Related Files**: VERSION_MANIFEST.md, 04_Working_Principles_updated.md

---

## OVERVIEW

Every document in Studio 3 must have structured metadata to enable:
- Version tracking and rollback capability
- Authorship and collaboration clarity
- AI model transparency (for reproducibility)
- Status and lifecycle management
- Dependency mapping
- Quality and confidence assessment

---

## METADATA SCHEMA

### REQUIRED FIELDS (All Documents)

```markdown
**Version**: v{major}.{minor}.{patch}
**Author**: {Primary author(s)}
**Date Created**: YYYY-MM-DD
**Date Modified**: YYYY-MM-DD (if different from created)
**Purpose**: {One-sentence description}
**Status**: {Draft | Review | Final | Deprecated | Ephemeral}
```

### CONDITIONAL FIELDS

**For AI-Generated Content**:
```markdown
**AI Model**: {model-identifier}
**AI Role**: {Framework Application | Research | Analysis | Code Generation}
**Human Validation**: {None | Reviewed | Validated | Approved}
```

**For Versioned Files**:
```markdown
**Related Files**: {List of dependencies or related docs}
**Change Log**: {What changed from previous version}
**Breaking Changes**: {Yes/No - if yes, describe}
```

**For Methodology/Framework Documents**:
```markdown
**Framework Type**: {Strategic Analysis | Quality Standard | Process Workflow}
**Target Grade**: {A | B | C - if applicable}
**Time Budget**: {X hours/mins - if applicable}
**Validated Against**: {Reference case or test}
```

**For Ephemeral Process Documents**:
```markdown
**Lifecycle**: {Single-Use | Time-Bound | Superseded By}
**Retention**: {Delete After | Archive | Integrate Into}
**Process Stage**: {Working | Reference | Historical}
```

---

## DOCUMENT CLASSIFICATION

### CLASS 1: VERSIONED OPERATIONAL DOCUMENTS
**Examples**: Trade files (38 .xlsx), Master docs (31 .md), IonWave_Ops_Model

**Required Metadata**:
- Version (tracked in VERSION_MANIFEST)
- Author
- Date Created / Modified
- Purpose
- Status
- Related Files
- Change Log

**Versioning Rules**:
- Auto-increment patch (+0.0.1) by default
- Minor bump (+0.1.0) when adding sections/sheets
- Major bump (+1.0.0) for restructures/breaking changes
- Tracked in VERSION_MANIFEST.md

**Example Header**:
```markdown
# 02_MARKET_INTELLIGENCE
**Version**: v1.0.1
**Author**: Caio, Danilo, Claude (collaborative)
**Date Created**: 2026-02-03
**Date Modified**: 2026-02-03
**AI Model**: claude-sonnet-4.5-20250929 (competitive intel sections)
**Purpose**: Competitive intelligence, market data, strategic frameworks for IonWave
**Status**: Final
**Related Files**: 03A_Customer_Research_ICP.xlsx, 03B_Customer_Research_VOC.xlsx
**Change Log**: v1.0.1 - Added CI Quality Standards, Current State Assessment, Intelligence Gaps Analysis sheets; updated Competitive Intel with graded LMNT data
```

---

### CLASS 2: METHODOLOGY & FRAMEWORK DOCUMENTS
**Examples**: Porter's Five Forces Methodology, CI Playbook, Quality Standards

**Required Metadata**:
- Version (tracked in VERSION_MANIFEST)
- Author
- Date Created / Modified
- AI Model (if AI-generated)
- Purpose
- Status
- Framework Type
- Target Grade / Time Budget
- Validated Against

**Versioning Rules**:
- Start at v1.0.0 when methodology is complete
- Patch (+0.0.1) for clarifications, examples, minor refinements
- Minor (+0.1.0) for new sections or significant enhancements
- Major (+1.0.0) for fundamental approach changes

**Example Header**:
```markdown
# PORTER'S FIVE FORCES - EXECUTION METHODOLOGY
**Version**: v1.0.0
**Author**: Claude
**Date Created**: 2026-02-03
**AI Model**: claude-sonnet-4.5-20250929
**Purpose**: Reusable framework for category-level competitive analysis using Porter's Five Forces
**Status**: Draft - Awaiting Approval
**Framework Type**: Strategic Analysis
**Target Grade**: B-grade (2 hours Track A work)
**Time Budget**: 2 hours (B-grade), 4 hours (A-grade)
**Validated Against**: IonWave / Electrolyte Category (pending execution)
**Related Files**: Competitive_Intelligence_Playbook_v0_1.xlsx, 02_Market_Intelligence.xlsx
```

---

### CLASS 3: EPHEMERAL PROCESS DOCUMENTS
**Examples**: Working drafts, iteration files, temporary analysis, uploaded reference materials

**Required Metadata**:
- Author
- Date Created
- Purpose
- Status: Ephemeral
- Lifecycle
- Retention instructions
- Process Stage

**Versioning Rules**:
- **NOT versioned** (not tracked in VERSION_MANIFEST)
- Include iteration/date in filename if multiple versions exist
- Example: `LMNT_Analysis_2026-01-31_v8.xlsx` → `LMNT_Analysis_2026-01-31_v9.xlsx`

**Example Header**:
```markdown
# LMNT INVESTOR LENS v9
**Author**: Danilo, Claude
**Date Created**: 2026-01-31
**AI Model**: claude-sonnet-4.5-20250929
**Purpose**: Competitive intelligence iteration on LMNT for IonWave bootstrap
**Status**: Ephemeral - Superseded By Integration
**Lifecycle**: Single-Use (integrated into 02_Market_Intelligence_v1.0.1.xlsx)
**Retention**: Archive for historical reference, not tracked in VERSION_MANIFEST
**Process Stage**: Historical (work complete, content integrated)
**Related Files**: 02_Market_Intelligence_v1.0.1.xlsx (final integrated version)
```

---

### CLASS 4: TRACKING DOCUMENTS (NOT VERSIONED)
**Examples**: Decision_Log.md, Open_Questions.md, Discrepancy_Register.md, AB_Test_Log.md

**Required Metadata**:
- Author (typically "Collaborative - Ongoing")
- Date Created
- Purpose
- Status: Live Tracking (Not Versioned)
- Update Frequency

**Versioning Rules**:
- **NOT versioned** per your explicit instruction
- Append-only or update-in-place
- No VERSION_MANIFEST entry

**Example Header**:
```markdown
# DECISION LOG
**Author**: Collaborative - Ongoing
**Date Created**: 2026-02-03
**Purpose**: Record all strategic decisions with rationale and context
**Status**: Live Tracking (Not Versioned)
**Update Frequency**: As decisions are made
**Related Files**: Open_Questions.md, VERSION_MANIFEST.md
```

---

## AI MODEL IDENTIFIERS

### Current Models in Use

| Model | Identifier | When to Use |
|-------|------------|-------------|
| Claude Sonnet 4.5 | claude-sonnet-4.5-20250929 | Default for all work |
| Claude Opus 4.5 | claude-opus-4-5-20251101 | Complex reasoning, extended analysis |
| Claude Haiku 4.5 | claude-haiku-4-5-20251001 | Quick tasks, simple formatting |

### When to Document AI Model

**ALWAYS document** when AI:
- Generated methodology or frameworks
- Performed competitive analysis or research
- Applied strategic frameworks (Porter's, etc.)
- Created quality standards or grading criteria
- Generated code or automation

**Optional to document** when AI:
- Formatted existing content
- Fixed typos or grammar
- Reorganized existing information
- Merged duplicate content

**Purpose**: Reproducibility and transparency. If someone needs to validate or recreate the analysis, they know which model was used.

---

## AUTHOR ATTRIBUTION GUIDELINES

### Single Author
```markdown
**Author**: Caio
```

### Multiple Distinct Authors
```markdown
**Author**: Danilo (strategy), Claude (execution)
```

### Collaborative / Iterative
```markdown
**Author**: Caio, Danilo, Claude (collaborative)
```

### AI-Primary with Human Validation
```markdown
**Author**: Claude
**Human Validation**: Reviewed by Caio (approved 2026-02-03)
```

### Unknown or Legacy
```markdown
**Author**: Unknown (pre-dating metadata standards)
**Last Modified**: Caio (2026-02-03)
```

---

## STATUS DEFINITIONS

| Status | Meaning | Who Can Change |
|--------|---------|----------------|
| **Draft** | Work in progress, not reviewed | Author |
| **Review** | Ready for feedback, not finalized | Author → Reviewer |
| **Final** | Approved, ready for use | Reviewer → Author |
| **Deprecated** | Superseded by newer version | Author |
| **Ephemeral** | Temporary, will be archived/deleted | Author |
| **Live Tracking** | Ongoing append-only doc (not versioned) | Anyone |

---

## FILENAME CONVENTIONS

### Versioned Files
**Format**: `{Name}_v{major}.{minor}.{patch}.{ext}`

**Examples**:
- `02_Market_Intelligence_v1.0.1.xlsx`
- `Porters_Five_Forces_Methodology_v1.0.0.md`
- `IonWave_Ops_Model_v10.0.1.xlsx`

**Note**: Base filename (without version) tracked in VERSION_MANIFEST

---

### Ephemeral Files
**Format**: `{Name}_{Date or Iteration}_{Descriptor}.{ext}`

**Examples**:
- `LMNT_Customer_Voice_A_Grade.xlsx` (final iteration, clear descriptor)
- `LMNT_Customer_Voice_10min_Pilot.xlsx` (time-boxed test)
- `IonWave_Market_Landscape_Assessment_v0_1.xlsx` (v0.x indicates pre-release)
- `Competitive_Intelligence_Playbook_v0_1.xlsx` (process artifact)

**Note**: NOT tracked in VERSION_MANIFEST, but should have metadata header

---

### Tracking Documents (Not Versioned)
**Format**: `{Name}.md` (no version suffix)

**Examples**:
- `Decision_Log.md`
- `Discrepancy_Register.md`
- `AB_Test_Log.md`
- `Open_Questions.md`

**Note**: Never versioned, append-only or update-in-place

---

## METADATA PLACEMENT

### For Markdown Files (.md)
**Place at top of file**, immediately after title:

```markdown
# DOCUMENT TITLE
**Version**: v1.0.0
**Author**: Claude
**Date Created**: 2026-02-03
**Purpose**: ...
**Status**: Draft

---

[Content begins here]
```

---

### For Excel Files (.xlsx)
**Option 1 - File Properties** (preferred):
- Right-click file → Properties → Details
- Enter: Title, Subject, Comments, Authors
- Comments field can hold version, purpose, status

**Option 2 - Metadata Sheet**:
- Create first sheet named "METADATA"
- Include all metadata fields
- Format as readable table

**Option 3 - Header in Primary Sheet**:
- First 5-10 rows of primary sheet contain metadata
- Clearly separated from content (blank row, border)

**Recommendation**: Use Option 2 (Metadata Sheet) for versioned operational files like Trade files.

---

### For Process Artifacts (uploaded ephemeral files)
**Add README.txt** in same directory or include metadata in accompanying documentation:

```
Competitive_Intelligence_Playbook_v0_1.xlsx
Author: Claude, Danilo
Date: 2026-01-31
Purpose: Quality standards for 21 competitive intelligence output types
Status: Ephemeral - Integrated into 02_Market_Intelligence_v1.0.1.xlsx (CI Quality Standards sheet)
Retention: Archive for reference, not actively maintained
```

---

## CHANGE LOG FORMAT

### Recommended Format
```markdown
**Change Log**:
- v1.0.1 (2026-02-03): Added CI Quality Standards, Current State Assessment, Intelligence Gaps sheets; updated Competitive Intel with graded LMNT data
- v1.0.0 (2026-02-03): Initial version from extraction and organization
```

### For Major Changes
```markdown
**Change Log**:
- v2.0.0 (2026-02-10): BREAKING - Restructured dependency mapping, added cross-sheet validation, renamed 5 sheets for clarity
- v1.1.0 (2026-02-05): Added Porter's Five Forces analysis, enhanced Intelligence Gaps with scenario planning
- v1.0.1 (2026-02-03): Added 3 new sheets, updated competitive intel
- v1.0.0 (2026-02-03): Initial version
```

---

## RELATED FILES DOCUMENTATION

### Purpose
Track dependencies so changes cascade properly.

### Format
```markdown
**Related Files**: 
- 03A_Customer_Research_ICP.xlsx (provides personas for analysis)
- LMNT_Customer_Voice_A_Grade.xlsx (source data for customer insights)
- Competitive_Intelligence_Playbook_v0_1.xlsx (quality standards reference)
```

### Bidirectional Linking
If File A depends on File B, then:
- File A lists File B in "Related Files"
- File B *should* list File A in "Used By" or "Dependents" (optional, for complex systems)

---

## IMPLEMENTATION CHECKLIST

### When Creating New Document

- [ ] Choose document class (Versioned / Methodology / Ephemeral / Tracking)
- [ ] Add all required metadata fields at top of document
- [ ] Add conditional fields if applicable (AI model, framework type, etc.)
- [ ] Use proper filename convention
- [ ] If versioned: Add to VERSION_MANIFEST.md
- [ ] If ephemeral: Document retention/lifecycle plan
- [ ] Include change log if v1.0.1+ (not needed for v1.0.0)

### When Updating Existing Document

- [ ] Increment version number appropriately
- [ ] Update "Date Modified" field
- [ ] Add change log entry describing what changed
- [ ] Update VERSION_MANIFEST.md with new version
- [ ] If breaking changes: Flag explicitly in metadata
- [ ] If dependencies changed: Update "Related Files"

### When Deprecating Document

- [ ] Change Status to "Deprecated"
- [ ] Add "Superseded By: [new file]" to metadata
- [ ] Update VERSION_MANIFEST.md (or remove if truly obsolete)
- [ ] Optionally: Move to archive directory

---

## SPECIAL CASES

### Collaborative Documents with Mixed Authorship
```markdown
**Author**: Caio (strategy, structure), Danilo (market research), Claude (framework application, synthesis)
**AI Model**: claude-sonnet-4.5-20250929 (Porter's Five Forces analysis, competitive intel sections)
**Human Validation**: Reviewed by Caio (approved 2026-02-03)
```

### Documents Generated by Multiple AI Iterations
```markdown
**AI Model**: claude-sonnet-4.5-20250929 (v1.0.0-v1.0.5), claude-opus-4-5-20251101 (v1.1.0+)
**Change Log**:
- v1.1.0 (2026-02-10): Upgraded to Opus for enhanced strategic analysis
- v1.0.5 (2026-02-08): Refinements with Sonnet
```

### Legacy Documents Without Metadata
Add metadata retroactively with note:
```markdown
**Version**: v1.0.0 (retroactive - originally created without version)
**Author**: Unknown (legacy document)
**Date Created**: Unknown (estimated 2025-Q4 based on content references)
**Date Modified**: 2026-02-03 (metadata added by Claude)
**Purpose**: [describe based on content analysis]
**Status**: Final (grandfathered)
```

---

## METADATA TEMPLATE

### Copy-Paste Template for New Documents

```markdown
# [DOCUMENT TITLE]
**Version**: v1.0.0
**Author**: [Name(s)]
**Date Created**: YYYY-MM-DD
**Date Modified**: YYYY-MM-DD (if different from created)
**AI Model**: [model-identifier] (if applicable)
**Purpose**: [One-sentence description]
**Status**: [Draft | Review | Final | Deprecated | Ephemeral | Live Tracking]
**Related Files**: [List dependencies]
**Change Log**: v1.0.0 - Initial version

---

[Content begins here]
```

---

## EXAMPLES BY DOCUMENT CLASS

### Example 1: Versioned Trade File

```markdown
# 02_MARKET_INTELLIGENCE
**Version**: v1.0.1
**Author**: Caio, Danilo, Claude (collaborative)
**Date Created**: 2026-02-03
**Date Modified**: 2026-02-03
**AI Model**: claude-sonnet-4.5-20250929 (CI Quality Standards, Intelligence Gaps, graded LMNT data)
**Purpose**: Competitive intelligence, market data, and strategic frameworks for IonWave
**Status**: Final
**Related Files**: 
- 03A_Customer_Research_ICP.xlsx (persona inputs)
- 03B_Customer_Research_VOC.xlsx (customer voice data)
- Competitive_Intelligence_Playbook_v0_1.xlsx (quality standards)
**Change Log**:
- v1.0.1 (2026-02-03): Added CI Quality Standards sheet, Current State Assessment sheet, Intelligence Gaps Analysis sheet; updated Competitive Intel with graded LMNT data (7 metrics with B+ to C grades); corrected v8 pricing error ($40.50 → $48.40)
- v1.0.0 (2026-02-03): Initial version from extraction and organization
```

---

### Example 2: Methodology Document

```markdown
# PORTER'S FIVE FORCES - EXECUTION METHODOLOGY
**Version**: v1.0.0
**Author**: Claude
**Date Created**: 2026-02-03
**AI Model**: claude-sonnet-4.5-20250929
**Purpose**: Reusable framework for category-level competitive analysis using Porter's Five Forces
**Status**: Draft - Awaiting Approval
**Framework Type**: Strategic Analysis
**Target Grade**: B-grade (2 hours Track A work)
**Time Budget**: 2 hours (B-grade), 4 hours (A-grade)
**Validated Against**: IonWave / Electrolyte Category (pending execution)
**Related Files**: 
- Competitive_Intelligence_Playbook_v0_1.xlsx (standards source)
- 02_Market_Intelligence.xlsx (output destination)
- 03A_Customer_Research_ICP.xlsx (persona context)
**Change Log**: v1.0.0 - Initial framework documentation
```

---

### Example 3: Ephemeral Process Document

```markdown
# LMNT INVESTOR LENS v9
**Author**: Danilo, Claude
**Date Created**: 2026-01-31
**AI Model**: claude-sonnet-4.5-20250929
**Purpose**: Competitive intelligence iteration on LMNT, upgrading from v8 to establish A-grade standards
**Status**: Ephemeral - Superseded By Integration
**Lifecycle**: Single-Use (integrated into 02_Market_Intelligence_v1.0.1.xlsx on 2026-02-03)
**Retention**: Archive for historical reference, content now in Trade file
**Process Stage**: Historical (work complete, content integrated)
**Related Files**: 
- 02_Market_Intelligence_v1.0.1.xlsx (final integrated version)
- LMNT_Customer_Voice_A_Grade.xlsx (supporting customer research)
- v8_vs_AGrade_Comparison.xlsx (quality assessment)
```

---

### Example 4: Tracking Document (Not Versioned)

```markdown
# DECISION LOG
**Author**: Collaborative - Ongoing
**Date Created**: 2026-02-03
**Purpose**: Record all strategic decisions with rationale, context, and reversibility assessment
**Status**: Live Tracking (Not Versioned)
**Update Frequency**: As decisions are made
**Format**: Append-only, chronological
**Related Files**: 
- Open_Questions.md (questions that led to decisions)
- VERSION_MANIFEST.md (tracks implementation)
```

---

## QUALITY SELF-CHECK

Before finalizing any document, verify metadata completeness:

- [ ] All required fields present for document class
- [ ] Version number follows convention (if versioned)
- [ ] Author attribution is accurate and clear
- [ ] AI model documented (if AI-generated)
- [ ] Purpose is clear and concise (one sentence)
- [ ] Status reflects current state accurately
- [ ] Related files listed (if dependencies exist)
- [ ] Change log updated (if v1.0.1+)
- [ ] Filename matches version (if versioned)
- [ ] VERSION_MANIFEST updated (if versioned)

---

## NEXT STEPS

1. **Approve this standard** (Caio decision)
2. **Apply metadata to Porter's Five Forces Methodology** (make it v1.0.0)
3. **Retroactively add metadata to key documents** (prioritize reusable frameworks)
4. **Update VERSION_MANIFEST** to include metadata fields
5. **Create metadata templates** for common document types

---

**This document will be versioned once approved.**

