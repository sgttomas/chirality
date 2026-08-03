# Command Results Digest

This digest records exact commands and outcomes without copying transient
credentials or isolated token material.

| Command | CWD | Exit / result |
|---|---|---|
| focused `npm run test -- ...` over D-APP-86 UI/runtime files | `projects/chirality-app-dev/frontend` | PASS, initially 48/48; with rollback probe 58/58 |
| `npm run typecheck` | `projects/chirality-app-dev/frontend` | PASS |
| `npm run build` | `projects/chirality-app-dev/frontend` | PASS |
| `npm run desktop:pack` | `projects/chirality-app-dev/frontend` | sandbox attempt stopped before package on `ENOTFOUND`; authorized network retry PASS, sole package |
| `npm run harness:validate:premerge` with isolated packaged-App env | `projects/chirality-app-dev/frontend` | PASS, Section 8 8/8; Section 9 16/16 report-only |
| `npm run validate:release-quality` with nested Retry-02 `tmp/` | `projects/chirality-app-dev/frontend` | FAIL: one AF_UNIX path-length `EINVAL`; all other wrapper checks PASS |
| `npm run validate:release-quality` with shortened same Retry-02 root | `projects/chirality-app-dev/frontend` | PASS; 1111 tests pass / 4 skipped; all wrapper commands PASS; no command skip |
| `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` | repository root | PASS |
| `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` | App root | PASS, v18, 8 MATCH, no drift |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py status --project app-dev` | repository root | PASS, 53 `IN_PROGRESS` |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | repository root | PASS at existing 4 REVIEW / 31 WARN baseline |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tools/practitioner_harness -q` | repository root | PASS, 349 in 15.23s |
| `node projects/chirality-app-dev/frontend/scripts/assert-harness-contract-deps.mjs` | repository root | PASS |
| source manifest `shasum -a 256 -c` | repository root | PASS, 380/380 |
| package manifest `shasum -a 256 -c` | repository root | PASS, 446/446 |
| `git diff --check` | repository root | PASS |

The exact reversible dependency projection was managed by the parent, not by
this Agent-2 instance. Both cycles restored the original real
`runtime/node_modules` directory. Final inode `22189023`, mode `drwxr-xr-x`,
uid/gid `501:20`, size `96`, mtime `1785698126`; backup absent; Root diff and
status empty.
