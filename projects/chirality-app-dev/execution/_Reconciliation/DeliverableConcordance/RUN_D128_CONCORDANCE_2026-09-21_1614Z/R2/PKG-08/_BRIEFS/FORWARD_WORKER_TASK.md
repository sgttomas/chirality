# Brief — R2 PKG-08 concordance worker (TASK, Type 2)

**Role.** TASK (Type 2). Do not delegate. Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128;
R2 authorized by D-APP-129). Manager: the PKG-08 WORKING_ITEMS manager, who resumes you later for the
reverse pass. Your disposition is evidence, never a ruling.

**Placeholders** (values are given in your dispatch prompt; never write the values into any output):
`<DEL-ID>`, `<FROZEN_TREE>` (frozen reading tree at `00115c719`), `<RUN>` (run folder), `<APP_WORK>`
(the working `projects/chirality-app-dev`, used **only** as the directory from which you run the
validator), `<DEL-FOLDER>` (deliverable folder, repo-relative), `<OUT>` = `<RUN>/R2/PKG-08/<DEL-ID>`.

## Read first

1. `<RUN>/CONVENTIONS.md` **in full**. It is your rulebook and is self-contained. Apply it literally.
2. `<RUN>/RUN_BASIS.md` §3, §4, §5 and both addenda (authority map: GOVERNING / flagged / CONTEXT).
3. Your deliverable at `<FROZEN_TREE>/<DEL-FOLDER>/`: `ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`,
   `Dependencies.csv`/`_DEPENDENCIES.md`, `_REFERENCES.md`, `MEMORY.md`, `_SEMANTIC*.md`,
   `Assessment_INSP-03_*`, `_run_records/**` (as needed).
4. `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` rows for `<DEL-ID>` (grep; note the `SubItems` column),
   `REMAINING_INVENTORY.csv` rows for `<DEL-ID>`, `HINTS/<DEL-ID>.csv` (summarize by script),
   `VERIFICATION_INDEX.csv`, `DIRECTION_RECORD_INDEX.csv` (CONTEXT locator).
5. Evidence pack `<RUN>/R2/PKG-08/EVIDENCE_PACK/` (see its `PACK_MANIFEST.md`): `TOUCHED_PATHS.csv`,
   `REACHABILITY.csv`, `REFERENCE_HASHES.csv`, `DECISION_HITS.csv`, `D-APP-127_APPLICATION_MAP.csv`.
6. If it exists: `<OUT>/PREGATHER.md` — candidate paths gathered by a read-only TASK. It is a locator,
   not evidence: open and confirm every path you cite.
7. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_{APP,RUNTIME}_00115c719.md`.
8. Decision register and rulings at
   `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/` (`_REGISTER.md`
   first; open ruling records as needed). Governing docs at
   `<FROZEN_TREE>/projects/chirality-app-dev/docs/{PRD,DIRECTIVE,CONTRACT,SPEC,TYPES}.md` and Root
   `<FROZEN_TREE>/docs/*` where App docs defer.

## Reading discipline (CONVENTIONS §7) — mandatory

- Read from `<FROZEN_TREE>` only. **Never** read the working repository's deliverable folders (they
  carry run edits). Never read `projects/chirality-runtime/execution/**` or any other project's
  execution tree.
- Do **not** read `<RUN>/R0_CALIBRATION/**` (calibration ledgers, verification, surfaces), nor any
  other worker's or package's folder under `<RUN>/R2/` (only `EVIDENCE_PACK/`, your `<OUT>`, and — in
  the reverse pass — the capability files the manager names).
- Economize: grep before you read, read line ranges, prefer deliverable files and the pack.
- Git: only read-only `git -C <FROZEN_TREE> log`, `show`, `blame -L` against the frozen tree. No other
  git, and nothing against the working repository. **No installs, no test runs, no builds.**
- Write only `<OUT>/<DEL-ID>_claims.csv`, `<OUT>/<DEL-ID>_notes.md` (forward), and later
  `<OUT>/<DEL-ID>_reverse.csv`, `_errata.csv`, `_reverse_notes.md`. **No absolute paths in any
  output** (repo-relative paths only; the validator checks).

## Forward pass (do this now)

1. Build `<OUT>/<DEL-ID>_claims.csv` per CONVENTIONS §2 (25-column header; every indexed unit at least
   once; SubItems → ≥ k rows; REM rows with verbatim gates; `REGISTER-n` / `STATE-n` run-local rows;
   final `#END` record) and `<OUT>/<DEL-ID>_notes.md` per §3 (all six sections).
2. Points calibration showed workers get wrong (apply the adopted rules, do not over-read them):
   - **MR-11 vs AUTHORITY_CONFLICT (§1):** use MR-11 only when the ruling explicitly addresses the
     clause or deliverable; if DIRECTIVE §0's order resolves it, apply it without AUTHORITY_CONFLICT;
     otherwise AUTHORITY_CONFLICT + `R4`/`R4-Qn`. Never resolve it yourself.
   - **Reachability:** every code-evidence row carries `REACH=` from `REACHABILITY.csv`; a requirement
     met only on a `LEGACY_ONLY` path is judged on the live path (§2.3). Rows turning on retained
     harness code versus the live Codex path cite `R4-Q1`; K-ENGINE-2 conformance of Codex → `R4-Q2`;
     `status_transition` actor check → `R4-Q3`.
   - **DirectionEvidence:** `CTX:` for CONTEXT, `GOV:` when a GOVERNING ruling itself explains it;
     search `_REGISTER.md` **and** CONTEXT before `NONE_FOUND`, and name the search in Notes / notes §4.
     `UNRECORDED_JUDGMENT` only with `DirectionEvidence = NONE_FOUND`.
   - **MR-8:** `ACCEPTED_DIVERGENCE` needs the text to acknowledge the gate **and** a GOVERNING ruling;
     snapshot-true claims are REGISTER rows; stale `_REFERENCES.md` hashes are one REGISTER row per
     document per deliverable citing `HASH-RECOMPUTE@00115c719` (pack item 3 shows all three `NO`).
   - **AuthorityTier:** highest source restated (§2.3); `NOT_APPLICABLE` never on REQUIREMENT /
     ACCEPTANCE / EXCLUSION; always on CONTEXT_CLAIM.
   - **PostReleaseBasis:** for a cited file listed in `TOUCHED_PATHS.csv`, run
     `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` on the relied-on lines; `YES` if any
     line blames to `da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a`. Never set it by assumption.
   - **CauseTag precedence (§4)** and `CAUSE2:` for secondaries; carrier notes not revised under
     D-APP-127 are `CARRIER_PROPAGATION` (pack item 5 helps).
   - Line anchors: cite lines at the frozen tree.
   - LOW rows need `LEAST-CONFIDENT:` with the alternative reading.
3. Validate, from `<APP_WORK>`:
   `python3 <RUN>/_scripts/validate_ledger.py ledger <OUT>/<DEL-ID>_claims.csv`
   Errors must be zero. Report warnings.
4. Compute `shasum -a 256 <OUT>/<DEL-ID>_claims.csv`. The ledger is now **sealed**: never edit it
   again, even in the reverse pass.

**Forward return (≤ 8 lines):** row count; rows by Disposition (top 6); split rate; SEE rows; count of
`HumanDecisionNeeded ≠ NO` by value; the validator `RULES`/`RESULT` lines; the sealed SHA-256.
Then stop and wait: the manager will resume you with the reverse-pass capability files.

## Reverse pass (only when the manager resumes you)

Per CONVENTIONS §5.1. For each capability file named by the manager (under `<RUN>/R2/SURFACES/`),
write one combined `<OUT>/<DEL-ID>_reverse.csv` (`CapabilityID,Response,ClaimKey,Rationale`, then
`#END`) answering **every** row of every named file: `CLAIMED_BY` / `PARTIAL` + one of your ClaimKeys,
or `NOT_MINE` with empty ClaimKey. Forward-row corrections go to `<OUT>/<DEL-ID>_errata.csv`
(`ClaimKey,Field,SealedValue,ProposedValue,Evidence`, `#END`; one row per (ClaimKey, Field);
SealedValue copied exactly). Coverage gaps (missing forward rows) and explanations go to
`<OUT>/<DEL-ID>_reverse_notes.md`. Validate from `<APP_WORK>`:
`python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <OUT>/REVERSE_INPUT_capabilities.csv <OUT>/<DEL-ID>_reverse.csv`
(the validator takes one capability file, so the manager writes `REVERSE_INPUT_capabilities.csv`, the
byte-level concatenation by script of the named area files' rows; read the area files and their
`<AREA>_notes.md` themselves for content) and
`python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv` when errata exist.
Confirm the sealed SHA-256 is unchanged.

**Reverse return (≤ 6 lines):** responses by type; errata rows by Field; coverage gaps; validator
lines; sealed SHA-256 re-check.
