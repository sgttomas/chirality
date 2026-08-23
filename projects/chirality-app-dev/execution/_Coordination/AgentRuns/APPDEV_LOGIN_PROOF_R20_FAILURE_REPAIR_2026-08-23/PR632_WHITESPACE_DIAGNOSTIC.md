# PR #632 controlling pre-repair whitespace diagnostic

- Basis: clean branch `codex/app-login-proof-r20-repair`, HEAD `85caafd4882a2ffff204ed87334171608ce462be`.
- Command, run exactly once before repair from repo root: `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`.
- Exit: `1`.
- Summary: `FAIL: candidate whitespace findings (untracked binary/symlink paths safely skipped: 0).`
- Exact flagged-file count: `12`.

## Lossless finding inventory

The validator's literal trailing U+0020 bytes are rendered below as `<SPACE>` so this governed Markdown record does not reproduce the defect. The three quoted diff lines were also reported once through `RETURN.md:23`–`25` and once directly through the raw log.

| Path relative to RunID | Finding |
| --- | --- |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md` | lines 23–25: one trailing U+0020 each in quoted raw output |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log` | lines 16–18: `   Generating static pages (6/24)<SPACE>`, `(12/24)<SPACE>`, `(18/24)<SPACE>` |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/app_hold.log` | line 660: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/corpus.log` | line 11: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/focused.log` | line 9: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/npm-test.local-socket-cure.log` | line 14: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/npm-test.sandboxed.log` | line 114: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/package_verify.log` | line 31: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/pytest.log` | line 7: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/receipt.log` | line 2: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/self_check.log` | line 90: new blank line at EOF |
| `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/typecheck.log` | line 4: new blank line at EOF |

## Frozen disposition before mutation

- Normalize only `RETURN.md` lines 23–25 by removing their one trailing U+0020 byte; no other Markdown byte changes.
- Replace each of the 11 immutable raw `.log` files with deterministic `gzip -n -9` preimages at `<name>.gz`; verify decompression reproduces the preimage byte-for-byte, then delete the raw file.
- Record exact preimage bytes/SHA-256 and postimage or gzip bytes/SHA-256 in the repair instance.
- Preserve all frontend and staged-procedure bytes exactly.
