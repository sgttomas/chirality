# Datasheet: DEL-07-02 Execution Root Scaffolding from Decomposition

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-07-02 |
| Deliverable Name | Execution Root Scaffolding from Decomposition |
| Package ID | PKG-07 |
| Package Name | Filesystem Execution, Lifecycle, and Dependencies |
| Decomposition Variant | SOFTWARE_DECOMP |
| Decomposition Revision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| Responsible Party | TBD |
| Context Envelope | M |
| Covers Scope Items | SOW-024, SOW-025 |
| Supports Objectives | OBJ-006 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary function | Scaffold SPEC-conformant execution roots from decomposition markdown idempotently and recoverably. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-07 table |
| Runtime surface | `/api/harness/scaffold` POST endpoint wraps execution-root scaffolding. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 7.3 |
| Execution root contents | `INIT.md`, flat package folders, and tool roots including `_Aggregation`, `_Change`, `_Coordination`, `_Decomposition`, `_Estimates`, `_Reconciliation`, `_Archive`, `_Scripts`, and `_Sources`. | `docs/SPEC.md` Section 2; `docs/PRD.md` FR-045 |
| Coordination artifact | `_Coordination/_COORDINATION.md` is part of the execution-root layout and scaffold output. | `docs/SPEC.md` Section 2.2; `docs/PRD.md` Section 7.3 |
| Package layout | Flat `PKG-XX_Label` or `PKG-XXX_Label` folders; no nested package layer. | `docs/SPEC.md` Section 2.1; `docs/PRD.md` FR-046; `docs/CONTRACT.md` K-HIER-1 |
| Deliverable layout | Deliverable folders are under `{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/`. | `docs/SPEC.md` Section 3 |
| Minimum deliverable fileset | `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md` placeholder. | `docs/SPEC.md` Section 3.1 |
| Document kit files | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` FR-049 |
| Metadata compatibility target | PREPARATION compatibility is reported before the user proceeds. | `docs/PRD.md` Section 7.3 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root basis | Project truth lives in plain files under the working root and accepted git history. | `docs/DIRECTIVE.md` Sections 1 and 2.1; `docs/CONTRACT.md` K-FS-1 |
| Root separation | Instruction root and working root are separate; ordinary project execution must not mutate the instruction root. | `docs/DIRECTIVE.md` Section 2.7; `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3 |
| Idempotence | Existing directories/files are preserved on rerun. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
| Recovery diagnostics | Failures are fail-fast and include stage, target path, and created paths for recovery. | `docs/PRD.md` Section 7.3 |
| Lifecycle state file | `_STATUS.md` is the canonical lifecycle file. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 |
| Source warning | `docs/PRD.md` is accessible but has a HASH_MISMATCH in `_REFERENCES.md`; use as a warning-bearing source per task brief. | `_REFERENCES.md` REF-006; task brief |

## Construction

| Component | Expected Construction | Source |
|---|---|---|
| Scaffold parser | Parse decomposition markdown sufficiently to identify package rows and deliverable rows for v3.2 SOFTWARE_DECOMP. Exact parser implementation details are TBD. | `_CONTEXT.md` Anticipated Artifacts; `docs/PRD.md` Section 7.3 |
| Root initializer | Create or validate `INIT.md` at execution root. Content schema is TBD from available sources. | `docs/SPEC.md` Section 2; `docs/PRD.md` FR-045 |
| Coordination initializer | Create or validate `_Coordination/_COORDINATION.md`. Coordination mode values should align to TYPES vocabulary where applicable. | `docs/SPEC.md` Section 2.2; `docs/TYPES.md` Section 13 |
| Package scaffolder | Create flat package folders using `{PKG-ID}_{Sanitize(PackageName)}/` and required/expected subfolders. | `docs/SPEC.md` Section 2.1 |
| Deliverable scaffolder | Create deliverable folders under `1_Working/` and seed minimum PREPARATION fileset. | `docs/SPEC.md` Section 3.1 |
| Validation summary | Return validation summaries, PREPARATION compatibility, issue counts, scaffold counts, created path inventory, and fail-fast recovery diagnostics including stage and target path. | `docs/PRD.md` Section 7.3; `docs/SPEC.md` Section 17.1 |
| Idempotence tests | Tests should prove reruns preserve existing directories, file contents, and file metadata where applicable, and report compatibility without duplicating or corrupting files. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |

## References

- `docs/DIRECTIVE.md` Sections 1, 2.1, and 2.7.
- `docs/CONTRACT.md` K-HIER-1, K-FS-1, K-ROOT-1 through K-ROOT-3, K-STATUS-1, K-INVENT-1, K-CONFLICT-1.
- `docs/SPEC.md` Sections 2, 3, 4, 5, and 17.1.
- `docs/TYPES.md` Sections 8.4 and 13.
- `docs/PRD.md` Sections 7.3, 8.8, 8.9, 11.2, and 17.1. Source warning: HASH_MISMATCH in `_REFERENCES.md`.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-07-02 and SOW-024/SOW-025 rows.
