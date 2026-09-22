# Worker brief — R2 concordance ledger, one deliverable (TASK, Type 2) — PKG-05

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-05 WORKING_ITEMS manager (wave 2). You do not
delegate. Your dispatch prompt supplies: `<DEL-ID>`, `<DEL-FOLDER>` (the deliverable folder name),
`<OUT>` (your output folder), and the placeholder values `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.
Use the values to work; **never write an absolute path into any output** — outputs use
repo-relative paths such as `projects/chirality-app-dev/frontend/src/lib/x.ts:120`.

## Target

- Deliverable: `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/<DEL-FOLDER>/`
  (ScopeOfWork.md, _STATUS.md, _CONTEXT.md, MEMORY.md, _DEPENDENCIES.md / Dependencies.csv,
  _REFERENCES.md, _SEMANTIC*.md, Assessment_INSP-03_*, Evidence_*, _run_records/**).
- Package-level evidence in the frozen tree, where relevant, in
  `.../PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/`:
  `Evidence_ADQ-08_Canonical_Session_Migration.md`, `Evidence_ADQ-09_Runtime_Transcript_View.md`,
  `Evidence_ADQ-10_Tool_Result_Artifacts.md`.
- Audit units: every row of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
  (filter it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column).

## Read first

1. `<RUN>/CONVENTIONS.md` **in full** — it is your rulebook and is self-contained.
2. `<RUN>/RUN_BASIS.md` §3, §5 and Addenda 1–7.
3. The evidence pack `<RUN>/R2/PKG-05/EVIDENCE_PACK/` (`PACK_MANIFEST.md` first):
   - `TOUCHED_PATHS.csv` — the post-release touched paths with line ranges (PostReleaseBasis);
   - `REACHABILITY.csv` — the static REACH map (LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED);
   - `REFERENCE_HASHES.csv` — every PKG-05 `_REFERENCES.md` MATCH hash fails to reproduce;
   - `DECISION_HITS.csv` — decision IDs cited by / naming your deliverable;
   - `D-APP-127_APPLICATION_MAP.csv` — which carriers cite D-APP-127/D-GOV-43 (in PKG-05 only
     DEL-05-02 `_STATUS.md`).
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
  deliverable folders (they carry run edits). Never read, list or grep
  `projects/chirality-runtime/execution/**` or any other project's execution tree — exclude it
  explicitly in every search (e.g. `grep -r --exclude-dir=execution` under `projects/chirality-runtime`,
  or search only `projects/chirality-runtime/packages` and `projects/chirality-runtime/tests`).
- Economize: grep before you read, read line ranges, prefer deliverable files and the evidence pack
  over broad sweeps. Read CSVs by script rather than dumping them.
- Git: **only** read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L` — nothing else, nothing against the working repository.
- No installs, no test runs, no builds. No edits anywhere outside `<OUT>`.
- Do not read `<RUN>/R0_CALIBRATION/**` (including any R0 ledger), or any other worker's or package's
  folder under `<RUN>/R2/**` (including other PKG-05 deliverable folders, any `_A`/`_B` sibling, and
  every other `R2/PKG-*` folder). You may read `<RUN>/R2/SURFACES/**` only when the manager names a
  file in pass 2.

## Rule reminders (apply the rulebook; these are reminders, not new rules)

- **Tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`** (CONVENTIONS §2.6,
  RUN_BASIS Addendum 5), verbatim:
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
- **Named R4 questions** (CONVENTIONS §2.4). Cite the named question instead of plain `R4` whenever
  the row turns on it: `R4-Q1` (legacy in-process harness vs live Codex path: is retained harness code
  history, compatibility or obligation), `R4-Q2` (Codex engine never run through K-ENGINE-2
  conformance), `R4-Q3` (actor check on the legacy `status_transition` tool), `R4-Q4` (whether the
  2026-09-09 v3 four-role adoption `9b005c23a` is a governing amendment of SPEC §7/§13 and the persona
  and matrix contracts), `R4-Q5` (RUN_BASIS Addendum 7: Codex event payloads stored as received —
  amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11 — or translated — unamended K-ENGINE-4, SPEC §10.3).
- **Legacy-versus-live subject test (R4-Q1)** (CONVENTIONS §2.4, RUN_BASIS Addendum 6), verbatim:
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
- **Reachability is a starting hint, not a verdict.** `REACHABILITY.csv` is import-based and
  module-level: a re-export or one imported helper marks a whole module LIVE, and some LIVE-tagged
  modules are never rendered or executed. Before tagging `REACH=LIVE`, confirm that the specific
  symbol you rely on is reached from an actual product entry point (a rendered page/component, an
  executed API route handler, `frontend/electron/main.ts`, or the packaged runtime-service entry) and
  say how in Notes when it is not obvious. A symbol in a LIVE module that no entry actually calls is
  judged as not live (`REACH=LEGACY_ONLY` + `UNREACHED` in Notes when nothing reaches it).
- **Judge on the live path** (§2.3 ImplementationEvidence): a requirement met only on a
  `LEGACY_ONLY` path is `PARTIALLY_IMPLEMENTED` / `IMPLEMENTED_DIFFERENTLY` /
  `DOCUMENTED_UNIMPLEMENTED` per the rule, never `ALIGNED`. Tag every code citation with REACH.
- **MR-11 vs AUTHORITY_CONFLICT (§1).** Apply MR-11 only when the ruling explicitly addresses the
  clause or deliverable. A ruling (e.g. D-GOV-43/D-APP-127) that undercuts an unamended GOVERNING
  clause without naming it → `AUTHORITY_CONFLICT` + R4/R4-Qn. Where DIRECTIVE §0's order resolves it,
  apply it and do not use AUTHORITY_CONFLICT.
- **DirectionEvidence.** Search `execution/_Coordination/_DECISIONS/_REGISTER.md` and CONTEXT sources
  before `NONE_FOUND`, and name the search in Notes. Prefix every record `CTX:` or `GOV:`.
  `ALIGNED`/`NOT_AUDITABLE` rows take `NOT_APPLICABLE`.
- **PostReleaseBasis.** Do not assume `NO`: for each cited file listed in `TOUCHED_PATHS.csv`, run
  `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` on the relied-on lines.
- **Register defects.** The `_REFERENCES.md` hash drift is one `REGISTER-n` row per deliverable
  (`HASH-RECOMPUTE@00115c719`); SoW rows restating it cite that key. Look also for stale conflict
  tables, stale dependency notes and stale status metadata.
- **Carrier propagation.** Where the SoW still describes the pre-D-GOV-43 topology or engine (daemon,
  per-root homes, Claude/Anthropic engine) while code has moved, say so with the right CauseTag.
- **SubItems.** A unit listing k ≥ 2 REQ/AC/VER items needs ≥ k rows, one `.n` per item, the item named
  in Notes (validator `V-SUBITEMS`).
- **AuthorityTier** = the highest source *restated*; `NOT_APPLICABLE` only for CONTEXT_CLAIM and for
  STATE_ASSERTION/REGISTER_DEFECT rows that restate nothing normative.
- **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism
  applies; UNRECORDED_JUDGMENT only with `DirectionEvidence = NONE_FOUND`; secondaries as `CAUSE2:`.
- A wrong citation or gloss is a defect even when the Disposition holds: cite lines that exist at the
  frozen tree and say what they actually do.
- **Coverage gaps.** If you find an indexed work item or SoW scope that has no forward row you can own
  (e.g. work delivered but undocumented, or scope whose owner is unclear), record it in your notes
  file (§3 section 5 or a "Coverage gaps" subsection) — never as a new row after sealing.

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
   — once per named capability file; and, if present,
   `python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv`. Errors must be 0.
4. Confirm the claims SHA-256 is unchanged. Return ≤ 8 lines: response counts, errata count, validator
   results, seal status.
