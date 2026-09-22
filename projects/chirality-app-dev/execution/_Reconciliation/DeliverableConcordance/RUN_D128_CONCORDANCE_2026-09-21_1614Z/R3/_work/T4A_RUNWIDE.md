# T4A: run-wide consistency calls (a), (b) and (g)

Task T4A, R3. These are consistency calls for this run's rows, not rulings. Evidence comes from the frozen tree at `00115c719` and the run folder.
- Re-mappings are in `R3/_work/T4A_REMAPS.csv`: 260 rows over 205 keys. Call a has 152 rows (132 keys), call b has 108 rows (73 keys), call g has none.
- Scripts are in `R3/_work/T4A_scripts/`: `symbol_use.py`, `groups.py`, `build_remaps.py`, `impact.py`, and `find_*.py`/`scan_*.py`.

## (a) Reach of the barrel-re-exported contract modules

**Evidence**
- Modules in dispute. `REACHABILITY.csv` rows 279–288 say LIVE for all seven. `RTCONTRACT_capabilities.csv` says:
  - TEST_ONLY: `harness/domain-profile.ts` (CAP-RTCONTRACT-040), `operation-proposal.ts` (041), `engine-conformance.ts` (039), `tool-catalog.ts` (043);
  - LEGACY_ONLY: `harness/tool-descriptor.ts` (042), `mcp/tool-names.ts` (044), `sdk-version.ts` (045).
  - All seven live under `projects/chirality-runtime/packages/contracts/src/`. The App re-export is the deprecated facade `frontend/packages/harness-contract/src/*.ts` (2-line `export *` files).
- The module is imported. The pack's chain is `projects/chirality-runtime/packages/daemon/src/standalone-bin.ts:2` (`import { RuntimeError } from "@chirality/runtime-contracts"`)
  > `contracts/src/index.ts:1` (`export * from "./harness/index.js"`) > `contracts/src/harness/index.ts:2-12` (`export *`).
  `standalone-bin.ts` is the packaged service entry: it is bundled by `frontend/scripts/build-electron.mjs:29,113-118` and launched by `frontend/electron/main.ts:461`.
- The relied-on symbols are not used on the live path. `symbol_use.py` scanned every exported symbol against the non-test files of `frontend/src`, `frontend/electron`, `frontend/scripts` and
  `chirality-runtime/packages/*`, excluding `contracts/src` and the facade.
  - domain-profile (19 symbols), operation-proposal (11) and engine-conformance (4) have no consumer.
  - tool-catalog is used only by `frontend/scripts/generate-tool-catalog.mjs:10`, a manual doc generator that call b makes TEST_ONLY.
  - tool-descriptor, tool-names and sdk-version are used only by `frontend/src/lib/harness/*`, and every such file is LEGACY_ONLY in `REACHABILITY.csv`.
    Examples: `tool-pool.ts`, `sdk-options-builder.ts`, `persona-manager.ts`, `runtime-fingerprint.ts`, `mcp/read-tools.ts`, `mcp/domain-proposal-tools.ts`, `claude-agent-sdk-manager.ts`.
  - The App domain registry `lib/harness/mcp/domain-profile-registry.ts` imports only `HarnessError`, and it is LEGACY_ONLY.
- The facade `@chirality/harness-contract` is imported only by `frontend/src/__tests__/lib/harness-contract-rollback.test.ts`.
  `scripts/assert-harness-contract-deps.mjs` only scans for the string; `generate-tool-catalog.mjs:6` names it in a comment.

**Call**
- The relied-on symbol decides the tag, not the barrel edge. domain-profile, operation-proposal, engine-conformance, tool-catalog and the facade files take
  `REACH=TEST_ONLY`; tool-descriptor, mcp/tool-names and sdk-version take `REACH=LEGACY_ONLY`.
