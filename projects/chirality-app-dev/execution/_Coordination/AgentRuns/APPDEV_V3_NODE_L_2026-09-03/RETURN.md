# RETURN — L1_IMPLEMENTER (frozen for independent review)

- **Status:** `REVIEW_READY`
- **Basis:** `fe0ce926d4475fa41cb91933ad1218b95083889b` (`origin/main`, PR #690 merge)
- **Branch:** `codex/app-v3-nodeL-consent-fake-guards-2026-09-03`
- **Content/evidence commit:** `7a2c336b8c46b905bcf1f5cfbf76409c987123a5`; this return lands in a record-only commit on top, whose SHA is reported to HELP_HUMAN as the review freeze. Nothing is pushed.
- **Executor attribution:** provider `OpenAI`; engine `Codex`; model `GPT-5 family (exact model identifier not exposed to the agent runtime)`; bounded ephemeral Agent 2 using `software-bounded-implementation`; no delegation.
- **Diff at content commit:** 8 files changed, 371 insertions, 4 deletions. Product/test bytes are confined to the fake port and its focused test; the other six files are Node L records/evidence.

## Implemented behavior

- **F2:** `resolveNetworkPrompt` now rejects unless consent is `granted`. When a granted consent becomes stale, the fake resets command networking to `off` and clears any pending prompt and session-accepted destinations.
- **F3:** a successful fresh grant after revocation restores the new generation's root-private home from `invalidated` to `present`, keeping `ambientCodexRead: false`.
- **F4:** `control.enqueueNetworkPrompt` ignores requests unless the selected posture is `askPerDestination`.
- Added one focused test per fix. The existing new-generation test's pinned expectation now agrees with the repaired private-home state.

## Decision latitude

D-APP-60/D-APP-64 latitude selected the fail-closed F2 posture reset. A stale consent cannot be reused, so preserving `on`, a pending prompt, or prior session acceptance in the fake would expose a misleading state to future live-adapter comparison. Rejected alternative: retain the selected posture and only guard prompt resolution; that would require a deliberate stale-plus-on fixture and leave session/posture state semantically active-looking despite invalid consent.

F3 deliberately changes only fake consistency. It does not decide whether real private-home invalidation logs out an account; the fake retains its signed-in account posture and recreates the home on a fresh grant. Root-owned configuration-digest semantics are untouched.

## Check results

| Check | Result |
|---|---|
| Runtime dependency build (`npm ci`, `npm run build`) | PASS |
| Frontend dependency install | PASS after the sandbox DNS-denied attempt was rerun with approved network access |
| Focused consent Vitest (3 files) | PASS — 68 tests |
| Registered full frontend Vitest | PASS — 165 files passed, 1 skipped; 1561 tests passed, 4 skipped |
| Frontend typecheck | PASS |
| APP-HOLD dispatch preflight / integrity | ALLOW / PASS |
| Harness self-check | PASS — unchanged baseline |
| Practitioner harness pytest | PASS — 350 tests |
| `git diff --check` | PASS |
| Exact change-scope validation | PASS — no violations |
| Authority corpus | PASS — v20, no drift |
| Receipt validator | PASS — ledger unchanged |
| JSON structure (`WORK_GRAPH.json`, registered-check evidence) | PASS |

The first unsandboxed full-suite attempt was not unsandboxed: it failed only because the sandbox denied test loopback/Unix-socket listeners (`EPERM`). The required suite passed when rerun with approved host capability. The first self-check/status call used macOS `/usr/bin/python3`, which lacked PyYAML; both passed with the existing read-only repository venv interpreter. These superseded environment attempts are recorded in `STEP0_DISCOVERY.md`; no pass is inferred from them. Normalized registered-check output is in `CHECKS_REGISTERED.json`.

Frontend build/premerge were not selected by `software-workflow.json` for the changed `frontend/src/**` and `execution/**` paths and were not named by V3-04's Checks line or the sealed implementation brief; they were skipped for this freeze. Runtime packages were built only to satisfy frontend typecheck imports.

## Scope and fence confirmation

- Changed product/test paths: `frontend/src/lib/consent/fake-hosted-engine-consent-port.ts` and `frontend/src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts` only.
- `consent-ux-fixtures.ts`, `hosted-engine-consent-port.ts`, and `account-consent-settings.tsx` are byte-identical to the basis. The existing fixture tests confirm secret-free snapshots and reserved `.test` hosts.
- No panel, vocabulary, Root, plan, register, decision-record, lifecycle, release, signing, notarization, publication, distribution, or host-state byte changed.
- The A1 re-stage declaration was recorded before product mutation in `STEP0_DISCOVERY.md`: this `frontend/` mutation invalidates the staged R20 procedure for any future proof claim and requires a newly staged revision and fresh owner-executed proof; historical R20 evidence remains historical only.
- F-APP-1 through F-APP-5 remain intact. No live-account or release-readiness claim is made.

## Residuals and next gate

- No implementation blocker or new discrepancy was found.
- The separate V3-03 Root-owned questions remain open: configuration-digest semantics and whether real private-home invalidation logs out the account.
- A fresh reviewer must inspect 100% of `git diff fe0ce926d..REVIEW_FREEZE`. No product or test byte may change after `REVIEW_PASS`.
- `_STATUS.md`, `MEMORY.md`, final `CHECKS.json`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, and `LOOP_RECEIPTS.md` remain untouched until `REVIEW_PASS`.
