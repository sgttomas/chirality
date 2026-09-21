# Worker brief — R2 concordance ledger, one deliverable (TASK, Type 2) — PKG-10

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-10 WORKING_ITEMS manager. You do not delegate.
Your dispatch prompt supplies: `<DEL-ID>`, `<DEL-FOLDER>` (the deliverable folder name),
`<OUT>` (your output folder), and the placeholder values `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.
Use the values to work; **never write an absolute path into any output** — outputs use
repo-relative paths such as `projects/chirality-app-dev/frontend/src/lib/harness/x.ts:120`.

## Target

- Deliverable: `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/<DEL-FOLDER>/`
  (ScopeOfWork.md, _STATUS.md, _CONTEXT.md, MEMORY.md, _DEPENDENCIES.md / Dependencies.csv,
  _REFERENCES.md, _SEMANTIC*.md, Assessment_INSP-03_*, Evidence_*, _run_records/**).
- Audit units: every row of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
  (filter it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column).

## Read first

1. `<RUN>/CONVENTIONS.md` **in full** — it is your rulebook and is self-contained.
2. `<RUN>/RUN_BASIS.md` §3, §5 and Addenda 1–7.
3. The evidence pack `<RUN>/R2/PKG-10/EVIDENCE_PACK/` (`PACK_MANIFEST.md` first):
   - `TOUCHED_PATHS.csv` — the post-release touched paths with line ranges (PostReleaseBasis);
   - `REACHABILITY.csv` — the static REACH map (LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED);
   - `REFERENCE_HASHES.csv` — every PKG-10 `_REFERENCES.md` hash fails to reproduce;
   - `DECISION_HITS.csv` — decision IDs cited by / naming your deliverable;
   - `D-APP-127_APPLICATION_MAP.csv` — which carriers cite D-APP-127/D-GOV-43 (none in PKG-10).
4. Helpful R1 inventories (read by script, filter to your deliverable): `R1_INVENTORY/HINTS/<DEL-ID>.csv`
   (grep hits of claim tokens in code — hints, not evidence), `IMPLEMENTATION_SURFACES.csv`,
   `VERIFICATION_INDEX.csv`, `DECISION_INDEX.csv`, `REMAINING_INVENTORY.csv`, `DIRECTION_RECORD_INDEX.csv`.
5. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`,
   `GATE_TRANSCRIPT_RUNTIME_00115c719.md` (cite as `GATE-TRANSCRIPT(APP@00115c719)` etc. plus the
   named test file and case).

## Reading discipline (CONVENTIONS §7)

- Read deliverables and code **from `<FROZEN_TREE>` only**. Never read the working repository's
  deliverable folders (they carry run edits). Never read `projects/chirality-runtime/execution/**` or
  any other project's execution tree.
- Economize: grep before you read, read line ranges, prefer deliverable files and the evidence pack
  over broad sweeps. Read CSVs by script rather than dumping them.
