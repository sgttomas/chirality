# D-PEC-100 — Scope of Work rebuild for the S2 rebuild class (DEL-01-01, DEL-01-06, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07) — proposal

Status: **DRAFT PROPOSAL / AWAITING_RULING**. **The number D-PEC-100 is provisional**: it becomes final only when HELP_HUMAN publishes this packet in `_DECISIONS/` with its register row. Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S2) for the PEC loop, 2026-09-26 (session date), from brief `briefs/S2P_SOW_REBUILD_PROPOSAL.md` (SHA-256 `31313b8fafc7fd25ea351eb2826a9e3c64cd5c5f9541f169a5f451a2cb6692d3`) and HELP_HUMAN's relayed brief amendment (quoted under Provenance). No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every check ran on `git archive` exports. At `origin/main` `dfb089b8a` the register has no D-PEC-100 row. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md`.

The act it asks for is bounded: **replace seven existing `ScopeOfWork.md` files with the exact bytes tabled below**, in one run of a bound act script, with no lifecycle change. Add-on M (question 3) is separate.

## Provenance

- **Owner acts relied on.**
  - The owner's 2026-09-25 steering, recorded in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…5a6b`): "You can continue with all the open work you identified." The work graph turns it into node S2, "SOW currency: rebuild class outside the S4 set" (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`, `5cee83f9…6788` at `dfb089b8a`; the S2 row is byte-identical at `aca930622`).
  - SCA-005 checkpoint 2 (`D-PEC-92`) accepted `Propagation_Plan.md` (`50cd0b1d…1350`). Its §B4 classes exactly eight contracts `STALE_REBUILD_REQUIRED`: DEL-01-01, DEL-01-06 ("gated on B6"), DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07 and DEL-04-01. It also carries the parser guard carry-forward and the housekeeping fixes (the unresolvable `@3623b958b` pin and the false "`_REFERENCES.md` still names revision 1.1" claim).
  - SCA-006 checkpoint 3 (accepted 2026-09-26; `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`) made decomposition revision 1.6 `current_basis` with PRD v2.4. Its Impact Assessment §7.1 (`93253b7d…b691`) classes all seven S2 deliverables `NOT_AFFECTED`.
  - `D-PEC-96` (ruled A, 2026-09-26; `D-PEC-96_RULING_2026-09-26.md`, `852057f0…399e`) and its act (PR #950, merge `73ed349ed`): registry schema v2, the closed three-profile vocabulary, PEC's row migrated. The ruling routes the stale "declares `remaining-loop` now" text to node S2 for the DEL-01-06 rebuild.
  - `D-PEC-99` (ruled A, 2026-09-26; `D-PEC-99_RULING_2026-09-26.md`) and its act (PR #957, `22502e059`): the `## Remaining` sections are retired; exhibit Part B carries DEL-02-07-REM-001..004 to node S2 (`D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`, `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`).
  - Precedents: `D-PEC-98` (ruled A + S + M, 2026-09-26) for an exact-bytes Scope of Work act with a bound script and a fresh verifier; `D-PEC-63` for a separately ruled status act.
- **Brief amendment (HELP_HUMAN, relayed 2026-09-26, recorded here as evidence).** It replaced the brief's "Method choice as an owner option" bullet: the Root notice says the owner defers action in PEC and "no adoption … is expected in this loop now", so adoption of `scope-of-work` `MODE=REVISE` is **not** put to the owner. The packet follows PEC's current practice (the `D-PEC-98` precedent) and mentions the new mode only as a one-line disclosure.
- **Fence.** `projects/pec/AGENTS.md` (`df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`) §"Write Scopes And Fences": every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the STATUS pointer needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. No earlier ruling opens the seven targets.
- **Source state.**
  - Checked at `origin/main` **`dfb089b8abae48ee699117c5bc167301963b2ab5`** (PR #961 merge) after `git fetch`. Since the drafting base `aca930622` (PR #958 merge), PR #961 changed only two work graphs and two review transcriptions; no file this packet pins, quotes or claims about changed (the S2 graph row is byte-identical).
  - **Observation commit `aca930622`** (`aca930622ba167689881416044ba0feaee3ef003`). Each candidate says that every unanchored state claim is an observation there. **Frontmatter pin `189f205ff02df4111b33c20be441ce06e65ada7a`** (SCA-006 checkpoint-3 acceptance, PR #954), an ancestor of `origin/main`. The decomposition, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv` and `docs/PRD.md` are byte-identical at the pin, at `aca930622` and at `dfb089b8a` (hashes under the grant).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`) was run from `projects/pec` with `--operation exact-correction-preparation` on all 21 possible targets (seven `ScopeOfWork.md`, seven `_STATUS.md`, seven `MEMORY.md`): `ALLOW`, exit 0, ×21 (`evidence/reliance_hold_preflight.out`).

## Method

- **Workflow.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3`; precedence project → user → bundled; no project or user workflow of that name exists). Files: `WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`, `resources/checks.md` `44ab41ac…f188`, `resources/tools.md` `fbd07771…6cc5`, `resources/representation-migration.md` `698957a5…3e3c3` (not loaded; conversion only). Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`.
- **How the rebuild is made (disclosed departure from `D-PEC-98`).** The seven candidates were **authored under `MODE=INIT` discipline** (whole contracts, source-grounded in the accepted revision-1.6 basis, `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, no evidence candidate, map, parity or finalizer). The recorded edition's `INIT` precondition is that no production contract exists; here all seven exist and validate `PASS format=SOW_V1`. So the act is **an owner-ruled exact-bytes replacement** of each contract, bound by preimage and postimage hashes, and **the method's `MODE=VERIFY` is the independent check** of each postimage. `D-PEC-98` created two new files; this act replaces seven existing ones. Authority for the bytes is this ruling, as it was for `D-PEC-98`.
- **Disclosure (one line).** Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` (`8829ac84…64af`) added `scope-of-work` `MODE=REVISE`; the owner has deferred adopting it in PEC, and this packet does not use it.
- **Rebuild rules the drafters followed** (brief `briefs/S2P_DRAFTER_BRIEF.md`, ``ab7fdc29e6c76b36b0c3abc1e0f480293cc1af5cac515fe08127290173d543fd``): keep each local ID whose meaning survives, with that meaning; retire (never reuse) an ID whose meaning is dropped; number new IDs after the highest; record a rebuild-provenance `AX-*` entry naming the prior contract hash, this packet (as "provisional `D-PEC-100`") and the retired IDs; keep every `Dependencies.csv` `EvidenceQuote` that cites the contract as a raw one-line substring; cite a sibling S2 obligation by qualified ID against the sibling's **postimage** (all seven land together), never by a sibling postimage hash.
- **Actors.** Seven Type 2 TASK drafters (one per deliverable), three rounds (author; cross-candidate reconciliation; two targeted fixes). WORKING_ITEMS integrated, bound the act and ran the checks. One fresh read-only `pec-reviewer` ran `MODE=VERIFY` and the packet review (below). Models: Opus 5.5 (`claude-opus-5-5`) at `high` for every actor, per the brief.
- **Tools** (`tools/scope_of_work/`, unchanged at `dfb089b8a`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py` `61a34722…0389`.

## What preparation found

### Scope and lifecycle

- **Seven deliverables, none in S4.** The S2 row names the six plus DEL-01-06. The S4 set fixed at SCA-006 checkpoint 2 (DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04, DEL-04-03, DEL-03-04, DEL-10-03, with DEL-00-03 through D1) contains none of them, and SCA-006 IA §7.1 classes all seven `NOT_AFFECTED`. The eighth §B4 rebuild contract, DEL-04-01, is in S4 and is not touched.
- **Lifecycle: all seven are `INITIALIZED`** at `aca930622` and at `dfb089b8a` (the brief expected five; each `_STATUS.md` was read). None is `CHECKING` or `ISSUED`.
- **What the method does to `_STATUS.md`: nothing.** `WORKFLOW.md`: "Do not modify `_STATUS.md`, lifecycle state, underscore control files, …"; `resources/checks.md` item 3: "`_STATUS.md` is byte-identical and its lifecycle state is unchanged". The standard (§8) defines `INITIALIZED` as the selected production contract existing and validating; each postimage validates, so the condition that made each deliverable `INITIALIZED` still holds after the act. **No transition is proposed**, and the act script refuses to run if any `_STATUS.md` differs from its pinned bytes.

### The candidates

| Deliverable | Lifecycle | Prior contract | Postimage | Lines | Defined IDs | Retired IDs | Checklist items | Quotes / claims checked |
|---|---|---|---|---|---|---|---|---|
| DEL-01-01 | `INITIALIZED` | `43f1f57a13bb…0170` | `14be02f5fd5b…8b88` | 245 | OUT 3, CLM 18, REQ 17, AC 17, VER 16, AX 12, TBD 6, CON 8 | AX-006 | 17 | 65 / 207 |
| DEL-01-06 | `INITIALIZED` | `5fdcfd968345…2fa8` | `2053fb65abc2…177e` | 243 | OUT 3, CLM 20, REQ 14, AC 15, VER 14, AX 12, TBD 4, CON 2 | CLM-007, CON-001, TBD-002 | 15 | 44 / 191 |
| DEL-02-03 | `INITIALIZED` | `c3e7928cbbcf…d872` | `c8bb9f1bb64d…294b` | 291 | OUT 3, CLM 22, REQ 18, AC 19, VER 18, AX 15, TBD 7, CON 6 | none | 19 | 77 / 174 |
| DEL-02-04 | `INITIALIZED` | `bdb4eea0143e…cb87` | `18183769b8b5…37b1` | 242 | OUT 2, CLM 18, REQ 15, AC 15, VER 14, AX 13, TBD 7, CON 5 | CON-002, CON-003 | 15 | 60 / 191 |
| DEL-02-05 | `INITIALIZED` | `192df47d8d3d…907e` | `0b2d571494c7…fd92` | 243 | OUT 2, CLM 19, REQ 15, AC 15, VER 14, AX 13, TBD 7, CON 7 | none | 15 | 65 / 179 |
| DEL-02-06 | `INITIALIZED` | `c8ca6292bae1…bec8` | `53d99682795a…2928` | 240 | OUT 2, CLM 20, REQ 14, AC 15, VER 14, AX 15, TBD 5, CON 6 | CON-002, CON-003, CON-005, TBD-004, TBD-005 | 15 | 70 / 170 |
| DEL-02-07 | `INITIALIZED` | `d044499ab5ac…2559` | `a07d5f173055…9079` | 292 | OUT 2, CLM 19, REQ 15, AC 16, VER 15, AX 14, TBD 6, CON 6 | CON-001, REQ-001 | 16 | 58 / 162 |

What each rebuild changes, in brief (the full account is in each contract's rebuild-provenance `AX-*` entry and in the drafter returns):

- **DEL-01-01 Record-tier schema & entity model.** Sixteen types per revision 1.6 `SOW-001` (WorkGraph and WorkNode added; Workplan/Step/Gate a declared historical-grammar entity with gate state re-sourced; Receipt covers ledgers and central `RECEIPT.md`). `REQ-006` keeps its ID with a **changed rule**: RunRecord now admits summaries joined on the declared run-identity token, with `STATUS.json`/`RUNTIME_SUMMARY.json` as declared historical grammar or current evidence per profile and Runtime service user-data never an input (the merged DEL-02-09 contract quotes the old text, anchored to the old hash). New: `REQ-015` (live/historical label, unobtained fields recorded), `REQ-016` (Loop: identity, entrypoint, procedure SHA only), `REQ-017` (out-of-guard values typed as their own kinds, never coerced); `CON-003` (store admission of every out-of-guard value the siblings route here), `CON-004` (the "remaining items" optional field), `CON-006` (work-graph DependencyEdge, with `DEL-02-08/CON-005`), `CON-007` (gate state from "scope-change pointers", which no feed covers), `CON-008` (DriftFinding and a harness-configuration divergence).
- **DEL-01-06 Loop registry.** States the ruled and applied `D-PEC-96` registry: schema version 2 only (version 1 rejected with a located error), rows `loop_id`, `loop_init_path`, `feed_profiles`; the closed three-profile vocabulary with disjoint surfaces and at least one live profile; `RegisteredLoop.feed_profiles`; PEC's row `shared-dev-loop` v1 live, `loop-receipts-ledger` v1 historical, `agentruns-json` v1 historical. The "declares `remaining-loop` now" sentences (SOW-094 Notes, the Description, `SOFTWARE_DECOMP.md` §9) are quoted and labelled stale design text (`CON-003`; COV-083, owner Q-CP3-1 (a)). RF-002 stays RESOLVED.
- **DEL-02-03 Receipts ledger parser.** Two grammar generations of one Receipt feed kind (per-loop `LOOP_RECEIPTS.md`, central `RECEIPT.md`); discovery by declared surface; the live/historical label from the declaration only; the SCA-005 §B7 fixture classes FC-1..3 golden-by-reference for X1. `CON-004`: the register says "live for PEC", PEC's row says `loop-receipts-ledger` historical and PEC's ledger is closed at Receipt 197.
- **DEL-02-04 Run-evidence JSON parser.** The daemon referent is replaced (D-GOV-43); discovery only from `agentruns-json`/`json-run-evidence`; the old `CON-003` retired as false. New finding, `CON-005`: under D-GOV-45 most run evidence moved to archive tag `archive/agent-runs-2026-09-25` (commit `8007c5927`); whether archived records are in the feed is open, and `REQ-001` reads nothing from an archive tag meanwhile.
- **DEL-02-05 Dependency register parser.** `Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar; `WORK_GRAPH.md` is DEL-02-08's (`CON-005` cross-references `DEL-02-08/CON-005` and `DEL-01-01/CON-006`); `RETIRED` rows carried, never dropped.
- **DEL-02-06 Workplan/LOOP_INIT parser.** `LOOP_INIT.md` identity, entrypoint and procedure SHA only, at the row's `loop_init_path`; workplans historical; the old `CON-005` retired as false (PEC has a `LOOP_INIT.md`). `CON-004`: no ruled profile declares a workplan surface, so the historical workplan grammar has no discovery basis today. The historical workplan grammar labels everything it extracts historical and emits no current gate state; whether a workplan's gate-shaped tokens are emitted at all, and into which DEL-01-01 type, is left open as new `CON-009`.
- **DEL-02-07 `adapter.yaml` consumer.** Re-purposed to the parity-peer reader (SCA-005 Q2 (b)): the harness `status_glob` compared with PEC's declared census population, divergence reported as a DriftFinding; the feed-manifest `REQ-001` retired. Carries the four Part B items (below). `CON-002` (loop-to-project relation) stays unresolved; `CON-003` (source of "PEC's declared census population") resolves at a DEL-02-01 revision or by scope change.

### Parser carry-forward (graph S2 row; SCA-005 §B4)

The `DEL-01-03` produced guard (`v2/src/pec_v2/core/content_minimal_guard.py`, `740a4a74…19ee9`, produced, not accepted) admits only `OPEN`..`ISSUED` as STATE values. Every S2 contract that emits a value outside the guard's classes records it as a `DEL-01-03/CON-001` case; DEL-01-01 `REQ-017` types those values and `CON-003` gathers them (`RETIRED` values, node states, run tokens, loop and project identifiers, profile identifiers, receipt tokens, dependency-register tokens, abbreviated SHAs, globs and others). No CON is resolved by assumption.

### `D-PEC-99` Part B landing (DEL-02-07)

Each item's "Carry-forward input for S2" paragraph and its Gate line are carried **verbatim** in blockquotes with the carve-out sentence, in DEL-02-07 `CLM-016`, and the quote verifier checks each against the exhibit (both sides). The contract states in its own voice (CLM-016 intro and `AX-011`) that the gates still bind at this destination: production of any source, test or fixture stays gated on a separate exact owner-ruled DEL-02-07 production packet (F-PEC-1), WORKING_ITEMS activation and a current reliance preflight, and REM-002 additionally on an accepted `CON-002` derivation or an owner-ruled scope change.

| Item | Lines in the DEL-02-07 postimage (carry-forward / Gate / mapping) | Local IDs that implement it |
|---|---|---|
| DEL-02-07-REM-001 | L139–145 (L141 / L143 / L145) | OUT-001, REQ-002, REQ-007, REQ-009, REQ-011, AC-001, AC-005, AC-009, AC-011, VER-001, VER-005, VER-008, VER-010, TBD-002, TBD-004 (the feed-manifest derivation is not carried; `REQ-001` retired) |
| DEL-02-07-REM-002 | L147–153 (L149 / L151, with the `CON-002` gate / L153) | CON-002, TBD-003, REQ-003, REQ-013, AC-002, AC-013, VER-002, VER-012, CLM-006, CLM-007 |
| DEL-02-07-REM-003 | L155–161 (L157 / L159 / L161) | REQ-004..007, AC-003..006, VER-003..006 |
| DEL-02-07-REM-004 | L163–169 (L165 / L167 / L169) | OUT-002, REQ-008, REQ-016, AC-007, AC-016, VER-007, VER-015 (registration in `software-workflow.json` gated; nothing registered) |

The heading is at L133, the shared introduction and the gates statement at L135–137, and `AX-011` at L268.

### Cross-candidate coherence and external anchors

- **Siblings cite postimages.** Every qualified citation of one S2 deliverable's ID in another S2 candidate resolves to an ID defined in that sibling's candidate: `check_sibling_ids.py` ``RESULT PASS 92/92``. No candidate contains a sibling's postimage hash.
- **Dependency quotes.** The seven ACTIVE `Dependencies.csv` rows whose `EvidenceFile` is an S2 contract keep their `EvidenceQuote` as a raw substring of the postimage (DEP-02-01..06-003 in DEL-01-01 `CLM-012`; DEP-02-07-003 in DEL-01-06 `CLM-006`), checked the way `gen_d95.py` checks it. No register is written.
- **Qualified citations from outside S2** (`DEL-01-01/REQ-006` from DEL-02-09; `/REQ-008`, `/AC-007`, `/CLM-006` from S2 siblings): all four IDs are kept. `REQ-006`'s rule changed, as stated above.

### Consequences outside this packet (disclosed; nothing here writes them)

- **Verbatim quotations of the prior S2 contracts in other contracts go stale.** `scan_external_quotes.py` (heuristic; `evidence/scan_external_quotes.out`) lists spans of prior S2 text, not found in any accepted upstream source, that no longer occur in the postimage. Confirmed by the drafters: DEL-02-01 (`REQ-002`, still naming DEL-02-07 as the feed-manifest supplier), DEL-02-02, DEL-03-01 (quotes of DEL-01-06 `REQ-005` "version-1", DEL-02-03, DEL-02-05 and DEL-02-06 `OUT-001`), DEL-03-03, DEL-04-01, DEL-04-05 (`CLM-011` quoting DEL-02-03 `REQ-001`), DEL-08-04, DEL-10-10 (DEL-02-05 `OUT-001`, `REQ-001`, `REQ-006`, `CON-004`); DEL-02-08 and DEL-02-09 quote the old DEL-01-01 text anchored to its old hash. All are `INITIALIZED`; they belong to S1, S4 or a later DEL-02-08/09 revision. **Recommended ordering:** rule S2 before the S1 and S4 packets are finalized, so those packets absorb these at their own basis.
- **Register wording left for a later PEC scope change** (each carried as a CON, not resolved): SOW-013 and the DEL-02-03 Description ("live for PEC"); SOW-014 ("current-by-own-practice for PEC/Root" against PEC's historical `agentruns-json`); SOW-016's workplan grammar with no declared surface; SOW-094 Notes, the DEL-01-06 Description and §9 (`remaining-loop`, COV-083); `SOFTWARE_DECOMP.md` §10 OI-012 still "undecided" after `D-PEC-72` O-B; DEP-02-06-003 and DEP-02-07-003 `Statement` cells predating SCA-005; no dependency edge from DEL-02-03/04/06 to DEL-01-06.
- **Other records:** the seven `_CONTEXT.md`/`_REFERENCES.md` still name revision 1.5 and PRD v2.3 (node K4); `D-PEC-96`'s `VALIDATION.md` maps its tests to the prior DEL-01-06 `VER-001..006`, several of which are now `VER-007..014`; the merged DEL-02-08/09 contracts say `OPEN`, true at their observation commit `53145aaeb` and superseded by `D-PEC-98` add-on S; the `D-PEC-99` exhibit's currency notes cite prior-contract line numbers (the exhibit is not edited, by rule).
- **Findings for the owner's attention:** the D-GOV-45 archive bears on DEL-02-04 and DEL-02-05 (`CON-005`, `CON-004`); DEL-02-06's workplan grammar has no discovery basis under the ruled vocabulary (`CON-004`, and the envelope evidence toward S in `CON-007`); DEL-01-01 `CON-007` (gate state from scope-change pointers that no feed covers); DEL-01-01 `CON-008` / DEL-02-07 `CON-006` (whether a harness-configuration divergence is a DriftFinding or a parity finding).

## Options

- **A — replace the seven contracts with the tabled bytes in one act, no lifecycle change (recommended).** **7 product paths, all modified**; nothing created or removed; no `_STATUS.md`, register, context, reference, dependency or `MEMORY.md` file touched. Add-on M (question 3) is independent.
- **A + M** — as A, plus the add-on M `MEMORY.md` rows at the undertaking's closeout (6 created files, 1 modified).
- **Amend** — for example: drop a deliverable (the candidates cite one another's postimages, so dropping DEL-01-01 or DEL-01-06 requires re-drafting its siblings, and dropping a parser requires re-checking DEL-01-01 `CLM-018`); change a requirement; resolve a CON now.
- **Defer** — nothing opens; X1 and P1 parser implementation wait on S2.

A per-deliverable split with the current bytes is not offered: the candidates are reconciled to land together (sibling citations resolve against postimages), so split acts would need re-drafted bytes. A split that writes contracts without their open items is not offered either: the method requires substantive ambiguity to be marked `CONFLICT`.

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once**, under `chirality-root:bundled:workflow:scope-of-work` with `STATUS_POLICY=NO_STATUS_TOUCH`, as the exact-bytes replacement described under Method. Paths are relative to `projects/pec/execution/`.

| Deliverable | Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|
| DEL-01-01 | `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md` | `43f1f57a13bb96b3235bbbb460342bd03518c503f23cb8b0560914f27a2f0170` | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| DEL-01-06 | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` | `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8` | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| DEL-02-03 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md` | `c3e7928cbbcf1c552883f8268bff4899996f9943cc8fb1b52ca14c223bd7d872` | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| DEL-02-04 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md` | `bdb4eea0143ef6c777b0ed5914e7a8846d818437f77ec96cea03d8557f3bcb87` | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| DEL-02-05 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md` | `192df47d8d3d15316951066a24032b9a7d7a6cd0b660935fcb1799daf8af907e` | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| DEL-02-06 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/ScopeOfWork.md` | `c8ca6292bae19d2da754918bdf530d32a4c0a8348146ed10743acfd0acfbbec8` | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| DEL-02-07 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` | `d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559` | `a07d5f17305598731e98d853f71361d0f8a1def3597d5b25c48eb25f03ff9079` |

The postimages are the exact candidate files, copied byte for byte into the run root as `candidates/…`. They have no date slot.

Read-only files the act re-verifies and never writes (SHA-256 at `dfb089b8a`; the first five equal at the pin `189f205ff` and at `aca930622`):

- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`
- `projects/pec/execution/_Decomposition/Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`
- `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`
- `projects/pec/docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`
- `projects/pec/v2/config/loops.json` `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7`
- `projects/pec/v2/config/loops.schema.json` `104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_STATUS.md` `26ec3a6e3d4b557cff30ff5a18014c5c9f2eef4da23bf0c25f19cf87b01af83d`
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_STATUS.md` `20e6db0216943cf93d734cf97a18c50ece47706e6a012e47580aea9745e5e90d`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_STATUS.md` `6f94c04f79b678082b0407f93ec9c898d988c2693c0d1e19791f5cff985cf06f`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_STATUS.md` `2ac8fd42d7c72f85fbf65daea10b6935c4a84dd1629756a55988476fc05d86a9`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_STATUS.md` `5feb5e170d196146a3a83fff4e1558468e85ea83ee7b35faba6e106ac6f589bb`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_STATUS.md` `a20147a10b21b709e6f31e0178b53921d58109447f8d607f3afe2e35b27ed055`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_STATUS.md` `653daef4a2eb08b74866d405534b41e0031c7c3590ac8f39be5f7a42c584060a`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/Dependencies.csv` `e736ce9a34f31b88c19c007371a87ddafbfc32544beeb0fc1a08dae8aca61a6d`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/Dependencies.csv` `51c7b725b91d7659496964f08b2d2d4934bd158c3fadc65be42dbf110436dfa1`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/Dependencies.csv` `c456c77f0203c24a1a4aae04fd286610a4391666cbd285548854079f731c1643`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/Dependencies.csv` `563b4c281ded7a410cf7587b71fc562f321b254e317ced29f42a6d306dd3e701`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/Dependencies.csv` `90f555eb870ed47e693456e6768060307bb93c2f48bfadf9344a22b6111618b1`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/Dependencies.csv` `8a88f50b462c9dc0614c6cac08f00fc3e6fa977e994b3ab1e56c3478a4cbc335`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/Dependencies.csv` `00b5a872ca0a62c9246591d513af11637e3e15dc764824fd28b7d8219f3c3ee3`

### Add-on M — MEMORY rows (only if question 3 selects it)

At the undertaking's closeout (graph node M1), WORKING_ITEMS writes, under `PKG-…/1_Working/<DEL folder>/`:

| Deliverable | Path | Preimage | Act |
|---|---|---|---|
| DEL-01-01 | `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/MEMORY.md` | absent | created from the template |
| DEL-01-06 | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/MEMORY.md` | `035ecb8686d72b18eb680531e1239ab4b2df4f5ae1b70811f6e4d667ccf30a3f` | modified: one row appended |
| DEL-02-03 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/MEMORY.md` | absent | created from the template |
| DEL-02-04 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/MEMORY.md` | absent | created from the template |
| DEL-02-05 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/MEMORY.md` | absent | created from the template |
| DEL-02-06 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/MEMORY.md` | absent | created from the template |
| DEL-02-07 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/MEMORY.md` | absent | created from the template |

Each new file is `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` row. DEL-01-06's existing `MEMORY.md` gains one row after any row the `D-PEC-96` add-on ("create MEMORY") writes at the same closeout. The row, in every file:

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | Scope of Work rebuilt under D-PEC-100 (graph node S2). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-100 ruling record> |
```

The slots `{D}`, `{PR}` and the two link targets are fixed at closeout; the verifier checks that no other byte departs from the template (new files) or from the preimage plus the named rows (DEL-01-06).

## Generation method (binding)

The seven postimages come from one run of `apply_s2p.py`, **SHA-256 `69ff97c002fd99326fb41f92cfb9b5a1450e9ee86cfb3ed005917d87970d16fe`**. It is stdlib-only Python, prepared with CPython 3.13.7, and is copied byte for byte into the run root with the seven candidate files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_REBUILD_S2_{D}/apply_s2p.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_REBUILD_S2_{D}/candidates [--check-only]
```

**Failure semantics.**

- **Preflight.** Every candidate hashes to its postimage; every target exists and holds its preimage; no temporary sibling exists; every pinned file hashes as tabled. Any failure exits 1 before any byte is written.
- **Write.** Each postimage is written to a temporary sibling (`…ScopeOfWork.md.s2ptmp`), hash-checked and renamed over its target. If any step after the first write fails (I/O error, hash mismatch, post-write inventory mismatch, changed pinned file), the script restores every replaced target from the preimage bytes it read at preflight, removes every temporary file, and exits 1. On exit 1 every target holds its preimage and no temporary file remains; exit 2 would report an incomplete rollback (never observed in testing).
- **Write set.** The script inventories every file under `projects/pec` (path and SHA-256) before and after the write, and requires the difference to be exactly the seven targets, each modified from preimage to postimage, with nothing created or removed.
- **Second run.** It fails preflight: the targets no longer hold their preimages. The script never touches `_STATUS.md` or `MEMORY.md`.

The check aids, which are not bound:

| Aid | SHA-256 | Role |
|---|---|---|
| `test_apply_s2p.py` | `9a680ba9df30df78d1a349c2579892236367bebba4ba3509aee3309395403908` | fault injection, seven cases |
| `verify_s2p_quotes.py` | `be74a06c74457256e12f0573837f8d35e41ee276d76b2e0dc660c376598854af` | two-sided quote check, raw dependency quotes, forbidden phrase, observation commit |
| `verify_s2p_state_claims.py` | `eb85c15f24ed79b9234a2ab3dd746bbaaa499ea7566bd99efa2e061d87dd8545` | commit-anchored state claims, each also matched in the candidate |
| `check_sibling_ids.py` | `e8c0f2bddbc443cd3a5e7f0c2c96c270e626c1d8e4612a061e0cf37f8e099a91` | qualified sibling citations resolve against postimages |
| `scan_external_quotes.py` | `e11fa9ada53490a23e66da4374d8a38b29a90f8ee0904d77ea5355c9584e94b8` | informational consequence scan |
| `run_s2p_checks.sh` | `52463303341920784eff5f9129650faf69da86e8cf4a9dcdf03934eed6465531` | runs checks 2–10 on pre/post exports |

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`, on the act branch. Record each command, exit code and output in the run root. `run_s2p_checks.sh` runs rows 2–10 on two `git archive` exports of one commit (pre and post), and is the rerun method.

| Check | Command | Required result |
|---|---|---|
| 1. Preconditions | ruling and register row on fetched `origin/main`; `apply_s2p.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `CHECK write set = grant (0 creates, 7 modifies, 0 removes)`; `ALLOW` everywhere; on any pin mismatch, stop and route to the owner (no re-pin is pre-authorized) |
| 2. Contract validity | `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` ×7 | `PASS format=SOW_V1` ×7 |
| 3. Checklist | `python3 tools/scope_of_work/derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, each twice | exit 0; reruns byte-identical; each equal to the prepared checklist (hashes under Preparation evidence) |
| 4. Boundary owners (QA 21) | `python3 tools/scope_of_work/check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×7 | exit 0; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; every `NOT_CHECKABLE` clause resolved by hand as tabled below |
| 5. Quote fidelity | `python3 <run root>/verify_s2p_quotes.py --tree . --gitdir . --prep <run root> --observation aca930622` | `RESULT PASS 460/460` (both sides; includes the seven raw dependency quotes, the forbidden-phrase and observation-commit checks) |
| 6. State claims | `python3 <run root>/verify_s2p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 1274/1274` (reads the named commits; independent of the working tree) |
| 7. Sibling IDs | `python3 <run root>/check_sibling_ids.py <run root>` | `RESULT PASS 92/92` |
| 8. Lifecycle preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty |
| 9. Strict registers (D-GOV-48) | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution`, before and after | exit code and output **identical** to the pre-act run (at `dfb089b8a`: exit 1, 0 errors, 26 pre-existing `XRG-013` warnings; owner-deferred). A new finding or a changed count fails |
| 10. Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | exit 0 each; output identical before and after |
| 11. Containment | `git diff --name-status origin/main...HEAD` | the seven modified contracts; M's files if selected; the run root and HELP_HUMAN's records under `execution/_Coordination/**`; nothing else |
| 12. Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. The act changes no decomposition truth, register or topology.

QA 21 hand resolution (per-act clauses the tool reports as `NOT_CHECKABLE`, or that cite owners through a claim):

| Contract | Requirement → owner | Cited claim |
|---|---|---|
| DEL-01-01 | REQ-003 → `DEL-04-03`; REQ-004 → `DEL-03-02`, `DEL-03-03`; REQ-005 → `DEL-03-01`; REQ-007 → `DEL-01-03`; REQ-015 → `DEL-04-05`; REQ-016 → `DEL-01-06` | CLM-012 |
| DEL-01-06 | none reported; REQ-014 checked by the tool (14 owners, all in CLM-013) | CLM-013 |
| DEL-02-03 | none reported; REQ-018 checked by the tool; per-act clauses in REQ-004, REQ-006, REQ-007, REQ-009, REQ-012 → `DEL-04-05`, `DEL-04-03`, `DEL-01-03`, `DEL-03-01`, `DEL-01-05` | CLM-015 |
| DEL-02-04 | none reported; REQ-011 checked by the tool, and the other exclusions route through it | CLM-011 |
| DEL-02-05 | none reported; REQ-011 checked by the tool | CLM-012 |
| DEL-02-06 | REQ-004 → `DEL-04-01`; REQ-006 → `DEL-04-03`; REQ-009 → `DEL-01-03`; REQ-010 → `DEL-03-01` | CLM-011 (and CLM-012 for REQ-004) |
| DEL-02-07 | REQ-004 → `DEL-04-05`; REQ-006 → `DEL-01-03` | CLM-014 |

In each case the cited claim names that owner (drafter returns; the verifier re-checks).

### Independent verifier

The method's independent verification is a separate `MODE=VERIFY` run, read-only on production content, by a TASK that authored nothing. The preparation verdicts are in the prep folder (`VERIFIER_VERDICT_NN.md`); a fresh one runs again at the act. It returns a verdict file; defects return to the author, and the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`; the run-root script hashes as bound; the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **`MODE=VERIFY`.** The mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21), including the QA 21 hand resolution.
4. **Semantics.** Every claim is true at the commit it names or at `aca930622`; every quotation is verbatim; no requirement adds scope beyond the deliverable's ledger rows, its `Deliverables.csv` row and PRD v2.4; every open item is `TBD`/`CON`; kept IDs keep their meaning and retired IDs are not reused; the Part B texts and gates are verbatim and the gates are stated as still binding; no Remaining section is read or presented as a surface.
5. **Containment and lifecycle.** As in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act, the checks and, if selected, add-on M at closeout. It runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/SOW_REBUILD_S2_{D}/`, in the default-writable fence: `apply_s2p.py` (exact bytes), `candidates/`, `quotes/`, `claims/`, the check aids and all outputs; `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`; `VERIFIER_VERDICT_NN.md`. No `_run_records/` entry is written in any deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under `D-PEC-88`. `_Evaluation/**`, registers and dependency files stay closed.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning, unless the owner states otherwise. Role identity is instruction-asserted.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the script leaves every target at its preimage and no temporary file. If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR restores the seven preimages tabled above, and removes M's six created files and DEL-01-06's added row if M ran. No lifecycle state changed, so nothing else is walked back. The ruling record and register row are never reverted; a rollback is its own register row and record. The run root stays as non-current evidence with a rollback note. No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + M or an amendment, grants none of the following:

- any `v2/**`, `software-workflow.json` or `docs/PRD.md` write, or any source, fixture or test file; the DEL-02-07 Part B production obligations stay gated as their contract states;
- any `_Decomposition/**` or `_ScopeChange/**` write, or any register write: no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `Dependencies.csv` or `_DEPENDENCIES.md` change, no dependency edge, and no action on the D-GOV-48 warnings;
- any `_CONTEXT.md`, `_REFERENCES.md` or `_SEMANTIC.md` write, or any file of a deliverable outside the seven (the disclosed consequences in other contracts are for their own packets);
- any lifecycle change or `_STATUS.md` write. No `## Remaining` entry is written or read;
- `CHECKING`, `ISSUED`, artifact acceptance, a REVIEW gate act, or any readiness or reliance claim;
- a registry, profile or D-PEC-96 act, or a resolution of any `CON` item;
- a Task Management disposition, an audit run, a pointer move, or an edit of the `D-PEC-99` exhibit;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- adoption of `scope-of-work` `MODE=REVISE` or any other new Root mode;
- a schedule reading: blocker output stays advisory.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**, the seven exact replacements in one act, authored under `INIT` discipline and verified by `MODE=VERIFY`, as described under Method.
2. **Part B reading.** Confirm that the ruling on this packet places DEL-02-07-REM-001..004 into the DEL-02-07 contract verbatim with their gates **still binding** (production stays gated on a separate exact owner-ruled DEL-02-07 production packet, WORKING_ITEMS activation and a current reliance preflight; REM-002 additionally on an accepted `CON-002` derivation or an owner-ruled scope change), and discharges only the exhibit's carry of that text. Recommendation: **confirm**. Without an answer, the text is applied and every gate stays binding.
3. **Add-on M — MEMORY rows.** Create the six `MEMORY.md` files (DEL-01-01, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07) and add one row to DEL-01-06's existing `MEMORY.md`, at closeout, as tabled (recommended); or record the run only in the graph and central receipt. `projects/pec/AGENTS.md` allows either on your decision.
4. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran on `git archive` exports in the session scratchpad, never on a checkout. Interpreter: Python 3.13.7 (CPython); local date 2026-09-26. The final run (`evidence/RUN_S2P_CHECKS.out`, from `run_s2p_checks.sh` at `dfb089b8a`):

```text
basis commit: dfb089b8abae48ee699117c5bc167301963b2ab5
python: Python 3.13.7
PASS act: check-only 0, apply 0, rerun refuses 1
PASS containment: 7 differing files, all ScopeOfWork.md
PASS validate DEL-01-01
PASS checklist DEL-01-01 (rerun byte-identical)
PASS boundary DEL-01-01 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-01-06
PASS checklist DEL-01-06 (rerun byte-identical)
PASS boundary DEL-01-06 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-02-03
PASS checklist DEL-02-03 (rerun byte-identical)
PASS boundary DEL-02-03 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-02-04
PASS checklist DEL-02-04 (rerun byte-identical)
PASS boundary DEL-02-04 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-02-05
PASS checklist DEL-02-05 (rerun byte-identical)
PASS boundary DEL-02-05 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-02-06
PASS checklist DEL-02-06 (rerun byte-identical)
PASS boundary DEL-02-06 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-02-07
PASS checklist DEL-02-07 (rerun byte-identical)
PASS boundary DEL-02-07 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS quotes: RESULT PASS 460/460
PASS state claims: RESULT PASS 1274/1274
PASS sibling IDs: RESULT PASS 92/92
INFO consequence scan (informational): SUMMARY stale=31 kept=32
PASS strict identical before/after, export root normalized (exit=1)
PASS harness identical before/after, export root normalized (exit=0)
PASS receipts identical before/after, export root normalized (exit=0)
PASS whitespace
PASS fault injection: RESULT PASS 7/7
OVERALL PASS
```

Negative controls (`evidence/negative_controls.out`, scratch copies): a dropped Gate phrase in DEL-02-07 fails the candidate side of two exhibit quotes; an altered exhibit fails the source side; a one-character change to DEL-01-01 `CLM-012` fails all six raw dependency quotes; a wrong hash fails its state claim; a removed matrix row fails validation and the checklist refuses with no artifact (QA 18).

Checklists (`evidence/run_main/checklist_<DEL>.json`): DEL-01-01 `b78dbeef1f70bb22822e910a7259ccdf39d76aa1c2af374a784f1bcde28ac827`; DEL-01-06 `964b543533ea3166b61a80424b04adc91c03914c61d88eb0f8b964e50bcff2aa`; DEL-02-03 `04392472eefaf4afb72110b33b1412029bac3c5b541c4cfd5be13da2cc8d55f0`; DEL-02-04 `2c2324f0a58065965351f38005737778a5511a15a93f238596d3e3f73ec34854`; DEL-02-05 `b035ea4a324f6ec373c147fb4ddbd49be268410e114bfac42052fc2c11e74534`; DEL-02-06 `d989b1f33e95a47515fc52d5934e507c9d131f3a0e723707c98798c1f7228982`; DEL-02-07 `97430073516f005222288554478ea35fd2343fc736783c3ff4e5cbf7e18f0e03`.

Preparation artifacts (all in this prep folder; hashes in `SHA256SUMS`):

- `candidates/projects/pec/execution/…/ScopeOfWork.md` ×7 (postimages as tabled);
- `quotes/DEL-*.json` ×7 and `claims/DEL-*.json` ×7 (the verifier inputs);
- `apply_s2p.py` (bound), `test_apply_s2p.py`, `verify_s2p_quotes.py`, `verify_s2p_state_claims.py`, `check_sibling_ids.py`, `scan_external_quotes.py`, `run_s2p_checks.sh`;
- `evidence/` (every check output, the reliance preflight and the checklists);
- `VERIFIER_VERDICT_NN.md` (the preparation verdicts).

Basis at `dfb089b8a`:

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `9ae4bea2…9665` / `1a13a5b0…8fb7` / `df9196d1…5eb8` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` |
| `docs/PRD.md` (v2.4) | `ae49b806…3fbe` |
| SCA-005 `Propagation_Plan.md` / SCA-005 `Amendment_Actions_CP2.csv` / SCA-006 `Impact_Assessment.md` | `50cd0b1d…1350` / `7bb3bada…9987` / `93253b7d…b691` |
| `D-PEC-96` ruling / `D-PEC-99` exhibit / `D-PEC-98` ruling / `_REGISTER.md` | `852057f0…399e` / `69b646f8…f45e` / `039dc7e2…8361` / `e845e1bb…48e2` |
| `v2/config/loops.json` / `loops.schema.json` / produced guard | `fd342b4f…53d7` / `104ed648…b143` / `740a4a74…19ee9` |
| `validate_decomposition_registers.py` / `write_status.sh` / `MEMORY_TEMPLATE.md` | `869df1d5…57ee` / `1857ad59…97bc` / `5a9564f4…6a5a` |
| Notices: project-setup incremental / D-GOV-48 package home | `8829ac84…64af` / `15ea36ee…e8e6` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, node S2 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with seven TASK drafters and one read-only reviewer as described under Method. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The roles and the `high` reasoning effort are instruction-asserted.
