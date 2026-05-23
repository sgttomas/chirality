# Semantic Lensing Register: DEL-02-04 Toolkit Options and Local UI State

**Generated:** 2026-05-20  
**DECOMP_VARIANT:** SOFTWARE  
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State  
**StatusPolicy:** NO_STATUS_TOUCH  
**Validator:** PASS - validate_lens_register.py passed on 2026-05-20  
**Warnings:** PRD source hash mismatch retained from _REFERENCES.md REF-006; production records contain TBD implementation and policy-mode evidence slots.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_CONTEXT.md#context-del-02-04-toolkit-options-and-local-ui-state
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_STATUS.md#status-del-02-04
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_SEMANTIC.md#semantic-lens-del-02-04-toolkit-options-and-local-ui-state
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Datasheet.md#datasheet-del-02-04-toolkit-options-and-local-ui-state
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md#specification-del-02-04-toolkit-options-and-local-ui-state
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Guidance.md#guidance-del-02-04-toolkit-options-and-local-ui-state
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Procedure.md#procedure-del-02-04-toolkit-options-and-local-ui-state
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_REFERENCES.md#references-del-02-04-toolkit-options-and-local-ui-state (metadata only; external paths not followed)

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 10
- By document:
  - Datasheet: 0
  - Specification: 5
  - Guidance: 1
  - Procedure: 3
  - Multi: 1
  - NA: 0
- By matrix:
  - A: 1
  - B: 1
  - C: 0
  - F: 3
  - D: 2
  - X: 1
  - E: 2
- By type:
  - Conflict: 1
  - VerificationGap: 4
  - MissingSlot: 3
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation (3x4) - Canonical

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction is traceable in the production set for normative/guiding without an additional enrichment entry. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice is traceable in the production set for normative/applying without an additional enrichment entry. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination is traceable in the production set for normative/judging without an additional enrichment entry. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Lensing regulatory audit identifies 1 production follow-up entry for normative/reviewing. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction is traceable in the production set for operative/guiding without an additional enrichment entry. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution is traceable in the production set for operative/applying without an additional enrichment entry. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment is traceable in the production set for operative/judging without an additional enrichment entry. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit is traceable in the production set for operative/reviewing without an additional enrichment entry. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation is traceable in the production set for evaluative/guiding without an additional enrichment entry. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application is traceable in the production set for evaluative/applying without an additional enrichment entry. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination is traceable in the production set for evaluative/judging without an additional enrichment entry. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal is traceable in the production set for evaluative/reviewing without an additional enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Retain PRD hash mismatch as a source-state conflict for human reconciliation before package closure. | The register must preserve audit-facing source caveats because _REFERENCES.md reports a PRD hash mismatch while production docs continue citing PRD content with warning. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_REFERENCES.md; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Guidance.md | _REFERENCES.md#authoritative-source-corpus; Guidance.md#conflict-table-for-human-ruling | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_REFERENCES.md#authoritative-source-corpus; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Guidance.md#conflict-table-for-human-ruling | PROPOSAL | TBD |

## Matrix B - Conceptualization (4x4) - Canonical

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact is traceable in the production set for data/necessity without an additional enrichment entry. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence is traceable in the production set for data/sufficiency without an additional enrichment entry. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | Lensing comprehensive record identifies 1 production follow-up entry for data/completeness. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement is traceable in the production set for data/consistency without an additional enrichment entry. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal is traceable in the production set for information/necessity without an additional enrichment entry. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context is traceable in the production set for information/sufficiency without an additional enrichment entry. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account is traceable in the production set for information/completeness without an additional enrichment entry. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message is traceable in the production set for information/consistency without an additional enrichment entry. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding is traceable in the production set for knowledge/necessity without an additional enrichment entry. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise is traceable in the production set for knowledge/sufficiency without an additional enrichment entry. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery is traceable in the production set for knowledge/completeness without an additional enrichment entry. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding is traceable in the production set for knowledge/consistency without an additional enrichment entry. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment is traceable in the production set for wisdom/necessity without an additional enrichment entry. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment is traceable in the production set for wisdom/sufficiency without an additional enrichment entry. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight is traceable in the production set for wisdom/completeness without an additional enrichment entry. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning is traceable in the production set for wisdom/consistency without an additional enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[completeness] | MissingSlot | Procedure | Procedure | Clarify whether upstream dependency edges remain intentionally absent or await later extraction. | Procedure records declared upstream dependencies as TBD while also saying _DEPENDENCIES has no accepted edges, leaving the production record incomplete for dependency closure. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Procedure.md | Procedure.md#prerequisites |  | PROPOSAL | TBD |

