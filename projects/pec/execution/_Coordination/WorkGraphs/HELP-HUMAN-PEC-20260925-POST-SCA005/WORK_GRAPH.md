# Work graph — PEC post-SCA-005 currency, reliance amendment and parser readiness

Saved at `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` under `projects/pec/loop/LOOP_INIT.md` (shared method, `D-PEC-94`). Method: `chirality-root:bundled:workflow:construct-local-work-graph` (`workflows/construct-local-work-graph/WORKFLOW.md`).

## Intent and selected route

- **Stable run identity:** `HELP-HUMAN-PEC-20260925-POST-SCA005`. The graph, the central receipt at `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/RECEIPT.md`, the affected `MEMORY.md` rows and the PRs all use this ID.
- **Steering basis:** the owner's direction of 2026-09-25, recorded verbatim in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md`: "You can continue with all the open work you identified.  Start with the loop migration, then use the loops for organizing the remaining work into a work graph to help plan and orchestrate the implementation.  You are now HELP_HUMAN in the Agent 0 role.  Read your instructions if you need a refresher and carry on." The loop migration landed as PR #917 (merge `13df8b795e47ab2284018eeefc9d5473d00c232d`). This graph organizes the rest. *Interpretation:* "all the open work" is the list in HELP_HUMAN's message after PR #915, together with the SCA-005 downstream table (`_ScopeChange/SCA-005_2026-09-23_2139/RUN_SUMMARY.md`) and the D-PEC-93 residuals.
- **Intended result:** PEC's derivative surfaces are current with decomposition revision 1.5 and PRD v2.3. The D-PEC-90 reliance direction is written into PEC's PRD and instructions. The parser deliverables, including the new DEL-02-08 and DEL-02-09, have current production contracts and the registry source they need, so P1 parser implementation can start from a clean basis.
- **Completion:** every node below is COMPLETE, or the owner has explicitly removed it. Each fenced write has been owner-ruled and merged. The closeout, receipt and MEMORY rows are done, and the final PR is merged.
- **Approach:**
  - First, mechanical currency that unblocks everything else: pointers, re-pinning, evidence quotes.
  - In parallel, the reliance scope change.
  - Then SOW currency, which is ordered after the reliance amendment for the deliverables that quote PEC-K-03 or §8.
  - Then the registry source packet and the derivative review, then fixtures.
  - Owner decisions are prepared as exact packets while unaffected work proceeds.
- **Left for later, not in this graph:**
  - P1 parser implementation itself (`v2/**` beyond the registry packet);
  - P2–P4;
  - CHECKING, ISSUED and acceptance acts, which are the owner's own;
  - retiring the `## Remaining` sections;
  - Root launcher alignment, which is Root-owned (notice only).
- **Route through the project DAG:**
  - Start from the accepted revision 1.5 decomposition and PRD v2.3 (`_Decomposition/_LATEST.md`, `docs/PRD.md`).
  - The currency packet (U1) is the prerequisite for SOW work, because SOW preparation reads the re-pinned contexts and refreshed evidence.
  - The reliance amendment (SCA-006) runs alongside it. Its checkpoint-1 impact assessment names the SOWs whose quoted PRD text it changes, and those SOWs wait for its application (S4).
  - The parser chain DEL-02-03 → DEL-02-08 and DEL-02-09, with the registry source DEL-01-06 (G1), leads to the P1 fixtures (X1).
  - Affected consumers outside PEC receive notices only: Root and App, under `D-PEC-90`.
- **Naming:** node IDs are local to this graph. "P1" to "P4" elsewhere in this file mean PEC's parser phases, never a node.
- **Open questions:** each node that writes fenced paths needs an owner ruling on an exact packet. These are listed per node, and none is pre-decided.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes | Nodes |
|---|---|---|---|
| Decomposition pointers, SCA-005 handoff, `_COORDINATION.md` | Revision 1.5 accepted. The pointers still carry the pre-setup audit reading; `_COORDINATION.md` names revision 1.4 | Present-current text | N1 |
| 42 `_CONTEXT.md`, 64 `_REFERENCES.md` | Pinned to revision 1.4 | Re-pin to revision 1.5 (B1) | N2 |
| 10 dependency registers (19 rows) | Stale EvidenceQuote text | Refreshed quotes (D-PEC-93 residual) | N3 |
| PRD v2.3 PEC-K-03, §8, §9, §12; `projects/pec/AGENTS.md`; response budgets | Verify-before-rely wording | Operational-reliance text and a direct-query-through-tool-calls access row, via the scope-change workflow (SCA-006) | R1–R4 |
| 23 SOW contracts, plus 5 housekeeping-only and first SOWs for DEL-02-08/09; DEL-04-02 if SCA-006 names it | SOWs at the revision-1.4 basis | Current with revision 1.5, PRD v2.3 and D-PEC-90 (B4) | S1–S4 |
| DEL-00-01 ADRs, DEL-00-03 SPEC (CHECKING) | Stale premises | Premise-only amendment (B5) | D1 |
| `v2/config/loops.json`, `loops.schema.json`, `RegisteredLoop` port | Strict version 1 | Schema v2 with feed profiles (B6) | G1 |
| DEL-02-03, DEL-02-08, DEL-02-09 fixture suites | None | P1 fixture classes (B7) | X1 |
| TM-PEC-023 | OPEN | `RESOLVED_BY_DECISION` (B8) | T1 |
| `projects/pec/AGENTS.md` residual staleness | "Implementation does not exist yet"; pre-v3 role names | Instruction corrections | I1 |

