# Dependency Projection Evidence — Cycle 02 Validation

Status: `RESTORED — PASS`

Authority: `BRIEF_AMENDMENT_01_DEPENDENCY_PROJECTION.md` plus parent-authorized
Retry 02 in `BRIEF_AMENDMENT_02_CDP_EQUIVALENT_STATE.md`.

Purpose: only the dependency-backed D-APP-86 validation commands remaining
after successful Retry-02 packaged UI observation.

## Pre-projection identity

Cycle 01 was already restored `PASS`. At this boundary:

- `runtime/node_modules` is a real directory, inode `22189023`, mode
  `drwxr-xr-x`, uid/gid `501:20`, size `96`, mtime epoch `1785698126`;
- `.vite` inode `22189024`, `.vite/vitest` inode `22189025`;
- relative recursive file aggregate
  `1061e05a417ec98bc49a5272fc970385b02dc57501f8c6b977dd27e486b446b8`;
- empty symlink aggregate
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- `git diff -- runtime` and `git status --short -- runtime` are empty;
- the exact Cycle-02 backup path
  `runtime/node_modules.dapp86-parity-validation-backup` is absent; and
- narrowly escalated read-only `lsof +D runtime/node_modules` returned exit 1
  with no output.

The manager will use only the exact Cycle-02 backup path above and the same
exact App dependency target as Cycle 01. Restoration and all identity checks
are mandatory immediately after the executor declares its last remaining
dependency-backed validation command complete.

The manager atomically renamed the preserved real object to the exact Cycle-02
backup path and created `runtime/node_modules` as a symlink exactly to
`/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/frontend/node_modules`.
The backup retained inode `22189023`; `git diff -- runtime` remained empty.

After the executor declared its last dependency-backed command complete, the
manager reran a narrowly escalated read-only holder check over the target;
`lsof +D` returned exit 1 with no output. It reverified the exact symlink,
target, backup type, and backup inode; unlinked only the exact symlink; and
atomically restored the preserved real object.

Post-restore identity exactly matches the pre-projection boundary:

- real directory inode `22189023`, mode `drwxr-xr-x`, uid/gid `501:20`, size
  `96`, mtime epoch `1785698126`;
- `.vite` inode `22189024`, `.vite/vitest` inode `22189025`, unchanged
  metadata;
- relative recursive file aggregate
  `1061e05a417ec98bc49a5272fc970385b02dc57501f8c6b977dd27e486b446b8`;
- empty symlink aggregate
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- Cycle-02 backup absent; and
- `git diff -- runtime` and `git status --short -- runtime` empty.
