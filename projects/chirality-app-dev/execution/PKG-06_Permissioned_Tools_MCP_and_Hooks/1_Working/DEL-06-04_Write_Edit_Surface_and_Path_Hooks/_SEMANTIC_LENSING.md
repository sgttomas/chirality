# Semantic Lensing Register: DEL-06-04 Write/Edit Surface and Path Hooks

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py returned VALID
**Warnings:** REF-006 PRD source remains HASH_MISMATCH in `_REFERENCES.md`; `MEMORY.md` is not present.

**Inputs Read:**
- _CONTEXT.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_CONTEXT.md#Context-DEL-06-04-Write-Edit-Surface-and-Path-Hooks
- _STATUS.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_STATUS.md#Status-DEL-06-04
- _SEMANTIC.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_SEMANTIC.md#Semantic-Lens-DEL-06-04-Write-Edit-Surface-and-Path-Hooks
- Datasheet.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/Datasheet.md#Datasheet-DEL-06-04-Write-Edit-Surface-and-Path-Hooks
- Specification.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/Specification.md#Specification-DEL-06-04-Write-Edit-Surface-and-Path-Hooks
- Guidance.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/Guidance.md#Guidance-DEL-06-04-Write-Edit-Surface-and-Path-Hooks
- Procedure.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/Procedure.md#Procedure-DEL-06-04-Write-Edit-Surface-and-Path-Hooks
- _REFERENCES.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_REFERENCES.md#References-DEL-06-04-Write-Edit-Surface-and-Path-Hooks

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Current ADQ-11 Note (2026-06-21)

This generated 2026-05-20 lens is not regenerated here, but ADQ-11/D-APP-43 retires the active
source-state, exact-edit, and controlled-write atomicity findings for current review. REF-006
`docs/PRD.md` is `MATCH` under the D-APP-38 authority corpus v2; hook-side exact `Edit.old_string`
preconditions and same-directory atomic controlled writes are evidenced in the current assessment,
tests, and ADQ-11 evidence. Future Chirality MCP write-tool inventory remains out of scope unless a
new write-capable MCP surface is exposed.

## Summary

- Total warranted items: 8
- By document:
  - Datasheet: 0
  - Specification: 2
  - Guidance: 2
  - Procedure: 2
  - Multi: 2
  - NA: 0
- By matrix:
  - A: 1
  - B: 1
  - C: 1
  - F: 2
  - D: 1
  - X: 1
  - E: 1
