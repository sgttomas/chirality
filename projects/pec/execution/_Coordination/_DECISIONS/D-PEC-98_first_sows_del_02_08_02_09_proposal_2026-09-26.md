# D-PEC-98 — First Scope of Work contracts for DEL-02-08 (work-graph parser) and DEL-02-09 (MEMORY run-index parser) — proposal

Status: **PROPOSAL / AWAITING_RULING** (revision 2). **The number D-PEC-98 is provisional**: it becomes final only when this packet is published with its register row. Prepared by a TASK (Type 2) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3) for the PEC loop, 2026-09-26 (session date), from brief `S3_FIRST_SOWS_PROPOSAL.md` (SHA-256 `ef12b7408b68edb283055200de424169878fd3d122df43892d099432a8ea537a`) and HELP_HUMAN's relayed revision instructions. No earlier direction approves this file. It performs no production act: no tracked file was edited, and every prototype ran on scratch copies only. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `origin/main` `53145aaeb` the register has no D-PEC-98 row. Filing name as published in PR #944: `execution/_Coordination/_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`.

The act it asks for is bounded: create two new files, `DEL-02-08/ScopeOfWork.md` and `DEL-02-09/ScopeOfWork.md`, with the exact bytes below. The lifecycle transition that PEC has paired with first contracts before is **not** part of option A; it is offered separately as add-on S (question 2).

**Revision 2.** Revision 1 was published unchanged as PR #944. HELP_HUMAN relayed that the independent `MODE=VERIFY` gave both candidates FAILED on claim grounding, with schema and mechanical checks passing. This TASK has not seen the verifier's report; it worked from the relayed findings:

