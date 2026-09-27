---
amendment_id: SCA-APP-011
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-27
status: awaiting_checkpoint_1_acceptance
revision: 2 (adds choice S-c; records stated owner selections A, B, D, S)
basis_commit: e548d4cfada4d2105de6231516dc6e5fc4bd4689
previous_candidate: 5843c0b8c9d283ba7c6683ddb2a342d7288f6142
workflow: scope-change (bundled)
---

# SCA-APP-011 — Checkpoint-group-1 Impact Assessment

> **Status: PROPOSED, awaiting the owner's checkpoint-group-1 act.** This
> package proposes a change and states its impact. It changes no
> decomposition, companion register, PRD, SPEC, PLAN, Scope of Work,
> `_CONTEXT.md`, `_STATUS.md`, dependency register, pointer or code. No
> decision snapshot, `DECISION.md`, `SCA-APP-011_GROUP-1_AUTHORIZED.md` or
> `_LATEST.md` change exists or is implied. Exact amendment text belongs to
> checkpoint group 2.

Abbreviations: **Row n** = row `ActionSeq = n` of `Intake_Actions.csv` in this
snapshot. **Lnnn** = a line of the named file at the basis commit. **SOW** =
the deliverable's `ScopeOfWork.md`. **D** = the App decomposition
`Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.

---

## Checkpoint group 1 — revision 2: final acceptance requested

### Your stated selections (recorded, not yet an acceptance)

On 2026-09-27, through the AskUserQuestion tool, you answered:

- **A** "Rescope it (Recommended)": DQ-R;
- **B** "Exclude it (Recommended)": no legacy-shell removal;
- **D** "Restate them (Recommended)";
- **S** "Remove the route too": S-c.

These are recorded verbatim in `Brief.md`. They are **not** the checkpoint-group-1
acceptance. Nothing is authorized until you accept this package.

### What S-c removes and what it leaves

**Removes** (Rows 33–40):

- the App HTTP route `POST /api/harness/scaffold`;
- its client function `scaffoldHarnessExecutionRoot`;
- the App-side proxy method `scaffold` on `DaemonHarnessPort`/`RuntimeDaemonHarnessPort`, plus their tests;
- DEL-07-02-REQ-009 and the SOW rows that name the route;
- the `/api/harness/scaffold` rows in PRD §9.1, SPEC §17.1 and DEL-03-03's route test index;
- the PRD Journey 7.3 step that calls the route.

It adds the same exception to the route-preservation clauses as for the three
deliverable routes.

**Leaves:**

- the App scaffold library (`lib/harness/scaffold.ts`: the scaffold and preview functions) and its tests;
- DEL-07-02, SOW-024 and SOW-025 (still IN, same carrier, same package);
- OBJ-006 (nine other supporters);
- the retained read-only `scaffold_preview` tool (no scaffold write tool is implemented; SPEC §14.2 lists `mcp__chirality__scaffold` as gated);
- the Root `project-setup` workflow and its packaged `tools/scaffolding` scripts;
- the Runtime's own scaffold API. That API is Runtime-owned; its loop gets an informational notice.

**Nothing working is lost.** In the shipped App the route already fails with
`ENGINE_UNAVAILABLE`/501. The Runtime composition passes no scaffold adapter
(`projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts`
L226), and DEL-07-02 already records this as open gap APP-R058. S-c closes
that gap by removal instead of repair.

**The gap it leaves:** the App has no UI or HTTP way to scaffold an
execution root. A user asks an agent to run the Root `project-setup` workflow.
It scaffolds into `<project>/execution` with the packaged
`scaffold_tool_root.sh`, `scaffold_package.sh`, `scaffold_deliverable.sh` and
`write_status.sh`, through Codex's shell under your approval and sandbox
policy. No live Chirality scaffold tool exists on the Codex path (§17.5).

### New points S-c raises

| # | Point | Options | Recommendation |
|---|---|---|---|
| **M** | **The "MCP interface" is not live on the Codex path.** At basis the App registers no Runtime application-tool catalog. The Chirality tools `status_read`, `status_transition`, `deps_read`, `deps_write` and `scaffold_preview` run only on the retained SDK path. DEL-07-04's SOW (L60) says D-GOV-43/D-APP-127 "do not make them live Codex tools". Exposing them is DEL-06-03's open work. This affects BASE (direction 2: "name MCP as the interface") as much as S-c. | **M-a:** name the library and the Chirality tool contracts as the interface, state plainly that live Codex exposure is DEL-06-03's open application-tool work, and name the Root tools (`write_status.sh`, dependency tools, `project-setup`) as today's agent path. **M-b:** keep the three deliverable routes and the scaffold route until DEL-06-03 exposes the tools live; this reverses directions 2 and S. | **M-a.** The removed routes had no live caller besides the deleted forms, and the scaffold route returns 501, so nothing working is lost. M-a only makes the text truthful. |
| S-lib | The App scaffold library after S-c | **Keep** (it is DEL-07-02's implementation, backs `scaffold_preview`, and is the natural basis for a later application tool), or delete its write path as unreachable. | **Keep.** |
| — | Follow-up to scaffold into `<project>/execution` | No record of this follow-up was found in the repository at basis. `project-setup` already defaults `EXECUTION_ROOT` to `<project>/execution`. The retained library still accepts any contained root. The follow-up belongs to whichever App-side entry is added later (DEL-06-03 tool or a Runtime `ProjectScaffoldPort`); S-c neither closes nor blocks it. | Record it as a DEL-07-02 follow-up at group 2 (informational) |

### Please accept, correct or return group 1

Accepting group 1 accepts, as the basis for group 2:

- the BASE set (Rows 1–19);
- DQ-R (Row 20);
- S-c (Rows 33–40);
- your D answer ("restate");
- set L excluded;
- **E: no change** to CONTRACT or companion-register enforcement wording;
- **M-a** and **S-lib keep**, unless you say otherwise.

That is 28 register rows at group 2: 27 MODIFY and 1 ADD. Topology stays
10 packages / 52 deliverables / 84 scope items / 10 objectives. It
authorizes drafting group 2 only: no file edit, merge, lifecycle, dependency
or pointer change.

A short answer is enough. For example: "Accept group 1: DQ-R, L excluded, D
restate, S-c, E no change, M-a, keep the scaffold library." I then record your
words verbatim in the group-1 decision snapshot and prepare group 2.

## Checkpoint group 1 — revision 1 presentation

Presented at `5843c0b8c`; kept for the record. Its recommendations stand. Its row S said S-c needed a separate SOW-024/DEL-07-02 assessment, which is now §17.

### What accepting group 1 authorizes

Accepting group 1 accepts the **proposed change and its impact** as the basis
for drafting group 2. Specifically:

1. The BASE set (Rows 1–19) as the owner-directed change:
   - delete the Workbench and Pipeline forms and their tests;
   - delete the three HTTP routes `GET /api/working-root/deliverable/status`,
     `POST /api/working-root/deliverable/status/transition` and
     `GET/PUT /api/working-root/deliverable/dependencies`, and the client fetch
     functions that call them;
   - keep the library and the MCP tools, and name them as the interface in
     DEL-07-04, DEL-07-05, DEL-09-03, the PRD and the SPEC;
   - remove the "code retained" clauses from DEL-08-03, SOW-007, SOW-001 and
     the decomposition notes;
   - carve the three routes out of the PRD, PLAN, SPEC and decomposition
     clauses that preserve every existing route.
2. Your choice of DEL-02-02 treatment (choice A) and of the other options
   below.
3. That I prepare the exact amendment text, `Amendment_Actions.csv`,
   `Supersession_Delta.csv` and the propagation plan for checkpoint group 2.

It does **not** authorize any file edit, code merge, dependency change,
lifecycle change or pointer move. The code removal still waits for group 3,
as your direction 3 set out.

### Choices you must make

| # | Choice | Options | Recommendation |
|---|---|---|---|
| **A** | **How to treat DEL-02-02** | **DQ-R:** MODIFY (rescope). Keep ID, name and its live right-panel scope; delete only the Workbench/Pipeline clauses. **DQ-X:** REMOVE, as your option text said, and re-home its right-panel scope. | **DQ-R.** DEL-02-02 is no longer the Workbench/Pipeline deliverable. Since SCA-APP-010 it is "Right-Panel Coordination, Workflows, and Proposal UX" and owns live code: Who is working, the Workflows view and forms, the proposal card and role entry. Retiring it moves that scope to a new carrier and adds churn with no benefit (§4.3). |
| A′ | If DQ-X: where the right-panel scope goes | **X-a:** ADD successor DEL-02-06 (topology 52 → 53). **X-b:** MODIFY DEL-02-01 to absorb it (envelope risk). | X-a, if you choose DQ-X. |
| **B** | **Include the legacy-shell removal (set L)?** | **Exclude** (default): only the forms and routes go, as you directed. **Include:** also delete the loop-first shell reachable only through `WovenDialogueRoute`'s discarded `legacy` prop (`loop-shell`, `portal-loop-shell`, `loop-tertiary-shell`, `sidebar-right-loop-layout`, `tertiary-sidebar-tabs`, `portal/agent-matrix`, the `legacy` prop). | Your call. Including it is the "separate owner decision" that PRD KG-033, PRD §6.4 and D-APP-74 L107 require before the loop-first UI can be retired. Excluding it leaves dead code but changes nothing you did not ask for. |
| **C** | **Scope Items that map only to DEL-02-02** | None exists. SOW-006, SOW-081 and SOW-082 each also map to other deliverables, and no Scope Item goes OUT under any option. What changes is their presentation carrier (§4.1). | Under DQ-R nothing moves. Under DQ-X they are re-homed to X-a or X-b (Rows 24–26); none goes OUT. |
| **D** | **PRD FR-011/FR-012, Journey 7.5 and success metric 7 (Pipeline controls)** | **Restate** as presentation-neutral dispatch-intent semantics owned by DEL-08-03 with no UI surface, or **retire** them. | **Restate.** SOW-007 and DEL-08-03 keep those semantics (`pipeline-dispatch-contract.ts`, `task-scope.ts`). FR-010 (Workbench) is retired either way. |
| **S** | **Execution-root scaffolding entry (`/api/harness/scaffold`)** | The Pipeline form was the only UI caller of `POST /api/harness/scaffold` and `scaffoldHarnessExecutionRoot`. **S-a:** keep the route and client function and restate PRD Journey 7.3 without "opens PIPELINE". **S-b:** also remove the now-unused client function. **S-c:** remove the route too. | **S-a.** You named only the three deliverable routes. S-c would need a separate SOW-024/DEL-07-02 assessment. |
| E | CONTRACT and companion-register enforcement wording ("Status transition API", "Dependency APIs") | **No change** (the library functions remain an API), or clarify it to "library and MCP tool" at group 2. | No change. |

**A short answer is enough**, for example: "Accept group 1 with DQ-R, exclude
L, D restate, S-a, E no change." I then record your words verbatim in the
group-1 decision snapshot and prepare group 2.

### What stays open after group 1

Exact text (group 2); the supersession bindings; the code change, rebased and
completed (§9); dependency re-extraction for DEL-02-02 and its neighbours;
and the post-acceptance `project-setup` INCREMENTAL and `audit-scope-closure`
runs.

---

## 1. Impact verdict

SCA-APP-011 is a **scope-reducing amendment that preserves topology**
(under DQ-R). It removes two obsolete UI forms and three HTTP routes that
only those forms called. It keeps every package, deliverable, objective and
scope item. Under DQ-R: 0 ADD deliverables, 0 REMOVE, 1 ADD Decision Log row,
and MODIFY on DEL-02-02, DEL-02-03, DEL-07-04, DEL-07-05, DEL-08-03,
DEL-09-03, SOW-001, SOW-007, the hard-constraint note, section 13, telemetry,
the PRD, the SPEC and the PLAN. With S-c it also removes `POST
/api/harness/scaffold` and MODIFIES DEL-07-02 and DEL-03-03 (§17). No scope item
goes OUT and no objective loses support. Its main costs are:

- **Verification coverage.** The route test
  `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`
  currently carries the human-ruled CHECKING reversal and the D-GOV-50/51
  ISSUED-reopening gate cases. These must be ported to the library or MCP
  tool before the routes go (§9).
- **Compatibility clauses.** Five App governance clauses promise to preserve
  "any existing route" or "browser API shapes" until separate owner
  acceptance (§5.2). This amendment is that acceptance and must say so.
- **Text alignment across nine Scope of Work contracts** (seven in BASE and
  DQ-R), plus dependency re-extraction (§6).

## 2. Evidence basis

| Evidence | SHA-256 / result |
|---|---|
| `Brief.md` (this snapshot, revision 2) | `177ab18a9c0d49fec1cf9b8005ba00b8ced9739c3fe3bedd72f9f2f8b6192edb` (revision 1: `cc14a829…dfdeef0`) |
| `Intake_Actions.csv` (this snapshot, revision 2) | `e35a3aa84d1943ba8fd41c194691267a893940bb6a4cc2628185007052a8e339`; 40 rows, all `PROPOSED` (revision 1: `ae71b8bf…af7bc`, 32 rows) |
| `Pre_Change_Coverage.json` (this snapshot, revision 2) | `ef2eb2f5e95b655440918d17fa09cfb83d1c8a0f1e1cf02a4a62efb2ff91ab82`; rerun at `5843c0b8c`, reproduced byte-identically; adds `scaffold_route_choice_s_c` |
| `Evidence/Group1/build_pre_change_baseline.py` (revision 2) | `d17933bb0fb136e45c5a40dd07de43eaed4956e54efbb7861ea27dec90f9b4c9` |
| DEL-07-02 SOW / DEL-03-03 SOW | `72c7998754f23868d414d510f6a7f769fe27dbd0cbaeac3fa61e8c52dd9472fb` (equal to the Task Management APP-R058 `SOW_SHA256`) / `b64b5a6183067a51bc9157752ca04a49d97f1cfc0861b2cbd71508cbf61e8eeb` |
| Runtime `packages/daemon/src/app-owned-composition.ts` | `4cd5b16a93b30ccddc05be3d2221cbb46fcd2a5c9c507886333c30974c67f565` (L226: no scaffold adapter) |
| Decomposition / companion register / `_LATEST.md` | `9261ce30…126ea8a6` / `918e475a…a942c` / `6fdba0c9…42c04e3` (full values in `Brief.md`) |
| DEL-02-02 SOW / `Dependencies.csv` / `_DEPENDENCIES.md` | `ade2efc2d8f5f5967e15e42bf697236e20b5f85665cce7652f08c544957f7e77` / `19c2d69e37550feee87ca885b7b3dda6ca073606fa7ea530391a55026389db0b` / `43424bcece77c23a7c60ffb1ebaad17dc805a2ca7c17a726ac10bfb8c7b29161` |
| DEL-02-01 / DEL-02-03 SOW | `e6b9bdd6ee8529af0d0577645f6cfb74f3b21d67e60c3764a24dca08fa521caf` / `b1331dc43e2ec096c13924ca5dbc200be9d1fc79ae60b9b1276aaa9b2020b48a` |
| DEL-07-04 / DEL-07-05 SOW | `7b4048b814680a668e2630d4cb6d689cc277816c9888696b74faa2f6fd14e00b` / `230aa4a92660f0d51822c911fbabf78f3dbd187069934c12b3fc05f2d4655405` |
| DEL-08-02 / DEL-08-03 SOW | `2a9dc258d8e79627b8fb36ed7dc72dc8ea0b22b396b80260942289fe6389c607` / `47842ddeac2a1508a2755a5b145c243b72d92d4b79276ec7e0a37840f493ade9` |
| DEL-09-03 SOW | `18b163976561487325e737116d85f350e9bda4d4b839e1afedada3e0be6002ec` |
| Code-removal candidate | `dcd37f9ae9d22bfedc86b921f6e2ac70b90e1419` on `worktree-agent-a0de269a96f5dd4af`; parent `947075c9a`, 22 commits behind `origin/main` |

## 3. Impact by action

| Row(s) | Set | Entity | Affected sections / files | Owning workflows after acceptance |
|---|---|---|---|---|
| 1 | BASE | DEL-07-04 | D L365 (artifacts); SOW L59, L64, L86, L116, L161-162 (REQ-007/008), L213, L296-297; `_CONTEXT.md` | project-setup INCREMENTAL (`scope-of-work` REVISE); dependency-extract |
| 2 | BASE | DEL-07-05 | SOW L60, L181, L211 (REQ-013), L242, L338; `_CONTEXT.md` | same |
| 3 | BASE | DEL-09-03 | SOW L157 | same |
| 4 | BASE | DEL-08-03 | D L375; SOW L38, L42, L48 (obligation 2), L111, L118, L134, L142, L239 (REQ-012), L267, L285, L293, L405, L438; `_CONTEXT.md` L39 | same |
| 5, 6 | BASE | SOW-007, SOW-001 | D L182/L415, L176/L409 (Notes only) | audit-decomp |
| 7 | BASE | Hard constraint | D L102 | audit-decomp |
| 8, 9, 10 | BASE | §13 note, DEC-026, telemetry | D L672, L613-L658, L496-L513 | audit-decomp |
| 11–14 | BASE | PRD | `docs/PRD.md` L140, L161, L289, L327, L353, L381, L424, L429, L442-443, L453, L459-472, L598-608, L879-881, L1656, L1669, L1709, L1738, L1744 | audit-scope-closure |
| 15–17 | BASE | SPEC | `docs/SPEC.md` §5.2 L422-423 and L474-475; §17.2 L1109-1111; §17.3 L1126-1127, L1132-1133; §17.9 L1237-1249 | audit-scope-closure |
| 18 | BASE | PLAN | `docs/PLAN.md` L36, L45, L114-118, §13 | audit-scope-closure |
| 19 | BASE | DEL-02-03 | SOW CLM-029 L322 | project-setup INCREMENTAL |
| 20 | DQ-R | DEL-02-02 | D L313; SOW L90 and L109 (obligation 1), SCA-APP-004 section L18-66 (obligation 4 at L61-63), CLM-001 to CLM-027 Workbench/Pipeline content (REQ table L234-244, CLM-014 L292-296); `_CONTEXT.md` L40 | project-setup INCREMENTAL; dependency-extract |
| 21–27 | DQ-X | DEL-02-02 REMOVE; DEL-02-06 ADD or DEL-02-01 MODIFY; SOW-006/081/082 ledger; telemetry | D L313, L414, L489, L490, L496-L524, L584; DEL-02-02 `_STATUS.md` history line | project-setup INCREMENTAL (scaffold DEL-02-06, record retirement); dependency-extract for DEL-02-02 and eight neighbours |
| 28–32 | L | DEL-02-01, DEL-08-02, SOW-001, PRD, PLAN, SPEC | DEL-02-01 SOW L57, L108; DEL-08-02 SOW verification hooks; D L176/L409; PRD L161, L327, L353, L381, L1669, L1709; PLAN L36, L118, L556; SPEC L1248 | project-setup INCREMENTAL; audit-scope-closure |
| 33–40 | S-c | DEL-07-02, DEL-03-03, PRD, SPEC, PLAN, hard constraint | DEL-07-02 SOW L53, L85, L119, L145, L178, L202, L220, L303, L320, L331, L405, L468; D L102, L324; DEL-03-03 SOW L181; PRD L161, L327, L381, L391, L426-438, L864, L868, L1651, L1669; SPEC L1095, L1099, L1244-1249; PLAN L44, L185 | project-setup INCREMENTAL (`scope-of-work` REVISE for DEL-07-02, DEL-03-03); audit-scope-closure; Runtime notice (informational) |

## 4. Coverage

### 4.1 Scope Items and Objectives

| Entity | Current carriers | Only via DEL-02-02? | DQ-R | DQ-X |
|---|---|---|---|---|
| SOW-006 (Who is working, Session view, role entry) | DEL-02-02, DEL-05-04, DEL-08-02 | No (but DEL-02-02 is the only **presentation** carrier; DEL-05-04 and DEL-08-02 own semantics) | Unchanged, IN | Re-home presentation to X-a/X-b; stays IN |
| SOW-081 (governed workflows and the Workflows view) | DEL-07-03, DEL-02-02, DEL-04-04 | No (DEL-02-02 is the only view/forms carrier) | Unchanged, IN | Re-home the view to X-a/X-b; stays IN |
| SOW-082 (prompted ladder and proposal card) | DEL-06-03, DEL-05-02, DEL-02-02, DEL-08-01 | No (DEL-02-02 is the only card carrier) | Unchanged, IN | Re-home the card to X-a/X-b; stays IN |
| SOW-007 (dispatch lane semantics) | DEL-08-03 | Not mapped to DEL-02-02 (DEP-02-02-003 already `RETIRED`) | Notes change (Row 5); stays IN | Same |
| SOW-028 / SOW-029 | DEL-07-04 / DEL-07-05, and DEL-09-03 | No | Interface named as library + MCP; stays IN | Same |
| OBJ-001 | 9 active deliverables | No (8 others) | Unchanged | Unchanged |
| OBJ-007 | 8 active deliverables | No (7 others) | Unchanged | Unchanged |

**No Scope Item or Objective loses its only deliverable, and none goes OUT,
under any option.** The amendment removes no scope item. The Workbench and
Pipeline presentation that was deleted never had a scope item of its own
after SCA-APP-010: SOW-007's presentation half was retired there, and the
Workbench form traced only to legacy PRD FR-010.

### 4.2 Requirements that lose their only home

| Requirement | Treatment (both DQ options unless stated) |
|---|---|
| DEL-02-02-REQ-001 to REQ-011, CLM-014 (Workbench/Pipeline selection and contract panels; REQ-004 names `canAgentTransitionLifecycle`, already removed by the candidate) | Retired as history, `[RETIRED — SCA-APP-011]` (DQ-R); or retired with the deliverable (DQ-X). No successor needed. |
| DEL-02-02 SCA-APP-004 obligation 4 (Workbench and Pipeline preserve deep-link intent, categories, lifecycle guards, disabled options) | Retired. Category and disabled-option semantics survive in DEL-08-03; deep-link and query compatibility survive in DEL-02-01/DEL-08-02 (page URLs stay, Q3). |
| DEL-07-04-REQ-007 / REQ-008 (HTTP status read/transition API) | Retired. Status read and transition remain through the library and the `status_read`/`status_transition` tool contracts (SPEC §14.2). These run on the retained SDK path only; their live Codex exposure is DEL-06-03's open work (§5.7, choice M). |
| REQ-DEL-07-05-013 (HTTP GET/PUT dependencies) | Restated to the library and `mcp__chirality__deps_read`/`deps_write`. |
| PRD FR-010 (Workbench) | Retired. |
| PRD FR-011, FR-012, Journey 7.5, success metric 7 | Restated to DEL-08-03 semantics (choice D, recommended) or retired. |
| PRD Journey 7.3 step 2 ("User opens PIPELINE") | Restated (choice S). |
| DEL-08-03-REQ-012 (pipeline selector tests) | Restated to task-scope selection and dispatch-contract tests. |
| DEL-02-03 CLM-029 Pipeline scope-scan examples | Withdrawn. |

### 4.3 Why DQ-R is recommended over DQ-X

- DQ-R changes one deliverable's text. DQ-X retires a deliverable with live,
  merged code (PR733 and the V3-04 slice) and seated Remaining items, then
  recreates the same scope under a new ID (X-a) or overloads DEL-02-01 (X-b).
- DQ-X invalidates cross-references by ID: DEP-06-03-014, DEP-08-01-018 (they
  cite `DEL-02-02-V3-04`), DEP-02-01-007, DEP-02-04-015, DEP-05-02-016,
  DEP-06-03-016, DEP-07-03-012, the D-APP-108/109/110 records and the
  Task Management items TM-APP-046/047. All of these would need re-keying.
- The contract prefers the smallest amendment (type-level change
  preference). The only reason for DQ-X is the folder name
  `…Workbench_and_Pipeline_Selection_UX`. A folder rename is not proposed:
  stable IDs and paths are kept, and the display name already reads
  correctly.

## 5. Findings

### 5.1 Known conflicts, each verified

| Reported conflict | Verified | Evidence at basis |
|---|---|---|
| SCA-APP-010 controlling contract, obligation 1: unmounted "with code, routes, and tests retained" | Yes | DEL-02-02 SOW L90 and L109; D L313; SCA-APP-010 `Brief.md` exclusion "Deletion of Workbench, Pipeline, or Work-projection code, routes, or tests"; Supersession_Map D-015 ("deletion remains separately gated") |
| DEL-02-02 REQ-001 to REQ-011 and CLM-014 describe the forms; REQ-004 names `canAgentTransitionLifecycle` | Yes, with a correction | SOW REQ table L234-244, CLM-014 L292-296. **Correction:** these are dated legacy clauses; DEL-02-02's controlling scope is the right-panel coordination carrier (Brief, premise correction) |
| DEL-08-03 obligation 2 and applied row note "(code retained)"; outputs list "Pipeline selector tests" | Yes | SOW L38, L42, L48; D L375; `_CONTEXT.md` L39 |
| DEL-07-04, DEL-07-05, DEL-09-03 SOWs name the three routes | Yes | DEL-07-04 SOW L59, L161-162, L296-297; DEL-07-05 SOW L60, L181, L211, L338; DEL-09-03 SOW L157 (status and dependencies only; the transition route is not named there) |
| Decomposition v3.2 "unmounted, not deleted" | Yes | D L672; also L176, L182, L313, L375, L409, L415 |
| PRD §8.2 FR-010 to FR-012 | Yes | PRD L605-607 |
| PLAN §1 / §13 | Yes | PLAN L36 and L45 (§1); L531-556 (§13.2) |
| PRD §2 | **Not reproduced** | PRD §2 (L31-L132) does not mention Workbench or Pipeline. The nearest is §3.1 goal 4 (L140) |
| PRD §6, §7, KG-033, §16 | Yes | L289, L327, L353, L381 (§6); L424-472 (§7); L1709 (KG-033); L1738, L1744 (§16) |
| App SPEC sections naming the routes or forms | Yes | §5.2 L422-423 and L474-475; §17.2 L1109-1111; §17.3 L1126-1127 and L1132-1133; §17.9 L1237-1249 |

### 5.2 Additional conflicts found

1. **Route-preservation clauses** that require separate owner acceptance
   before any existing route is deleted: PRD §3.1 goal 25 (L161), §6.1 (L327),
   §6.4 out-of-scope (L381), §14 metric 20 (L1669); PLAN §3 (L114-118); SPEC
   §17.9 (L1244-1249); decomposition hard constraint (L102); D-APP-74 L97-99.
   Rows 7, 13, 15 and 18 carry these.
2. **PRD §9.2** lists the three routes (L879-881). Row 12.
3. **PRD Journey 7.3** begins "User opens PIPELINE" to scaffold. The Pipeline
   form was the only UI caller of `POST /api/harness/scaffold` (choice S).
4. **Test coverage of lifecycle gates.** The route test carries the
   CHECKING-reversal and ISSUED-reopening cases (`deliverable-contracts.test.ts`
   describe blocks at L331 and L522). DEL-07-04's verification hooks name it.
   It must be ported, not deleted (§9).
5. **DEL-02-03 CLM-029** keeps "scope-scan/deliverable-routing examples from
   the old Pipeline surface" as current compatibility obligations. Row 19.
6. **Legacy loop-first UI** (set L only): DEL-02-01 SOW L57 ("Keep the
   existing loop-first and matrix UI reachable until separately …") and L108;
   PRD KG-033 "do not retire the existing legacy loop-first UI without a
   separate owner decision"; D-APP-74 L107.
7. `projects/chirality-app-dev/docs/ISSUE_READINESS_PROFILES.md` L38 names
   "workbench/pipeline" as an example deliverable class for the UI/product
   evidence profile. This is descriptive, not scope. NO_CHANGE; optional
   wording tidy by the owning loop.
8. `exports/chirality-app/` projection lists the deleted files. It is a
   derivative, regenerated with the code change.

### 5.3 DEL-02-02 identity

See `Brief.md`, "Premise correction". Decomposition L313 name and
description; SOW L82-91; DEP-02-02-010/011/013-022 rows; live code under
`frontend/src/components/woven-dialogue/`.

### 5.4 DEL-08-03 type

DEL-08-03 is typed `UX_UI_SLICE` but will have no UI consumer. Changing its
type would be a contract-level attribute change with no scope effect. No
change is proposed. The owner may raise it later.

### 5.5 Page URLs

`/workbench` and `/pipeline` (and `/`, `/chat`) are page routes, not the HTTP
API routes. After the forms are gone they still resolve into the dialogue
shell (`WovenDialogueRoute` discards its `legacy` prop). D-APP-108 Q3 stands
under every set. `SPEC §17.9` query parameters (`category`, `taskScopeMode`,
`scopeKey`, `targetDeliverableKey`) stay round-trippable. With the forms gone
they have no consumer. This is recorded, not changed.

### 5.6 Surfaces proposed NO_CHANGE

| Surface | Reason |
|---|---|
| `docs/CONTRACT.md` K-GATE-1, K-STATUS-1/2, K-DEP-1 enforcement columns ("Status transition API", "Dependency APIs") and the matching companion-register rows | The library functions remain APIs and the MCP tools are already named. Choice E |
| `docs/TYPES.md` §4 Pipeline terms | DEL-08-03 dispatch vocabulary, unchanged |
| `docs/DIRECTIVE.md` L234 | Preserves routes, queries, aliases and matrix behavior; page URLs stay |
| DEL-05-01 SOW L350 (`"mode": "WORKBENCH"`) | Historical session-record fixture value |
| DEL-08-02 SOW L183 (PRD "workbench context" source row) | Historical source reference (set L touches only its hooks) |
| DEC-025 and the Change Log entry of SCA-APP-010 | Historical records; DEC-026 records the change |
| `frontend/docs/harness/tool_catalog.md`, Runtime tool descriptors | MCP tools unchanged |

### 5.7 The Chirality tools are not live on the Codex path (choice M)

The App registers no Runtime application-tool catalog at basis: no App source
calls `registerApplicationTools`, and the Runtime's `ApplicationToolRegistry`
is empty unless a host registers one. The Chirality tools in
`frontend/src/lib/harness/mcp/read-tools.ts` (`status_read`,
`status_transition`, `deps_read`, `deps_write`, `scope_scan`,
`scaffold_preview`) are wired only through the retained SDK path
(`sdk-options-builder.ts` and `claude-agent-sdk-manager.ts`, reached through `lib/harness/runtime.ts`, which no product module imports). DEL-07-04 SOW L60
records that D-GOV-43/D-APP-127 "do not make them live Codex tools".
DEL-06-03 (SOW L35 and L93) owns exposing them through the Runtime
application-tool interface; that work is open.

Direction 2 ("name MCP as the interface") therefore needs truthful wording.
Removing the routes loses nothing live: their only caller was the deleted
forms. But after removal, an agent on Codex reads or transitions status and
dependencies through the Root tools (`write_status.sh`, the dependency
workflows) or file edits, not through a Chirality tool. The presentation
offers M-a (recommended: truthful wording) and M-b (keep the routes until
DEL-06-03 lands).

## 6. Dependencies and the DAG

**D-GOV-49 currency.** The App has **no accepted project DAG** (no
`execution/_DAG/`; D-GOV-49 Adoption; App SPEC §5.2 L420). Its blockers follow
the recorded registers. There is therefore no accepted DAG version to mark
stale and no `DAG pending` state. The legacy SCC case home stays in PKG-00.
Closure at basis: 54 nodes, 111 edges, **0 SCCs** (`Pre_Change_Coverage.json`
`tools.analyze_dep_closure`).

**Rows touching DEL-02-02** (27 in total: 22 in its own register, 5 in others):

| Rows | Content | DQ-R | DQ-X |
|---|---|---|---|
| DEP-02-02-001 to 004, 010 to 012 (anchors) | PKG-02, SOW-006, SOW-007 (already `RETIRED`), OBJ-001, SOW-081, SOW-082, OBJ-007 | Unchanged | Whole register retired; successor re-extracted |
| DEP-02-02-005 to 009 | Retained Workbench/Pipeline code → DEL-02-01, DEL-02-03, DEL-07-04, DEL-07-05, DEL-08-03 | **Retire** (the retained code is deleted) | Retire |
| DEP-02-02-013 to 022 | Right-panel interfaces (DEL-07-03, DEL-06-03, DEL-05-02, DEL-08-05, DEL-05-04, DEL-08-04, DEL-08-02, DEL-02-03, DEL-02-04) | Unchanged | Move to the successor |
| DEP-02-01-007 (DEL-02-01 → DEL-02-02, Workbench deep-link compatibility) and DEP-02-01-008 (→ DEL-08-03, Pipeline deep-link) | Open owner item HGD-2 in DEL-02-01 `_DEPENDENCIES.md` ("retire or keep as compatibility-only") | Retire DEP-02-01-007; DEP-02-01-008 decided by HGD-2 at re-extraction | Same, retargeted |
| DEP-02-04-015, DEP-05-02-016 (already `RETIRED`), DEP-06-03-016, DEP-07-03-012; statement references in DEP-06-03-014, DEP-08-01-018 | Right-panel handovers | Unchanged | Retarget to the successor |
| DEP-08-03-010 (pipeline selector test handover), DEP-08-02-003/005 (WORKBENCH wording) | Statement wording | Refresh at re-extraction | Same |

Only edges are removed. No new edge is proposed, so no cycle can form. Every
change is a dependency-extract rerun after acceptance, never a direct write
by this workflow.

## 7. Downstream consumers

| Consumer | Uses the three routes? | Effect |
|---|---|---|
| App frontend | Only through `lib/workspace/deliverable-api.ts`, called only by the Workbench and Pipeline forms | Removed with the forms |
| MCP tools (`frontend/src/lib/harness/mcp/read-tools.ts`) | No. They call `deliverable-contracts.ts` directly | Unchanged |
| Runtime (`projects/chirality-runtime`) | Not the three deliverable routes: `packages/contracts/src/harness/tool-descriptor.ts` and `mcp/tool-names.ts` name only the MCP tools `deps_read`, `status_transition` and `deps_write`. Under S-c, the Runtime scaffold API (`/v1/projects/{id}/scaffold`) loses its only client (§17.1) | BASE: none. S-c: informational notice to the Runtime loop, which decides whether to keep its API |
| App harness catalog `frontend/docs/harness/tool_catalog.md` | MCP only | None |
| Piping, PEC, Root `tools/` | No reference found | None |
| `exports/chirality-app` projection | Lists the files | Regenerated with the code change |
| Historical run records, secret-scan and review hash files, tranche manifests | Mention paths | Historical; not rewritten |

## 8. ISSUED deliverables

**None.** Verified across the whole App: 53 deliverables `IN_PROGRESS`, 1
`OPEN` (retired DEL-09-07); no `ISSUED`; no `CHECKING`. All eight affected
deliverables are `IN_PROGRESS`. No reopening is authorized or needed, and no
`CHECKING` reversal is involved. `ScopeChanging` is recorded on every row
regardless.

## 9. The code-removal candidate `dcd37f9ae`

**What it does** (26 files, +331/−3869): deletes `WorkbenchSurface`,
`PipelineSurface`, `LifecycleGateFields` and their tests
(`workbench-surface.test.ts`, `pipeline-surface.test.ts`,
`lifecycle-transition-gates.test.tsx`); removes their tertiary sidebar tabs,
form-only CSS and form-only helpers in `deliverable-api.ts` (including
`canAgentTransitionLifecycle`); trims two shell tests; edits App SPEC §5.2 and
§17.3, the DEL-02-02, DEL-07-04 and DEL-08-03 SOW verification hooks, three
MEMORY files, two receipts, a work graph, `LOOP_RECEIPTS.md`, the export
projection and a tranche manifest. **It keeps the three routes and the
client fetch functions**, because it predates your direction 2.

**What it still needs once SCA-APP-011 is accepted:**

1. **Rebase** onto current `main`. It is 22 commits behind. A test merge
   conflicts only in `exports/chirality-app/export-report.md`, a derivative to
   regenerate.
2. **Delete the routes:**
   `frontend/src/app/api/working-root/deliverable/status/route.ts`,
   `…/status/transition/route.ts` and `…/dependencies/route.ts`. Keep
   `…/content/route.ts`, which `components/shell/document-view.tsx` calls.
3. **Delete the client fetch functions.** After the candidate,
   `lib/workspace/deliverable-api.ts` exports only `fetchDeliverableStatus`,
   `transitionDeliverableStatus` (client copy), `fetchDeliverableDependencies`,
   their types and `WorkspaceApiClientError`. Its only importer is its own
   test. Delete the file and
   `__tests__/lib/workspace-deliverable-api.test.ts`. The library
   `transitionDeliverableStatus` in `deliverable-contracts.ts` stays.
4. **Port, do not drop, the route tests.**
   `__tests__/api/working-root/deliverable-contracts.test.ts` exercises the
   status, transition and dependency routes, including the CHECKING-reversal
   and ISSUED-reopening gates. Retarget those cases to
   `lib/workspace/deliverable-contracts.ts` and/or the MCP tool tests
   (`chirality-mutating-mcp.test.ts`), and keep the content-route cases.
   DEL-07-04 and DEL-07-05 hooks then name the new tests.
5. **Fix the SPEC text it wrote.** Its §5.2 keeps "the working-root
   dependencies API", and its §17.3 says the rules are "served by the §17.2
   APIs and the MCP tools". Both become the library and MCP tools.
6. **Take scope text from group 2, not from the candidate.** The candidate
   edited three SOWs and the SPEC before any checkpoint. Its receipt already
   holds the merge. Those edits should be dropped from the code PR, or
   replaced by the exact group-2 text inside its write boundary. Either way
   they land only after group-3 acceptance.
7. **Also update** the scope text named in Rows 1–4, 19 and 20 (or 21–27),
   the decomposition, PRD, SPEC and PLAN rows. This is the SCA-APP-011
   application, not the code PR.
8. **(Set L is excluded by the stated selection B.) If set L were included:** delete `tertiary-sidebar-tabs.tsx` outright
   (the candidate only trims it) together with the other legacy-shell files
   and tests.
9. **Update** the tranche manifest `APP-REMOVE-LEGACY-FORMS-20260927.yaml`
   for the added deletions, and regenerate the export projection.
10. **S-c:** remove the scaffold route, client function and App port member as in §17.2, and keep the scaffold library.
11. **Rerun** the affected checks on the actual rebased candidate:
    typecheck, full frontend tests, and the harness and registered checks.

## 10. Package-role classification and derivative status

| Surface | Package role | Classification | Authority basis |
|---|---|---|---|
| Decomposition v3.2 | Working surface | DIRECT_EDIT at application | Group-2 exact text |
| `contract_invariant_coverage_register.csv` | Authoritative companion register | NO_CHANGE (choice E) | §5.6 |
| `docs/PRD.md`, `docs/SPEC.md`, `docs/PLAN.md` | Authoritative carriers outside the decomposition | DIRECT_EDIT only if the group-2 write boundary names them | Contract `ALLOWED_PROPAGATION_WRITES` |
| Affected `ScopeOfWork.md` (DEL-02-02, 02-03, 07-04, 07-05, 08-03, 09-03; set L adds 02-01, 08-02) | Deliverable production contracts | Named in the group-2 boundary, or handed to `project-setup` INCREMENTAL (`scope-of-work` REVISE) | Contract non-ownership |
| Affected `_CONTEXT.md` | Working surface | DIRECT_EDIT at application | Contract default write scope |
| DEL-02-02 `_STATUS.md` | Working surface | DQ-X only: one appended history line | Contract retirement rule |
| `Dependencies.csv` / `_DEPENDENCIES.md` | Deliverable dependency evidence | RECOMPUTE by dependency-extract | §6 |
| `_ScopeChange/_LATEST.md` | Snapshot / handoff artifact | Unchanged until group 3 | Candidate posture `ACCEPTED_PREDECESSOR` (SCA-APP-010) |
| `_Evaluation/DecompCoverage`, `ScopeClosureAudit`, `DepClosure` snapshots | Derived publication artifacts | STALE_REBUILD_REQUIRED after application | audit-decomp, audit-scope-closure, analyze_dep_closure |
| `exports/chirality-app` | Derived publication artifact | Regenerated with the code change | Export tooling |

## 11. Orphan and structural risk

| Check | DQ-R | DQ-X (X-a) | DQ-X (X-b) |
|---|---|---|---|
| IN scope items without a deliverable | 0 | 0 (after Rows 24–26) | 0 (after Rows 24–26) |
| Objectives without a deliverable | 0 | 0 | 0 |
| Packages without a deliverable | 0 | 0 (PKG-02 keeps four active plus DEL-02-06) | 0 |
| Dangling dependency references | 5 own rows + DEP-02-01-007 to retire | 22 own rows retired; 7 cross-references to re-key | same as X-a |
| Topology | 10 / 52 / 84 / 10 | 10 / 53 (two retired IDs) / 84 / 10 | 10 / 52 / 84 / 10, DEL-02-01 envelope reassessed |
| Package-discipline rule | Kept | Kept | Risk: DEL-02-01 likely exceeds envelope M |

S-c changes no topology, count or mapping (§17.4).

## 12. Estimate and schedule staleness

The App carries no `_Estimates` tool root. The structure audit reports it
missing, which is carried. No estimate or schedule artifact is affected.
Work graphs that cite the forms (`app-lifecycle-deps-2026-09-26`, where the
candidate withdraws FU3) are execution-state records maintained by their
loop.

## 13. Active snapshot and handoff-state impact

- Pointer posture for group 3: **`ACCEPTED_PREDECESSOR`**, with
  `_LATEST.md` naming SCA-APP-010. It stays unchanged until SCA-APP-011's
  group-3 acceptance.
- Group-1 and group-2 decisions will be recorded under
  `_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-{1,2}_{date}/`, with
  `SCA-APP-011_GROUP-{1,2}_AUTHORIZED.md` pointers. This is the first App run
  to use that layout. The folder does not yet exist and is not created here.
- The cumulative supersession map is carried forward from SCA-APP-010
  through `accumulate_supersession_map.py` at group 3.

## 14. Supersession bindings to prepare at group 2

| Rows | Superseded authority fact | Type |
|---|---|---|
| 1, 2, 7, 12, 13, 15 | D-APP-74 L97-99: existing routes and browser APIs remain compatibility surfaces "until separately retired" | SUPERSESSION (the three deliverable routes retired) |
| 4, 5, 20 or 21 | SCA-APP-010 Supersession_Map D-006 and D-015; SR-06 "the code stays"; D-APP-74 L107 | SUPERSESSION (form code and tests deleted) |
| 28, 30, 31, 32 (set L only; excluded by stated selection B) | D-APP-74 L107; PRD KG-033 "separate owner decision" | SUPERSESSION (loop-first UI retired) |
| 33, 34, 35, 37, 39, 40 (S-c) | D-APP-74 L97-99 for `POST /api/harness/scaffold` | SUPERSESSION (scaffold route retired) |

## 15. Recommended downstream reruns (after group 3; none executed here)

1. `project-setup` in `INCREMENTAL` mode: `scope-of-work` REVISE for the
   modified deliverables not written directly, and, under DQ-X, recording the
   DEL-02-02 retirement and scaffolding DEL-02-06.
2. `dependency-extract` for DEL-02-02 (or its successor), DEL-02-01,
   DEL-02-03, DEL-07-04, DEL-07-05, DEL-08-02 and DEL-08-03, then
   `analyze_dep_closure.py`.
3. `audit-decomp` (post-change baseline) and `audit-scope-closure`.
4. Under S-c, an informational notice to the Runtime loop about its now-unused scaffold API (§17.3).
5. The code change (§9, §17.8), under the App loop and standing Git authority, once
   group 3 is accepted.

## 16. What checkpoint group 2 will contain

`Amendment_Preview.md` with exact before/after text for every selected row;
`Propagation_Plan.md` with the exact write boundary, including which SOWs and
PRD/SPEC/PLAN passages this amendment writes directly; `Amendment_Actions.csv`
limited to the selected sets, with `ScopeChanging` on every row;
`Supersession_Delta.csv`; and the validation plan. Under M-a, the interface wording in Rows 1, 2, 12, 15, 33 and 36 names the library and the Chirality tool contracts, states that live Codex exposure is DEL-06-03's open application-tool work, and names the Root tools as today's agent path.

## 17. Choice S-c — removing `POST /api/harness/scaffold` (Rows 33–40)

### 17.1 Call chain at basis

| Layer | Element | Location | Other callers? |
|---|---|---|---|
| UI | Pipeline form, "Execution Root Scaffold" panel | `components/pipeline/pipeline-surface.tsx` L9, L665, L929 | Deleted by BASE |
| App client | `scaffoldHarnessExecutionRoot` | `lib/harness/client.ts` L431-445 | **None** in product code; test `__tests__/lib/harness-client.test.ts` L9, L248-290 |
| App HTTP route | `POST /api/harness/scaffold` | `app/api/harness/scaffold/route.ts` | Only the client function; test `__tests__/api/harness/scaffold-route.test.ts` |
| App → Runtime port | `DaemonHarnessPort.scaffold` (interface L317-320, unavailable stub L358, scope map L423) and `RuntimeDaemonHarnessPort.scaffold` (L602-619, containment check, then `client.scaffold`) | `lib/runtime-client/daemon-harness-port.ts`, `runtime-daemon-harness-port.ts` | Only the route; tests `runtime-daemon-harness-port.test.ts` L96 and L1004-1045, `daemon-proxy-boundary.test.ts` L49, `turn-route-attachments.test.ts` L54, `fake-daemon-harness-port.ts` L262 |
| Runtime (Runtime-owned) | `RuntimeClient.scaffold`, `RUNTIME_ROUTES.scaffold` (`/v1/projects/{id}/scaffold`), daemon handler, `RuntimeService.scaffold`, `ProjectScaffoldPort`, `ScaffoldRequest`/`ScaffoldResponse` | `projects/chirality-runtime/packages/{client,contracts,daemon,core}` | Only the App port. **No `ProjectScaffoldPort` implementation exists**: the production composition (`packages/daemon/src/app-owned-composition.ts` L226) and every test or CI composition pass `undefined`, so `RuntimeService.scaffold` throws `ENGINE_UNAVAILABLE` (501) |
| App library | `scaffoldExecutionRoot` (write) | `lib/harness/scaffold.ts` L852 | **No product caller today**, since the route goes to the Runtime, not to the library. Test callers: `harness-scaffold.test.ts` and the test fake port |
| App library | `previewScaffoldExecutionRoot` (read) | `lib/harness/scaffold.ts` L507 | `scaffold_preview` tool in `lib/harness/mcp/read-tools.ts` L756-762 (retained SDK path) and tests |
| Shared types | `ScaffoldExecutionRootRequest/Response` | Runtime `packages/contracts/src/harness/types.ts` L98, L137 | Used by the App port and by Runtime; stay while Runtime keeps its API |

Other projects: the Electron main/desktop (`frontend/electron`), App
`scripts/`, Piping, PEC and Root `tools/` have no reference to the route or
the client function. `scripts/prepare-packaged-instruction-root.mjs`
packages Root `tools/scaffolding/*` into the instruction root. That is the
Root scaffolding path, and it is unaffected. Historical run records and
secret-scan lists mention the paths and are not rewritten.

### 17.2 What S-c removes (after group 3; not in this package)

1. `app/api/harness/scaffold/route.ts` and `__tests__/api/harness/scaffold-route.test.ts`.
2. `scaffoldHarnessExecutionRoot` in `lib/harness/client.ts`, the
   `ScaffoldExecutionRootResponse` import if it then has no other use, and the
   client test case.
3. The App-side `scaffold` member of `DaemonHarnessPort`: the interface,
   `daemonClientUnavailable` entry and scope map in `daemon-harness-port.ts`,
   `RuntimeDaemonHarnessPort.scaffold`, and the matching test stubs and cases
   in the four test files above. The scope-map type
   (`Record<keyof DaemonHarnessPort, …>`) makes a partial removal fail to
   compile, which is a useful check.
4. Scope and governance text: Rows 33–40.

### 17.3 What stays

- `lib/harness/scaffold.ts` (both functions) and `harness-scaffold.test.ts`
  (choice S-lib, recommended keep). This is DEL-07-02's implementation and
  the basis of `scaffold_preview`. If S-lib were "delete the write path", DEL-07-02
  would keep only the preview and parser, and SOW-024 would rest on Root tools
  alone. That is not recommended.
- The retained SDK-path tools (`scaffold_preview`; SPEC §14.2's gated
  `mcp__chirality__scaffold`, not implemented), unchanged.
- The Runtime scaffold API. It loses its only client. Keeping or removing it is
  the Runtime loop's decision; an informational notice is recommended at
  application (no Runtime scope or behaviour changes because of this
  amendment).
- `/api/working-root/deliverable/content`, `/api/project/deliverables` and all
  other `/api/harness/*` routes.

### 17.4 Scope, coverage and deliverables

| Entity | Effect | Only deliverable lost? | OUT? |
|---|---|---|---|
| SOW-024 (execution-root scaffolding), IN, PKG-07 | Carrier DEL-07-02 unchanged; it loses its App HTTP entry, not its scope | No (DEL-07-02 remains) | No |
| SOW-025 (flat package/deliverable layout), IN, PKG-07 | Unaffected; the library and scanner keep the layout rules | No | No |
| OBJ-006 | DEL-07-02 plus 9 other active supporters | No | — |
| DEL-07-02 (IN_PROGRESS) | MODIFY, `ScopeChanging` YES (Row 33): REQ-009 retired; route rows in SOW L53, L85, L119, L145, L178, L202, L220, L303, L320, L331, L405 restated; APP-R058 (L468) closed by removal; decomposition row L363 unchanged | — | — |
| DEL-03-03 (IN_PROGRESS) | MODIFY, `ScopeChanging` YES (Row 34): decomposition row L324 "keep `/api/harness/*` shapes … stable" gains the exception; SOW CLM-019 route index drops the row (L181) | — | — |
| DEL-09-03 | Its SOW names no scaffold route test; the `scaffold` behaviour list is unchanged | — | — |
| Dependency rows | DEL-07-02 has 7 rows (3 anchors, 4 upstream); none names the route; no row in any register names `/api/harness/scaffold` | No edge change | — |
| Tracking | Task Management `APP-R058` (`SCAFFOLD_LIVE_GAP_TRANSFER`, `DEFER_WITH_HOLD`: "No scaffold live-operation acceptance while ProjectScaffoldPort/501 composition is absent") | Its premise changes: after S-c there is no App live scaffold operation to accept. Group 2 proposes the exact disposition note | — |

No Scope Item or Objective loses its only deliverable or goes OUT. The
decomposition topology and counts are unchanged by S-c.

### 17.5 The resulting gap, and how a user scaffolds

With the Pipeline form and the route gone, **the App has no UI or HTTP way to
scaffold an execution root**. There is also no live Chirality tool for it on
the Codex path: the App registers no Runtime application-tool catalog, and
`scaffold_preview` is read-only and SDK-path only.

In practice the same is already true today, because the route returns 501
in the shipped composition. A user scaffolds by asking an agent in a chat
whose folder is the project (typically WORKING_ITEMS, `Workflow:
project-setup`, `INITIAL` mode). The workflow:

- defaults `EXECUTION_ROOT` to `<project>/execution`
  (`workflows/project-setup/resources/contract.md` L9);
- runs the packaged Root scripts `scaffold_tool_root.sh`, `scaffold_package.sh`,
  `scaffold_deliverable.sh` and `write_status.sh`
  (`workflows/project-setup/resources/method.md` L83-L111) through Codex's
  native shell, under the user's approval and sandbox policy;
- stops at its human scaffold gate.

The scripts need `zsh`, which the packaging script declares.

**Follow-up to scaffold into `<project>/execution`.** The coordinator
reported this as a known follow-up. No repository record of it was found at
basis. The Root path already targets `<project>/execution`. The retained App
library and the Runtime API accept any root contained in the project. The
follow-up therefore belongs to whichever App-side scaffold entry is added
later (a DEL-06-03 application tool or a composed `ProjectScaffoldPort`),
under a separate amendment. S-c neither closes nor blocks it. Group 2 will
record it as a DEL-07-02 note.

### 17.6 Governance text touched by S-c

| Surface | Lines | Row |
|---|---|---|
| PRD §9.1 route table; compatibility line "Existing `/api/harness/*` route shapes remain stable" | L864; L868 | 35 |
| PRD Journey 7.3 (steps 2 and 4, acceptance kept); §7.1 step 4; §14 success metric 2 | L426-438; L391; L1651 | 36 (replaces the S-a handling of 7.3 in Row 14) |
| PRD route-preservation clauses §3.1 goal 25, §6.1, §6.4, §14 metric 20 | L161, L327, L381, L1669 | 40 |
| SPEC §17.1 route row; "Existing route shapes remain stable"; §17.9 exception | L1095; L1099; L1244-1249 | 37 |
| PLAN §1 baseline "Execution-root scaffolding"; R1 "Route shapes and SSE event names are unchanged" | L44; L185 | 38 |
| Decomposition hard constraint | L102 | 39 (extends Row 7) |
| DEL-03-03 decomposition row and SOW route index | D L324; SOW L181 | 34 |
| DEL-07-02 SOW | as §17.4 | 33 |
| NO_CHANGE: PRD FR-119, §8.13 and R2 (SDK MCP tools incl. scaffold; historical SDK path), §8.8 FR-045-FR-051 (no route), NFR-011; SPEC L376 and §14.2; CONTRACT K-HIER-1 "scaffold service" (library remains; choice E); TYPES §8.4 | — | — |

### 17.7 Supersession

Rows 33, 34, 35, 37, 39 and 40 supersede D-APP-74 L97-99 ("existing routes
… browser APIs … remain compatibility surfaces until separately retired") for
`POST /api/harness/scaffold`. Group 2 adds one `Supersession_Delta.csv` row
for this.

### 17.8 Code-change additions for the candidate (`dcd37f9ae`)

Beyond §9: carry out §17.2 items 1–3; keep `harness-scaffold.test.ts`; rerun
typecheck (the port scope map will flag any partial removal) and the full
tests. The candidate currently keeps the scaffold route (its receipt L143-144).
