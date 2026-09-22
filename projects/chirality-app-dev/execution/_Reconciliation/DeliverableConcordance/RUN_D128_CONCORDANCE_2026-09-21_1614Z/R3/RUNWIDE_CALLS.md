# R3 run-wide consistency calls — RUN_D128_CONCORDANCE_2026-09-21_1614Z

One section per call: the evidence, the call, and the affected rows re-mapped under `R3_RUNWIDE` (each re-mapping is in `REMAP_LOG.csv` with `RuleOrEvidence` naming `RUNWIDE_CALLS.md (<call>)`). Calls were decided from code and records in the evidence roots only, by TASK workers T4A (a, b, g), T4B (c, d, f), T6 (e) and T2B (the disposition consequence of a and b), and integrated by the R3 manager. They are consistency calls for this run's rows, not rulings. Where two readings stayed defensible, both are kept in the rows' Notes.

| Call | Rows re-mapped (keys) | REMAP_LOG lines by field |
|---|---:|---|
| (a) | 132 | CauseTag 1, Disposition 1, ImplementationEvidence 152, Notes 1 |
| (b) | 73 | ImplementationEvidence 108 |
| (c) | 21 | CauseTag 11, Disposition 8, Notes 21, RemainingWork 1 |
| (d) | 89 | Disposition 14, HumanDecisionNeeded 31, Notes 89 |
| (e) | 11 | CauseTag 5, Disposition 5, HumanDecisionNeeded 4, Notes 11 |
| (f) | 28 | HumanDecisionNeeded 2, Notes 30 |
| (g) | 0 | none |

Manager integration notes:
- HumanDecisionNeeded values from (c), (d), (f) and (e) were applied as token operations (add/remove), so tokens added by the Addendum 6/8 R4-Q1 re-derivation and the Addenda 4/7/9 mapping are kept.
- Two manager consistency re-mappings are logged under (c) and (d)/(f) (`_work/MGR_REMAPS.csv`): DEL-05-03#CLM-014.1 RemainingWork → NONE_OBSERVED (consequence of C1), and HumanDecisionNeeded `R4` restored on AUTHORITY_CONFLICT rows DEL-06-04#STATE-2, DEL-09-04#CLM-022 and #CLM-023.3, where CORRECTIONS had set `NO` (MR-11). All three are marked CONTESTED in Notes: the verifiers read them as needing no owner decision, a verdict-field view that was not applied.
- Run-wide reach re-tags (a)/(b) are applied before the R4-Q1 re-derivation, so rule 3 reads the re-tagged cells.

## (a) Reach of the barrel-re-exported contract modules

*Source write-up: `R3/_work/T4A_RUNWIDE.md`.*

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

*Source write-up: `R3/_work/T4A_RUNWIDE.md`.*

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

### Disposition consequence of (a) and (b) (T2B)

*Source: `R3/_work/T2B_NOTES.md`, `T2B_VERDICTS.csv`.* 99 rows whose sealed Disposition says code meets the claim lost every LIVE tag under (a)/(b); each was put through the Addendum 6 subject test.

Task T2B, R3. Input `R3/_work/CAND_SUBJECT.csv` (99 rows). Consistency calls, not rulings.
Outputs: `R3/_work/T2B_VERDICTS.csv` (99 rows), `R3/_work/T2B_REMAPS.csv` (3 rows, 1 key).
Script: `R3/_work/T2B_scripts/t2b_build.py` (the verdicts are recorded in it; it only assembles).
#### Counts
- KEEP_OTHER 67 (PKG-09 34, PKG-10 29, PKG-06 3, EXT 1). KEEP_MODULE 30 (PKG-10 21, EXT 6, PKG-06 3).
- REDISPOSITION 1: DEL-06-01#CLM-034.2 (ALIGNED to IMPLEMENTED_DIFFERENTLY; CauseTag NONE to NATIVE_DELEGATION).
- UNDECIDED 1: DEL-06-03#CLM-010.4. HumanDecisionNeeded is not changed on any row.
#### Patterns
- PKG-09 (call b, 34 rows): every row is about validation, CI or release tooling or its records. TEST_ONLY
  is the tooling's own reach, so the Disposition judges the tooling (as T4A reads it).
- PKG-10 contract shapes (call a): DomainEngineProfile and OperationProposal field sets, enums and guards
  name a type and state only its contract (rule 1). Sealed notes already call the types inert with no
  product caller, so those ALIGNED verdicts were module-level from the start.
