# PROJECT_SETUP — SCA-005 A4 + B3 (D-PEC-93 option A) Handoff State

**Act date:** 2026-09-25
**Coordinator:** WORKING_ITEMS (Type 1), node C5 of HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`
**Branch / basis:** `claude/pec-d93-project-setup-act` from `origin/main` `04e04da00f620a1a5786ee744b167490cc90531c`
**Publication:** through its own PR under the standing Git authorization of 2026-09-12; not merged by this act.

## SCA-005 open-work ledger close-out

Per the proposal (§"Administrative grant", "Records not opened"), the SCA-005
open-work items that D-PEC-92 and checkpoint 3 left open are closed out here,
not by editing the accepted SCA-005 snapshot:

| Item | State after this act |
|---|---|
| A4 — DEL-02-08 / DEL-02-09 folders, metadata files and `Dependencies.csv` anchors | DONE — two folders, 12 files; both `_STATUS.md` created at `OPEN` (`TASK+preparation`) |
| B3 — dependency retirements, refresh, new edges and mirrors | DONE — 20 rows retired, 1 refreshed, 8 added, 0 deleted; 13 mirrors edited, 2 created |
| Re-audit after A4 and B3 | DONE — `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`, 0 BLOCKER, `overall_status` `WARNINGS` |
| `_Evaluation/DecompCoverage/_LATEST.md` | MOVED to `COV_SCA005_POSTSETUP_2026-09-25_1606` (condition "0 BLOCKERs" met) |
| B1 — re-pin 42 `_CONTEXT.md` and 64 `_REFERENCES.md` to revision 1.5 | OPEN — not selected (owner ruled A without B1); re-audit COV-068/069 (prior COV-077/078) carry it |
| B4 — first Scope of Work for DEL-02-08 / DEL-02-09 | OPEN — outside this packet; no `## Remaining` entry was written |

## Re-audit snapshot (immutable)

| File | SHA-256 |
|---|---|
| `Brief.md` | `327f37d916cd511e42ec4f2af66e1fb7362ff822edfd3f6cfa2e9f7e643e8c97` |
| `Decision_Log.md` | `5f250cdb61a860f2bf509465c33e8e73f9ce063cbc1267e5fd7c6b7deeede170` |
| `Decomp_Coverage_IssueLog.csv` (73 rows) | `3e93aaf3784545ca777ab620598522d9a4ce4cd0eaf3bf9ad9d34ebf57505850` |
| `Decomp_Coverage_Matrix.csv` (66 rows) | `328118f62d82eb3db62b0c5f0bcec0802b83a3219c136ce9b561df741526c5fa` |
| `Decomp_Coverage_Report.md` | `7b3b586a79b83eb9955f5171c75b4c37c747e9966b2e2bb6a6a23e5bf467ac34` |
| `PrePost_Comparison.md` | `76181ac5bbbc30ac139e08726cd8eb7deb7cc7de7ec1644101e46d10496a5657` |
| `QA_Report.md` | `1774cb0ff215a5ea4e1feb7406b5a6ad9e710a998977ac6a10798707500b6c64` |
| `RUN_SUMMARY.md` | `b30751377f0c94bad336590645e3ecb90ed1579b3722fc62ebf9f8e868006311` |
| `coverage_summary.json` | `b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d` |

## Residuals (recorded, not repaired here)

1. **Evidence-quote currency.** 19 ACTIVE EXECUTION rows in 10 registers cite
   quotes no longer verbatim (proposal finding 1; re-audit COV-072). The owner
   ruled them carried as a residual for a later `dependency-extract` refresh or
   packet. The act did not touch those rows.
2. **B1 metadata alignment.** 42 contexts and 64 of 66 reference packets still
   name revision 1.4 (re-audit COV-068/069). A separate short packet.
3. **Stale pre-act descriptions outside this grant.** The SCA-005
   `Handoff_State.md` / `RUN_SUMMARY.md` and both revision/scope-change
   `_LATEST.md` pointers still describe A4 as not created and the audit as
   blocked (re-audit COV-073); `_Coordination/_COORDINATION.md` still names
   revision 1.4 (proposal finding 5). None is opened by D-PEC-93.
4. **Later `dependency-extract` runs (ruling N5).** The four new EXECUTION rows
   survive a later `MODE=UPDATE` only if that deliverable's sources then show
   the edge. A known property, not a defect.
5. **Loop records.** The D-PEC-93 register-row status after merge, the receipt
   and the `docs/STATUS.md` / `README.md` lines are HELP_HUMAN's records under
   D-PEC-88; this act writes none of them.

## Execution disclosures

- **Generator executor.** The proposal's administrative grant describes "one
  bounded TASK author" running the generator. The C5 brief assigned the run
  to this WORKING_ITEMS manager and limited its children to the `audit-decomp`
  TASK and the verifier, so the manager ran the generator. The history lines
  of the two new `_STATUS.md` files read `TASK+preparation`, the actor string
  fixed in the ruled postimage bytes (ruling Q5); they were not changed.
- **`--repo` argument.** Passed as the literal repository root because the
  host refused `$(git rev-parse --show-toplevel)`; the value is identical.
- **Commit before audit.** The product writes and checks were committed
  (`995af4f36`) before the audit dispatch, so the audit cites a fixed commit.

## Rollback (ruling N6)

- **Before merge:** close the PR and discard the branch and worktree.
- **After merge (owner direction):** a revert PR of this act — restoring the 19
  modified preimages and `DecompCoverage/_LATEST.md` `0084d218…7432`, and
  removing the two new folders (12 files). The `COV_SCA005_POSTSETUP_*`
  snapshot and this run root stay as non-current evidence, with a rollback
  note appended here. No history reset; no silent downstream repair.

## Independent verification

See `VERIFIER_VERDICT_NN.md` in this run root and
`AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/C5_VERIFIER_VERDICT_NN.md`.

## Not claimed

No CHECKING, ISSUED, artifact acceptance, readiness or reliance. Nothing here
prompts about CHECKING.
