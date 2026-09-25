# D-PEC-93 — PROJECT_SETUP packet: SCA-005 Lane A4 (DEL-02-08/09 preparation) with Lane B3 (dependency retirements, new edges, mirrors), re-audit and audit pointer — proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by a TASK (Type 2) under HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`, node H8) for the PEC loop, 2026-09-25 (session date), from brief `H8_D93_PROJECT_SETUP_PROPOSAL.md` (SHA-256 `8f040e8d83061820e6a5e98958ce0aba4648096b8474f91123fe63b7bbc13c78`). No earlier direction approves this file. It performs no production act: no tracked file was edited, and every prototype ran on scratch exports only. It asks for two new `OPEN` lifecycle files and no other lifecycle change. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `6dac281c6` the register has no D-PEC-93 row and no file under `_DECISIONS/` carries the number; this packet uses the number its brief assigned. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-93_project_setup_sca005_a4_b3_proposal_2026-09-25.md`.

## Provenance

- **Owner acts.** Checkpoint 2, 2026-09-25: "CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred." (`_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md`, `ca88f6a8…3d66`; register row `D-PEC-92`). That record sends A4 — the DEL-02-08/09 folders, their metadata files and their `Dependencies.csv` ANCHOR rows — to "PROJECT_SETUP under its own packet, together with the Lane B3 dependency work". Checkpoint 3, 2026-09-25: "CP3: accept; Q1 a" (`…/SCA-005_GROUP-3_2026-09-25/DECISION.md`, `35c211a6…f673`), closure `CLOSED_FOR_SCOPE_CHANGE_ONLY`, with A4 + B3 and "a re-audit after A4 and B3" recorded open, and `_Evaluation/DecompCoverage/_LATEST.md` "left to the audit workflow's owner". The brief reports the owner's later direction "go ahead with the PROJECT_SETUP packet"; this TASK did not observe that message and records it as the brief states it.
- **Fence.** `projects/pec/AGENTS.md` (`46689c36…3846`) §"Write Scopes And Fences": every write outside `execution/_Coordination/**` needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. D-PEC-92 opened none of the A4/B3 paths.
- **Intent of record.** SCA-005 `Propagation_Plan.md` (accepted at `50cd0b1d…1350`) §A4, §B3, §C2, §C4 and §"Failure and rollback"; `Amendment_Preview.md` (`ad48cc56…e65ebe4`) A-19/A-20 rows; `RUN_SUMMARY.md` (`e9a0224e…e518`) §"Recommended downstream reruns" and its COV-072 correction (42, not 40, contexts await B1). The plan's A4/B3 is intent; the bytes below are this packet's.
- **Accepted basis.** Decomposition revision 1.5 `current_basis` (`SOFTWARE_DECOMP.md` `dc2b8479…9660`; `Deliverables.csv` `b8628fc4…d65a`; `ScopeLedger.csv` `83152a94…d9df`; `ContextBudgetQA.csv` `2a194105…0df`; `Companion_Inventory.csv` `7c8a24a8…ef8`); PRD v2.3 (`docs/PRD.md` `fff27a66…fdc32`).
- **Precedents.** D-PEC-62 §3.1/§3.2 (`4aa1b83b…8924`; the scaffold and seeding scripts in `_Coordination/SEED_D-PEC-62/`); the SCA-004 PROJECT_SETUP closeout `_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/` (MANIFEST / VALIDATION / HANDOFF_STATE; one exact ANCHOR row `DEP-01-06-003` added by PROJECT_SETUP); D-PEC-66 (struck-through mirror form for a withdrawn edge); D-PEC-91 (packet format, slot-free exact grant, rollback by PR revert).
- **Source state.** Every hash here was read at `origin/main` `6dac281c679e779e9e8507add693554f102242d2`, detached, clean (`git status --short --ignored` hashed `fe89c08e…5d5d` before and after preparation; HEAD unchanged).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`), run from `projects/pec` with `--register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --operation exact-correction-preparation`, returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}`, exit 0, for all 36 targets: the 33 product paths of options A and O, `_Evaluation/DecompCoverage/_LATEST.md`, the audit-folder stem and the run-root stem.

## What preparation found

### Folder names (the PROJECT_SETUP naming rule)

The project rule is D-PEC-62 §3.1: "`{ID}_{Label}` where Label = deliverable/package name with non-alphanumerics mapped to `_`, runs collapsed, no leading/trailing `_`" — implemented as `re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]", "_", name)).strip("_")` in `SEED_D-PEC-62/scaffold_pec.py`.

| Accepted name (`Deliverables.csv`) | Output folder (under `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/`) |
|---|---|
| DEL-02-08 `Work-graph parser` | `DEL-02-08_Work_graph_parser` |
| DEL-02-09 `MEMORY run-index parser` | `DEL-02-09_MEMORY_run_index_parser` |

Check: the rule reproduces all 64 existing folder names (64/64; 66/66 in the prototype). The bundled `preparation` skill's own minimum rule (replace `/ \ : * ? " < > |` with `-`, collapse whitespace) would give `DEL-02-08_Work-graph parser` and matches 0 of the 64 existing folders; the project rule governs, and it is also filesystem-safe. The outputs equal the paths the plan anticipated.

### Method identity

`workflows/index.json` (`213a0738…fca3c`) resolves the effective descriptor `{kind: "skill", name: "preparation", source: "bundled", sourceRootId: "chirality-root"}` (`.agents/skills/preparation/SKILL.md` `8ae93a30…a444`, `references/scaffold-contract.md` `316b5f51…c5c4`, `execution.json` `dd59f002…c2bd`). The ordered `methods` field is therefore `[{kind: "skill", name: "preparation", source: "bundled", sourceRootId: "chirality-root"}]`. Disclosed collision: a bundled **workflow** also named `preparation` exists (`workflows/preparation/WORKFLOW.md` `cf0c79f4…8d78`); it is a different kind and is not selected. No project `.chirality/workflows` or user `~/.agents/skills` origin exists on this host. The other methods are `workflow project-setup`, `workflow audit-decomp` and `skill software-code-review`, all `bundled` / `chirality-root`.

Where the skill and the PEC precedent differ, this packet follows the precedent and says so: `_CONTEXT.md` uses the D-PEC-62 field table (as all 64 existing files do); `_SEMANTIC.md` stays a zero-byte stub (D-PEC-62 §3.1: "`_SEMANTIC.md` remains a stub"; all 64 existing files are empty); `_DEPENDENCIES.md` uses the D-PEC-62 seeded layout, not the skill's `NOT_RUN_YET` container. No `MEMORY.md` is created (the skill creates it only when explicitly selected).

### How `_STATUS.md` is created

Yes, a tool writes `OPEN`: `tools/scaffolding/write_status.sh <folder> OPEN <ACTOR>` (`b6194cc0…52ed`) creates a new `_STATUS.md` only at `OPEN` (its `NEW_FILE_NOT_OPEN` guard blocks anything else) and stamps the local date. It cannot parse the zero-byte `_STATUS.md` stub that `scaffold_deliverable.sh` (`7a04c1a9…7a23`) creates (exit 2) — the tool-sequence defect D-PEC-62 §3.1 resolved by deleting the fresh stub first. This packet avoids any deletion: create the empty folder, run `write_status.sh … OPEN TASK+preparation`, then run `scaffold_deliverable.sh`, which skips the existing `_STATUS.md` and creates the other four stubs. The prototype proved the two orders give byte-identical `_STATUS.md` and `_SEMANTIC.md`. Actor string: `TASK+preparation` (the actual executor and method, in the `TASK+status-advance` form the history lines already use). The resulting bytes, with `{D}` the act date:

```text
# Status: DEL-02-08

**Current State:** OPEN
**Last Updated:** {D}

## History
- {D} — State set to OPEN (TASK+preparation)
```

No `## Remaining` section is written (DEL-04-04 is an existing plain-`OPEN` precedent); work items for the first Scope of Work belong to B4.

