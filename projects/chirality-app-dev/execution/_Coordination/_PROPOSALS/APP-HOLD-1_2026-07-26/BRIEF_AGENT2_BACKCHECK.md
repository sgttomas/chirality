# Sealed Brief — APP-HOLD-1 Corrected-Candidate Backcheck

BriefID: `APP-HOLD-1-A2-BACKCHECK-2026-07-26`  
Parent: HELPS_HUMANS (Agent 1)  
Reviewer: same read-only ephemeral Agent 2 that authored
`ADVERSARIAL_REVIEW_PASS1.md`  
Write targets: none  
Corrected-basis hash list: `ARTIFACT_HASHES.sha256`  
Hash-list SHA-256:
`4b672856e74815f30be96e52958adfe4c2c6cdc3143bd8dccfdf8c9f65e38e75`

## Objective

Backcheck every pass-1 finding against the corrected candidate and decide
whether the exact candidate may enter the owner gate.

## Corrections presented

1. Removed the runtime exception register, `--exceptions` input, and owner
   prose parser. A held target always blocks. Human override requires a later
   separately accepted and applied App-loop amendment before dispatch.
2. Made test path resolution explicit for candidate and proposed live layouts.
3. Restricted repository, SOW, register, fixture, and JSON output paths.
4. Added exact proposed root tool-registry and App script-catalog entries plus
   tool I/O, exit, error, and idempotence contract.
5. Made top-level front-matter and register parsing fail closed on duplicate,
   malformed, missing, or extra fields.
6. Stated that the universal prohibition is not universal product-code
   interception.
7. Expanded the suite to 11 tests, including the removed exception bypass,
   path layouts, malformed inputs, canonical Git root, and output containment.

## Required backcheck

- Reverify all files listed in the corrected hash list.
- Rerun the corpus scan and test suite where feasible.
- Disposition AHR-001 through AHR-006 as `CLOSED | PARTIAL | OPEN`.
- Confirm whether the proposed application-surface inventory is complete and
  no broader than required.
- Identify any new material defect.
- Return `ADMIT | ADMIT_WITH_WARNINGS | RETURN_FOR_CORRECTION`.
- Confirm no write and report engine/provider/model.

Do not edit, stage, commit, or apply any file. Do not delegate.

