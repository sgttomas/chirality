# Manager validation — third D-APP-93 lineage blocked at N1

Verdict: `BLOCK_DAPP93_THIRD_EXCLUDED_ROOT_SEARCH_SCOPE_VIOLATION`

## Accepted control evidence

- dispatch-time frozen graph SHA-256:
  `060a9d014160ca84270819824bdc78e782c025576da7f1179aeed150ec5f9922`;
- dispatch-time sealed N1 brief SHA-256:
  `c2f706937cbacdc6b1863fb5463ea36171eeb3f75b36aaa0a65693c58717b5f7`;
- post-terminal LF-hygiene final graph and brief SHA-256 identities:
  `accae9ca94b40aba132bdf9240f814922042725ba51e969d3c6f81942e16b7ed`
  and `b943fc689618a0866524a4020abceb1e6dbc051589a515c65a54b554d3496bc2`;
- final N1 return SHA-256:
  `639711fe1c63d6c3e0b671bed226591e2966dce076f3bf27838f6ce21b190e12`;
- final Stage 6 block record SHA-256:
  `9b50c68b74a94232acca87de7cca48f0d55987c92578c27ca0ef9a8078c3ed5c`;
- mechanically complete 80-row ledger SHA-256:
  `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`;
- runtime summary PASS SHA-256:
  `816b048c7cb83cc86a2d1e712b301c29a7eba94dc3e15913e3e2bc81f95dae13`
  (28 events, four complete sessions, no unmatched session).

These are preserved blocked-run evidence, not accepted N1 authoring fan-in.

## Pacing and telemetry result

The owner-prescribed cadence worked as designed:

- Stage 1 completed durably before its 10-minute expectation.
- Checkpoint 1 occurred at/after minute 10: two files, 18,078 bytes, delta
  +2 files/+18,078 bytes from dispatch.
- Stages 3-6 continued to write durable outputs and amendments, all recorded
  with counts, bytes, deltas, stage posture, and explicit native-context
  telemetry unavailability.
- Checkpoint 2 occurred at/after minute 22: six source-reconstruction files,
  110,306 bytes, delta +4 files/+92,228 bytes from checkpoint 1.
- The terminal N1 return followed; no silence-based interruption occurred.

Two telemetry correction events explicitly supersede an undercount and one
mistyped intermediate Stage 3 hash. Before final summarization, the provisional
N1 PASS event was normalized from `FINISH/PASS` to `CHECK/INFO` because it was
explicitly pending manager fan-in and the child then self-reported the blocking
violation; the later `FINISH/BLOCKED` is the sole terminal event. The preserved
event IDs, correction details, and final summary make the sequence
reconstructable.

## Mechanical ledger evidence

Static manager checks reproduce 80 unique contiguous IDs
`L3-CMD-001..L3-CMD-080`, 13 required CSV fields per row, no empty required
field, and zero matches for every manager-defined historical command-identity
pattern in the final ledger. N1 recorded complete phase coverage and no
represented operational command was executed.

## Blocking defect

Before fan-in, N1 self-reported that one Stage 3 read-only `rg -l` command
searched broadly below `projects/chirality-app-dev`; its intended excluded-root
globs did not match. Returned path names included files in all three historical
blocked roots, so the content search necessarily read excluded bytes. No
excluded content was displayed, cited, copied, or used, and every historical
root remained byte-identical, but the sealed absolute read exclusion was
violated.

Attribution is narrower than the fence: the owner prohibited resuming,
copying, or repairing prior drafts; the owner did not explicitly impose an
absolute no-read rule. HELP_HUMAN/WORKING_ITEMS introduced that stricter child
read fence as a conservative operationalization. Supervisory design also
contributed to the failure by not requiring path-allowlisted search enforcement
in the pre-dispatch graph/brief despite imposing the absolute fence. Therefore
the search proves violation of the sealed manager/Agent0 brief, not by itself
violation of the owner's stated non-reuse direction.

The defect invalidates N1 regardless of ledger completeness. The frozen graph
contains no retry/replacement node. N2 packet authoring, manager packet
validation, byte freeze, fresh verifier, approval hash, and owner approval gate
were never released or reached.

## Disposition

Reject N1 fan-in; preserve all third-lineage evidence; close this lineage
blocked; append a Receipt-150 closeout through CHANGE; present the blocker and
`CAUSAL_ANALYSIS_THREE_LINEAGES.md` to the owner. Do not start, imply, or reuse
this evidence for a fourth lineage without new owner direction.

No packet, freeze manifest, verifier brief/return/PASS, exact approval hash,
execution authority, runtime, debugger/LLDB, attach, package/build, helper/GUI,
signal, replay, Security/Keychain, credential, product, release, reliance, Git,
Task Management, register, decision, lifecycle, receipt, or foreign-loop effect
was created by this WORKING_ITEMS run.