### Can `dependency-extract` produce B3?

No, not as specified. Its method extracts from the deliverable's **own** source documents, forbids cross-deliverable synthesis, and writes only the host deliverable's two dependency files. DEL-02-08/09 have no source documents yet (no Scope of Work), the DEL-03-01 edges come from PRD v2.3 PEC-RCN-002 rather than DEL-03-01's accepted SOW, and it preserves `Origin=DECLARED` rows, so it cannot retire the 8 tree anchors. The two ruled precedents for this situation are D-PEC-62 §3.2 (a deterministic seed "outside the dependency-extract lifecycle by packet ruling") and the SCA-004 PROJECT_SETUP act (one exact ANCHOR row). This packet binds the exact rows through a deterministic generator and applies `dependency-extract`'s Function 5 checks as acceptance checks (schema, enums, DependencyID uniqueness, evidence present, parent-anchor count). A later `dependency-extract` run in `MODE=UPDATE` keeps the rows (`Origin=DECLARED` is preserved; `EXTRACTED` rows are matched by `DependencyID`).

### The new edges and the optional DEL-04-01 edge

Each new EXECUTION edge follows the stratum and field pattern of its closest existing sibling (PROPOSAL / `EXTRACTED` / `IMPLICIT` / `MEDIUM` / `INITIALIZED`, like E-P07 and E-P19..E-P25), with evidence quoted verbatim from the accepted sources (the generator asserts each quote is a substring of its file):

| Edge | Row (owner) | From → To | Evidence |
|---|---|---|---|
| E-P79 | `DEP-02-08-003` (DEL-02-08) | DEL-02-08 → DEL-01-01 | `Deliverables.csv` row DEL-01-01 Description: "16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows)" |
| E-P80 | `DEP-02-09-003` (DEL-02-09) | DEL-02-09 → DEL-01-01 | same row: "RunRecord is sourced from central receipts, work graphs and the MEMORY run index" |
| E-P81 | `DEP-03-01-015` (DEL-03-01) | DEL-03-01 → DEL-02-08 | PRD §9.2 PEC-RCN-002: "work graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`" |
| E-P82 | `DEP-03-01-016` (DEL-03-01) | DEL-03-01 → DEL-02-09 | PRD §9.2 PEC-RCN-002: "run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence" |

Edge IDs continue the exhibit's `E-P` series (maximum in use `E-P78`; `E-P79`..`E-P83` are unused anywhere in the repository).

**Optional DEL-04-01 → DEL-02-08 (E-P83): recommend omitting it.** It is prototyped (option O: `DEP-04-01-006`, PEC-ORI-001 "gate states (from decision registers, scope-change state and work-graph `BLOCKED` nodes)"; 112 edges, still 0 SCCs). Three reasons to omit it. DEL-04-01 already reaches DEL-02-08 through DEL-04-01 → DEL-03-01 (E-P32) → DEL-02-08 (E-P81). DEL-04-01 has no direct edge to any of the seven existing parsers, although PEC-ORI-001 names receipts and decision registers as well; orientation reads the reconciled record tier, not parser output. And the information-flow model does not add an edge for a relationship that is structural adjacency already carried by the path.

### Topology (observed on the prototype)

`analyze_dep_closure.py`: 119 EXECUTION edges / 64 nodes now → **111 edges / 66 nodes, 0 SCCs, 0 bidirectional pairs, isolated DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05** (option A; option O 112). The plan's 119 → 108 → 107 → 111/112 is confirmed. The six isolated units are the closure tool's `isolated_units` WARNING the plan's §C4 anticipated for the four retired deliverables plus the two pre-existing ones. The one hub, DEL-03-01, rises from degree 24 to 25 (threshold 20; pre-existing hub WARNING).

### Findings beyond the plan (disclosed; not repaired here)

1. **Evidence-quote currency (new).** After B3, 19 surviving ACTIVE EXECUTION rows cite an `EvidenceQuote` that is no longer verbatim in the cited file. Sixteen became stale through SCA-005 (they were verbatim at revision 1.4 / PRD v2.2): `DEP-03-01-005`, `-008`..`-013` (the old PEC-RCN-002 wording), `DEP-05-01-004`, `DEP-05-02-003`, `DEP-06-03-003`, `DEP-08-05-004`, `DEP-09-05-006`..`-008`, `DEP-10-10-003`, `DEP-10-12-003`. Three were already non-verbatim at revision 1.4 (`DEP-08-04-005`, `DEP-10-05-004`, `DEP-10-05-005`). No validator checks quote currency (EVQ checks presence and shape only), so every check below still passes. The plan named only `DEP-03-01-007`, which this packet refreshes. See owner question 4.
2. **Five mirrors the plan's list omits.** Besides the eight consumer mirrors the plan names, five other `_DEPENDENCIES.md` files name an edge B3 retires: DEL-02-07 (downstream E-P25) and the four retired deliverables' own files (their upstream tables and the downstream bullets E-N02 and E-P46). Left alone, they would contradict their registers; `dependency-extract`'s QA requires the mirror to agree with `Dependencies.csv`. Option A includes them; option P does not.
3. **Parent anchors of the four retired registers.** Retiring both tree anchors per the plan leaves DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 with 0 ACTIVE `IMPLEMENTS_NODE` rows — `dependency-extract`'s `FLOATING_NODE` warning, expected for retired deliverables. `analyze_dep_closure.py` counts anchors regardless of `Status` (`anchor_coverage` PASS).
4. **Tool mismatch.** `tools/validation/validate_id_format.sh` checks PROJECT-variant IDs (`DEL-NNN-NN`) and rejects every PEC SOFTWARE ID, including existing ones such as DEL-02-01. It is not used; `DRB-006` and the closure tool's ID pattern cover SOFTWARE IDs (0 invalid IDs, 0 normalizations).
5. **Stale orientation text outside this grant.** `execution/_Coordination/_COORDINATION.md` (`8da03a2f…879c`) still names revision 1.4 as the accepted basis. That is HELP_HUMAN's D-PEC-88 surface and is not opened here.

## Options

- **A — A4 + B3 + re-audit + audit pointer (recommended).** One PROJECT_SETUP act on **31 product paths** (12 created in two new folders; 19 modified: 6 `Dependencies.csv` and 13 `_DEPENDENCIES.md`), then a TASK `audit-decomp` re-audit into a new `COV_SCA005_POSTSETUP_*` folder and, if the re-audit has no BLOCKER, the `DecompCoverage/_LATEST.md` pointer move. Row counts: **20 retired** (18 in the four retired registers, `DEP-09-05-005`, `DEP-03-01-014`), **1 refreshed** (`DEP-03-01-007`), **8 added** (4 ANCHOR + 2 EXECUTION in the new registers, 2 EXECUTION in DEL-03-01); 0 deleted. Mirrors: 13 edited + 2 created.
- **P — plan-listed mirrors only (narrower).** As A, but only the eight `_DEPENDENCIES.md` files the plan names: **26 product paths**. Validator and topology results are identical to A (mirrors are not read by the tools). DEL-02-07's mirror and the four retired deliverables' mirrors keep describing edges as live while their registers say `RETIRED`. Not recommended.
- **O — optional add-on: the DEL-04-01 → DEL-02-08 edge.** +2 paths (DEL-04-01 `Dependencies.csv`, `_DEPENDENCIES.md`), a different DEL-02-08 `_DEPENDENCIES.md`, 1 more added row; 112 edges. Not recommended (above).
- **B1 — optional add-on: re-pin 42 `_CONTEXT.md` and 64 `_REFERENCES.md` to revision 1.5.** Scope: the 42 contexts not written in A2 get the A2 provenance tail ("then by revision 1.4 (`current_basis`, SCA-004 successor),⏎then by revision 1.5 (`current_basis`, SCA-005 successor)."); all 64 existing references get two bullet changes (revision 1.4/SCA-004 → 1.5/SCA-005; PRD v2.2 → v2.3). Semantic fields are untouched. Cost: **+106 paths** (137 in total with A), +212/−170 lines, across 64 deliverables (4 CHECKING, 2 IN_PROGRESS, 26 INITIALIZED, 28 OPEN, 4 RETIRED). The generator is `gen_d93_b1.py` (`eff5d2fb…677c`). It fails closed on any anchor miss and on any population other than 42/64. Pre/post aggregates: `33ffe763…b8f2` → `734d229a…cc0c`; path-list hash `f20d8729…4030`. Strict validator 0/0 and topology unchanged on the prototype. It would clear the re-audit's COV-077/078 INFO rows and let `MetadataAlignmentState` close. **Not recommended for bundling.** It is a separate lane with its own closure record (the SCA-004 precedent ran it as its own act). It more than quadruples the review surface for no effect on the blockers this packet exists to clear. Its trigger ("after checkpoint 3") is met, so it can follow as its own short packet at the same cost.
- **Amend.** The owner changes the scope — for example, to add the evidence-quote refresh (finding 1), change the actor string, or strike the pointer move — and the packet is re-prepared.
- **Defer.** Nothing opens. COV-001/002 (BLOCKER) and COV-070/071 remain, the strict validator keeps its two DRB-008 warnings, `DEP-09-05-005` still points at a retired deliverable, and the 18 ACTIVE rows remain in the retired registers.