## Matrix C - Formulation (3x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding option duty | 0 | NO_ITEMS | binding option duty is traceable in the production set for normative/necessity without an additional enrichment entry. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate control basis | 0 | NO_ITEMS | adequate control basis is traceable in the production set for normative/sufficiency without an additional enrichment entry. |
| C:[normative]:[completeness] | normative | completeness | complete rule posture | 0 | NO_ITEMS | complete rule posture is traceable in the production set for normative/completeness without an additional enrichment entry. |
| C:[normative]:[consistency] | normative | consistency | coherent authority signal | 0 | NO_ITEMS | coherent authority signal is traceable in the production set for normative/consistency without an additional enrichment entry. |
| C:[operative]:[necessity] | operative | necessity | required interaction path | 0 | NO_ITEMS | required interaction path is traceable in the production set for operative/necessity without an additional enrichment entry. |
| C:[operative]:[sufficiency] | operative | sufficiency | usable control context | 0 | NO_ITEMS | usable control context is traceable in the production set for operative/sufficiency without an additional enrichment entry. |
| C:[operative]:[completeness] | operative | completeness | complete state handling | 0 | NO_ITEMS | complete state handling is traceable in the production set for operative/completeness without an additional enrichment entry. |
| C:[operative]:[consistency] | operative | consistency | reliable behavior pattern | 0 | NO_ITEMS | reliable behavior pattern is traceable in the production set for operative/consistency without an additional enrichment entry. |
| C:[evaluative]:[necessity] | evaluative | necessity | value grounded need | 0 | NO_ITEMS | value grounded need is traceable in the production set for evaluative/necessity without an additional enrichment entry. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment ready context | 0 | NO_ITEMS | judgment ready context is traceable in the production set for evaluative/sufficiency without an additional enrichment entry. |
| C:[evaluative]:[completeness] | evaluative | completeness | holistic quality frame | 0 | NO_ITEMS | holistic quality frame is traceable in the production set for evaluative/completeness without an additional enrichment entry. |
| C:[evaluative]:[consistency] | evaluative | consistency | principled fit signal | 0 | NO_ITEMS | principled fit signal is traceable in the production set for evaluative/consistency without an additional enrichment entry. |

