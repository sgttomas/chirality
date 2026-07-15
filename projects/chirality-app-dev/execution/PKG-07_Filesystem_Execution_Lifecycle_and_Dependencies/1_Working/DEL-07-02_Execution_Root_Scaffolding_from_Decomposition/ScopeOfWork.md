---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-02
package_id: PKG-07
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@2770fda4c63c98ee9f18cffbafd14c9aa59f497f
project_scope_refs: [SOW-024, SOW-025]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-07-02

## Purpose and Objective Traceability

This candidate defines `DEL-07-02` in service of project scope [SOW-024, SOW-025] and package objectives [OBJ-006].

- **OUT-001** — A decomposition-driven execution-root scaffolder producing INIT.md, coordination, flat package and deliverable folders, minimum PREPARATION files, diagnostics, and idempotence evidence.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-02 Execution Root Scaffolding from Decomposition

> #### Datasheet: DEL-07-02 Execution Root Scaffolding from Decomposition
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-07-02 |
> | Deliverable Name | Execution Root Scaffolding from Decomposition |
> | Package ID | PKG-07 |
> | Package Name | Filesystem Execution, Lifecycle, and Dependencies |
> | Decomposition Variant | SOFTWARE_DECOMP |
> | Decomposition Revision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible Party | TBD |
> | Context Envelope | M |
> | Covers Scope Items | SOW-024, SOW-025 |
> | Supports Objectives | OBJ-006 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary function | Scaffold SPEC-conformant execution roots from decomposition markdown idempotently and recoverably. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-07 table |
> | Runtime surface | `/api/harness/scaffold` POST endpoint wraps execution-root scaffolding. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 7.3 |
> | Execution root contents | `INIT.md`, flat package folders, and tool roots including `_Aggregation`, `_Change`, `_Coordination`, `_Decomposition`, `_Estimates`, `_Reconciliation`, `_Archive`, `_Scripts`, and `_Sources`. | `docs/SPEC.md` Section 2; `docs/PRD.md` FR-045 |
> | Coordination artifact | `_Coordination/_COORDINATION.md` is part of the execution-root layout and scaffold output. | `docs/SPEC.md` Section 2.2; `docs/PRD.md` Section 7.3 |
> | Package layout | Flat `PKG-XX_Label` or `PKG-XXX_Label` folders; no nested package layer. | `docs/SPEC.md` Section 2.1; `docs/PRD.md` FR-046; `docs/CONTRACT.md` K-HIER-1 |
> | Deliverable layout | Deliverable folders are under `{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/`. | `docs/SPEC.md` Section 3 |
> | Minimum deliverable fileset | `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md` placeholder. | `docs/SPEC.md` Section 3.1 |
> | Document kit files | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` FR-049 |
> | Metadata compatibility target | PREPARATION compatibility is reported before the user proceeds. | `docs/PRD.md` Section 7.3 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Working-root basis | Project truth lives in plain files under the working root and accepted git history. | `docs/DIRECTIVE.md` Sections 1 and 2.1; `docs/CONTRACT.md` K-FS-1 |
> | Root separation | Instruction root and working root are separate; ordinary project execution must not mutate the instruction root. | `docs/DIRECTIVE.md` Section 2.7; `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3 |
> | Idempotence | Existing directories/files are preserved on rerun. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
> | Recovery diagnostics | Failures are fail-fast and include stage, target path, and created paths for recovery. | `docs/PRD.md` Section 7.3 |
> | Lifecycle state file | `_STATUS.md` is the canonical lifecycle file. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 |
> | Source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; task brief — reconciled under D-APP-38 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected Construction | Source |
> |---|---|---|
> | Scaffold parser | Parse decomposition markdown sufficiently to identify package rows and deliverable rows for v3.2 SOFTWARE_DECOMP. Exact parser implementation details are TBD. | `_CONTEXT.md` Anticipated Artifacts; `docs/PRD.md` Section 7.3 |
> | Root initializer | Create or validate `INIT.md` at execution root. Content schema is TBD from available sources. | `docs/SPEC.md` Section 2; `docs/PRD.md` FR-045 |
> | Coordination initializer | Create or validate `_Coordination/_COORDINATION.md`. Coordination mode values should align to TYPES vocabulary where applicable. | `docs/SPEC.md` Section 2.2; `docs/TYPES.md` Section 13 |
> | Package scaffolder | Create flat package folders using `{PKG-ID}_{Sanitize(PackageName)}/` and required/expected subfolders. | `docs/SPEC.md` Section 2.1 |
> | Deliverable scaffolder | Create deliverable folders under `1_Working/` and seed minimum PREPARATION fileset. | `docs/SPEC.md` Section 3.1 |
> | Validation summary | Return validation summaries, PREPARATION compatibility, issue counts, scaffold counts, created path inventory, and fail-fast recovery diagnostics including stage and target path. | `docs/PRD.md` Section 7.3; `docs/SPEC.md` Section 17.1 |
> | Idempotence tests | Tests should prove reruns preserve existing directories, file contents, and file metadata where applicable, and report compatibility without duplicating or corrupting files. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
>