- By type:
  - Conflict: 2
  - VerificationGap: 1
  - MissingSlot: 1
  - WeakStatement: 1
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 2
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | A:[normative]:[guiding] scan found the prescriptive direction role traceable in the scoped production documents without a separate enrichment input. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 1 | HAS_ITEMS | mandatory practice lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | A:[normative]:[judging] scan found the compliance determination role traceable in the scoped production documents without a separate enrichment input. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | A:[normative]:[reviewing] scan found the regulatory audit role traceable in the scoped production documents without a separate enrichment input. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | A:[operative]:[guiding] scan found the procedural direction role traceable in the scoped production documents without a separate enrichment input. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | A:[operative]:[applying] scan found the practical execution role traceable in the scoped production documents without a separate enrichment input. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | A:[operative]:[judging] scan found the performance assessment role traceable in the scoped production documents without a separate enrichment input. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | A:[operative]:[reviewing] scan found the process audit role traceable in the scoped production documents without a separate enrichment input. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | A:[evaluative]:[guiding] scan found the value orientation role traceable in the scoped production documents without a separate enrichment input. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | A:[evaluative]:[applying] scan found the merit application role traceable in the scoped production documents without a separate enrichment input. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | A:[evaluative]:[judging] scan found the worth determination role traceable in the scoped production documents without a separate enrichment input. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | A:[evaluative]:[reviewing] scan found the quality appraisal role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[applying] | Conflict | Multi | Guidance | Settle canonical containment-root vocabulary before implementation surfaces public names. | Guidance records a conflict between decomposition project-root wording and governance working-root wording, while Specification and Procedure currently bridge both terms. | Guidance.md; Specification.md; Procedure.md | Guidance.md#Conflict-Table-for-human-ruling; Specification.md#Scope; Procedure.md#Steps | Guidance.md#DEL-06-04-CONFLICT-001; Specification.md#Scope; Procedure.md#Steps | PROPOSAL | TBD |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | B:[data]:[necessity] scan found the essential fact role traceable in the scoped production documents without a separate enrichment input. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | B:[data]:[sufficiency] scan found the adequate evidence role traceable in the scoped production documents without a separate enrichment input. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | B:[data]:[completeness] scan found the comprehensive record role traceable in the scoped production documents without a separate enrichment input. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | B:[data]:[consistency] scan found the reliable measurement role traceable in the scoped production documents without a separate enrichment input. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | B:[information]:[necessity] scan found the essential signal role traceable in the scoped production documents without a separate enrichment input. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | B:[information]:[sufficiency] scan found the adequate context role traceable in the scoped production documents without a separate enrichment input. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | B:[information]:[completeness] scan found the comprehensive account role traceable in the scoped production documents without a separate enrichment input. |
| B:[information]:[consistency] | information | consistency | coherent message | 1 | HAS_ITEMS | coherent message lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | B:[knowledge]:[necessity] scan found the fundamental understanding role traceable in the scoped production documents without a separate enrichment input. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | B:[knowledge]:[sufficiency] scan found the competent expertise role traceable in the scoped production documents without a separate enrichment input. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | B:[knowledge]:[completeness] scan found the thorough mastery role traceable in the scoped production documents without a separate enrichment input. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | B:[knowledge]:[consistency] scan found the coherent understanding role traceable in the scoped production documents without a separate enrichment input. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | B:[wisdom]:[necessity] scan found the essential discernment role traceable in the scoped production documents without a separate enrichment input. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | B:[wisdom]:[sufficiency] scan found the adequate judgment role traceable in the scoped production documents without a separate enrichment input. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | B:[wisdom]:[completeness] scan found the holistic insight role traceable in the scoped production documents without a separate enrichment input. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | B:[wisdom]:[consistency] scan found the principled reasoning role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[information]:[consistency] | Conflict | Multi | Guidance | Retain REF-006 HASH_MISMATCH warning on PRD-derived controlled-write details until reference reconciliation occurs. | Datasheet, Specification, Guidance, and Procedure all use PRD Section 7.9 while _REFERENCES marks REF-006 as HASH_MISMATCH. | _REFERENCES.md; Datasheet.md; Specification.md; Guidance.md; Procedure.md | _REFERENCES.md#Authoritative-Source-Corpus; Datasheet.md#Conditions; Specification.md#Standards; Guidance.md#PRD-Hash-Warning; Procedure.md#Verification | _REFERENCES.md#REF-006; Guidance.md#DEL-06-04-CONFLICT-002 | PROPOSAL | TBD |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding authorization basis | 0 | NO_ITEMS | C:[normative]:[necessity] scan found the binding authorization basis role traceable in the scoped production documents without a separate enrichment input. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate control basis | 0 | NO_ITEMS | C:[normative]:[sufficiency] scan found the adequate control basis role traceable in the scoped production documents without a separate enrichment input. |
| C:[normative]:[completeness] | normative | completeness | complete governance record | 0 | NO_ITEMS | C:[normative]:[completeness] scan found the complete governance record role traceable in the scoped production documents without a separate enrichment input. |
| C:[normative]:[consistency] | normative | consistency | coherent enforcement rationale | 0 | NO_ITEMS | C:[normative]:[consistency] scan found the coherent enforcement rationale role traceable in the scoped production documents without a separate enrichment input. |
| C:[operative]:[necessity] | operative | necessity | actionable execution basis | 0 | NO_ITEMS | C:[operative]:[necessity] scan found the actionable execution basis role traceable in the scoped production documents without a separate enrichment input. |
| C:[operative]:[sufficiency] | operative | sufficiency | sufficient operating evidence | 1 | HAS_ITEMS | sufficient operating evidence lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| C:[operative]:[completeness] | operative | completeness | complete process account | 0 | NO_ITEMS | C:[operative]:[completeness] scan found the complete process account role traceable in the scoped production documents without a separate enrichment input. |
| C:[operative]:[consistency] | operative | consistency | coherent runtime behavior | 0 | NO_ITEMS | C:[operative]:[consistency] scan found the coherent runtime behavior role traceable in the scoped production documents without a separate enrichment input. |
| C:[evaluative]:[necessity] | evaluative | necessity | value-grounded criteria | 0 | NO_ITEMS | C:[evaluative]:[necessity] scan found the value-grounded criteria role traceable in the scoped production documents without a separate enrichment input. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate judgment basis | 0 | NO_ITEMS | C:[evaluative]:[sufficiency] scan found the adequate judgment basis role traceable in the scoped production documents without a separate enrichment input. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete appraisal frame | 0 | NO_ITEMS | C:[evaluative]:[completeness] scan found the complete appraisal frame role traceable in the scoped production documents without a separate enrichment input. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent quality rationale | 0 | NO_ITEMS | C:[evaluative]:[consistency] scan found the coherent quality rationale role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[sufficiency] | TBD_Question | Procedure | Procedure | Identify the exact edit matcher, stale-content behavior, and diff strategy owner. | Procedure Step 4 and Records leave the exact matching algorithm and validator paths as TBD, so execution sufficiency cannot be closed from current production text. | Procedure.md | Procedure.md#Steps; Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | mandatory control threshold | 0 | NO_ITEMS | F:[normative]:[necessity] scan found the mandatory control threshold role traceable in the scoped production documents without a separate enrichment input. |
| F:[normative]:[sufficiency] | normative | sufficiency | sufficient compliance evidence | 0 | NO_ITEMS | F:[normative]:[sufficiency] scan found the sufficient compliance evidence role traceable in the scoped production documents without a separate enrichment input. |
| F:[normative]:[completeness] | normative | completeness | complete policy trace | 0 | NO_ITEMS | F:[normative]:[completeness] scan found the complete policy trace role traceable in the scoped production documents without a separate enrichment input. |
| F:[normative]:[consistency] | normative | consistency | consistent authority proof | 0 | NO_ITEMS | F:[normative]:[consistency] scan found the consistent authority proof role traceable in the scoped production documents without a separate enrichment input. |
| F:[operative]:[necessity] | operative | necessity | required execution gate | 0 | NO_ITEMS | F:[operative]:[necessity] scan found the required execution gate role traceable in the scoped production documents without a separate enrichment input. |
| F:[operative]:[sufficiency] | operative | sufficiency | adequate mutation proof | 0 | NO_ITEMS | F:[operative]:[sufficiency] scan found the adequate mutation proof role traceable in the scoped production documents without a separate enrichment input. |
| F:[operative]:[completeness] | operative | completeness | complete action record | 1 | HAS_ITEMS | complete action record lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| F:[operative]:[consistency] | operative | consistency | consistent runtime guard | 0 | NO_ITEMS | F:[operative]:[consistency] scan found the consistent runtime guard role traceable in the scoped production documents without a separate enrichment input. |
| F:[evaluative]:[necessity] | evaluative | necessity | necessary review criteria | 0 | NO_ITEMS | F:[evaluative]:[necessity] scan found the necessary review criteria role traceable in the scoped production documents without a separate enrichment input. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | sufficient assurance basis | 1 | HAS_ITEMS | sufficient assurance basis lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete audit basis | 0 | NO_ITEMS | F:[evaluative]:[completeness] scan found the complete audit basis role traceable in the scoped production documents without a separate enrichment input. |
| F:[evaluative]:[consistency] | evaluative | consistency | consistent acceptance rationale | 0 | NO_ITEMS | F:[evaluative]:[consistency] scan found the consistent acceptance rationale role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[completeness] | MissingSlot | Specification | Specification | Name the write/edit hook module, path-policy helper, resolver integration, exact edit validator, and test evidence paths. | Specification Documentation lists all implementation evidence slots as TBD; the deliverable cannot later verify complete action records without these concrete paths. | Specification.md | Specification.md#Documentation |  | PROPOSAL | TBD |
| F-002 | F:[evaluative]:[sufficiency] | VerificationGap | Specification | Specification | Add an explicit verifier for PRD warning carry-forward and source-state reconciliation before accepting PRD-derived behavior. | Verification covers functional write/edit checks, but PRD hash-warning closure is represented as a residual note rather than a concrete acceptance check. | Specification.md; Procedure.md; _REFERENCES.md | Specification.md#Verification; Procedure.md#Verification; _REFERENCES.md#Authoritative-Source-Corpus |  | PROPOSAL | TBD |

