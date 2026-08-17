# WORKING_ITEMS manager return

Verdict: `ACCEPT` for PKG-05 / DEL-05-04.

The gated residual is now proven by a dedicated real-daemon integration test.
The authenticated Desktop port and actual Root `runCli session replay --json`
façade decode structurally equal parsed canonical manager/child sessions before
and after a fresh service restart, with exact
recorded parentage and engine attribution. Legacy source bytes remain unchanged.
No App source defect was exposed. Focused Vitest, worktree-correct typecheck,
scope/whitespace validation, APP-HOLD integrity, and harness self-check passed.
Integrated review found one record-only claim-calibration issue: structural
equality had been overstated as byte equivalence. All node-created records were
corrected. A second finding rejected a second `RuntimeClient` as CLI evidence;
amendment v2 now crosses CLI parsing/rendering with captured decoded output.
Fresh review then required raw-buffer comparison for the limited legacy-byte
claim. The final candidate is `310e0c9539dbac6af89159bd312b2a93a082689b`;
focused test/typecheck and review backcheck PASS with no remaining findings.
Renewed fan-in is ACCEPT. No full-tranche gate or release claim is made.

Changed node paths are the dedicated integration test, DEL-05-04 status/memory
and one run record, plus this unique managed run root. Concurrent PKG-08 state
is external and excluded. Blockers: none. Next owner: `CHANGE` after integrated
closeout accepts the parallel-node candidate. Rerun on Root daemon/client/
session migration/replay changes or App runtime-client/Woven hierarchy changes.
