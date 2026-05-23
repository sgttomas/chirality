# Semantic Lensing Register: DEL-09-03 Unit and Integration Test Expansion

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — validate_lens_register.py completed successfully after generation
**Warnings:** PRD hash mismatch retained as human-ruling conflict; dependency extraction remains deferred; implementation paths remain TBD until coding work.

**Inputs Read:**
- _CONTEXT.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/_CONTEXT.md#identity
- _STATUS.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/_STATUS.md#history
- _SEMANTIC.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/_SEMANTIC.md#semantic-lens-del-09-03-unit-and-integration-test-expansion
- Datasheet.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/Datasheet.md#construction
- Specification.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/Specification.md#requirements
- Guidance.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/Guidance.md#principles
- Procedure.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/Procedure.md#steps
- _REFERENCES.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/_REFERENCES.md#authoritative-source-corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 8
- By document:
  - Datasheet: 0
  - Specification: 2
  - Guidance: 0
  - Procedure: 4
  - Multi: 0
  - NA: 1
- By matrix:
  - A: 1
  - B: 1
  - C: 1
  - F: 1
  - D: 1
  - X: 1
  - E: 2
- By type:
  - Conflict: 1
  - VerificationGap: 2
  - MissingSlot: 4
  - WeakStatement: 0
  - RationaleGap: 0
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction lens maps to current DEL-09-03 text through normative/guiding without an additional grounded enrichment entry. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 1 | HAS_ITEMS | mandatory practice lens produced 1 evidence-linked register item for normative/applying review. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination lens maps to current DEL-09-03 text through normative/judging without an additional grounded enrichment entry. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit lens maps to current DEL-09-03 text through normative/reviewing without an additional grounded enrichment entry. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction lens maps to current DEL-09-03 text through operative/guiding without an additional grounded enrichment entry. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution lens maps to current DEL-09-03 text through operative/applying without an additional grounded enrichment entry. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment lens maps to current DEL-09-03 text through operative/judging without an additional grounded enrichment entry. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit lens maps to current DEL-09-03 text through operative/reviewing without an additional grounded enrichment entry. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation lens maps to current DEL-09-03 text through evaluative/guiding without an additional grounded enrichment entry. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application lens maps to current DEL-09-03 text through evaluative/applying without an additional grounded enrichment entry. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination lens maps to current DEL-09-03 text through evaluative/judging without an additional grounded enrichment entry. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal lens maps to current DEL-09-03 text through evaluative/reviewing without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[applying] | VerificationGap | Specification | Specification | Clarify whether each mandatory behavior group requires at least one implemented test case before closure. | Specification lists behavior groups and verification modes, but it does not state a minimum per-group closure threshold for later implementation review. | Specification.md | Requirements |  | PROPOSAL | TBD |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact lens maps to current DEL-09-03 text through data/necessity without an additional grounded enrichment entry. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens maps to current DEL-09-03 text through data/sufficiency without an additional grounded enrichment entry. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | comprehensive record lens produced 1 evidence-linked register item for data/completeness review. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement lens maps to current DEL-09-03 text through data/consistency without an additional grounded enrichment entry. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens maps to current DEL-09-03 text through information/necessity without an additional grounded enrichment entry. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens maps to current DEL-09-03 text through information/sufficiency without an additional grounded enrichment entry. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account lens maps to current DEL-09-03 text through information/completeness without an additional grounded enrichment entry. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message lens maps to current DEL-09-03 text through information/consistency without an additional grounded enrichment entry. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens maps to current DEL-09-03 text through knowledge/necessity without an additional grounded enrichment entry. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens maps to current DEL-09-03 text through knowledge/sufficiency without an additional grounded enrichment entry. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery lens maps to current DEL-09-03 text through knowledge/completeness without an additional grounded enrichment entry. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding lens maps to current DEL-09-03 text through knowledge/consistency without an additional grounded enrichment entry. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens maps to current DEL-09-03 text through wisdom/necessity without an additional grounded enrichment entry. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens maps to current DEL-09-03 text through wisdom/sufficiency without an additional grounded enrichment entry. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens maps to current DEL-09-03 text through wisdom/completeness without an additional grounded enrichment entry. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens maps to current DEL-09-03 text through wisdom/consistency without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[completeness] | MissingSlot | Procedure | Procedure | Populate concrete test source files, fixtures, and command evidence after implementation paths are selected. | Procedure Records leaves test source files, fixtures, and command evidence as TBD, so the comprehensive-record lens exposes missing closure evidence. | Procedure.md | Records |  | PROPOSAL | TBD |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | test mandate | 0 | NO_ITEMS | test mandate lens maps to current DEL-09-03 text through normative/necessity without an additional grounded enrichment entry. |
| C:[normative]:[sufficiency] | normative | sufficiency | coverage warrant | 0 | NO_ITEMS | coverage warrant lens maps to current DEL-09-03 text through normative/sufficiency without an additional grounded enrichment entry. |
| C:[normative]:[completeness] | normative | completeness | contract scope | 0 | NO_ITEMS | contract scope lens maps to current DEL-09-03 text through normative/completeness without an additional grounded enrichment entry. |
| C:[normative]:[consistency] | normative | consistency | source coherence | 0 | NO_ITEMS | source coherence lens maps to current DEL-09-03 text through normative/consistency without an additional grounded enrichment entry. |
| C:[operative]:[necessity] | operative | necessity | fixture need | 1 | HAS_ITEMS | fixture need lens produced 1 evidence-linked register item for operative/necessity review. |
| C:[operative]:[sufficiency] | operative | sufficiency | execution proof | 0 | NO_ITEMS | execution proof lens maps to current DEL-09-03 text through operative/sufficiency without an additional grounded enrichment entry. |
| C:[operative]:[completeness] | operative | completeness | workflow coverage | 0 | NO_ITEMS | workflow coverage lens maps to current DEL-09-03 text through operative/completeness without an additional grounded enrichment entry. |
| C:[operative]:[consistency] | operative | consistency | runtime stability | 0 | NO_ITEMS | runtime stability lens maps to current DEL-09-03 text through operative/consistency without an additional grounded enrichment entry. |
| C:[evaluative]:[necessity] | evaluative | necessity | review criterion | 0 | NO_ITEMS | review criterion lens maps to current DEL-09-03 text through evaluative/necessity without an additional grounded enrichment entry. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | evidence judgment | 0 | NO_ITEMS | evidence judgment lens maps to current DEL-09-03 text through evaluative/sufficiency without an additional grounded enrichment entry. |
| C:[evaluative]:[completeness] | evaluative | completeness | regression appraisal | 0 | NO_ITEMS | regression appraisal lens maps to current DEL-09-03 text through evaluative/completeness without an additional grounded enrichment entry. |
| C:[evaluative]:[consistency] | evaluative | consistency | quality coherence | 0 | NO_ITEMS | quality coherence lens maps to current DEL-09-03 text through evaluative/consistency without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[necessity] | MissingSlot | Procedure | Procedure | Identify exact frontend test directories and files before creating fixtures or assertions. | Procedure Prerequisites marks implementation paths as TBD, making fixture execution dependent on a later implementation-path decision. | Procedure.md | Prerequisites |  | PROPOSAL | TBD |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | coverage obligation | 0 | NO_ITEMS | coverage obligation lens maps to current DEL-09-03 text through normative/necessity without an additional grounded enrichment entry. |
| F:[normative]:[sufficiency] | normative | sufficiency | proof threshold | 1 | HAS_ITEMS | proof threshold lens produced 1 evidence-linked register item for normative/sufficiency review. |
| F:[normative]:[completeness] | normative | completeness | contract closure | 0 | NO_ITEMS | contract closure lens maps to current DEL-09-03 text through normative/completeness without an additional grounded enrichment entry. |
| F:[normative]:[consistency] | normative | consistency | trace coherence | 0 | NO_ITEMS | trace coherence lens maps to current DEL-09-03 text through normative/consistency without an additional grounded enrichment entry. |
| F:[operative]:[necessity] | operative | necessity | fixture prerequisite | 0 | NO_ITEMS | fixture prerequisite lens maps to current DEL-09-03 text through operative/necessity without an additional grounded enrichment entry. |
| F:[operative]:[sufficiency] | operative | sufficiency | test evidence | 0 | NO_ITEMS | test evidence lens maps to current DEL-09-03 text through operative/sufficiency without an additional grounded enrichment entry. |
| F:[operative]:[completeness] | operative | completeness | workflow closure | 0 | NO_ITEMS | workflow closure lens maps to current DEL-09-03 text through operative/completeness without an additional grounded enrichment entry. |
| F:[operative]:[consistency] | operative | consistency | execution reliability | 0 | NO_ITEMS | execution reliability lens maps to current DEL-09-03 text through operative/consistency without an additional grounded enrichment entry. |
| F:[evaluative]:[necessity] | evaluative | necessity | assessment basis | 0 | NO_ITEMS | assessment basis lens maps to current DEL-09-03 text through evaluative/necessity without an additional grounded enrichment entry. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | review evidence | 0 | NO_ITEMS | review evidence lens maps to current DEL-09-03 text through evaluative/sufficiency without an additional grounded enrichment entry. |
| F:[evaluative]:[completeness] | evaluative | completeness | confidence closure | 0 | NO_ITEMS | confidence closure lens maps to current DEL-09-03 text through evaluative/completeness without an additional grounded enrichment entry. |
| F:[evaluative]:[consistency] | evaluative | consistency | quality alignment | 0 | NO_ITEMS | quality alignment lens maps to current DEL-09-03 text through evaluative/consistency without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Capture actual command output or stable validation artifact for npm run test when the implementation run occurs. | Specification and Procedure name npm run test as the gate, but current records do not yet contain passing command evidence. | Specification.md; Procedure.md | Verification; Records |  | PROPOSAL | TBD |

