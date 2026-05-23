# Semantic Lensing Register: DEL-07-03 Deliverable Metadata and Document Kit Contracts

**Generated:** 2026-05-20
**Deliverable Folder:** `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts`
**DECOMP_VARIANT:** SOFTWARE
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts`
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
- `[WARNING] SOURCE_STATE`: `_REFERENCES.md` marks `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived file-layout claims remain warning-qualified.
- `[WARNING] TBD_IMPLEMENTATION_CONTRACTS`: implementation location, scanner output schema, severity policy, and final test command names remain TBD in the production kit.
- `[WARNING] DEPENDENCY_STATE`: `_DEPENDENCIES.md` contains extracted ACTIVE dependency rows while the declared dependency sections remain unaccepted/TBD.

## Summary

Total warranted items: 11

By matrix:
- A: 1
- B: 1
- C: 1
- F: 2
- D: 2
- X: 2
- E: 2

By type:
- MissingSlot: 3
- WeakStatement: 1
- Conflict: 0
- VerificationGap: 4
- RationaleGap: 1
- Normalization: 1
- TBD_Question: 1
- MatrixError: 0

By document:
- Datasheet.md: 2
- Specification.md: 7
- Guidance.md: 6
- Procedure.md: 8
- _DEPENDENCIES.md: 1
- _REFERENCES.md: 1

## Matrix A

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `A:[normative]:[guiding]` | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Prescriptive direction is clear in the named file-contract categories and root-authority guidance. |
| `A:[normative]:[applying]` | normative | applying | mandatory practice | 1 | HAS_ITEMS | Mandatory practice exposes that scanner implementation ownership is still not assigned. |
| `A:[normative]:[judging]` | normative | judging | compliance determination | 0 | NO_ITEMS | Compliance determination is deferred to scanner and fixture evidence rather than asserted in the draft. |
| `A:[normative]:[reviewing]` | normative | reviewing | regulatory audit | 0 | NO_ITEMS | Regulatory audit is represented by source-warning visibility and document-kit evidence posture. |
| `A:[operative]:[guiding]` | operative | guiding | procedural direction | 0 | NO_ITEMS | Procedural direction is ordered through scope confirmation, fixture definition, scanner implementation, and verification steps. |
| `A:[operative]:[applying]` | operative | applying | practical execution | 0 | NO_ITEMS | Practical execution gaps are more concrete under F, D, X, and E where implementation details are missing. |
| `A:[operative]:[judging]` | operative | judging | performance assessment | 0 | NO_ITEMS | Performance assessment is tied to test fixture results, not an orientation-only issue. |
| `A:[operative]:[reviewing]` | operative | reviewing | process audit | 0 | NO_ITEMS | Process audit is bounded to local records and warning preservation without sibling expansion. |
| `A:[evaluative]:[guiding]` | evaluative | guiding | value orientation | 0 | NO_ITEMS | Value orientation is stable: make deliverable-local filesystem truth machine-readable. |
| `A:[evaluative]:[applying]` | evaluative | applying | merit application | 0 | NO_ITEMS | Merit application is limited to scanner use and does not add a separate production-document gap. |
| `A:[evaluative]:[judging]` | evaluative | judging | worth determination | 0 | NO_ITEMS | Worth determination awaits implementation and verification evidence. |
| `A:[evaluative]:[reviewing]` | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Quality appraisal is sufficiently framed by explicit optional, required, recommended, and prohibited file categories. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | `A:[normative]:[applying]` | MissingSlot | Procedure.md | Procedure.md | Assign the scanner implementation location and owning backend surface for deliverable-folder detection, metadata validation, document-kit detection, memory checks, and semantic placeholder checks. | Procedure lists implementation location as TBD, while Specification requires scanner and validator behavior; mandatory practice cannot close without an implementation anchor. | Procedure.md; Specification.md | Prerequisites; Requirements | Specification.md#Requirements | PROPOSAL | TBD |

