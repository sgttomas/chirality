# D-PEC-101 (provisional) — Revision-1.6 currency and setup packet: context and reference re-pin (K4), and DEL-08-06 / DEL-10-13 setup with dependency rows, SOW-097..100 anchors and two evidence-quote refreshes (K1) — proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph nodes K4 and K1) for the PEC loop, 2026-09-26 (session date), from brief `K14P_REV16_CURRENCY_SETUP_PROPOSAL.md` (SHA-256 `3c16bb93710b63429cd04b3ccb8d41bc5620584965dcb5228218c3dfaf1f38b1`; copy in `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`) and its HELP_HUMAN amendment of the same day (below). No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every prototype ran on scratch exports only. It asks for two new `OPEN` lifecycle files (K1) and no other lifecycle change. The number `D-PEC-101` is provisional. K1's output embeds it (row Notes, provenance, `_DEPENDENCIES.md` Status and Run History, refresh Notes, the `_REFERENCES.md` closing line, the Declared Upstream text and the DEL-10-13 Run Notes), so a different final number requires rebuilding the K1 generator, its tables and aggregates, and a fresh review; K4's output bytes carry no packet number (only the K4 generator's docstring names it). `D-PEC-100` is provisionally taken by the S2 Scope of Work rebuild packet prepared at the same time, which is why this packet is numbered 101. HELP_HUMAN assigns the final number, files the packet in `_DECISIONS/` and adds the `_REGISTER.md` row. At `aca930622` the register's last row is `D-PEC-99` and no file under `projects/pec` carries `D-PEC-101`. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md`.

The two parts are **separately rulable** (as `D-PEC-95` offered N1–N3): K4 and K1 touch disjoint paths and neither generator writes the other's targets (K1 reads the PKG-08 and PKG-10 sibling `_CONTEXT.md` files, which are K4 targets, only to check package names; K4 run after K1 reads K1's new context and reference files through its population check, which tolerates them); the prototypes prove either order gives the same tree.

## Provenance