## Matrix F - Requirements (3x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | enforceable option basis | 0 | NO_ITEMS | enforceable option basis is traceable in the production set for normative/necessity without an additional enrichment entry. |
| F:[normative]:[sufficiency] | normative | sufficiency | sufficient governance guard | 1 | HAS_ITEMS | Lensing sufficient governance guard identifies 1 production follow-up entry for normative/sufficiency. |
| F:[normative]:[completeness] | normative | completeness | complete authority model | 0 | NO_ITEMS | complete authority model is traceable in the production set for normative/completeness without an additional enrichment entry. |
| F:[normative]:[consistency] | normative | consistency | consistent policy signal | 0 | NO_ITEMS | consistent policy signal is traceable in the production set for normative/consistency without an additional enrichment entry. |
| F:[operative]:[necessity] | operative | necessity | necessary workflow affordance | 0 | NO_ITEMS | necessary workflow affordance is traceable in the production set for operative/necessity without an additional enrichment entry. |
| F:[operative]:[sufficiency] | operative | sufficiency | viable interaction support | 0 | NO_ITEMS | viable interaction support is traceable in the production set for operative/sufficiency without an additional enrichment entry. |
| F:[operative]:[completeness] | operative | completeness | complete persistence pattern | 1 | HAS_ITEMS | Lensing complete persistence pattern identifies 1 production follow-up entry for operative/completeness. |
| F:[operative]:[consistency] | operative | consistency | stable fallback behavior | 1 | HAS_ITEMS | Lensing stable fallback behavior identifies 1 production follow-up entry for operative/consistency. |
| F:[evaluative]:[necessity] | evaluative | necessity | value evidence basis | 0 | NO_ITEMS | value evidence basis is traceable in the production set for evaluative/necessity without an additional enrichment entry. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate review posture | 0 | NO_ITEMS | adequate review posture is traceable in the production set for evaluative/sufficiency without an additional enrichment entry. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete quality view | 0 | NO_ITEMS | complete quality view is traceable in the production set for evaluative/completeness without an additional enrichment entry. |
| F:[evaluative]:[consistency] | evaluative | consistency | principled appraisal signal | 0 | NO_ITEMS | principled appraisal signal is traceable in the production set for evaluative/consistency without an additional enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Add acceptance evidence for Toolkit mode controls mapping to permission policy modes once policy engine contracts exist. | Requirements mention policy-mode mapping and not treating modes as prompt hints, but verification is explicitly deferred until the policy engine exists. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md | Specification.md#requirements; Specification.md#verification |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[completeness] | MissingSlot | Specification | Specification | Define or defer the local storage schema for draft and attachment-selection keys by root/persona/mode. | The production set requires local persistence but leaves the exact storage schema TBD, which affects complete persistence handling. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md | Specification.md#assumptions-and-tbds |  | PROPOSAL | TBD |
| F-003 | F:[operative]:[consistency] | VerificationGap | Specification | Specification | Add tests showing unknown option keys warn, are ignored, and do not silently mutate runtime behavior. | Deterministic fallback and unknown-key warnings are specified, but the verification table still needs concrete option-handoff test records downstream. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md; /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Procedure.md | Specification.md#verification; Procedure.md#verification |  | PROPOSAL | TBD |

## Matrix D - Decision (3x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | directed governance closure | 0 | NO_ITEMS | directed governance closure is traceable in the production set for normative/guiding without an additional enrichment entry. |
| D:[normative]:[applying] | normative | applying | mandatory option control | 0 | NO_ITEMS | mandatory option control is traceable in the production set for normative/applying without an additional enrichment entry. |
| D:[normative]:[judging] | normative | judging | compliance resolution basis | 0 | NO_ITEMS | compliance resolution basis is traceable in the production set for normative/judging without an additional enrichment entry. |
| D:[normative]:[reviewing] | normative | reviewing | audit ready boundary | 0 | NO_ITEMS | audit ready boundary is traceable in the production set for normative/reviewing without an additional enrichment entry. |
| D:[operative]:[guiding] | operative | guiding | procedural state closure | 0 | NO_ITEMS | procedural state closure is traceable in the production set for operative/guiding without an additional enrichment entry. |
| D:[operative]:[applying] | operative | applying | practical interaction control | 1 | HAS_ITEMS | Lensing practical interaction control identifies 1 production follow-up entry for operative/applying. |
| D:[operative]:[judging] | operative | judging | performance proof basis | 0 | NO_ITEMS | performance proof basis is traceable in the production set for operative/judging without an additional enrichment entry. |
| D:[operative]:[reviewing] | operative | reviewing | process review boundary | 0 | NO_ITEMS | process review boundary is traceable in the production set for operative/reviewing without an additional enrichment entry. |
| D:[evaluative]:[guiding] | evaluative | guiding | value aligned closure | 0 | NO_ITEMS | value aligned closure is traceable in the production set for evaluative/guiding without an additional enrichment entry. |
| D:[evaluative]:[applying] | evaluative | applying | merit based control | 0 | NO_ITEMS | merit based control is traceable in the production set for evaluative/applying without an additional enrichment entry. |
| D:[evaluative]:[judging] | evaluative | judging | worth resolution basis | 0 | NO_ITEMS | worth resolution basis is traceable in the production set for evaluative/judging without an additional enrichment entry. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal boundary | 1 | HAS_ITEMS | Lensing quality appraisal boundary identifies 1 production follow-up entry for evaluative/reviewing. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | VerificationGap | Procedure | Procedure | Record selected implementation files or review notes for Toolkit controls and pane resize/collapse behavior. | Procedure records for Toolkit controls and pane behavior are TBD, so practical interaction control lacks closure evidence. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Procedure.md | Procedure.md#records |  | PROPOSAL | TBD |
| D-002 | D:[evaluative]:[reviewing] | RationaleGap | Specification | Guidance | Identify the accepted polish checklist or review rubric for the professional dense interface requirement. | The UI quality requirement cites accepted polish planning, but the exact checklist location is still TBD. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md | Specification.md#verification |  | PROPOSAL | TBD |

