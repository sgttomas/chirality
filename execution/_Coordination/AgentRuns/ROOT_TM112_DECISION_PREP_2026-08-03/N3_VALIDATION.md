# N3 validation

Verdict: `PASS`

- HEAD/origin-main exact; PR #491 merge ancestor check PASS.
- Decision-support manifest SHA-256 exact; 3/3 member hashes PASS.
- Matrix: 27 exact ordered rows, 54 options, each recommendation is a declared
  option; form recommendations match matrix exactly.
- Census: exactly four allowed tuples; recommended tuple is allowed tuple 1.
- Validation order preserved: options, tuple, package hash, signer/date.
- Forms: three; option IDs exact; all owner fields null; every return template
  retains `<ACCOUNTABLE_HUMAN_NAME>` and `<YYYY-MM-DD>` placeholders.
- Basis manifest: 22 identities; all filesystem hashes reproduce.
- Packet includes the exact fully populated recommended TM121 token and is
  marked non-authoritative/unsigned.
- Markdown/JSON/CSV read successfully; `git diff --check` PASS.
- N3 write containment: RunID only. The sole tracked worktree change remains
  the already authorized N2 Root handoff repair; no N3 tracked or foreign edit.

