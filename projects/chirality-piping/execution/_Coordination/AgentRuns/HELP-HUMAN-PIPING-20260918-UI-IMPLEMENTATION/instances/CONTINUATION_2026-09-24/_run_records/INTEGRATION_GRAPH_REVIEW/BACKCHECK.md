# IGR-01 record repair backcheck

**PASS — IGR-01 is closed.** The only change since the original reviewed graph is the two-line Pipes record repair at WORK_GRAPH lines49 and203. Replacing those two lines with their recorded preimages reconstructs the complete original graph SHA-256 `3e8aff489f41ddc202e8144832899a29302b99cb3513d191fc71c42ca9647296`; current graph SHA-256 is `ebad61356f6d45bfabf9eb0e4d05afbffc2a0d30ebd22ac4b28e04a5b9e14477`.

The old checkpoint is now accurately labelled the frozen source/resume basis, and the direct current FINAL_CHECKS_R3 link resolves. Its observed records substantiate130 frontend tests, TypeScript exit0, rebuilt WASM exit0 with no maintained-input mismatches, and all10 unchanged backend probes passing. All nine current source hashes still match the browser invocation freeze.

The graph explicitly preserves the pre-edit expected-completed/actual-failed solve discrepancy and makes no full browser pass claim. The retained partial trace call@808 independently shows expected state=completed and observed state=failed with zero result rows. The interruption record preserves the stalled-teardown failure context. Diagnosis, remaining browser work, native, CI, clean sweep and merge remain open.

This closes the record inconsistency only. It provides no source, solver or browser qualification and does not waive any later check. Original RETURN.md and MANIFEST.json are unchanged; only BACKCHECK.md and BACKCHECK_MANIFEST.json were written. No heavy check, product edit, native/browser action, network or Git mutation occurred.
