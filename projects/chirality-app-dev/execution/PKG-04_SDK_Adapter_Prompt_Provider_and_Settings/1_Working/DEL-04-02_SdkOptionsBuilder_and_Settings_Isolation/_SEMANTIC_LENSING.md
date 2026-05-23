# Semantic Lensing Register: DEL-04-02 SdkOptionsBuilder and Settings Isolation

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — validate_lens_register.py returned VALID
**Warnings:** PRD source is available but REF-006 reports HASH_MISMATCH; missing exact SDK probe/type details remain TBD.

**Inputs Read:**
- _CONTEXT.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_CONTEXT.md#Identity
- _STATUS.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_STATUS.md#Current-State
- _SEMANTIC.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_SEMANTIC.md#Matrix-A
- Datasheet.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/Datasheet.md#Attributes
- Specification.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/Specification.md#Requirements
- Guidance.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/Guidance.md#Principles
- Procedure.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/Procedure.md#Steps
- _REFERENCES.md — /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_REFERENCES.md#Authoritative-Source-Corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 14
- By document:
  - Datasheet: 2
  - Specification: 5
  - Guidance: 3
  - Procedure: 2
  - Multi: 2
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
  - Conflict: 1
  - VerificationGap: 4
  - MissingSlot: 4
  - WeakStatement: 1
  - RationaleGap: 2
  - Normalization: 1
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Checked A prescriptive direction against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 1 | HAS_ITEMS | Evidence review under A mandatory practice produced registered item(s) for later enrichment. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Checked A compliance determination against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | Checked A regulatory audit against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Checked A procedural direction against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[operative]:[applying] | operative | applying | practical execution | 1 | HAS_ITEMS | Evidence review under A practical execution produced registered item(s) for later enrichment. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Checked A performance assessment against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Checked A process audit against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Checked A value orientation against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Checked A merit application against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Checked A worth determination against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Checked A quality appraisal against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[applying] | VerificationGap | Specification | Specification | Add an acceptance check that unknown option keys warn without changing resolved SDK behavior. | The applying-normative lens highlights mandatory practice. Specification states the MUST requirement but does not yet name the warning assertion shape or fixture boundary. | Specification.md | Requirements |  | PROPOSAL | TBD |
| A-002 | A:[operative]:[applying] | MissingSlot | Procedure | Procedure | Name the eventual module path or keep a tracked TBD for sdk-options-builder.ts export placement. | The operative applying lens asks how execution will occur. Procedure and Datasheet both leave the implementation module path unresolved. | Procedure.md; Datasheet.md | Records; Construction |  | PROPOSAL | TBD |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | Checked B essential fact against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Checked B adequate evidence against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | Evidence review under B comprehensive record produced registered item(s) for later enrichment. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | Checked B reliable measurement against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Checked B essential signal against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | Checked B adequate context against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | Checked B comprehensive account against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[information]:[consistency] | information | consistency | coherent message | 1 | HAS_ITEMS | Evidence review under B coherent message produced registered item(s) for later enrichment. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Checked B fundamental understanding against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Checked B competent expertise against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Checked B thorough mastery against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Checked B coherent understanding against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Checked B essential discernment against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Checked B adequate judgment against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Checked B holistic insight against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Checked B principled reasoning against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[completeness] | MissingSlot | Datasheet | Datasheet | Record the exact TypeScript input type once the SDK probe and implementation convention are accepted. | The data-completeness lens exposes a missing concrete record. Datasheet explicitly says the exact input type is TBD. | Datasheet.md | Attributes |  | PROPOSAL | TBD |
| B-002 | B:[information]:[consistency] | Conflict | Multi | NA | Keep PRD-backed details under source-state warning until REF-006 hash state is resolved. | The information-consistency lens surfaces that PRD content is used while _REFERENCES reports HASH_MISMATCH. The documents already flag this but the ruling remains TBD. | _REFERENCES.md; Guidance.md | Authoritative Source Corpus; Conflict Table | _REFERENCES.md#Authoritative Source Corpus; Guidance.md#Conflict Table | PROPOSAL | TBD |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding option rationale | 0 | NO_ITEMS | Checked C binding option rationale against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate policy envelope | 0 | NO_ITEMS | Checked C adequate policy envelope against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[normative]:[completeness] | normative | completeness | traceable setting coverage | 0 | NO_ITEMS | Checked C traceable setting coverage against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[normative]:[consistency] | normative | consistency | stable governance signal | 0 | NO_ITEMS | Checked C stable governance signal against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[operative]:[necessity] | operative | necessity | required runtime input | 1 | HAS_ITEMS | Evidence review under C required runtime input produced registered item(s) for later enrichment. |
| C:[operative]:[sufficiency] | operative | sufficiency | sufficient builder context | 0 | NO_ITEMS | Checked C sufficient builder context against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[operative]:[completeness] | operative | completeness | complete option assembly | 0 | NO_ITEMS | Checked C complete option assembly against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[operative]:[consistency] | operative | consistency | repeatable execution shape | 0 | NO_ITEMS | Checked C repeatable execution shape against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[evaluative]:[necessity] | evaluative | necessity | decision quality basis | 0 | NO_ITEMS | Checked C decision quality basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate adapter judgment | 1 | HAS_ITEMS | Evidence review under C adequate adapter judgment produced registered item(s) for later enrichment. |
| C:[evaluative]:[completeness] | evaluative | completeness | holistic posture review | 0 | NO_ITEMS | Checked C holistic posture review against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent value rationale | 0 | NO_ITEMS | Checked C coherent value rationale against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[necessity] | MissingSlot | Specification | Specification | Define the required runtime input object fields or reference the owning adjacent contracts for persona, session, hooks, MCP, and settings policy. | The required runtime input lens finds that scope lists inputs but exact TypeScript input shape remains TBD. | Specification.md; Datasheet.md | Scope; Attributes |  | PROPOSAL | TBD |
| C-002 | C:[evaluative]:[sufficiency] | RationaleGap | Guidance | Guidance | Add a short rationale for how the builder judges adapter-policy adequacy before constructing SDK options. | Guidance states principles but does not spell out the adequacy decision for accepting policy inputs versus failing closed. | Guidance.md | Principles; Considerations |  | PROPOSAL | TBD |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | mandatory isolation basis | 0 | NO_ITEMS | Checked F mandatory isolation basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[normative]:[sufficiency] | normative | sufficiency | validated policy adequacy | 0 | NO_ITEMS | Checked F validated policy adequacy against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[normative]:[completeness] | normative | completeness | complete compliance record | 1 | HAS_ITEMS | Evidence review under F complete compliance record produced registered item(s) for later enrichment. |
| F:[normative]:[consistency] | normative | consistency | consistent rule expression | 0 | NO_ITEMS | Checked F consistent rule expression against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[operative]:[necessity] | operative | necessity | required builder behavior | 0 | NO_ITEMS | Checked F required builder behavior against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[operative]:[sufficiency] | operative | sufficiency | sufficient runtime evidence | 0 | NO_ITEMS | Checked F sufficient runtime evidence against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[operative]:[completeness] | operative | completeness | complete assembly proof | 0 | NO_ITEMS | Checked F complete assembly proof against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[operative]:[consistency] | operative | consistency | stable execution evidence | 1 | HAS_ITEMS | Evidence review under F stable execution evidence produced registered item(s) for later enrichment. |
| F:[evaluative]:[necessity] | evaluative | necessity | necessary risk rationale | 0 | NO_ITEMS | Checked F necessary risk rationale against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate judgment basis | 0 | NO_ITEMS | Checked F adequate judgment basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete review rationale | 0 | NO_ITEMS | Checked F complete review rationale against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| F:[evaluative]:[consistency] | evaluative | consistency | coherent acceptance basis | 0 | NO_ITEMS | Checked F coherent acceptance basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[completeness] | VerificationGap | Specification | Specification | Add evidence expectations that shipped, development-project, user, and local settings-source cases are each covered. | The complete compliance record lens points to settings isolation tests, but the expected evidence does not enumerate all forbidden and permitted setting-source cases. | Specification.md; Procedure.md | Verification; Steps |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[consistency] | VerificationGap | Specification | Specification | Add a deterministic-order fixture covering tools, MCP server IDs, allow/deny lists, and permission policy inputs together. | Stable execution evidence requires a composite fixture. Current verification mentions deterministic ordering and permission posture in separate checks. | Specification.md; Procedure.md | Verification; Verification |  | PROPOSAL | TBD |

