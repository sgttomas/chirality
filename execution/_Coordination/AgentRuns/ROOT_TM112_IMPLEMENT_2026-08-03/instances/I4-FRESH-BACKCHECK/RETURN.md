# I4 fresh backcheck return

Status: `PASS_WITH_NONBLOCKING_FINDINGS`

The final-hash TM-ROOT-112 candidate survives independent refutation. All
N-STOP-1..7 clauses and every bounded matrix row trace to the final code and
passing tests. M-I2-01 and M-I2-02 are closed without regression:

- later pre-force Agent-1 identity is retried after every iterator result and
  starts exactly one canonical interrupt; force expiry still forbids any late
  interrupt;
- pre-bind foreign-path refusal preserves the path and live-owner bytes;
  start-failure unlink remains enabled after an actual listener bind, while
  owner removal remains guarded by daemon/process/generation identity.

Prescribed final checks, each run once on the sealed hashes: strict full check
exit 0; I2 adversarial 2/2; canonical daemon 15/15; full runtime 74/74 across
8 files; evidence build exit 0 with 47 files / 404 KiB emitted inside I4.
Platform was Darwin 25.6.0 arm64, Node 24.18.0, Vitest 3.2.4, TypeScript 5.9.3.

No material finding exists. Nonblocking gaps are the unavailable Node 22.19
floor and the use of the installed main-checkout toolchain because this
worktree has no local runtime dependency tree. These gaps are recorded without
claiming Node 22 coverage.

Final product hashes remain:

- SPEC: `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f`
- daemon: `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2`
- tests: `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352`

Full trace, exact commands, results, scope evidence, and finding
classifications are in `BACKCHECK.md`. I4 made no product or outward workflow
write; App notice, lifecycle acceptance, Git, and human repair acceptance stay
held.