## Matrix D — Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | authoritative control closure | 0 | NO_ITEMS | D:[normative]:[guiding] scan found the authoritative control closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[normative]:[applying] | normative | applying | enforceable practice closure | 0 | NO_ITEMS | D:[normative]:[applying] scan found the enforceable practice closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[normative]:[judging] | normative | judging | compliance closure judgment | 0 | NO_ITEMS | D:[normative]:[judging] scan found the compliance closure judgment role traceable in the scoped production documents without a separate enrichment input. |
| D:[normative]:[reviewing] | normative | reviewing | auditable governance closure | 0 | NO_ITEMS | D:[normative]:[reviewing] scan found the auditable governance closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[operative]:[guiding] | operative | guiding | procedural gate closure | 0 | NO_ITEMS | D:[operative]:[guiding] scan found the procedural gate closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[operative]:[applying] | operative | applying | controlled execution closure | 0 | NO_ITEMS | D:[operative]:[applying] scan found the controlled execution closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[operative]:[judging] | operative | judging | performance evidence closure | 0 | NO_ITEMS | D:[operative]:[judging] scan found the performance evidence closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance closure | 1 | HAS_ITEMS | process assurance closure lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| D:[evaluative]:[guiding] | evaluative | guiding | value alignment closure | 0 | NO_ITEMS | D:[evaluative]:[guiding] scan found the value alignment closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[evaluative]:[applying] | evaluative | applying | merit evidence closure | 0 | NO_ITEMS | D:[evaluative]:[applying] scan found the merit evidence closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[evaluative]:[judging] | evaluative | judging | worth judgment closure | 0 | NO_ITEMS | D:[evaluative]:[judging] scan found the worth judgment closure role traceable in the scoped production documents without a separate enrichment input. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality assurance closure | 0 | NO_ITEMS | D:[evaluative]:[reviewing] scan found the quality assurance closure role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[reviewing] | WeakStatement | Guidance | Guidance | Clarify where post-failure write/edit evidence ends and DEL-06-06 hook lifecycle mirroring begins. | Guidance says post-failure evidence should be captured where runtime supports it, but may belong to DEL-06-06; the boundary needs a concrete handoff rule for process assurance. | Guidance.md; Specification.md | Guidance.md#Hook-Placement; Specification.md#Scope |  | PROPOSAL | TBD |

