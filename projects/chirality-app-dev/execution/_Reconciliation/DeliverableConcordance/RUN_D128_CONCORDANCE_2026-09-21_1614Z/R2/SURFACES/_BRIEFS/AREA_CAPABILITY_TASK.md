# Brief — R1b area capability inventory (TASK, Type 2)

**Role:** TASK (Type 2). One bounded assignment. You do not delegate, do not spawn agents,
do not commit. Parent: the R1b WORKING_ITEMS manager of run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`
(authorized by D-APP-129 ruling C). Your prompt names `<AREA>` and supplies the placeholder values
`<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.

## Read first

1. `<RUN>/CONVENTIONS.md` §5.2 (capability file), §7 (reading discipline), §9 item 2 (reach vocabulary).
   Read §1–§4 only if you need vocabulary context; you write no ledger.
2. `<RUN>/R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` and `HARNESS_notes.md`: the model output
   (format, granularity, notes layout). It predates the reach/state tags; yours must carry them.
3. Your file list: the rows of `<RUN>/R1_INVENTORY/IMPLEMENTATION_SURFACES.csv` whose `Area` is `<AREA>`.
   That list is authoritative for "files covered versus total".
4. Evidence pack (built by the manager at `<RUN>/R2/_shared/EVIDENCE_PACK/`):
   - `REACHABILITY.csv`: static reach per module (`LIVE`, `LEGACY_ONLY`, `TEST_ONLY`, `UNREACHED`)
     with the shortest import chain. Method: see the docstring of `<RUN>/R2/_scripts/reachability.py`.
     Type-only imports are **not** reach edges there.
   - `TOUCHED_PATHS.csv`: line ranges (frozen basis) last changed by the four post-release commits.

## Output (write only these two files)

- `<RUN>/R2/SURFACES/<AREA>_capabilities.csv`
- `<RUN>/R2/SURFACES/<AREA>_notes.md`

### Capability CSV (CONVENTIONS §5.2)

Header exactly: `CapabilityID,Area,Capability,Paths,EntryPoints,CoveringTests,PostReleaseBasis,Notes`
then data rows, then a final record `#END`. UTF-8, standard CSV quoting.

- `CapabilityID` `CAP-<AREA>-001`… sequential, 3 digits. `Area` = `<AREA>`.
- **Granularity:** one row per user- or system-observable behaviour or contract surface a deliverable
  could plausibly own; not per file or function. **Target 20–60 rows.** Fold helpers into the behaviour
  they serve. No owner column; do not name deliverables as owners.
- `Paths`: repo-relative paths (e.g. `projects/chirality-app-dev/frontend/src/lib/x.ts`), `;`-separated.
- `EntryPoints`: exported symbols, and/or repo-relative consumer paths, `;`-separated.
- `CoveringTests`: repo-relative test paths `;`-separated, or `NONE_FOUND`. Mark indirect coverage
  with a ` (indirect)` suffix on that path. App tests: `projects/chirality-app-dev/frontend/src/__tests__/**`.
  Runtime tests: `projects/chirality-runtime/tests/**`, `packages/cli/test/**`, `packages/client/test/**`.
- `PostReleaseBasis`: `YES` if code this capability relies on falls inside a `TOUCHED_PATHS.csv` line
  range (confirm with read-only `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` when in doubt);
  else `NO`.
- `Notes` **must** contain, verified from code (not inferred from names):
  - `REACH=LIVE`, `REACH=LEGACY_ONLY` or `REACH=TEST_ONLY` (only these three values).
    Use `REACHABILITY.csv` as the static map and confirm it. Where it says `UNREACHED`, write
    `REACH=LEGACY_ONLY` and the word `UNREACHED` (Addendum 1 item 4). If a capability spans paths
    of different reach, tag the capability by its live path and name the other paths' reach
    (e.g. `REACH=LIVE; legacy fallback in b.ts REACH=LEGACY_ONLY`).
    A pure type/contract module consumed by LIVE code only through `import type` is `REACH=LIVE`
    with `TYPE-ONLY` in Notes (the pack shows it UNREACHED/TEST_ONLY because type edges are erased).
  - `STATE=ENABLED` or `STATE=DISABLED`: whether the behaviour is switched on at the frozen basis
    (feature flags, env gates, platform gates, unmounted/retired UI, stubs that throw, config defaults).
    Cite the gate briefly (`STATE=DISABLED (flag X default false, file:line)`).
  - Anything else short: observed dead code, retired-but-kept presentation code, duplicate surfaces.
- No absolute paths anywhere; no machine-specific paths.

### Notes file `<AREA>_notes.md`

Sections (follow `HARNESS_notes.md`):
1. **Census:** row count; counts of REACH=LIVE / LEGACY_ONLY / TEST_ONLY; count of rows marked
   `UNREACHED`; STATE=ENABLED / DISABLED counts. Put them on one line exactly like:
   `CENSUS rows=N LIVE=a LEGACY_ONLY=b TEST_ONLY=c UNREACHED=d ENABLED=e DISABLED=f`
2. **Granularity rationale.**
3. **Files covered versus total:** `COVERAGE covered=X total=Y` (files of your Area list named in at
   least one row's `Paths`), and list every uncovered file with the reason (e.g. stylesheet, config, `.d.ts`).
4. **Dead, unreached, disabled or retired code observed** (with evidence).
5. **Method friction** with §5.2, with a proposed revision.
6. **Effort:** approximate files read; whether the context budget was tight.

## Rules

- **Read from `<FROZEN_TREE>` only** (repo-relative paths resolve there). Never read the working
  repository's code or deliverables.
- **Do not read deliverable folders** (`projects/chirality-app-dev/execution/**`, any `DEL-*` folder)
  or `projects/chirality-runtime/execution/**`. Capability rows must not be anchored to deliverables.
- **Git:** only read-only `git -C <FROZEN_TREE> log`, `show`, `blame -L`. Nothing against the working
  repository. No installs, builds or test runs.
- **Economize:** grep before reading; read line ranges; compute import/test maps with small read-only
  scripts in your scratchpad if useful (never write scripts into the run folder).
- **Validate** before returning, from `<APP_WORK>`:
  `python3 <RUN>/_scripts/validate_ledger.py capabilities <RUN>/R2/SURFACES/<AREA>_capabilities.csv`
  Errors must be zero.
- **Return** (≤ 8 lines): output paths (repo-relative), the CENSUS and COVERAGE lines, validator
  RESULT line, `shasum -a 256` of the CSV, and anything notable.
