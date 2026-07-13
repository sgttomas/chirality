# D-GOV-16 Stage-2 Plan Snapshot Binding

Status: `STAGE2_PLAN_PRESENTED_AWAITING_ACCEPTANCE`

## Bound snapshot

- Branch: `codex/sow-stage2-plan`.
- Parent synchronized-main basis:
  `c9af689118e4e87f329e1ab4c6e71fea331b2674`.
- Immutable plan snapshot:
  `27f03730c956447b9a9696422cc9c63b8f061939`
  (`governance: present D-GOV-16 Stage-2 orchestration plan`).

## Sealed ORCHESTRATOR outputs

| Output | SHA-256 |
|---|---|
| `ORCHESTRATION_PLAN.md` | `20e3b3c4940f435fc32984a3ac3ce8d032f7939c1713efb9c3549fc694dee415` |
| `WORK_GRAPH.v1.md` | `a50329569eac50a6d27f7b22a007b01cf6bfbe4f10382a819ff567c5a5e9bac1` |
| `CENSUS_REFRESH.md` | `dc54e5124f372f7a6e1c7b6be0bbb05446d67fd07d0f3344c9376b4c280a0df7` |
| `CALLER_REFRESH.md` | `11d307b29a45cdf9a038489cacc04b263845bda964c626f67c9b7e3a3ceee9ae` |
| `D_GOV_16_TRACEABILITY.md` | `f312542edd27835061b57540608a1f3d124509bb2b2d58891650cae793e1ba31` |
| `HANDOFF_STATE.md` | `633765f95b099eea51556df7c64beeb07c1a5c640ca57de330aa19c5ba2a4a48` |

## Gate

The plan is presented for human acceptance, amendment, deferral, or rejection.
No Stage-2 node is dispatched by this binding. Any later accepted execution run
must rerun the synchronized-main basis, census, patch-applicability, and active
caller checks before dispatch.
