# Semantic Lensing Register: DEL-01-02 Reliance Boundary Register

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — validate_lens_register.py returned VALID
**Warnings:** REF-006 docs/PRD.md hash mismatch preserved as source-state warning; exact implementation paths and some validation IDs remain TBD by production-document design.

**Inputs Read:**
- _CONTEXT.md — _CONTEXT.md#identity
- _STATUS.md — _STATUS.md#history
- _SEMANTIC.md — _SEMANTIC.md#semantic-lens-del-01-02-reliance-boundary-register
- Datasheet.md — Datasheet.md#boundary-taxonomy
- Specification.md — Specification.md#requirements
- Guidance.md — Guidance.md#principles
- Procedure.md — Procedure.md#steps
- _REFERENCES.md — _REFERENCES.md#authoritative-source-corpus; metadata only, external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 21
- By document:
  - Datasheet: 2
  - Specification: 4
  - Guidance: 4
  - Procedure: 3
  - Multi: 8
  - NA: 0
- By matrix:
  - A: 4
  - B: 2
  - C: 2
  - F: 3
  - D: 3
  - X: 3
  - E: 4
- By type:
  - Conflict: 3
  - VerificationGap: 7
  - MissingSlot: 5
  - WeakStatement: 1
  - RationaleGap: 2
  - Normalization: 1
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 3
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 1 | HAS_ITEMS | A-001 records warranted enrichment under this lens. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice lens over normative/applying found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[normative]:[judging] | normative | judging | compliance determination | 1 | HAS_ITEMS | A-003 records warranted enrichment under this lens. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit lens over normative/reviewing found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction lens over operative/guiding found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[operative]:[applying] | operative | applying | practical execution | 1 | HAS_ITEMS | A-002 records warranted enrichment under this lens. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment lens over operative/judging found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit lens over operative/reviewing found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation lens over evaluative/guiding found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application lens over evaluative/applying found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination lens over evaluative/judging found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix A. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 1 | HAS_ITEMS | A-004 records warranted enrichment under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[guiding] | RationaleGap | Guidance | Guidance | Clarify that PRD-derived guidance remains source-warning-limited until hash reconciliation. | The guidance relies on accessible PRD content while also preserving a HASH_MISMATCH warning; the normative direction needs an explicit rationale boundary for later enrichment. | Guidance.md; _REFERENCES.md | Guidance.md#source-state-handling; _REFERENCES.md#authoritative-source-corpus |  | PROPOSAL | TBD |
| A-002 | A:[operative]:[applying] | MissingSlot | Multi | Specification | Add exact implementation file paths for runtime contract, permissions, hooks, settings, event log, and subagent bridge when downstream modules exist. | The production docs intentionally leave implementation surfaces as TBD, which is warranted under the practical-execution lens because enforcement cannot be inspected without concrete paths. | Specification.md; Guidance.md; Procedure.md | Specification.md#open-items; Guidance.md#implementation-surfaces-that-may-be-tbd; Procedure.md#build-boundary-inventory |  | PROPOSAL | TBD |
| A-003 | A:[normative]:[judging] | VerificationGap | Specification | Specification | Require a verification row proving no P0 boundary is prompt-only or opaque-SDK-default-only. | Specification requirements prohibit prompt-only and SDK-default-only enforcement, but final judging needs generated-register evidence after the artifact exists. | Specification.md; Procedure.md | Specification.md#requirements; Procedure.md#cross-check-against-specification |  | PROPOSAL | TBD |
| A-004 | A:[evaluative]:[reviewing] | Conflict | Multi | NA | PRD content may support drafting, but final acceptance requires human/source reconciliation of the hash mismatch. | The docs simultaneously use accessible PRD content and mark the PRD reference as hash-mismatched; this is a recorded conflict requiring human ruling. | Guidance.md; Datasheet.md; _REFERENCES.md | Guidance.md#conflict-table-for-human-ruling; Datasheet.md#source-state; _REFERENCES.md#authoritative-source-corpus | Guidance.md#conflict-table-for-human-ruling; _REFERENCES.md#authoritative-source-corpus | PROPOSAL | TBD |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact lens over data/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens over data/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | B-005 records warranted enrichment under this lens. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement lens over data/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens over information/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens over information/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account lens over information/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[information]:[consistency] | information | consistency | coherent message | 1 | HAS_ITEMS | B-006 records warranted enrichment under this lens. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens over knowledge/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens over knowledge/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery lens over knowledge/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding lens over knowledge/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens over wisdom/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens over wisdom/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens over wisdom/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens over wisdom/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix B. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-005 | B:[data]:[completeness] | MissingSlot | Datasheet | Datasheet | ResponsibleParty remains TBD and needs human assignment before ownership fields are complete. | The datasheet and context both preserve ResponsibleParty as TBD, leaving the ownership record incomplete. | Datasheet.md; _CONTEXT.md | Datasheet.md#identification; _CONTEXT.md#identity |  | PROPOSAL | TBD |
| B-006 | B:[information]:[consistency] | Normalization | Multi | Guidance | Normalize TBD validation identifiers across Datasheet candidate index, Specification open items, and Procedure verification steps. | The docs consistently allow TBD validation IDs, but later enrichment should preserve one naming convention as Section 9 tests land. | Datasheet.md; Specification.md; Procedure.md | Datasheet.md#candidate-validation-index; Specification.md#open-items; Procedure.md#attach-validation-evidence |  | PROPOSAL | TBD |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding source rationale | 1 | HAS_ITEMS | C-007 records warranted enrichment under this lens. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate governance basis | 0 | NO_ITEMS | adequate governance basis lens over normative/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[normative]:[completeness] | normative | completeness | complete rule record | 0 | NO_ITEMS | complete rule record lens over normative/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[normative]:[consistency] | normative | consistency | coherent control doctrine | 0 | NO_ITEMS | coherent control doctrine lens over normative/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[operative]:[necessity] | operative | necessity | required action basis | 0 | NO_ITEMS | required action basis lens over operative/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[operative]:[sufficiency] | operative | sufficiency | workable evidence frame | 0 | NO_ITEMS | workable evidence frame lens over operative/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[operative]:[completeness] | operative | completeness | complete process record | 1 | HAS_ITEMS | C-008 records warranted enrichment under this lens. |
| C:[operative]:[consistency] | operative | consistency | stable execution signal | 0 | NO_ITEMS | stable execution signal lens over operative/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[evaluative]:[necessity] | evaluative | necessity | essential value basis | 0 | NO_ITEMS | essential value basis lens over evaluative/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate merit frame | 0 | NO_ITEMS | adequate merit frame lens over evaluative/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete appraisal record | 0 | NO_ITEMS | complete appraisal record lens over evaluative/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent merit rationale | 0 | NO_ITEMS | coherent merit rationale lens over evaluative/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix C. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-007 | C:[normative]:[necessity] | Conflict | Multi | NA | Binding source rationale for PRD-cited rows remains conditional on resolving REF-006 HASH_MISMATCH. | A binding-source lens cannot treat hash-mismatched PRD content as accepted authority even though the content is currently used for drafting. | Datasheet.md; Guidance.md; _REFERENCES.md | Datasheet.md#source-state; Guidance.md#source-state-handling; _REFERENCES.md#authoritative-source-corpus | Datasheet.md#source-state; _REFERENCES.md#authoritative-source-corpus | PROPOSAL | TBD |
| C-008 | C:[operative]:[completeness] | MissingSlot | Procedure | Procedure | Record completion criteria for the downstream docs/harness/reliance_boundary_register.md artifact once produced. | Procedure names the final artifact and review checks, but the register itself is downstream and not yet present in this deliverable folder. | Procedure.md; Specification.md | Procedure.md#produce-artifacts; Specification.md#documentation |  | PROPOSAL | TBD |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | binding evidence threshold | 0 | NO_ITEMS | binding evidence threshold lens over normative/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[normative]:[sufficiency] | normative | sufficiency | governance proof standard | 1 | HAS_ITEMS | F-009 records warranted enrichment under this lens. |
| F:[normative]:[completeness] | normative | completeness | complete obligation frame | 0 | NO_ITEMS | complete obligation frame lens over normative/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[normative]:[consistency] | normative | consistency | stable conformance rule | 0 | NO_ITEMS | stable conformance rule lens over normative/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[operative]:[necessity] | operative | necessity | action proof threshold | 0 | NO_ITEMS | action proof threshold lens over operative/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[operative]:[sufficiency] | operative | sufficiency | execution adequacy frame | 0 | NO_ITEMS | execution adequacy frame lens over operative/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[operative]:[completeness] | operative | completeness | complete workflow evidence | 1 | HAS_ITEMS | F-010 records warranted enrichment under this lens. |
| F:[operative]:[consistency] | operative | consistency | stable process rule | 0 | NO_ITEMS | stable process rule lens over operative/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[evaluative]:[necessity] | evaluative | necessity | value proof threshold | 0 | NO_ITEMS | value proof threshold lens over evaluative/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | merit adequacy frame | 0 | NO_ITEMS | merit adequacy frame lens over evaluative/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete appraisal evidence | 0 | NO_ITEMS | complete appraisal evidence lens over evaluative/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix F. |
| F:[evaluative]:[consistency] | evaluative | consistency | stable judgment rule | 1 | HAS_ITEMS | F-011 records warranted enrichment under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-009 | F:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Add acceptance evidence that PRD hash reconciliation or human approval occurred before final acceptance. | The current proof standard depends on a source-state warning and open item rather than a completed reconciliation record. | Specification.md; Procedure.md | Specification.md#requirements; Procedure.md#remaining-blockers |  | PROPOSAL | TBD |
| F-010 | F:[operative]:[completeness] | VerificationGap | Procedure | Procedure | Cross-check generated register rows against all RBR requirements after the downstream register exists. | Procedure defines cross-checks, but complete workflow evidence cannot be produced until the final register artifact has rows to inspect. | Procedure.md; Specification.md | Procedure.md#cross-check-against-specification; Specification.md#verification |  | PROPOSAL | TBD |
| F-011 | F:[evaluative]:[consistency] | VerificationGap | Guidance | Guidance | Preserve SDK API drift as a residual-risk topic until R0/R1 probes confirm behavior. | Guidance identifies SDK API drift as residual risk and Procedure carries an SDK probe blocker; stable judgment needs empirical evidence. | Guidance.md; Procedure.md | Guidance.md#residual-risk-topics; Procedure.md#remaining-blockers |  | PROPOSAL | TBD |

