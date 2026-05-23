# Semantic Lensing Register: DEL-02-05 API Key UI and Runtime Feedback

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py passed after generation
**Warnings:** REF-006 PRD hash mismatch remains a source warning; dependency extraction remains deferred; SOW-019 cross-package ownership remains unresolved.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_CONTEXT.md#context-del-02-05-api-key-ui-and-runtime-feedback
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_STATUS.md#status-del-02-05
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_SEMANTIC.md#semantic-lens-del-02-05-api-key-ui-and-runtime-feedback
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Datasheet.md#datasheet-del-02-05-api-key-ui-and-runtime-feedback
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Specification.md#specification-del-02-05-api-key-ui-and-runtime-feedback
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Guidance.md#guidance-del-02-05-api-key-ui-and-runtime-feedback
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Procedure.md#procedure-del-02-05-api-key-ui-and-runtime-feedback
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_REFERENCES.md#references-del-02-05-api-key-ui-and-runtime-feedback metadata only; external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 8
- By document:
  - Datasheet: 0
  - Specification: 1
  - Guidance: 1
  - Procedure: 2
  - Multi: 4
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
  - VerificationGap: 3
  - MissingSlot: 2
  - WeakStatement: 1
  - RationaleGap: 0
  - Normalization: 0
  - TBD_Question: 0
  - MatrixError: 0
