# Checks and evidence lineage — PR #632 UID portability implementation

| Check | Result |
| --- | --- |
| APP-HOLD dispatch | PASS: `ALLOW`; DEL-09-04 `CLEAR` / `NOT_HELD` |
| Ordinary focused suite | PASS: `1` file; `72/72` tests |
| `umask 0002` focused suite | PASS: `1` file; `72/72` tests |
| Exact full local-socket suite | PASS: `155` files passed, `1` skipped; `1,282` tests passed, `4` skipped |
| Typecheck | PASS |
| Unchanged proof-script syntax | PASS |
| Static whole-file inventory | PASS |
| Immutable R19 fixture | PASS: `3,049` bytes / `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` |
| Immutable product script | PASS: `56,144` bytes / `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306` |

Complete invocations and outputs are preserved in `COMMAND_OUTPUTS.md`. The short outputs did not require binary log compression; this Markdown is the lossless textual evidence record, including exact aggregate counts, timings, and the full APP-HOLD JSON.

The exact `git diff --check`, App/frontend containment, index, and terminal candidate-whitespace commands are reserved until after all instance records are frozen. Their results will be returned out of band; no evidence byte will be changed afterward.

No retry occurred. No ordinary-sandbox full-suite diagnostic, supply, build, package, daemon, preflight, proof, GUI, launchctl, operator/private-root/Desktop, network, or Git mutation was performed.