| Finding | Change in revision 2 |
|---|---|
| B1: "at the basis" claims false at the pin `c9e5cd87d` (no D-PEC-96 row, template `4411d0c2…`, workflow `24268f35…`) | Each contract now states an **observation commit**, `origin/main` `53145aaeb`. Every unanchored state claim is an observation at that commit, and the phrase "at the basis" no longer appears. DEL-02-08 CLM-013 gives the template and workflow hashes at both commits and names the Root commit that changed them. The D-PEC-96 status now reads: revision 4 merged at `6281273fa`; at `53145aaeb` the register row reads `RULED A / EFFECTIVE ON MERGE` (ruling record merged in PR #946 at `f90320c1d`), and the registry act is not applied (`loops.json` is still schema version 1). The contracts still rely on no D-PEC-96 identifier. A new `verify_d98_state_claims.py` checks every commit-anchored claim with `git show` (44/44). The quote verifier fails any candidate that contains "at the basis" |
| B2: strict-register row required 0/0 | The row now requires the exit code and output to be identical to the pre-act run, and names the 26 pre-existing D-GOV-48 `XRG-013` warnings (exit 1 under `--strict`). The notice is finding 10 |
| C1: DEL-02-09 "entry counts per file" | Dropped from REQ-003 and AC-003, which now extract only the three `SOW-096` fields "and no other field" |
| C2: question 4 re-pin | Question 4 now says exactly which bytes move, how `TARGETS` and `PINNED` are re-bound, which "revision 1.5" and "PRD v2.3" mentions stay and why, and how the basis and observation commit move |
| C3: quote verifier one-sided | Every check now requires the quoted text in the candidate and at the source. A candidate-side negative control fails as designed. Writing the two-sided check found two revision-1 defects. DEL-02-09 cited PEC-K-10 without quoting it, so that check was wrongly applied to it and is removed. DEL-02-09 quoted a fragment ("S, LOW") too short to verify, so the quotation is lengthened to the full §8 sentence |
| C4: add-on M paths | The grant names both `MEMORY.md` paths |
| C8: add-on S and `NO_STATUS_TOUCH` | S runs after the scope-of-work run has returned, and outside it. It is a separate generic-shell TASK dispatched by WORKING_ITEMS, as D-PEC-63 §3.2 did, so `NO_STATUS_TOUCH` holds literally |
| C9: failure wording; write set | `apply_d98.py` now writes through temporary files and rolls back on any post-write failure, so on exit 1 no target or temporary file remains. It inventories every file under `projects/pec` before and after, and requires the difference to be exactly the two targets. `test_apply_d98.py` injects five faults, 5/5 PASS |

## Provenance

- **Owner acts relied on.**
  - The owner's 2026-09-25 steering, recorded in `D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…5a6b`): "You can continue with all the open work you identified." HELP_HUMAN's work graph turns it into node S3, "First SOWs for DEL-02-08 and DEL-02-09 … via preparation → Scope of Work (WORKING_ITEMS)" (`WORK_GRAPH.md` `a203523d…6720` at `53145aaeb`).
  - SCA-005 checkpoint 2 (`D-PEC-92`, 2026-09-25) accepted `Propagation_Plan.md` (`50cd0b1d…1350`). Its §B4 says: "The two new deliverables receive first SOWs through the ordinary preparation → Scope of Work path", and carries forward the guard cases these contracts must address. Its §B7 places the P1 fixture strategy "inside the DEL-02-08/09 and DEL-02-03 SOWs". Checkpoint 3 accepted revision 1.5 as `current_basis`.
  - `D-PEC-93: A.` (`D-PEC-93_RULING_2026-09-25.md`, `ffb0b582…3709`) created both folders with the `preparation` skill. `D-PEC-95` (ruled P + R) re-pinned the metadata the contracts read.
  - `D-PEC-63` (RULED 2026-07-25) is the precedent for first-contract authoring and for a separately ruled `OPEN → INITIALIZED` status act. `REV_DEL-01-06_2026-08-04_1113` is the precedent for a SOW act that leaves lifecycle unchanged.
  - `D-GOV-16` (RULED APPROVED 2026-07-12) ratified `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`: "New deliverables use `SOW_V1`" (§7).
- **Observed, not needed by this act.** The owner's D-PEC-96 ruling of 2026-09-26, "D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults" (`D-PEC-96_RULING_2026-09-26.md`, `852057f0…399e`, merged in PR #946 at `f90320c1d`; register row `RULED A / EFFECTIVE ON MERGE`). The contracts rely on none of its identifiers. Its "create MEMORY" answers D-PEC-96 question 6 for DEL-01-06; it is not an answer to this packet's question 3.
- **Fence.** `projects/pec/AGENTS.md` (`c9d3b44d…197a`) §"Write Scopes And Fences": only `execution/_Coordination/**`, `AGENTS.md` and the one-time STATUS pointer are default-writable; every other write under `projects/pec` needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. No earlier ruling opens the target paths. `D-PEC-93` opened folder creation only; `D-PEC-95` opened `_CONTEXT.md` and `_REFERENCES.md` anchors.
- **Source state.**
  - Every hash below was read at `origin/main` **`53145aaebb23b617e7ba1d2c626a6218d2be9176`** (PR #947) after `git fetch`, from `git archive` exports and a scratch clone.
  - Since revision 1's basis `8f9bd314c`: PR #940 merged the owner-direction records, PR #941 published D-PEC-96 revision 4 (merge `6281273fa`), Root PR #942 made D-GOV-48 effective, PR #945 applied workflow wave-3 fixes, PR #946 recorded the D-PEC-96 ruling (merge `f90320c1d`), and Root PR #947 generalized the `change` workflow. PR #947 changed `workflows/index.json`, but its `scope-of-work` entry is unchanged.
  - Among the basis files, `tools/scaffolding/write_status.sh` changed (wave 3: `--ruling` resolved with `pwd -P`), `project-setup` `method.md` shifted one line, and `scope-of-work` `resources/representation-migration.md` changed. The last is conversion-only and not loaded. The decomposition registers, PRD, templates, the `scope-of-work` entrypoint and tools, and every file the candidates quote are unchanged.
  - The checkout was not changed by this TASK.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`) was run from `projects/pec` with `--operation exact-correction-preparation` on all six possible targets (both `ScopeOfWork.md`, both `_STATUS.md`, both `MEMORY.md`): `ALLOW`, exit 0, ×6.

## Method

- **Workflow.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`6c549b59…ee4c`; precedence project → user → bundled; no project or user workflow of that name exists). Files: `WORKFLOW.md` `d616865a5cbfa84b47fd509d2910826106db57473543a86d067ddc3edf6fbd8b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `a082f1af…5145`, `resources/tools.md` `2bbb55cc…0f3f`, `resources/checks.md` `fbb2c8eb…76b8`, `resources/representation-migration.md` `698957a5…3e3c3` (not loaded; conversion only).
- **Mode.** `MODE=INIT`, `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, `RENDER_HTML=false`. INIT is source-grounded authoring: no conversion, claim map, parity or finalizer.
- **Transition contract.** The workflow's "active SOW_V1 transition contract" is `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (`26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`), ratified by D-GOV-16.
- **`preparation`.** Not re-run. The folders and control files were created under `D-PEC-93` by the `preparation` skill, so the method's "preparation → Scope of Work" path is at its second step.
- **Tools** (`tools/scope_of_work/`, unchanged at `53145aaeb`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, with `common.py` `61a34722…0389` and `id_catalog.json` `7a1f8a12…757`.

## What preparation found

### The two candidates

| | DEL-02-08 Work-graph parser | DEL-02-09 MEMORY run-index parser |
|---|---|---|
| Scope item / objectives | `SOW-095` / `OBJ-001`, `OBJ-002` (indirect, §3 mapping note) | `SOW-096` / `OBJ-001`, `OBJ-002` (indirect; `OBJ-002` leg stated as thin) |
| Basis pin / observation commit | `SOFTWARE_DECOMP.md@c9e5cd87d` (checkpoint-3 acceptance, revision 1.5) / `53145aaeb` | same |
| Definitions | 3 OUT, 18 CLM, 20 REQ, 21 AC, 20 VER, 12 AX, 7 TBD, 5 CON | 2 OUT, 17 CLM, 16 REQ, 17 AC, 16 VER, 11 AX, 7 TBD, 4 CON |
| Outputs | parser; pinned FC-1/FC-2/FC-3 fixture suites; synthetic grammar-edge fixtures and test suite (the register's three-part artifact list) | parser; fixture test suite for the table, bullet and dated-heading forms |
| Size / SHA-256 | 262 lines, `03cce13f484a9b595b5162bd662af42bcd67aae37a8843304bf03cfbb3badc0a` | 235 lines, `aafb54fd6457f09da8304ead444686703d5f8d2c28f4c94ec4eab4d2737b188b` |

Both follow the sibling PKG-02 contracts' form (`DEL-02-01`, `-03`, `-04`): the same frontmatter keys, the six required headings, the "Identity of record / Placement in the work graph / Boundaries" subsections, qualified upstream IDs, one acceptance criterion per matrix row, and a closing human-review criterion for objective traceability.

**Observation commit (B1).** The decomposition pin `c9e5cd87d` binds the accepted revision-1.5 register and PRD bytes. Much that the contracts describe did not exist there, including this deliverable's folder, D-PEC-96's row and the revised graph template. Each contract therefore says: "Unless a claim names another commit, every statement below about the state of a file, record, lifecycle or decision is an observation at `origin/main` `53145aaeb`". It also says the three registers and PRD are byte-identical at both commits. The corpus observations keep their own anchors (`7a00a88df` for the graph and MEMORY counts, `d61981ee2` for the fixture blobs). `verify_d98_state_claims.py` rechecks each anchored claim at its named commit.

**What the contracts require, in brief.**

- **DEL-02-08.**
  - Discovery only at the canonical path, and only where the loop's registered feed profile declares the work-graph surface.
  - The integration ref by default; branch refs opt-in and labelled unintegrated; read-only plumbing, no fetch.
  - Exactly the eight `SOW-095` fields, under a declared, versioned grammar.
  - Node states only from the method's closed vocabulary. An unknown token becomes a limitation, never coerced and never copied.
  - Declared activity, never liveness or completion.
  - The run identity only from the declared field.
  - PR numbers resolved to local merge commits, or "unresolved locally"; never guessed.
  - Explicit limitations, no prose, provenance, no writes, determinism, no own record-tier type.
  - No `## Remaining` read. A template-form boundary exclusion.
- **DEL-02-09.**
  - Reading only where the profile declares the MEMORY run index. A missing `MEMORY.md` or `## Runs` is a stated coverage limit.
  - Three declared grammars: template table, bullet, dated heading.
  - Exactly run-ID tokens, dates and link targets, and no other field.
  - A run token only where the grammar fixes its position.
  - Join evidence only.
  - The same limitation, content-minimal, provenance, read-only, determinism, typing, no-Remaining and boundary rules.

**Fixture classes (brief item).**

- Both contracts state the SCA-005 §B7 classes assigned to node X1, quoting §B7 verbatim: **FC-1 receipt present**, **FC-2 evidence-only** and **FC-3 no AgentRuns record**.
- They are golden-by-reference fixtures pinned at `d61981ee2`, and nothing is copied into PEC's tree. Synthetic grammar-edge fixtures are added.
- The fixtures themselves remain X1's, under a later v2 packet. The five pinned blobs are unchanged at `7a00a88df` and `53145aaeb` (state-claims check).

**Open decisions recorded, not assumed.**

| Contract item | What is open | Where it resolves |
|---|---|---|
| 08 CON-001 / 09 CON-001 | Upstream typing. The accepted `DEL-01-01` contract (`43f1f57a…0170`) obliges exactly fourteen types, with no WorkGraph/WorkNode, and admits only JSON evidence into RunRecord (`DEL-01-01/REQ-006`). | `DEL-01-01` rebuild (graph S2); implementation ordering is a graph/owner choice |
| 08 CON-002 / 09 CON-002 | Discovery basis. No registry declares feed profiles at `53145aaeb` (D-PEC-96 is ruled but not applied). `DEL-01-06`'s contract is strict version-1, and no dependency row links either parser to `DEL-01-06`. | The ruled D-PEC-96 act and the `DEL-01-06` rebuild (S2); the edge question belongs to `dependency-extract` |
| 08 CON-003 / 09 CON-003 | Guard admission. Node states, node IDs, run tokens, DEL bindings, PR numbers, dates and abbreviated SHAs are outside the produced guard's classes. These are `DEL-01-03/CON-001` cases. | `DEL-01-03` / `DEL-01-01` packets |
| 08 CON-004 | FX-PEC-0 (§B7, under `remaining-loop`). No FX-PEC-0 output and no Remaining-reading fixture. | X1 / `DEL-10-10` |
| 08 CON-005 | Work-graph dependencies: routed to `SOW-095` by PRD §7.1 and the `SOW-015` Notes cell, but not named in its field list. No DependencyEdge. | scope change or owner ruling (question 5) |
| 09 CON-004 | Run tokens in dated headings. A token is emitted only where a declared grammar fixes its position. | method or scope decision |
| TBD-001..007 (each) | ResponsibleParty; exact grammars; PR-resolution syntax; profile identifiers; ref selection and "Current graph ref" (08); golden format and threshold; abbreviated SHAs (08); MEMORY folder pattern, mixed-form files and join ownership (09) | production within the REQs, or the named owner |

### Dependencies on D-PEC-96 (without presuming its ruling)

- **State at `53145aaeb`.**
  - The published proposal is revision 4 (`4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e`, merged at `6281273fa`, PR #941). The register row reads `RULED A / EFFECTIVE ON MERGE`, and the ruling is recorded in `D-PEC-96_RULING_2026-09-26.md` (merged in PR #946 at `f90320c1d`).
  - Its closed vocabulary is `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1. The `status-remaining` surface is removed, and `shared-dev-loop` covers the `work-graphs` and `memory-run-index` surfaces.
  - The registry act the ruling authorizes is not applied at `53145aaeb`: `v2/config/loops.json` still carries `"schema_version": 1` and no feed profile, and the `DEL-01-06` contract is not rebuilt.
  - The contracts state exactly this in DEL-02-08 CLM-009 and DEL-02-09 CLM-008.
- **What the contracts assume.** Only that a loop's registry row may declare the work-graph and MEMORY run-index surfaces, as PRD v2.3 PEC-RCN-002 and §16.3 already say. They depend on no D-PEC-96 identifier; the identifiers stay TBD-004 (08) and TBD-003 (09).
- **Remaining sections.** There is no Remaining-reading dependency.
  - PRD v2.3 §7.1's "remaining items is a per-loop optional field, read only where the loop's feed profile declares it" is a `_STATUS.md` field. It belongs to `DEL-02-01`, not to a work-graph or MEMORY surface (08 CLM-018, 09 CLM-017).
  - **The parsers do not read `## Remaining` sections**: 08 REQ-001 and REQ-015, 09 REQ-001 and REQ-013, with matching acceptance criteria and verification methods.
  - Revision 4 contains no Remaining-reading profile, and neither contract needs one.
- **Under each outcome, the contract bytes stay valid.**
  - **Once the ruled act is applied.** PEC's row declares `shared-dev-loop` live, so PEC's own graph and DEL-01-03's `MEMORY.md` fall inside discovery.
  - **Until then, or if the registry later changes.** Whatever profile declares the two surfaces applies. Where none does, the parsers discover nothing and report the missing declaration (REQ-001).
  - **Ordering.** This packet does not need the D-PEC-96 act applied first. Implementation and X1 need the registry and the `DEL-01-06` rebuild. CON-002 stays open until then.

### Lifecycle: what the method does to `_STATUS.md`

- **The method never touches it.**
  - `WORKFLOW.md`: "Do not modify `_STATUS.md`, lifecycle state, underscore control files, …".
  - `resources/brief.md`: `STATUS_POLICY` defaults to `NO_STATUS_TOUCH`, and "`ADVANCE_ON_PASS` additionally requires the brief to authorize `_STATUS.md` writes".
  - `resources/tools.md`: the tools "do not modify lifecycle state".
  - `resources/checks.md` item 3: "`_STATUS.md` is byte-identical and its lifecycle state is unchanged".
- **What the standard and project-setup say.** Standard §8: "`INITIALIZED` means that the deliverable's selected production contract exists and validates". `project-setup` `method.md` (`882dfc71…15ac`) L158: scope-of-work "never edits `_STATUS.md`; recording `INITIALIZED` is a separate authorized status act". Its `contract.md` (`4115c777…7b4a`): scope-of-work INIT "may support `INITIALIZED` only after validated `SOW_V1` exists under the human-confirmed lifecycle policy".
- **Answer.** Writing a first SOW changes nothing in `_STATUS.md`. It makes the deliverable *eligible* for `INITIALIZED`; recording that state is a separate act needing its own authorization. The method does not require it.
- **PEC precedent.** `D-PEC-63` §3.2 ruled such an act separately: a generic TASK, after validator `PASS format=SOW_V1`, ran `write_status.sh … INITIALIZED "TASK+status-advance"`, and the scope-of-work prohibition was "honored, not overridden". The DEL-01-06 SOW revision left lifecycle unchanged. Option A makes no lifecycle change, and add-on S is the explicit question.
- **Consequence without S.** Both deliverables stay `OPEN` holding a valid `SOW_V1` contract, which is a valid format state (standard §7). `DEL-03-01`'s edges `[E-P81]`/`[E-P82]` stay unmet in the advisory `FULL_GRAPH` view. Their `SatisfactionStatus` cells stay `PENDING` either way.

### SCA-006 and the basis

- The accepted SCA-006 checkpoint-2 package (`D-PEC-97`) classes neither deliverable as affected. None of its 54 checkpoint-2 actions acts on `SOW-095`, `SOW-096`, DEL-02-08 or DEL-02-09; four mention `SOW-096` only as the ID after which new items append.
- Its PRD v2.4 candidate (H-01..H-17) changes none of the PRD text these contracts quote. Its revision-1.6 candidate leaves every quoted register cell, both objective statements and the §3 parser mapping note unchanged.
- SCA-006's §12 reliance gate requires "passing parser fixture suites". The `DEL-10-13` EXECUTION edges it plans would live in `DEL-10-13`'s register.
- SCA-006 group-2 amendment 1 (on `origin/main` since PR #940) carries a `projects/pec/AGENTS.md` correction of its Remaining sentences into the checkpoint-3 instruction tranche. DEL-02-09 CLM-012 quotes two other `AGENTS.md` phrases, about MEMORY. If checkpoint 3 lands first, question 4's check reruns those quotes.
- **If SCA-006 checkpoint 3 merges before this act,** the bound act stops on its pins, and question 4 applies.

### Findings beyond the brief (disclosed)

1. **Resolvable basis pin.** The sibling contracts pin `@3623b958b`, which does not resolve. These pin `@c9e5cd87d`, an ancestor of `origin/main`.
2. **Upstream contract gap (CON-001).** No parser can be implemented to a contract-obliged type until `DEL-01-01` is rebuilt. That argues for S2's `DEL-01-01` rebuild before P1 parser implementation.
3. **Missing registry edge (CON-002).** Neither register records an edge to `DEL-01-06`. This is a `dependency-extract` question.
4. **Scope gap on graph dependencies (CON-005).** A candidate for the next PEC scope change.
5. **Guard gaps (CON-003).** Graphs cite 9-character SHAs; the produced guard admits only 40- or 64-character digests.
6. **Method revision.** Root commit `ea5009d05` (wave-2A execution tranche) revised the graph template and workflow after the pin. It added the "A node awaiting a human decision is BLOCKED …" sentence and the "Current graph ref" and "Open deferrals" bullets, and left the six state tokens unchanged. DEL-02-08 CLM-013 now states this with both commits' hashes.
7. **Root notices already recorded.** D-GOV-46, D-GOV-47 and the review/CHECKING-reversal notice: none bears on the candidates.
8. **D-PEC-96 records.**
   - PR #940 put the owner-direction record (`D-PEC-96_AMEND_DIRECTION_2026-09-26.md`, `c506732e…d3b2`) on `origin/main`.
   - PR #941 published revision 4.
   - PR #946 recorded the ruling (A), at `f90320c1d`. Revision 2 cites the ruled revision 4 and the register state at `53145aaeb`, and depends on none of its identifiers.
9. **The graph's S3 wording.** "via preparation → Scope of Work": preparation is complete under `D-PEC-93`.
10. **D-GOV-48 (Root PR #942; `NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md`, `15ea36ee…e8e6`).**
    - Every scope item now needs a Package home. At `53145aaeb`, `validate_decomposition_registers.py --strict projects/pec/execution` reports **26 `XRG-013` warnings**, 0 errors, **exit 1**: the 18 OUT and 8 TBD items with a blank `PackageID`.
    - The notice records that the owner defers action on these while PEC is redeveloped.
    - This packet writes no register, so the output is identical before and after the act, and the verification row now requires exactly that (B2).
11. **Wave 3 (`NOTICE_2026-09-26_WORKFLOW_WAVE3_NITS.md`, `7fbbd1aa…7175`).** Its `write_status.sh` change (`pwd -P` for `--ruling`) leaves add-on S's postimages unchanged. The prototype ran with the `7a00a88df`, `8f9bd314c` and `53145aaeb` editions, and all three produced identical bytes. The owner defers action on the notice in PEC.
12. **C1 background.** The SCA-005 design note (§3.2) proposed extracting a MEMORY "row count", but the accepted `SOW-096` names only run-ID tokens, dates and link targets. Revision 2 follows the accepted text.

## Options

- **A — write the two exact contracts, no lifecycle change (recommended).** One act on **2 product paths**, both created. Nothing is modified or deleted, and no `_STATUS.md`, register, context or dependency file is touched. Add-ons S (question 2) and M (question 3) are independent.
- **A + S — as A, then the `OPEN → INITIALIZED` status act on both deliverables,** outside the scope-of-work run, after validator `PASS format=SOW_V1` and independent verification, on the D-PEC-63 §3.2 pattern. It adds 2 modified paths.
- **A + M** (combinable with S) — as A, plus two new `MEMORY.md` files at closeout. It adds 2 created paths.
- **Amend.** Write only one contract; resolve a CON item now; add a PEC self-ingest fixture over shared-method surfaces; bind D-PEC-96's identifiers once its registry act is applied; change a requirement.
- **Defer.** Nothing opens. X1 and P1 parser implementation wait.

A split that writes contracts without their open items is not offered: the method requires substantive ambiguity to be marked `CONFLICT`, not formatted away.

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once** under `chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`). Paths are relative to `projects/pec/execution/`.

| Item | Path | Preimage | Postimage SHA-256 |
|---|---|---|---|
| A | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` | absent (new file) | `03cce13f484a9b595b5162bd662af42bcd67aae37a8843304bf03cfbb3badc0a` |
| A | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` | absent (new file) | `aafb54fd6457f09da8304ead444686703d5f8d2c28f4c94ec4eab4d2737b188b` |
| S (if selected) | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_STATUS.md` | `d80800a48b45a43d641916bd5ee67c4b478e21538281b833e34dbc7cfe5f0eef` | `4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe` (`{D}` = 2026-09-26) |
| S (if selected) | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_STATUS.md` | `3e14313c78e2500cabbd3f4897f9095daabc75c6468169074cb4400f4667d768` | `e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056` (`{D}` = 2026-09-26) |
| M (if selected) | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/MEMORY.md` | absent (new file) | template instance with slots (below) |
| M (if selected) | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/MEMORY.md` | absent (new file) | template instance with slots (below) |

The A postimages are the exact candidate files, copied byte for byte into the run root as `candidates/…`. They have no date slot.

Read-only files the act re-verifies and never writes (SHA-256 at `53145aaeb`, equal at the pin `c9e5cd87d` for the first four):

- `_Decomposition/SOFTWARE_DECOMP.md` `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`;
- `_Decomposition/Deliverables.csv` `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a`;
- `_Decomposition/ScopeLedger.csv` `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df`;
- `docs/PRD.md` (relative to `projects/pec/`) `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32`;
- the two `_STATUS.md` preimages above;
- DEL-02-08 `Dependencies.csv` `c23cd711fc8762dbd4a8629ba277753544f9f9e91368f789140b040f94cf701e`;
- DEL-02-09 `Dependencies.csv` `41afd6dc44f21200f6b2a1c480e9175d98b64d49b12e638bca67edcd15168e4b`.

### Add-on S — status act (only if question 2 selects it)

**Actor and separation.** The scope-of-work run returns first; its `STATUS_POLICY=NO_STATUS_TOUCH` covers everything it does, and it writes no `_STATUS.md`. Afterwards, outside that run, WORKING_ITEMS dispatches one generic-shell TASK with no workflow selected. This follows `D-PEC-63` §3.2, which the history label `TASK+status-advance` records. Its allowed write targets are exactly the two `_STATUS.md` paths.

The TASK runs the commands below from the repository root. It runs each one only if `validate_scope_of_work.py` on that deliverable prints `PASS format=SOW_V1`, and only after the independent verifier has passed the act:

```text
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser" INITIALIZED "TASK+status-advance"
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser" INITIALIZED "TASK+status-advance"
```

**Slot rule.** The only varying bytes are the act date `{D}`, in `**Last Updated:** {D}` and the appended line `- {D} — State set to INITIALIZED (TASK+status-advance)`. `**Current State:**` becomes `INITIALIZED`, and every other byte is unchanged. The tool is forward-only.

### Add-on M — MEMORY files (only if question 3 selects it)

At the undertaking's closeout (graph node M1), WORKING_ITEMS creates the two `MEMORY.md` paths tabled above. Each is instantiated from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b…6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` table row:

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | First Scope of Work contract written under D-PEC-98 (graph node S3). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-98 ruling record> |
```

The slots `{D}`, `{PR}` and the two link targets are fixed at closeout. The verifier checks that no other byte departs from the template.

## Generation method (binding)

The A bytes come from one run of `apply_d98.py`, **SHA-256 `19c2ecb6bd40082c2397956dee2e0efb48b7a2aef5ec56e7498d4ed5e2fc419e`**. It is stdlib-only Python, prepared with CPython 3.13.7, and is copied byte for byte into the run root with the two candidate files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_INIT_D98_{D}/apply_d98.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_INIT_D98_{D}/candidates [--check-only]
```

**Failure semantics (C9).**

- **Preflight.** The script checks the two candidate hashes, that both targets and their temporary names are absent and their folders present, and the eight pinned hashes. Any failure exits 1 before any byte is written.
- **Write.** Each file is written to a temporary sibling (`…ScopeOfWork.md.d98tmp`), hash-checked, and renamed into place. If any step after the first write fails, the script deletes every temporary file and every target it created, and exits 1. Failures include an I/O error, a hash mismatch, a post-write inventory mismatch or a changed pinned file.
- **Result.** On exit 1, no target file and no temporary file remains. The script cannot revert changes made by another process; it detects them and fails.
- **Write set.** The script inventories every file under `projects/pec` (path and SHA-256) before and after the write. It requires the difference to be exactly the two targets, both created, with nothing modified or removed under `projects/pec`.
- **Second run.** It fails preflight. The script never touches `_STATUS.md`; S is a separate step by a separate actor.

The check aids, which are not bound:

| Aid | SHA-256 | Role |
|---|---|---|
| `test_apply_d98.py` | `ad7dce86b07d5c0fd36fb4ed46324b40be4d30559be2b0c18d258ffcc3e79a7a` | fault injection, five cases |
| `verify_d98_quotes.py` | `9cadc2c44359c9ea2d4d20c6a95122e9be02cf221612032f0c5bf6a06cadb745` | two-sided quote check |
| `verify_d98_state_claims.py` | `7bb9e6bbe3ad6e2bfa68c19c56c8b2e786b91f2e362c2a5e9e2fdddbc598b673` | commit-anchored claims |
| `run_d98_checks.sh` | `abc20da2d6fa8e3a590997ef6b15848449869fa23dd492ef5c41c110e9793b8d` | runs all checks |

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`. Record each command, exit code and output in the run root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | ruling and register row on fetched `origin/main`; `apply_d98.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `CHECK write set = grant`; `ALLOW` everywhere; otherwise stop and route (question 4 covers a revision-1.6 basis) |
| Contract validity | `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` ×2 | `PASS format=SOW_V1` ×2 |
| Checklist | `python3 tools/scope_of_work/derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, each twice | exit 0; 21 and 17 items in source order, bound to the postimage SHA-256; byte-identical to the prepared `54c84487…e2db` and `2f495a54…86f3` |
| Boundary owners (QA 21) | `python3 tools/scope_of_work/check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×2 | exit 0; 1 checked and 0 failing, each; the three `NOT_CHECKABLE` per-act clauses per contract resolved by hand as below |
| Quote fidelity | `python3 <run root>/verify_d98_quotes.py . <08 folder> <09 folder>` | `RESULT PASS 69/69` (candidate side and source side) |
| State claims | `python3 <run root>/verify_d98_state_claims.py .` | `RESULT PASS 44/44` (reads the named commits; independent of the working tree) |
| Lifecycle preserved (A) | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty under A; under S exactly the two tabled postimages |
| Strict registers (B2) | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution`, before and after the act | **exit code and output identical to the pre-act run**. At `53145aaeb` that run exits **1** with 0 errors and **26 pre-existing `XRG-013` warnings** (D-GOV-48; owner-deferred; finding 10). A new finding, or a change in count or exit code, fails the check |
| Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | exit 0 each; output identical before and after |
| Containment | `git diff --name-status origin/main...HEAD` | the two created contracts; S's two `_STATUS.md` and M's two `MEMORY.md` if selected; the run root and HELP_HUMAN's records under `execution/_Coordination/**`; nothing else |
| Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. The act changes no decomposition truth, register or topology.

QA 21 hand resolution (the per-act clauses the tool reports as `NOT_CHECKABLE`):

| Contract | Requirement → owner | Cited claim |
|---|---|---|
| DEL-02-08 | REQ-009 → `DEL-04-05`; REQ-010 → `DEL-01-03`; REQ-011 → `DEL-04-03` | CLM-011 |
| DEL-02-09 | REQ-007 → `DEL-04-05`; REQ-008 → `DEL-01-03`; REQ-009 → `DEL-04-03` | CLM-010 |

In each case the cited claim names that owner.

### Independent verifier

The method's independent verification is a separate `MODE=VERIFY` run, read-only on production content. Revision 1 received one on PR #944: FAILED on claim grounding, with schema and mechanical checks passing. Revision 2 needs a fresh one, by a TASK that authored nothing, before the owner rules, and again at the act. It returns a verdict file; defects return to the author, and the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`; the run-root script hashes as bound; the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **`MODE=VERIFY`.** The mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21), including the QA 21 hand resolution.
4. **Semantics.**
   - Every claim is true at the commit it names, or at the observation commit `53145aaeb` where it names none. `verify_d98_state_claims.py` covers the mechanical part; the verifier also reads the rest.
   - Every quotation is verbatim.
   - No requirement adds scope beyond `SOW-095`/`SOW-096`, the register rows and PRD v2.3.
   - Every open item is marked `TBD`/`CON`.
   - The `OBJ-002` qualification is no stronger than the §3 mapping note.
   - No D-PEC-96 identifier is relied on, and no Remaining section is read.
5. **Containment and lifecycle.** As in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act and the checks, and M if selected. S, if selected, is one separate generic-shell TASK as described above. The manager runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/SOW_INIT_D98_{D}/`, in the default-writable fence, holds:
  - `apply_d98.py` (exact bytes), `candidates/`, the check aids and all check outputs;
  - `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md`;
  - `VERIFIER_VERDICT_NN.md`.

  No `_run_records/` entry is written in either deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under D-PEC-88. `_Evaluation/**`, registers and dependency files stay closed.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning, unless the owner states otherwise. Role identity is instruction-asserted.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the script leaves no target or temporary file (C9). If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR removes the two created contracts, and M's two files if created. If S ran, it restores the two `_STATUS.md` preimages tabled above. `write_status.sh` blocks backward transitions, so file revert is the only walk-back (`D-PEC-63` §6). History is preserved.
  - The ruling record and register row are never reverted; a rollback is recorded as its own register row and record.
  - The run root stays as non-current evidence, with a rollback note.
  - No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + S, A + M, A + S + M or an amendment, grants none of the following:

- any `v2/**`, `software-workflow.json` or `docs/PRD.md` write, or any source, fixture or test file (the fixture suites are X1's);
- any `_Decomposition/**` or `_ScopeChange/**` write, or any register write: no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `Dependencies.csv` or `_DEPENDENCIES.md` change, no dependency edge, and no action on the D-GOV-48 warnings;
- any `_CONTEXT.md`, `_REFERENCES.md` or `_SEMANTIC.md` write, or any other deliverable's file;
- any lifecycle change other than add-on S's single `OPEN → INITIALIZED` per deliverable, and none under A. No `## Remaining` entry is written or read;
- `CHECKING`, `ISSUED`, artifact acceptance, a REVIEW gate act, or any readiness or reliance claim. `CHECKING` is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it;
- a registry, profile or D-PEC-96 act, or a resolution of any `CON` item;
- a Task Management disposition, an audit run or a pointer move;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- a schedule reading: blocker output stays advisory.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**.
2. **Add-on S — record `INITIALIZED` for both deliverables,** by a separate TASK outside the scope-of-work run, after the contracts validate and pass independent verification.
   - Recommendation: **S**. Standard §8 defines `INITIALIZED` as exactly this condition, and D-PEC-63 ruled the same act for all seven sibling parsers.
   - Choose "A without S" to keep this act lifecycle-neutral.
   - Without an answer, **no status act is performed**.
3. **Add-on M — MEMORY files.** Create both `MEMORY.md` files at closeout (recommended), or record the run only in the graph and central receipt. `projects/pec/AGENTS.md` allows either on your decision.
4. **Basis re-pin if SCA-006 checkpoint 3 lands first.** `apply_d98.py` would then stop on its pinned register and PRD hashes. **Recommended:** the same ruling covers the following bounded mechanical re-pin; otherwise the packet is re-presented.
   - **What moves in each candidate.**
     - The frontmatter `decomposition_basis` commit becomes the SCA-006 checkpoint-3 acceptance commit.
     - In the Purpose, the paragraph beginning "The accepted basis is …" is restated for revision 1.6: revision, accepting act and date, pin commit, and the three register and PRD hashes at the new pin.
     - In the "**Observation commit.**" paragraph, the clause stating that the registers and PRD at `53145aaeb` equal the pin becomes a statement that they differ, and which quoted loci were re-verified.
     - No other byte moves.
   - **What stays, by design.**
     - The observation commit `53145aaeb` and every commit-anchored claim remain true as observations.
     - The "revision 1.5" and "PRD v2.3" mentions elsewhere stay. Examples are the ledger row's `SourceRef` "PEC-RCN-002 (PRD v2.3)", the §7.1 and PEC-RCN-002 quotations labelled PRD v2.3, "`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 … at `53145aaeb`", and the SCA-005 history. Each is either verbatim accepted text or an observation at a named commit.
     - Preparation found every quoted locus unchanged in the revision-1.6 candidate.
   - **Condition.** `verify_d98_quotes.py`, rerun against the new tree, must still pass every check. If any quoted locus changed, the re-pin is void and the packet is re-presented.
   - **Re-binding the act script.**
     - A new `apply_d98.py` is generated by changing only `TARGETS` (the two new candidate hashes) and the four register and PRD entries of `PINNED` (their hashes at the new pin). The four deliverable-file pins stay.
     - Its hash, the new candidate hashes and a word diff against these candidates go in the run root.
     - `verify_d98_state_claims.py` gains the new pin as a second `PIN` with its register hashes, and keeps every existing check.
     - The independent verifier confirms that the word diff touches only the three places above. It also confirms that the new `TARGETS`/`PINNED` values equal the recomputed hashes.
5. **CON-005 routing (work-graph dependencies).** Leave it open and route it to the next PEC scope change (recommended), or direct now, by amendment, whether DEL-02-08 extracts node-ID references from "Needs" cells.
6. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran in `mktemp -d` directories in the session scratchpad, outside the checkout:

- `s3base.*` are `git archive` exports at `7a00a88df`, `8f9bd314c`, `5bbc9de22` and `53145aaeb` (revision 2 was first checked at `5bbc9de22`; PR #946 merged during the revision, so every check was rerun at `53145aaeb`);
- `s3proto.*` is where the revision-1 candidates were authored;
- `s3gitmeta.*/repo` is a `git clone --shared --no-checkout`, last detached at `53145aaeb`. It reads the repository's objects and writes nothing to the repository.

Interpreter: Python 3.13.7 (CPython); local date 2026-09-26. Nothing was written to the checkout or its repository except `git fetch`. `verify_d98_state_claims.py` was also run read-only against the checkout's object store.

Final run (`evidence/RUN_D98_CHECKS_at_53145aaeb.out`, from `run_d98_checks.sh`), on the final candidates at `53145aaeb`:

| Command (scratch) | Exit | Result |
|---|---|---|
| `validate_scope_of_work.py` ×2 | 0 / 0 | `PASS format=SOW_V1`; JSON `issues: []` |
| `derive_review_checklist.py` ×2, each twice | 0 | 21 / 17 items, source order, bound to the candidate SHA-256; reruns byte-identical |
| `check_boundary_owner_resolution.py --show-not-checkable` ×2 | 0 / 0 | 1 checked, 0 failing each; three `NOT_CHECKABLE` each (hand-resolved) |
| `verify_d98_quotes.py` | 0 | `RESULT PASS 69/69` (two-sided) |
| `verify_d98_state_claims.py` | 0 | `RESULT PASS 44/44` |
| ID-collision scan (QA 19) | — | 106 / 90 local definitions; no undefined or quoted-upstream local ID |
| `validate_decomposition_registers.py --strict` before / after | 1 / 1 | 0 errors, 26 `XRG-013` warnings (pre-existing, D-GOV-48); output identical |
| `validate_pec_loop_receipts.py --repo-root .` before / after | 0 / 0 | output identical |
| `harness.py self-check` before / after | 0 / 0 | output identical |
| `git diff --check` (intent-to-add) | 0 | clean |
| containment | — | exactly the two new `ScopeOfWork.md`; both `_STATUS.md` blobs unchanged |
| `pec_reliance_hold.py … exact-correction-preparation` ×6 | 0 ×6 | `ALLOW` |
| add-on S prototype, `write_status.sh` edition `1857ad59…97bc` (`53145aaeb`) | 0 ×2 | postimages as tabled; identical to the `7a00a88df` and `8f9bd314c` editions |
| `apply_d98.py --check-only`, apply, rerun on a fresh export | 0 / 0 / 1 | write set = grant; 2 created, 0 modified, 0 removed; rerun refuses; diff against the export is exactly the two files |
| `test_apply_d98.py` | 0 | `RESULT PASS 5/5`: rename failure on the second target; post-write modified file; post-write extra file (each exit 1, no target or temporary left); changed pin (preflight exit 1); check-only/apply/rerun |
| negative controls (`evidence/negative_controls.out`) | 1 each | matrix row removed: validator `FAIL format=INVALID`, checklist refuses with no artifact (QA 18); source-side mutation: 3 checks fail; candidate-side mutation (dropped phrase, reintroduced "At the basis"): 2 checks fail |

Scratch artifacts, in the preparer's `s3/` folder and listed with hashes in `s3/SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` | `03cce13f484a9b595b5162bd662af42bcd67aae37a8843304bf03cfbb3badc0a` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` | `aafb54fd6457f09da8304ead444686703d5f8d2c28f4c94ec4eab4d2737b188b` |
| `apply_d98.py` (bound) | `19c2ecb6bd40082c2397956dee2e0efb48b7a2aef5ec56e7498d4ed5e2fc419e` |
| `verify_d98_quotes.py` / `verify_d98_state_claims.py` / `test_apply_d98.py` / `run_d98_checks.sh` | `9cadc2c4…b745` / `7bb9e6bb…b673` / `ad7dce86…9a7a` / `abc20da2…b8d` |
| `evidence/checklist_DEL-02-08.json`, `evidence/checklist_DEL-02-09.json` | `54c84487…e2db`, `2f495a54…86f3` |
| `evidence/RUN_D98_CHECKS_at_53145aaeb.out` and the other outputs; `evidence/BASIS_SHA256_at_7a00a88df.txt` (revision-1 basis list) | in `SHA256SUMS` |

Basis at `53145aaeb` (changed since revision 1 marked †):

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…` / `1a13a5b0…` / `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` (equal at `c9e5cd87d`) | `dc2b8479…9660` / `b8628fc4…3d65a` / `83152a94…9df` / `2a194105…eb0df` |
| `docs/PRD.md` (v2.3; equal at `c9e5cd87d`) | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| SCA-005 `Propagation_Plan.md` / `Impact_Assessment.md` / feed-model design note | `50cd0b1d…1350` / `0bcbe9bd…39bf` / `4b9ccb9f…12da` |
| D-PEC-96 proposal, revision 4 † / amend direction † / ruling † / `_REGISTER.md` † | `4506597b…180e` / `c506732e…d3b2` / `852057f0…399e` / `01b8d184…1a14` |
| Work graph `HELP-HUMAN-PEC-20260925-POST-SCA005` † | `a203523d57b2f4337bd83cb3ad49d2e254a52797f911cdb014b01ef438296720` |
| Upstream SOWs DEL-01-01 / DEL-01-03 / DEL-01-06 | `43f1f57a…0170` / `986ef155…6341` / `5fdcfd96…a2fa8` |
| `construct-local-work-graph` template / `WORKFLOW.md` (at `c9e5cd87d`: `4411d0c2…2261` / `24268f35…4525`); `MEMORY_TEMPLATE.md` | `5661c609…6fa6` / `3e197c9d…9dc3`; `5a9564f4…6a5a` |
| `project-setup` `method.md` † / `contract.md` †; `write_status.sh` † | `882dfc71…15ac` / `4115c777…7b4a`; `1857ad59…97bc` |
| `validate_decomposition_registers.py` † | `869df1d5…57ee` |
| Notices: D-GOV-48 † / wave 3 † | `15ea36ee…e8e6` / `7fbbd1aa…7175` |
| Produced guard `v2/src/pec_v2/core/content_minimal_guard.py` (unaccepted) | `740a4a74…19ee9` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d931…41cbc` / `b1712e4b…cd0e` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node S3 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
