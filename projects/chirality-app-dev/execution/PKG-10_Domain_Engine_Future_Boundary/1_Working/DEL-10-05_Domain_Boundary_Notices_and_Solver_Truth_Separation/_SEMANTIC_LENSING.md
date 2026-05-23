# Semantic Lensing Register: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation`
**Warnings:** PRD source hash mismatch remains a source-warning conflict; no production documents were edited.

**Inputs Read:**
- _CONTEXT.md - _CONTEXT.md#Context
- _STATUS.md - _STATUS.md#Status
- _SEMANTIC.md - _SEMANTIC.md#Semantic Lens
- Datasheet.md - Datasheet.md#Datasheet
- Specification.md - Specification.md#Specification
- Guidance.md - Guidance.md#Guidance
- Procedure.md - Procedure.md#Procedure
- _REFERENCES.md - _REFERENCES.md#References metadata only; external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 14
- By document:
  - Datasheet: 0
  - Specification: 3
  - Guidance: 4
  - Procedure: 3
  - Multi: 4
  - NA: 0
- By matrix:
  - A: 2
  - B: 2
  - C: 2
  - F: 2
  - D: 2
  - X: 2
  - E: 2
- By type:
  - Conflict: 3
  - VerificationGap: 2
  - MissingSlot: 4
  - WeakStatement: 0
  - RationaleGap: 0
  - Normalization: 1
  - TBD_Question: 4
  - MatrixError: 0
