# Semantic Lensing Register: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py passed for this deliverable
**Warnings:** Existing deliverable has pre-run uncommitted changes; this run writes only _SEMANTIC_LENSING.md and its TASK run record.

**Inputs Read:**
- _CONTEXT.md - `_CONTEXT.md#identity`
- _STATUS.md - `_STATUS.md#status-del-01-01`
- _SEMANTIC.md - `_SEMANTIC.md`
- Datasheet.md - `Datasheet.md#attributes`
- Specification.md - `Specification.md#requirements`
- Guidance.md - `Guidance.md#principles`
- Procedure.md - `Procedure.md#steps`
- _REFERENCES.md - `_REFERENCES.md#authoritative-source-corpus` metadata only; external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 7
- By document:
  - Datasheet: 0
  - Specification: 1
  - Guidance: 1
  - Procedure: 2
  - Multi: 3
  - NA: 0
- By matrix:
  - A: 1
  - B: 1
  - C: 1
  - F: 1
  - D: 1
  - X: 1
  - E: 1
- By type:
  - Conflict: 2
  - VerificationGap: 2
  - MissingSlot: 1
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 2
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction lens checked normative/guiding evidence without surfacing a distinct enrichment input. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice lens checked normative/applying evidence without surfacing a distinct enrichment input. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination lens checked normative/judging evidence without surfacing a distinct enrichment input. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | regulatory audit lens yields 1 warranted register item for normative/reviewing governance follow-up. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction lens checked operative/guiding evidence without surfacing a distinct enrichment input. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution lens checked operative/applying evidence without surfacing a distinct enrichment input. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment lens checked operative/judging evidence without surfacing a distinct enrichment input. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit lens checked operative/reviewing evidence without surfacing a distinct enrichment input. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation lens checked evaluative/guiding evidence without surfacing a distinct enrichment input. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application lens checked evaluative/applying evidence without surfacing a distinct enrichment input. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination lens checked evaluative/judging evidence without surfacing a distinct enrichment input. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal lens checked evaluative/reviewing evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Keep the PRD hash mismatch as source-warning status until a human ruling accepts, bypasses, or updates REF-006. | The lens exposes regulatory-audit posture: Guidance records DEL-01-01-C001 and R001, while Specification Standards also mark PRD as hash-mismatched. The register should preserve the conflict rather than resolve it. | Guidance.md; Specification.md | Guidance.md#conflict-table-for-human-ruling; Specification.md#standards | Guidance.md#conflict-table-for-human-ruling; Specification.md#standards | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact lens checked data/necessity evidence without surfacing a distinct enrichment input. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens checked data/sufficiency evidence without surfacing a distinct enrichment input. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record lens checked data/completeness evidence without surfacing a distinct enrichment input. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | reliable measurement lens yields 1 warranted register item for data/consistency governance follow-up. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens checked information/necessity evidence without surfacing a distinct enrichment input. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens checked information/sufficiency evidence without surfacing a distinct enrichment input. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account lens checked information/completeness evidence without surfacing a distinct enrichment input. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message lens checked information/consistency evidence without surfacing a distinct enrichment input. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens checked knowledge/necessity evidence without surfacing a distinct enrichment input. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens checked knowledge/sufficiency evidence without surfacing a distinct enrichment input. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery lens checked knowledge/completeness evidence without surfacing a distinct enrichment input. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding lens checked knowledge/consistency evidence without surfacing a distinct enrichment input. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens checked wisdom/necessity evidence without surfacing a distinct enrichment input. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens checked wisdom/sufficiency evidence without surfacing a distinct enrichment input. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens checked wisdom/completeness evidence without surfacing a distinct enrichment input. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens checked wisdom/consistency evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | VerificationGap | Multi | Specification | Add an acceptance check requiring source-warning evidence to be tied to the exact reference row or human bypass decision before clean reliance. | Reliable-measurement lens finds that the documents identify the PRD hash mismatch but do not define a pass/fail measurement for when warning status becomes accepted. | Specification.md; Guidance.md | Specification.md#verification; Guidance.md#considerations |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding basis | 0 | NO_ITEMS | binding basis lens checked normative/necessity evidence without surfacing a distinct enrichment input. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequacy threshold | 1 | HAS_ITEMS | adequacy threshold lens yields 1 warranted register item for normative/sufficiency governance follow-up. |
| C:[normative]:[completeness] | normative | completeness | coverage standard | 0 | NO_ITEMS | coverage standard lens checked normative/completeness evidence without surfacing a distinct enrichment input. |
| C:[normative]:[consistency] | normative | consistency | coherence rule | 0 | NO_ITEMS | coherence rule lens checked normative/consistency evidence without surfacing a distinct enrichment input. |
| C:[operative]:[necessity] | operative | necessity | execution prerequisite | 0 | NO_ITEMS | execution prerequisite lens checked operative/necessity evidence without surfacing a distinct enrichment input. |
| C:[operative]:[sufficiency] | operative | sufficiency | evidence practice | 0 | NO_ITEMS | evidence practice lens checked operative/sufficiency evidence without surfacing a distinct enrichment input. |
| C:[operative]:[completeness] | operative | completeness | record discipline | 0 | NO_ITEMS | record discipline lens checked operative/completeness evidence without surfacing a distinct enrichment input. |
| C:[operative]:[consistency] | operative | consistency | measurement control | 0 | NO_ITEMS | measurement control lens checked operative/consistency evidence without surfacing a distinct enrichment input. |
| C:[evaluative]:[necessity] | evaluative | necessity | discernment basis | 0 | NO_ITEMS | discernment basis lens checked evaluative/necessity evidence without surfacing a distinct enrichment input. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment warrant | 0 | NO_ITEMS | judgment warrant lens checked evaluative/sufficiency evidence without surfacing a distinct enrichment input. |
| C:[evaluative]:[completeness] | evaluative | completeness | insight standard | 0 | NO_ITEMS | insight standard lens checked evaluative/completeness evidence without surfacing a distinct enrichment input. |
| C:[evaluative]:[consistency] | evaluative | consistency | reasoned appraisal | 0 | NO_ITEMS | reasoned appraisal lens checked evaluative/consistency evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[sufficiency] | TBD_Question | Multi | NA | Who is the assigned ResponsibleParty for DEL-01-01, and when may ownership replace TBD? | The adequacy-threshold lens finds all production documents preserve ResponsibleParty as TBD, which is correct until a human assignment exists but remains a blocking open governance datum. | Datasheet.md; Specification.md; Guidance.md; Procedure.md | Datasheet.md#identification; Specification.md#scope; Guidance.md#considerations; Procedure.md#verification |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | authority prerequisite | 0 | NO_ITEMS | authority prerequisite lens checked normative/necessity evidence without surfacing a distinct enrichment input. |
| F:[normative]:[sufficiency] | normative | sufficiency | evidence warrant | 0 | NO_ITEMS | evidence warrant lens checked normative/sufficiency evidence without surfacing a distinct enrichment input. |
| F:[normative]:[completeness] | normative | completeness | closure basis | 1 | HAS_ITEMS | closure basis lens yields 1 warranted register item for normative/completeness governance follow-up. |
| F:[normative]:[consistency] | normative | consistency | alignment discipline | 0 | NO_ITEMS | alignment discipline lens checked normative/consistency evidence without surfacing a distinct enrichment input. |
| F:[operative]:[necessity] | operative | necessity | work precondition | 0 | NO_ITEMS | work precondition lens checked operative/necessity evidence without surfacing a distinct enrichment input. |
| F:[operative]:[sufficiency] | operative | sufficiency | context warrant | 0 | NO_ITEMS | context warrant lens checked operative/sufficiency evidence without surfacing a distinct enrichment input. |
| F:[operative]:[completeness] | operative | completeness | trace coverage | 0 | NO_ITEMS | trace coverage lens checked operative/completeness evidence without surfacing a distinct enrichment input. |
| F:[operative]:[consistency] | operative | consistency | coherence practice | 0 | NO_ITEMS | coherence practice lens checked operative/consistency evidence without surfacing a distinct enrichment input. |
| F:[evaluative]:[necessity] | evaluative | necessity | ruling basis | 0 | NO_ITEMS | ruling basis lens checked evaluative/necessity evidence without surfacing a distinct enrichment input. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment threshold | 0 | NO_ITEMS | judgment threshold lens checked evaluative/sufficiency evidence without surfacing a distinct enrichment input. |
| F:[evaluative]:[completeness] | evaluative | completeness | integrity review | 0 | NO_ITEMS | integrity review lens checked evaluative/completeness evidence without surfacing a distinct enrichment input. |
| F:[evaluative]:[consistency] | evaluative | consistency | reasoning discipline | 0 | NO_ITEMS | reasoning discipline lens checked evaluative/consistency evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[completeness] | MissingSlot | Specification | Specification | Define final artifact filenames and destination locations for governance consistency notes, authority checklist, project-truth checklist, runtime-audit checklist, diff checklist, acceptance checklist, and conflict table. | The closure-basis lens finds the expected artifact set named, but Specification explicitly leaves final filenames and destinations as TBD. | Specification.md; Guidance.md | Specification.md#documentation; Guidance.md#human-rulings-needed |  | PROPOSAL | TBD |

