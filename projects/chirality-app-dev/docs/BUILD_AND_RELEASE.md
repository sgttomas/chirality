# BUILD AND RELEASE - Chirality App Dev

**Status:** Draft governance support surface
**Date:** 2026-06-13
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** local build evidence, Electron packaging evidence, instruction-root integrity, and future release-candidate review

## 1. Purpose

This guide records the current app-dev build, packaging, and release-evidence skeleton for Chirality App. It gives agents and maintainers a stable local command map for collecting software-quality evidence before any future hosted CI, signing, notarization, publication, or release-label process is selected.

This guide is not a live CI workflow, release publication authorization, lifecycle issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or external distribution approval. It does not change `frontend/package.json`, application code, package dependencies, runtime language, provider policy, tool exposure, or desktop wrapper architecture.

## 2. Authority Boundary

Build and release evidence is governed by:

- `docs/DIRECTIVE.md` for founding intent and professional-boundary posture;
- `docs/CONTRACT.md` for packaging, validation, network, SDK, and release invariants;
- `docs/VALIDATION_STRATEGY.md` for evidence classification and command routing;
- `docs/RELEASE_QUALITY_GATES.md` for release-quality gate selection;
- `frontend/package.json` for the current executable command surface;
- `frontend/docs/harness/README.md` for harness validation prerequisites and artifacts;
- git history for committed source-state identity.

If this guide disagrees with an executable script, source code, package manifest, or a higher-authority governance document, surface the discrepancy. Do not silently treat this guide as implementation truth.

## 3. Current Baseline

The current app-dev implementation is a Next.js plus Electron desktop workspace under `frontend/`. The current package manifest declares:

- Node engine: `>=20`;
- Next build command with telemetry disabled;
- Electron main-process TypeScript build;
- Vitest test suite;
- TypeScript typecheck for frontend and Electron entry surfaces;
- harness validation scripts;
- instruction-root integrity verification;
- network-policy proof;
- unsigned local macOS arm64 package and DMG commands using `electron-builder`.

The current release target remains the `docs/CONTRACT.md` K-RELEASE-1 target: macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless a governed amendment changes it.

## 4. Local Command Map

Run commands from `frontend/` unless stated otherwise.

| Command | Role |
|---|---|
| `npm run test` | Runs Vitest unit and contract tests. |
| `npm run typecheck` | Runs TypeScript checks for frontend and Electron entry surfaces. |
| `npm run harness:validate:section8` | Runs harness validation against a reachable local harness API and emits machine-readable status lines. |
| `npm run harness:validate:section9` | Runs deterministic Section 9 runtime-ID validation over targeted Vitest files and writes the stable Section 9 summary artifact. |
| `npm run harness:validate:premerge` | Runs the premerge harness validator and writes the stable summary artifact. |
| `npm run harness:validate:agentsdk-dev-turn` | Runs route-level opt-in `agentSdk` scripted dev-turn validation through the real SDK `query()` path with an offline scripted subprocess. |
| `npm run harness:validate:agentsdk-packaged-proof` | Runs a no-live packaged SDK proof from `app.asar.unpacked`, records the resolved native subprocess command, and verifies controlled `CLAUDE_CONFIG_DIR`/`HOME` propagation. |
| `npm run instruction-root:integrity` | Verifies required instruction-root resources and writes the integrity summary artifact. |
| `npm run proof:network-policy` | Runs the current network-policy proof. Add `-- --provider agentSdk --scripted-agent-sdk` for the non-packaged STAB-02(c) opt-in SDK network proof. |
| `npm run build` | Builds Next.js and Electron main-process output. |
| `npm run desktop:pack` | Builds and produces an unsigned local macOS arm64 app directory with publishing disabled, then verifies instruction-root integrity. |
| `npm run desktop:dist` | Builds and produces an unsigned/unnotarized local-builder macOS arm64 DMG with publishing disabled, then verifies instruction-root integrity. |

`npm run harness:validate:premerge` requires a running harness API. By default it targets `http://127.0.0.1:3000`; see `frontend/docs/harness/README.md` for `HARNESS_BASE_URL` and `HARNESS_PROJECT_ROOT` overrides.

## 5. Evidence Bundles

A build or release-evidence record should capture:

| Field | Required value |
|---|---|
| Source revision | Git commit hash, or explicit dirty working-tree state if evidence is pre-commit. |
| Branch and remote | Current branch and upstream target. |
| Working tree state | Clean, or list of changed files if evidence is exploratory. |
| Runtime versions | Node, npm, Electron/Next package versions where relevant. |
| Commands run | Exact command, working directory, environment overrides, pass/fail result, and duration when available. |
| Generated artifacts | Paths to summaries, build outputs, packaged app directory, DMG, or logs reviewed. |
| Validation gate | Applicable gate from `docs/RELEASE_QUALITY_GATES.md`, or explicit governance-only skip rationale. |
| Known limitations | Open risks, skipped checks, unresolved `TBD` items, and human-ruling blockers. |
| Human gate | Human ruling, waiver, or release authority record when required. |

Working-tree evidence may support review, but release-candidate evidence should bind to a committed source revision unless a human release authority records an exception.

## 6. Artifact Locations

Current known artifact locations include:

- Next build output: `frontend/.next/`;
- Electron main-process output: `frontend/dist-electron/`;
- Electron-builder output: `frontend/dist/`;
- harness validation summary: `frontend/artifacts/harness/section8/latest/summary.json`;
- harness Section 9 summary: `frontend/artifacts/harness/section9/latest/summary.json`;
- instruction-root integrity summary: `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`;
- packaged SDK resolver/HOME proof summary: `frontend/artifacts/harness/packaged-agent-sdk/latest/summary.json`;
- live harness validation output under `${TMPDIR:-/tmp}/chirality-harness-validation/latest/`.

Generated build and packaging outputs are evidence artifacts, not project truth. They do not create release publication authorization, lifecycle issuance, professional approval, certification, sealing, authentication, or code-compliance acceptance.

## 7. Suggested Local Profiles

These profiles are documentation labels, not new scripts.

| Profile | Commands | Intended use |
|---|---|---|
| Governance-only | Static checks over docs, plans, and coordination files; no frontend commands unless the tranche changes executable behavior. | Control-plane documentation tranches. |
| Runtime premerge | `npm run test`; `npm run typecheck`; `npm run harness:validate:section9`; `npm run harness:validate:premerge`; `npm run instruction-root:integrity`. | Shared runtime, API, SDK, event, permission, or harness workflow changes. |
| Network/security | Runtime premerge plus `npm run proof:network-policy`. | Network, provider, API-key, redaction, or outbound-policy changes. |
| Packaging review | `npm run build`; `npm run instruction-root:integrity`; `npm run desktop:pack` or `npm run desktop:dist` as applicable; `npm run harness:validate:agentsdk-packaged-proof` when SDK subprocess resolver or transcript/HOME posture is in scope. | Instruction-root, packaging, app metadata, SDK resolver posture, or distribution artifact changes. |
| Release-candidate dry run | Runtime premerge plus packaging review, with known limitations and human-gate state recorded. | Future release-candidate evidence only after human authorization. |

## 8. Packaging Skeleton

A packaging review should:

1. Confirm source revision and working-tree state.
2. Confirm `frontend/package.json` command and `build` configuration are the intended source of package behavior.
3. Run applicable validation gates from `docs/RELEASE_QUALITY_GATES.md`.
4. Run `npm run instruction-root:integrity`.
5. Run `npm run build`.
6. Run `npm run desktop:pack` for app-directory packaging review, or `npm run desktop:dist` for DMG review when in scope.
7. Record generated artifact paths and checksums when a release-candidate review requires them.
8. Record signing and notarization state. Current ordinary output is unsigned and unnotarized.
9. Record known limitations, skipped checks, unresolved decisions, and any human waiver or acceptance record.

No packaging review may imply that the package is published, professionally approved, externally validated, code-compliant, certified, sealed, authenticated, notarized, or suitable for reliance.

## 9. Future CI And Release Mapping

Hosted CI, public/private data handling, release matrix, signing, notarization, publication, and attestation remain future human-gated decisions. When selected, hosted workflows should call the same local command surface or a documented equivalent so local and hosted evidence remain comparable.

Hosted workflows must not receive private project data, API keys, protected professional work, SDK transcripts containing secrets, signing credentials, publishing credentials, or broader network permissions unless a recorded human decision authorizes the handling model.

## 10. Open Decisions

- Hosted CI provider, workflow location, and private-data handling.
- Supported OS/architecture release matrix beyond the current macOS 15+ Apple Silicon local-builder target.
- Signing, notarization, checksum publication, publication destination, and attestation.
- Release-label vocabulary and release-candidate evidence-bundle format.
- Coverage, performance, and platform-threshold policy.
- Concrete provider/network implementation beyond the current shipped Anthropic path.
- Any attempt to reverse the D-APP-01/D-APP-02 Pi pattern-corpus-only ruling.
