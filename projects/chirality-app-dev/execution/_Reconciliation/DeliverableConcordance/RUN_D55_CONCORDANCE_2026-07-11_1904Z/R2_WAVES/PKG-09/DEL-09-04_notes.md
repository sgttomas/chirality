# DEL-09-04 concordance notes (R2 Wave-4, PKG-09)

Source state: `frontend/` at `fac46e33f` (byte-identical through HEAD `6f7c06814`; `git diff fac46e33f 6f7c06814 -- projects/chirality-app-dev/frontend` empty). Behavioral verification bound via `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped) plus named test files/line anchors. No tests executed by this agent.

## Census

16 claim rows.

By ClaimType: REQUIREMENT 10; EXCLUSION 2; ACCEPTANCE 1; IMPLEMENTED_UNMAPPED 1; REMAINING_WORK 1; REGISTER_DEFECT 1.

By Disposition: ALIGNED 7; PARTIALLY_IMPLEMENTED 6; STALE_SPECIFICATION 1; IMPLEMENTED_UNDOCUMENTED 1; REMAINING_STATE_MISMATCH 1.

Requirement-index coverage: R1 `REQUIREMENT_INDEX.csv` lists DEL-09-04-REQ-001..010; all ten are re-derived here 1:1 from `Specification.md` (no parser-gap; the regex parser scanned all ten). Exclusions and the PRD-hash acceptance condition are additional (not in the requirement index).

## Reading of the deliverable (packaging-deliverable caveat)

DEL-09-04 is a `CI_CD_CHANGE` packaging deliverable whose acceptance fundamentally requires *produced* artifacts (the assessment's Issuance-Gate observation). At `fac46e33f` there is **no `frontend/dist/`** (DMG/app bundle) and **no `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`** — both are gitignored generated outputs (`.gitignore` lines `dist/` and `artifacts/harness/instruction-root-integrity/latest/summary.json`); direct listing this run found neither. Therefore:

- Config/policy/fail-closed requirements satisfied by config + passing unit tests → **ALIGNED**: REQ-001 (unsigned arm64 macOS 15+ dmg target), REQ-006 (extraResources bundling + integrity chaining), REQ-007 (P0 fail-closed blocker), REQ-010 (no win/linux target), plus EXC-001/EXC-002.
- Requirements whose acceptance needs a produced/probed real artifact → **PARTIALLY_IMPLEMENTED** (script/config/tests present, no source-state-bound produced artifact): REQ-002 (desktop:dist run), REQ-003 (DMG file), REQ-004 (app bundle), REQ-005 (summary.json), REQ-008 (packaged SDK probe), REQ-009 (packaged network proof). The residual work for these is the assessment's four Forward Development Recommendations; it is captured in each row's `RemainingWork` and is **not yet recorded in `_STATUS.md ## Remaining`** (which holds only the concordance bootstrap). That omission is the normal discovery output at this phase (R5 adds ruled residuals), **not** a `REMAINING_STATE_MISMATCH` — flagged here for transparency rather than as a defect row.

## MANDATORY DUTY — packaged-SDK verification surface handle (W3 DEL-08-01 refutation)

At PKG-08 W3 fan-in, DEL-08-01 `UNMAPPED-1` was REFUTED to ALIGNED and folded under DEL-09-04's decomposition assignment (decomposition v3.2 line 363 "prove ... SDK packaging posture are valid" / artifact "SDK subprocess packaging probe"; DEL-09-04 `Specification.md` DEL-09-04-REQ-008, line 32). **Determination: my claim set DOES cover the packaged-SDK verification surface.** DEL-09-04-REQ-008 covers it across three sub-surfaces:

1. `frontend/scripts/verify-packaged-agent-sdk-runtime.mjs` (no-live scripted resolver proof: command under `app.asar.unpacked/node_modules`, controlled `CLAUDE_CONFIG_DIR`/`HOME`) — tested by `verify-packaged-agent-sdk-runtime.test.ts`.
2. `frontend/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs` (live read-tool proof; refuses ambient key, writes no key material) — tested by `run-live-packaged-agent-sdk-read-tool-proof.test.ts`; historically executed and PASSED against an app-directory build under `RULING-RECORD(D-APP-18)` (approved by D-APP-15).
3. The **folded DEL-08-01 handle**: `frontend/scripts/verify-instruction-root-integrity.mjs` `verifyUnpackedSdkBundle` (lines 382-461), the required-unpacked-SDK-files presence check DEL-08-01 UNMAPPED-1 cites. That script's *test-suite ownership* stays on DEL-08-01 (DEL0801-REQ003); its *SDK-bundle verification requirement ownership* is DEL-09-04-REQ-008. No new ownership decision packet is needed — the mapping is accepted in decomposition v3.2 line 363 + DEL-09-04's Specification, matching the DEL-08-01 agent's recorded handle.

REQ-008 remains PARTIALLY_IMPLEMENTED at the source state because the *mechanism* is complete/tested but no current DMG-layout probe artifact exists and the D-APP-18 pass was against the `--dir` app-directory build, not the DMG.

## Least-confident rows (self-flagged; alternative readings that would flip them)