### CLM-006 — References

> ##### References
>
> - `docs/DIRECTIVE.md` Sections 1, 2.1, and 2.7.
> - `docs/CONTRACT.md` K-HIER-1, K-FS-1, K-ROOT-1 through K-ROOT-3, K-STATUS-1, K-INVENT-1, K-CONFLICT-1.
> - `docs/SPEC.md` Sections 2, 3, 4, 5, and 17.1.
> - `docs/TYPES.md` Sections 8.4 and 13.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-07-02 and SOW-024/SOW-025 rows.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-07-02 Execution Root Scaffolding from Decomposition

> #### Specification: DEL-07-02 Execution Root Scaffolding from Decomposition
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies the backend feature slice that scaffolds a SPEC-conformant execution root from accepted decomposition markdown for Chirality App vNext. The slice covers SOW-024 execution-root scaffolding and SOW-025 flat package/deliverable folder layout for PKG-07.
>
> In scope:
>
> - Parse the active decomposition markdown enough to derive packages and deliverables.
> - Create or validate `INIT.md`, tool roots, `_Coordination/_COORDINATION.md`, package folders, deliverable folders, and the minimum PREPARATION fileset.
> - Preserve flat package topology and deliverable folder naming.
> - Return diagnostics that support idempotent reruns and recovery after fail-fast errors.
> - Support the `/api/harness/scaffold` runtime route or its backend service layer.
>
> Out of scope:
>
> - UI presentation beyond the scaffold API result surface.
> - Lifecycle transition enforcement beyond seeding the scaffold baseline; status transition APIs belong to DEL-07-04.
> - `Dependencies.csv` parser/writer behavior beyond creating or leaving dependency placeholders; dependency register behavior belongs to DEL-07-05.
> - Human assignment of `ResponsibleParty`, which remains `TBD` until assigned.
>
> Sources: `_CONTEXT.md`; `docs/SPEC.md` Sections 2 and 3; `docs/PRD.md` Sections 7.3 and 8.8; decomposition DEL-07-02 row.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification | Source |
> |---|---|---|---|
> | DEL-07-02-REQ-001 | The scaffold operation MUST create or validate an execution root containing `INIT.md`, package folders, and the SPEC-listed tool roots. | Unit/API test checks resulting tree and layout validation payload. | `docs/SPEC.md` Section 2; `docs/PRD.md` FR-045 |
> | DEL-07-02-REQ-002 | Package folders MUST be flat and named `{PKG-ID}_{Sanitize(PackageName)}/`; the scaffold operation MUST NOT introduce nested packages. | Fixture decomposition with multiple packages; resulting tree contains only flat package folders. | `docs/SPEC.md` Section 2.1; `docs/CONTRACT.md` K-HIER-1; `docs/PRD.md` FR-046 |
> | DEL-07-02-REQ-003 | Each deliverable folder MUST be created under `{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/`. | Fixture decomposition with deliverable rows; path assertions. | `docs/SPEC.md` Section 3; `docs/PRD.md` FR-047 |
> | DEL-07-02-REQ-004 | Each newly scaffolded deliverable folder MUST include the minimum PREPARATION fileset: `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md`. | Fixture result verifies required files exist for every deliverable. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` FR-048 |
> | DEL-07-02-REQ-005 | New deliverable `_STATUS.md` files MUST represent the `OPEN` scaffold state and remain canonical lifecycle inputs for later status workflows. | Status parser test reads `Current State: OPEN` from scaffold output. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 |
> | DEL-07-02-REQ-006 | The scaffold operation MUST create or validate `_Coordination/_COORDINATION.md` under the execution root. | Tree assertion and coordination-file existence check. | `docs/SPEC.md` Section 2; `docs/PRD.md` Section 7.3 |
> | DEL-07-02-REQ-007 | The scaffold operation MUST be idempotent for existing directories and files; reruns preserve existing paths and existing file contents unless a separately authorized workflow owns migration or repair. | Rerun test against a previously scaffolded root verifies no duplicate path creation, no destructive rewrite, and unchanged pre-existing file content hashes or byte comparisons. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
> | DEL-07-02-REQ-008 | Failures MUST fail fast and return diagnostics including stage, target path, and created paths sufficient for recovery. | Conflict-path test asserts typed failure payload. | `docs/PRD.md` Section 7.3 |
> | DEL-07-02-REQ-009 | The scaffold route MUST expose the operation through `POST /api/harness/scaffold`. | API route test posts request and verifies response. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 17.1 |
> | DEL-07-02-REQ-010 | The scaffold operation SHOULD report PREPARATION compatibility before downstream TASK work proceeds. | Response payload contains compatibility readiness and issue count. | `docs/PRD.md` Section 7.3 |
> | DEL-07-02-REQ-011 | Runtime tools involved in scaffolding MUST enforce working-root containment and must not mutate the instruction root during ordinary project execution. | Path-policy and write-denial tests. | `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3; `docs/PRD.md` NFR-005 and NFR-006 |
> | DEL-07-02-REQ-012 | Unknown decomposition-derived values or unsupported parser details MUST be preserved as `TBD` or reported diagnostics rather than guessed. | Fixture with missing values verifies explicit `TBD` or typed issue. | `docs/CONTRACT.md` K-INVENT-1 |
> | DEL-07-02-REQ-013 | The parser support boundary MUST be explicit: the first supported input is the accepted v3.2 SOFTWARE_DECOMP package and deliverable table shape, with unsupported or ambiguous markdown shapes reported as compatibility issues instead of silently accepted. | Parser fixture tests include the accepted v3.2 table shape, missing-value rows, and unsupported table-shape diagnostics. | `_CONTEXT.md`; decomposition DEL-07-02 row; `docs/PRD.md` Section 7.3; `docs/CONTRACT.md` K-INVENT-1 |
>

