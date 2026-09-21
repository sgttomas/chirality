# Brief — R2 package concordance manager (WORKING_ITEMS, Type 1)

**Role.**
- You are WORKING_ITEMS and own the concordance of one package, `<PKG-ID>`.
- You dispatch TASK workers (Type 2, no delegation) and verifier shards, and you
  integrate their returns.
- You never edit deliverables and never commit. You return to HELP_HUMAN.

**Run.** `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2 authorized by D-APP-129).

**Placeholders**, supplied at dispatch:
- `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`: as in the other briefs.
- `<PKG-ID>`: the package.
- `<DOUBLE_BLIND>`: a DEL-ID or `NONE`.

**Read first:**
- `<RUN>/CONVENTIONS.md`, in full. It is your rulebook; §10 is the operating rules.
- `<RUN>/RUN_BASIS.md`, including its addenda.
- `<RUN>/R0_CALIBRATION/R0_CALIBRATION_REPORT.md` §3, §4 and §8. These list the patterns
  workers got wrong and the early findings.
- `agents/AGENT_WORKING_ITEMS.md` and `agents/AGENT_TASK.md` in `<FROZEN_TREE>`.

## Steps

1. **Preflight.**
   - For every deliverable in the package, from `<APP_WORK>`, run:
     `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path "RECONCILIATION:D-APP-128:R2" --target <DEL-ID>`
   - Write the output to `<RUN>/R2/<PKG-ID>/PREFLIGHT/<DEL-ID>.json`. Do not use `--output`;
     that flag rejects paths outside its evidence roots.
   - Do not dispatch any deliverable whose verdict is not `ALLOW`. Report it instead.
2. **Evidence pack.** Build it at `<RUN>/R2/<PKG-ID>/EVIDENCE_PACK/`.
   - Copy items 1, 2 and 5 byte-for-byte from `<RUN>/R2/_shared/EVIDENCE_PACK/` and
     confirm the SHA-256 values match.
   - Run the `<RUN>/R2/_scripts/` item 3 and item 4 scripts with `--package <PKG-ID>`.
   - Write `PACK_MANIFEST.md`.
3. **Worker sizing** (CONVENTIONS §10).
   - One worker per deliverable.
   - For deliverables on the pre-gather list, first dispatch one read-only
     evidence-gathering TASK. It writes `<RUN>/R2/<PKG-ID>/<DEL-ID>/PREGATHER.md`: candidate
     code and test paths per indexed unit, with REACH tags taken from pack item 2. It
     writes no dispositions.
   - Split-listed deliverables get two workers, divided by SoW section range. Each writes
     its own `_claims.csv` into a subfolder. You merge the two with a script and validate
     the merged file.
   - Retired deliverables get a light worker using `RETIRED_BY_RULING`.
4. **Double-blind.** If `<DOUBLE_BLIND>` is not `NONE`:
   - Run two independent workers on that deliverable, writing to `<DEL-ID>_A/` and
     `<DEL-ID>_B/`. Use A as the ledger of record.
   - Compare them with `<RUN>/R0_CALIBRATION/_scripts/double_blind.py`, adapted by path
     only.
   - Write `<RUN>/R2/<PKG-ID>/DOUBLE_BLIND_<DEL-ID>.md`.
5. **Forward pass.**
   - Each worker writes `<RUN>/R2/<PKG-ID>/<DEL-ID>/<DEL-ID>_claims.csv` and `_notes.md`,
     then validates them (§6).
   - You record the sealed SHA-256.
6. **Reverse pass.** After sealing, determine the worker's capability areas by script:
   - the `Area` (from `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv`) of every code path
     cited in the sealed ledger's `ImplementationEvidence`;
   - plus the areas of the deliverable's `R1_INVENTORY/HINTS/<DEL-ID>.csv` hits.

   Then resume the same worker via `SendMessage` (load it with ToolSearch
   `select:SendMessage`) and give it those capability files from
   `<RUN>/R2/SURFACES/`, which holds all 11 areas, including the re-tagged HARNESS. It writes `_reverse.csv`
   and, if needed, `_errata.csv` and `_reverse_notes.md`. Validate both. The seal must
   still hold.
7. **Verification.**
   - Select items per §10 class (a), plus 30% of the other non-ALIGNED rows, 15% of
     ALIGNED rows and 20% of `CLAIMED_BY`/`PARTIAL` responses. Selection is deterministic
     by `sha256(key)` as in R0.
   - Include every errata row.
   - Dispatch fresh verifier shards of at most 50 items each, with one shared grading key.
     Verifiers never edit ledgers.
   - Write `<RUN>/R2/<PKG-ID>/VERIFICATION.md`, containing: the structural result, a
     recheck table per deliverable, every REFUTED and CONTESTED item with its evidence,
     and patterns.
   - A ledger with any structural failure, or with more than 10% REFUTED among checked
     rows, is rerun by a fresh worker. Keep the original and record why it was rerun.
8. **Package summary.** Produce `<RUN>/R2/<PKG-ID>/PACKAGE_SUMMARY.md` **by script**
   from the accepted ledgers. It covers:
   - censuses by ClaimType, Disposition, CauseTag, AuthorityTier and REACH;
   - `HumanDecisionNeeded` tallies, including R4-Q1..Q3;
   - errata-applied figures shown next to the sealed figures;
   - verifier outcomes;
   - capability responses: `CLAIMED_BY`, `PARTIAL`, `NOT_MINE`.

   Add a short hand-written section of cross-package observations for R3. It is
   evidence, not rulings.

## Rules

- **Concurrency.** At most **4** of your children run at once. Every spawn uses
  `model: "opus"`.
- **Notifications.** Child completion notifications go to HELP_HUMAN, not to you. Drive
  the work from files: poll output folders with a Bash `until` loop (sleep 30–60 s),
  checking for `#END` and a passing validator. Do not end your turn until the whole
  package is complete.
- **Validation.** Run the validator from `<APP_WORK>`. A failing output goes back to its
  worker once; after that, a fresh worker reruns it. Never patch a child's CSV.
- **State.** Keep `<RUN>/R2/<PKG-ID>/STATE.jsonl`, one line per dispatch or return. You
  are its only writer.
- **Worker briefs.** Every worker brief is self-contained and includes:
  - the target, output paths and placeholder values;
  - CONVENTIONS §7 reading discipline;
  - read-only `git log/show/blame` against `<FROZEN_TREE>` only, and no other git;
  - no installs and no test runs;
  - no absolute paths in outputs;
  - never reading other workers' folders, the working repository's deliverable folders,
    or `projects/chirality-runtime/execution/**`.
- **Write scope.** You and your children write only under `<RUN>/R2/<PKG-ID>/`.
- **Context discipline.** Read CSVs only through scripts. Children return short
  summaries.

## Return

At most 15 lines:
- per deliverable: row count, top dispositions, and seal and validator status;
- verifier counts;
- double-blind agreement, if run;
- reruns and preflight issues;
- the SHA-256 of `PACKAGE_SUMMARY.md` and `VERIFICATION.md`;
- the 3 most consequential findings for R3/R4.