- **DEL-09-04-REQ-008 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative reading → **ALIGNED**: the no-live proof, live read-tool proof, and folded presence check are all present and unit-tested, and `RULING-RECORD(D-APP-18)` records a *passing* app-directory live packaged read-tool proof; one could read the requirement (verify SDK subprocess findable/executable from package layout) as satisfied by that combination. I held PARTIALLY_IMPLEMENTED because (a) no probe artifact is reproducible/bound at `fac46e33f`, (b) D-APP-18's pass was the `--dir` app-directory layout, not the DMG bundle REQ-003/004 name, and (c) Guidance CONF-004 (full packaged SDK-backed turn start as a closure blocker) is unresolved. Flip hinges on whether a historical app-directory ruling record counts as source-state-bound packaged-DMG evidence.
- **UNMAPPED-1 / desktop:pack (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** Alternative reading → **fold into REQ-002 as IMPLEMENTED_DIFFERENTLY / not material**: `desktop:pack` is the `--dir` sibling of the required `desktop:dist` and is the default `bundleRoot` the packaged probes consume, so it could be read as implicit REQ-002/REQ-008 verification tooling rather than an unrequired standalone behavior. I emitted it because no requirement names it and it is a distinct release-significant entrypoint (`docs/CONTRACT.md` K-VALIDATE-1 lists `desktop:dist`, not `desktop:pack`), and it is the exact layout D-APP-18 exercised.
- **REGISTER-1 / _DEPENDENCIES.md REF-006 lag (REMAINING_STATE_MISMATCH, MEDIUM).** Alternative reading → **no defect**: the REF-006 warning sits in `_DEPENDENCIES.md`'s *Run Notes*/*Run History*, which are inherently historical records of the 2026-05-20 extraction run, so presenting the then-true hash mismatch is arguably not a current-truth claim. I emitted it because MR-5 names register *metadata lag* as a REGISTER_DEFECT trigger and the warning is not scoped as historical in-line; the fix is a one-line annotation. The authoritative `_REFERENCES.md` register is itself already correct (REF-006 = MATCH), so the defect is confined to `_DEPENDENCIES.md` narrative.
- **DEL-09-04-REQ-006 (ALIGNED, MEDIUM).** Alternative reading → **PARTIALLY_IMPLEMENTED**: "verify integrity before distribution" is only exercised against synthetic bundle fixtures; no end-to-end produced-DMG integrity run exists. I held ALIGNED because the requirement is structural (bundling config + integrity script + `desktop:dist` chaining + passing tests all present) and fail-closed behavior is separately proven under REQ-007.

## Register-defect summary

One REGISTER_DEFECT: **REGISTER-1** — `_DEPENDENCIES.md` REF-006 HASH_MISMATCH warning lags `_REFERENCES.md` (now MATCH) post D-APP-35/D-APP-38. Disposition REMAINING_STATE_MISMATCH.

Register cross-checks that came back CLEAN (no defect emitted):
- `Dependencies.csv` v3.1 has 9 ACTIVE rows; `_DEPENDENCIES.md` counts (DependencyType OTHER=4/PREREQUISITE=2/CONSTRAINT=3; SatisfactionStatus NOT_APPLICABLE=3/TBD=6; TargetType PACKAGE=1/REQUIREMENT=4/EXTERNAL=2/UNKNOWN=2) all reconcile against the live CSV; the Compact Register matches. `Procedure.md` line 14 ("9 ACTIVE rows; six TBD") agrees.
- DepClosure snapshot `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z/Evidence/coverage.csv` row `DEL-09-04,Y,9,Y,Y` re-verified against the live 9-row register (HasDependencyCsv Y, RowCount 9, SchemaValid Y, HasImplementsNode Y — parent anchor DEP-09-04-001). The six TBD SatisfactionStatus rows (SOW-073, Node/deps prereq, pre-packaging checks, OI-004, OI-003, REQ-009 network guardrails) are legitimately open given the unproduced artifacts and the IN_PROGRESS state — not treated as defects.
- `_REFERENCES.md` REF-001..007 all MATCH; live `shasum -a 256 docs/PRD.md` = `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` = REF-006 Expected==Actual, confirming the register is truthful at the source state.
- `_DEPENDENCIES.md` Declared Upstream/Downstream are both bare "TBD" — per the Wave-4 rule (docs/SPEC.md §5.2 human-owned declaration sections, TBD by design) these are **not** register defects; noted only.

## Decisions consulted (MR-7)

`DECISION_INDEX.csv` names no decision for DEL-09-04/PKG-09; a direct `_REGISTER.md` sweep found: D-APP-35 (Option A refresh accepted REF-006 hash) and D-APP-38 (Option D versioned corpus snapshots, v6) — govern ACC-001 and REGISTER-1; D-APP-15 (approved one bounded live packaged agentSdk read-tool proof) and D-APP-18 (app-directory packaged live read-tool proof PASSED) — govern the REQ-008 live-proof surface. No ruling governs the unsigned/DMG release-target posture (REQ-001), the win/linux exclusion (REQ-010), or the network-guardrail preservation (REQ-009) → NONE_FOUND. Cross-project gate claims: none required (F-APP-3 respected; no other project's execution tree read).

## Method deviations

None. 19-column header copied verbatim from the R0 exemplar; MR-1..MR-11 applied; read-only discovery; no lifecycle transitions; no tests executed.
