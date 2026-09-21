# Brief — R1a TASK: deterministic inventories

**Role:** TASK (Type 2); you do not delegate. **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`
(D-APP-128; overlap with the R0 gate authorized by ruling §5.5.6). Placeholders supplied at
dispatch: `<FROZEN_TREE>` (read-only checkout at `00115c719`), `<RUN>` (run folder in the
working repository), `<APP>` = `<FROZEN_TREE>/projects/chirality-app-dev`,
`<RT>` = `<FROZEN_TREE>/projects/chirality-runtime`.

## Purpose

Produce source-state-bound inventories **by script, with no model judgment in any CSV
cell**, so R2 workers and R3 synthesis have deterministic coverage checklists.
`R1_INVENTORY/CLAIM_INDEX.csv` and `_scripts/claim_index.py` already exist and are owned by
HELP_HUMAN: do not modify them (read them for key formats).

## Outputs (all under `<RUN>/R1_INVENTORY/`; scripts under `<RUN>/R1_INVENTORY/_scripts/`)

Every CSV has a header and ends with a final line `#END`. Paths are repo-relative. Save each
generating script; each must run as `python3 <script> --frozen-root <FROZEN_TREE> --out <file>`.

1. `DELIVERABLE_INVENTORY.csv` — `PackageID,DeliverableID,Path,LifecycleState,LastUpdated,SoWLines,ClaimUnits,RemainingItems,GatedRemainingItems,AssessmentFile,AssessmentDate,DecompositionBasis,HasDependenciesCsv` (54 rows; `ClaimUnits` counted from CLAIM_INDEX).
2. `REMAINING_INVENTORY.csv` — `ClaimKey,DeliverableID,ItemText,ParsedGates,ParsedDepends` for every REM/REMTXT unit in CLAIM_INDEX; gates are verbatim `(gated: …)`, `(stage-gated: …)`, `NOT_SELECTABLE_UNTIL: …` fragments.
3. `DECISION_INDEX.csv` — `DecisionID,State,StateCellVerbatimShort,PacketPath,RulingPath,EffectFlag,DeliverablesNamed,PackagesNamed` from `<APP>/execution/_Coordination/_DECISIONS/_REGISTER.md` (all rows). `EffectFlag` = `PENDING_EFFECT` when the state or ruling cell contains any of `pending|HELD|held|remain|not applied|awaiting` (case-insensitive), else `NONE` — a mechanical flag only.
4. `VERIFICATION_INDEX.csv` — `Root,TestFile,LOC,TestCount` for every `*.test.ts(x)` under `<APP>/frontend/src/__tests__/**` and `<RT>/tests/**` (`TestCount` = count of `it(`/`test(` call sites).
5. `IMPLEMENTATION_SURFACES.csv` — `Root,Path,LOC,Area` for every non-test source file (`.ts,.tsx,.mjs,.js,.cjs,.json` in package dirs, `.css`) under `<APP>/frontend/{src,electron,packages,scripts,build}` (excluding `src/__tests__`), `<APP>/frontend/{package.json,next.config.mjs,tsconfig*.json}`, `<APP>/instructions/**`, and `<RT>/packages/**` (excluding `dist`, `node_modules`). `Area` by first matching rule:
   - `ELECTRON` `frontend/electron/**`
   - `BUILD` `frontend/scripts/**`, `frontend/build/**`, frontend top-level config files
   - `ROUTES` `frontend/src/app/**`
   - `HARNESS` `frontend/src/lib/harness/**`
   - `SHELL` `frontend/src/components/shell/**`, `frontend/src/lib/shell/**`
   - `WOVEN` `frontend/src/components/woven-dialogue/**`, `frontend/src/lib/woven-dialogue/**`
   - `WORKSPACE` `frontend/src/components/{workspace,pipeline,workbench,portal}/**`, `frontend/src/lib/{workspace,pipeline,portal}/**`
   - `SETTINGS` `frontend/src/components/settings/**`, `frontend/src/lib/{consent,dependencies,lifecycle,runtime-client}/**`, `frontend/src/lib/*.ts`, `frontend/src/types/**`, `frontend/packages/**`
   - `RTCORE` `chirality-runtime/packages/{core,cli,daemon}/**`
   - `RTCONTRACT` `chirality-runtime/packages/{contracts,client,engine-claude,engine-pi-omlx}/**`
   - `INSTRUCTIONS` `chirality-app-dev/instructions/**`
   - `UNASSIGNED` anything else (must be reported; target zero).
   Also emit `AREA_SUMMARY.csv` — `Area,Files,LOC`.
6. `DIRECTION_RECORD_INDEX.csv` — `Path,Kind,Date,Title,SHA256` for `<FROZEN_TREE>/plans/chirality_app_v3_*`, `<FROZEN_TREE>/plans/steers/chirality_app_v3_*`, `<APP>/execution/_ScopeChange/SCA-APP-00[89]*/**/*.md` (top two levels only), and each `<APP>/execution/_Coordination/AgentRuns/{APP_V3_*,APPDEV_V3_NODE_*,CHIRALITY_V3_*}/` folder's handoff/owner files (`HANDOFF*`, `OWNER*`, `*RULING*`). `Kind` from filename pattern.
7. `HINTS/<DEL-ID>.csv` (54 files) — `ClaimKey,Token,HitPath,HitLine` — for each CLAIM_INDEX unit, extract candidate identifiers mechanically from the claim's block text in the frozen SoW (backticked tokens, CamelCase identifiers ≥ 6 chars, file-like tokens with `/` or a code extension, `SOW-nnn`/`REQ-…`/`K-…` IDs), then grep them (fixed-string, case-sensitive) across the §5 implementation roots and the two test roots; keep at most 5 hits per token and 40 per unit. Hints are pointers, not evidence; header comment row not allowed — plain CSV + `#END`.
8. `R1_NOTES.md` — method table (file → script → rule), counts, anything UNASSIGNED, parser caveats, and the SHA-256 of every output.

## Rules

Read `<FROZEN_TREE>` only (never the working repository's deliverables); do not read
`projects/chirality-runtime/execution/**`. Write only under `<RUN>/R1_INVENTORY/` (not
`CLAIM_INDEX.csv`). No git, installs, or test runs. No absolute machine paths in outputs.
Scripts must be deterministic (sorted output).

## Return

Short: each output path with row count, the `AREA_SUMMARY` table, the UNASSIGNED count, and any
parser caveat. Do not paste CSV contents.