### CLM-010 — Scaffold API Result Contract

> ##### Scaffold API Result Contract
>
> The `POST /api/harness/scaffold` response shape remains an implementation contract to finalize, but tests should expect these source-backed semantic fields:
>
> | Field Group | Expected Semantics | Status / Source |
> |---|---|---|
> | Request echo | Execution root or working root target and decomposition path used for the scaffold operation. | Source-backed by `docs/PRD.md` Section 7.3 and `docs/SPEC.md` Section 17.1; exact field names TBD. |
> | Scaffold counts | Package count and deliverable count parsed from supported decomposition rows. | Source-backed by `docs/PRD.md` Section 7.3; exact field names TBD. |
> | Created/existing inventory | Created path inventory plus already-existing path/file indicators sufficient to verify idempotence. | Source-backed by `docs/PRD.md` Section 7.3 and NFR-011; exact field names TBD. |
> | Validation summaries | Layout validation and PREPARATION compatibility readiness, including issue count. | Source-backed by `docs/PRD.md` Section 7.3; exact field names TBD. |
> | Failure diagnostics | Fail-fast stage, target path, and created path inventory. | Source-backed by `docs/PRD.md` Section 7.3; exact field names TBD. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Execution Root Layout | Governs root folders, package folders, tool roots, and deliverable paths. | `docs/SPEC.md` Sections 2 and 3 |
> | Lifecycle File Contract | Governs `_STATUS.md` scaffold state and later lifecycle transition compatibility. | `docs/SPEC.md` Section 4 |
> | Filesystem Execution Model | Product requirements for scaffold layout, package/deliverable structures, metadata files, document kits, and path policy. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | Reliability Requirement NFR-011 | Idempotent and recoverable scaffolding. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | Invariant Catalog | Governs flat hierarchy, project truth, root separation, lifecycle canonicality, no invention, and conflict surfacing. | `docs/CONTRACT.md` K-HIER-1, K-FS-1, K-ROOT-1 through K-ROOT-3, K-STATUS-1, K-INVENT-1, K-CONFLICT-1 |
> | TYPES Vocabulary | Governs initial Chirality MCP tool names and coordination representation terms where the scaffold API exposes or records those concepts. | `docs/TYPES.md` Sections 8.4 and 13 |
>