## Matrix X - Synthesis (4x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | directed factual basis | 0 | NO_ITEMS | directed factual basis is traceable in the production set for guiding/necessity without an additional enrichment entry. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | adequate intent support | 0 | NO_ITEMS | adequate intent support is traceable in the production set for guiding/sufficiency without an additional enrichment entry. |
| X:[guiding]:[completeness] | guiding | completeness | complete orientation record | 0 | NO_ITEMS | complete orientation record is traceable in the production set for guiding/completeness without an additional enrichment entry. |
| X:[guiding]:[consistency] | guiding | consistency | reliable direction signal | 0 | NO_ITEMS | reliable direction signal is traceable in the production set for guiding/consistency without an additional enrichment entry. |
| X:[applying]:[necessity] | applying | necessity | practice ready fact | 0 | NO_ITEMS | practice ready fact is traceable in the production set for applying/necessity without an additional enrichment entry. |
| X:[applying]:[sufficiency] | applying | sufficiency | contextual execution support | 0 | NO_ITEMS | contextual execution support is traceable in the production set for applying/sufficiency without an additional enrichment entry. |
| X:[applying]:[completeness] | applying | completeness | complete action account | 0 | NO_ITEMS | complete action account is traceable in the production set for applying/completeness without an additional enrichment entry. |
| X:[applying]:[consistency] | applying | consistency | coherent control message | 0 | NO_ITEMS | coherent control message is traceable in the production set for applying/consistency without an additional enrichment entry. |
| X:[judging]:[necessity] | judging | necessity | evidence based finding | 0 | NO_ITEMS | evidence based finding is traceable in the production set for judging/necessity without an additional enrichment entry. |
| X:[judging]:[sufficiency] | judging | sufficiency | competent assessment basis | 0 | NO_ITEMS | competent assessment basis is traceable in the production set for judging/sufficiency without an additional enrichment entry. |
| X:[judging]:[completeness] | judging | completeness | complete proof mastery | 0 | NO_ITEMS | complete proof mastery is traceable in the production set for judging/completeness without an additional enrichment entry. |
| X:[judging]:[consistency] | judging | consistency | coherent verdict rationale | 0 | NO_ITEMS | coherent verdict rationale is traceable in the production set for judging/consistency without an additional enrichment entry. |
| X:[reviewing]:[necessity] | reviewing | necessity | traceable audit fact | 0 | NO_ITEMS | traceable audit fact is traceable in the production set for reviewing/necessity without an additional enrichment entry. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | adequate review context | 1 | HAS_ITEMS | Lensing adequate review context identifies 1 production follow-up entry for reviewing/sufficiency. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete inspection account | 0 | NO_ITEMS | complete inspection account is traceable in the production set for reviewing/completeness without an additional enrichment entry. |
| X:[reviewing]:[consistency] | reviewing | consistency | coherent appraisal rationale | 0 | NO_ITEMS | coherent appraisal rationale is traceable in the production set for reviewing/consistency without an additional enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[sufficiency] | TBD_Question | Guidance | NA | Who resolves the PRD hash mismatch, and what snapshot or ruling closes source reconciliation? | Guidance states a human ruling is needed before final package closure, but no owner or closure artifact is identified. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Guidance.md | Guidance.md#rulings-needed |  | PROPOSAL | TBD |

