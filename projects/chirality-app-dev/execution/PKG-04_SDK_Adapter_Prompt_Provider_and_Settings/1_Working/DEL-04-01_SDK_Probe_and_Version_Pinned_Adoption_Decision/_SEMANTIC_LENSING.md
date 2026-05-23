# Semantic Lensing Register: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_CONTEXT.md#Identity
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_STATUS.md#History
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_SEMANTIC.md#Matrix A - Orientation (3x4) - Canonical
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Datasheet.md#Attributes
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Specification.md#Requirements
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Guidance.md#Principles
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Procedure.md#Steps
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_REFERENCES.md#Authoritative Source Corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 14
- By document:
  - Datasheet: 0
  - Specification: 6
  - Guidance: 3
  - Procedure: 3
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
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Direction role is represented by SDK-as-replaceable-substrate framing and no additional prescription gap surfaced. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | Mandatory-practice role is carried by MUST requirements without a separate practice conflict. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Compliance judgment role is expressed through adoption decision and verification checks without a new item here. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Source-state conflict affects audit readiness and requires a human ruling before closure. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Procedure gives operational probe direction and no separate procedural-direction issue surfaced. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Execution practice is deferred to probe steps and downstream code slices without an added register item. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Performance assessment is represented by probe verification rows; detailed evidence gaps are registered under X. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Process audit posture is present in Procedure verification and dependency warnings without a distinct issue. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Value orientation appears in fallback and reliance-boundary principles without a separate item. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Merit application is deferred to the adoption verdict and fallback threshold items. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Worth determination remains tied to the adoption verdict item under E. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Quality appraisal is handled through residual-risk review items under E. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Guidance | Guidance | Carry REF-006 source-state conflict as a closure blocker until human/source refresh resolves or accepts PRD hash mismatch. | Guidance records SRC-001 because PRD content is useful but _REFERENCES marks docs/PRD.md HASH_MISMATCH. A reviewing/regulatory lens requires the conflict to remain visible before closure. | Guidance.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus | _REFERENCES.md#REF-006; Guidance.md#Conflict Table (for human ruling) | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 1 | HAS_ITEMS | essential fact lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | comprehensive record lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[necessity] | MissingSlot | Specification | Specification | Exact @anthropic-ai/claude-agent-sdk version and Claude Code subprocess version remain TBD pending probe evidence. | Specification requires exact version evidence, while Datasheet records adoption decision state as TBD. The essential-fact lens exposes a required data slot that cannot be inferred from roadmap text. | Specification.md; Datasheet.md | Specification.md#Requirements; Datasheet.md#Attributes |  | PROPOSAL | TBD |
| B-002 | B:[data]:[completeness] | MissingSlot | Procedure | Procedure | Probe record needs lockfile/package evidence and subprocess version capture location once implementation begins. | Procedure step 3 tells the operator to capture version evidence but the current records do not name the evidence file or captured values. The comprehensive-record lens marks this as incomplete rather than assumed. | Procedure.md; Specification.md | Procedure.md#Steps; Specification.md#Verification |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding evidence basis | 0 | NO_ITEMS | binding evidence basis lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate governance context | 0 | NO_ITEMS | adequate governance context lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[normative]:[completeness] | normative | completeness | complete compliance record | 0 | NO_ITEMS | complete compliance record lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[normative]:[consistency] | normative | consistency | coherent control rationale | 1 | HAS_ITEMS | coherent control rationale lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| C:[operative]:[necessity] | operative | necessity | actionable evidence basis | 0 | NO_ITEMS | actionable evidence basis lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[operative]:[sufficiency] | operative | sufficiency | sufficient execution context | 0 | NO_ITEMS | sufficient execution context lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[operative]:[completeness] | operative | completeness | complete process record | 0 | NO_ITEMS | complete process record lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[operative]:[consistency] | operative | consistency | coherent process rationale | 0 | NO_ITEMS | coherent process rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[evaluative]:[necessity] | evaluative | necessity | value evidence basis | 0 | NO_ITEMS | value evidence basis lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate appraisal context | 0 | NO_ITEMS | adequate appraisal context lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete quality record | 0 | NO_ITEMS | complete quality record lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent merit rationale | 0 | NO_ITEMS | coherent merit rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[consistency] | RationaleGap | Guidance | Guidance | State why corroborated PRD claims may remain draft context while source-state closure stays blocked. | Guidance warns about REF-006 and includes a proposed authority treatment, but the rationale for using corroborated PRD claims before closure is terse. The coherent-control-rationale lens calls for explicit reasoning. | Guidance.md; _REFERENCES.md | Guidance.md#Considerations; _REFERENCES.md#Authoritative Source Corpus |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | binding acceptance basis | 0 | NO_ITEMS | binding acceptance basis lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[normative]:[sufficiency] | normative | sufficiency | sufficient control proof | 1 | HAS_ITEMS | sufficient control proof lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| F:[normative]:[completeness] | normative | completeness | complete governance dossier | 0 | NO_ITEMS | complete governance dossier lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[normative]:[consistency] | normative | consistency | coherent approval rationale | 0 | NO_ITEMS | coherent approval rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[operative]:[necessity] | operative | necessity | actionable probe basis | 0 | NO_ITEMS | actionable probe basis lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[operative]:[sufficiency] | operative | sufficiency | sufficient execution proof | 1 | HAS_ITEMS | sufficient execution proof lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| F:[operative]:[completeness] | operative | completeness | complete implementation dossier | 0 | NO_ITEMS | complete implementation dossier lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[operative]:[consistency] | operative | consistency | coherent delivery rationale | 0 | NO_ITEMS | coherent delivery rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[evaluative]:[necessity] | evaluative | necessity | value decision basis | 0 | NO_ITEMS | value decision basis lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | sufficient risk proof | 0 | NO_ITEMS | sufficient risk proof lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete residual dossier | 1 | HAS_ITEMS | complete residual dossier lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| F:[evaluative]:[consistency] | evaluative | consistency | coherent merit rationale | 0 | NO_ITEMS | coherent merit rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Add acceptance detail for proving shipped SDK options use settingSources: [] and do not load user/local settings. | Specification requires the settings isolation probe, but the required evidence form is still only described at a high level. The sufficient-control-proof lens asks for the proof threshold. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Verification |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[sufficiency] | VerificationGap | Specification | Specification | Define permission-probe evidence rows for allowedTools, disallowedTools, permissionMode, canUseTool, hooks, and deny-first overlay outcome. | The documents require permission behavior testing and warn that allowedTools is not a restriction boundary, but they do not yet define the minimal passing evidence row set. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Guidance.md#Principles; Procedure.md#Steps |  | PROPOSAL | TBD |
| F-003 | F:[evaluative]:[completeness] | MissingSlot | Procedure | Procedure | Record Electron packaging result, subprocess path behavior, asarUnpack/signing needs, environment handling, and residual-risk verdict. | Procedure step 10 requires packaging probing, but current records mark exact packaging requirements and results as TBD. The complete-residual-dossier lens exposes an unresolved residual record slot. | Procedure.md; Specification.md | Procedure.md#Steps; Specification.md#Documentation |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governed adoption direction | 1 | HAS_ITEMS | governed adoption direction lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| D:[normative]:[applying] | normative | applying | controlled adoption practice | 0 | NO_ITEMS | controlled adoption practice lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[normative]:[judging] | normative | judging | closed conformance judgment | 0 | NO_ITEMS | closed conformance judgment lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[normative]:[reviewing] | normative | reviewing | auditable release review | 0 | NO_ITEMS | auditable release review lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[operative]:[guiding] | operative | guiding | probe execution direction | 0 | NO_ITEMS | probe execution direction lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[operative]:[applying] | operative | applying | settings isolation practice | 0 | NO_ITEMS | settings isolation practice lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[operative]:[judging] | operative | judging | observed performance judgment | 0 | NO_ITEMS | observed performance judgment lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[operative]:[reviewing] | operative | reviewing | process evidence review | 1 | HAS_ITEMS | process evidence review lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| D:[evaluative]:[guiding] | evaluative | guiding | risk value direction | 0 | NO_ITEMS | risk value direction lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[evaluative]:[applying] | evaluative | applying | fallback decision practice | 0 | NO_ITEMS | fallback decision practice lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[evaluative]:[judging] | evaluative | judging | resolved worth judgment | 0 | NO_ITEMS | resolved worth judgment lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality evidence review | 0 | NO_ITEMS | quality evidence review lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[normative]:[guiding] | TBD_Question | Specification | Specification | Who approves ADOPT, ADOPT_WITH_RESIDUAL_RISK, or FALLBACK after probe evidence is complete? | Procedure says to draft a version-pinned adoption decision but ownership and final verdict remain TBD. The governed-adoption-direction lens requires human decision routing. | Procedure.md; _CONTEXT.md | Procedure.md#Steps; _CONTEXT.md#Identity |  | PROPOSAL | TBD |
| D-002 | D:[operative]:[reviewing] | TBD_Question | Procedure | Procedure | Which transcript/store posture will be accepted: SessionStore, CLAUDE_CONFIG_DIR, both, or default-path cross-reference with residual risk? | Guidance and Procedure leave transcript placement unresolved. The process-evidence-review lens turns the unresolved implementation posture into a review question. | Guidance.md; Procedure.md | Guidance.md#Considerations; Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | adoption evidence threshold | 0 | NO_ITEMS | adoption evidence threshold lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | adequate runtime proof | 0 | NO_ITEMS | adequate runtime proof lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[guiding]:[completeness] | guiding | completeness | complete boundary record | 0 | NO_ITEMS | complete boundary record lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[guiding]:[consistency] | guiding | consistency | coherent fallback rationale | 0 | NO_ITEMS | coherent fallback rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[applying]:[necessity] | applying | necessity | practice evidence threshold | 0 | NO_ITEMS | practice evidence threshold lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[applying]:[sufficiency] | applying | sufficiency | adequate settings proof | 0 | NO_ITEMS | adequate settings proof lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[applying]:[completeness] | applying | completeness | complete permission record | 0 | NO_ITEMS | complete permission record lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[applying]:[consistency] | applying | consistency | coherent hook rationale | 1 | HAS_ITEMS | coherent hook rationale lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| X:[judging]:[necessity] | judging | necessity | conformance evidence threshold | 0 | NO_ITEMS | conformance evidence threshold lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate mapping proof | 1 | HAS_ITEMS | adequate mapping proof lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| X:[judging]:[completeness] | judging | completeness | complete event record | 1 | HAS_ITEMS | complete event record lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| X:[judging]:[consistency] | judging | consistency | coherent verdict rationale | 0 | NO_ITEMS | coherent verdict rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit evidence threshold | 0 | NO_ITEMS | audit evidence threshold lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | adequate packaging proof | 0 | NO_ITEMS | adequate packaging proof lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete residual record | 0 | NO_ITEMS | complete residual record lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| X:[reviewing]:[consistency] | reviewing | consistency | coherent review rationale | 0 | NO_ITEMS | coherent review rationale lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Define mapping pass/fail criteria for observed SDK query() messages into stable UIEvent and HarnessEvent categories. | Specification requires message mapping but does not enumerate the acceptance criteria for adequate mapping proof. The judging/sufficiency lens makes this a conformance evidence gap. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Steps |  | PROPOSAL | TBD |
| X-002 | X:[judging]:[completeness] | VerificationGap | Specification | Specification | Require success, failure, interruption, and cancellation terminal event evidence before production default use. | Specification and Procedure require interrupt/cancel behavior, but the current deliverable has no probe result demonstrating complete terminal event persistence. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Verification |  | PROPOSAL | TBD |
| X-003 | X:[applying]:[consistency] | VerificationGap | Multi | Specification | Capture API key active-turn handoff and redaction evidence across logs, events, transcripts, and tool artifacts. | Specification requires API key environment handling and redaction, while Procedure asks for confirmation. The coherent-hook-rationale lens requires consistent evidence across surfaces. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Steps |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | evidence governed facts | 0 | NO_ITEMS | evidence governed facts lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[guiding]:[information] | guiding | information | signal controlled adoption | 0 | NO_ITEMS | signal controlled adoption lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding based direction | 0 | NO_ITEMS | understanding based direction lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[guiding]:[wisdom] | guiding | wisdom | discernment led fallback | 1 | HAS_ITEMS | discernment led fallback lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |
| E:[applying]:[data] | applying | data | settings verified facts | 0 | NO_ITEMS | settings verified facts lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[applying]:[information] | applying | information | contextual practice proof | 0 | NO_ITEMS | contextual practice proof lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[applying]:[knowledge] | applying | knowledge | expertise based execution | 0 | NO_ITEMS | expertise based execution lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[applying]:[wisdom] | applying | wisdom | judgment guided practice | 0 | NO_ITEMS | judgment guided practice lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[judging]:[data] | judging | data | mapped event facts | 0 | NO_ITEMS | mapped event facts lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[judging]:[information] | judging | information | accountable conformance proof | 0 | NO_ITEMS | accountable conformance proof lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[judging]:[knowledge] | judging | knowledge | mastery based verdict | 0 | NO_ITEMS | mastery based verdict lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[judging]:[wisdom] | judging | wisdom | principled risk judgment | 0 | NO_ITEMS | principled risk judgment lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[reviewing]:[data] | reviewing | data | packaging verified facts | 0 | NO_ITEMS | packaging verified facts lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[reviewing]:[information] | reviewing | information | message based audit | 0 | NO_ITEMS | message based audit lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | understanding based review | 0 | NO_ITEMS | understanding based review lens was checked against DEL-04-01 documents; related evidence is handled by more specific probe, decision, or residual-risk lenses. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | reasoned quality appraisal | 1 | HAS_ITEMS | reasoned quality appraisal lens surfaced 1 warranted item(s) for DEL-04-01 evidence enrichment. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[wisdom] | TBD_Question | Multi | Guidance | Which fallback trigger threshold converts SDK uncertainty into custom-runtime fallback rather than residual-risk adoption? | Fallback criteria are required, but the current documents do not yet identify the decision threshold for unverifiable product-critical boundaries. The discernment-led-fallback lens requires a human-governed threshold. | Datasheet.md; Specification.md; Guidance.md; Procedure.md | Datasheet.md#Construction; Specification.md#Requirements; Guidance.md#Purpose; Procedure.md#Steps |  | PROPOSAL | TBD |
| E-002 | E:[reviewing]:[wisdom] | RationaleGap | Guidance | Guidance | Explain residual-risk appraisal method for SDK API drift, settings leakage, transcript location, packaging, SDK boundary, subagents, platform dependency, and lock-in. | Specification lists residual risks and Procedure says to draft notes, but the appraisal method for judging reasoned quality is not yet explicit. The reasoned-quality-appraisal lens warrants a rationale entry. | Specification.md; Guidance.md; Procedure.md | Specification.md#Requirements; Guidance.md#Trade-offs; Procedure.md#Steps |  | PROPOSAL | TBD |
