# MAPPING — plan WP / gate / AT to App carrier, Root or external owner, or unseated state

**RunID:** `APP_V3_PATHWAY_SEATING_2026-09-03` · **Node:** N0 · **Basis:** `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` (candidate branch cut at `1537ddad1`, re-based onto the PR #680 merge)

Sources: current `main` for every status claim; the pinned plan
`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`
(SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`)
only for what a WP, gate, or AT means when complete (sections 9, 10.1, 11,
extracted from the HTML bytes with a Python HTML parser, not from memory);
the accepted SCA-APP-008 `Carrier_Map.md` for App carrier assignment; the
applied decomposition at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`
for the containing row text.

State vocabulary: `ACCEPTED` (owner-accepted on `main`) · `OPEN` (seated,
work remains) · `HELD` (an owner act or held binding is absent) ·
`APP_OWNED` (App carrier item; see the deliverable-local `Remaining` ID) ·
`ROOT_OWNED` (Root DEL-02-06 … DEL-02-12; appears here only as a dependency,
never as App work) · `SCOPE_AMENDMENT_REQUIRED` (the Carrier Map or plan
assigns an App obligation that the applied decomposition row text does not
cover; left unseated). No state below infers a pass.

## Root carrier reference (dependency targets only)

| Root carrier | Pathway responsibility (Root R17 N2 table) |
|---|---|
| DEL-02-06 | WP-01 Root integration, ten-binding state, held-act coordination |
| DEL-02-07 | WP-03/WP-06 process supervisor, containment, G-HELPER/G-SBX/G-PROT/G-ENV/G-ROLE/G-SIG/G-DUAL |
| DEL-02-08 | WP-02 exact supply/protocol pinning; G2 accepted at R15 with documented gaps |
| DEL-02-09 | WP-04 account, consent, root-private home, role, environment, sentinel |
| DEL-02-10 | WP-05/WP-06 API v2, approvals, closed event/terminal schema, role projection |
| DEL-02-11 | WP-03/WP-05/WP-08 retirement, restart, journal, fresh-thread, crash, replay |
| DEL-02-12 | WP-10 Root conformance, source identity, held-binding visibility, release fan-in |

Root's own seating candidate ("Root pathway seating") was **not selected** by
the owner on 2026-09-03; the Root carriers above therefore currently carry no
merged v3 `Remaining` items on `main` (checked: `execution/PKG-02_*/1_Working/DEL-02-07_*/_STATUS.md` has no `Remaining` section). App items that depend on Root
returns are parked as `NOT_SELECTABLE_UNTIL` the corresponding routed notice
exists under `projects/chirality-app-dev/execution/_Coordination/NOTICE_*`.

## A. Work packages

| WP | Plan meaning (completion) | App carrier item(s) | Root / external owner | State |
|---|---|---|---|---|
| WP-00 | Staged owner proof executed before frontend drift; re-stage rule | DEL-09-04 (no new item; A1 re-stage rule is a standing Step 0 declaration in the successor workplan) | owner (R20 proof, A1) | `ACCEPTED` (A1 2026-08-23; `_run_records/R21_…`) |
| WP-01 | Governed basis; no hold lifted implicitly; exit at G0.5/G1 and AT-053 | DEL-01-01-V3-01 (AT-053 App evidence); this candidate (exact SOW re-basis); A11 (TM triage) | Root DEL-02-06/DEL-02-03 (D-GOV supersession, Root SCA-004, ten-binding matrix) | App portion `OPEN`; SCA-APP-008 `ACCEPTED` (PR #662/#665); G0.5 `HELD` (Root R16: `source_identity`, `implementation_act` unavailable) |
| WP-02 | Exact App Server supply/protocol unit frozen; exit at G2 | none seated — the DEL-04-01 App Server probe is `SCOPE_AMENDMENT_REQUIRED` (row L312 covers the first Root-runtime adapter probe only) | Root DEL-02-08 (G2 accepted R15 with documented gaps) | `ROOT_OWNED` / App probe `SCOPE_AMENDMENT_REQUIRED` |
| WP-03 | Delegated Harness Process Supervisor built and proved; exit at G-SIG/G-DUAL, AT-054/055/058 | DEL-09-04-V3-01 (package supervisor/runtime bytes; `NOT_SELECTABLE_UNTIL` Root bytes + implementation act + G5 identity); App two-job installer/migration/rollback through runtime-control IPC is `SCOPE_AMENDMENT_REQUIRED` (row L367 covers DMG production/posture only) | Root DEL-02-07/DEL-02-11; DEL-02-06 implementation act `HELD` | `HELD` |
| WP-04 | Provider-neutral account/consent boundaries; exit at G3, G-KEY | DEL-02-05-V3-01 (`SELECTABLE`), DEL-02-05-V3-02 (`SELECTABLE`), DEL-02-05-V3-03, DEL-04-05-V3-01 (`SELECTABLE`), DEL-04-05-V3-02, DEL-09-06-V3-02 | Root DEL-02-09 (contract, device-code, keyring policy, `HostedEngineConsentPort` semantics) | `OPEN` |
| WP-05 | Delegated-harness adapter and terminal protocol; exit with conformance, G-WIRE, AT-055 | DEL-03-01-V3-01, DEL-03-03-V3-01, DEL-05-02-V3-01, DEL-05-03-V3-01 (all `NOT_SELECTABLE_UNTIL` Root API/event schema v2) | Root DEL-02-10/DEL-02-11; implementation act `HELD` | `HELD` (Root) / App consumption `OPEN` |
| WP-06 | Native delegation inside the hard envelope; exit at G-ROLE/G-APPR/G-SBX/G-SENT/G-PROT/G-ENV/G4 | DEL-08-04-V3-01, DEL-08-05-V3-01, DEL-09-02-V3-01, DEL-02-02-V3-02 (all `NOT_SELECTABLE_UNTIL` WP-03/05 fixtures) | Root DEL-02-07/DEL-02-09/DEL-02-10; D-GOV-35 `ACCEPTED` (notice on App surface) | `OPEN` (parked) |
| WP-07 | Understandable desktop UX and privacy posture; exit at G-CSP/G4 and AT-057 | DEL-02-02-V3-01 (`SELECTABLE`), DEL-02-05-V3-01/02 (`SELECTABLE`), DEL-02-05-V3-03, DEL-09-06-V3-01 (`SELECTABLE`), DEL-04-05-V3-01 (`SELECTABLE`) | — (App-owned; live claims wait for Root G3/G-WIRE) | `APP_OWNED`, `OPEN` |
| WP-08 | Data preserved; restart/upgrade behaviour defined; exit with v2→v3, account-null/change, root-home, deletion, restart, retirement, rollback tests | DEL-05-01-V3-01 (`SELECTABLE`), DEL-05-01-V3-02, DEL-05-04-V3-01, DEL-04-05-V3-01 (typed safeStorage failure, `SELECTABLE`); App consent/root-home migration and account-change invalidation are `SCOPE_AMENDMENT_REQUIRED` (row L322 covers session records only); App resume-continuity decision logic on DEL-03-03 is `SCOPE_AMENDMENT_REQUIRED` (row L305) | Root DEL-02-11 (storage/consent/retirement schemas, fresh-thread policy) | `OPEN` |
| WP-09 | Repeatable preparation packages and the release procedure without releasing; exit at G5 | DEL-09-05-V3-01/02/03 (`SELECTABLE`), DEL-09-05-V3-04, DEL-09-04-V3-01, DEL-09-06-V3-03 | owner host act for the self-signed identity; D-APP-97/F-APP-2 active | `APP_OWNED`, `OPEN` |
| WP-10 | Conformance fan-in and release readiness; no open P0/high | DEL-09-01-V3-01, DEL-09-02-V3-01, DEL-09-03-V3-01/02, DEL-09-06-V3-02, DEL-03-01-V3-01 (RQG §13 contribution), DEL-05-02-V3-01, DEL-05-03-V3-01 | Root DEL-02-12; REVIEW/EVALUATION verify | `OPEN` (parked on Root inputs) |
| WP-11 | Actual release operation; exit at G8 | DEL-09-05-V3-05 (`NOT_SELECTABLE_UNTIL` G6a; owner/CHANGE acts only) | owner; CHANGE for authorized Git/publication | `HELD` |

## B. Gates

| Gate | Decision owner (plan) | Current state on `main` | App carrier item(s) contributing evidence |
|---|---|---|---|
| G0 | owner | `ACCEPTED` (`plans/steers/chirality_app_v3_g0_record_2026-08-22.md`; TM triage dispositions A11) | — |
| G0.25 | owner + App loop | `ACCEPTED` (A1; R20 owner proof, DEL-09-04 R21 record) | A1 re-stage rule carried as a standing Step 0 declaration |
| G0.5 | owner / owning loops | `HELD` — Root R16 routed the ten bindings; `source_identity` and `implementation_act` remain `HELD_UNAVAILABLE`; App SCA-APP-008 `ACCEPTED`; D-APP-103 recorded | DEL-01-01-V3-01 (AT-053 App half) |
| G1 | REVIEW + owner | `OPEN` — App Electron authority drift resolved on the App side by PR #680 (corpus v20; Receipt 204); combined echo to Root and TM-ROOT-122 disposition pending (Root); AT-053 evidence pending | DEL-01-01-V3-01 |
| G2 | owner | `ACCEPTED` with documented gaps (R15, PR #673 merge `baa29d22f`); App consumption not yet routed | DEL-03-01-V3-01 exact-pin claims wait for consumable supply; DEL-09-05-V3-02 SBOM input |
| G-HELPER | Root/App architecture review; owner (TM-APP-030 bundle identity) | `HELD` | none (installer `SCOPE_AMENDMENT_REQUIRED`) |
| G-SIG, G-DUAL | Root runtime / Root+App review | `ROOT_OWNED`, `OPEN` | DEL-09-04-V3-01 observation only |
| G-SBX, G-SENT, G-PROT, G-ENV | security / domain-runtime review | `ROOT_OWNED`, `OPEN` | DEL-09-04-V3-01 fuse/entitlement posture observation (G-SBX App package portion) |
| G-ROLE | Root governance + runtime review | `ROOT_OWNED`, `OPEN`; failure posture pre-decided (G0 A3: label `role not mechanically enforced`) | DEL-02-02-V3-01, DEL-02-05-V3-02 labels; DEL-08-04-V3-01, DEL-08-05-V3-01 |
| G-APPR | security + UX + Root contract review | `ROOT_OWNED`, `OPEN` | DEL-09-06-V3-02, DEL-04-05-V3-02 App boundary portions |
| G-WIRE | privacy/security review | `OPEN` (Root schema v2 first) | DEL-03-03-V3-01, DEL-05-02-V3-01, DEL-05-03-V3-01, DEL-09-06-V3-02 |
| G-CSP | App security review | `APP_OWNED`, `OPEN` | DEL-09-06-V3-01 (`SELECTABLE`) |
| G3 | REVIEW (owner-authenticated proof) | `OPEN` | DEL-02-05-V3-03, DEL-04-05-V3-02 (live); DEL-02-05-V3-02 fixtures |
| G4 | owner accepts Preview boundary | `OPEN` | DEL-02-02-V3-02, DEL-08-04-V3-01, DEL-08-05-V3-01, DEL-09-02-V3-01 |
| G5 | REVIEW | `OPEN` | DEL-09-05-V3-01/02/03/04, DEL-09-04-V3-01, DEL-09-01-V3-01, DEL-09-06-V3-03 |
| G6a | owner | `HELD` (D-APP-97 / F-APP-2 active; exact candidate not named) | DEL-09-05-V3-05 fires only after the ruling |
| G6b, G-KEY, G7, G8 | owner (+ security review; CHANGE at G8) | `HELD` | DEL-09-05-V3-05, DEL-09-03-V3-02 rerun |

## C. Acceptance matrix AT-001 … AT-058

"App item" names the deliverable-local `Remaining` ID that carries the App
portion of the scenario; "Root/external" names the owner of the remainder.
`SELECTABLE` marks App items selectable after merge; every other App item is
`NOT_SELECTABLE_UNTIL` its named gate.

| AT | Scenario (plan) | Primary gate | App item(s) | Root / external | State |
|---|---|---|---|---|---|
| AT-001 | Exact supply identity | G2/G5 | DEL-09-05-V3-02 (SBOM/notices input; `SELECTABLE`) | Root DEL-02-08 (G2 `ACCEPTED`) | `ROOT_OWNED`/App evidence `OPEN` |
| AT-002 | Unsupported drift | G2 | DEL-03-01-V3-01 (typed unavailable consumption) | Root DEL-02-08/DEL-02-10 | `ROOT_OWNED` |
| AT-003 | Worker-key isolation | G-DUAL/G-ROLE | — | Root DEL-02-07/DEL-02-09 | `ROOT_OWNED` |
| AT-004 | Graceful shutdown | G-SIG | — | Root DEL-02-07/DEL-02-11 | `ROOT_OWNED` |
| AT-005 | Forced shutdown | G-SIG | — | Root DEL-02-11 | `ROOT_OWNED` |
| AT-006 | Environment and shell isolation | G-ENV | — | Root DEL-02-07/DEL-02-09 | `ROOT_OWNED` |
| AT-007 | Consent, account, root continuity | G-SENT/G4 | DEL-02-05-V3-03 | Root DEL-02-09 (`HostedEngineConsentPort` semantics) | `HELD` on Root contract |
| AT-008 | Device login success | G3/G-WIRE | DEL-02-05-V3-02 (fixture), DEL-02-05-V3-03 (live), DEL-04-05-V3-02 (typed transport) | Root DEL-02-09 | `OPEN` |
| AT-009 | Login cancel/stale/offline | G3 | DEL-02-05-V3-02/03 | Root DEL-02-09 | `OPEN` |
| AT-010 | Logout | G3/G-SIG | DEL-02-05-V3-03 | Root DEL-02-09/DEL-02-11 | `OPEN` |
| AT-011 | Keyring unavailable | G3/G-KEY | DEL-04-05-V3-01, DEL-02-05-V3-01 (App safeStorage analogue; `SELECTABLE`) | Root DEL-02-09 (App Server keyring) | `OPEN` |
| AT-012 | Model/capability discovery | G3 | DEL-02-05-V3-02 (fixture)/V3-03 | Root DEL-02-10 | `OPEN` |
| AT-013 | Primary turn | G3 | DEL-03-01-V3-01, DEL-09-03-V3-01 (client portions) | Root DEL-02-10 | `OPEN` |
| AT-014 | Interrupt and retirement fan-out | G-SIG/G4 | DEL-09-03-V3-01 (test portion) | Root DEL-02-11 | `ROOT_OWNED` |
| AT-015 | Protocol failure | G3 | DEL-03-01-V3-01 | Root DEL-02-10 | `OPEN` |
| AT-016 | Rate limit | G3 | DEL-02-05-V3-02 (status presentation) | Root DEL-02-10 | `OPEN` |
| AT-017 | No automatic fallback | G3 | DEL-03-01-V3-01 | Root DEL-02-10 | `OPEN` |
| AT-018 | Actual-turn sandbox sentinel | G-SBX/G-SENT/G-ENV | — | Root DEL-02-07 | `ROOT_OWNED` |
| AT-019 | Protected material round trip | G-PROT/G4 | — | Root DEL-02-07/DEL-02-09 | `ROOT_OWNED` |
| AT-020 | Network posture | G-APPR/G4 | DEL-04-05-V3-02, DEL-09-06-V3-02 | Root DEL-02-10 (`networkApprovalContext`) | `OPEN` |
| AT-021 | Escalation denial | G-APPR | DEL-09-03-V3-01 (denied-action test portion) | Root DEL-02-10 | `ROOT_OWNED` |
| AT-022 | Concurrent approval attribution | G-APPR | — | Root DEL-02-10 | `ROOT_OWNED` |
| AT-023 | Session approval | G-APPR | DEL-02-05-V3-02 (`acceptForSession` UI fixture) | Root DEL-02-10 | `OPEN` |
| AT-024 | Raw-event rejection | G-WIRE | DEL-03-03-V3-01, DEL-05-02-V3-01 | Root DEL-02-10 | `OPEN` |
| AT-025 | Secret and ceremony-data scan | G-WIRE | DEL-05-03-V3-01, DEL-09-06-V3-03 | Root DEL-02-10/DEL-02-09 | `OPEN` |
| AT-026 | Native delegation available | G4 | DEL-08-04-V3-01 | Root DEL-02-07/DEL-02-10 | `OPEN` (parked) |
| AT-027 | No Chirality topology cap | G-ROLE/G4 | DEL-08-04-V3-01 | Root DEL-02-09/DEL-02-10 | `OPEN` (parked) |
| AT-028 | Parentage visibility and enumeration | G4 | DEL-08-05-V3-01, DEL-02-02-V3-02, DEL-09-02-V3-01 | Root DEL-02-10 | `OPEN` (parked) |
| AT-029 | Untyped/Agent 0/1 posture | G-ROLE/G4 | DEL-08-04-V3-01 | Root DEL-02-09 | `OPEN` (parked) |
| AT-030 | Explicit Codex Agent 2/TASK posture | G-ROLE/G4 | DEL-08-04-V3-01; labels DEL-02-02-V3-01 (`SELECTABLE`), DEL-02-05-V3-02 (`SELECTABLE`); DEL-09-02-V3-01 | Root DEL-02-09 (G-ROLE proof) | `OPEN` |
| AT-031 | Semantic failure containment | G4 | DEL-08-04-V3-01 | Root DEL-02-07 | `OPEN` (parked) |
| AT-032 | Retirement cleanup and reconciliation | G-SIG/G4 | DEL-09-02-V3-01 (report row) | Root DEL-02-11 | `ROOT_OWNED` |
| AT-033 | Renderer hardening | G-CSP | DEL-09-06-V3-01 (`SELECTABLE`) | — | `APP_OWNED`, `OPEN` |
| AT-034 | Accessibility | G4/G7 | DEL-02-05-V3-02 (fixture), DEL-02-05-V3-03 | — | `APP_OWNED`, `OPEN` |
| AT-035 | v2 data and two-job migration | G-HELPER/G5/G7 | DEL-05-01-V3-01 (`SELECTABLE`, v2 data), DEL-05-01-V3-02; two-job installer: `SCOPE_AMENDMENT_REQUIRED` (DEL-09-04) | Root DEL-02-07 | `OPEN` / installer `SCOPE_AMENDMENT_REQUIRED` |
| AT-036 | Restart posture | G-SIG/G5 | DEL-05-04-V3-01, DEL-05-02-V3-01 | Root DEL-02-11 | `OPEN` (parked) |
| AT-037 | Native-engine regression | G5/G7 | DEL-09-01-V3-01 | — | `APP_OWNED`, `OPEN` (parked on first v3 landing) |
| AT-038 | Unsigned preparation artifact | G5 | DEL-09-04-V3-01; D-APP-97 C1 workflow evidence exists (PR #583 run `32327128935`) | — | `APP_OWNED`, `OPEN` |
| AT-039 | Release identity freeze | G6a | DEL-09-05-V3-01/02/03 (method, SBOM/notices, version; `SELECTABLE`) | owner (G6a act) | `OPEN` / freeze `HELD` |
| AT-040 | Signed/notarized artifact | G6b | DEL-09-05-V3-05 | owner | `HELD` |
| AT-041 | Clean-machine release smoke | G7 | DEL-09-05-V3-05 | owner | `HELD` |
| AT-042 | Public download backcheck | G8 | DEL-09-05-V3-05 | owner / CHANGE | `HELD` |
| AT-043 | Version identity | G5/G7 | DEL-09-05-V3-03 (`SELECTABLE`; product application waits for G5) | — | `APP_OWNED`, `OPEN` |
| AT-044 | Root-private account state | G3/G-KEY/G-DUAL | DEL-02-05-V3-03, DEL-04-05-V3-02 | Root DEL-02-09 | `OPEN` (parked) |
| AT-045 | Instruction and role identity | G-ROLE/G4 | DEL-08-04-V3-01, DEL-08-05-V3-01; labels DEL-02-02-V3-01 | Root DEL-02-09/DEL-02-10 | `OPEN` (parked) |
| AT-046 | Thread/session deletion | G4/G5 | DEL-05-01-V3-01/02 | Root DEL-02-11 | `OPEN` |
| AT-047 | Preparation nested-byte survival | G5 | DEL-09-04-V3-01 | — | `APP_OWNED`, `OPEN` (parked) |
| AT-048 | Finder activation during work | G-HELPER/G-DUAL/G-SIG | — | Root DEL-02-07 | `ROOT_OWNED` |
| AT-049 | Packaged sandbox enforcement | G-SBX | DEL-09-04-V3-01 (fuse/entitlement posture in the package) | Root DEL-02-07 | `ROOT_OWNED` / App package portion `OPEN` |
| AT-050 | Role-profile isolation | G-ROLE | — | Root DEL-02-08/DEL-02-09 | `ROOT_OWNED` |
| AT-051 | Credential signature transition | G-KEY/G7 | DEL-09-05-V3-04, DEL-09-06-V3-03, DEL-04-05-V3-01 (`SELECTABLE`) | owner (host identity; release lane) | `OPEN` / release lane `HELD` |
| AT-052 | Exact signed-byte regression fan-in | G7 | DEL-09-03-V3-02 | owner | `HELD` |
| AT-053 | Governed basis and shared-runtime gate | G0/G0.5/G1 | DEL-01-01-V3-01 (`SELECTABLE`) | Root DEL-02-06/DEL-02-12 | `OPEN` |
| AT-054 | Two-job install transaction | G-HELPER/G-CSP/G-DUAL | App installer entry through runtime-control IPC: `SCOPE_AMENDMENT_REQUIRED` (DEL-09-04) | Root DEL-02-07 | `SCOPE_AMENDMENT_REQUIRED` (App) / `ROOT_OWNED` |
| AT-055 | Retirement failure recovery | G-SIG | — | Root DEL-02-11 | `ROOT_OWNED` |
| AT-056 | Private CODEX_HOME lifecycle | G-DUAL/G-ENV/G-KEY | DEL-02-05-V3-02 (explanation copy fixture) | Root DEL-02-09 | `ROOT_OWNED` / UI `OPEN` |
| AT-057 | Credential IPC and typed storage states | G-CSP/G-KEY | DEL-09-06-V3-01, DEL-04-05-V3-01, DEL-02-05-V3-01 (`SELECTABLE`); identity-transition tests DEL-09-06-V3-03, DEL-09-05-V3-04 | — | `APP_OWNED`, `OPEN` |
| AT-058 | Signed Electron-as-Node host | G-HELPER/G-SBX/G6b/G7 | DEL-09-04-V3-01 (preparation observation) | Root DEL-02-07; owner (signed bytes) | `ROOT_OWNED` / `HELD` |

## D. SCOPE_AMENDMENT_REQUIRED (unseated; returned for a later SCOPE_CHANGE act)

| # | Carrier | Obligation assigned by the Carrier Map / plan | Why unseated (applied row text at `d6f6cadb2`) |
|---|---|---|---|
| S-1 | DEL-04-01 | WP-02 App-side probe of the exact App Server supply/protocol/config/role behaviour with adoption evidence (AT-001/002/050 observation) | Row L312 covers the *first Root-runtime adapter* probe (version, messages, policy inputs, hooks, MCP, session linkage, interruption, packaging, conformance); the App Server is a different adapter and the Gate-5 application did not amend this row. The Electron 43.2.0 drift observation is carried by A11 E2 (PR #680). |
| S-2 | DEL-09-04 | WP-03 App-side two-job installer/migration/rollback through runtime-control IPC (AT-054 App entry; AT-035 installer half) | Row L367 covers producing the unsigned arm64 DMG and proving instruction-root/SDK packaging posture; it does not cover installer transactions through runtime-control IPC. |
| S-3 | DEL-03-03 | WP-08/G0 A4 App-side resume-continuity decision logic (`thread/resume` only on exact root/account/policy match, else fresh thread) | Row L305 covers keeping `/api/harness/*` shapes and SSE names stable while policy moves behind services; the resume decision is runtime policy. Root DEL-02-11 owns restart/fresh-thread policy and DEL-05-04-V3-01 carries truthful presentation, so the owner may find no amendment necessary. |
| S-4 | DEL-05-01 | WP-08 consent/root-home migration and account-change invalidation | Row L322 covers legacy project-local *session record* access and migration; consent, root-home, and account-change semantics are Root-owned (DEL-02-09/DEL-02-11) and the row does not assign an App migration of them. |
| S-5 | DEL-04-05 | Carrier Map "extend … to OAuth/device-code/keyring … and root-account transitions" beyond typed transport conformance | Row L316 covers credential entry/status participation, safeStorage boundary participation, and verification of ruled provider/network behaviour; OAuth/device-code/keyring semantics stay Root-owned. Only the typed-transport and posture conformance portions are seated (DEL-04-05-V3-02). |
| S-6 | DEL-09-05 | CI wiring of SBOM/notice tooling into repo-root `.github/workflows/**` | Not a scope gap in the row but a write-scope limit: the loop's write scope is `projects/chirality-app-dev/**` unless the owner grants wider scope; tooling under `frontend/scripts/**` is seated (DEL-09-05-V3-02), workflow wiring is not. |

Everything else the Carrier Map assigns is contained by its row (see
`COVERAGE_MATRIX.md`).

## E. Current-main status citations used above

- SCA-APP-008: applied (`d6f6cadb2`, PR #662 merge `d5e40b3c25fe527919f1d2d2a31ea97ce2835795`); pointer act PR #665 (`4251530ec8a5d5b7abfc035cbdde63dab7fa80f3`); Root ingestion PR #668 (`eb2ea19db5b86ad33760345d274b828d7a12e6cc`); `Phase5/CLOSURE_ADDENDUM_2026-09-03.md`.
- G2: Root R15 (`plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md`), PR #673 merge `baa29d22fa034784cda221b2929061213e83ec91`, with the four `UNAVAILABLE_UNDER_BOUNDS` gaps and the R13-B G5 finding.
- G0.5 / bindings: Root R16 (`…r16_2026-08-27.md`) routed the ten DEL-02-06 bindings; `source_identity`, `implementation_act`, `cutover_act`, `release_act` remain `HELD_UNAVAILABLE`; R17 preserved R16-A/B/C/E and rejected PR #676.
- G1: A11 E2 concordance merged as PR #680 (`8140daec7ab7165f8972451dbdd3a67b8bb2fd38`; corpus v20; Receipt 204; `NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md` prepared); TM-ROOT-106/122 remain open and unruled on Root.
- APP-HOLD-1: `app_hold.py check --operation dispatch` returns `ALLOW` for all nineteen carriers; `scan --require-register-match` passes (see `VALIDATION_EVIDENCE.md`).
- Task Management: live register post-A11 SHA-256 `bae90ca564f45d51bbb94722cf64b3cda6bc0d614365a2c177b2b79c55844931` (TM-APP-030 `OPEN` for G-HELPER; 027/028/032 `DEFERRED`).
- D-APP-97 / F-APP-2: active through preparation (register row D-APP-97 `RULED` C1); lift only at G6a with the exact candidate.