### CLM-012 — Verification

> ##### Verification
>
> Required verification set:
>
> 1. Scaffold route API test for `POST /api/harness/scaffold`.
> 2. Unit test for parsing decomposition package and deliverable tables.
> 3. Layout test for SPEC Section 2 execution-root tree.
> 4. Package-layout test proving flat package folders and required/expected subfolders.
> 5. Deliverable-layout test proving `1_Working/{DEL-ID}_{DelLabel}/` placement and minimum PREPARATION fileset.
> 6. Idempotence test proving rerun preservation for existing directories and files.
> 7. Fail-fast conflict test proving stage, target path, and created path inventory are reported.
> 8. Path-policy test proving writes remain under the active working root and do not target the instruction root.
> 9. PREPARATION compatibility test proving result summaries identify blockers before downstream TASK execution.
> 10. Parser-boundary test proving unsupported decomposition table shapes produce compatibility issues rather than guessed package or deliverable records.
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required or expected artifacts:
>
> - Scaffold parser.
> - `INIT.md` creation/validation behavior.
> - `_Coordination/_COORDINATION.md` creation/validation behavior.
> - Package and deliverable folder creation behavior.
> - Idempotence tests.
> - Fail-fast recovery diagnostics.
> - API contract notes for `/api/harness/scaffold`.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-014 — Assumptions and TBDs

> ##### Assumptions and TBDs
>
> | Item | Status |
> |---|---|
> | Exact `INIT.md` content schema | TBD; sources identify required presence but not a complete content template. |
> | Exact `_COORDINATION.md` content schema for scaffold output | TBD; sources identify required presence and coordination vocabulary, but not a complete content template. |
> | Exact decomposition parser grammar | TBD; deliverable scope identifies decomposition markdown parsing, but implementation grammar is not specified in authoritative sources. |
> | C-001 parser grammar disposition | Converted to explicit support-boundary requirement and fixture expectation; complete grammar remains TBD pending implementation evidence. |
> | F-001 INIT schema disposition | Already covered as a named TBD; sources require `INIT.md` presence but do not provide a complete content schema. |
> | F-002 coordination schema disposition | Already covered as a named TBD; sources require `_Coordination/_COORDINATION.md` presence and coordination vocabulary but do not provide a complete template. |
> | F-003 idempotence disposition | Incorporated by requiring rerun tests to preserve existing file contents, not only paths. |
> | E-001 scaffold API response disposition | Incorporated as a semantic response-field contract with exact field names left TBD. |
> | Existing code surface | ASSUMPTION: existing frontend scaffold service and tests may be reusable, but code files are not listed as authoritative references for this deliverable kit. |

- **AC-001** — The accepted v3.2 decomposition shape produces the SPEC-conformant flat execution tree and PREPARATION fileset, preserves existing content on rerun, reports unsupported shapes and failures without guessing, and confines writes to the working root.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-07-02 Execution Root Scaffolding from Decomposition

> #### Procedure: DEL-07-02 Execution Root Scaffolding from Decomposition
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-016 — Purpose

