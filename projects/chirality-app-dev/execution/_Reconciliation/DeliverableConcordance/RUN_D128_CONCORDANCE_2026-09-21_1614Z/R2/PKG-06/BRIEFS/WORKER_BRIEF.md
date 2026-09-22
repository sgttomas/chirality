# Worker brief — R2 concordance ledger, one deliverable (TASK, Type 2) — PKG-06

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-06 WORKING_ITEMS manager. You do not delegate.
Your dispatch prompt supplies: `<DEL-ID>`, `<DEL-FOLDER>` (the deliverable folder name),
`<OUT>` (your output folder), and the placeholder values `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.
Use the values to work; **never write an absolute path into any output** — outputs use
repo-relative paths such as `projects/chirality-app-dev/frontend/src/lib/harness/x.ts:120`.

## Target

- Deliverable: `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/<DEL-FOLDER>/`
  (ScopeOfWork.md, _STATUS.md, _CONTEXT.md, MEMORY.md, _DEPENDENCIES.md / Dependencies.csv,
  _REFERENCES.md, _SEMANTIC*.md, Assessment_INSP-03_*, Evidence_*, _run_records/**).
- Package-level evidence in the frozen tree, where relevant:
  `.../PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/Evidence_ADQ-11_Permission_Tool_Residuals.md`.
- Audit units: every row of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
  (filter it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column).

## Read first

1. `<RUN>/CONVENTIONS.md` **in full** — it is your rulebook and is self-contained.
2. `<RUN>/RUN_BASIS.md` §3, §5, Addendum 1 and Addendum 2.
3. The evidence pack `<RUN>/R2/PKG-06/EVIDENCE_PACK/` (`PACK_MANIFEST.md` first):
   - `TOUCHED_PATHS.csv` — the post-release touched paths with line ranges (PostReleaseBasis);
   - `REACHABILITY.csv` — the static REACH map (LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED);
   - `REFERENCE_HASHES.csv` — every PKG-06 `_REFERENCES.md` MATCH hash fails to reproduce;
   - `DECISION_HITS.csv` — decision IDs cited by / naming your deliverable;
   - `D-APP-127_APPLICATION_MAP.csv` — which carriers cite D-APP-127/D-GOV-43 (none in PKG-06).
4. Helpful R1 inventories (read by script, filter to your deliverable): `R1_INVENTORY/HINTS/<DEL-ID>.csv`
   (grep hits of claim tokens in code — hints, not evidence), `IMPLEMENTATION_SURFACES.csv`,
   `VERIFICATION_INDEX.csv`, `DECISION_INDEX.csv`, `REMAINING_INVENTORY.csv`, `DIRECTION_RECORD_INDEX.csv`.
5. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`,
   `GATE_TRANSCRIPT_RUNTIME_00115c719.md` (cite as `GATE-TRANSCRIPT(APP@00115c719)` etc. plus the
   named test file and case).
6. If `<OUT>/PREGATHER.md` exists (or the prompt names one), use it as a map of candidate code and
   test paths — verify everything you cite yourself.

## Reading discipline (CONVENTIONS §7)

- Read deliverables and code **from `<FROZEN_TREE>` only**. Never read the working repository's
  deliverable folders (they carry run edits). Never read `projects/chirality-runtime/execution/**` or
  any other project's execution tree.
- Economize: grep before you read, read line ranges, prefer deliverable files and the evidence pack
  over broad sweeps. Read CSVs by script rather than dumping them.
