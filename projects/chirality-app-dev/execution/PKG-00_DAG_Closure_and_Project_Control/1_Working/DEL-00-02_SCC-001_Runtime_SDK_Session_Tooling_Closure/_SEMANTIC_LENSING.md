# Semantic Lensing Register: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

**Generated:** 2026-05-24
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — validate_lens_register.py and validate_semantic_pipeline_scope.py --step lens passed
**Warnings:** none

**Inputs Read:**
- _CONTEXT.md — _CONTEXT.md
- _STATUS.md — _STATUS.md
- _SEMANTIC.md — _SEMANTIC.md
- Datasheet.md — Datasheet.md
- Specification.md — Specification.md
- Guidance.md — Guidance.md
- Procedure.md — Procedure.md
- _REFERENCES.md — _REFERENCES.md

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 9
- By document:
  - Datasheet: 1
  - Specification: 3
  - Guidance: 0
  - Procedure: 3
  - Multi: 2
  - NA: 0
- By matrix:
  - A: 1
  - B: 1
  - C: 1
  - F: 2
  - D: 1
  - X: 1
  - E: 2
- By type:
  - Conflict: 1
  - VerificationGap: 3
  - MissingSlot: 3
  - WeakStatement: 0
  - RationaleGap: 0
  - Normalization: 1
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Prescriptive direction is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 1 | HAS_ITEMS | Warranted item records the mandatory practice lens against deliverable-local evidence. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Compliance determination is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | Regulatory audit is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Procedural direction is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Practical execution is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Performance assessment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Process audit is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Value orientation is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Merit application is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Worth determination is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Quality appraisal is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[applying] | MissingSlot | Datasheet | Datasheet | Assign ResponsibleParty or identify the owning human/agent for SCC-001 rulings. | The identification table leaves ResponsibleParty as TBD, so the governed practice lens exposes an ownership slot needed before row decisions can be accepted. | Datasheet.md | Identification |  | PROPOSAL | TBD |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | Essential fact is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Adequate evidence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | Warranted item records the comprehensive record lens against deliverable-local evidence. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | Reliable measurement is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Essential signal is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | Adequate context is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | Comprehensive account is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | Coherent message is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Fundamental understanding is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Competent expertise is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Thorough mastery is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Coherent understanding is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Essential discernment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Adequate judgment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Holistic insight is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Principled reasoning is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[completeness] | VerificationGap | Specification | Specification | Add a verification check that the focused workbook includes all 12 SCC-001 bidirectional pairs and excludes the SCC-002 pair. | The procedure states the selection rule and Guidance quantifies 12 SCC-001 pairs, but Specification verification only says pairs are drawn from the evidence file and does not capture the expected count/exclusion. | Specification.md; Guidance.md; Procedure.md | Specification#Verification; Guidance#Considerations; Procedure#Steps |  | PROPOSAL | TBD |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | control mandate | 0 | NO_ITEMS | Control mandate is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[normative]:[sufficiency] | normative | sufficiency | evidence threshold | 0 | NO_ITEMS | Evidence threshold is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[normative]:[completeness] | normative | completeness | authority record | 0 | NO_ITEMS | Authority record is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[normative]:[consistency] | normative | consistency | boundary coherence | 1 | HAS_ITEMS | Warranted item records the boundary coherence lens against deliverable-local evidence. |
| C:[operative]:[necessity] | operative | necessity | workflow prerequisite | 0 | NO_ITEMS | Workflow prerequisite is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[operative]:[sufficiency] | operative | sufficiency | execution proof | 0 | NO_ITEMS | Execution proof is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[operative]:[completeness] | operative | completeness | procedure record | 0 | NO_ITEMS | Procedure record is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[operative]:[consistency] | operative | consistency | process alignment | 0 | NO_ITEMS | Process alignment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[evaluative]:[necessity] | evaluative | necessity | ruling criterion | 0 | NO_ITEMS | Ruling criterion is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment basis | 0 | NO_ITEMS | Judgment basis is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[evaluative]:[completeness] | evaluative | completeness | review coverage | 0 | NO_ITEMS | Review coverage is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| C:[evaluative]:[consistency] | evaluative | consistency | assessment coherence | 0 | NO_ITEMS | Assessment coherence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[consistency] | Conflict | Multi | TBD | Resolve lifecycle/status presentation before downstream handoff. | Guidance records a conflict between DAG_CLOSURE_CONTROL current queue and _STATUS.md; Datasheet also reports CurrentLifecycleState INITIALIZED, so a human ruling remains pending for the authoritative status narrative. | Guidance.md; Datasheet.md; _STATUS.md | Guidance#Conflict Table (for human ruling); Datasheet#Identification; _STATUS#History | Guidance.md#Conflict Table (for human ruling); Datasheet.md#Identification; _STATUS.md#History | PROPOSAL | TBD |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | governance condition | 0 | NO_ITEMS | Governance condition is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[normative]:[sufficiency] | normative | sufficiency | evidence warrant | 1 | HAS_ITEMS | Warranted item records the evidence warrant lens against deliverable-local evidence. |
| F:[normative]:[completeness] | normative | completeness | control inventory | 0 | NO_ITEMS | Control inventory is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[normative]:[consistency] | normative | consistency | rule coherence | 0 | NO_ITEMS | Rule coherence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[operative]:[necessity] | operative | necessity | workbook prerequisite | 0 | NO_ITEMS | Workbook prerequisite is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[operative]:[sufficiency] | operative | sufficiency | ruling support | 1 | HAS_ITEMS | Warranted item records the ruling support lens against deliverable-local evidence. |
| F:[operative]:[completeness] | operative | completeness | handoff record | 0 | NO_ITEMS | Handoff record is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[operative]:[consistency] | operative | consistency | schema alignment | 0 | NO_ITEMS | Schema alignment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[evaluative]:[necessity] | evaluative | necessity | review criterion | 0 | NO_ITEMS | Review criterion is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | audit basis | 0 | NO_ITEMS | Audit basis is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[evaluative]:[completeness] | evaluative | completeness | closure evidence | 0 | NO_ITEMS | Closure evidence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| F:[evaluative]:[consistency] | evaluative | consistency | verdict coherence | 0 | NO_ITEMS | Verdict coherence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[sufficiency] | MissingSlot | Specification | Specification | Identify the source location for existing dependency schema actions and allowed fields before row-classification work. | Specification Standards marks the existing dependency schema source location as TBD, while Requirements prohibit inventing new dependency types. The evidence warrant lens exposes that schema authority is not yet located. | Specification.md | Standards |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[sufficiency] | TBD_Question | Procedure | Procedure | Who will provide access to owning product dependency registers and cited source evidence for SCC-001 workbook rows? | Procedure prerequisites require access before future row decisions can be accepted, but the deliverable does not name an access owner or acquisition path. | Procedure.md; Datasheet.md | Procedure#Prerequisites; Datasheet#Identification |  | PROPOSAL | TBD |