## Matrix B

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `B:[data]:[necessity]` | data | necessity | essential fact | 0 | NO_ITEMS | Essential facts name the required metadata files, document-kit files, memory file, optional files, and lifecycle states. |
| `B:[data]:[sufficiency]` | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Evidence sufficiency is source-cited across Datasheet, Specification, Guidance, and Procedure, subject to the PRD warning. |
| `B:[data]:[completeness]` | data | completeness | comprehensive record | 0 | NO_ITEMS | Comprehensive record needs are described through required artifacts, records, and fixture expectations. |
| `B:[data]:[consistency]` | data | consistency | reliable measurement | 1 | HAS_ITEMS | Reliable measurement is weakened by open severity vocabulary for required, recommended, optional, and prohibited conditions. |
| `B:[information]:[necessity]` | information | necessity | essential signal | 0 | NO_ITEMS | Essential signals include missing metadata, document-kit bucket presence, canonical memory, and prohibited memory detection. |
| `B:[information]:[sufficiency]` | information | sufficiency | adequate context | 0 | NO_ITEMS | Adequate context is bounded to DEL-07-03 and excludes status transition and dependency parser ownership. |
| `B:[information]:[completeness]` | information | completeness | comprehensive account | 0 | NO_ITEMS | Comprehensive account is present through scope, requirements, trade-offs, examples, and procedure records. |
| `B:[information]:[consistency]` | information | consistency | coherent message | 0 | NO_ITEMS | Coherent message is maintained by repeated strict treatment of `_MEMORY.md` and optional treatment of `_SEMANTIC_LENSING.md`. |
| `B:[knowledge]:[necessity]` | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Fundamental understanding distinguishes file presence scanning from lifecycle transition enforcement. |
| `B:[knowledge]:[sufficiency]` | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Competent expertise depends on implementation selection and is registered under A and D rather than duplicated here. |
| `B:[knowledge]:[completeness]` | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Thorough mastery is represented by the planned fixture categories. |
| `B:[knowledge]:[consistency]` | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Coherent understanding holds across memory, semantic, metadata, and document-kit concepts. |
| `B:[wisdom]:[necessity]` | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Essential discernment is clear in refusing `_MEMORY.md` compatibility fallback. |
| `B:[wisdom]:[sufficiency]` | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Adequate judgment is expressed by tying missing document-kit severity to lifecycle state. |
| `B:[wisdom]:[completeness]` | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Holistic insight spans source warnings, file categories, boundaries, and sibling ownership exclusions. |
| `B:[wisdom]:[consistency]` | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Principled reasoning is stable: explicit contracts take precedence over inference. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | `B:[data]:[consistency]` | Normalization | Guidance.md | Specification.md | Normalize the scanner finding categories and severity names for required metadata, PREPARATION baseline files, recommended document kit files, optional files, prohibited files, and source warnings. | Guidance says severity policy is partly source-defined and partly implementation-defined, while Specification verification still uses baseline warning or failure state language; measurement will be inconsistent without one vocabulary map. | Guidance.md; Specification.md; Procedure.md | Considerations; Requirements REQ-003; Verification | Guidance.md#Considerations; Procedure.md#Verification | PROPOSAL | TBD |