An A4-only option (folders and anchors without B3) is not offered. It would leave DEL-02-08/09 as two new isolated units, keep every pre-B3 defect, and separate what the owner deferred as one unit.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance under `chirality-root:bundled:workflow:project-setup` may run **one** PROJECT_SETUP act. It creates or modifies only these paths, relative to `projects/pec/execution/`, with the preimage SHA-256 at `6dac281c6` and the postimage SHA-256 computed with the act-date slot `{D}` = `2026-09-25`:

| Deliverable, file | Act | Preimage SHA-256 | Postimage SHA-256 (`{D}` = 2026-09-25) |
|---|---|---|---|
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/` (folder) | CREATE | absent | — |
| DEL-02-08 `_STATUS.md` | CREATE | absent | `d80800a48b45a43d641916bd5ee67c4b478e21538281b833e34dbc7cfe5f0eef` |
| DEL-02-08 `_CONTEXT.md` | CREATE | absent | `721a9807211b1330b0cd124139d37fdb9b2f9167b9edc461f218bb4570f34d20` |
| DEL-02-08 `_REFERENCES.md` | CREATE | absent | `87f95d423851a800651c6e01c4b04a7434b5f56f3476b5512075da556563840b` |
| DEL-02-08 `_DEPENDENCIES.md` | CREATE | absent | `0ee572b955cedf628958305e049b0f776bec3fad39dada73bca88b1421959a3d` |
| DEL-02-08 `_SEMANTIC.md` (empty) | CREATE | absent | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| DEL-02-08 `Dependencies.csv` | CREATE | absent | `c23cd711fc8762dbd4a8629ba277753544f9f9e91368f789140b040f94cf701e` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/` (folder) | CREATE | absent | — |
| DEL-02-09 `_STATUS.md` | CREATE | absent | `3e14313c78e2500cabbd3f4897f9095daabc75c6468169074cb4400f4667d768` |
| DEL-02-09 `_CONTEXT.md` | CREATE | absent | `2413b5c0b241eb44c9e53401499729ca3b84e23860692b63f09104af56640502` |
| DEL-02-09 `_REFERENCES.md` | CREATE | absent | `211cb59ce46a7399ba56775fa57024f018322ebf2f50ecaf0887eb419d06073f` |
| DEL-02-09 `_DEPENDENCIES.md` | CREATE | absent | `41c841a4cac76634bd5f1aae664152f9488c073b5ef5c254f2fe2cdaaebadf3a` |
| DEL-02-09 `_SEMANTIC.md` (empty) | CREATE | absent | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| DEL-02-09 `Dependencies.csv` | CREATE | absent | `41afd6dc44f21200f6b2a1c480e9175d98b64d49b12e638bca67edcd15168e4b` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/Dependencies.csv` | MODIFY | `5f68759d07cc001e139fc351e33748ef7f03ba5ba9cd7ed77a6182ad8161bd65` | `833fbfe0c2a09ab8b564866dff8e55327fb005d5c4993973ef93408d2e2a436b` |
| `PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/Dependencies.csv` | MODIFY | `f4eaf5266f131437b31cee5edfd5dcbadc9c7aee59e5b41cba76107bc7f7f4fb` | `ac55576e8bb4b17ba57d7e1d92e96415ce4f9da40c2c742e8be769df4d49b8fc` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/Dependencies.csv` | MODIFY | `bd4c16fadb7025f1b22c039713fc755a53b18949c85d8a60f8abbb51f8714821` | `77230bbbc0e809c4e9e0c3a8353ad5bf4f42ee7ad7849b7199a33c84f0b1d8dd` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/Dependencies.csv` | MODIFY | `5d684e2425e365b2e09bd3e6e7faf63d5a2efd7acbe50634d52075a30bc90fe6` | `cbb2175b28c4a1ba8e7ec58777d8831d20053b14363f63647ff727f7a5392b12` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/Dependencies.csv` | MODIFY | `4c2c93eafff62d6f00e5668ebaaab40e75f06693a0bf5809478c81d14b4c322f` | `aa1dbe679b23450fed5eb603d687ae91cfa3fa9550f33d057094f9366ec6d41c` |
| `PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/Dependencies.csv` | MODIFY | `c62d3d262b258be6151bb9ca6d8b8d096db917867febee7fc7bb4d5b0958dd68` | `9811343ccb1f9e6820a03ebdac5aa53f163d355049508815438befb35db032d5` |
| `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_DEPENDENCIES.md` (plan) | MODIFY | `2242ca8a785ba74d2fc885d86eff606587888af3ff4ed4f21ff52a52b141468f` | `818a06a33952651ce70c415b33bfc7c381898eda4891cd33cb21472bc4b62c3c` |
| `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_DEPENDENCIES.md` (plan) | MODIFY | `91d67bc8fab21e6f62ba084383f5e5dae13ce27aef9cf5824f74c084dc80e6bf` | `1c39420c392e09b7e37edb48680bf203018ddad64a1cfbdae98808bbab5172f0` |
| `PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_DEPENDENCIES.md` (plan) | MODIFY | `2e566074e54d1d92fa7dcd5a632ae6d2f782568fcaccc446c915ba139a5dee0f` | `625bb400c65ff866369bfb1789244e651570555f2ac7054cd9ceac505455052e` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_DEPENDENCIES.md` (plan) | MODIFY | `398f651d4b6701c7dd98cbe72f78c04035f5b1c7de8e9ae2e2e1d8c9837baa60` | `e039ded3a08b3951540d960c3c626ebccde1f24df7584416326325dcd8d261ec` |
| `PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_DEPENDENCIES.md` (plan) | MODIFY | `f2567c0ecd883673e3b2b73870bdfc479ee187a59af8acbad9ac71cb33249590` | `9fd90c726544d06550f730c383a38df4aedcfb8dc0d5582432af0a80a5d1afad` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_DEPENDENCIES.md` (plan) | MODIFY | `8fc61c243907764803f40b04631b78883ad00b54a2189f727f71997af80ac6cb` | `2ea6519dec0866dc38881d0074d2893cb7b635c53ea703516b21014ff10a5360` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_DEPENDENCIES.md` (plan) | MODIFY | `b100e6b67a39d342751ec9e343d4bf391790bb5ffabb9974d3b001d703b42c69` | `a9536c7a9a7caf419a941f204f9cd4d71b328b5047e142fb04d96017655d7b8b` |
| `PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_DEPENDENCIES.md` (plan) | MODIFY | `c41aa4e4ff8506f409c7f33fe90687906ac7489ec0fecbfa96632091bd77440f` | `faa212e0c6f667c291177f6a2859799302fe84d0fdea20f83c91e35e45965251` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_DEPENDENCIES.md` (completeness; not under P) | MODIFY | `f5b6e9d2d84be5415b747cb04e32d5dffd1f38e8040ab41786bcc92bea9afed2` | `2e53136f4580ae902b732c0ae657913d02e380b2a30350be39935347f88c8cdb` |
| `PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_DEPENDENCIES.md` (completeness; not under P) | MODIFY | `a9c3dd391c26628c4510544173f41bc1441b1d2279f384ecda0942da51a73426` | `d6a1ad590fddacf18132411661a11fa613436573fc3b480f7cad61f90e4d034d` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_DEPENDENCIES.md` (completeness; not under P) | MODIFY | `07c16cc4937df6e3c15123cce31a35f99e6274a588ddfea01c450a223c9b9bde` | `f315d8a8bd7bb34ecabc0d32fd6a6c92ceaf6e070ae26c346d87cc3f3d06da89` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_DEPENDENCIES.md` (completeness; not under P) | MODIFY | `cb354e3d4b601eb07047aff4a38dc4841801af0ebd617182265eb543b7a9bfb6` | `b1dc2ed3c6d78e3412907d72fbc2ea4b229861717b985a7f16852808b9df3ac6` |
| `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_DEPENDENCIES.md` (completeness; not under P) | MODIFY | `ba39a3898a7a76e26ffc72ec9b68a0d2d0db9edf36fd0775def2ddcf3e90981c` | `fc43eb3d3873cce8f9e488a039bcf8379ea7ecbc83436d2817e925ca3b863617` |

