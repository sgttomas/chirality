# Apply, Target, and Rollback Simulation

Verdict: `PASS`.

The verifier-owned simulation starts with the exact four source hashes and
status hash. The target operation deletes the four legacy production files and
adds only clean production `ScopeOfWork.md` at SHA-256
`23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21`.
The target validates as single-format `SOW_V1`; `_STATUS.md` remains
byte-identical and `ISSUED`. The inverse removes that SOW and restores the four
exact source blobs; byte comparison against the preimage passes for all five
bound inputs. Exact operations are recorded in
`simulation/REPLACEMENT_MANIFEST.tsv` and `simulation/ROLLBACK_MANIFEST.tsv`.

This is an isolated filesystem simulation only. It is not integration,
rollback authorization, H1 approval, reissue, reauthentication, release,
reliance, or lifecycle action.