- Notable conflicts: 2
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction scan found source-backed key secrecy and project-truth direction already represented in the local documents. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 1 | HAS_ITEMS | mandatory practice scan exposes 1 local gap in how the API key settings surface is bound to implementation evidence. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination scan found verification obligations stated without an additional distinct ruling input for this lens. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit scan found review concerns represented through secret hygiene and source-warning records. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction scan found the procedure preserves the UI-slice boundary and retry workflow orientation. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution scan found steps for key status, secure storage feedback, runtime error display, retry state, and SSE compatibility. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment scan found expected checks listed for key status, safeStorage, runtime errors, retry, SSE, and secret hygiene. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit scan found records requested for implementation, tests, and human rulings. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation scan found operator confidence and recovery value represented in Guidance principles. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application scan found actionable feedback constrained by secrecy and runtime-authority boundaries. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination scan found user-visible recovery value covered without a separate enrichment issue. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal scan found trust and secret-hygiene checks already surfaced in Procedure verification. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[applying] | WeakStatement | Specification | Specification | Bind DEL-02-05-R01 to the eventual API key settings component/module path once selected. | Specification requires an API key settings surface and Datasheet says the specific component path is TBD. The mandatory UI practice is clear, but the later implementation target remains weakly specified. | Specification.md; Datasheet.md | Specification.md#requirements DEL-02-05-R01; Datasheet.md#construction |  | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact scan found required status values, precedence, event names, and secret boundaries recorded. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence scan found source citations for API key status, safeStorage, retry preservation, and SSE compatibility. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record scan found local records identify required implementation and test evidence categories. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | reliable measurement scan exposes 1 grounded verification gap around measuring precedence/status behavior. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal scan found user-facing `ui`, `env`, and `none` status signals named. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context scan found next-step runtime error messaging and secure-storage error context addressed. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account scan found key UI, secure-storage feedback, typed errors, retry state, and event compatibility all represented. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message scan found Guidance aligns UI feedback with secrecy and non-authority boundaries. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding scan found adjacent runtime/security ownership limits stated. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise scan found source-backed standards for storage policy, SSE contract, and redaction policy. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery scan found taxonomy ownership marked as an assumption instead of invented locally. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding scan found production docs consistently keep runtime authority outside the UI slice. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment scan found PRD hash mismatch and cross-package ownership caveats surfaced for human judgment. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment scan found conservative PRD use and corroborated SPEC/CONTRACT/TYPES preference recorded. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight scan found user recovery, security, event compatibility, and project-truth boundaries considered together. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning scan found trade-offs keep detail, secrecy, ownership, and compatibility aligned. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | VerificationGap | Multi | Specification | Add a verification fixture or test name that proves key status rendering and precedence for `ui`, `env`, and `none`. | Specification and Procedure require status and precedence checks, but neither identifies the concrete fixture, module, or command that will make those data states measurable. | Specification.md; Procedure.md | Specification.md#verification DEL-02-05-R02 and DEL-02-05-R03; Procedure.md#verification |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | Binding Control Rationale | 0 | NO_ITEMS | Binding Control Rationale scan found key secrecy and project-truth boundaries supported by CONTRACT, SPEC, PRD, DIRECTIVE, and TYPES citations. |
| C:[normative]:[sufficiency] | normative | sufficiency | Defensible Rule Support | 0 | NO_ITEMS | Defensible Rule Support scan found corroborating sources for storage policy and redaction despite PRD warning. |
| C:[normative]:[completeness] | normative | completeness | Complete Standard Picture | 0 | NO_ITEMS | Complete Standard Picture scan found in-scope and out-of-scope standards separated in Specification. |
| C:[normative]:[consistency] | normative | consistency | Coherent Rule Logic | 1 | HAS_ITEMS | Coherent Rule Logic scan exposes 1 source-state conflict affecting PRD-cited requirements. |
| C:[operative]:[necessity] | operative | necessity | Necessary Action Basis | 0 | NO_ITEMS | Necessary Action Basis scan found procedure prerequisites name available or mocked runtime/API contracts. |
| C:[operative]:[sufficiency] | operative | sufficiency | Workable Execution Proof | 0 | NO_ITEMS | Workable Execution Proof scan found checks for status, safeStorage, errors, retry state, SSE, and secret hygiene. |
| C:[operative]:[completeness] | operative | completeness | Complete Action Trace | 0 | NO_ITEMS | Complete Action Trace scan found records requested for implementation and tests across all anticipated artifacts. |
| C:[operative]:[consistency] | operative | consistency | Stable Operating Logic | 0 | NO_ITEMS | Stable Operating Logic scan found event compatibility and non-authoritative UI state preserved across steps. |
| C:[evaluative]:[necessity] | evaluative | necessity | Essential Value Basis | 0 | NO_ITEMS | Essential Value Basis scan found operator recovery confidence grounded in retry preservation and actionable errors. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | Qualified Value Support | 0 | NO_ITEMS | Qualified Value Support scan found guidance balances specificity against secrecy and taxonomy ownership. |
| C:[evaluative]:[completeness] | evaluative | completeness | Holistic Value Account | 0 | NO_ITEMS | Holistic Value Account scan found all four production docs include recovery, feedback, and boundary concerns. |
| C:[evaluative]:[consistency] | evaluative | consistency | Principled Value Logic | 0 | NO_ITEMS | Principled Value Logic scan found trust language constrained to UI assistance rather than approval or certification. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[consistency] | Conflict | Multi | NA | Record human ruling for use of PRD-backed API key and runtime recovery requirements while REF-006 has HASH_MISMATCH. | Guidance treats the PRD hash mismatch as a warning, while _REFERENCES records REF-006 as HASH_MISMATCH. Requirements R01-R07 and R09 cite PRD content, so the source-state conflict remains relevant to later closure. | Guidance.md; _REFERENCES.md; Specification.md | Guidance.md#conflict-table-for-human-ruling C-001; _REFERENCES.md#authoritative-source-corpus REF-006; Specification.md#requirements | Guidance.md#conflict-table-for-human-ruling C-001; _REFERENCES.md#authoritative-source-corpus REF-006 | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | Required Boundary Condition | 0 | NO_ITEMS | Required Boundary Condition scan found mandatory key secrecy, local UI state, and runtime-authority boundaries stated. |
| F:[normative]:[sufficiency] | normative | sufficiency | Acceptable Control Evidence | 0 | NO_ITEMS | Acceptable Control Evidence scan found verification approaches for storage path, status, precedence, safeStorage, SSE, and redaction. |
| F:[normative]:[completeness] | normative | completeness | Full Governance Coverage | 1 | HAS_ITEMS | Full Governance Coverage scan exposes 1 missing evidence slot for governance closure records. |
| F:[normative]:[consistency] | normative | consistency | Aligned Rule Assurance | 0 | NO_ITEMS | Aligned Rule Assurance scan found consistent prohibition against treating keys, logs, drafts, transcripts, or UI state as project truth. |
| F:[operative]:[necessity] | operative | necessity | Required Execution Trigger | 0 | NO_ITEMS | Required Execution Trigger scan found safeStorage unavailable and runtime error states identified as UI triggers. |
| F:[operative]:[sufficiency] | operative | sufficiency | Sufficient Operating Basis | 0 | NO_ITEMS | Sufficient Operating Basis scan found mocked or available runtime/API contracts allowed for UI work. |
| F:[operative]:[completeness] | operative | completeness | End-to-End Recovery Trace | 1 | HAS_ITEMS | End-to-End Recovery Trace scan exposes 1 missing slot around retry state ownership and evidence. |
| F:[operative]:[consistency] | operative | consistency | Repeatable Recovery Behavior | 0 | NO_ITEMS | Repeatable Recovery Behavior scan found repeated checks for draft/attachment preservation and event compatibility. |
| F:[evaluative]:[necessity] | evaluative | necessity | Essential Operator Confidence | 0 | NO_ITEMS | Essential Operator Confidence scan found user-visible status and actionable error feedback required. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | Adequate Recovery Confidence | 0 | NO_ITEMS | Adequate Recovery Confidence scan found next-step copy required while exact approved wording remains deferred. |
| F:[evaluative]:[completeness] | evaluative | completeness | Whole Feedback Assurance | 0 | NO_ITEMS | Whole Feedback Assurance scan found key, storage, typed error, retry, SSE, and redaction assurance surfaces named. |
| F:[evaluative]:[consistency] | evaluative | consistency | Stable Trust Signal | 0 | NO_ITEMS | Stable Trust Signal scan found trust cues constrained by secret redaction and non-authoritative UI state. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[completeness] | MissingSlot | Procedure | Procedure | Replace record placeholders with final evidence paths for API key settings panel, typed error display, secure-storage UI, and secret-hygiene checks. | Procedure Records list the required implementation and test evidence categories, but not accepted paths or commands. Governance coverage remains incomplete until those records are bound. | Procedure.md | Procedure.md#records |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[completeness] | MissingSlot | Multi | Specification | Name the retry state owner for draft prompt text and attachment metadata after runtime errors. | Specification and Procedure require retry preservation, while Datasheet says the exact local state owner is TBD. End-to-end recovery cannot be traced until the owning UI state surface is identified. | Specification.md; Procedure.md; Datasheet.md | Specification.md#documentation; Procedure.md#steps step 5; Datasheet.md#construction |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | Controlled Recovery Direction | 0 | NO_ITEMS | Controlled Recovery Direction scan found recovery feedback bounded by key secrecy and source warnings. |
| D:[normative]:[applying] | normative | applying | Enforced Feedback Practice | 0 | NO_ITEMS | Enforced Feedback Practice scan found required UI practices stated for storage, status, secure-storage errors, typed errors, retry, and SSE. |
| D:[normative]:[judging] | normative | judging | Conformance Closure Basis | 0 | NO_ITEMS | Conformance Closure Basis scan found verification approaches listed for each requirement. |
| D:[normative]:[reviewing] | normative | reviewing | Assurance Review Path | 0 | NO_ITEMS | Assurance Review Path scan found source warnings and human-ruling entries recorded. |
| D:[operative]:[guiding] | operative | guiding | Actionable Failure Direction | 0 | NO_ITEMS | Actionable Failure Direction scan found the procedure tells implementers how to respond to missing key, unavailable safeStorage, runtime error, and event outcomes. |
| D:[operative]:[applying] | operative | applying | Usable Recovery Control | 1 | HAS_ITEMS | Usable Recovery Control scan exposes 1 unresolved cross-package ownership conflict. |
| D:[operative]:[judging] | operative | judging | Recoverable Failure Judgment | 0 | NO_ITEMS | Recoverable Failure Judgment scan found representative typed errors and retry preservation in verification expectations. |
| D:[operative]:[reviewing] | operative | reviewing | Repeatable Process Check | 0 | NO_ITEMS | Repeatable Process Check scan found repeatable checks identified, pending concrete evidence. |
| D:[evaluative]:[guiding] | evaluative | guiding | Operator Confidence Direction | 0 | NO_ITEMS | Operator Confidence Direction scan found guidance favors clear user recovery without exposing secrets. |
| D:[evaluative]:[applying] | evaluative | applying | Helpful Recovery Support | 0 | NO_ITEMS | Helpful Recovery Support scan found next-step text and retry preservation as the user-facing support mechanism. |
| D:[evaluative]:[judging] | evaluative | judging | Feedback Worth Judgment | 0 | NO_ITEMS | Feedback Worth Judgment scan found visible secure-storage and runtime failure feedback tied to user value. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | Trust Quality Review | 0 | NO_ITEMS | Trust Quality Review scan found redaction and non-authority checks included in review expectations. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | Conflict | Guidance | NA | Human ruling needed on SOW-019 boundary: DEL-02-05 UI feedback surface versus PKG-09, DEL-04-05, and DEL-09-06 storage/security enforcement. | Guidance records that SOW-019 primary ownership sits outside this UI slice while DEL-02-05 still covers API key UI/status. The deliverable should not silently decide adjacent storage, provider, or security enforcement authority. | Guidance.md; _CONTEXT.md | Guidance.md#conflict-table-for-human-ruling C-002; _CONTEXT.md#traceability | Guidance.md#conflict-table-for-human-ruling C-002; _CONTEXT.md#traceability | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | Required Recovery Signal | 0 | NO_ITEMS | Required Recovery Signal scan found missing key, secure-storage failure, runtime error, and process exit signals identified. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | Supported Recovery Path | 0 | NO_ITEMS | Supported Recovery Path scan found status display, next-step copy, and retry preservation described. |
| X:[guiding]:[completeness] | guiding | completeness | Complete Recovery Orientation | 0 | NO_ITEMS | Complete Recovery Orientation scan found all anticipated artifacts represented in documentation requirements. |
| X:[guiding]:[consistency] | guiding | consistency | Coherent Recovery Cue | 0 | NO_ITEMS | Coherent Recovery Cue scan found UI messages constrained by SSE compatibility and secret redaction. |
| X:[applying]:[necessity] | applying | necessity | Required Feedback Action | 0 | NO_ITEMS | Required Feedback Action scan found user-visible secure-storage and typed runtime error actions specified. |
| X:[applying]:[sufficiency] | applying | sufficiency | Workable Feedback Support | 0 | NO_ITEMS | Workable Feedback Support scan found mocks allowed where runtime/API contracts are not finalized. |
| X:[applying]:[completeness] | applying | completeness | Complete Support Trace | 0 | NO_ITEMS | Complete Support Trace scan found implementation and tests required for panel, error display, secure-storage UI, and secret boundaries. |
| X:[applying]:[consistency] | applying | consistency | Repeatable Support Behavior | 0 | NO_ITEMS | Repeatable Support Behavior scan found precedence, status, retry, and event compatibility checks expressed as repeatable verification expectations. |
| X:[judging]:[necessity] | judging | necessity | Necessary Recovery Verdict | 0 | NO_ITEMS | Necessary Recovery Verdict scan found pass/fail checks for preserving draft and attachment context. |
| X:[judging]:[sufficiency] | judging | sufficiency | Adequate Failure Verdict | 0 | NO_ITEMS | Adequate Failure Verdict scan found representative typed errors required for mapping tests. |
| X:[judging]:[completeness] | judging | completeness | Complete Recovery Verdict | 0 | NO_ITEMS | Complete Recovery Verdict scan found runtime failure display, retry state, and event handling all included. |
| X:[judging]:[consistency] | judging | consistency | Consistent Failure Judgment | 0 | NO_ITEMS | Consistent Failure Judgment scan found provider detail must be redacted across visible and logged channels. |
| X:[reviewing]:[necessity] | reviewing | necessity | Required Assurance Check | 0 | NO_ITEMS | Required Assurance Check scan found key-material exclusion and project-truth exclusion checks stated. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | Sufficient Trust Check | 0 | NO_ITEMS | Sufficient Trust Check scan found source-backed redaction and non-authority standards cited. |
| X:[reviewing]:[completeness] | reviewing | completeness | Complete Assurance Review | 1 | HAS_ITEMS | Complete Assurance Review scan exposes 1 evidence-completeness gap for final test artifacts. |
| X:[reviewing]:[consistency] | reviewing | consistency | Reliable Trust Review | 0 | NO_ITEMS | Reliable Trust Review scan found trust review expectations aligned with non-leakage and event compatibility. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[completeness] | VerificationGap | Procedure | Procedure | Add final test/evidence references for status rendering, precedence, unavailable safeStorage, typed error mapping, retry preservation, SSE compatibility, and redaction. | The Procedure verification table defines the checks, but the Records section has not yet bound them to actual artifacts. Complete assurance review needs those references after implementation exists. | Procedure.md; Specification.md | Procedure.md#verification; Procedure.md#records; Specification.md#verification |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | Recoverable Status Fact | 0 | NO_ITEMS | Recoverable Status Fact scan found status values, precedence, and event names captured as facts. |
| E:[guiding]:[information] | guiding | information | Actionable Recovery Message | 0 | NO_ITEMS | Actionable Recovery Message scan found title, message, and next-step text required for typed errors. |
| E:[guiding]:[knowledge] | guiding | knowledge | Recovery Guidance Understanding | 0 | NO_ITEMS | Recovery Guidance Understanding scan found runtime authority and taxonomy ownership boundaries stated. |
| E:[guiding]:[wisdom] | guiding | wisdom | Prudent Recovery Choice | 0 | NO_ITEMS | Prudent Recovery Choice scan found recovery advice constrained by source warnings and secret hygiene. |
| E:[applying]:[data] | applying | data | Displayed Recovery Fact | 0 | NO_ITEMS | Displayed Recovery Fact scan found UI may display source/status but not key material. |
| E:[applying]:[information] | applying | information | Usable Feedback Message | 0 | NO_ITEMS | Usable Feedback Message scan found secure-storage and runtime error feedback requirements. |
| E:[applying]:[knowledge] | applying | knowledge | Operational Recovery Knowhow | 0 | NO_ITEMS | Operational Recovery Knowhow scan found implementer steps for status UI, safeStorage feedback, typed errors, retry, and events. |
| E:[applying]:[wisdom] | applying | wisdom | Helpful Failure Judgment | 0 | NO_ITEMS | Helpful Failure Judgment scan found UI support should avoid raw provider details and approved/certified language. |
| E:[judging]:[data] | judging | data | Failure Status Finding | 0 | NO_ITEMS | Failure Status Finding scan found status and failure checks stated in verification form. |
| E:[judging]:[information] | judging | information | Clear Failure Explanation | 0 | NO_ITEMS | Clear Failure Explanation scan found typed runtime errors must map to title, message, and next-step fields. |
| E:[judging]:[knowledge] | judging | knowledge | Failure Interpretation Frame | 0 | NO_ITEMS | Failure Interpretation Frame scan found canonical taxonomy ownership deferred to runtime/provider layers. |
| E:[judging]:[wisdom] | judging | wisdom | Sound Failure Judgment | 0 | NO_ITEMS | Sound Failure Judgment scan found human review required for taxonomy ownership and source-state caveats. |
| E:[reviewing]:[data] | reviewing | data | Assurance Check Fact | 1 | HAS_ITEMS | Assurance Check Fact scan exposes 1 record-assurance gap for concrete evidence artifacts. |
| E:[reviewing]:[information] | reviewing | information | Trust Review Message | 0 | NO_ITEMS | Trust Review Message scan found user-facing trust cues kept informational and non-authoritative. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | Assurance Review Insight | 0 | NO_ITEMS | Assurance Review Insight scan found review standards grounded in CONTRACT, SPEC, PRD, TYPES, and DIRECTIVE citations. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | Principled Trust Appraisal | 0 | NO_ITEMS | Principled Trust Appraisal scan found source warnings and ownership conflicts left for human ruling. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[data] | VerificationGap | Multi | Specification | Define concrete acceptance evidence paths or commands for key storage secrecy, runtime redaction, and non-authoritative UI state. | Datasheet and Specification state that keys, logs, drafts, transcripts, and UI state must not become project truth, while Procedure Records leave evidence locations open. Record assurance remains incomplete until the checks are bound. | Datasheet.md; Specification.md; Procedure.md | Datasheet.md#conditions; Specification.md#verification DEL-02-05-R08 and DEL-02-05-R09; Procedure.md#records |  | PROPOSAL | TBD |
