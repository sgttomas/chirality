# D-PEC-98 — First Scope of Work contracts for DEL-02-08 (work-graph parser) and DEL-02-09 (MEMORY run-index parser) — proposal

Status: **PROPOSAL / AWAITING_RULING**. **The number D-PEC-98 is provisional**: it becomes final only when this packet is published with its register row. Prepared by a TASK (Type 2) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3) for the PEC loop, 2026-09-26 (session date), from brief `S3_FIRST_SOWS_PROPOSAL.md` (SHA-256 `ef12b7408b68edb283055200de424169878fd3d122df43892d099432a8ea537a`). No earlier direction approves this file. It performs no production act: no tracked file was edited, and every prototype ran on scratch copies only. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `origin/main` `8f9bd314c` the register has no D-PEC-98 row and no file under `projects/pec` carries the number; this packet uses the number its brief assigned, provisionally. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-98_first_sows_del_02_08_09_proposal_2026-09-26.md`.

The act it asks for is bounded: create two new files, `DEL-02-08/ScopeOfWork.md` and `DEL-02-09/ScopeOfWork.md`, with the exact bytes below. The lifecycle transition that PEC has paired with first contracts before is **not** part of option A; it is offered separately as add-on S (question 2).

## Provenance

- **Owner acts relied on.**
  - The owner's 2026-09-25 steering, recorded in `D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…5a6b`): "You can continue with all the open work you identified." HELP_HUMAN's work graph turns it into node S3, "First SOWs for DEL-02-08 and DEL-02-09 … via preparation → Scope of Work (WORKING_ITEMS)", now `READY — packet preparation; U1 and R1 are met` (`WORK_GRAPH.md` `24901c3a…41be` at `origin/main`).
  - SCA-005 checkpoint 2 (`D-PEC-92`, 2026-09-25) accepted `Propagation_Plan.md` (`50cd0b1d…1350`). Its §B4 says: "The two new deliverables receive first SOWs through the ordinary preparation → Scope of Work path", and carries forward the guard cases these contracts must address. Its §B7 places the P1 fixture strategy "inside the DEL-02-08/09 and DEL-02-03 SOWs". Checkpoint 3 accepted revision 1.5 as `current_basis`.
  - `D-PEC-93: A.` (`D-PEC-93_RULING_2026-09-25.md`, `ffb0b582…3709`) created both folders with the `preparation` skill. `D-PEC-95` (ruled P + R; `51dceb71…`) re-pinned the metadata the contracts read.
  - `D-PEC-63` (RULED 2026-07-25, `0241db82…`) is the precedent for first-contract authoring and for a separately ruled `OPEN → INITIALIZED` status act. `REV_DEL-01-06_2026-08-04_1113` is the precedent for a SOW act that leaves lifecycle unchanged ("Gate 5/lifecycle: `HOLD` / `INITIALIZED`, unchanged").
  - `D-GOV-16` (RULED APPROVED 2026-07-12) ratified `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`: "New deliverables use `SOW_V1`" (§7).
- **Fence.** `projects/pec/AGENTS.md` (`c9d3b44d…197a`) §"Write Scopes And Fences": only `execution/_Coordination/**`, `AGENTS.md` and the one-time STATUS pointer are default-writable; every other write under `projects/pec` needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. No earlier ruling opens the two target paths: `D-PEC-93` opened folder creation only, and `D-PEC-95` opened `_CONTEXT.md` and `_REFERENCES.md` anchors, not `ScopeOfWork.md`.
- **Source state.** Every hash below was read at `origin/main` **`8f9bd314c5f2499e6faf5bf4bdce917927e8185e`** (PR #939) after `git fetch`, from `git archive` exports. Preparation began at `7a00a88df` (PR #937). The later commits touch no basis file except `tools/scaffolding/write_status.sh`, a CHECKING-reversal change that leaves `OPEN → INITIALIZED` unchanged; add-on S's prototype gives identical postimages with either edition. Every check was rerun at `8f9bd314c` on the final candidates. The checkout was not changed by this TASK; during preparation it moved, outside this TASK, from branch `claude/pec-graph-cp2-d96` to `claude/pec-owner-directions-20260926` (`a07f62190`), whose unmerged commits are not relied on as rulings (see "Findings", item 8).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`) was run from `projects/pec` with `--operation exact-correction-preparation` on all four possible targets (both `ScopeOfWork.md` and both `_STATUS.md`): `{"operation": "exact-correction-preparation", "status": "ALLOW"}`, exit 0, ×4.

## Method

- **Workflow.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`eac61b43…d102`; `schema: chirality-method-index/v1`, precedence project → user → bundled; no project or user workflow of that name exists). Files: `WORKFLOW.md` `d616865a5cbfa84b47fd509d2910826106db57473543a86d067ddc3edf6fbd8b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `a082f1af…5145`, `resources/tools.md` `2bbb55cc…0f3f`, `resources/checks.md` `fbb2c8eb…76b8`, `resources/representation-migration.md` `43459252…6729` (not loaded; conversion only).
- **Mode.** `MODE=INIT`, `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, `RENDER_HTML=false`. INIT is source-grounded authoring: no conversion, claim map, parity or finalizer.
- **Transition contract.** The workflow's "active SOW_V1 transition contract" is `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (`26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`), ratified by D-GOV-16 (published at `7584718aa`). Its banner makes the text effective "IF AND ONLY IF D-GOV-16 IS RULED APPROVED"; the governance register records that ruling.
- **`preparation`.** Not re-run. The folders and control files already exist, created under `D-PEC-93` by the `preparation` skill, so the method's "preparation → Scope of Work" path is at its second step.
- **Tools** (`tools/scope_of_work/`, unchanged at `8f9bd314c`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, with `common.py` `61a34722…0389` and `id_catalog.json` `7a1f8a12…757`.

## What preparation found

### The two candidates

| | DEL-02-08 Work-graph parser | DEL-02-09 MEMORY run-index parser |
|---|---|---|
| Scope item / objectives | `SOW-095` / `OBJ-001`, `OBJ-002` (indirect, §3 mapping note) | `SOW-096` / `OBJ-001`, `OBJ-002` (indirect; `OBJ-002` leg stated as thin) |
| Basis pin | `SOFTWARE_DECOMP.md@c9e5cd87d` (checkpoint-3 acceptance commit, revision 1.5; resolves on `origin/main`) | same |
| Definitions | 3 OUT, 18 CLM, 20 REQ, 21 AC, 20 VER, 12 AX, 7 TBD, 5 CON | 2 OUT, 17 CLM, 16 REQ, 17 AC, 16 VER, 11 AX, 7 TBD, 4 CON |
| Outputs | parser; pinned FC-1/FC-2/FC-3 fixture suites; synthetic grammar-edge fixtures and test suite (the register's three-part artifact list) | parser; fixture test suite for the table, bullet and dated-heading forms |
| Size / SHA-256 | 255 lines, `b28cf13d93851dc875575dafd759171205a75bc4bb63ef67e103fa2094d10b24` | 228 lines, `c9705ca28da82687e82bccdeb1bca5e271833d267c4afe23526965c4e13c7bd9` |

Both follow the sibling PKG-02 contracts' form (`DEL-02-01`, `-03`, `-04`): the same frontmatter keys, the six required headings, the "Identity of record / Placement in the work graph / Boundaries" subsections, qualified upstream IDs, one acceptance criterion per matrix row, and a closing human-review criterion for objective traceability.

**What the contracts require, in brief.**

- **DEL-02-08.** Discovery only at the canonical path and only where the loop's registered feed profile declares the work-graph surface; integration ref by default, branch refs opt-in and labelled unintegrated; read-only plumbing, no fetch. Extraction of exactly the eight `SOW-095` fields under a declared, versioned grammar. Node states only from the method's closed vocabulary (`PLANNED`, `READY`, `ACTIVE`, `BLOCKED`, `UNCERTAIN`, `COMPLETE`); an unknown token becomes a limitation, never coerced and never copied. Declared activity, never liveness or completion. The run identity only from the declared field, never from the folder name. PR numbers resolved to local merge commits or "unresolved locally", never guessed or fetched, and no SHA padded. Explicit limitations with parse outcomes, no prose in the output, provenance per fact, no writes, determinism. No record-tier type of its own and no other entity. A template-form boundary exclusion naming every sibling and downstream owner.
- **DEL-02-09.** Reading only where the profile declares the MEMORY run index; a missing `MEMORY.md` or `## Runs` is a stated coverage limit, never nonconformance. Three declared grammars (template table, bullet, dated heading). Extraction of exactly run-ID tokens, dates and link targets. A run token only where the grammar fixes its position, otherwise "run-ID unavailable". Join evidence only: no join, no RunRecord, no run-outcome claim. The same limitation, content-minimal, provenance, read-only, determinism, typing and boundary rules as DEL-02-08.

**Fixture classes (brief item).** Both contracts state the SCA-005 §B7 classes assigned to node X1, quoting §B7 verbatim: **FC-1 receipt present** (Piping `PIPING_LINTER_SCOPE_20260923`), **FC-2 evidence-only** (Piping `PIP-DEC025-BASELINE-2026-09-23`) and **FC-3 no AgentRuns record** (App `APP-REPLAY-BOUNDARY-2026-09-23`). They are golden-by-reference `(commit, path, blob)` fixtures pinned at `d61981ee2`, with content-minimal goldens and nothing copied into PEC's tree, plus synthetic grammar-edge fixtures. DEL-02-08 REQ-016/017 bind the three classes and six synthetic cases. DEL-02-09 REQ-014 exercises the bullet and dated-heading forms from those classes and the template table synthetically, because the corpus holds no table instance. The fixtures themselves remain X1's, under a later v2 packet. All five pinned blobs named in IA §9.3 resolve at `d61981ee2` and are unchanged at `origin/main`.

**Open decisions recorded, not assumed.**

| Contract item | What is open | Where it resolves |
|---|---|---|
| 08 CON-001 / 09 CON-001 | Upstream typing. The accepted `DEL-01-01` contract (`43f1f57a…0170`) obliges exactly fourteen types, with no WorkGraph/WorkNode, and admits only JSON evidence into RunRecord (`DEL-01-01/REQ-006`). Revision 1.5 says otherwise. | `DEL-01-01` rebuild, graph node S2; whether implementation waits for it is a graph/owner ordering choice |
| 08 CON-002 / 09 CON-002 | Discovery basis. No accepted registry declares feed profiles; `DEL-01-06`'s contract is strict version-1, and no dependency row links either parser to `DEL-01-06`. | `D-PEC-96` ruling, then the `DEL-01-06` rebuild (S2); edge question for `dependency-extract` |
| 08 CON-003 / 09 CON-003 | Guard admission. Node states, node IDs, run tokens, DEL bindings, PR numbers, dates and abbreviated SHAs are outside the produced guard's classes (`OPEN`..`ISSUED`; 40/64-hex SHAs). These are `DEL-01-03/CON-001` cases (the SCA-005 §B4 carry-forward). | `DEL-01-03` / `DEL-01-01` under their own packets |
| 08 CON-004 | FX-PEC-0. §B7 lists it under `remaining-loop`; the register's artifacts do not; `D-PEC-94` changed PEC's shape, and the revision-4 direction drops `remaining-loop`. No FX-PEC-0 output and no Remaining-reading fixture. | X1 / `DEL-10-10` |
| 08 CON-005 | Work-graph dependencies. PRD §7.1 and the `SOW-015` Notes cell route Markdown graph dependencies through `SOW-095`, but its field list does not name them, and in graphs they live in prose "Needs" cells. No DependencyEdge. | scope-change or owner ruling (question 5) |
| 09 CON-004 | Run tokens in dated headings. `SOW-096` puts them in scope, but observed headings declare no token position and are otherwise description. A token is emitted only where a declared grammar fixes it. | method or scope decision |
| TBD-001..007 (each) | ResponsibleParty; exact grammars; PR-resolution syntax; profile identifiers (pending D-PEC-96); ref selection and the template's new "Current graph ref" bullet (08); golden format and threshold; abbreviated SHAs (08); MEMORY folder pattern, mixed-form files and join ownership (09) | production within the REQs, or the named owner |

### Dependencies on D-PEC-96 (without presuming its ruling)

- **State of D-PEC-96.** At `origin/main` `8f9bd314c` the register row reads `PROPOSAL / AWAITING_RULING`, and the published text is revision 3 (`2f7d9875…afc4`). HELP_HUMAN reports an owner amend direction of 2026-09-26: "revision 4: drop remaining-items and remaining-loop". It followed the owner's question: "Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them." The record of that direction is on the unmerged branch `claude/pec-owner-directions-20260926` (`D-PEC-96_AMEND_DIRECTION_2026-09-26.md` at `c0a668181`), not on `origin/main`. Revision 4 itself is unpublished. **Neither revision is ruled**, and this packet presumes no ruling.
- **The revision-4 vocabulary the contracts cite.** `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, all at version 1. The `status-remaining` surface is removed, and PEC's proposed row is `shared-dev-loop` live with the other two historical. The contracts state this in DEL-02-08 CLM-009 and DEL-02-09 CLM-008, labelled unruled and not relied on. They name the published revision 3 as the register's current text.
- **What the contracts assume.** Only that a loop's registry row may declare the work-graph and MEMORY run-index surfaces, as PRD v2.3 PEC-RCN-002 and §16.3 already say. They depend on no D-PEC-96 identifier; the identifiers stay TBD-004 (08) and TBD-003 (09).
- **Remaining sections.** No Remaining-reading dependency exists.
  - PRD v2.3 §7.1 makes "remaining items" "a per-loop optional field, read only where the loop's feed profile declares it", on the Package/Deliverable census read from `_STATUS.md`.
  - That field is `DEL-02-01`'s feed, not a work-graph or MEMORY surface. New claims DEL-02-08 CLM-018 and DEL-02-09 CLM-017 say so.
  - **The parsers do not read `## Remaining` sections**: 08 REQ-001 and REQ-015, 09 REQ-001 and REQ-013, each with a matching acceptance criterion and verification method.
  - Their discovery depends on no profile or surface that reads Remaining sections. Revision 4 contains none, and neither contract needs `remaining-loop` or `remaining-items`.
  - Both contracts take no FX-PEC-0 output and no Remaining-reading fixture (08 CON-004, 09 CLM-013). The §B7 quotation that names FX-PEC-0 under `remaining-loop` stays verbatim as accepted text.
- **Under each outcome, the contract bytes stay valid:**
  - **Ruled as revision 4 (A).** `shared-dev-loop` covers both surfaces and PEC's row declares it live, so PEC's own graph and DEL-01-03's `MEMORY.md` fall inside discovery.
  - **Ruled otherwise, or amended again.** Whatever profile declares the two surfaces applies; if none does for a loop, the parsers discover nothing there and report that no declaration exists (REQ-001).
  - **Deferred.** No registry declares anything, so production discovery is empty until a registry version-2 act. Tests use fixture registries (VER-001).
- **Ordering.** This packet does not need D-PEC-96 ruled first; the graph records that S3 is not blocked on S2 or G1. Implementation and X1 will need the registry and the `DEL-01-06` rebuild. CON-002 stays open until then.
- **"At the basis" wording.** The sentences stating D-PEC-96's status are written as of the basis, so a later ruling or revision makes them dated, not false.

### Lifecycle: what the method does to `_STATUS.md`

- **The method never touches it.**
  - `WORKFLOW.md`: "Do not modify `_STATUS.md`, lifecycle state, underscore control files, …"
  - `resources/brief.md`: `STATUS_POLICY` defaults to `NO_STATUS_TOUCH`, and "`ADVANCE_ON_PASS` additionally requires the brief to authorize `_STATUS.md` writes".
  - `resources/tools.md`: the tools "do not modify lifecycle state".
  - `resources/checks.md` item 3: "`_STATUS.md` is byte-identical and its lifecycle state is unchanged".
- **What the standard and project-setup say.** Standard §8: "`INITIALIZED` means that the deliverable's selected production contract exists and validates", and "`_STATUS.md` remains the sole lifecycle authority". `project-setup` `method.md` (`e375104d…`) L157: scope-of-work "never edits `_STATUS.md`; recording `INITIALIZED` is a separate authorized status act". Its `contract.md` says scope-of-work INIT "may support `INITIALIZED` only after validated `SOW_V1` exists under the human-confirmed lifecycle policy".
- **Answer.** Writing a first SOW changes nothing in `_STATUS.md`. It makes the deliverable *eligible* for `INITIALIZED`; recording that state is a separate act that needs its own authorization. The method does not require that act.
- **PEC precedent.**
  - `D-PEC-63` §3.2 ruled such an act separately. After validator `PASS format=SOW_V1`, a generic TASK ran `tools/scaffolding/write_status.sh "<DEL_PATH>" INITIALIZED "TASK+status-advance"`. It "honored, not overridden" the scope-of-work prohibition. All seven sibling parsers reached `INITIALIZED` that way.
  - The DEL-01-06 SOW revision left lifecycle unchanged.
  - This packet follows both: option A makes no lifecycle change, and add-on S is the explicit question.
- **Consequence without S.** Both deliverables stay `OPEN` holding a valid `SOW_V1` contract. That is a valid format state (standard §7, "One valid `ScopeOfWork.md` only → `SOW_V1`"). `DEL-03-01`'s edges `[E-P81]`/`[E-P82]` (`RequiredMaturity` `INITIALIZED`) stay unmet in the advisory `FULL_GRAPH` blocker view. Their `SatisfactionStatus` cells stay `PENDING` either way, because no register is written.

### SCA-006 and the basis

- The accepted SCA-006 checkpoint-2 package (`D-PEC-97`) classes neither deliverable as affected. None of its 54 checkpoint-2 actions acts on `SOW-095`, `SOW-096`, DEL-02-08 or DEL-02-09; four mention `SOW-096` only as the ID after which new items append.
- Its PRD v2.4 candidate (H-01..H-17) changes none of the PRD text these contracts quote (PEC-RCN-002, the §7.1 WorkGraph/WorkNode and RunRecord rows, PEC-K-10). Its revision-1.6 candidate (`CP2_CANDIDATE/_Decomposition/`) leaves every quoted register cell unchanged: the `SOW-095`/`SOW-096` rows, the DEL-01-01/02-05/02-08/02-09 rows and the ContextBudgetQA rows compared identical. The objective statements and the §3 parser mapping note are also unchanged; only the objective-side mapped-item lists grow.
- SCA-006 adds a §12 reliance-advertisement gate requiring "passing parser fixture suites". Its plan §B2 foresees `DEL-10-13` EXECUTION edges to "the PKG-02 parser deliverables whose fixture suites the gate composes". Those edges would live in `DEL-10-13`'s register and impose nothing on these contracts.
- **If SCA-006 checkpoint 3 merges before this act,** `current_basis` becomes revision 1.6 and PRD v2.4. The bound act then stops on its pinned hashes. Question 4 asks whether a bounded mechanical re-pin may follow.

### Findings beyond the brief (disclosed)

1. **Resolvable basis pin.** The sibling contracts pin `@3623b958b`, which does not resolve in this repository (SCA-005 §B4 housekeeping, 16 contracts). These candidates pin `@c9e5cd87d`, which resolves and is an ancestor of `origin/main`.
2. **Upstream contract gap.** The typing gap of CON-001 means neither parser can be implemented to a contract-obliged type until `DEL-01-01` is rebuilt. That argues for S2's `DEL-01-01` rebuild before P1 parser implementation. It is a graph consequence, not a change to S3.
3. **Missing registry edge.** Both parsers depend on the registry declaration by the scope text itself, but neither register records an edge to `DEL-01-06`. This is a `dependency-extract` question, left to its owner.
4. **Scope gap on graph dependencies (CON-005).** A candidate for the next PEC scope change.
5. **Guard gaps (CON-003).** They include abbreviated SHAs. Graphs cite 9-character SHAs, and the produced guard admits only 40- or 64-character digests.
6. **Method revision.** The Root wave-2A tranche `ROOT-WORKFLOW-WAVE2A-EXECUTION-20260926` added "Current graph ref" and "Open deferrals and follow-ups" bullets to the graph template and left the state vocabulary unchanged (commit `ea5009d05`). DEL-02-08 records the ref bullet as TBD-005 and reads neither bullet's prose.
7. **Later Root notices.** `NOTICE_2026-09-26_DEPENDENCY_SCHEMA_D-GOV-46.md`, `…_DECOMP_RULINGS_D-GOV-47.md` and `…_REVIEW_SPEC34_REVERSAL.md` arrived during preparation. None bears on these candidates. The candidates cite `_DEPENDENCIES.md`'s existing `FULL_GRAPH` mode, which D-GOV-46 preserves.
8. **Unmerged owner-direction record.** The D-PEC-96 revision-4 direction (above) is recorded on branch `claude/pec-owner-directions-20260926` (`c0a668181`), not on `origin/main`. `projects/pec/AGENTS.md` says to rely on an owner act only once its record is observable on `origin/main`. The contracts therefore cite the revision-4 vocabulary as unruled context, at HELP_HUMAN's direction, and depend on none of it. The same branch records SCA-006 checkpoint-3 directions, which this packet also does not rely on.
9. **The graph's S3 wording.** It says "via preparation → Scope of Work". Preparation is complete under `D-PEC-93`, so only the Scope of Work step remains.

## Options

- **A — write the two exact contracts, no lifecycle change (recommended).**
  - One act on **2 product paths**, both created. Nothing is modified or deleted, and no `_STATUS.md`, register, context or dependency file is touched.
  - Add-ons S (question 2) and M (question 3) are independent.
- **A + S — as A, then the `OPEN → INITIALIZED` status act on both deliverables,** by `write_status.sh` after independent validator `PASS format=SOW_V1`, on the D-PEC-63 §3.2 pattern. It adds 2 modified paths (`_STATUS.md` ×2).
- **A + M** (combinable with S) — as A, plus two new `MEMORY.md` files from the template at closeout, so the undertaking's M1 node can index this run. It adds 2 created paths.
- **Amend.** The owner changes the scope and the packet is re-prepared. Examples:
  - write only one contract;
  - resolve a CON item now (for example, have DEL-02-08 extract node-ID references from "Needs" cells, CON-005);
  - add a PEC self-ingest fixture over PEC's shared-method surfaces as an output (never a Remaining-reading one);
  - bind D-PEC-96's identifiers once it is ruled;
  - change a requirement or criterion.
- **Defer.** Nothing opens.
  - The two deliverables stay `OPEN` without contracts.
  - X1 (fixtures) and any P1 parser implementation wait, because the graph orders X1 after S3.
  - Waiting until the `DEL-01-01` and `DEL-01-06` rebuilds would remove CON-001 and CON-002 from the contracts instead of recording them. That is a legitimate choice, but it trades a contract now for a cleaner one later.

A split that writes contracts without their open items is not offered: the method requires substantive ambiguity to be marked `CONFLICT`, not formatted away.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once** under `chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`). Paths are relative to `projects/pec/execution/`.

| Path | Preimage | Postimage SHA-256 |
|---|---|---|
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` | absent (new file) | `b28cf13d93851dc875575dafd759171205a75bc4bb63ef67e103fa2094d10b24` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` | absent (new file) | `c9705ca28da82687e82bccdeb1bca5e271833d267c4afe23526965c4e13c7bd9` |

The postimages are the exact candidate files, copied byte for byte into the run root as `candidates/…` (see "Preparation evidence"). They have no date slot.

Read-only files the act re-verifies and never writes (SHA-256 at `8f9bd314c`):

- `_Decomposition/SOFTWARE_DECOMP.md` `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`;
- `_Decomposition/Deliverables.csv` `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a`;
- `_Decomposition/ScopeLedger.csv` `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df`;
- `docs/PRD.md` (relative to `projects/pec/`) `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32`;
- DEL-02-08 `_STATUS.md` `d80800a48b45a43d641916bd5ee67c4b478e21538281b833e34dbc7cfe5f0eef` and `Dependencies.csv` `c23cd711fc8762dbd4a8629ba277753544f9f9e91368f789140b040f94cf701e`;
- DEL-02-09 `_STATUS.md` `3e14313c78e2500cabbd3f4897f9095daabc75c6468169074cb4400f4667d768` and `Dependencies.csv` `41afd6dc44f21200f6b2a1c480e9175d98b64d49b12e638bca67edcd15168e4b`.

### Add-on S — status act (only if question 2 selects it)

After the act's checks pass and the independent verifier has passed, the same WORKING_ITEMS instance runs, from the repository root:

```text
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser" INITIALIZED "TASK+status-advance"
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser" INITIALIZED "TASK+status-advance"
```

It runs each command only if `validate_scope_of_work.py` on that deliverable prints `PASS format=SOW_V1`. The tool is forward-only.

| Path | Preimage SHA-256 | Postimage SHA-256 (`{D}` = 2026-09-26) |
|---|---|---|
| DEL-02-08 `_STATUS.md` | `d80800a48b45a43d641916bd5ee67c4b478e21538281b833e34dbc7cfe5f0eef` | `4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe` |
| DEL-02-09 `_STATUS.md` | `3e14313c78e2500cabbd3f4897f9095daabc75c6468169074cb4400f4667d768` | `e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056` |

**Slot rule.** The only varying bytes are the act date `{D}`, in two places per file: `**Last Updated:** {D}` and the appended history line `- {D} — State set to INITIALIZED (TASK+status-advance)`. `**Current State:**` becomes `INITIALIZED`, and every other byte is unchanged. At another date, the verifier reruns the two commands on a fresh export and compares byte for byte. The prototype ran both the `7a00a88df` and the `8f9bd314c` editions of the tool (`d2c4def1…9c3d`, which adds the CHECKING reversal), and both produced the tabled postimages.

### Add-on M — MEMORY files (only if question 3 selects it)

- **Paths.** At the undertaking's closeout (graph node M1), WORKING_ITEMS creates `DEL-02-08_Work_graph_parser/MEMORY.md` and `DEL-02-09_MEMORY_run_index_parser/MEMORY.md`. Both are new files, so their preimages are absent.
- **Content.** Each is instantiated from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b…6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` table row: `| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | First Scope of Work contract written under D-PEC-98 (graph node S3). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-98 ruling record> |`.
- **Slots.** `{D}`, `{PR}` and the two link targets are fixed at closeout. The verifier checks that no other byte departs from the template.

## Generation method (binding)

The bytes come from one run of `apply_d98.py`, **SHA-256 `0f99d4b931c4e7189d111b96cd7f8c74f93751466b2dd2184a0a50b4e86881da`**. It is stdlib-only Python, prepared with CPython 3.13.7, and is copied byte for byte into the run root with the two candidate files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_INIT_D98_{D}/apply_d98.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_INIT_D98_{D}/candidates [--check-only]
```

Before any write, it checks:

- the two candidate hashes;
- that both targets are absent and their folders present;
- the eight pinned read-only hashes;
- that the write set equals the grant.

It exits 1 with nothing written on any failure, and exits 1 if run a second time. It never touches `_STATUS.md`; S is a separate step. `verify_d98_quotes.py` (`68813344eb49a4ba2d159361bac93cdba69d8c4d0b21f103e4354bbf27c9d30b`) and `run_d98_checks.sh` (`dfce71921817c18bf7a2fbdd5ca5f1e4ab83f114ab02eb08d6e8e4420466d1e1`) are the check aids; they are not bound.

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`. Record each command, exit code and output in the run root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | ruling and register row on fetched `origin/main`; `apply_d98.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `ALLOW` everywhere; otherwise stop and route the discrepancy (question 4 covers a revision-1.6 basis) |
| Contract validity | `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` ×2 | `PASS format=SOW_V1` ×2 |
| Checklist | `python3 tools/scope_of_work/derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>` ×2, each twice | exit 0; 21 and 17 items, every `AC-*` once in source order, bound to the postimage SHA-256; reruns byte-identical to the prepared `aec6d9bf…b0e5` and `a66599e4…e1c8` |
| Boundary owners (QA 21) | `python3 tools/scope_of_work/check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×2 | exit 0; 1 checked, 0 failing, each; the three `NOT_CHECKABLE` per-act clauses per contract resolved by hand as recorded below |
| Quote fidelity | `python3 <run root>/verify_d98_quotes.py . <08 folder> <09 folder>` | `RESULT PASS 71/71` |
| Lifecycle preserved (A) | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty under A; under S exactly the two tabled postimages |
| Strict registers | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | exit 0, 0 errors / 0 warnings, output identical to the pre-act run |
| Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | exit 0 each; output identical before and after |
| Containment | `git diff --name-status origin/main...HEAD` | the two created contracts, plus S's two `_STATUS.md`, plus M's two `MEMORY.md` if selected, plus the run root and HELP_HUMAN's records under `execution/_Coordination/**`; nothing else |
| Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. Adding two contracts changes no decomposition truth, register or topology; the audit's context and reference fidelity is unaffected. Recommended hand-carried QA 21 resolution: DEL-02-08 REQ-009 → `DEL-04-05`, REQ-010 → `DEL-01-03`, REQ-011 → `DEL-04-03`, each cited to CLM-011, which names that owner; DEL-02-09 REQ-007 → `DEL-04-05`, REQ-008 → `DEL-01-03`, REQ-009 → `DEL-04-03`, each cited to CLM-010.

### Independent verifier

The method's independent verification is a separate `MODE=VERIFY` run, read-only on production content. This preparer authored the candidates, and a TASK cannot delegate, so **no independent verification has run yet**. Recommended: a fresh read-only TASK that authored nothing performs it twice. First on this packet's PR, before the owner rules, as part of the PR's required review. Then at the act, on the written files. It returns a verdict file; defects return to the author, and the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`, the run-root script hashes as bound, and the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **`MODE=VERIFY`.** The mode-applicable QA subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21), including the QA 21 hand resolution above.
4. **Semantics.**
   - Every CLM quotation is verbatim at its cited locus and every observation is true at the stated commit.
   - No requirement adds scope beyond `SOW-095`/`SOW-096`, the register rows and PRD v2.3.
   - Every open item is marked `TBD`/`CON` rather than decided.
   - The `OBJ-002` qualification is no stronger than the §3 mapping note.
   - No D-PEC-96 identifier is relied on.
5. **Containment and lifecycle.** As in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act, the checks and, if selected, S and M. The manager runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/SOW_INIT_D98_{D}/`, in the default-writable fence, holds:
  - `apply_d98.py` (exact bytes) and `candidates/` (the two exact files);
  - `verify_d98_quotes.py` and `run_d98_checks.sh`;
  - the validator, checklist, boundary and quote outputs, and the preflight results;
  - `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md`;
  - `VERIFIER_VERDICT_NN.md`.

  No `_run_records/` entry is written in either deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under D-PEC-88, and the change is named in the graph. `_Evaluation/**` is not opened. Neither is any register or dependency file.
- **MEMORY rows.** Only through add-on M (question 3).
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for manager and verifier, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12 (Root `AGENTS.md`), with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** The script writes nothing unless every check passes. If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR removes the two created contracts, and M's two files if created. If S ran, the revert also restores the two `_STATUS.md` preimages tabled above. `write_status.sh` blocks backward transitions, so file revert is the only walk-back, as `D-PEC-63` §6 recorded. History is preserved and no reset is made.
  - The ruling record and register row are never reverted; a rollback is recorded as its own new register row and record.
  - The run root stays as non-current evidence, with a rollback note appended to its `HANDOFF_STATE.md`.
  - No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + S, A + M, A + S + M or an amendment, grants none of the following:

- any `v2/**`, `software-workflow.json` or `docs/PRD.md` write, or any source, fixture or test file. The fixture suites are X1's, under a later v2 packet;
- any `_Decomposition/**` or `_ScopeChange/**` write, or any register write: no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `Dependencies.csv` or `_DEPENDENCIES.md` change, and no dependency edge added;
- any `_CONTEXT.md`, `_REFERENCES.md` or `_SEMANTIC.md` write, or any other deliverable's file;
- any lifecycle change other than add-on S's single `OPEN → INITIALIZED` per deliverable, and none at all under A. No `## Remaining` entry is written;
- `CHECKING`, `ISSUED`, artifact acceptance, a REVIEW gate act, or any readiness or reliance claim. `CHECKING` is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it;
- a registry, profile or D-PEC-96 act, or a resolution of any `CON` item recorded in the contracts;
- a Task Management disposition, an audit run or a pointer move;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- a schedule reading: blocker output stays advisory (`FULL_GRAPH`, threshold `INITIALIZED`).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**.
2. **Add-on S — record `INITIALIZED` for both deliverables after the contracts validate and pass independent verification.**
   - Recommendation: **S**. Standard §8 defines `INITIALIZED` as exactly this condition, D-PEC-63 ruled the same act for all seven sibling parsers, and without it `DEL-03-01`'s advisory edges to these parsers stay unmet.
   - Choose "A without S" to keep this act lifecycle-neutral; the status act can then ride a later packet.
   - Without an answer, **no status act is performed**.
3. **Add-on M — MEMORY files.** Create both `MEMORY.md` files from the template at closeout so the M1 node can write the run row (recommended; the same choice D-PEC-96 question 6 offers for DEL-01-06). The alternative is to record the run only in the graph and central receipt and complete without rows, as `projects/pec/AGENTS.md` allows on your decision.
4. **Basis re-pin if SCA-006 checkpoint 3 lands first.**
   - **Recommended:** the same ruling covers a bounded mechanical re-pin. It changes only the frontmatter `decomposition_basis` commit, the Purpose paragraph's revision, commit and SHA sentence, and the PRD version and SHA sentence. It is valid only if `verify_d98_quotes.py`, rerun against the new tree, still passes 71/71 with every quoted locus unchanged (preparation found them unchanged in the revision-1.6 candidate). The independent verifier confirms that no other byte moved, and the postimage hashes are recomputed and recorded.
   - **Otherwise:** re-present the packet.
5. **CON-005 routing (work-graph dependencies).** Leave it open and route it to the next PEC scope change (recommended). Or direct now, by amendment, whether DEL-02-08 extracts node-ID references from "Needs" cells as DependencyEdge evidence.
6. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran in fresh `mktemp -d` directories in the session scratchpad, outside the checkout:

- `s3base.*` is a `git archive` export of the whole tree at `7a00a88df`, and a second one at `8f9bd314c`;
- `s3proto.*` is the `7a00a88df` export in which the candidates were authored;
- `s3gitmeta.*/repo` is a `git clone --shared --no-checkout` of the repository, detached first at `7a00a88df` and then at `8f9bd314c`. It gives the git-dependent validators a history. It reads the repository's objects and writes nothing to the repository.

Interpreter: Python 3.13.7 (CPython); local date 2026-09-26. Nothing was written to the checkout or its repository except the `git fetch` the brief requires.

| Command (scratch) | Exit | Result |
|---|---|---|
| `validate_scope_of_work.py` on both final candidates (at `8f9bd314c`; earlier drafts also at `7a00a88df`) | 0 ×2 | `PASS format=SOW_V1`; JSON `issues: []` |
| `derive_review_checklist.py` ×2 per candidate | 0 | 21 / 17 items; order equals source `AC-*` order; bound to the candidate SHA-256; reruns byte-identical |
| `check_boundary_owner_resolution.py --show-not-checkable` | 0 ×2 | 1 checked, 0 failing each; `NOT_CHECKABLE` 08: REQ-009/010/011, 09: REQ-007/008/009 (hand-resolved above) |
| negative control: the same candidate with one matrix row removed | 1 / 1 | validator `FAIL format=INVALID`; checklist refuses with no output artifact (QA 18) |
| ID-collision scan (QA 19; `evidence/id_collision_scan.out`) | — | one own-voice quoted `"CON-001"` (upstream) found in an early draft and rewritten as `DEL-01-03/CON-001`; none remains |
| `verify_d98_quotes.py` | 0 | `RESULT PASS 71/71` (every quotation at its cited locus: ledger rows, register cells, PRD, decomposition, SCA-005 plan and IA, templates, method, `AGENTS.md`, `DEL-01-01` SOW) |
| the same with one candidate quote mutated in each file (negative control) | 1 | the three affected checks fail |
| `validate_decomposition_registers.py --strict` before and after | 0 / 0 | 0 errors / 0 warnings; output identical |
| `validate_pec_loop_receipts.py --repo-root .` before and after | 0 / 0 | output identical |
| `harness.py self-check` before and after | 0 / 0 | output identical |
| `git diff --check` with the two files intent-to-add | 0 | clean |
| containment | — | exactly the two new `ScopeOfWork.md`; `_STATUS.md` blobs unchanged |
| `apply_d98.py --check-only`, then apply, then rerun, on a fresh export | 0 / 0 / 1 | 2 RENDER; 2 WRITE with "targets 2/2 byte-exact; pinned 8/8 unchanged"; rerun refuses with nothing written; the diff against the export is exactly the two files |
| option S prototype: `write_status.sh … INITIALIZED "TASK+status-advance"` ×2 in the scratch clone (tool editions `7a00a88df` and `8f9bd314c`) | 0 ×2 each | postimages as tabled at `{D}` = 2026-09-26, identical across editions |
| `pec_reliance_hold.py … exact-correction-preparation` ×4 | 0 ×4 | `ALLOW` |

Scratch artifacts, in the preparer's `s3/` folder and listed with hashes in `s3/SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` | `b28cf13d93851dc875575dafd759171205a75bc4bb63ef67e103fa2094d10b24` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` | `c9705ca28da82687e82bccdeb1bca5e271833d267c4afe23526965c4e13c7bd9` |
| `apply_d98.py` (the bound act script) | `0f99d4b931c4e7189d111b96cd7f8c74f93751466b2dd2184a0a50b4e86881da` |
| `verify_d98_quotes.py`, `run_d98_checks.sh` (check aids) | `68813344…d30b`, `dfce7192…d1e1` |
| `evidence/checklist_DEL-02-08.json`, `evidence/checklist_DEL-02-09.json` | `aec6d9bf…b0e5`, `a66599e4…e1c8` |
| `evidence/RUN_D98_CHECKS_at_8f9bd314c.out` (the full rerunnable run), `evidence/negative_controls.out` and the other outputs | in `SHA256SUMS` |
| `evidence/BASIS_SHA256_at_7a00a88df.txt` (77 basis files; all unchanged at `8f9bd314c` except `write_status.sh`) | in `SHA256SUMS` |

