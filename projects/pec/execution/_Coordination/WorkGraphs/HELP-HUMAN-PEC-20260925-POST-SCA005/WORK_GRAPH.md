# Work graph — PEC post-SCA-005 currency, reliance amendment and parser readiness

Saved at `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` under `projects/pec/loop/LOOP_INIT.md` (shared method, `D-PEC-94`). Method: `chirality-root:bundled:workflow:construct-local-work-graph` (`workflows/construct-local-work-graph/WORKFLOW.md`).

## Intent and selected route

- **Stable run identity:** `HELP-HUMAN-PEC-20260925-POST-SCA005`. The graph, the central receipt at `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/RECEIPT.md`, the affected `MEMORY.md` rows and the PRs all use this ID.
- **Steering basis:** the owner's direction of 2026-09-25, recorded verbatim in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md`: "You can continue with all the open work you identified. Start with the loop migration, then use the loops for organizing the remaining work into a work graph to help plan and orchestrate the implementation." The loop migration landed as PR #917 (merge `13df8b795e47ab2284018eeefc9d5473d00c232d`). This graph organizes the rest. *Interpretation:* "all the open work" is the list in HELP_HUMAN's message after PR #915, together with the SCA-005 downstream table (`_ScopeChange/SCA-005_2026-09-23_2139/RUN_SUMMARY.md`) and the D-PEC-93 residuals.
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
- **Open questions:** each node that writes fenced paths needs an owner ruling on an exact packet. These are listed per node, and none is pre-decided.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes | Nodes |
|---|---|---|---|
| Decomposition pointers, SCA-005 handoff, `_COORDINATION.md` | Revision 1.5 accepted. The pointers still carry the pre-setup audit reading; `_COORDINATION.md` names revision 1.4 | Present-current text | N1 |
| 42 `_CONTEXT.md`, 64 `_REFERENCES.md` | Pinned to revision 1.4 | Re-pin to revision 1.5 (B1) | N2 |
| 10 dependency registers (19 rows) | Stale EvidenceQuote text | Refreshed quotes (D-PEC-93 residual) | N3 |
| PRD v2.3 PEC-K-03, §8, §9, §12; `projects/pec/AGENTS.md`; response budgets | Verify-before-rely wording | Operational-reliance text and a direct-query-through-tool-calls access row, via the scope-change workflow (SCA-006) | R1–R4 |
| 23 SOW contracts, plus 5 housekeeping-only and first SOWs for DEL-02-08/09 | SOWs at the revision-1.4 basis | Current with revision 1.5, PRD v2.3 and D-PEC-90 (B4) | S1–S4 |
| DEL-00-01 ADRs, DEL-00-03 SPEC (CHECKING) | Stale premises | Premise-only amendment (B5) | D1 |
| `v2/config/loops.json`, `loops.schema.json`, `RegisteredLoop` port | Strict version 1 | Schema v2 with feed profiles (B6) | G1 |
| DEL-02-03, DEL-02-08, DEL-02-09 fixture suites | None | P1 fixture classes (B7) | X1 |
| TM-PEC-023 | OPEN | `RESOLVED_BY_DECISION` (B8) | T1 |
| `projects/pec/AGENTS.md` residual staleness | "Implementation does not exist yet"; pre-v3 role names | Instruction corrections | I1 |

## Work

