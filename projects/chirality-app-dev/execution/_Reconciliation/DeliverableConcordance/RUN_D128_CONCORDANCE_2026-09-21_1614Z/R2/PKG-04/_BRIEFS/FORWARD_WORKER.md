# Brief — R2 forward-pass concordance worker (TASK, Type 2) — PKG-04

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-04 WORKING_ITEMS manager. **Do not delegate.**
Your dispatch prompt gives `<DEL-ID>`, `<FROZEN_TREE>`, `<RUN>` and `<APP_WORK>`. Use them literally
in your own commands; **never write them, or any other absolute path, into an output file.**

## Target and outputs

- Target: deliverable `<DEL-ID>` of `PKG-04`, read at
  `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/<DEL-ID>_*/`.
- Your folder: `<RUN>/R2/PKG-04/<DEL-ID>/`. Write **only** there, and only:
  - `<DEL-ID>_claims.csv` (the ledger, CONVENTIONS §2), then
  - `<DEL-ID>_notes.md` (CONVENTIONS §3).
  - Later, if the manager resumes you for the reverse pass: `_reverse.csv`, `_errata.csv`,
    `_reverse_notes.md` (you will get separate instructions then).
- If `<RUN>/R2/PKG-04/<DEL-ID>/PREGATHER.md` exists, read it first: it lists candidate code and
  test paths per indexed unit with REACH tags. It is a lead list, not evidence; confirm what you cite.

## Read first

1. `<RUN>/CONVENTIONS.md`, **in full**. It is the rulebook and is self-contained. Apply it exactly.
2. `<RUN>/RUN_BASIS.md` §3, §4, §5 and Addenda 1–2 (evidence roots, fences, authority map).
3. Your units: the rows of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
   (read it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column).
4. The evidence pack `<RUN>/R2/PKG-04/EVIDENCE_PACK/` (read `PACK_MANIFEST.md`; query the CSVs by
   script or grep, filtered to your deliverable or to cited paths):
   - `TOUCHED_PATHS.csv` → PostReleaseBasis (blame only files on this list);
   - `REACHABILITY.csv` → the `REACH=` tag of every cited code path (read its known limits in the
     shared manifest `<RUN>/R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`, "Item 2");
   - `REFERENCE_HASHES.csv` → `_REFERENCES.md` MATCH hashes (REGISTER rows, `HASH-RECOMPUTE@00115c719`);
   - `DECISION_HITS.csv` → decisions naming your deliverable (start of the register search);
   - `D-APP-127_APPLICATION_MAP.csv` → which of your carriers were revised for D-APP-127/D-GOV-43.
5. Optional lead list: `<RUN>/R1_INVENTORY/HINTS/<DEL-ID>.csv` (`ClaimKey,Token,HitPath,HitLine`:
   mechanical grep hits, often noisy; never cite a hint without opening the line).
6. Gate transcripts `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_{APP,RUNTIME}_00115c719.md` for
   VerificationEvidence (grep for the test file you cite).

## Reading discipline (CONVENTIONS §7) — mandatory

- **Read deliverables, code, tests and decision records from `<FROZEN_TREE>` only.** Never read the
  working repository's deliverable folders (`<APP_WORK>/execution/PKG-*/**`): they carry run edits.
- **Out of bounds:** `projects/chirality-runtime/execution/**` and any other project's execution
  tree; other workers' folders (`<RUN>/R2/PKG-04/<other DEL-ID>/`, `<RUN>/R2/PKG-*/` of other
  packages); **all of `<RUN>/R0_CALIBRATION/`** (earlier calibration ledgers must not influence
  your forward pass); `<RUN>/R2/SURFACES/` until the manager gives you capability files after sealing.
- Economize: grep before you read, read line ranges, prefer the deliverable files and the pack
  over broad code sweeps. Implementation evidence roots: `projects/chirality-app-dev/frontend/**`,
  `projects/chirality-runtime/packages/**`, `projects/chirality-runtime/tests/**`.
