# Semantic Lensing Register: DEL-07-06 Reference Hash and Snapshot Conventions

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py completed after generation
**Warnings:** REF-006 remains HASH_MISMATCH in _REFERENCES.md; production documents preserve it as source-state warning

**Inputs Read:**
- _CONTEXT.md - `_CONTEXT.md#Identity`
- _STATUS.md - `_STATUS.md#History`
- _SEMANTIC.md - `_SEMANTIC.md`
- Datasheet.md - `Datasheet.md#Attributes`
- Specification.md - `Specification.md#Requirements`
- Guidance.md - `Guidance.md#Principles`
- Procedure.md - `Procedure.md#Steps`
- _REFERENCES.md - `_REFERENCES.md#Authoritative Source Corpus` metadata only; external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 9
- By document:
  - Datasheet: 1
  - Specification: 2
  - Guidance: 1
  - Procedure: 3
  - Multi: 2
  - NA: 0
- By matrix:
  - A: 2
  - B: 2
  - C: 1
  - F: 1
  - D: 1
  - X: 1
  - E: 1
- By type:
  - Conflict: 3
  - VerificationGap: 3
  - MissingSlot: 0
  - WeakStatement: 0
  - RationaleGap: 0
  - Normalization: 0
  - TBD_Question: 3
  - MatrixError: 0
