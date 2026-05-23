# Specification: DEL-07-02 Execution Root Scaffolding from Decomposition

## Scope

This deliverable specifies the backend feature slice that scaffolds a SPEC-conformant execution root from accepted decomposition markdown for Chirality App vNext. The slice covers SOW-024 execution-root scaffolding and SOW-025 flat package/deliverable folder layout for PKG-07.

In scope:

- Parse the active decomposition markdown enough to derive packages and deliverables.
- Create or validate `INIT.md`, tool roots, `_Coordination/_COORDINATION.md`, package folders, deliverable folders, and the minimum PREPARATION fileset.
- Preserve flat package topology and deliverable folder naming.
- Return diagnostics that support idempotent reruns and recovery after fail-fast errors.
- Support the `/api/harness/scaffold` runtime route or its backend service layer.

Out of scope:

- UI presentation beyond the scaffold API result surface.
- Lifecycle transition enforcement beyond seeding the scaffold baseline; status transition APIs belong to DEL-07-04.
- `Dependencies.csv` parser/writer behavior beyond creating or leaving dependency placeholders; dependency register behavior belongs to DEL-07-05.
- Human assignment of `ResponsibleParty`, which remains `TBD` until assigned.

Sources: `_CONTEXT.md`; `docs/SPEC.md` Sections 2 and 3; `docs/PRD.md` Sections 7.3 and 8.8; decomposition DEL-07-02 row.

## Requirements

| ID | Requirement | Verification | Source |
|---|---|---|---|
| DEL-07-02-REQ-001 | The scaffold operation MUST create or validate an execution root containing `INIT.md`, package folders, and the SPEC-listed tool roots. | Unit/API test checks resulting tree and layout validation payload. | `docs/SPEC.md` Section 2; `docs/PRD.md` FR-045 |
| DEL-07-02-REQ-002 | Package folders MUST be flat and named `{PKG-ID}_{Sanitize(PackageName)}/`; the scaffold operation MUST NOT introduce nested packages. | Fixture decomposition with multiple packages; resulting tree contains only flat package folders. | `docs/SPEC.md` Section 2.1; `docs/CONTRACT.md` K-HIER-1; `docs/PRD.md` FR-046 |
| DEL-07-02-REQ-003 | Each deliverable folder MUST be created under `{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/`. | Fixture decomposition with deliverable rows; path assertions. | `docs/SPEC.md` Section 3; `docs/PRD.md` FR-047 |
| DEL-07-02-REQ-004 | Each newly scaffolded deliverable folder MUST include the minimum PREPARATION fileset: `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md`. | Fixture result verifies required files exist for every deliverable. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` FR-048 |
| DEL-07-02-REQ-005 | New deliverable `_STATUS.md` files MUST represent the `OPEN` scaffold state and remain canonical lifecycle inputs for later status workflows. | Status parser test reads `Current State: OPEN` from scaffold output. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 |
| DEL-07-02-REQ-006 | The scaffold operation MUST create or validate `_Coordination/_COORDINATION.md` under the execution root. | Tree assertion and coordination-file existence check. | `docs/SPEC.md` Section 2; `docs/PRD.md` Section 7.3 |
| DEL-07-02-REQ-007 | The scaffold operation MUST be idempotent for existing directories and files; reruns preserve existing paths and existing file contents unless a separately authorized workflow owns migration or repair. | Rerun test against a previously scaffolded root verifies no duplicate path creation, no destructive rewrite, and unchanged pre-existing file content hashes or byte comparisons. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
| DEL-07-02-REQ-008 | Failures MUST fail fast and return diagnostics including stage, target path, and created paths sufficient for recovery. | Conflict-path test asserts typed failure payload. | `docs/PRD.md` Section 7.3 |
| DEL-07-02-REQ-009 | The scaffold route MUST expose the operation through `POST /api/harness/scaffold`. | API route test posts request and verifies response. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 17.1 |
| DEL-07-02-REQ-010 | The scaffold operation SHOULD report PREPARATION compatibility before downstream TASK work proceeds. | Response payload contains compatibility readiness and issue count. | `docs/PRD.md` Section 7.3 |
| DEL-07-02-REQ-011 | Runtime tools involved in scaffolding MUST enforce working-root containment and must not mutate the instruction root during ordinary project execution. | Path-policy and write-denial tests. | `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3; `docs/PRD.md` NFR-005 and NFR-006 |
| DEL-07-02-REQ-012 | Unknown decomposition-derived values or unsupported parser details MUST be preserved as `TBD` or reported diagnostics rather than guessed. | Fixture with missing values verifies explicit `TBD` or typed issue. | `docs/CONTRACT.md` K-INVENT-1 |
| DEL-07-02-REQ-013 | The parser support boundary MUST be explicit: the first supported input is the accepted v3.2 SOFTWARE_DECOMP package and deliverable table shape, with unsupported or ambiguous markdown shapes reported as compatibility issues instead of silently accepted. | Parser fixture tests include the accepted v3.2 table shape, missing-value rows, and unsupported table-shape diagnostics. | `_CONTEXT.md`; decomposition DEL-07-02 row; `docs/PRD.md` Section 7.3; `docs/CONTRACT.md` K-INVENT-1 |

