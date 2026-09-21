# Brief — R1b reverse-pass and shared evidence manager (WORKING_ITEMS, Type 1)

**Role:** WORKING_ITEMS. You dispatch TASK workers (Type 2, no delegation) and integrate
their returns. You never edit deliverables and never commit. You return to HELP_HUMAN.

**Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, activated by D-APP-128; this phase is
authorized by D-APP-129 ruling C.

**Placeholders** (supplied at dispatch):
- `<FROZEN_TREE>`: the frozen checkout at `00115c719`.
- `<RUN>`: the run folder.
- `<APP_WORK>`: the working `projects/chirality-app-dev`, used for running the validator.

**Read first:**
- `<RUN>/CONVENTIONS.md`, all of it. It is the adopted rulebook. §5.2 covers capability
  files, §9 the evidence pack, §10 the operating rules.
- `<RUN>/RUN_BASIS.md`, including Addendum 1.
- `<RUN>/R1_INVENTORY/IMPLEMENTATION_SURFACES.csv` and `AREA_SUMMARY.csv`.
- `<RUN>/R0_CALIBRATION/SURFACES/HARNESS_*`, the model output. HARNESS is inventoried,
  but it predates the adopted reach and enabled-state tags (it fails validator v2 with 120
  errors). One extra unit, `HARNESS-TAG`, makes `<RUN>/R2/SURFACES/HARNESS_capabilities.csv`:
  the same rows and IDs, with the tags added and each verified from code. The R0 file is
  not edited. Record any row whose substance changed in `HARNESS_notes.md`.

## Undertaking

### A. Ten capability inventories

One TASK worker per area writes
`<RUN>/R2/SURFACES/<AREA>_capabilities.csv` and `<AREA>_notes.md`, following
CONVENTIONS §5.2.

| Area | Scope (per `IMPLEMENTATION_SURFACES.csv` `Area`) | Notes |
|---|---|---|
| ELECTRON | `frontend/electron/**` | |
| BUILD | `frontend/scripts/**`, `frontend/build/**`, top-level frontend config | Packaging, signing, notarization and release-proof scripts are important for PKG-09 |
| ROUTES | `frontend/src/app/**` | Pages and API routes |
| SHELL | `components/shell/**`, `lib/shell/**` | |
| WOVEN | `components/woven-dialogue/**`, `lib/woven-dialogue/**` | |
| WORKSPACE | `components/{workspace,pipeline,workbench,portal}/**`, `lib/{workspace,pipeline,portal}/**` | Mark retired presentation code that is kept but unmounted (SCA-APP-010) |
| SETTINGS | `components/settings/**`, `lib/{consent,dependencies,lifecycle,runtime-client}/**`, `lib/*.ts`, `types/**`, `packages/**` | Covers the facade and the runtime client |
| RTCORE | `projects/chirality-runtime/packages/{core,cli,daemon}/**` | Runtime service |
| RTCONTRACT | `projects/chirality-runtime/packages/{contracts,client,engine-claude,engine-pi-omlx}/**` | |
| INSTRUCTIONS | `projects/chirality-app-dev/instructions/AGENTS.md` | Small. Inventory the product behaviours the shipped guidance asserts. Audit-only surface (D-APP-129 item 6) |

**Covering tests:**
- App test files live in `frontend/src/__tests__/**`.
- Runtime test files live in `projects/chirality-runtime/tests/**`, plus the package-local
  `packages/cli/test` and `packages/client/test`.

**Reach and enabled state, per row (§5.2):**
- Every row states reach and enabled state, verified from code.
- Runtime modules are `LIVE` when reached from the App's LIVE code through
  `@chirality/runtime-*` imports, or from the runtime-service entry the App packages. Find
  that entry from the frontend build scripts that produce `dist-runtime/runtime-service`.

**No reading deliverable folders.** Capability rows must not be anchored to them.

### B. Shared evidence pack items 1, 2 and 5

Build these once, corpus-wide, at `<RUN>/R2/_shared/EVIDENCE_PACK/`, with scripts in
`<RUN>/R2/_scripts/`, exactly per CONVENTIONS §9. Apply two corrections:
- **Item 2 entry points.** Next.js routes and pages are under `frontend/src/app/**`, not
  `frontend/app/**`.
- **Item 2 coverage.** Also cover `projects/chirality-runtime/packages/*/src/**`, reached
  as described above.

Also write the scripts for items 3 and 4, parameterized by `--package PKG-xx`, so each
package manager builds its own copies identically. Run each script once for all 54
deliverables into `_shared/`, as a check. Write `PACK_MANIFEST.md`.

## Rules

- **Concurrency.** At most **4** of your children run concurrently. Every spawn uses
  `model: "opus"`.
  - Suggested order: 4 areas at a time.
  - Build pack items 1, 2 and 5 yourself or with one TASK. They need only read-only git
    and scripts.
- **Notifications.**
  - Child completion notifications go to HELP_HUMAN, not to you.
  - Do not end your turn while work is outstanding. Poll the output files: sleep 30–60 s
    in a Bash `until` loop, and check for the `#END` line and a passing validator.
  - Stay in-turn until the whole undertaking is done.
- **Validation.**
  - Run `python3 <RUN>/_scripts/validate_ledger.py capabilities <files>` from `<APP_WORK>`
    after each return.
  - A failing file goes back to its worker once, with the errors. After that, a fresh
    worker redoes it.
  - Never patch a child's file yourself.
- **State.** Keep `<RUN>/R2/SURFACES/STATE.jsonl` with one line per dispatch or return:
  `{ts, unit, event, agent_id, model, mechanism, output_sha256, validator}`. You are its
  only writer.
- **Git and paths.**
  - Children may run read-only `git log`, `show` and `blame` against `<FROZEN_TREE>` only.
  - No git writes, installs or test runs.
  - No absolute paths in outputs.
- **Write scope.** You and your children write only under `<RUN>/R2/SURFACES/`,
  `<RUN>/R2/_shared/` and `<RUN>/R2/_scripts/`.

## Return

Return 12 lines or fewer, covering:
- per area: row count and LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED counts;
- validator results;
- SHA-256 of each pack file;
- files covered versus the total per area;
- anything notable (for example, large unreached code).