## Matrix C

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `C:[normative]:[necessity]` | normative | necessity | source mandate | 0 | NO_ITEMS | Source mandate is grounded in SPEC, PRD, TYPES, CONTRACT, DIRECTIVE, and PLAN references. |
| `C:[normative]:[sufficiency]` | normative | sufficiency | evidence threshold | 0 | NO_ITEMS | Evidence threshold is clear for local drafting, with the PRD mismatch kept visible. |
| `C:[normative]:[completeness]` | normative | completeness | record baseline | 0 | NO_ITEMS | Record baseline includes metadata, document-kit, memory, semantic placeholder, and optional-file categories. |
| `C:[normative]:[consistency]` | normative | consistency | policy coherence | 1 | HAS_ITEMS | Policy coherence is limited by the unresolved PRD hash mismatch for several source-backed requirements. |
| `C:[operative]:[necessity]` | operative | necessity | action prerequisite | 0 | NO_ITEMS | Action prerequisites are captured as source confirmation, fixture definition, implementation, and verification steps. |
| `C:[operative]:[sufficiency]` | operative | sufficiency | execution proof | 0 | NO_ITEMS | Execution proof gaps are tied to concrete test and implementation evidence under D and X. |
| `C:[operative]:[completeness]` | operative | completeness | task coverage | 0 | NO_ITEMS | Task coverage spans the anticipated artifacts named in context and decomposition. |
| `C:[operative]:[consistency]` | operative | consistency | process alignment | 0 | NO_ITEMS | Process alignment is maintained by explicit exclusion of DEL-07-04 and DEL-07-05 responsibilities. |
| `C:[evaluative]:[necessity]` | evaluative | necessity | value criterion | 0 | NO_ITEMS | Value criterion is the scanner-readable representation of deliverable-local contracts. |
| `C:[evaluative]:[sufficiency]` | evaluative | sufficiency | appraisal basis | 0 | NO_ITEMS | Appraisal basis remains warning-aware and implementation-evidence-dependent. |
| `C:[evaluative]:[completeness]` | evaluative | completeness | judgment coverage | 0 | NO_ITEMS | Judgment coverage is expected after fixture results exist. |
| `C:[evaluative]:[consistency]` | evaluative | consistency | review coherence | 0 | NO_ITEMS | Review coherence is supported by source warning notes and scope exclusions. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | `C:[normative]:[consistency]` | RationaleGap | Guidance.md | Guidance.md | Human or source-state owner should accept, correct, or explicitly bypass the `docs/PRD.md` hash mismatch before PRD-derived scanner contract rows are treated as closure evidence. | The production kit uses PRD sections for folder layout, document-kit, and memory requirements while `_REFERENCES.md` records REF-006 as HASH_MISMATCH; the rationale for proceeding is warning posture, not accepted source closure. | _REFERENCES.md; Guidance.md; Datasheet.md | Authoritative Source Corpus REF-006; Source Warning Notes; References | Datasheet.md#References; Procedure.md#Prerequisites | PROPOSAL | TBD |

## Matrix F

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `F:[normative]:[necessity]` | normative | necessity | rule obligation | 0 | NO_ITEMS | Rule obligation is explicit for required metadata files, canonical memory, and prohibited `_MEMORY.md`. |
| `F:[normative]:[sufficiency]` | normative | sufficiency | proof standard | 0 | NO_ITEMS | Proof standard is conceptually present through verification rows and expected test fixtures. |
| `F:[normative]:[completeness]` | normative | completeness | baseline coverage | 0 | NO_ITEMS | Baseline coverage includes `_SEMANTIC.md` and optional `_SEMANTIC_LENSING.md` distinction. |
| `F:[normative]:[consistency]` | normative | consistency | policy alignment | 0 | NO_ITEMS | Policy alignment holds by leaving lifecycle transitions and dependency parsing to sibling slices. |
| `F:[operative]:[necessity]` | operative | necessity | task prerequisite | 1 | HAS_ITEMS | Task prerequisite exposes the missing scanner output schema. |
| `F:[operative]:[sufficiency]` | operative | sufficiency | execution evidence | 1 | HAS_ITEMS | Execution evidence exposes unresolved severity policy for scanner findings. |
| `F:[operative]:[completeness]` | operative | completeness | workflow coverage | 0 | NO_ITEMS | Workflow coverage is described from fixture definition through records maintenance. |
| `F:[operative]:[consistency]` | operative | consistency | process coherence | 0 | NO_ITEMS | Process coherence is maintained by preserving source warnings and boundary exclusions. |
| `F:[evaluative]:[necessity]` | evaluative | necessity | value requirement | 0 | NO_ITEMS | Value requirement is scanner-readable deliverable contract enforcement. |
| `F:[evaluative]:[sufficiency]` | evaluative | sufficiency | merit evidence | 0 | NO_ITEMS | Merit evidence will come from implementation and tests, not additional Phase 2.4 text. |
| `F:[evaluative]:[completeness]` | evaluative | completeness | appraisal coverage | 0 | NO_ITEMS | Appraisal coverage is bounded to metadata, kit, memory, and semantic placeholder behavior. |
| `F:[evaluative]:[consistency]` | evaluative | consistency | judgment coherence | 0 | NO_ITEMS | Judgment coherence is adequate once unresolved TBD values are carried forward. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | `F:[operative]:[necessity]` | MissingSlot | Procedure.md | Specification.md | Define the scanner output schema for findings, file categories, lifecycle-conditioned kit findings, source/hash warnings, and unknown unsupported conditions. | Procedure lists scanner output schema as TBD and Guidance assumes structured findings; task prerequisite cannot be implemented deterministically without the shape of the result contract. | Procedure.md; Guidance.md; Specification.md | Prerequisites; Considerations; Requirements REQ-009 | Guidance.md#Considerations | PROPOSAL | TBD |
| F-002 | `F:[operative]:[sufficiency]` | VerificationGap | Specification.md | Specification.md | Decide and test exact severity behavior for missing `_SEMANTIC.md`, missing initialized document-kit files, optional-file absence, prohibited `_MEMORY.md`, and source/hash warnings. | Specification and Guidance repeatedly mark exact severity as TBD; execution evidence cannot prove scanner behavior if expected severity is not accepted. | Specification.md; Guidance.md; Procedure.md | Requirements REQ-003; Trade-offs; Verification | Specification.md#Verification; Guidance.md#Trade-offs | PROPOSAL | TBD |

