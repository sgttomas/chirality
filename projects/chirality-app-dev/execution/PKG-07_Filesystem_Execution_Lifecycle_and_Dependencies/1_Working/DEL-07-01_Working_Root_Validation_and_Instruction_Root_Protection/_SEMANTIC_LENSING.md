# Semantic Lensing Register: DEL-07-01 Working Root Validation and Instruction Root Protection

**Generated:** 2026-05-20
**Deliverable Folder:** `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection`
**DECOMP_VARIANT:** SOFTWARE
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection`
**Purpose:** Matrix-organized lensing register generated from `_SEMANTIC.md` primary Result tables and deliverable-local production documents.

**Inputs Read:**
- `_CONTEXT.md` - local identity and scope metadata
- `_STATUS.md` - read only; no status edits made
- `_SEMANTIC.md` - primary Result tables for matrices A, B, C, F, D, X, and E
- `Datasheet.md` - production evidence
- `Specification.md` - production evidence
- `Guidance.md` - production evidence
- `Procedure.md` - production evidence
- `_REFERENCES.md` - metadata only; external paths not followed
- `_DEPENDENCIES.md` - read only local dependency context

**Warnings:**
- `[WARNING] SOURCE_STATE`: `_REFERENCES.md` marks `docs/PRD.md` as `HASH_MISMATCH`; PRD-dependent requirements remain review-aware.
- `[WARNING] TBD_IMPLEMENTATION_PATHS`: implementation file paths, helper names, and final test command names are not accepted in the production kit.
- `[WARNING] OPEN_DEPENDENCY_STATE`: `_DEPENDENCIES.md` records no accepted upstream or downstream dependency edges and marks code module locations as an execution prerequisite.

## Summary

Total warranted items: 9

By matrix:
- A: 1
- B: 1
- C: 1
- F: 1
- D: 1
- X: 2
- E: 2

By type:
- MissingSlot: 2
- WeakStatement: 0
- Conflict: 0
- VerificationGap: 3
- RationaleGap: 1
- Normalization: 1
- TBD_Question: 2
- MatrixError: 0

By document:
- Datasheet.md: 3
- Specification.md: 5
- Guidance.md: 4
- Procedure.md: 5

## Matrix A

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `A:[normative]:[guiding]` | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Prescriptive direction is represented by the root separation and path containment scope statements without a separate enrichment input. |
| `A:[normative]:[applying]` | normative | applying | mandatory practice | 1 | HAS_ITEMS | Mandatory practice exposes the gap between required code-level enforcement and still-unidentified implementation locations. |
| `A:[normative]:[judging]` | normative | judging | compliance determination | 0 | NO_ITEMS | Compliance determination maps to typed denial and fixture expectations in the specification, with no local contradiction surfaced. |
| `A:[normative]:[reviewing]` | normative | reviewing | regulatory audit | 0 | NO_ITEMS | Regulatory audit is bounded to local source-state warnings and evidence records; the register finds no additional audit slot here. |
| `A:[operative]:[guiding]` | operative | guiding | procedural direction | 0 | NO_ITEMS | Procedural direction is expressed by the ordered implementation steps and does not require an added production-document input. |
| `A:[operative]:[applying]` | operative | applying | practical execution | 0 | NO_ITEMS | Practical execution is constrained by the procedure's root, path, hook, and symlink steps without a distinct warranted item. |
| `A:[operative]:[judging]` | operative | judging | performance assessment | 0 | NO_ITEMS | Performance assessment is tied to fixture and test-output records; no extra ambiguity appears under this orientation lens. |
| `A:[operative]:[reviewing]` | operative | reviewing | process audit | 0 | NO_ITEMS | Process audit is addressed through source-state confirmation and verification evidence records within the local kit. |
| `A:[evaluative]:[guiding]` | evaluative | guiding | value orientation | 0 | NO_ITEMS | Value orientation is clear: protect instruction-root integrity while enabling working-root execution state. |
| `A:[evaluative]:[applying]` | evaluative | applying | merit application | 0 | NO_ITEMS | Merit application does not add a separate item beyond the documented deny-beats-allow and code-owns-boundary principles. |
| `A:[evaluative]:[judging]` | evaluative | judging | worth determination | 0 | NO_ITEMS | Worth determination remains tied to security acceptance evidence rather than a new document edit. |
| `A:[evaluative]:[reviewing]` | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Quality appraisal is locally bounded by fixture coverage, PRD warning preservation, and no sibling expansion. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | `A:[normative]:[applying]` | MissingSlot | Specification.md | Specification.md | Implementation worker must identify the runtime module, hook module, path helper, and tests that carry root and instruction-root enforcement. | The specification requires enforcement in runtime code, hooks, and policy helpers, while Datasheet and Procedure both leave code module locations as TBD. | Specification.md | Requirements, REQ-07-01-009; Documentation gaps | Datasheet.md#Construction; Procedure.md#Prerequisites | PROPOSAL | TBD |

## Matrix B

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `B:[data]:[necessity]` | data | necessity | essential fact | 0 | NO_ITEMS | Essential facts for working-root and instruction-root meanings are present in Datasheet attributes. |
| `B:[data]:[sufficiency]` | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Adequate evidence is framed by source citations in the four-document kit and does not surface a new item. |
| `B:[data]:[completeness]` | data | completeness | comprehensive record | 0 | NO_ITEMS | Comprehensive record needs are carried by expected records and artifacts in Procedure. |
| `B:[data]:[consistency]` | data | consistency | reliable measurement | 1 | HAS_ITEMS | Reliable measurement exposes acceptance evidence that is named but not yet produced for invalid-root and denial cases. |
| `B:[information]:[necessity]` | information | necessity | essential signal | 0 | NO_ITEMS | Essential signals are the validator, containment, and denial cues already described across Guidance and Procedure. |
| `B:[information]:[sufficiency]` | information | sufficiency | adequate context | 0 | NO_ITEMS | Adequate context is limited to DEL-07-01 and does not require following sibling deliverables. |
| `B:[information]:[completeness]` | information | completeness | comprehensive account | 0 | NO_ITEMS | Comprehensive account is supplied by the combined scope, conditions, trade-offs, and procedure steps. |
| `B:[information]:[consistency]` | information | consistency | coherent message | 0 | NO_ITEMS | Coherent message is maintained by repeated root separation and deny-beats-allow language. |
| `B:[knowledge]:[necessity]` | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Fundamental understanding is documented as working-root mutability versus instruction-root protection. |
| `B:[knowledge]:[sufficiency]` | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Competent expertise is deferred to implementer identification of code paths and does not create a second item under this lens. |
| `B:[knowledge]:[completeness]` | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Thorough mastery is represented by the test matrix requirements rather than a separate semantic enrichment. |
| `B:[knowledge]:[consistency]` | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Coherent understanding is maintained by consistent root/path vocabulary, except for the project-root normalization item recorded under F. |
| `B:[wisdom]:[necessity]` | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Essential discernment is expressed by strict initial symlink rejection and denial precedence. |
| `B:[wisdom]:[sufficiency]` | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Adequate judgment remains a human-governed future relaxation path for symlink policy. |
| `B:[wisdom]:[completeness]` | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Holistic insight is bounded by local root, hook, path, and fixture scope. |
| `B:[wisdom]:[consistency]` | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Principled reasoning is present in Guidance trade-offs and does not expose an extra local gap. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | `B:[data]:[consistency]` | VerificationGap | Procedure.md | Procedure.md | Record concrete fixture output for relative, missing, non-directory, unreadable, unwritable, instruction-root-contained, outside-root, traversal, instruction-root write, and symlink cases. | Procedure names the required cases and records, but this Phase 2.4 register has no produced test evidence or command output to confirm reliable measurement. | Procedure.md | Steps, step 9; Verification; Records | Specification.md#Verification | PROPOSAL | TBD |

## Matrix C

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `C:[normative]:[necessity]` | normative | necessity | binding evidence frame | 0 | NO_ITEMS | Binding evidence is grounded in cited CONTRACT, SPEC, and PRD rows, with PRD warning tracked separately. |
| `C:[normative]:[sufficiency]` | normative | sufficiency | warranted control basis | 0 | NO_ITEMS | Warranted control basis is clear for root rejection, containment, and instruction-root write denial. |
| `C:[normative]:[completeness]` | normative | completeness | complete rule account | 0 | NO_ITEMS | Complete rule account spans validator, path helper, hooks, and symlink policy. |
| `C:[normative]:[consistency]` | normative | consistency | stable compliance signal | 1 | HAS_ITEMS | Stable compliance signal is weakened by the recorded PRD hash mismatch for several requirement citations. |
| `C:[operative]:[necessity]` | operative | necessity | executable proof basis | 0 | NO_ITEMS | Executable proof basis is represented by required tests and expected records. |
| `C:[operative]:[sufficiency]` | operative | sufficiency | workable context frame | 0 | NO_ITEMS | Workable context is limited to the active project root and instruction root boundary. |
| `C:[operative]:[completeness]` | operative | completeness | complete action record | 0 | NO_ITEMS | Complete action record expectations are named in Procedure records without a second distinct gap here. |
| `C:[operative]:[consistency]` | operative | consistency | stable process signal | 0 | NO_ITEMS | Stable process signal is handled by fail-closed hooks and denial precedence language. |
| `C:[evaluative]:[necessity]` | evaluative | necessity | value proof basis | 0 | NO_ITEMS | Value proof basis is the protection of release-managed governance assets. |
| `C:[evaluative]:[sufficiency]` | evaluative | sufficiency | warranted merit context | 0 | NO_ITEMS | Warranted merit context does not introduce a new edit beyond existing security-control scope. |
| `C:[evaluative]:[completeness]` | evaluative | completeness | complete appraisal account | 0 | NO_ITEMS | Complete appraisal account is deferred to verification evidence once implementation exists. |
| `C:[evaluative]:[consistency]` | evaluative | consistency | stable quality signal | 0 | NO_ITEMS | Stable quality signal is maintained by explicit PRD warning preservation and no external expansion. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | `C:[normative]:[consistency]` | RationaleGap | Guidance.md | Guidance.md | Human or source-state owner should accept, correct, or replace the mismatched PRD snapshot before PRD-dependent rows are treated as stable. | Guidance records the hash mismatch as a warning, but several requirements depend on PRD rows; the rationale for proceeding is recorded as Phase 2.2 drafting posture, not closure. | Guidance.md | Considerations; Source-State Warnings | _REFERENCES.md#Authoritative Source Corpus | PROPOSAL | TBD |

## Matrix F

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `F:[normative]:[necessity]` | normative | necessity | binding readiness warrant | 0 | NO_ITEMS | Binding readiness is stated through absolute path, existence, directory, access, and containment preconditions. |
| `F:[normative]:[sufficiency]` | normative | sufficiency | controlled adequacy basis | 0 | NO_ITEMS | Controlled adequacy is represented by denial precedence and code-owned boundary enforcement. |
| `F:[normative]:[completeness]` | normative | completeness | governed coverage frame | 0 | NO_ITEMS | Governed coverage covers validator, helper, hooks, instruction-root denial, and symlink rejection. |
| `F:[normative]:[consistency]` | normative | consistency | stable conformance signal | 0 | NO_ITEMS | Stable conformance is limited by PRD warning but no new F-level conformance issue appears. |
| `F:[operative]:[necessity]` | operative | necessity | executable readiness warrant | 0 | NO_ITEMS | Executable readiness is framed by Procedure prerequisites and implementation steps. |
| `F:[operative]:[sufficiency]` | operative | sufficiency | workable adequacy basis | 0 | NO_ITEMS | Workable adequacy is expressed through normalized path containment and fixture requirements. |
| `F:[operative]:[completeness]` | operative | completeness | bounded coverage frame | 0 | NO_ITEMS | Bounded coverage is explicitly restricted to filesystem policy rather than UI presentation or broad write governance. |
| `F:[operative]:[consistency]` | operative | consistency | stable workflow signal | 1 | HAS_ITEMS | Stable workflow signal exposes terminology that should be normalized between working root, project root, active project root, and accepted root. |
| `F:[evaluative]:[necessity]` | evaluative | necessity | value readiness warrant | 0 | NO_ITEMS | Value readiness aligns with preserving release-managed instruction-root materials. |
| `F:[evaluative]:[sufficiency]` | evaluative | sufficiency | merit adequacy basis | 0 | NO_ITEMS | Merit adequacy is constrained to security-control behavior and not product UI. |
| `F:[evaluative]:[completeness]` | evaluative | completeness | appraisal coverage frame | 0 | NO_ITEMS | Appraisal coverage is expected after implementation evidence exists. |
| `F:[evaluative]:[consistency]` | evaluative | consistency | stable quality signal | 0 | NO_ITEMS | Stable quality signal is sufficiently carried by source warning and test evidence requirements. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | `F:[operative]:[consistency]` | Normalization | Guidance.md | Specification.md | Normalize whether implementation text should use working root, active project root, projectRoot, accepted root, or active root for each boundary check. | Procedure Step 4 introduces active `projectRoot`, while Datasheet and Specification alternate between working root, active project root, and accepted root; implementation APIs need one accepted vocabulary map. | Procedure.md | Steps, steps 4 and 5 | Datasheet.md#Conditions; Specification.md#Requirements; Guidance.md#Principles | PROPOSAL | TBD |

## Matrix D

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `D:[normative]:[guiding]` | normative | guiding | policy closure frame | 0 | NO_ITEMS | Policy closure is represented by mandatory root separation and instruction-root mutation denial. |
| `D:[normative]:[applying]` | normative | applying | mandatory closure method | 0 | NO_ITEMS | Mandatory closure method is the combination of validator, path helper, hooks, and denial precedence. |
| `D:[normative]:[judging]` | normative | judging | conformance verdict basis | 0 | NO_ITEMS | Conformance verdict basis is named in verification approaches and does not add an item here. |
| `D:[normative]:[reviewing]` | normative | reviewing | audit closure standard | 0 | NO_ITEMS | Audit closure standard is linked to preserving source warnings and evidence records. |
| `D:[operative]:[guiding]` | operative | guiding | procedure closure frame | 0 | NO_ITEMS | Procedure closure frame is ordered and complete enough for implementation handoff. |
| `D:[operative]:[applying]` | operative | applying | execution closure method | 1 | HAS_ITEMS | Execution closure method exposes the assumed API reuse path, which requires implementation confirmation. |
| `D:[operative]:[judging]` | operative | judging | performance verdict basis | 0 | NO_ITEMS | Performance verdict basis is test-output driven and covered by the B and X verification items. |
| `D:[operative]:[reviewing]` | operative | reviewing | process assurance standard | 0 | NO_ITEMS | Process assurance standard is carried by fail-closed hook and triage record expectations. |
| `D:[evaluative]:[guiding]` | evaluative | guiding | value closure frame | 0 | NO_ITEMS | Value closure frame remains root integrity plus safe execution state. |
| `D:[evaluative]:[applying]` | evaluative | applying | merit closure method | 0 | NO_ITEMS | Merit closure method is not separate from mandatory enforcement and fixture evidence. |
| `D:[evaluative]:[judging]` | evaluative | judging | worth verdict basis | 0 | NO_ITEMS | Worth verdict basis awaits implementation evidence and does not need a new production edit in this lens. |
| `D:[evaluative]:[reviewing]` | evaluative | reviewing | quality assurance standard | 0 | NO_ITEMS | Quality assurance standard is represented by warning preservation and complete fixture coverage. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | `D:[operative]:[applying]` | VerificationGap | Specification.md | Specification.md | Confirm whether `/api/working-root/validate` is the implementation surface and whether downstream tree, scan, chat session, scaffold, and contract APIs reuse the same normalized root. | Specification marks endpoint reuse as an ASSUMPTION and Procedure Step 4 uses equivalent language, so execution closure cannot treat the reuse path as verified. | Specification.md | Requirements, REQ-07-01-011; Verification | Procedure.md#Steps step 4 | PROPOSAL | TBD |

## Matrix X

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `X:[guiding]:[necessity]` | guiding | necessity | root validity warrant | 0 | NO_ITEMS | Root validity warrant is explicit for absolute, existing, directory, readable, writable roots outside instruction root. |
| `X:[guiding]:[sufficiency]` | guiding | sufficiency | containment adequacy proof | 0 | NO_ITEMS | Containment adequacy proof is named through helper tests and hook integration expectations. |
| `X:[guiding]:[completeness]` | guiding | completeness | boundary coverage account | 0 | NO_ITEMS | Boundary coverage account spans working-root selection, path containment, instruction-root protection, and symlink rejection. |
| `X:[guiding]:[consistency]` | guiding | consistency | denial coherence signal | 0 | NO_ITEMS | Denial coherence signal is expressed by deny-beats-allow and fail-closed guidance. |
| `X:[applying]:[necessity]` | applying | necessity | enforcement readiness proof | 0 | NO_ITEMS | Enforcement readiness proof is represented by required implementation artifacts. |
| `X:[applying]:[sufficiency]` | applying | sufficiency | containment context basis | 0 | NO_ITEMS | Containment context basis is limited to active project-root and instruction-root checks. |
| `X:[applying]:[completeness]` | applying | completeness | bounded path record | 0 | NO_ITEMS | Bounded path record is described through test matrix and expected records. |
| `X:[applying]:[consistency]` | applying | consistency | closed failure signal | 0 | NO_ITEMS | Closed failure signal is explicit in hook failure behavior. |
| `X:[judging]:[necessity]` | judging | necessity | failure evidence basis | 0 | NO_ITEMS | Failure evidence basis is covered by typed or inspectable error expectations. |
| `X:[judging]:[sufficiency]` | judging | sufficiency | typed denial warrant | 0 | NO_ITEMS | Typed denial warrant is represented in verification pass conditions. |
| `X:[judging]:[completeness]` | judging | completeness | fixture coverage account | 1 | HAS_ITEMS | Fixture coverage account exposes missing final test command names and evidence locations. |
| `X:[judging]:[consistency]` | judging | consistency | separation coherence signal | 0 | NO_ITEMS | Separation coherence signal is consistent across Datasheet, Specification, Guidance, and Procedure. |
| `X:[reviewing]:[necessity]` | reviewing | necessity | audit evidence frame | 0 | NO_ITEMS | Audit evidence frame is the record set named in Procedure. |
| `X:[reviewing]:[sufficiency]` | reviewing | sufficiency | boundary assurance basis | 0 | NO_ITEMS | Boundary assurance basis is clear for this deliverable without external source expansion. |
| `X:[reviewing]:[completeness]` | reviewing | completeness | omission coverage record | 0 | NO_ITEMS | Omission coverage is captured by documentation gaps and records still TBD. |
| `X:[reviewing]:[consistency]` | reviewing | consistency | source warning signal | 1 | HAS_ITEMS | Source warning signal exposes dependency and sibling-scope caution that remains unaccepted as a formal edge. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | `X:[judging]:[completeness]` | MissingSlot | Procedure.md | Procedure.md | Implementation worker must fill final test command names and evidence record locations for root validation, path policy, instruction-root protection, hook failure, and symlink fixtures. | Procedure records final test command names and implementation paths as TBD, so fixture coverage cannot be complete until those evidence routes are identified. | Procedure.md | Records still TBD; Verification | Specification.md#Documentation gaps | PROPOSAL | TBD |
| X-002 | `X:[reviewing]:[consistency]` | TBD_Question | Guidance.md | Guidance.md | Decide whether DEL-06-04 is only a coordination note or should become an accepted dependency edge for write/edit hook enforcement. | Guidance states the DEL-06-04 relationship is inferred and not accepted as a dependency edge, while `_DEPENDENCIES.md` also records no formal downstream or upstream edges. | Guidance.md | Considerations | _DEPENDENCIES.md#Declared Upstream; _DEPENDENCIES.md#Declared Downstream | PROPOSAL | TBD |

## Matrix E

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `E:[guiding]:[data]` | guiding | data | factual routing warrant | 0 | NO_ITEMS | Factual routing warrant is supported by root meaning, instruction-root meaning, and ordinary write-location attributes. |
| `E:[guiding]:[information]` | guiding | information | contextual containment frame | 0 | NO_ITEMS | Contextual containment frame is bounded to the active working root and instruction root. |
| `E:[guiding]:[knowledge]` | guiding | knowledge | enforcement understanding map | 0 | NO_ITEMS | Enforcement understanding map is present across principles, examples, and procedure steps. |
| `E:[guiding]:[wisdom]` | guiding | wisdom | principled boundary judgment | 0 | NO_ITEMS | Principled boundary judgment is expressed by deny precedence and initial symlink rejection. |
| `E:[applying]:[data]` | applying | data | actionable validation proof | 0 | NO_ITEMS | Actionable validation proof is named through root validation cases and evidence records. |
| `E:[applying]:[information]` | applying | information | usable containment context | 0 | NO_ITEMS | Usable containment context is clear for project-relative, absolute-inside, absolute-outside, and traversal paths. |
| `E:[applying]:[knowledge]` | applying | knowledge | enforcement readiness map | 0 | NO_ITEMS | Enforcement readiness map is limited by code-path TBDs already recorded in A and X. |
| `E:[applying]:[wisdom]` | applying | wisdom | prudent denial judgment | 1 | HAS_ITEMS | Prudent denial judgment highlights that symlink relaxation needs governed amendment and tests before acceptance. |
| `E:[judging]:[data]` | judging | data | error fact basis | 0 | NO_ITEMS | Error fact basis is expected through typed or inspectable rejection evidence. |
| `E:[judging]:[information]` | judging | information | typed denial context | 0 | NO_ITEMS | Typed denial context is described by verification pass conditions without a separate new item. |
| `E:[judging]:[knowledge]` | judging | knowledge | protection understanding map | 0 | NO_ITEMS | Protection understanding map is clear across root separation, containment, and instruction-root denial. |
| `E:[judging]:[wisdom]` | judging | wisdom | principled verdict judgment | 0 | NO_ITEMS | Principled verdict judgment remains future acceptance evidence rather than a current edit. |
| `E:[reviewing]:[data]` | reviewing | data | audit fact basis | 0 | NO_ITEMS | Audit fact basis is the preserved warning plus test evidence route. |
| `E:[reviewing]:[information]` | reviewing | information | source warning context | 1 | HAS_ITEMS | Source warning context exposes the need to carry the PRD mismatch into future implementation and review records. |
| `E:[reviewing]:[knowledge]` | reviewing | knowledge | coverage understanding map | 0 | NO_ITEMS | Coverage understanding map is bounded by the complete fixture list in Procedure. |
| `E:[reviewing]:[wisdom]` | reviewing | wisdom | closure judgment frame | 0 | NO_ITEMS | Closure judgment frame awaits accepted evidence and source-state disposition. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | `E:[applying]:[wisdom]` | VerificationGap | Guidance.md | Procedure.md | If any future symlink-write relaxation is proposed, require an amendment reference and targeted fixture evidence before treating it as accepted. | Guidance and Procedure both state initial symlink rejection and future relaxation by governed amendment, but no amendment or relaxation evidence exists in this deliverable. | Guidance.md | Considerations; Trade-offs | Procedure.md#Steps step 8; Specification.md#Requirements REQ-07-01-007 | PROPOSAL | TBD |
| E-002 | `E:[reviewing]:[information]` | TBD_Question | Datasheet.md | Procedure.md | Determine where implementation and review records must preserve the `docs/PRD.md` hash mismatch warning. | Datasheet and Procedure require preserving the PRD hash warning, but final evidence location and review-note convention remain unspecified. | Datasheet.md | Conditions; References | Procedure.md#Verification; Procedure.md#Records | PROPOSAL | TBD |