Aggregates (members in bytewise-sorted `projects/pec/…` path order, concatenated): option A postimage `c4525add6b621d16523ad7567410b96f1864683cf93fd0d03c3f43954a79727a` over 31 files (path-list hash `1133e1ab…b9f1`); P `db640591…0119` (26; `151bd95f…7719`); A+O `924afa8f…0720` (33; `eeed7977…ef21`). Under O: DEL-02-08 `_DEPENDENCIES.md` becomes `6c1b1b15212a8a79e2811a4ab77a87a151f5024973148e650b90fef7224d861f`, and DEL-04-01 `Dependencies.csv` `2daee4e7…16e4` → `14fec24616ad58c2d9c9dafabbc73c3059640f13285b0108710aeb751821db26` and `_DEPENDENCIES.md` `ea057889…4c0c` → `f52f344bfd9bc7d0484b1e196ea2d80017e1bcb495db3b236c9739123b2017bb` are opened as well.

Read-only basis the act re-verifies but never writes: `_Decomposition/Deliverables.csv` `b8628fc4…d65a`, `_Decomposition/ScopeLedger.csv` `83152a94…d9df`, `docs/PRD.md` `fff27a66…fdc32`, and the tools `scaffold_deliverable.sh` `7a04c1a9…7a23`, `write_status.sh` `b6194cc0…52ed`, `check_min_viable_fileset.sh` `a6c4af3c…8c20f8c`.

### Generation method (binding)

The bytes are produced by one run of the generator `gen_d93.py`, **SHA-256 `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2`**. The generator is copied byte-for-byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_{D}/gen_d93.py --repo "$(git rev-parse --show-toplevel)" --act-date {D}
```

(option P adds `--mirror-set plan`; option O adds `--optional-edge`). Before any write, it:

- checks every preimage hash above;
- checks that both target folders are absent;
- checks that the local date equals `{D}`;
- renders every postimage;
- round-trips every touched CSV row byte-exactly, so only the named cells change;
- asserts every mirror anchor occurs exactly once;
- asserts every new `EvidenceQuote` is verbatim in its cited file.

Only then does it create the two folders with the repository tools, in the order stated above, and write. It exits 1 with nothing written on any failure. It exits 1 if run a second time, because the preimages have changed. Stdlib only; CSV rows use the corpus convention (`csv.writer`, `QUOTE_MINIMAL`, CRLF); Markdown files are LF with one trailing newline.

**Slot rule.** The only varying bytes are the act date `{D}`, at these loci:

- the new `_STATUS.md` date and history lines;
- the provenance lines of the six new Markdown files;
- `FirstSeen`/`LastSeen` of the 8 added rows;
- `LastSeen` of the 21 retired or refreshed rows;
- the `RETIRED {D}` / `refresh {D}` notes in the mirrors.

The hashes above are at `{D}` = `2026-09-25`. At another date, the verifier runs the same generator with that date on a fresh `git archive` export of the preimage commit and compares the two trees byte for byte. It records both the table hash and the slot-substituted hash.

### A4 — what the new files contain

- `_CONTEXT.md`: the D-PEC-62 field table (DeliverableID, Canonical name, PackageID with `File-Truth Parsers`, Type, ContextEnvelope, PhaseHint, CoversScopeItems, SupportsObjectives, ResponsibleParty `TBD (assignment at WORKING_ITEMS activation)`), then Description, Anticipated artifacts and Envelope notes. Every field is the exact revision-1.5 `Deliverables.csv` cell. The provenance paragraph reads: "Scaffolded under `D-PEC-93` ({D}) from accepted decomposition `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.5 (`current_basis`, SCA-005 successor; deliverable added by A-19 / A-20). Fields templated deterministically from `Deliverables.csv`; this file restates register truth and is not an independent authority."
- `_REFERENCES.md`: the SCA-004-era seven-bullet list at revision 1.5, with `docs/PRD.md` v2.3 and the covered SOW-095 / SOW-096. The D-PEC-62 DAG-exhibit bullet, which predates these deliverables, is replaced by the SCA-005 snapshot folder (A-19 / A-20). Closing line: "Populated deterministically under `D-PEC-93` ({D}); extend during production."
- `_DEPENDENCIES.md`: the D-PEC-62 layout with the header "Seeded deterministically under `D-PEC-93` ({D}) from accepted decomposition revision 1.5 (SCA-005, A-19|A-20) and PRD v2.3; the D-PEC-62 DAG exhibit predates this deliverable." It has one upstream row (DEL-01-01, PROPOSAL, CONSUMES, E-P79 or E-P80), one downstream bullet (DEL-03-01, E-P81 or E-P82), constraints C-04 and C-10 verbatim, and the standard blocker-semantics lines.
- `Dependencies.csv` (v3.1, 29 columns): three rows each. `DEP-02-0x-001` is ANCHOR `IMPLEMENTS_NODE` → PKG-02 and `-002` is ANCHOR `TRACES_TO_REQUIREMENT` → SOW-095 / SOW-096. Both use the exact D-PEC-62 anchor field values, with Notes `Tree anchor seeded under D-PEC-93`. `-003` is the EXECUTION row in the edge table, with Notes `PROPOSAL; Flag=none; EdgeID=E-P79|E-P80; seeded under D-PEC-93 (SCA-005 B3)`.

The rendered bytes at `{D}` = 2026-09-25 are in the prototype diff (`protoA_vs_base.diff`, `99c95ad2…81e7`).

### B3 — every register row touched (before → after)

Retirement representation, per plan: keep the row; set `Status=RETIRED` and `LastSeen={D}`; prefix `Notes` with `Retired under SCA-005 (<reason>); `. No other cell changes and no row is deleted.

