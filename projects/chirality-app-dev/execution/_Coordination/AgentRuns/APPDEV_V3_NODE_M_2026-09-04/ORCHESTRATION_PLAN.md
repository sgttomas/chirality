# Orchestration Plan — APPDEV_V3_NODE_M_2026-09-04

- **Run ID:** `APPDEV_V3_NODE_M_2026-09-04`
- **Selection authority:** HUMAN — owner Ryan Tufts supplied three typed
  plain-text authorizations in the HELP_HUMAN session on 2026-09-04. A15 is
  the durable ruling form; this run record is evidence and coordination.
- **Accepted basis:**
  `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (`origin/main`, PR #693
  merge).
- **Supervisor:** HELP_HUMAN (Agent 0).
- **Execution class:** `delegated-harness-native` for M1 and every reviewer.
  Native descent does not mechanically assign an Agent role. Every Agent-2
  label in this record is therefore `role not mechanically enforced`, with
  governed-workflow role evidence `instruction-asserted`.
- **Implementer:** M1, instructed to operate in bounded ephemeral Agent-2
  mode under that calibration.
- **Reviewers:** M2, M3, M4, and M5 were separate fresh, read-only
  descendants instructed to operate in ephemeral Agent-2 reviewer mode under
  that same calibration. M6 is the required next fresh reviewer over the
  complete round-5 freeze.
- **K-SUBAGENT calibration:** each child was instructed and configured not to
  create descendants. Non-delegation is instruction+config asserted, not
  mechanism-proven; no descendants were observed.
- **Posture:** sequential implement → independent review → remediate → fresh
  independent review. There was no concurrent write fan-out.

## Actual execution sequence

1. M1 recorded the A15 candidate and the bounded deliverable/receipt effects,
   corrected its deterministic evidence record, and froze
   `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`.
2. M2 reviewed the complete basis-to-freeze diff and returned FAIL with three
   MAJOR findings. Its immutable report is filed at
   `instances/M2_REVIEWER/REVIEW_NODE_M_R1.md`.
3. M1 accepted and remediated all M2 findings and froze
   `4fa170341700e491dff8c72ce1229ba84735f073`.
4. M3 reviewed the complete basis-to-remediation diff and returned FAIL with
   two MAJOR findings. Its immutable report is filed at
   `instances/M3_REVIEWER/REVIEW_NODE_M_R2.md`.
5. M1 accepted and remediated both M3 findings. The resulting Git commit is
   the round-3 review freeze; this record does not embed a self-referential
   commit identifier.
6. M4 independently reviewed 100% of the accepted-basis-to-round-3-freeze
   diff and returned FAIL with one MAJOR finding. Its immutable report is
   filed at `instances/M4_REVIEWER/REVIEW_NODE_M_R3.md`.
7. M1 accepted and remediated M4's evidence-calibration finding. The
   resulting Git commit is the round-4 review freeze; this record does not
   embed a self-referential commit identifier.
8. M5 independently reviewed 100% of the accepted-basis-to-round-4-freeze
   diff at `c3c3b628203ccc949d3ee3b3573a96b45f472278` and returned FAIL
   with one MAJOR finding. Its immutable report is filed at
   `instances/M5_REVIEWER/REVIEW_NODE_M_R4.md`.
9. M1 accepted and remediated M5's current-round/handoff-coherence finding.
   The resulting Git commit is the round-5 review freeze; this record does
   not embed a self-referential commit identifier.
10. M6 must independently review 100% of the
    accepted-basis-to-round-5-freeze diff. Manager fan-in requires zero
    BLOCKER and zero MAJOR findings.

## Write boundary

Only these paths may change:

- `plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md`
- DEL-09-05 `_STATUS.md`
- DEL-09-06 `_STATUS.md`
- `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/**`
- append-only corrective Receipt 221 in `loop/LOOP_RECEIPTS.md` (Receipt
  220 remains preserved earlier tranche evidence)

The two deliverable paths and every AgentRuns/ledger path above are relative
to `projects/chirality-app-dev/`; A15 is repo-root. No product, `frontend/`,
host, Root, lifecycle, Checking Approval SHA, register, decomposition,
SCOPE_CHANGE, signing, notarization, publication, distribution, or release
act is in scope.

## Evidence calibration

M1's launch brief is a contemporaneous verbatim copy of the received sealed
brief and is preserved unchanged; its Agent-2 and non-delegation directions
are instruction-mode terms subject to the execution-class calibration above,
not claims of mechanical enforcement. The M2 launch/status/return records were reconstructed after round 2
from M2's immutable report and the supervisor's retained runtime evidence;
they are explicitly labelled non-verbatim. M3's launch record is an accurate
structured rendering of the actual dispatch supplied by the supervisor, not
a claim of byte-verbatim prompt preservation. M4's launch record is an
accurate structured reconstruction from the sealed R3 handoff, immutable R3
report, and supervisor direction; it is not a byte-verbatim prompt claim.
M5's launch record is an accurate structured reconstruction from the spent
historical R4 handoff, immutable R4 report, and supervisor direction; it is
not a byte-verbatim prompt claim. The M2, M3, M4, and M5 review reports are
immutable contemporaneous reviewer outputs and govern if a summary record
differs.

No child push, PR, merge, host act, or product-byte mutation was observed.
No child descendants were observed, with K-SUBAGENT evidence limited to
instruction+config assertion rather than mechanism proof. No PASS is inferred
from deterministic checks or remediation; fresh M6 review under the active
`REVIEW_R5_HANDOFF.md` remains required. The pre-review candidate
intentionally cannot include a future round-5 verdict/report. If round 5
passes, its immutable report and final narrative closeout may be filed after
PASS without changing ruling or deliverable bytes.