## Matrix D — Synthesis

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | binding direction rule | 0 | NO_ITEMS | binding direction rule lens over normative/guiding found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[normative]:[applying] | normative | applying | mandatory closure practice | 1 | HAS_ITEMS | D-012 records warranted enrichment under this lens. |
| D:[normative]:[judging] | normative | judging | conformance decision basis | 0 | NO_ITEMS | conformance decision basis lens over normative/judging found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[normative]:[reviewing] | normative | reviewing | audit closure standard | 0 | NO_ITEMS | audit closure standard lens over normative/reviewing found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[operative]:[guiding] | operative | guiding | procedural closure path | 0 | NO_ITEMS | procedural closure path lens over operative/guiding found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[operative]:[applying] | operative | applying | practical enforcement action | 1 | HAS_ITEMS | D-013 records warranted enrichment under this lens. |
| D:[operative]:[judging] | operative | judging | performance proof basis | 0 | NO_ITEMS | performance proof basis lens over operative/judging found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[operative]:[reviewing] | operative | reviewing | process evidence check | 0 | NO_ITEMS | process evidence check lens over operative/reviewing found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[evaluative]:[guiding] | evaluative | guiding | value closure rationale | 0 | NO_ITEMS | value closure rationale lens over evaluative/guiding found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[evaluative]:[applying] | evaluative | applying | merit enforcement basis | 0 | NO_ITEMS | merit enforcement basis lens over evaluative/applying found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[evaluative]:[judging] | evaluative | judging | worth decision rationale | 0 | NO_ITEMS | worth decision rationale lens over evaluative/judging found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix D. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality evidence standard | 1 | HAS_ITEMS | D-014 records warranted enrichment under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-012 | D:[normative]:[applying] | WeakStatement | Guidance | Guidance | Convert advisory wording around row expectations into explicit enrichment criteria where it affects required register fields. | Guidance uses should-language for register row content; where the same concepts are required by Datasheet and Specification, later enrichment should avoid advisory ambiguity. | Guidance.md; Datasheet.md; Specification.md | Guidance.md#boundary-granularity; Datasheet.md#minimum-register-fields; Specification.md#requirements |  | PROPOSAL | TBD |
| D-013 | D:[operative]:[applying] | MissingSlot | Multi | Specification | Fill exact enforcement owner and surface paths after runtime modules and validation hooks are implemented. | Practical enforcement action is intentionally conceptual at this stage, with exact files and implementation IDs deferred. | Datasheet.md; Guidance.md; Specification.md | Datasheet.md#minimum-register-fields; Guidance.md#implementation-surfaces-that-may-be-tbd; Specification.md#open-items |  | PROPOSAL | TBD |
| D-014 | D:[evaluative]:[reviewing] | RationaleGap | Guidance | Guidance | State why source-warning rows remain review blockers rather than accepted closure evidence. | The docs surface PRD source-state risk, but later quality review benefits from a concise rationale tying that risk to closure limits. | Guidance.md; Procedure.md | Guidance.md#source-state-handling; Procedure.md#review-and-close |  | PROPOSAL | TBD |

