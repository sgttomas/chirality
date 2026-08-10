# D-APP-94 Option C evidence-return contract

Status: `FROZEN CANDIDATE — DERIVATIVE RAW EVIDENCE ONLY`

The frozen driver writes bounded raw stdout, stderr, and decimal exit-status
files for host identity, Electron identity/extraction, default/search-list
prestate, isolated-HOME comparison, isolated-keychain creation/unlock/binding,
bound state, safeStorage output, prompt observation, and exact restoration.

On a fully passing route, every regular file under the fixed `evidence/` source
is copied byte-for-byte to `returned/`; every returned primary receives an
adjacent `<primary>.sha256.txt` whole-file SHA-256 sidecar. Cleanup adds and
hashes these direct-return primaries:

- `delete-keychain.stdout.txt`;
- `delete-keychain.stderr.txt`;
- `delete-keychain.exit-status.txt`;
- `probe-keychain-absence.exit-status.txt`;
- `temp-root-remove.exit-status.txt`;
- `temp-root-absence.exit-status.txt`;
- `final-status.txt`.

`final-status.txt` may contain only
`PASS_FEASIBILITY_ONLY_NO_RELIANCE`. Its presence does not create an ingestion,
product, trace, or reliance verdict. Later intake must reproduce every sidecar,
enumerate every returned primary, confirm restoration comparisons are zero,
confirm delete/root-absence statuses are zero, and retain prompt/probe outcomes
without upgrading their scope.

On failure, raw source evidence and the isolated keychain remain under the fixed
root; no successful returned package is claimed. If a partial returned directory
exists, it is immutable partial evidence and is never reused or overwritten.

No evidence object may contain a Keychain item listing, key bytes, ciphertext,
owner/provider credential, password, environment dump, or memory dump.
