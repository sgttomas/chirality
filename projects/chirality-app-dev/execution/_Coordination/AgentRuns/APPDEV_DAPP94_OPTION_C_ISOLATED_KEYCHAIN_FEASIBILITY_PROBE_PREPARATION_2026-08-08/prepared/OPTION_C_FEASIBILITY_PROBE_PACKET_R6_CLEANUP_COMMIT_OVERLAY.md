# D-APP-94 Option C R6 cleanup-commit packet overlay

Status: `FROZEN VERSIONED SUCCESSOR CANDIDATE — ONE FRESH VERIFIER PASS REQUIRED`

Accepted R5 packet:
`OPTION_C_FEASIBILITY_PROBE_PACKET_R5_ISOLATED_HOME.md`, SHA-256
`54341e7a1399b8b588aa25cb86aba410e9f8e45709b277c2e698cfc2d96f3027`.
All R5 pre-MATCH bytes, isolated-HOME domain boundary, owner drift/backstop
logic, failure retention, R4 disposition, probe/material scope, prompt rule,
and exclusions remain unchanged.

Repair authority adoption:
`R6_POST_MATCH_CLEANUP_REPAIR_AUTHORITY_ADOPTION.md`, SHA-256
`f14a0e311ae26044e9eac5472885909f30d4089b0999f8f6c6b89e9fd488725b`.

R6 driver:
`prepared/run-dapp94-option-c-probe-r6.zsh`, SHA-256
`8a6af3ae2049797c03af27085a26bfe539193cc2aedc4e3fc05794d339a0753c`.

## Authorized post-MATCH delta

After exact owner `MATCH` and backstop `NOT_NEEDED`, R6 ignores INT/TERM/HUP
and removes the EXIT trap before evidence copy/hash. Any copy, hash, state, or
PASS-commit failure exits before deletion; the isolated keychain and R5 root
remain retained.

Before the first destructive command, R6 writes and hashes both:

- `final-status.txt` =
  `PASS_FEASIBILITY_ONLY_NO_RELIANCE_CLEANUP_COMMITTED`;
- `cleanup-commit.txt` =
  `PASS_COMMITTED_BEFORE_DESTRUCTIVE_CLEANUP`.

Only after both immutable commit objects and sidecars exist does R6 attempt
isolated-HOME keychain deletion. Operational signals stay ignored through
delete, conditional R5-root removal, cleanup-outcome recording, sidecar
attempts, and exit.

Every post-commit route remains a passing feasibility measurement. Cleanup is
reported separately as `PASS_COMMITTED_CLEANUP_COMPLETE` or
`PASS_COMMITTED_CLEANUP_INCOMPLETE_RETAIN_REMAINDER`; incomplete cleanup does
not erase or downgrade the already committed feasibility result. R5-root
removal is attempted only when delete and isolated-keychain absence both pass.
There is no post-commit nonzero exit.

The operational namespace remains R5's previously absent root and
`returned_r5/`; changing it would exceed the byte-preservation authority. R5
candidate bytes remain immutable. No command was executed during R6 repair.
