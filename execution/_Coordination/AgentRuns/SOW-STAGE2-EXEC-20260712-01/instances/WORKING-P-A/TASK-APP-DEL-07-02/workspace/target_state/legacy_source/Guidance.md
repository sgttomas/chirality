# Guidance: DEL-07-02 Execution Root Scaffolding from Decomposition

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

This deliverable exists to turn accepted SOFTWARE_DECOMP markdown into a filesystem execution root that downstream Chirality workflows can inspect, validate, and continue. Its value is not the folder creation alone; it is the preservation of project truth as explicit files under the working root with stable package and deliverable identity.

Sources: `docs/DIRECTIVE.md` Sections 1 and 2.1; `docs/CONTRACT.md` K-FS-1 and K-ID-1; decomposition DEL-07-02 row.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Filesystem truth first | Treat created files and folders under the working root as the project substrate. Runtime state, chats, and SDK transcripts do not replace governed project files. | `docs/DIRECTIVE.md` Section 2.1; `docs/CONTRACT.md` K-FS-1 |
| Stable identifiers over path labels | Preserve package IDs and deliverable IDs even if labels or paths later change. | `docs/CONTRACT.md` K-ID-1 and K-PATH-1 |
| Flat hierarchy | Keep the project hierarchy as packages containing deliverables; do not add phases or nested packages inside the scaffold output. | `docs/CONTRACT.md` K-HIER-1; `docs/SPEC.md` Section 2.1 |
| Root separation | Enforce working-root containment and avoid instruction-root mutation during scaffold operations. | `docs/DIRECTIVE.md` Section 2.7; `docs/CONTRACT.md` K-ROOT-1 through K-ROOT-3 |
| Idempotent recovery | Preserve existing paths on rerun and make partial failure recovery explicit through created-path inventories and stage diagnostics. | `docs/PRD.md` Section 7.3; `docs/PRD.md` NFR-011 |
| Lifecycle compatibility | Seed `_STATUS.md` as the canonical lifecycle file so later status APIs and human gates operate on a consistent contract. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 |
| Unknowns stay visible | Missing values, parser uncertainties, or source gaps should produce `TBD`, diagnostics, or compatibility issues rather than invented project truth. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |

## Considerations

- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- Scaffold output is a boundary between decomposition truth and execution working state. The scaffold service should copy or reference the accepted decomposition snapshot without treating generated folders as a replacement for the decomposition authority.
- PREPARATION compatibility should be treated as an operator-facing readiness check, not as proof that downstream deliverables are complete.
- The scaffold operation should avoid over-owning adjacent responsibilities. Metadata contract validation belongs primarily to DEL-07-03, lifecycle transition enforcement to DEL-07-04, and `Dependencies.csv` v3.1 behavior to DEL-07-05.
- ASSUMPTION: Because DEL-07-02 is a backend feature slice with multiple file outputs, tests should emphasize fixture coverage and recovery diagnostics more than UI presentation.

## Trade-offs

| Topic | Trade-off | Recommended Direction |
|---|---|---|
| Strict failure vs. best-effort creation | Best-effort creation can leave ambiguous partial state; strict fail-fast behavior may require reruns. | Prefer fail-fast with created-path inventory, matching PRD acceptance. |
| Preserve existing files vs. normalize on rerun | Rewriting existing files could repair drift but risks destroying human or agent work. | Preserve existing paths/files during scaffold rerun; report compatibility issues separately. |
| Generated defaults vs. source fidelity | Rich defaults make folders look complete but can invent unsupported values. | Seed required files conservatively and use `TBD` where source data is missing. |
| Route-owned behavior vs. service-owned behavior | Fat routes are easy to wire but hard to test and reuse. | Keep `/api/harness/scaffold` thin and place behavior in a reusable scaffold service, consistent with PRD route principles. |
| Broad markdown parser vs. bounded fixture support | A broad parser may appear flexible but can silently reinterpret unsupported decomposition shapes. | Start with the accepted v3.2 SOFTWARE_DECOMP package/deliverable table shape, then report unsupported shapes as compatibility issues until additional grammars are source-backed. |

## Examples

### Expected root shape

```text
{EXECUTION_ROOT}/
├── INIT.md
├── PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/
│   └── 1_Working/
│       └── DEL-07-02_Execution_Root_Scaffolding_from_Decomposition/
├── _Coordination/
│   └── _COORDINATION.md
└── _Decomposition/
```

Source: `docs/SPEC.md` Sections 2 and 3.

### Expected rerun posture

On rerun, an existing package folder, deliverable folder, or metadata file should be preserved unless a separately authorized workflow owns migration or repair. The scaffold response should report what already existed, what was newly created, and what prevents PREPARATION compatibility.

Source: `docs/PRD.md` Section 7.3 and NFR-011.

P3 disposition: F-003 is incorporated here by making file-content preservation explicit, not only path preservation.

### Dependency-readiness posture

Declared upstream dependencies remain unresolved for this deliverable. Treat `_DEPENDENCIES.md` as the current dependency evidence container and do not infer accepted upstream closure from extracted rows alone.

Source: `_DEPENDENCIES.md` Declared Upstream and Extracted Dependency Register; `docs/CONTRACT.md` K-DEP-1.

P3 disposition: X-001 is already covered in Procedure prerequisites and reinforced here as an explicit readiness posture.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | Task brief | All documents using PRD citations | Use PRD with explicit warning. | TBD — reconciled under D-APP-38 |