## Matrix D — Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | control direction | 0 | NO_ITEMS | Control direction is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[normative]:[applying] | normative | applying | governed practice | 0 | NO_ITEMS | Governed practice is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[normative]:[judging] | normative | judging | rule determination | 0 | NO_ITEMS | Rule determination is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[normative]:[reviewing] | normative | reviewing | authority review | 0 | NO_ITEMS | Authority review is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[operative]:[guiding] | operative | guiding | workflow direction | 0 | NO_ITEMS | Workflow direction is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[operative]:[applying] | operative | applying | reconciliation execution | 1 | HAS_ITEMS | Warranted item records the reconciliation execution lens against deliverable-local evidence. |
| D:[operative]:[judging] | operative | judging | evidence assessment | 0 | NO_ITEMS | Evidence assessment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[operative]:[reviewing] | operative | reviewing | process review | 0 | NO_ITEMS | Process review is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[evaluative]:[guiding] | evaluative | guiding | closure orientation | 0 | NO_ITEMS | Closure orientation is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[evaluative]:[applying] | evaluative | applying | ruling application | 0 | NO_ITEMS | Ruling application is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[evaluative]:[judging] | evaluative | judging | verdict determination | 0 | NO_ITEMS | Verdict determination is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality review | 0 | NO_ITEMS | Quality review is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | MissingSlot | Procedure | Procedure | Define the focused SCC-001 ruling workbook output path/name and minimum columns before execution. | Procedure requires creating the workbook but does not specify the record location or column contract needed for repeatable reconciliation execution. | Procedure.md; Specification.md | Procedure#Steps; Specification#Documentation |  | PROPOSAL | TBD |