| Owning file (deliverable) | Row | Kind → target | Before (`Status` / `LastSeen` / `Notes`) | After |
|---|---|---|---|---|
| DEL-06-04 | `DEP-06-04-001` | ANCHOR IMPLEMENTS_NODE → PKG-06 | `ACTIVE` / `2026-07-25` / `Tree anchor seeded under D-PEC-62` | `RETIRED` / `{D}` / `Retired under SCA-005 (A-34: DEL-06-04 retired, SOW-029 OUT); ` + before |
| DEL-06-04 | `DEP-06-04-002` | ANCHOR TRACES → SOW-029 | same | same prefix |
| DEL-06-04 | `DEP-06-04-003` | EXEC → DEL-01-02 (E-N09) | `ACTIVE` / `2026-07-25` / `PROPOSAL; Flag=none; EdgeID=E-N09` | same prefix |
| DEL-06-04 | `DEP-06-04-004` | EXEC → DEL-06-01 (E-N10) | … `PROPOSAL; Flag=none; EdgeID=E-N10` | same prefix |
| DEL-06-04 | `DEP-06-04-005` | EXEC → DEL-07-02 (E-P46) | … `DERIVED; Flag=none; EdgeID=E-P46` | same prefix |
| DEL-06-04 | `DEP-06-04-006` | EXEC → DEL-07-03 (E-P47) | … `DERIVED; Flag=none; EdgeID=E-P47` | same prefix |
| DEL-07-02 | `DEP-07-02-001` / `-002` | ANCHOR → PKG-07 / SOW-035 | `ACTIVE` / `2026-07-25` / `Tree anchor seeded under D-PEC-62` | `RETIRED` / `{D}` / `Retired under SCA-005 (A-35: DEL-07-02 retired, SOW-035 OUT); ` + before |
| DEL-07-02 | `DEP-07-02-003` | EXEC → DEL-00-02 (E-A03) | … `DERIVED; Flag=none; EdgeID=E-A03` | same prefix |
| DEL-07-02 | `DEP-07-02-004` | EXEC → DEL-07-01 (E-P48) | … `PROPOSAL; Flag=none; EdgeID=E-P48` | same prefix |
| DEL-07-04 | `DEP-07-04-001` / `-002` | ANCHOR → PKG-07 / SOW-037 | `ACTIVE` / `2026-07-25` / `Tree anchor seeded under D-PEC-62` | `RETIRED` / `{D}` / `Retired under SCA-005 (A-78: DEL-07-04 retired, SOW-037 OUT); ` + before |
| DEL-07-04 | `DEP-07-04-003` | EXEC → DEL-00-02 (E-A04) | … `DERIVED; Flag=none; EdgeID=E-A04` | same prefix |
| DEL-07-04 | `DEP-07-04-004` | EXEC → DEL-07-01 (E-P50) | … `PROPOSAL; Flag=none; EdgeID=E-P50` | same prefix |
| DEL-07-05 | `DEP-07-05-001` / `-002` | ANCHOR → PKG-07 / SOW-087 | `ACTIVE` / `2026-07-25` / `Tree anchor seeded under D-PEC-62` | `RETIRED` / `{D}` / `Retired under SCA-005 (A-36: DEL-07-05 retired, SOW-087 OUT); ` + before |
| DEL-07-05 | `DEP-07-05-003` | EXEC → DEL-00-02 (E-N01) | … `DERIVED; Flag=none; EdgeID=E-N01` | same prefix |
| DEL-07-05 | `DEP-07-05-005` | EXEC → DEL-01-01 (E-P14) | … `PROPOSAL; Flag=none; EdgeID=E-P14` | same prefix |
| DEL-09-05 | `DEP-09-05-005` | EXEC → DEL-06-04 (E-N02) | `ACTIVE` / `2026-07-25` / `DERIVED; Flag=PHASE_TENSION; EdgeID=E-N02` | `RETIRED` / `{D}` / `Retired under SCA-005 (A-33, A-38: target DEL-06-04 retired); ` + before |
| DEL-03-01 | `DEP-03-01-014` | EXEC → DEL-02-07 (E-P25) | `ACTIVE` / `2026-07-25` / `PROPOSAL; Flag=none; EdgeID=E-P25` | `RETIRED` / `{D}` / `Retired under SCA-005 (A-07, A-18: adapter.yaml is a parity-peer input, not the feed manifest; see DEP-03-01-007); ` + before |
| DEL-03-01 | `DEP-03-01-007` (refresh; stays `ACTIVE`) | EXEC → DEL-01-06 (E-P18) | EvidenceFile `execution/_Decomposition/Deliverables.csv`; SourceRef `Deliverables.csv row DEL-01-06 Description`; EvidenceQuote "Local configuration naming the loops PEC serves: one loop at P1 (PEC's own build, OI-010), extended to all five registered loops at P2." (no longer in the revision-1.5 row); LastSeen `2026-07-25`; Notes `PROPOSAL; Flag=none; EdgeID=E-P18` | EvidenceFile `docs/PRD.md`; SourceRef `PRD.md §9.2 requirement PEC-RCN-002`; EvidenceQuote "The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row"; LastSeen `{D}`; Notes `Evidence refreshed under SCA-005 (A-07, A-18: loop-registry feed profiles replace the adapter.yaml feed manifest); PROPOSAL; Flag=none; EdgeID=E-P18`. Statement unchanged. |

Rows **added**: `DEP-02-08-001`..`003` and `DEP-02-09-001`..`003` (new files), plus `DEP-03-01-015` (→ DEL-02-08, E-P81) and `DEP-03-01-016` (→ DEL-02-09, E-P82), both appended to DEL-03-01's register. Their field values are in the edge table and the generator. With `{D}`, the two appended rows are exactly:

```text
v3.1,DEP-03-01-015,PKG-03,DEL-03-01,Full-rebuild reconciler (one command),EXECUTION,NOT_APPLICABLE,UPSTREAM,PREREQUISITE,DELIVERABLE,PKG-02,DEL-02-08,DEL-02-08,Work-graph parser,execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser,Full rebuild ingests work graphs,docs/PRD.md,PRD.md §9.2 requirement PEC-RCN-002,work graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`,IMPLICIT,INITIALIZED,TBD,PENDING,MEDIUM,EXTRACTED,{D},{D},ACTIVE,PROPOSAL; Flag=none; EdgeID=E-P81; seeded under D-PEC-93 (SCA-005 B3)
v3.1,DEP-03-01-016,PKG-03,DEL-03-01,Full-rebuild reconciler (one command),EXECUTION,NOT_APPLICABLE,UPSTREAM,PREREQUISITE,DELIVERABLE,PKG-02,DEL-02-09,DEL-02-09,MEMORY run-index parser,execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser,Full rebuild ingests the MEMORY run index,docs/PRD.md,PRD.md §9.2 requirement PEC-RCN-002,run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence,IMPLICIT,INITIALIZED,TBD,PENDING,MEDIUM,EXTRACTED,{D},{D},ACTIVE,PROPOSAL; Flag=none; EdgeID=E-P82; seeded under D-PEC-93 (SCA-005 B3)
```

Row totals across the 66 registers: 255 → **263** (ANCHOR 136 → 140; EXECUTION 119 → 123; ACTIVE 255 → 243; RETIRED 0 → 20).

### B3 — exact `_DEPENDENCIES.md` mirror edits

Each edit is an exact string replacement that must match once (the generator's `mirror_edits`). Three forms are used. Each is modelled on the D-PEC-66 struck-through precedent, and each keeps the old text visible.

- **Downstream bullet retired:** `- X — CONSUMES [E]` → `- ~~X — CONSUMES [E]~~ — **RETIRED {D} under SCA-005 (D-PEC-93)**: <reason>; register row \`<row>\` kept with \`Status=RETIRED\``.
- **Upstream table row retired:** `| P | S | K | F | E |` → `| ~~P~~ | S | K | F | ~~E~~ |`, followed by one explanatory paragraph after the table.
- **New edges:** new bullets or rows in `EdgeID` order.

