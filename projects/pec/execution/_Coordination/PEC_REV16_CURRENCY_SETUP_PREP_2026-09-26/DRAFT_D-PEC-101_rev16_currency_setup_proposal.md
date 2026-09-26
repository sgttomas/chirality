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

The K4 generator globs all 66 deliverable folders at run time. It requires, and stops if any fails, that:

- the 61 `_CONTEXT.md` whose provenance ends ``then by revision 1.5 (`current_basis`, SCA-005 successor).`` (CTX_STD) and the 2 whose `D-PEC-93` provenance reads ``SCA-005 successor; deliverable added by A-19). Fields templated`` (A-20 for DEL-02-09) (CTX_D93) are exactly the pinned 63;
- the three SCA-006 A2 mirrors (DEL-04-03, DEL-08-01, DEL-08-03), which already carry ``then by revision 1.6 (`current_basis`, SCA-006 successor).``, are byte-identical to their pinned hashes and are not written;
- the 66 `_REFERENCES.md` naming ``(revision 1.5, accepted `current_basis`; SCA-005 successor)`` and `` `docs/PRD.md` v2.3 `` are exactly the pinned 66;
- any other context or reference already names revision 1.6 (and PRD v2.4) — the tolerance that lets K4 run before or after K1, whose new folders are born at revision 1.6;
- each anchor occurs exactly once.

So the plan's 63 / 66 holds (unlike `D-PEC-95`'s 40 → 42).

The acts:

- **CTX_STD (61):** ``then by revision 1.5 (`current_basis`, SCA-005 successor).⏎`` → ``then by revision 1.5 (`current_basis`, SCA-005 successor),⏎then by revision 1.6 (`current_basis`, SCA-006 successor).⏎`` — the exact form the three A2 mirrors carry. After the act the 64 `D-PEC-62`-scaffolded contexts share one byte-identical provenance block (checked).
- **CTX_D93 (2):** ``SCA-005 successor; deliverable added by A-19). Fields templated⏎`` → ``SCA-005 successor; deliverable added by A-19),⏎then by revision 1.6 (`current_basis`, SCA-006 successor). Fields templated⏎`` (A-20 for DEL-02-09).
- **References (66):** ``(revision 1.5, accepted `current_basis`; SCA-005 successor)`` → ``(revision 1.6, accepted `current_basis`; SCA-006 successor)`` and `` `docs/PRD.md` v2.3 `` → `` `docs/PRD.md` v2.4 ``.
- **Add-on C (`--covers`, 2 of the 66):** DEL-04-03 ``covers SOW-006;SOW-007)`` → ``covers SOW-006;SOW-007;SOW-097)``; DEL-08-03 ``covers SOW-043)`` → ``covers SOW-043;SOW-098)``, each asserted equal to its `Deliverables.csv` cell.

No other byte changes; no `_SEMANTIC.md`, `_DEPENDENCIES.md`, `Dependencies.csv` or `_STATUS.md` is touched. Lifecycle census (from `_STATUS.md`, unchanged by K4):

| Population | Count | Lifecycle states |
|---|---:|---|
| Deliverable folders `PKG-*/1_Working/DEL-*` | 66 | CHECKING 4, INITIALIZED 28, IN_PROGRESS 2, OPEN 28, RETIRED 4 |
| Contexts re-pinned (CTX_STD, final clause revision 1.5) | 61 | CHECKING 4, INITIALIZED 23, IN_PROGRESS 2, OPEN 28, RETIRED 4 |
| Contexts re-pinned (CTX_D93: DEL-02-08, DEL-02-09) | 2 | INITIALIZED 2 |
| Contexts re-pinned, total | 63 | CHECKING 4, INITIALIZED 25, IN_PROGRESS 2, OPEN 28, RETIRED 4 |
| Contexts read-only: SCA-006 A2 mirrors (DEL-04-03, DEL-08-01, DEL-08-03) | 3 | INITIALIZED 3 |
| References re-pinned | 66 | CHECKING 4, INITIALIZED 28, IN_PROGRESS 2, OPEN 28, RETIRED 4 |
| Union of folders touched (contexts ∪ references) | 66 | CHECKING 4, INITIALIZED 28, IN_PROGRESS 2, OPEN 28, RETIRED 4 |
| Add-on C references (DEL-04-03, DEL-08-03) | 2 | INITIALIZED 2 |

The re-pin changes deliverable metadata, not the artifacts under `CHECKING` (DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01) or `IN_PROGRESS` (DEL-01-03, DEL-01-05), and changes no lifecycle state; the `D-PEC-95` and SCA-004 re-pins are the precedents.

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

