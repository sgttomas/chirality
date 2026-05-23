# Semantic Lensing Register: DEL-02-03 Working Root File Tree and Scope Scan UI

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py returned VALID
**Warnings:** PRD REF-006 hash mismatch remains a source warning; package-folder label mismatch remains HumanRuling=TBD.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_CONTEXT.md#context-del-02-03-working-root-file-tree-and-scope-scan-ui
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_STATUS.md#status-del-02-03
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_SEMANTIC.md#semantic-lens-del-02-03-working-root-file-tree-and-scope-scan-ui
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Datasheet.md#datasheet-del-02-03-working-root-file-tree-and-scope-scan-ui
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Specification.md#specification-del-02-03-working-root-file-tree-and-scope-scan-ui
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Guidance.md#guidance-del-02-03-working-root-file-tree-and-scope-scan-ui
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Procedure.md#procedure-del-02-03-working-root-file-tree-and-scope-scan-ui
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_REFERENCES.md#references-del-02-03-working-root-file-tree-and-scope-scan-ui (metadata only; external paths not followed)

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 7
- By document:
  - Datasheet: 0
  - Specification: 3
  - Guidance: 2
  - Procedure: 1
  - Multi: 1
  - NA: 0
- By matrix:
  - A: 1
  - B: 1
  - C: 0
  - F: 1
  - D: 0
  - X: 3
  - E: 1
