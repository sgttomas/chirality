# Semantic Lensing Register: DEL-04-04 PersonaComposer from Instruction Root

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py ran after generation and returned VALID.
**Warnings:** PRD_HASH_MISMATCH from _REFERENCES.md preserved; dependency-state normalization item recorded without editing dependency files.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/_CONTEXT.md#Identity
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/_STATUS.md#Current State
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/_SEMANTIC.md#Matrix A - Orientation
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Datasheet.md#Identification
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Specification.md#Scope
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Guidance.md#Purpose
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/Procedure.md#Purpose
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root/_REFERENCES.md#Authoritative Source Corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 6
- By document:
  - Datasheet: 0
  - Specification: 1
  - Guidance: 1
  - Procedure: 1
  - Multi: 3
  - NA: 0
- By matrix:
  - A: 1
  - B: 1
  - C: 0
  - F: 1
  - D: 1
  - X: 1
  - E: 1
- By type:
  - Conflict: 1
  - VerificationGap: 1
  - MissingSlot: 1
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 1
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction was checked against the production set without a distinct enrichment input under this lens. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice was checked against the production set without a distinct enrichment input under this lens. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination was checked against the production set without a distinct enrichment input under this lens. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | regulatory audit exposes 1 warranted enrichment input recorded below. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction was checked against the production set without a distinct enrichment input under this lens. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution was checked against the production set without a distinct enrichment input under this lens. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment was checked against the production set without a distinct enrichment input under this lens. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit was checked against the production set without a distinct enrichment input under this lens. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation was checked against the production set without a distinct enrichment input under this lens. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application was checked against the production set without a distinct enrichment input under this lens. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination was checked against the production set without a distinct enrichment input under this lens. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal was checked against the production set without a distinct enrichment input under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Resolve whether PRD-derived persona error and fingerprint details may be promoted while REF-006 remains HASH_MISMATCH. | Guidance CT-001 records a PRD hash mismatch, while Specification requirements retain PRD-derived details with warnings. The later enrichment pass needs a human ruling before those details are treated as stable authority. | Guidance.md; Specification.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); Specification.md#Requirements; _REFERENCES.md#Authoritative Source Corpus | Guidance.md#Conflict Table (for human ruling); Specification.md#Requirements; _REFERENCES.md#Authoritative Source Corpus | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact was checked against the production set without a distinct enrichment input under this lens. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence was checked against the production set without a distinct enrichment input under this lens. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record was checked against the production set without a distinct enrichment input under this lens. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement was checked against the production set without a distinct enrichment input under this lens. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal was checked against the production set without a distinct enrichment input under this lens. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context was checked against the production set without a distinct enrichment input under this lens. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account was checked against the production set without a distinct enrichment input under this lens. |
| B:[information]:[consistency] | information | consistency | coherent message | 1 | HAS_ITEMS | coherent message exposes 1 warranted enrichment input recorded below. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding was checked against the production set without a distinct enrichment input under this lens. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise was checked against the production set without a distinct enrichment input under this lens. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery was checked against the production set without a distinct enrichment input under this lens. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding was checked against the production set without a distinct enrichment input under this lens. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment was checked against the production set without a distinct enrichment input under this lens. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment was checked against the production set without a distinct enrichment input under this lens. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight was checked against the production set without a distinct enrichment input under this lens. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning was checked against the production set without a distinct enrichment input under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[information]:[consistency] | Normalization | Multi | Datasheet; Procedure | Normalize dependency wording that still says dependencies are TBD after the extracted dependency register is available. | Datasheet Conditions and Procedure Prerequisites preserve TBD dependency language, while the deliverable-local dependency register now lists active extracted edges. This creates a terminology/state mismatch for a later enrichment pass to reconcile without editing dependency files in this run. | Datasheet.md; Procedure.md; _DEPENDENCIES.md | Datasheet.md#Conditions; Procedure.md#Prerequisites; _DEPENDENCIES.md#Extracted Dependency Register |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding prompt rationale | 0 | NO_ITEMS | binding prompt rationale was checked against the production set without a distinct enrichment input under this lens. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate governance context | 0 | NO_ITEMS | adequate governance context was checked against the production set without a distinct enrichment input under this lens. |
| C:[normative]:[completeness] | normative | completeness | traceable instruction coverage | 0 | NO_ITEMS | traceable instruction coverage was checked against the production set without a distinct enrichment input under this lens. |
| C:[normative]:[consistency] | normative | consistency | stable persona signal | 0 | NO_ITEMS | stable persona signal was checked against the production set without a distinct enrichment input under this lens. |
| C:[operative]:[necessity] | operative | necessity | required composer input | 0 | NO_ITEMS | required composer input was checked against the production set without a distinct enrichment input under this lens. |
| C:[operative]:[sufficiency] | operative | sufficiency | sufficient assembly context | 0 | NO_ITEMS | sufficient assembly context was checked against the production set without a distinct enrichment input under this lens. |
| C:[operative]:[completeness] | operative | completeness | complete prompt assembly | 0 | NO_ITEMS | complete prompt assembly was checked against the production set without a distinct enrichment input under this lens. |
| C:[operative]:[consistency] | operative | consistency | repeatable prompt shape | 0 | NO_ITEMS | repeatable prompt shape was checked against the production set without a distinct enrichment input under this lens. |
| C:[evaluative]:[necessity] | evaluative | necessity | decision quality basis | 0 | NO_ITEMS | decision quality basis was checked against the production set without a distinct enrichment input under this lens. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate boundary judgment | 0 | NO_ITEMS | adequate boundary judgment was checked against the production set without a distinct enrichment input under this lens. |
| C:[evaluative]:[completeness] | evaluative | completeness | holistic prompt review | 0 | NO_ITEMS | holistic prompt review was checked against the production set without a distinct enrichment input under this lens. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent reliance rationale | 0 | NO_ITEMS | coherent reliance rationale was checked against the production set without a distinct enrichment input under this lens. |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | mandatory source basis | 0 | NO_ITEMS | mandatory source basis was checked against the production set without a distinct enrichment input under this lens. |
| F:[normative]:[sufficiency] | normative | sufficiency | validated governance adequacy | 0 | NO_ITEMS | validated governance adequacy was checked against the production set without a distinct enrichment input under this lens. |
| F:[normative]:[completeness] | normative | completeness | complete authority record | 0 | NO_ITEMS | complete authority record was checked against the production set without a distinct enrichment input under this lens. |
| F:[normative]:[consistency] | normative | consistency | consistent persona rule | 0 | NO_ITEMS | consistent persona rule was checked against the production set without a distinct enrichment input under this lens. |
| F:[operative]:[necessity] | operative | necessity | required composition behavior | 0 | NO_ITEMS | required composition behavior was checked against the production set without a distinct enrichment input under this lens. |
| F:[operative]:[sufficiency] | operative | sufficiency | sufficient runtime evidence | 1 | HAS_ITEMS | sufficient runtime evidence exposes 1 warranted enrichment input recorded below. |
| F:[operative]:[completeness] | operative | completeness | complete assembly proof | 0 | NO_ITEMS | complete assembly proof was checked against the production set without a distinct enrichment input under this lens. |
| F:[operative]:[consistency] | operative | consistency | stable prompt evidence | 0 | NO_ITEMS | stable prompt evidence was checked against the production set without a distinct enrichment input under this lens. |
| F:[evaluative]:[necessity] | evaluative | necessity | necessary reliance rationale | 0 | NO_ITEMS | necessary reliance rationale was checked against the production set without a distinct enrichment input under this lens. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate boundary basis | 0 | NO_ITEMS | adequate boundary basis was checked against the production set without a distinct enrichment input under this lens. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete review rationale | 0 | NO_ITEMS | complete review rationale was checked against the production set without a distinct enrichment input under this lens. |
| F:[evaluative]:[consistency] | evaluative | consistency | coherent acceptance basis | 0 | NO_ITEMS | coherent acceptance basis was checked against the production set without a distinct enrichment input under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[sufficiency] | VerificationGap | Specification | Specification | Split boot-fingerprint verification between available composer inputs and adjacent optional inputs that remain TBD. | PC-REQ-010 and its verification approach enumerate many fingerprint inputs, but adjacent slices still own some of those shapes. A later pass should avoid making unavailable inputs look immediately testable. | Specification.md | Specification.md#Requirements; Specification.md#Verification |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governed prompt closure | 0 | NO_ITEMS | governed prompt closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[normative]:[applying] | normative | applying | enforced source closure | 0 | NO_ITEMS | enforced source closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[normative]:[judging] | normative | judging | verified authority closure | 0 | NO_ITEMS | verified authority closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[normative]:[reviewing] | normative | reviewing | auditable persona closure | 0 | NO_ITEMS | auditable persona closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[operative]:[guiding] | operative | guiding | directed composer closure | 0 | NO_ITEMS | directed composer closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[operative]:[applying] | operative | applying | implemented assembly closure | 1 | HAS_ITEMS | implemented assembly closure exposes 1 warranted enrichment input recorded below. |
| D:[operative]:[judging] | operative | judging | measured prompt closure | 0 | NO_ITEMS | measured prompt closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[operative]:[reviewing] | operative | reviewing | inspected process closure | 0 | NO_ITEMS | inspected process closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[evaluative]:[guiding] | evaluative | guiding | oriented reliance closure | 0 | NO_ITEMS | oriented reliance closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[evaluative]:[applying] | evaluative | applying | applied boundary closure | 0 | NO_ITEMS | applied boundary closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[evaluative]:[judging] | evaluative | judging | determined acceptance closure | 0 | NO_ITEMS | determined acceptance closure was checked against the production set without a distinct enrichment input under this lens. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | appraised quality closure | 0 | NO_ITEMS | appraised quality closure was checked against the production set without a distinct enrichment input under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | MissingSlot | Procedure | Procedure | Name the accepted PersonaComposer input interface or preserve it as an explicit TBD before implementation. | Procedure steps depend on selected persona, working-root summary, mode, permitted tool surface, governance preface, and fingerprint inputs, but the exact runtime interface remains open in Records. That missing slot affects implementation sequencing. | Procedure.md | Procedure.md#Steps; Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | required governance proof | 0 | NO_ITEMS | required governance proof was checked against the production set without a distinct enrichment input under this lens. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | sufficient direction evidence | 0 | NO_ITEMS | sufficient direction evidence was checked against the production set without a distinct enrichment input under this lens. |
| X:[guiding]:[completeness] | guiding | completeness | complete closure trace | 0 | NO_ITEMS | complete closure trace was checked against the production set without a distinct enrichment input under this lens. |
| X:[guiding]:[consistency] | guiding | consistency | consistent posture signal | 0 | NO_ITEMS | consistent posture signal was checked against the production set without a distinct enrichment input under this lens. |
| X:[applying]:[necessity] | applying | necessity | required implementation proof | 0 | NO_ITEMS | required implementation proof was checked against the production set without a distinct enrichment input under this lens. |
| X:[applying]:[sufficiency] | applying | sufficiency | sufficient execution basis | 0 | NO_ITEMS | sufficient execution basis was checked against the production set without a distinct enrichment input under this lens. |
| X:[applying]:[completeness] | applying | completeness | complete behavior trace | 0 | NO_ITEMS | complete behavior trace was checked against the production set without a distinct enrichment input under this lens. |
| X:[applying]:[consistency] | applying | consistency | consistent prompt behavior | 0 | NO_ITEMS | consistent prompt behavior was checked against the production set without a distinct enrichment input under this lens. |
| X:[judging]:[necessity] | judging | necessity | required validation proof | 1 | HAS_ITEMS | required validation proof exposes 1 warranted enrichment input recorded below. |
| X:[judging]:[sufficiency] | judging | sufficiency | sufficient assessment basis | 0 | NO_ITEMS | sufficient assessment basis was checked against the production set without a distinct enrichment input under this lens. |
| X:[judging]:[completeness] | judging | completeness | complete decision trace | 0 | NO_ITEMS | complete decision trace was checked against the production set without a distinct enrichment input under this lens. |
| X:[judging]:[consistency] | judging | consistency | consistent verdict basis | 0 | NO_ITEMS | consistent verdict basis was checked against the production set without a distinct enrichment input under this lens. |
| X:[reviewing]:[necessity] | reviewing | necessity | required audit proof | 0 | NO_ITEMS | required audit proof was checked against the production set without a distinct enrichment input under this lens. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | sufficient inspection basis | 0 | NO_ITEMS | sufficient inspection basis was checked against the production set without a distinct enrichment input under this lens. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete review trace | 0 | NO_ITEMS | complete review trace was checked against the production set without a distinct enrichment input under this lens. |
| X:[reviewing]:[consistency] | reviewing | consistency | consistent oversight basis | 0 | NO_ITEMS | consistent oversight basis was checked against the production set without a distinct enrichment input under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[necessity] | TBD_Question | Multi | TBD | Identify the consuming deliverable or interface for boot/session fingerprint handoff currently recorded as UNKNOWN. | The production documents call for boot fingerprint updates and integration evidence, while the dependency notes preserve the downstream consumer as UNKNOWN. This requires routing clarification before closure. | Datasheet.md; Procedure.md; _DEPENDENCIES.md | Datasheet.md#Construction; Procedure.md#Records; _DEPENDENCIES.md#Run Notes |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | governance fact basis | 0 | NO_ITEMS | governance fact basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[guiding]:[information] | guiding | information | directional context basis | 0 | NO_ITEMS | directional context basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[guiding]:[knowledge] | guiding | knowledge | governed understanding basis | 0 | NO_ITEMS | governed understanding basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled direction basis | 1 | HAS_ITEMS | principled direction basis exposes 1 warranted enrichment input recorded below. |
| E:[applying]:[data] | applying | data | implementation fact basis | 0 | NO_ITEMS | implementation fact basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[applying]:[information] | applying | information | execution context basis | 0 | NO_ITEMS | execution context basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[applying]:[knowledge] | applying | knowledge | practical mastery basis | 0 | NO_ITEMS | practical mastery basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[applying]:[wisdom] | applying | wisdom | judged execution basis | 0 | NO_ITEMS | judged execution basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[judging]:[data] | judging | data | validation fact basis | 0 | NO_ITEMS | validation fact basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[judging]:[information] | judging | information | assessment context basis | 0 | NO_ITEMS | assessment context basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[judging]:[knowledge] | judging | knowledge | competence verdict basis | 0 | NO_ITEMS | competence verdict basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned verdict basis | 0 | NO_ITEMS | reasoned verdict basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[reviewing]:[data] | reviewing | data | audit fact basis | 0 | NO_ITEMS | audit fact basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[reviewing]:[information] | reviewing | information | inspection context basis | 0 | NO_ITEMS | inspection context basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | review mastery basis | 0 | NO_ITEMS | review mastery basis was checked against the production set without a distinct enrichment input under this lens. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | quality reasoning basis | 0 | NO_ITEMS | quality reasoning basis was checked against the production set without a distinct enrichment input under this lens. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[wisdom] | RationaleGap | Guidance | Guidance | Add decision rationale for when alias resolution is owned locally versus delegated to an accepted resolver. | Guidance identifies direct alias handling versus delegated resolver as a trade-off, but does not state the decision criterion for selecting either path. That rationale gap matters because DEL-08-02 may own the alias routing contract. | Guidance.md | Guidance.md#Considerations; Guidance.md#Trade-offs |  | PROPOSAL | TBD |
