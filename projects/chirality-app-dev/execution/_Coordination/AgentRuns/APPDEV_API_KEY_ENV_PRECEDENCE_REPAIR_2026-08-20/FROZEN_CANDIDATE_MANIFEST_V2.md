# Frozen integrated candidate manifest v2

- Frozen after integrated remediation 01 terminal SUCCESS
- Branch: `codex/app-api-key-precedence-20260820`
- Basis / stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`
- Candidate paths: `94`
- Product/test paths: `4`
- Evidence/state/control paths: `90`
- Aggregate SHA-256: `eeda6c56d07326b0c30c186627d14a8319c3f8239b497b507f314724e544b788`
- Raw N3 host proof: `/tmp/chirality-precedence-closure.pXvs6Z`
- Normalized N3 harness evidence SHA-256:
  `e89bf83dc90073f775b8a80a1216b9bd68a0f4157928ddd866e6b30363c175ed`

## Exact reconstruction

Before this v2 manifest and Review 02 controls were created, the complete
tracked-plus-untracked candidate was enumerated by:

```text
{ git diff --name-only --diff-filter=ACMRTUXB; git ls-files --others --exclude-standard; } | sort -u
```

The aggregate is the SHA-256 of the newline-delimited per-file
`shasum -a 256` output in that exact 94-path order. Review 02 must exclude
only this v2 manifest and its own launch/status/return controls, reconstruct
exactly 94 paths, and match the aggregate above. The original manifest,
Review 01 controls, and remediation 01 controls are included in the 94.

## Remediation identities

- F1: 15 cited trailing blanks removed; complete 94-path scan reports zero
  whitespace findings.
- F2: DEL-09-06 REQ015 now cites compact summary for artifact/assertion/result
  binding and the TASK run record for exact host commands.
- F3: `instances/WI-PKG09-API-KEY-PRECEDENCE-01/N3_MANAGER_REGISTERED_CHECKS.json`
  records normalized PASS for `harness-pytest` (350) and
  `harness-self-check` (exit 0).
- Product/test hashes remain `d810b1ef…1444db`, `c9cadac3…17dac4`,
  `3293cbf1…ed3cb`, and `818b7424…74b1a6`.
- Compact proof hashes and raw host proof identity remain unchanged.

Review 02 covers all 94 paths and the raw host directory. This manifest and
Review 02's own controls are consistency inputs outside the frozen aggregate.
