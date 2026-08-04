# AUTHOR brief amendment 1 — exact source-identity correction

- Status: `SEALED`
- Node: `AUTHOR`
- Applies to: attempt 2
- Detection layer: child pre-write source-identity verification
- Failure class: `MANAGER_TRANSCRIPTION_DEFECT`
- Reason code: `AUTHOR-SOURCE-HASH-MISMATCH-OWNER-SELECTION-MATRIX`

AUTHOR attempt 1 stopped before writing because `ACTIVATION_RECORD.md`
transcribed the wrong SHA-256 for
`decision_support/OWNER_SELECTION_MATRIX.csv`. No deliverable-local output
exists from attempt 1.

The corrected accepted identity is:

`57b27b486e4c06d23425e3dd0760904a1b4a04bf0bcf49e0610b6c677a398c92`

This value is independently reproduced by the live file and is recorded in
both `decision_support/PACKAGE_MANIFEST.sha256` and
`decision_support/DECISION_SUPPORT_ACCEPTANCE.md`. The package manifest file
continues to hash to the signed identity
`623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`.

No authority, selection, source membership, write scope, output, acceptance
criterion, exclusion, or semantic instruction changes. All other identities
and all terms of `briefs/AUTHOR.md` remain sealed and unchanged.
