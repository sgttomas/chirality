# Amendment 06 — PR #632 record-only whitespace repair

- Date: `2026-08-23`.
- Authority: exact owner direction in `CHAT_TRANSCRIPTION.md`.
- Accepted basis: branch `codex/app-login-proof-r20-repair`, exact clean HEAD `85caafd4882a2ffff204ed87334171608ce462be`, frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- First gate: run the exact candidate whitespace validator once before repair and freeze its complete diagnostic and exact file/line inventory.
- Repair convention: deterministic gzip replacement for validator-flagged immutable raw command-capture `.log` files; minimal trailing-whitespace/terminal-blank normalization only for validator-flagged governed non-raw records. Every repair records byte count, preimage SHA-256, postimage/gzip SHA-256, and exact decompression or normalization identity.
- Preserved scope: no path under `projects/chirality-app-dev/frontend/`; no package, daemon, staged R20 procedure, test, proof, or claim byte.
- Validation: full non-product pre-push gate set, including exact candidate whitespace validator against `origin/main`, receipt validator, `git diff --check`, App containment, empty index, instruction-root current-byte integrity, and frontend tree/revision identity. Prior product tests/build/package/proof are retained, not rerun.
- Review: one genuinely fresh evidence-only delegated-harness-native Agent 2 after repair and validation bytes freeze.
- Git fence: WORKING_ITEMS does not stage, commit, fetch, push, open/alter a PR, rebase, force-push, or merge. CHANGE/HELP_HUMAN owns publication after validated fan-in.
