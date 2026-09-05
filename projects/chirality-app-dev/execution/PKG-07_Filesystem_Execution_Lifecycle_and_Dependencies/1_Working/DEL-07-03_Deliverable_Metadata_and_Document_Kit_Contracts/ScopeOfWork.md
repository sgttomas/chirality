---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-03
package_id: PKG-07
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-026, SOW-081]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-07-03

## Purpose and Objective Traceability

This candidate defines `DEL-07-03` in service of project scope [SOW-026, SOW-081] and package objectives [OBJ-006].

- **OUT-001** — Metadata scanner and document-kit contract implementation with evidence for required, baseline, optional, and prohibited deliverable-local file handling.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

`DEL-07-03 Deliverable Metadata and Document Kit Contracts` (BACKEND_FEATURE_SLICE, applied decomposition row L359):

Scan and validate deliverable metadata files, canonical memory, semantic
placeholders, and document kit buckets; define the governed workflow file
contract (front matter, roadmap grammar with gate markers, app-maintained
position, library/bind copy semantics) and the rule that the file steers and
never records.

Applied row notes: One deliverable-folder contract slice.

Applied row outputs: Metadata scanners; document kit detection; `_MEMORY.md`
rejection tests; workflow file contract and validator tests.

### Current acceptance obligations

1. Deliverable metadata, canonical memory, semantic placeholders, and document kit buckets are scanned and validated as before.
2. The governed workflow file contract defines front matter (agent role, folder, permission, delegation policy, where briefs run, `roadmapSource` and hash), the roadmap grammar with human-gate markers, the app-maintained position with who-advanced attribution (Q16), and library/bind copy semantics (Q10).
3. The file steers and never records: status, approvals, and evidence stay in deliverable records and the validator refuses them.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-07-03-V3-01. Ruled
questions applied here: Q10, Q16. Alignment writes WI-046, WI-047, WI-048,
WI-049, WI-050 performed in run `APP_SCA_APP_010_SEATING_2026-09-04`; dependency
writes DEP-019, DEP-020 await the registered dependency-extract pass after owner
acceptance of this alignment. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> #### Datasheet: DEL-07-03 Deliverable Metadata and Document Kit Contracts
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value | Source |
> |---|---|---|
> | Deliverable ID | DEL-07-03 | `_CONTEXT.md` / Identity |
> | Deliverable name | Deliverable Metadata and Document Kit Contracts | `_CONTEXT.md` / Identity |
> | Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies | `_CONTEXT.md` / Identity; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / PKG-07 |
> | Decomposition variant | SOFTWARE_DECOMP v3.2 | `_CONTEXT.md` / Identity |
> | Responsible party | TBD | `_CONTEXT.md` / Identity |
> | Type | BACKEND_FEATURE_SLICE | `_CONTEXT.md` / Identity |
> | Context envelope | M | `_CONTEXT.md` / Identity |
> | Scope item | SOW-026 | `_CONTEXT.md` / Traceability; decomposition / SOW mapping |
> | Objective | OBJ-006 | `_CONTEXT.md` / Traceability |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary subject | Scan and validate deliverable metadata files, canonical memory, semantic placeholders, and document kit buckets. | `_CONTEXT.md` / Deliverable Scope; decomposition / DEL-07-03 row |
> | Anticipated artifacts | Metadata scanners; document kit detection; `_MEMORY.md` rejection tests | `_CONTEXT.md` / Anticipated Artifacts; decomposition / DEL-07-03 row |
> | Required metadata files | `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md` | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 |
> | Minimum PREPARATION fileset | Required metadata files plus `_SEMANTIC.md` placeholder | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 |
> | Document kit files | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 |
> | Canonical memory file | `MEMORY.md` | `docs/SPEC.md` / Section 5.4 |
> | Disabled memory file | `_MEMORY.md` MUST NOT be created in this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 |
> | Optional deliverable files | `Dependencies.csv`, `MEMORY.md`, `_SEMANTIC_LENSING.md`, `HASH_VERIFICATION_BYPASS.jsonl` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 |
> | Lifecycle states | `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, `ISSUED` | `docs/SPEC.md` / Section 4.2; `docs/TYPES.md` / lifecycle state table |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Working-root authority | Project truth is written under the working root; instruction-root writes are outside ordinary execution. | `docs/DIRECTIVE.md` / Section 2.7; `docs/CONTRACT.md` / K-ROOT-1 through K-ROOT-3 |
> | Evidence posture | Important claims and dependency evidence use source paths; assumptions, proposals, unknowns, and conflicts remain visible. | `docs/DIRECTIVE.md` / Section 2.5; `docs/CONTRACT.md` / K-CONFLICT-1 |
> | Lifecycle transition rule | `_STATUS.md` is canonical; transitions are forward-only unless a human explicitly amends the record. | `docs/SPEC.md` / Section 4.3; `docs/PRD.md` / FR-052 and FR-053 |
> | Human gate rule | `CHECKING` and `ISSUED` transitions require approval SHA evidence and cannot be authored by agents. | `docs/SPEC.md` / Section 4.3; `docs/CONTRACT.md` / K-AUTH-1, K-GATE-1 |
> | Reference hash posture | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` / REF-006 — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected construction | Source |
> |---|---|---|
> | Metadata scanner | Detect deliverable folders by valid `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` prefix and presence of `_STATUS.md`; validate required metadata files against SPEC/PRD expectations. | `docs/PRD.md` / FR-047, FR-048; `docs/SPEC.md` / Section 3.1 |
> | Document kit detector | Treat `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` as first-class knowledge buckets. | `docs/PRD.md` / FR-049; `docs/SPEC.md` / Section 3.1 |
> | Memory contract validator | Accept `MEMORY.md` as canonical when present and reject `_MEMORY.md` in this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 |
> | Semantic placeholder validator | Recognize `_SEMANTIC.md` as part of the PREPARATION baseline and `_SEMANTIC_LENSING.md` as optional semantic analysis narrative. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 |
> | Test coverage | Metadata scanner, document-kit detection, and `_MEMORY.md` rejection coverage lives in `frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`; project-deliverables route integration is covered by `frontend/src/__tests__/api/project/deliverables-route.test.ts`. | `_CONTEXT.md` / Anticipated Artifacts; decomposition / DEL-07-03 row |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use | Status |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Evidence, hidden-memory, root-separation posture | MATCH |
> | REF-002 | `docs/CONTRACT.md` | Governance invariants for root, write scope, human gates, conflict surfacing | MATCH |
> | REF-003 | `docs/SPEC.md` | Deliverable folder layout, lifecycle, context/dependency/reference/memory contracts | MATCH |
> | REF-004 | `docs/TYPES.md` | Deliverable and lifecycle vocabulary | MATCH |
> | REF-005 | `docs/PLAN.md` | Local source policy and PKG-07 roadmap context | MATCH |
> | REF-006 | `docs/PRD.md` | Filesystem requirements and deliverable folder layout | MATCH status in `_REFERENCES.md` — reconciled under D-APP-38 |
> | REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH; no deliverable-specific requirements used |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> #### Specification: DEL-07-03 Deliverable Metadata and Document Kit Contracts
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable covers backend support for scanning and validating deliverable-local filesystem contracts in PKG-07. The covered contracts are deliverable metadata files, canonical memory, semantic placeholders, and four-document kit buckets. Sources: `_CONTEXT.md` / Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / DEL-07-03 row.
>
> In scope:
>
> - Detect and validate deliverable metadata files against SPEC/PRD file inventory expectations.
> - Detect the four-document kit as first-class knowledge buckets.
> - Validate canonical memory behavior by accepting `MEMORY.md` and rejecting `_MEMORY.md` for this project profile.
> - Recognize semantic baseline and optional semantic lens files.
> - Provide test coverage for metadata scanners, document kit detection, and `_MEMORY.md` rejection.
>
> Out of scope:
>
> - UI presentation except scope scan results, per package exclusion. Source: `_CONTEXT.md` / Package Scope.
> - Status transition enforcement beyond the file-contract checks in this deliverable; that is covered by DEL-07-04. Source: decomposition / PKG-07 rows.
> - Dependency register read/write/lint behavior beyond recognizing optional `Dependencies.csv`; that is covered by DEL-07-05. Source: decomposition / PKG-07 rows.
> - Human approval, checking, or issued-state authorization. Agents must not author binding approvals. Source: `docs/CONTRACT.md` / K-AUTH-1 and K-GATE-1.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-07-03-REQ-001 | The scanner shall identify deliverable folders by the valid `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` structure and the presence of `_STATUS.md`. | `docs/PRD.md` / FR-047; `docs/SPEC.md` / Section 3 | Unit tests with valid and invalid folder names and missing `_STATUS.md` fixtures |
> | DEL-07-03-REQ-002 | The validator shall require `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` as canonical metadata files for deliverable folders. | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 | Metadata scanner tests for complete and incomplete metadata sets |
> | DEL-07-03-REQ-003 | The validator shall recognize `_SEMANTIC.md` as part of the minimum PREPARATION fileset. | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 | Fixture with missing `_SEMANTIC.md` reports the expected baseline warning or failure state; exact severity TBD |
> | DEL-07-03-REQ-004 | The validator shall detect the document kit files `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` as first-class knowledge buckets. | `docs/PRD.md` / FR-049 and Section 10.8; `docs/SPEC.md` / Section 3.1 | Document kit detection tests for all-present, partially-present, and absent kit states |
> | DEL-07-03-REQ-005 | The validator shall treat `MEMORY.md` as the canonical deliverable-local working memory file when present. | `docs/SPEC.md` / Section 5.4; `docs/PRD.md` / Section 10.8 | Fixture asserting `MEMORY.md` is accepted as canonical memory |
> | DEL-07-03-REQ-006 | The validator shall reject `_MEMORY.md` in this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 | `_MEMORY.md` rejection tests |
> | DEL-07-03-REQ-007 | The validator shall recognize `_SEMANTIC_LENSING.md` and `HASH_VERIFICATION_BYPASS.jsonl` as optional deliverable-local files, not required PREPARATION files. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Fixture showing optional files do not make a valid folder invalid when absent |
> | DEL-07-03-REQ-008 | The implementation shall preserve working-root containment and must not mutate the instruction root during ordinary project execution. | `docs/DIRECTIVE.md` / Section 2.7; `docs/CONTRACT.md` / K-ROOT-1 through K-ROOT-3; `docs/PRD.md` / FR-050 and FR-051 | Path containment tests; instruction-root protection fixtures where this scanner accepts paths |
> | DEL-07-03-REQ-009 | Validation output shall surface source/hash warnings and unsupported or unknown conditions instead of silently treating them as accepted truth. | `docs/DIRECTIVE.md` / Section 2.5; `docs/CONTRACT.md` / K-CONFLICT-1; `_REFERENCES.md` / REF-006 | Fixture or unit test for reference warning reporting; exact output schema TBD |
> | DEL-07-03-REQ-010 | ASSUMPTION: Scanner outputs should be consumable by `/api/working-root/scope` or adjacent working-root/project APIs without changing their public route shapes. | `docs/SPEC.md` / Section 17.2; `docs/PLAN.md` / current baseline; decomposition / DEL-07-03 anticipated artifacts | Integration test TBD after implementation location is selected |
>