| Mirror | Edits |
|---|---|
| DEL-00-02 (plan: E-A03, E-A04, E-N01) | 3 downstream bullets struck (DEL-07-02 A-35 `DEP-07-02-003`; DEL-07-04 A-78 `DEP-07-04-003`; DEL-07-05 A-36 `DEP-07-05-003`) |
| DEL-01-01 (plan: E-P14) | E-P14 bullet struck (A-36, `DEP-07-05-005`); two bullets added after it: `- DEL-02-08 (Work-graph parser) — CONSUMES [E-P79]`, `- DEL-02-09 (MEMORY run-index parser) — CONSUMES [E-P80]` |
| DEL-01-02 (plan: E-N09) | 1 bullet struck (A-34, `DEP-06-04-003`) |
| DEL-06-01 (plan: E-N10) | 1 bullet struck (A-34, `DEP-06-04-004`) |
| DEL-07-01 (plan: E-P48, E-P50) | 2 bullets struck (A-35 `DEP-07-02-004`; A-78 `DEP-07-04-004`) |
| DEL-07-03 (plan: E-P47) | 1 bullet struck (A-34, `DEP-06-04-006`) |
| DEL-09-05 (plan: E-N02) | upstream row E-N02 struck; paragraph after the table: "**RETIRED {D} under SCA-005 (D-PEC-93):** \`E-N02\` — register row \`DEP-09-05-005\` kept with \`Status=RETIRED\`: DEL-06-04 is retired and the presence board no longer renders live hierarchy edges (A-33, A-38)." |
| DEL-03-01 (plan: E-P25, E-P18) | upstream row E-P25 struck; rows added: `\| DEL-02-08 (Work-graph parser) \| PROPOSAL \| CONSUMES \|  \| E-P81 \|` and `\| DEL-02-09 (MEMORY run-index parser) \| PROPOSAL \| CONSUMES \|  \| E-P82 \|`; paragraph: "**SCA-005 dependency refresh {D} (D-PEC-93):** \`E-P25\` is retired — register row \`DEP-03-01-014\` kept with \`Status=RETIRED\`, because \`_harness/adapter.yaml\` is a parity-peer input, not the feed manifest (A-07, A-18). \`E-P18\` (\`DEP-03-01-007\`) now cites PRD v2.3 PEC-RCN-002: each loop-registry row declares the feed profile the reconciler reads. \`E-P81\` and \`E-P82\` (\`DEP-03-01-015\`, \`DEP-03-01-016\`) add the work-graph and MEMORY run-index parsers (A-19, A-20)." |
| DEL-02-07 (completeness) | E-P25 downstream bullet struck (reason "\`_harness/adapter.yaml\` is a parity-peer input, not the feed manifest (A-07, A-18)", `DEP-03-01-014`) |
| DEL-06-04 (completeness) | 4 upstream rows struck (E-N09, E-N10, E-P46, E-P47); paragraph "**RETIRED {D} under SCA-005 (D-PEC-93):** DEL-06-04 is retired (A-34; SOW-029 OUT). Every row of \`Dependencies.csv\` is kept with \`Status=RETIRED\` — tree anchors \`DEP-06-04-001\`/\`002\` and execution rows \`DEP-06-04-003\`..\`006\`; the struck edges above no longer gate or feed any deliverable."; E-N02 downstream bullet struck (`DEP-09-05-005`) |
| DEL-07-02 (completeness) | 2 upstream rows struck (E-A03, E-P48); the same paragraph form (A-35; SOW-035 OUT; `-001`/`002`, `-003`/`004`); E-P46 downstream bullet struck (`DEP-06-04-005`) |
| DEL-07-04 (completeness) | 2 upstream rows struck (E-A04, E-P50); paragraph (A-78; SOW-037 OUT) |
| DEL-07-05 (completeness) | 2 upstream rows struck (E-N01, E-P14); paragraph (A-36; SOW-087 OUT), placed before the existing D-PEC-66 "DECLINED" paragraph, which stays byte-unchanged |

DEL-01-06's mirror (E-P18 downstream bullet) is unchanged, because the edge survives. DEL-08-02's struck E-N13 bullet is unchanged.

## Finite verification

Run from the repository root (and `projects/pec` where noted) with `PYTHONDONTWRITEBYTECODE=1`. Record every command, exit code and output under the run root.

| Check | Command | Required result (option A) |
|---|---|---|
| Preconditions | the generator's built-in checks; plus the ruling and its register row on fetched `origin/main`; `pec_reliance_hold.py --operation dispatch-for-production` on every target before dispatch, and `rely-for-production` before fan-in | preimages as tabled; `ALLOW` everywhere; otherwise stop and route the exact discrepancy |
| Strict registers | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` | exit 0; 66 registers; 263 rows; **0 errors / 0 warnings** (both DRB-008 cleared) |
| Closure | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <run root>/closure` | exit 0; `subject_status` PASS; **111 edges; 66 nodes; 0 SCCs; 0 bidirectional pairs; 0 orphans; isolated exactly DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05**; hub DEL-03-01 only. Option O: 112 edges, the same isolated set |
| Schema per register | `python3 tools/validation/validate_dependencies_schema.py <path>` for the 8 registers written | VALID ×8 |
| Minimum fileset | `zsh tools/validation/check_min_viable_fileset.sh <folder>` for both new folders | PASS ×2 |
| Byte identity | recompute SHA-256 of the 31 paths; at `{D}` ≠ 2026-09-25, the slot rule | equal to the table |
| Containment | `git diff --name-status origin/main...HEAD` | exactly the 31 product paths, `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_*/**`, `_Evaluation/DecompCoverage/_LATEST.md` and the run root — nothing else |
| Whitespace | `git diff --check origin/main...HEAD` | clean (`.gitattributes` gives `projects/pec/execution/**/Dependencies.csv` `whitespace=cr-at-eol`; without it, 31 CR-at-EOL notices on CSV rows are expected) |
| Row conservation | for each of the 8 touched registers, the `DependencyID` set after is a superset of the set before, and `ACTIVE` rows gain only the 8 added | holds |
| Quote currency (new rows) | every new or refreshed `EvidenceQuote` is a verbatim substring of its `EvidenceFile` | holds (the generator asserts it) |

### Re-audit and audit pointer

After the product writes are verified, and before publication, WORKING_ITEMS dispatches one TASK under `chirality-root:bundled:workflow:audit-decomp` with these parameters:

- `DECOMP_VARIANT=SOFTWARE`, full scope (`ALL`);
- `EXPECTED_SOURCE_SNAPSHOT` = decomposition revision 1.5 `current_basis` (`dc2b8479…9660`), SCA-005 closed for scope change only, plus the D-PEC-93 poststate;
- prior run `COV_SCA005_POSTCHANGE_2026-09-25_1344` (`coverage_summary.json` `912610ff…4deb`) for the comparison.

The snapshot folder comes from `tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV SCA005_POSTSETUP`, giving `COV_SCA005_POSTSETUP_{YYYY-MM-DD}_{HHMM}/`. It holds the method's eight required files plus `PrePost_Comparison.md`, and the audit writes nothing else.

Expected results:

- **Cleared:** COV-001/002 (BLOCKER), COV-070/071 (WARNING), COV-068/069 (INFO) and COV-079/080/081 (the pre-B3 INFO rows). Forward production-unit coverage returns to 100 %.
- **Unchanged:** the three PRE-EXISTING v2-artifact-location warnings (COV-006/008/042) and COV-077/078 (B1 open; they clear only under the B1 add-on).
- **New:** the closure tool's six isolated units, reported as expected.
- **Carried:** COV-072 (the plan-count defect) is historical text in the accepted plan; the re-audit may carry it or mark it resolved by the `RUN_SUMMARY.md` correction.
- **Expected verdict:** 0 blockers; `overall_status` WARN.

**Pointer.** Recommend including the `_Evaluation/DecompCoverage/_LATEST.md` move. D-PEC-92 did not open it, the group-3 record left it to the audit workflow's owner, and the audit method's own final step is the pointer update. Act: only if the re-audit reports 0 BLOCKERs, run `tools/scaffolding/update_latest_pointer.sh projects/pec/execution/_Evaluation/DecompCoverage COV_SCA005_POSTSETUP_{YYYY-MM-DD}_{HHMM}` (`21899520…10cb25`). Preimage `0084d218b6106482dbf3f73933d44de5ed43c15b8515b48c70b098c985df7432` (names `COV_SCA004_POSTCHANGE_2026-08-03_1442`). Postimage, exactly the tool's two lines: `Latest: COV_SCA005_POSTSETUP_{YYYY-MM-DD}_{HHMM}` and `Updated: {date}`. The hand-added paragraph in the current pointer is not carried. If any BLOCKER remains, the pointer is not moved and WORKING_ITEMS returns the findings.

