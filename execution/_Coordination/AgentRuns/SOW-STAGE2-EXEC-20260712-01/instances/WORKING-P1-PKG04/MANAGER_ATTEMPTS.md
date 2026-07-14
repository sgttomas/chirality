# Manager Attempts and Remediations

| Attempt | Layer | Result | Class | Reason code | Disposition |
|---:|---|---|---|---|---|
| 1 | preflight ad-hoc reader | FAIL | mechanical | `EXPECTED_BINDING_HEADER_CASE` | Corrected field names from assumed title case to the actual lower-case TSV schema; no output was accepted. |
| 2 | frozen preflight reproduction | PASS | none | `NONE` | Accepted for child dispatch. |
| 3 | manager author-manifest rebind | FAIL | mechanical | `SHELL_INTERPRETER_MISMATCH` | Invoked Bash finalizers through zsh, triggering zsh's reserved `path` variable and loss of command lookup; no candidate/project effect. Reran with Bash. |
| 4 | manager author-manifest rebind | PASS | mechanical repair | `RETAIN_NORMALIZATION_LEDGER` | Reconstructed the 6- and 10-row normalization ledgers from live-vs-derivative byte proofs after the generic finalizer cleared them, then rebuilt and verified both self-excluding manifests and rebound parent acceptances. |
