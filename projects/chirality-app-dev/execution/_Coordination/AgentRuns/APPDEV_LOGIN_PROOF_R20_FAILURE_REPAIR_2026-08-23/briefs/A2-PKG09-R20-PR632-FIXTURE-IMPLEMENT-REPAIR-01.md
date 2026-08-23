# Sealed brief — fixture implementation evidence hygiene repair cycle 1

- Child: `A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-01`, explicit Agent-2 mode, instruction-asserted non-delegation; do not delegate.
- Objective: repair exactly four terminal blank-line findings in the implementation instance, freeze one-byte lineage, and run only authorized postchecks.
- AllowedWriteTargets: the four named implementation records plus `instances/A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-01/repair-cycle-1/`. No source/shared/product path.
- Preconditions: freeze each exact preimage bytes/SHA and tail `0a0a`; test source SHA and proof-script SHA must equal Amendment 09.
- Repair: remove only the last `0a`; require postimage ends `0a` but not `0a0a`; require `postimage + 0a` equals preimage.
- Checks: immutable test/proof/gzip hashes; App-only containment; empty index; exact `validate_candidate_whitespace.py --base-ref origin/main` once after all repair records freeze. Do not rerun any test/typecheck/syntax/APP-HOLD/diff assertion.
- Outputs: repair-cycle `ACTIVATION.md`, `REPAIR_LINEAGE.md`, `RETURN.md`; exact hashes and PASS/FAIL.
- Failure: any mismatch/new finding stops. No repair expansion.
- Git fence: no stage/commit/fetch/push/PR/rebase/force-push/merge.