- Notable conflicts: 3
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction lens found aligned local coverage for normative/guiding without a separate register item. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice lens found aligned local coverage for normative/applying without a separate register item. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination lens found aligned local coverage for normative/judging without a separate register item. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | regulatory audit lens exposes 1 evidence-linked item(s) for normative/reviewing review. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction lens found aligned local coverage for operative/guiding without a separate register item. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution lens found aligned local coverage for operative/applying without a separate register item. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment lens found aligned local coverage for operative/judging without a separate register item. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit lens found aligned local coverage for operative/reviewing without a separate register item. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation lens found aligned local coverage for evaluative/guiding without a separate register item. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application lens found aligned local coverage for evaluative/applying without a separate register item. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 1 | HAS_ITEMS | worth determination lens exposes 1 evidence-linked item(s) for evaluative/judging review. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal lens found aligned local coverage for evaluative/reviewing without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Resolve whether REF-006 PRD text remains warning-qualified or is accepted after hash reconciliation. | Guidance records SOURCE-WARN-001 because PRD is accessible and used for vNext direction while _REFERENCES.md reports HASH_MISMATCH. | Guidance.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus | Guidance.md#SOURCE-WARN-001; _REFERENCES.md#REF-006 | PROPOSAL | TBD |
| A-002 | A:[evaluative]:[judging] | TBD_Question | Datasheet | TBD | Assign ResponsibleParty for DEL-07-06 or explicitly retain unassigned ownership for the next phase. | Datasheet and _CONTEXT both preserve ResponsibleParty as TBD, so ownership-dependent review or closure cannot be judged from current files. | Datasheet.md; _CONTEXT.md | Datasheet.md#Identification; _CONTEXT.md#Identity |  | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact lens found aligned local coverage for data/necessity without a separate register item. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens found aligned local coverage for data/sufficiency without a separate register item. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record lens found aligned local coverage for data/completeness without a separate register item. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | reliable measurement lens exposes 1 evidence-linked item(s) for data/consistency review. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens found aligned local coverage for information/necessity without a separate register item. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens found aligned local coverage for information/sufficiency without a separate register item. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account lens found aligned local coverage for information/completeness without a separate register item. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message lens found aligned local coverage for information/consistency without a separate register item. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens found aligned local coverage for knowledge/necessity without a separate register item. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens found aligned local coverage for knowledge/sufficiency without a separate register item. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 1 | HAS_ITEMS | thorough mastery lens exposes 1 evidence-linked item(s) for knowledge/completeness review. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding lens found aligned local coverage for knowledge/consistency without a separate register item. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens found aligned local coverage for wisdom/necessity without a separate register item. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens found aligned local coverage for wisdom/sufficiency without a separate register item. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens found aligned local coverage for wisdom/completeness without a separate register item. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens found aligned local coverage for wisdom/consistency without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | Conflict | Multi | NA | Determine accepted handling for docs/PRD.md HASH_MISMATCH before treating PRD-derived statements as closure-ready. | The reference table records mismatched expected and actual SHA values while production documents continue to cite PRD-derived requirements with a warning. | _REFERENCES.md; Specification.md; Guidance.md | _REFERENCES.md#Authoritative Source Corpus; Specification.md#Requirements; Guidance.md#Considerations | _REFERENCES.md#REF-006; Specification.md#DEL-07-06-REQ-014; Guidance.md#PRD source warning | PROPOSAL | TBD |
| B-002 | B:[knowledge]:[completeness] | TBD_Question | Specification | Specification | Provide exact deterministic tool and script registry evidence when verified by the owning implementation slice. | Specification REQ-013 and Datasheet construction keep exact registry membership TBD, leaving completeness of tool continuity knowledge unresolved. | Specification.md; Datasheet.md; Guidance.md | Specification.md#Documentation; Datasheet.md#Construction; Guidance.md#Considerations |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding basis | 0 | NO_ITEMS | binding basis lens found aligned local coverage for normative/necessity without a separate register item. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequacy threshold | 1 | HAS_ITEMS | adequacy threshold lens exposes 1 evidence-linked item(s) for normative/sufficiency review. |
| C:[normative]:[completeness] | normative | completeness | coverage standard | 0 | NO_ITEMS | coverage standard lens found aligned local coverage for normative/completeness without a separate register item. |
| C:[normative]:[consistency] | normative | consistency | coherence rule | 0 | NO_ITEMS | coherence rule lens found aligned local coverage for normative/consistency without a separate register item. |
| C:[operative]:[necessity] | operative | necessity | execution prerequisite | 0 | NO_ITEMS | execution prerequisite lens found aligned local coverage for operative/necessity without a separate register item. |
| C:[operative]:[sufficiency] | operative | sufficiency | evidence practice | 0 | NO_ITEMS | evidence practice lens found aligned local coverage for operative/sufficiency without a separate register item. |
| C:[operative]:[completeness] | operative | completeness | record discipline | 0 | NO_ITEMS | record discipline lens found aligned local coverage for operative/completeness without a separate register item. |
| C:[operative]:[consistency] | operative | consistency | measurement control | 0 | NO_ITEMS | measurement control lens found aligned local coverage for operative/consistency without a separate register item. |
| C:[evaluative]:[necessity] | evaluative | necessity | discernment basis | 0 | NO_ITEMS | discernment basis lens found aligned local coverage for evaluative/necessity without a separate register item. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment warrant | 0 | NO_ITEMS | judgment warrant lens found aligned local coverage for evaluative/sufficiency without a separate register item. |
| C:[evaluative]:[completeness] | evaluative | completeness | insight standard | 0 | NO_ITEMS | insight standard lens found aligned local coverage for evaluative/completeness without a separate register item. |
| C:[evaluative]:[consistency] | evaluative | consistency | reasoned appraisal | 0 | NO_ITEMS | reasoned appraisal lens found aligned local coverage for evaluative/consistency without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Add or retain a check that PRD-derived requirements visibly carry the REF-006 warning until reconciliation or acceptance. | Specification includes REQ-014 and a verification row for the warning; this lens flags it as an adequacy threshold that must survive later enrichment. | Specification.md | Specification.md#Requirements; Specification.md#Verification |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | authority prerequisite | 0 | NO_ITEMS | authority prerequisite lens found aligned local coverage for normative/necessity without a separate register item. |
| F:[normative]:[sufficiency] | normative | sufficiency | evidence warrant | 0 | NO_ITEMS | evidence warrant lens found aligned local coverage for normative/sufficiency without a separate register item. |
| F:[normative]:[completeness] | normative | completeness | closure basis | 0 | NO_ITEMS | closure basis lens found aligned local coverage for normative/completeness without a separate register item. |
| F:[normative]:[consistency] | normative | consistency | alignment discipline | 0 | NO_ITEMS | alignment discipline lens found aligned local coverage for normative/consistency without a separate register item. |
| F:[operative]:[necessity] | operative | necessity | work precondition | 0 | NO_ITEMS | work precondition lens found aligned local coverage for operative/necessity without a separate register item. |
| F:[operative]:[sufficiency] | operative | sufficiency | context warrant | 0 | NO_ITEMS | context warrant lens found aligned local coverage for operative/sufficiency without a separate register item. |
| F:[operative]:[completeness] | operative | completeness | trace coverage | 1 | HAS_ITEMS | trace coverage lens exposes 1 evidence-linked item(s) for operative/completeness review. |
| F:[operative]:[consistency] | operative | consistency | coherence practice | 0 | NO_ITEMS | coherence practice lens found aligned local coverage for operative/consistency without a separate register item. |
| F:[evaluative]:[necessity] | evaluative | necessity | ruling basis | 0 | NO_ITEMS | ruling basis lens found aligned local coverage for evaluative/necessity without a separate register item. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment threshold | 0 | NO_ITEMS | judgment threshold lens found aligned local coverage for evaluative/sufficiency without a separate register item. |
| F:[evaluative]:[completeness] | evaluative | completeness | integrity review | 0 | NO_ITEMS | integrity review lens found aligned local coverage for evaluative/completeness without a separate register item. |
| F:[evaluative]:[consistency] | evaluative | consistency | reasoning discipline | 0 | NO_ITEMS | reasoning discipline lens found aligned local coverage for evaluative/consistency without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[completeness] | TBD_Question | Procedure | Procedure | Identify the accepted dependency edge record source or retain dependency availability as TBD for this deliverable. | Procedure prerequisites say accepted dependency edges are TBD and cite _DEPENDENCIES.md, so trace coverage is incomplete until a dependency run or human ruling closes it. | Procedure.md | Procedure.md#Prerequisites |  | PROPOSAL | TBD |