Basis read for preparation, at `8f9bd314c` unless stated (full list in `evidence/BASIS_SHA256_at_7a00a88df.txt`):

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…` / `1a13a5b0…` / `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `_Decomposition/SOFTWARE_DECOMP.md` (rev. 1.5) / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` / `_LATEST.md` | `dc2b8479…9660` / `b8628fc4…3d65a` / `83152a94…9df` / `2a194105…eb0df` / `626feaaf…12dd` |
| `docs/PRD.md` (v2.3) | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| SCA-005 `Propagation_Plan.md` / `Impact_Assessment.md` / feed-model design note | `50cd0b1d…1350` / `0bcbe9bd…39bf` / `4b9ccb9f…12da` |
| D-PEC-96 proposal (rev. 3) / D-PEC-95 proposal / D-PEC-95 ruling / D-PEC-93 ruling / D-PEC-63 / D-PEC-94 / `_REGISTER.md` | `2f7d9875…afc4` / `9137d387…` / `51dceb71…` / `ffb0b582…3709` / `0241db82…` / `b6814e90…` / `cdfc4719…d519` |
| `REV_DEL-01-06_2026-08-04_1113` `Review_Summary.md` / `Decision_Log.md` | `c5919cd3…` / `9cd4873d…` |
| Work graph `HELP-HUMAN-PEC-20260925-POST-SCA005` | `24901c3a80f7a49ae4de3c35e94a5e2f9521c397c57dacb83371068f008f41be` |
| Sibling SOWs DEL-02-01 / -03 / -04 | `5d286ec9…` / `c3e7928c…` / `bdb4eea0…` |
| Upstream SOWs DEL-01-01 / DEL-01-03 / DEL-01-06 | `43f1f57a…0170` / `986ef155…6341` / `5fdcfd96…a2fa8` |
| `construct-local-work-graph` `WORKFLOW.md` / template; `MEMORY_TEMPLATE.md` | `3e197c9d…9dc3` / `5661c609…6fa6`; `5a9564f4…6a5a` |
| Wave-2A notices (EXECUTION / SETUP_DEPS / CLOSURE / FORMATION / CHANGE_CONCERNS) | `d194b1b5…` / `b57c725e…` / `6e03c273…` / `ad28534c…` / `e0f17813…` |
| Produced guard `v2/src/pec_v2/core/content_minimal_guard.py` (unaccepted) | `740a4a74…19ee9` |
| SCA-006 `PRD_V2_4_SUCCESSOR_DIFF.md` / `Propagation_Plan.md` / `Impact_Assessment.md` | `a743a527…` / `f95d00d1…` / `93253b7d…` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d931…41cbc` / `b1712e4b…cd0e` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node S3 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
