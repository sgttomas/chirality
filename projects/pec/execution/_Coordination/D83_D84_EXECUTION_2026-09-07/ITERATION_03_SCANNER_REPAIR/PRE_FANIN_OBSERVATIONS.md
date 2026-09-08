# Pre-fan-in observations

These are HELP_HUMAN-relayed progress observations, not accepted terminal
fan-in. The owning WORKING_ITEMS records and final seals govern.

- Source author PASS: focused 23, full enforcement 28, posture PASS, API 6,
  harness exit 0, and exact three postimages. Scanner behavior remains bounded
  to the two authorized repairs.
- First fresh verifier completed checks with zero reported findings but stalled
  before durable outputs. WORKING_ITEMS interrupted it and preserves the attempt
  record; no acceptance is inferred.
- Replacement `/root/pec_d84_repair/verifier_attempt2` was configured
  `gpt-5.6-sol`, `medium`, `fork_turns=none`. It independently reproduced
  authority, holds, hashes, focused 23, full 28, posture, API 6 and harness;
  final probes and seal remain pending.
- An initial auxiliary-runner scratch-path failure and the replacement's first
  wrong-cwd harness invocation are tool/invocation failures corrected in the
  owning evidence. They are not product defects and are not erased.
- Direct six-file RECONCILIATION backcheck is not released until HELP_HUMAN
  accepts a terminal source-verifier PASS.

Later fan-in update: source verification and the six-file backcheck were
accepted. HELP_HUMAN rejected the first WORKING_ITEMS terminal manifest
(`339bb9…`) because it bound 36 files while 38 total files existed: its
enumerator excluded every basename `OUTPUT_MANIFEST.json`, including the
nested verifier manifest, instead of excluding only the root self-manifest.
All bound hashes passed and source/verifier/backcheck bytes stayed unchanged.
The rejected attempt is preserved in the owning dispatch evidence; a bounded
root-manifest correction is pending, expected to bind 37 entries / 38 total.

Common candidate whitespace later identified two trailing spaces in the
accepted verifier `REVIEW.md`; they were Markdown hard-break formatting, but
HELP_HUMAN refused a waiver. Exact two-line normalization was routed through
the owning verifier, with prior sealed bytes preserved in dispatch evidence.
RECONCILIATION may refresh only bound evidence hashes, then WORKING_ITEMS
reseals the root. No claim or product test rerun is required; Receipt 175 and
common final seal remain withheld for the refreshed terminal binding.