## Matrix D — Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governed option closure | 0 | NO_ITEMS | Checked D governed option closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[normative]:[applying] | normative | applying | enforced isolation closure | 1 | HAS_ITEMS | Evidence review under D enforced isolation closure produced registered item(s) for later enrichment. |
| D:[normative]:[judging] | normative | judging | verified policy closure | 0 | NO_ITEMS | Checked D verified policy closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[normative]:[reviewing] | normative | reviewing | auditable rule closure | 0 | NO_ITEMS | Checked D auditable rule closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[operative]:[guiding] | operative | guiding | directed builder closure | 0 | NO_ITEMS | Checked D directed builder closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[operative]:[applying] | operative | applying | implemented runtime closure | 0 | NO_ITEMS | Checked D implemented runtime closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[operative]:[judging] | operative | judging | measured assembly closure | 0 | NO_ITEMS | Checked D measured assembly closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[operative]:[reviewing] | operative | reviewing | inspected process closure | 1 | HAS_ITEMS | Evidence review under D inspected process closure produced registered item(s) for later enrichment. |
| D:[evaluative]:[guiding] | evaluative | guiding | oriented risk closure | 0 | NO_ITEMS | Checked D oriented risk closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[evaluative]:[applying] | evaluative | applying | applied judgment closure | 0 | NO_ITEMS | Checked D applied judgment closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[evaluative]:[judging] | evaluative | judging | determined acceptance closure | 0 | NO_ITEMS | Checked D determined acceptance closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | appraised quality closure | 0 | NO_ITEMS | Checked D appraised quality closure against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[normative]:[applying] | WeakStatement | Guidance | Guidance | Clarify whether development project settings are rejected at builder input validation or omitted from shipped option construction. | The enforced isolation closure lens finds a release boundary principle, but the operational enforcement point is still implicit. | Guidance.md; Procedure.md | Principles; Steps |  | PROPOSAL | TBD |
| D-002 | D:[operative]:[reviewing] | MissingSlot | Procedure | Procedure | Identify the targeted test command or validation suite once the implementation path exists. | The inspected process closure lens needs an executable verification route. Procedure names tests but leaves concrete command records for later implementation. | Procedure.md | Records; Verification |  | PROPOSAL | TBD |

