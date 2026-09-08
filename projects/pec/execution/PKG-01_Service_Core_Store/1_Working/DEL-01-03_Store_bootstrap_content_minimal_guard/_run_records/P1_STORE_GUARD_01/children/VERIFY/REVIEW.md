# D85 store guard independent review

Status: **FAIL — blocking finding open**.

Reviewed candidate: manager-frozen attempt 1 in
`../../CANDIDATE_ATTEMPT_01_MANIFEST.json`; all nine listed product and
configuration hashes verified against the reviewed bytes before this return
was sealed.

Scope validation passed for the nine exact D-PEC-85 product/configuration
paths and the authorized DEL-01-03 / D85 closeout administration. Affected
check selection resolves exactly the five checks recorded by the author and
manager.

## Blocking findings

### V-F001 — Forged typed wrappers bypass validation or crash admission

Location: `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py:145-151`,
`:182-189`, and `:200-209`.

The guard uses `isinstance` to trust `RepositoryPath`, `ShaDigest`, and
`ContentHash` objects that were validated only by their constructors. Frozen
dataclasses are not an admission-time trust boundary: callers can construct an
instance with `object.__new__` and set invalid attributes with
`object.__setattr__`. A forged `RepositoryPath` therefore persists arbitrary
or non-normalized text, and forged digest wrappers can persist invalid values
or raise `AttributeError` while rendering `.algorithm.value`. This defeats the
brief's explicit forged-dataclass bypass requirement and violates the located,
explicit rejection contract.

Remediation direction: revalidate every wrapper's inner algorithm/value at
the guard boundary and return a located `AdmissionFailure`; add fixtures for
forged source paths, field paths, SHA values, and hash values, including
invalid enum attributes and prose/non-normalized payloads.

### V-F002 — VER-009 evidence is a source-tag self-assertion

Location: `projects/pec/v2/tests/storage/test_store_lifecycle.py:154-161` and
`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/AUTHOR/CHECKS_REGISTERED.json:21`.

The VER-009 test concatenates test source files and checks only that each
`VER-001:` through `VER-009:` string occurs. That passes when labels exist in
docstrings even if the corresponding tests are skipped, undiscovered, or do
not execute the claimed behavior. The normalized unittest output contains
only twelve dots and therefore does not map executed test identities to the
declared verification methods. This is the exact self-asserting mapping the
sealed verifier brief requires the review to reject.

Remediation direction: produce normalized execution evidence that enumerates
the discovered and executed test identities (for example, verbose unittest
output or an equivalent structured list), bind those identities to
VER-001..009, and make VER-009 validate the actual discovered/executed suite
rather than source-text labels alone.

## Evidence and scope verdict

- Candidate scope: PASS.
- Frozen-candidate identity: PASS; all nine attempt-1 hashes are current.
- Registered check selection: PASS; five checks selected.
- Author evidence: all five selected registered checks report PASS; the
  focused storage run reports 12 tests and exit 0. The evidence is normalized
  and the AUTHOR manifest's seven listed evidence-file hashes verify against
  current bytes. Default candidate-whitespace evidence explicitly reports
  untracked-file coverage and PASS.
- AUTHOR manifest completeness: PASS for the AUTHOR subtree (seven files plus
  its excluded root manifest; no nested manifests).
- Evidence sufficiency: FAIL because VER-009 does not prove the required
  executed-test mapping, and the passing suite has no forged-wrapper cases.
- Contracts/dependencies/generated artifacts: no schema migration, generated
  product artifact, external dependency, or public path/SQLite/connection
  leakage was found. The profile change is additive and preserved all prior
  checks according to manager evidence.

## Non-blocking residual risks

- Real reconciler, presence, and event consumers are outside this slice, so
  their eventual use of this boundary remains unproved here as documented.
- System kill/parity behavior remains outside DEL-01-03 and was not assessed.
- The adapter trusts database scalar values on read beyond checking the stored
  field-class enum; direct corruption is surfaced only for an invalid class.
  No public bypass write was found, so this is recorded as residual hardening
  risk rather than a finding in this bounded ingest review.

## Fan-in verdict

**FAIL / BLOCKED_FOR_FAN_IN.** Invalid for WORKING_ITEMS technical fan-in
while V-F001 and V-F002 remain open. This is technical review only and makes
no artifact, lifecycle, release, kill/parity, D83-inquiry, DEL-01-03, or P1
acceptance decision.
