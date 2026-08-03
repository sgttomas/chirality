# Dependency Projection Evidence

Status: `RESTORED — PASS`

Authority: `BRIEF_AMENDMENT_01_DEPENDENCY_PROJECTION.md`

The frozen identity and precondition evidence is recorded in the amendment.

The manager verified the backup path absent, the live path a real directory
with inode `22189023`, and the target a real materialized directory. It then
atomically renamed the preserved object to
`runtime/node_modules.dapp86-parity-backup` and created
`runtime/node_modules` as a symlink exactly to
`/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/frontend/node_modules`.
The backup retained inode `22189023`. `git diff -- runtime` remained empty;
`git status --short -- runtime` reported only the two expected transient
untracked paths. No Root source, manifest, lock, or dependency install was
performed.

After the executor declared its last dependency-backed command complete, the
manager reran a narrowly escalated read-only holder check over the projection
target; `lsof +D` returned exit 1 with no output. The manager then reverified
the symlink and target, unlinked only the exact symlink, and atomically renamed
the preserved real object back to `runtime/node_modules`.

Post-restore results match the frozen pre-projection identity exactly:

- live path is a real directory, inode `22189023`, mode `drwxr-xr-x`, uid/gid
  `501:20`, size `96`, mtime epoch `1785698126`;
- `.vite` inode `22189024` and `.vite/vitest` inode `22189025` retain their
  frozen metadata;
- the relative-path recursive file aggregate is
  `1061e05a417ec98bc49a5272fc970385b02dc57501f8c6b977dd27e486b446b8`;
- the symlink aggregate is
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- the backup path is absent; and
- `git diff -- runtime` and `git status --short -- runtime` are empty.

One intermediate aggregate printed after restoration used absolute pathnames
and therefore differed because `shasum` includes the pathname in its aggregate
input. Recomputing with the same relative-path command as the frozen boundary
returned the exact frozen aggregate above. No file-content discrepancy exists.