- Notable conflicts: 3
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction lens maps to the normative/guiding role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice lens maps to the normative/applying role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[normative]:[judging] | normative | judging | compliance determination | 1 | HAS_ITEMS | compliance determination lens surfaces 1 warranted register item(s) tied to normative/judging evidence. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit lens maps to the normative/reviewing role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction lens maps to the operative/guiding role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution lens maps to the operative/applying role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment lens maps to the operative/judging role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit lens maps to the operative/reviewing role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation lens maps to the evaluative/guiding role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application lens maps to the evaluative/applying role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 1 | HAS_ITEMS | worth determination lens surfaces 1 warranted register item(s) tied to evaluative/judging evidence. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal lens maps to the evaluative/reviewing role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[judging] | Conflict | Multi | NA | Keep PRD hash mismatch visible as a source-warning conflict until reconciled. | Compliance-determination language depends partly on PRD requirements, and the deliverable records a PRD expected/actual hash mismatch while using the accessible PRD under dispatch instruction. | _REFERENCES.md; Guidance.md | _REFERENCES.md#Authoritative Source Corpus; Guidance.md#Conflict Table (for human ruling) | _REFERENCES.md#Authoritative Source Corpus; Guidance.md#Conflict Table (for human ruling) | PROPOSAL | TBD |
| A-002 | A:[evaluative]:[judging] | TBD_Question | Guidance | Guidance | Should the standard and compact boundary notices be accepted wording or remain proposal copy? | The guidance explicitly lists acceptance of the notice wording as a human ruling needed, so worth determination cannot be closed by TASK. | Guidance.md | Guidance.md#Human Rulings Needed |  | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact lens maps to the data/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens maps to the data/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record lens maps to the data/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement lens maps to the data/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens maps to the information/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens maps to the information/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account lens maps to the information/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[information]:[consistency] | information | consistency | coherent message | 1 | HAS_ITEMS | coherent message lens surfaces 1 warranted register item(s) tied to information/consistency evidence. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens maps to the knowledge/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens maps to the knowledge/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 1 | HAS_ITEMS | thorough mastery lens surfaces 1 warranted register item(s) tied to knowledge/completeness evidence. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding lens maps to the knowledge/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens maps to the wisdom/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens maps to the wisdom/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens maps to the wisdom/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens maps to the wisdom/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[information]:[consistency] | Normalization | Multi | Guidance | Qualify validate/validation wording as deterministic format, manifest, operation-precondition, or profile-rule checks when not discussing prohibited professional validation. | The kit prohibits claims that Chirality validates professional work while also allowing deterministic adapters to validate bounded technical artifacts, creating a terminology risk if copied without qualifiers. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Guidance.md#Trade-offs; Procedure.md#Verification | Specification.md#Requirements; Guidance.md#Trade-offs; Procedure.md#Verification | PROPOSAL | TBD |
| B-002 | B:[knowledge]:[completeness] | TBD_Question | Specification | Specification | What accepted generic DomainEngineProfile fields and copy locations should be cited after DEL-10-01 is accepted? | The specification marks the accepted generic profile specification as TBD and guidance warns not to invent profile fields beyond source-backed examples. | Specification.md; Guidance.md | Specification.md#Standards; Guidance.md#Considerations; Guidance.md#Human Rulings Needed |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | boundary warrant | 0 | NO_ITEMS | boundary warrant lens maps to the normative/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[normative]:[sufficiency] | normative | sufficiency | notice threshold | 0 | NO_ITEMS | notice threshold lens maps to the normative/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[normative]:[completeness] | normative | completeness | coverage discipline | 0 | NO_ITEMS | coverage discipline lens maps to the normative/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[normative]:[consistency] | normative | consistency | claim coherence | 0 | NO_ITEMS | claim coherence lens maps to the normative/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[operative]:[necessity] | operative | necessity | review prerequisite | 0 | NO_ITEMS | review prerequisite lens maps to the operative/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[operative]:[sufficiency] | operative | sufficiency | proposal evidence | 0 | NO_ITEMS | proposal evidence lens maps to the operative/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[operative]:[completeness] | operative | completeness | record discipline | 1 | HAS_ITEMS | record discipline lens surfaces 1 warranted register item(s) tied to operative/completeness evidence. |
| C:[operative]:[consistency] | operative | consistency | separation control | 0 | NO_ITEMS | separation control lens maps to the operative/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[evaluative]:[necessity] | evaluative | necessity | reliance discernment | 0 | NO_ITEMS | reliance discernment lens maps to the evaluative/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | acceptance judgment | 1 | HAS_ITEMS | acceptance judgment lens surfaces 1 warranted register item(s) tied to evaluative/sufficiency evidence. |
| C:[evaluative]:[completeness] | evaluative | completeness | boundary integrity | 0 | NO_ITEMS | boundary integrity lens maps to the evaluative/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| C:[evaluative]:[consistency] | evaluative | consistency | reasoned restraint | 0 | NO_ITEMS | reasoned restraint lens maps to the evaluative/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[completeness] | MissingSlot | Procedure | Procedure | Add a concrete review-output record template or reference for checklist result, reviewed surface, reviewer, date, pass/fail, and human-ruling carryforward. | The procedure instructs reviewers to record outcomes, but the production kit does not define the durable record shape for that outcome. | Procedure.md; Guidance.md | Procedure.md#Records; Guidance.md#Domain Review Checklist |  | PROPOSAL | TBD |
| C-002 | C:[evaluative]:[sufficiency] | TBD_Question | Guidance | Guidance | Who can accept proposed notice copy as sufficient for future UI, documentation, and event-record surfaces? | Acceptance judgment for notice copy is explicitly deferred to a human ruling; the current text provides proposal-quality copy but not an acceptance decision. | Guidance.md | Guidance.md#Boundary Notice Copy; Guidance.md#Human Rulings Needed |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | authority prerequisite | 1 | HAS_ITEMS | authority prerequisite lens surfaces 1 warranted register item(s) tied to normative/necessity evidence. |
| F:[normative]:[sufficiency] | normative | sufficiency | nonapproval warrant | 0 | NO_ITEMS | nonapproval warrant lens maps to the normative/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[normative]:[completeness] | normative | completeness | closure boundary | 0 | NO_ITEMS | closure boundary lens maps to the normative/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[normative]:[consistency] | normative | consistency | wording discipline | 0 | NO_ITEMS | wording discipline lens maps to the normative/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[operative]:[necessity] | operative | necessity | surface precondition | 0 | NO_ITEMS | surface precondition lens maps to the operative/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[operative]:[sufficiency] | operative | sufficiency | review warrant | 0 | NO_ITEMS | review warrant lens maps to the operative/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[operative]:[completeness] | operative | completeness | trace coverage | 1 | HAS_ITEMS | trace coverage lens surfaces 1 warranted register item(s) tied to operative/completeness evidence. |
| F:[operative]:[consistency] | operative | consistency | proposal control | 0 | NO_ITEMS | proposal control lens maps to the operative/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[evaluative]:[necessity] | evaluative | necessity | ruling basis | 0 | NO_ITEMS | ruling basis lens maps to the evaluative/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | acceptance threshold | 0 | NO_ITEMS | acceptance threshold lens maps to the evaluative/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[evaluative]:[completeness] | evaluative | completeness | integrity review | 0 | NO_ITEMS | integrity review lens maps to the evaluative/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| F:[evaluative]:[consistency] | evaluative | consistency | restraint discipline | 0 | NO_ITEMS | restraint discipline lens maps to the evaluative/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[necessity] | VerificationGap | Specification | Specification | Before closure, verify each selected future surface category has a required notice pattern or an explicit out-of-scope rationale. | REQ-001 through REQ-007 define mandatory notice and review behavior, but this package does not include an inventory of concrete future surfaces selected for verification. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Steps |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[completeness] | MissingSlot | Guidance | Guidance | Add a completed-checklist capture location or example so trace coverage can distinguish checklist definition from checklist execution. | The guidance defines the domain review checklist, while the procedure says to record pass/fail; no production document shows where a completed checklist is captured. | Guidance.md; Procedure.md | Guidance.md#Domain Review Checklist; Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | notice authority | 0 | NO_ITEMS | notice authority lens maps to the normative/guiding role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[normative]:[applying] | normative | applying | boundary practice | 0 | NO_ITEMS | boundary practice lens maps to the normative/applying role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[normative]:[judging] | normative | judging | claim closure | 0 | NO_ITEMS | claim closure lens maps to the normative/judging role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[normative]:[reviewing] | normative | reviewing | notice audit | 0 | NO_ITEMS | notice audit lens maps to the normative/reviewing role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[operative]:[guiding] | operative | guiding | review method | 0 | NO_ITEMS | review method lens maps to the operative/guiding role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[operative]:[applying] | operative | applying | proposal practice | 0 | NO_ITEMS | proposal practice lens maps to the operative/applying role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[operative]:[judging] | operative | judging | review closure | 1 | HAS_ITEMS | review closure lens surfaces 1 warranted register item(s) tied to operative/judging evidence. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance | 0 | NO_ITEMS | process assurance lens maps to the operative/reviewing role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[evaluative]:[guiding] | evaluative | guiding | reliance orientation | 0 | NO_ITEMS | reliance orientation lens maps to the evaluative/guiding role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[evaluative]:[applying] | evaluative | applying | acceptance practice | 1 | HAS_ITEMS | acceptance practice lens surfaces 1 warranted register item(s) tied to evaluative/applying evidence. |
| D:[evaluative]:[judging] | evaluative | judging | boundary judgment | 0 | NO_ITEMS | boundary judgment lens maps to the evaluative/judging role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality restraint | 0 | NO_ITEMS | quality restraint lens maps to the evaluative/reviewing role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[judging] | MissingSlot | Procedure | Procedure | Specify minimum evidence for a review-closure decision, including source warning status and unresolved human-ruling items. | The procedure has verification checks and records, but it does not define closure evidence needed to judge a reviewed notice package complete. | Procedure.md; Guidance.md | Procedure.md#Verification; Procedure.md#Records; Guidance.md#Human Rulings Needed |  | PROPOSAL | TBD |
| D-002 | D:[evaluative]:[applying] | TBD_Question | Guidance | Guidance | What engine-specific wording should replace fixture-level placeholders if OpenPipeStress or another engine is adopted by amendment? | Guidance keeps OpenPipeStress fixture-only and names engine-specific wording as a future human ruling, so acceptance practice cannot be finalized here. | Guidance.md; Specification.md | Guidance.md#Fixture Notice; Guidance.md#Human Rulings Needed; Specification.md#Requirements |  | PROPOSAL | TBD |

