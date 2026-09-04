# Sealed round-4 review handoff — APPDEV_V3_NODE_M_2026-09-04

## Reviewer execution and evidence contract

Dispatch a new fresh, read-only descendant through the
`delegated-harness-native` execution class. Instruct it to operate in
ephemeral Agent-2 reviewer mode, with `role not mechanically enforced` and
governed-workflow role evidence `instruction-asserted`. Instruct and configure
it not to create descendants; K-SUBAGENT/non-delegation is instruction+config
asserted, not mechanism-proven, and the return must report whether any
descendant was observed.

The reviewer must have no Node M implementation or prior-review participation.
Review 100% of
`git diff 719fe5e34cefc40fe0dab4b045f5f2a89341ae2f..<ROUND_4_FREEZE>`, where
`<ROUND_4_FREEZE>` is the exact commit returned by M1 after this record is
finalized. The complete live range governs. Return PASS only with zero
BLOCKER and zero MAJOR findings.

## Immutable inputs

- Basis: `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge).
- Round-1 report: `instances/M2_REVIEWER/REVIEW_NODE_M_R1.md`, SHA-256
  `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`.
- Round-2 report: `instances/M3_REVIEWER/REVIEW_NODE_M_R2.md`, SHA-256
  `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`.
- Round-3 report: `instances/M4_REVIEWER/REVIEW_NODE_M_R3.md`, SHA-256
  `2c5ceb0c930f566b9f375d2f8f8b1f62b9123f55e175a438d37fcf9e160a8802`.
- Finding dispositions: `REVIEW_DISPOSITIONS.md`.
- Execution record: `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.md`, and
  `instances/**`.
- Owner-source transcription: contemporaneous verbatim sealed
  `instances/M1/LAUNCH_BRIEF.md`.

## Required verification

1. Reverify every R1/R2/R3 disposition and the byte identities of all three
   immutable reports. Confirm the M1 sealed brief remains byte-identical to
   the previously reviewed candidate.
2. For M-R3-F1, confirm every mutable role statement identifies
   `delegated-harness-native`; every Agent-2 label is qualified `role not
   mechanically enforced`; governed-workflow role evidence is
   `instruction-asserted`; and K-SUBAGENT/non-delegation is instruction+config
   asserted, not mechanism-proven, with no descendants observed.
3. Treat role/non-delegation language inside preserved immutable reports and
   the contemporaneous sealed M1 brief as quoted historical direction or
   reviewer output governed by adjacent calibration, not mechanism evidence.
4. Recheck owner-question/answer fidelity, mobile-fallback provenance,
   authorization-versus-performance, A14's prospective lift, parked
   DEL-09-05-V3-02 and V3-04, selectable nonce-only DEL-09-06-V3-04, the
   DEL-09-06-V3-03 byte fence, Receipt 220, F-APP-2, exact scope, complete
   manifest membership, and all closeout pointers.
5. Confirm no product/frontend byte, host act, descendant, push, PR, merge,
   signing, notarization, publication, distribution, or release-readiness
   act or positive claim is observed. Non-delegation remains calibrated as
   instruction+config asserted, not mechanism-proven.

## Deterministic checks to rerun

- Exact basis/ancestry, commit inventory, and changed-path inventory.
- `git diff --check`.
- Receipt validator and Receipt 220 parent/vocabulary/measurement posture.
- Authority-corpus v20 status.
- APP-HOLD integrity, reliance, and dispatch for DEL-09-05 and DEL-09-06.
- Harness self-check and harness pytest using the repository Python 3.13
  runtime.
- Exact change-scope against the sealed write set.
- Strict JSON plus complete manifest membership/hash verification.
- F-APP-2 and forbidden-path scans.
- DEL-09-06-V3-03 and Current State / Checking Approval SHA byte fences.
- A14 and pinned completion-reference identities; route inventory; observed
  absence of Syft and the disposable identity without host mutation.

Frontend gates remain skipped unless the diff unexpectedly contains a
`frontend/` path, which is a scope failure. The reviewer may write only its
external report; no repository edit or commit, push, PR, merge, host act,
signing, notarization, publication, distribution, or release execution is
authorized.