### CLM-010 — Scanner Finding Contract (P3)

> ##### Scanner Finding Contract (P3)
>
> This section records the Pass 3 contract shape needed for later implementation without selecting concrete files, public route changes, or final enum names. It responds to B-001, F-001, F-002, X-001, X-002, E-001, and E-002 from the current `_SEMANTIC_LENSING.md` worklist.
>

### CLM-011 — Finding Categories

> ###### Finding Categories
>
> | Category | Applies to | Source basis | Severity posture |
> |---|---|---|---|
> | Required metadata | Missing `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, or `_REFERENCES.md` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Must be reported as invalid or blocking; exact enum name TBD |
> | Preparation baseline | Missing `_SEMANTIC.md` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Must be reported as a baseline issue; exact severity TBD |
> | Lifecycle-conditioned document kit | Missing `Datasheet.md`, `Specification.md`, `Guidance.md`, or `Procedure.md` | `docs/SPEC.md` / Section 3.1 and Section 4.2; `docs/PRD.md` / FR-049 | Warning or failure depends on lifecycle state; exact state-to-severity map TBD |
> | Canonical memory | Present or missing `MEMORY.md` | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 | Should be visible in output; exact requiredness TBD |
> | Prohibited memory | Present `_MEMORY.md` | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 | Must be reported as prohibited for this profile |
> | Optional files | Present or absent `Dependencies.csv`, `_SEMANTIC_LENSING.md`, or `HASH_VERIFICATION_BYPASS.jsonl` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Absence must not invalidate a folder solely by itself |
> | Source/hash warning | Reference hash status: MATCH, bypass record, or unsupported source state | `_REFERENCES.md` / REF-006; `docs/CONTRACT.md` / K-CONFLICT-1 | Must remain visible as warning evidence — reconciled under D-APP-38 |
> | Unknown unsupported condition | File or state condition not covered by the accepted contract | `docs/CONTRACT.md` / K-INVENT-1 and K-CONFLICT-1 | Must surface as unknown/TBD, not silently accepted |
>

### CLM-012 — Minimum Result Fields

> ###### Minimum Result Fields
>
> Until an implementation-specific schema is accepted, scanner findings should preserve at least: `deliverableId`, `path`, `category`, `condition`, `lifecycleState`, `severity`, `sourceRef`, `evidence`, and `message`. The exact TypeScript type, API response shape, and persisted test fixture names remain TBD. If the scanner output is exposed through `/api/working-root/scope` or `/api/project/deliverables`, route shape compatibility must be proven by implementation tests rather than assumed from this document.
>

### CLM-013 — Standards

> ##### Standards
>
> | Standard or governing source | Applicability | Location |
> |---|---|---|
> | `docs/SPEC.md` | Primary physical file-layout, lifecycle, and deliverable-local contract source | Sections 3, 4, 5, 17.2 |
> | `docs/PRD.md` | Product requirements for filesystem execution and deliverable folder layout | Sections 8.8, 8.9, 10.8; MATCH status per `_REFERENCES.md` — reconciled under D-APP-38 |
> | `docs/TYPES.md` | Vocabulary for deliverables, artifacts, lifecycle states, and dependency classes | Sections 1.2, 1.3, lifecycle state table |
> | `docs/CONTRACT.md` | Governance invariants for roots, authority, hidden truth, and conflicts | K-AUTH, K-ROOT, K-CONFLICT |
> | `docs/DIRECTIVE.md` | Evidence posture, no hidden memory, root separation, provider-neutral governance | Sections 2.5, 2.6, 2.7 |
> | `docs/PLAN.md` | Roadmap and local source policy | Control-Plane Boundary; Local Source Policy; PKG-07 roadmap |
>

### CLM-014 — Verification

> ##### Verification
>
> | Verification item | Required evidence | Related requirements |
> |---|---|---|
> | Metadata scanner fixtures | Passing tests for required metadata files, missing metadata files, and valid/invalid deliverable folder identities | REQ-001, REQ-002 |
> | Semantic placeholder fixtures | Test or documented validator behavior for `_SEMANTIC.md` baseline and optional `_SEMANTIC_LENSING.md` | REQ-003, REQ-007 |
> | Document kit detection fixtures | Passing tests for complete, partial, and absent four-document kits | REQ-004 |
> | Memory contract fixtures | Passing test accepting `MEMORY.md` and rejecting `_MEMORY.md` | REQ-005, REQ-006 |
> | Path/root governance fixtures | Tests showing project-root containment and instruction-root write protection are preserved where this code handles paths | REQ-008 |
> | Warning propagation | Test or review evidence that reference hash warnings and unknowns remain visible | REQ-009 |
> | API compatibility | Integration or route-level evidence once implementation binding is selected | REQ-010 |
>

### CLM-015 — P3 Verification Additions

> ###### P3 Verification Additions
>
> | Verification target | Required evidence before closure | Disposition |
> |---|---|---|
> | B-001 normalized categories and severity names | Test fixture expectations must use one category/severity vocabulary for required, baseline, recommended, optional, prohibited, warning, and unknown findings. | Converted to explicit TBD contract above |
> | F-001 / E-001 scanner output schema | Accepted implementation type or schema and fixtures covering all finding categories. | Converted to minimum result fields; final schema TBD |
> | F-002 severity behavior | Fixtures for missing `_SEMANTIC.md`, initialized missing document-kit files, optional-file absence, `_MEMORY.md`, and source/hash warnings. | Converted to required verification evidence |
> | X-001 concrete tests | Passing test names, fixture paths, and command outputs from the implementation slice. | Deferred as closure evidence; exact paths/commands TBD |
> | X-002 warning propagation | Test or review evidence preserving REF-006 MATCH and unknown unsupported conditions. | Converted to required verification evidence — reconciled under D-APP-38 |
> | E-002 API consumer contract | Integration evidence for `/api/working-root/scope` or an accepted adjacent API, if scanner output is exposed there. | Reframed as assumption pending implementation proof |
>

### CLM-016 — Documentation

> ##### Documentation
>
> Required or expected artifacts for closure:
>
> - Metadata scanner implementation.
> - Document kit detection implementation.
> - `_MEMORY.md` rejection tests.
> - Test fixtures covering valid, incomplete, optional, and prohibited deliverable-local files.
> - Documentation or inline contract comments for scanner output severity (`TBD` until implementation schema is selected).
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-017 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-131 supersedes the integration-test TBD: additive `/api/project/deliverables` binding exists and is fixture-locked.

- **AC-001** — The scanner identifies valid deliverable folders, requires canonical metadata, recognizes the semantic baseline and four-document kit, accepts MEMORY.md, rejects _MEMORY.md, treats optional files as non-required, preserves working-root containment, and surfaces warnings and unknown conditions.

## Production and Verification Method — Praxeology

### CLM-018 — Procedure: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> #### Procedure: DEL-07-03 Deliverable Metadata and Document Kit Contracts
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-019 — Purpose

> ##### Purpose
>
> Define the working procedure for producing and verifying the DEL-07-03 backend feature slice: scanner/validator support for deliverable metadata files, canonical memory, semantic placeholders, and four-document kit buckets. Sources: `_CONTEXT.md` / Deliverable Scope; decomposition / DEL-07-03 row.
>

### CLM-020 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status or source |
> |---|---|
> | Accepted decomposition entry for DEL-07-03 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / DEL-07-03 row |
> | Governing file layout and lifecycle contract | `docs/SPEC.md` / Sections 3, 4, 5 |
> | Product requirements for filesystem execution model | `docs/PRD.md` / Sections 8.8, 8.9, 10.8; MATCH status in `_REFERENCES.md` — reconciled under D-APP-38 |
> | Vocabulary for deliverables, artifacts, and lifecycle states | `docs/TYPES.md` / Sections 1.2, 1.3, lifecycle state table |
> | Governance posture for roots, memory, evidence, and conflicts | `docs/DIRECTIVE.md` / Sections 2.5, 2.6, 2.7; `docs/CONTRACT.md` / K-ROOT, K-CONFLICT |
> | Declared upstream dependencies | TBD - no declared upstream dependency edges have been accepted by a human. Extracted ACTIVE rows exist in `_DEPENDENCIES.md` and `Dependencies.csv`, but they are not accepted declared dependencies for this prerequisite row. Source: `_DEPENDENCIES.md` / Declared Upstream and Extracted Dependency Register |
> | Implementation location | `frontend/src/lib/workspace/filesystem.ts` (`scanDeliverableDocumentKitContract`), consumed by the project-deliverables API scan. |
> | Scanner output schema | Minimum result fields are recorded in `Specification.md` / Scanner Finding Contract (P3); final implementation schema remains TBD. |
>

### CLM-021 — Steps

> ##### Steps
>
> 1. Confirm scope and source contracts.
>    - Read DEL-07-03 context, references, and decomposition row.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>
> 2. Define fixture cases.
>    - Include valid `OPEN` baseline, initialized four-doc kit, missing metadata file, missing recommended document kit file, prohibited `_MEMORY.md`, optional `_SEMANTIC_LENSING.md` absence, and optional `HASH_VERIFICATION_BYPASS.jsonl` presence.
>    - Source basis: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.
>
> 3. Implement or update deliverable folder detection.
>    - Detect `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` deliverable folders with `_STATUS.md`.
>    - Keep path handling within working-root containment.
>    - Source basis: `docs/PRD.md` / FR-047 and FR-050.
>
> 4. Implement metadata file validation.
>    - Require `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md`.
>    - Recognize `_SEMANTIC.md` as part of the minimum PREPARATION fileset.
>    - Distinguish required, recommended, optional, and prohibited files in output.
>    - Use the Pass 3 finding categories in `Specification.md` as the working vocabulary until an implementation schema is accepted.
>    - Source basis: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / FR-048 and Section 10.8.
>
> 5. Implement document kit detection.
>    - Detect `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` as document kit buckets.
>    - Tie missing-kit findings to lifecycle state where available: missing kit in `OPEN` differs from missing kit after `INITIALIZED`.
>    - Source basis: `docs/SPEC.md` / Section 3.1 and Section 4.2; `docs/PRD.md` / FR-049.
>
> 6. Implement memory contract checks.
>    - Accept `MEMORY.md` as canonical when present.
>    - Reject or flag `_MEMORY.md` as prohibited for this project profile.
>    - Source basis: `docs/SPEC.md` / Section 3.1 and Section 5.4.
>
> 7. Implement semantic placeholder checks.
>    - Recognize `_SEMANTIC.md` as baseline.
>    - Recognize `_SEMANTIC_LENSING.md` as optional.
>    - Source basis: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.
>
> 8. Preserve responsibility boundaries.
>    - Do not implement lifecycle transition authorization in this slice except as read/report behavior; DEL-07-04 owns transitions.
>    - Do not implement `Dependencies.csv` parser/writer behavior beyond optional-file recognition; DEL-07-05 owns dependency register behavior.
>    - Source basis: decomposition / PKG-07 deliverable rows.
>
> 9. Add tests and run verification.
>    - Add metadata scanner tests, document kit detection tests, and `_MEMORY.md` rejection tests.
>    - Add path/root containment fixtures if this code accepts filesystem paths.
>    - Include fixture coverage for missing `_SEMANTIC.md`, initialized folders missing one or more document-kit files, optional-file absence, optional-file presence, prohibited `_MEMORY.md`, REF-006 MATCH propagation, and unknown unsupported conditions. (reconciled under D-APP-38).
>    - Exact test command is TBD until implementation location is selected.
>

### CLM-022 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Required metadata files complete | Validator reports required metadata present |
> | Required metadata file missing | Validator reports missing canonical metadata file |
> | `_SEMANTIC.md` missing from PREPARATION baseline | Validator reports baseline semantic placeholder issue; severity TBD |
> | Four document kit complete | Validator detects all four knowledge buckets |
> | Four document kit partial | Validator reports missing bucket names |
> | `MEMORY.md` present | Validator accepts canonical memory file |
> | `_MEMORY.md` present | Validator rejects or flags prohibited file |
> | `_SEMANTIC_LENSING.md` absent | Validator does not fail solely for optional absence |
> | PRD hash status: MATCH present in references | Output/report preserves source warning — reconciled under D-APP-38 |
> | Instruction-root path supplied to write-capable path handling | Write operation is blocked or not available from this slice |
> | Extracted dependency rows present but declared sections remain TBD | Procedure treats extracted rows as evidence records, not accepted declared prerequisites |
> | Scanner result consumed by scope API or adjacent API | Compatibility is proven by implementation or route-level tests; no route-shape change is assumed here |
>

### CLM-023 — Records

> ##### Records
>
> Maintain the following records for closure:
>
> - Source references and hash warning notes used by implementation.
> - Scanner/validator implementation diff.
> - Fixture list and test results.
> - Any unresolved `TBD` values from this procedure, especially implementation location, scanner output schema, and severity policy.
> - Evidence that `_MEMORY.md` rejection was tested.
> - P3 disposition trace for A-001, B-001, C-001, D-001, D-002, F-001, F-002, X-001, X-002, E-001, and E-002.

- **VER-001** — Run the metadata-scanner and project-deliverables route fixtures identified by the source kit, then review path-containment, warning-propagation, and API-compatibility evidence against the source requirements.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> #### Guidance: DEL-07-03 Deliverable Metadata and Document Kit Contracts
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-025 — Purpose

> ##### Purpose
>
> DEL-07-03 exists to make deliverable-local filesystem contracts machine-readable and testable. It turns the SPEC/PRD deliverable folder contract into backend scanner and validator behavior for metadata files, document kit buckets, canonical memory, and semantic placeholders. Sources: `_CONTEXT.md` / Deliverable Scope; decomposition / DEL-07-03 row; `docs/PRD.md` / FR-047 through FR-049.
>

### CLM-026 — Principles

> ##### Principles
>
> 1. Preserve filesystem truth.
>    - The working root is the mutable project-truth location; instruction-root mutation is outside ordinary execution. Source: `docs/DIRECTIVE.md` / Section 2.7; `docs/CONTRACT.md` / K-ROOT-1 through K-ROOT-3.
>
> 2. Prefer explicit file contracts over inference.
>    - Required metadata files, document kit files, optional files, and prohibited `_MEMORY.md` are named in SPEC/PRD. Scanner behavior should reflect those named contracts before adding heuristics. Source: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.
>
> 3. Keep lifecycle meaning separate from file presence.
>    - `OPEN` means the minimum viable fileset exists; `INITIALIZED` means the document kit has been drafted or initialized. The scanner can report presence and state, but DEL-07-04 owns transition enforcement. Source: `docs/SPEC.md` / Section 4.2 and Section 4.3; decomposition / DEL-07-04 row.
>
> 4. Treat memory strictly.
>    - `MEMORY.md` is canonical deliverable-local working memory; `_MEMORY.md` is disabled in this project profile. A permissive fallback to `_MEMORY.md` would contradict the source contract. Source: `docs/SPEC.md` / Section 5.4; `docs/PRD.md` / Section 10.8.
>
> 5. Surface uncertainty.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-027 — Considerations

> ##### Considerations
>
> - Severity policy is partly source-defined and partly implementation-defined. Required metadata files are clearly required, document kit files are "SHOULD when initialized", and optional files are not required. Exact scanner severity levels are TBD until the implementation schema is selected. Sources: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - The deliverable should not absorb sibling package responsibilities. Status transition authorization belongs to DEL-07-04; dependency register parsing and writing belongs to DEL-07-05. Source: decomposition / PKG-07 rows.
> - If scanner results feed `/api/working-root/scope` or `/api/project/deliverables`, keep route shapes stable unless the implementation task explicitly includes API contract changes. Source: `docs/SPEC.md` / Section 17.2; `docs/PLAN.md` / Current Baseline.
> - ASSUMPTION: The scanner should return structured findings that distinguish missing required files, missing recommended files, optional-file absence, prohibited-file presence, and source/hash warnings. This follows the source contracts but the exact data model is TBD.
> - Pass 3 normalization keeps the distinction between source-backed categories and implementation-selected enum names. B-001 is addressed by using required metadata, preparation baseline, lifecycle-conditioned document kit, canonical memory, prohibited memory, optional files, source/hash warning, and unknown unsupported condition as the working vocabulary; final enum names remain TBD until implementation.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-028 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance | Source |
> |---|---|---|
> | Strict failure vs warning for missing document kit files | Treat missing document kit files as a condition tied to lifecycle state: expected when initialized, not necessarily invalid for `OPEN`. Exact severity TBD. | `docs/SPEC.md` / Section 3.1 and Section 4.2 |
> | Required vs optional semantic files | `_SEMANTIC.md` is part of the minimum PREPARATION fileset; `_SEMANTIC_LENSING.md` is optional. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 |
> | Memory compatibility vs project profile | Do not add compatibility support for `_MEMORY.md`; reject it for this profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4 |
> | Scanner ownership vs lifecycle ownership | Scanner may report state and file presence; lifecycle transition logic stays with the status API/tool slice. | `docs/SPEC.md` / Section 4.3; decomposition / DEL-07-04 |
> | Local requirements vs hash warning | Use local PRD content as requested source material but carry the MATCH status in output evidence. | `_REFERENCES.md` / REF-006 — reconciled under D-APP-38 |
>

### CLM-029 — P3 Disposition Guidance

> ##### P3 Disposition Guidance
>
> | Item | Guidance disposition |
> |---|---|
> | A-001 | Rejected for this P3 text pass as an implementation binding: implementation location and owning backend surface remain TBD until the implementation slice selects files. |
> | B-001 | Incorporated as normalized category vocabulary, with exact enum names and severity levels still TBD. |
> | C-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | D-001 | Converted to closure evidence requirements for implementation files, fixtures, and commands; exact paths remain TBD. |
> | D-002 | Reconciled as current-state language: extracted ACTIVE rows exist, while declared upstream/downstream dependency sections remain unaccepted/TBD. |
> | F-001 | Incorporated as minimum result-field guidance; final scanner schema remains TBD. |
> | F-002 | Converted to fixture/severity evidence requirements. |
> | X-001 | Converted to required implementation test evidence. |
> | X-002 | Converted to warning-propagation test evidence. |
> | E-001 | Incorporated with F-001 as the minimum scanner result model. |
> | E-002 | Reframed as an API compatibility assumption requiring implementation proof before closure. |
>

### CLM-030 — Examples

> ##### Examples
>
> | Scenario | Expected scanner/validator disposition | Source |
> |---|---|---|
> | Deliverable folder has `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md`, but no document kit, and status is `OPEN` | Valid PREPARATION baseline; document kit not yet initialized. | `docs/SPEC.md` / Section 3.1 and Section 4.2 |
> | Deliverable folder has status `INITIALIZED` but is missing `Specification.md` | Report missing document kit bucket. Exact severity TBD. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / FR-049 |
> | Deliverable folder contains `_MEMORY.md` | Reject or flag as prohibited for this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4 |
> | Deliverable folder lacks `_SEMANTIC_LENSING.md` | Do not fail solely for that absence; it is optional. | `docs/SPEC.md` / Section 3.1 |
>

### CLM-031 — Source Warning Notes

> ##### Source Warning Notes
>
> REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-026 OBJ-006 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
