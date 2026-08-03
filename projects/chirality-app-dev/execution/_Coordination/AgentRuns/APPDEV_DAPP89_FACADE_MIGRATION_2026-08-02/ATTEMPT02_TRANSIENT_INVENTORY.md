# D-APP-89 Option B — Attempt 02 transient inventory

Status: `INVENTORIED — RETAINED FOR AUTHORIZED LATER LANES`

Date: `2026-08-02`

The exact repository commands produced or refreshed ignored build, test, and
packaging output. Nothing in this inventory is an authoritative snapshot or a
tracked implementation change.

| Path | Post-run size | Treatment |
|---|---:|---|
| `projects/chirality-app-dev/frontend/.next/` | 196M | retained; ignored Next build output |
| `projects/chirality-app-dev/frontend/dist-electron/` | 3.7M | retained; ignored Electron bundle |
| `projects/chirality-app-dev/frontend/dist-runtime/` | 260K | retained; ignored runtime CLI bundle |
| `projects/chirality-app-dev/frontend/dist/mac-arm64/` | 1.1G parent tree | retained; ignored `--dir` packaging output |
| `projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/` | 32K | retained; ignored integrity output |
| `runtime/packages/*/dist/` | 1.6M aggregate (approximately) | retained; ignored Root build output |

The App dependency tree itself remains present for later authorized lanes:

- directory inode/metadata unchanged:
  `23346623 drwxr-xr-x 501:20 size 15200 mtime 1785734623`;
- counts unchanged: 59,536 files, 66 links, 5,475 directories;
- symlink aggregate unchanged:
  `721e2d6944b31d7ed97d06c4304a493b748f241d67b16c1f4b0be2bd016797b7`;
- both lock hashes remain exact as recorded in
  `ATTEMPT02_COMMAND_RESULTS.md`.

The App file-tree aggregate changed from
`e0a36dbabdf1b3bbc4725d7c1ddc1c522e6795c860071d55a4493612d95ce29d`
immediately before Amendment 04 to
`fe5b596555020e90310cd9ec41e6f382f2596e1fcb80a10c6d33a30265762be9`
after it. The only file with a modification time during the sequence was the
Vitest command cache
`frontend/node_modules/.vite/vitest/da39a3ee5e6b4b0d3255bfef95601890afd80709/results.json`,
whose post-run SHA-256 is
`62aa3661974c0b8cd465bac2c6eefb7e1855d9f815692264c8311d6bd2bc09dc`.
It is a command-produced ignored cache file, not a dependency or lock change.

No generated output or cache was deleted because the brief requires the
parent-materialized App tree to remain available and forbids cache
manipulation. `git status --ignored` confirms these paths are ignored; none
appears as a tracked or untracked product-source change.