| # | Path | Preimage SHA-256 | Postimage SHA-256 (A) | Postimage SHA-256 (A+C, where different) |
|---:|---|---|---|---|
| 1 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_CONTEXT.md` | `2fe92b000bc2829d4bc3dc69d01d64044ada2db28b11ba70e22118a95ab05e75` | `f9647800b5bba9cb13ebedc666ca680d6b41ee00344afffcd4a9817a0ac25701` |  |
| 2 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REFERENCES.md` | `db32c618c8beab8d418805c69f6a3d53871a01981f6e063ca1c414c33f401f7c` | `f38d9257b5fff875a7e9d11c9832ed2e08a814a24eac2b3390a95f76e61387eb` |  |
| 3 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_CONTEXT.md` | `beafd08c5112cf5f5b8edb81ecbfdb98128441b8c407eb7e1dc0ec07fe46bb58` | `9ca53f26c7e0e60e4443546b61c2e6779c33d4b35ab8b29a0880d8837086c14a` |  |
| 4 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_REFERENCES.md` | `005aac9b9612ce10bfc06c9a2ccf256f9c06ababc192724a55cb592cf5c732dc` | `4d27f6cd4fcb742727a306a270dd765886ee4f8fbac44d8abf1b1a22d3f7f0e3` |  |
| 5 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_CONTEXT.md` | `05a2e5d08fa5366c21f7ebfe52e7c80503e484fecb2f582bf8d302214346e578` | `d4742ccaf65aeb05620e88413b14c56f416a23920d1b044538ee3a174b05be14` |  |
| 6 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_REFERENCES.md` | `21b2110208b72467d01dde4460ef7b16fbf41afe11d101a69f8f7b0fe320534d` | `fb18afbb27fe54493f6dac0df890d86359db43ad0b4b8fefbd84075bf68a1146` |  |
| 7 | `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_CONTEXT.md` | `cab17da6dbdd6e086426813406fffa4b478f1607daf8c716ff38e2effb343975` | `dbc66850f7b930bba67cd76c08e754bc356b0065b30ea605719620344a77bd40` |  |
| 8 | `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_REFERENCES.md` | `8f67568f44f9c386cfcfdb3230899b5e84924527991d351e2c9b936743f32205` | `8602a533f337066ab2f1e2c53e2e7763a6c308bf24d07155f6dec06950213fbc` |  |
| 9 | `PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_CONTEXT.md` | `53f11105266638f39f1f1601f9a7c72fc0bff245bb4f722be6798e8b5effa16e` | `41a07a3ac9ba46880f8137f6317171497b7d5447b1517d02f553d430e3b35317` |  |
| 10 | `PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_REFERENCES.md` | `cf3eabd186c5b2186c60845c975b827d1b5003c060d1cb2c0a223e36e4f7ffe7` | `1b9c4da789fb0e02a37c6a71e11b2d951068c2b5ad2eb0b4063d0ba15287d283` |  |
| 11 | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_CONTEXT.md` | `e97e3c07b999f2fb5a6f13176dfe2a7c3f58403308554d02da876e93cf26e77b` | `d38c7203bb3f0e0e816053cc9e302860e1072336c745155785513a1f55e40d20` |  |
| 12 | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_REFERENCES.md` | `8f0dfcd7b1664bcc1173d4f099a7e74ca0b5b4f10755d53bb90cf022171b9400` | `4f6fb542f0b7b55ae69846e8030d0824c5f80e76d633a9e4b08f85e1c7847d4d` |  |
| 13 | `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_CONTEXT.md` | `52a4d9337e7551bf154bec549bfdcaa76ae94c96dccbf37959bd9eeaacba969a` | `d99de7f1f233b3ff637bf615da9d41f0f48b5ed4ffccdc289338bbda99a69a68` |  |
| 14 | `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_REFERENCES.md` | `f503808a708413cfdbf0020a0b3f3116c5aeb242a0355e083077f20101f1216f` | `9129fc3f64a268573089996cc6628e6a2be7a2e22458a01ddaafd4201e69950f` |  |
| 15 | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_CONTEXT.md` | `a687ad1f91bcfa82c24fc08c5577435b79e56d4884936e2903f0f6633f2675f5` | `926d2efb0cd34908ee399abe7cef77b752fe553442f99ea728195dbe2996614b` |  |
| 16 | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_REFERENCES.md` | `20d344699830c43b00464ca0e41efcf3e415c695d38427ba0b8e81f28342e2c3` | `235d0081d8e9412c94948d57dc46a9183594daa79b8557cd48a0f7c2538fbe74` |  |
| 17 | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md` | `1362ed668436b5af79fe54dd5f7ab660dac9ddd29dad2a0d1b0adebb01ad5919` | `897e3a63bc4fef9967485dd6411265ec47cdf9a824968ea8d4f0d57682824d1f` |  |
| 18 | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_REFERENCES.md` | `6e640cf84b3beb619c7503c7702017d786b80da237ae1be8ea01275c6d9c63b1` | `c46c0589285f9ec9340927aa626fe3d6b85eb6b42ed29114b587f24c421aa0fc` |  |
| 19 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_CONTEXT.md` | `7b4132ab8be4e6b5fa7a2956563fd8148967bc6fede9beba6df41b96a638c92e` | `0d40e31d260b640fa9b6a0c1214fa4a44491abba1e41a77a09534acb5c34f67f` |  |
| 20 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_REFERENCES.md` | `370181a2da1f92b6672fcc424d263fa567a1a35c5e8f795f52a0591cc964bdc1` | `539332d7d3190a0333a58702ac2fc138853951d760b3c2461f62d60f823503bc` |  |
| 21 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_CONTEXT.md` | `3c1e856db52c85de42a7e794b7a4110387a9dc2316851061f0f21f054eb26125` | `49c7dc169ad1c132ea18631466ae67824eb23a9d75bd88e4714d2503422be256` |  |
| 22 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_REFERENCES.md` | `152c6af2b22f60414ac215240207518d794a2869b6e4639b3ebb396d96c81acb` | `e1514ad8e748531bf116b0d2fb98e3e0b0c89326c91d9e8941ecc17d90ae9baf` |  |
| 23 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_CONTEXT.md` | `aafac18687dae3703e2ea0e903fc790df5123ea78cbba5682a532b54422f1d12` | `620a3dcb2a7c4df94083f30da3fcc913a3a1f87e48f7882afcf0655663357477` |  |
| 24 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_REFERENCES.md` | `e3962d35eac198dadc0c666b08a668da881500f59006966ef5e9d1bf1efde9bc` | `c1ff933c2d421dc24a90a19bc035eb8e7d701ae5fe4d92306bf90b23aa2b2f83` |  |
| 25 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_CONTEXT.md` | `7f72f6d7304254cb05cf22eb941341627ea2372e549426722311da13595666c2` | `24b09d8c74f020b2067e4663359bc5fca077a3215c44f54d335cd313860dab99` |  |
| 26 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_REFERENCES.md` | `bec637be26e4875954acb67ba346120f497ed9b94555932c18577e434a091796` | `a11ae18598e43f2c444d45db16bb489a967588172c044e5791601b7c3cf06cf0` |  |
| 27 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_CONTEXT.md` | `6c3ffcff5cb13773bbac24b821ac7d0e101f99ee414b1806a5bd6006b5e38899` | `621309de611491dc468a357bf2fe4463e8250a59d5dfec32a033b051f9032116` |  |
| 28 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_REFERENCES.md` | `9d83d55b306857b70ebd608dbf473a916c99626c48a7642011a75281b7b4cd3e` | `556814896093b7153ac37e2868ac12ce7f9603f37db4efc60d4ba7e1a3cb7a16` |  |
| 29 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_CONTEXT.md` | `3a09d9792f1a025f807ca63239b7a7c9622226880bb9706a62a10d6e093c1ec1` | `8a524017fb2f17564d3ea22edc08cf3d4ddfd45a96c973689d26056ed20b1756` |  |
| 30 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_REFERENCES.md` | `1000ff3dd8ce0ec7ad23ec5f658994000a1ab512eaa6a323a295b74a98c1a4a7` | `b12c67f1a093347045ed1721ef97d8c9616b15852077c1653ed438c66f5409d0` |  |
| 31 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_CONTEXT.md` | `fdad5d912567281dabcc61713175a75bed477e225507310f7458b72d698f04c8` | `ea5a1c07a6e66bb33e410ad6cf288a75dc7ec067618229697b28f4907ae1b9f6` |  |
| 32 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_REFERENCES.md` | `15c7018e01f4acb32e319fd93c48331139e8fea5c23c9d9410737e029a590861` | `49e0636cc4f42d81c740b4da5db98eff5a9b002534eb12b9ac2a6a7c5172991d` |  |
| 33 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_CONTEXT.md` | `721a9807211b1330b0cd124139d37fdb9b2f9167b9edc461f218bb4570f34d20` | `c12af31ce4e3ae97a56a8e9e90135f74514588d3ed3605f250da7c56f25be395` |  |
| 34 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_REFERENCES.md` | `87f95d423851a800651c6e01c4b04a7434b5f56f3476b5512075da556563840b` | `a75eb7ef69a1301886e7d77f1526acdf2569c613a986000e4df77bace5f4fb26` |  |
| 35 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_CONTEXT.md` | `2413b5c0b241eb44c9e53401499729ca3b84e23860692b63f09104af56640502` | `3fe84b03e5d4e9eb6b65e693a3a17eb6b9eb6bad6b2bbaed9f1c7f5c8c95b69c` |  |
| 36 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_REFERENCES.md` | `211cb59ce46a7399ba56775fa57024f018322ebf2f50ecaf0887eb419d06073f` | `ba1024bdc73b3733667cdca99ba32922f38c98ff6c307e92452392e8feeacf3d` |  |
| 37 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_CONTEXT.md` | `8a5874c2e46ac1c5519ea2a3123be618754f5c0989084dfed1cc562d7ac508f5` | `e38cd1e0f9f1fcca98bb70031501aa582433cc2c41eb030572aedfc6e547203a` |  |
| 38 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_REFERENCES.md` | `a7886e3cc64c79c9ccfb099fdafb829736b69368af76d62b6183ffea5a6995e6` | `3bdd8afdb636913b18188be2fbf53a97de1c8804a4e8e74019ce6dfb55d8e993` |  |
| 39 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_CONTEXT.md` | `415a4a4252978e4617236cc67adf37b59d50ddc6eb08270a06398d359137c996` | `608481fdf3065e7336687bd8aae966603234d8d815fe98f2751d07ccffe77382` |  |
| 40 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_REFERENCES.md` | `09975b4636056f878aca7574142379d0573d58bc85fda28e8cbe482865bf7ebc` | `32fa28f56637317bd306d59d1c3282f4322645d4a745c31050b06f63e53a6769` |  |
| 41 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_CONTEXT.md` | `0181f52d5a1c4199f3a29eb61c286d4fb916c91833d47f1a5c90c026d6d08a4b` | `8fd655f1ace5fce24820f740c37575fb32154bfb5f831b36296c8059f1f5fef0` |  |
| 42 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_REFERENCES.md` | `f11685f717abe03d25b92bc183d67e40264d6f317471ce9b13db3d4f9697ca73` | `1ec7dc8476e1d9f7b948a608a4ede2d2d43f4cec2e541936d0addf040976a315` |  |
| 43 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_CONTEXT.md` | `2407e64f042e0c7da7e8f2ae7aabfbab59c23976d4f7c954d541daf6ae524bf7` | `97a646855963419ec6c6884f4ecb9fb9bc23d5a437162931be304447962778f8` |  |
| 44 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_REFERENCES.md` | `9366b6ed7867aa339766765a48d4bf3ba64e703cd9a74bd964bbf2546160fd4f` | `b33563ec724b080d3fddce73f7c98e645d0944a88f545c2bef9013873d0b1e67` |  |
| 45 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_CONTEXT.md` | `4e89162e0c483b34afc4a0e954263c9929ef333a228f656075638c93a7116a17` | `9bb8130eb84975bdf46056ff74c898186297c65b7049bd1a71f7414f53375a60` |  |
| 46 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_REFERENCES.md` | `dd731f5d56f40bf42d20a6a60c35e5e31ff55d8291dfcbc28cf653a11eed4f8f` | `cbe89e8b448f913ed3c6df5bf38e518256d6cb53cae932791546ae2782fe15a4` |  |
| 47 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_CONTEXT.md` | `5502601cfe9f1c469b0df2474943f870d6e57f9514d6df830f7f6d9e32356470` | `a9146af362e1a82576822dc856e1199c9b3ffc03f64382fbcdbeac66600b2a98` |  |
| 48 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_REFERENCES.md` | `9e8ef0044e7232699c7c8f39d45aecf3d4063dfa93cd9558d03b5713a61b68d5` | `ad13bd0211647f7fb112f931c61da2305ab4f7750598e3af3d105c42df82552f` |  |
| 49 | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_CONTEXT.md` | `107a293ff8de3b127d2ee2c8c2c71171ee1578ca0d1aaa36842e9c90314aa85f` | `cc4834123977a860ecf135d16046c61fc5b4bfc8403865d153721f7815ee5915` |  |
| 50 | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_REFERENCES.md` | `334caab42cab5e50e41397f2c00540fbded70ab30d33c7a3eb68469ad2c417b6` | `5dfa71440fc03dbb75cd306c01d23158a7d4077f87bbe5162f2b3fa85d3c67d7` |  |
| 51 | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_CONTEXT.md` | `1374dc7d81acf021e85404615097207948d96106ddcea9bd24b0e6823fdbdbe0` | `c3af7967ff2a6c775c6156b748ba61b95c5a5c288de316f03e0c198cbdc1b94f` |  |
| 52 | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_REFERENCES.md` | `b039d6736b01f5399d87dd09f07cbcb13a6d94f343f7b935cc6405efd9cc194b` | `ace8f385aeb79cf023c3968a7cc86866868a3903270a7e4cc16ec0c1273aa8e1` |  |
| 53 | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_REFERENCES.md` | `81b7f2cf5f5d7a61448ceade15edfab416ecb77eb7185b9156d3abc1d458acd6` | `07f4677bf2ef1d06b540c2a980a0b740dc87b8ba7b0d2f4127230de20f611d78` | `8980ddef0542dfe77c63258c8dc84c75eca7dcf6b8798f68596fb08b944c2aee` |
| 54 | `PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_CONTEXT.md` | `cdcc030c868471ecf0a4bf13f315b171a9fab990fa1b1140d4f060bfa1d6294f` | `735646618f0766db248250a14328dd1f8718344599b906097b3a508b4142be83` |  |
| 55 | `PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_REFERENCES.md` | `d96e4e4c608cb552f1ceb71daf46d6772f573efc09e6161270ff8cbdfc5ed003` | `ca6e498e2f8e70b568135a22124d210aaa92889400b35db18196e1defe260962` |  |
| 56 | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_CONTEXT.md` | `4c1cb297d34552e03fab61f08f0105a5b04779a8e71755a2bbcea584ab902112` | `715b8582b230a849806b8f2671c11cfaa967986f47657bcf43b8d2f9e69229e1` |  |
| 57 | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_REFERENCES.md` | `cbcfd50a884e507e06f55b017df463348bd61368389270e9b9acd35b1959793d` | `5fe3f8a969294cd2b60b0f55a8ffd96030bd148e9d5e5ae850fcd2cf0d160ac7` |  |
| 58 | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_CONTEXT.md` | `142528619a8d497437fbd0232b0bda28d3c720a9356b180455265f325b8cbe15` | `d23aea861d12c28d01b7bb081ef95fb21b4f1ca2c8e819baaf58188674c5adb3` |  |
| 59 | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_REFERENCES.md` | `787380f88ec5e753548f5a4c8c842a94fd238b8eebe045dca9a007e4816fa1f1` | `1f79723c263cc649dc906eee4c36b228f3a55ec698e379e338d184e1a7797cb9` |  |
| 60 | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_CONTEXT.md` | `a0eea793cf9f871f0c6c7fdcbab87a352b60fe800fa36e693f25357529c2126d` | `fdd4b02d6545a101d22c25ad62f06eb01c8bc466f1c4269690e95ebe61de64f5` |  |
| 61 | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_REFERENCES.md` | `f32444f02048580d05cbe58aabc3e660987edad6861092aae4e9736081172e80` | `a71982b128f3a180cb275f33be394543bf5243bd3ce2a905ecb580c7276fc76e` |  |
| 62 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_CONTEXT.md` | `c9dbe25c44ab78d4e970a94c792865f5b028a905c789111a2c80c9759350d412` | `f3e4a9ec479e34452ce88940eba5e9948c2936f7dfa63fdc42132a92f01b84c6` |  |
| 63 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_REFERENCES.md` | `cbec466b9054bc22206c2ffc2c295a218eebb49b7fe9d9283c5f085e71017382` | `10124d48e3041b2d054e7aa9f7cf88738ae2d7a4e826e2669f858b3012846bd9` |  |
| 64 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_CONTEXT.md` | `9338cf5592fcaa103fe8a5fc8245d4d6e2e1d533b88a97cd28f031a12874fe99` | `e7e52f57f9daf98d671841efcc5cc3fa6e5b725cf4b6d3532bece20428a63335` |  |
| 65 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_REFERENCES.md` | `a92d69179a62cbc2d327547c4729cabf9f44a2a44d45dbef2fa654d4623b4438` | `d93b07d23646e016fc5808b6cd64860b6cfc6ad7068e63924b150db5f07308fa` |  |
| 66 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_CONTEXT.md` | `b117fac353aa4f043e2cedc07c7cf393c3e7cb41b519bac7ae753cf3a03e1470` | `f7c84f192a5d188eaa6a9ca26097844f0a55fe5bab0d31e7a3b6a647c0ae70fb` |  |
| 67 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_REFERENCES.md` | `4e6a306004fef85ff35606ee38ee4ffc08686e4495e3e69f98b97abaca28d945` | `902e7420f0ea45406c0bf017bb82e2c7054ec22925f3249fcd992f6d0af25062` |  |
| 68 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_CONTEXT.md` | `a0aee56bc26a769f3ef617ed2f836050c8634b4b7ca3df14554ecee33b47fc30` | `519975f12076e06c33d5f18723fcdfa90133ce173d434c4774a645c906ef9f76` |  |
| 69 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_REFERENCES.md` | `ca03c93f1ab4cdacf2bca1390fcb59308c12e655798c21fb522b8176f97fce18` | `27d9e8e1fc652a6a93d4632fe2c111761f069ee2da895d72d80e2418cf387e66` |  |
| 70 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_CONTEXT.md` | `a8e76d8999dbd8e3f9ce32f42823736789905576e6678679b1d320d6c81e66e8` | `3897ae437aee0a4ae30cd9c7463f15a176bad21accb0bd37222c540b792c61b2` |  |
| 71 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_REFERENCES.md` | `bcb24a8424d3b8157342dd7aeb0b5852cfcb86bc1a9517ea89f11823faca51d4` | `febe1a8393c0e98773b371ffff07dbc61dd968fb30a5d6d0b754ab4e076898c6` |  |
| 72 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_CONTEXT.md` | `9717a0a2500a193136cb162d90275615fc87eb8cfdc477decf7b06424be73a48` | `01fb14b80494b890110dfe202651c9def133b398b4e13dc80bed4a0afa35fdbe` |  |
| 73 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_REFERENCES.md` | `21fc6146c658b6f1e793a0b7c84b8a7d9a0b420787edb7a2b978ced9e4a0134c` | `7e7e41942ce942fa035f984beecec6c01935dd35b652ba75e21f1b928af5c2de` |  |
| 74 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_CONTEXT.md` | `f84331ff03d83f5f1ac2116907e3fbae8358fbc4e5f56a40cc6debaa0568e02d` | `0b3268f57859ee24b003c0c3a9efb7406d4642900052b73aac728057e02c5df0` |  |
| 75 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_REFERENCES.md` | `d7cddbe827d48097a614492aabe7c6a14ec914a98071529e324b9ba83b5ccf49` | `a4835fe7c0113266fbbd274ae5871bad064fc7b8462770627e104fd4d7d0d156` |  |
| 76 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_CONTEXT.md` | `0bb820ded2fe598b8484ee37ae11ae35a81720f8088b490e5c438725cf6af3f0` | `adf9cc6e92d7ffe3c69df5d65a0bbdd90692860754719c633afec78975801765` |  |
| 77 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_REFERENCES.md` | `de57dac815c281c09ce079ac8ec7b24f60956a20cf4631fe002f947f827c6ce0` | `5328803874606797a7d0664ff44b6372368169de63f621b595c554d1a7957983` |  |
| 78 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_CONTEXT.md` | `508bd1de276c4235ecadadb2261ed7be470c78e87bdf2c32d45f774103215431` | `f739531ff5760b52124b478365a1827e77a8ae830bde5573c070dfd09f01eee6` |  |
| 79 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_REFERENCES.md` | `2530101559e367c8ac390c3e9279f72ce1bd4c2d8ef53f637d92aeab9ee11376` | `1a3b18afe54083479c66c5359696ccbdd65d1f977cbd54aa6775f2a9c0d71043` |  |
| 80 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_CONTEXT.md` | `5ac0787f665f6603fdc461e5816681584431715019937f292f26c9242dc81b43` | `b913349e12eb5ceb8dc60b1e5cc9d53e7889bcf384e620f59017835ef2933b99` |  |
| 81 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_REFERENCES.md` | `da78383887097c25858fdf531362d9f64604ca682d1ff909d7663f3bbe9a8869` | `b97839bcd817e6ee321b48ccd64e7b32713372a33039152e20c53d2136b47f8f` |  |
| 82 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_CONTEXT.md` | `1adc79cd3779b756d80ff681e975adb52e776d612081e52bd0ad5acc618de12e` | `af0ebcb962262539e9fed73d858d8503537cebfd245ec2ff90afcdbe9b18f5d8` |  |
| 83 | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_REFERENCES.md` | `c6a7a19512730fa3b255b4855e03aadbe02e4f4b71171805df9fe8972cccf57d` | `1e3614e69844ec44f99e414fa86c6db99596c23438280a30016ad6f2f3a4cf8f` |  |
| 84 | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_REFERENCES.md` | `482b9f05504719abbc30ae38cdd8ef7a6b4b62d47b9042bbf8c9311a9a440bf2` | `d0320ce635b489c7cf296234aea44f5790544055280ccd1be5197deed2ea0e88` |  |
| 85 | `PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_CONTEXT.md` | `38acdd6c8a7d812ba61387f91a751db7ffab723813546910cba3f5c23e52307d` | `be136315cb4f4d88696880d2dccee24abbc174495c136a74e495d69a933b55b9` |  |
| 86 | `PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_REFERENCES.md` | `4b9071df7e447bfd122d240588e6ea2238b7c537cdf04a199df9228f755d06c0` | `87be501eb2603ab40d508f580e71892063f1fa0489442651819c49aff5c6d278` |  |
| 87 | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_REFERENCES.md` | `f5610e5c224662cc7df0b1fc5475893f75388fe17e503beb0db870c5264f0f4c` | `cfbd8d91ca47c2b4fc2a28c9a76a2bc5e77e4293d57e07b7689f379b23002652` | `3f1b57666335f4905ee0605a40dcbddabd42bf0f44f35b52e361e27b9bd476a3` |
| 88 | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_CONTEXT.md` | `f5dd9ea168be0fc6fb6bd74dbf680f1e218867844bb619510e8c4bbd90df4634` | `8774cd9d11eef9fc40a48ce999cb11f5a2ff60be3695d894e9ac19bcd19a0c96` |  |
| 89 | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_REFERENCES.md` | `1bfa6baf155e153f1e9607be9b8e57e3ee6d31f04e4ec40e0220f8201c8f873b` | `c882f26762d85f08770eeac930211a34ad6950732c1cb6f523d3571d12259ef7` |  |
| 90 | `PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_CONTEXT.md` | `ba3f7d6e10d52c9b6fc1185538d891ccad0833afea16107fd1b060d5cd4ae31d` | `0ace29eae7ca6d34f7c18b5a5a4742ffa5a1f8e911ef48d4d4f8060cb3a55f72` |  |
| 91 | `PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_REFERENCES.md` | `95fd692f88487d6f72c887512fcf618c7bb1ab4109a29650491a7bbaf470d6f1` | `5f758df803c425a496f9743108d1a5db6f58c76801207c284f946f2a9821325f` |  |
| 92 | `PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_CONTEXT.md` | `0a82ce9ef981ebab381b2897d6f42873dc80aad57ebc37bd695f6faeddc96131` | `c1c52a0c4a96f60124adc3f382916c78447c30c28afe6748a2659d8df9fcf9ea` |  |
| 93 | `PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_REFERENCES.md` | `8ff66a8b3896cde83f907737b630fc6fc45b5e8e53acad646906b3dd22f14147` | `3221424f1fdb47f0cc530b264cf1c2f699d198e8147633f48f179909ce3cc273` |  |
| 94 | `PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_CONTEXT.md` | `d9a623d6c6bc1a8651a84447b9e1cf85804aa26effecb95573acb253af6159c4` | `9897044575a3f7062a75c5c3ccd8860b013c1ebe096783585b07c1d333685c47` |  |
| 95 | `PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_REFERENCES.md` | `298ccd42e5fc6dabf85193cd14dba1c998f3056ff52bbb048387068c009170e8` | `4ae871e20f914550860d421ef5109884edc56269b5d624c151749eac7b2d6b56` |  |
| 96 | `PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_CONTEXT.md` | `899954af31d1be0b19fb6cdfb94acfde72fbcddbc2519ebecc107dfe155089de` | `c42ea26272d2e705fc29b50f4b3dae5beee25f713642bfe0d4b747af98acab8e` |  |
| 97 | `PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_REFERENCES.md` | `c3905be1b42cef9e9965d486e0e8573bb82fdfa672afbe14aa68dce8b8a3130a` | `6b2365b566ed5fec800375572dd262db7a207186fc465d395a80fdccd4801076` |  |
| 98 | `PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_CONTEXT.md` | `a84fdb13b87ac8ac761898430bbe6d37b26d61f5db9db99b98e893f496c2773b` | `fb36dee745b5b6561b060090d0c102034b156c575b0b084930b5d6f377c91fcf` |  |
| 99 | `PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_REFERENCES.md` | `37f5f6e22af354d35de5c7ab5023a627582d6c36b262e226abc9ce8776532538` | `74b709ab2f54c3903f1b20bb3789b4100a40779d646c3ef65855b4fe313c030d` |  |
| 100 | `PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_CONTEXT.md` | `cd2b2f6b4e14c2b47d9ee98f545cdc27f006275c92d3b01ef1d3142c6b52cab9` | `450adac9fe8218971ee64170af978349007878d29c9c64c84275518eec5103ef` |  |
| 101 | `PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_REFERENCES.md` | `9a64f20affd93c89e895414b64f79aed500be6cf39c16c44854dea6bc70c3f2f` | `a1603bd2ada43145b69e75ffb236f6fd72aa442446fa5d6b7a2271ad118c9981` |  |
| 102 | `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_CONTEXT.md` | `16157838aabf1d7b3acbd11d378df77975bdb086b23829dd4cd095803e5b99ce` | `cb9fde43acca79bf48647aed8d4331d273a5b8fed44648e2c7910737f7315771` |  |
| 103 | `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_REFERENCES.md` | `971473698783d8eddbd6781b15c94d709bfdc7b8de5390a63f49bdacae855c22` | `9974a41e0674446c20bc58a71f1e3091353aff61bdf5d1687a2e61ab8fe2526d` |  |
| 104 | `PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_CONTEXT.md` | `d7f98897834c9c8308c30f62a767912143dcf52d59731f796de62058958c38d5` | `2322328474ae395e4402632194072cd59881301754c23c0b7e8fadbb41c52007` |  |
| 105 | `PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_REFERENCES.md` | `9adf8d8f56e53a08452a6aadc5f866a2c1d646a02235b7bff9b302cd2bfddef3` | `0bd314ffe377ade3e9dcfcc1f40cc79cb15f8b2057d02867ff1c48b8244c2863` |  |
| 106 | `PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_CONTEXT.md` | `94c93a624a2c84e1433d4c72712e5067e7e31fe1ed37cbad11d114bb4fdedbe5` | `ded4beedf677d6c80592a96f9c3ea032529ef7183c6bac470dd5060b0bd2141d` |  |
| 107 | `PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_REFERENCES.md` | `7b831447e279d9e296b9fecebe07fa3552b63a751ea5f750fa34ebe1b4ffe438` | `f628732d9b1603157cfdd8674d1183d24801fe55170a4d3dfda71a1d4d98d5ca` |  |
| 108 | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_CONTEXT.md` | `da16ba796b54e3615d85f275b923d838f40140a216707e4a5a26427af28bd9de` | `5be729385fabf562fad7ba016e646f8f9a2171a200302edd7222c8ca2929795b` |  |
| 109 | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_REFERENCES.md` | `90ceb3a244b5b67d71f1ed350325c99eb92f190fbb8f2004b27c571b966256c8` | `195a8797abe9139118b4d0091ca7d47de49565d2933df48a22730b92211ebddb` |  |
| 110 | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_CONTEXT.md` | `2042fecf8c1c4c2b2ab993ba1170d6205ec07592e1dadaff2d7be6a30f760044` | `7c6aca03b53eddd4b0c442f775f24fe9ce1db46afd44b06bb1de672ad596a3f9` |  |
| 111 | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_REFERENCES.md` | `53469876f8fa7478b693ae399797335b00d2e38584feec99a4ca1a148450a5f8` | `c7030b415207b53afb6920bb9ca28e9abac90c401940c86a4d9d0955afcca0a0` |  |
| 112 | `PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_CONTEXT.md` | `50afd95f55c1b82298ca132c2b28da65c4f7524e3b0f262236591eaa1124cd72` | `e00c919b275848290701531107b0949529015901c43e1f9409d018cf891da5c3` |  |
| 113 | `PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_REFERENCES.md` | `2e63822889ea6445a1c14ebc3f485f2ebc31972ff9f0a7b9f17d1553b4cbaa17` | `adefdf5e6f1c3bf12cba889a57898591580a1869e7647f41306158a68cbbe94c` |  |
| 114 | `PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_CONTEXT.md` | `23962c3bed576f73d9847c6cf486584d71ae8bdca8f07338af122c8ceaf5f204` | `752344a3afd248b6633cf493cd46fc3840d3fe332634702a06926fcc1cdf30aa` |  |
| 115 | `PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_REFERENCES.md` | `401555caaba8bd84d864d842553cfcd539a8aab1871ea46e11fc60151d4d0788` | `89151faec0c1842572e42bc4616294de3c34b47d6485c178ad6657ac617c4eb3` |  |
| 116 | `PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_CONTEXT.md` | `fce20f41e538794ef2e281b7d946e7956daa5ef9b915887fc0cf8a34faaf8129` | `22b5154492b64162bf543347c985ff4ee0b2c4a6b28d058a14bbf7dd001d2a92` |  |
| 117 | `PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_REFERENCES.md` | `7fa66b924fd5c2c3b372037c4a7a58bb1a7f37803335511ba908341209890c59` | `7d7770d2f0433bb9caa44f9b59233da242ef7054363e7d6c0b003ae9b7e30319` |  |
| 118 | `PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_CONTEXT.md` | `695088ed3e70385121e22f31825b33efb2fd68e9452f41b500bc7d1d85eb7597` | `44aa11d4c13cbe68a5d7a844b345c6402aaaac598fd46e760c29fed262350ce6` |  |
| 119 | `PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_REFERENCES.md` | `c1bdc4ea35a1ecfa98037b9465bf4bc7457e62b6a67ee5b3dce27078a26a2a3c` | `0623dd85a3f7ef9515609762842d3a2e35cc5c30cb84f7bcb409136b9bdebef6` |  |
| 120 | `PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_CONTEXT.md` | `d08c2b9050b93b1ca0581b5b08b39334c129e2dc47ad2b72bad9485ab6ae18d0` | `227b049e2bf781910e8731ee33e96ccd46096f2bb86a69e852ebf392bb788991` |  |
| 121 | `PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_REFERENCES.md` | `c33e13a6782af6218edebe4a8c72b07bee0d82f1c60e730af616459af09ee874` | `42689b4f66f0dd51a749cf16ef6a30c3dd18e788aebb54c01c59b2dbbb40be49` |  |
| 122 | `PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_CONTEXT.md` | `6ff57483f8c75a268ea990c8dcc077e13169d78496c377aadec9007bdc55ac9a` | `a700adf4d7b0b8b592b70533febdcbef11a59fab312156dc2cfad08cddda99c2` |  |
| 123 | `PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_REFERENCES.md` | `a07e02eef7fa4256aa47ee80d1003ca82d7f891d9a6fe040246938c854fa00fa` | `ca9d61f88ba4e8aba3d9e75a9c68c55ff08d9d98a53acd326d46bdc27c8de712` |  |
| 124 | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_CONTEXT.md` | `7f3d7035d5760ce4f6636212f4b7932c5daff5170c3089bc0414a1372dde7c09` | `db388dd7c0e1df15f95cb161d11a9cbf87621757635ee2bdd7c9965ac7b72f5e` |  |
| 125 | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_REFERENCES.md` | `f9ce0996b74fb257b8a312652f940b12369ad169b8170bcff778e817b4967f7d` | `1eca0b3504bb90347290df8048443cbd15da61b716c61e8132baa26d9249b151` |  |
| 126 | `PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_CONTEXT.md` | `cda340e681a8ee5c7d2b005b5a703988ba37dcdebd6f18a1d3f8c8d6591d945e` | `78b557289c92d12dadd925962d81288ab7e5c259e333c8c28a5d46e7ad154b26` |  |
| 127 | `PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_REFERENCES.md` | `e2dfd94a6dfd78ab6f9b28a2c2b4eae7e630a80562f8a8001b6c1a77f4a42c23` | `b1d59b6d1bec37c1fe3f2c1a8ff007675a5b0c1232e35b80c71ec9647504a440` |  |
| 128 | `PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_CONTEXT.md` | `23ce69245e66b4ad5104b9ed2189ae49b09e30df69f2f0aef0d03cd535cbba05` | `4704028f49fa0b23c3d39361cce61f18885a83abb47f20c3914a6f11b76a414e` |  |
| 129 | `PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_REFERENCES.md` | `cdd04184fcd742061e2d568120f14a34830827b753e559fc10d646cbd5a13983` | `4900fc843fa029483a9588255758b8a09e7bd132c26a3a44f4682180706a27d5` |  |

K4 aggregates (bytewise-sorted `projects/pec/…` path order; SHA-256 over the concatenated bytes; path list = SHA-256 of the paths each followed by LF):

| set | files | pathlist_sha256 | pre_sha256 | post_sha256 |
|---|---|---|---|---|
| all_A | 129 | `bbd1374c165624fcadf37ccf7e788599a5e5a07c6886af59f40e62fbfc7bf7f3` | `7d6d801687022d6845cff6db46a641775e72f313813828f04abda77e552e2105` | `dafb404ab728774eb3a4a8a4e88c38f7928c217c992c01910699532e0a9dd64c` |
| contexts_A | 63 | `fd8255f43139d476ffc95615649f900ad0bb4d5dfb70dd8a1646c50f4b76c94f` | `ac196e7b5d01965fd0558ec680a694ab88c320d556b79b5ba60372eeea464c2a` | `7d4f81d0c9200b59cab6b43a3af1f9a6c14ce6862acc7ef3b7129be335c035be` |
| references_A | 66 | `dcde792435bbb7557fb17b3cf0c913e725a99a79ae06cc1e790669be2e12fb1d` | `b0341a8b3439bf558ad9a2ed4e3a5f225b4f1434da699d0e6da597a997bfce7e` | `e3efeb42b5cf2bf47960417faf3b909bf7b7fab3773b8e32087aa37404e87db4` |
| all_A+C | 129 | `bbd1374c165624fcadf37ccf7e788599a5e5a07c6886af59f40e62fbfc7bf7f3` | `7d6d801687022d6845cff6db46a641775e72f313813828f04abda77e552e2105` | `01bd1f7bcdc28519e8b4ed5a767a3a362004d412bd350fe3816eabd425576b3d` |
| references_A+C | 66 | `dcde792435bbb7557fb17b3cf0c913e725a99a79ae06cc1e790669be2e12fb1d` | `b0341a8b3439bf558ad9a2ed4e3a5f225b4f1434da699d0e6da597a997bfce7e` | `0168d726cc2d5ee661703be89281b1f596710d70f6923e1bf34c127b31e1e07d` |
| addonC_two_files_A+C | 2 | `084b142b1e9925e700e6cf6757c991fa1b4bfcbd2dfaac582a8b628edfd49605` | `e7d73e3b4bc223248915e4e69c2fd092a3e261b604edea22ef59edb9fd3589a1` | `dd4ffe4cea39e0a9df039b0d8246d70896b2db0f82e489d17bb0b2879a4f7227` |

### Part K1 (32 paths; postimages at `{D}` = 2026-09-26)

| Act | Path (relative to `projects/pec/execution/`) | Preimage SHA-256 | Postimage SHA-256 (`{D}` = 2026-09-26) |
|---|---|---|---|
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_DEPENDENCIES.md` | `0ab78b34f0d63d827274572c321c4e45577047f0c1ecfb1d6583f25cc954db50` | `717aaa3cdb8403329063590a60546505480af4c6c8f612a9cea10f58da67a7c7` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_DEPENDENCIES.md` | `aba521cb8d43aae8b581760a4b71917328298e31dae463c3af039aa3836d234d` | `8c846a672427f15b69b9b2f8f5a8f2a13080c93d9a96762fabbbb2f8d8ab3f3f` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_DEPENDENCIES.md` | `9236ee4daa25a52970c3ffbba0aad5c3fbed1f72e3875e1e9cafff7c743cf995` | `c99a227eb951cf388988cae1d2f08be4648073354cf503cad94763c5a5680dc2` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_DEPENDENCIES.md` | `e18a07fe6a6b9068740bb863ff4f07eabb321ff11dc1321a1c0a7e1bda1b14e1` | `8dfd0f97d8c270d132c5d8aae0008c77f59d2a41855234069cfa9f20ccc46e17` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_DEPENDENCIES.md` | `d6e96904ebf002c66181e2c5b8b79217e80a3823885910ce5783f5cd6f8cb3f5` | `cdaf2357d420d164cdd35d9f2aa9e0e99b86012a99bc1b2ef12bc46e9b0a3584` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_DEPENDENCIES.md` | `11dad24a7aba6d62af6c82a2041e281689283f1733bece207083ef644fafcbb2` | `803d25b7c1ab250bf9ba6b3861ed8e66c2363c01c7682d8eeec87d15e3255a8a` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_DEPENDENCIES.md` | `0ee572b955cedf628958305e049b0f776bec3fad39dada73bca88b1421959a3d` | `6a83c7be4b0be40771d212be8bbe83d19d9cb8b748e70637994a4fadff0f0011` |
| MODIFY | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_DEPENDENCIES.md` | `41c841a4cac76634bd5f1aae664152f9488c073b5ef5c254f2fe2cdaaebadf3a` | `fd313520803aad9312cf45ba7340a9e651f46b6d95d64173e4883c13705b84bb` |
| MODIFY | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_DEPENDENCIES.md` | `8212ce880d76091baac8e1c45553a146b98d1447263589a9d8816b7bd1726df9` | `7e5af6d5ffa40ddcf8648fa419d441fcac7d54916b5a4b616810cc0f4005eb18` |
| MODIFY | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_DEPENDENCIES.md` | `ea0578890660a7d00f40a8278bf2ea5e320014d4713565b44b7826830c4b4c0c` | `cc6e31deab4cdaa6c9aae0830ef6e5b7f46fdec0d01ff629ee3c771d6e7d1597` |
| MODIFY | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/Dependencies.csv` | `9ed5f8851ae1f6ad2d859f776b4b52bb4793daf73377eae107940a7f5d414542` | `0d479ce3a539844a5387edc8c680b83c704b77ff1e1b6ae11c6c4c2984023518` |
| MODIFY | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_DEPENDENCIES.md` | `a70848ef91cf2275ff950a8f1b45cde2d5edd6e6248575091823559ee802516a` | `703d29e3c356f6c8cdd058cf55766dd3c1fb50a7db0339a9b72e4abac355ab28` |
| MODIFY | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_DEPENDENCIES.md` | `4b5669bb2f1839852934cecf82e5b3abfc106fca4de7bfe5c365ee6ef1419716` | `57d89a3f57d0dc643ec8cc013938ab301b4afb9f788f2e37571716280c1fa1e6` |
| MODIFY | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_DEPENDENCIES.md` | `2add0ac7ca75f28c2a0e52592bce384b3d2e008467ad1b04c07f455997278aed` | `ddfbadaeb1829e0b73abf5aada5f9d86308940dd720f064e6ed0d95b6ed586ad` |
| MODIFY | `PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_DEPENDENCIES.md` | `2c23de02146d9233153ae6213bca09c9b20bc0fc4f5428c9108e42a1f2183f62` | `946725a6d59e9c172392998015ebfe4d2ffadf0a3fdd536606e7d6f2d90131a1` |
| MODIFY | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/Dependencies.csv` | `d46bb9f09a8d73e2dc767f544b0fbd5207d54032f70edfb1b03ce99379f385a3` | `7959badef5ec0727513ffc669968c876608c0fa3adc1a408c6ae30a7848695bc` |
| MODIFY | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_DEPENDENCIES.md` | `1e149ae0815b3a5815664b487aa94aabba3449b51175a3f5d32ec11db2c6fd45` | `7f2d1b1dd8423c21ab762c1fa795f6321bbf02059e427f005a49ebdae9aaf133` |
| CREATE | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/Dependencies.csv` | absent | `10d7b0d8ec9939179797082e3a78aa895c2bd52fd1fce8e3d8e2521486eb5050` |
| CREATE | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_CONTEXT.md` | absent | `900748777076fd0ecd16b6e2f95b0105ef590890aace871cb44196d0390136cc` |
| CREATE | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_DEPENDENCIES.md` | absent | `6aa230b1cf03a15791b730e4d20a62047053c83df19531feef162fbcbc9f01fd` |
| CREATE | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_REFERENCES.md` | absent | `9f19e3a66ada49a396f1b8e1f386a6b3946793b5d1dd9115fe7cc1e630e0987e` |
| CREATE | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_SEMANTIC.md` | absent | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| CREATE | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_STATUS.md` | absent | `73e21846186b3ab46d4d11042ecb2bb00d0c69a0d7b4fa70734c75e65a892511` |
| MODIFY | `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/Dependencies.csv` | `481ef94fe68faff3e4d41f7c240f7208ed06cc4c339fb1166372fdef207dd946` | `aab67dbfc873123b635f502a5bde2e9317e941ce86c79e31038c05c797e385cd` |
| MODIFY | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_DEPENDENCIES.md` | `021820b8cc9bd034ffdc95709864e1cdb1009ea93026ab2297a5fdc24453159b` | `8dea82047a6fdf57307b4336bbdf1adff1269a59272964b39f437488b7904f5b` |
| MODIFY | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/Dependencies.csv` | `3cfa7fa3dc5c587492d9896cf82bcb079a5e2c0151d929cd98275dd25f76bf70` | `760afab019689cdde07c2004c5db30757db76d51360b19474fec331c8fd9f33f` |
| CREATE | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/Dependencies.csv` | absent | `334b9edcf1af9334ccae91136cc88e6b4cdc2abf075a3db1a1d5b2c50e7a6e7a` |
| CREATE | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_CONTEXT.md` | absent | `5efdf4a1f0199f50c542a2b3cedcab1229b9331f5a2d5cdc120b325eca588035` |
| CREATE | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md` | absent | `5087e581b00557cac9c245c543d0a690ed2a9fc992a96d8e60769f8a44baeb63` |
| CREATE | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_REFERENCES.md` | absent | `c0070adad3a46d2a8b4f70c907829d3fd74589c9782270f2cbab995be2131656` |
| CREATE | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_SEMANTIC.md` | absent | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| CREATE | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_STATUS.md` | absent | `c7a5705d7203a26f525317e85fa068d29cfeb49b8686eab1b5cd3e782e22543b` |

K1 aggregates (same conventions):

| set | files | pathlist_sha256 | pre_sha256 | post_sha256 |
|---|---|---|---|---|
| all_K1 | 32 | `c1fbca79ae25d68c5e34aed84f536197c727dce2ae13d602bd82b8f1224fa7f4` | (12 absent) | `483ec2393ac4a9256fe2c0ab294c7f563c622349076a9a87ba36dc862d020234` |
| modified_K1 | 20 | `8c569e6091905c043113aff302804066daaae50aaf76ea54b79042792a92db2f` | `48e96f7244f3c8ae72b7aa2b9e21d24def0663b87b0785ba348c28858d782516` | `186d9c72282424bd8eb317106d9dbc72b9d595b35e4227822f2869fc9bb06e8f` |
| created_K1 | 12 | `bfca84fab01676f7380f7af04241e83719501236cbcc2d966b90f63c83be7eef` | absent | `e72fc7e9702f5f7acb4e2870cb1b53385b2b874635c7a6fd60b01e2a3f35e887` |

Read-only basis the generators re-verify but never write: `_Decomposition/Deliverables.csv` `94ee5d18…9805`, `_Decomposition/ScopeLedger.csv` `1d24a4b8…e916e`, `_Decomposition/SOFTWARE_DECOMP.md` `9374c21f…08eb1`, `docs/PRD.md` `ae49b806…83fbe`; K4 also the three A2 `_CONTEXT.md` mirrors (DEL-04-03, DEL-08-01, DEL-08-03); K1 also the three tools named above.

### Generation method (binding)

**K4: `gen_d101_k4.py`, SHA-256 `075036f0a8c214a156aec151aaa52f6d1b78c2694f4306d410579ffcef9f0e73`.** Stdlib-only Python, prepared with CPython 3.13.7 (TASK-authored, manager-rerun and rebuilt byte-identically from exports of `aca930622` and `dfb089b8a`). Copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/<run root>/gen_d101_k4.py --repo "$(git rev-parse --show-toplevel)" [--covers]
```