## Matrix D — Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | scope direction | 0 | NO_ITEMS | scope direction lens maps to current DEL-09-03 text through normative/guiding without an additional grounded enrichment entry. |
| D:[normative]:[applying] | normative | applying | coverage practice | 0 | NO_ITEMS | coverage practice lens maps to current DEL-09-03 text through normative/applying without an additional grounded enrichment entry. |
| D:[normative]:[judging] | normative | judging | contract determination | 0 | NO_ITEMS | contract determination lens maps to current DEL-09-03 text through normative/judging without an additional grounded enrichment entry. |
| D:[normative]:[reviewing] | normative | reviewing | validation audit | 1 | HAS_ITEMS | validation audit lens produced 1 evidence-linked register item for normative/reviewing review. |
| D:[operative]:[guiding] | operative | guiding | fixture direction | 0 | NO_ITEMS | fixture direction lens maps to current DEL-09-03 text through operative/guiding without an additional grounded enrichment entry. |
| D:[operative]:[applying] | operative | applying | test execution | 0 | NO_ITEMS | test execution lens maps to current DEL-09-03 text through operative/applying without an additional grounded enrichment entry. |
| D:[operative]:[judging] | operative | judging | regression assessment | 0 | NO_ITEMS | regression assessment lens maps to current DEL-09-03 text through operative/judging without an additional grounded enrichment entry. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance | 0 | NO_ITEMS | process assurance lens maps to current DEL-09-03 text through operative/reviewing without an additional grounded enrichment entry. |
| D:[evaluative]:[guiding] | evaluative | guiding | quality orientation | 0 | NO_ITEMS | quality orientation lens maps to current DEL-09-03 text through evaluative/guiding without an additional grounded enrichment entry. |
| D:[evaluative]:[applying] | evaluative | applying | confidence application | 0 | NO_ITEMS | confidence application lens maps to current DEL-09-03 text through evaluative/applying without an additional grounded enrichment entry. |
| D:[evaluative]:[judging] | evaluative | judging | readiness determination | 0 | NO_ITEMS | readiness determination lens maps to current DEL-09-03 text through evaluative/judging without an additional grounded enrichment entry. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | release appraisal | 0 | NO_ITEMS | release appraisal lens maps to current DEL-09-03 text through evaluative/reviewing without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[normative]:[reviewing] | Conflict | Guidance | NA | PRD hash mismatch remains a human-ruling conflict for source-grounded PRD references. | Guidance records CONFLICT-001 with expected and observed PRD SHA256 mismatch; the register must preserve the audit issue without resolving it. | Guidance.md; _REFERENCES.md | Conflict Table; Authoritative Source Corpus | Guidance.md#Conflict Table; _REFERENCES.md#Authoritative Source Corpus | PROPOSAL | TBD |