## Matrix D

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `D:[normative]:[guiding]` | normative | guiding | contract direction | 0 | NO_ITEMS | Contract direction names strict file categories and warning visibility. |
| `D:[normative]:[applying]` | normative | applying | required practice | 0 | NO_ITEMS | Required practice is clear at the document-contract level, pending implementation binding. |
| `D:[normative]:[judging]` | normative | judging | conformance finding | 0 | NO_ITEMS | Conformance finding is test-driven and not claimed in this setup register. |
| `D:[normative]:[reviewing]` | normative | reviewing | governance review | 0 | NO_ITEMS | Governance review is supported by evidence posture and human-gate exclusions. |
| `D:[operative]:[guiding]` | operative | guiding | scanner direction | 0 | NO_ITEMS | Scanner direction is sufficiently described in the procedure sequence. |
| `D:[operative]:[applying]` | operative | applying | validation execution | 1 | HAS_ITEMS | Validation execution is blocked by unassigned implementation and test paths. |
| `D:[operative]:[judging]` | operative | judging | behavior assessment | 0 | NO_ITEMS | Behavior assessment is represented by verification rows and fixture categories. |
| `D:[operative]:[reviewing]` | operative | reviewing | workflow audit | 1 | HAS_ITEMS | Workflow audit exposes the mismatch between declared and extracted dependency state. |
| `D:[evaluative]:[guiding]` | evaluative | guiding | source posture | 0 | NO_ITEMS | Source posture is explicit through the HASH_MISMATCH warning and local evidence notes. |
| `D:[evaluative]:[applying]` | evaluative | applying | merit use | 0 | NO_ITEMS | Merit use is bounded to scanner output consumption by adjacent APIs. |
| `D:[evaluative]:[judging]` | evaluative | judging | warning disposition | 0 | NO_ITEMS | Warning disposition remains open and is captured under C and X rather than duplicated. |
| `D:[evaluative]:[reviewing]` | evaluative | reviewing | quality review | 0 | NO_ITEMS | Quality review can proceed after severity, schema, and fixture paths are assigned. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | `D:[operative]:[applying]` | VerificationGap | Procedure.md | Procedure.md | Name implementation files, fixture locations, and final test commands for metadata scanner, document-kit detection, canonical memory acceptance, `_MEMORY.md` rejection, semantic placeholders, warning propagation, and route/API compatibility. | Procedure records implementation location and exact test command as TBD, while Specification requires multiple verification categories; validation execution cannot close without concrete evidence paths. | Procedure.md; Specification.md | Prerequisites; Steps 9; Verification; Documentation | Specification.md#Verification | PROPOSAL | TBD |
| D-002 | `D:[operative]:[reviewing]` | TBD_Question | Procedure.md | Procedure.md | Reconcile whether extracted ACTIVE dependency rows in `_DEPENDENCIES.md` should update the Procedure prerequisite that declared upstream dependencies are TBD and unaccepted. | Procedure says no accepted dependency edges have been extracted yet, but `_DEPENDENCIES.md` now lists 10 ACTIVE extracted rows; workflow audit needs an explicit current-state ruling without treating extracted rows as accepted declared dependencies. | Procedure.md; _DEPENDENCIES.md | Prerequisites; Extracted Dependency Register | _DEPENDENCIES.md#Declared Upstream; _DEPENDENCIES.md#Extracted Dependency Register | PROPOSAL | TBD |