Add-on C adds `--covers`. Before any write it checks: all 136 pinned hashes (129 targets; `PRD.md`, `SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv` and the three A2 mirrors); pinned literal anchors showing PRD version 2.4 and revision 1.6 `current_basis`; the population rule above; each anchor exactly once; the rendered post-state (every context ends its provenance at revision 1.6; every reference names revision 1.6 and PRD v2.4 and neither 1.5 nor v2.3; one provenance block across the 64); and that the write set equals the 129 targets. It exits 1 with nothing written on any failure, and a second run exits 1. `--check-only` renders without writing. K4 is **slot-free**: no date appears in any postimage, so there is no `--act-date`, no local-date check and no slot rule; the verifier's reproduction is a byte comparison on a fresh export. `build_gen_d101_k4.py`, `gen_d101_k4.template.py` and `tables_k4.py` are preparation aids, not bound.

**K1: `gen_d101_k1.py`, SHA-256 `4892c6a3c7fab4ba405b1ca201b7cab423c8c59644dee5f1d675d2e5f692cecb`.** Stdlib-only Python, prepared with CPython 3.13.7. It is copied byte for byte into the run root and run from the repository root:

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

K1 prototype suite (`k1/run_k1_prototypes.sh`, rerun with `PRECOMMIT` = current `origin/main` `dfb089b8abae48ee699117c5bc167301963b2ab5`; the first run at `aca930622` is kept in `k1/evidence_aca930622/`, with identical results and identical postimage hashes). Exit 1 is expected where the description says so; the strict validator exits 1 whenever warnings exist under `--strict`.

