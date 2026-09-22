# Pre-gather brief — read-only evidence map (TASK, Type 2) — PKG-06

You are a read-only evidence-gathering TASK (Type 2) in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`,
dispatched by the PKG-06 manager under CONVENTIONS §10 (pre-gather list). You do not delegate.
Your prompt supplies `<DEL-ID>`, `<DEL-FOLDER>`, `<OUT>` and the values of `<FROZEN_TREE>`, `<RUN>`.

**Output:** exactly one file, `<OUT>/PREGATHER.md`. **You write no dispositions, no judgments of
alignment and no ledger rows** — a later worker does that. Never write an absolute path; use
repo-relative paths (`projects/chirality-app-dev/frontend/...:line`).

## Inputs

- The deliverable at `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/<DEL-FOLDER>/`.
- Its indexed units: rows of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` with `DeliverableID = <DEL-ID>`
  (read by script; note `SubItems`).
- `<RUN>/R1_INVENTORY/HINTS/<DEL-ID>.csv`, `IMPLEMENTATION_SURFACES.csv` (Area per path),
  `VERIFICATION_INDEX.csv` (test files).
- `<RUN>/R2/PKG-06/EVIDENCE_PACK/REACHABILITY.csv` (pack item 2) for REACH tags and
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

Format: a Markdown table per SoW section, columns `Unit | Label | Candidate code (REACH) | Candidate tests | Remarks`.
Remarks are factual pointers only (e.g. "symbol renamed; see x.ts:40"), never verdicts.

## Discipline

- Read from `<FROZEN_TREE>` only; never the working repository's deliverable folders; never
  `projects/chirality-runtime/execution/**` or another project's execution tree; never
  `<RUN>/R0_CALIBRATION/**` or other workers' folders.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No installs, test runs or builds.
- Grep before you read; read line ranges.
- Return ≤ 5 lines: units covered, units with NO_CANDIDATE, and the file's SHA-256.