## Matrix E - Evaluation (4x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | fact based orientation | 0 | NO_ITEMS | fact based orientation is traceable in the production set for guiding/data without an additional enrichment entry. |
| E:[guiding]:[information] | guiding | information | signal based direction | 0 | NO_ITEMS | signal based direction is traceable in the production set for guiding/information without an additional enrichment entry. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding led guidance | 0 | NO_ITEMS | understanding led guidance is traceable in the production set for guiding/knowledge without an additional enrichment entry. |
| E:[guiding]:[wisdom] | guiding | wisdom | discernment led framing | 0 | NO_ITEMS | discernment led framing is traceable in the production set for guiding/wisdom without an additional enrichment entry. |
| E:[applying]:[data] | applying | data | fact ready practice | 0 | NO_ITEMS | fact ready practice is traceable in the production set for applying/data without an additional enrichment entry. |
| E:[applying]:[information] | applying | information | context ready action | 0 | NO_ITEMS | context ready action is traceable in the production set for applying/information without an additional enrichment entry. |
| E:[applying]:[knowledge] | applying | knowledge | expertise driven execution | 1 | HAS_ITEMS | Lensing expertise driven execution identifies 1 production follow-up entry for applying/knowledge. |
| E:[applying]:[wisdom] | applying | wisdom | judgment ready conduct | 0 | NO_ITEMS | judgment ready conduct is traceable in the production set for applying/wisdom without an additional enrichment entry. |
| E:[judging]:[data] | judging | data | evidence ready finding | 1 | HAS_ITEMS | Lensing evidence ready finding identifies 1 production follow-up entry for judging/data. |
| E:[judging]:[information] | judging | information | message aware assessment | 0 | NO_ITEMS | message aware assessment is traceable in the production set for judging/information without an additional enrichment entry. |
| E:[judging]:[knowledge] | judging | knowledge | mastery based verdict | 0 | NO_ITEMS | mastery based verdict is traceable in the production set for judging/knowledge without an additional enrichment entry. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned merit finding | 0 | NO_ITEMS | reasoned merit finding is traceable in the production set for judging/wisdom without an additional enrichment entry. |
| E:[reviewing]:[data] | reviewing | data | record ready audit | 0 | NO_ITEMS | record ready audit is traceable in the production set for reviewing/data without an additional enrichment entry. |
| E:[reviewing]:[information] | reviewing | information | contextual inspection basis | 0 | NO_ITEMS | contextual inspection basis is traceable in the production set for reviewing/information without an additional enrichment entry. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery informed appraisal | 0 | NO_ITEMS | mastery informed appraisal is traceable in the production set for reviewing/knowledge without an additional enrichment entry. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled review judgment | 0 | NO_ITEMS | principled review judgment is traceable in the production set for reviewing/wisdom without an additional enrichment entry. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[applying]:[knowledge] | MissingSlot | Specification | Specification | List the runtime-supported Toolkit option inventory or mark unavailable controls explicitly. | Specification assumes controls present only supported runtime option fields, but exact control inventory remains TBD. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Specification.md | Specification.md#assumptions-and-tbds |  | PROPOSAL | TBD |
| E-002 | E:[judging]:[data] | VerificationGap | Procedure | Procedure | Populate implementation or test records for local-state non-authority, fallback behavior, accessibility, and storage guards. | Procedure verification expectations are present, but records for implementation notes and test evidence remain TBD. | /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/Procedure.md | Procedure.md#records |  | PROPOSAL | TBD |
