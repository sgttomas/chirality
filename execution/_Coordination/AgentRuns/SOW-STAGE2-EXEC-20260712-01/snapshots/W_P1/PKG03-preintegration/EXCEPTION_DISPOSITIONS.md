# PKG-03 Exception Dispositions

## Retained upstream exceptions

1. Batch-02 author terminal manifest attempt 1 was stale because terminal
   evidence changed after generation. It was rejected.
2. Batch-02 author terminal manifest regeneration attempts 2 and 3 were
   incomplete. Both were rejected.
3. The fully populated 425-row Batch-02 author manifest was generated last,
   self-excluded, and rehashed 425/425. The reconciliation independently
   reproduces all 425 current rows without erasing the failed chain.
4. Batch-02 verifier attempt 1 for `DEL-03-07` failed because comma-separated
   reference items were not whitespace-normalized. The verifier-local attempt
   wrote neither candidate nor project paths. The corrected fresh restart
   returned `PASS_UNCHANGED`; reconciliation freshly reproduces `DEL-03-07`
   and all other package members.
5. The manager's initial finalization schema-key guess failed before candidate
   mutation. The complete successful manager rerun and this independent full
   package reproduction use the registered schema keys.

None of these exceptions changes a candidate, source, status, control,
dependency, acceptance criterion, semantic verdict, or project path. They are
retained process/substrate history and are the reason full-package—not
sample-only—reproduction was mandatory.

## Current runtime blocker

The required `FULL-PACKAGE-VERIFY` Agent 2 launch was attempted three times.
Each dispatch failed before child execution with `agent thread limit reached`.
The sealed brief exists, but it is not claimed as executed. Under the runtime
doctrine and parent direction, this blocks a reconciliation `PASS` despite the
complete successful manager reproduction.