## Matrix D - Implementation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governing direction | 0 | NO_ITEMS | governing direction lens checked normative/guiding evidence without surfacing a distinct enrichment input. |
| D:[normative]:[applying] | normative | applying | binding practice | 0 | NO_ITEMS | binding practice lens checked normative/applying evidence without surfacing a distinct enrichment input. |
| D:[normative]:[judging] | normative | judging | closure determination | 0 | NO_ITEMS | closure determination lens checked normative/judging evidence without surfacing a distinct enrichment input. |
| D:[normative]:[reviewing] | normative | reviewing | audit discipline | 0 | NO_ITEMS | audit discipline lens checked normative/reviewing evidence without surfacing a distinct enrichment input. |
| D:[operative]:[guiding] | operative | guiding | execution direction | 0 | NO_ITEMS | execution direction lens checked operative/guiding evidence without surfacing a distinct enrichment input. |
| D:[operative]:[applying] | operative | applying | controlled performance | 0 | NO_ITEMS | controlled performance lens checked operative/applying evidence without surfacing a distinct enrichment input. |
| D:[operative]:[judging] | operative | judging | assessment closure | 1 | HAS_ITEMS | assessment closure lens yields 1 warranted register item for operative/judging governance follow-up. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance | 0 | NO_ITEMS | process assurance lens checked operative/reviewing evidence without surfacing a distinct enrichment input. |
| D:[evaluative]:[guiding] | evaluative | guiding | value rationale | 0 | NO_ITEMS | value rationale lens checked evaluative/guiding evidence without surfacing a distinct enrichment input. |
| D:[evaluative]:[applying] | evaluative | applying | merit standard | 0 | NO_ITEMS | merit standard lens checked evaluative/applying evidence without surfacing a distinct enrichment input. |
| D:[evaluative]:[judging] | evaluative | judging | worth closure | 0 | NO_ITEMS | worth closure lens checked evaluative/judging evidence without surfacing a distinct enrichment input. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality judgment | 0 | NO_ITEMS | quality judgment lens checked evaluative/reviewing evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[judging] | Conflict | Procedure | Procedure | Update the lifecycle prerequisite wording to reflect Current State INITIALIZED, or record why the OPEN wording is historical. | The assessment-closure lens finds Procedure Prerequisites says lifecycle state permits OPEN, while _STATUS.md states Current State INITIALIZED. This is a local consistency conflict for later procedural use. | Procedure.md; _STATUS.md | Procedure.md#prerequisites; _STATUS.md#status-del-01-01 | Procedure.md#prerequisites; _STATUS.md#status-del-01-01 | PROPOSAL | TBD |