### Independent verifier

A fresh read-only TASK that authored nothing applies `chirality-root:bundled:skill:software-code-review`, adapted to governed metadata, and returns a verdict file. Defects return to the author; the verifier does not repair. It checks:

1. **Basis.** The ruling and its register row are on `origin/main`. The run-root copy of the generator hashes `cfae0052…d6c2`. The recorded preimages match `6dac281c6`.
2. **Reproduction.** It reruns the generator on a fresh `git archive` export of the preimage commit at the actual `{D}` and gets a byte-identical tree for the 31 paths.
3. **The fixed checks.** It reruns the verification table and gets the same numbers.
4. **Semantics.**
   - Every `_CONTEXT.md` field equals its revision-1.5 `Deliverables.csv` cell.
   - Every retired row maps to its accepted action (A-07, A-18, A-33, A-34, A-35, A-36, A-38, A-78).
   - The four new EXECUTION edges are warranted by PEC-RCN-002 and the DEL-01-01 register row, and none duplicates a pair.
   - Every mirror strike corresponds one-to-one to a retired row, and nothing retired remains unstruck in any mirror under option A.
   - No row is deleted.
   - The only lifecycle writes are the two new `OPEN` files, stamped `TASK+preparation`.
5. **Containment.** The changed-path containment check passes, the SCA-005 snapshot and all `checkpoint_snapshots/**` are byte-unchanged, and no `_Decomposition/**`, `docs/PRD.md`, `ScopeOfWork.md`, other `_STATUS.md`, other `_CONTEXT.md` or `_REFERENCES.md`, `v2/**` or pointer other than `DecompCoverage/_LATEST.md` changed.
6. **Audit.** The snapshot is new and immutable, cites the expected source, includes the comparison, and supports the pointer decision.

## Administrative grant

