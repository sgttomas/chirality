# SCA-APP-008 revision note: D-GOV-43 application (topology A2), 2026-09-12

**Status of the packet after this note:** `AWAITING_OWNER_ACCEPTANCE` with the
parts listed below marked `SUPERSEDED_BEFORE_ACCEPTANCE`. Accepting the packet
as originally written would re-ratify the retired daemon architecture
(`D-GOV-43` `IMPACT.md`, App loop table); this note revises it first. The
original text is preserved in place; each affected file carries a short
revision block pointing here.

**Authority:** D-GOV-43 (ruled 2026-09-11) item 11 and the A2 supplement
(recorded 2026-09-12), applied to the App loop by
`execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`.
Publication SHA `d2878462be59a43b4afc175a8cce85abca9cf696`. This note is a
record of application, not owner acceptance of SCA-APP-008.

## Superseded parts

| Where | Original seating | Disposition | Replacement (A2 pathway) |
| --- | --- | --- | --- |
| `Brief.md` action 4; `Carrier_Map.md` DEL-02-05, DEL-04-05, DEL-05-01, DEL-09-06 rows; `Contract_Amendments.proposed.md` K-CONSENT-1; `Impact_Assessment.md` "Add account/consent boundary" and "Add three command-network postures" | `HostedEngineConsentPort` as the sole coordinator boundary; root-private `CODEX_HOME` per canonical root; per-root consent, generations and revocation; three per-root command-network postures | Superseded (family 1 and 3) | One Chirality-owned effective Codex home with shared configuration by reference and private `auth.json`; sign-in through Codex's own account methods; approval policy and sandbox mode are the user's choice per project with per-turn override (D-GOV-43 items 3, 4, 6). No consent port and no per-root generation is seated. |
| `Brief.md` action 5; `Carrier_Map.md` DEL-09-04 row; `Impact_Assessment.md` WP-03 and "Add installer/release lanes" | Two-job installer through runtime-control IPC; packaged supervisor and runtime bytes; DEL-09-07 and `APP-HOLD-1` | Superseded (family 1) | The App starts, owns and stops the Runtime service as a child process; no LaunchAgent, installer, migration or rollback transaction; DEL-09-07 retired with `APP-HOLD-1`. DEL-09-04 packages the bundled stock `@openai/codex` dependency and the Runtime service. |
| `Contract_Amendments.proposed.md` K-CONTROL-1 "two purpose-limited sockets"; `DRAFT_NOTICE_TO_ROOT.md` "second supervisor socket"; `Brief.md` action 6 and `Handoff_State.md` contract row | Exactly two Unix-domain sockets: the daemon API and a private daemon-to-supervisor socket | Superseded in the second-socket part | K-CONTROL-1 keeps its spine: one Unix-socket API with client tokens private to the application and no TCP listener; the supervisor socket and job are retired (A2 supplement, effect on item 7). Contract wording follows the Root `docs/CONTRACT.md` §1.13 amendment of the same tranche. |
| `Contract_Amendments.proposed.md` K-EVENT-6; `Carrier_Map.md` DEL-03-03, DEL-05-02, DEL-05-03 rows; `Impact_Assessment.md` WP-05 | Closed, versioned `HarnessEvent` schema v2; unknown upstream types reduced to diagnostic codes; four terminal identifiers | Superseded (family 2) | An extensible event representation preserving upstream method names, identifiers and payloads, with normalized views for known items; unfamiliar notifications stay inspectable; every server request is answered explicitly (D-GOV-43 item 2; A2 supplement clarification 1). Redaction of secrets before every sink is retained. |
| `Carrier_Map.md` DEL-03-03 and DEL-05-04 rows | `thread/resume` only when canonical root, account identity and policy digest match, else fresh thread | Superseded (family 2) | App relaunch resumes threads through `thread/resume`; the App keeps its own chat index keyed by Codex thread ID (D-GOV-43 item 5). The rule that an in-flight turn is never claimed re-attached is replaced by the disconnection rule: the Runtime owns the active turn, a renderer subscription observes it, and reopening recovers state without re-sending the prompt. |
| `Carrier_Map.md` DEL-09-05 row; `Impact_Assessment.md` WP-09 and WP-11; `Handoff_State.md` held boundaries on the A1 re-stage rule | Twenty-five-step exact-candidate spine (G5, G6a, G7, G8), A1 re-stage rule, exact-candidate hold lifting | Superseded (family 1 and 5) | The short procedure: build, sign, notarize, verify the bundle signature and the Codex pin, then the distinct packaged checks (S-6, S-8, signature and pin verification as the expected minimum, not a ceiling). `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md`. Signing, notarization and publishing remain owner acts. |

## Retained parts

Actions 1 to 3 and 7 of `Brief.md` (carrier seating on live deliverables,
the D-APP-74 prospective supersession for multi-child managed execution, the
role-entry parity with the `role not mechanically enforced` label, the App
DAG) are architecture-neutral and stand for owner review. K-ROLE-2 and
K-UNTYPED-1 stand with D-GOV-35's "hard outer envelope" re-expressed as the
user-chosen policy of D-GOV-43 item 4. DEL-04-01 remains probe-only. The
`Opt-in Preview` label and the macOS arm64 single target stand. Ordinary
software integrity (lockfile pin, signing, notarization, renderer isolation
and validated IPC, the DEL-09-06 network, key and renderer checks) is
retained.

## Effect on the packet state

`SCAStatus` remains `AWAITING_OWNER_ACCEPTANCE`. `DecompositionTruthState`,
`ImplementationAuthority`, `LifecycleAuthority` and `ReleaseAuthority` are
unchanged. A later acceptance act must accept the packet as revised by this
note; the superseded rows are not to be applied to decomposition truth. The
`SCA-APP-008 package-shape disposition` named open in `_LATEST.md` remains
open.