## Matrix D - Method

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governing direction | 0 | NO_ITEMS | governing direction lens found aligned local coverage for normative/guiding without a separate register item. |
| D:[normative]:[applying] | normative | applying | binding practice | 0 | NO_ITEMS | binding practice lens found aligned local coverage for normative/applying without a separate register item. |
| D:[normative]:[judging] | normative | judging | closure determination | 1 | HAS_ITEMS | closure determination lens exposes 1 evidence-linked item(s) for normative/judging review. |
| D:[normative]:[reviewing] | normative | reviewing | audit discipline | 0 | NO_ITEMS | audit discipline lens found aligned local coverage for normative/reviewing without a separate register item. |
| D:[operative]:[guiding] | operative | guiding | execution direction | 0 | NO_ITEMS | execution direction lens found aligned local coverage for operative/guiding without a separate register item. |
| D:[operative]:[applying] | operative | applying | controlled performance | 0 | NO_ITEMS | controlled performance lens found aligned local coverage for operative/applying without a separate register item. |
| D:[operative]:[judging] | operative | judging | assessment closure | 0 | NO_ITEMS | assessment closure lens found aligned local coverage for operative/judging without a separate register item. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance | 0 | NO_ITEMS | process assurance lens found aligned local coverage for operative/reviewing without a separate register item. |
| D:[evaluative]:[guiding] | evaluative | guiding | value rationale | 0 | NO_ITEMS | value rationale lens found aligned local coverage for evaluative/guiding without a separate register item. |
| D:[evaluative]:[applying] | evaluative | applying | merit standard | 0 | NO_ITEMS | merit standard lens found aligned local coverage for evaluative/applying without a separate register item. |
| D:[evaluative]:[judging] | evaluative | judging | worth closure | 0 | NO_ITEMS | worth closure lens found aligned local coverage for evaluative/judging without a separate register item. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality judgment | 0 | NO_ITEMS | quality judgment lens found aligned local coverage for evaluative/reviewing without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[normative]:[judging] | VerificationGap | Procedure | Procedure | Confirm closure review checks approval SHA evidence before any CHECKING or ISSUED transition. | Specification REQ-011 requires approval SHA evidence, while Procedure verification describes content checks but does not itself execute or record a lifecycle transition approval. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Verification |  | PROPOSAL | TBD |

