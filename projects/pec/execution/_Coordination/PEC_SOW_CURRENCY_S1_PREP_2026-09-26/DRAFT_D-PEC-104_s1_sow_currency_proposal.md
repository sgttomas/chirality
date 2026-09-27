# D-PEC-104 — Scope of Work currency for the S1 review and housekeeping class (DEL-01-03, DEL-01-04, DEL-01-05, DEL-02-01, DEL-02-02, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-06, DEL-04-05, DEL-10-02, DEL-10-10) — proposal

Status: **DRAFT PROPOSAL / AWAITING_RULING**. **The number D-PEC-104 is provisional**: the brief assigned it, the register (`_REGISTER.md` `33b43ae8…5a2f` at `origin/main` `3488a236a`) has no D-PEC-102..104 row, and it becomes final only when HELP_HUMAN publishes this packet in `_DECISIONS/` with its register row. Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S1) for the PEC loop, 2026-09-26 (session date), from brief `briefs/S1P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `9718ab7307b8575b286369b99ae015f4c42d6edff0f3be546e83518786b79f17`) and HELP_HUMAN's two relayed directions (quoted under Provenance). No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every check ran on `git archive` exports. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-104_s1_sow_currency_proposal_2026-09-26.md`.

The act it asks for is bounded: **replace twelve existing `ScopeOfWork.md` files with the exact bytes tabled below**, in one run of a bound act script, with no lifecycle change. Add-on M (question 4) is separate.

## Provenance