## Matrix X

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `X:[guiding]:[necessity]` | guiding | necessity | contract need | 0 | NO_ITEMS | Contract need is explicit for metadata, document kit, memory, semantic placeholder, and optional-file handling. |
| `X:[guiding]:[sufficiency]` | guiding | sufficiency | source proof | 0 | NO_ITEMS | Source proof is sufficient for drafting when the PRD warning remains attached. |
| `X:[guiding]:[completeness]` | guiding | completeness | contract coverage | 0 | NO_ITEMS | Contract coverage includes the core file categories named by context and production docs. |
| `X:[guiding]:[consistency]` | guiding | consistency | authority coherence | 0 | NO_ITEMS | Authority coherence is maintained by preserving source mismatch status rather than resolving it locally. |
| `X:[applying]:[necessity]` | applying | necessity | practice prerequisite | 0 | NO_ITEMS | Practice prerequisites are captured in the implementation-location and schema items. |
| `X:[applying]:[sufficiency]` | applying | sufficiency | validation evidence | 1 | HAS_ITEMS | Validation evidence is missing for final tests and fixture outputs. |
| `X:[applying]:[completeness]` | applying | completeness | bucket coverage | 0 | NO_ITEMS | Bucket coverage is clear at the document level for Datasheet, Specification, Guidance, and Procedure. |
| `X:[applying]:[consistency]` | applying | consistency | workflow alignment | 0 | NO_ITEMS | Workflow alignment is preserved by not absorbing DEL-07-04 or DEL-07-05 responsibilities. |
| `X:[judging]:[necessity]` | judging | necessity | conformance criterion | 0 | NO_ITEMS | Conformance criteria are enumerated in the verification table. |
| `X:[judging]:[sufficiency]` | judging | sufficiency | finding evidence | 0 | NO_ITEMS | Finding evidence is expected from tests once implementation paths exist. |
| `X:[judging]:[completeness]` | judging | completeness | warning coverage | 1 | HAS_ITEMS | Warning coverage requires a tested output/report representation for source hash warnings and unknowns. |
| `X:[judging]:[consistency]` | judging | consistency | disposition coherence | 0 | NO_ITEMS | Disposition coherence remains warning-aware and human-ruling dependent. |
| `X:[reviewing]:[necessity]` | reviewing | necessity | audit need | 0 | NO_ITEMS | Audit need is represented by records for references, fixtures, diffs, test results, and unresolved TBDs. |
| `X:[reviewing]:[sufficiency]` | reviewing | sufficiency | review evidence | 0 | NO_ITEMS | Review evidence is unavailable until the implementation pass runs tests. |
| `X:[reviewing]:[completeness]` | reviewing | completeness | assurance coverage | 0 | NO_ITEMS | Assurance coverage is complete in concept across file categories and source warnings. |
| `X:[reviewing]:[consistency]` | reviewing | consistency | quality coherence | 0 | NO_ITEMS | Quality coherence depends on carrying blockers forward rather than editing production docs in this phase. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | `X:[applying]:[sufficiency]` | VerificationGap | Specification.md | Specification.md | Provide concrete passing test names, fixture paths, and command outputs for complete and incomplete metadata, valid and invalid folder identity, document-kit states, memory behavior, semantic placeholders, optional files, and path/root governance where applicable. | Specification lists verification items but no concrete tests or fixtures; applying-level validation evidence cannot be sufficient until the implementation pass produces those records. | Specification.md; Procedure.md | Verification; Steps 2 and 9; Records | Procedure.md#Records | PROPOSAL | TBD |
| X-002 | `X:[judging]:[completeness]` | VerificationGap | Specification.md | Specification.md | Verify that output/report behavior preserves REF-006 HASH_MISMATCH and unsupported or unknown conditions with the accepted schema and severity vocabulary. | Requirement REQ-009 requires warning visibility, but exact output schema remains TBD and no warning propagation test is cited. | Specification.md; Procedure.md; _REFERENCES.md | Requirements REQ-009; Verification; Authoritative Source Corpus REF-006 | Guidance.md#Source Warning Notes | PROPOSAL | TBD |

