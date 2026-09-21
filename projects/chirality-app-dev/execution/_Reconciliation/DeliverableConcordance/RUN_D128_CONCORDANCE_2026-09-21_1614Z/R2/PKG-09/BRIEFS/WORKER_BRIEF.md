# Worker brief — R2 concordance ledger, one deliverable (TASK, Type 2) — PKG-09

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-09 WORKING_ITEMS manager (wave 5: packaging,
signing, notarization and release proof). You do not delegate. Your dispatch prompt supplies:
`<DEL-ID>`, `<DEL-FOLDER>` (the deliverable folder name), `<OUT>` (your output folder), the values of
`<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`, and, for a split worker, a `<PART>` section (below).
Use the values to work; **never write an absolute path into any output** — outputs use repo-relative
paths such as `projects/chirality-app-dev/frontend/scripts/pack-electron.mjs:86`.

## Target

- Deliverable: `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/<DEL-FOLDER>/`
  (ScopeOfWork.md, _STATUS.md, _CONTEXT.md, MEMORY.md, _DEPENDENCIES.md / Dependencies.csv,
  _REFERENCES.md, _SEMANTIC*.md, Assessment_INSP-03_*, Evidence*, _run_records/**, and any other file in it).
- Package-level evidence in the frozen tree, where relevant, in
  `.../PKG-09_Validation_Packaging_Security_and_Release/1_Working/`:
  `Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md`, `Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`,
  `Evidence_ADQ-16_Secret_Network_Proof.md`.
- Audit units: every row of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
  (filter it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column, `|`-separated).

## Read first

1. `<RUN>/CONVENTIONS.md` **in full** — it is your rulebook and is self-contained.
2. `<RUN>/RUN_BASIS.md` §3, §5 and Addenda 1–7.
3. The evidence pack `<RUN>/R2/PKG-09/EVIDENCE_PACK/` (`PACK_MANIFEST.md` first):
   - `TOUCHED_PATHS.csv` — the post-release touched paths with line ranges (PostReleaseBasis);
   - `REACHABILITY.csv` — the static REACH map (LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED); it does
     **not** cover build/packaging scripts (see the manifest's content notes);
   - `REFERENCE_HASHES.csv` — no PKG-09 `_REFERENCES.md` MATCH hash reproduces at the frozen basis;
   - `DECISION_HITS.csv` — decision IDs cited by / naming your deliverable;
   - `D-APP-127_APPLICATION_MAP.csv` — which carriers cite D-APP-127/D-GOV-43.
4. Helpful R1 inventories (read by script, filter to your deliverable): `R1_INVENTORY/HINTS/<DEL-ID>.csv`
   (grep hits of claim tokens in code — hints, not evidence), `IMPLEMENTATION_SURFACES.csv`,
   `VERIFICATION_INDEX.csv`, `DECISION_INDEX.csv`, `REMAINING_INVENTORY.csv`, `DIRECTION_RECORD_INDEX.csv`.
5. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`,
   `GATE_TRANSCRIPT_RUNTIME_00115c719.md` (cite as `GATE-TRANSCRIPT(APP@00115c719)` etc. plus the
   named test file and case). They cover typecheck, Vitest and the Runtime build only: no packaging,
   signing, DMG or release run was executed for this run.
6. If `<OUT>/PREGATHER.md` exists (or the prompt names one), use it as a map of candidate code and
   test paths — verify everything you cite yourself.
7. CONTEXT only (RUN_BASIS §5; CONVENTIONS §1): `<RUN>/R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md`.
   Its questions Q-01..Q-13 are **not** HumanDecisionNeeded tokens and are never cited as rulings; mention
   the relevant `Q-nn` in Notes. **Q-02** (whether the session publishing approval counts as the release act
   and F-APP-2 fence lift; D-APP-97 keeps F-APP-2 fencing signing, notarization and distribution) is the one
   most likely to touch PKG-09 rows.

## Evidence roots and reading discipline (CONVENTIONS §7; strict for this wave)

- Read **only**:
  - `<FROZEN_TREE>/projects/chirality-app-dev/**` — **except** other packages' deliverable folders
    (`execution/PKG-0x_*/` for any package other than PKG-09). Decision records, the register, the
    decomposition, SCAs, `plans/**` CONTEXT sources, `docs/**` and `frontend/**` (including
    `frontend/scripts/**`, `frontend/package.json`, the builder config) and
    `projects/chirality-app-dev/.github/workflows/**` are in bounds;
  - `<FROZEN_TREE>/projects/chirality-runtime/packages/**` and `<FROZEN_TREE>/projects/chirality-runtime/tests/**`;
  - the run-folder inputs named in this brief;
  - Root governance docs (`<FROZEN_TREE>/docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md`) only where the App docs
    defer to them (RUN_BASIS §5), and Root instruction-bundle sources (root `AGENTS.md`, `agents/**`,
    `workflows/`, `.agents/skills`, `tools/`) only where your deliverable packages them, as packaged
    product content (RUN_BASIS §3).
- **Never** read Root `execution/`, the repository-root `.github/**`, `projects/chirality-runtime/execution/**`,
  or any other project's execution tree. Exclude them explicitly in every search (e.g. search only
  `projects/chirality-runtime/packages` and `projects/chirality-runtime/tests`; `grep -r --exclude-dir=execution`).
  If the only evidence for a claim lies outside these roots, do not read it: judge on in-root evidence and write
  `OUT_OF_ROOT:<path>` in Notes.
- Never read the working repository's deliverable folders (they carry run edits); read deliverables from
  `<FROZEN_TREE>` only.
- Economize: grep before you read, read line ranges, prefer deliverable files and the evidence pack over
  broad sweeps. Read CSVs by script rather than dumping them.
- Git: **only** read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L` — nothing else, nothing against the working repository.
- No installs, no test runs, no builds, no packaging runs. No edits anywhere outside `<OUT>`.
- Do not read `<RUN>/R0_CALIBRATION/**` (including the R0 DEL-09-07 ledger), or any other worker's or
  package's folder under `<RUN>/R2/**` (including other PKG-09 deliverable folders, any `_A`/`_B` or `P1`/`P2`
  sibling not named in your prompt, and every other `R2/PKG-*` or `R2/EXT` folder). You may read
  `<RUN>/R2/SURFACES/**` only when the manager names a file in pass 2.

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

  HELP_HUMAN clarification of rule 3 (verbatim): Cite R4-Q1 only when LEGACY_ONLY code is the only code
  meeting the claim on the product path. TEST_ONLY code does not meet a product claim.
- **Named R4 questions** (CONVENTIONS §2.4). Cite the named question instead of plain `R4` whenever the
  row turns on it: `R4-Q1` (legacy in-process harness vs live Codex path: is retained harness code history,
  compatibility or obligation), `R4-Q2` (Codex engine never run through K-ENGINE-2 conformance), `R4-Q3`
  (actor check on the legacy `status_transition` tool), `R4-Q4` (whether the 2026-09-09 v3 four-role adoption
  `9b005c23a` is a governing amendment of SPEC §7/§13 and the persona and matrix contracts), `R4-Q5` (Codex
  event payloads stored as received — amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11 — or translated —
  unamended K-ENGINE-4, SPEC §10.3), `R4-Q6` (RUN_BASIS Addendum 9: do the unamended App DIRECTIVE §2.8, §2.10,
  §4.1, §4.2 and CONTRACT K-PERM-1/K-PERM-6 still bind the Codex-hosted App, or did D-GOV-43 supersede them — the
  Anthropic API-key UI, the live "Full access" option, the unfiltered `~/.codex` link; Dispositions unchanged, the
  owner's recorded answer becomes GOVERNING only at R4). Done-declaration questions (Q-02 etc.) go in Notes only.
- **CauseTag for the v3 role adoption.** Where the cause is the 2026-09-09 v3 four-role adoption, write exactly
  `OTHER:V3_ROLE_ADOPTION`.
- **Reachability is a starting hint, not a verdict.** `REACHABILITY.csv` is import-based and module-level: a
  re-export or one imported helper marks a whole module LIVE, and some LIVE-tagged modules are never rendered
  or executed. Before tagging `REACH=LIVE`, confirm that the specific symbol you rely on is reached from an
  actual product entry point. For PKG-09 the relevant entries are also the **packaging and build entries**:
  the `frontend/package.json` scripts that build, pack, sign and verify the App (e.g. the script that runs
  `frontend/scripts/pack-electron.mjs`), the builder configuration, `frontend/electron/main.ts`, and the
  packaged runtime-service entry. A build/packaging script is `REACH=LIVE` when a `package.json` release or
  packaging script (or the in-root workflow) invokes it in the default path; a script no such entry invokes, or
  a code branch that is disabled by default (e.g. signing without an identity), is judged as not live —
  say so in Notes (`UNREACHED` or `DISABLED_BY_DEFAULT`). A script invoked only by a test is `REACH=TEST_ONLY`.
- **Judge on the live path** (§2.3 ImplementationEvidence): a requirement met only on a `LEGACY_ONLY` path is
  `PARTIALLY_IMPLEMENTED` / `IMPLEMENTED_DIFFERENTLY` / `DOCUMENTED_UNIMPLEMENTED` per the rule, never
  `ALIGNED`. Tag every code citation with REACH.
- **Proof versus capability.** Many PKG-09 claims are about release *proof* (a signed, notarized, verified
  DMG; recorded proof runs). Code that could produce the proof is not the proof. Distinguish the capability
  (script present and live) from the recorded evidence of a run (evidence file, run record), and do not
  treat an agent-recorded run as a ruling.
- **MR-11 vs AUTHORITY_CONFLICT (§1).** Apply MR-11 only when the ruling explicitly addresses the clause or
  deliverable. A ruling (e.g. D-GOV-43/D-APP-127) that undercuts an unamended GOVERNING clause without naming
  it → `AUTHORITY_CONFLICT` + R4/R4-Qn. Where DIRECTIVE §0's order resolves it, apply it and do not use
  AUTHORITY_CONFLICT. Note: the App DIRECTIVE §2.8 was never amended for D-GOV-43; apply CONVENTIONS §1 and
  the DIRECTIVE §0 authority order.
- **Retired content.** `RETIRED_BY_RULING` applies only where a GOVERNING ruling names the deliverable or item
  retired and preserves its text as history (§2.6 iii); cite that ruling (governing) in `LatestDecision`.
  CONTEXT or an agent tranche return saying "retired" is not a ruling. Text outside the preserved set stays
  under MR-11.
- **DirectionEvidence.** Search `execution/_Coordination/_DECISIONS/_REGISTER.md` and CONTEXT sources before
  `NONE_FOUND`, and name the search in Notes. Prefix every record `CTX:` or `GOV:`. `ALIGNED`/`NOT_AUDITABLE`
  rows take `NOT_APPLICABLE`.
- **PostReleaseBasis.** Do not assume `NO`: for each cited file listed in `TOUCHED_PATHS.csv`, run
  `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` on the relied-on lines.
- **Register defects.** The `_REFERENCES.md` hash drift is one `REGISTER-n` row per deliverable
  (`HASH-RECOMPUTE@00115c719`); SoW rows restating it cite that key. Look also for stale conflict tables,
  stale dependency notes and stale status metadata.
- **Carrier propagation.** Where the SoW still describes the pre-D-GOV-43 topology or engine (daemon,
  LaunchAgent, per-root homes, Claude/Anthropic/Pi engine, two-job installer) while code has moved, say so
  with the right CauseTag.
- **SubItems.** A unit listing k ≥ 2 REQ/AC/VER items needs ≥ k rows, one `.n` per item, the item named in
  Notes (validator `V-SUBITEMS`).
- **AuthorityTier** = the highest source *restated*; `NOT_APPLICABLE` only for CONTEXT_CLAIM and for
  STATE_ASSERTION/REGISTER_DEFECT rows that restate nothing normative.
- **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism applies;
  UNRECORDED_JUDGMENT only with `DirectionEvidence = NONE_FOUND`; secondaries as `CAUSE2:`.
- A wrong citation or gloss is a defect even when the Disposition holds: cite lines that exist at the frozen
  tree and say what they actually do.
- **Coverage gaps.** If you find an indexed work item or SoW scope that has no forward row you can own (e.g.
  work delivered but undocumented, or scope whose owner is unclear), record it in your notes file under a
  "Coverage gaps" subsection — never as a new row after sealing.

## Split workers only (`<PART>` given in your prompt)

Your prompt names your part (`P1` or `P2`), the indexed units you own, and a part index file
`<PART_INDEX>`. Write your ledger for **only those units** plus the run-local rows assigned to your part, as
`<OUT>/<DEL-ID>_claims.csv` (same file name; `<OUT>` is your part subfolder) with its own notes file. Number
run-local rows in the range your prompt gives, so the manager can merge both parts without key collisions.
Validate with `--index <PART_INDEX>` added after `ledger` (the part index lists exactly your units). The
manager merges the two parts by script and validates the merged ledger; you may read the deliverable in full
for context, but never the other part's folder.

## Pass 1 — forward (then STOP)

1. Write `<OUT>/<DEL-ID>_claims.csv` (25-column header from CONVENTIONS §2.1, rows, final `#END`) and
   `<OUT>/<DEL-ID>_notes.md` (§3 sections 1–6, plus "Coverage gaps").
2. From `<APP_WORK>` run:
   `python3 <RUN>/_scripts/validate_ledger.py ledger <OUT>/<DEL-ID>_claims.csv`
   (split workers: `ledger --index <PART_INDEX> <OUT>/<DEL-ID>_claims.csv`).
   Errors must be 0 (warnings reported). Fix and re-run until it passes.
3. Compute `shasum -a 256 <OUT>/<DEL-ID>_claims.csv`. The ledger is now **sealed**: never edit it again.
4. Return a short summary (≤ 8 lines): row count, Disposition census, validator RESULT line, the SHA-256, and
   your top 3 findings. **Then stop and wait** — the manager will resume you for pass 2.

## Pass 2 — reverse (only when the manager resumes you)

The manager's message names one or more capability files from `<RUN>/R2/SURFACES/` (and, for a split
deliverable, the merged ledger you answer for).

1. Write `<OUT>/<DEL-ID>_reverse.csv`: header `CapabilityID,Response,ClaimKey,Rationale`, one row per
   capability in **every** named file (concatenate in the order given), final `#END`. Response ∈
   `CLAIMED_BY` (+ owning ClaimKey), `PARTIAL` (+ the key covering part), `NOT_MINE` (empty ClaimKey).
2. Forward-row corrections found now go to `<OUT>/<DEL-ID>_errata.csv`
   (`ClaimKey,Field,SealedValue,ProposedValue,Evidence`, `#END`; one row per (ClaimKey, Field); SealedValue
   copied exactly). A missing forward row (coverage gap) is **not** an erratum: describe it in
   `<OUT>/<DEL-ID>_reverse_notes.md`. Explanations go in reverse_notes. If an errata file exists, also put
   sealed vs errata-applied census figures in reverse_notes.
3. Validate from `<APP_WORK>`: for each capability file,
   `python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <cap.csv> <OUT>/<DEL-ID>_reverse.csv`
   — once per named capability file; and, if present,
   `python3 <RUN>/_scripts/validate_ledger.py errata <OUT>/<DEL-ID>_errata.csv` (split deliverables: add
   `--ledger <merged claims path>` as the manager's message says). Errors must be 0.
4. Confirm the claims SHA-256 is unchanged. Return ≤ 8 lines: response counts, errata count, validator
   results, seal status.
