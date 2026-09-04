# Step 0 discovery — APPDEV_V3_NODE_O_2026-09-04

Recorded before evidence execution on 2026-09-04 by O1_IMPLEMENTER. Execution class is `delegated-harness-native`; Agent-2 role is `role not mechanically enforced`, governed-workflow role evidence is `instruction-asserted`, and K-SUBAGENT/non-delegation is instruction+config asserted rather than mechanism-proven. No descendant was observed.

## Basis and live state

| Observation | Result |
|---|---|
| Isolated branch | Clean `codex/app-v3-nodeO-section8-rev3-2026-09-04`; `HEAD` and `origin/main` both `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40` |
| Standing-plan loader | Bytewise-last committed plan is the unique mode-`100644` blob `loop/WORKPLAN_2026-09-03_app_dev_loop.md`, read with `git show HEAD:<path>` |
| Receipt structure | PASS/VALID; newest physical cursor Receipt 224 |
| Authority corpus | PASS; v20, no drift |
| Decision-register scan | No live `AWAITING_RULING` or `NOT_PREPARED` row that gates this revision |
| APP-HOLD dispatch | PASS/ALLOW for DEL-09-01; no active or scanned hold; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f` |
| Completion-reference pin | PASS; SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |
| Practitioner status | PASS/exit 0 under repository Python 3.13 |
| Harness self-check | PASS/exit 0 under repository Python 3.13; only known repo-wide non-blocking findings outside this tranche |
| Git status | Clean before run-control records were authored |

## Exact selectability determination

The live `DEL-09-01-V3-01` tag permits revision when a later merged v3 product change touches `frontend/electron/**` or another named trigger. Accepted revision 2 is based on `ede175910c67b384332324622b17695f69e6a715`. PR #695 merged Node N at `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40` and changed `frontend/electron/main.ts` plus `frontend/electron/renderer-window-policy.ts`, satisfying the trigger. It also changed five related frontend/test surfaces. PR #696 is the intervening first-parent merge `137e8a422cd7ecb2853dc12e9e58cc8561f26322`; its diff is confined to historical `projects/chirality-app-dev/plans/shell-redesign_2026-09-04/**`, so it is included in the actual basis but is not a trigger or work source. Revision 3 is therefore selectable, while final item removal remains gated on G5 fan-in.

## A1 re-stage declaration

The accepted runner writes ignored/generated paths under `projects/chirality-app-dev/frontend/`; therefore A1 applies even though this tranche authorizes no tracked frontend mutation. Historical staged R20 remains historical only. Any future reliance requires a newly staged revision and fresh owner-executed proof. This evidence run is not that owner proof and does not claim otherwise.

## Scope and boundaries

The existing runner and evaluator must remain byte-identical. Only revision-3 evidence additions, one deliverable-local run record, and the Node O coordination package are writable before review. No product/test/CSS/runtime/workflow, status, memory, receipt, plans, register, Root, SCOPE_CHANGE, Task Management, host act, G5/G6a, version, signing, notarization, publication, distribution, or release-readiness mutation or claim is permitted.
