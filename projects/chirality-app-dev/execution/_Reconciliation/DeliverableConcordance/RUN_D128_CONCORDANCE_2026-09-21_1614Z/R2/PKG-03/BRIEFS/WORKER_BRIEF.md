# Worker brief — R2 concordance ledger, one deliverable (TASK, Type 2) — PKG-03

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-03 WORKING_ITEMS manager. You do not delegate.
Your dispatch prompt supplies: `<DEL-ID>`, `<DEL-FOLDER>` (the deliverable folder name),
`<OUT>` (your output folder), and the placeholder values `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.
Use the values to work; **never write an absolute path into any output** — outputs use
repo-relative paths such as `projects/chirality-runtime/packages/core/src/x.ts:120`.

## Target

- Deliverable: `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/<DEL-FOLDER>/`
  (ScopeOfWork.md, _STATUS.md, _CONTEXT.md, MEMORY.md, _DEPENDENCIES.md / Dependencies.csv,
  _REFERENCES.md, _SEMANTIC*.md, Assessment_INSP-03_*, Evidence_*, other deliverable-local files, _run_records/**).
- Package-level evidence in the frozen tree, where relevant:
  `.../PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/Evidence_ADQ-05_G5_Runtime_Taxonomy.md` and
  `.../1_Working/Evidence_ORN-09_Route_SSE_Fixture_Index.md`.
- Audit units: every row of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
  (filter it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column).

## Read first

1. `<RUN>/CONVENTIONS.md` **in full** — it is your rulebook and is self-contained.
2. `<RUN>/RUN_BASIS.md` §3, §5 and Addenda 1–3.
3. The evidence pack `<RUN>/R2/PKG-03/EVIDENCE_PACK/` (`PACK_MANIFEST.md` first):
   - `TOUCHED_PATHS.csv` — the post-release touched paths with line ranges (PostReleaseBasis);
   - `REACHABILITY.csv` — the static module map (LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED);
   - `REFERENCE_HASHES.csv` — every PKG-03 `_REFERENCES.md` MATCH hash fails to reproduce;
   - `DECISION_HITS.csv` — decision IDs cited by / naming your deliverable;
   - `D-APP-127_APPLICATION_MAP.csv` — only `_STATUS.md` cites D-APP-127/D-GOV-43 in each PKG-03 deliverable.
4. Helpful R1 inventories (read by script, filter to your deliverable): `R1_INVENTORY/HINTS/<DEL-ID>.csv`
   (grep hits of claim tokens in code — hints, not evidence), `IMPLEMENTATION_SURFACES.csv`,
   `VERIFICATION_INDEX.csv`, `DECISION_INDEX.csv`, `REMAINING_INVENTORY.csv`, `DIRECTION_RECORD_INDEX.csv`.
5. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`,
   `GATE_TRANSCRIPT_RUNTIME_00115c719.md` (cite as `GATE-TRANSCRIPT(APP@00115c719)` etc. plus the
   named test file and case).

## Reading discipline (CONVENTIONS §7)

- Read deliverables and code **from `<FROZEN_TREE>` only**. Never read the working repository's
  deliverable folders (they carry run edits). **Never read, list or grep
  `projects/chirality-runtime/execution/**`** or any other project's execution tree — exclude it
  explicitly in every search (e.g. `grep -r ... --exclude-dir=execution` when searching under
  `projects/chirality-runtime`, or search only `projects/chirality-runtime/packages` and `/tests`).
- Economize: grep before you read, read line ranges, prefer deliverable files and the evidence pack
  over broad sweeps. Read CSVs by script rather than dumping them.
