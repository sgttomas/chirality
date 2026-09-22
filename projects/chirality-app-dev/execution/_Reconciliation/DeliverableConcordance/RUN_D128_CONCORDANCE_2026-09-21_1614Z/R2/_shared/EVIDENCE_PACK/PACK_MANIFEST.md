# Evidence pack manifest — shared items 1, 2, 5 (R1b)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the R1b WORKING_ITEMS manager under
  D-APP-129 ruling C and `BRIEFS/R1B_SURFACES_MANAGER.md`; format per `CONVENTIONS.md` §9.
- **Basis:** every file is built from the frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1`
  (`<FROZEN_TREE>` below). Git use is read-only against that tree only (`show`, `blame`, `rev-parse`,
  `cat-file -e`); items 2 and 5 read files without git.
- **Placeholders in commands:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder.
  Commands are run from `<RUN>/R2`.
- **Package managers** copy the three item files (1, 2, 5) byte-for-byte into
  `<RUN>/R2/<PKG-ID>/EVIDENCE_PACK/` and check the SHA-256 below. Items 3 and 4 are built per package
  with the scripts below (`--package PKG-xx`).
- All scripts are deterministic: a re-run on the same frozen tree reproduces the same bytes.

## Shared files (this folder)

| # | File | Rows | SHA-256 | Command |
|---|---|---|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `python3 _scripts/touched_paths.py --frozen <FROZEN_TREE> --out _shared/EVIDENCE_PACK/TOUCHED_PATHS.csv` |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `python3 _scripts/reachability.py --frozen <FROZEN_TREE> --harness-caps <RUN>/R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv --out _shared/EVIDENCE_PACK/REACHABILITY.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `python3 _scripts/dapp127_map.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --out _shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv` |

Rows exclude the header and the `#END` record.

## Per-package scripts (items 3 and 4)

