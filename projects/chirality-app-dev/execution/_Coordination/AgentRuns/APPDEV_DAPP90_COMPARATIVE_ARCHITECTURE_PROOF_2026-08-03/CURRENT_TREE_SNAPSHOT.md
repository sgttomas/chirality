# Current App Tree Snapshot

Snapshot kind: `DERIVATIVE — CURRENT WORKING BYTES`

Base commit: `7249281e1f84ba5abee3c31c2fea3736b22000d3`

The source/config files named in `BASIS_MANIFEST.csv` were hashed from the
current App worktree after D-APP-89's accepted migration bytes were present.
They are not represented as committed-main source bytes. This distinction is
intentional: D-APP-90 asks for maps over the current App tree, while its Piping
prerequisite separately requires committed-main bytes.

## Mechanical inventory

Commands used:

```text
find frontend/<area> -type f \( -name '*.ts' -o -name '*.tsx' -o -name '*.mjs' -o -name '*.json' -o -name '*.css' \)
find frontend/src frontend/electron -type f \( -name '*.ts' -o -name '*.tsx' \) ! -path '*/__tests__/*'
find frontend/src/__tests__ -type f \( -name '*.ts' -o -name '*.tsx' \)
```

| Area | Counted files | Counted lines | Interpretation |
|---|---:|---:|---|
| `src/app` | 27 | 4,676 | one Next app-router graph, including 22 page/API-route entry files |
| `src/components` | 41 | 9,075 | shared UI composition; 32 files are under `shell/` plus `woven-dialogue/` |
| `src/lib` | 88 | 25,379 | shared client, harness, shell, workspace, pipeline, and Woven logic |
| `electron` | 13 | 3,204 | one Electron process/preload graph |
| `scripts` | 22 | 7,726 | one current build/package/validation tool surface |
| `packages` | 14 | 58 | one retained compatibility-facade workspace and metadata; D-APP-89 migration accepted, facade not retired |

Additional exact counts:

- 169 non-test TypeScript/TSX files across `src/` and `electron/`;
- 146 TypeScript/TSX files under `src/__tests__/`;
- 22 `page.tsx`/`route.ts` App Router entry files;
- 32 shell/Woven component files; and
- 4 workspace-provider component files.

A broader architecture corpus of 181 TypeScript/TSX files across `src/app`,
`src/components`, `src/lib`, `electron`, and the retained facade's `src`, plus
four root config files (`package.json`, `next.config.mjs`, `tsconfig.json`, and
`tsconfig.electron.json`), totals 185 files. The ordered `(file SHA-256, path)`
fingerprint was independently reproduced as:

`ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4`.

The contemporaneous `git status --porcelain -- frontend` digest was:

`000738ad4b88597c0dc0c5639fd74071c6219d3e530f1dda437f64fa57bdb3c9`.

## Present load-bearing topology

```text
package.json (one workspace + one electron-builder manifest)
  -> next.config.mjs (one renderer build)
  -> scripts/build-electron.mjs
       -> electron/main.ts (one process entry)
       -> electron/preload.ts (one preload entry)
       -> runtime CLI entry
  -> src/app/layout.tsx (one global provider stack)
       -> RuntimeConnectivityProvider
       -> WorkspaceProvider
       -> DeliverablesProvider
       -> ToolkitProvider
       -> HarnessEventsProvider
  -> src/app/page.tsx
       -> WovenDialogueRoute
            -> WovenDialogueShell
            -> legacy PortalLoopShell
```

`domain-profile-registry.ts` contains closed runtime-engine registrations. It
does not define target name, resources, navigation, shell slots, build profile,
bundle identity, or data-root policy, so it cannot be reused as product-profile
authority without a later ruling.

## Source limitations

- Generated `.next/`, `dist/`, `dist-electron/`, `dist-runtime/`, and
  `node_modules/` were excluded from architecture counts.
- Counts are descriptive current-tree evidence, not implementation estimates
  by themselves.
- No build, package, source edit, or dependency install was performed.
