# RETURN — M1 — APPDEV_V3_NODE_M_2026-09-04

**Status:** `REVIEW_READY_R2 — round-1 FAIL accepted and remediated; awaiting fresh round-2 review`

**Basis:** `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge)

**Branch:** `codex/app-v3-nodeM-a15-owner-rulings-2026-09-04`

**Freeze:** the Git HEAD returned with this record; no self-referential commit SHA is embedded.

**Model:** provider OpenAI; engine Codex; model GPT-5 family (exact model identifier not exposed to the agent runtime), as ephemeral Agent 2 under HELP_HUMAN.

## Result

- Transcribed the owner's three 2026-09-04 answers into A15. The A15 file
  SHA-256 is
  `89633722ecefc3907c44e1c964353ed33c793f65ec1686afde3ae015d86f305c`.
- A15 selects a per-response CSP nonce with dynamic rendering for the four
  packaged routes `/`, `/chat`, `/pipeline`, and `/workbench`.
  DEL-09-06-V3-04 is annotated `SELECTABLE` once A15 lands. The outcome is
  authorized, not an exact implementation shape; hash/SRI is not selected.
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
  All findings are accepted and remediated in `REVIEW_DISPOSITIONS.md`; the
  next fresh reviewer consumes `REVIEW_R2_HANDOFF.md`.

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
DEL-09-06-V3-03 byte-section comparison, and `git diff --check` pass. Round-1
review failed; its report and accepted/remediated disposition table are filed,
and round 2 remains pending. The initial harness status/self-check errors and the over-broad status-field grep,
plus their corrected passes, are recorded honestly in `CHECKS.json`. Frontend gates are skipped
because no `frontend/` path changed; A1 is not applicable.

## Boundaries and remaining actions

No Developer ID signing, notarization, Apple call, distribution,
publication, release-readiness, production identity, product, `frontend/`,
host, Root, lifecycle, Checking Approval SHA, register, decomposition, or
SCOPE_CHANGE act or claim occurred. Fresh round-2 review, HELP_HUMAN fan-in,
and owner merge remain the gates. After merge, the newly selectable nonce implementation and the two
separately authorized owner-host acts may proceed only through their own
bounded work.

**Uncertainty:** none in the transcription or live-state observations.