- Git: **only** read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L` — nothing else, nothing against the working repository.
- No installs, no test runs, no builds. No edits anywhere outside `<OUT>`.
- Do not read `<RUN>/R0_CALIBRATION/**` (in particular no R0 ledger) or any other worker's folder under
  `<RUN>/R2/**` (including other PKG-10 deliverable folders and any other package's folder).

## Rules adopted during R2 (RUN_BASIS Addenda 4, 5, 6 and 7; already in CONVENTIONS.md)

- **R4-Q4** (CONVENTIONS §2.4): cite `R4-Q4` instead of plain `R4` on rows that turn on whether the
  2026-09-09 v3 four-role adoption (`9b005c23a`) is a governing amendment of SPEC §7/§13 and the persona
  and matrix contracts.
- **R4-Q5** (CONVENTIONS §2.4; RUN_BASIS Addendum 7): cite `R4-Q5` instead of plain `R4` on rows that turn on
  whether Codex event payloads are stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11) or
  translated (unamended K-ENGINE-4, SPEC §10.3).
- **Tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`** (CONVENTIONS §2.6), verbatim:
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
- **Legacy-versus-live subject test for R4-Q1** (CONVENTIONS §2.4; RUN_BASIS Addendum 6), verbatim:
  1. **Decide the subject from the claim text, not from where the code lives.** The subject is
     *product behaviour* if the claim names the App, the system, the user, a session, a turn or
     an agent run; states an observable outcome (something allowed, blocked, recorded, shown or
     sent); or states a guarantee or control (permission, path containment, hooks, redaction,
     approval), even when the text also names the component meant to provide it. The subject
     is *the module* only if the claim names a specific code unit (class, function, file, tool
     or API) and describes only that unit's own contract (inputs, outputs, structure), with no
     outcome the product can observe.
  2. **If the text supports both readings, treat it as product behaviour** and judge it on the
     live path (§2.3).
  3. **R4-Q1 is cited by evidence, not by opinion.** Cite `R4-Q1` in HumanDecisionNeeded on every
     row where the only code meeting the claim is tagged `REACH=LEGACY_ONLY`, whether the row is
     judged on the live path or at module level. Rows met by `LIVE` code, and rows with no code
     evidence, do not cite R4-Q1 for this reason.
  4. **Record the other reading.** On a product-behaviour row met only by legacy code, add
     `ALSO_MODULE:<verdict>` to Notes, giving the verdict a module-level reading would have
     produced.

## Known pitfalls from R0 calibration (apply the rulebook; these are reminders, not new rules)

- **Domain-engine code and the legacy path.** PKG-10's contract types
  (`projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`, `operation-proposal.ts`)
  are LIVE by the module map, but the domain registry, domain tools, headless preview runner and PEC bridge
  client under `frontend/src/lib/harness/mcp/**` are `LEGACY_ONLY` — reachable only through the retained
  Claude SDK / Pi in-process path. A type definition existing is not the behaviour being enforced: judge
  behavioural requirements on the live path (§2.3), tag every code citation with REACH, and apply **one
  consistent measure** across all your rows (do not judge some rows against product reachability and others
  against the mere code surface). Cite `R4-Q1` in HumanDecisionNeeded where a row turns on whether retained
  harness code is history, compatibility or obligation. `R4-Q2` = Codex never run through K-ENGINE-2;
  `R4-Q3` = the actor check on the legacy `status_transition` tool.
- **Future-boundary scope.** Much of this package describes a *future* domain-engine boundary. Where the SoW
  itself keeps an item future/deferred, say what the text asserts and judge that assertion; do not mark a
  present-tense GOVERNING requirement ALIGNED merely because the SoW defers it — check whether the
  requirement is present-tense in its source.
- **MR-11 vs AUTHORITY_CONFLICT (§1).** Apply MR-11 only when the ruling explicitly addresses the
  clause or deliverable. A ruling (e.g. D-GOV-43/D-APP-127) that undercuts an unamended GOVERNING
  clause without naming it → `AUTHORITY_CONFLICT` + R4/R4-Qn. Where DIRECTIVE §0's order resolves it,
  apply it instead.
- **"No direction found" needs a real search.** Before `NONE_FOUND` DirectionEvidence, `UNRECORDED_JUDGMENT`,
  `UNKNOWN`, or a claim that a decision "appears on no App surface", search at least: a
  `_DECISIONS/_REGISTER.md` grep (and the ruling records it points to), the decomposition DEC rows in
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `docs/harness/*register*`
  (e.g. `reliance_boundary_register.md`), the GOVERNING K-rows for the clause, and the CONTEXT sources
  (RUN_BASIS §5). Name the search in Notes. RULED harness-extraction/facade decisions (e.g. the D-APP-7x/8x
  series) are GOVERNING explanations and defeat UNRECORDED_JUDGMENT; ruled mitigations must be considered.
- **DirectionEvidence** prefixes every record `CTX:` or `GOV:`; `ALIGNED`/`NOT_AUDITABLE` rows take
  `NOT_APPLICABLE`.
- **PostReleaseBasis.** Do not assume `NO`: for each cited file listed in `TOUCHED_PATHS.csv`, run
  `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` on the relied-on lines.
- **Register defects.** The `_REFERENCES.md` hash drift is one `REGISTER-n` row per deliverable
  (`HASH-RECOMPUTE@00115c719`); SoW rows restating it cite that key. Look also for stale conflict
  tables, stale dependency notes and stale status metadata.
- **Carrier propagation.** No PKG-10 carrier cites D-APP-127/D-GOV-43; where the SoW still describes
  the pre-D-GOV-43 topology or engine, say so with the right CauseTag.
- **Internal consistency.** An ALIGNED row with `RemainingWork = UNKNOWN`, or with an assessment's
  PARTIAL/FAIL finding marked `STILL CURRENT`, is self-contradictory — resolve it.
- **SubItems.** A unit listing k ≥ 2 REQ/AC/VER items needs ≥ k rows, one `.n` per item, the item named
  in Notes (validator `V-SUBITEMS`).
- **AuthorityTier** = the highest source *restated*; `NOT_APPLICABLE` only for CONTEXT_CLAIM and for
  STATE_ASSERTION/REGISTER_DEFECT rows that restate nothing normative. SPEC/CONTRACT restatements are
  `GOVERNANCE_INVARIANT`, not `PRD`.
- **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism
  applies (check dates with `git log` when it matters); UNRECORDED_JUDGMENT only with
  `DirectionEvidence = NONE_FOUND`; secondaries as `CAUSE2:`.
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
   also put sealed vs errata-applied census figures in reverse_notes.
3. Validate from `<APP_WORK>`: for each capability file,
   `python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <cap.csv> <OUT>/<DEL-ID>_reverse.csv`
   — run it once per named capability file; and, if present,
   `python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv`. Errors must be 0.
4. Confirm the claims SHA-256 is unchanged. Return ≤ 8 lines: response counts, errata count, validator
   results, seal status.