## Matrix X — Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | authorized fact boundary | 0 | NO_ITEMS | X:[guiding]:[necessity] scan found the authorized fact boundary role traceable in the scoped production documents without a separate enrichment input. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | sufficient direction proof | 0 | NO_ITEMS | X:[guiding]:[sufficiency] scan found the sufficient direction proof role traceable in the scoped production documents without a separate enrichment input. |
| X:[guiding]:[completeness] | guiding | completeness | complete control record | 0 | NO_ITEMS | X:[guiding]:[completeness] scan found the complete control record role traceable in the scoped production documents without a separate enrichment input. |
| X:[guiding]:[consistency] | guiding | consistency | consistent policy signal | 0 | NO_ITEMS | X:[guiding]:[consistency] scan found the consistent policy signal role traceable in the scoped production documents without a separate enrichment input. |
| X:[applying]:[necessity] | applying | necessity | required practice evidence | 1 | HAS_ITEMS | required practice evidence lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| X:[applying]:[sufficiency] | applying | sufficiency | adequate execution context | 0 | NO_ITEMS | X:[applying]:[sufficiency] scan found the adequate execution context role traceable in the scoped production documents without a separate enrichment input. |
| X:[applying]:[completeness] | applying | completeness | complete action account | 0 | NO_ITEMS | X:[applying]:[completeness] scan found the complete action account role traceable in the scoped production documents without a separate enrichment input. |
| X:[applying]:[consistency] | applying | consistency | consistent implementation message | 0 | NO_ITEMS | X:[applying]:[consistency] scan found the consistent implementation message role traceable in the scoped production documents without a separate enrichment input. |
| X:[judging]:[necessity] | judging | necessity | necessary compliance proof | 0 | NO_ITEMS | X:[judging]:[necessity] scan found the necessary compliance proof role traceable in the scoped production documents without a separate enrichment input. |
| X:[judging]:[sufficiency] | judging | sufficiency | sufficient assessment context | 0 | NO_ITEMS | X:[judging]:[sufficiency] scan found the sufficient assessment context role traceable in the scoped production documents without a separate enrichment input. |
| X:[judging]:[completeness] | judging | completeness | complete verification mastery | 0 | NO_ITEMS | X:[judging]:[completeness] scan found the complete verification mastery role traceable in the scoped production documents without a separate enrichment input. |
| X:[judging]:[consistency] | judging | consistency | consistent judgment logic | 0 | NO_ITEMS | X:[judging]:[consistency] scan found the consistent judgment logic role traceable in the scoped production documents without a separate enrichment input. |
| X:[reviewing]:[necessity] | reviewing | necessity | essential audit trace | 0 | NO_ITEMS | X:[reviewing]:[necessity] scan found the essential audit trace role traceable in the scoped production documents without a separate enrichment input. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | adequate review basis | 0 | NO_ITEMS | X:[reviewing]:[sufficiency] scan found the adequate review basis role traceable in the scoped production documents without a separate enrichment input. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete assurance insight | 0 | NO_ITEMS | X:[reviewing]:[completeness] scan found the complete assurance insight role traceable in the scoped production documents without a separate enrichment input. |
| X:[reviewing]:[consistency] | reviewing | consistency | consistent appraisal reasoning | 0 | NO_ITEMS | X:[reviewing]:[consistency] scan found the consistent appraisal reasoning role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[applying]:[necessity] | TBD_Question | Procedure | Procedure | Inventory current and future Chirality MCP write tools that must pass through equivalent gates. | Procedure Step 1 asks to identify SDK Write/Edit and any Chirality MCP write tools currently exposed, while records do not yet name the exact MCP write surface. | Procedure.md; Specification.md | Procedure.md#Steps; Procedure.md#Verification |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual boundary evidence | 0 | NO_ITEMS | E:[guiding]:[data] scan found the factual boundary evidence role traceable in the scoped production documents without a separate enrichment input. |
| E:[guiding]:[information] | guiding | information | contextual direction evidence | 0 | NO_ITEMS | E:[guiding]:[information] scan found the contextual direction evidence role traceable in the scoped production documents without a separate enrichment input. |
| E:[guiding]:[knowledge] | guiding | knowledge | mastered control rationale | 0 | NO_ITEMS | E:[guiding]:[knowledge] scan found the mastered control rationale role traceable in the scoped production documents without a separate enrichment input. |
| E:[guiding]:[wisdom] | guiding | wisdom | reasoned policy judgment | 0 | NO_ITEMS | E:[guiding]:[wisdom] scan found the reasoned policy judgment role traceable in the scoped production documents without a separate enrichment input. |
| E:[applying]:[data] | applying | data | execution fact proof | 0 | NO_ITEMS | E:[applying]:[data] scan found the execution fact proof role traceable in the scoped production documents without a separate enrichment input. |
| E:[applying]:[information] | applying | information | contextual practice basis | 0 | NO_ITEMS | E:[applying]:[information] scan found the contextual practice basis role traceable in the scoped production documents without a separate enrichment input. |
| E:[applying]:[knowledge] | applying | knowledge | mastered implementation basis | 0 | NO_ITEMS | E:[applying]:[knowledge] scan found the mastered implementation basis role traceable in the scoped production documents without a separate enrichment input. |
| E:[applying]:[wisdom] | applying | wisdom | reasoned action judgment | 0 | NO_ITEMS | E:[applying]:[wisdom] scan found the reasoned action judgment role traceable in the scoped production documents without a separate enrichment input. |
| E:[judging]:[data] | judging | data | compliance fact proof | 0 | NO_ITEMS | E:[judging]:[data] scan found the compliance fact proof role traceable in the scoped production documents without a separate enrichment input. |
| E:[judging]:[information] | judging | information | contextual assessment evidence | 0 | NO_ITEMS | E:[judging]:[information] scan found the contextual assessment evidence role traceable in the scoped production documents without a separate enrichment input. |
| E:[judging]:[knowledge] | judging | knowledge | mastered verification basis | 0 | NO_ITEMS | E:[judging]:[knowledge] scan found the mastered verification basis role traceable in the scoped production documents without a separate enrichment input. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned acceptance judgment | 0 | NO_ITEMS | E:[judging]:[wisdom] scan found the reasoned acceptance judgment role traceable in the scoped production documents without a separate enrichment input. |
| E:[reviewing]:[data] | reviewing | data | audit fact trace | 0 | NO_ITEMS | E:[reviewing]:[data] scan found the audit fact trace role traceable in the scoped production documents without a separate enrichment input. |
| E:[reviewing]:[information] | reviewing | information | contextual review proof | 0 | NO_ITEMS | E:[reviewing]:[information] scan found the contextual review proof role traceable in the scoped production documents without a separate enrichment input. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastered assurance record | 1 | HAS_ITEMS | mastered assurance record lens surfaces 1 warranted production-document item(s) tied to this semantic role. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | reasoned appraisal basis | 0 | NO_ITEMS | E:[reviewing]:[wisdom] scan found the reasoned appraisal basis role traceable in the scoped production documents without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[knowledge] | RationaleGap | Guidance | Guidance | Document the rationale and selected conditions for atomic write/edit behavior once implementation design chooses the strategy. | Guidance frames atomic mutation as practical rather than absolute and Procedure leaves evidence format TBD; the assurance record lacks the implementation rationale that review will need. | Guidance.md; Procedure.md; Datasheet.md | Guidance.md#Trade-offs; Procedure.md#Records; Datasheet.md#Construction |  | PROPOSAL | TBD |
