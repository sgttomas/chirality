# RTCONTRACT capability inventory: notes (R2 reverse pass, R1b dispatch)

Area: `projects/chirality-runtime/packages/{contracts,client,engine-claude,engine-pi-omlx}/**` at frozen basis `00115c719`. It has 44 files, taken from the `IMPLEMENTATION_SURFACES.csv` rows with `Area=RTCONTRACT`.
Output: `RTCONTRACT_capabilities.csv`, 53 rows (`CAP-RTCONTRACT-001`…`053`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders and no `projects/chirality-runtime/execution/**` files were read. The rows come from code, from a symbol-level import map (a scratchpad script over App `src/`, `electron/`, `scripts/`, Runtime `packages/*/src` and the tests), and from `REACHABILITY.csv` and `TOUCHED_PATHS.csv`.

## 1. Census

CENSUS rows=53 LIVE=38 LEGACY_ONLY=7 TEST_ONLY=8 UNREACHED=4 ENABLED=37 DISABLED=16

- UNREACHED rows:
  - 025: `events.ts`, and the v1-to-v2 projection.
  - 028: the runtime tool callback bridge in `delegated.ts`.
  - 038: `RuntimeEnginePort` and `asHarnessSession` in `engine.ts`.
  - 053: `engine-claude`.
  - Rows 028 and 038 are UNREACHED at the symbol level: the module is LIVE, but the symbols have no importer outside `contracts`.
- DISABLED rows fall into four groups:
  - Switched off by the App-owned composition: 045–048 (the credential store, OMLX residency and the Agent 1 runs route), plus the SDK version pins.
  - Retired on the App side: 011 (provider network consent).
  - Legacy or retained engines: 042, 044, 050–053.
  - No product consumer: 025, 028, 038, 040, 041.

## 2. Granularity rationale

- One row per contract surface or client behaviour, organised by **behaviour** rather than by file. Where a behaviour spans the DTO or validator in `contracts` and the `RuntimeClient` method in `client`, one row names both. Examples: steering (016), server requests (017) and native plan (029).
- **`delegated.ts` (336 lines) is split into eight rows**, because different deliverables plausibly own its parts:
  - hosted account (010)
  - consent (011)
  - model catalog (012)
  - server requests (017)
  - policy mapping (019)
  - worker supervision (026)
  - delegated turn and supervisor ports (027)
  - the unused tool-callback bridge (028)
- **`v3.ts` is split into five rows:** native plan, roles, method catalog, selected context, and instruction basis.
- **`client.ts` (773 lines) is folded into the behaviours it transports.** Two client-only rows are kept separate:
  - transport and authentication (005) and SSE (006);
  - the application-tool client methods (035). This behaviour is post-release and test-only, so it is split from the LIVE application-tool contract (034).
- **One row per module** for the retained engines (050–053) and for harness modules with a single purpose (039–045).
- **Contracts barrel.** The package manifest and the barrels form one row (001), because the export map is a contract surface that App build tooling consumes.

## 3. Files covered versus total

COVERAGE covered=40 total=44

Uncovered files, all build configuration with no behaviour:
- `projects/chirality-runtime/packages/client/tsconfig.json`
- `projects/chirality-runtime/packages/contracts/tsconfig.json`
- `projects/chirality-runtime/packages/engine-claude/tsconfig.json`
- `projects/chirality-runtime/packages/engine-pi-omlx/tsconfig.json`

**PostReleaseBasis.** `TOUCHED_PATHS.csv` has five ranges in this area, all from `da95ec194` ("Add application-owned dynamic tools to Runtime"):
- `client.ts:50-54` and `client.ts:363-383`
- `application-tools.ts:1-92`
- `index.ts:11`
- `protocol.ts:66-71`

Rows 001, 004, 034 and 035 are `YES`; every other row is `NO`.

## 4. Dead, unreached, disabled or retired code observed

- **Barrel inflation of the static map.**
  - `REACHABILITY.csv` marks every module re-exported by `contracts/src/index.ts` as LIVE via `standalone-bin>contracts/src/index.ts`.
  - The symbol map shows that several have no non-test consumer at all:
    - `harness/domain-profile.ts`, `harness/operation-proposal.ts` and `harness/engine-conformance.ts`: TEST_ONLY.
    - `harness/tool-catalog.ts`: TEST_ONLY, plus the dev script `frontend/scripts/generate-tool-catalog.mjs`.
  - Others are consumed only by legacy `lib/harness` engine files:
    - `harness/tool-descriptor.ts`, `harness/mcp/tool-names.ts` and `harness/sdk-version.ts`: LEGACY_ONLY.
  - I recorded the verified reach and cited the pack's barrel basis in `Notes`.
- **TYPE-ONLY modules reached as LIVE.** Examples: `harness/types.ts` (33 types, no values), `session.ts`, `residency.ts`, and most of `v3.ts` and `delegated.ts`. They are tagged `REACH=LIVE; TYPE-ONLY`.
- **`engine-claude`: no importer anywhere, tests included.**
  - `frontend/package.json:65` still declares it as a `file:` dependency, and `frontend/scripts/generate-third-party-notices.mjs:55` lists it.
  - `frontend/scripts/verify-packaged-dependency-boundary.mjs:149,169,180` lists it as forbidden in the App, service and CLI bundles.
- **`engine-pi-omlx`: imported only by Runtime tests** (`omlx-client.test.ts`, `pi-turn-runtime.test.ts`, `pi-packaging.test.ts`).
  - It is also declared at `frontend/package.json:66` and forbidden from bundles by the same boundary script and by `build-controlled-ci-runtime.mjs:51-52`.
  - `createPiOmlxEngineAdapter` has no test caller.
- **Switched off by the App-owned Runtime composition** (`daemon/src/app-owned-composition.ts`):
  - Credentials: the stub status returns `configured:false`, and set/remove throw `ENGINE_UNAVAILABLE` (lines 180, 225). The App still calls `credentialStatus`, `storeCredential` and `removeCredential` from `electron/api-key-ipc.ts`.
  - OMLX residency: `listStatus` returns `[]`, and load/unload throw (lines 180–181). `RUNTIME_ERROR_CODES` still carries the `OMLX_*` and `RESIDENCY_*` codes.
  - Agent 1 runs: no `Agent1RunPort` is supplied, so `RuntimeService.runAgent1` throws `REQUIRED_DELEGATION_MISSING` (`core/src/runtime-service.ts:664-670`).
- **Retired but kept:**
  - Provider network consent. The App port reads status instead of granting consent (`runtime-daemon-harness-port.ts:765-778`, citing D-GOV-43). `RuntimeClient.grantHostedProviderNetworkConsent` is kept deliberately; `client.test.ts:272` asserts it.
  - The native-plan qualified disposition (`assertQualifiedNativePlanEvent`) is not admitted, because the composition admits only `CODEX_NATIVE_PLAN_TRIAL_ADMISSION`.
- **Unreferenced symbols** (no importer outside `contracts`):
  - `RuntimeToolCallbackDeclaration`, `RuntimeToolCallbackMessage`, `RuntimeToolCallbackResult`, `SupervisorRuntimeToolPort`
  - `RuntimeEnginePort`, `RuntimeEngineTurnInput`, `RuntimeEngineTurnResult`, `asHarnessSession`
  - `DelegatedRoleEvidence`, `FLOW_A_CONTRACT_VERSION`, `ResidencyEpoch`
- **Client methods with no App or CLI caller:**
  - `health`, `listAgents`, `registerHostedBootstrapProject` and `grantHostedProviderNetworkConsent`.
  - All five application-tool methods (added post-release). The daemon side of application tools is wired, but only the owning application client may use it, and no App code registers tools.
  - `releaseApplicationTools` and `listAgents` have no test caller either.
- **`events.ts`: UNREACHED.** Its only edge is a type import from `v2-events.ts`, used by `projectRuntimeEventV2`, which only a test calls.

## 5. Method friction with §5.2

- **Module-level reach cannot see barrel re-exports.** `export *` barrels make the pack's module-level reach overstate LIVE for contract packages.
  - Proposal: compute reach at the symbol level for barrel-re-exported modules, or have the pack add a `BarrelOnly=YES` flag when the only LIVE edge runs through an `export *` barrel.
- **Symbol-level dead contracts do not fit the reach vocabulary.** Rows 028 and 038 describe dead symbols inside a LIVE module. I used `REACH=LEGACY_ONLY; UNREACHED (symbol level…)` because the brief allows only three values.
  - Proposal: allow a `DEAD` marker in Notes, distinct from UNREACHED.
- **STATE is ambiguous for contracts.** It is unclear whether STATE means "the contract is in force" or "the behaviour runs in the product composition". I tagged DISABLED where the App-owned composition stubs the behaviour, even when the client and route are LIVE (045–048).
  - Proposal: define STATE against the packaged App composition explicitly.
- **Some rows mix reach.** A row can combine a LIVE contract with a TEST_ONLY client method (009, 011). I followed the brief: the tag names the LIVE path, and Notes name the other.
- **EntryPoints cannot distinguish members.** Class members are written `RuntimeClient.<method>` to tell them apart from free functions.
  - Proposal: allow this dotted form explicitly.

## 6. Effort

- Files read partially or by grep: about 25 of the 40 area source files and about 12 consumer files (daemon composition, the App runtime port, `electron/main.ts`, build and boundary scripts), plus the listing of the Runtime tests.
- The import and test maps were computed with scratchpad scripts, not by reading.
- Context was adequate, not tight.