## Matrix X - Assessment

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | directive warrant | 0 | NO_ITEMS | directive warrant lens checked guiding/necessity evidence without surfacing a distinct enrichment input. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | grounded threshold | 0 | NO_ITEMS | grounded threshold lens checked guiding/sufficiency evidence without surfacing a distinct enrichment input. |
| X:[guiding]:[completeness] | guiding | completeness | coverage rationale | 0 | NO_ITEMS | coverage rationale lens checked guiding/completeness evidence without surfacing a distinct enrichment input. |
| X:[guiding]:[consistency] | guiding | consistency | coherent direction | 0 | NO_ITEMS | coherent direction lens checked guiding/consistency evidence without surfacing a distinct enrichment input. |
| X:[applying]:[necessity] | applying | necessity | practice prerequisite | 0 | NO_ITEMS | practice prerequisite lens checked applying/necessity evidence without surfacing a distinct enrichment input. |
| X:[applying]:[sufficiency] | applying | sufficiency | implementation warrant | 0 | NO_ITEMS | implementation warrant lens checked applying/sufficiency evidence without surfacing a distinct enrichment input. |
| X:[applying]:[completeness] | applying | completeness | complete practice | 0 | NO_ITEMS | complete practice lens checked applying/completeness evidence without surfacing a distinct enrichment input. |
| X:[applying]:[consistency] | applying | consistency | coherent application | 0 | NO_ITEMS | coherent application lens checked applying/consistency evidence without surfacing a distinct enrichment input. |
| X:[judging]:[necessity] | judging | necessity | decision basis | 0 | NO_ITEMS | decision basis lens checked judging/necessity evidence without surfacing a distinct enrichment input. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate assessment | 0 | NO_ITEMS | adequate assessment lens checked judging/sufficiency evidence without surfacing a distinct enrichment input. |
| X:[judging]:[completeness] | judging | completeness | closure finding | 0 | NO_ITEMS | closure finding lens checked judging/completeness evidence without surfacing a distinct enrichment input. |
| X:[judging]:[consistency] | judging | consistency | consistent appraisal | 0 | NO_ITEMS | consistent appraisal lens checked judging/consistency evidence without surfacing a distinct enrichment input. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit trigger | 0 | NO_ITEMS | audit trigger lens checked reviewing/necessity evidence without surfacing a distinct enrichment input. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | evidence threshold | 0 | NO_ITEMS | evidence threshold lens checked reviewing/sufficiency evidence without surfacing a distinct enrichment input. |
| X:[reviewing]:[completeness] | reviewing | completeness | review coverage | 1 | HAS_ITEMS | review coverage lens yields 1 warranted register item for reviewing/completeness governance follow-up. |
| X:[reviewing]:[consistency] | reviewing | consistency | assurance coherence | 0 | NO_ITEMS | assurance coherence lens checked reviewing/consistency evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[completeness] | VerificationGap | Procedure | Procedure | Add a verification row for binding governance notes to git SHA or equivalent immutable evidence when they become acceptance evidence. | The review-coverage lens finds Guidance requires acceptance evidence to bind to git SHA or equivalent, but Procedure Verification does not carry a corresponding explicit pass condition. | Guidance.md; Procedure.md | Guidance.md#considerations; Procedure.md#verification |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual warrant | 0 | NO_ITEMS | factual warrant lens checked guiding/data evidence without surfacing a distinct enrichment input. |
| E:[guiding]:[information] | guiding | information | signal rationale | 0 | NO_ITEMS | signal rationale lens checked guiding/information evidence without surfacing a distinct enrichment input. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding frame | 0 | NO_ITEMS | understanding frame lens checked guiding/knowledge evidence without surfacing a distinct enrichment input. |
| E:[guiding]:[wisdom] | guiding | wisdom | discernment guide | 0 | NO_ITEMS | discernment guide lens checked guiding/wisdom evidence without surfacing a distinct enrichment input. |
| E:[applying]:[data] | applying | data | fact practice | 0 | NO_ITEMS | fact practice lens checked applying/data evidence without surfacing a distinct enrichment input. |
| E:[applying]:[information] | applying | information | context enactment | 0 | NO_ITEMS | context enactment lens checked applying/information evidence without surfacing a distinct enrichment input. |
| E:[applying]:[knowledge] | applying | knowledge | expertise method | 0 | NO_ITEMS | expertise method lens checked applying/knowledge evidence without surfacing a distinct enrichment input. |
| E:[applying]:[wisdom] | applying | wisdom | judgment practice | 0 | NO_ITEMS | judgment practice lens checked applying/wisdom evidence without surfacing a distinct enrichment input. |
| E:[judging]:[data] | judging | data | evidence decision | 0 | NO_ITEMS | evidence decision lens checked judging/data evidence without surfacing a distinct enrichment input. |
| E:[judging]:[information] | judging | information | message assessment | 0 | NO_ITEMS | message assessment lens checked judging/information evidence without surfacing a distinct enrichment input. |
| E:[judging]:[knowledge] | judging | knowledge | mastery appraisal | 0 | NO_ITEMS | mastery appraisal lens checked judging/knowledge evidence without surfacing a distinct enrichment input. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned finding | 0 | NO_ITEMS | reasoned finding lens checked judging/wisdom evidence without surfacing a distinct enrichment input. |
| E:[reviewing]:[data] | reviewing | data | record audit | 1 | HAS_ITEMS | record audit lens yields 1 warranted register item for reviewing/data governance follow-up. |
| E:[reviewing]:[information] | reviewing | information | account review | 0 | NO_ITEMS | account review lens checked reviewing/information evidence without surfacing a distinct enrichment input. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery assurance | 0 | NO_ITEMS | mastery assurance lens checked reviewing/knowledge evidence without surfacing a distinct enrichment input. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled appraisal | 0 | NO_ITEMS | principled appraisal lens checked reviewing/wisdom evidence without surfacing a distinct enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[data] | RationaleGap | Guidance | Guidance | Explain when runtime audit records, checklist outputs, and accepted git history each become evidence for review, without treating any as approval by itself. | The record-audit lens finds strong boundary statements, but the rationale connecting runtime audit records, checklist artifacts, and immutable acceptance evidence is scattered across Guidance and Procedure. | Guidance.md; Procedure.md | Guidance.md#principles; Guidance.md#considerations; Procedure.md#records |  | PROPOSAL | TBD |
