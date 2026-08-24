# APP V3 Phase 0 — Orchestration Plan v1

**RunID:** `APP_V3_PHASE0_2026-08-23`
**Selection authority:** `HUMAN` — Ryan Tufts, 2026-08-23 App Session Init
**Posture:** `TERMINAL_FAN_OUT_IN`
**Basis:** `origin/main` and branch basis `3af765222bbd4f43a52dcbe17bd151c13942e5ac`
**Branch:** `codex/app-v3-phase0-2026-08-23`
**Frontend tree quarantine:** `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`

## Objective

Produce the assessment-only App Phase-0 basis directed by
`plans/steers/chirality_app_v3_phase0_steer_app_reissued_2026-08-23.md`:
SCA-APP-008 Gate-1 assessment and App DAG, Task Management owner-triage
packet, and preparation-lane baseline report. No acceptance, contract, code,
register, lifecycle, pointer, frontend, Root-loop, or release write is in
scope.

## Basis-gate result

`PASS` before project-content writes. The three steer instruments match their
owner-supplied SHA-256 values; required ancestry, plan, frontend tree, routed
D-GOV-35 notice, active SCA pointer, 13-row App Task Management register, and
Receipt 194 match the re-issued steer. Receipt validation, authority-corpus
status, practitioner status, repository self-check, and App register
validation passed on the basis.

## Nodes

| Node | Manager | Content write set | Control-plane write set | Dependencies | Required return |
| --- | --- | --- | --- | --- | --- |
| N1 | SCOPE_CHANGE | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/**` | `instances/N1-SCOPE-CHANGE-01/**` | No execution dependency; may cite accepted N3 report at fan-in | Gate-1 assessment, proposed amendments, App DAG, AUDIT_DEP_CLOSURE return, four-state handoff, fresh-review PASS |
| N2 | TASK_MANAGEMENT | `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/TRIAGE_PACKET_2026-08-23_V3_G0.md`; optional `HARVEST_2026-08-23_V3_G0.md` | `instances/N2-TASK-MANAGEMENT-01/**` | None | Federation preflight, trigger re-check, recommendation-only triage/harvest, register byte identity, fresh-review PASS |
| N3 | EVALUATION | `projects/chirality-app-dev/execution/_Evaluation/V3_PREP_BASELINE_2026-08-23/**` | `instances/N3-EVALUATION-01/**` | None | Path/line/blob-SHA evidence report, AT-ID mapping, reproducibility check, fresh-review PASS |

All node write sets are disjoint. Each node must stop on any scope expansion,
preserve claims as assessment or recommendation only, repair every review
finding inside its fixed write set, and obtain a fresh re-review after each
repair until PASS or a genuine blocker is returned.

## Fan-in and sequencing

Execution is concurrent. Validated commit order is N3, then N2, then N1.
Receipt 195 is appended once after those commits and is not owned by a node.
CHANGE owns scoped staging, commits, push, and PR creation. No merge is
authorized. If `origin/main` advances, work stops at a clean boundary for
owner sync authorization; no rebase or force-push.

## Human gates after this tranche

- SCA-APP-008 remains `AWAITING_OWNER_ACCEPTANCE`; `_LATEST.md` is untouched.
- Task Management recommendations/candidates remain for later owner disposition.
- G0.5 and all later release-pathway gates remain human acts.
- Signing, notarization, deployment, distribution, publication,
  release-readiness, issuance, and acceptance remain outside authority.