## Matrix X — Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | scope prerequisite | 0 | NO_ITEMS | scope prerequisite lens maps to current DEL-09-03 text through guiding/necessity without an additional grounded enrichment entry. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | direction evidence | 0 | NO_ITEMS | direction evidence lens maps to current DEL-09-03 text through guiding/sufficiency without an additional grounded enrichment entry. |
| X:[guiding]:[completeness] | guiding | completeness | coverage mandate | 0 | NO_ITEMS | coverage mandate lens maps to current DEL-09-03 text through guiding/completeness without an additional grounded enrichment entry. |
| X:[guiding]:[consistency] | guiding | consistency | source alignment | 0 | NO_ITEMS | source alignment lens maps to current DEL-09-03 text through guiding/consistency without an additional grounded enrichment entry. |
| X:[applying]:[necessity] | applying | necessity | practice prerequisite | 0 | NO_ITEMS | practice prerequisite lens maps to current DEL-09-03 text through applying/necessity without an additional grounded enrichment entry. |
| X:[applying]:[sufficiency] | applying | sufficiency | test proof | 0 | NO_ITEMS | test proof lens maps to current DEL-09-03 text through applying/sufficiency without an additional grounded enrichment entry. |
| X:[applying]:[completeness] | applying | completeness | execution closure | 0 | NO_ITEMS | execution closure lens maps to current DEL-09-03 text through applying/completeness without an additional grounded enrichment entry. |
| X:[applying]:[consistency] | applying | consistency | runtime reliability | 0 | NO_ITEMS | runtime reliability lens maps to current DEL-09-03 text through applying/consistency without an additional grounded enrichment entry. |
| X:[judging]:[necessity] | judging | necessity | verdict basis | 0 | NO_ITEMS | verdict basis lens maps to current DEL-09-03 text through judging/necessity without an additional grounded enrichment entry. |
| X:[judging]:[sufficiency] | judging | sufficiency | conformance evidence | 0 | NO_ITEMS | conformance evidence lens maps to current DEL-09-03 text through judging/sufficiency without an additional grounded enrichment entry. |
| X:[judging]:[completeness] | judging | completeness | determination closure | 1 | HAS_ITEMS | determination closure lens produced 1 evidence-linked register item for judging/completeness review. |
| X:[judging]:[consistency] | judging | consistency | decision coherence | 0 | NO_ITEMS | decision coherence lens maps to current DEL-09-03 text through judging/consistency without an additional grounded enrichment entry. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit basis | 0 | NO_ITEMS | audit basis lens maps to current DEL-09-03 text through reviewing/necessity without an additional grounded enrichment entry. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | assurance evidence | 0 | NO_ITEMS | assurance evidence lens maps to current DEL-09-03 text through reviewing/sufficiency without an additional grounded enrichment entry. |
| X:[reviewing]:[completeness] | reviewing | completeness | review closure | 0 | NO_ITEMS | review closure lens maps to current DEL-09-03 text through reviewing/completeness without an additional grounded enrichment entry. |
| X:[reviewing]:[consistency] | reviewing | consistency | release assurance | 0 | NO_ITEMS | release assurance lens maps to current DEL-09-03 text through reviewing/consistency without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[completeness] | MissingSlot | Procedure | Procedure | Record final test source paths, fixture paths, and validation command evidence before determination closure. | Procedure Records explicitly leaves all implementation evidence fields TBD, preventing a complete determination package. | Procedure.md | Records |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | source direction | 0 | NO_ITEMS | source direction lens maps to current DEL-09-03 text through guiding/data without an additional grounded enrichment entry. |
| E:[guiding]:[information] | guiding | information | context direction | 0 | NO_ITEMS | context direction lens maps to current DEL-09-03 text through guiding/information without an additional grounded enrichment entry. |
| E:[guiding]:[knowledge] | guiding | knowledge | coverage understanding | 0 | NO_ITEMS | coverage understanding lens maps to current DEL-09-03 text through guiding/knowledge without an additional grounded enrichment entry. |
| E:[guiding]:[wisdom] | guiding | wisdom | boundary discernment | 0 | NO_ITEMS | boundary discernment lens maps to current DEL-09-03 text through guiding/wisdom without an additional grounded enrichment entry. |
| E:[applying]:[data] | applying | data | fixture practice | 1 | HAS_ITEMS | fixture practice lens produced 1 evidence-linked register item for applying/data review. |
| E:[applying]:[information] | applying | information | test method | 0 | NO_ITEMS | test method lens maps to current DEL-09-03 text through applying/information without an additional grounded enrichment entry. |
| E:[applying]:[knowledge] | applying | knowledge | runtime expertise | 0 | NO_ITEMS | runtime expertise lens maps to current DEL-09-03 text through applying/knowledge without an additional grounded enrichment entry. |
| E:[applying]:[wisdom] | applying | wisdom | method judgment | 0 | NO_ITEMS | method judgment lens maps to current DEL-09-03 text through applying/wisdom without an additional grounded enrichment entry. |
| E:[judging]:[data] | judging | data | evidence verdict | 0 | NO_ITEMS | evidence verdict lens maps to current DEL-09-03 text through judging/data without an additional grounded enrichment entry. |
| E:[judging]:[information] | judging | information | context verdict | 0 | NO_ITEMS | context verdict lens maps to current DEL-09-03 text through judging/information without an additional grounded enrichment entry. |
| E:[judging]:[knowledge] | judging | knowledge | confidence determination | 0 | NO_ITEMS | confidence determination lens maps to current DEL-09-03 text through judging/knowledge without an additional grounded enrichment entry. |
| E:[judging]:[wisdom] | judging | wisdom | release judgment | 0 | NO_ITEMS | release judgment lens maps to current DEL-09-03 text through judging/wisdom without an additional grounded enrichment entry. |
| E:[reviewing]:[data] | reviewing | data | audit evidence | 0 | NO_ITEMS | audit evidence lens maps to current DEL-09-03 text through reviewing/data without an additional grounded enrichment entry. |
| E:[reviewing]:[information] | reviewing | information | assurance context | 1 | HAS_ITEMS | assurance context lens produced 1 evidence-linked register item for reviewing/information review. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | review expertise | 0 | NO_ITEMS | review expertise lens maps to current DEL-09-03 text through reviewing/knowledge without an additional grounded enrichment entry. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | release discernment | 0 | NO_ITEMS | release discernment lens maps to current DEL-09-03 text through reviewing/wisdom without an additional grounded enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[applying]:[data] | MissingSlot | Procedure | Procedure | Replace fixture path TBDs with actual fixture files for symlink, budget, malformed JSONL, dependency, status, and denied-tool cases. | Procedure Step 5 names fixture classes, while Records leaves fixture locations TBD until implementation identifies paths. | Procedure.md | Steps; Records |  | PROPOSAL | TBD |
| E-002 | E:[reviewing]:[information] | TBD_Question | Procedure | TBD | Determine whether upstream dependency edges must be extracted before final release-readiness review. | Procedure Prerequisites states upstream dependencies are TBD and no accepted dependency edges have been extracted, so review context remains incomplete. | Procedure.md | Prerequisites |  | PROPOSAL | TBD |