- **Owner acts relied on.**
  - SCA-006 checkpoint 2 (2026-09-25): "SCA-006 CP2: accept; Q1 a; Q2 a" (`_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md`, `30aebd16…abf989`; register row `D-PEC-97`). It accepted `Propagation_Plan.md` (`f95d00d1…87d7d8`), whose Lane B names B1 (scaffold DEL-08-06 and DEL-10-13), B2 (their dependency rows and the SOW-097..100 anchors), B3 (re-quote DEP-09-06-003 and DEP-10-03-003) and B7 (re-pin to revision 1.6 / PRD v2.4), each "under a later `D-PEC` packet". Under Q-CP2-2 (a) the group-2 packet opened Lane A only: the option text (`Propagation_Plan.md` L545) says it "does **not** open B1 (PROJECT_SETUP for DEL-08-06 and DEL-10-13) or any other Lane B item".
  - SCA-006 checkpoint 3 (2026-09-26): "SCA-006 CP3: accept; Q1 a; Q2 a." (`…/SCA-006_GROUP-3_2026-09-26/DECISION.md`, `22aad7eb…036bc6`). Revision 1.6 is `current_basis` (`_Decomposition/SOFTWARE_DECOMP.md` `9374c21f…908eb1`, front matter `revision: "1.6"`, `status: current_basis`), PRD v2.4 is the product definition of record (`docs/PRD.md` `ae49b806…483fbe`), closure `CLOSED_FOR_SCOPE_CHANGE_ONLY`, and the audit pointer names `COV_SCA006_POSTCHANGE_2026-09-26_0051`. `RUN_SUMMARY.md` §6 (`6c627456…b92b`) lists B1–B3 and B7 as `FROZEN` until their own packets.
  - The owner's 2026-09-25 steering, recorded in `D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…1e5a6b` at `aca930622`): "You can continue with all the open work you identified." HELP_HUMAN's work graph (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`, `f2cdfb0e…384f6` at `aca930622`) turns this into nodes K1 and K4, both "READY — packet preparation; R3 met".
- **Brief amendment (HELP_HUMAN, 2026-09-26, recorded here as received).** It replaced the brief's "Method choice as an owner option" bullet: Root's notice says the owner defers action in PEC and "no adoption, `SETUP_LOG.md` baseline or incremental setup run is expected in this loop now", so K1 is prepared on PEC's current practice (the `D-PEC-93` precedent), the `project-setup` `INCREMENTAL` mode is disclosed in one line only, and its adoption is **not** put to the owner.
- **Resume amendment (HELP_HUMAN, 2026-09-26, recorded here as received).** Keep the human-owned `_COORDINATION.md` Notes line as a separate optional owner question with exact replacement text, applied by HELP_HUMAN only if the owner authorizes (question 4); drop the DEL-10-13 C-08 question if it can wait for K2 without affecting this packet's bytes (it can: finding 4); confirm no pinned preimage changed at the newer `origin/main` and rerun the checks there (see Source state); leave the "Update the PR base" CI failure to HELP_HUMAN.
- **Fence.** `projects/pec/AGENTS.md` (`df9196d1…eb8` at `aca930622`) §"Write Scopes And Fences": only `execution/_Coordination/**`, `AGENTS.md` and the one-time STATUS pointer are default-writable; every other write under `projects/pec` needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. `F-PEC-1` (`D-T0-15`, `95c245b5…0b09`) is the outer fence. No earlier ruling opens any path below.
- **Intent of record.** SCA-006 `Propagation_Plan.md` §B1, §B2, §B3, §B7 and §"Derivative status per package"; `Impact_Assessment.md` (`93253b7d…cb691`) §9.1, which lists the expected edges "for extraction"; the post-change audit `COV_SCA006_POSTCHANGE_2026-09-26_0051` (issue log `37f4f6dc…026d3`), whose EXPECTED_CONSEQUENCE rows COV-003/004 and COV-073/074 (the two absent folders), COV-075/076 (the two quotes), COV-077/078 (the re-pin) and COV-080 (no register traces SOW-097..100) are exactly this packet's scope. The plan is intent; the bytes below are this packet's.
- **Precedents.** `D-PEC-93` (proposal `46470575…f489422`, ruling `ffb0b582…3709`): folder naming, `write_status.sh` then `scaffold_deliverable.sh`, zero-byte `_SEMANTIC.md`, deterministic rows "outside the dependency-extract lifecycle by packet ruling" (D-PEC-62 §3.2), mirror bullets, revert-PR rollback and the partial-failure and same-day-reproduction clarifications of its ruling. `D-PEC-95` (proposal `9137d387…4b22`, ruling P + R `51dceb71…beb`): the re-pin generator with pinned preimages, exact postimages and anchor lines only, add-on R for a covers bullet the new revision contradicts, and the N3 quote-refresh representation (`EvidenceQuote`, `LastSeen` = act date, `Notes` prefixed "Evidence refreshed under …").
- **Source state.** Every hash here was read at `origin/main` `aca930622ba167689881416044ba0feaee3ef003` (PR #958), from a `git archive` export. The preparation branch `claude/pec-rev16-currency-setup-proposal` was cut from that commit and changes only this preparation folder, the brief copy and the return. During preparation `origin/main` advanced to `dfb089b8abae48ee699117c5bc167301963b2ab5` (PR #961, PEC work graphs and review returns; PR #960, App files). Between the two commits nothing under `projects/pec` changed except the two work graphs and two review returns, and no tool, workflow or index changed: every pinned preimage and basis hash below is the same at both. Both generators rebuild byte-identically from an export of `dfb089b8a`, and the K1 prototype suite, the combined K4 + K1 runs and the git-backed checks were rerun there with identical postimages (`k1/evidence/`; the first run is kept in `k1/evidence_aca930622/`). The act re-verifies preimages at whatever commit it runs on.
- **Methods (from `workflows/index.json`, `2bfa2c5f…fb3`).** `chirality-root:bundled:workflow:project-setup` (`WORKFLOW.md` `7aa4c30a…dd6d`, `resources/method.md` `37c285a2…f042`, `resources/contract.md` `e9f0d11b…c218e`); the ordered `methods` field `[{kind: "skill", name: "preparation", source: "bundled", sourceRootId: "chirality-root"}]` (`.agents/skills/preparation/SKILL.md` `0662dc88…6d38`, `references/scaffold-contract.md` `aa95078f…cda4`, `execution.json` `dd59f002…ec2d`); `chirality-root:bundled:workflow:dependency-extract` (`WORKFLOW.md` `e5523eba…f18c3`, `resources/checks.md` `a12aa8b3…0457`) whose Function 5 checks are applied as acceptance checks; `chirality-root:bundled:workflow:audit-decomp` (`WORKFLOW.md` `7ba6291c…246b`) for add-on V; `chirality-root:bundled:skill:software-code-review` (`SKILL.md` `ee085d58…888bca`) for the verifier. No project `.chirality/workflows` or user `~/.agents/skills` / `~/.chirality/workflows` origin exists on this host, and the bundled **workflow** named `preparation` that `D-PEC-93` disclosed as a same-name collision no longer exists (`workflows/preparation/` is absent at `aca930622`).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`), run from `projects/pec` with `--operation exact-correction-preparation`, returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0 for all **161** targets: K4's 129 paths and K1's 32 (`evidence/hold_targets.txt`, `evidence/hold_results.tsv`). Before dispatching the K4 preparation TASK, the manager also ran `dispatch-for-production` on K4's 132 candidate files (all `ALLOW`; that first run's output was not kept, so it was rerun and recorded in `evidence/hold_dispatch_k4_candidates.tsv`, 132/132 `ALLOW`).

## What preparation found

### K4 — the re-pin population (recounted at `aca930622`)

{{K4_CENSUS}}

### K1 — folder names, method and file forms

- **Folder names.** The project rule is `D-PEC-62` §3.1 ("`{ID}_{Label}` where Label = deliverable/package name with non-alphanumerics mapped to `_`, runs collapsed, no leading/trailing `_`"), which `D-PEC-93` applied. It gives `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/` and `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/`, exactly the paths the plan anticipated.
- **Method.** WORKING_ITEMS with `project-setup`; the scaffold is the `preparation` skill's deliverable fileset operation through the repository tools, as in `D-PEC-93`: create the empty folder, `tools/scaffolding/write_status.sh <folder> OPEN TASK+preparation` (`1857ad59…97bc`; it changed since `D-PEC-93` but writes the same bytes, checked), then `tools/scaffolding/scaffold_deliverable.sh` (`7a04c1a9…7a23`), which skips the existing `_STATUS.md` and creates the four stubs, and finally `tools/validation/check_min_viable_fileset.sh` (`a6c4af3c…20f8c`). `dependency-extract` cannot produce the rows as specified, for the reasons `D-PEC-93` gave (the new deliverables have no source documents; edges are warranted by the accepted register and PRD, not by their own SOWs), so the rows are bound by the generator and its Function 5 checks are acceptance checks.
- **Where the files follow the precedent and where they follow the skill.** `_CONTEXT.md` uses the `D-PEC-62` field table, templated from the revision-1.6 `Deliverables.csv` row, with a `D-PEC-101` provenance paragraph born at revision 1.6. `_REFERENCES.md` uses the `D-PEC-93` seven-bullet form at revision 1.6 and PRD v2.4, with the SCA-006 snapshot folder (A-28 / A-29). `_SEMANTIC.md` stays a zero-byte stub and `_STATUS.md` is the `write_status.sh` form, as in all 66 existing folders (the skill's `PLACEHOLDER` lens and `# Status: <ID> <Name>` heading are not used; disclosed). **`_DEPENDENCIES.md` follows the D-GOV-46 heading schema** (`docs/SPEC.md` §5.2; Root notice `NOTICE_2026-09-26_DEPENDENCY_SCHEMA_D-GOV-46.md`, `33e8d77b…790f`: "New files use the amended schema"): the preparation skill's skeleton exactly, Mode `FULL_GRAPH` from `_COORDINATION.md`, both declared sections reading "None declared at setup" (nothing is a human declaration), and the Extracted Dependency Register section carrying the seeded rows as a table (status `SEEDED … under D-PEC-101 … outside the dependency-extract lifecycle by packet ruling`). The register-wide rules C-04 and C-10 move into Run Notes, since §5.2 has no heading for them. Existing `_DEPENDENCIES.md` files keep their legacy headings, as the notice requires.
- **Incremental setup (disclosure only).** Root's `project-setup` now has an `INCREMENTAL` mode with a `SETUP_LOG.md` baseline for exactly this post-acceptance case (`NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md`, `8829ac84…f64af`); the owner has deferred its adoption in PEC, and this packet does not use it.
- **`_STATUS.md` bytes.** For each new folder, with `{D}` the act date and `<ID>` the deliverable:

  ```text
  # Status: <ID>

  **Current State:** OPEN
  **Last Updated:** {D}

  ## History
  - {D} — State set to OPEN (TASK+preparation)
  ```

  No `## Remaining` section is written (`D-PEC-99`). No existing deliverable's lifecycle changes. First Scope of Work contracts are node K2, not this packet.

### K1 — the dependency rows (B2) and the two quote refreshes (B3)

Edges follow the accepted plan's list (§B2, IA §9.1). Edge IDs continue the `E-P` series. `E-P79`..`E-P82` are in use; `E-P83` is skipped because `D-PEC-93`'s unselected option O named it in its generator bytes; `E-P84`..`E-P99` are unused anywhere in the repository (the generator re-checks every register and mirror). Every row is `PREREQUISITE` / `UPSTREAM` / `RequiredMaturity INITIALIZED` / `ProposedMaturity TBD` / `SatisfactionStatus PENDING` / `Origin EXTRACTED`, the corpus pattern for extracted rows. Strata follow C-10: an ID-named target reached through the accepted row's own words is recorded at the `DERIVED` stratum (`EXPLICIT` / `MEDIUM`), because "composes" is not in C-10's closed `DECLARED` verb list and the rows are not owner-exhibit edges; a target resolved by heuristic is `PROPOSAL` (`IMPLICIT` / `MEDIUM`). All strata require owner acceptance; this ruling is that acceptance.

| Row | From → To (edge) | Stratum / Kind | Locus (`EvidenceFile` — `SourceRef`) | `EvidenceQuote` (verbatim) |
|---|---|---|---|---|
| `DEP-08-06-003` | DEL-08-06 → DEL-08-01 (E-P84) | DERIVED / CONSUMES | `docs/PRD.md` — PRD.md §9.6 requirement PEC-API-007 | under the `agent` access class |
| `DEP-08-06-004` | DEL-08-06 → DEL-08-02 (E-P85) | DERIVED / CONSUMES | same | over the same versioned API and responses (PEC-API-003, PEC-API-004, PEC-API-006, PEC-ORI-007) |
| `DEP-08-06-005` | DEL-08-06 → DEL-08-03 (E-P86) | DERIVED / CONSUMES | same | same quote (PEC-API-004 and PEC-API-006 are SOW-043 and SOW-098, both DEL-08-03) |
| `DEP-08-06-006` | DEL-08-06 → DEL-04-01 (E-P87) | PROPOSAL / CONSUMES | `docs/PRD.md` — PRD.md §8 access classes (`agent` class) | class is read-only query access for tool calls: orientation |
| `DEP-10-13-003` | DEL-10-13 → DEL-03-04 (E-P88) | DERIVED / TESTS | `execution/_Decomposition/Deliverables.csv` — Deliverables.csv row DEL-10-13 Description | composes DEL-03-04 parity |
| `DEP-10-13-004` | DEL-10-13 → DEL-04-03 (E-P89) | DERIVED / TESTS | same | the DEL-04-03 reliance envelope |
| `DEP-10-13-005` | DEL-10-13 → DEL-04-05 (E-P90) | DERIVED / TESTS | same | DEL-04-05 coverage honesty under seeded feed failures |
| `DEP-10-13-006` | DEL-10-13 → DEL-10-02 (E-P91) | DERIVED / TESTS | same | the DEL-10-02 kill test |
| `DEP-10-13-007`..`-014` | DEL-10-13 → DEL-02-01, 02-02, 02-03, 02-04, 02-05, 02-06, 02-08, 02-09 (E-P92..E-P99) | PROPOSAL / TESTS | same | the PKG-02 parser fixture suites |

Tree anchors (`ANCHOR`, `EXPLICIT` / `HIGH` / `DECLARED` / `SATISFIED`, the `D-PEC-62` anchor field values): `DEP-08-06-001` `IMPLEMENTS_NODE` → PKG-08 and `DEP-08-06-002` `TRACES_TO_REQUIREMENT` → SOW-099; `DEP-10-13-001` → PKG-10 and `DEP-10-13-002` → SOW-100 (Notes `Tree anchor seeded under D-PEC-101`); and, appended to existing registers, `DEP-04-03-005` → SOW-097 and `DEP-08-03-005` → SOW-098 (Notes `Tree anchor seeded under D-PEC-101 (SCA-006 B2; A-24, A-30)` and `(…; A-25, A-32)`). Each new EXECUTION row's `Notes` is `<STRATUM>; Flag=none; EdgeID=<E>; seeded under D-PEC-101 (SCA-006 B2)`. After the act every IN scope item is traced by an ACTIVE `TRACES_TO_REQUIREMENT` row in the register of each deliverable it names (74/74 IN items; today 70/74), which is COV-080's closure condition.

**B3.** Revision 1.6 re-expressed the DEL-08-01 description (A-31). The two rows keep their IDs, loci and every other cell except the `Notes` prefix and `LastSeen` shown below:

| Row | Before (`EvidenceQuote`) | After (`EvidenceQuote`, the whole revision-1.6 cell) | `Notes` prefix; `LastSeen` |
|---|---|---|---|
| `DEP-09-06-003` (DEL-09-06 → DEL-08-01, E-N06) and `DEP-10-03-003` (DEL-10-03 → DEL-08-01, E-P54) | Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006. | Local-only Unix-socket binding with token-scoped access classes (owner, harness, agent, admin; agent is read-only query for tool calls); auth-reuse choice tracked by OI-006. | `Evidence refreshed under D-PEC-101 (SCA-006 A-31: DEL-08-01 description re-expressed); ` ; `{D}` |

No `_DEPENDENCIES.md` mirrors either quote. After rendering, **127/127** ACTIVE EXECUTION quotes are verbatim in their evidence files (today 109/111; the two stale rows are COV-075/076).

**Mirrors.** Today every ACTIVE EXECUTION edge appears once as a `| E |` row in its source's `_DEPENDENCIES.md` and once as a `[E]` bullet in its target's (checked: 111/111). K1 keeps that invariant: each new edge is a table row in the new file's Extracted section and one appended downstream bullet in its target's file, in the form `- DEL-08-06 (Agent tool-call query surface) — CONSUMES [E-P84]` or `- DEL-10-13 (Reliance-advertisement gate) — TESTS [E-P88]`. Fourteen targets append to their existing "Downstream (informational; consumers of this deliverable)" section; DEL-04-05 and DEL-10-02 have none, so the same legacy heading is inserted (before "Non-gating constraints" and before "Standing obligation (constraint C-08)", following DEL-03-04's section order). Mirror edits only add lines (checked). DEL-08-02 is `CHECKING`; its `_DEPENDENCIES.md` gains one bullet, which is deliverable metadata, not the artifact under checking (the `D-PEC-95` stance).

### Topology and validators (observed on the prototypes)

- **Closure** (`tools/coordination/analyze_dep_closure.py`, `2b8de3cb…a9adc`, which since the D-GOV-46 follow-ups reads the union of `Dependencies.csv` rows and the declared sections, legacy informational downstream bullets included): 111 edges / 66 nodes today → **127 edges / 68 nodes, 0 SCCs, 0 bidirectional pairs, 0 orphans, 0 declared disagreements**, isolated the same six (DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05), hub DEL-03-01 only (degree 25, unchanged). `declared_only_rows` 111 → 127 (the new downstream bullets), `declared_unread_count` 136 unchanged (the new files' table sits in the Extracted section, which the union does not read). DEL-08-06 and DEL-10-13 have no dependants, so no cycle can form.
- **Strict registers** (`tools/validation/validate_decomposition_registers.py`, `869df1d5…57ee`): today exit 1 with 0 ERROR, 26 WARNING XRG-013 and 2 WARNING DRB-008 (66 registers, 263 rows). After K1: exit 1 with **0 ERROR, 26 WARNING XRG-013, 0 DRB-008** (68 registers, 285 rows; ANCHOR 146, EXECUTION 139). The 26 XRG-013 are the pre-existing D-GOV-48 package-home warnings (same 26 IDs), on which the owner defers action; this packet does not act on them. K4 alone leaves the output byte-identical to today's.

### Findings beyond the brief (disclosed)

1. **Add-on C — two stale "covers" bullets.** Revision 1.6 added SOW-097 to DEL-04-03 and SOW-098 to DEL-08-03 (`CoversScopeItems` `SOW-006;SOW-007;SOW-097` and `SOW-043;SOW-098`), and their A2 contexts already say so, but their `_REFERENCES.md` still read "covers SOW-006;SOW-007" and "covers SOW-043". K4 as briefed leaves semantic fields untouched, so those two files would newly name revision 1.6 next to a coverage list revision 1.6 contradicts, the case `D-PEC-95` add-on R handled for the retired four. Add-on C (`--covers`) rewrites that one bullet in each to the register value. It adds no path. Every other `_REFERENCES.md` covers list agrees with its register (the retired four in their add-on R form).
2. **DEL-02-07 is not given an edge.** The plan says "the PKG-02 parser deliverables". Eight PKG-02 deliverables are named parsers; DEL-02-07 is the "`adapter.yaml` feed-manifest consumer", read "as a parity-peer input only", whose output reaches the gate through DEL-03-04 parity. Adding it (a ninth PROPOSAL edge, E-P100) is an amend.
3. **DEL-08-06 → DEL-04-03 is not added.** PEC-API-007 cites PEC-ORI-007 (SOW-097, DEL-04-03), but the accepted plan lists DEL-04-01, and DEL-08-06 already reaches DEL-04-03 through DEL-08-03 → DEL-04-03 (E-P53). The same reasoning `D-PEC-93` gave for omitting its option O applies. Adding it is an amend.
4. **DEL-10-13 and constraint C-08.** The accepted row says the gate is "re-proved at each such release" and consumes no internals "(as DEL-10-02)"; DEL-10-02 and DEL-03-04 are C-08 standing nodes (owner-confirmed at `D-PEC-62`). Classifying DEL-10-13 as standing changes one-shot blocker arithmetic and is an owner classification. The new `_DEPENDENCIES.md` records the observation in Run Notes and makes no classification, so the question can wait for DEL-10-13's first Scope of Work (node K2): neither later answer changes any byte of this packet, and it is not asked here.
5. **Later `dependency-extract` runs.** Under the D-GOV-46 follow-ups (`NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md`, `4f06f230…6a11`; PEC defers adoption), a future `dependency-extract` run would mirror legacy informational downstream bullets into `Origin=DECLARED` `ENABLES` rows. That is true of all 111 existing bullets as well as the 16 new ones; this packet adds nothing to that exposure beyond the new edges, and runs no extraction.
6. **The human-owned `_COORDINATION.md` Notes line** (L225–227, `_COORDINATION.md` `95ebe344…8a90c`) still says "revision 1.5 is `current_basis` since SCA-005" (review record `returns/REVIEW_PR954_03.md`, `beaaa497…23fa`). It is not this packet's to edit; question 4, a separate optional question, offers exact text.
7. **An edge into a standing node.** DEL-10-13 → DEL-10-02 (E-P91) is a `PREREQUISITE` edge into DEL-10-02, a C-08 standing node that "gates releases, not successors". The accepted plan names this edge, and E-A18 (DEL-10-11 → DEL-03-04) is a precedent for an edge into a standing node. If K2 later classifies DEL-10-13 itself as standing, the K2 packet should name DEL-10-13's `_DEPENDENCIES.md` for the C-08 section.
8. **Re-audit ordering.** The audit pointer names `COV_SCA006_POSTCHANGE_2026-09-26_0051`, whose EXPECTED_CONSEQUENCE rows this packet resolves. Without a re-audit they stay on record as expected consequences; nothing is mis-stated, because they were attributed to deferred Lane B work.

## Options (two separately rulable parts, one add-on)

- **Part K4 — re-pin (B7).** One act on **129 product paths**, all modifications: 63 `_CONTEXT.md` and 66 `_REFERENCES.md`. Slot-free (no date in any postimage). **Add-on C** (recommended) gives two of the 66 references different postimages and adds no path. Without C, K4 stays inside the brief's "semantic fields untouched".
- **Part K1 — setup and dependency work (B1–B3).** One act on **32 product paths**: 12 created in the two new folders; 20 modified (4 `Dependencies.csv`, 16 `_DEPENDENCIES.md`). Rows: **22 added** (4 new-folder ANCHOR + 2 appended ANCHOR + 16 EXECUTION), **2 refreshed**, 0 retired, 0 deleted. Two new `OPEN` lifecycle files.
- **Add-on V — re-audit after the act (recommended with K1).** A TASK `audit-decomp` run into a new `COV_D101_POSTSETUP_*` folder, with the `_Evaluation/DecompCoverage/_LATEST.md` move only on 0 BLOCKERs (the `D-PEC-93` rule). It confirms forward coverage back at 100 % (68/68) and records COV-003/004/073–078/080 as resolved. With K4 alone it is not recommended (version-only metadata, checked mechanically).
- **Amend.** For example: add DEL-02-07 (finding 2) or DEL-08-06 → DEL-04-03 (finding 3); different strata or quotes.
- **Defer (either part).** Nothing opens. Deferring K4 leaves COV-077/078 on record (version-only staleness). Deferring K1 leaves the two DRB-008 warnings, COV-003/004/073/074/075/076/080, and blocks K2 (first SOWs for the two deliverables) and so K3.

K4 and K1 may ride one PR or two. If both are ruled, the recommended order is K1 then K4 (either works; the trees are identical).

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance under `chirality-root:bundled:workflow:project-setup` may have each selected generator run **once**: the K1 generator by one bounded TASK (the eligible `preparation` actor, recorded `TASK+preparation`), the K4 generator by that TASK or by the manager (see Administrative grant). Paths are relative to `projects/pec/execution/`; preimages at `aca930622`.

### Part K4 (129 paths; slot-free)

{{K4_TABLE}}

{{K4_AGG}}

### Part K1 (32 paths; postimages at `{D}` = 2026-09-26)

{{K1_TABLE}}

{{K1_AGG}}

Read-only basis the generators re-verify but never write: `_Decomposition/Deliverables.csv` `94ee5d18…9805`, `_Decomposition/ScopeLedger.csv` `1d24a4b8…e916e`, `_Decomposition/SOFTWARE_DECOMP.md` `9374c21f…08eb1`, `docs/PRD.md` `ae49b806…83fbe`; K4 also the three A2 `_CONTEXT.md` mirrors (DEL-04-03, DEL-08-01, DEL-08-03); K1 also the three tools named above.

### Generation method (binding)

{{K4_GEN}}

**K1: `gen_d101_k1.py`, SHA-256 `{{K1_GEN_HASH}}`.** Stdlib-only Python, prepared with CPython 3.13.7. It is copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/<run root>/gen_d101_k1.py --repo "$(git rev-parse --show-toplevel)" --act-date {D}
```

Before any write it checks: all 27 pinned hashes (20 targets, 4 basis files, 3 tools); that neither folder exists; that the local date equals `{D}`; that the registers still assign SOW-099/100 to the new deliverables and SOW-097/098 to DEL-04-03/DEL-08-03; that the package names match the sibling contexts; that no new `DependencyID` or `EdgeID` is in use; that every new quote is a substring of its cited locus (the named register cell, the single PRD requirement row, or the single PRD §8 line); that the two refreshed rows carry the pinned old quote, locus and target; that every CSV row round-trips byte for byte, so only named cells change and appended rows are the only additions; that each mirror anchor occurs exactly once and each new downstream bullet lands at the end of its section; that every ACTIVE EXECUTION quote in the corpus is verbatim after rendering (127/127); and that the write set equals the grant. Only then does it create the two folders with the tools (`write_status.sh` → `scaffold_deliverable.sh`), check that `_STATUS.md` equals the form above and the stubs are empty, write every file, and run `check_min_viable_fileset.sh` (PASS ×2). It exits 1 on any failure; a second run exits 1. `--check-only` renders without writing. `--reproduction` lifts only the local-date check (the tool-stamped `_STATUS.md` date is rewritten to `--act-date`) so a verifier can replay a recorded date on a scratch export. `build_gen_d101_k1.py` and `gen_d101_k1.template.py` are preparation aids, not bound. As in the `D-PEC-93` ruling (N1), folder creation precedes the main writes, so a failure at that step can leave untracked files: the act runs in an isolated worktree, and any failure discards it.

**K1 bound options.** The tabled K1 hashes assume `--actor TASK+preparation` (the default) and no `--reproduction`; the act uses exactly those. `--reproduction` is for the verifier only. A different actor string would change the two `_STATUS.md` postimages and the `all_K1` and `created_K1` aggregates and needs a re-rendered table.

**K1 slot rule.** With the bound options, the only varying bytes are `{D}`: the two `_STATUS.md` date and history lines; the provenance of the two `_CONTEXT.md` and closing lines of the two `_REFERENCES.md`; the Status and Run History lines of the two new `_DEPENDENCIES.md`; `FirstSeen`/`LastSeen` of the 22 added rows; `LastSeen` of the 2 refreshed rows. The 16 mirrors are date-free. On the prototype, `{D}` = 2026-09-27 (`--reproduction`) differed from 2026-09-26 in exactly 14 files, all identical after substituting the date. At another date the verifier reruns the generator on a fresh export of `aca930622` with that date and compares byte for byte.

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`. Record each command, exit code and output in the run root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | the generators' built-in checks; the ruling and its register row on fetched `origin/main`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | preimages as tabled; `ALLOW` everywhere; otherwise stop and route the discrepancy |
| Strict registers | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` | **K4 only:** exit 1, output byte-identical to the pre-act run (66 registers, 263 rows; 0 ERROR; 26 XRG-013; 2 DRB-008). **K1 (with or without K4):** exit 1; 68 registers; 285 rows (ANCHOR 146 / EXECUTION 139); **0 ERROR; exactly the same 26 XRG-013; 0 DRB-008** |
| Closure | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <run root>/closure` | exit 0; `subject_status` PASS. **K4 only:** `closure_summary.json` byte-identical to pre-act. **K1:** 127 edges; 68 nodes; 0 SCCs; 0 bidirectional; 0 orphans; 0 declared disagreements; isolated exactly the six above; hub DEL-03-01 only; `declared_only_rows` 127; `declared_unread_count` 136 |
| Quote currency | K1's report line `CHECK active_execution_quotes_verbatim 127 127`; `verify_d101_k1.py` | 127/127 (K4 does not touch registers) |
| Anchor coverage (COV-080) | `verify_d101_k1.py` | every IN scope item traced by each deliverable it names; SOW-097..100 traced |
| Postimage checks | `verify_d101_k4.py <pre export> <repo> [--covers] [--allow-k1]`; `verify_d101_k1.py <pre export> <repo> [--allow-k4]` (on a combined tree use the K1 verifier's `--allow-k4`; the K4 verifier's `--allow-k1` tolerates only K1's new folders, so its containment line reports K1's 20 modified files, by design, while its other checks pass) | PASS (K4: edits confined to the anchors, 63 + 66, one provenance block across the 64 `D-PEC-62` contexts, every context and reference names revision 1.6 and PRD v2.4; K1: containment, row conservation, mirrors insertion-only, mirror invariant, new-file forms). When both parts ride one act (either order), run the K4 verifier against the original export as its before-state: it reports exactly one FAIL, its containment line listing K1's 20 modified paths (149 changed against 129 expected), and every other K4 check passes. This is recorded without `--covers` in `k1/evidence/verify_k4_on_both.out`, and reviews 02 and 03 reproduced the same single FAIL with `--covers`. Do not use a K1-applied tree as the K4 verifier's before-state: its census and one-provenance-block checks count K1's two new `_CONTEXT.md` and fail by design (`REVIEW_VERDICT_02.md`, `REVIEW_VERDICT_03.md`) |
| Schema per register | `python3 tools/validation/validate_dependencies_schema.py <path>` for K1's 6 written registers | VALID ×6 |
| Minimum fileset | the K1 generator's report | PASS ×2 |
| Every-PR checks | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check`; `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | exit 0; output identical before and after (as on the prototypes) |
| Byte identity | recompute SHA-256 of the written paths; for K1 at `{D}` ≠ 2026-09-26, the slot rule | equal to the tables |
| Containment | `git diff --name-status origin/main...HEAD` | exactly the selected parts' paths, the run root and (with V) the audit folder and pointer; nothing else |
| Whitespace | `git diff --check origin/main...HEAD` | clean for the product paths (`.gitattributes` gives `Dependencies.csv` `cr-at-eol`). The run root carries its own `.gitattributes` with `-whitespace` for its generator reports and closure outputs (which keep empty trailing fields and CRLF), as this preparation folder's `k1/` and `k4/` do |

### Add-on V (if selected)

After the product writes are verified, WORKING_ITEMS dispatches one TASK under `chirality-root:bundled:workflow:audit-decomp` (`DECOMP_VARIANT=SOFTWARE`, scope `ALL`, expected source revision 1.6 `current_basis` `9374c21f…08eb1` plus the D-PEC-101 poststate, prior run `COV_SCA006_POSTCHANGE_2026-09-26_0051` for the comparison) into a folder from `tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV D101_POSTSETUP`. Expected: COV-003/004/073/074 (folders), COV-075/076 (quotes), COV-080 (anchors) and, with K4, COV-077/078 resolved; the three pre-existing Check-6 warnings unchanged; 0 BLOCKER. Only on 0 BLOCKERs, `tools/scaffolding/update_latest_pointer.sh projects/pec/execution/_Evaluation/DecompCoverage COV_D101_POSTSETUP_{YYYY-MM-DD}_{HHMM}` (`21899520…15bc`) moves the pointer (preimage `f8469f88…a9dea`); otherwise the findings return to the owner.

### Independent verifier

A fresh read-only TASK that authored nothing applies `chirality-root:bundled:skill:software-code-review`, adapted to governed metadata, and returns a verdict file. Defects return to the author; the verifier does not repair. It checks:

1. **Basis.** The ruling and its register row are on `origin/main`; the run-root generator hashes match; the recorded preimages match `aca930622`.
2. **Reproduction.** On the act's local date it reruns each generator on a fresh `git archive` export of `aca930622` and gets byte-identical files; otherwise it uses K1's `--reproduction` with the recorded date (K4 is slot-free). It says which method it used.
3. **The fixed checks.** It reruns the verification table and gets the same results.
4. **Semantics.** Each new edge is warranted by its quote and locus, none duplicates a pair, and the strata follow C-10; the refreshed quotes support their rows at least as well as before; every new `_CONTEXT.md` field equals its revision-1.6 register cell; the new `_DEPENDENCIES.md` follow §5.2; no context or reference byte outside K4's anchors (and C's two bullets) changed; the only lifecycle writes are the two new `OPEN` files stamped `TASK+preparation`.
5. **Containment.** No `_Decomposition/**`, `docs/PRD.md`, `ScopeOfWork.md`, `MEMORY.md`, other `_STATUS.md`, `v2/**`, `checkpoint_snapshots/**`, SCA-006 snapshot file or (without V) `_Evaluation/**` path changed.

## Administrative grant

- **Scope.** WORKING_ITEMS owns the act(s): project-setup for two folders plus B2/B3 (K1), and the B7 re-pin (K4). One bounded TASK author runs the K1 generator (the eligible `preparation` actor, recorded `TASK+preparation`); the K4 generator may run in the same TASK or by the manager; with V, one TASK runs `audit-decomp`; one fresh read-only TASK verifies. The manager runs the reliance preflights and, with V, the pointer step.
- **Run root.** `execution/_Coordination/REV16_CURRENCY_SETUP_D101_{D}/` (default-writable) holds the exact generator copies and their stdout reports, the verify scripts and outputs, the closure output, validator and preflight outputs, `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the PROJECT_SETUP closeout format, and `VERIFIER_VERDICT_NN.md`. No `_run_records/` entry is written in any deliverable.
- **Records not opened.** `checkpoint_snapshots/**`; the SCA-006 snapshot folder (its Lane B closeout is recorded in the run root's `HANDOFF_STATE.md`, the SCA-004/005 practice); both `_LATEST.md` pointers under `_Decomposition/` and `_ScopeChange/`; `_Evaluation/**` unless V is selected; `docs/STATUS.md` and `README.md`, which stay with HELP_HUMAN under D-PEC-88.
- **MEMORY rows.** None are opened. The acts change deliverable metadata and create two folders but perform no deliverable run; whether the undertaking's closeout writes MEMORY rows is the graph's decision under `projects/pec/AGENTS.md` §"Deliverable records and loop ownership".
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for manager, authors, auditor and verifier, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12 (Root `AGENTS.md`), with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** Each generator writes nothing unless every pre-write check passes. If a later check fails, discard the worktree and branch (which removes any untracked folder); nothing reaches `origin/main`.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR of the act restores the tabled preimages (129 for K4; 20 for K1) and removes the two new folders (12 files), the one case where a revert removes files, and they are exactly the files K1 created. With V, the revert also restores `DecompCoverage/_LATEST.md` `f8469f88…a9dea`; the audit folder and the run root stay as non-current evidence, with a rollback note appended to the run root's `HANDOFF_STATE.md`. History is preserved; no reset; no silent downstream repair.

## Limits

This proposal, and any ruling selecting K4, K1, C, V or an amendment, grants none of the following:

- any `ScopeOfWork.md` (K2 is its own packet), `MEMORY.md`, `v2/**`, `software-workflow.json` or `docs/PRD.md` write;
- any `_Decomposition/**` write, including `_LATEST.md` and the registers; any `_ScopeChange/**` or `checkpoint_snapshots/**` write;
- any lifecycle change beyond creating the two `_STATUS.md` files at `OPEN`; no `## Remaining` section;
- `CHECKING`, `ISSUED`, artifact acceptance, or any readiness or reliance claim; the owner reserves any CHECKING declaration to their own initiative, and this packet creates no prompt, gate or reminder about it;
- any `_CONTEXT.md` or `_REFERENCES.md` byte outside K4's anchors and C's two bullets (and outside the two new folders);
- any `Dependencies.csv` or `_DEPENDENCIES.md` write outside the tabled paths and cells; any row retired or deleted; any `dependency-extract` run;
- any action on the 26 D-GOV-48 XRG-013 warnings;
- a `project-setup` `INCREMENTAL` run, `SETUP_LOG.md` or `project-dag` adoption;
- an audit run or pointer move under `_Evaluation/**` unless V is selected, and then only as stated;
- the tier-0 profile act (K3), a foreign, Root or instruction-surface write, including `projects/pec/AGENTS.md`, and the human-owned `_COORDINATION.md` Notes section (question 4 is separate);
- a schedule reading: blocker output stays advisory (`FULL_GRAPH`, threshold `INITIALIZED`).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **Part K4.** Take K4 with add-on C (recommended), K4 without C, amend, or defer.
2. **Part K1.** Take K1 as prepared (recommended), amend (for example findings 2 or 3), or defer.
3. **Add-on V (re-audit).** With K1: run it, moving the audit pointer only on 0 BLOCKERs (recommended). With K4 alone: none (recommended).
4. **Optional, separate from the grant: the human-owned `_COORDINATION.md` Notes line.** It is outside this packet's grant, and nothing in K4 or K1 depends on it. Either (a) authorize HELP_HUMAN to replace `_COORDINATION.md` L225–227 (inside "## Notes (human-owned)"; file `95ebe344…8a90c` at `aca930622`), whose current text is

   ```text
     (revision 1.1 at seeding; revision 1.5 is `current_basis` since
     SCA-005, whose dependency rerun under `D-PEC-93` retired, refreshed and
     added register rows) and are never a substitute for decomposition truth.
   ```

   with, if K1 is ruled,

   ```text
     (revision 1.1 at seeding; revision 1.6 is `current_basis` since
     SCA-006; SCA-005's dependency rerun under `D-PEC-93` retired, refreshed
     and added register rows, and `D-PEC-101` added the DEL-08-06 and
     DEL-10-13 registers) and are never a substitute for decomposition truth.
   ```

   or, without K1,

   ```text
     (revision 1.1 at seeding; revision 1.6 is `current_basis` since
     SCA-006; SCA-005's dependency rerun under `D-PEC-93` retired, refreshed
     and added register rows) and are never a substitute for decomposition truth.
   ```

   (recommended); (b) edit it yourself; or (c) leave it. HELP_HUMAN applies (a) only on your explicit authorization; no other byte of that section changes.
5. **Actor string and models.** Keep `TASK+preparation` and the defaults above (recommended), or state others. A different actor string changes two K1 postimages (the `_STATUS.md` files) and two aggregates, so K1's tables would be re-rendered before the act.

## Preparation evidence

Everything ran on scratch copies under the session scratchpad: `base` is a `git archive` export of `aca930622`; each prototype is an APFS clone (`cp -Rc`) of `base`; the git-dependent checks ran in `git clone --shared --no-checkout` clones detached at `aca930622`. Nothing was written to any checkout's production paths. Interpreter: Python 3.13.7 (CPython); local date 2026-09-26 (America/Edmonton).

{{EVIDENCE_TABLE}}

Preparation artifacts in `execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/` (hashes in its `SHA256SUMS`):

{{ARTIFACT_TABLE}}

Basis read for preparation, at `aca930622` unless stated:

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `projects/pec/AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` / `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` / `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| SCA-006 group-2 / group-3 `DECISION.md` | `30aebd162e98cdc91923468852af6833feda84c3a3d9d3efe252dc8a87abf989` / `22aad7eb09958370e7bf8b3d06eff56e8bf459f9b8c56f8cbaad2c3384036bc6` |
| SCA-006 `Propagation_Plan.md` / `RUN_SUMMARY.md` / `Impact_Assessment.md` / `Amendment_Actions_CP2.csv` | `f95d00d154610d44a37d4aeabfae3fff29aac6c0a0c016bb1241810ebc87d7d8` / `6c627456471fe175f63e1070a7243301a4c92c0a9a107a7a8d39b6b8a689b92b` / `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` / `d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de` |
| `COV_SCA006_POSTCHANGE_2026-09-26_0051` issue log / `_Evaluation/DecompCoverage/_LATEST.md` | `37f4f6dc730cebfec173ca965c5afe00b5c506afbec5cb67f4f1e498087026d3` / `f8469f88ad503ef79f436df3595cf34fd5d9ce624390fa836720227a7eda9dea` |
| `D-PEC-93` proposal / ruling; `D-PEC-95` proposal / ruling; `D-PEC-94` record; `_DECISIONS/_REGISTER.md` | `46470575…f489422` / `ffb0b582…3709`; `9137d387…4b22` / `51dceb7136c24c1dea2f68c2338f66781de17fb2b63a8caf8bc719dd5a4e2beb`; `b6814e902c23f24020337ab925a7c287b66b5ee485785bee07b042e25e1e5a6b`; `e845e1bbbc8e4f97edd7082197c37061d5c2c4170eeafaa966f74c29fd3a48e2` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `docs/PRD.md` | `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1` / `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` / `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` / `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| Notices: `PROJECT_SETUP_INCREMENTAL` / `DEPENDENCY_SCHEMA_D-GOV-46` / `DEPENDENCY_FOLLOWUPS` | `8829ac840f7429e2c1780f8d512eee16187bca1ff229257ce07309928eff64af` / `33e8d77b423aebf0215f34b056aa3063166950768aadf0509482b37e7484790f` / `4f06f230289eb442ac468b8d4b288f10270aabf1cc9a5fd8e1db519752e66a11` |
| Work graph (at `aca930622`) / `_COORDINATION.md` / `REVIEW_PR954_03.md` | `f2cdfb0e88f4f0b426dbface29a8488ddedf7bd393461e28bb723fa3487384f6` / `95ebe344ee894f5f69d8b6c3067db9ecbaa4f67786afc3f7d27c920d11d8a90c` / `beaaa49772d4c21433a5ae7f5d586efd7a40b76f822e54dcf9bf6c802add23fa` |
| `workflows/index.json` / `project-setup` `WORKFLOW.md` / `method.md` / `contract.md` | `2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3` / `7aa4c30a09183b83341937960a637a89eb8da2f8800aa88a12ec8de7ab14dd6d` / `37c285a2055c48c52478b7713cf501be5a7617ec534523f6fdd0798d2360f042` / `e9f0d11ba520397da5b51f8271b01341bd77c1239f857046b60a7b1885ec218e` |
| `preparation` `SKILL.md` / `scaffold-contract.md` / `execution.json` | `0662dc88b5c1deff27280480395d355e5b073a3eb5eb9887f1459861ced96d38` / `aa95078f13af0586a3d8617f5122e2c6337ce389fc59850fccc33c6948e4cda4` / `dd59f002bdfe7b8b86555d7786dedbc88394b015b3b3dc90665f520ffa4bec2d` |
| `dependency-extract` `WORKFLOW.md` / `checks.md`; `audit-decomp` `WORKFLOW.md`; `software-code-review` `SKILL.md` | `e5523ebabccf44337ec531280d4d91be2ce7ff1477bd39568a18bb0c4c9f18c3` / `a12aa8b32c955d623623353c39b76f771ad9d6b48a9e513b0e0bad9a706a0457`; `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b`; `ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca` |
| Tools: `write_status.sh` / `scaffold_deliverable.sh` / `check_min_viable_fileset.sh` / `update_latest_pointer.sh` / `create_snapshot_folder.sh` | `1857ad5933edad290f479955df167cb05561476a7052f550e8a7f0043f2d97bc` / `7a04c1a9a9231befa50a5113de72ea148abc52808bd6c0c5d2b1225e1a7f7a23` / `a6c4af3c684aa22b2ff9baa89ca4108cfe3a976da04aabfb852371c2c5c20f8c` / `21899520ab84e0d88056b19a4318810cc3a730bc4b6d22e7ec66291549f015bc` / `7db42ee6963dbe8306047dc5afbeb911be7fecdd92b05a239987be05c8d95640` |
| Tools: `validate_decomposition_registers.py` / `analyze_dep_closure.py` / `dependency_evidence.py` / `validate_dependencies_schema.py` / `validate_pec_loop_receipts.py` / `harness.py` | `869df1d5484603016e030d9e3c6619077925806b8db553da00add82dcb9157ee` / `2b8de3cbd2439ba1234aadf10e07348c4e2d30dd73da66cd0d88774e417a9adc` / `125939c02482b8d90db97c96c378b249c55abee7647db5cc6d85f35a53a4dc0d` / `75cd74768cc8edf91c6f40b582f0fb570d2427894e6c2236ea2fe7d384291f5f` / `8eb6299558a4038f5a62f5f979a86460f16fece6ed6e2fcb8dd00ce12952bad9` / `01a9b9541ded993364f7db8a8e8a59087bf26649094a522867a658e2eae561f3` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` / `D-T0-15` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` / `95c245b5b78d102e4531a132aab7d010b320c5c4e1065875c3f08d6c1ff70b09` |
| Brief K14P (copy in `briefs/`) | `3c16bb93710b63429cd04b3ccb8d41bc5620584965dcb5228218c3dfaf1f38b1` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, nodes K4 and K1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`. The K1 generator, verifier and prototypes were authored by the manager; the K4 generator, verifier and prototypes by one delegated TASK (`pec-task`, brief `child_briefs/T_K4_GENERATOR.md`), integrated and rerun by the manager. The TASK disclosed that a manager commit (`3430993ea`) captured a mid-run snapshot of `k4/` (superseded by the current bytes and `k4/SHA256SUMS`) and that one of its runs lost evidence files to an unexplained external deletion; it wiped and reran, and all K4 results come from that clean run. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`); roles and the `high` reasoning effort are instruction-asserted.
