# R3 focus-test backcheck

**Clear for the manager to resume validation; no actionable finding.** This is a source/evidence backcheck, not a test pass.

The failure in [ui-final.log](../_run_records/FINAL_CHECKS_REPAIR/ui-final.log) reports 129 passed and one failed. The failed assertion compares the originally stored mill-tolerance button (tabindex -1) with the focused live button carrying the same row/column/test identity (tabindex 0). The unchanged `EngineeringTable.tsx` render path replaces that button with an editor anchor during editing and creates a new button afterward. This establishes a stale DOM-reference test defect, not evidence that focus returned to a different cell.

The only R3 change is in `ModelTree.table.test.tsx:282–289`: the test now queries the same exact cell before each edit and after editor closure. It still asserts exact focus, editor closure, zero operation dispatch for all four equivalent spellings, retained wrong-unit rejection, and unchanged input. No focus assertion, scenario, or protected criterion was weakened.

All nine files match [COMBINED_FREEZE_R3.json](../_run_records/COMBINED_FREEZE_R3.json); the complete diff hash is `ca59c34444cdcfdd82e8e0fb8172feaeef2f15000f88446c3bc406003dafee2b`. Eight file hashes, including every product file, are unchanged from the R1/R2 reviewed freeze. The sole changed test hash is `a904128367ad9b1719d91b724aa3d7d501b5de7e13d24b2e4d163f5b0f610599`. The original review and R1/R2 backcheck remain preserved.

Independent TASK `/root/native_pan_manager/pipes_review` performed read-only diff, hash, failure-output and editor-lifecycle inspection, then wrote this return and [_run_records/R3_BACKCHECK_MANIFEST.json](_run_records/R3_BACKCHECK_MANIFEST.json). No tests, build, browser/native, Git, product edits or delegation were performed. The failed run remains failed; the corrected test has not been rerun in this review. All affected execution results and ROOT native/CI/sweep/integration gates remain outstanding.
