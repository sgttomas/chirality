# Brief — R2 PKG-08 pre-gather TASK (Type 2, read-only evidence gathering)

**Role.** TASK (Type 2). Do not delegate. Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128;
R2 authorized by D-APP-129). Manager: the PKG-08 WORKING_ITEMS manager.

**Placeholders** (values are given in your dispatch prompt; never write the values into any output):
`<DEL-ID>`, `<FROZEN_TREE>` (frozen reading tree at `00115c719`), `<RUN>` (run folder),
`<DEL-FOLDER>` (the deliverable folder, repo-relative, under `<FROZEN_TREE>`).

## Purpose

Deliverable `<DEL-ID>` is on the pre-gather list (`CONVENTIONS.md` §10). A separate forward worker
will disposition its claims. You locate evidence so that worker can read economically. **You write no
dispositions, no judgments of alignment, no CauseTags.**

## Inputs

- `<RUN>/CONVENTIONS.md` §1, §2.3 (`ImplementationEvidence` / REACH rules), §7, §9.
- `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv`: rows whose `DeliverableID` is `<DEL-ID>` (grep them; do not
  read the whole file).
- `<RUN>/R1_INVENTORY/HINTS/<DEL-ID>.csv` (`ClaimKey,Token,HitPath,HitLine`): token hits, a starting
  point only. Summarize it with scripts (e.g. `python3`/`awk` counts per ClaimKey and path); do not
  dump it whole.
- `<RUN>/R1_INVENTORY/VERIFICATION_INDEX.csv` (test files), `IMPLEMENTATION_SURFACES.csv` (`Area`
  per code path).
- Evidence pack `<RUN>/R2/PKG-08/EVIDENCE_PACK/`: `REACHABILITY.csv` (item 2: `Reach` per module),
  `TOUCHED_PATHS.csv` (item 1), `DECISION_HITS.csv` (item 4).
- The deliverable's files at `<FROZEN_TREE>/<DEL-FOLDER>/` (ScopeOfWork.md, _STATUS.md, _CONTEXT.md,
  Dependencies.csv, _REFERENCES.md, …).
- Code and tests at `<FROZEN_TREE>/projects/chirality-app-dev/frontend/**` and
  `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`.

## Reading discipline (CONVENTIONS §7)

- Read from `<FROZEN_TREE>` only. Never read the working repository's deliverable folders (they carry
  run edits). Never read `projects/chirality-runtime/execution/**` or any other project's execution tree.
- Do not read `<RUN>/R0_CALIBRATION/**` ledgers or verification files, nor any other folder under
  `<RUN>/R2/` except `<RUN>/R2/PKG-08/EVIDENCE_PACK/` and your output folder.
- Economize: grep before you read; read line ranges.
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No other git, none against the
  working repository. No installs, no test runs, no builds.
- Write only `<RUN>/R2/PKG-08/<DEL-ID>/PREGATHER.md`. No absolute paths in it (repo-relative only).

## Output: `<RUN>/R2/PKG-08/<DEL-ID>/PREGATHER.md`

1. Header: deliverable, basis `00115c719`, method (searches run), counts.
2. One section per indexed unit (every `ClaimKey` of `<DEL-ID>` in CLAIM_INDEX, in index order):
   - one-line gist of what the unit asserts (neutral paraphrase, ≤ 25 words, no verdict);
   - **candidate code paths** with symbol and line (`path:line symbol`), each tagged with its
     `REACH=` value copied from `REACHABILITY.csv` (runtime/`frontend` modules not in the map: say
     `REACH=NOT_IN_MAP`); mark touched-path hits `TOUCHED(<commit>)` when the lines fall in a
     `TOUCHED_PATHS.csv` range;
   - **candidate test paths** (`test-file :: case name` where findable);
   - **candidate decision records** (IDs from `DECISION_HITS.csv` or the register at
     `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`);
   - `NO_CANDIDATES` with the searches tried, when nothing is found (common for documentary units).
   - Units of type REM: quote the gate suffix(es) verbatim and name where each gate's status may be
     checked (App surfaces only).
3. A short "cross-cutting" section: modules that recur across many units, and the live-versus-legacy
   split you observed (as reach facts only).

End the file with a line `#END`.

## Return (≤ 6 lines)

Units covered / total, units with `NO_CANDIDATES`, top 5 recurring modules with REACH, and the SHA-256
of `PREGATHER.md`.
