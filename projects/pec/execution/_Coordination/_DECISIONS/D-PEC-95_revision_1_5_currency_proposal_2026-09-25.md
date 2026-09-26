# D-PEC-95 — Revision-1.5 currency packet: records currency (N1), context and reference re-pin (N2), evidence-quote refresh (N3), and the TM-PEC-023 disposition (T1) — proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by a TASK (Type 2) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph nodes N1–N3 and T1) for the PEC loop, 2026-09-25 (session date), from brief `H9_D95_CURRENCY_PROPOSAL.md` (SHA-256 `02fb7370e835a165a3c36f4f044447b598828050c6e2a069a66f0fa8a84945a1`). No earlier direction approves this file. It performs no production act: no tracked file was edited, and every prototype ran on scratch copies only. It asks for no lifecycle change. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `13df8b795` the register has no D-PEC-95 row and no file under `projects/pec` carries the number; the work graph on branch `claude/pec-post-sca005-graph` (PR #919) names it for this packet, and this packet uses the number its brief assigned. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md`.

## Provenance

- **Owner acts relied on.**
  - SCA-005 checkpoint 1, amendment 1 (2026-09-24), the TM-PEC-023 selections: "Besides that, I reviewed and accept your  read for each mapping." (`_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/DECISION.md`, `4328633c…8f3013`; the double space is in the record).
  - Checkpoint 2 (2026-09-25): "CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred." (`…/SCA-005_GROUP-2_2026-09-25/DECISION.md`, `ca88f6a8…3d66`; register row `D-PEC-92`). It accepted `Propagation_Plan.md` (`50cd0b1d…1350`), whose §B1 plans the re-pin and §B8 names "TM-PEC-023 closure `RESOLVED_BY_DECISION` citing SCA-005" for task-management "after checkpoint 3".
  - Checkpoint 3 (2026-09-25): "CP3: accept; Q1 a" (`…/SCA-005_GROUP-3_2026-09-25/DECISION.md`, `35c211a6…f673`). Revision 1.5 became `current_basis`, closure `CLOSED_FOR_SCOPE_CHANGE_ONLY`, with B1 and B8 recorded open and separately gated.
  - `D-PEC-93: A.` (`D-PEC-93_RULING_2026-09-25.md`, `ffb0b582…3709`). Its question 4 carried the 19 stale quotes "as a recorded residual"; B1 was not selected.
  - The owner's 2026-09-25 steering, recorded in `D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`eb9793aa…5e81`): "You can continue with all the open work you identified." The brief reports that HELP_HUMAN's work graph turns this into nodes N1–N3 and T1; this TASK read that graph at branch commit `87f6bfe30` (`WORK_GRAPH.md` `f669ebe5…0f78`), not on `origin/main`.
