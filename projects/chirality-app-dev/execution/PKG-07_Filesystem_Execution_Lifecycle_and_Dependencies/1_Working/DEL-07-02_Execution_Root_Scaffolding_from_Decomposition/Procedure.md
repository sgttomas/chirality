# Procedure: DEL-07-02 Execution Root Scaffolding from Decomposition

## Purpose

Define the operational workflow for implementing and verifying execution-root scaffolding from decomposition markdown for DEL-07-02. The procedure describes how to produce the backend feature slice and how the scaffold operation should behave when invoked.

## Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Accepted decomposition markdown path is available. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; decomposition downstream execution notes |
| Working root has been selected and validated. | `docs/PRD.md` Section 7.3; `docs/SPEC.md` Section 1/2 context |
| Instruction root and working root are distinct. | `docs/DIRECTIVE.md` Section 2.7; `docs/CONTRACT.md` K-ROOT-1 |
| Scaffold operation target is under the active working root. | `docs/CONTRACT.md` K-ROOT-3 and K-PATH-2 |
| Required source contracts are available. | `_REFERENCES.md` REF-001 through REF-007; REF-006 warning noted |
| Declared upstream dependencies for this deliverable. | TBD; `_DEPENDENCIES.md` declares no accepted upstream edges yet. |

## Steps

1. Confirm the active decomposition reference.
   - Verify the operator-provided decomposition path resolves to the accepted v3.2 SOFTWARE_DECOMP working surface.
   - Preserve decomposition-derived IDs and names in scaffold output.
   - Source: decomposition downstream execution notes; `docs/CONTRACT.md` K-ID-1.

2. Validate the target working root.
   - Confirm the root is absolute, accessible, and not inside the instruction root.
   - Reject scaffold writes outside the active working root.
   - Source: `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3; `docs/PRD.md` NFR-005 and NFR-006.

3. Parse decomposition package and deliverable rows.
   - Extract package ID, package name, deliverable ID, deliverable name, type, description, anticipated artifacts, scope items, objectives, and context envelope where present.
   - If a required value is missing, emit `TBD` or a typed compatibility issue rather than inventing it.
   - Source: decomposition DEL-07-02 row; `docs/CONTRACT.md` K-INVENT-1.

4. Create or validate execution-root tool roots.
   - Ensure `INIT.md` and the SPEC-listed tool roots exist or are validated.
   - Ensure `_Coordination/_COORDINATION.md` exists or is validated.
   - Source: `docs/SPEC.md` Section 2; `docs/PRD.md` Section 7.3.

5. Create or validate package folders.
   - Use `{PKG-ID}_{Sanitize(PackageName)}/`.
   - Create or validate required/expected package subfolders, especially `1_Working/`.
   - Do not create nested package layers.
   - Source: `docs/SPEC.md` Section 2.1; `docs/CONTRACT.md` K-HIER-1.

6. Create or validate deliverable folders.
   - Place deliverables under `{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/`.
   - Seed the minimum PREPARATION fileset for new deliverables.
   - Preserve existing directories and files on rerun.
   - Source: `docs/SPEC.md` Section 3.1; `docs/PRD.md` Section 7.3.

7. Seed lifecycle state.
   - New deliverable `_STATUS.md` files should represent `OPEN` scaffold state.
   - Do not perform later lifecycle transitions as part of this scaffold slice.
   - Source: `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1.

8. Return scaffold result diagnostics.
   - Report execution root, decomposition path, package count, deliverable count, created directory/file inventory, layout validation, and PREPARATION compatibility.
   - On failure, report fail-fast stage, target path, and created path inventory.
   - Source: `docs/PRD.md` Section 7.3.

9. Verify with tests.
   - Run unit tests for parser, layout creation, idempotence, fail-fast conflict handling, and path policy.
   - Run API route tests for `POST /api/harness/scaffold`.
   - Source: `docs/PRD.md` FR-045 through FR-048, FR-064; NFR-011.

## Verification

| Check | Expected Result | Requirement Link |
|---|---|---|
| Execution-root layout | `INIT.md`, flat package folders, `_Coordination/_COORDINATION.md`, and tool roots exist. | DEL-07-02-REQ-001, DEL-07-02-REQ-006 |
| Package flatness | Package folders are not nested and use `PKG-XX_Label` or `PKG-XXX_Label` structure. | DEL-07-02-REQ-002 |
| Deliverable placement | Deliverables are under each package `1_Working/` folder with valid DEL prefixes. | DEL-07-02-REQ-003 |
| Minimum fileset | New deliverables include `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md`. | DEL-07-02-REQ-004 |
| Status baseline | New scaffolded deliverables start at `OPEN`. | DEL-07-02-REQ-005 |
| Idempotence | Rerun preserves existing paths/files and reports already-existing content without destructive rewrite. | DEL-07-02-REQ-007 |
| Fail-fast recovery | Filesystem conflicts return stage, target path, and created paths. | DEL-07-02-REQ-008 |
| API route | `POST /api/harness/scaffold` invokes scaffold behavior and returns summary payload. | DEL-07-02-REQ-009 |
| Path policy | Writes outside active working root and instruction-root writes are rejected. | DEL-07-02-REQ-011 |

## Records

Implementation should leave or update these records:

- Source code for scaffold parser/service and route integration.
- Unit and API test results for scaffold behavior.
- Scaffold result payload examples or fixtures.
- PREPARATION compatibility diagnostics.
- Any human rulings for `INIT.md` or `_COORDINATION.md` content templates.
- Warning record that `docs/PRD.md` was used despite `_REFERENCES.md` HASH_MISMATCH under explicit task instruction.

## Open Items

| Item | Needed Ruling or Evidence |
|---|---|
| `INIT.md` exact content schema | Human or source-backed template needed. |
| `_COORDINATION.md` exact scaffold template | Human or source-backed template needed. |
| Parser grammar for decomposition markdown variants | Implementation decision and tests needed; current sources specify behavior but not full grammar. |
