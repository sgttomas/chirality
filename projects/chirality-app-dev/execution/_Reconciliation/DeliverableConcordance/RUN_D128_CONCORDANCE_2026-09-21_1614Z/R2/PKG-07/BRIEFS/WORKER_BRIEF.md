# Worker brief — R2 concordance ledger, one deliverable (TASK, Type 2) — PKG-07

You are a TASK (Type 2) worker in run `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128; R2
authorized by D-APP-129), dispatched by the PKG-07 WORKING_ITEMS manager (wave 3). You do not
delegate. Your dispatch prompt supplies: `<DEL-ID>`, `<DEL-FOLDER>` (the deliverable folder name),
`<OUT>` (your output folder), and the placeholder values `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`.
Use the values to work; **never write an absolute path into any output** — outputs use
repo-relative paths such as `projects/chirality-app-dev/frontend/src/lib/x.ts:120`.

## Target

- Deliverable: `<FROZEN_TREE>/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/<DEL-FOLDER>/`
  (ScopeOfWork.md, _STATUS.md, _CONTEXT.md, MEMORY.md, _DEPENDENCIES.md / Dependencies.csv,
  _REFERENCES.md, _SEMANTIC*.md, Assessment_INSP-03_*, Evidence_*, _run_records/**).
- Audit units: every row of `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` whose `DeliverableID` is `<DEL-ID>`
  (filter it with a script, e.g. `python3 -c` + `csv`; note the `SubItems` column).

## Evidence roots (strict)

You read **only**:
- `<FROZEN_TREE>/projects/chirality-app-dev/**`, **except** the deliverable folders of other
  packages (`execution/PKG-xx_*/1_Working/DEL-*` for any package other than PKG-07). Other PKG-07
  deliverables' folders may be read only to follow an explicit cross-reference from your deliverable.
  App governance (`docs/`), the decision register and ruling records
  (`execution/_Coordination/_DECISIONS/`), `execution/_ScopeChange/`, `execution/_Decomposition/`,
  and the CONTEXT sources of `RUN_BASIS.md` §5 are inside this root.
- `<FROZEN_TREE>/projects/chirality-runtime/packages/**` and `<FROZEN_TREE>/projects/chirality-runtime/tests/**`.
- The run-folder inputs named in this brief.

You do **not** read: Root `execution/`; `projects/chirality-runtime/execution/**` (never list, grep or
read it — search only `projects/chirality-runtime/packages` and `/tests`, or pass
`--exclude-dir=execution`); any other project's tree; the working repository's deliverable folders
(they carry run edits); `<RUN>/R0_CALIBRATION/**`; any folder under `<RUN>/R2/**` other than
`<RUN>/R2/PKG-07/EVIDENCE_PACK/`, `<RUN>/R2/SURFACES/` (pass 2 only) and your own `<OUT>`. In
particular never read another worker's folder, another package's R2 folder, or any R0 ledger.

## Read first

1. `<RUN>/CONVENTIONS.md` **in full** — it is your rulebook and is self-contained.
2. `<RUN>/RUN_BASIS.md` §3, §5 and Addenda 1–7.
3. The evidence pack `<RUN>/R2/PKG-07/EVIDENCE_PACK/` (`PACK_MANIFEST.md` first):
   - `TOUCHED_PATHS.csv` — the post-release touched paths with line ranges (PostReleaseBasis);
   - `REACHABILITY.csv` — the static module map (LIVE / LEGACY_ONLY / TEST_ONLY / UNREACHED);
   - `REFERENCE_HASHES.csv` — every PKG-07 `_REFERENCES.md` MATCH hash fails to reproduce;
   - `DECISION_HITS.csv` — decision IDs cited by / naming your deliverable;
   - `D-APP-127_APPLICATION_MAP.csv` — **no** PKG-07 carrier (not even `_STATUS.md`) cites D-APP-127/D-GOV-43.
4. Helpful R1 inventories (read by script, filter to your deliverable): `R1_INVENTORY/HINTS/<DEL-ID>.csv`
   (grep hits of claim tokens in code — hints, not evidence), `IMPLEMENTATION_SURFACES.csv`,
   `VERIFICATION_INDEX.csv`, `DECISION_INDEX.csv`, `REMAINING_INVENTORY.csv`, `DIRECTION_RECORD_INDEX.csv`.
5. Gate transcripts: `<RUN>/GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`,
   `GATE_TRANSCRIPT_RUNTIME_00115c719.md` (cite as `GATE-TRANSCRIPT(APP@00115c719)` etc. plus the
   named test file and case).

## Reading discipline (CONVENTIONS §7)

- Read deliverables and code **from `<FROZEN_TREE>` only**.
- Economize: grep before you read, read line ranges, prefer deliverable files and the evidence pack
  over broad sweeps. Read CSVs by script rather than dumping them.
- Git: **only** read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show` and
  `git -C <FROZEN_TREE> blame -L` — nothing else, nothing against the working repository.
- No installs, no test runs, no builds. No edits anywhere outside `<OUT>`.

## Reachability (read this carefully)

`REACHABILITY.csv` is import-based and module-level. A re-export or a single imported helper marks a
whole module LIVE, and some LIVE-tagged modules are never rendered or executed (for example retired
Pipeline / Workbench / Portal presentation components, barrel re-exports, unmarked type-only
imports). **Treat it as a starting hint.** Before tagging `REACH=LIVE`, confirm reach **for the specific
symbol you cite** from the actual entry point: the rendered page/component tree, the route handler
that actually executes the code, the Electron main process, or the packaged runtime-service entry
(for `projects/chirality-runtime/packages/**`, follow the path from the App's runtime-service host
into the package). If the map says LIVE but the symbol is not executed on the product path, tag what
you found (`REACH=LEGACY_ONLY` + `UNREACHED` in Notes when nothing reaches it, or `REACH=TEST_ONLY`)
and state the map disagreement in Notes. In pass 2, note in reverse_notes where a capability file's
REACH/STATE note disagrees with the pack or with your ledger. Say in your notes file how you
confirmed reach.

## Authority order

- The App DIRECTIVE §2.8 was **never amended for D-GOV-43**. Do not assume the Codex-only preambles of
  PRD/CONTRACT win automatically. Apply CONVENTIONS §1 (MR-11 only when the ruling explicitly
  addresses the clause or deliverable) and the DIRECTIVE §0 authority order: where §0 resolves a
  disagreement among GOVERNING sources, apply it and cite both; where a ruling undercuts an
  unamended GOVERNING clause without naming it, or §0 does not resolve it, the row is
  `AUTHORITY_CONFLICT` with `HumanDecisionNeeded = R4` or the matching `R4-Qn`.

## Named R4 questions (CONVENTIONS §2.4; cite instead of plain `R4` whenever the row turns on one)

- `R4-Q1`: legacy in-process harness versus the live Codex path (retained harness code: history,
  compatibility or obligation; K-PATH, K-ROOT, K-HOOK, SPEC §15.2 unamended for D-GOV-43).
- `R4-Q2`: the Codex engine never run through the K-ENGINE-2 conformance suite.
- `R4-Q3`: the actor check on the legacy `status_transition` tool, which the agent supplies itself.
- `R4-Q4` (RUN_BASIS Addendum 4): whether the 2026-09-09 v3 four-role adoption (`9b005c23a`; alias
  map, default role, retired agent matrix and Pipeline surface, new agent-file header format) is a
  governing amendment of SPEC §7 and §13 and the persona and matrix contracts, which were not amended.
- `R4-Q5` (RUN_BASIS Addendum 7): Codex event payloads, stored as received (amended CONTRACT
  K-EVENT-1/K-EVENT-6, SPEC §11) or translated (unamended K-ENGINE-4, SPEC §10.3)?

## Rule texts adopted by owner direction (verbatim; apply to your forward pass)

**RUN_BASIS Addendum 5 / CONVENTIONS §2.6 — Tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`:**

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

**RUN_BASIS Addendum 6 / CONVENTIONS §2.4 — Legacy-versus-live subject test (R4-Q1):**

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

## Known pitfalls from R0 calibration and waves 1–2 (reminders, not new rules)

- **PKG-07 specifics.** Working-root validation and instruction-root protection (DEL-07-01) are
  path-containment guarantees: decide the subject by the test above and judge on the live path
  (the Codex sandbox/approval path versus the App's own gates). The `status_transition` tool (DEL-07-04)
  is where R4-Q3 lives; its route/API surface and its MCP-tool surface may differ in reach — tag each.
  Scaffolding, metadata/document-kit, Dependencies.csv and reference-hash tooling (DEL-07-02..06) may
  live in App `frontend/**`, in Runtime packages, or only in Root tools outside your evidence roots:
  when the only implementation is outside your roots, write `NONE_FOUND` after a stated search and say
  so in Notes; do not read Root `tools/` or Root `execution/` to confirm it.
- **Engine surface.** Codex is the sole production engine (D-GOV-43 / D-APP-127). Judge each
  requirement on the live path, tag every code citation with REACH, and choose the CauseTag by
  mechanism (`CAUSE2:` for a secondary).
- **MR-11 vs AUTHORITY_CONFLICT (§1).** A decomposition/SCA/SoW restatement against an **amended**
  CONTRACT or SPEC clause is resolved by DIRECTIVE §0 (usually STALE_SPECIFICATION), not AUTHORITY_CONFLICT.
- **DirectionEvidence.** Search `execution/_Coordination/_DECISIONS/_REGISTER.md` and CONTEXT sources
  before `NONE_FOUND`, and name the search in Notes. Prefix every record `CTX:` or `GOV:`.
  `ALIGNED`/`NOT_AUDITABLE` rows take `NOT_APPLICABLE`. Do not repeat an unverified gloss down a SEE chain.
- **PostReleaseBasis.** Do not assume `NO`: for each cited file listed in `TOUCHED_PATHS.csv`, run
  `git -C <FROZEN_TREE> blame -L <a>,<b> 00115c719 -- <path>` over the whole cited range (wave 1 missed
  a single line inside a cited range that blamed to `da95ec194`).
- **Register defects.** The `_REFERENCES.md` hash drift is one `REGISTER-n` row per deliverable
  (`HASH-RECOMPUTE@00115c719`); SoW rows restating it cite that key. Look also for stale conflict
  tables, stale dependency notes and stale status metadata.
- **Carrier propagation.** No PKG-07 carrier cites D-APP-127/D-GOV-43. Where the SoW, `_STATUS.md`,
  `_CONTEXT.md` or `Dependencies.csv` still describe the pre-D-GOV-43 topology or engine, say so
  (CARRIER_PROPAGATION or the mechanism tag, per §4 precedence).
- **SubItems.** A unit listing k ≥ 2 REQ/AC/VER items needs ≥ k rows, one `.n` per item, the item named
  in Notes (validator `V-SUBITEMS`).
- **AuthorityTier** = the highest source *restated*; `NOT_APPLICABLE` only for CONTEXT_CLAIM and for
  STATE_ASSERTION/REGISTER_DEFECT rows that restate nothing normative.
- **CauseTag** names the mechanism; PRE_V3_DRIFT for pre-2026-08-22 divergence unless a v3 mechanism
  applies; UNRECORDED_JUDGMENT only with `DirectionEvidence = NONE_FOUND`.
- A wrong citation or gloss is a defect even when the Disposition holds: cite lines that exist at the
  frozen tree and say what they actually do.
- **Coverage gaps.** If you find an indexed work item or SoW scope that no forward row can own (for
  example a SoW section that is not an indexed unit), record it under a `## Coverage gaps` heading in
  your notes file.

## Pass 1 — forward (then STOP)

1. Write `<OUT>/<DEL-ID>_claims.csv` (25-column header from CONVENTIONS §2.1, rows, final `#END`; use a
   CSV writer) and `<OUT>/<DEL-ID>_notes.md` (§3 sections 1–6, plus `## Coverage gaps` if any).
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