| Step | Exit | Meaning |
|---|---:|---|
| `genK1` | 0 | K1 act |
| `genK1b` | 0 | K1 act, second fresh clone |
| `det_report` | 0 | reports identical (0 = identical) |
| `det_tree` | 0 | trees identical (0 = identical) |
| `rerun` | 1 | rerun on applied tree (expect 1) |
| `wrongdate` | 1 | act date != local date (expect 1) |
| `checkonly` | 0 | check-only |
| `checkonly_untouched` | 0 | check-only tree equals base (0 = equal) |
| `genR` | 0 | K1 at another date (slot rule) |
| `slot_diff` | 1 | D vs D+1 diff written (1 = differences) |
| `slot_rule` | 0 | every difference is the date slot (0 = yes) |
| `K1_strict` | 1 | strict registers (exit 1 = warnings only) |
| `base_strict` | 1 | strict registers on base |
| `K1_closure` | 0 | closure |
| `base_closure` | 0 | closure on base |
| `schema` | 0 | projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/Dependencies.csv |
| `schema` | 0 | projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/Dependencies.csv |
| `schema` | 0 | projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/Dependencies.csv |
| `schema` | 0 | projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/Dependencies.csv |
| `schema` | 0 | projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/Dependencies.csv |
| `schema` | 0 | projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/Dependencies.csv |
| `verify_K1` | 0 | independent postimage checks |
| `verify_sanity` | 1 | verify base against itself (expect 1) |
| `diff` | 1 | K1 vs base diff written (1 = differences) |
| `pre_receipts` | 0 | receipts validator, pre |
| `pre_harness` | 0 | harness self-check, pre |
| `genG` | 0 | K1 act in git clone |
| `genG_same` | 0 | git-clone report equals protoK1 report (0 = equal) |
| `containment` | 0 | changed paths == write set (0 = equal) |
| `diffcheck` | 0 | git diff --check (.gitattributes in force) |
| `post_receipts` | 0 | receipts validator, post |
| `post_harness` | 0 | harness self-check, post |
| `receipts_same` | 0 | receipts output equal (0 = equal) |
| `harness_same` | 0 | harness output equal (0 = equal) |
| `entrypoints` | 0 | instruction entrypoints |
| `o1_k4` | 0 | K4 first |
| `o1_k1` | 0 | then K1 |
| `o2_k1` | 0 | K1 first |
| `o2_k4` | 0 | then K4 |
| `order_same` | 0 | K4+K1 == K1+K4 trees (0 = equal) |
| `both_strict` | 1 | strict on K1+K4 |
| `both_closure` | 0 | closure on K1+K4 |
| `both_closure_same` | 0 | closure equals K1-only (0 = equal) |
| `verify_both` | 0 | K1 checks on K1+K4 (--allow-k4) |

