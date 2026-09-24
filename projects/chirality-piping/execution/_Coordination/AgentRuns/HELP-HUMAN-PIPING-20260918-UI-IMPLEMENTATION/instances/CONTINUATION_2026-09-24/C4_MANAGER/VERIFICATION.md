# C4 bounded verification

ROOT subsequently activated exact locked dependency installation, normal WASM setup with `CARGO_BUILD_JOBS=2`, focused maintained tests and appropriate TypeScript checking in the isolated checkout. Native remained idle and the separate B4 browser slot was retained by its owner. This actual later grant supersedes only the initial no-setup/no-test resource limitation; it does not authorize browser/native/server/app-build work, broad tests, scope expansion or publication. The source was frozen at `0ec48a4f891de3a1a48fb967c52da75b0640a196`, with evidence head `3b36fe81b0d5becc59e062804d12515a9e410cfc` throughout these checks. ROOT's independent `/root/c4_review` was separately reviewing that frozen diff read-only.

All admitted commands passed (exit 0):

| Working directory relative to REPO_ROOT | Command | Result |
|---|---|---|
| `projects/chirality-piping` | `npm ci --offline --ignore-scripts` | Exact lock install, 206 packages added; no tracked lock/config changes |
| `projects/chirality-piping` | `CARGO_BUILD_JOBS=2 npm run build:wasm --workspace apps/desktop` | Normal operation and self-weight WASM setup completed offline; generated assets remain ignored |
| `projects/chirality-piping` | `./node_modules/.bin/tsc --noEmit -p apps/desktop/tsconfig.json` | Full desktop TypeScript check passed, no app bundle build |
| REPO_ROOT | `npm --prefix projects/chirality-piping/apps/desktop test -- src/features/viewport/labelPolicy.test.ts src/features/viewport/labelPlacement.test.ts src/features/viewport/labelCollisionIndex.test.ts` | Normal configured Vitest: 3 files, 15 tests passed |

Raw outputs and exits are preserved in `_run_records/npm-ci-offline.txt`, `wasm-setup.txt`, `typescript.txt` and `focused-vitest.txt`. `_run_records/verification-environment.json` records OS/tool versions, lock/config/setup/source identities and generated engine hashes. The normal setup loaded the real generated engine; no alternate test configuration or weakened harness was introduced. There were no failed test or setup attempts in this activation. Earlier dependency absence remains historical in readiness.txt and TASK_POLICY/RETURN.md.

All six source/test SHA-256 values still match the original frozen child output manifest. No source change, repair, generated asset commit, app build, browser/native/CUA/server/port work or broad suite ran. Tests and type checks establish only their bounded static/pure behavior; they do not establish live rendered plates, picking projection, actual DOM diagnostics, current-row publication, accessibility or performance qualification.

Fresh independent source review findings are owned by ROOT and must be combined with this execution result before readiness. UI_HANDOFF.md remains the integration scope: canvas projection/measurement/pick-target wiring, independently resolved shell current-row publication, shared mode/session controls and truthful applied diagnostics. Required connected checks, native witness, final candidate review/DEC-025 and second-profile qualification remain later obligations.
