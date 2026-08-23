# Full-suite cure checks

Status: `CURE_PASS_PENDING_FRESH_REVIEW`

| Gate | Result |
|---|---|
| exact one `npm test`, exact cwd, local test-socket permission only | PASS |
| unrestricted cure result | PASS — exit 0; 1,267 passed / 4 skipped |
| pre/post five semantic hashes | PASS — exact equality |
| pre/post complete candidate diff | PASS — exact byte equality |
| retained sandbox diagnostic classification | preserved, not PASS — `ENVIRONMENT_SANDBOX_SOCKET_DENIAL` |
| R18/status/TM documentation | PASS — bounded authorized updates only |
| APP-HOLD `scan --require-register-match` | PASS — 53 contracts, held count 0, register match true |
| practitioner `self-check` | PASS — exit 0 at calibrated non-blocking baseline |
| practitioner pytest | not rerun; documentation mapping is unchanged and parent follow-up forbade additional tests; retained fresh-review result is 350/350 |
| prior-ledger App receipt validator | PASS; ledger unchanged |
| run-root JSON parse | PASS |
| docs and tracked `git diff --check` | PASS |
| all App untracked files staged-equivalent whitespace | PASS after output-log terminal-blank normalization |
| App-only porcelain containment | PASS |
| final run-root inventory | 78 files |
| final porcelain inventory | 85 entries, all under `projects/chirality-app-dev/` |
| empty real index | PASS |

No focused test, typecheck, second full test, pack, instruction-root,
practitioner pytest, network, source/test/package change, receipt, Git
integration, or proof action occurred after the one authorized cure command.
Fresh evidence-only review is required and must not rerun outside the sandbox.