## Work

"Packet" means an owner-ruled D-PEC packet with exact paths, acts, verification and rollback, as `projects/pec/AGENTS.md` §Write Scopes And Fences requires for writes outside PEC's default surfaces. The owner named in each row does the work. HELP_HUMAN prepares every packet and brings it to the owner.

| ID / outcome | Deliverables and write scope (owner) | Needs / why | Completion check | State |
|---|---|---|---|---|
| N1 Records currency | Both `_LATEST.md` pointers; SCA-005 `Handoff_State.md`/`RUN_SUMMARY.md` outcome; `_COORDINATION.md` present-current lines (default-writable, may land first) (TASK under HELP_HUMAN) | Packet `D-PEC-95` for the fenced `_Decomposition/**` and `_ScopeChange/**` parts | Texts match the live audit and revision; validators unchanged; review | ACTIVE — `D-PEC-95` draft in preparation (read-only) |
| N2 Re-pin contexts and references to revision 1.5 | 42 `_CONTEXT.md`, 64 `_REFERENCES.md`, semantic fields untouched (TASK under HELP_HUMAN) | Packet `D-PEC-95`; generator re-prepared against the current tree | Strict registers 0/0; every file names revision 1.5; review | ACTIVE — in `D-PEC-95` |
| N3 Evidence-quote refresh | 19 rows in 10 `Dependencies.csv` (TASK under HELP_HUMAN) | Packet `D-PEC-95`; exact new quotes verbatim in the cited files | Every ACTIVE EvidenceQuote verbatim; strict 0/0; closure unchanged | ACTIVE — in `D-PEC-95` |
| U1 Currency PR | N1–N3 (HELP_HUMAN) | Owner ruling on `D-PEC-95` | PR merged after review and CI | PLANNED |
| R1 SCA-006 checkpoint 1: reliance amendment intake and impact | Snapshot folder `_ScopeChange/SCA-006_<date>/` only. It assesses PRD PEC-K-03, §8 (agents, access classes, direct query through tool calls), §9 reliance envelope and §12 release gate; response-size budgets; the `projects/pec/AGENTS.md` K-02 gloss; and the explicit list of affected SOWs and ADR/SPEC rows (WORKING_ITEMS, `scope-change`) | `D-PEC-90` R-A; `chirality-root:bundled:workflow:scope-change` | Owner accepts checkpoint 1 | ACTIVE — package in preparation |
| R2 SCA-006 checkpoint 2: exact amendment and propagation | PRD v2.4 candidate; the affected SOW and ADR/SPEC set fixed as exact rows (WORKING_ITEMS) | R1 accepted | Owner accepts checkpoint 2, which fixes the S4 set | PLANNED |
| R3 SCA-006 checkpoint 3: apply and audit | Lane A writes per the accepted plan (WORKING_ITEMS) | R2 accepted | Owner accepts checkpoint 3 | PLANNED |
| R4 Reliance notices | Root and App notices, per the `D-PEC-90` grant. A Runtime notice only if the checkpoint-2 plan names one (HELP_HUMAN) | R3 | Notices merged | PLANNED |
| S1 SOW currency: review class outside the S4 set | Review-class SOWs from SCA-005 §B4 that SCA-006 does not name as affected, plus the 5 housekeeping-only (pins, false revision-1.1 claims) (WORKING_ITEMS with REVIEW or artifact gates) | U1; the R1 affected-SOW list, which removes its members from S1; packet per batch | Each SOW validator-clean and reviewed | PLANNED |
| S2 SOW currency: rebuild class outside the S4 set | DEL-01-01, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07; DEL-01-06 after G1 (WORKING_ITEMS) | U1; packet(s); parser carry-forward (CON-001 cases for RETIRED, node states, run tokens). A member that R1 names as affected moves to S4 | Same | PLANNED |
| S3 First SOWs for DEL-02-08 and DEL-02-09 | Their `ScopeOfWork.md`, via preparation → Scope of Work (WORKING_ITEMS) | U1; packet; S2 context for parsers | Same | PLANNED |
| S4 SOWs whose quoted PRD text SCA-006 changes | The set that checkpoint 2 fixes. Candidates from a grep of head `5570fd095`: quoting PEC-K-03 or verify-before-rely, DEL-04-01, DEL-04-02, DEL-08-01 and DEL-08-03; citing PRD §8, DEL-01-01, DEL-01-05, DEL-02-03, DEL-04-02, DEL-04-03, DEL-08-01 and DEL-08-04. DEL-04-02 is `current` under SCA-005 §B4 but is included because of CLM-016 (WORKING_ITEMS) | R3; packet, or the accepted checkpoint-2 propagation plan where it binds exact rows | Same | PLANNED |
| G1 Registry source packet | `v2/config/loops.json`, `loops.schema.json`, `RegisteredLoop` port and tests (WORKING_ITEMS) | Packet (F-PEC-1); VER-001/VER-003 rerun | v2 checks pass; review | PLANNED |
| D1 Derivative premise review | DEL-00-01 ADRs, DEL-00-03 SPEC (WORKING_ITEMS with owning workflows) | Packet binding exact bytes (outside default surfaces); after R3 for K-03 text | Owner rules the packet; premise-only amendments merged | PLANNED |
| X1 P1 fixture suites | DEL-02-03, DEL-02-08, DEL-02-09 fixture classes (receipt present, evidence-only, no AgentRuns record) (WORKING_ITEMS) | S2, S3; v2 packet (SCA-005 Propagation_Plan §B7) | Fixtures committed under the ruled packet | PLANNED |
| T1 TM-PEC-023 disposition | Task Management register row (WORKING_ITEMS, `task-management`) | Owner basis: checkpoint-2 acceptance of SCA-005 Propagation_Plan §B8 ("TM-PEC-023 closure `RESOLVED_BY_DECISION` citing SCA-005", after checkpoint 3). `D-PEC-95` checks whether that is the human's actual disposition that `task-management` requires, or whether the owner disposes of the row directly | Row closed on a cited owner disposition | UNCERTAIN — basis under check in `D-PEC-95` |
| I1 `AGENTS.md` residual corrections | `projects/pec/AGENTS.md` (HELPS_HUMANS) | Instruction tranche with manifest | Validators pass; notice | PLANNED — may ride R3's instruction change |
| C1 Bounded closeout | Affected deliverables and records (HELP_HUMAN) | All substantive PRs merged | `bounded-reconciliation` comparisons; warranted edits | PLANNED |
| M1 Record the run | Central `RECEIPT.md`; MEMORY rows named by the governing packets (HELP_HUMAN) | C1 | Receipt and rows written | PLANNED |
| F1 Final PR | Integrated undertaking (HELP_HUMAN) | M1 and all checks | Final PR merged | PLANNED |