## Matrix E

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `E:[guiding]:[data]` | guiding | data | factual contract | 0 | NO_ITEMS | Factual contract is present in the Datasheet file inventories and lifecycle states. |
| `E:[guiding]:[information]` | guiding | information | signal authority | 0 | NO_ITEMS | Signal authority is clear for source warning, root authority, and hidden-memory posture. |
| `E:[guiding]:[knowledge]` | guiding | knowledge | conceptual boundary | 0 | NO_ITEMS | Conceptual boundary separates scanner reporting from lifecycle transition and dependency parser ownership. |
| `E:[guiding]:[wisdom]` | guiding | wisdom | principled contract | 0 | NO_ITEMS | Principled contract favors explicit named files over heuristic inference. |
| `E:[applying]:[data]` | applying | data | file evidence | 1 | HAS_ITEMS | File evidence needs an accepted machine-readable result model. |
| `E:[applying]:[information]` | applying | information | contextual finding | 0 | NO_ITEMS | Contextual findings are described by missing required, recommended, optional, prohibited, and warning categories. |
| `E:[applying]:[knowledge]` | applying | knowledge | scanner mastery | 0 | NO_ITEMS | Scanner mastery is pending implementation and test evidence already registered under D and X. |
| `E:[applying]:[wisdom]` | applying | wisdom | reasoned practice | 0 | NO_ITEMS | Reasoned practice is to reject `_MEMORY.md` and keep optional-file absence non-fatal. |
| `E:[judging]:[data]` | judging | data | factual criterion | 0 | NO_ITEMS | Factual criteria are stated in verification checks. |
| `E:[judging]:[information]` | judging | information | message finding | 0 | NO_ITEMS | Message finding requires accepted schema but has no separate item beyond E-001. |
| `E:[judging]:[knowledge]` | judging | knowledge | conformance mastery | 1 | HAS_ITEMS | Conformance mastery is limited by an assumption about API consumers and route shape stability. |
| `E:[judging]:[wisdom]` | judging | wisdom | principled disposition | 0 | NO_ITEMS | Principled disposition is to keep warnings visible and human-ruling dependent. |
| `E:[reviewing]:[data]` | reviewing | data | audit fact | 0 | NO_ITEMS | Audit facts are expected in source references, implementation diff, fixture list, and test results. |
| `E:[reviewing]:[information]` | reviewing | information | assurance signal | 0 | NO_ITEMS | Assurance signal remains incomplete until unresolved TBD values are cleared. |
| `E:[reviewing]:[knowledge]` | reviewing | knowledge | quality mastery | 0 | NO_ITEMS | Quality mastery is bounded to the deliverable-local scanner contract. |
| `E:[reviewing]:[wisdom]` | reviewing | wisdom | reasoned assurance | 0 | NO_ITEMS | Reasoned assurance is possible only after warning, schema, severity, and fixture evidence are accepted. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | `E:[applying]:[data]` | MissingSlot | Specification.md | Specification.md | Define the scanner result data model for present files, missing canonical files, missing lifecycle-conditioned document-kit buckets, accepted canonical memory, prohibited `_MEMORY.md`, optional-file absence, optional-file presence, source warnings, and unknown conditions. | The documents name categories but leave the machine-readable output schema TBD; applying-level file evidence cannot be consumed reliably without stable fields. | Specification.md; Guidance.md; Procedure.md | Requirements; Considerations; Prerequisites | Guidance.md#Considerations | PROPOSAL | TBD |
| E-002 | `E:[judging]:[knowledge]` | WeakStatement | Specification.md | Specification.md | Replace or confirm the API compatibility assumption with an accepted consumer contract for `/api/working-root/scope` or adjacent project APIs, including whether public route shapes are fixed. | Specification REQ-010 says scanner outputs should be consumable by adjacent APIs without changing route shapes, but the implementation binding and integration test remain TBD. | Specification.md; Guidance.md; Procedure.md | Requirements REQ-010; Considerations; Verification | Guidance.md#Considerations | PROPOSAL | TBD |