## Matrix X — Integration

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | control need | 0 | NO_ITEMS | Control need is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | evidence direction | 0 | NO_ITEMS | Evidence direction is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[guiding]:[completeness] | guiding | completeness | scope record | 0 | NO_ITEMS | Scope record is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[guiding]:[consistency] | guiding | consistency | boundary alignment | 0 | NO_ITEMS | Boundary alignment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[applying]:[necessity] | applying | necessity | practice condition | 0 | NO_ITEMS | Practice condition is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[applying]:[sufficiency] | applying | sufficiency | execution warrant | 0 | NO_ITEMS | Execution warrant is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[applying]:[completeness] | applying | completeness | workbook account | 0 | NO_ITEMS | Workbook account is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[applying]:[consistency] | applying | consistency | schema discipline | 0 | NO_ITEMS | Schema discipline is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[judging]:[necessity] | judging | necessity | decision criterion | 0 | NO_ITEMS | Decision criterion is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[judging]:[sufficiency] | judging | sufficiency | ruling evidence | 0 | NO_ITEMS | Ruling evidence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[judging]:[completeness] | judging | completeness | decision record | 0 | NO_ITEMS | Decision record is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[judging]:[consistency] | judging | consistency | classification coherence | 0 | NO_ITEMS | Classification coherence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[reviewing]:[necessity] | reviewing | necessity | review threshold | 0 | NO_ITEMS | Review threshold is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | audit evidence | 0 | NO_ITEMS | Audit evidence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| X:[reviewing]:[completeness] | reviewing | completeness | closure package | 1 | HAS_ITEMS | Warranted item records the closure package lens against deliverable-local evidence. |
| X:[reviewing]:[consistency] | reviewing | consistency | handoff coherence | 0 | NO_ITEMS | Handoff coherence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[completeness] | VerificationGap | Specification | Specification | Add acceptance evidence for the explicit handoff state: upstream snapshot, derivative status, closure verdict, rerun requirements, and remaining blockers. | Specification Documentation names the handoff state, but Verification does not directly check all closure-rule fields required by the governance handoff. | Specification.md; Procedure.md | Specification#Documentation; Procedure#Records |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | control fact | 0 | NO_ITEMS | Control fact is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[guiding]:[information] | guiding | information | direction signal | 0 | NO_ITEMS | Direction signal is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[guiding]:[knowledge] | guiding | knowledge | boundary understanding | 0 | NO_ITEMS | Boundary understanding is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[guiding]:[wisdom] | guiding | wisdom | closure discernment | 0 | NO_ITEMS | Closure discernment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[applying]:[data] | applying | data | practice evidence | 0 | NO_ITEMS | Practice evidence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[applying]:[information] | applying | information | workbook context | 1 | HAS_ITEMS | Warranted item records the workbook context lens against deliverable-local evidence. |
| E:[applying]:[knowledge] | applying | knowledge | schema expertise | 0 | NO_ITEMS | Schema expertise is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[applying]:[wisdom] | applying | wisdom | ruling judgment | 0 | NO_ITEMS | Ruling judgment is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[judging]:[data] | judging | data | decision evidence | 0 | NO_ITEMS | Decision evidence is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[judging]:[information] | judging | information | classification message | 0 | NO_ITEMS | Classification message is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[judging]:[knowledge] | judging | knowledge | ruling understanding | 0 | NO_ITEMS | Ruling understanding is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[judging]:[wisdom] | judging | wisdom | verdict reasoning | 0 | NO_ITEMS | Verdict reasoning is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[reviewing]:[data] | reviewing | data | audit record | 1 | HAS_ITEMS | Warranted item records the audit record lens against deliverable-local evidence. |
| E:[reviewing]:[information] | reviewing | information | handoff account | 0 | NO_ITEMS | Handoff account is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | closure mastery | 0 | NO_ITEMS | Closure mastery is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | governance reasoning | 0 | NO_ITEMS | Governance reasoning is represented in the current control, workflow, verification, or handoff text without an additional warranted gap. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[data] | VerificationGap | Procedure | Procedure | Record the follow-up DepClosure snapshot path and strict FULL_GRAPH result as post-ruling audit evidence. | Procedure and Specification require a new DepClosure scan after accepted row updates; the audit-record lens warrants an explicit records check for the immutable follow-up snapshot. | Procedure.md; Specification.md | Procedure#Records; Specification#Verification |  | PROPOSAL | TBD |
| E-002 | E:[applying]:[information] | Normalization | Multi | Guidance | Normalize the relationship between triage classification vocabulary and allowed dependency-schema actions. | Guidance calls the classification list a triage vocabulary, Procedure asks to classify each edge using those categories, and Specification forbids new dependency types; downstream use needs a clear mapping to existing schema actions. | Guidance.md; Procedure.md; Specification.md | Guidance#Considerations; Procedure#Steps; Specification#Requirements | Guidance.md#Considerations; Procedure.md#Steps; Specification.md#Requirements | PROPOSAL | TBD |
