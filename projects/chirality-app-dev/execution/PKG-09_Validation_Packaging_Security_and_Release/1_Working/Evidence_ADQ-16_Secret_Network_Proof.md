# Evidence: ADQ-16 Secret Scan and Network Proof

## Scope

This record closes the eligible ADQ-16 evidence slice: whole-product secret scan and network-policy
proof evidence. It does not authorize release-readiness, signing, notarization, publication, external
distribution, lifecycle issuance, professional approval, certification, sealing, authentication,
code-compliance acceptance, provider expansion, remote MCP, plugins, or non-Anthropic network paths.

## Source State

| Field | Value |
|---|---|
| Branch | `codex/fuwenc-24554` |
| Base revision before ADQ-16 edits | `2e98d998f33d4184cbd399cba392054f537e351b` |
| Working tree before ADQ-16 | Clean and synced with `origin/codex/fuwenc-24554` |
| Runtime versions | Node `v24.5.0`; npm `11.5.2` |

## Implemented Evidence Command

ADQ-16 added `npm run proof:secret-scan`, implemented by
`frontend/scripts/scan-secret-evidence.mjs`. The scanner covers git-tracked app-dev files plus
generated `frontend/artifacts/harness/` evidence files, skips non-text/build directories, detects
environment-secret exact matches, Anthropic-key-shaped tokens, and URL credentials, and writes only
hash/length metadata for findings. Raw secret values are not written to the summary.

The first scanner run found one blocked URL-credential fixture in
`frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`. The scanner was corrected to
classify credential-bearing URLs under test paths as allowed fixtures while still blocking them
elsewhere.

## Commands And Results

| Command | Cwd | Result | Evidence |
|---|---|---|---|
| `npm run proof:secret-scan` | `frontend/` | Pass after fixture-classifier correction | `frontend/artifacts/harness/security/latest/secret-scan-summary.json` |
| `npm run proof:network-policy -- --runs 1 --idle-seconds 5 --idle-sample-seconds 5 --provider agentSdk --scripted-agent-sdk --output-dir artifacts/harness/network-policy/adq16-2026-06-21` | `frontend/` | Pass | `frontend/artifacts/harness/network-policy/adq16-2026-06-21/summary.json` |
| `npm run proof:secret-scan` | `frontend/` | Pass after network proof artifacts were generated | `frontend/artifacts/harness/security/latest/secret-scan-summary.json` |
| `npm run test -- src/__tests__/scripts/build-network-policy.test.ts --testTimeout=15000` | `frontend/` | Pass | 1 file / 5 tests passed. |
| `npm run typecheck` | `frontend/` | Pass | TypeScript checks passed for frontend and Electron entry surfaces. |
| `npm run test -- --testTimeout=15000` | `frontend/` | Pass | 76 files / 521 tests passed. |

Port 3000 was clear before the network proof and clear after the proof completed.

## Secret Scan Summary

| Field | Result |
|---|---|
| Status | `pass` |
| Scanned files | `1734` |
| Skipped files | `14` |
| Git-tracked files in candidate set | `1722` |
| Generated artifact files in candidate set | `26` |
| `ANTHROPIC_API_KEY` in scanner environment | Not present |
| `CHIRALITY_ANTHROPIC_API_KEY` in scanner environment | Not present |
| Blocked findings | `0` |
| Allowed fixture findings | `10` |
| Raw secret values written | `false` |

Allowed fixture findings are test or placeholder values; blocked findings would include exact
environment secret values, high-confidence non-fixture Anthropic key tokens, or URL credentials outside
test fixtures.

## Network Proof Summary

| Field | Result |
|---|---|
| Run count | `1` |
| Provider mode | `agentSdk` |
| Scripted Agent SDK subprocess | `yes` |
| Idle window | `5` seconds |
| Aggregate verdict | `PASS` |
| Failed runs | `0` |
| Scenario completed | `true` |
| Blocked renderer diagnostics observed | `1` |
| Network probe payloads observed | `1` |
| Non-allowlisted endpoints | `0` |

The proof was scripted/offline for the Agent SDK path and did not expand provider policy. The proof
summary retains the existing `CONF-002` caveat: OCSP/CRL carve-out wording remains unresolved, and the
summary reports explicit non-allowlisted TCP endpoints plus renderer policy diagnostics.

## Skips And Boundaries

- The network proof used one scripted run with a 5-second idle window, not the script defaults of
  three 600-second runs. This ADQ-16 tranche records bounded current evidence, not a release-readiness
  claim.
- `npm run harness:validate:premerge`, `npm run desktop:dist`, and live packaged SDK read-tool proof
  were not rerun in ADQ-16; ADQ-14 and ADQ-15 own the current runtime-wrapper and packaging evidence.
- `npm run build` was not rerun in ADQ-16 because this tranche changed the validation script surface,
  docs, and evidence records, not app runtime, Electron wrapper, or packaged resources.
- No `_STATUS.md`, dependency row, authority document, lifecycle state, signing/notarization,
  publication, external distribution, provider/network expansion, release-readiness, professional
  approval, certification, sealing, authentication, or code-compliance claim changed.
