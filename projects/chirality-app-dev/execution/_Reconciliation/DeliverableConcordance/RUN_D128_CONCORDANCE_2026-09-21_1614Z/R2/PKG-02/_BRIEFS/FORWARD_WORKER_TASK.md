# Brief — R2 PKG-02 concordance worker (TASK, Type 2)

**Role.** TASK (Type 2). Do not delegate. Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128;
R2 authorized by D-APP-129). Manager: the PKG-02 WORKING_ITEMS manager, who resumes you later for the
reverse pass. Your disposition is evidence, never a ruling.

**Placeholders** (values are given in your dispatch prompt; never write the values into any output):
`<DEL-ID>`, `<FROZEN_TREE>` (frozen reading tree at `00115c719`), `<RUN>` (run folder), `<APP_WORK>`
(the working `projects/chirality-app-dev`, used **only** as the directory from which you run the
validator), `<DEL-FOLDER>` (deliverable folder, repo-relative), `<OUT>` (your output folder, given in the
dispatch prompt; normally `<RUN>/R2/PKG-02/<DEL-ID>`). If your dispatch prompt names a split half, also
follow `<RUN>/R2/PKG-02/_BRIEFS/SPLIT_PLAN.md`.

## Read first

1. `<RUN>/CONVENTIONS.md` **in full**. It is your rulebook and is self-contained. Apply it literally.
2. `<RUN>/RUN_BASIS.md` §3, §4, §5 and Addenda 1–7 (authority map: GOVERNING / flagged / CONTEXT).
3. Your deliverable at `<FROZEN_TREE>/<DEL-FOLDER>/`: `ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`,
   `Dependencies.csv`/`_DEPENDENCIES.md`, `_REFERENCES.md`, `MEMORY.md`, `_SEMANTIC*.md`,
   `Assessment_INSP-03_*`, `_run_records/**` (as needed).
4. `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` rows for `<DEL-ID>` (grep; note the `SubItems` column),
   `REMAINING_INVENTORY.csv` rows for `<DEL-ID>`, `HINTS/<DEL-ID>.csv` (summarize by script),
   `VERIFICATION_INDEX.csv`, `DIRECTION_RECORD_INDEX.csv` (CONTEXT locator).
5. Evidence pack `<RUN>/R2/PKG-02/EVIDENCE_PACK/` (see its `PACK_MANIFEST.md`): `TOUCHED_PATHS.csv`,
   `REACHABILITY.csv`, `REFERENCE_HASHES.csv`, `DECISION_HITS.csv`, `D-APP-127_APPLICATION_MAP.csv`.
6. If it exists: `<RUN>/R2/PKG-02/<DEL-ID>/PREGATHER.md` — candidate paths gathered by a read-only
   TASK. It is a locator, not evidence: open and confirm every path you cite.
7. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_{APP,RUNTIME}_00115c719.md`.
8. Decision register and rulings at
   `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/` (`_REGISTER.md`
   first; open ruling records as needed). Governing docs at
   `<FROZEN_TREE>/projects/chirality-app-dev/docs/{PRD,DIRECTIVE,CONTRACT,SPEC,TYPES}.md` and Root
   `<FROZEN_TREE>/docs/*` where App docs defer.

## Reading discipline (CONVENTIONS §7) — mandatory

- Read from `<FROZEN_TREE>` only. **Never** read the working repository's deliverable folders (they
  carry run edits). Never read, list or grep `projects/chirality-runtime/execution/**` or any other
  project's execution tree: exclude it explicitly in every search (scope runtime greps to
  `projects/chirality-runtime/packages/` and `projects/chirality-runtime/tests/`).
- Do **not** read anything under `<RUN>/R0_CALIBRATION/` (calibration ledgers, verification, surfaces),
  nor any other worker's or package's folder under `<RUN>/R2/` (only `EVIDENCE_PACK/`, your `<OUT>`, the
  `PREGATHER.md` named above, and — in the reverse pass — the capability files the manager names).
- Economize: grep before you read, read line ranges, prefer deliverable files and the pack.
- Git: only read-only `git -C <FROZEN_TREE> log`, `show`, `blame -L` against the frozen tree. No other
  git, and nothing against the working repository. **No installs, no test runs, no builds.**
- Write only `<OUT>/<DEL-ID>_claims.csv`, `<OUT>/<DEL-ID>_notes.md` (forward), and later
  `<OUT>/<DEL-ID>_reverse.csv`, `_errata.csv`, `_reverse_notes.md`. **No absolute paths in any
  output** (repo-relative paths only; the validator checks).

## Rules adopted after R0 — verbatim rule texts (apply from the start)

**RUN_BASIS Addendum 5 — tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`
(CONVENTIONS §2.6, verbatim):**

> **Tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`** [A0: owner direction
> `r2_tiebreak_adopt`, RUN_BASIS Addendum 5]:
>
> 1. Use `STALE_SPECIFICATION` when the text states a present fact that is now false (a hash
>    recorded as `MATCH`, a path called "current", a dependency marked `SATISFIED`, a file said
>    to exist). The rule is the same for SoW, `_STATUS`, register and references text.
> 2. Use `REMAINING_STATE_MISMATCH` only for (a) an item in `## Remaining`, or a `REMAINING_WORK`
>    row, whose open or done status is contradicted by the evidence; or (b) register
>    bookkeeping that is behind but says nothing false about the product or its references
>    (a `Last Updated` date, a `TBD` placeholder, a lagging status field).
> 3. MR-8(iv) clarified: a claim tied to a named snapshot ("MATCH at v23") stays a REGISTER row.
>    Text that restates it as current ("is MATCH") without naming the snapshot takes
>    `STALE_SPECIFICATION` and points to the REGISTER row (`SEE:`).
> 4. If both still fit, choose the verdict whose repair is a change to deliverable text, and
>    record the other in Notes as `ALSO:<verdict>`.

**RUN_BASIS Addendum 6 — legacy-versus-live subject test for R4-Q1 (CONVENTIONS §2.4, verbatim):**

> **Legacy-versus-live subject test (R4-Q1)** [A0: owner direction `r2_r4q1_subject_test`,
> RUN_BASIS Addendum 6]. It makes precise the §2.3 ImplementationEvidence rule on module-level
> claims:
>
> 1. **Decide the subject from the claim text, not from where the code lives.** The subject is
>    *product behaviour* if the claim names the App, the system, the user, a session, a turn or
>    an agent run; states an observable outcome (something allowed, blocked, recorded, shown or
>    sent); or states a guarantee or control (permission, path containment, hooks, redaction,
>    approval), even when the text also names the component meant to provide it. The subject
>    is *the module* only if the claim names a specific code unit (class, function, file, tool
>    or API) and describes only that unit's own contract (inputs, outputs, structure), with no
>    outcome the product can observe.
> 2. **If the text supports both readings, treat it as product behaviour** and judge it on the
>    live path (§2.3).
> 3. **R4-Q1 is cited by evidence, not by opinion.** Cite `R4-Q1` in HumanDecisionNeeded on every
>    row where the only code meeting the claim is tagged `REACH=LEGACY_ONLY`, whether the row is
>    judged on the live path or at module level. Rows met by `LIVE` code, and rows with no code
>    evidence, do not cite R4-Q1 for this reason.
> 4. **Record the other reading.** On a product-behaviour row met only by legacy code, add
>    `ALSO_MODULE:<verdict>` to Notes, giving the verdict a module-level reading would have
>    produced.

**RUN_BASIS Addendum 4 — R4-Q4.** Rows turning on whether the 2026-09-09 v3 four-role adoption
(`9b005c23a`; alias map, default role, retired agent matrix and Pipeline surface, new agent-file header
format) is a governing amendment of SPEC §7 and §13 and the persona and matrix contracts cite `R4-Q4`
(CONVENTIONS §2.4). The retired Pipeline surface and agent matrix are squarely in PKG-02's scope.

**RUN_BASIS Addendum 7 — R4-Q5.** Rows turning on whether Codex event payloads are stored as received
(amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11) or translated (unamended K-ENGINE-4, SPEC §10.3) cite
`R4-Q5` instead of plain `R4` (CONVENTIONS §2.4; the validator accepts it, including on
AUTHORITY_CONFLICT rows).

## Forward pass (do this now)

1. Build `<OUT>/<DEL-ID>_claims.csv` per CONVENTIONS §2 (25-column header; every indexed unit at least
   once; SubItems → ≥ k rows; REM rows with verbatim gates; `REGISTER-n` / `STATE-n` run-local rows;
   final `#END` record) and `<OUT>/<DEL-ID>_notes.md` per §3 (all six sections).
2. Points calibration and waves 1–2 showed workers get wrong (apply the adopted rules, do not
   over-read them):
   - **Reach is module-level in the pack; confirm it for the symbol.** `REACHABILITY.csv` is
     import-based: a re-export or one imported helper marks a whole module `LIVE`, and some
     `LIVE`-tagged modules (e.g. retired Pipeline / Workbench / Portal presentation) are never
     rendered or constructed. Before tagging `REACH=LIVE` for a claim, confirm from the actual entry
     point (`frontend/src/app/**` pages, `frontend/src/app/api/**` routes, `frontend/electron/main.ts`)
     that the specific symbol the claim relies on is rendered, called or constructed on the product
     path. Where the module is LIVE by import but the symbol is not used, keep the pack's tag in
     ImplementationEvidence, state the symbol-level fact in Notes (`SYMBOL-UNREACHED: <why>`), and
     judge the claim on what the product actually does (§2.3).
   - **Authority order (§1).** The App DIRECTIVE §2.8 was never amended for D-GOV-43. Do not assume
     the Codex-only preambles of PRD/CONTRACT automatically win: apply CONVENTIONS §1 and the DIRECTIVE
     §0 authority order yourself, cite both sources, and use `AUTHORITY_CONFLICT` + `R4`/`R4-Qn` only
     where that order does not resolve the disagreement.
   - **MR-11 vs AUTHORITY_CONFLICT (§1):** use MR-11 only when the ruling explicitly addresses the
     clause or deliverable. Never resolve an authority conflict yourself.
   - **Reachability:** every code-evidence row carries `REACH=` from `REACHABILITY.csv`; apply the
     Addendum 6 subject test above. `R4-Q1` by evidence (rule 3); K-ENGINE-2 conformance of Codex →
     `R4-Q2`; `status_transition` actor check → `R4-Q3`; v3 four-role adoption → `R4-Q4`; Codex event payloads as received vs translated → `R4-Q5`.
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
     D-APP-127 are `CARRIER_PROPAGATION` (pack item 5: every PKG-02 carrier is `NO` except DEL-02-05
     `_STATUS.md`). The shell redesign (SCA-APP-010) is `SHELL_REDESIGN`.
   - Line anchors: cite lines at the frozen tree.
   - LOW rows need `LEAST-CONFIDENT:` with the alternative reading.
3. **Coverage gaps.** If you find an indexed work item or SoW scope item for which there is no forward
   row you can own (e.g. the code exists but the unit that would own it is in another deliverable, or
   scope in `_STATUS`/decisions has no indexed unit), record it in notes §5 under a heading
   `Coverage gaps (for R3)`; do not invent keys for it.
4. Validate, from `<APP_WORK>`:
   `python3 <RUN>/_scripts/validate_ledger.py ledger <OUT>/<DEL-ID>_claims.csv`
   (split halves: add `--index <RUN>/R2/PKG-02/_split/INDEX_<half>.csv`, see SPLIT_PLAN.md).
   Errors must be zero. Report warnings.
5. Compute `shasum -a 256 <OUT>/<DEL-ID>_claims.csv`. The ledger is now **sealed**: never edit it
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
concatenation by script of the named area files' rows; read the area files and their `<AREA>_notes.md`
themselves for content) and
`python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv` when errata exist.
Confirm the sealed SHA-256 is unchanged.

**Reverse return (≤ 6 lines):** responses by type; errata rows by Field; coverage gaps; validator
lines; sealed SHA-256 re-check.
