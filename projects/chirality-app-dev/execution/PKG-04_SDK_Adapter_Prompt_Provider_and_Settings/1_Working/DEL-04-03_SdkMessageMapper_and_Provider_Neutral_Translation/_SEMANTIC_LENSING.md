# Semantic Lensing Register: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

**Generated:** 2026-05-21
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py passed after generation
**Warnings:** REF-006 HASH_MISMATCH recorded in source metadata; SDK probe fixtures, dependency edges, concrete code paths, terminal mapping boundaries, and adapter metadata placement remain TBD.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/_CONTEXT.md#identity
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/_STATUS.md#history
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/_SEMANTIC.md
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/Datasheet.md#attributes
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/Specification.md#requirements
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/Guidance.md#principles
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/Procedure.md#steps
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation/_REFERENCES.md#authoritative-source-corpus (metadata only; external paths not followed)

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 6
- By document:
  - Datasheet: 0
  - Specification: 1
  - Guidance: 2
  - Procedure: 2
  - Multi: 1
  - NA: 0
- By matrix:
  - A: 0
  - B: 1
  - C: 1
  - F: 1
  - D: 1
  - X: 1
  - E: 1
- By type:
  - Conflict: 1
  - VerificationGap: 1
  - MissingSlot: 2
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | A normative/guiding lens (prescriptive direction) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | A normative/applying lens (mandatory practice) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | A normative/judging lens (compliance determination) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | A normative/reviewing lens (regulatory audit) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | A operative/guiding lens (procedural direction) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | A operative/applying lens (practical execution) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | A operative/judging lens (performance assessment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | A operative/reviewing lens (process audit) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | A evaluative/guiding lens (value orientation) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | A evaluative/applying lens (merit application) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | A evaluative/judging lens (worth determination) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | A evaluative/reviewing lens (quality appraisal) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | B data/necessity lens (essential fact) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | B data/sufficiency lens (adequate evidence) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | B data/completeness lens (comprehensive record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | Carry REF-006 PRD hash mismatch as a warning-qualified source-state blocker until source hash reconciliation is accepted. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | B information/necessity lens (essential signal) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | B information/sufficiency lens (adequate context) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | B information/completeness lens (comprehensive account) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | B information/consistency lens (coherent message) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | B knowledge/necessity lens (fundamental understanding) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | B knowledge/sufficiency lens (competent expertise) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | B knowledge/completeness lens (thorough mastery) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | B knowledge/consistency lens (coherent understanding) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | B wisdom/necessity lens (essential discernment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | B wisdom/sufficiency lens (adequate judgment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | B wisdom/completeness lens (holistic insight) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | B wisdom/consistency lens (principled reasoning) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | Conflict | Multi | NA | Carry REF-006 PRD hash mismatch as a warning-qualified source-state blocker until source hash reconciliation is accepted. | The production documents use PRD-derived SDK requirements while _REFERENCES.md records REF-006 as HASH_MISMATCH. The register can surface that source-state tension without resolving source authority. | _REFERENCES.md; Datasheet.md; Specification.md; Guidance.md; Procedure.md | _REFERENCES.md#authoritative-source-corpus; Datasheet.md#identification; Specification.md#standards; Guidance.md#conflict-table-for-human-ruling; Procedure.md#prerequisites | _REFERENCES.md#authoritative-source-corpus; Guidance.md#conflict-table-for-human-ruling | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding rationale | 0 | NO_ITEMS | C normative/necessity lens (binding rationale) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[normative]:[sufficiency] | normative | sufficiency | sufficient authorization | 0 | NO_ITEMS | C normative/sufficiency lens (sufficient authorization) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[normative]:[completeness] | normative | completeness | complete obligation | 0 | NO_ITEMS | C normative/completeness lens (complete obligation) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[normative]:[consistency] | normative | consistency | coherent control | 0 | NO_ITEMS | C normative/consistency lens (coherent control) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[operative]:[necessity] | operative | necessity | required procedure | 0 | NO_ITEMS | C operative/necessity lens (required procedure) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[operative]:[sufficiency] | operative | sufficiency | adequate execution | 1 | HAS_ITEMS | After DEL-04-01/OI-001, name the observed SDK message payload categories that graduate from TBD fixtures into supported mapper inputs. |
| C:[operative]:[completeness] | operative | completeness | full workflow | 0 | NO_ITEMS | C operative/completeness lens (full workflow) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[operative]:[consistency] | operative | consistency | stable operation | 0 | NO_ITEMS | C operative/consistency lens (stable operation) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[evaluative]:[necessity] | evaluative | necessity | essential criterion | 0 | NO_ITEMS | C evaluative/necessity lens (essential criterion) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate merit | 0 | NO_ITEMS | C evaluative/sufficiency lens (adequate merit) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[evaluative]:[completeness] | evaluative | completeness | whole appraisal | 0 | NO_ITEMS | C evaluative/completeness lens (whole appraisal) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent judgment | 0 | NO_ITEMS | C evaluative/consistency lens (coherent judgment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[sufficiency] | MissingSlot | Guidance | Guidance | After DEL-04-01/OI-001, name the observed SDK message payload categories that graduate from TBD fixtures into supported mapper inputs. | Guidance and Specification intentionally leave exact SDK message categories and payload fields probe-dependent. Adequate execution needs a bounded enrichment slot for probe-backed categories rather than guessed SDK shapes. | Guidance.md; Specification.md; Datasheet.md | Guidance.md#considerations; Specification.md#requirements; Datasheet.md#attributes |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | binding requirement | 0 | NO_ITEMS | F normative/necessity lens (binding requirement) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[normative]:[sufficiency] | normative | sufficiency | acceptable evidence basis | 0 | NO_ITEMS | F normative/sufficiency lens (acceptable evidence basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[normative]:[completeness] | normative | completeness | exhaustive control record | 0 | NO_ITEMS | F normative/completeness lens (exhaustive control record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[normative]:[consistency] | normative | consistency | consistent obligation rule | 0 | NO_ITEMS | F normative/consistency lens (consistent obligation rule) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[operative]:[necessity] | operative | necessity | required implementation path | 0 | NO_ITEMS | F operative/necessity lens (required implementation path) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[operative]:[sufficiency] | operative | sufficiency | sufficient operating proof | 0 | NO_ITEMS | F operative/sufficiency lens (sufficient operating proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[operative]:[completeness] | operative | completeness | complete process coverage | 1 | HAS_ITEMS | Confirm whether accepted dependency edges must be populated before implementation closure for DEL-04-03. |
| F:[operative]:[consistency] | operative | consistency | reliable execution pattern | 0 | NO_ITEMS | F operative/consistency lens (reliable execution pattern) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[evaluative]:[necessity] | evaluative | necessity | essential review criterion | 0 | NO_ITEMS | F evaluative/necessity lens (essential review criterion) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate value proof | 0 | NO_ITEMS | F evaluative/sufficiency lens (adequate value proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete assessment basis | 0 | NO_ITEMS | F evaluative/completeness lens (complete assessment basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| F:[evaluative]:[consistency] | evaluative | consistency | coherent acceptance rationale | 0 | NO_ITEMS | F evaluative/consistency lens (coherent acceptance rationale) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[completeness] | TBD_Question | Procedure | Procedure | Confirm whether accepted dependency edges must be populated before implementation closure for DEL-04-03. | Procedure lists declared upstream dependencies as TBD, and Datasheet states dependency extraction has not accepted edges. Complete process coverage depends on whether dependency closure is prerequisite work or later handoff state. | Procedure.md; Datasheet.md | Procedure.md#prerequisites; Procedure.md#records; Datasheet.md#conditions |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | authoritative direction | 0 | NO_ITEMS | D normative/guiding lens (authoritative direction) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[normative]:[applying] | normative | applying | binding practice closure | 0 | NO_ITEMS | D normative/applying lens (binding practice closure) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[normative]:[judging] | normative | judging | accountable compliance verdict | 0 | NO_ITEMS | D normative/judging lens (accountable compliance verdict) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[normative]:[reviewing] | normative | reviewing | governed audit closure | 0 | NO_ITEMS | D normative/reviewing lens (governed audit closure) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[operative]:[guiding] | operative | guiding | actionable procedure path | 1 | HAS_ITEMS | Record the accepted backend mapper path, UI/HarnessEvent type import paths, and mapper test locations after code discovery. |
| D:[operative]:[applying] | operative | applying | executable work closure | 0 | NO_ITEMS | D operative/applying lens (executable work closure) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[operative]:[judging] | operative | judging | measurable performance verdict | 0 | NO_ITEMS | D operative/judging lens (measurable performance verdict) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[operative]:[reviewing] | operative | reviewing | traceable process review | 0 | NO_ITEMS | D operative/reviewing lens (traceable process review) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[evaluative]:[guiding] | evaluative | guiding | principled value direction | 0 | NO_ITEMS | D evaluative/guiding lens (principled value direction) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[evaluative]:[applying] | evaluative | applying | justified merit use | 0 | NO_ITEMS | D evaluative/applying lens (justified merit use) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[evaluative]:[judging] | evaluative | judging | reasoned worth verdict | 0 | NO_ITEMS | D evaluative/judging lens (reasoned worth verdict) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality review closure | 0 | NO_ITEMS | D evaluative/reviewing lens (quality review closure) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[guiding] | MissingSlot | Procedure | Procedure | Record the accepted backend mapper path, UI/HarnessEvent type import paths, and mapper test locations after code discovery. | The procedure says to add sdk-message-mapper.ts or equivalent in the accepted backend runtime location, but the current production docs do not identify concrete code paths. Actionable procedure path needs these locations once implementation begins. | Procedure.md; Datasheet.md; Specification.md | Procedure.md#steps; Procedure.md#records; Datasheet.md#construction; Specification.md#documentation |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | governing premise | 0 | NO_ITEMS | X guiding/necessity lens (governing premise) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | adequate directive proof | 0 | NO_ITEMS | X guiding/sufficiency lens (adequate directive proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[guiding]:[completeness] | guiding | completeness | complete direction basis | 0 | NO_ITEMS | X guiding/completeness lens (complete direction basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[guiding]:[consistency] | guiding | consistency | consistent guidance record | 0 | NO_ITEMS | X guiding/consistency lens (consistent guidance record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[applying]:[necessity] | applying | necessity | required practice basis | 0 | NO_ITEMS | X applying/necessity lens (required practice basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[applying]:[sufficiency] | applying | sufficiency | sufficient execution proof | 0 | NO_ITEMS | X applying/sufficiency lens (sufficient execution proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[applying]:[completeness] | applying | completeness | complete application record | 0 | NO_ITEMS | X applying/completeness lens (complete application record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[applying]:[consistency] | applying | consistency | stable practice pattern | 0 | NO_ITEMS | X applying/consistency lens (stable practice pattern) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[judging]:[necessity] | judging | necessity | compliance evidence basis | 0 | NO_ITEMS | X judging/necessity lens (compliance evidence basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate verdict proof | 1 | HAS_ITEMS | Clarify verification boundaries for terminal success, failure, interruption, and cancellation mapping against the TurnEngine/runtime contract. |
| X:[judging]:[completeness] | judging | completeness | complete assessment record | 0 | NO_ITEMS | X judging/completeness lens (complete assessment record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[judging]:[consistency] | judging | consistency | coherent determination basis | 0 | NO_ITEMS | X judging/consistency lens (coherent determination basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit evidence basis | 0 | NO_ITEMS | X reviewing/necessity lens (audit evidence basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | sufficient review proof | 0 | NO_ITEMS | X reviewing/sufficiency lens (sufficient review proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[reviewing]:[completeness] | reviewing | completeness | comprehensive audit record | 0 | NO_ITEMS | X reviewing/completeness lens (comprehensive audit record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| X:[reviewing]:[consistency] | reviewing | consistency | reliable review rationale | 0 | NO_ITEMS | X reviewing/consistency lens (reliable review rationale) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Clarify verification boundaries for terminal success, failure, interruption, and cancellation mapping against the TurnEngine/runtime contract. | Specification requires terminal outcome information for persistence while Guidance notes completion and terminal split depends on the TurnEngine contract. Adequate verdict proof needs tests that show which terminal semantics are mapper-owned and which remain upstream runtime behavior. | Specification.md; Guidance.md; Procedure.md | Specification.md#requirements; Specification.md#verification; Guidance.md#examples; Procedure.md#steps |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | authoritative evidence signal | 0 | NO_ITEMS | E guiding/data lens (authoritative evidence signal) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[guiding]:[information] | guiding | information | contextual direction proof | 0 | NO_ITEMS | E guiding/information lens (contextual direction proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[guiding]:[knowledge] | guiding | knowledge | understood governance basis | 0 | NO_ITEMS | E guiding/knowledge lens (understood governance basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[guiding]:[wisdom] | guiding | wisdom | reasoned direction judgment | 0 | NO_ITEMS | E guiding/wisdom lens (reasoned direction judgment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[applying]:[data] | applying | data | binding execution fact | 0 | NO_ITEMS | E applying/data lens (binding execution fact) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[applying]:[information] | applying | information | contextual practice proof | 0 | NO_ITEMS | E applying/information lens (contextual practice proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[applying]:[knowledge] | applying | knowledge | competent application basis | 1 | HAS_ITEMS | Explain the rationale for approved adapter metadata placement for sdkSessionId, sdkTranscriptPath, SDK tool names, permission modes, and provider identifiers. |
| E:[applying]:[wisdom] | applying | wisdom | judged practice sufficiency | 0 | NO_ITEMS | E applying/wisdom lens (judged practice sufficiency) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[judging]:[data] | judging | data | verdict evidence signal | 0 | NO_ITEMS | E judging/data lens (verdict evidence signal) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[judging]:[information] | judging | information | contextual assessment proof | 0 | NO_ITEMS | E judging/information lens (contextual assessment proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[judging]:[knowledge] | judging | knowledge | understood compliance basis | 0 | NO_ITEMS | E judging/knowledge lens (understood compliance basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned verdict judgment | 0 | NO_ITEMS | E judging/wisdom lens (reasoned verdict judgment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[reviewing]:[data] | reviewing | data | audit evidence record | 0 | NO_ITEMS | E reviewing/data lens (audit evidence record) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[reviewing]:[information] | reviewing | information | contextual review proof | 0 | NO_ITEMS | E reviewing/information lens (contextual review proof) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastered audit basis | 0 | NO_ITEMS | E reviewing/knowledge lens (mastered audit basis) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled appraisal judgment | 0 | NO_ITEMS | E reviewing/wisdom lens (principled appraisal judgment) was checked against Datasheet, Specification, Guidance, and Procedure; cited content left this register cell without an extra enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[applying]:[knowledge] | RationaleGap | Guidance | Guidance | Explain the rationale for approved adapter metadata placement for sdkSessionId, sdkTranscriptPath, SDK tool names, permission modes, and provider identifiers. | Documents consistently say SDK identifiers belong only in explicit adapter metadata, but the reasoned placement rule is distributed across principles, requirements, and leakage tests. Competent application would benefit from a concise rationale without inventing final schema fields. | Guidance.md; Specification.md; Datasheet.md | Guidance.md#principles; Guidance.md#trade-offs; Specification.md#requirements; Datasheet.md#construction |  | PROPOSAL | TBD |