- **Scope.** WORKING_ITEMS owns this PROJECT_SETUP act only (project-setup Phase 2.1 for two folders, plus B3). Work graph: one bounded TASK author runs the generator (the eligible `preparation` actor, recorded as `TASK+preparation`); one TASK runs `audit-decomp`; one fresh read-only TASK verifier. The manager runs the reliance preflights and the pointer step.
- **Run root.** `execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_{D}/` (in the default-writable fence) holds:
  - `gen_d93.py` (exact bytes above) and its stdout report;
  - `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the SCA-004 PROJECT_SETUP format;
  - the closure output directory;
  - the strict-validator and schema outputs and the preflight results;
  - `VERIFIER_VERDICT_NN.md`.

  Probe scripts live here, never under a deliverable folder. The generator writes no `_run_records/` entry in any deliverable.
- **Records not opened.** The SCA-005 snapshot folder, `checkpoint_snapshots/**` and both revision/scope-change `_LATEST.md` pointers. The SCA-005 open-work ledger is closed out in this run root's `HANDOFF_STATE.md`, not by editing the accepted snapshot (SCA-004 precedent, Propagation_Plan §B2).
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for manager, author, auditor and verifier, as under D-PEC-87/89/91, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** CHANGE owns branch, commit, push, PR, merge and `origin/main` observation under the standing Git authorization of 2026-09-12. The register row, receipt and `docs/STATUS.md` / `README.md` lines are ordinary loop records maintained by HELP_HUMAN under D-PEC-88.

## Rollback

- **During execution.** The generator writes nothing unless every check passes. If a later check fails before publication, discard the slice branch; nothing reaches `origin/main`.
- **Before merge.** Close the PR and discard the branch.
- **After merge (owner direction).** CHANGE reverts the slice PR's product paths and the pointer in a revert commit (history preserved; no reset). That restores:
  - the 19 modified preimages tabled above;
  - `DecompCoverage/_LATEST.md` `0084d218…7432`;
  - the absence of the two new folders (12 files) — the one case where a revert removes files, and they are exactly the files this act created.

  The `COV_SCA005_POSTSETUP_*` snapshot and the run root stay as non-current evidence, with a rollback note appended to the run root's `HANDOFF_STATE.md`. No other file is touched; no silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, P, O or B1, grants none of the following:

- any `ScopeOfWork.md`, `v2/**`, `software-workflow.json`, `docs/PRD.md` or `_Decomposition/**` write (decomposition text, registers, `_LATEST.md`), or any SCA-005 snapshot or `checkpoint_snapshots/**` write;
- any lifecycle change beyond creating the two `_STATUS.md` files at `OPEN`. No other `_STATUS.md` is touched; no `## Remaining` entry is written;
- `CHECKING`, `ISSUED`, artifact acceptance or any readiness or reliance claim. The owner reserves any CHECKING declaration to their own initiative (D-PEC-87 ruling, L-2a as amended). CHECKING is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it;
- any `_CONTEXT.md` or `_REFERENCES.md` write outside the two new folders (unless B1 is selected);
- any `_DEPENDENCIES.md` or `Dependencies.csv` write outside the tabled paths, including the evidence-quote currency rows of finding 1;
- a pointer move other than `DecompCoverage/_LATEST.md` under the stated condition;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md` and `_COORDINATION.md`;
- a schedule reading: blocker output stays advisory (FULL_GRAPH, threshold INITIALIZED).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, P, amend or defer; and whether to add O and/or B1.** Recommendation: **A**, without O and without B1.
2. **The five completeness mirrors** (DEL-02-07 and the four retired deliverables' own `_DEPENDENCIES.md`), which the plan's list does not name. Include them (A, recommended), or take the plan's list only (P).
3. **The `DecompCoverage/_LATEST.md` move.** Include it, conditional on a re-audit with 0 BLOCKERs (recommended), or leave it for a later act.
4. **Evidence-quote currency (finding 1)** — the 16 SCA-005-stale quotes and 3 older ones. Carry them as a recorded residual for a later `dependency-extract` refresh or packet (recommended), or amend this packet to refresh them now (re-preparation needed: new exact quotes for 19 rows in 10 registers).
5. **Actor string and model steer.** Keep `TASK+preparation` and the default models above, or state others.

## Preparation evidence

All of it ran in a fresh `mktemp -d` directory under the host's temporary area, outside the session scratchpad and the checkout (path given in the TASK return):

- `base` is a `git archive` export of the whole tree at `6dac281c6`;
- each `proto*` is an APFS clone of `base` (`cp -Rc`) with a variant applied by the generator.

Nothing was written to the checkout or its repository. The interpreter was Python 3.13.7 (CPython), and the local date was 2026-09-25.

| Command (scratch) | Exit | Result |
|---|---|---|
| strict validator on `base` | 1 | 64 registers, 255 rows, 0 errors, 2 warnings (DRB-008 DEL-02-08, DEL-02-09) — equals the C2 record |
| closure on `base` | 0 | 119 edges, 64 nodes, 0 SCCs, 0 bidirectional pairs, isolated DEL-00-03, DEL-01-05; hub DEL-03-01 (24) |
| `gen_d93.py` on `protoA` (`--act-date 2026-09-25`) | 0 | 31 writes as tabled; `check_min_viable_fileset` PASS ×2 |
| `gen_d93.py` on a second fresh clone | 0 | byte-identical tree and report (deterministic) |
| `gen_d93.py` rerun on the applied `protoA` | 1 | fails closed on the first preimage; nothing written |
| `gen_d93.py --act-date 2026-09-26` | 1 | "local date … != --act-date"; tree unchanged (`diff -rq` empty) |
| strict validator on `protoA` | **0** | 66 registers, 263 rows (ANCHOR 140 / EXECUTION 123), evidence file populated and resolving 263/263, **0 errors / 0 warnings** |
| closure on `protoA` | 0 | **111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs**, 0 orphans, 0 invalid IDs, isolated the six named; checks: `isolated_units` and `hubs` WARNING, everything else PASS |
| schema validator on the 8 written registers | 0 ×8 | VALID |
| `protoP` (`--mirror-set plan`) | 0 / 0 / 0 | 26 writes; strict 0/0; 111 / 66 / 0 / 0 |
| `protoO` (`--optional-edge`) | 0 / 0 / 0 | 33 writes; strict 0/0; **112** / 66 / 0 / 0; isolated the same six |
| `protoB` = `protoA` + `gen_d93_b1.py` | 0 / 0 / 0 | 42 contexts + 64 references; strict 0/0; 111 / 66 / 0 / 0 |
| D-PEC-62 order (scaffold → remove stub → `write_status.sh`) against this packet's order | — | `_STATUS.md` and `_SEMANTIC.md` byte-identical for both folders |
| `git diff --no-index --check` with `core.whitespace=cr-at-eol`, `base`→`protoA` and `protoA`→`protoB` | — | empty output |
| `audit_structure.py` / `audit_dependencies.py` (`--variant SOFTWARE`), `base` vs `protoA` | 0 | units 64 → 66, all pass; lifecycle OPEN 28 → 30; register files 64 → 66, schema-valid 66/66, anchor files 66/66, evidence 263/263; the two pre-existing structure issues (untracked empty package subfolders in an export; tool roots) unchanged |
| evidence-quote currency scan (ACTIVE EXECUTION rows) | — | `base` 27 non-verbatim; `protoA` 19 (16 SCA-005-induced, 3 older) — finding 1 |
| `pec_reliance_hold.py … --operation exact-correction-preparation` (in the checkout) | 0 ×36 | `ALLOW` |

Scratch artifacts (in the preparer's `h8/` folder, for HELP_HUMAN's run evidence):

| Artifact | SHA-256 |
|---|---|
| `gen_d93.py` (the bound generator) | `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2` |
| `gen_d93_b1.py` (B1 add-on) | `eff5d2fb6811ad6fb4a08e995b1a6444ff2be456358d19ff4c39de0fc6f1677c` |
| `protoA_vs_base.diff` (option A, rendered at 2026-09-25) | `99c95ad2c0ed2c3359626ba2783f1f11597f94fe5a9c891b22876a12e6f581e7` |
| `protoO_vs_protoA.diff` (option O increment) | `4e701af0797c4958d4115192a26caf4997aa366c2a7760236363113aa3b1c25f` |
| `evidence/` (generator reports, validator and closure outputs for base / A / P / O / B, structure and dependency audits, hold results) | listed in the TASK return |

Basis read for preparation, at `6dac281c6`:

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| SCA-005 `Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| SCA-005 `Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| SCA-005 `Amendment_Actions_CP2.csv` | `7bb3bada88ed20adccab6a4077d77d2d7702f03637db230d88f862dea2a09987` |
| SCA-005 `Impact_Assessment.md` | `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
| SCA-005 `RUN_SUMMARY.md` | `e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518` |
| SCA-005 `Handoff_State.md` | `a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a` |
| SCA-005 `Decision_Log.md` | `09f99fb175c0b81c23b4f680babd04272a8e1e4126887f30582d7a072bb95a6e` |
| group-2 `DECISION.md` / `ACCEPTED_MANIFEST.csv` | `ca88f6a8f9bca197f64a56f07c73364cd8f7533acb7bf64206a34e0e1fba3d66` / `10d2c250e2d2daf3d5f43a145c3fbcaf29863f16b005c47dd5999fbd7788b9dc` |
| group-3 `DECISION.md` / `ACCEPTED_MANIFEST.csv` | `35c211a604cb7a05d3fca5cec86fe6bb297a095ad6aa7c5efa72b2cd1599f673` / `1eb20bc9d9cd9b37b205e6d0e29a4392b9b6fb165f57c756e76fcf912fd13dc7` |
| `…/_DECISIONS/_REGISTER.md` (rows D-PEC-86, D-PEC-92; no D-PEC-93) | `993b8e80d758db92b4aebebf705393954010dc939fe14f751ea7467ad030a044` |
| D-PEC-91 proposal / ruling | `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec` / `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| D-PEC-62 packet | `4aa1b83b9701b005307e3ea93696ac5b83e2e4f123243ffac6237314a7498924` |
| `SEED_D-PEC-62/scaffold_pec.py` / `seed_local_dependencies.py` | `01b04b5f1bbe068ecf2f87e9c0c2ef113c575bbbf16e92d17796e43e12c3ceca` / `137d9d19cfec5f95730c06e370d48d31352c97aba4218f4034b6ef320ea8c37a` |
| SCA-004 PROJECT_SETUP `MANIFEST.md` / `VALIDATION.md` / `HANDOFF_STATE.md` | `c6e2346154fcf5c62b7f8056c5a2c6ae904dce6aca3cc13ae5a97e4c17a92170` / `7f18561bf0cc8bc699c95c94bf04b72dc0d3b28c2255d9a0fbf9056861b21037` / `93a3337b3c1f4ebee5ccee48a191e8a67ea4b080dedf88a82b6bcc7af6b58b1f` |
| `_Decomposition/SOFTWARE_DECOMP.md` (rev 1.5) | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `_Decomposition/_LATEST.md` / `_ScopeChange/_LATEST.md` | `1f2cdcba31b3db2fd8818b16202d2bbc89c3f4a20702a962d133a73e10f556b6` / `a2b5b789d996d52aa43c86419c9a4f02d1aa01f438f1616f3d51921e34f84268` |
| `docs/PRD.md` (v2.3) | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| `workflows/project-setup/` `WORKFLOW.md` / `contract.md` / `method.md` | `51c1cb9f7492aa28aaaa3f042ba3404e344f5870ff85f318112e05c4fdbea5a2` / `a99966c5873748c5b327baee80ef3e805e26a89600ccf3b9b5f9aacec883145f` / `ce23e911e2f35e8c0644f344f096a39a46be95056736249c18b55c126fbb75ed` |
| `workflows/dependency-extract/WORKFLOW.md` | `b79b011c44f21a311e1ffa49295ef50ea6b3644ca6c52a2aacfbfc393d26b18f` |
| `workflows/audit-decomp/` `WORKFLOW.md` / `contract.md` / `method.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` / `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` / `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` |
| `workflows/audit-dep-closure/WORKFLOW.md` (read; its analyzer is the closure check above) | `b436fa343058795398633410bd9e0abd19a37dc5b2869c14617016df5e63fcb1` |
| `tools/validation/validate_decomposition_registers.py` / `validate_dependencies_schema.py` | `590d9aa368c84230533d84819c53e52b441f48904f602446ec174f68cfe08818` / `75cd74768cc8edf91c6f40b582f0fb570d2427894e6c2236ea2fe7d384291f5f` |
| `tools/coordination/analyze_dep_closure.py` / `tools/evaluation/audit_common.py` | `fe546d0f18aac3ab44866d55d6e6ca39c2b6d323ee0355e923b01106a1698ccd` / `2d5eb4f62cc3fb13cce39b2e80ee92f55ff737fed181f98745a63966f1fef026` |
| `tools/scaffolding/create_snapshot_folder.sh` / `update_latest_pointer.sh` | `2a01157959d7ac8fe55cd621c43ef61118b83370778f3f24cf54a4641fd1c361` / `21899520ab84e0d88056b19a4318810cc3a730bc4b6d22e7ec66291549f015bc` |
| `COV_SCA005_POSTCHANGE_2026-09-25_1344/coverage_summary.json` / `Decomp_Coverage_IssueLog.csv` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` / `e4a9633a7df410c416826d944eb6bc4f41cd6bfb36cf248c9c5ed31aba46af5c` |
| `execution/_Coordination/_COORDINATION.md` | `8da03a2f0157ba097e4db5b34dff4cd68c03e69c5d0ec72f8a8f49c23d38879c` |
| Brief H8 (scratch) | `8f040e8d83061820e6a5e98958ce0aba4648096b8474f91123fe63b7bbc13c78` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node H8, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
