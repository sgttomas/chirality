# Semantic Lensing Register: DEL-08-03 Pipeline Category and Task Scope Dispatch

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/_CONTEXT.md#Identity
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/_STATUS.md#History
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/_SEMANTIC.md#Matrix A - Orientation (3x4) - Canonical
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/Datasheet.md#Attributes
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/Specification.md#Requirements
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/Guidance.md#Principles
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/Procedure.md#Steps
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/_REFERENCES.md#Authoritative Source Corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 14
- By document:
  - Datasheet: 1
  - Specification: 5
  - Guidance: 2
  - Procedure: 4
  - Multi: 2
  - NA: 0
- By matrix:
  - A: 1
  - B: 2
  - C: 1
  - F: 3
  - D: 2
  - X: 3
  - E: 2
- By type:
  - Conflict: 1
  - VerificationGap: 5
  - MissingSlot: 3
  - WeakStatement: 0
  - RationaleGap: 2
  - Normalization: 0
  - TBD_Question: 3
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Direction is explicit in the PIPELINE category and TASK scope requirements without another prescriptive gap. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | Mandatory selector and disabled-option practices are stated as P0/P1 requirements. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Compliance posture is carried by verification rows and governance guard review expectations. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Source-state mismatch affects audit closure for PRD-derived selector requirements. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Procedure gives direct step ordering for selectors, discovery, reset, and tests. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Implementation actions are bounded by Procedure steps without a separate action ambiguity. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Performance checks are represented by named verification checks rather than missing criteria here. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Process review is expressed in records and governance boundary review instructions. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Value orientation is clear: visible routes without expanding runtime authority. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Trade-off guidance supports applying reset, visibility, and vocabulary choices. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Worth judgment is deferred to tests and review evidence, not a new register item. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Quality appraisal is covered by ADQ-12 evidence and D-APP-38 source reconciliation. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Resolved | Guidance | Guidance | Former PRD source-state warning is resolved under D-APP-38. | `_REFERENCES.md` now records REF-006 as `MATCH`; Specification and Guidance keep implementation proof separate from source-state proof. | _REFERENCES.md; Specification.md; Guidance.md | _REFERENCES.md#Authoritative Source Corpus; Specification.md#Source State; Guidance.md#Conflict Table (for human ruling) | _REFERENCES.md#Authoritative Source Corpus; Guidance.md#Conflict Table (for human ruling) | D-APP-38 | D-APP-38 accepted current authority corpus |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 1 | HAS_ITEMS | Essential implementation locations remain absent from the construction record. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Evidence expectations are named in Specification verification rows. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | Dependency edge records remain deferred and affect completeness. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | Canonical source references align across the four production documents. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Required selector and scan signals are present in requirements and procedure. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | Context envelope and scope statements provide enough local context for this phase. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | The account covers categories, task scopes, discovery, reset, and disabled options. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | Guidance and Procedure use compatible framing for UI intent versus runtime authority. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | The deliverable explains the operator-facing dispatch model at required depth. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Standards and examples provide sufficient operator-facing understanding. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Full mastery is implementation-phase evidence, not a lens-register prerequisite. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | The governance boundary is consistently described across Specification and Guidance. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Required discernment is present in disabled-option and authority-boundary trade-offs. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Judgment posture is adequate for setup: describe intent, do not grant authority. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Cross-surface insight is carried by tests plus governance review records. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Reasoning remains anchored to canonical vocabulary and fail-closed governance. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[necessity] | MissingSlot | Datasheet | Datasheet | Confirm implementation component and test file paths for category selector, TASK scope selector, scope scan, and reset behavior. | Datasheet Construction records every implementation location as TBD. The essential-fact lens treats those locations as required slots for later implementation handoff. | Datasheet.md; Guidance.md | Datasheet.md#Construction; Guidance.md#Assumptions |  | PROPOSAL | TBD |
| B-002 | B:[data]:[completeness] | MissingSlot | Procedure | Procedure | Record accepted upstream and downstream dependency edges once dependency extraction is performed. | Procedure Prerequisites state declared upstream and downstream dependencies are TBD because no accepted edges have been extracted. The comprehensive-record lens marks this as a closure-relevant record slot. | Procedure.md; Specification.md | Procedure.md#Prerequisites; Specification.md#Scope |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding evidence frame | 0 | NO_ITEMS | Binding evidence basis is identified through PRD, TYPES, SPEC, and CONTRACT references. |
| C:[normative]:[sufficiency] | normative | sufficiency | warranted control basis | 0 | NO_ITEMS | Control basis is sufficient for setup because authority expansion is explicitly forbidden. |
| C:[normative]:[completeness] | normative | completeness | complete rule account | 0 | NO_ITEMS | Rule account names categories, scope modes, bucket vocabulary, and disabled options. |
| C:[normative]:[consistency] | normative | consistency | stable compliance signal | 1 | HAS_ITEMS | Metadata bucket exposure needs clearer rationale to keep vocabulary consistency stable. |
| C:[operative]:[necessity] | operative | necessity | executable proof basis | 0 | NO_ITEMS | Execution proof is directed to selector, discovery, reset, and governance checks. |
| C:[operative]:[sufficiency] | operative | sufficiency | workable context frame | 0 | NO_ITEMS | Procedure gives workable sequencing for a future implementation worker. |
| C:[operative]:[completeness] | operative | completeness | complete action record | 0 | NO_ITEMS | Required records are listed and can be populated after implementation. |
| C:[operative]:[consistency] | operative | consistency | stable process signal | 0 | NO_ITEMS | Process signals use the same selector and scope terminology as Specification. |
| C:[evaluative]:[necessity] | evaluative | necessity | value proof basis | 0 | NO_ITEMS | Value proof is tied to avoiding stale execution and unsupported path activation. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | warranted merit context | 0 | NO_ITEMS | Merit context includes operator clarity, roadmap visibility, and governance separation. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete appraisal account | 0 | NO_ITEMS | Appraisal scope is bounded to UI state and tests, excluding broader hardening. |
| C:[evaluative]:[consistency] | evaluative | consistency | stable quality signal | 0 | NO_ITEMS | Quality signal is consistent with visible but non-executable unsupported options. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[consistency] | RationaleGap | Guidance | Guidance | Explain when metadata buckets should be exposed with KnowledgeTypeOption vocabulary versus deferred from the UI. | Specification requires alignment when metadata buckets are exposed, while Guidance says to account for them if exposed. The stable-compliance-signal lens warrants a rationale so optional exposure does not become parallel taxonomy drift. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Guidance.md#Considerations; Procedure.md#Steps |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | binding readiness warrant | 0 | NO_ITEMS | Binding readiness is represented by P0 requirements for categories, scope, and authority. |
| F:[normative]:[sufficiency] | normative | sufficiency | controlled adequacy basis | 1 | HAS_ITEMS | Governance guard proof needs a sharper acceptance threshold. |
| F:[normative]:[completeness] | normative | completeness | governed coverage frame | 0 | NO_ITEMS | Governed coverage includes selector, discovery, reset, and unsupported-option behavior. |
| F:[normative]:[consistency] | normative | consistency | stable conformance signal | 0 | NO_ITEMS | Conformance vocabulary is stable across standards and requirements. |
| F:[operative]:[necessity] | operative | necessity | executable readiness warrant | 0 | NO_ITEMS | Procedure identifies the executable readiness sequence. |
| F:[operative]:[sufficiency] | operative | sufficiency | workable adequacy basis | 1 | HAS_ITEMS | Scope API usage requires concrete evidence criteria before closure. |
| F:[operative]:[completeness] | operative | completeness | bounded coverage frame | 1 | HAS_ITEMS | Test inventory needs named fixtures for all reset triggers. |
| F:[operative]:[consistency] | operative | consistency | stable workflow signal | 0 | NO_ITEMS | Workflow instructions preserve target reset order and deliverable-bound knowledge mode. |
| F:[evaluative]:[necessity] | evaluative | necessity | value readiness warrant | 0 | NO_ITEMS | Value readiness is grounded in preventing unsupported or stale execution. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | merit adequacy basis | 0 | NO_ITEMS | Adequacy is framed through operator clarity and governance guardrails. |
| F:[evaluative]:[completeness] | evaluative | completeness | appraisal coverage frame | 0 | NO_ITEMS | Appraisal coverage is scoped to this UI dispatch slice and its tests. |
| F:[evaluative]:[consistency] | evaluative | consistency | stable quality signal | 0 | NO_ITEMS | Quality signal aligns with the deliverable's exclusion of runtime subagent bridge work. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Define pass evidence for proving selector state cannot bypass Type 2 sealed context, approval metadata, or fail-closed gates. | Requirement DEL-08-03-REQ-011 requires no authority expansion, but Verification accepts governance tests or review evidence without a minimal proof threshold. The controlled-adequacy lens calls for acceptance detail. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Specification.md#Verification; Guidance.md#Principles |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[sufficiency] | VerificationGap | Procedure | Procedure | Specify how `/api/working-root/scope` integration or mock evidence demonstrates active-root scanning rather than hard-coded project assumptions. | Requirement DEL-08-03-REQ-010 and Procedure step 5 require the working-root scope surface, but the procedure does not yet name the evidence shape for API usage. The workable-adequacy lens warrants this proof detail. | Specification.md; Procedure.md | Specification.md#Verification; Procedure.md#Steps |  | PROPOSAL | TBD |
| F-003 | F:[operative]:[completeness] | VerificationGap | Procedure | Procedure | Add named fixtures for root change, removed deliverable, disabled marker, and stale knowledge target reset cases. | Procedure and Specification require stale-selection reset coverage, but current records do not enumerate fixture names or exact cases. The bounded-coverage lens marks the reset evidence as incomplete. | Specification.md; Procedure.md | Specification.md#Verification; Procedure.md#Verification |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | policy closure frame | 1 | HAS_ITEMS | Closure needs a human path for PRD hash reconciliation. |
| D:[normative]:[applying] | normative | applying | mandatory closure method | 0 | NO_ITEMS | Mandatory method is selector visibility plus disabled unsupported routes. |
| D:[normative]:[judging] | normative | judging | conformance verdict basis | 0 | NO_ITEMS | Verdict basis is expected through tests and governance review evidence. |
| D:[normative]:[reviewing] | normative | reviewing | audit closure standard | 0 | NO_ITEMS | Audit standard keeps source warnings visible and status untouched. |
| D:[operative]:[guiding] | operative | guiding | procedure closure frame | 0 | NO_ITEMS | Procedure closure frame is explicit in eight implementation steps. |
| D:[operative]:[applying] | operative | applying | execution closure method | 0 | NO_ITEMS | Execution method is bounded to UI/state tests and implementation notes. |
| D:[operative]:[judging] | operative | judging | performance verdict basis | 0 | NO_ITEMS | Performance verdict is represented by the expected test categories. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance standard | 1 | HAS_ITEMS | Downstream closure needs the confirmed component and test path record. |
| D:[evaluative]:[guiding] | evaluative | guiding | value closure frame | 0 | NO_ITEMS | Value closure frame remains operator clarity without runtime authority. |
| D:[evaluative]:[applying] | evaluative | applying | merit closure method | 0 | NO_ITEMS | Merit closure method preserves roadmap visibility while preventing execution. |
| D:[evaluative]:[judging] | evaluative | judging | worth verdict basis | 0 | NO_ITEMS | Worth verdict can be judged from tests, D-APP-38 source state, and ADQ-12 selector evidence. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality assurance standard | 0 | NO_ITEMS | Quality assurance standard is bounded to selector behavior and knowledge discovery. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[normative]:[guiding] | Resolved | Multi | Guidance | REF-006 source state is reconciled by D-APP-38. | Guidance and `_REFERENCES.md` now record current REF-006 MATCH state for this tranche. | Guidance.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus |  | D-APP-38 | D-APP-38 accepted current authority corpus |
| D-002 | D:[operative]:[reviewing] | Resolved | Procedure | Procedure | ADQ-12 records final UI component paths and test file paths. | Datasheet now records `pipeline-surface.tsx`, Pipeline surface tests, task-scope tests, and deliverables route tests. | Datasheet.md; Procedure.md | Datasheet.md#Construction; Procedure.md#Records |  | ADQ-12 | ADQ-12 accepted component/test evidence |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | route validity warrant | 0 | NO_ITEMS | Route validity is anchored by canonical category and scope requirements. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | selector adequacy proof | 1 | HAS_ITEMS | Selector adequacy proof needs documented option-list expectations per category. |
| X:[guiding]:[completeness] | guiding | completeness | dispatch coverage account | 0 | NO_ITEMS | Dispatch coverage spans DECOMP, PREP, TASK, AUDIT, deliverables, and knowledge types. |
| X:[guiding]:[consistency] | guiding | consistency | vocabulary coherence signal | 0 | NO_ITEMS | Vocabulary coherence is supported by TYPES-derived terms and Guidance principles. |
| X:[applying]:[necessity] | applying | necessity | action readiness proof | 0 | NO_ITEMS | Action readiness follows from the ordered Procedure steps. |
| X:[applying]:[sufficiency] | applying | sufficiency | usable context basis | 0 | NO_ITEMS | Context basis is usable without selecting implementation paths prematurely. |
| X:[applying]:[completeness] | applying | completeness | bounded scan record | 1 | HAS_ITEMS | Knowledge bucket discovery evidence should distinguish document-kit and metadata buckets. |
| X:[applying]:[consistency] | applying | consistency | reset coherence signal | 0 | NO_ITEMS | Reset behavior is coherently described for root, deliverable, marker, and stale target changes. |
| X:[judging]:[necessity] | judging | necessity | failure evidence basis | 0 | NO_ITEMS | Failure evidence is implied by disabled and stale target tests. |
| X:[judging]:[sufficiency] | judging | sufficiency | typed feedback warrant | 1 | HAS_ITEMS | Disabled option behavior needs non-interactivity evidence, not just visibility evidence. |
| X:[judging]:[completeness] | judging | completeness | option coverage account | 0 | NO_ITEMS | Option coverage is stated at category, task-scope, and knowledge-bucket levels. |
| X:[judging]:[consistency] | judging | consistency | state coherence signal | 0 | NO_ITEMS | State coherence is enforced through invalid-selection reset requirements. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit evidence frame | 0 | NO_ITEMS | Audit evidence frame includes source warning and governance guard review. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | boundary assurance basis | 0 | NO_ITEMS | Boundary assurance is explicit in no-authority-expansion language. |
| X:[reviewing]:[completeness] | reviewing | completeness | omission coverage record | 0 | NO_ITEMS | Omission handling is bounded by out-of-scope and deferred dependency statements. |
| X:[reviewing]:[consistency] | reviewing | consistency | source warning signal | 0 | NO_ITEMS | Source warning signal is repeated consistently in Specification, Guidance, and Procedure. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[guiding]:[sufficiency] | MissingSlot | Specification | Specification | Name the documented category-specific option lists or fixtures expected under DECOMP, PREP, TASK, and AUDIT. | Requirement DEL-08-03-REQ-002 requires documented category-specific options, but current production docs do not enumerate the option lists or fixture source. The selector-adequacy lens exposes the missing slot. | Specification.md; Procedure.md; Datasheet.md | Specification.md#Requirements; Procedure.md#Steps; Datasheet.md#Attributes |  | PROPOSAL | TBD |
| X-002 | X:[applying]:[completeness] | VerificationGap | Specification | Specification | Require discovery evidence for Datasheet, Specification, Guidance, Procedure, and any exposed metadata buckets using canonical KnowledgeTypeOption labels. | Specification requires document-kit discovery and metadata vocabulary alignment when exposed, but verification only names document-kit and metadata bucket discovery broadly. The bounded-scan lens warrants precise discovery evidence. | Specification.md; Guidance.md; Procedure.md | Specification.md#Verification; Guidance.md#Considerations; Procedure.md#Steps |  | PROPOSAL | TBD |
| X-003 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Disabled unsupported variants must be visible, carry disabled or coming-soon semantics, and be unable to initiate execution. | Specification and Procedure mention disabled visibility and non-interactivity, but final evidence should prove all three aspects together. The typed-feedback lens requires a sufficient disabled-option warrant. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Guidance.md#Trade-offs; Procedure.md#Verification |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual route warrant | 0 | NO_ITEMS | Factual route warrant is grounded in accepted decomposition and TYPES vocabulary. |
| E:[guiding]:[information] | guiding | information | contextual selector frame | 0 | NO_ITEMS | Selector context is clear across Purpose, Principles, and Scope. |
| E:[guiding]:[knowledge] | guiding | knowledge | dispatch understanding map | 0 | NO_ITEMS | Dispatch understanding includes category, task scope, and knowledge-bucket dimensions. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled boundary judgment | 1 | HAS_ITEMS | Boundary judgment would benefit from clearer residual-risk handling for UI intent. |
| E:[applying]:[data] | applying | data | actionable route proof | 0 | NO_ITEMS | Actionable route proof is assigned to selector and scope tests. |
| E:[applying]:[information] | applying | information | usable bucket context | 0 | NO_ITEMS | Bucket context is usable for four-document kit discovery. |
| E:[applying]:[knowledge] | applying | knowledge | implementation readiness map | 0 | NO_ITEMS | Implementation readiness remains bounded by TBD paths and future worker notes. |
| E:[applying]:[wisdom] | applying | wisdom | prudent reset judgment | 0 | NO_ITEMS | Reset judgment favors clearing stale state and is described consistently. |
| E:[judging]:[data] | judging | data | error fact basis | 0 | NO_ITEMS | Error facts are expected through disabled and stale target test failures. |
| E:[judging]:[information] | judging | information | typed message context | 0 | NO_ITEMS | Typed feedback context is sufficient at register stage. |
| E:[judging]:[knowledge] | judging | knowledge | acceptance understanding map | 0 | NO_ITEMS | Acceptance understanding is distributed across verification and records sections. |
| E:[judging]:[wisdom] | judging | wisdom | principled verdict judgment | 0 | NO_ITEMS | Verdict judgment remains tied to human source reconciliation and test evidence. |
| E:[reviewing]:[data] | reviewing | data | audit fact basis | 0 | NO_ITEMS | Audit facts include status history and D-APP-38 source-state metadata. |
| E:[reviewing]:[information] | reviewing | information | source-state context | 1 | HAS_ITEMS | Source-state context is resolved by D-APP-38 while implementation proof remains separate. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | coverage understanding map | 0 | NO_ITEMS | Coverage understanding names what is in and out of scope. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | closure judgment frame | 0 | NO_ITEMS | Closure judgment can proceed only after derivative evidence and human rulings are current. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[wisdom] | RationaleGap | Guidance | Guidance | Explain that UI dispatch expresses operator intent and route selection but runtime authority remains with TASK and Type 2 governance checks. | Guidance states this principle, but the later enrichment pass should make the boundary rationale durable for implementers who may wire selectors to execution surfaces. The principled-boundary lens warrants a rationale entry. | Guidance.md; Specification.md | Guidance.md#Purpose; Guidance.md#Principles; Specification.md#Scope |  | PROPOSAL | TBD |
| E-002 | E:[reviewing]:[information] | Resolved | Multi | Guidance | D-APP-38 distinguishes source-state proof from implementation proof. | Specification and Guidance now state REF-006 is current while selector behavior remains proven by code/tests. | Specification.md; Guidance.md; _REFERENCES.md | Specification.md#Source State; Guidance.md#Considerations; _REFERENCES.md#Authoritative Source Corpus |  | D-APP-38 | D-APP-38 accepted current authority corpus |
