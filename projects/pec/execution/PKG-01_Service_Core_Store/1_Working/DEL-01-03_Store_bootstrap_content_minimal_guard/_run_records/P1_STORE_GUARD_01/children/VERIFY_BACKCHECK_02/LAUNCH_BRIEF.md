# TASK backcheck brief — D85 store guard corrected candidate

RequestedBy: WORKING_ITEMS. RunID: P1_STORE_GUARD_01.
ParentInstanceID: pec_d85_production. ChildInstanceID: VERIFY_BACKCHECK_02.
PackageID: PKG-01. DeliverableIDs: DEL-01-03.
TaskSkill: software-code-review. ApplyEdits: false.
Model request: gpt-5.6-sol. Reasoning: medium. ForkTurns: none.
Role and non-delegation evidence: instruction-asserted; do not delegate.

This is a bounded continuation by the same independent verifier. Read the
original VERIFY launch brief, sealed FAIL review and manifest, the author
remediation run/evidence, `CANDIDATE_ATTEMPT_01_MANIFEST.json`, and
`CANDIDATE_ATTEMPT_02_MANIFEST.json`. Bind every observation to attempt 2.

Objective: backcheck V-F001 and V-F002 against corrected postimages, then
complete review of every original criterion not closed by attempt 1. Do not
limit review to the two corrections and do not repair findings.

AllowedWriteTargets: only
`{ScopePath}/_run_records/P1_STORE_GUARD_01/children/VERIFY_BACKCHECK_02/**`.
No product/config/status/memory/coordination/receipt/Git write is allowed.

Required checks:

- reproduce all attempt-2 product and author-manifest hashes;
- verify forged path/SHA/hash/state/source wrappers yield located failures,
  no crash, and no persisted residue;
- verify VER-009 loaded-suite identity/coverage separately from the verbose
  executed-test ledger, and confirm every mapped test has a PASS outcome;
- verify exact attempt-1 reverse artifact decodes/applies in scratch and
  reconstructs the four frozen hashes;
- finish the original guard, persistence, effective-ignore/tracked-artifact,
  lifecycle, interface, dependency/locality, documentation, test-quality,
  scope and evidence review;
- confirm the exact five selected/registered checks and current post-correction
  evidence; run only skill-allowed deterministic review helpers.

ExpectedReturn: PASS or FAIL, actionable findings and exact locations,
V-F001/V-F002 disposition, all-original-criteria coverage, scope/evidence
verdict, residual risk, and fan-in validity. Write compact evidence
incrementally and seal a recursive MANIFEST.json including nested manifests
and excluding only itself. No artifact/lifecycle acceptance or broader
completion claim.