| ID / outcome | Deliverables and write scope | Needs / why | Completion check | State |
|---|---|---|---|---|
| N1 Records currency packet | Both `_LATEST.md` pointers; SCA-005 `Handoff_State.md`/`RUN_SUMMARY.md` outcome; `_COORDINATION.md` present-current lines (default-writable, may land first) | D-PEC packet ruled for the fenced `_Decomposition/**` and `_ScopeChange/**` parts | Texts match live audit and revision; validators unchanged; review | PLANNED — packet to prepare with N2/N3 as one currency packet |
| N2 Re-pin contexts and references to revision 1.5 | 42 `_CONTEXT.md`, 64 `_REFERENCES.md` (semantic fields untouched) | Same packet; generator re-prepared against the current tree | Strict registers 0/0; every file names revision 1.5; review | PLANNED |
| N3 Evidence-quote refresh | 19 rows in 10 `Dependencies.csv` | Same packet; exact new quotes verbatim in cited files | Every ACTIVE EvidenceQuote verbatim; strict 0/0; closure unchanged | PLANNED |
| P1 Currency PR | N1–N3 | Owner ruling on the currency packet | PR merged after review and CI | PLANNED |
| R1 SCA-006 checkpoint 1 — reliance amendment intake and impact | PRD PEC-K-03, §8 (agents, access classes, direct query through tool calls), §9 reliance envelope, §12 release gate; response-size budgets; `projects/pec/AGENTS.md` K-02 gloss; DEL-04-01 and DEL-00-03 quotations | `D-PEC-90` R-A; scope-change workflow | Owner accepts checkpoint 1 | PLANNED — ready now |
| R2 SCA-006 checkpoint 2 — exact amendment and propagation | PRD v2.4 candidate; affected SOW and ADR rows | R1 accepted | Owner accepts checkpoint 2 | PLANNED |
| R3 SCA-006 checkpoint 3 — apply and audit | Lane A writes per the accepted plan | R2 accepted | Owner accepts checkpoint 3 | PLANNED |
| R4 Reliance notices | Root, App, Runtime notices (consumer-owned use) | R3 | Notices merged | PLANNED |
| S1 SOW currency — review class, not K-03-bound | 15 review-class SOWs minus DEL-04-01-dependent ones, plus 5 housekeeping-only (pins, false rev-1.1 claims) | Owner-ruled packet per batch; WORKING_ITEMS with REVIEW or artifact gates | Each SOW validator-clean and reviewed | PLANNED — ready after P1 |
| S2 SOW currency — rebuild class | DEL-01-01, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07 (DEL-01-06 waits for G1; DEL-04-01 waits for R3) | Packet(s); parser carry-forward (CON-001 cases for RETIRED, node states, run tokens) | Same | PLANNED |
| S3 First SOWs for DEL-02-08 and DEL-02-09 | Their `ScopeOfWork.md` via preparation → Scope of Work | Packet; S2 context for parsers | Same | PLANNED |
| S4 K-03-bound SOWs | DEL-04-01, DEL-08-04, DEL-01-06 | R3 (and G1 for DEL-01-06) | Same | PLANNED |
| G1 Registry source packet | `v2/config/loops.json`, `loops.schema.json`, `RegisteredLoop` port and tests | Owner-ruled D-PEC packet (F-PEC-1); VER-001/VER-003 rerun | v2 checks pass; review | PLANNED |
| D1 Derivative premise review | DEL-00-01 ADRs, DEL-00-03 SPEC | Owning workflows plus exact-byte gates; after R3 for K-03 text | Premise-only amendments accepted by the owner | PLANNED |
| X1 P1 fixture suites | DEL-02-03, DEL-02-08, DEL-02-09 fixture classes (receipt present, evidence-only, no AgentRuns record) | S2, S3 | Fixtures committed under their SOWs | PLANNED |
| T1 TM-PEC-023 disposition | Task Management register | SCA-005 closed | Row `RESOLVED_BY_DECISION` via task-management | PLANNED — ready now |
| I1 AGENTS.md residual corrections | `projects/pec/AGENTS.md` | Instruction tranche | Validators pass; notice | PLANNED — may ride R3's instruction change |
| C1 Bounded closeout | Affected deliverables and records | All substantive PRs merged | `bounded-reconciliation` comparisons; warranted edits | PLANNED |
| M1 Record the run | Central `RECEIPT.md`; MEMORY rows named by the governing packets | C1 | Receipt and rows written | PLANNED |
| F1 Final PR | Integrated undertaking | M1 and all checks | Final PR merged | PLANNED |

**Order.**
- Ready now: T1 and R1. P1 starts with packet preparation now.
- After P1: S1, S2 and S3.
- After G1: DEL-01-06 in S4.
- After R3: S4, D1 and I1.
- After S2 and S3: X1.
- Then C1 → M1 → F1.

The dependencies are acyclic, and the named inputs, not this listing, decide when a node is ready.

## Current state and recovery

- **Checked basis:** `origin/main` `13df8b795` (PR #917 merged; PEC runs the shared loop under `D-PEC-94`).
- **Next work:**
  - Prepare the currency packet (N1–N3) and the SCA-006 checkpoint-1 package (R1).
  - Run T1.
  - Each fenced packet comes to the owner to rule on.
- **Local or unmerged work:** this graph's first PR (branch `claude/pec-post-sca005-graph`).
- **Graph maintainer:** HELP_HUMAN.
- **Earlier run:** `HELP-HUMAN-PEC-20260923-SCA005`, under PEC's former loop; its `RUN.md` is history. The owner's CHECKING reservation for DEL-01-03 stands, and nothing here prompts for it.

## Owner-direction evidence and D-PEC-88 trace

- 2026-09-25, owner, verbatim: "re: D-PEC-88 confirmed yes it carries over". This confirms the carry-over that `D-PEC-94` recorded as HELP_HUMAN's interpretation. The record of this act is the owner-confirmation section added to `D-PEC-94` in this graph's first PR.
- STATUS/README changes made under `D-PEC-88` in this undertaking are listed here and carried into the central receipt at closeout:
  - First PR: `docs/STATUS.md` now points the open-work paragraph at this graph.
