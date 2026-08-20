# D-APP-100 packaged-daemon instruction root — 2026-08-19

Run: `execution/_Coordination/AgentRuns/APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19/`

The packaged daemon now resolves `CHIRALITY_INSTRUCTION_ROOT` through the
authorized project registry/manifest and uses packaged resources only when no
registered manifest root resolves. Success and classified fallback are written
to the durable daemon log. The regression binds Desktop/app and CLI to the same
registered project and proves the daemon chooses that manifest root.

Validation: focused D-APP-100 suite 12/12; full Vitest 1139 pass with four
existing skips; typecheck, production build, Section 9, unsigned `desktop:pack`,
packaged dependency boundary, and instruction-root integrity pass; release
quality `pass_with_skips` because the registered premerge owned service reached
Next but the absent local runtime-daemon project binding returned HTTP 503 (PR
CI owes that row). The packaged isolation proof passed all nine checks with no
ambient instruction-root override, global Node, distribution signature, or
repository cwd. Fresh read-only review 05 returned PASS with no findings.

The exact D-APP-100 Remaining item is removed. Other Remaining scope,
`IN_PROGRESS`, Checking Approval SHA, and all release/signing/notarization/
distribution fences are unchanged.