## Scaffold API Result Contract

The `POST /api/harness/scaffold` response shape remains an implementation contract to finalize, but tests should expect these source-backed semantic fields:

| Field Group | Expected Semantics | Status / Source |
|---|---|---|
| Request echo | Execution root or working root target and decomposition path used for the scaffold operation. | Source-backed by `docs/PRD.md` Section 7.3 and `docs/SPEC.md` Section 17.1; exact field names TBD. |
| Scaffold counts | Package count and deliverable count parsed from supported decomposition rows. | Source-backed by `docs/PRD.md` Section 7.3; exact field names TBD. |
| Created/existing inventory | Created path inventory plus already-existing path/file indicators sufficient to verify idempotence. | Source-backed by `docs/PRD.md` Section 7.3 and NFR-011; exact field names TBD. |
| Validation summaries | Layout validation and PREPARATION compatibility readiness, including issue count. | Source-backed by `docs/PRD.md` Section 7.3; exact field names TBD. |
| Failure diagnostics | Fail-fast stage, target path, and created path inventory. | Source-backed by `docs/PRD.md` Section 7.3; exact field names TBD. |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Execution Root Layout | Governs root folders, package folders, tool roots, and deliverable paths. | `docs/SPEC.md` Sections 2 and 3 |
| Lifecycle File Contract | Governs `_STATUS.md` scaffold state and later lifecycle transition compatibility. | `docs/SPEC.md` Section 4 |
| Filesystem Execution Model | Product requirements for scaffold layout, package/deliverable structures, metadata files, document kits, and path policy. | `docs/PRD.md` Section 8.8; source warning HASH_MISMATCH |
| Reliability Requirement NFR-011 | Idempotent and recoverable scaffolding. | `docs/PRD.md` Section 11.2; source warning HASH_MISMATCH |
| Invariant Catalog | Governs flat hierarchy, project truth, root separation, lifecycle canonicality, no invention, and conflict surfacing. | `docs/CONTRACT.md` K-HIER-1, K-FS-1, K-ROOT-1 through K-ROOT-3, K-STATUS-1, K-INVENT-1, K-CONFLICT-1 |
| TYPES Vocabulary | Governs initial Chirality MCP tool names and coordination representation terms where the scaffold API exposes or records those concepts. | `docs/TYPES.md` Sections 8.4 and 13 |

## Verification

Required verification set:

1. Scaffold route API test for `POST /api/harness/scaffold`.
2. Unit test for parsing decomposition package and deliverable tables.
3. Layout test for SPEC Section 2 execution-root tree.
4. Package-layout test proving flat package folders and required/expected subfolders.
5. Deliverable-layout test proving `1_Working/{DEL-ID}_{DelLabel}/` placement and minimum PREPARATION fileset.
6. Idempotence test proving rerun preservation for existing directories and files.
7. Fail-fast conflict test proving stage, target path, and created path inventory are reported.
8. Path-policy test proving writes remain under the active working root and do not target the instruction root.
9. PREPARATION compatibility test proving result summaries identify blockers before downstream TASK execution.
10. Parser-boundary test proving unsupported decomposition table shapes produce compatibility issues rather than guessed package or deliverable records.

## Documentation

Required or expected artifacts:

- Scaffold parser.
- `INIT.md` creation/validation behavior.
- `_Coordination/_COORDINATION.md` creation/validation behavior.
- Package and deliverable folder creation behavior.
- Idempotence tests.
- Fail-fast recovery diagnostics.
- API contract notes for `/api/harness/scaffold`.
- Source warning note that `docs/PRD.md` is being used despite `_REFERENCES.md` HASH_MISMATCH under the explicit task instruction.

## Assumptions and TBDs

| Item | Status |
|---|---|
| Exact `INIT.md` content schema | TBD; sources identify required presence but not a complete content template. |
| Exact `_COORDINATION.md` content schema for scaffold output | TBD; sources identify required presence and coordination vocabulary, but not a complete content template. |
| Exact decomposition parser grammar | TBD; deliverable scope identifies decomposition markdown parsing, but implementation grammar is not specified in authoritative sources. |
| C-001 parser grammar disposition | Converted to explicit support-boundary requirement and fixture expectation; complete grammar remains TBD pending implementation evidence. |
| F-001 INIT schema disposition | Already covered as a named TBD; sources require `INIT.md` presence but do not provide a complete content schema. |
| F-002 coordination schema disposition | Already covered as a named TBD; sources require `_Coordination/_COORDINATION.md` presence and coordination vocabulary but do not provide a complete template. |
| F-003 idempotence disposition | Incorporated by requiring rerun tests to preserve existing file contents, not only paths. |
| E-001 scaffold API response disposition | Incorporated as a semantic response-field contract with exact field names left TBD. |
| Existing code surface | ASSUMPTION: existing frontend scaffold service and tests may be reusable, but code files are not listed as authoritative references for this deliverable kit. |
