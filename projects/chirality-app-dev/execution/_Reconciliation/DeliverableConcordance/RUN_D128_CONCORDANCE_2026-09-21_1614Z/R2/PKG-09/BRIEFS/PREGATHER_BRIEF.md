# Pre-gather brief — read-only evidence map (TASK, Type 2) — PKG-09

You are a read-only evidence-gathering TASK (Type 2) in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-09 manager under CONVENTIONS §10 (pre-gather list). You do not delegate.
Your prompt supplies `<DEL-ID>`, `<DEL-FOLDER>`, `<OUT>` and the values of `<FROZEN_TREE>`, `<RUN>`.

**Output:** exactly one file, `<OUT>/PREGATHER.md`. **You write no dispositions, no judgments of
alignment and no ledger rows** — a later worker does that. Never write an absolute path; use
repo-relative paths (`projects/chirality-app-dev/frontend/...:line`).

## Inputs

- The deliverable at `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/<DEL-FOLDER>/`.
- Its indexed units: rows of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` with `DeliverableID = <DEL-ID>`
  (read by script; note `SubItems`).
- `<RUN>/R1_INVENTORY/HINTS/<DEL-ID>.csv`, `IMPLEMENTATION_SURFACES.csv` (Area per path),
  `VERIFICATION_INDEX.csv` (test files).
- `<RUN>/R2/PKG-09/EVIDENCE_PACK/REACHABILITY.csv` (pack item 2) for REACH tags and
  `TOUCHED_PATHS.csv` (item 1) to flag post-release-touched files.
- Code and tests: `<FROZEN_TREE>/projects/chirality-app-dev/frontend/**`,
  `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`.

## Method

For every indexed unit (and each listed sub-item), list the candidate implementation paths
(file:line or symbol) and candidate test files/cases, each code path with its REACH tag from
`REACHABILITY.csv` (`REACH=LIVE|LEGACY_ONLY|TEST_ONLY`, `UNREACHED` → `REACH=LEGACY_ONLY` +
`UNREACHED`), and `TOUCHED` if the path appears in `TOUCHED_PATHS.csv`. Write `NO_CANDIDATE`
with the grep terms you tried when you find none; mark purely documentary units `DOC_ONLY`.
Also list, at the top: the deliverable's key files and sizes, the decision IDs it cites
most, and the main code areas involved.

`REACHABILITY.csv` does not cover build/packaging scripts (`frontend/scripts/**`, builder config,
`frontend/package.json` scripts, `projects/chirality-app-dev/.github/workflows/**`). For those, record which
`package.json` script or in-root workflow step invokes the file (e.g. `pack:mac -> scripts/pack-electron.mjs`), or
`NO_INVOKER_FOUND`, and note code branches that are off by default (e.g. signing without an identity). Record
also the recorded proof artefacts (evidence files, run records) for each unit, separately from code.

The REACH tag is the module-level map value and is a **hint only**: the map is import-based, so a
re-export or one imported helper marks a whole module LIVE. Where you can see cheaply that the cited
symbol is (or is not) called from an actual entry point (rendered page/component, executed API route,
`frontend/electron/main.ts`, packaged runtime-service entry), add a factual Remark
(e.g. "symbol X not called from any route; only tests import it"). Search Runtime code only under
`projects/chirality-runtime/packages` and `projects/chirality-runtime/tests` — never list or grep
`projects/chirality-runtime/execution/**`.

Format: a Markdown table per SoW section, columns `Unit | Label | Candidate code (REACH) | Candidate tests | Remarks`.
Remarks are factual pointers only (e.g. "symbol renamed; see x.ts:40"), never verdicts.

## Discipline

- Evidence roots are strict: `<FROZEN_TREE>/projects/chirality-app-dev/**` except other packages'
  deliverable folders, `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`, and the run-folder
  inputs named here. Never Root `execution/`, the repository-root `.github/**`, or
  `projects/chirality-runtime/execution/**`. Where evidence lies only outside these roots, write
  `OUT_OF_ROOT:<path>` without reading it.
- Read from `<FROZEN_TREE>` only; never the working repository's deliverable folders; never
  `projects/chirality-runtime/execution/**` or another project's execution tree; never
  `<RUN>/R0_CALIBRATION/**`, other workers' folders, or any other `<RUN>/R2/PKG-*` folder.
- Write only `<OUT>/PREGATHER.md`; never an absolute path in it.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No installs, test runs or builds.
- Grep before you read; read line ranges.
- Return ≤ 5 lines: units covered, units with NO_CANDIDATE, and the file's SHA-256.
