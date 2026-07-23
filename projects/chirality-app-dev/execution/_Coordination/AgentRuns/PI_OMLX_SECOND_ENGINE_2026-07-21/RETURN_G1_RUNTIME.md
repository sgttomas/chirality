# Return — G1 Desktop Runtime Prerequisite

- **RunID:** `PI_OMLX_SECOND_ENGINE_2026-07-21`
- **Node:** `G1_RUNTIME_PREREQUISITE`
- **Verdict:** `PASS_WITH_RECORDED_RESIDUALS`
- **Actual model:** `gpt-5.6-sol` (no substitution)
- **Authority:** `D-APP-72`, `SCA-APP-002`, and recorded G0 independent authority-audit PASS

## Changed paths

- `.github/workflows/harness-premerge.yml`
- `projects/chirality-app-dev/frontend/package.json`
- `projects/chirality-app-dev/frontend/package-lock.json`
- `projects/chirality-app-dev/frontend/docs/harness/README.md`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/dmg-packaging-policy.test.ts`
- this return

No Electron source compatibility repair was required. No Pi package, provider behavior, credential behavior, or network-policy expansion was added.

## Resolved runtime

- Host Node: `24.18.0`
- Host npm: `11.16.0`
- Electron: exact `43.1.1`
- Electron embedded Node: `24.18.0`
- electron-builder: exact `26.15.3`
- `@types/node`: exact `24.12.4`
- Project Node floor: `>=22.19.0`
- Active premerge CI Node: `24`
- Pi dependency scan: absent

The Electron binary was explicitly primed after install and both its Electron and embedded-Node versions were observed. The npm 11 lock regeneration also refreshed transitive resolutions permitted by existing caret ranges; for example, Next resolved from `14.2.33` to `14.2.35` without a direct manifest change.

## Validation

| Check | Result | Evidence |
|---|---|---|
| Exact root manifest/lock assertions | PASS | all approved versions and Node floor exact; Pi absent |
| Focused Electron/package policy tests | PASS | 4 files, 22 tests |
| Full typecheck | PASS | renderer and Electron TypeScript configurations |
| Full Vitest suite | PASS | 98 files passed, 1 skipped; 780 tests passed, 4 skipped |
| Production build | PASS | Next `14.2.35`; 23 routes/pages generated; Electron TypeScript build passed |
| `desktop:pack` | PASS after network approval | Electron 43.1.1 arm64 unsigned directory bundle created by builder 26.15.3 |
| Instruction-root integrity | PASS | 43 files checked; no missing, mismatched, or unexpected bundled files |
| Packaged Claude SDK resolver proof | PASS | scripted no-provider proof resolved the arm64 Claude command below `app.asar.unpacked` |
| Packaged app startup | PASS | app remained running; packaged Next listener observed only on `127.0.0.1` |
| Packaged app shutdown | PASS | process and loopback listener absent after controlled termination |
| Scripted renderer network-policy smoke | PASS | 1 run, 1-second idle, Agent SDK scripted mode; evidence written outside the repository at `/private/tmp/chirality-g1-network-policy` |
| Scoped diff whitespace check | PASS | `git diff --check` clean for all G1 source paths |

The first sandboxed `desktop:pack` attempt reached packaging and failed only with `getaddrinfo ENOTFOUND github.com`. The same command passed after scoped network approval downloaded the approved Electron payload.

## Packaging observations

- Bundle: `frontend/dist/mac-arm64/Chirality.app`
- Renderer server bound to an ephemeral `127.0.0.1` port; no non-loopback listener was observed.
- Claude executable resolved to `Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64/claude`.
- Builder reported no signing identity because `CSC_IDENTITY_AUTO_DISCOVERY=false`, as required; no signing, notarization, release, or distribution action occurred.
- Builder retained the default Electron icon; this is unchanged product behavior.
- Startup emitted Node deprecation `DEP0180` (`fs.Stats` constructor). Startup and shutdown still passed; no G1-scoped source call site was identified.

## Residuals and explicit non-actions

- `npm install` reported 20 advisories total. `npm audit --omit=dev` reported 8 production-tree advisories: 1 low, 4 moderate, and 3 high, principally through existing Next and Claude/MCP dependency trees. Suggested complete remedies include breaking Next or Claude SDK changes and were not applied in this bounded runtime prerequisite.
- npm 11 reported unapproved lifecycle scripts for `esbuild@0.21.5`, `fsevents@2.3.3`, and `electron-winstaller@5.4.0`. No approval was granted; typecheck, tests, production build, arm64 packaging, and runtime smoke all passed without it.
- Instruction-root `status` is `pass`. Its separate source-completeness advisory remains `needs_remediation` because root `examples/` is absent; bundle comparison itself had zero missing or mismatched files. This is pre-existing and outside G1.
- The disabled desktop release template still references Node 20, builder 25.1.8, and stale paths. It was not changed because it is inactive and outside the enumerated G1 write scope; it must be repaired before activation.
- No live Anthropic request was made. Claude and stub regressions are covered by the full offline test suite and packaged scripted resolver proof.

## Fan-in statement

The G1 prerequisite gate is satisfied: exact Electron 43.1.1 / Node 24 tooling is installed, compiled, packaged, and smoke-tested without a required Electron source change, and existing Claude/stub behavior remains green under the available offline validation suite. G2 may consume the provider-neutral contract surfaces after the integration owner accepts these recorded residuals.
