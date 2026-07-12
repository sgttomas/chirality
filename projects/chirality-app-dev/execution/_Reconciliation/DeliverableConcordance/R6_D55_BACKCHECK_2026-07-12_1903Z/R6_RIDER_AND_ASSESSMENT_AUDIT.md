# R6 Rider and Stale-Assessment Audit

## Explicit rider evidence

| Rider | Exact live proof | Verdict |
|---|---|---|
| P39 CQ-F5 | `loop/LOOP_RECEIPTS.md:1333-1337` records reviewed/no-repair; DEL-02-01 `_STATUS.md` retains the Checking Approval SHA and D-APP-19 Authorization Basis as historical evidence. | CONFIRMED |
| P43 DEL-03-04 REQ-004 | DEL-03-04 `Assessment_INSP-03_DEL-03-04.md:67-75` preserves the PARTIAL verdict and names REQ-004 in the ORN-09 supersession. | CONFIRMED |
| P43 DEL-03-04 REQ-005 | The same annotation preserves PARTIAL and cites `message.accepted` durability. | CONFIRMED |
| P43 DEL-03-04 ACC-002 | The same append-only annotation explicitly names ACC-002 without recoding the historical matrix. | CONFIRMED |
| P43 DEL-03-04 ACC-003 | The same append-only annotation explicitly names ACC-003 without recoding the historical matrix. | CONFIRMED |
| P45 UPD-106 | `frontend/src/__tests__/components/shell-frame.test.tsx` proves active-link rendering. | CONFIRMED |
| P45 UPD-110 | `frontend/src/__tests__/components/app-shell-resize.test.tsx` proves the focusable separator and Home/End/Arrow interaction. | CONFIRMED |
| P45 UPD-140 | `frontend/src/__tests__/scripts/validate-harness-premerge.test.ts` proves missing-runtime failure. | CONFIRMED |
| P45 UPD-141 | The same premerge test proves removed-regression-ID failure. | CONFIRMED |
| P45 six-pin root export | Receipt 39 (`loop/LOOP_RECEIPTS.md:1362-1369`) quotes the owner's pointer-based direction deferring the rider to separate authorization; Receipt 44 (`:1462-1470`) confirms no root export edit. | CONFIRMED DEFERRED / OUTSIDE CLOSEOUT |

## Exact P04 proof

- Normative: DEL-06-06 `Specification.md:35,66` requires `hook.progress` and stdout/stderr/output preservation.
- Implementation: `frontend/src/lib/harness/sdk-message-mapper.ts:986-997` emits `hook.progress`.
- Tests: `frontend/src/__tests__/lib/sdk-message-mapper.test.ts:156-177` proves emission and field preservation; `frontend/src/__tests__/lib/session-events.test.ts:47-65` proves JSONL persistence/replay.

## Exact P19 proof

- Implementation: `frontend/src/lib/lifecycle/transition.ts:67-73` exact-matches `HUMAN`, `USER`, and `OPERATOR`.
- Negative tests: `frontend/src/__tests__/lib/lifecycle-status.test.ts:138-153` rejects `HUMANOID`, `HUMAN_RESOURCES`, and `HUMAN AGENT` with `UNAUTHORIZED_ACTOR`.
- Positive/gate tests: `frontend/src/__tests__/lib/lifecycle-status.test.ts:155-170` accepts the three exact aliases and preserves the Checking Approval SHA.

## Stale-assessment current-state audit

The P43 commit `9b972c07c` identifies exactly twelve assessment files: DEL-00-02, DEL-01-01, DEL-01-02, DEL-01-03, DEL-02-01, DEL-03-04, DEL-04-03, DEL-07-03, DEL-10-01, DEL-10-02, DEL-10-03, and DEL-10-05. Each live file retains its historical verdict table and has a `D-APP-56 R5 P43 annotation` current-state block. DEL-03-04's block covers its four rider claims. DEL-10-04 was reviewed/no-edit because it has neither a P43 proposal row nor rider.

Verdict: **12/12 CONFIRMED; zero historical verdict recodes; zero immutable-run edits.**