- Git: **only** read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L` — nothing else, nothing against the working repository.
- No installs, no test runs, no builds. No edits anywhere outside `<OUT>`.
- Do not read `<RUN>/R0_CALIBRATION/**` (it holds earlier-convention ledgers for DEL-03-01; you
  must produce a fresh ledger under CONVENTIONS.md), nor any other worker's folder under `<RUN>/R2/**`
  (including other PKG-03 deliverable folders and other packages).

## Reachability (read this carefully)

`REACHABILITY.csv` is import-based and module-level. In wave 1 it tagged as LIVE some modules the
product never renders or executes (barrel re-exports, unmarked type-only imports, components imported
but never mounted). **Treat it as a starting hint.** Before tagging `REACH=LIVE`, confirm the reach from
the actual entry point: the rendered page/component tree, the route handler that actually executes the
code, or the packaged runtime-service entry (for `projects/chirality-runtime/packages/**`, follow the
path from the App's runtime-service host into the package). If the map says LIVE but you find the code
is not executed on the product path, tag what you found (`REACH=LEGACY_ONLY` + `UNREACHED` in Notes
when nothing reaches it, or `REACH=TEST_ONLY`) and state the map disagreement in Notes. Say in your
notes file how you confirmed reach.

## Known pitfalls from R0 calibration and wave 1 (reminders, not new rules)

- **Engine surface.** Codex is the sole production engine (D-GOV-43 / D-APP-127). The AgentEnginePort
  conformance suite (K-ENGINE-2) passes only against scripted Claude SDK / Pi adapters; rows turning on
  the Codex engine never having been run through it cite `R4-Q2`. Rows turning on whether retained
  legacy in-process harness code is history, compatibility or obligation cite `R4-Q1`. `R4-Q3` = the
  actor check on the legacy `status_transition` tool. Cite the named question instead of plain `R4`.
- **Runtime extraction.** Turn engine, session locking, interrupt/cancel and event handling may now
  live in `projects/chirality-runtime/packages/**` behind the App-owned Runtime service (A2 topology).
  Judge each requirement on the live path, tag every code citation with REACH, and choose the CauseTag
  by mechanism (RUNTIME_EXTRACTION, A2_TOPOLOGY, CODEX_SOLE_ENGINE, …; `CAUSE2:` for a secondary).
- **Event types.** CONTRACT K-ENGINE-1/4 versus SPEC §11 / K-EVENT-6 on `codex.*` canonical event
  types (and "translate" versus "preserve upstream payload") may be an unresolved GOVERNING tension.
  Where DIRECTIVE §0's authority order resolves it, apply it and cite both; otherwise AUTHORITY_CONFLICT
  with R4. Decide on the text, and explain in Notes.
- **MR-11 vs AUTHORITY_CONFLICT (§1).** Apply MR-11 only when the ruling explicitly addresses the
  clause or deliverable. A ruling that undercuts an unamended GOVERNING clause without naming it →
  `AUTHORITY_CONFLICT` + R4/R4-Qn. A decomposition/SCA/SoW restatement against an **amended** CONTRACT or
  SPEC clause is resolved by DIRECTIVE §0 (→ usually STALE_SPECIFICATION), not AUTHORITY_CONFLICT.
- **DirectionEvidence.** Search `execution/_Coordination/_DECISIONS/_REGISTER.md` and CONTEXT sources
  before `NONE_FOUND`, and name the search in Notes. Prefix every record `CTX:` or `GOV:`.
  `ALIGNED`/`NOT_AUDITABLE` rows take `NOT_APPLICABLE`. Do not repeat an unverified gloss down a SEE chain.
- **PostReleaseBasis.** Do not assume `NO`: for each cited file listed in `TOUCHED_PATHS.csv`, run
  `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` on the relied-on lines, the whole cited
  range (wave 1 missed a single line inside a cited range that blamed to `da95ec194`).
- **Register defects.** The `_REFERENCES.md` hash drift is one `REGISTER-n` row per deliverable
  (`HASH-RECOMPUTE@00115c719`); SoW rows restating it cite that key. Look also for stale conflict
  tables, stale dependency notes and stale status metadata.
- **Carrier propagation.** D-APP-127/D-GOV-43 reached `_STATUS.md` only; where the SoW, `_CONTEXT.md` or
  `Dependencies.csv` still describe the pre-D-GOV-43 topology or engine, say so (CARRIER_PROPAGATION or
  the mechanism tag, per §4 precedence).
- **Dated carrier notes** restating a register value (e.g. "REF-00n MATCH (…, 2026-07-xx)") — decide
  STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH by the §2.6/§2.7/MR-8 text and give the alternative
  reading in Notes when it is close.
- **SubItems.** A unit listing k ≥ 2 REQ/AC/VER items needs ≥ k rows, one `.n` per item, the item named
  in Notes (validator `V-SUBITEMS`).
- **AuthorityTier** = the highest source *restated*; `NOT_APPLICABLE` only for CONTEXT_CLAIM and for
  STATE_ASSERTION/REGISTER_DEFECT rows that restate nothing normative.
- **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism
  applies; UNRECORDED_JUDGMENT only with `DirectionEvidence = NONE_FOUND`.
- A wrong citation or gloss is a defect even when the Disposition holds: cite lines that exist at the
  frozen tree and say what they actually do.

## Pass 1 — forward (then STOP)

1. Write `<OUT>/<DEL-ID>_claims.csv` (25-column header from CONVENTIONS §2.1, rows, final `#END`; use a
   CSV writer) and `<OUT>/<DEL-ID>_notes.md` (§3 sections 1–6).
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
   also put sealed vs errata-applied census figures in reverse_notes.
3. Validate from `<APP_WORK>`: for each capability file,
   `python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <cap.csv> <OUT>/<DEL-ID>_reverse.csv`
   — once per named capability file (each run checks that file's rows are all answered; rows from other
   areas are ignored); and, if present,
   `python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv`. Errors must be 0.
4. Confirm the claims SHA-256 is unchanged. Return ≤ 8 lines: response counts, errata count, validator
   results, seal status.

## Rule additions adopted during wave 2 (apply to every unsealed forward pass)

- **R4-Q4** (RUN_BASIS Addendum 4; CONVENTIONS §2.4): a valid HumanDecisionNeeded token for
  whether the 2026-09-09 v3 four-role adoption (`9b005c23a`) is a governing amendment of SPEC §7/§13
  and the persona and matrix contracts. Cite `R4-Q4` instead of plain `R4` on rows that turn on it.
- **Tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`** (RUN_BASIS Addendum 5;
  CONVENTIONS §2.6), verbatim:

  1. Use `STALE_SPECIFICATION` when the text states a present fact that is now false (a hash
     recorded as `MATCH`, a path called "current", a dependency marked `SATISFIED`, a file said
     to exist). The rule is the same for SoW, `_STATUS`, register and references text.
  2. Use `REMAINING_STATE_MISMATCH` only for (a) an item in `## Remaining`, or a `REMAINING_WORK`
     row, whose open or done status is contradicted by the evidence; or (b) register
     bookkeeping that is behind but says nothing false about the product or its references
     (a `Last Updated` date, a `TBD` placeholder, a lagging status field).
  3. MR-8(iv) clarified: a claim tied to a named snapshot ("MATCH at v23") stays a REGISTER row.
     Text that restates it as current ("is MATCH") without naming the snapshot takes
     `STALE_SPECIFICATION` and points to the REGISTER row (`SEE:`).
  4. If both still fit, choose the verdict whose repair is a change to deliverable text, and
     record the other in Notes as `ALSO:<verdict>`.