**Order.**
- Active now: R1, and the `D-PEC-95` preparation for N1–N3 and T1.
- After U1 and R1: S1, S2 and S3. Their membership excludes the R1 affected set.
- After G1: DEL-01-06 in S2.
- After R3: S4, D1 and I1.
- After S2 and S3: X1.
- Then C1 → M1 → F1.

The dependencies are acyclic, and the named inputs, not this listing, decide when a node is ready.

## Current state and recovery

- **Checked basis:** `origin/main` `13df8b795` (PR #917 merged; PEC runs the shared loop under `D-PEC-94`).
- **Next work:**
  - Complete the `D-PEC-95` draft (N1–N3, T1) and the SCA-006 checkpoint-1 package (R1), then bring each to the owner.
  - Each fenced packet comes to the owner to rule on.
- **Local or unmerged work:** this graph's first PR (#919, branch `claude/pec-post-sca005-graph`).
- **Active operations and ownership:**
  - `D-PEC-95` draft: TASK under HELP_HUMAN, read-only, writing a HELP_HUMAN scratch folder. HELP_HUMAN publishes it.
  - SCA-006 checkpoint-1 package: WORKING_ITEMS, branch `claude/pec-sca006-cp1-package`. Returns go under `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`.
- **Graph maintainer:** HELP_HUMAN.
- **Earlier run:** `HELP-HUMAN-PEC-20260923-SCA005`, under PEC's former loop; its `RUN.md` is history. The owner's CHECKING reservation for DEL-01-03 stands, and nothing here prompts for it.

| Completed work / node | What changed and was checked | Unresolved consequence |
|---|---|---|
| Graph PR #919, review 01 | Review 01 blocked on SOW sequencing. Repaired: S4 is gated on the SCA-006 affected set, DEL-04-02/08-01/08-03 are added as candidates, and DEL-01-06 is relabelled as waiting on G1. Seven non-blocking findings also repaired. Transcription: `returns/REVIEW_PR919_01.md` | Re-review of the repair head |

## Owner-direction evidence and D-PEC-88 trace

- 2026-09-25, owner, verbatim: "re: D-PEC-88 confirmed yes it carries over". This confirms the carry-over that `D-PEC-94` recorded as HELP_HUMAN's interpretation. The record of this act is the owner-confirmation section added to `D-PEC-94` in this graph's first PR.
- STATUS/README changes made under `D-PEC-88` in this undertaking are listed here and carried into the central receipt at closeout:
  - First PR: `docs/STATUS.md` now points the open-work paragraph at this graph.
  - First PR, review repair: the `docs/STATUS.md` SCA-005 paragraph heading no longer calls SCA-005 active.