## Matrix X - Review

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | directive warrant | 0 | NO_ITEMS | directive warrant lens found aligned local coverage for guiding/necessity without a separate register item. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | grounded threshold | 0 | NO_ITEMS | grounded threshold lens found aligned local coverage for guiding/sufficiency without a separate register item. |
| X:[guiding]:[completeness] | guiding | completeness | coverage rationale | 0 | NO_ITEMS | coverage rationale lens found aligned local coverage for guiding/completeness without a separate register item. |
| X:[guiding]:[consistency] | guiding | consistency | coherent direction | 0 | NO_ITEMS | coherent direction lens found aligned local coverage for guiding/consistency without a separate register item. |
| X:[applying]:[necessity] | applying | necessity | practice prerequisite | 0 | NO_ITEMS | practice prerequisite lens found aligned local coverage for applying/necessity without a separate register item. |
| X:[applying]:[sufficiency] | applying | sufficiency | implementation warrant | 0 | NO_ITEMS | implementation warrant lens found aligned local coverage for applying/sufficiency without a separate register item. |
| X:[applying]:[completeness] | applying | completeness | complete practice | 0 | NO_ITEMS | complete practice lens found aligned local coverage for applying/completeness without a separate register item. |
| X:[applying]:[consistency] | applying | consistency | coherent application | 0 | NO_ITEMS | coherent application lens found aligned local coverage for applying/consistency without a separate register item. |
| X:[judging]:[necessity] | judging | necessity | decision basis | 0 | NO_ITEMS | decision basis lens found aligned local coverage for judging/necessity without a separate register item. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate assessment | 0 | NO_ITEMS | adequate assessment lens found aligned local coverage for judging/sufficiency without a separate register item. |
| X:[judging]:[completeness] | judging | completeness | closure finding | 0 | NO_ITEMS | closure finding lens found aligned local coverage for judging/completeness without a separate register item. |
| X:[judging]:[consistency] | judging | consistency | consistent appraisal | 0 | NO_ITEMS | consistent appraisal lens found aligned local coverage for judging/consistency without a separate register item. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit trigger | 0 | NO_ITEMS | audit trigger lens found aligned local coverage for reviewing/necessity without a separate register item. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | evidence threshold | 1 | HAS_ITEMS | evidence threshold lens exposes 1 evidence-linked item(s) for reviewing/sufficiency review. |
| X:[reviewing]:[completeness] | reviewing | completeness | review coverage | 0 | NO_ITEMS | review coverage lens found aligned local coverage for reviewing/completeness without a separate register item. |
| X:[reviewing]:[consistency] | reviewing | consistency | assurance coherence | 0 | NO_ITEMS | assurance coherence lens found aligned local coverage for reviewing/consistency without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[sufficiency] | VerificationGap | Procedure | Procedure | For hash bypass review, require evidence that human approval and a durable bypass record exist when a bypass is used. | Procedure Step 4 names the bypass convention, but any concrete bypass instance still needs evidence before review can pass. | Procedure.md; Specification.md | Procedure.md#Steps; Specification.md#Requirements |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual warrant | 0 | NO_ITEMS | factual warrant lens found aligned local coverage for guiding/data without a separate register item. |
| E:[guiding]:[information] | guiding | information | signal rationale | 0 | NO_ITEMS | signal rationale lens found aligned local coverage for guiding/information without a separate register item. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding frame | 0 | NO_ITEMS | understanding frame lens found aligned local coverage for guiding/knowledge without a separate register item. |
| E:[guiding]:[wisdom] | guiding | wisdom | discernment guide | 0 | NO_ITEMS | discernment guide lens found aligned local coverage for guiding/wisdom without a separate register item. |
| E:[applying]:[data] | applying | data | fact practice | 0 | NO_ITEMS | fact practice lens found aligned local coverage for applying/data without a separate register item. |
| E:[applying]:[information] | applying | information | context enactment | 0 | NO_ITEMS | context enactment lens found aligned local coverage for applying/information without a separate register item. |
| E:[applying]:[knowledge] | applying | knowledge | expertise method | 0 | NO_ITEMS | expertise method lens found aligned local coverage for applying/knowledge without a separate register item. |
| E:[applying]:[wisdom] | applying | wisdom | judgment practice | 0 | NO_ITEMS | judgment practice lens found aligned local coverage for applying/wisdom without a separate register item. |
| E:[judging]:[data] | judging | data | evidence decision | 0 | NO_ITEMS | evidence decision lens found aligned local coverage for judging/data without a separate register item. |
| E:[judging]:[information] | judging | information | message assessment | 0 | NO_ITEMS | message assessment lens found aligned local coverage for judging/information without a separate register item. |
| E:[judging]:[knowledge] | judging | knowledge | mastery appraisal | 0 | NO_ITEMS | mastery appraisal lens found aligned local coverage for judging/knowledge without a separate register item. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned finding | 0 | NO_ITEMS | reasoned finding lens found aligned local coverage for judging/wisdom without a separate register item. |
| E:[reviewing]:[data] | reviewing | data | record audit | 0 | NO_ITEMS | record audit lens found aligned local coverage for reviewing/data without a separate register item. |
| E:[reviewing]:[information] | reviewing | information | account review | 1 | HAS_ITEMS | account review lens exposes 1 evidence-linked item(s) for reviewing/information review. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery assurance | 0 | NO_ITEMS | mastery assurance lens found aligned local coverage for reviewing/knowledge without a separate register item. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled appraisal | 0 | NO_ITEMS | principled appraisal lens found aligned local coverage for reviewing/wisdom without a separate register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[information] | Conflict | Guidance | NA | Keep SOURCE-WARN-001 open until the PRD hash mismatch is reconciled or explicitly accepted. | The account-review lens surfaces the same unresolved source-state conflict recorded in the human-ruling table. | Guidance.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus | Guidance.md#SOURCE-WARN-001; _REFERENCES.md#REF-006 | PROPOSAL | TBD |
