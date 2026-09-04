# RETURN — M1 — APPDEV_V3_NODE_M_2026-09-04

**Status:** `REVIEW_READY_R4 — round-1 through round-3 FAIL findings accepted and remediated; awaiting fresh round-4 review`

**Basis:** `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)

**Branch:** `codex/app-v3-nodeM-a15-owner-rulings-2026-09-04`

**Freeze:** the Git HEAD returned with this record; no self-referential commit SHA is embedded.

**Model and execution calibration:** provider OpenAI; engine Codex; model
GPT-5 family (exact model identifier not exposed to the agent runtime);
execution class `delegated-harness-native`. Ephemeral Agent-2 mode is `role
not mechanically enforced`; governed-workflow role evidence is
`instruction-asserted`. K-SUBAGENT/non-delegation is instruction+config
asserted, not mechanism-proven; no descendants were observed.

## Result

- Transcribed the owner's three 2026-09-04 answers into A15. The A15 file
  SHA-256 is
  `89633722ecefc3907c44e1c964353ed33c793f65ec1686afde3ae015d86f305c`.
- A15 selects a per-response CSP nonce with dynamic rendering for the four
  packaged routes `/`, `/chat`, `/pipeline`, and `/workbench`.
  DEL-09-06-V3-04 is annotated `SELECTABLE` once A15 lands. The outcome is
  authorized, not an exact implementation shape; hash/SRI is not selected.
  Its Return and Removed-when clauses are now nonce-only.
- A15 prospectively authorizes the owner-host Syft `v1.18.1` install and
  creation plus performance of the disposable self-signed A→B
  credential-transition drill. A14's dated deferrals remain historically
  valid and are lifted prospectively only.
- Neither host act was performed. DEL-09-05-V3-02 is
  `NOT_SELECTABLE_UNTIL` owner-installed Syft `v1.18.1` is observable.
  DEL-09-05-V3-04 remains blocked until
  the owner-created disposable identity exists; DEL-04-05-V3-01 is already
  landed.
- DEL-09-06-V3-03 is byte-unchanged. No item was removed, split, or completed.
- Receipt 220 appends after Receipt 219 and names Receipt 219 as its parent.
- Independent review round 1 over `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`
  returned FAIL with M-R1-F1/F2/F3. The immutable report is filed verbatim at
  `instances/M2_REVIEWER/REVIEW_NODE_M_R1.md` (SHA-256
  `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`).
  All findings are accepted and remediated in `REVIEW_DISPOSITIONS.md`.
- Independent review round 2 over `4fa170341700e491dff8c72ce1229ba84735f073`
  returned FAIL with M-R2-F1/F2. The immutable report is filed verbatim at
  `instances/M3_REVIEWER/REVIEW_NODE_M_R2.md` (SHA-256
  `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`).
  Both findings are accepted and remediated in `REVIEW_DISPOSITIONS.md`.
- `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.md`, and the M1–M4 child records
  now represent the actual sequential execution. M2 metadata is explicitly a
  source-calibrated non-verbatim reconstruction; M3 metadata is an accurate
  structured actual-dispatch record, not a byte-verbatim prompt claim. The
  immutable review reports govern. The next fresh reviewer consumes
  `REVIEW_R3_HANDOFF.md`.
- Independent review round 3 over `52998709c5c19bc5c3df3944735593299d60be56`
  returned FAIL with M-R3-F1. The immutable report is filed verbatim at
  `instances/M4_REVIEWER/REVIEW_NODE_M_R3.md` (SHA-256
  `2c5ceb0c930f566b9f375d2f8f8b1f62b9123f55e175a438d37fcf9e160a8802`).
  The finding is accepted and remediated in `REVIEW_DISPOSITIONS.md`.
- All execution nodes are now identified as `delegated-harness-native`.
  Every Agent-2 role is qualified `role not mechanically enforced`, with
  governed-workflow role evidence `instruction-asserted`.
  K-SUBAGENT/non-delegation is instruction+config asserted, not
  mechanism-proven; no descendants were observed. M4 launch/status/return
  evidence is filed, and the next fresh reviewer consumes
  `REVIEW_R4_HANDOFF.md`.

## Changed paths

1. `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md`
2. DEL-09-05 `_STATUS.md`
3. DEL-09-06 `_STATUS.md`
4. `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/`
5. `loop/LOOP_RECEIPTS.md` (existing append-only Receipt 220 amended in
   place; no second receipt)

All project-relative paths in this return are under
`projects/chirality-app-dev/` except the repo-root A15 record.

## Checks

Receipt validation, authority-corpus status, APP-HOLD integrity/reliance/
dispatch, harness self-check, harness pytest, exact change scope, manifest
verification, F-APP-2/no-positive-claim scan, forbidden-path scan,
DEL-09-06-V3-03 byte-section comparison, V3-04 selected-outcome coherence,
multi-agent record completeness, all three review-report identities, and
`git diff --check` pass. Round-1 through round-3 reviews failed; all reports
and accepted/remediated disposition tables are filed, and round 4 remains
pending. Native-descendant role/non-delegation evidence calibration passes.
Earlier corrected check attempts remain recorded honestly in
`CHECKS.json`. Frontend gates are skipped because no `frontend/` path changed;
A1 is not applicable.

## Boundaries and remaining actions

No Developer ID signing, notarization, Apple call, distribution,
publication, release-readiness, production identity, product, `frontend/`,
host, Root, lifecycle, Checking Approval SHA, register, decomposition, or
SCOPE_CHANGE act or claim occurred. Fresh round-4 review, HELP_HUMAN fan-in,
and owner merge remain the gates. After merge, the newly selectable nonce implementation and the two
separately authorized owner-host acts may proceed only through their own
bounded work.

**Uncertainty:** none in the transcription or live-state observations.
