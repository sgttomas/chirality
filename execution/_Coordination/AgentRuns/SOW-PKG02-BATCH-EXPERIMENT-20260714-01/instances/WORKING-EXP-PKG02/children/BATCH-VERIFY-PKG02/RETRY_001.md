# Verifier Retry 001

- Member: `DEL-02-01`
- Stage: production-bound map/parity result inspection
- Candidate/project effect: none
- Cause: verifier-local harness assumed lowercase `line_start`/`line_end`
  column names for the claim-map CSV. The registered tool emits
  `SourceLineStart`/`SourceLineEnd`; the parity JSON independently uses the
  lowercase names inside its `checks` array.
- Disposition: retained the complete failed attempt under
  `retained_attempts/DEL-02-01-attempt-001/`, corrected only the verifier-local
  harness schema binding, syntax-checked it, and restarted DEL-02-01 from the
  frozen row. No candidate was repaired or rewritten.

## Retry 002

- Member: `DEL-02-01`
- Stage: deterministic checklist binding inspection
- Candidate/project effect: none
- Cause: the verifier-local harness looked for a flat
  `scope_of_work_sha256` field. The registered checklist schema binds the
  production hash at `source.sha256` and repeats it for each item at
  `items[].source_identity.sha256`.
- Disposition: retained the complete second attempt under
  `retained_attempts/DEL-02-01-attempt-002/`, corrected only this verifier-local
  schema lookup, syntax-checked the harness, and restarted from the frozen row.

## Retry 003

- Member: `DEL-02-01`
- Stage: mutated-clean parity negative
- Candidate/project effect: none
- Cause: the harness required absence of the parity report. The registered
  parity tool correctly fails with nonzero exit while deliberately retaining
  a structured report whose `pass` is false and whose `issues` record the
  production-hash mismatch. This report is failure evidence, not a successful
  output artifact.
- Disposition: retained the complete third attempt under
  `retained_attempts/DEL-02-01-attempt-003/`; the corrected gate now requires
  nonzero exit plus a retained failed parity report with issues.
