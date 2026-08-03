# Brief Amendment 01 — Reversible Dependency Projection

Date: `2026-08-03`

Status: `AUTHORIZED BY APP HELP_HUMAN PARENT — ENVIRONMENT ONLY`

Applies to: `A2-PARITY-EXECUTOR-01/LAUNCH_BRIEF.md`

## Trigger

The executor's six focused suites passed 48/48, but App Vite could not resolve
Root `@chirality/runtime-contracts` from the Root runtime-client because the
real repo-root `runtime/node_modules` is a `.vite`-only cache. This reproduces
the exact environment substrate encountered and reversibly handled in the
accepted D-APP-89 run. It is not evidence of an App source defect.

## Parent authorization

The App `HELP_HUMAN` parent directed the WORKING_ITEMS manager to version the
brief and establish only the exact D-APP-89-style reversible ignored
dependency projection needed for D-APP-86, with before/after identity gates
and zero Root tracked diff. No Root source, manifest, lock, dependency install,
owner-daemon, or generic runtime work is authorized.

## Frozen pre-projection identity

At the amendment boundary `runtime/node_modules` was a real directory:

- inode `22189023`, mode `drwxr-xr-x`, uid/gid `501:20`, size `96`, mtime
  epoch `1785698126`;
- `.vite` inode `22189024` and `.vite/vitest` inode `22189025`, with the same
  mode, uid/gid, size, and mtime epoch;
- recursive file aggregate
  `1061e05a417ec98bc49a5272fc970385b02dc57501f8c6b977dd27e486b446b8`;
- empty symlink aggregate
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- exact descendants: `.vite/vitest/da39a3ee5e6b4b0d3255bfef95601890afd80709/results.json` and its parent directories;
- `git diff -- runtime` and `git status --short -- runtime`: empty;
- narrowly escalated read-only `lsof +D` returned exit 1 with no output,
  meaning no open file was reported under the object at the check boundary.

## Exact amendment

The manager may:

1. require the backup path
   `runtime/node_modules.dapp86-parity-backup` to be absent;
2. atomically rename the real directory to that exact backup path;
3. create `runtime/node_modules` as a symlink exactly to
   `/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/frontend/node_modules`;
4. permit the executor to run the already sealed D-APP-86 instrument and
   validations while this projection is active; and
5. immediately after the executor's dependency-backed commands finish,
   reverify the exact symlink target, unlink only that symlink, atomically
   rename the preserved real directory back, and prove every frozen identity
   value plus zero Root tracked diff.

Any failed type/target/backup/holder/identity/precondition check stops the run
as `BLOCKED/PARTIAL`. The executor may not mutate this projection itself and
all other brief constraints remain unchanged.