- PKG-10 copy, principles, procedures and check definitions are deliverable text. Documentary evidence
  meets them; the re-tagged type was corroboration only.
- Staged-surface rows (DEL-10-01#CLM-004.1, 012.2; DEL-10-04#CLM-004.1, 010.1) were already live-path
  PARTIALLY_IMPLEMENTED. The gated half (no endpoints, apply or protected-path hooks) still holds live.
- Rows resting on absence on every path (no domain output, apply, endpoint or protected write), and the two
  ACCEPTED_DIVERGENCE rows, do not rest on the re-tagged code.
- DEL-10-04#CLM-004.6, 010.4, 028 concern where OpenPipeStress concepts sit. The descriptor is still in the
  public runtime-contracts package. Their notes call it "LIVE"; it is now LEGACY_ONLY by symbol, but the
  location finding is unchanged.
- DEL-06-02#CLM-035.1 and DEL-10-01#CLM-016.1 (IMPLEMENTED_DIFFERENTLY) are module-level readings (moved module).
#### Redisposition
- DEL-06-01#CLM-034.2: "hard-denied outside workspaceWrite" is a permission control (rule 1). The sealed
  ALIGNED judged the LEGACY_ONLY overlay at module level; after call a the descriptor text is LEGACY_ONLY
  too. Live operator modes map to Codex sandbox policy (`codex-supervisor.ts:104-109`,
  `chat-panel.tsx:123-136`), with no Chirality coordination class; delegation is Codex-native.
  IMPLEMENTED_DIFFERENTLY, ALSO_MODULE:ALIGNED, as sibling DEL-06-03#CLM-035.1. Other reading:
  DOCUMENTED_UNIMPLEMENTED if the Codex sandbox is not counted as the mechanism.
#### Undecided
- DEL-06-03#CLM-010.4 ("Tool definitions declare schema, permissions, ..."). A (rule 1, module): fields exist
  (`tool-descriptor.ts:84-106`), so ALIGNED. B (sealed live-path reading): no LIVE code declares Chirality
  tool metadata and the Runtime records `mcpServers: []` (SEE DEL-06-03#CLM-003), so
  DOCUMENTED_UNIMPLEMENTED with ALSO_MODULE:ALIGNED. Neither reading keeps the sealed PARTIALLY_IMPLEMENTED.
#### Least-confident KEEP
- DEL-10-04#CLM-010.3: the partial rests on the registry and the Root validator. The alternative is
  DOCUMENTED_UNIMPLEMENTED on the live path: no validation step runs there, and no domain surface is exposed.

## (c) SoW-conversion parity items (AC-001 / VER-001; D-APP-68, D-GOV-16)

*Source write-up: `R3/_work/T4B_RUNWIDE.md`.*

**Evidence.**
- Population: a script search of both concordances for AC-001/VER-001/parity/D-APP-68/D-GOV-16 gave 126 hits. Most are functional AC-001/VER-001 rows. 42 rows state the SoW conversion itself: legacy content kept (AC-001) or conversion checks run (VER-001).
- D-GOV-16 (Root `docs/governance_harness/_DECISIONS/`, cited by D-APP-68 disposition 2 as "the conversion authority"), items 7–8. The conversion gate needs validator, map, parity, checklist and render results, plus per-deliverable receipts and verifier returns. These live in the Stage-2 wave run. That run is Root `execution/`, outside the evidence roots.
- App `AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A*` hold only the frontend runtime activation, not per-deliverable parity.
- D-APP-68 dispositions 1–2 (`D-APP-68_PACKET_CONCORDANCE_RULINGS_2026-07-19.md:58-71`) repair live CLM rows and citations. They do not rule that any parity check was met.
- T4B recomputed line parity from frozen git (`T4B_scripts/parity.py`: non-empty legacy lines, heading and blockquote markers stripped):
  - DEL-00-02: 209/209 lines kept at fae8e5117 and 670a71ed0. 11 lines changed later: 1 by 7fd0466f9 (D-APP-65) and 10 by 03f4e10d8 (D-APP-68, disposition 1 names the PKG-00/01 rows).
  - DEL-05-03: 248/248 lines kept at e9b9e302c and 571e729d1. One line (R14) changed by 03f4e10d8 (D-APP-68 disposition 7 names DEL-05-03).
- Sealed dispositions on the same fact pattern (no conversion record in the App tree): DOCUMENTED_UNIMPLEMENTED ×3; UNKNOWN ×6; PARTIALLY_IMPLEMENTED ×5; ALIGNED ×2.

**Call (one shape, three sub-classes).**
- **C1: AC-001 legacy content.** This is a present-state documentary fact, checkable from git. The row is ALIGNED when traceability holds and parity is kept, allowing changes made under a ruling that names the rows (MR-11). Two sealed UNKNOWN rows had not recomputed parity. T4B did, so they move to ALIGNED.
- **C2: VER-001 conversion checks with no conversion record in the evidence roots.** This is an off-code event, and the only evidence is an absent record, so the row is UNKNOWN + OWNER_CHECK (Addendum 10). The CauseTag is DOC_HYGIENE. Positive partial records stay in Notes: a validator PASS, or parity markers in git history. The human-review half is an open lifecycle gate on IN_PROGRESS deliverables. This is kept as `ALSO:PARTIALLY_IMPLEMENTED`.
- **C2-R: parity reproduced by an R2 worker.** Unchanged: DEL-04-03#CLM-019.2 ALIGNED, DEL-10-03#CLM-022 ALIGNED, DEL-10-02#CLM-019.2 STALE_VERIFICATION (a note is added only).
- One OWNER_CHECK wording is used on every C2 row, so the rows group in `OWNER_CHECK.md`.

**Affected rows.**
- C1:
  - DEL-00-02#CLM-014.2: UNKNOWN → ALIGNED.
  - DEL-05-03#CLM-014.1: UNKNOWN → ALIGNED, CauseTag DOC_HYGIENE → NONE. Its RemainingWork should be NONE_OBSERVED; that field is outside the T4B remap fields, so the manager sets it.
- C2, Disposition changes to UNKNOWN (CauseTag change in brackets):
  - DEL-00-01#CLM-018.2 DOCUMENTED_UNIMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
  - DEL-00-02#CLM-021.2 PARTIALLY_IMPLEMENTED.
  - DEL-01-01#CLM-018 ALIGNED (NONE → DOC_HYGIENE). The Records half holds.
  - DEL-01-02#CLM-038.4 PARTIALLY_IMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
  - DEL-01-03#CLM-022 and DEL-01-04#CLM-020.2 PARTIALLY_IMPLEMENTED (LIFECYCLE_GATE_PENDING → DOC_HYGIENE).
  - DEL-02-01#CLM-023.2 DOCUMENTED_UNIMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
  - DEL-02-05#CLM-020.1 DOCUMENTED_UNIMPLEMENTED (LIFECYCLE_GATE_PENDING → DOC_HYGIENE).
  - DEL-10-01#CLM-022.2 ALIGNED (NONE → DOC_HYGIENE). The sealed ALIGNED rested on a Root record outside the roots.
  - DEL-10-05#CLM-020.1 PARTIALLY_IMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
- C2, already UNKNOWN:
  - CauseTag only: DEL-02-02#CLM-021.2 (PRE_V3_DRIFT → DOC_HYGIENE).
  - OWNER_CHECK note only: DEL-02-03#CLM-023.2, DEL-02-04#CLM-021.2, DEL-05-03#CLM-020.1, DEL-05-04#CLM-019.2, DEL-10-04#CLM-023.2.
- Notes only, Disposition kept (it stands on other evidence):
  - DEL-03-02#CLM-018 STALE_SPECIFICATION.
  - DEL-05-05#CLM-020.2 STALE_VERIFICATION.
  - DEL-10-02#CLM-019.2 STALE_VERIFICATION.
- Unchanged, outside the class shape:
  - Distinct positive defects: DEL-02-02#CLM-014.2 STALE_SPECIFICATION (SOW-007 trace) and DEL-05-02#CLM-019 STALE_SPECIFICATION (retired kit files in the records list).
  - Mixed functional rows: DEL-06-03#CLM-016 and #CLM-024, DEL-03-03#CLM-013, DEL-01-01#CLM-012.

**Limits.**
- ALIGNED AC-001 rows whose worker checked traceability but not parity were not recomputed:
  - DEL-00-01#CLM-012.2, DEL-01-02#CLM-023.2, DEL-01-03#CLM-013, DEL-01-04#CLM-013.2;
  - DEL-02-01, -03, -04 #CLM-015.2; DEL-02-05#CLM-013.6;
  - DEL-10-04#CLM-016.2, DEL-10-05#CLM-012.1. The same script can confirm them.
- The 0410a15df `decomposition_basis` pin edit touches many converted SoWs. Only DEL-10-02 treats it as invalidating verification (RUN_BASIS §5 known defect). Two readings remain.
- Overlap with T3 (CAND_ADD10): DEL-00-01#CLM-018.2, DEL-01-03#CLM-022, DEL-02-01#CLM-023.2, DEL-02-05#CLM-020.1 and DEL-05-05#CLM-020.2. T4B's class verdict is REMAP_UNKNOWN, except DEL-05-05, which is NOTE_ONLY.

## (d) D-GOV-43 policy rows under R4-Q6

*Source write-up: `R3/_work/T4B_RUNWIDE.md`.*

**Evidence.**
- Script search: rows citing K-PERM-1/6, DIRECTIVE §2.8/§2.10/§4.1/§4.2, Full access, `~/.codex`, approval policy, shared config, pass-through or R4-Q6, together with D-GOV-43. This gave 183 rows. Each AUTHORITY_CONFLICT and IMPLEMENTED_DIFFERENTLY row was read for the clause it turns on.
- The App DIRECTIVE clauses are unamended at 00115c719: §2.8 (`DIRECTIVE.md:115-136`: Chirality owns permission semantics and hard-deny precedence; Claude is the key-aware default); §2.10 (:144-148); §4.1 (:227-248: Anthropic access, API key); §4.2 (:250-270: no ambient settings, no shipped `bypassPermissions`, no remote MCP/plugins or bash before governance).
- CONTRACT K-PERM-1 and K-PERM-6 (`CONTRACT.md:90,95`) are unamended.
- D-GOV-43 item 3 shares the user's Codex configuration and resources. Item 4 leaves approval and sandbox policy to the user, including Full access. Neither item names these clauses. The ruling sits outside the §0 order, so the order does not resolve the conflict. Under CONVENTIONS §1 this is AUTHORITY_CONFLICT with R4-Q6.
- The owner's answer (Addendum 9) is context only. It is not applied.

**Call.**
- Every row whose claim restates one of the six R4-Q6 texts, where live code follows D-GOV-43 item 3 or 4, is AUTHORITY_CONFLICT with `R4-Q6` in HumanDecisionNeeded.
- R4-Q1 stays where rule 3 applies, because only LEGACY_ONLY code meets the claim.
- R4-Q5 stays where the row also turns on K-ENGINE-4 against K-EVENT.
- Plain `R4` stays only for the K-PERM-4/K-PERM-5 half, which R4-Q6 does not name.
- ID→AC rows keep `ALSO:IMPLEMENTED_DIFFERENTLY`.

**Affected rows** (sub-cluster: key sealed → new).
- **SC, shared config and resources:**
  - DEL-01-02#CLM-006.7 and #CLM-018.8: AUTHORITY_CONFLICT, HDN `R4-Q1; R4` → `R4-Q1; R4-Q6`.
  - DOC:RELIANCE#3.8 and #4.8, SOW:SOW-045.2: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT, HDN `R4-Q1` → `R4-Q1; R4-Q6`.
  - HDN `R4` → `R4-Q6`: SOW:SOW-076; SOW:SOW-075.2 (DIRECTIVE §2.6 via the `~/.codex` memories link); DEL-01-04#CLM-003.1, #CLM-003.4, #CLM-006.1, #CLM-010.2, #CLM-023; DEL-01-04#CLM-004.5 (PARTIALLY_IMPLEMENTED, kept).
- **AP, approval policy and permission ownership:**
  - IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT, HDN `R4-Q1` → `R4-Q1; R4-Q6`: DEL-01-02#CLM-006.3, #CLM-007.4,
    #CLM-018.10; DEL-06-01#CLM-003, #CLM-009.3, #CLM-024, #CLM-025.
  - DOC:RELIANCE#3.4 and #4.4: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT, HDN `R4` → `R4-Q1; R4-Q6`.
  - DEL-09-03#CLM-005.8 and #CLM-009.9: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT (HDN already R4-Q6).
  - AUTHORITY_CONFLICT, HDN `R4-Q1` → `R4-Q1; R4-Q6`: DEL-01-02#CLM-044; DEL-01-03#CLM-024; DEL-06-04#CLM-003,
    #CLM-009.7, #CLM-018, #CLM-022; DEL-06-05#CLM-022, #CLM-004.2; DEL-06-03#CLM-004; DEL-09-02#CLM-010.6; SOW:SOW-050.2.
- **FA, Full access:**
  - AUTHORITY_CONFLICT, HDN `R4; R4-Q1` → `R4-Q1; R4-Q6`: DEL-01-04#CLM-003.5, #CLM-006.2, #CLM-010.4, #CLM-024,
    #CLM-025.
  - DEL-06-01#CLM-009.9: `R4` → `R4-Q1; R4-Q6`.
  - DEL-06-01#CLM-004, #CLM-027, #CLM-031: `R4; R4-Q1` → `R4; R4-Q1; R4-Q6`.
  - DEL-01-04#REGISTER-3 (STALE_SPECIFICATION kept): `R4; R4-Q1` → `R4-Q1; R4-Q6`.
  - DEL-06-01#CLM-032 (STALE_SPECIFICATION kept): `R4` → `R4-Q6`.
- **EV, event pass-through:**
  - These rows cite DIRECTIVE §2.10 as well as K-ENGINE-4, so they turn on R4-Q5 and R4-Q6.
  - DEL-01-01#CLM-009.7, #CLM-021.5, #CLM-023: `R4-Q5; R4-Q1` → `R4-Q1; R4-Q5; R4-Q6`.
  - DEL-03-01#CLM-004.1, #CLM-004.6, #CLM-009.2, #CLM-009.7 and DEL-04-05#CLM-026: `R4` → `R4-Q5; R4-Q6`.
  - Belongs to R4-Q5 only, unchanged: DEL-01-02#CLM-018.5. It turns on K-ENGINE-4 against K-EVENT-1 and cites no DIRECTIVE or K-PERM text. DEL-09-03#CLM-023 already carries both.
- **ED, Claude/Anthropic default and API-key UI (UNDECIDED):**
  - The same statement ("Claude Agent SDK / Anthropic remains the first concrete/current path", "key-aware default") is AUTHORITY_CONFLICT on 11 rows and STALE_SPECIFICATION on 23.
  - Reading A: unamended §2.8, not named by D-GOV-43, gives AUTHORITY_CONFLICT.
  - Reading B: §2.8's own clause "Every other provider or harness path requires a fresh governed tranche", with D-GOV-43 and amended K-ENGINE-3 as that tranche. The §0 order then resolves it, as DEL-04-02#CLM-004 reads.
  - Both readings are defensible. Dispositions are kept, and both readings are recorded in Notes on all 34 rows.
  - HDN on the 11 AUTHORITY_CONFLICT rows:
    - DEL-01-01#STATE-1 and DEL-01-02#STATE-1: `R4-Q1; R4` → `R4-Q1; R4-Q6`.
    - DEL-01-02#CLM-040, DEL-01-04#STATE-2, #STATE-4: `R4; R4-Q1` → `R4-Q1; R4-Q6`.
    - DEL-01-03#STATE-1, #STATE-3 and DEL-04-01#CLM-003: `R4-Q1` → `R4-Q1; R4-Q6`.
    - DEL-02-05#CLM-003.1, #CLM-004.2, #CLM-005.2: `R4` → `R4-Q6`.
  - The 23 STALE_SPECIFICATION rows get Notes only: DEL-03-01#CLM-021; DEL-04-01#STATE-2; DEL-04-02#CLM-004,
    #CLM-023, #STATE-1; DEL-04-04#STATE-1; DEL-04-05#STATE-2; DEL-06-01#STATE-1; DEL-06-02#REGISTER-4; DEL-06-03#STATE-1; DEL-06-04#STATE-1; DEL-06-05#REGISTER-5; DEL-09-01..03#STATE-1; DEL-09-04#REGISTER-52; DEL-09-05#REGISTER-55; DEL-09-06#STATE-1; DEL-10-01..05 STATE/REGISTER rows.
- **Adjacent, not R4-Q6** (no change; they turn on clauses R4-Q6 does not name, mostly R4-Q1 or an unframed K-PERM-3/4/5 or K-BASH-1 question):
  - DEL-06-01#CLM-009.1, .2, .4, .5, .6, .7, .12, .15, #CLM-005, #CLM-019, #CLM-028;
  - DEL-06-02#CLM-010.11;
  - DEL-06-04#CLM-004.2, .004.3, .008, .009.1–.009.4, .009.6, .009.8, .009.9, .009.13, .013, .025, .029, .030;
  - DEL-06-05#CLM-003, .005, .008, .009.1–.009.5, .009.12, .009.13, .013, .018, .024, .026, .029;
  - DEL-07-01#CLM-011.4–.011.7 (K-ROOT/K-PATH; .011.6 is Full access through K-ROOT-2), .011.9, .024;
  - DEL-01-02#CLM-006.4, .006.6, .006.10, .013; DEL-01-03#CLM-009.7 (K-RELIANCE-2/§2.9); DOC:RELIANCE#3.5, #4.5,
    #3.11, #4.11; DOC:ADDING_A_TOOL#3; SOW:SOW-027.2, SOW-060.2;
  - DEL-04-02#CLM-009 (a Claude builder scope statement).
- DEL-01-04#CLM-010.3 stays ALIGNED. It names only `~/.claude` files, which live code does not load. Its sibling CLM-023 carries the conflict.

**Limits.**
- 43 of these keys are also in CAND_R4PLAIN (T1). The manager should reconcile T1's R4→R4-Qn mapping with the values above.
- The ID→AC change on 14 rows follows the brief's normalisation. The sealed readings ("authority route: none; the tension is R4-Q1") stay as `ALSO:`.
- The ED split is not resolved. The R4-Q6 packet should include both populations.

## (e) DEL-02-01 half A / half B splits (fresh re-examination)

*Source write-up: `R3/_work/T6_RUNWIDE_E.md`.*

Fresh re-examination against the frozen tree `00115c719`. I formed my reading from the SoW, the
governing sources and the code before I read the halves' cells. Remaps: `R3/_work/T6_REMAPS.csv`.

### Evidence

- **Governing texts keep the legacy UI.** These all keep the loop-first UI and the legacy 3x4 matrix
  as compatibility surfaces until they are separately retired:
  - D-APP-74 ruling (`_DECISIONS/D-APP-74_RULING_2026-07-23.md:94-108`);
  - PRD FR-001 and FR-007 (`docs/PRD.md:591,602`);
  - App DIRECTIVE §4.1 (`docs/DIRECTIVE.md:234`);
  - TYPES §4 (`docs/TYPES.md:139-145`);
  - decomposition SOW-001 and SOW-005 (`_Decomposition/..._v3_2.md:171,175`).

  D-APP-74 adds that "Old-UI retirement requires separate owner acceptance after parity,
  accessibility, compatibility, and packaged Desktop evidence".
- **What the governing rulings do permit.** SCA-APP-010 and D-APP-108 (DEC-025, SOW-001) permit:
  - a frame with no header row;
  - Workbench and Pipeline presentation retired from the active shell, with the code kept;
  - (Q3) `/workbench` and `/pipeline` staying reachable by URL, unlisted and unmounted.

  D-APP-74 and TYPES §4 permit a target shell with no visual matrix.
- **No ruling covers the matrix removal.** No App register row rules the retirement of the matrix or
  the loop-first UI. I searched `_REGISTER.md` for matrix, PORTAL, loop-first, role adoption,
  `9b005c23a`, Pipeline and Workbench. `9b005c23a` touched no App `docs/` file and no App register.
- **Code history.**
  - `03e61f38f` (2026-09-05, implementing SCA-APP-010) made non-dialogue routes render the legacy
    loop-first element (`git show`).
  - `9b005c23a` (2026-09-09) removed that branch and the `?legacy=1` branch. At
    `woven-dialogue-route.tsx:16-18` the route now does `void legacy`.
  - `9b005c23a` also rewrote `agent-matrix.tsx` into a role directory with no grid (`:38-59`).
  - `WovenDialogueShell` ignores `defaultSurface` (`woven-dialogue-shell.tsx:77`).
  - Result: no live path renders PORTAL, the matrix, or the Workbench/Pipeline surfaces.

### Call

1. **Rows about the matrix or PORTAL compatibility surface are not ACCEPTED_DIVERGENCE.** No
   GOVERNING ruling permits removing that surface, and D-APP-74 requires owner acceptance first.
   The matching verdicts are `IMPLEMENTED_DIFFERENTLY` (another live mechanism) or
   `DOCUMENTED_UNIMPLEMENTED` (row and column labels absent on the live path). Both carry R4-Q4 and
   `OTHER:V3_ROLE_ADOPTION`. This matches half A.
2. **Rows about the header only keep ACCEPTED_DIVERGENCE.** SCA-APP-010 obligation 1 (no header
   row) is a GOVERNING ruling. Both halves agree, so there is no change.
3. **Rows about the `/workbench` and `/pipeline` URLs stay ACCEPTED_DIVERGENCE.** The Q3 wording
   still holds literally: reachable, no 404, unmounted. The other reading is recorded in Notes:
   Q3 was implemented as the URL showing the retired surface, and `9b005c23a` removed that. The
   Disposition is not changed.
4. **REQ-010 / CLM-020.8 (unsupported variants) splits between the halves, and both readings stay
   defensible.** The Disposition is kept, and each row gets a marker.

### Affected rows

| Key | Half | Current Disp / HDN | R3 Disp / HDN | Reason |
|---|---|---|---|---|
| CLM-017 | B | ACCEPTED_DIVERGENCE / R4-Q4 | IMPLEMENTED_DIFFERENTLY / R4-Q4 | PORTAL access removed with no ruling; same content as CLM-010.1 (A) |
| CLM-025 | B | ACCEPTED_DIVERGENCE / R4-Q4 | IMPLEMENTED_DIFFERENTLY / R4-Q4 | SEE:CLM-017 row; follows it |
| CLM-020.3 | B | ACCEPTED_DIVERGENCE / NO | IMPLEMENTED_DIFFERENTLY / R4-Q4 | Role directory replaces the 3x4 matrix; matches CLM-010.4 (A) |
| CLM-020.4 | B | ACCEPTED_DIVERGENCE / NO | DOCUMENTED_UNIMPLEMENTED / R4-Q4 | No live row labels; matches CLM-010.5 (A) |
| CLM-020.5 | B | ACCEPTED_DIVERGENCE / NO | DOCUMENTED_UNIMPLEMENTED / R4-Q4 | No live column labels; matches CLM-010.6 (A) |
| CLM-021 | B | STALE_SPECIFICATION / NO | STALE_SPECIFICATION / R4-Q4 | Matrix-test evidence went stale through `9b005c23a`; matches CLM-012.2-.5 (A) |
| CLM-020.8 | B | ACCEPTED_DIVERGENCE / NO | unchanged (marker) | Half A read IMPLEMENTED_DIFFERENTLY (CLM-010.10) |
| CLM-010.10 | A | IMPLEMENTED_DIFFERENTLY / R4-Q4 | unchanged (marker) | Half B read ACCEPTED_DIVERGENCE (CLM-020.8) |
| CLM-010.2 | A | ACCEPTED_DIVERGENCE / NO | unchanged (note) | Q3 holds literally; other reading recorded |
| CLM-020.1 | B | ACCEPTED_DIVERGENCE / NO | unchanged (note) | Same as CLM-010.2 |
| CLM-029.3 | B | ACCEPTED_DIVERGENCE / NO | unchanged (note) | SEE:CLM-020.1 row; same as above |

The CauseTag on the five changed rows goes from `SHELL_REDESIGN` to `OTHER:V3_ROLE_ADOPTION`.

**Checked and consistent, no change** (all `IMPLEMENTED_DIFFERENTLY`, `DOCUMENTED_UNIMPLEMENTED`,
`PARTIALLY_IMPLEMENTED` or `STALE_*` with R4-Q4): SEC-1 to SEC-4; CLM-003, 005, 009, 010.1,
010.4-010.9, 010.11; CLM-012.1-012.5, 015.1; CLM-019, 020.6, 020.7, 026, 029.1, 029.2; REM-4.

CLM-010.3 and CLM-020.2 are header-only and stay ACCEPTED_DIVERGENCE.

### Limits

- **CAUSE2 conflict.** The five changed rows already have `CAUSE2:OTHER:V3_ROLE_ADOPTION` in Notes,
  and Notes can only be appended to. After the CauseTag swap that token equals the primary. The
  appended note records the secondary as SHELL_REDESIGN, and the manager should reconcile it.
- **LatestDecision not changed.** It says D-APP-108 on CLM-017, 025 and 020.3-.5. The ruling that
  governs the matrix clause is arguably D-APP-74. This task's output fields do not cover it.
- **Static reach.** `REACHABILITY.csv` tags `agent-matrix.tsx` and `portal-loop-shell.tsx` as LIVE
  because of imports. The runtime render is voided at `woven-dialogue-route.tsx:18`, so the live
  readings above rest on symbol-level non-render (SYMBOL-UNREACHED), not on the import map.
- **Root D-GOV-42** (the Root record of the adoption) is not on the App GOVERNING map (RUN_BASIS §5).
  Whether it amends the App texts is R4-Q4 itself, and I did not decide it.
- **Not run.** No tests and no builds. Git was read-only against the frozen tree.

## (f) DEL-09-04 / DEL-09-05 release-signing cluster (framed, not resolved)

*Source write-up: `R3/_work/T4B_RUNWIDE.md`.*

**Evidence.**
- Reading 1, STALE_SPECIFICATION (MR-11 through §0):
  - The amended CONTRACT preamble (`CONTRACT.md:17`, 23b3879b3) names K-RELEASE-1 and reads it with D-GOV-43 items 1 and 4. It lists bundle signing and notarization as ordinary integrity.
  - SPEC §19.4 and PRD §7.12/§12.8/NFR-030 name a signed, notarized candidate.
  - K-RELEASE-1 itself says "unless amended" (:138).
  - PRD §6.2 (:339-346) is below CONTRACT and SPEC in the §0 order.
  - V-DEL-09-04 REFUTED the AUTHORITY_CONFLICT reading on CLM-022 and CLM-023.3.
- Reading 2, AUTHORITY_CONFLICT:
  - The K-RELEASE-1 row text and PRD §6.2 are unamended.
  - D-APP-97 (`D-APP-97_RULING_RELEASE_PREPARATION_2026-08-17.md:20`) keeps the F-APP-2 fence on signing, notarization and distribution, and no ruling names F-APP-2 as lifted.
  - The decomposition v3_2 DEL-09-05 row keeps the G6a exact-candidate gate, and D-APP-127 does not name G6a.
  - V-DEL-09-05 graded CLM-026 CONTESTED.
- Done-declaration Q-02 is context only.
- **Question for the owner:** does the amended CONTRACT preamble (with SPEC §19.4 and PRD §12.8) supersede the unsigned/unnotarized target, the F-APP-2 signing fence and the G6a gate for DEL-09-04 and DEL-09-05?

**Call.**
- The rows below form one cluster, marked by Notes+ `R3_CLUSTER:RELEASE_SIGNING`. Dispositions are unchanged.
- MR-11 consistency: DEL-09-04#CLM-022 and #CLM-023.3 are AUTHORITY_CONFLICT but carry `NO`. PKG-09 CORRECTIONS applied only the HumanDecisionNeeded half of V-DEL-09-04's REFUTED verdict.
- The consistent value while the Disposition stands is `R4`. No named question fits: this is not R4-Q6, because K-RELEASE-1 is not a DIRECTIVE or K-PERM text.
- If the manager instead applies the Disposition half of that verdict (STALE_SPECIFICATION), `NO` becomes consistent. That is outside T4B's brief.
- DEL-09-05#REM-2 is REMAINING_STATE_MISMATCH with `NO`, which is consistent. It gets the marker only.

**Affected rows** (all Notes+ `R3_CLUSTER:RELEASE_SIGNING`).
- DEL-09-04:
  - CLM-003.1, 004.3, 008, 009.1, 011.6, 012.2: STALE_SPECIFICATION/NO.
  - CLM-016: IMPLEMENTED_DIFFERENTLY/R4. CLM-017: PARTIALLY_IMPLEMENTED/R4.
  - CLM-022 and CLM-023.3: AUTHORITY_CONFLICT, HDN **NO → R4**.
- DEL-09-05:
  - STATE-1, CLM-003, 009, 010.6, 010.7, 012, 013: STALE_SPECIFICATION/NO.
  - CLM-016.3: AUTHORITY_CONFLICT/R4 (G6a). CLM-016.6: PARTIALLY_IMPLEMENTED/R4.
  - CLM-020 and 023.2: STALE_SPECIFICATION/R4. CLM-026: AUTHORITY_CONFLICT/R4.
  - REM-2: REMAINING_STATE_MISMATCH/NO. REGISTER-52: STALE_SPECIFICATION/NO (G6a, `MOOT:D-APP-127`). STATE-52: STALE_SPECIFICATION/NO.
- EXT: SOW:SOW-072 ALIGNED/NO. It reads the unsigned target as unamended, which is a third disposition of the same text. DOC:BUILDREL#4.14 and #11: STALE_SPECIFICATION/NO.

**Limits.**
- DOC:BUILDREL#10.8 (ALIGNED: "current ordinary output is unsigned") and DEL-09-05#CLM-016.2 are not marked. They describe build output or the phase boundary and do not turn on the question.
- Several cluster rows are also T3 Addendum 10 candidates (signing and notarization events), for example DEL-09-05#CLM-026 and #CLM-016.3.
- The owner's statement that v3.0.1 was notarized is not applied.
- Outside the three calls: DEL-06-04#STATE-2 is also AUTHORITY_CONFLICT with `NO` (from CORRECTION). This breaks the same MR-11 rule, and the manager should check it.

## (g) RUN_BASIS §5 "GOVERNING, flagged" list

*Source write-up: `R3/_work/T4A_RUNWIDE.md`.*

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