K4 prototype suite (`k4/run_k4_prototypes.sh`, TASK-run at `aca930622`; K4's pinned files are byte-identical at `dfb089b8a`, and the manager's combined runs above exercise the same generator there):

| Step | Exit | Meaning |
|---|---:|---|
| `genA` | 0 | option A (re-pin) on clone |
| `genA2` | 0 | option A on a second fresh clone |
| `genAC` | 0 | option A + add-on C (--covers) on clone |
| `det_report` | 0 | reports A vs A2 identical (0 = identical) |
| `det_tree` | 0 | whole trees A vs A2 identical (0 = identical) |
| `rerun` | 1 | rerun on applied tree (expect 1) |
| `rerun_nothing_written` | 0 | after rerun, tree A still equals A2 (0 = nothing written) |
| `checkonly` | 0 | check-only on clone |
| `checkonly_unchanged` | 0 | check-only clone equals base (0 = unchanged) |
| `checkonly_covers` | 0 | check-only --covers on clone |
| `checkonly_same` | 0 | check-only report equals A report apart from RENDER/WRITE rows (0 = equal) |
| `checkonly_rows` | 0 | RENDER rows equal WRITE rows of A (0 = equal) |
| `verify_A` | 0 | verify A (expect 0) |
| `verify_AC` | 0 | verify A+C (expect 0) |
| `verify_sanity` | 1 | verify base vs base (expect 1) |
| `verify_AC_noflag` | 1 | verify A+C without --covers (expect 1: covers flag discipline) |
| `base_strict` | 1 | strict registers (expect 1: warnings under --strict) |
| `base_closure` | 0 | closure (full output in scratch; summary copied) |
| `protoA_strict` | 1 | strict registers (expect 1: warnings under --strict) |
| `protoA_closure` | 0 | closure (full output in scratch; summary copied) |
| `protoAC_strict` | 1 | strict registers (expect 1: warnings under --strict) |
| `protoAC_closure` | 0 | closure (full output in scratch; summary copied) |
| `protoA_strict_same` | 0 | strict output equals base (0 = equal) |
| `protoA_closure_same` | 0 | closure_summary.json equals base (0 = equal) |
| `protoAC_strict_same` | 0 | strict output equals base (0 = equal) |
| `protoAC_closure_same` | 0 | closure_summary.json equals base (0 = equal) |
| `base_strict_counts` | 0 | 0 ERROR / 26 XRG-013 / 2 DRB-008 / 28 WARNING (0 = as expected) |
| `protoA_strict_counts` | 0 | 0 ERROR / 26 XRG-013 / 2 DRB-008 / 28 WARNING (0 = as expected) |
| `protoAC_strict_counts` | 0 | 0 ERROR / 26 XRG-013 / 2 DRB-008 / 28 WARNING (0 = as expected) |
| `whitespace` | 0 | written files: no CR, no trailing whitespace, one final LF (A and A+C) |
| `G_clone` | 0 | git clone --shared --no-checkout |
| `G_checkout` | 0 | checkout detached at aca930622 |
| `base_equals_commit` | 0 | BASE projects/ equals the aca930622 checkout (0 = equal) |
| `G_pre_receipts` | 0 | receipts validator, pre-state |
| `G_pre_harness` | 0 | harness self-check, pre-state |
| `genG` | 0 | option A in the git clone via --repo $(git rev-parse --show-toplevel) |
| `genG_same` | 0 | git-clone report equals protoA report (0 = equal) |
| `G_containment` | 0 | git diff --name-only equals the write set (0 = equal) |
| `G_no_other_status` | 0 | no untracked or non-modify status entries (0 = none) |
| `G_diffcheck` | 0 | git diff --check |
| `G_post_receipts` | 0 | receipts validator, post-state |
| `G_post_harness` | 0 | harness self-check, post-state |
| `G_receipts_same` | 0 | receipts output identical pre/post (0 = equal) |
| `G_harness_same` | 0 | harness output identical pre/post (0 = equal) |
| `verify_G` | 0 | verify the git-clone post-state (expect 0) |
| `genK1` | 0 | synthetic K1-first tree: generator tolerates the new folder (expect 0) |
| `genK1_population` | 0 | report counts the tolerated folder (0 = as expected) |
| `genK1_same_writes` | 0 | same 129 writes and postimages as A (0 = equal) |
| `verify_K1_allow` | 0 | verify with --allow-k1 (expect 0) |
| `verify_K1_noallow` | 1 | verify without --allow-k1 (expect 1) |
| `genK1bad` | 1 | unpinned context still at revision 1.5 (expect 1) |
| `genK1bad_nothing_written` | 0 | refused run wrote nothing (0 = nothing written) |
| `diff_addonC` | 1 | A+C vs A diff written (1 = differences; file timestamps stripped from ---/+++ lines) |
| `tables` | 0 | grant_table.md, aggregates.txt, census.md |
| `base_untouched` | 0 | BASE projects/ manifest unchanged across the run (0 = unchanged) |

