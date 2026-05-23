# Semantic Lensing Register: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

**Generated:** 2026-05-21
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py passed after generation
**Warnings:** REF-006 PRD hash mismatch retained as warning-only source tension; implementation paths, exact test commands, and evidence artifact paths remain TBD in production documents.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_CONTEXT.md#identity
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md#history
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_SEMANTIC.md
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Datasheet.md#attributes
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Specification.md#requirements
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Guidance.md#principles
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Procedure.md#steps
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_REFERENCES.md#authoritative-source-corpus (metadata only; external paths not followed)

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 6
- By document:
  - Datasheet: 0
  - Specification: 2
  - Guidance: 1
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
  - VerificationGap: 3
  - MissingSlot: 1
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 0
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | A normative/guiding lens checked whether security-control direction is stated as policy; Specification and Guidance already state the bounded network, key, and attachment posture. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | A normative/applying lens checked mandatory security practices; Requirements already use shall-language for key, endpoint, renderer, and attachment checks. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | A normative/judging lens checked compliance framing; verification rows already map requirements to evidence artifact classes. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | A normative/reviewing lens checked audit posture; Records and References provide review inputs without creating a new local ruling. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | A operative/guiding lens checked procedure direction; Procedure steps cover scope confirmation, target identification, checks, and validation execution. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | A operative/applying lens checked practical execution; Procedure names concrete negative cases and validation surfaces. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | A operative/judging lens checked performance assessment; evidence gaps are captured under more precise D and X lenses. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | A operative/reviewing lens checked process audit mechanics; Procedure records list the evidence classes to retain. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | A evaluative/guiding lens checked value orientation; Guidance anchors the deliverable in release readiness and professional safety. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | A evaluative/applying lens checked applied merit; the documents tie merit to repeatable checks instead of assertions. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | A evaluative/judging lens checked acceptance value; the need for current evidence is registered under D and X rather than duplicated here. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | A evaluative/reviewing lens checked quality appraisal; the review surface is clear enough for Phase 2.4 and has no separate item in A. |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | B data/necessity lens checked essential facts; Datasheet lists key order, storage path, endpoint, extensions, and byte budgets. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | B data/sufficiency lens checked evidence categories; Specification and Procedure name the required test families. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | B data/completeness lens checked record scope; exact artifact paths remain separately captured under X. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | Carry REF-006 PRD hash mismatch as a source-state warning until a later phase records the accepted ruling. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | B information/necessity lens checked required signals; the production docs preserve the security surfaces and warning state. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | B information/sufficiency lens checked context; scope, in-scope, out-of-scope, and source-warning text provide adequate context. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | B information/completeness lens checked account breadth; all four named surfaces are represented in requirements and procedure. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | B information/consistency lens checked message alignment; Datasheet, Specification, Guidance, and Procedure describe the same allowlist/key/attachment boundaries. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | B knowledge/necessity lens checked basic understanding; Guidance states runtime code is the security boundary. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | B knowledge/sufficiency lens checked expertise signal; guidance distinguishes unit and integration checks by surface. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | B knowledge/completeness lens checked mastery; implementation-location gaps are captured under F rather than repeated here. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | B knowledge/consistency lens checked conceptual coherence; the documents separate renderer policy from Node/SDK provider policy. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | B wisdom/necessity lens checked discernment; Guidance reserves broader network access for governed future scope. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | B wisdom/sufficiency lens checked judgment; trade-offs identify test granularity, redaction breadth, retry location, and network split. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | B wisdom/completeness lens checked holistic framing; security posture, trust boundary, and failure handling are included. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | B wisdom/consistency lens checked principled reasoning; source warning treatment is explicit and does not expand authority. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | Conflict | Multi | NA | Carry REF-006 PRD hash mismatch as warning-only source tension for all PRD-grounded security checks. | The register depends on PRD-derived requirements while _REFERENCES.md records REF-006 as HASH_MISMATCH and Guidance treats the mismatch as warning-only. Reliable measurement needs the tension visible without selecting a new source authority. | _REFERENCES.md; Datasheet.md; Guidance.md; Procedure.md | _REFERENCES.md#authoritative-source-corpus; Datasheet.md#conditions; Guidance.md#considerations; Procedure.md#prerequisites | _REFERENCES.md#authoritative-source-corpus; Guidance.md#conflict-table-for-human-ruling | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | authoritative evidence frame | 0 | NO_ITEMS | C normative/necessity lens checked authoritative evidence framing; standards and references identify PRD, SPEC, CONTRACT, and decomposition sources. |
| C:[normative]:[sufficiency] | normative | sufficiency | binding proof context | 0 | NO_ITEMS | C normative/sufficiency lens checked binding proof context; each requirement carries a verification approach. |
| C:[normative]:[completeness] | normative | completeness | complete compliance record | 0 | NO_ITEMS | C normative/completeness lens checked compliance record shape; completion evidence is deferred to D and X items. |
| C:[normative]:[consistency] | normative | consistency | coherent control rationale | 0 | NO_ITEMS | C normative/consistency lens checked control rationale; source-warning handling and security principles are aligned. |
| C:[operative]:[necessity] | operative | necessity | required execution basis | 0 | NO_ITEMS | C operative/necessity lens checked execution basis; Procedure begins with target identification before check construction. |
| C:[operative]:[sufficiency] | operative | sufficiency | adequate test coverage | 1 | HAS_ITEMS | Name exact command paths and test locations once implementation targets are selected. |
| C:[operative]:[completeness] | operative | completeness | complete process evidence | 0 | NO_ITEMS | C operative/completeness lens checked process evidence; broader evidence retention is covered by D and X items. |
| C:[operative]:[consistency] | operative | consistency | stable runtime signal | 0 | NO_ITEMS | C operative/consistency lens checked runtime signal stability; requirements separate renderer, provider, key, and attachment surfaces. |
| C:[evaluative]:[necessity] | evaluative | necessity | value proof basis | 0 | NO_ITEMS | C evaluative/necessity lens checked value proof; release readiness is tied to repeatable validation rather than assertions. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequate assurance judgment | 0 | NO_ITEMS | C evaluative/sufficiency lens checked assurance judgment; the itemized verification approaches are suitable pending command evidence. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete quality account | 0 | NO_ITEMS | C evaluative/completeness lens checked quality account; the four production docs cover identity, requirements, rationale, and procedure. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent acceptance rationale | 0 | NO_ITEMS | C evaluative/consistency lens checked acceptance rationale; acceptance remains evidence-dependent and no new assertion is warranted here. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[sufficiency] | VerificationGap | Specification | Specification | Add exact test file paths and command names for key, provider, renderer, attachment, and retry checks after implementation locations are confirmed. | Specification documents the required coverage but its Documentation section and Procedure prerequisites keep exact test file paths and command names as TBD. Adequate test coverage needs those identifiers before release-significant acceptance. | Specification.md; Procedure.md; Guidance.md | Specification.md#documentation; Procedure.md#prerequisites; Guidance.md#considerations |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | mandatory evidence threshold | 0 | NO_ITEMS | F normative/necessity lens checked mandatory evidence threshold; fourteen requirements identify release-relevant checks. |
| F:[normative]:[sufficiency] | normative | sufficiency | sufficient control proof | 0 | NO_ITEMS | F normative/sufficiency lens checked control proof; verification approaches are mapped by requirement group. |
| F:[normative]:[completeness] | normative | completeness | complete compliance basis | 0 | NO_ITEMS | F normative/completeness lens checked compliance basis; source warning is captured under B, evidence gaps under D and X. |
| F:[normative]:[consistency] | normative | consistency | consistent policy rationale | 0 | NO_ITEMS | F normative/consistency lens checked policy rationale; Guidance and Specification agree on the allowlist and key secrecy posture. |
| F:[operative]:[necessity] | operative | necessity | required test enactment | 0 | NO_ITEMS | F operative/necessity lens checked required test enactment; Procedure lists concrete checks for every security surface. |
| F:[operative]:[sufficiency] | operative | sufficiency | adequate execution proof | 0 | NO_ITEMS | F operative/sufficiency lens checked execution proof; C and D carry the command/evidence gaps. |
| F:[operative]:[completeness] | operative | completeness | complete validation coverage | 1 | HAS_ITEMS | Resolve TBD implementation targets for renderer guard, provider policy, key storage, redaction, attachment resolver, and route/UI handling. |
| F:[operative]:[consistency] | operative | consistency | consistent runtime behavior | 0 | NO_ITEMS | F operative/consistency lens checked runtime behavior; requirements distinguish successful, rejected, partial-failure, and total-failure paths. |
| F:[evaluative]:[necessity] | evaluative | necessity | necessary assurance basis | 0 | NO_ITEMS | F evaluative/necessity lens checked assurance basis; OBJ-008 and PKG-09 release readiness are represented. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | sufficient release confidence | 0 | NO_ITEMS | F evaluative/sufficiency lens checked release confidence; confidence remains gated by current evidence, captured under D and X. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete quality judgment | 0 | NO_ITEMS | F evaluative/completeness lens checked quality judgment; the requirements span network, key, provider, attachment, retry, and release checks. |
| F:[evaluative]:[consistency] | evaluative | consistency | consistent acceptance reasoning | 0 | NO_ITEMS | F evaluative/consistency lens checked acceptance reasoning; no contradiction was found among the four production documents for this cell. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[completeness] | MissingSlot | Procedure | Procedure | Fill implementation target paths for renderer network guard, provider base URL validation, API key storage/resolution, redaction helper/logger, attachment resolver, and route/UI failure handling. | Procedure step 2 requires locating these targets, and the prerequisites explicitly mark implementation paths as TBD. Complete validation coverage cannot be enacted repeatably until those targets are recorded. | Procedure.md; Specification.md | Procedure.md#prerequisites; Procedure.md#steps; Specification.md#documentation |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | binding evidence direction | 0 | NO_ITEMS | D normative/guiding lens checked evidence direction; Specification gives requirement IDs and source standards. |
| D:[normative]:[applying] | normative | applying | assured practice closure | 0 | NO_ITEMS | D normative/applying lens checked practice closure; Procedure enumerates the security checks to build. |
| D:[normative]:[judging] | normative | judging | compliance proof closure | 0 | NO_ITEMS | D normative/judging lens checked compliance closure; current-run command evidence is registered under operative/judging. |
| D:[normative]:[reviewing] | normative | reviewing | audit evidence closure | 0 | NO_ITEMS | D normative/reviewing lens checked audit evidence closure; X carries the artifact-path inspection gap. |
| D:[operative]:[guiding] | operative | guiding | execution control path | 0 | NO_ITEMS | D operative/guiding lens checked execution path; Procedure preserves the sequence from source state to validation run. |
| D:[operative]:[applying] | operative | applying | validated implementation closure | 0 | NO_ITEMS | D operative/applying lens checked implementation closure; F captures the missing implementation target slots. |
| D:[operative]:[judging] | operative | judging | performance proof closure | 1 | HAS_ITEMS | Capture release-readiness command output and exact command identity for REQ-014. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance closure | 0 | NO_ITEMS | D operative/reviewing lens checked process assurance closure; Procedure records identify the evidence classes to preserve. |
| D:[evaluative]:[guiding] | evaluative | guiding | assurance value path | 0 | NO_ITEMS | D evaluative/guiding lens checked assurance value; Guidance ties checks to professional safety and release readiness. |
| D:[evaluative]:[applying] | evaluative | applying | release merit closure | 0 | NO_ITEMS | D evaluative/applying lens checked release merit; all merit claims remain contingent on test evidence. |
| D:[evaluative]:[judging] | evaluative | judging | acceptance proof closure | 0 | NO_ITEMS | D evaluative/judging lens checked acceptance proof; no accepted proof is invented in this register. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality evidence closure | 0 | NO_ITEMS | D evaluative/reviewing lens checked quality evidence closure; inspection-record completion is captured under X. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[judging] | VerificationGap | Specification | Specification | Record the exact release-readiness validation command and current-run output or CI artifact for DEL-09-06 REQ-014. | Specification REQ-014 requires explicit repeatable local checks before release-significant acceptance, but Verification marks the exact command TBD and Procedure says command names remain TBD. Performance proof closure needs current command evidence. | Specification.md; Procedure.md | Specification.md#requirements; Specification.md#verification; Procedure.md#prerequisites; Procedure.md#steps |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | evidence readiness standard | 0 | NO_ITEMS | X guiding/necessity lens checked evidence readiness; source state and release-significant scope are explicit. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | sufficient direction proof | 0 | NO_ITEMS | X guiding/sufficiency lens checked direction proof; the procedure gives adequate direction pending target selection. |
| X:[guiding]:[completeness] | guiding | completeness | complete control map | 0 | NO_ITEMS | X guiding/completeness lens checked control map; all named security surfaces appear in the requirements. |
| X:[guiding]:[consistency] | guiding | consistency | coherent assurance path | 0 | NO_ITEMS | X guiding/consistency lens checked assurance path; Guidance separates renderer policy from provider policy. |
| X:[applying]:[necessity] | applying | necessity | execution proof threshold | 0 | NO_ITEMS | X applying/necessity lens checked execution threshold; negative and positive cases are listed. |
| X:[applying]:[sufficiency] | applying | sufficiency | adequate practice evidence | 0 | NO_ITEMS | X applying/sufficiency lens checked practice evidence; C captures missing test file and command identifiers. |
| X:[applying]:[completeness] | applying | completeness | complete validation method | 0 | NO_ITEMS | X applying/completeness lens checked validation method; F captures missing implementation target identifiers. |
| X:[applying]:[consistency] | applying | consistency | consistent implementation signal | 0 | NO_ITEMS | X applying/consistency lens checked implementation signals; no conflicting runtime behavior statements were found. |
| X:[judging]:[necessity] | judging | necessity | acceptance evidence basis | 0 | NO_ITEMS | X judging/necessity lens checked acceptance evidence basis; D captures the missing current command output. |
| X:[judging]:[sufficiency] | judging | sufficiency | sufficient decision proof | 0 | NO_ITEMS | X judging/sufficiency lens checked decision proof; acceptance is not asserted without evidence. |
| X:[judging]:[completeness] | judging | completeness | complete conformance account | 0 | NO_ITEMS | X judging/completeness lens checked conformance account; the artifact-path gap is assigned to reviewing/completeness. |
| X:[judging]:[consistency] | judging | consistency | coherent verdict rationale | 0 | NO_ITEMS | X judging/consistency lens checked verdict rationale; warning treatment and evidence dependency are coherent. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit proof threshold | 0 | NO_ITEMS | X reviewing/necessity lens checked audit proof threshold; records categories are present. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | adequate review evidence | 0 | NO_ITEMS | X reviewing/sufficiency lens checked review evidence; D carries current-run command evidence. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete inspection record | 1 | HAS_ITEMS | Fill exact security-test, network-guard, attachment-resolver, key-storage, provider-policy, redaction, and validation artifact paths. |
| X:[reviewing]:[consistency] | reviewing | consistency | consistent oversight rationale | 0 | NO_ITEMS | X reviewing/consistency lens checked oversight rationale; records and guidance use consistent evidence categories. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[completeness] | VerificationGap | Procedure | Procedure | Replace TBD record paths with exact artifact paths for security tests, network guard tests, attachment resolver validation, key storage checks, provider policy tests, redaction fixtures, and validation output. | Procedure Records lists the required evidence classes but leaves exact artifact paths TBD. A complete inspection record needs the selected evidence locations after implementation and validation run. | Procedure.md; Specification.md | Procedure.md#records; Specification.md#documentation; Specification.md#verification |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | evidential release posture | 0 | NO_ITEMS | E guiding/data lens checked release posture data; Datasheet preserves scope, source warning, and key constants. |
| E:[guiding]:[information] | guiding | information | contextual control assurance | 0 | NO_ITEMS | E guiding/information lens checked contextual assurance; Guidance explains why runtime code and tests are the boundary. |
| E:[guiding]:[knowledge] | guiding | knowledge | mastery of safeguards | 0 | NO_ITEMS | E guiding/knowledge lens checked safeguard mastery; the documents cover key, network, provider, attachment, retry, and redaction concerns. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled security direction | 1 | HAS_ITEMS | Clarify the principle that Anthropic provider access and renderer network allowlisting are separate enforcement surfaces. |
| E:[applying]:[data] | applying | data | execution fact pattern | 0 | NO_ITEMS | E applying/data lens checked execution facts; Procedure supplies concrete positive and negative fact patterns. |
| E:[applying]:[information] | applying | information | contextual practice proof | 0 | NO_ITEMS | E applying/information lens checked practice context; trade-offs describe unit/integration split and retry localization. |
| E:[applying]:[knowledge] | applying | knowledge | validated operational mastery | 0 | NO_ITEMS | E applying/knowledge lens checked operational mastery; current validation evidence remains captured in D and X. |
| E:[applying]:[wisdom] | applying | wisdom | principled implementation basis | 0 | NO_ITEMS | E applying/wisdom lens checked implementation basis; broader network enablement is explicitly out of scope. |
| E:[judging]:[data] | judging | data | verdict evidence basis | 0 | NO_ITEMS | E judging/data lens checked verdict evidence; command and artifact evidence gaps are already registered. |
| E:[judging]:[information] | judging | information | contextual acceptance proof | 0 | NO_ITEMS | E judging/information lens checked acceptance context; acceptance is tied to repeatable security-control evidence. |
| E:[judging]:[knowledge] | judging | knowledge | mastery of conformance | 0 | NO_ITEMS | E judging/knowledge lens checked conformance mastery; requirements map to verification approaches by surface. |
| E:[judging]:[wisdom] | judging | wisdom | principled decision basis | 0 | NO_ITEMS | E judging/wisdom lens checked decision basis; no human ruling beyond source-warning treatment is introduced. |
| E:[reviewing]:[data] | reviewing | data | audit evidence record | 0 | NO_ITEMS | E reviewing/data lens checked audit evidence record; X captures the exact artifact-path completion gap. |
| E:[reviewing]:[information] | reviewing | information | contextual inspection proof | 0 | NO_ITEMS | E reviewing/information lens checked inspection context; records categories are named without overclaiming path availability. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery of oversight | 0 | NO_ITEMS | E reviewing/knowledge lens checked oversight mastery; production docs are sufficient for setup-phase review. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled review basis | 0 | NO_ITEMS | E reviewing/wisdom lens checked principled review; source warning, TBDs, and out-of-scope boundaries are visible. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[wisdom] | RationaleGap | Guidance | Guidance | Add a concise rationale that Anthropic provider access and renderer network allowlisting are related but separately enforced surfaces. | Guidance states renderer and provider network checks should be allowlist-oriented and its trade-off table says renderer and Node/SDK provider policy are separate surfaces. A concise rationale would reduce future review ambiguity without changing requirements. | Guidance.md; Specification.md | Guidance.md#principles; Guidance.md#trade-offs; Specification.md#requirements |  | PROPOSAL | TBD |
