# Sealed Brief — TASK + dependency-extract — DEL-09-05

- Parent: `N4-SCOPE-CHANGE-01` / SCOPE_CHANGE.
- TaskSkill: `dependency-extract`.
- Basis: `cc196023a5532fe58955655c1144cd09ee88343a`; applied decomposition SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`.
- Scope: exactly `DEL-09-05_CI_Artifact_and_Release_Verification_Workflow`.
- Mode: `UPDATE`; strictness: `CONSERVATIVE`; consumer context: `RECONCILIATION`.
- Read: the scoped deliverable, its current v19 `_REFERENCES.md`, and the exact post-application decomposition.
- Write: only scoped `Dependencies.csv`, `_DEPENDENCIES.md`, a TASK run record under the scoped deliverable, plus `RETURN.md` and `STATUS.json` in this brief folder.
- Preserve: `_REFERENCES.md`, ScopeOfWork, status, context, memory, lifecycle, code, and every other deliverable.
- Method: execute both ANCHOR and EXECUTION passes; preserve declared rows and stable DependencyIDs; do not invent graph edges from SCC ordering alone.
- A2-B posture: E-032 (`DEL-09-05` feedback to `DEL-09-06`) remains non-gating under the accepted inversion. Preserve/surface it only where source evidence supports the existing information-flow edge; keep WP-09 authoring separate from WP-11 release execution and do not infer release authority.
- Acceptance: v3.1 schema passes; canonical enums; exact evidence; source documents unchanged; returned pre/post identities and row counts.