Preparation artifacts in `execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/` (hashes in its `SHA256SUMS`):

| Artifact | SHA-256 |
|---|---|
| `README.md` | `2940a6320c200c0be36eba2530cc3db77799167285fa8d27ed5959ef4d3cb85a` |
| `REVIEW_VERDICT_01.md` | `017f2af13d18b277b39ff602fab30d1b1433aa3006d1dfefcd1ca6c1fcdad078` |
| `REVIEW_VERDICT_02.md` | `5d2fb71e17f6e2bb7ddfb20bda727543f1a9a589c4ca2d78bf4ab4952d326cc8` |
| `REVIEW_VERDICT_03.md` | `0d27872cda2d18004d1902192aa64e0f0ba7612568051430275cd9ba62c30b26` |
| `check_short_hashes.py` | `4faf5ccc0967a39a9e358b607deb2042afa57cce0bf2ee266d63f8f9dc921e38` |
| `child_briefs/T_K4_GENERATOR.md` | `daa69a7444b20d43f4c0ac8d471f2745f543ee76f8d01f6b875a5ceb8b839d16` |
| `fill_draft.py` | `a9e7cd0a93a0a0cfe586736ad9ed798dd2559b27054b7f3c18c5da9dd97bfa3c` |
| `k1/build_gen_d101_k1.py` | `225b70379c3ea19dcf0751c978dad3287c49fb7f2d4539f60d28bae960190d6b` |
| `k1/evidence_aca930622/grant_table.md` | `3186754a3fe2ec7c0e6e07ed734fd2555fbd71a8d0f4fdce29a114c6e955b2d2` |
| `k1/gen_d101_k1.py` | `4892c6a3c7fab4ba405b1ca201b7cab423c8c59644dee5f1d675d2e5f692cecb` |
| `k1/gen_d101_k1.template.py` | `5a02c6e2dda00c912b71e39dcae74b0a2f9998082259ea314201edae7c5dc069` |
| `k1/run_k1_prototypes.sh` | `3a16ff0d97ad777fd4049c5b7bf60cf55d8600211bfca2fcc5c96c9eb6301360` |
| `k1/verify_d101_k1.py` | `8b42926edad0cceef8a109f230081de58a805855a880712bc97a479b2320cc42` |
| `k4/build_gen_d101_k4.py` | `7b0338321ba2713870028a9e144402429eeb01d641e8844d99aee9b30ab9a0de` |
| `k4/gen_d101_k4.py` | `075036f0a8c214a156aec151aaa52f6d1b78c2694f4306d410579ffcef9f0e73` |
| `k4/gen_d101_k4.template.py` | `97304ec9518cb6108e0032be71278013262add3f1107641f057eb66c437296fd` |
| `k4/run_k4_prototypes.sh` | `5bcbbfb3b5b617bcc9fce25c1270e76664d50678bf68a79de98e749a670d9bec` |
| `k4/tables_k4.py` | `7b1b8a2137596ea5dddacacef41609cc3925998d0f586cc0fc55c3e03f896f8b` |
| `k4/verify_d101_k4.py` | `39f9bbd07a56e88ea06fb105d11d382b05c4a8fd796068342c42101191bc240f` |

Evidence files (`k1/evidence/`, `k1/evidence_aca930622/`, `k4/evidence/`, `evidence/`) are hashed in `SHA256SUMS`.

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