- Git: **only** read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L` — nothing else, nothing against the working repository.
- No installs, no test runs, no builds. No edits anywhere outside `<OUT>`.
- Do not read `<RUN>/R0_CALIBRATION/**` or any other worker's folder under `<RUN>/R2/**`
  (including other PKG-06 deliverable folders and any `_A`/`_B` sibling).

## Known pitfalls from R0 calibration (apply the rulebook; these are reminders, not new rules)

- **Legacy path.** Much of PKG-06's code (`frontend/src/lib/harness/**` tool surface, permission
  overlay, hooks) is `LEGACY_ONLY` — reachable only through the retained Claude SDK / Pi in-process
  path; the live Codex path is bounded by the user's Codex sandbox/approval choice. Judge requirements
  on the live path (§2.3 ImplementationEvidence), tag every code citation with REACH, and cite
  `R4-Q1` in HumanDecisionNeeded where the row turns on whether retained harness code is history,
  compatibility or obligation. `R4-Q2` = Codex never run through K-ENGINE-2; `R4-Q3` = the actor check
  on the legacy `status_transition` tool.
- **MR-11 vs AUTHORITY_CONFLICT (§1).** Apply MR-11 only when the ruling explicitly addresses the
  clause or deliverable. A ruling (e.g. D-GOV-43/D-APP-127) that undercuts an unamended GOVERNING
  clause (K-PATH, K-ROOT, K-HOOK, SPEC §15.2) without naming it → `AUTHORITY_CONFLICT` + R4/R4-Qn.
- **DirectionEvidence.** Search `execution/_Coordination/_DECISIONS/_REGISTER.md` and CONTEXT sources
  before `NONE_FOUND`, and name the search in Notes. Prefix every record `CTX:` or `GOV:`.
  `ALIGNED`/`NOT_AUDITABLE` rows take `NOT_APPLICABLE`.
- **PostReleaseBasis.** Do not assume `NO`: for each cited file listed in `TOUCHED_PATHS.csv`, run
  `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` on the relied-on lines (an R0 row
  was wrong by assumption: a `codex-supervisor.ts` line blamed to `da95ec194`).
- **Register defects.** The `_REFERENCES.md` hash drift is one `REGISTER-n` row per deliverable
  (`HASH-RECOMPUTE@00115c719`); SoW rows restating it cite that key. Look also for stale conflict
  tables, stale dependency notes and stale status metadata.
- **Carrier propagation.** No PKG-06 carrier cites D-APP-127/D-GOV-43; where the SoW still describes
  the pre-D-GOV-43 topology or engine, say so with the right CauseTag.
- **SubItems.** A unit listing k ≥ 2 REQ/AC/VER items needs ≥ k rows, one `.n` per item, the item named
  in Notes (validator `V-SUBITEMS`).
- **AuthorityTier** = the highest source *restated*; `NOT_APPLICABLE` only for CONTEXT_CLAIM and for
  STATE_ASSERTION/REGISTER_DEFECT rows that restate nothing normative.
- **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism
  applies; UNRECORDED_JUDGMENT only with `DirectionEvidence = NONE_FOUND`; secondaries as `CAUSE2:`.
- A wrong citation or gloss is a defect even when the Disposition holds: cite lines that exist at the
  frozen tree and say what they actually do.

## Pass 1 — forward (then STOP)

1. Write `<OUT>/<DEL-ID>_claims.csv` (25-column header from CONVENTIONS §2.1, rows, final `#END`) and
   `<OUT>/<DEL-ID>_notes.md` (§3 sections 1–6).
2. From `<APP_WORK>` run:
   `python3 <RUN>/_scripts/validate_ledger.py ledger <OUT>/<DEL-ID>_claims.csv`
   Errors must be 0 (warnings reported). Fix and re-run until it passes.
3. Compute `shasum -a 256 <OUT>/<DEL-ID>_claims.csv`. The ledger is now **sealed**: never edit it again.
4. Return a short summary (≤ 8 lines): row count, Disposition census, validator RESULT line, the
   SHA-256, and your top 3 findings. **Then stop and wait** — the manager will resume you for pass 2.

## Pass 2 — reverse (only when the manager resumes you)

The manager's message names one or more capability files from `<RUN>/R2/SURFACES/`.

1. Write `<OUT>/<DEL-ID>_reverse.csv`: header `CapabilityID,Response,ClaimKey,Rationale`, one row per
   capability in **every** named file (concatenate in the order given), final `#END`. Response ∈
   `CLAIMED_BY` (+ owning ClaimKey), `PARTIAL` (+ the key covering part), `NOT_MINE` (empty ClaimKey).
2. Forward-row corrections found now go to `<OUT>/<DEL-ID>_errata.csv`
   (`ClaimKey,Field,SealedValue,ProposedValue,Evidence`, `#END`; one row per (ClaimKey, Field);
   SealedValue copied exactly). A missing forward row (coverage gap) is **not** an erratum: describe
   it in `<OUT>/<DEL-ID>_reverse_notes.md`. Explanations go in reverse_notes. If an errata file exists,
   also append sealed vs errata-applied census figures to reverse_notes (the notes file is not
   sealed, but prefer reverse_notes for pass-2 content).
3. Validate from `<APP_WORK>`: for each capability file,
   `python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <cap.csv> <OUT>/<DEL-ID>_reverse.csv`
   — run it once per named capability file (each run checks that file's rows are all answered; the
   extra rows from other areas are ignored); and, if present,
   `python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv`. Errors must be 0.
4. Confirm the claims SHA-256 is unchanged. Return ≤ 8 lines: response counts, errata count, validator
   results, seal status.
