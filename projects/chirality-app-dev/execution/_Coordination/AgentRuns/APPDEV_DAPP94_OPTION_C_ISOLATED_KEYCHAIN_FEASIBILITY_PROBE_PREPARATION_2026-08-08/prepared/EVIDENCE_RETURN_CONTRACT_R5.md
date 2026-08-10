# D-APP-94 Option C R5 evidence-return contract

Status: `FROZEN CANDIDATE — DERIVATIVE RAW EVIDENCE ONLY`

Raw R5 evidence records host/Electron identity, owner prestate, isolated-HOME
initial tuple, isolated create/unlock/bind/observations, probe/prompt output,
owner after-check, byte-comparison statuses, drift verdict, backstop action,
terminal status, and applicable cleanup statuses. Every command tuple retains
whole stdout, stderr, and decimal exit-status files.

On a passing route every raw evidence primary is copied byte-for-byte to the
previously absent `returned_r5/` and receives an adjacent whole-file SHA-256
sidecar before any deletion. Cleanup then adds and hashes:

- `delete-isolated-keychain.stdout.txt`;
- `delete-isolated-keychain.stderr.txt`;
- `delete-isolated-keychain.exit-status.txt`;
- `isolated-keychain-absence.exit-status.txt`;
- `r5-temp-root-remove.exit-status.txt`;
- `r5-temp-root-absence.exit-status.txt`;
- `final-status.txt`.

Passing evidence must show owner pre/post baseline matches,
`OWNER_STATE_MATCH_NO_BACKSTOP_WRITE`, backstop `NOT_NEEDED`, prompt `NONE`,
and the expected bare-Electron feasibility booleans. Any failure, cancellation,
observation error, proven drift, or backstop action retains the R5 root and
does not claim a passing return. A partial `returned_r5/` is immutable and not
reused.

No object may contain a Keychain item listing, key bytes, ciphertext,
credential, password, environment dump, memory dump, product evidence, or
reliance claim.