- By type:
  - Conflict: 2
  - VerificationGap: 2
  - MissingSlot: 1
  - WeakStatement: 0
  - RationaleGap: 0
  - Normalization: 0
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 2
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Lens check for normative/guiding: prescriptive direction is represented by the scanned docs without a separate enrichment row. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | Lens check for normative/applying: mandatory practice is represented by the scanned docs without a separate enrichment row. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Lens check for normative/judging: compliance determination is represented by the scanned docs without a separate enrichment row. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Registers 1 item(s) where regulatory audit exposes an unresolved enrichment input. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Lens check for operative/guiding: procedural direction is represented by the scanned docs without a separate enrichment row. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Lens check for operative/applying: practical execution is represented by the scanned docs without a separate enrichment row. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Lens check for operative/judging: performance assessment is represented by the scanned docs without a separate enrichment row. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Lens check for operative/reviewing: process audit is represented by the scanned docs without a separate enrichment row. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Lens check for evaluative/guiding: value orientation is represented by the scanned docs without a separate enrichment row. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Lens check for evaluative/applying: merit application is represented by the scanned docs without a separate enrichment row. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Lens check for evaluative/judging: worth determination is represented by the scanned docs without a separate enrichment row. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Lens check for evaluative/reviewing: quality appraisal is represented by the scanned docs without a separate enrichment row. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Guidance | NA | Human ruling needed for stale dispatch package-folder label versus scaffolded PKG-02 folder label. | The guidance conflict table records a dispatch path naming `PKG-02_Desktop_UI_and_Local_Experience` while the accessible scaffold and context use `PKG-02_Desktop_Shell_Navigation_and_Operator_State`. This affects auditability of path-based run records without changing stable IDs. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Guidance.md#guidance-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_CONTEXT.md#context-del-02-03-working-root-file-tree-and-scope-scan-ui | Guidance.md#conflict-table-for-human-ruling; _CONTEXT.md#identity | Dispatch brief#ScopePath; _CONTEXT.md#Identity | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | Lens check for data/necessity: essential fact is represented by the scanned docs without a separate enrichment row. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Lens check for data/sufficiency: adequate evidence is represented by the scanned docs without a separate enrichment row. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | Lens check for data/completeness: comprehensive record is represented by the scanned docs without a separate enrichment row. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | Lens check for data/consistency: reliable measurement is represented by the scanned docs without a separate enrichment row. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Lens check for information/necessity: essential signal is represented by the scanned docs without a separate enrichment row. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | Lens check for information/sufficiency: adequate context is represented by the scanned docs without a separate enrichment row. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | Lens check for information/completeness: comprehensive account is represented by the scanned docs without a separate enrichment row. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | Lens check for information/consistency: coherent message is represented by the scanned docs without a separate enrichment row. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Lens check for knowledge/necessity: fundamental understanding is represented by the scanned docs without a separate enrichment row. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 1 | HAS_ITEMS | Registers 1 item(s) where competent expertise exposes an unresolved enrichment input. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Lens check for knowledge/completeness: thorough mastery is represented by the scanned docs without a separate enrichment row. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Lens check for knowledge/consistency: coherent understanding is represented by the scanned docs without a separate enrichment row. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Lens check for wisdom/necessity: essential discernment is represented by the scanned docs without a separate enrichment row. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Lens check for wisdom/sufficiency: adequate judgment is represented by the scanned docs without a separate enrichment row. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Lens check for wisdom/completeness: holistic insight is represented by the scanned docs without a separate enrichment row. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Lens check for wisdom/consistency: principled reasoning is represented by the scanned docs without a separate enrichment row. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[knowledge]:[sufficiency] | TBD_Question | Multi | TBD | Confirm exact UI component/module paths and API response field names before implementation acceptance. | Specification and Guidance identify component paths, truncation/inaccessible response field names, and exact UI copy as TBD. Those details are needed before the implementation knowledge base is sufficient for acceptance. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Specification.md#specification-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Guidance.md#guidance-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Procedure.md#procedure-del-02-03-working-root-file-tree-and-scope-scan-ui | Specification.md#documentation; Guidance.md#human-ruling-needed; Procedure.md#steps |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding evidence frame | 0 | NO_ITEMS | Lens check for normative/necessity: binding evidence frame is represented by the scanned docs without a separate enrichment row. |
| C:[normative]:[sufficiency] | normative | sufficiency | warranted control basis | 0 | NO_ITEMS | Lens check for normative/sufficiency: warranted control basis is represented by the scanned docs without a separate enrichment row. |
| C:[normative]:[completeness] | normative | completeness | complete rule account | 0 | NO_ITEMS | Lens check for normative/completeness: complete rule account is represented by the scanned docs without a separate enrichment row. |
| C:[normative]:[consistency] | normative | consistency | stable compliance signal | 0 | NO_ITEMS | Lens check for normative/consistency: stable compliance signal is represented by the scanned docs without a separate enrichment row. |
| C:[operative]:[necessity] | operative | necessity | executable proof basis | 0 | NO_ITEMS | Lens check for operative/necessity: executable proof basis is represented by the scanned docs without a separate enrichment row. |
| C:[operative]:[sufficiency] | operative | sufficiency | workable context frame | 0 | NO_ITEMS | Lens check for operative/sufficiency: workable context frame is represented by the scanned docs without a separate enrichment row. |
| C:[operative]:[completeness] | operative | completeness | complete action record | 0 | NO_ITEMS | Lens check for operative/completeness: complete action record is represented by the scanned docs without a separate enrichment row. |
| C:[operative]:[consistency] | operative | consistency | stable process signal | 0 | NO_ITEMS | Lens check for operative/consistency: stable process signal is represented by the scanned docs without a separate enrichment row. |
| C:[evaluative]:[necessity] | evaluative | necessity | value proof basis | 0 | NO_ITEMS | Lens check for evaluative/necessity: value proof basis is represented by the scanned docs without a separate enrichment row. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | warranted merit context | 0 | NO_ITEMS | Lens check for evaluative/sufficiency: warranted merit context is represented by the scanned docs without a separate enrichment row. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete appraisal account | 0 | NO_ITEMS | Lens check for evaluative/completeness: complete appraisal account is represented by the scanned docs without a separate enrichment row. |
| C:[evaluative]:[consistency] | evaluative | consistency | stable quality signal | 0 | NO_ITEMS | Lens check for evaluative/consistency: stable quality signal is represented by the scanned docs without a separate enrichment row. |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | binding readiness warrant | 0 | NO_ITEMS | Lens check for normative/necessity: binding readiness warrant is represented by the scanned docs without a separate enrichment row. |
| F:[normative]:[sufficiency] | normative | sufficiency | controlled adequacy basis | 0 | NO_ITEMS | Lens check for normative/sufficiency: controlled adequacy basis is represented by the scanned docs without a separate enrichment row. |
| F:[normative]:[completeness] | normative | completeness | governed coverage frame | 0 | NO_ITEMS | Lens check for normative/completeness: governed coverage frame is represented by the scanned docs without a separate enrichment row. |
| F:[normative]:[consistency] | normative | consistency | stable conformance signal | 0 | NO_ITEMS | Lens check for normative/consistency: stable conformance signal is represented by the scanned docs without a separate enrichment row. |
| F:[operative]:[necessity] | operative | necessity | executable readiness warrant | 0 | NO_ITEMS | Lens check for operative/necessity: executable readiness warrant is represented by the scanned docs without a separate enrichment row. |
| F:[operative]:[sufficiency] | operative | sufficiency | workable adequacy basis | 0 | NO_ITEMS | Lens check for operative/sufficiency: workable adequacy basis is represented by the scanned docs without a separate enrichment row. |
| F:[operative]:[completeness] | operative | completeness | bounded coverage frame | 0 | NO_ITEMS | Lens check for operative/completeness: bounded coverage frame is represented by the scanned docs without a separate enrichment row. |
| F:[operative]:[consistency] | operative | consistency | stable workflow signal | 1 | HAS_ITEMS | Registers 1 item(s) where stable workflow signal exposes an unresolved enrichment input. |
| F:[evaluative]:[necessity] | evaluative | necessity | value readiness warrant | 0 | NO_ITEMS | Lens check for evaluative/necessity: value readiness warrant is represented by the scanned docs without a separate enrichment row. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | merit adequacy basis | 0 | NO_ITEMS | Lens check for evaluative/sufficiency: merit adequacy basis is represented by the scanned docs without a separate enrichment row. |
| F:[evaluative]:[completeness] | evaluative | completeness | appraisal coverage frame | 0 | NO_ITEMS | Lens check for evaluative/completeness: appraisal coverage frame is represented by the scanned docs without a separate enrichment row. |
| F:[evaluative]:[consistency] | evaluative | consistency | stable quality signal | 0 | NO_ITEMS | Lens check for evaluative/consistency: stable quality signal is represented by the scanned docs without a separate enrichment row. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[consistency] | VerificationGap | Procedure | Procedure | Add or link acceptance evidence for selector, invalid-root feedback, bounded tree behavior, scope reset, and deliverable routing. | The procedure lists verification checks and records expected evidence, but no test artifact or acceptance record is present in the deliverable folder. Later enrichment should preserve this as required evidence rather than imply it already exists. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Procedure.md#procedure-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Specification.md#specification-del-02-03-working-root-file-tree-and-scope-scan-ui | Procedure.md#verification; Specification.md#verification |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | policy closure frame | 0 | NO_ITEMS | Lens check for normative/guiding: policy closure frame is represented by the scanned docs without a separate enrichment row. |
| D:[normative]:[applying] | normative | applying | mandatory closure method | 0 | NO_ITEMS | Lens check for normative/applying: mandatory closure method is represented by the scanned docs without a separate enrichment row. |
| D:[normative]:[judging] | normative | judging | conformance verdict basis | 0 | NO_ITEMS | Lens check for normative/judging: conformance verdict basis is represented by the scanned docs without a separate enrichment row. |
| D:[normative]:[reviewing] | normative | reviewing | audit closure standard | 0 | NO_ITEMS | Lens check for normative/reviewing: audit closure standard is represented by the scanned docs without a separate enrichment row. |
| D:[operative]:[guiding] | operative | guiding | procedure closure frame | 0 | NO_ITEMS | Lens check for operative/guiding: procedure closure frame is represented by the scanned docs without a separate enrichment row. |
| D:[operative]:[applying] | operative | applying | execution closure method | 0 | NO_ITEMS | Lens check for operative/applying: execution closure method is represented by the scanned docs without a separate enrichment row. |
| D:[operative]:[judging] | operative | judging | performance verdict basis | 0 | NO_ITEMS | Lens check for operative/judging: performance verdict basis is represented by the scanned docs without a separate enrichment row. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance standard | 0 | NO_ITEMS | Lens check for operative/reviewing: process assurance standard is represented by the scanned docs without a separate enrichment row. |
| D:[evaluative]:[guiding] | evaluative | guiding | value closure frame | 0 | NO_ITEMS | Lens check for evaluative/guiding: value closure frame is represented by the scanned docs without a separate enrichment row. |
| D:[evaluative]:[applying] | evaluative | applying | merit closure method | 0 | NO_ITEMS | Lens check for evaluative/applying: merit closure method is represented by the scanned docs without a separate enrichment row. |
| D:[evaluative]:[judging] | evaluative | judging | worth verdict basis | 0 | NO_ITEMS | Lens check for evaluative/judging: worth verdict basis is represented by the scanned docs without a separate enrichment row. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality assurance standard | 0 | NO_ITEMS | Lens check for evaluative/reviewing: quality assurance standard is represented by the scanned docs without a separate enrichment row. |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | root validity warrant | 0 | NO_ITEMS | Lens check for guiding/necessity: root validity warrant is represented by the scanned docs without a separate enrichment row. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | selector adequacy proof | 0 | NO_ITEMS | Lens check for guiding/sufficiency: selector adequacy proof is represented by the scanned docs without a separate enrichment row. |
| X:[guiding]:[completeness] | guiding | completeness | tree coverage account | 0 | NO_ITEMS | Lens check for guiding/completeness: tree coverage account is represented by the scanned docs without a separate enrichment row. |
| X:[guiding]:[consistency] | guiding | consistency | route coherence signal | 0 | NO_ITEMS | Lens check for guiding/consistency: route coherence signal is represented by the scanned docs without a separate enrichment row. |
| X:[applying]:[necessity] | applying | necessity | action readiness proof | 0 | NO_ITEMS | Lens check for applying/necessity: action readiness proof is represented by the scanned docs without a separate enrichment row. |
| X:[applying]:[sufficiency] | applying | sufficiency | usable context basis | 0 | NO_ITEMS | Lens check for applying/sufficiency: usable context basis is represented by the scanned docs without a separate enrichment row. |
| X:[applying]:[completeness] | applying | completeness | bounded scan record | 1 | HAS_ITEMS | Registers 1 item(s) where bounded scan record exposes an unresolved enrichment input. |
| X:[applying]:[consistency] | applying | consistency | reset coherence signal | 0 | NO_ITEMS | Lens check for applying/consistency: reset coherence signal is represented by the scanned docs without a separate enrichment row. |
| X:[judging]:[necessity] | judging | necessity | failure evidence basis | 0 | NO_ITEMS | Lens check for judging/necessity: failure evidence basis is represented by the scanned docs without a separate enrichment row. |
| X:[judging]:[sufficiency] | judging | sufficiency | typed feedback warrant | 1 | HAS_ITEMS | Registers 1 item(s) where typed feedback warrant exposes an unresolved enrichment input. |
| X:[judging]:[completeness] | judging | completeness | snapshot coverage account | 0 | NO_ITEMS | Lens check for judging/completeness: snapshot coverage account is represented by the scanned docs without a separate enrichment row. |
| X:[judging]:[consistency] | judging | consistency | identity coherence signal | 0 | NO_ITEMS | Lens check for judging/consistency: identity coherence signal is represented by the scanned docs without a separate enrichment row. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit evidence frame | 0 | NO_ITEMS | Lens check for reviewing/necessity: audit evidence frame is represented by the scanned docs without a separate enrichment row. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | boundary assurance basis | 0 | NO_ITEMS | Lens check for reviewing/sufficiency: boundary assurance basis is represented by the scanned docs without a separate enrichment row. |
| X:[reviewing]:[completeness] | reviewing | completeness | omission coverage record | 0 | NO_ITEMS | Lens check for reviewing/completeness: omission coverage record is represented by the scanned docs without a separate enrichment row. |
| X:[reviewing]:[consistency] | reviewing | consistency | source warning signal | 1 | HAS_ITEMS | Registers 1 item(s) where source warning signal exposes an unresolved enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[applying]:[completeness] | TBD_Question | Specification | Specification | Confirm API response shapes for skipped, inaccessible, and truncated tree/scope scan results. | The file-tree and scope-scan behavior depends on bounded API result details, while Specification and Procedure mark the exact response shape details as TBD. This is needed to complete the bounded scan record lens. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Specification.md#specification-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Procedure.md#procedure-del-02-03-working-root-file-tree-and-scope-scan-ui | Specification.md#documentation; Procedure.md#prerequisites |  | PROPOSAL | TBD |
| X-002 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Preserve typed validation and scan error fields in UI tests or acceptance notes. | The requirements call for typed-error preservation, but exact error copy and field-level display expectations remain TBD. A verification note should bind the acceptance check to type/status/message/details where available. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Specification.md#specification-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Datasheet.md#datasheet-del-02-03-working-root-file-tree-and-scope-scan-ui | Specification.md#requirements; Datasheet.md#construction |  | PROPOSAL | TBD |
| X-003 | X:[reviewing]:[consistency] | Conflict | Guidance | NA | PRD hash mismatch remains a source warning and requires human ruling before closure. | Datasheet, Guidance, Procedure, and _REFERENCES all record that PRD-derived requirements are usable for this run only as warned source material. The register should keep the source warning visible for later closure rather than normalizing it away. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_REFERENCES.md#references-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Guidance.md#guidance-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Procedure.md#procedure-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Datasheet.md#datasheet-del-02-03-working-root-file-tree-and-scope-scan-ui | _REFERENCES.md#authoritative-source-corpus; Guidance.md#conflict-table-for-human-ruling; Procedure.md#prerequisites; Datasheet.md#conditions | _REFERENCES.md#REF-006; dispatch instruction#source-warning | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual routing warrant | 0 | NO_ITEMS | Lens check for guiding/data: factual routing warrant is represented by the scanned docs without a separate enrichment row. |
| E:[guiding]:[information] | guiding | information | contextual selector frame | 0 | NO_ITEMS | Lens check for guiding/information: contextual selector frame is represented by the scanned docs without a separate enrichment row. |
| E:[guiding]:[knowledge] | guiding | knowledge | operational understanding map | 0 | NO_ITEMS | Lens check for guiding/knowledge: operational understanding map is represented by the scanned docs without a separate enrichment row. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled boundary judgment | 0 | NO_ITEMS | Lens check for guiding/wisdom: principled boundary judgment is represented by the scanned docs without a separate enrichment row. |
| E:[applying]:[data] | applying | data | actionable root proof | 0 | NO_ITEMS | Lens check for applying/data: actionable root proof is represented by the scanned docs without a separate enrichment row. |
| E:[applying]:[information] | applying | information | usable scan context | 0 | NO_ITEMS | Lens check for applying/information: usable scan context is represented by the scanned docs without a separate enrichment row. |
| E:[applying]:[knowledge] | applying | knowledge | implementation readiness map | 0 | NO_ITEMS | Lens check for applying/knowledge: implementation readiness map is represented by the scanned docs without a separate enrichment row. |
| E:[applying]:[wisdom] | applying | wisdom | prudent reset judgment | 0 | NO_ITEMS | Lens check for applying/wisdom: prudent reset judgment is represented by the scanned docs without a separate enrichment row. |
| E:[judging]:[data] | judging | data | error fact basis | 0 | NO_ITEMS | Lens check for judging/data: error fact basis is represented by the scanned docs without a separate enrichment row. |
| E:[judging]:[information] | judging | information | typed message context | 1 | HAS_ITEMS | Registers 1 item(s) where typed message context exposes an unresolved enrichment input. |
| E:[judging]:[knowledge] | judging | knowledge | acceptance understanding map | 0 | NO_ITEMS | Lens check for judging/knowledge: acceptance understanding map is represented by the scanned docs without a separate enrichment row. |
| E:[judging]:[wisdom] | judging | wisdom | principled verdict judgment | 0 | NO_ITEMS | Lens check for judging/wisdom: principled verdict judgment is represented by the scanned docs without a separate enrichment row. |
| E:[reviewing]:[data] | reviewing | data | audit fact basis | 0 | NO_ITEMS | Lens check for reviewing/data: audit fact basis is represented by the scanned docs without a separate enrichment row. |
| E:[reviewing]:[information] | reviewing | information | source warning context | 0 | NO_ITEMS | Lens check for reviewing/information: source warning context is represented by the scanned docs without a separate enrichment row. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | coverage understanding map | 0 | NO_ITEMS | Lens check for reviewing/knowledge: coverage understanding map is represented by the scanned docs without a separate enrichment row. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | closure judgment frame | 0 | NO_ITEMS | Lens check for reviewing/wisdom: closure judgment frame is represented by the scanned docs without a separate enrichment row. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[judging]:[information] | MissingSlot | Specification | Specification | Define exact status/dependency summary widget fields or mark unsupported fields as deferred. | The UI must consume status and dependency snapshots read-only where applicable, while Specification leaves exact widget fields TBD and dependency extraction deferred. This missing slot affects the typed message context used for summary widgets. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Specification.md#specification-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Guidance.md#guidance-del-02-03-working-root-file-tree-and-scope-scan-ui; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/Procedure.md#procedure-del-02-03-working-root-file-tree-and-scope-scan-ui | Specification.md#documentation; Guidance.md#considerations; Procedure.md#steps |  | PROPOSAL | TBD |

