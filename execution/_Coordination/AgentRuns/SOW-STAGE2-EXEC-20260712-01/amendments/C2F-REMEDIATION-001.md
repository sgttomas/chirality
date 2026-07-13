# C2F Remediation Amendment 001

Status: `ACTIVE — NON-CONSEQUENTIAL ACCEPTANCE-CRITERIA REPAIR`

## Trigger

RECON-C2F and EVAL-C2F independently confirmed that the initial C2 root and
App implementations accept an arbitrary self-bound syntactic
`D-GOV-16@<7-64 hex>` token, including the tests' unruled
`D-GOV-16@0123456`, rather than proving the accepted ruling
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`. They also confirmed that
the root ISSUED converter binds source commit, source hashes, and status hash
but exposes and embeds no accepted-basis input. EVAL-C2F additionally found
the root C2A return pointer stale despite a terminal project-local PASS.

## Disposition

This amendment does not change objective, authority, risk, ownership,
write-scope class, lifecycle meaning, or acceptance criteria. It repairs the
implementation to satisfy the already-accepted D-GOV-16 items 4, 6, and 8 and
the accepted Stage-2 C2F gate. No new human ruling is required.

- `C2R-R1`: require exact equality to the ruled D-GOV-16 authority, add and
  bind an ISSUED accepted-basis input, add positive/negative regression tests,
  and refresh root lane evidence.
- `C2A-R1`: require the exact ruled D-GOV-16 authority in the App scanner and
  add positive/negative regression tests.
- Parent: bind the already-terminal project-local C2A return at the root.
- `C2F-R1`: rerun read-only reconciliation, evaluation, and exact REVIEW
  calibration after both repairs PASS.

Scope clarification 001-A: the full root suite revealed one additional
fixture-only consumer, `tools/reporting/test_generate_coverage_csv.py`, that
asserts authorized dual behavior with the same synthetic unruled authority.
It is added to C2R-R1 solely to replace positive fixture authority with the
exact ruled value and, where useful, retain an unruled negative case. This is
a test-fixture refresh inside the already classified C2R root caller lane; it
does not change production behavior or acceptance criteria.

All original content, lifecycle, deliverable, Git, release, H1, H2, and legacy
retirement fences remain unchanged. C2G stays parked until C2F-R1 PASS.

Scope clarification 001-B: the C2A-R1 independent reviewer found that trimming
the supplied authority before equality allowed a padded version of the ruled
token. App repaired the input seam and corrected its regression to keep the
candidate marker exact while padding only the supplied token. The root
resolver/converter use the same trimming pattern, so C2R-R2 is released to
reject leading/trailing whitespace before exact comparison and add the same
negative regression. This is another fail-closed repair to the existing exact
authority criterion; it changes no authority or scope class.

Scope clarification 001-C: EVAL-C2F-R1 reproduced that
`tools/scope_of_work/derive_review_checklist.py` independently strips the CLI
authority before calling the exact resolver. A padded ruled token therefore
emits a checklist and records the normalized authority. C2R-R3 is released,
after the C2F-R1 terminal evidence is durable, to remove that normalization
and add an end-to-end no-output regression. This is the same exact-authority
criterion on an already-classified active caller; no production-contract or
authority change is introduced.

Evidence-format normalization 001-D: CHANGE-C2G's staged diff gate found one
trailing blank line in each of six C2F-R1 evaluation records. HELP_HUMAN
authorized removal of only those terminal blank lines. No finding, verdict,
claim, evidence reference, or accepted hash in P2_CONSUMERS changed; the six
records are not hash-bound by the P2 manifest. CHANGE must restage them and
rerun `git diff --cached --check` before evidence integration.
