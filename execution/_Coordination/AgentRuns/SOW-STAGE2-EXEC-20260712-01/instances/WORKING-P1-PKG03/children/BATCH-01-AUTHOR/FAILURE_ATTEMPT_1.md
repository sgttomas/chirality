# Retained harness attempt 1

- Stage: harness bootstrap, before member checkpoint 1.
- Result: failed closed with exit `127`.
- Finding class: execution substrate / helper bootstrap.
- Reason code: `HARNESS_FUNCTION_IMPORT_NOT_PERSISTED`.
- Observed stderr: helper functions `utc` and `progress` were unavailable after
  sourcing the accepted template through process substitution.
- Remediation: changed the read-only template import to evaluate the same
  frozen function prefix directly in the current Bash process.
- Candidate or project effect: none; no member conversion started and no
  project path was written.
- Rerun: required after `bash -n` succeeds.