## Matrix X — Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | required governance proof | 0 | NO_ITEMS | Checked X required governance proof against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | sufficient direction evidence | 0 | NO_ITEMS | Checked X sufficient direction evidence against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[guiding]:[completeness] | guiding | completeness | complete closure trace | 0 | NO_ITEMS | Checked X complete closure trace against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[guiding]:[consistency] | guiding | consistency | consistent posture signal | 0 | NO_ITEMS | Checked X consistent posture signal against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[applying]:[necessity] | applying | necessity | required implementation proof | 0 | NO_ITEMS | Checked X required implementation proof against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[applying]:[sufficiency] | applying | sufficiency | sufficient execution basis | 0 | NO_ITEMS | Checked X sufficient execution basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[applying]:[completeness] | applying | completeness | complete behavior trace | 1 | HAS_ITEMS | Evidence review under X complete behavior trace produced registered item(s) for later enrichment. |
| X:[applying]:[consistency] | applying | consistency | consistent option behavior | 0 | NO_ITEMS | Checked X consistent option behavior against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[judging]:[necessity] | judging | necessity | required validation proof | 1 | HAS_ITEMS | Evidence review under X required validation proof produced registered item(s) for later enrichment. |
| X:[judging]:[sufficiency] | judging | sufficiency | sufficient assessment basis | 0 | NO_ITEMS | Checked X sufficient assessment basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[judging]:[completeness] | judging | completeness | complete decision trace | 0 | NO_ITEMS | Checked X complete decision trace against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[judging]:[consistency] | judging | consistency | consistent verdict basis | 0 | NO_ITEMS | Checked X consistent verdict basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[reviewing]:[necessity] | reviewing | necessity | required audit proof | 0 | NO_ITEMS | Checked X required audit proof against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | sufficient inspection basis | 0 | NO_ITEMS | Checked X sufficient inspection basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete review trace | 0 | NO_ITEMS | Checked X complete review trace against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| X:[reviewing]:[consistency] | reviewing | consistency | consistent oversight basis | 0 | NO_ITEMS | Checked X consistent oversight basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[applying]:[completeness] | VerificationGap | Specification | Specification | Add a visible metadata fixture that proves safe fields are present and secrets or API keys are absent. | The complete behavior trace lens links visible metadata and redaction requirements; current verification lists both but not a single fixture tying them together. | Specification.md; Datasheet.md | Verification; Construction |  | PROPOSAL | TBD |
| X-002 | X:[judging]:[necessity] | TBD_Question | Multi | TBD | Which adjacent deliverable owns the terminal max-turn error fixture consumed by this builder validation? | Required validation proof depends on runtime/event handoff, but the exact terminal event fixture is marked TBD and owned by adjacent deliverables. | Specification.md; Procedure.md | Verification; Steps |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | governance fact basis | 1 | HAS_ITEMS | Evidence review under E governance fact basis produced registered item(s) for later enrichment. |
| E:[guiding]:[information] | guiding | information | directional context basis | 0 | NO_ITEMS | Checked E directional context basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[guiding]:[knowledge] | guiding | knowledge | governed understanding basis | 0 | NO_ITEMS | Checked E governed understanding basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled direction basis | 0 | NO_ITEMS | Checked E principled direction basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[applying]:[data] | applying | data | implementation fact basis | 0 | NO_ITEMS | Checked E implementation fact basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[applying]:[information] | applying | information | execution context basis | 0 | NO_ITEMS | Checked E execution context basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[applying]:[knowledge] | applying | knowledge | practical mastery basis | 0 | NO_ITEMS | Checked E practical mastery basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[applying]:[wisdom] | applying | wisdom | judged execution basis | 0 | NO_ITEMS | Checked E judged execution basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[judging]:[data] | judging | data | validation fact basis | 0 | NO_ITEMS | Checked E validation fact basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[judging]:[information] | judging | information | assessment context basis | 0 | NO_ITEMS | Checked E assessment context basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[judging]:[knowledge] | judging | knowledge | competence verdict basis | 0 | NO_ITEMS | Checked E competence verdict basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned verdict basis | 0 | NO_ITEMS | Checked E reasoned verdict basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[reviewing]:[data] | reviewing | data | audit fact basis | 0 | NO_ITEMS | Checked E audit fact basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[reviewing]:[information] | reviewing | information | inspection context basis | 0 | NO_ITEMS | Checked E inspection context basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | review mastery basis | 0 | NO_ITEMS | Checked E review mastery basis against builder scope, settings posture, tool mapping, metadata, and TBD markers; current documents give a traceable statement for this lens. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | quality reasoning basis | 1 | HAS_ITEMS | Evidence review under E quality reasoning basis produced registered item(s) for later enrichment. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[data] | Normalization | Datasheet | Guidance | Normalize SDK package version wording so it is adapter metadata, not a public product-version authority. | The governance fact basis lens flags safe metadata wording. Documents allow SDK package version in metadata while warning that SDK-specific details must not define public semantics. | Datasheet.md; Guidance.md | Attributes; Principles |  | PROPOSAL | TBD |
| E-002 | E:[reviewing]:[wisdom] | RationaleGap | Guidance | Guidance | Capture the review rationale for treating exact SDK option property names as TBD until DEL-04-01 probe evidence is accepted. | The quality reasoning basis lens finds the rule in multiple places, but a concise review rationale would help later authors avoid filling SDK fields prematurely. | Specification.md; Guidance.md; Procedure.md | Requirements; Principles; Prerequisites |  | PROPOSAL | TBD |