| # | File | Script (SHA-256) | Per-package command |
|---|---|---|---|
| 3 | `REFERENCE_HASHES.csv` | `_scripts/reference_hashes.py` (`9a2af186dfc9b8ed4f71ba1e94c8e0990cb5ae329031072c640a17e3bdc7c30c`) | `python3 <RUN>/R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-xx --out <RUN>/R2/PKG-xx/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | `_scripts/decision_hits.py` (`0c452b6da528c1a8613d1ce078d8d015539719f177c902a349c96d85cf06bbfb`) | `python3 <RUN>/R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-xx --out <RUN>/R2/PKG-xx/EVIDENCE_PACK/DECISION_HITS.csv` |

**Corpus-wide check run** (all 54 deliverables, `--all`), kept at `<RUN>/R2/_shared/ALL_DELIVERABLES_CHECK/`
and not part of any package pack:

| File | Rows | SHA-256 |
|---|---|---|
| `REFERENCE_HASHES.csv` | 162 (54 × 3) | `b155451494e8c8f3de887b9f54f6bf0e6e9ce2520237afa62baafcae2f6186d3` |
| `DECISION_HITS.csv` | 6,084 | `95da0296bd8dc4c92a4917735f1bbfacf1958a9e15c2b1267dc5004ad8c5f525` |

Check: the `--package PKG-03` output of each script equals the `DEL-03-*` rows of the `--all` output
(verified by diff).

Other scripts: `_scripts/state_log.py` (`ec2d73c82de2d6713313ea4bf344d6af5a72ebd36c2bfc3a439215dfe5463029`)
appends to `R2/SURFACES/STATE.jsonl`; it builds no pack file. The per-script docstrings are the
normative method statement.

## Method notes and findings

### Item 1: `TOUCHED_PATHS.csv`
- `git -C <FROZEN_TREE> show --name-only --format= <c>` for `da95ec194`, `cb08dbe2f`, `9ecbdecdf`,
  `ccb95e06a`; then `git blame --line-porcelain 00115c719 -- <path>` per existing path, grouping
  maximal runs of final-line numbers blamed to the commit.
- 28 distinct paths are touched (file lists: `da95ec194` 15, `cb08dbe2f` 3, `9ecbdecdf` 8,
  `ccb95e06a` 5); 26 of them have rows. The App/Runtime code paths are all under
  `projects/chirality-runtime/packages/{client,contracts,core,daemon}/src/**`. `9ecbdecdf` touches only
  `projects/chirality-runtime/execution/_Coordination/**`. That tree is out of bounds for reading, but
  the pack lists it because the rule is path-based. `ccb95e06a` touches exports, a tranche manifest, a CI action
  and `frontend/electron/plan-export-ipc-contract.ts`.
- **No deleted paths.** Some existing touched paths have no line blamed to the commit, so they have
  no row. The commit deleted lines only, or later commits re-touched every line. These are
  `.github/actions/setup-piping-e2e/action.yml` and
  `projects/chirality-app-dev/frontend/electron/plan-export-ipc-contract.ts`, both from `ccb95e06a`.
- No `frontend/**` line is blamed to any of the four commits.

### Item 2: `REACHABILITY.csv`
- Brief corrections applied:
  - entry points are under `frontend/src/app/**`;
  - coverage includes `projects/chirality-runtime/packages/*/src/**`.
- **Entry points (54):**
  - the Next.js special files under `frontend/src/app/**`: 44 `route.ts`, 4 `page.tsx`, `layout.tsx`
    and `not-found.tsx`;
  - `frontend/electron/main.ts`;
  - `frontend/electron/preload.ts`, which `frontend/scripts/build-electron.mjs` bundles as its own
    entry;
  - the two Runtime bundles the App packages (`build-electron.mjs`, `package.json`
    `build.extraResources`): `packages/daemon/src/standalone-bin.ts` (`dist-runtime/runtime-service`)
    and `packages/cli/src/bin.ts` (`dist-runtime/runtime-cli`).
- **Resolution:**
  - relative specifiers, with `.js` mapped to `.ts`, and index files;
  - `@chirality/runtime-*` and `@chirality/engine-*` through each package's `exports` or `main`,
    with dist mapped to src (the same mapping as `build-electron.mjs` `runtimePackagePlugin`);
  - `@chirality/harness-contract` through its source `exports`.
- **Edges:**
  - static `import` and `export … from`, side-effect imports, and string-literal `import()` and
    `require()`;
  - **type-only imports and exports are not edges**, because they are erased at build.
- **LEGACY_ONLY seeds.** 43 files are named in the `Paths` of HARNESS R0 rows whose Notes carry
  `LEGACY-IN-PROCESS:`. They were re-verified: a seed reached from LIVE code is LIVE.
- **Result, 348 modules:** LIVE 280, LEGACY_ONLY 43 (all under `frontend/src/lib/harness`),
  TEST_ONLY 20, UNREACHED 5.
  - The UNREACHED modules are `app/api/working-root/workflow/workflow-read-contract.ts`,
    `lib/woven-dialogue/contracts.ts`, `contracts/src/events.ts`, `daemon/src/hosted.ts` and
    `engine-claude/src/index.ts`. Several of them are types-only.
- **Known limits, for workers:**
  1. **Module-level, not symbol-level.** A module re-exported through a barrel (`export *`) that
     LIVE code imports counts as LIVE even if no LIVE code uses its symbols. The RTCORE and
     RTCONTRACT capability files refine this at symbol level, and their Notes govern capability tags.
  2. **Type-only modules show as UNREACHED or TEST_ONLY** even when LIVE code consumes their types.
     The area briefs tag such capabilities `REACH=LIVE` with `TYPE-ONLY`.
  3. Scripts under `frontend/scripts/**` are traversed but are not entry points. Modules reached
     only from scripts are UNREACHED unless a seed or a test reaches them.
  4. `frontend/packages/**` (the deprecated `@chirality/harness-contract` facade) is traversed but
     gets no rows, because it is outside the §9 row scope. No production importer resolves to it.
  5. **Unmarked type-only imports count as edges.** An import that names only a type but has no
     `type` keyword counts as a runtime edge, although the compiler erases it. For example,
     `app/api/harness/scaffold/route.ts:3` imports `CoordinationMode`, so `lib/harness/scaffold.ts`
     shows LIVE. The HARNESS capability file (CAP-HARNESS-052) keeps it LEGACY_ONLY and records
     why.
  6. Import detection is regex-based. `import()` and `require()` on comment lines (`//`, `*`) are
     skipped.

### Item 5: `D-APP-127_APPLICATION_MAP.csv`
- 54 deliverables × 5 carriers, taken from `R1_INVENTORY/DELIVERABLE_INVENTORY.csv`.
- **YES** means a carrier line cites `D-APP-127` or `D-GOV-43` and states an applied effect, i.e.
  the same line matches `application|applied|revised|re-pointed|retired`. **PARTIAL** means it cites
  them without such a line.
- **Result:**
  - `_STATUS.md` is `YES` for 11 deliverables: DEL-02-05, 03-01, 03-02, 03-03, 03-04, 05-02,
    09-03, 09-04, 09-05, 09-06 and 09-07.
  - Every other carrier is `NO`, or `ABSENT` for the 2 missing `Dependencies.csv` files. No
    `ScopeOfWork.md`, `_CONTEXT.md`, `Dependencies.csv` or `_REFERENCES.md` cites D-APP-127 or
    D-GOV-43.
- The map records carrier text only. It does not judge which deliverables D-APP-127 should reach.

### Item 3 and 4 check-run findings (corpus-wide)
- **REFERENCE_HASHES.** 51 deliverables record CONTRACT, SPEC and PRD hashes with verdict `MATCH`.
  None of the 153 reproduces at the frozen basis: `Match = NO` everywhere. The recorded hashes are
  a single set (`fa8fc9dc…`, `01e1c75c…`, `8649ccba…`); the recomputed ones are `57411f8d…`,
  `8b0d805b…` and `17ca3f3c…`.
  - DEL-09-07 records the same hashes in list form, with no verdict.
  - DEL-00-01 and DEL-00-02 record none of the three documents.
- **DECISION_HITS.** 6,084 rows:
  - DELIVERABLE 5,867 (RULED 5,718, ROOT/D-GOV 128, AWAITING_RULING 21);
  - REGISTER 69;
  - RULING 148.
  - Every cited D-APP ID exists in the register.
