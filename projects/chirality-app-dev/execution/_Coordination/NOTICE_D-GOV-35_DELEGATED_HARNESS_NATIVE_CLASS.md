# Root Notice — D-GOV-35 Delegated-Harness-Native Class

Status: `ROUTED 2026-08-22 — COORDINATION, NOT AUTHORITY`

Source decision:
`docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md`

Root `AGENTS.md` changed from SHA-256
`268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`
to SHA-256
`377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`
by applying the exact ruled patch at SHA-256
`4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`.

## Root change

Root now recognizes two executable delegation classes:
`Chirality-managed` and `delegated-harness-native`. Managed children remain
the sole Chirality-managed path. Untyped, Agent 0, and Agent 1 primary Codex
sessions may use native delegation within the hard outer envelope. Native
descent does not assign an Agent 0/1/2 role. Codex Agent 0/1/2 entry remains
available; where `G-ROLE` cannot prove non-delegation, Agent 2/TASK remains
offered as `role not mechanically enforced` and governed-workflow evidence is
`instruction-asserted`. For the native class, K-SUBAGENT non-delegation is
instruction+config asserted, not mechanism-proven.

## App-owned surfaces and follow-on

SCA-APP-008 and App WP-06 own the prospective App disposition across:

- App `docs/CONTRACT.md` K-SUBAGENT-1/2/3;
- immutable D-APP-68 disposition 4 and its prospective App-owned successor;
- DEL-08-04 `ScopeOfWork.md`, DEL-08-05's record boundary, and
  `frontend/src/lib/harness/subagent-governance.ts:205-213`;
- App-local `AGENTS.md` and the generated packaged instruction-root mirror
  controlled by `frontend/package.json` and
  `frontend/scripts/verify-instruction-root-integrity.mjs`; and
- the App authority-reference corpus, currently v18 and not currently pinning
  Root `AGENTS.md`, if App elects to expand it.

The following exact-hash evidence groups named by D-GOV-35 `IMPACT.md` are
historical and immutable, not live mirrors: both 2026-08-20 DEL-09-06 packaged
security proof instruction-root `manifest.json`/`summary.json` pairs; the
D-APP-86 helper-parity baseline `SOURCE_MANIFEST.sha256` and
`PACKAGE_MANIFEST.sha256`; D-APP-88 single/standard `FILE_HASHES.txt` and
implementation `PACKAGE_MANIFEST.md`; the 2026-08-03 parity baseline
`PACKAGE_MANIFEST.sha256`; the 2026-08-22 login-proof
`integrity-evidence.log`; and the 2026-07-11 D55 concordance
`AUTHORITY_MAP.md` frozen-process-input snapshot. Do not rewrite them. App
decides whether a new candidate needs new evidence.

The Root-owned `exports/chirality-app/` projection is stale after this Root
instruction change. R1-B explicitly defers its regeneration to the next Root
export release; it is not an App write.

The App loop may adopt, amend, decline, or defer this notice through
SCA-APP-008 and WP-06 under App authority. This notice changes no App
contract, SOW, product source, lifecycle, hold, pin, release, or reliance
state.
