# R4.4.4 host-path executable audit

Verdict: `PASS — 24/24 HOST TOOLS EXECUTABLE — ZERO MISSING`

Authority adoption SHA-256:
`4352747755ae49e8189685874d77ca8e62f94324c37fdd875d7424956ff5063d`.
Work-graph amendment v1.14 SHA-256:
`f5ab40b4067ce19f0312d820595cd0b2f9f1cc34595d7788bbbb9592cea439b5`.

## Literal extractor method

The audit read all 93 exact main operation cells and all 87 individually
enumerated subinputs from `prepared/COMMAND_AUTHORITY_LEDGER.md`. For every
inline literal it extracted absolute executable tokens at command start,
after shell separators/pipes, after `exec`, after `find -exec`, and as the
payload executable following `/usr/bin/env -i` assignments. It did not treat
placeholders, PATH values, arguments, redirection targets, evidence/data
paths, or shell builtins as absolute executable tokens.

Each host-tool token was checked with both regular-file and executable-bit
tests on this host. The two C1114/C1117 absolute application executables are
separately classified as run-generated C1108 outputs: their absence before
packaging is required, and their post-C1108 existence/identity remains a
runbook precondition rather than a host-tool installation assertion.

## Host-tool results

| Absolute executable token | Result |
|---|---|
| `/Users/ryan/.local/share/mise/installs/node/24/bin/node` | PASS |
| `/Users/ryan/.local/share/mise/installs/node/24/bin/npm` | PASS |
| `/bin/cp` | PASS |
| `/bin/kill` | PASS |
| `/bin/ln` | PASS |
| `/bin/ls` | PASS |
| `/bin/mkdir` | PASS |
| `/bin/ps` | PASS |
| `/bin/rm` | PASS |
| `/bin/sleep` | PASS |
| `/bin/test` | PASS |
| `/bin/zsh` | PASS |
| `/usr/bin/diff` | PASS |
| `/usr/bin/ditto` | PASS |
| `/usr/bin/env` | PASS |
| `/usr/bin/find` | PASS |
| `/usr/bin/git` | PASS |
| `/usr/bin/plutil` | PASS |
| `/usr/bin/printf` | PASS |
| `/usr/bin/readlink` | PASS |
| `/usr/bin/shasum` | PASS |
| `/usr/bin/stat` | PASS |
| `/usr/bin/tee` | PASS |
| `/usr/bin/xcrun` | PASS |

Host-tool count: 24 unique; missing: 0. `/bin/printf` is absent and has zero
live ledger occurrences.

## Correctly phase-classified generated executables

| Absolute generated executable path | Producer / gate |
|---|---|
| `/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service` | produced by C1108; identity/topology checked by C1109-C1113 before C1114 |
| `/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality` | produced by C1108; identity/topology checked by C1109-C1113 before C1117 |

## Exact substitution proof

- New ledger SHA-256:
  `4989ac38d2f6e4b9bc353fdbf842a2db98c9163914f6c79f93751fd581649fa5`.
- It contains exactly 34 `/usr/bin/printf` occurrences: four in C1105-C1108
  operation cells and thirty in C1146.01-C1146.30 subinputs.
- It contains zero standalone `/bin/printf` occurrences.
- Replacing those exact 34 new strings back with `/bin/printf` in memory
  reproduces the predecessor ledger SHA-256 exactly:
  `34cdde1a1c6ee9660e7b15e20b7112b7306fc94b26758404acdc30d497da6aa6`.
- The 87-subinput LF-delimited digest changes only for the thirty C1146 inputs,
  from `d98d0bdcc52e495d8d8ac3cb80de88ce77044c9f15241f5c4180c2998196d65f`
  to `6bf71985b45520231c7a7405728280c196af2cb504ddd5b7cb9d9242fb28e683`.
- C196 and C197 newline-terminated row hashes remain
  `9fcd7d9f3b804e5706c17d372dd0977d8b4634b7bc7540c9a0b1728fd5772dfb`
  and `610b7d237e37b1532b804b00c88cd5cfd6d35453ad17cb84ad4efbde5435df52`.

This audit executes no ledger literal and makes no runtime or product claim.