- The code supports both readings. At module level, the pack's §9 definition is met. At symbol level, no relied-on symbol runs live. R3 applies the symbol-level reading because:
  - §2.3 judges a claim on the path that meets it;
  - the PKG-09 worker brief already requires it ("confirm that the specific symbol you rely on is reached"), and so do the verifier CORRECTION notes on DEL-01-02#CLM-006.1 and DEL-10-02#REGISTER-4;
  - an `export *` edge carries no behaviour.
- `events.ts` is not in dispute: both sources say UNREACHED.

**Affected rows** (132 keys, 152 remaps)
- Tag changes: 80 LIVE→TEST_ONLY, 69 LIVE→LEGACY_ONLY and 1 LEGACY_ONLY→TEST_ONLY (the DEL-06-02#CLM-035.1 facades).
- Two tags are inserted where one group tag covered modules with different calls (DEL-10-03#CLM-010.4, DEL-10-05#CLM-004.1). The shared tag in SOW-048.2 is split.
- Keys: DEL-06-01 CLM-034.1, 034.2 · DEL-06-02 CLM-003, 004.2, 005, 006, 010.1, 010.3, 010.4, 010.6–010.8, 010.10, 013, 014, 019, 021.1, 026, 027, 032, 035.1, 035.2, STATE-2 ·
  DEL-06-03 CLM-003, 010.1, 010.2, 010.4, 010.9, 010.14, 014, 020, 030, 035.1, 035.2, SEC-1, SEC-2.3 · DEL-06-04 CLM-004.5, 009.5, 009.9, 027 · DEL-06-06 CLM-010.7 ·
  DEL-08-03 CLM-013.11, 031 · DEL-08-04 CLM-003.2 · DEL-10-01 CLM-003.1, 004.1–004.4, 004.6, 006, 007, 011, 012.2–012.9, 012.11, 014, 016.1, 021, 025.1 ·
  DEL-10-02 CLM-003.2, 003.4, 010.4–010.6, 010.9, 010.10, 022, REGISTER-4, REM-1 · DEL-10-03 CLM-003.1, 003.2, 005, 010.1, 010.2, 010.4–010.7, 012.1, 019.1, 025.1, 028, REGISTER-5 ·
  DEL-10-04 CLM-003, 004.1, 004.5, 004.6, 009, 010.1–010.4, 010.6–010.8, 010.11, 012, 016.2, 026, 028 · DEL-10-05 CLM-004.1, 008, 009.3–009.5, 009.7, 024, 029, 030 ·
  EXT DOC:ADDING_A_TOOL#0, #1, #2, #6, #7; DOC:RUNTIME_ENGINE_CONTRACT#6, #7, #9; DOC:TOOL_CATALOG#0, #3; SOW:SOW-037, 044.2, 048.2, 066, 067, 069.
- Dispositions possibly affected (not re-dispositioned here; see `impact.py`):
  - After the tag changes, 91 keys have no LIVE tag left: ALIGNED 45, STALE_SPECIFICATION 23, PARTIALLY_IMPLEMENTED 14, IMPLEMENTED_DIFFERENTLY 4, AUTHORITY_CONFLICT 3, ACCEPTED_DIVERGENCE 2.
  - Where the claim is product behaviour, the Addendum 6/8 subject test may move these rows off ALIGNED, because TEST_ONLY code does not meet a product claim.
    This applies mostly to DEL-10-01/03/04/05 and the DEL-06-02/03 descriptor rows.
  - 28 of the 91 keys now have LEGACY_ONLY as their only non-test code and do not cite R4-Q1, so they are rule-3 candidates: DEL-06-01#CLM-034.1;
    DEL-06-02#CLM-005, 006, 013, 014, 021.1, 026, 035.2; DEL-06-03#CLM-035.2, SEC-2.3; DEL-10-01#CLM-004.3, 004.6, 012.5; DEL-10-02#CLM-003.2; DEL-10-03#CLM-010.5, 028;
    DEL-10-04#CLM-004.5, 009, 010.3, 010.8, 012, 016.2; DEL-10-05#CLM-009.3, 009.4; DOC:ADDING_A_TOOL#0, #2; DOC:RUNTIME_ENGINE_CONTRACT#7; DOC:TOOL_CATALOG#0.
  - Owner-deferred DEL-06-02#CLM-005 and #CLM-032 (Addendum 5) get only a tag change. Their Dispositions and worker B's ledger stand.
    A rule-3 re-derivation that touches them is for R3 to note, not to resolve.

**Limits**
- The symbol scan matches whole words. It would miss dynamic access or renamed re-exports; none was seen.
- Tree-shaking of the `standalone-bin` bundle was not examined. If it removes these modules from the package, the call is stronger.
- Mentions inside NONE_FOUND search statements, and parenthetical mentions with no tag of their own, were left untagged.
  Examples: DEL-01-02#CLM-006.11, DEL-06-03#SEC-2.2, DOC:ADDING_A_TOOL#5, and the facade note in DOC:ADDING_A_TOOL#0.
- Dead symbols inside otherwise LIVE modules were not re-tagged, because they cannot be separated by path: the `delegated.ts` tool-callback types, and `RuntimeEnginePort`/`asHarnessSession` in `engine.ts` (RTCONTRACT 028, 038).

## (b) Reach of build and validation scripts

**Evidence**
- Sources: the frozen `frontend/package.json`, and a caller census over `frontend/scripts/*`, `frontend/src/__tests__` and the in-root workflow `projects/chirality-app-dev/.github/workflows/harness-premerge.yml`.
- The chains:
  - `desktop:prepare` (:41), `desktop:pack` (:42) and `desktop:dist` (:43) chain `instruction-root:prepare`, `runtime:build`, `build`/`build:electron`, `pack-electron.mjs`,
    `desktop:verify-dependencies`, `desktop:verify-codex-pin` and `instruction-root:integrity`.
  - electron-builder runs `finalize-electron-resources.mjs` as `afterPack` (:109) and `sign-electron-runtime-v2.mjs` as `mac.sign` (:154).
  - `pack-electron.mjs` calls `verify-electron-dist.mjs`.
- Standalone entries: `validate:release-quality` (:29), `harness:validate:*` (:19-27), `proof:*` (:32-34), `test` and `typecheck`.
  - No desktop chain invokes them.
  - `validate-release-quality-evidence.mjs:416-431` runs `npm run test` and `typecheck`, and `:8` imports the premerge validator.
  - The in-root workflow runs only `npm run harness:validate:premerge` (:52).
- Callers of the remaining scripts:
  - `run-network-policy-proof.mjs` and `run-packaged-security-proof.mjs` are imported by their tests (PKG-09 VERIFICATION §3).
  - `scan-secret-evidence.mjs` has the `proof:secret-scan` entry and one test.
  - `controlled-ci-runtime.ts` and `build-controlled-ci-runtime.mjs` have only a test caller in the roots. BUILD_notes §4 cites the Root workflow, which is out of the roots.
  - The legacy-path scripts (BUILD CAP-BUILD-031..035) target Claude Agent SDK and Pi packages that `verify-packaged-dependency-boundary.mjs` forbids.

**Call** (one reading per script class, based on how it is invoked)
- **b1 Packaging chain → LIVE.** Default path of `desktop:prepare`, `desktop:pack` or `desktop:dist`, or an electron-builder hook: build-electron, pack-electron,
  prepare-packaged-instruction-root, verify-instruction-root-integrity, verify-codex-pin, verify-packaged-dependency-boundary, finalize-electron-resources, verify-electron-dist and sign-electron-runtime-v2.
  The signing hook is dormant by default (`pack-electron.mjs:86-95`): it stays LIVE with STATE disabled, as every row already has it.
- **b2 Release-artifact generators → LIVE (manual).** `generate-sbom`, `generate-third-party-notices` and `verify-version-identity`. Rows already agree.
- **b3 Release-validation scripts → TEST_ONLY.** They check the product and never build it or run inside it:
  - the release-quality wrapper, `assert-harness-contract-deps`, `validate-harness-premerge`, `-section8`, `-section9` and `harness-section9-manifest.json`;
  - the package.json `test`, `typecheck`, `validate:release-quality` and `harness:validate:*` entries.
- **b4 Proof scripts → TEST_ONLY.** `scan-secret-evidence`, `run-network-policy-proof` and `run-packaged-security-proof`.
  - A `proof:*` entry invokes each one, so Addendum 1 item 4 (code reached from nothing) does not apply.
  - They are not on the legacy SDK/Pi path. The `api.anthropic.com` posture is a stale-content finding, not a reach finding.
- **b5 CI and developer tooling → TEST_ONLY.** `controlled-ci-runtime.ts`, `build-controlled-ci-runtime.mjs`, `generate-tool-catalog.mjs` and `pec-scratch-server.mjs`.
  The legacy modules the fixture imports keep their own tags.
- **b6 Legacy-path scripts → LEGACY_ONLY.** The agent-sdk packaged proofs, the Pi packaged proof, `normalize-pi-lock-integrity` and `verify-pi-supply-chain`.
- **b7 Nothing invokes → LEGACY_ONLY + UNREACHED.** `generate-macos-icon`, `run-pec-bridge-rehearsal` and both `run-dapp52-*`.
- b3 has two supported readings:
  - PKG-09 key 4b counts any package.json release script as LIVE. V-DEL-09-03 used it to keep DEL-09-03#CLM-003 and #CLM-009.12 LIVE.
  - R3 applies TEST_ONLY. §9 anchors reach at product entry points, and a validation wrapper is its own entry, not a step that produces the product.
    The BUILD capability file (R1b) and DOC:README#1 already use TEST_ONLY.

**Affected rows** (73 keys, 108 remaps)
- Tag changes: 98 LIVE→TEST_ONLY; 7 LEGACY_ONLY→TEST_ONLY; 2 TEST_ONLY→LEGACY_ONLY (`verify-packaged-agent-sdk-runtime.mjs` in DOC:README#1 and #5);
  1 TEST_ONLY→LIVE (`verify-instruction-root-integrity.mjs` in DOC:README#5).
- Keys: DEL-06-02 STATE-1 · DEL-09-01 CLM-003, 004, 005, 008, 009.1, 009.3–009.6, 009.8, 012, 013, 016, 017, 018.1–018.5, 019, 022, 023 ·
  DEL-09-02 CLM-003, 005, 007, 009, 010.1, 010.12–010.16, 012.1, 012.3, 014, 018, 019, 020.1, 020.2, 023, 024, 025, 027, 028, REGISTER-3, REM-1 · DEL-09-03 CLM-003, 009.12 ·
  DEL-09-04 CLM-017 · DEL-09-05 CLM-007, 010.1, 010.5, 010.8–010.11, 010.15, 012, 016.1, 020, 021, 022, 023.3, 027 · DEL-09-06 CLM-010.14, 016, 020, 021, REM-3 ·
  EXT DOC:README#1, #5; DOC:VALSTRAT#4.3.
- Dispositions possibly affected:
  - After the tag changes, 48 keys have no LIVE tag left: ALIGNED 27, STALE_SPECIFICATION 14, PARTIALLY_IMPLEMENTED 7.
  - Most of these are claims about the tooling itself, so the subject is the module and the Disposition should hold. PKG-09 VERIFICATION §5.3 found no Disposition that depends on this tag.
  - DEL-09-02#CLM-019 (CONTESTED on HumanDecisionNeeded) is now met only by LEGACY_ONLY code, so its sealed R4-Q1 holds by rule 3.
  - The LEGACY_ONLY proof-script tags on DEL-09-06 are removed, so R3's scripted R4-Q1 re-derivation will not read them as retained-harness obligation.
  - No re-mapped b row newly qualifies for rule 3.

**Limits**
- The Root `.github/workflows/**` is out of the roots. The CI class rests on the in-root workflow and BUILD_notes.
- Script mentions that carry no tag were not given one. Examples: DEL-04-01#CLM-003 and #STATE-2 ("outside the REACH map"), the manifest target lists in DEL-09-02#CLM-010.2–010.11, and DEL-05-04#CLM-010.10.
- Package.json cells were re-mapped only where the cited entry names validation or test commands and nothing else (8 cells).

## (g) RUN_BASIS §5 "GOVERNING, flagged" list

**Evidence**: `execution/_Coordination/_DECISIONS/_REGISTER.md` rows 119–150, the ruling records, read-only git and code.

| Decision | Recorded flag | Frozen-basis evidence | Finding |
|---|---|---|---|
| D-APP-104 | "Git closeout pending" | `06068dfb8` (apply DEL-09-07 APP-HOLD bootstrap) and merge `92a76d21f` (PR #703) are ancestors of `00115c719`. D-APP-107 retired the hold row. D-APP-127 retired the subject (ruling :159-174) | **Stale**: landed, then superseded |
| D-APP-107 | "integration pending" | `e079cbc39` and `be243fdf6` are ancestors. `DEL-09-07_.../ScopeOfWork.md` exists. D-APP-127 supersedes it in whole (:159) | **Stale**: landed, then superseded |
| D-APP-121 | "main/application gates pending" | `frontend/electron/preload.ts:77` has `inlinePdfPreview: false`. The ruling's EffectStatus is HELD | **Accurate** |
| D-APP-122 | "effect HELD until fetched main" | `DEL-02-05/_STATUS.md` history (2026-09-07): PR745 merged as `8275b4a75`. D-APP-127 (:103-110) supersedes only the daemon-target and host-gate parts, and says the presentation loci stand | **Stale** for the presentation effect |
| D-APP-123 | "effect HELD until fetched main" | `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx:1062` passes `primarySessionId` to ActivityStrip. Commit `a52e75449` is the D123 closeout | **Stale** |
| D-APP-125 | "dependent implementation main/contract-held" | Items 1, 2, 4 and 5 are contract finalization, with no observable App surface (EXT: CONTESTED). D-APP-127 supersedes item 3 (:56) | **Accurate** for items 1, 2, 4, 5. Item 3 is retired, not pending |
| D-APP-126 | "owning adoption/main/exact-brief gates remain" | D-APP-127 (:82-101) supersedes all three App-path boundaries. No landed effect was found | Nothing landed, as the flag says. The effect is **retired**, not pending |

**Call**
- EXT's finding is confirmed for D-APP-104, 107, 122 and 123: their flags lag the frozen basis, and the effects landed.
- The flags for D-APP-121 and D-APP-125 items 1, 2, 4 and 5 are accurate.
- D-APP-125 item 3 and D-APP-126 are superseded by D-APP-127, so read their pending wording as retired.
- This is a finding only. RUN_BASIS belongs to HELP_HUMAN and is not edited.

**Affected rows**
- `find_g.py` searched all fields of both concordance files. 28 rows name D-APP-104, 107, 122 or 123: DEL-02-04#REM-2; DEL-02-05#SEC-2.2, SEC-2.3;
  DEL-09-07#SEC-1, SEC-2.1–2.8, SEC-3.1–3.4, SEC-4, STATE-2, STATE-3; DEC:D-APP-104, 107, 122, 123, 127; DEC:REGISTER-1, -2; SOW:SOW-006.2, SOW-024.2.
- None relies on the stale flag. Rows that address the effect already treat it as landed or superseded: DEC:D-APP-104 and 107 say EFFECT_LANDED_THEN_SUPERSEDED;
  DEC:D-APP-122 and 123 are ALIGNED; DEL-02-04#REM-2 says the D-APP-123 effect is now observable; the DEL-09-07 rows rest on D-APP-127;
  DEC:REGISTER-1 and -2 are the stale-register findings themselves.
- No Disposition rests on the flag alone, so call g re-maps nothing.

**Limits**
- Rows citing D-APP-121, 125 or 126 were not checked for reliance, because those flags are accurate or the effect is retired.
- The finding for D-APP-125 items 1, 2, 4 and 5 repeats EXT's CONTESTED reading: the finalization may be owned by Runtime or Root.
