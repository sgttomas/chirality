# Terminal handoff — ROOT_TM112_STOP_CONTRACT_2026-08-03

- **Accepted upstream:** signed `ROOT-TM112-STOP-CONTRACT-01 OPTION 1` and Owner
  Addition 4 transcript SHA-256
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`;
  N1 executed results SHA-256
  `cc2d703a32899e905ee44455f32a75f0ac7c79ca912d7dd4e2e181201f903ea2`;
  current HEAD/origin-main `88e7590d3664d4f1daf91bed2a8899bda0748b92`.
- **Derivative status:** `CURRENT DECISION SUPPORT / NON-AUTHORITATIVE`. E1 is
  bound installed-runtime evidence; E2 is a source/contract map; manager options
  and clauses are proposals; E3/E4 are independent refutation evidence. None is
  accepted runtime contract or implementation.
- **Closure verdict:** semantic-preparation phase `COMPLETE / PASS FOR HUMAN
  DECISION`. E3 blockers were repaired and E4 closed them. Deterministic
  validation passed. Human semantic acceptance remains open.
- **Recommendation:** G2/C1/F1 with 2,000 ms grace, immediate canonical SSE
  interruption, closeAll-plus-tracked residual force, and human-policy 500 ms
  force-settle cap. Exact consequences include degraded-vs-cleanup-failed
  states, coalesced stop, concurrent-start rejection, generation safety, and
  restart only after successful stop.
- **Held:** no contract/source/test implementation; no canonical docs,
  registers, App content, lifecycle, or Git action; no Root-to-App notice.
- **Rerun requirements:** rebind/regenerate if the owner chooses a nonrecommended
  option; rerun evidence/compatibility if Node/source/lock/contract/N1 basis
  drifts; test Node 22.19 support floor and target IPC platforms in the later
  accepted implementation tranche.
- **Remaining blockers:** accountable-human selection/acceptance. After that,
  implementation remains limited to the already-approved shutdown contract
  surface, `runtime-daemon.ts`, and bounded `daemon.test.ts` cases. Any inability
  to meet canonical interruption inside that boundary returns as scope change.
- **Downstream condition:** only after semantic acceptance and an accepted
  repair lands may Root route the App notice. App then owns the required
  non-blocking parity rerun; App-specific causality and process/SIGTERM behavior
  remain unproved.
- **Next owner:** `HELP_HUMAN` presents the packet; accountable human returns a
  signed selection. No manager may treat validation, hashes, or publication as
  semantic acceptance.