- **Owner acts relied on.**
  - The owner's 2026-09-25 steering, recorded in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…5a6b`): "You can continue with all the open work you identified." The work graph turns it into node S1, "SOW currency: review class outside the S4 set" (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`; the S1 row is byte-identical at `125cfacc1` and at `3488a236a`).
  - SCA-005 checkpoint 2 (`D-PEC-92`) accepted `Propagation_Plan.md` (`50cd0b1d…1350`). Its §B4 table classes each existing contract and names the housekeeping fixes that ride the same pass: the unresolvable `@3623b958b` basis pin and the false "`_REFERENCES.md` still names revision 1.1" claim.
  - SCA-006 checkpoint 3 (accepted 2026-09-26; `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`) made decomposition revision 1.6 `current_basis` with PRD v2.4. Its Impact Assessment §7.1 (`93253b7d…b691`) classes all twelve deliverables here `NOT_AFFECTED`; its `Propagation_Plan.md` §B4 (`f95d00d1…d7d8`) fixes the S4 set and leaves the other 23 contracts with their SCA-005 classes (graph S1/S2).
  - `D-PEC-99` (ruled A, 2026-09-26; `D-PEC-99_RULING_2026-09-26.md`, `3e34403a…c989`): the `## Remaining` sections are retired; exhibit Part B (`D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`, `69b646f8…f45e`) carries DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004 and DEL-04-05-REM-003 to node S1. Its question 1 (a) carries DEL-03-06-REM-004 "for this correction only".
  - `D-PEC-100` (ruled, 2026-09-26; `D-PEC-100_RULING_2026-09-26.md`, `13690e20…729b`; act PR #979, merge `125cfacc1`): the seven S2 contracts were replaced. Its proposal (`39c4331e…5b25`) names the contracts that quote the replaced S2 text and recommends that S2 land before S1 and S4 are finalized.
  - `D-PEC-101` (ruled; act PR #976, merge `ce934ac33`): contexts and references re-pinned to revision 1.6 / PRD v2.4; DEL-08-06 and DEL-10-13 set up with 22 dependency rows. `D-PEC-96` (ruled A; act PR #950, `73ed349ed`): registry schema version 2 and the closed three-profile vocabulary.
  - Precedents: `D-PEC-100` (exact-bytes replacement of existing contracts, bound script, fresh verifiers) and `D-PEC-98` (two new contracts; add-on S for a status act).
- **HELP_HUMAN directions relayed during preparation (recorded here as evidence, not as rulings).**
  - Confirmed: of the five housekeeping-only contracts, DEL-08-02 is excluded (lifecycle `CHECKING`) and DEL-10-03 is in S4, so three are here; and DEL-03-06 takes the REM-004 correction only, with its other stale text disclosed as out of scope.
  - DEL-01-03 and DEL-01-05 are `IN_PROGRESS` with produced artifacts verified against their current contracts (the `D-PEC-85/87/89/91` store/guard slices; the `D-PEC-84` scanner repairs): their revisions are currency only; no requirement, acceptance criterion or verification method that produced artifacts or their recorded evidence were checked against may change; every ID other contracts cite is kept (`DEL-01-03/CON-001`, and `DEL-01-03/REQ-003` verbatim); the packet states per deliverable that the verification basis is unchanged and lists anything that would change it as an open item.
  - Nothing prompts the owner about CHECKING.
- **Fence.** `projects/pec/AGENTS.md` (`df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`) §"Write Scopes And Fences": every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the STATUS pointer needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. No earlier ruling opens the twelve targets.
- **Source state.**
  - **Observation commit `125cfacc1`** (`125cfacc10f664685cb91802a9166b1041f42a25`, PR #979 merge, which applied `D-PEC-100`). Each rewritten candidate says that every unanchored state claim is an observation there (the correction-only DEL-03-06 keeps its own dated basis). **Frontmatter pin `189f205ff02df4111b33c20be441ce06e65ada7a`** (SCA-006 checkpoint-3 acceptance, PR #954), an ancestor of `125cfacc1`. The decomposition, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv` and `docs/PRD.md` are byte-identical at the pin, at `125cfacc1` and at `3488a236a`.
  - Checked again at `origin/main` **`3488a236a`** after `git fetch` (the branch merges it). PRs landed since `125cfacc1`: #981 (`947075c9a`: the undertaking's work graph and three review transcriptions), #982 (`ce99bc256`: the retirement undertaking's closeout — its graph, a central `RECEIPT.md`, `docs/STATUS.md`, review transcriptions) and #973 (Piping files). None changes a target, a pinned file, or a file any candidate quotes at `125cfacc1`; every candidate claim and tree quotation is anchored to a named commit.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…1cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`) was run from `projects/pec` on a `125cfacc1` export with `--operation exact-correction-preparation` on all 36 possible targets (twelve `ScopeOfWork.md`, twelve `_STATUS.md`, twelve `MEMORY.md`): `ALLOW`, exit 0, ×36 (`evidence/reliance_hold_preflight.out`).

## Method

- **Workflow.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`2bfa2c5f…dafb3`; precedence project → user → bundled; no project or user workflow of that name exists). Files: `WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`, `resources/checks.md` `44ab41ac…f188`, `resources/tools.md` `fbd07771…6cc7`. Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`.
- **How the candidates are made (as in `D-PEC-100`).** Each candidate was **authored under `MODE=INIT` discipline** (source-grounded in the accepted revision-1.6 basis, `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, no evidence candidate, map, parity or finalizer) starting from the prior contract's bytes: a **currency revision**, not a rebuild, keeping every unaffected byte, every ID and every ID's meaning. The act is **an owner-ruled exact-bytes replacement** bound by preimage and postimage hashes, and **the method's `MODE=VERIFY` is the independent check** of each postimage. Authority for the bytes is this ruling.
- **Disclosure (one line).** Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` added `scope-of-work` `MODE=REVISE`; the owner has deferred adopting it in PEC, and this packet does not use it.
- **Currency rules the drafters followed** (brief `briefs/S1P_DRAFTER_BRIEF.md`, `d20a35b687d8dc78c1af28e6ddd8b2eb1be77524409ec6bf13b76aa8dfb9c87e`). Common edits (every target except DEL-03-06): C1 the frontmatter pin; C2 the basis paragraph (revision 1.6 with the pin and hashes, the authoring basis kept as dated history) and a Purpose sentence naming the prior hash; C3 an observation-commit paragraph; C4 the false revision-1.1 claim replaced by the ruled `D-PEC-99` DEL-04-05 wording ("The deliverable-local `_REFERENCES.md` and `_CONTEXT.md` carry their own revision pins; this contract asserts nothing about their present text."); C5 every quotation re-verified at its source and re-quoted or kept as dated history with its commit; C6 quotations of replaced S2 text brought current to the S2 postimages; C7 stale state claims corrected as observations; C8 the per-deliverable SCA-005 cause; C9 one new currency-provenance `AX` entry naming the prior contract's full hash, "the S1 Scope of Work currency packet (provisional `D-PEC-104`)", the kinds of change, retired and new IDs.
- **Actors.** Twelve Type 2 TASK drafters (one per deliverable). WORKING_ITEMS relayed HELP_HUMAN's DEL-01-03/DEL-01-05 constraint to those two drafters mid-draft and sibling-text reconciliation notes to four others, integrated, bound the act and ran the checks. Fresh read-only `pec-reviewer` TASKs ran `MODE=VERIFY` and the packet review (`VERIFIER_VERDICT_01.md` onward; brief `briefs/S1P_VERIFIER_BRIEF.md`, `06816f92…a8c2`). Models: Opus 5.5 (`claude-opus-5-5`) at `high` for every actor, per the brief.
- **Tools** (`tools/scope_of_work/`, unchanged at `3488a236a`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py` `61a34722…0389`.

## What preparation found

### Scope and lifecycle

- **The target list** (SCA-005 §B4, SCA-006 IA §7.1 and Propagation_Plan §B4, the current tree):
  - **Review class outside S4 (8):** DEL-01-03 (`STALE_REVIEW_REQUIRED (quotation)`), DEL-01-05 (quotation), DEL-02-01, DEL-02-02 (quotation), DEL-03-01, DEL-03-03 (new content), DEL-04-05, DEL-10-10.
  - **Housekeeping only (3 of 5):** DEL-01-04, DEL-03-02, DEL-10-02. DEL-08-02 is `CHECKING` and excluded; DEL-10-03 is in S4.
  - **Correction only (1):** DEL-03-06 (SCA-005 class `current`), for DEL-03-06-REM-004 only.
  - **Excluded:** DEL-00-01 and DEL-00-03 (`CHECKING`; DEL-00-03 goes through D1); the S4 set (DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04, DEL-04-03, DEL-03-04, DEL-10-03); the S2 set (applied); DEL-02-08/09 (not in §B4; their quotations of the old DEL-01-01 text are anchored to its old hash and belong to a later revision of those contracts); SCA-005 `current` contracts DEL-04-02 (S4), DEL-10-01 (`CHECKING`) and DEL-10-11.
  - Every prior contract hash equals its SCA-005 §B4 prefix (none changed since checkpoint 1).
- **Lifecycle: ten are `INITIALIZED`, DEL-01-03 and DEL-01-05 are `IN_PROGRESS`** at `125cfacc1` (each `_STATUS.md` read). None is `CHECKING` or `ISSUED`.
- **What the method does to `_STATUS.md`: nothing.** `WORKFLOW.md`: "Do not modify `_STATUS.md`, lifecycle state, underscore control files, …"; `resources/checks.md` item 3. Each postimage validates, so the condition behind `INITIALIZED` still holds, and the two `IN_PROGRESS` deliverables stay `IN_PROGRESS`. **No transition is proposed**; the act script refuses to run if any `_STATUS.md` differs from its pinned bytes.
- **Produced artifacts (DEL-01-03, DEL-01-05): verification basis unchanged.** Every `REQ`, `AC` and `VER` line of both candidates is byte-identical to the prior contract (diff; verdict 01), so the produced artifacts and their recorded evidence were checked against exactly the requirements, criteria and methods the postimages carry. `DEL-01-03/REQ-003` is byte-identical and `DEL-01-03/CON-001` keeps its subject. Items that would change the verification basis are carried as open items, not changes: DEL-01-05 `REQ-007` still reads "follows the pending `C-08` confirmation recorded at CON-002" although the `D-PEC-77` G-A confirmations are on file (resolving it would change a requirement the artifacts were checked against); DEL-01-05's new `AX-009` is not added to a verified matrix row; and DEL-01-05 `CON-002`'s kept clause on what is open (a later exact-artifact owner confirmation, per `D-PEC-77`) and its Praxeology phrase "the future enforcement must satisfy" are left as they were (verdict 01, V3-2 and V3-3). DEL-01-03 `CON-001` now also quotes the SCA-005 §B4 parser carry-forward naming the out-of-class values other contracts route to it; verdict 01 found this keeps its meaning and leaves the basis unchanged (no admitted field class is added, so the decisions `AC-009` and `VER-008` check are the same, and the produced guard and its design note already route rejected STATE values to `CON-001`), and DEL-01-03 `AX-007` says so.

### The candidates

| Deliverable | Lifecycle | Prior contract | Postimage | Lines | Defined IDs | Retired IDs | New IDs | Checklist items | Quotes / claims checked |
|---|---|---|---|---|---|---|---|---|---|
| DEL-01-03 | `IN_PROGRESS` | `986ef15532cd…6341` | `65c7f4086f8a…a367` | 141→156 | OUT 3, CLM 10, REQ 10, AC 10, VER 9, AX 7, TBD 2, CON 1 | none | AX-007 | 10 | 40 / 47 |
| DEL-01-04 | `INITIALIZED` | `4dd777f8f30c…7e62` | `16ac1cd956c9…ca41` | 125→139 | OUT 3, CLM 9, REQ 8, AC 7, VER 7, AX 6, TBD 3, CON 1 | none | AX-006 | 7 | 25 / 46 |
| DEL-01-05 | `IN_PROGRESS` | `53ba3be30415…de53` | `a0a73eb5537b…84bf` | 161→180 | OUT 3, CLM 10, REQ 12, AC 11, VER 9, AX 9, TBD 5, CON 2 | none | AX-009 | 11 | 40 / 57 |
| DEL-02-01 | `INITIALIZED` | `5d286ec97f4c…4440` | `82caf28a3757…5872` | 260→311 | OUT 2, CLM 15, REQ 13, AC 13, VER 12, AX 13, TBD 4, CON 6 | none | CLM-014, CLM-015, CON-004..006, AX-013 | 13 | 95 / 89 |
| DEL-02-02 | `INITIALIZED` | `5f20b1c48f4f…db6e` | `84e55e58e663…fa86` | 222→267 | OUT 2, CLM 13, REQ 10, AC 10, VER 9, AX 12, TBD 4, CON 3 | none | CLM-013, CON-003, AX-012 | 10 | 71 / 65 |
| DEL-03-01 | `INITIALIZED` | `564955235aea…92d2` | `5b71d3583b2e…8276` | 486→536 | OUT 2, CLM 22, REQ 16, AC 17, VER 16, AX 14, TBD 4, CON 5 | TBD-005 | AX-014 | 17 | 143 / 147 |
| DEL-03-02 | `INITIALIZED` | `d1335c01c546…85b5` | `d823d55d9e71…a3d0` | 367→386 | OUT 2, CLM 15, REQ 14, AC 15, VER 14, AX 13, TBD 5, CON 4 | none | AX-013 | 15 | 74 / 81 |
| DEL-03-03 | `INITIALIZED` | `5ce8ab72425a…eaa7` | `c2b88cb65c71…9526` | 346→380 | OUT 2, CLM 15, REQ 17, AC 18, VER 17, AX 13, TBD 5, CON 7 | none | CLM-015, TBD-005, REQ-015..017, AC-016..018, VER-015..017, CON-006, CON-007, AX-013 | 18 | 100 / 71 |
| DEL-03-06 | `INITIALIZED` | `90de9c2d93d8…c97e` | `f9c3a0577172…8bd4` | 533→533 | OUT 2, CLM 20, REQ 14, AC 16, VER 13, AX 12, TBD 5, CON 6 | none | none | 16 | 16 / 27 |
| DEL-04-05 | `INITIALIZED` | `933c012cf16b…a579` | `88029fead86c…eafd` | 322→332 | OUT 2, CLM 17, REQ 14, AC 15, VER 14, AX 12, TBD 4, CON 4 | none | AX-012 | 15 | 100 / 74 |
| DEL-10-02 | `INITIALIZED` | `99730e4e85ce…1a82` | `f5590cf55b19…436e` | 407→423 | OUT 2, CLM 14, REQ 14, AC 13, VER 12, AX 13, TBD 5, CON 4 | none | CLM-014, AX-013 | 13 | 85 / 84 |
| DEL-10-10 | `INITIALIZED` | `640f23711f93…bd5e` | `15c10a56c21b…35f4` | 466→506 | OUT 1, CLM 21, REQ 14, AC 16, VER 14, AX 12, TBD 5, CON 6 | none | CLM-021, CON-006, AX-012 | 16 | 95 / 106 |

Quotes / claims are the checks each verifier run counts per deliverable (quote entries plus the forbidden-phrase and observation-commit checks; commit-anchored claims). What each currency revision changes, in brief (each candidate's currency-provenance `AX` entry and diff are the full account):

- **Common to eleven (all but DEL-03-06):** the unresolvable `@3623b958b` pin (eight contracts) or the superseded `11a494e9a`/`65955cceb` pins (DEL-01-05, DEL-10-10; DEL-03-01) replaced by `189f205ff…`; revision 1.6 as the accepted basis, the authoring basis kept as dated history; the observation commit `125cfacc1`; the false revision-1.1 claim (the eight contracts SCA-005 §B4 ticks) and DEL-01-05/DEL-10-10's stale "`_REFERENCES.md`/`_CONTEXT.md` record the current basis" claims replaced by the ruled `D-PEC-99` wording; stale lifecycle claims (`OPEN` where the deliverable is `INITIALIZED` or `IN_PROGRESS`) corrected; PRD quotations re-quoted from v2.4; register cells repaired under `D-PEC-65`, `D-PEC-93`, `D-PEC-95` or `D-PEC-101` brought current with the authoring-time cells kept as dated history.
- **DEL-01-03 Store bootstrap & content-minimal guard** (cause: `CON-001` quoted stale PRD v2.1 "pec/bridge ledgers are prose-structured" text). `CON-001` re-quotes PRD v2.4 §7.1 (Receipt, WorkGraph content-minimal extraction list, Loop `LOOP_INIT.md`-only read) and the SCA-005 §B4 carry-forward; its subject is unchanged and it resolves nothing. `CLM-008` no longer names the retired P4 bridges DEL-07-02/DEL-07-04; `CLM-009` records `IN_PROGRESS` and the produced source without any acceptance claim. REQ/AC/VER byte-identical.
- **DEL-01-04 Self-observability logging** (housekeeping). The PRD §11 heading phrase the prior quoted is v2.1 text; re-quoted from v2.4.
- **DEL-01-05 Zero-dependency & locality enforcement** (cause: PEC-API-001 citation). `CLM-009` re-quotes PEC-API-001 from PRD v2.4 and brings the runtime-ownership referent to `D-GOV-43` A2; `CLM-010` records `IN_PROGRESS`, the `D-PEC-84` reversal and repair and `D-PEC-99` question 4 (acceptance separate); `CON-002` records the owner's `D-PEC-77` G-A acts as history and stays open. REQ/AC/VER byte-identical.
- **DEL-02-01 `_STATUS.md` parser** (cause: remaining items; PEC-RCN-002; guard STATE note). `REQ-002` keeps its first sentence (the declared admission rule, cited by `DEL-02-07/CON-003`) and replaces the stale "feed manifest is `DEL-02-07`'s" sentence with discovery through the `DEL-01-06` registry's `status-lifecycle` declaration (`DEL-01-06/REQ-010`). `REQ-003` "sixteen". `REQ-007` reads no remaining-items section while no profile declares that field. New `CON-004` (which deliverable supplies "PEC's declared census population", recorded jointly with `DEL-02-07/CON-003`, not resolved), `CON-005` (`RETIRED` outside the guard's classes, a `DEL-01-03/CON-001` case), `CON-006` (no `Dependencies.csv` edge to DEL-01-06).
- **DEL-02-02 Decision register & packet parser** (cause: PEC-RCN-002 quotation). PEC-RCN-002 re-quoted in full; DEL-01-01 quotations brought to the postimage (sixteen types); `TBD-004` names the registry, not `adapter.yaml`, as the feed declaration; new `CON-003` (decision states outside the guard's classes, a `DEL-01-03/CON-001` case).
- **DEL-03-01 Full-rebuild reconciler** (cause: ingest boundary follows the feed list; `[E-P25]` replaced). Eight upstream feed units (DEL-02-01..06, DEL-02-08, DEL-02-09), discovered through the declared feed profiles; `DEP-03-01-014` shown `RETIRED`, `DEP-03-01-007` refreshed, `DEP-03-01-015/016` added; S2 quotations current (DEL-01-06 schema version 2; DEL-01-01 sixteen types). `TBD-005` (loop-to-project resolution of an `adapter.yaml` feed manifest) **retired**, its premise gone.
- **DEL-03-02 Incremental reconcile** (housekeeping) with **DEL-03-02-REM-016** applied; the claims that no store or registry exists and that it is the "only" P1 act reading Git corrected.
- **DEL-03-03 Drift classification** (cause: new lag classes, SCA-005 A-21) with **DEL-03-03-REM-004** applied. New `REQ-015..017` with `AC-016..018` and `VER-015..017` for the three lag classes that the revision-1.6 `Deliverables.csv` description names; new `CON-006` (snapshot-to-snapshot versus within-snapshot comparison) and `CON-007` ("historical surfaces"), `TBD-005` (surfacing a "trailing by method design" result).
- **DEL-03-06 Rebuild performance bounds**: **DEL-03-06-REM-004 only** (four loci); nothing else changed.
- **DEL-04-05 Measurement-limitation honesty** (cause: an absent or historical ledger is a normal, declared case) with **DEL-04-05-REM-003** applied. The `CLM-011` consequence restates the case against the DEL-02-03 postimage (declared-historical silence is never staleness; PEC's ledger closed at Receipt 197); no requirement added.
- **DEL-10-02 Kill test** (housekeeping). New `CLM-014` records the downstream `[E-P91]` edge from DEL-10-13 (`D-PEC-101`); `CON-002` keeps the old DEL-01-05 phrase as dated history and stays open.
- **DEL-10-10 Directed-bootstrap self-ingest** (cause: TBD-005 "structurally different loop"; DEL-02-05 premise). New `CON-006` (the test of "structurally different" is undefined under feed profiles; X1's FX-PEC-0 design is not decided here); DEL-02-05 quotations brought to the postimage.

### `D-PEC-99` Part B landing (node S1)

Each item's correction input is applied **verbatim** (replacement strings byte-exact; the quote verifier checks each against the exhibit, both sides), and each re-quoted evidence value is re-verified at `125cfacc1` against its register cell and PRD row (the `gen_d95` quote-currency check, which also passes corpus-wide 127/127 before and after). **The gates bind**: each item authorizes only its named loci; the other changes in the same contracts come from the S1 currency causes under this packet, not from the item.

| Item | Contract | Landing lines in the postimage | Authored wording |
|---|---|---|---|
| DEL-03-02-REM-016 | DEL-03-02 | L148 (CLM-007, prior L134), L150 (CLM-007, prior L136) | none |
| DEL-03-03-REM-004 | DEL-03-03 | L169 (CLM-008: all four replacements), L347 (AX-009) | none |
| DEL-03-06-REM-004 | DEL-03-06 | L220 (shared values), L222–225 (table `EvidenceQuote` column), L229 (register-hygiene paragraph), L476 (AX-009) | L229: the direction "re-state it as dated provenance" is met by authored wording stating only the facts the item states; the "same disposition" comparison is removed. (The exhibit calls this locus "L228"; in the prior bytes L228 is blank and the paragraph is L229.) |
| DEL-04-05-REM-003 | DEL-04-05 | (1) L20; (2) L116 and L118–122; (3) L124; (4) L142; (5) L296; (6) L242 and L332 | (1) the bracket resolved to "**revision 1.6** (`current_basis`, SCA-006 successor)", since SCA-006 checkpoint 3 was accepted before this packet; (2) the placement of the added `EvidenceFile` column |

### Cross-candidate coherence and external anchors

- **Dependency quotes.** No ACTIVE `Dependencies.csv` row has an S1 contract as its `EvidenceFile` (the verifier's DEP check finds 0 rows for each), so no raw-substring anchor binds the postimages. No register is written.
- **Externally cited IDs kept:** `DEL-01-03/CON-001` (cited by DEL-01-01, DEL-01-06, DEL-02-03..09; subject kept), `DEL-01-03/REQ-003` (byte-identical; quoted by DEL-01-01 `CON-005`), `DEL-02-01/REQ-002` (cited by DEL-02-07 `CON-003`; its admission-rule sentence byte-identical). Qualified citations in the candidates resolve — S1 siblings against their candidates, every other deliverable against its contract at `125cfacc1`: `check_qualified_ids.py` `RESULT PASS 44/44`.
- **Sibling quotations.** Quotations of another S1 contract read the act tree (the sibling's candidate). DEL-03-01's candidate changes one quoted sentence (`CON-005`, "every manifest-named feed" → "every profile-declared feed"); DEL-10-02 and DEL-10-10 were reconciled to it, and DEL-03-02, DEL-03-03 and DEL-10-10 quote DEL-03-01 text that is byte-identical in its candidate.

### Consequences outside this packet (disclosed; nothing here writes them)

- **DEL-03-06, left stale by the correction-only scope (HELP_HUMAN: disclose, do not change):** frontmatter pin `@11a494e9a` and the revision-1.3 basis; L21–22 claims `_REFERENCES.md` cites that basis (re-pinned to 1.6 under `D-PEC-101`); L377 `CLM-017` names DEL-02-01..07 as "the seven feed grammars and the feed manifest", and L303/L398 say "manifest-named feed" (stale since SCA-005 and `D-PEC-100`); L359 "fourteen record-tier types" inside its `CLM-013` quotation. **After this act two of its quotations stop being verbatim:** L284 (`CLM-011`, quoting DEL-03-01 `CON-005`) and L346 (`CLM-013`, quoting DEL-03-02 `CON-001`). The D-PEC-100 heuristic's DEL-03-06 flag ("citation does not convert `PROPOSAL` to `DECLARED`.") is the contract's own voice, not a quotation. These belong to a later DEL-03-06 packet.
- **Other contracts quoting S1 text** (`scan_s1_consequences.py`, heuristic; `evidence/scan_s1_consequences.out`): DEL-03-04 (S4) quotes DEL-03-01 `CON-005` ("manifest-named feed"), which goes stale here — for the S4 packet to absorb, or a later one. The other hits are shared register-row phrasing or attribution boilerplate. DEL-02-07 `CON-003`'s premise ("that contract still expects this deliverable to supply 'the feed manifest'") becomes stale once DEL-02-01's `REQ-002` lands; the census-population question it routes stays open in both contracts. DEL-04-05 `CLM-012` quotes DEL-04-03 `CON-003`, which S4 is rebuilding.
- **S2 quotation currency (the `D-PEC-100` "consequence" list).** Of its fifteen contracts, nine are here: DEL-02-01, DEL-02-02, DEL-03-01, DEL-03-02, DEL-03-03, DEL-04-05, DEL-10-02 and DEL-10-10 are brought current; DEL-03-06 carries no quotation of replaced S2 text (the flag is a false positive). DEL-04-01, DEL-04-02, DEL-08-04 and DEL-10-03 are S4's; DEL-02-08 and DEL-02-09 a later revision of their own.
- **Register and record wording, reported only:** `_Decomposition/_LATEST.md` still says DEL-08-06 and DEL-10-13 have "no folders yet" (created under `D-PEC-101`); the `Deliverables.csv` DEL-01-06 Description `remaining-loop` text (COV-083); DEL-01-05 and DEL-10-10 `_DEPENDENCIES.md` "(owner-confirmed at D-PEC-62 ruling)"; the `D-PEC-84` register row "publication effect pending until merged"; SCA-005 IA §14 routes survey finding DR-14 to "DEL-02-02 SOW currency" (informational; not absorbed).
- **Findings for the owner's attention (open items, none resolved):** DEL-03-03 `CON-006`/`CON-007` (the lag classes rest on the `Deliverables.csv` description only; which comparison they are, and what "historical surfaces" covers); DEL-02-01 `CON-004` with `DEL-02-07/CON-003` (census population); DEL-10-10 `CON-006` (what "structurally different" means under feed profiles); DEL-01-05 `REQ-007` "pending" wording (a verification-basis item, left open).

## Options

- **A — replace the twelve contracts with the tabled bytes in one act, no lifecycle change (recommended).** **12 product paths, all modified**; nothing created or removed; no `_STATUS.md`, register, context, reference, dependency or `MEMORY.md` file touched. Add-on M (question 4) is independent.
- **A + M** — as A, plus the add-on M `MEMORY.md` records at the undertaking's closeout (11 created, 1 modified).
- **Amend** — for example: drop a deliverable (DEL-03-01 is quoted by DEL-03-02, DEL-03-03, DEL-10-02 and DEL-10-10, so dropping it requires re-drafting their sibling quotations; dropping any other single contract needs only a re-run of the checks); change a requirement; widen DEL-03-06 beyond REM-004 (needs a new candidate); resolve a CON now.
- **Defer** — nothing opens; the old S2 quotations and stale pins stay.

A per-deliverable split with the current bytes is not offered for DEL-03-01 and its quoting siblings (they are reconciled to land together); the method requires substantive ambiguity to be marked `CONFLICT`, so a split that drops open items is not offered either.

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once**. This ruling is the authority for the twelve replacements; the scope-of-work workflow supplies the authoring discipline (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`) and the independent `MODE=VERIFY`, as described under Method. Paths are relative to `projects/pec/execution/`.

| Deliverable | Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|
| DEL-01-03 | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` | `65c7f4086f8a053c41219c4966dd062a3821d43927c24fffe29f4e9046d2a367` |
| DEL-01-04 | `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/ScopeOfWork.md` | `4dd777f8f30cf5483d3c33bd002359e7266f8e411e74ba8655e2afc5aa367e62` | `16ac1cd956c90f0e757c9ce54c4e6645eea50e6d46d69b26f8052ad0484cca41` |
| DEL-01-05 | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md` | `53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53` | `a0a73eb5537b92d3a21ca8b01c0fc824b1cfb16823299dd3f3464e38a66784bf` |
| DEL-02-01 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/ScopeOfWork.md` | `5d286ec97f4c262be9e106537e3b7527e9756b6dd5bf0f1beb8259e1ca114440` | `82caf28a3757089ec07cd9a21ef70f97840fda7b92f1017236ce5062fdf55872` |
| DEL-02-02 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/ScopeOfWork.md` | `5f20b1c48f4f383a07240e04bdf524e8b2443af37cb745c549f939cd6bb8db6e` | `84e55e58e6632845f7462970180c052ebec5fc677072a4bd883f871a002ffa86` |
| DEL-03-01 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md` | `564955235aeab60f169e6377dd9d5bb5fbe2a88a8cc66094e17f6f83987792d2` | `5b71d3583b2e661564acf889c0a0d6fef93ce24302f29845c3cda0a367ae8276` |
| DEL-03-02 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/ScopeOfWork.md` | `d1335c01c54686427d6a04658a43ce9e5c4abe2e446e0acf4d1e87df3a7785b5` | `d823d55d9e714ac3142c02ee5d599d7167e0836c89c1abee7c513b072073a3d0` |
| DEL-03-03 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/ScopeOfWork.md` | `5ce8ab72425ab417c90c3e64a152912a7e39b243f3905e65477dbfd91a40eaa7` | `c2b88cb65c71bf017fc42c85e164470f0ea86696bd100ed0157d4c2a53f79526` |
| DEL-03-06 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md` | `90de9c2d93d8350805410753a21f19c5cf141e48c3e94ffc8096621b3a42c97e` | `f9c3a057717292e7ccd6def6e0496f69ad6c5100457b15cd17b37477adff8bd4` |
| DEL-04-05 | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md` | `933c012cf16bb161b0ac1acdbf3caeaac408fa441b6e175b8fc2e7d8b265a579` | `88029fead86c1f3f36c98c065f3f283370bd772e16c4dd9aeda2a8193595eafd` |
| DEL-10-02 | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md` | `99730e4e85ce4920d676d9fd62d26c193d5fd714ea0592c15462f37a62011a82` | `f5590cf55b19f3170cb04e65340e076e672d5d54d8f1e98385372d1dd8f3436e` |
| DEL-10-10 | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md` | `640f23711f93ec7e987742ed5ed998bea04c681f14bff06bdf2e35a669fcbd5e` | `15c10a56c21bf35e18d93b46d47f5f91e2d079872c1fc644aae89704bd0135f4` |

The postimages are the exact candidate files, copied byte for byte into the run root as `candidates/…`. They have no date slot.

Read-only files the act re-verifies and never writes (SHA-256 at `125cfacc1`, equal at `3488a236a`; the first five equal at the pin `189f205ff`): `SOFTWARE_DECOMP.md` `9374c21f…8eb1`, `Deliverables.csv` `94ee5d18…9805`, `ScopeLedger.csv` `1d24a4b8…916e`, `ContextBudgetQA.csv` `93b0bb07…4c7c`, `docs/PRD.md` `ae49b806…3fbe`, `v2/config/loops.json` `fd342b4f…53d7`, `loops.schema.json` `104ed648…b143`, `projects/pec/AGENTS.md` `df9196d1…5eb8`, the `D-PEC-99` exhibit `69b646f8…f45e`, and each target's `_STATUS.md` and `Dependencies.csv` (24 files). The full values are the `PINNED` table of `apply_s1p.py` (33 files).

### Add-on M — MEMORY records (only if question 4 selects it)

At the undertaking's closeout (graph node M1), WORKING_ITEMS writes, in each target's folder:

| Deliverable | `MEMORY.md` preimage | Act |
|---|---|---|
| DEL-01-03 | `44b360c57b934c585befe2cf6a0741199d4cc4ac6b8fc64c04f7be33b88bdae6` | modified: one dated section appended in the file's existing form (`## {D} — D-PEC-104 S1 Scope of Work currency (graph node S1)` with one line linking the central receipt, PR #{PR} and the ruling record) |
| DEL-01-04, DEL-01-05, DEL-02-01, DEL-02-02, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-06, DEL-04-05, DEL-10-02, DEL-10-10 | absent | created from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` row |

The row, in every created file:

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | Scope of Work brought current under D-PEC-104 (graph node S1). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-104 ruling record> |
```

The slots `{D}`, `{PR}` and the link targets are fixed at closeout; the verifier checks that no other byte departs from the template (new files) or from the preimage plus the named section (DEL-01-03).

## Generation method (binding)

The twelve postimages come from one run of `apply_s1p.py`, **SHA-256 `41d1e5f89de94b573e4103cb73cac26ffb8a260eea8b640bc652ea650f6c090e`**. It is stdlib-only Python on the `D-PEC-100` `apply_s2p.py` pattern, prepared with CPython 3.13.7, and is copied byte for byte into the run root with the twelve candidate files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_CURRENCY_S1_{D}/apply_s1p.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_CURRENCY_S1_{D}/candidates [--check-only]
```

**Failure semantics.**

- **Preflight.** Every candidate hashes to its postimage; every target exists and holds its preimage; no temporary sibling exists; every pinned file hashes as tabled; and, if the script's directory path begins with `projects/pec/`, that path must begin with a run root (`projects/pec/execution/_Coordination/SOW_CURRENCY_S1_*`). Any failure exits 1 before any byte is written.
- **Write.** Each postimage is written to a temporary sibling (`…ScopeOfWork.md.s1ptmp`), hash-checked and renamed over its target. If any step after the first write fails (I/O error, hash mismatch, post-write inventory mismatch, changed pinned file), the script restores every replaced target from the preimage bytes it read at preflight, removes every temporary file, and exits 1; exit 2 would report an incomplete rollback (never observed in testing).
- **Write set.** The script inventories every file under `projects/pec` (path and SHA-256), except its own directory (the run root), before and after the write, and requires the difference to be exactly the twelve targets, each modified from preimage to postimage, with nothing created or removed.
- **Second run.** It fails preflight: the targets no longer hold their preimages. The script never touches `_STATUS.md` or `MEMORY.md`.

The check aids, which are not bound:

| Aid | SHA-256 | Role |
|---|---|---|
| `test_apply_s1p.py` | `3e555e69b4f67d2732267bae4bf89a44ad41552e9786f284c55e57ee8f0c7310` | fault injection, nine cases |
| `verify_s1p_quotes.py` | `c9d6f4506a8eec86341f5b4b43abda0213664f9a64da9f1ffed5aba8e6acf57f` | two-sided quote check, raw dependency quotes, forbidden phrase, observation commit (DEL-03-06 exempt) |
| `verify_s1p_state_claims.py` | `5cf34ac18632cb2d1369af025188be58b32b13489bd9ac4478fde30567133bb6` | commit-anchored state claims, each also matched in the candidate |
| `check_qualified_ids.py` | `1d77fb5bf8baedabe27ef66a340864351b36c616bccfd5e1d3c576a0f590f873` | qualified citations resolve (S1 siblings against candidates; others against `125cfacc1`) |
| `check_dep_quote_currency.py` | `bb802d7bd161bb54b901db5be697e8fc1a0a47a46a5b01333053f50dae78eabd` | the `gen_d95` quote-currency check, corpus-wide |
| `scan_s1_consequences.py` | `154ef6b0531189dbbcac6e2fd4284b0b459b181aceb9ec306c104bbb01faa9db` | informational consequence scan |
| `aids/audit_quotes.py` | `26af567140698480448e2bca24f09af2c0c47bf93b565b1c72a3311ac6f8944e` | informational quote-source audit (drafting aid) |
| `run_s1p_checks.sh` | `8cc735dbfd06b12803fa7e3e644f902215101a3b30d549e683322a16e9fd2a35` | runs checks 2–11 on pre/post exports |
| `negative_controls.sh` | `81525d370c9272c7d51c0cd8a9f4ba084a4e87a0e211363917ebd5dd00f6c0d2` | eight negative controls |

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`, on the act branch. Record each command, exit code and output in the run root. `run_s1p_checks.sh` runs rows 2–11 on two `git archive` exports of one commit (pre and post), and is the rerun method.

| Check | Command | Required result |
|---|---|---|
| 1. Preconditions | ruling and register row on fetched `origin/main`; `apply_s1p.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `--check-only` exits 0 with `CHECK preflight passed`; `ALLOW` everywhere; on any pin mismatch, stop and route to the owner (no re-pin is pre-authorized) |
| 2. Contract validity | `validate_scope_of_work.py <DEL folder>` ×12 | `PASS format=SOW_V1` ×12 |
| 3. Checklist | `derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, each twice | exit 0; reruns byte-identical; each equal to the prepared checklist (hashes under Preparation evidence) |
| 4. Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json … --show-not-checkable <DEL folder>/ScopeOfWork.md` ×12 | exit 0; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; every `NOT_CHECKABLE` clause resolved by hand as tabled below |
| 5. Quote fidelity | `verify_s1p_quotes.py --tree . --gitdir . --prep <run root> --observation 125cfacc1 --obs-exempt DEL-03-06` | `RESULT PASS 884/884` (both sides). Tree quotations carry `"commit": "125cfacc1"` or an older commit and are read there; only quotations of an S1 sibling read the act tree |
| 6. State claims | `verify_s1p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 894/894` |
| 7. Qualified IDs | `check_qualified_ids.py --prep <run root> --gitdir . --observation 125cfacc1` | `RESULT PASS 44/44` |
| 8. Dependency quote currency | `check_dep_quote_currency.py .`, before and after | `RESULT PASS 127/127` each |
| 9. Lifecycle preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty |
| 10. Strict registers (D-GOV-48) | `validate_decomposition_registers.py --strict projects/pec/execution`, before and after | exit code and output **identical** to the pre-act run (at `3488a236a`: exit 1, 0 errors, 26 pre-existing `XRG-013` warnings, owner-deferred under D-GOV-48). A new finding or a changed count fails |
| 11. Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | exit 0 each; output identical before and after |
| 12. Containment | `git diff --name-status origin/main...HEAD` | the twelve modified contracts; M's files if selected; the run root and HELP_HUMAN's records under `execution/_Coordination/**`; nothing else |
| 13. Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. The act changes no decomposition truth, register or topology.

QA 21 hand resolution (clauses the tool reports as `NOT_CHECKABLE`, each resolved by the drafter and checked by the verdicts):

| Contract | Requirement → owner (cited claim) |
|---|---|
| DEL-01-03 | REQ-006 (unchanged) → `DEL-07-01` event ingest, P1 reconciler and P3 presence/Git paths (CLM-008) |
| DEL-02-01 | REQ-002 → `DEL-01-06` (CLM-011), `DEL-02-07` (CLM-004, CLM-011); REQ-003 → `DEL-01-01` (CLM-007, CLM-011); REQ-005 (unchanged) → `DEL-04-03` (CLM-011; REQ-005 cites CLM-007, pre-existing); REQ-012 → the owners named in CLM-004 and CLM-011 |
| DEL-02-02 | REQ-005 (unchanged; cites no claim) → `DEL-04-03` (SOW-007), `DEL-03-01` (SOW-010, CLM-009) |
| DEL-03-01 | REQ-007 → `DEL-02-06` (CLM-016, CLM-019), PKG-02 (CLM-007, CLM-019); REQ-009 → `DEL-04-05` (CLM-019) |
| DEL-03-03 | REQ-015 → `DEL-02-08` (work-graph parse and PR resolution), `DEL-04-01` (terminal completion) (CLM-015) |
| DEL-04-05 | REQ-003 (unchanged) → `DEL-08-03` (CLM-014, CLM-016); REQ-005 (unchanged) → `DEL-04-03` (CLM-012, CLM-016) |
| DEL-01-04, DEL-01-05, DEL-03-02, DEL-03-06, DEL-10-02, DEL-10-10 | none reported |

### Independent verifier

The method's independent verification is a separate `MODE=VERIFY` run, read-only on production content, by a TASK that authored nothing. The preparation verdicts are in the prep folder (`VERIFIER_VERDICT_01.md` onward, each with the manager's dispositions); a fresh one runs again at the act. It returns a verdict file; defects return to the author, and the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`; the run-root script hashes as bound; the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **`MODE=VERIFY`.** The mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21), including the QA 21 hand resolution.
4. **Semantics.** Every claim is true at the commit it names or at `125cfacc1`; every quotation is verbatim; no requirement adds scope beyond the deliverable's ledger rows, its `Deliverables.csv` row and PRD v2.4; every open item is `TBD`/`CON`; kept IDs keep their meaning and retired IDs are not reused; the Part B replacement strings are byte-exact and the gates are respected; DEL-01-03 and DEL-01-05 REQ/AC/VER are byte-identical to their preimages; DEL-03-06 differs from its preimage only at the four REM-004 loci; no Remaining section is read or presented as a surface; nothing mentions CHECKING.
5. **Containment and lifecycle.** As in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act, the checks and, if selected, add-on M at closeout. It runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/SOW_CURRENCY_S1_{D}/`, in the default-writable fence: `apply_s1p.py` (exact bytes), `candidates/`, `quotes/`, `claims/`, the check aids and all outputs; `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`; `VERIFIER_VERDICT_NN.md`. No `_run_records/` entry is written in any deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under `D-PEC-88`. `_Evaluation/**`, registers and dependency files stay closed.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning, unless the owner states otherwise. Role identity is instruction-asserted.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the script leaves every target at its preimage and no temporary file. If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR restores the twelve preimages tabled above, and removes M's eleven created files and DEL-01-03's appended section if M ran. No lifecycle state changed, so nothing else is walked back. The ruling record and register row are never reverted; a rollback is its own register row and record. The run root stays as non-current evidence with a rollback note. No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + M or an amendment, grants none of the following:

- any `v2/**`, `software-workflow.json` or `docs/PRD.md` write, or any source, fixture or test file; nothing here accepts, re-verifies or changes the produced DEL-01-03 or DEL-01-05 artifacts;
- any `_Decomposition/**` or `_ScopeChange/**` write, or any register write: no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `Dependencies.csv` or `_DEPENDENCIES.md` change, no dependency edge (DEL-02-01 `CON-006` stays open), and no action on the D-GOV-48 warnings;
- any `_CONTEXT.md`, `_REFERENCES.md` or `_SEMANTIC.md` write, or any file of a deliverable outside the twelve (the disclosed consequences in other contracts, including the rest of DEL-03-06, are for their own packets);
- any lifecycle change or `_STATUS.md` write. No `## Remaining` entry is written or read;
- `CHECKING`, `ISSUED`, artifact acceptance, a REVIEW gate act, or any readiness or reliance claim;
- a registry, profile or D-PEC-96 act, or a resolution of any `CON` item;
- a Task Management disposition, an audit run, a pointer move, or an edit of the `D-PEC-99` exhibit;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- adoption of `scope-of-work` `MODE=REVISE` or any other new Root mode;
- a schedule reading: blocker output stays advisory.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**, the twelve exact replacements in one act, authored under `INIT` discipline and verified by `MODE=VERIFY`, as described under Method.
2. **Part B reading.** Confirm that the ruling on this packet accepts the exact wording tabled under "`D-PEC-99` Part B landing" for DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004 and DEL-04-05-REM-003 — including the authored DEL-03-06 L229 paragraph and the DEL-04-05 bracket resolved to revision 1.6 — and discharges each item's gate only for the text it applies. Recommendation: **confirm**. Without an answer, the text is applied and each gate stays binding on anything further.
3. **DEL-03-06 scope.** The packet applies the REM-004 correction only, as `D-PEC-99` question 1 (a) and the S1 graph row state; the rest of DEL-03-06's stale text (listed under Consequences, including two sibling quotations this act makes non-verbatim) waits for a later packet. Recommendation: **keep correction-only**; an amendment widening DEL-03-06 needs a new candidate.
4. **Add-on M — MEMORY records.** Create the eleven `MEMORY.md` files and append one section to DEL-01-03's existing `MEMORY.md`, at closeout, as tabled (recommended); or record the run only in the graph and central receipt. `projects/pec/AGENTS.md` allows either on your decision.
5. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran on `git archive` exports in the session scratchpad, never on a checkout. Interpreter: Python 3.13.7 (CPython); local date 2026-09-26. The final run (`evidence/run_main/SUMMARY.out`, from `run_s1p_checks.sh` at `3488a236a` with observation `125cfacc1`; every raw output is beside it):

```text
basis commit: 3488a236af293762ef47b0101a4c209845f372e7
python: Python 3.13.7
PASS act: check-only 0, apply 0, rerun refuses 1
PASS containment: 12 differing files, all ScopeOfWork.md
PASS validate / checklist (rerun byte-identical) / boundary ×12
PASS quotes: RESULT PASS 884/884
PASS state claims: RESULT PASS 894/894
PASS qualified IDs: RESULT PASS 44/44
PASS dependency quote currency (pre): RESULT PASS 127/127
PASS dependency quote currency (post): RESULT PASS 127/127
INFO quote audit (informational): S2-STALE 2 NOTFOUND 0
PASS strict identical before/after, export root normalized (exit=1)
PASS harness identical before/after, export root normalized (exit=0)
PASS receipts identical before/after, export root normalized (exit=0)
PASS whitespace
PASS fault injection: RESULT PASS 9/9
OVERALL PASS
```

The two informational S2-STALE hits are both in DEL-03-01 and neither is a quotation of replaced S2 text: L305 is its own attribution line and L198 is the DL-4 rationale, verified at `SOFTWARE_DECOMP.md`.

Negative controls (`evidence/negative_controls.out`, scratch copies): an altered DEL-03-02 Part B replacement string, a one-character change to DEL-02-02's PEC-RCN-002 quotation, a wrong hash in a DEL-01-04 claim, a removed DEL-03-01 `CON-005` definition that siblings cite, a changed DEL-03-01 `OUT-001` under DEL-03-02's sibling quotation, a candidate differing from its tabled postimage, and a removed DEL-01-04 matrix row (validator fails; checklist refuses with no artifact) — each is caught.

Checklists (`evidence/run_main/checklist_<DEL>.json`): DEL-01-03 `e3fe784b…6a95`; DEL-01-04 `ab1efb30…1b22`; DEL-01-05 `a7d58cbd…f164`; DEL-02-01 `691455d0…545a`; DEL-02-02 `78336479…fc07`; DEL-03-01 `9f683083…6db1`; DEL-03-02 `3a1f8098…35e2`; DEL-03-03 `e7e76f9b…cfe8`; DEL-03-06 `e0bcdb5e…fc46`; DEL-04-05 `04e72e08…920f`; DEL-10-02 `9f038cda…cb9b`; DEL-10-10 `d3fe09a3…eeea`.

Preparation artifacts (all in this prep folder; hashes in `SHA256SUMS`): `candidates/…/ScopeOfWork.md` ×12; `quotes/DEL-*.json` ×12 and `claims/DEL-*.json` ×12; the bound script and the aids above; `briefs/` (drafter and verifier briefs); `evidence/`; `VERIFIER_VERDICT_01.md` onward.

Basis at `125cfacc1`:

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `9ae4bea2…9665` / `1a13a5b0…8fb7` / `df9196d1…5eb8` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` |
| `docs/PRD.md` (v2.4) | `ae49b806…3fbe` |
| SCA-005 `Propagation_Plan.md` / SCA-006 `Impact_Assessment.md` / SCA-006 `Propagation_Plan.md` | `50cd0b1d…1350` / `93253b7d…b691` / `f95d00d1…d7d8` |
| `D-PEC-99` ruling / exhibit; `D-PEC-100` ruling / proposal; `_REGISTER.md` | `3e34403a…c989` / `69b646f8…f45e`; `13690e20…729b` / `39c4331e…5b25`; `33b43ae8…5a2f` |
| `v2/config/loops.json` / `loops.schema.json` / produced guard | `fd342b4f…53d7` / `104ed648…b143` / `740a4a74…19ee9` |
| `validate_decomposition_registers.py` / `MEMORY_TEMPLATE.md` / `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `300a321f…ee20` / `5a9564f4…6a5a` / `f877d931…1cbc` / `b1712e4b…cd0e` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, node S1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with twelve TASK drafters and fresh read-only reviewers (one per verdict) as described under Method. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The roles and the `high` reasoning effort are instruction-asserted.