## Matrix X — Assessment

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | essential direction proof | 0 | NO_ITEMS | essential direction proof lens over guiding/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | adequate rule support | 0 | NO_ITEMS | adequate rule support lens over guiding/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[guiding]:[completeness] | guiding | completeness | complete intent record | 0 | NO_ITEMS | complete intent record lens over guiding/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[guiding]:[consistency] | guiding | consistency | coherent boundary rationale | 0 | NO_ITEMS | coherent boundary rationale lens over guiding/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[applying]:[necessity] | applying | necessity | essential practice proof | 0 | NO_ITEMS | essential practice proof lens over applying/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[applying]:[sufficiency] | applying | sufficiency | adequate action support | 0 | NO_ITEMS | adequate action support lens over applying/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[applying]:[completeness] | applying | completeness | complete enforcement record | 1 | HAS_ITEMS | X-016 records warranted enrichment under this lens. |
| X:[applying]:[consistency] | applying | consistency | coherent execution rule | 0 | NO_ITEMS | coherent execution rule lens over applying/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[judging]:[necessity] | judging | necessity | essential decision proof | 0 | NO_ITEMS | essential decision proof lens over judging/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate assessment basis | 0 | NO_ITEMS | adequate assessment basis lens over judging/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[judging]:[completeness] | judging | completeness | complete verdict record | 0 | NO_ITEMS | complete verdict record lens over judging/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[judging]:[consistency] | judging | consistency | coherent judgment rationale | 0 | NO_ITEMS | coherent judgment rationale lens over judging/consistency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[reviewing]:[necessity] | reviewing | necessity | essential audit proof | 0 | NO_ITEMS | essential audit proof lens over reviewing/necessity found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | adequate review basis | 0 | NO_ITEMS | adequate review basis lens over reviewing/sufficiency found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete inspection record | 0 | NO_ITEMS | complete inspection record lens over reviewing/completeness found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix X. |
| X:[reviewing]:[consistency] | reviewing | consistency | coherent assurance rationale | 1 | HAS_ITEMS | X-017 records warranted enrichment under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-015 | X:[guiding]:[data] | VerificationGap | Specification | Specification | Require source trace checks to distinguish matched references from REF-006 hash-mismatched PRD usage. | Source trace assurance is incomplete unless validation can show which rows depend on hash-verified sources versus warning-limited PRD content. | Datasheet.md; Specification.md | Datasheet.md#source-state; Specification.md#verification |  | PROPOSAL | TBD |
| X-016 | X:[applying]:[completeness] | MissingSlot | Datasheet | Datasheet | Complete enforcement record fields with concrete module or check locations when downstream deliverables land. | The minimum field schema requires enforcement surfaces, but the current package permits TBD for unavailable implementation paths. | Datasheet.md; Guidance.md | Datasheet.md#minimum-register-fields; Guidance.md#implementation-surfaces-that-may-be-tbd |  | PROPOSAL | TBD |
| X-017 | X:[reviewing]:[consistency] | VerificationGap | Procedure | Procedure | Run cross-document terminology and boundary-ID consistency checks after final register generation. | Procedure lists cross-document consistency as verification, but the final register artifact is still an anticipated output. | Procedure.md; Specification.md | Procedure.md#verification; Specification.md#verification |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | source trace assurance | 1 | HAS_ITEMS | E-018 records warranted enrichment under this lens. |
| E:[guiding]:[information] | guiding | information | contextual intent assurance | 0 | NO_ITEMS | contextual intent assurance lens over guiding/information found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[guiding]:[knowledge] | guiding | knowledge | expertise alignment assurance | 0 | NO_ITEMS | expertise alignment assurance lens over guiding/knowledge found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled direction assurance | 0 | NO_ITEMS | principled direction assurance lens over guiding/wisdom found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[applying]:[data] | applying | data | fact pattern readiness | 0 | NO_ITEMS | fact pattern readiness lens over applying/data found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[applying]:[information] | applying | information | contextual practice readiness | 0 | NO_ITEMS | contextual practice readiness lens over applying/information found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[applying]:[knowledge] | applying | knowledge | expertise execution readiness | 1 | HAS_ITEMS | E-019 records warranted enrichment under this lens. |
| E:[applying]:[wisdom] | applying | wisdom | principled action readiness | 0 | NO_ITEMS | principled action readiness lens over applying/wisdom found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[judging]:[data] | judging | data | fact basis verdict | 0 | NO_ITEMS | fact basis verdict lens over judging/data found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[judging]:[information] | judging | information | contextual assessment verdict | 0 | NO_ITEMS | contextual assessment verdict lens over judging/information found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[judging]:[knowledge] | judging | knowledge | expertise appraisal verdict | 0 | NO_ITEMS | expertise appraisal verdict lens over judging/knowledge found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[judging]:[wisdom] | judging | wisdom | principled decision verdict | 1 | HAS_ITEMS | E-020 records warranted enrichment under this lens. |
| E:[reviewing]:[data] | reviewing | data | fact basis inspection | 0 | NO_ITEMS | fact basis inspection lens over reviewing/data found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[reviewing]:[information] | reviewing | information | contextual audit assurance | 0 | NO_ITEMS | contextual audit assurance lens over reviewing/information found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | expertise review assurance | 1 | HAS_ITEMS | E-021 records warranted enrichment under this lens. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled quality assurance | 0 | NO_ITEMS | principled quality assurance lens over reviewing/wisdom found aligned source, boundary, and verification language without an additional warranted enrichment item for Matrix E. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-018 | E:[guiding]:[data] | Conflict | Multi | NA | Source trace assurance must preserve the REF-006 conflict until a human/source owner resolves the expected PRD hash. | The conflict table and open items show accessible PRD content cannot yet be treated as final accepted truth. | Guidance.md; Specification.md; _REFERENCES.md | Guidance.md#conflict-table-for-human-ruling; Specification.md#open-items; _REFERENCES.md#authoritative-source-corpus | Guidance.md#conflict-table-for-human-ruling; Specification.md#open-items | PROPOSAL | TBD |
| E-019 | E:[applying]:[knowledge] | TBD_Question | Multi | TBD | Which SDK transcript storage and mirroring decision will be accepted after the R1 probe? | Specification, Guidance, and Procedure all preserve transcript placement as unresolved pending empirical probe evidence. | Specification.md; Guidance.md; Procedure.md | Specification.md#open-items; Guidance.md#assumptions-and-tbds; Procedure.md#remaining-blockers |  | PROPOSAL | TBD |
| E-020 | E:[judging]:[wisdom] | TBD_Question | Multi | NA | Has a human/source owner approved the current PRD content as accepted despite the recorded hash mismatch? | Human ruling is explicitly required before PRD-derived content becomes final accepted truth. | Guidance.md; Specification.md | Guidance.md#conflict-table-for-human-ruling; Specification.md#open-items |  | PROPOSAL | TBD |
| E-021 | E:[reviewing]:[knowledge] | VerificationGap | Specification | Specification | Confirm exact Section 9 validation file or test names as runtime validation suite is implemented. | The docs include candidate validation IDs but leave exact implementation IDs as TBD. | Datasheet.md; Specification.md; Guidance.md | Datasheet.md#candidate-validation-index; Specification.md#open-items; Guidance.md#assumptions-and-tbds |  | PROPOSAL | TBD |
