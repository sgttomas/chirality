# D-APP-94 Option C R6 evidence-return cleanup-commit overlay

Status: `FROZEN CANDIDATE — DERIVATIVE RAW EVIDENCE ONLY`

Accepted R5 evidence contract SHA-256:
`e16e625cda1f6914b0eeb1a9197f9309c46fb3bb9998c7d8bc9ed0444a51ddd8`.
All raw evidence content, bounded-output, no-secret, no-product, and partial-
return immutability semantics remain unchanged except the authorized terminal
cleanup finalization below.

R6 copies/hashes all raw evidence before destructive cleanup, then creates and
hashes authoritative PASS commit objects `final-status.txt` and
`cleanup-commit.txt`. Their successful creation is the terminal feasibility
commit. Before that commit, every non-passing route retains the isolated
keychain and R5 root.

After commit, cleanup evidence records delete status, keychain absence, root
remove status, root absence, and `cleanup-outcome.txt`. Complete cleanup is
distinct from committed feasibility; incomplete cleanup remains a committed
PASS with retained remainder and requires owner reporting, not a retry or
reliance inference. Operational INT/TERM/HUP are ignored throughout this
post-MATCH phase.

Adjacent sidecars for commit objects are mandatory before deletion. Cleanup
sidecars are attempted after cleanup; their absence cannot turn a committed
PASS into a non-passing route. No credential, Keychain item, key, ciphertext,
environment, memory, product, or reliance evidence is added.