- **Fence.** `projects/pec/AGENTS.md` (`c9d3b44d…197a` at `13df8b795`) §"Write Scopes And Fences": only `execution/_Coordination/**`, `AGENTS.md` and the one-time STATUS pointer are default-writable. Every other write under `projects/pec` needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. `F-PEC-1` (`D-T0-15`, `95c245b5…0b09`) is the outer fence and is opened only by such a per-tranche clause. No earlier ruling opens the paths below. D-PEC-92 opened Lane A for checkpoint-3 preparation and acceptance: the decomposition and registers, the PRD, 22 `_CONTEXT.md` mirrors, four `_STATUS.md` retirements, the SCA-005 snapshot folder for A5 and the two pointers for A6. It opened no Lane B path and no later edit, and checkpoint 3 authorized none. D-PEC-93 opened only its own 31 paths and the audit pointer.
- **Intent of record.** SCA-005 `Propagation_Plan.md` §B1 ("Re-pin to revision 1.5 the provenance of the … `_CONTEXT.md` files not written in A2 and all 64 existing `_REFERENCES.md` (semantic fields unchanged)") and §B8. The D-PEC-93 run root `HANDOFF_STATE.md` (`0887a9c9…4a06`) lists residuals 1–3: quote currency, B1, and stale descriptions outside its grant. The post-setup re-audit `COV_SCA005_POSTSETUP_2026-09-25_1606` (issue log `3e93aaf3…5850`) records them as COV-068/069 (42 contexts and 64 references at revision 1.4), COV-072 (19 non-verbatim quotes) and COV-073 (stale handoff surfaces), all INFO.
- **Precedents.** D-PEC-93 (format, bound generator, slot rule, revert-PR rollback) and its prepared-but-unselected `gen_d93_b1.py` (`eff5d2fb…677c`). This packet re-derives that generator against the current tree and does not reuse its bytes. Also: the SCA-004 re-pin (PROJECT_SETUP, 64/64); the SCA-004 WORKING_ITEMS currency sweep, which appended supersession notes to mutable handoffs and recorded pointers for immutable ones in `_COORDINATION.md`; and D-PEC-93's `DEP-03-01-007` refresh (`LastSeen` = act date; `Notes` prefixed "Evidence refreshed under …").
- **Source state.** Every hash below was read at `origin/main` `13df8b795e47ab2284018eeefc9d5473d00c232d` (PR #917), from a `git archive` export. The checkout (branch `claude/pec-post-sca005-graph`) was not changed. Commits on that branch after `13df8b795` touch none of the 121 target paths (checked with `git diff --name-only 13df8b795 87f6bfe30`).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`, the same bytes on the checkout's HEAD) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`) was run from `projects/pec` with `--operation exact-correction-preparation` on all 123 targets: the 121 product paths of option A and both Task Management registers. Every run returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0.

## What preparation found

### Fence status of each surface

| Surface | Paths | Fenced? | Grant needed |
|---|---|---|---|
| `_Decomposition/_LATEST.md` | 1 | yes (`execution/_Decomposition/**`) | this packet |
| `_ScopeChange/_LATEST.md` | 1 | yes (`execution/_ScopeChange/**`) | this packet |
| SCA-005 `Handoff_State.md`, `RUN_SUMMARY.md` | 2 | yes (`execution/_ScopeChange/**`) | this packet (option A only) |
| `_Coordination/_COORDINATION.md` | 1 | **no**: default-writable under `execution/_Coordination/**` | none. It is included so that one reviewed act carries all the currency text. Its last edit sits in the section headed "Notes (human-owned)" (question 4) |
| 42 `_CONTEXT.md`, 64 `_REFERENCES.md` | 106 | yes (deliverable folders) | this packet |
| 10 `Dependencies.csv` | 10 | yes (deliverable folders) | this packet |
| Task Management `REGISTER.csv` / `REGISTER_CLOSED.csv` (T1) | 2 | **no**: default-writable | none from this packet. Only a recorded human disposition, applied by WORKING_ITEMS under `task-management` (see T1) |

D-PEC-93 finding 5 called `_COORDINATION.md` "HELP_HUMAN's D-PEC-88 surface". D-PEC-88 (`266a1411…fef5`) covers only `docs/STATUS.md` and `README.md`. `_COORDINATION.md` needs no packet. `docs/STATUS.md` and `README.md` are not in this packet; HELP_HUMAN updates them under D-PEC-88 after the act and names the change in the graph.

### N1 — what is stale, and what replaces it

Observed at `13df8b795`:

- `_Decomposition/_LATEST.md` lines 33–52 give the checkpoint-3 audit (`BLOCKERS` 2/6/74) as current, say the audit pointer "still names the SCA-004 audit", and list A4, the re-audit and the pointer move as open. All three were done under D-PEC-93: PR #914, merge `961ee1054210fbae7ef5b403547e7a397fb18c95`. The re-audit reads `WARNINGS` 0/3/70, and `_Evaluation/DecompCoverage/_LATEST.md` (`2b43dc3b…1450`) names `COV_SCA005_POSTSETUP_2026-09-25_1606`. The same block lists the `projects/pec/AGENTS.md` instruction tranche (plan §B8: L28, L170 and Shared Runtime Boundary) as open. At `13df8b795`, `projects/pec/AGENTS.md` names PRD v2.3 and the D-GOV-43 A2 Runtime boundary, through the D-PEC-94 adoption in PR #917.
- `_ScopeChange/_LATEST.md` rows `DerivativePackageState`, `DownstreamRerunState` (`FROZEN`), `MetadataAlignmentState` and `AuditState` (`BLOCKED`), and its "Downstream boundary" paragraph, describe the same pre-D-PEC-93 state.
- SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` end at the checkpoint-3 acceptance. Both are accumulating records: the group-3 `ACCEPTED_MANIFEST.csv` lists `Handoff_State.md` as "Context; updated additively by this act". The checkpoint-3 amendment says the audit pointer and re-audit are open.
- `_COORDINATION.md` lines 15–21 give revision 1.4 as the accepted upstream basis. Lines 182–184, in "Notes (human-owned)", say "revision 1.4 is `current_basis` since SCA-004, with topology and execution-dependency bytes preserved". B3 changed the execution rows. Dated items 12 and 13 use present tense for revision 1.4 and for TM-PEC-023 "held" for a mapping session. They are dated history, so the packet labels them superseded without editing them.

Acts (exact bytes in the generator; rendered at `{D}` = 2026-09-25 in `optionA_vs_13df8b795.diff`):

1. **`_Decomposition/_LATEST.md`.** One replacement of the "Audit", "Scope-change snapshot" and "Derivative state" bullets. The new text:
   - names the post-setup audit and its reading;
   - says its INFO findings COV-068/069/072/073 were addressed on `{D}` under D-PEC-95 without a further audit;
   - sets `DownstreamRerunState = IN_PROGRESS` and `MetadataAlignmentState = COMPLETE`;
   - lists what is done (D-PEC-93, D-PEC-95, and AGENTS.md under D-PEC-94) and what is open (SOW currency, derivative review, registry source packet, fixtures, D-PEC-90 amendment);
   - says TM-PEC-023's state is in the Task Management register;
   - points to the undertaking's work graph.

   The authority-fence bullet and every line above the audit bullet are unchanged.
2. **`_ScopeChange/_LATEST.md`.** Four table rows and the "Downstream boundary" paragraph are replaced:
   - `DerivativePackageState`: `INCOMPLETE` (A4, B3, B1 done; B4–B7 and the D-PEC-90 amendment open);
   - `DownstreamRerunState`: `IN_PROGRESS`;
   - `MetadataAlignmentState`: `COMPLETE`;
   - `AuditState`: `WARNINGS`.

   The Status, CurrentGate, AcceptedBasis, Authority and ClosureVerdict rows are unchanged.
3. **SCA-005 `Handoff_State.md` (option A only).** One paragraph is appended: "Amendment {D} (post-closure outcome note, `D-PEC-95`; append-only)". It records the D-PEC-93 outcome, the re-audit and pointer, the D-PEC-95 re-pin and quote refresh, the AGENTS.md state and the state fields now, and gives the new hash of `RUN_SUMMARY.md`. Nothing above it changes. The earlier hash tables stay as they are, including the C5 table's checkpoint-3-preparation hashes of `RUN_SUMMARY.md` and `Decision_Log.md` (a historical table; not repaired).
4. **SCA-005 `RUN_SUMMARY.md` (option A only).** One section is appended: "Post-closure outcome ({D}, `D-PEC-95`; append-only)". It holds a nine-row table of the downstream items with their state and record, and the state fields. It says its audit IDs are those of the post-setup audit, because `COV-072` in this file's earlier sections means the checkpoint-3 audit's plan-count defect, a different finding.
5. **`_COORDINATION.md`.** Three edits:
   - the accepted-basis bullet now names revision 1.5 (D-PEC-92, checkpoint 3) and adds revision 1.4 to the historical list;
   - a new dated item 14, "SCA-005 feed-model rebaseline and downstream currency", states the current basis, the TM-PEC-023 selections applied, the D-PEC-93 topology (66 registers, 263 rows, strict 0/0, 111 edges, 0 SCCs) and the D-PEC-95 re-pin and refresh, and says it supersedes the present-tense statements of items 12 and 13. Under option P it instead records the two SCA-005 files' hashes as superseded pointers, which is the SCA-004 practice for immutable handoffs;
   - the human-owned Notes line now reads "revision 1.5 is `current_basis` since SCA-005, whose dependency rerun under `D-PEC-93` retired, refreshed and added register rows".

### N2 — the re-pin population and form

The generator globs all 66 deliverable folders at the act. It requires the following, and stops if any fails:

- the `_CONTEXT.md` files carrying the tail "then by revision 1.4 (`current_basis`, SCA-004 successor)." are exactly the pinned 42;
- the other 24 already name revision 1.5: the 22 A2 mirrors, plus DEL-02-08 and DEL-02-09, whose D-PEC-93 provenance wraps the phrase across a line;
- no context has both forms or neither;
- the `_REFERENCES.md` files naming revision 1.4 are exactly the pinned 64, with DEL-02-08 and DEL-02-09 already at 1.5;
- each anchor occurs exactly once.

The acts:

- **Context (42):** ``then by revision 1.4 (`current_basis`, SCA-004 successor).⏎`` → ``then by revision 1.4 (`current_basis`, SCA-004 successor),⏎then by revision 1.5 (`current_basis`, SCA-005 successor).⏎``. This is the exact form the 22 A2 mirrors already carry. After the act, all 64 pre-existing contexts have one identical provenance block (checked).
- **Reference (64):** two bullet replacements: ``(revision 1.4, accepted `current_basis`; SCA-004 successor)`` → ``(revision 1.5, accepted `current_basis`; SCA-005 successor)``, and `` `docs/PRD.md` v2.2 `` → `` `docs/PRD.md` v2.3 ``.

No other byte changes. The field tables, descriptions, "covers" lists (unless add-on R is chosen), closing lines and every `_SEMANTIC.md`, `_DEPENDENCIES.md` and `_STATUS.md` stay untouched.

The 106 files lie in 64 deliverable folders: 28 `OPEN`, 26 `INITIALIZED`, 4 `CHECKING` (DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01), 2 `IN_PROGRESS` (DEL-01-03, DEL-01-05) and 4 `RETIRED`. The 42 contexts are 20 `OPEN`, 16 `INITIALIZED`, 4 `CHECKING` and 2 `IN_PROGRESS`; the retired deliverables' contexts are A2 mirrors. The re-pin changes deliverable metadata, not the artifacts under CHECKING or IN_PROGRESS, and changes no lifecycle state. The SCA-004 re-pin (64/64) is the precedent. The owner's CHECKING reservation for DEL-01-03 is untouched, and nothing here prompts about CHECKING.

Paths: every one is in the grant table below. The context path list hashes `55f28c89…b648` and the reference path list `a3500747…d6ea`.

### N3 — the 19 quotes, before and after

Rules applied to every row:

- **Identity.** `DependencyID`, row order and every other cell are unchanged. `EvidenceFile` and `SourceRef` are unchanged, so each new quote comes from the same cited locus: the named `Deliverables.csv` or `ScopeLedger.csv` cell, or the PRD requirement row. The generator asserts each new quote is a substring of that locus, not merely of the file.
- **`LastSeen`.** Set to the act date `{D}`; all 19 are `2026-07-25` today. This follows D-PEC-93's `DEP-03-01-007` refresh: the evidence was re-observed on that date. `FirstSeen` is unchanged.
- **`Notes`.** Prefixed with `Evidence refreshed under D-PEC-95 (<cause>); `, keeping the old Notes, including `EdgeID`, verbatim after it. The cause names the change that made the quote stale:
  - an SCA-005 action ID (`Amendment_Actions_CP2.csv`, `7bb3bada…9987`), for the 16 made stale by SCA-005;
  - for the 3 that were already stale at revision 1.4: PRD v2.2 / D-PEC-68 (commit `f22cfcc76`) and SCA-003 revision 1.3 (commit `42e291db1`).
- **Serialization.** CSV rows keep the corpus convention (`csv.writer`, `QUOTE_MINIMAL`, CRLF). Every untouched row round-trips byte for byte.

The quotes below are shown as written; any backticks belong to the quoted text. The exact bytes are in `gen_d95.py` (`QUOTES`) and `optionA_vs_13df8b795.diff`.

| Row → target (edge) | Locus (unchanged `EvidenceFile` — `SourceRef`) | Before (`EvidenceQuote`) | After (`EvidenceQuote`) | `Notes` prefix |
|---|---|---|---|---|
| `DEP-03-01-005` → DEL-01-01 (E-P10) | `Deliverables.csv` — Deliverables.csv row DEL-01-01 ContextEnvelopeNotes | 14 entity types and the schema every derivation package depends on | 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on | `Evidence refreshed under D-PEC-95 (SCA-005 A-12: DEL-01-01 envelope notes name 16 entity types);` |
| `DEP-03-01-008` → DEL-02-01 (E-P19) | `PRD.md` — PRD.md §9.2 requirement PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect) | at minimum: `_STATUS.md` (declared parser dialect) | `Evidence refreshed under D-PEC-95 (SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording);` |
| `DEP-03-01-009` → DEL-02-02 (E-P20) | `PRD.md` — PRD.md §9.2 requirement PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets | decision registers and packets (row identity and status only) | `Evidence refreshed under D-PEC-95 (SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording);` |
| `DEP-03-01-010` → DEL-02-03 (E-P21) | `PRD.md` — PRD.md §9.2 requirement PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it) | receipts — `LOOP_RECEIPTS.md` ledgers (per-loop grammar; the `receipt-contract-v2` marker where a ledger carries it; live or declared historical per profile) and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` | `Evidence refreshed under D-PEC-95 (SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording);` |
| `DEP-03-01-011` → DEL-02-04 (E-P22) | `PRD.md` — PRD.md §9.2 requirement PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json` | `STATUS.json` / `RUNTIME_SUMMARY.json` as declared historical grammar or current evidence per profile | `Evidence refreshed under D-PEC-95 (SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording);` |
| `DEP-03-01-012` → DEL-02-05 (E-P23) | `PRD.md` — PRD.md §9.2 requirement PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers | dependency registers (`Dependencies.csv`; `WORK_GRAPH.json` as declared historical grammar) | `Evidence refreshed under D-PEC-95 (SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording);` |
| `DEP-03-01-013` → DEL-02-06 (E-P24) | `PRD.md` — PRD.md §9.2 requirement PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT | `LOOP_INIT.md` loop identity, entrypoint and procedure SHA only (workplans as declared historical grammar) | `Evidence refreshed under D-PEC-95 (SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording);` |
| `DEP-05-01-004` → DEL-01-01 (E-P12) | `Deliverables.csv` — Deliverables.csv row DEL-01-01 (ContextEnvelopeNotes) | 14 entity types and the schema every derivation package depends on | 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on | `Evidence refreshed under D-PEC-95 (SCA-005 A-12: DEL-01-01 envelope notes name 16 entity types);` |
| `DEP-05-02-003` → DEL-01-01 (E-P13) | `Deliverables.csv` — Deliverables.csv row DEL-01-01 (ContextEnvelopeNotes) | 14 entity types and the schema every derivation package depends on | 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on | `Evidence refreshed under D-PEC-95 (SCA-005 A-12: DEL-01-01 envelope notes name 16 entity types);` |
| `DEP-06-03-003` → DEL-06-01 (E-P41) | `Deliverables.csv` — Deliverables.csv row DEL-06-01 (Description) | Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes); identity/lifecycle stay daemon-owned. | Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes), arriving only from an explicitly authorized hooks consumer; identity/lifecycle are Runtime-owned per application (C13). | `Evidence refreshed under D-PEC-95 (SCA-005 A-37: DEL-06-01 description re-expressed);` |
| `DEP-08-04-005` → DEL-04-01 (E-P51) | `PRD.md` — PRD.md §9.6 requirement PEC-API-002 | Orientation reads shall complete in ≤100 ms at p95 against the current corpus (session-start critical path). | Orientation reads shall complete in ≤100 ms at p95 against the current corpus (latency-sensitive pull path; any session-start use requires a separately adopted consumer duty). | `Evidence refreshed under D-PEC-95 (PRD v2.2 PEC-API-002 wording, D-PEC-68; stale before SCA-005);` |
| `DEP-08-05-004` → DEL-06-01 (E-P57) | `Deliverables.csv` — Deliverables.csv row DEL-06-01 Description | Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes); identity/lifecycle stay daemon-owned. | Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes), arriving only from an explicitly authorized hooks consumer; identity/lifecycle are Runtime-owned per application (C13). | `Evidence refreshed under D-PEC-95 (SCA-005 A-37: DEL-06-01 description re-expressed);` |
| `DEP-09-05-006` → DEL-06-03 (E-P64) | `Deliverables.csv` — Deliverables.csv row DEL-09-05 | Sessions x worktrees x live hierarchy with heartbeat age and advisory overlap warnings. | Sessions (when hook-reported) x worktrees x graph-declared activity with heartbeat/scan age and advisory overlap warnings | `Evidence refreshed under D-PEC-95 (SCA-005 A-38: DEL-09-05 description re-expressed);` |
| `DEP-09-05-007` → DEL-06-05 (E-P65) | `ScopeLedger.csv` — ScopeLedger.csv row SOW-049 | Dashboard — presence board: sessions × worktrees × live hierarchy with heartbeat age and advisory overlap warnings | Dashboard — presence board: sessions (when hook-reported) × worktrees × graph-declared activity, with heartbeat/scan age and advisory overlap warnings | `Evidence refreshed under D-PEC-95 (SCA-005 A-33: SOW-049 statement re-expressed);` |
| `DEP-09-05-008` → DEL-06-06 (E-P66) | `Deliverables.csv` — Deliverables.csv row DEL-09-05 | Sessions x worktrees x live hierarchy with heartbeat age and advisory overlap warnings. | Sessions (when hook-reported) x worktrees x graph-declared activity with heartbeat/scan age and advisory overlap warnings | `Evidence refreshed under D-PEC-95 (SCA-005 A-38: DEL-09-05 description re-expressed);` |
| `DEP-10-05-004` → DEL-04-01 (E-P75) | `Deliverables.csv` — Deliverables.csv row DEL-10-05 Description column | Orientation-read and dashboard-consultation logging sufficient to evaluate the P2 exit test | Owner use or non-use logging sufficient for the P2-B uptake observation and falsification evidence | `Evidence refreshed under D-PEC-95 (SCA-003 revision 1.3: DEL-10-05 description re-expressed; stale before SCA-005);` |
| `DEP-10-05-005` → DEL-09-01 (E-P76) | `ScopeLedger.csv` — ScopeLedger.csv row SOW-085 | Log orientation-read and dashboard-consultation activity sufficient to evaluate the §12 P2 exit test | Log owner use or non-use of PEC orientation and dashboard surfaces sufficient to evaluate the §12 P2-B uptake observation and the §11 falsification clause | `Evidence refreshed under D-PEC-95 (SCA-003 revision 1.3: SOW-085 statement re-expressed; stale before SCA-005);` |
| `DEP-10-10-003` → DEL-02-05 (E-P73) | `Deliverables.csv` — Deliverables.csv row DEL-02-05 (Description column) | `Dependencies.csv` and `WORK_GRAPH.json` into DependencyEdge. | `Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping, into DependencyEdge | `Evidence refreshed under D-PEC-95 (SCA-005 A-16: DEL-02-05 description re-expressed);` |
| `DEP-10-12-003` → DEL-04-01 (E-A22) | `ScopeLedger.csv` — ScopeLedger.csv row SOW-004 (ScopeItemStatement; DeliverableIDs names DEL-04-01) | Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action | Serve per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking owner action | `Evidence refreshed under D-PEC-95 (SCA-005 A-02: SOW-004 statement re-sourced);` |

After rendering, the generator checks every ACTIVE EXECUTION row in all 66 registers: **111/111** quotes are verbatim in their evidence files, against 92/111 today. ANCHOR rows (140) use the D-PEC-62 field-summary form (for example "PackageID PKG-00"), not verbatim quotes. The verifier instead checks their meaning against the registers: 132/132 ACTIVE anchors agree. The 12 RETIRED EXECUTION rows keep their evidence as the record of what was retired; 7 of them are non-verbatim and stay so.

### T1 — TM-PEC-023 disposition

**Observed.** TM-PEC-023 is `OPEN` in `REGISTER.csv` (`d350d007…799d`). Its concern is the nine deliverables without `SupportsObjectives` from the SCA-004 audit, COV-062..COV-070. At revision 1.5:

- DEL-00-02 carries OBJ-003, DEL-03-05 OBJ-001, DEL-05-01 OBJ-004, DEL-07-03 OBJ-003, DEL-08-05 OBJ-001;OBJ-003 and DEL-10-08 OBJ-001. These are exactly the amendment-1 selections.
- DEL-07-02, DEL-07-04 and DEL-07-05 are RETIRED with blank cells, as amendment 1 made those rows moot.
- No IN scope item lacks an objective. The post-setup audit reports "0 IN rows and 0 active deliverables unmapped".

The amendment-1 record says: "closes no Task Management row: TM-PEC-023 closes `RESOLVED_BY_DECISION` only after the SCA-005 amendment applies". The checkpoint-2-accepted plan §B8 names that closure, and checkpoint 3 applied the amendment.

**Does the method let WORKING_ITEMS apply this as a record of existing decisions?**

- `task-management` (contract `e1c97a76…c837`) says "Promotion and disposition are human acts. WORKING_ITEMS applies the exact recorded decision; TASK never writes register rows". The invocation mode "resolution of specified ruled items" is one "the human selects".
- Root `docs/CONTRACT.md` K-TM-3 (`64747d2a…95bd`) names "the owner triage session" as "the sole disposition authority".
- The substance was decided by the owner (the selections), and the exact disposition value appears in an owner-accepted plan row.
- But no owner statement disposes of the register row itself. The two statements that it "closes `RESOLVED_BY_DECISION`" are a plan row and a HELP_HUMAN interpretation section. The group-3 interpretation lists the disposition as open and "separately gated". The work graph marks T1 `UNCERTAIN` for this reason.

**Conclusion: the substance needs no new decision, but the disposition should be the owner's explicit act.** Under K-TM-3, a plan-level acceptance is not a clear enough disposition source. This packet therefore asks question 2, and one word in the D-PEC-95 ruling settles it. Recording that answer is not a D-PEC-95 grant, because the register is default-writable. It is the human disposition that WORKING_ITEMS then applies under `task-management`.

**Draft row (applied by WORKING_ITEMS after the owner's answer).** Only these cells change, by `t1_tm_pec_023.py` (`0e0cd6f9…7bec`):

- `Status` `OPEN` → `CLOSED`; `Disposition` → `RESOLVED_BY_DECISION`;
- `EvidenceRef` = the four records, `; `-separated: `Propagation_Plan.md`, the group-2 `DECISION.md`, the group-3 `DECISION.md` and the amendment-1 `DECISION.md`;
- `EvidenceSha` = their SHA-256 values in the same order;
- `EvidenceQuote` = "TM-PEC-023 closure `RESOLVED_BY_DECISION` citing SCA-005", verbatim in `Propagation_Plan.md` (checked);
- `LastReviewed` = `Closed` = `{D}`;
- `Notes` = the old Notes plus "; Closed {D} as RESOLVED_BY_DECISION by WORKING_ITEMS under task-management, applying recorded owner decisions, confirmed in the D-PEC-95 ruling (question 2): …".

The note's full text is in the script. It is true only if question 2 is answered "confirm". If the owner disposes of the row differently, the script is not used and the row records the owner's own words.

Then `tools/taskmgmt/taskmgmt.py archive` moves the one closed row to `REGISTER_CLOSED.csv`, following the 2026-09-22 review practice. On the prototype, `taskmgmt validate` passed for both registers before closing, after closing and after archiving. The results:

- live register: 9 rows (8 `OPEN`, 1 `DEFERRED`);
- archive: 16 rows;
- `REGISTER.csv` `634641f0b7bf2d1f53d74283cc5e5253fee49ee6292e58a74b751f477345376a`, `REGISTER_CLOSED.csv` `3c1349ba79ffb6eb0abc3502b0325da93ff28e7ecafd5498739a28ea0af11fd2` at `{D}` = 2026-09-25. The closed row before archiving: `REGISTER.csv` `62f897ab174d46282ce7762f2020a2dc94ef445db185d79303cd5526937d4e24`.

A second run of the script fails closed on the changed preimage.

### Findings beyond the brief (disclosed)

1. **Retired deliverables' "covers" bullets (add-on R).** The four retired deliverables' `_REFERENCES.md` say "covers SOW-029", "SOW-035", "SOW-037" and "SOW-087". Revision 1.5 moved those scope items `OUT` (Deferred) and blanked the deliverables' `CoversScopeItems`, and their A2 contexts already read "(none — retired under SCA-005)". N2 as briefed leaves semantic fields untouched, so these four files would newly name revision 1.5 next to a coverage claim revision 1.5 contradicts. Add-on R (`--retired-covers`) rewrites that one bullet in each file to "covers none — retired under SCA-005, formerly SOW-0NN". It touches no extra path, only different postimages for 4 of the 121 files. It goes beyond the brief's N2 definition and is offered as question 1.
2. **DEP-10-05-004 has a weaker warrant after refresh.** Its locus, `Deliverables.csv` DEL-10-05 Description, no longer names orientation reads; SCA-003 re-expressed it as "Owner use or non-use logging …". The refreshed quote is verbatim, but it supports the DEL-10-05 → DEL-04-01 edge only implicitly. The row is `IMPLICIT` / `MEDIUM` already. The alternative would re-locate the evidence to `ScopeLedger.csv` SOW-085, whose statement names "PEC orientation and dashboard surfaces". That changes `EvidenceFile` and `SourceRef`, which the brief keeps fixed, so it is an "amend" choice, not prepared.
3. **Quotes citing Scope of Work files.** Eleven ACTIVE EXECUTION rows cite a deliverable `ScopeOfWork.md`: six of DEL-01-01's, two of DEL-08-01's, and one each of DEL-01-06's, DEL-08-02's and DEL-08-03's. SOW currency (graph nodes S1–S4) can make them stale again, and no validator checks quote currency; EVQ checks presence and shape. Recommended carry-forward: each SOW packet runs this generator's corpus-wide quote check (or `verify_d95.py`'s) as an acceptance check.
4. **Audit-ID collision.** `COV-072` means the plan-count defect in the checkpoint-3 audit and in SCA-005's own records. It means the quote-currency finding in the post-setup audit. Every N1 text that cites it names the audit.
5. **Ordering with SCA-006.** The SCA-006 checkpoint-1 preparation (graph node R1) dispatches `audit-decomp` as its pre-change baseline (scope-change method step 5). If that runs before this act merges, it will again report the INFO findings this act clears. This is a consequence to note, not a defect.

## Options

- **A — N1 + N2 + N3, with dated notes appended to the SCA-005 handoff files (recommended with add-on R).**
  - One act on **121 product paths**, all modifications: 5 N1 records, 42 contexts, 64 references and 10 registers.
  - Rows: 19 quote refreshes, 0 added, 0 retired, 0 deleted. Topology and register counts are unchanged.
  - T1 follows under `task-management` once question 2 is answered.
  - R is recommended because it keeps the four retired reference packets from asserting revision 1.5 alongside a stale coverage claim. It adds no path. Take A without R to stay inside the brief's "semantic fields untouched".
- **P — as A without touching the SCA-005 snapshot files (narrower).** **119 paths.** `Handoff_State.md` and `RUN_SUMMARY.md` stay byte-identical, and `_COORDINATION.md` item 14 records them as superseded for current state by hash, as the SCA-004 sweep did for SCA-003. COV-073's snapshot half stays stale-conservative, meaning the files claim less closure than has happened, never more. Choose P if the accepted scope-change snapshot should not gain text after closure.
- **Amend.** The owner changes scope and the packet is re-prepared. Examples:
  - re-locate `DEP-10-05-004`'s evidence to SOW-085 (finding 2);
  - choose different quotes;
  - drop the human-owned Notes edit in `_COORDINATION.md`;
  - add a re-audit and the audit-pointer move (question 3).
- **Defer.** Nothing opens.
  - The pointers keep describing the pre-D-PEC-93 state. They understate closure, so this is not unsafe.
  - COV-068/069/072/073 remain INFO.
  - The graph's SOW nodes (S1–S3) wait, because the graph orders the currency PR (U1) before SOW preparation, which reads the re-pinned contexts and refreshed evidence.

A split offering only N2 and N3 is not proposed as a separate option. The N1 text states the N2/N3 result, and the graph plans all three as one PR (U1).

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound generator **once** under `chirality-root:bundled:workflow:project-setup` (B1 is PROJECT_SETUP's lane). Evidence refresh and records currency are included by this packet's ruling, outside the `dependency-extract` lifecycle, as D-PEC-62 §3.2 and D-PEC-93 did.

The generator modifies only these paths, relative to `projects/pec/execution/`. The table gives each path's preimage SHA-256 at `13df8b795` and its postimage SHA-256 with `{D}` = `2026-09-25`. N2 postimages do not depend on the date.

| Item | Path | Preimage SHA-256 | Postimage SHA-256 (A, `{D}` = 2026-09-25) |
|---|---|---|---|
| N1 | `_Coordination/_COORDINATION.md` | `8da03a2f0157ba097e4db5b34dff4cd68c03e69c5d0ec72f8a8f49c23d38879c` | `268fb20071fafadfed8f8e9382eb7bc6e23d46922043142356cd8bbf521952c4` (P: `a6a188823bfdd1c5acfff1a6e9b51e6e3bf54e5f7d015493d426227de7eb644c`) |
| N1 | `_Decomposition/_LATEST.md` | `1f2cdcba31b3db2fd8818b16202d2bbc89c3f4a20702a962d133a73e10f556b6` | `626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd` |
| N1 | `_ScopeChange/SCA-005_2026-09-23_2139/Handoff_State.md` | `a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a` | `25626a35fe1b09cd4f2fcdf54c6962ac6ca63037eaeb8101972136c4ca7b6a13` (not under P) |
| N1 | `_ScopeChange/SCA-005_2026-09-23_2139/RUN_SUMMARY.md` | `e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518` | `bfc151a5c97e94eefdc344877a275ba7a6b6dd39a7fd6cb43cc49d3cd36e3172` (not under P) |
| N1 | `_ScopeChange/_LATEST.md` | `a2b5b789d996d52aa43c86419c9a4f02d1aa01f438f1616f3d51921e34f84268` | `e92b3b16a48cd72288c8b6eddc08d62e3e79e0c9bec521864ee7d5484a307d24` |
| N3 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/Dependencies.csv` | `833fbfe0c2a09ab8b564866dff8e55327fb005d5c4993973ef93408d2e2a436b` | `150d1261fb6c1739cd160ae9bbc529b3619ce1a1a7b2f1721afeab5983c97ea5` |
| N3 | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/Dependencies.csv` | `affd7d783e4fb3a44cb45dc4e79011d6afd7509545c0bc3119a779ca07c5bf98` | `0472cb33a3be93b605edebeb419add6cdb123c80f77327d5d311796c4d614b86` |
| N3 | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/Dependencies.csv` | `dcf99c85eeb91c50eb1fa93869e448dcf9c5f568f9287dffd1614eec530eb74a` | `c566fd01abe6d8b833a36789d36dd0d3590ea25b0da4cfc385d345cfdf7a04b4` |
| N3 | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/Dependencies.csv` | `7b4d78c8d9411f2de916ec6510186baecd79f7f5790d9afa97c7cd7d4fc56b76` | `13e7fa920e7844f5b04b09ba5ca109794b3090072bb481aa689eeef91e65e40f` |
| N3 | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/Dependencies.csv` | `1770f6fa3b2e740fff44f85c24d6d256e32ad50ba61e37c4495be9455fef6a4a` | `4438197af5d66b5ebb642222547d9e9d2b40ffe7294cac7e52342badc99dc76d` |
| N3 | `PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/Dependencies.csv` | `58b97ea5d8df6124ac6b94baa922983e82e05cadf8892404b174e6c4a262f1ba` | `1eb7eccf2f5390e7280711ae3cf56b71256787407ac8b56fb71c97a049a081d9` |
| N3 | `PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/Dependencies.csv` | `9811343ccb1f9e6820a03ebdac5aa53f163d355049508815438befb35db032d5` | `45c8911ad7f6cde1d3f6418c813c64146e116f40f362229ae88f23db2eda0c95` |
| N3 | `PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/Dependencies.csv` | `324e0d6b1d420bf2be50f1f138d4924e57f2b36139add83e3335a5f26b41fc24` | `74528397254c086aaaec7d0f0a37684889e0893c4c20cfd6729debcaf77b8584` |
| N3 | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/Dependencies.csv` | `9efe23791eda63ea5ec44e477bb800276812a98a51f5c594d27a49f5cdebca97` | `ebcd9b43734315aff524a17f0766a97e041cd46ff661423e82af38b3c4a3f8b7` |
| N3 | `PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/Dependencies.csv` | `9fc8fb4993a6e9bcfbd0a88b5b6e4220def243a0d41b0362c5e3be8d008b4985` | `06d64c9f75a393c061ff2382f14ab24b4855a03c1528fbb40fdf9c071f7e0db4` |
| N2 context | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_CONTEXT.md` | `70e70f495817dbab5c25c67c4b4bd5aac756816d3df9103e57ad991c286817c5` | `2fe92b000bc2829d4bc3dc69d01d64044ada2db28b11ba70e22118a95ab05e75` |
| N2 context | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_CONTEXT.md` | `59fec8afea9544061dcd9fb0a6510c5492b2480e7d71b35624cf64ced9b81a8c` | `05a2e5d08fa5366c21f7ebfe52e7c80503e484fecb2f582bf8d302214346e578` |
| N2 context | `PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_CONTEXT.md` | `4d49f17b8a6aadb9961780ac3fc425df3e4fccd10f9321bb2c84427b32214337` | `53f11105266638f39f1f1601f9a7c72fc0bff245bb4f722be6798e8b5effa16e` |
| N2 context | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_CONTEXT.md` | `ed453eaa112e1c8af9b1c201d0e4c3b5bb00b11e776c7658cbd333d430a6e058` | `e97e3c07b999f2fb5a6f13176dfe2a7c3f58403308554d02da876e93cf26e77b` |
| N2 context | `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_CONTEXT.md` | `b479ce57949d78b9db78a54c8b77eae418d8e345843d303c69fc54087e694afa` | `52a4d9337e7551bf154bec549bfdcaa76ae94c96dccbf37959bd9eeaacba969a` |
| N2 context | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_CONTEXT.md` | `4bf394696c386f6a5f792a8f9967abc03e1d1339dc6715de09647f296ad25da1` | `a687ad1f91bcfa82c24fc08c5577435b79e56d4884936e2903f0f6633f2675f5` |
| N2 context | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_CONTEXT.md` | `6829fef13bd2b65dbb79ced9225cb91b806016d5d363a1135e194901311d7746` | `7b4132ab8be4e6b5fa7a2956563fd8148967bc6fede9beba6df41b96a638c92e` |
| N2 context | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_CONTEXT.md` | `8cfabfe6bffb9325246e4d94be47c2da2b65a22eebae8e01dde7292f48aec382` | `3c1e856db52c85de42a7e794b7a4110387a9dc2316851061f0f21f054eb26125` |
| N2 context | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_CONTEXT.md` | `fcf60b19d2be414dbf6d1572b035ceb5404aa86ac8240709c5e6405762af3346` | `8a5874c2e46ac1c5519ea2a3123be618754f5c0989084dfed1cc562d7ac508f5` |
| N2 context | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_CONTEXT.md` | `0d9ccb791028d4d59c345612fd27e7e755882899161be15076875bc7a78b0271` | `415a4a4252978e4617236cc67adf37b59d50ddc6eb08270a06398d359137c996` |
| N2 context | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_CONTEXT.md` | `006c508a849aa2b5316166029aa5f737494e781ca9b2d12594dbca9ed53e5c5c` | `2407e64f042e0c7da7e8f2ae7aabfbab59c23976d4f7c954d541daf6ae524bf7` |
| N2 context | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_CONTEXT.md` | `bfe3b987d85cd13dde55cc0db22caddf68c8525180b026a2bb3977cbeac5855a` | `5502601cfe9f1c469b0df2474943f870d6e57f9514d6df830f7f6d9e32356470` |
| N2 context | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_CONTEXT.md` | `242107d811521e1ae2b6645b6ce12a198e8b2ca91c4d53298a1c5f5e804807f6` | `1374dc7d81acf021e85404615097207948d96106ddcea9bd24b0e6823fdbdbe0` |
| N2 context | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md` | `0b56862a83014d469cc00ddd663dc2e60cb93ac4249eeed169480b88e7ec9b21` | `a505c2686af7c6d51fe4d1d8dad25bcadd3a5d9c59372c3f9226d31fed2263da` |
| N2 context | `PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_CONTEXT.md` | `3f068736b91bfdb60681e9019f5c936edd2d74b29e0f918989f0122015b1e700` | `cdcc030c868471ecf0a4bf13f315b171a9fab990fa1b1140d4f060bfa1d6294f` |
| N2 context | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_CONTEXT.md` | `20710c09a9524586b9efd61bcd20a768df4ffe37b33862c80a00e069e189bed6` | `4c1cb297d34552e03fab61f08f0105a5b04779a8e71755a2bbcea584ab902112` |
| N2 context | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_CONTEXT.md` | `ab427727f5e9049f9e2b341b201929b2485d1a97654b51bab7d2391605defaed` | `a0eea793cf9f871f0c6c7fdcbab87a352b60fe800fa36e693f25357529c2126d` |
| N2 context | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_CONTEXT.md` | `7ae79b2138fb458203f7105cd863419769f60308e17072ab4e2b0a13b610ba40` | `9338cf5592fcaa103fe8a5fc8245d4d6e2e1d533b88a97cd28f031a12874fe99` |
| N2 context | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_CONTEXT.md` | `1ed76ac629d33bad7d077b50a70026f90d25fba858df9b93a0084711f7490071` | `b117fac353aa4f043e2cedc07c7cf393c3e7cb41b519bac7ae753cf3a03e1470` |
| N2 context | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_CONTEXT.md` | `ad7fe45e8b9b2b2f541ea97607625af108700dc7228077a8ef0701e6d03f9ec1` | `a8e76d8999dbd8e3f9ce32f42823736789905576e6678679b1d320d6c81e66e8` |
| N2 context | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_CONTEXT.md` | `3db26dc1456daa09654fca7d88186563611db462a5788d46e2e0b84fa4538f95` | `9717a0a2500a193136cb162d90275615fc87eb8cfdc477decf7b06424be73a48` |
| N2 context | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_CONTEXT.md` | `e20c22ee0d6fb78e54519194a8e1eb1e0ef9594b96fa5854525a0006df13a986` | `f84331ff03d83f5f1ac2116907e3fbae8358fbc4e5f56a40cc6debaa0568e02d` |
| N2 context | `PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_CONTEXT.md` | `375f46713bd275576a8343feb6a1768abbe0c1f5cfd61e888bb60111abe44cc9` | `38acdd6c8a7d812ba61387f91a751db7ffab723813546910cba3f5c23e52307d` |
| N2 context | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md` | `d9b84e656c69f09de9f3b0cc55fa87663ad39cb3236200493ca0720a46da1c58` | `4644758f07a93eb203bce19533916fbf4e55d52e867895f2a87a5b99b4aec73d` |
| N2 context | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_CONTEXT.md` | `787d462878730161f667e6c8edb928f2248a8ab460c409566f826ed9c6265a6d` | `f5dd9ea168be0fc6fb6bd74dbf680f1e218867844bb619510e8c4bbd90df4634` |
| N2 context | `PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_CONTEXT.md` | `2ed591ad9008ebfa144e9c5b9a7f0a1d5f2ff858002c9b6a49939dbe46b3ccb0` | `0a82ce9ef981ebab381b2897d6f42873dc80aad57ebc37bd695f6faeddc96131` |
| N2 context | `PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_CONTEXT.md` | `f757ca97a8f822bd74876b03ef3cbb4f5a61846cef0b369487cf730b680d4832` | `d9a623d6c6bc1a8651a84447b9e1cf85804aa26effecb95573acb253af6159c4` |
| N2 context | `PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_CONTEXT.md` | `e53497585ebce826bd16244f924a9164f5cb46334e935daae50a55ebed1a9996` | `899954af31d1be0b19fb6cdfb94acfde72fbcddbc2519ebecc107dfe155089de` |
| N2 context | `PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_CONTEXT.md` | `1e5957cd85780fa5dbb4b6f6353564a49ec79c4cf436b62726e17bf269d0d01f` | `a84fdb13b87ac8ac761898430bbe6d37b26d61f5db9db99b98e893f496c2773b` |
| N2 context | `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_CONTEXT.md` | `a146fc6acb4fe5da4d513312f11c8c2db3c3d2cff77aa4720b484b260a1f86bf` | `16157838aabf1d7b3acbd11d378df77975bdb086b23829dd4cd095803e5b99ce` |
| N2 context | `PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_CONTEXT.md` | `21c858156a5f4636bc3d79765f9c88a5438efa0e90254097e30b77603e9dd54d` | `d7f98897834c9c8308c30f62a767912143dcf52d59731f796de62058958c38d5` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_CONTEXT.md` | `b216baa191be3309f98f938b06f2a9df1204b8d02d20088705e70c41561845ba` | `94c93a624a2c84e1433d4c72712e5067e7e31fe1ed37cbad11d114bb4fdedbe5` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_CONTEXT.md` | `43a5587fa48498909290540492de137c38ab3c82a96c4caea035ce6831a9edca` | `da16ba796b54e3615d85f275b923d838f40140a216707e4a5a26427af28bd9de` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_CONTEXT.md` | `244b635d3864c91d768c0dba6874168fb851062fdaa309587af1240ea0a6248d` | `2042fecf8c1c4c2b2ab993ba1170d6205ec07592e1dadaff2d7be6a30f760044` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_CONTEXT.md` | `c57966413a2174ad2d979d31de4fee08e7e9b02a6e53c2e157fb4c19f577ddc4` | `50afd95f55c1b82298ca132c2b28da65c4f7524e3b0f262236591eaa1124cd72` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_CONTEXT.md` | `ccbbfb44c7143aea9067d1d0cf38247aee71dd4cb07fb97249d1fa121bab4d33` | `23962c3bed576f73d9847c6cf486584d71ae8bdca8f07338af122c8ceaf5f204` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_CONTEXT.md` | `1898159dc8cfb1f33e75a4e1330b63f533a5acc4775ffea7a97e192376a4f657` | `fce20f41e538794ef2e281b7d946e7956daa5ef9b915887fc0cf8a34faaf8129` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_CONTEXT.md` | `88bdda5d9c590df9969d22bfddeafa441cec74a11e31e2e27e9488d66af50af9` | `695088ed3e70385121e22f31825b33efb2fd68e9452f41b500bc7d1d85eb7597` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_CONTEXT.md` | `0fd365a5b1f86bbc1e5f596ee0ea945275e3693f4c78d68cfcf6a6fed02f55cd` | `6ff57483f8c75a268ea990c8dcc077e13169d78496c377aadec9007bdc55ac9a` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_CONTEXT.md` | `7ad8761a61727297478eaaac5737af6cea9bc0cc7e1f146c70ff4966d52154c7` | `7f3d7035d5760ce4f6636212f4b7932c5daff5170c3089bc0414a1372dde7c09` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_CONTEXT.md` | `6bfde0e0f01a12c3d4d48cf067872b2752a41dd334def4bdc339af9e83e0b6aa` | `cda340e681a8ee5c7d2b005b5a703988ba37dcdebd6f18a1d3f8c8d6591d945e` |
| N2 context | `PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_CONTEXT.md` | `c7e16840930fb534e9591364a9cc772aa00d74f8441d196d07323b83495fd222` | `23ce69245e66b4ad5104b9ed2189ae49b09e30df69f2f0aef0d03cd535cbba05` |
| N2 reference | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REFERENCES.md` | `21560f41e7fb075fb72fcbe419ce0c7136941622134cecfdf125d7ed4b904fd4` | `db32c618c8beab8d418805c69f6a3d53871a01981f6e063ca1c414c33f401f7c` |
| N2 reference | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_REFERENCES.md` | `d4bee4effb1c47744438f691d1821ce7953f4da40aa17eecd200cdc88386fa74` | `005aac9b9612ce10bfc06c9a2ccf256f9c06ababc192724a55cb592cf5c732dc` |
| N2 reference | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_REFERENCES.md` | `481b34847cbbc9bb15d792e0990b0b8f0b2a5750c82a041d65bb50bff4ff615f` | `21b2110208b72467d01dde4460ef7b16fbf41afe11d101a69f8f7b0fe320534d` |
| N2 reference | `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_REFERENCES.md` | `e72764eb33fe0deadb9d7f4e33b43e3a3e10e44949f5cd7aa46fc7c56e6611b2` | `8f67568f44f9c386cfcfdb3230899b5e84924527991d351e2c9b936743f32205` |
| N2 reference | `PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_REFERENCES.md` | `e323c6a086b2ed7907fc5c80d502197b56c1983cb14e0fd67f24aa33ba319774` | `cf3eabd186c5b2186c60845c975b827d1b5003c060d1cb2c0a223e36e4f7ffe7` |
| N2 reference | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_REFERENCES.md` | `8a661ac88c3047e1c6892a6e24544f2714329579c6717f0c05ac840e4f468bcc` | `8f0dfcd7b1664bcc1173d4f099a7e74ca0b5b4f10755d53bb90cf022171b9400` |
| N2 reference | `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_REFERENCES.md` | `53ffa97f12951dd4086fc80ce3e907cf57ca273381b30018b922644f100e3dd9` | `f503808a708413cfdbf0020a0b3f3116c5aeb242a0355e083077f20101f1216f` |
| N2 reference | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_REFERENCES.md` | `20c53f9b060f24c5278199c8357c64cc5f1a36fabf218da6d855f2f12a40647a` | `20d344699830c43b00464ca0e41efcf3e415c695d38427ba0b8e81f28342e2c3` |
| N2 reference | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_REFERENCES.md` | `a4da999cef5d3c94d9ed61f2cddca297481be7ebdde52d13d2f8a9e213a35693` | `6e640cf84b3beb619c7503c7702017d786b80da237ae1be8ea01275c6d9c63b1` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_REFERENCES.md` | `42c74660a51bd92fb8df13d0b1c3109651d2304b35413b25ac5b6b281d7cd882` | `370181a2da1f92b6672fcc424d263fa567a1a35c5e8f795f52a0591cc964bdc1` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_REFERENCES.md` | `25ba5e5b64588948a5c5e66e083367fd696e9d36a6fc109fe4b5f5ea51db1c5d` | `152c6af2b22f60414ac215240207518d794a2869b6e4639b3ebb396d96c81acb` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_REFERENCES.md` | `b5e3211557729e3eaeca9d257417a1fccd64374aea66833639bb011b67c771f8` | `e3962d35eac198dadc0c666b08a668da881500f59006966ef5e9d1bf1efde9bc` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_REFERENCES.md` | `9275945f28d5722112a20e2329c5b6723f13c28cc1431942bbcfb463d9946125` | `bec637be26e4875954acb67ba346120f497ed9b94555932c18577e434a091796` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_REFERENCES.md` | `57cdc7bc7e6229c19e144352b8de2f8868c0039d6faaa025caf08b46008e4843` | `9d83d55b306857b70ebd608dbf473a916c99626c48a7642011a75281b7b4cd3e` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_REFERENCES.md` | `5c3ddbf2269e91165e8a2df5cd1eb3c88aa4a8e219afeda65a12530d2215f82c` | `1000ff3dd8ce0ec7ad23ec5f658994000a1ab512eaa6a323a295b74a98c1a4a7` |
| N2 reference | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_REFERENCES.md` | `228c49f4b1ff8a54f99e58510e8f145535b6ffba69c922aeb88493cfdcabaf25` | `15c7018e01f4acb32e319fd93c48331139e8fea5c23c9d9410737e029a590861` |
| N2 reference | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_REFERENCES.md` | `682edec873d4771213845ed35ce2afe2b8b6ed218bcc920e63bf08abe79a937f` | `a7886e3cc64c79c9ccfb099fdafb829736b69368af76d62b6183ffea5a6995e6` |
| N2 reference | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_REFERENCES.md` | `8a5a1e1824365c365024fb08f0333d2ea0fd0bef80e0b99cc57d068342491ec5` | `09975b4636056f878aca7574142379d0573d58bc85fda28e8cbe482865bf7ebc` |
| N2 reference | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_REFERENCES.md` | `8d12f602e86792c6ebd02db6e540b41e219201adae8bab8a6dd2d79f3abbe9b5` | `f11685f717abe03d25b92bc183d67e40264d6f317471ce9b13db3d4f9697ca73` |
| N2 reference | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_REFERENCES.md` | `f0ff68a4c268e11f9d9d32d87a377d3b2877832eb9b3ea21d438115aaec177c9` | `9366b6ed7867aa339766765a48d4bf3ba64e703cd9a74bd964bbf2546160fd4f` |
| N2 reference | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_REFERENCES.md` | `7200cda06600495b7b5321fcfadcdbfbc27762ba7521d3513e4e56a5647e9224` | `dd731f5d56f40bf42d20a6a60c35e5e31ff55d8291dfcbc28cf653a11eed4f8f` |
| N2 reference | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_REFERENCES.md` | `73b4e4cc9116a115201f23a5296edf0e905355d6ac2e2b0da558609ec5c9d4ab` | `9e8ef0044e7232699c7c8f39d45aecf3d4063dfa93cd9558d03b5713a61b68d5` |
| N2 reference | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_REFERENCES.md` | `fb2348289bbd2da6df823a1c9dc001bf62fa460aea8132e413c0266d322d7e0d` | `334caab42cab5e50e41397f2c00540fbded70ab30d33c7a3eb68469ad2c417b6` |
| N2 reference | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_REFERENCES.md` | `55eea82370f608dd7ea75418004af9a77cc1417d08d7b8baaf55db2b22eeebab` | `b039d6736b01f5399d87dd09f07cbcb13a6d94f343f7b935cc6405efd9cc194b` |
| N2 reference | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_REFERENCES.md` | `d3a41d79d4687fd15052d95186626c4dc6db3f45d1c900d1cbc835b977920058` | `81b7f2cf5f5d7a61448ceade15edfab416ecb77eb7185b9156d3abc1d458acd6` |
| N2 reference | `PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_REFERENCES.md` | `873889e0812dc9e0f808f75ebe0425b82ebfa6cdb2b04ff63c2388805f213038` | `d96e4e4c608cb552f1ceb71daf46d6772f573efc09e6161270ff8cbdfc5ed003` |
| N2 reference | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_REFERENCES.md` | `bd866c34c6c7d5daffd3a136cdd2541da8f1c2585a8890cca466743a27b3a71a` | `cbcfd50a884e507e06f55b017df463348bd61368389270e9b9acd35b1959793d` |
| N2 reference | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_REFERENCES.md` | `fd226572dd115a54fed3bf651d6b58fead77b86777165d7a27331c402c1886a8` | `787380f88ec5e753548f5a4c8c842a94fd238b8eebe045dca9a007e4816fa1f1` |
| N2 reference | `PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_REFERENCES.md` | `6beaa2761fb978ba07a4b6e1259b51bf939dfe6a67bc4a0053e7dc02c55368b8` | `f32444f02048580d05cbe58aabc3e660987edad6861092aae4e9736081172e80` |
| N2 reference | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_REFERENCES.md` | `d052d61c1b38925f298bc659bb796c8a5eb796811558cdefd8139e4361fe01a9` | `cbec466b9054bc22206c2ffc2c295a218eebb49b7fe9d9283c5f085e71017382` |
| N2 reference | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_REFERENCES.md` | `d00ed531a857aa0ca172e3dc3f17cefda433e7073b189610615938d026e44ece` | `a92d69179a62cbc2d327547c4729cabf9f44a2a44d45dbef2fa654d4623b4438` |
| N2 reference | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_REFERENCES.md` | `a38bc032d32d811e10db9ec2dfe8359c5b1192e811d16341aa0efd25747ed182` | `4e6a306004fef85ff35606ee38ee4ffc08686e4495e3e69f98b97abaca28d945` |
| N2 reference | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_REFERENCES.md` | `93303124d4e8db243c0b6f95753a0887d22b35e32cb8e8b756bd96d1dc0bd407` | `88a7ab2f0f096f05f26d3c0c8d2b64d98b6b9c5c5de878298e56097c4a027f50` (A+R: `ca03c93f1ab4cdacf2bca1390fcb59308c12e655798c21fb522b8176f97fce18`) |
| N2 reference | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_REFERENCES.md` | `68f93f33b49245085d8726226f0f60b5dff2a8e33504505eceb3d971e81dc80f` | `bcb24a8424d3b8157342dd7aeb0b5852cfcb86bc1a9517ea89f11823faca51d4` |
| N2 reference | `PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_REFERENCES.md` | `11bfe2a700df99ae0d963c28b1733e2f636039337944fb34748d3624ee4709d3` | `21fc6146c658b6f1e793a0b7c84b8a7d9a0b420787edb7a2b978ced9e4a0134c` |
| N2 reference | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_REFERENCES.md` | `7db708f869b0579b009238744fbece05b43275c960f3c0ae544da233f6a34860` | `d7cddbe827d48097a614492aabe7c6a14ec914a98071529e324b9ba83b5ccf49` |
| N2 reference | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_REFERENCES.md` | `69d76c3e9eba29d2c160fd68c024ff21fcbcebe7833c726244c2876e993c9c74` | `66fbcf827f083b459ea4a0f296085631cfcfaf5a9cdf95487369371355f3779a` (A+R: `de57dac815c281c09ce079ac8ec7b24f60956a20cf4631fe002f947f827c6ce0`) |
| N2 reference | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_REFERENCES.md` | `896c1f6926360a9ae5db919f8506794ca2e2890d817dbf2c592e99733bb416fe` | `2530101559e367c8ac390c3e9279f72ce1bd4c2d8ef53f637d92aeab9ee11376` |
| N2 reference | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_REFERENCES.md` | `2289938931aaacc4cd29fdfdb3fc49cbc02b6e7f7f281d10c45f401082713dc4` | `eb2442c990e31c5fc97b667e23c23bc5b345492d9a6ba1bbbcd61c3c11571523` (A+R: `da78383887097c25858fdf531362d9f64604ca682d1ff909d7663f3bbe9a8869`) |
| N2 reference | `PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_REFERENCES.md` | `5d4cdd94f23b89411fcd4b16d4ae6e7f25258390cafb63c0e7ddbf798cbe821f` | `3d220b0e7905239971e01fc5cfac1670af45078a9b5059ad77f28ac02a38c674` (A+R: `c6a7a19512730fa3b255b4855e03aadbe02e4f4b71171805df9fe8972cccf57d`) |
| N2 reference | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_REFERENCES.md` | `83e25138dc8ebf7e7102c651742c77e1ea9748b9417c9ac89d166f81bdfb39fe` | `482b9f05504719abbc30ae38cdd8ef7a6b4b62d47b9042bbf8c9311a9a440bf2` |
| N2 reference | `PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_REFERENCES.md` | `734258088c76a48636751b5f7bdd7e5467e2e939e2158dff7037d1833a8396ca` | `4b9071df7e447bfd122d240588e6ea2238b7c537cdf04a199df9228f755d06c0` |
| N2 reference | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_REFERENCES.md` | `ae13d4f030682b0d90db4f2a7884cc01a1f47abd2baed9dbb4646cf6346111f8` | `f5610e5c224662cc7df0b1fc5475893f75388fe17e503beb0db870c5264f0f4c` |
| N2 reference | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_REFERENCES.md` | `9948422bcf701bb31d4738c4d2655fa7975178fa87c14264a2f0f23c6d089fb4` | `1bfa6baf155e153f1e9607be9b8e57e3ee6d31f04e4ec40e0220f8201c8f873b` |
| N2 reference | `PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_REFERENCES.md` | `66489416f3dfe9c61f7a25865238cf1bf4a54c9e398b53c076e1fcc56af86b1d` | `95fd692f88487d6f72c887512fcf618c7bb1ab4109a29650491a7bbaf470d6f1` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_REFERENCES.md` | `7cc4faf411a85a3cf17a33a0a50f5065aace83ef3eef003298dc721bbe6dac0d` | `8ff66a8b3896cde83f907737b630fc6fc45b5e8e53acad646906b3dd22f14147` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_REFERENCES.md` | `0d34444f7faaa91e4e5aa8b4a16cb05707d491a353c863bb12387fedd9c08487` | `298ccd42e5fc6dabf85193cd14dba1c998f3056ff52bbb048387068c009170e8` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_REFERENCES.md` | `78ab3bb0f5957b152a05bd712b6f55fe900ebd4f47234bfa1c878daa8a620537` | `c3905be1b42cef9e9965d486e0e8573bb82fdfa672afbe14aa68dce8b8a3130a` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_REFERENCES.md` | `3275cdc25d61bdab3baa276ac917af67a666b7091dfe73078391c41f544c9f55` | `37f5f6e22af354d35de5c7ab5023a627582d6c36b262e226abc9ce8776532538` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_REFERENCES.md` | `57c637d457886cda3c23a51b02167484eef670f4bcb7d41dae98547a61721145` | `9a64f20affd93c89e895414b64f79aed500be6cf39c16c44854dea6bc70c3f2f` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_REFERENCES.md` | `7d814916e089a74cfc54c330e4041af2c40b7339b774b10d1062b4a6004f8580` | `971473698783d8eddbd6781b15c94d709bfdc7b8de5390a63f49bdacae855c22` |
| N2 reference | `PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_REFERENCES.md` | `d74fa83df09a07d1a96b7407c2a748b7e9821861e3556a54d0d0eb9ad859d168` | `9adf8d8f56e53a08452a6aadc5f866a2c1d646a02235b7bff9b302cd2bfddef3` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_REFERENCES.md` | `c50bb2b69a39901a60866c2b2bb3d652f570ae10b827f7845b4b3e3fd1542c7c` | `7b831447e279d9e296b9fecebe07fa3552b63a751ea5f750fa34ebe1b4ffe438` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_REFERENCES.md` | `106baf2082bd0b82e1475f56b15f1bf0d2280a83188f017d7c261b2ad2ec1181` | `90ceb3a244b5b67d71f1ed350325c99eb92f190fbb8f2004b27c571b966256c8` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_REFERENCES.md` | `99b871635d9a3a4ec61393c63138211f9ff8bfaae0a4175596b3b85644a847d4` | `53469876f8fa7478b693ae399797335b00d2e38584feec99a4ca1a148450a5f8` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_REFERENCES.md` | `0dc254ab57227b1fbf0109d2ebfc14a41654ec0c85c1eda3050ac569671d5b58` | `2e63822889ea6445a1c14ebc3f485f2ebc31972ff9f0a7b9f17d1553b4cbaa17` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_REFERENCES.md` | `6e64cb640b394c931f1c20306b28fc5f95fa60d8f5dd4280911c739c825b8f02` | `401555caaba8bd84d864d842553cfcd539a8aab1871ea46e11fc60151d4d0788` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_REFERENCES.md` | `1052ada927f89b19705ec27e9de9701cb9024cb08d4ec71210e4ef7de63b4944` | `7fa66b924fd5c2c3b372037c4a7a58bb1a7f37803335511ba908341209890c59` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_REFERENCES.md` | `bdc61af4db54085784362cd33149c4ec90ce60c09b5df5fcecda62add0f15e45` | `c1bdc4ea35a1ecfa98037b9465bf4bc7457e62b6a67ee5b3dce27078a26a2a3c` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_REFERENCES.md` | `7884c0402107ed45b37e170094f83c0dac26d276439604b70e3c9b86cfc67fed` | `c33e13a6782af6218edebe4a8c72b07bee0d82f1c60e730af616459af09ee874` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_REFERENCES.md` | `a52cbe5b267ead64a733aa3383e14b7761ab2fa6bb0523c4257e68a6bad60a52` | `a07e02eef7fa4256aa47ee80d1003ca82d7f891d9a6fe040246938c854fa00fa` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_REFERENCES.md` | `d8efe5e540b8b0ae32ca1e9c26b85d8abdbcc01898c31694165934fa9958a20b` | `f9ce0996b74fb257b8a312652f940b12369ad169b8170bcff778e817b4967f7d` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_REFERENCES.md` | `94d1fd3dae2d8453907db80eb2368cac713889e940d97bb846f329b97e01202d` | `e2dfd94a6dfd78ab6f9b28a2c2b4eae7e630a80562f8a8001b6c1a77f4a42c23` |
| N2 reference | `PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_REFERENCES.md` | `9f0d557bda938e1a9180af89c5b98bed308fbdaa19032fa12c90eb0067beb151` | `cdd04184fcd742061e2d568120f14a34830827b753e559fc10d646cbd5a13983` |

Aggregates: members in bytewise-sorted `projects/pec/…` path order, SHA-256 over the concatenated bytes.

| Set | Files | Pre | Post (`{D}` = 2026-09-25) | Path-list hash |
|---|---|---|---|---|
| A | 121 | `9e6aa1c5ffce22f167b29cf4e2f454a63dc4974cff49923c5d66cc2a9cbebd88` | `946646dd90a9637e7881932957e2974757ba37ba137ca04daa67ad9403853bde` | `4dc3be1a26fc8e0e3c69a8ce555568d6fc879e090749f5106c36ded2cc4534e4` |
| A + R | 121 | same | `282450fc40bc021cf609cc9326c51651e56dd5bc423dd0449a05cbfaaff5fb4f` | same |
| P | 119 | `b8ce26799bb6e1a3acd4204f8cfa632f429b730751449553030b43794c54e7ed` | `f0b9f72662290b72a5a0e0d86cd3aff06b54b1d5c1b41d7b1b3504508e30fb7e` | `ebac38d0f8acb0556a88d83669d37e64e9965beba0ffc4adafdc9da6867edd03` |
| N1 (A) | 5 | `d95826bc534937edc1a8c9703c8a45838aef3cbe9bb0161a2f1dc183fe87bc1c` | `de4e939317949d0d690fe6c03603fe7ca537858354dc702d22ec832bb90dc47c` | `9a77ca76583fc7c124cbac7cc6dd92dc1a0b775954f184d6f91ed86eada2db2a` |
| N2 contexts | 42 | `0f62438a1f26365b1996fa39b391fd64fbc501d8d754e71f40eaeead75740207` | `61587b93958effcb93a74cbaeb75aabaf15622c18868ce926066f6f1d3e3bb25` | `55f28c895d3eed2ffaaafd8b0c1fb5e8fa09a06e3a77696bbf9530a0117db648` |
| N2 references (without R) | 64 | `98af4a4d43932c559d183d130d5523c1b5457273f3153d74f7d91f8a90ce53d7` | `2f46427b34f129c059092940325eaeeb313a09e9d1797f07b0b56cc268fb6308` | `a350074796280909948b0aa6ffb91f75b432a83b3222b62fa8ec43e6b5b5d6ea` |
| N3 | 10 | `36945d7f38b93989ecc5b6543b1b89c0660c48eaee1ea90e9d292fc4c8306d28` | `7100246ab9bcb9faab2c3b7f015b6ba4a2cb0e2220a4bbafeca1bbc59d2da429` | `3978e4554ee279f4d3073d76846ba0aa3062a1c03621deff595014a46f48ce50` |

Read-only basis the generator re-verifies but never writes: `docs/PRD.md` `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32`, `_Decomposition/Deliverables.csv` `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a`, `_Decomposition/ScopeLedger.csv` `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df`.

### Generation method (binding)

The bytes come from one run of `gen_d95.py`, **SHA-256 `0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78`**. It is stdlib-only Python and was prepared with CPython 3.13.7. It is copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/CURRENCY_REV15_D95_{D}/gen_d95.py --repo <REPO_ROOT> --act-date {D} [--retired-covers] [--option P]
```

Option A with R adds `--retired-covers`; option P adds `--option P`. Before any write, it:

- checks all 124 pinned preimages: 121 targets and 3 basis files;
- checks the N2 population and that every anchor occurs exactly once;
- checks that the 19 rows are ACTIVE EXECUTION, with pinned `EvidenceFile`, `SourceRef` and old quote, and that each new quote is inside its locus;
- round-trips every CSV row byte for byte;
- checks that all 111 ACTIVE EXECUTION quotes are verbatim after rendering;
- checks that the write set equals the grant for the chosen option;
- checks that the local date equals `{D}`.

It exits 1 with nothing written on any failure, and exits 1 if run a second time. `--check-only` renders and checks without writing. `--reproduction` lifts only the local-date check, so a verifier can replay a recorded act date on a scratch export. `build_gen_d95.py` (`a67afc51…e438`) fills the generator's pinned block from an export. `gen_d95.template.py` (`c799ef0c…065e`) is the unpinned source. Both are preparation aids, not bound.

**Slot rule.** The only varying bytes are the act date `{D}`:

- in the N1 texts: `_Decomposition/_LATEST.md` (1 locus), `_ScopeChange/_LATEST.md` (3), `_COORDINATION.md` (1), and the two SCA-005 notes;
- in `LastSeen` of the 19 refreshed rows;

plus the one derived hash of `RUN_SUMMARY.md` quoted in the `Handoff_State.md` note. The prototype at `{D}` = 2026-09-26 (`--reproduction`) differed from the 2026-09-25 run in exactly 15 files. In 14 of them, replacing the date made the files identical; `Handoff_State.md` differed also in that hash. At another date, the verifier reruns the generator on a fresh export of `13df8b795` with that date and compares byte for byte.

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`. Record each command, exit code and output in the run root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | the generator's built-in checks; the ruling and its register row on fetched `origin/main`; PR #919 (the work graph the N1 texts cite) merged on `origin/main`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | preimages as tabled; `ALLOW` everywhere; otherwise stop and route the discrepancy |
| Strict registers | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` | exit 0; 66 registers; 263 rows; **0 errors / 0 warnings**; output byte-identical to the pre-act run |
| Closure | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <run root>/closure` | exit 0; `closure_summary.json` byte-identical to D-PEC-93's (`bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a`): **111 edges, 66 nodes, 0 SCCs**, 0 bidirectional pairs, 0 orphans, isolated the same six |
| Quote currency | the generator's report line `CHECK active_execution_quotes_verbatim 111 111`; `verify_d95.py` | 111/111 |
| Revision pins | `verify_d95.py <pre export> <repo root> --option A [--retired-covers]` | contexts 66/66 and references 66/66 name revision 1.5 (references also PRD v2.3); edits confined to the anchors (42 + 64); one shared provenance block across the 64 pre-existing contexts; exactly 19 rows changed, in `EvidenceQuote`, `LastSeen` and `Notes` only; ANCHOR rows 132/132; the SCA-005 files append-only (A) or unchanged (P) |
| Schema per register | `python3 tools/validation/validate_dependencies_schema.py <path>` for the 10 registers | VALID ×10 |
| Receipts validator unaffected | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | exit 0; output identical before and after (the ledger is not a target) |
| Every-PR check | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | exit 0; no finding cites a target path that the pre-act run did not (on the prototype, without a run root, the output was identical before and after) |
| Byte identity | recompute SHA-256 of the written paths; apply the slot rule at another `{D}` | equal to the table |
| Containment | `git diff --name-status origin/main...HEAD` | exactly the grant's paths plus the run root; with T1 in the same PR, also the two Task Management registers; nothing else |
| Whitespace | `git diff --check origin/main...HEAD` | clean (`.gitattributes` gives `Dependencies.csv` `cr-at-eol`) |
| T1 (if confirmed) | `taskmgmt.py validate` on `REGISTER.csv` and `REGISTER_CLOSED.csv` after closing and after `archive` | PASS / PASS |

**Re-audit: not recommended now, and the audit pointer does not move.**

- Every change is derivative text, and each is checked mechanically above.
- The audit's blocker and warning counts cannot change. The four affected findings are INFO, context fidelity was already 66/66, and topology is byte-identical.
- The next scope change, SCA-006 (graph node R1), begins with an `audit-decomp` pre-change baseline under the scope-change method. That baseline will observe this state, so a separate re-audit now would largely duplicate it.
- The N1 texts say plainly that COV-068/069/072/073 were addressed "without a further audit", so no pointer claims an audit that did not run.

If the owner wants one anyway (question 3), the amend adds a TASK `audit-decomp` run into a new `COV_D95_POSTCURRENCY_*` folder. It would move `_Evaluation/DecompCoverage/_LATEST.md` (`2b43dc3b…1450`) only on 0 BLOCKERs, by the D-PEC-93 rule.

### Independent verifier

A fresh read-only TASK that authored nothing applies `chirality-root:bundled:skill:software-code-review`, adapted to governed metadata, and returns a verdict file. Defects return to the author; the verifier does not repair. It checks:

1. **Basis.** The ruling and its register row are on `origin/main`. The run-root generator hashes `0e9ede50…be78`. The recorded preimages match `13df8b795`.
2. **Reproduction.** On the act's local date, it reruns the generator on a fresh `git archive` export of `13df8b795` and gets byte-identical files. Otherwise it uses `--reproduction` with the recorded act date. It says which method it used.
3. **The fixed checks.** It reruns the verification table and gets the same results.
4. **Semantics.**
   - Each new quote supports its row's `Statement` and target at least as well as the old one (note DEP-10-05-004).
   - The N1 texts state nothing that `origin/main` does not show.
   - No context or reference field outside the anchors, or outside R's four bullets, changed.
   - No lifecycle file changed.
5. **Containment.** Nothing under `_Decomposition/` other than `_LATEST.md` changed: no decomposition text, registers or `SOFTWARE_DECOMP.md`. Also unchanged: `docs/PRD.md`, any `ScopeOfWork.md`, any `_STATUS.md`, `v2/**`, `checkpoint_snapshots/**`, any other SCA-005 snapshot file and `_Evaluation/**`.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the generator and the checks. The manager runs the reliance preflights. One fresh read-only TASK is the verifier. T1 is a separate `task-management` invocation by WORKING_ITEMS, which may be the same instance, after the owner's answer to question 2. It may ride the same PR.
- **Run root.** `execution/_Coordination/CURRENCY_REV15_D95_{D}/`, in the default-writable fence, holds:
  - `gen_d95.py` (exact bytes) and its stdout report;
  - `verify_d95.py` and its output;
  - `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the PROJECT_SETUP closeout format;
  - the closure output;
  - the validator outputs and preflight results;
  - `VERIFIER_VERDICT_NN.md`.

  No `_run_records/` entry is written in any deliverable.
- **Records not opened.** `checkpoint_snapshots/**`; every SCA-005 snapshot file except the two named under A; `_Evaluation/**`, including the audit pointer; `docs/STATUS.md` and `README.md`, which stay with HELP_HUMAN under D-PEC-88.
- **MEMORY rows.** None are opened by this packet. The act changes metadata of 64 deliverables but performs no deliverable run. Whether the undertaking's closeout writes MEMORY rows for it is the graph's decision under `projects/pec/AGENTS.md` §"Deliverable records and loop ownership", which requires naming those paths in a governing packet.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for manager, author and verifier, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12 (Root `AGENTS.md`), with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** The generator writes nothing unless every check passes. If a later check fails, discard the branch or worktree; nothing reaches `origin/main`.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR of the act restores the 121 preimages tabled above, or the 119 under P. If T1 rode the same PR, the revert also restores `REGISTER.csv` `d350d007…799d` and `REGISTER_CLOSED.csv` `ea730ae0…afd94`. The act creates and deletes no file, so the revert removes nothing. History is preserved and no reset is made. The run root stays as non-current evidence, with a rollback note appended to its `HANDOFF_STATE.md`. No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + R, P or an amendment, grants none of the following:

- any `ScopeOfWork.md`, `v2/**`, `software-workflow.json` or `docs/PRD.md` write;
- any `_Decomposition/**` write other than `_LATEST.md`: no decomposition text or register content (`SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`);
- any `checkpoint_snapshots/**` or other SCA-005 snapshot write beyond the two appended notes (A only);
- any lifecycle change: no `_STATUS.md` is touched and no `## Remaining` entry is written;
- `CHECKING`, `ISSUED`, artifact acceptance, or any readiness or reliance claim. The owner reserves any CHECKING declaration to their own initiative, and this packet creates no prompt, gate or reminder about it;
- any `_CONTEXT.md` or `_REFERENCES.md` byte outside the N2 anchors, and outside R's four bullets if R is chosen;
- any `Dependencies.csv` cell other than `EvidenceQuote`, `LastSeen` and `Notes` of the 19 rows; any `_DEPENDENCIES.md` write; any row added, retired or deleted;
- an audit run or a pointer move under `_Evaluation/**`;
- a Task Management disposition. T1 happens only on the owner's answer to question 2;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- a schedule reading: blocker output stays advisory (`FULL_GRAPH`, threshold `INITIALIZED`).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, A + R, P, amend or defer.** Recommendation: **A + R**. R rewrites the four retired deliverables' "covers" bullet (finding 1). It goes beyond the brief's "semantic fields untouched"; A alone stays inside it.
2. **T1 — TM-PEC-023.** Confirm that TM-PEC-023 closes `RESOLVED_BY_DECISION` on the existing record: amendment-1 selections, the checkpoint-2-accepted plan §B8 (D-PEC-92) and the checkpoint-3 acceptance. Then WORKING_ITEMS applies the drafted row and archives it (recommended: **confirm**). The alternative is to dispose of it yourself differently. Without an answer, the row stays `OPEN` and nothing else waits on it.
3. **Re-audit.** None now; SCA-006's baseline will observe this state (recommended). Or add a re-audit, with the audit-pointer move on 0 BLOCKERs (amend).
4. **The human-owned `_COORDINATION.md` Notes line.** Include the one-line currency edit (recommended), or leave that section to you. Leaving it is an amend: the generator's Notes replacement is dropped and the packet is re-prepared.
5. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran in a fresh `mktemp -d` directory under the host's temporary area, outside the session scratchpad and the checkout:

- `base` is a `git archive` export of the whole tree at `13df8b795`. Its `projects/pec` equals a second fresh export byte for byte after all runs;
- each `proto*` is an APFS clone (`cp -Rc`) of `base` with a variant applied;
- `gitmeta` is a `git clone --shared --no-checkout` of the repository, detached at `13df8b795` in the scratch directory. It gives the git-dependent validators a history. It reads the repository's objects and writes nothing to the repository.

Interpreter: Python 3.13.7 (CPython); local date 2026-09-25 (MDT). Nothing was written to the checkout or its repository.

| Command (scratch) | Exit | Result |
|---|---|---|
| strict validator on `base` | 0 | 66 registers, 263 rows (ANCHOR 140 / EXECUTION 123), 0 errors, 0 warnings |
| closure on `base` | 0 | 111 edges, 66 nodes, 0 SCCs, 0 bidirectional; `closure_summary.json` `bd73806c…187a` (= the D-PEC-93 run root's) |
| quote-currency scan on `base` (ACTIVE EXECUTION) | — | 92/111 verbatim; the 19 non-verbatim equal COV-072's list exactly |
| `gen_d95.py` option A on `protoA` (`--act-date 2026-09-25`) | 0 | 124 READ, 121 WRITE; `CHECK active_execution_quotes_verbatim 111 111` |
| the same on a second fresh clone | 0 | report and tree byte-identical (deterministic) |
| option P on `protoP` | 0 | 119 WRITE; the SCA-005 files unchanged; only `_COORDINATION.md` differs from A |
| option A + R on `protoAR` | 0 | 121 WRITE; 4 reference postimages differ from A |
| option A at `--act-date 2026-09-26 --reproduction` | 0 | 15 files differ from the 2026-09-25 run, all in the slot loci only |
| rerun on the applied `protoA` | 1 | "preimage mismatch …/_Decomposition/_LATEST.md"; nothing written |
| `--act-date 2026-09-26` without `--reproduction` | 1 | "local date 2026-09-25 != --act-date 2026-09-26; nothing written" |
| `--check-only` on `base` | 0 | 121 RENDER; `base` unchanged |
| strict validator on A, P, A + R | 0 ×3 | 0 / 0; output byte-identical to `base` |
| closure on A, P, A + R | 0 ×3 | `closure_summary.json` byte-identical to `base` |
| schema validator on the 10 registers (A) | 0 ×10 | VALID |
| `verify_d95.py` on A, P, A + R | 0 ×3 | all checks PASS; the self-comparison of `base` fails as designed (exit 1) |
| `gitmeta`: option A via `--repo "$(git rev-parse --show-toplevel)"` | 0 | report hash columns identical to `protoA` |
| `gitmeta`: containment (`git diff --name-only` vs the write set) | — | equal, 121 paths |
| `gitmeta`: `git diff --check` | 0 | clean |
| `gitmeta`: `validate_pec_loop_receipts.py --repo-root .` before and after | 0 / 0 | output identical |
| `gitmeta`: `harness.py self-check` before and after | 0 / 0 | output identical |
| `gitmeta`: `validate_instruction_entrypoints.py .` | 0 | PASS (no instruction surface touched) |
| `gitmeta`: `t1_tm_pec_023.py`, then `taskmgmt validate` ×2, `archive`, `validate` ×2 (Task Management files first reset to `13df8b795`) | 0 / 0 ×2 / 0 / 0 ×2 | closed, archived; 9 live rows, 16 archived; a second run fails closed (exit 1) |
| `pec_reliance_hold.py … --operation exact-correction-preparation` from `base/projects/pec` | 0 ×123 | `ALLOW` |

Scratch artifacts in the preparer's `h9/` folder, listed with hashes in `h9/SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `gen_d95.py` (the bound generator) | `0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78` |
| `verify_d95.py` (postimage checks) | `fcf172b5aa2ec6179a5af541f1a01d68a0148590d3b3f6eafbf913e64bfb185f` |
| `t1_tm_pec_023.py` (T1 draft row) | `0e0cd6f94448005ecf17f564f35ef72a42f2c2862e97bc33256a3c701b957bec` |
| `build_gen_d95.py`, `gen_d95.template.py`, `run_prototypes.sh` (preparation aids) | `a67afc51…e438`, `c799ef0c…065e`, `a9fec935…6705` |
| `evidence/optionA_vs_13df8b795.diff` (option A at 2026-09-25) | `099e0ca339587feabc818e45c6e2b635efe7cacd81ed510c70d1fee6aec1b783` |
| `evidence/optionP_vs_optionA.diff`, `evidence/addonR_vs_optionA.diff`, `evidence/T1_vs_13df8b795.diff` | `26f5cba7…db6d7`, `438ece68…ab63`, `a6739110…ec1d` |

Basis read for preparation, at `13df8b795` unless stated:

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `1a13a5b0…c8fb7` / `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| D-PEC-93 proposal / ruling | `46470575625522398fa47d0a39aa09d2b4d252dd89c083ba317f9e577f489422` / `ffb0b58293d868e1d7ddf61d2958a6b18ca73fa0c36da077f5309a8782153709` |
| D-PEC-93 `gen_d93.py` / prep `gen_d93_b1.py` / run-root `HANDOFF_STATE.md` | `cfae0052…d6c2` / `eff5d2fb…677c` / `0887a9c92985c87f74a40fed16d3d0783c1178eb6dbab8adeee3651305cc4a06` |
| D-PEC-88 / D-PEC-94 / `_DECISIONS/_REGISTER.md` | `266a1411…fef5` / `eb9793aa…5e81` / `031adae37d3984c26545a21662d010b7377532aefefe79c5c7addeccca4ba2f7` |
| `COV_SCA005_POSTSETUP_2026-09-25_1606` `Decomp_Coverage_IssueLog.csv` / `RUN_SUMMARY.md` / `coverage_summary.json` | `3e93aaf3…5850` / `b3075137…6311` / `b7b432a2…128d` |
| `_Evaluation/DecompCoverage/_LATEST.md` | `2b43dc3bb34163ae51067f6176ebf235430b59aa668890c1e65d7cc9d3cf1450` |
| SCA-005 `Propagation_Plan.md` / `Amendment_Actions_CP2.csv` | `50cd0b1d…1350` / `7bb3bada…9987` |
| checkpoint `DECISION.md`: group-1 amendment 1 / group 2 / group 3; group-3 `ACCEPTED_MANIFEST.csv` | `4328633c…8f3013` / `ca88f6a8…3d66` / `35c211a6…f673`; `1eb20bc9…dc7` |
| `_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5) | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| Task Management `REGISTER.csv` / `REGISTER_CLOSED.csv` | `d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d` / `ea730ae06f0805c720bbb29aed6d681c323e6d3b0c4a38d53db27e1075fafd94` |
| `workflows/task-management/` `WORKFLOW.md` / `contract.md` / `method.md` | `db06263d…e9b` / `e1c97a76…c837` / `7f9e0d5e…e2f8` |
| `workflows/scope-change/resources/contract.md` (state-field values) / `docs/CONTRACT.md` (K-TM-3) | `4453a719…4d02` / `64747d2a…95bd` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d931…41cbc` / `b1712e4b…cd0e` |
| `tools/taskmgmt/taskmgmt.py` / `validate_decomposition_registers.py` / `validate_dependencies_schema.py` / `analyze_dep_closure.py` / `validate_pec_loop_receipts.py` / `practitioner_harness/harness.py` | `9c5cdc56…101` / `590d9aa3…8818` / `75cd7476…291f5f` / `fe546d0f…8ccd` / `8eb62995…bad9` / `01a9b954…61f3` |
| `D-T0-15_pec_loop_goal_fences.md` | `95c245b5…0b09` |
| Work graph (branch commit `87f6bfe30`, not on `origin/main`) | `f669ebe53d483419799e5c947ea903996187570e608f3ee2b849030c0ec00f78` |
| Brief H9 (scratch) | `02fb7370e835a165a3c36f4f044447b598828050c6e2a069a66f0fa8a84945a1` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, nodes N1–N3 and T1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