> ##### Purpose
>
> Define the operational workflow for implementing and verifying execution-root scaffolding from decomposition markdown for DEL-07-02. The procedure describes how to produce the backend feature slice and how the scaffold operation should behave when invoked.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Source |
> |---|---|
> | Accepted decomposition markdown path is available. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; decomposition downstream execution notes |
> | Working root has been selected and validated. | `docs/PRD.md` Section 7.3; `docs/SPEC.md` Section 1/2 context |
> | Instruction root and working root are distinct. | `docs/DIRECTIVE.md` Section 2.7; `docs/CONTRACT.md` K-ROOT-1 |
> | Scaffold operation target is under the active working root. | `docs/CONTRACT.md` K-ROOT-3 and K-PATH-2 |
> | Required source contracts are available. | `_REFERENCES.md` REF-001 through REF-007; REF-006 warning noted |
> | Declared upstream dependencies for this deliverable. | TBD; `_DEPENDENCIES.md` declares no accepted upstream edges yet. X-001 disposition: keep this as an explicit readiness blocker until accepted upstream edges or a human ruling are available. |
>

### CLM-018 — Steps

> ##### Steps
>
> 1. Confirm the active decomposition reference.
>    - Verify the operator-provided decomposition path resolves to the accepted v3.2 SOFTWARE_DECOMP working surface.
>    - Preserve decomposition-derived IDs and names in scaffold output.
>    - Source: decomposition downstream execution notes; `docs/CONTRACT.md` K-ID-1.
>
> 2. Validate the target working root.
>    - Confirm the root is absolute, accessible, and not inside the instruction root.
>    - Reject scaffold writes outside the active working root.
>    - Source: `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3; `docs/PRD.md` NFR-005 and NFR-006.
>
> 3. Parse decomposition package and deliverable rows.
>    - Extract package ID, package name, deliverable ID, deliverable name, type, description, anticipated artifacts, scope items, objectives, and context envelope where present.
>    - If a required value is missing, emit `TBD` or a typed compatibility issue rather than inventing it.
>    - Treat the accepted v3.2 SOFTWARE_DECOMP package and deliverable table shape as the initial supported parser fixture boundary; unsupported markdown shapes should produce compatibility issues.
>    - Source: decomposition DEL-07-02 row; `docs/CONTRACT.md` K-INVENT-1.
>
> 4. Create or validate execution-root tool roots.
>    - Ensure `INIT.md` and the SPEC-listed tool roots exist or are validated.
>    - Ensure `_Coordination/_COORDINATION.md` exists or is validated.
>    - Source: `docs/SPEC.md` Section 2; `docs/PRD.md` Section 7.3.
>
> 5. Create or validate package folders.
>    - Use `{PKG-ID}_{Sanitize(PackageName)}/`.
>    - Create or validate required/expected package subfolders, especially `1_Working/`.
>    - Do not create nested package layers.
>    - Source: `docs/SPEC.md` Section 2.1; `docs/CONTRACT.md` K-HIER-1.
>
> 6. Create or validate deliverable folders.
>    - Place deliverables under `{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/`.
>    - Seed the minimum PREPARATION fileset for new deliverables.
>    - Preserve existing directories and files on rerun.
>    - Source: `docs/SPEC.md` Section 3.1; `docs/PRD.md` Section 7.3.
>
> 7. Seed lifecycle state.
>    - New deliverable `_STATUS.md` files should represent `OPEN` scaffold state.
>    - Do not perform later lifecycle transitions as part of this scaffold slice.
>    - Source: `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1.
>
> 8. Return scaffold result diagnostics.
>    - Report execution root, decomposition path, package count, deliverable count, created directory/file inventory, already-existing path/file indicators, layout validation, PREPARATION compatibility, and issue count.
>    - On failure, report fail-fast stage, target path, and created path inventory.
>    - Source: `docs/PRD.md` Section 7.3.
>
> 9. Verify with tests.
>    - Run unit tests for parser, layout creation, idempotence, fail-fast conflict handling, and path policy.
>    - Run API route tests for `POST /api/harness/scaffold`.
>    - Source: `docs/PRD.md` FR-045 through FR-048, FR-064; NFR-011.
>

### CLM-019 — Verification

> ##### Verification
>
> | Check | Expected Result | Requirement Link |
> |---|---|---|
> | Execution-root layout | `INIT.md`, flat package folders, `_Coordination/_COORDINATION.md`, and tool roots exist. | DEL-07-02-REQ-001, DEL-07-02-REQ-006 |
> | Package flatness | Package folders are not nested and use `PKG-XX_Label` or `PKG-XXX_Label` structure. | DEL-07-02-REQ-002 |
> | Deliverable placement | Deliverables are under each package `1_Working/` folder with valid DEL prefixes. | DEL-07-02-REQ-003 |
> | Minimum fileset | New deliverables include `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md`. | DEL-07-02-REQ-004 |
> | Status baseline | New scaffolded deliverables start at `OPEN`. | DEL-07-02-REQ-005 |
> | Idempotence | Rerun preserves existing paths/files and reports already-existing content without destructive rewrite. | DEL-07-02-REQ-007 |
> | Fail-fast recovery | Filesystem conflicts return stage, target path, and created paths. | DEL-07-02-REQ-008 |
> | API route | `POST /api/harness/scaffold` invokes scaffold behavior and returns summary payload. | DEL-07-02-REQ-009 |
> | Path policy | Writes outside active working root and instruction-root writes are rejected. | DEL-07-02-REQ-011 |
> | Parser boundary | Accepted v3.2 SOFTWARE_DECOMP fixtures parse; unsupported table shapes return compatibility issues. | DEL-07-02-REQ-013 |
>

### CLM-020 — Records

> ##### Records
>
> Implementation should leave or update these records:
>
> - Source code for scaffold parser/service and route integration.
> - Unit and API test results for scaffold behavior.
> - Scaffold result payload examples or fixtures.
> - PREPARATION compatibility diagnostics.
> - Any human rulings for `INIT.md` or `_COORDINATION.md` content templates.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-021 — Open Items

> ##### Open Items
>
> | Item | Needed Ruling or Evidence |
> |---|---|
> | `INIT.md` exact content schema | Human or source-backed template needed. |
> | `_COORDINATION.md` exact scaffold template | Human or source-backed template needed. |
> | Parser grammar for decomposition markdown variants | Implementation decision and tests needed; current sources specify behavior but not full grammar. |
> | Scaffold API response field names | Implementation decision needed; current sources define response semantics for validation summaries, PREPARATION compatibility, issue counts, and fail-fast diagnostics but not exact field names. |

- **VER-001** — Run the source-defined decomposition parser, scaffold API, layout, PREPARATION, idempotence, fail-fast recovery, path-policy, and unsupported-shape tests and review the resulting tree and diagnostics.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-07-02 Execution Root Scaffolding from Decomposition

> #### Guidance: DEL-07-02 Execution Root Scaffolding from Decomposition
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-023 — Purpose

> ##### Purpose
>
> This deliverable exists to turn accepted SOFTWARE_DECOMP markdown into a filesystem execution root that downstream Chirality workflows can inspect, validate, and continue. Its value is not the folder creation alone; it is the preservation of project truth as explicit files under the working root with stable package and deliverable identity.
>
> Sources: `docs/DIRECTIVE.md` Sections 1 and 2.1; `docs/CONTRACT.md` K-FS-1 and K-ID-1; decomposition DEL-07-02 row.
>

### CLM-024 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Filesystem truth first | Treat created files and folders under the working root as the project substrate. Runtime state, chats, and SDK transcripts do not replace governed project files. | `docs/DIRECTIVE.md` Section 2.1; `docs/CONTRACT.md` K-FS-1 |
> | Stable identifiers over path labels | Preserve package IDs and deliverable IDs even if labels or paths later change. | `docs/CONTRACT.md` K-ID-1 and K-PATH-1 |
> | Flat hierarchy | Keep the project hierarchy as packages containing deliverables; do not add phases or nested packages inside the scaffold output. | `docs/CONTRACT.md` K-HIER-1; `docs/SPEC.md` Section 2.1 |
> | Root separation | Enforce working-root containment and avoid instruction-root mutation during scaffold operations. | `docs/DIRECTIVE.md` Section 2.7; `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3 |
> | Idempotent recovery | Preserve existing paths on rerun and make partial failure recovery explicit through created-path inventories and stage diagnostics. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
> | Lifecycle compatibility | Seed `_STATUS.md` as the canonical lifecycle file so later status APIs and human gates operate on a consistent contract. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 |
> | Unknowns stay visible | Missing values, parser uncertainties, or source gaps should produce `TBD`, diagnostics, or compatibility issues rather than invented project truth. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
>

### CLM-025 — Considerations

> ##### Considerations
>
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Scaffold output is a boundary between decomposition truth and execution working state. The scaffold service should copy or reference the accepted decomposition snapshot without treating generated folders as a replacement for the decomposition authority.
> - PREPARATION compatibility should be treated as an operator-facing readiness check, not as proof that downstream deliverables are complete.
> - The scaffold operation should avoid over-owning adjacent responsibilities. Metadata contract validation belongs primarily to DEL-07-03, lifecycle transition enforcement to DEL-07-04, and `Dependencies.csv` v3.1 behavior to DEL-07-05.
> - ASSUMPTION: Because DEL-07-02 is a backend feature slice with multiple file outputs, tests should emphasize fixture coverage and recovery diagnostics more than UI presentation.
>

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Topic | Trade-off | Recommended Direction |
> |---|---|---|
> | Strict failure vs. best-effort creation | Best-effort creation can leave ambiguous partial state; strict fail-fast behavior may require reruns. | Prefer fail-fast with created-path inventory, matching PRD acceptance. |
> | Preserve existing files vs. normalize on rerun | Rewriting existing files could repair drift but risks destroying human or agent work. | Preserve existing paths/files during scaffold rerun; report compatibility issues separately. |
> | Generated defaults vs. source fidelity | Rich defaults make folders look complete but can invent unsupported values. | Seed required files conservatively and use `TBD` where source data is missing. |
> | Route-owned behavior vs. service-owned behavior | Fat routes are easy to wire but hard to test and reuse. | Keep `/api/harness/scaffold` thin and place behavior in a reusable scaffold service, consistent with PRD route principles. |
> | Broad markdown parser vs. bounded fixture support | A broad parser may appear flexible but can silently reinterpret unsupported decomposition shapes. | Start with the accepted v3.2 SOFTWARE_DECOMP package/deliverable table shape, then report unsupported shapes as compatibility issues until additional grammars are source-backed. |
>

### CLM-027 — Examples

> ##### Examples
>

### CLM-028 — Expected root shape

> ###### Expected root shape
>
> ```text
> {EXECUTION_ROOT}/
> ├── INIT.md
> ├── PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/
> │   └── 1_Working/
> │       └── DEL-07-02_Execution_Root_Scaffolding_from_Decomposition/
> ├── _Coordination/
> │   └── _COORDINATION.md
> └── _Decomposition/
> ```
>
> Source: `docs/SPEC.md` Sections 2 and 3.
>

### CLM-029 — Expected rerun posture

> ###### Expected rerun posture
>
> On rerun, an existing package folder, deliverable folder, or metadata file should be preserved unless a separately authorized workflow owns migration or repair. The scaffold response should report what already existed, what was newly created, and what prevents PREPARATION compatibility.
>
> Source: `docs/PRD.md` Section 7.3 and NFR-011.
>
> P3 disposition: F-003 is incorporated here by making file-content preservation explicit, not only path preservation.
>

### CLM-030 — Dependency-readiness posture

> ###### Dependency-readiness posture
>
> Declared upstream dependencies remain unresolved for this deliverable. Treat `_DEPENDENCIES.md` as the current dependency evidence container and do not infer accepted upstream closure from extracted rows alone.
>
> Source: `_DEPENDENCIES.md` Declared Upstream and Extracted Dependency Register; `docs/CONTRACT.md` K-DEP-1.
>
> P3 disposition: X-001 is already covered in Procedure prerequisites and reinforced here as an explicit readiness posture.
>

### CLM-031 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | None | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | Task brief | All documents using PRD citations | Use PRD with explicit warning. | TBD — reconciled under D-APP-38 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-024 SOW-025 OBJ-006 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
