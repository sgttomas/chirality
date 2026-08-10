# D-APP-94 Option C R2 restoration-guard fresh verifier return

Verdict: `BLOCK_DAPP94_OPTION_C_R2_RESTORATION_GUARD`

Role: exactly one new genuinely fresh read-only ephemeral Agent 2 verifier.
Candidate execution: none.
Repair or delegation: none.

## Findings

1. **PASS — frozen authority and predecessor preservation.** The repair
   authority is captured verbatim. The predecessor freeze, predecessor BLOCK
   return, predecessor driver, all predecessor-bound objects, Electron archive
   and executable-member identity, and `security(1)` manual identity matched
   their frozen SHA-256 values on the initial and final checks.
2. **PASS — authorized textual delta.** The predecessor/R2 driver diff is
   confined to replacing `RESTORING` with `RESTORE_STATE`, adding signal-trap
   arming, and wiring the restoration/trap guard. All non-guard commands,
   operands, order, evidence names, fixed namespaces, routes, cleanup, and
   exclusions remain identical.
3. **PASS — single-entry and no-retry state gating.** Only `NOT_STARTED` can
   enter restoration commands. `IN_PROGRESS` and `FAILED` reject entry, while
   `SUCCEEDED` returns success without commands. Ordinary restoration failure
   publishes `FAILED` before returning, so the following EXIT trap cannot
   retry; trap-initiated success or failure likewise cannot retry.
4. **BLOCK — active-restoration signal exclusion is not continuous.** In
   `restore_owner_state`, the R2 driver executes
   `RESTORE_STATE=IN_PROGRESS` and only in the following shell command executes
   `trap '' INT TERM HUP`. An `INT`, `TERM`, or `HUP` handled between those two
   commands sees `IN_PROGRESS`; `fail_closed_trap` therefore does not restore,
   and its operational signal handler exits the shell. The shell can thus be
   interrupted while the published restoration state is `IN_PROGRESS`, before
   the first restoration command, leaving the owner-domain mutation
   unrestored. This directly fails the sealed requirement that such signals
   cannot interrupt the shell at any time while restoration is in progress.
5. **BLOCK — trap-initiated entry has the same sequencing exposure.** Before
   calling `restore_owner_state`, `fail_closed_trap` resets EXIT/INT/TERM/HUP
   dispositions with `trap -`. Until the callee later reaches its ignore-trap
   command, a further operational signal can terminate the shell before
   restoration ownership is safely established. This is the same smallest
   guard-ordering defect, not a separate scope issue.
6. **PASS — terminal publication and retention.** On the paths that reach the
   terminal branch, success publishes `RESTORED=1` and `SUCCEEDED` before
   re-arming operational traps and before evidence copy/deletion. Failure
   publishes `FAILED`, retains the isolated keychain, fixed root, and evidence,
   performs no cleanup, and the ordinary failure path exits `90`.
7. **PASS — static identity checks.** The R2 driver parses under
   `/bin/zsh -n`. The common preamble digest is
   `65b00c309d0542b8214c28c5461c008dc3479284f3ec954e3ea12e655b581e90`;
   the unchanged body from `fail_before_mutation()` through EOF is
   `a7d6071208a765a63e66dbfd4de4c196dba0bd8b1732a89b2f232e68899d4e5a`;
   and the ordered restoration security/cmp command digest is
   `1be58214f86fce0cdcf2fd78cb9b9b74f99ef51d94d0e8fea0eaf5f0be9e57a3`
   for both predecessor and R2.
8. **PASS — overlay scope; BLOCK — safety claim.** The packet overlay,
   validation, freeze, and R2 token mechanically bind the successor driver
   path/hash and preserve the predecessor scope and authority boundary. Their
   claim that signals are ignored for the complete active restoration is not
   accurate because of the command-boundary window above.
9. **BLOCK — future token remains withheld.** The exact R2 token remains
   unapproved and is not presentable under this verdict. It grants no hidden
   execution authority.

## Smallest material blocker

Signal-ignore disposition is established after, rather than before, publishing
`RESTORE_STATE=IN_PROGRESS`. The resulting command-boundary race permits a
signal handler to exit the shell during active restoration without performing
or completing owner-state restoration. `NOT_STARTED` gating closes all
double-restoration paths, and terminal-state-before-re-arm closes later retry
paths, but neither closes this interruption window. The original no-second-
restoration defect is therefore replaced by a material fail-closed restoration
continuity defect. No repair or second verifier is requested or performed.

## Final freeze stability

- R2 manager freeze:
  `5ab689e62c4e92074a8989a9de4ddfc7224aebcf55a4fe14704f463b89e4aecb`;
- R2 driver:
  `42d4206281afc0939f41c1bb03082162e4f3d978be8013e2edb37bb899f6a835`;
- R2 overlay:
  `4472af19a4f7b9433052e21bb7efca747cdbc42a58c5d9f9678e330da1a82a8f`;
- withheld R2 token:
  `98e80432dc61e11aa41fe39be810faf2dcb42d315e175812edf6f3a192144c05`;
- R2 validation:
  `8ca8d18e44f799d43e2af60daf8e054ab312edc163bfaf73cee6c37334758392`.

All remained byte-stable through the final pre-return check.