## Matrix X - Acceptance

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | notice warrant | 0 | NO_ITEMS | notice warrant lens maps to the guiding/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | grounded threshold | 0 | NO_ITEMS | grounded threshold lens maps to the guiding/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[guiding]:[completeness] | guiding | completeness | coverage rationale | 0 | NO_ITEMS | coverage rationale lens maps to the guiding/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[guiding]:[consistency] | guiding | consistency | coherent direction | 0 | NO_ITEMS | coherent direction lens maps to the guiding/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[applying]:[necessity] | applying | necessity | proposal prerequisite | 1 | HAS_ITEMS | proposal prerequisite lens surfaces 1 warranted register item(s) tied to applying/necessity evidence. |
| X:[applying]:[sufficiency] | applying | sufficiency | practice warrant | 0 | NO_ITEMS | practice warrant lens maps to the applying/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[applying]:[completeness] | applying | completeness | complete practice | 0 | NO_ITEMS | complete practice lens maps to the applying/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[applying]:[consistency] | applying | consistency | coherent application | 0 | NO_ITEMS | coherent application lens maps to the applying/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[judging]:[necessity] | judging | necessity | claim basis | 0 | NO_ITEMS | claim basis lens maps to the judging/necessity role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate assessment | 0 | NO_ITEMS | adequate assessment lens maps to the judging/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[judging]:[completeness] | judging | completeness | closure finding | 0 | NO_ITEMS | closure finding lens maps to the judging/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[judging]:[consistency] | judging | consistency | consistent appraisal | 0 | NO_ITEMS | consistent appraisal lens maps to the judging/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit trigger | 1 | HAS_ITEMS | audit trigger lens surfaces 1 warranted register item(s) tied to reviewing/necessity evidence. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | evidence threshold | 0 | NO_ITEMS | evidence threshold lens maps to the reviewing/sufficiency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[reviewing]:[completeness] | reviewing | completeness | review coverage | 0 | NO_ITEMS | review coverage lens maps to the reviewing/completeness role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| X:[reviewing]:[consistency] | reviewing | consistency | assurance coherence | 0 | NO_ITEMS | assurance coherence lens maps to the reviewing/consistency role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[necessity] | Conflict | Multi | NA | Treat the PRD hash mismatch as an audit trigger that remains open until source reconciliation closes it. | The production documents rely on PRD FR-106 through FR-115 while also recording a HASH_MISMATCH for PRD in the reference table. | _REFERENCES.md; Datasheet.md; Procedure.md | _REFERENCES.md#Authoritative Source Corpus; Datasheet.md#Conditions; Procedure.md#Prerequisites | _REFERENCES.md#Authoritative Source Corpus; Procedure.md#Prerequisites | PROPOSAL | TBD |
| X-002 | X:[applying]:[necessity] | VerificationGap | Specification | Specification | Verify whether OperationProposal record fields are defined in an accepted upstream artifact before using operation-proposal notice examples as closure evidence. | The specification requires human acceptance for domain operation copy, but current package language stays at notice/checklist level and does not cite an accepted OperationProposal schema. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Guidance.md#Operation Proposal Notice; Procedure.md#Steps |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual warrant | 0 | NO_ITEMS | factual warrant lens maps to the guiding/data role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[guiding]:[information] | guiding | information | signal rationale | 0 | NO_ITEMS | signal rationale lens maps to the guiding/information role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding frame | 0 | NO_ITEMS | understanding frame lens maps to the guiding/knowledge role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[guiding]:[wisdom] | guiding | wisdom | discernment guide | 0 | NO_ITEMS | discernment guide lens maps to the guiding/wisdom role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[applying]:[data] | applying | data | fact practice | 0 | NO_ITEMS | fact practice lens maps to the applying/data role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[applying]:[information] | applying | information | context enactment | 0 | NO_ITEMS | context enactment lens maps to the applying/information role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[applying]:[knowledge] | applying | knowledge | expertise method | 0 | NO_ITEMS | expertise method lens maps to the applying/knowledge role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[applying]:[wisdom] | applying | wisdom | judgment practice | 0 | NO_ITEMS | judgment practice lens maps to the applying/wisdom role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[judging]:[data] | judging | data | evidence decision | 1 | HAS_ITEMS | evidence decision lens surfaces 1 warranted register item(s) tied to judging/data evidence. |
| E:[judging]:[information] | judging | information | message assessment | 0 | NO_ITEMS | message assessment lens maps to the judging/information role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[judging]:[knowledge] | judging | knowledge | mastery appraisal | 0 | NO_ITEMS | mastery appraisal lens maps to the judging/knowledge role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned finding | 0 | NO_ITEMS | reasoned finding lens maps to the judging/wisdom role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[reviewing]:[data] | reviewing | data | record audit | 0 | NO_ITEMS | record audit lens maps to the reviewing/data role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[reviewing]:[information] | reviewing | information | account review | 1 | HAS_ITEMS | account review lens surfaces 1 warranted register item(s) tied to reviewing/information evidence. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery assurance | 0 | NO_ITEMS | mastery assurance lens maps to the reviewing/knowledge role in current notices, checklist, examples, or future-scope cautions without another grounded item. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled appraisal | 0 | NO_ITEMS | principled appraisal lens maps to the reviewing/wisdom role in current notices, checklist, examples, or future-scope cautions without another grounded item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[judging]:[data] | Conflict | Multi | NA | Do not use PRD-derived requirement evidence as unqualified closure proof until the hash warning is resolved or formally waived. | Evidence decisions for this package cite PRD requirements, and the references ledger records a PRD HASH_MISMATCH that remains unresolved. | _REFERENCES.md; Specification.md; Guidance.md | _REFERENCES.md#Authoritative Source Corpus; Specification.md#Documentation; Guidance.md#Conflict Table (for human ruling) | _REFERENCES.md#Authoritative Source Corpus; Guidance.md#Conflict Table (for human ruling) | PROPOSAL | TBD |
| E-002 | E:[reviewing]:[information] | MissingSlot | Procedure | Procedure | Add owner or resolution-path fields for maintaining the PRD source-warning note until reconciled. | The procedure records that the source-warning note must persist, but it does not identify who owns reconciliation or what evidence closes the warning. | Procedure.md; Guidance.md | Procedure.md#Records; Guidance.md#Conflict Table (for human ruling) |  | PROPOSAL | TBD |