- **Git:** only read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L …` against the frozen tree. No other git, and no git against the
  working repository.
- **No installs, no test runs, no builds.** Running the validator script is allowed.
- No absolute paths in any output (the validator checks this). Use repo-relative paths such as
  `projects/chirality-app-dev/frontend/src/lib/harness/x.ts:120`.

## Pitfalls seen in R0 calibration (apply the rule; these are reminders, not rulings)

- **Authority.** The App `docs/PRD.md` and `docs/CONTRACT.md` both open with a GOVERNING
  "Current Codex-only MVP release basis" preamble stating that Claude/Anthropic and Pi/oMLX
  descriptions describe compatibility history. When a claim restates Claude-SDK/Anthropic
  requirements, consider that preamble and DIRECTIVE §0's authority order **before** choosing
  `AUTHORITY_CONFLICT` (CONVENTIONS §1): use AUTHORITY_CONFLICT only when the authority order does
  not resolve it. Cite what you relied on.
- **Legacy path.** Claude SDK / in-process harness code is typically `LEGACY_ONLY` in
  `REACHABILITY.csv`. Judge a requirement on the **live** path (§2.3 ImplementationEvidence rule);
  a claim about the retained module itself is judged at module level with its REACH tag. Rows that
  turn on whether retained harness code is history, compatibility or obligation cite
  `HumanDecisionNeeded = R4-Q1` (or R4-Q2 / R4-Q3 when those apply), not plain `R4`.
- **DirectionEvidence.** Search `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`
  and the CONTEXT sources (RUN_BASIS §5) **before** writing `NONE_FOUND`, and name the search in
  Notes/notes §4. Use `CTX:` vs `GOV:` prefixes correctly; `NOT_APPLICABLE` on ALIGNED/NOT_AUDITABLE.
- **PostReleaseBasis** is set by `git blame -L` on the relied-on lines of files listed in
  `TOUCHED_PATHS.csv`, never by assumption; other files are `NO`.
- **AuthorityTier** is the highest source the claim restates (§2.3); `NOT_APPLICABLE` only for
  CONTEXT_CLAIM and for STATE_ASSERTION/REGISTER_DEFECT rows that restate no normative source.
- **CauseTag** precedence (§4): mechanism first; `PRE_V3_DRIFT` for pre-2026-08-22 divergence unless
  a named v3 mechanism applies; `UNRECORDED_JUDGMENT` only with `DirectionEvidence = NONE_FOUND`.
- **Carriers.** Check whether D-APP-127/D-GOV-43 reached your SoW, `_CONTEXT.md`, `Dependencies.csv`
  (pack item 5); stale gates on retired premises take `MOOT:<ruling>` (§2.5).
- **Coverage.** Every indexed unit at least once; units with `SubItems` need one `.n` row per listed
  item (validator `V-SUBITEMS`). Register defects and REFERENCES hash drift are `REGISTER-n` rows.
- Every LOW row carries `LEAST-CONFIDENT:` with the alternative reading.

## Procedure

1. Read the rulebook, your units, the deliverable files (ScopeOfWork, _STATUS, _CONTEXT, MEMORY,
   _DEPENDENCIES/Dependencies.csv, _REFERENCES, _SEMANTIC*, the Assessment and Evidence files as
   needed) and the pack rows for your deliverable.
2. Gather code/test evidence per unit (economically), apply the rules, and write
   `<DEL-ID>_claims.csv` (25-column header, data rows, final `#END` record).
3. Write `<DEL-ID>_notes.md` with the six §3 sections.
4. Validate, from `<APP_WORK>`:
   `python3 <RUN>/_scripts/validate_ledger.py ledger <RUN>/R2/PKG-04/<DEL-ID>/<DEL-ID>_claims.csv`
   Fix until **0 errors**; report warnings.
5. Compute `shasum -a 256` of the claims file. **The ledger is now sealed: never edit it again.**

## Return (short, ≤ 10 lines)

Row count; counts by Disposition (top 5); HumanDecisionNeeded ≠ NO count; validator RULES and
RESULT lines; the sealed SHA-256; the two or three most consequential findings. Do not paste CSV
content. Then stop and wait: the manager may resume you for the reverse pass.
