# SCA-005 checkpoint 1 — resolutions from the repository (HELP_HUMAN, 2026-09-24)

Prepared after the owner asked whether the checkpoint-1 question set could be
answered from the repository rather than handed over as open choices. Filed in
the run record (D-PEC-86 §4 opens `AgentRuns/**`); the SCA-005 snapshot
`Decision_Log.md` points here and is otherwise unchanged in substance. Each
item below cites the accepted source that decides it. This note changes no
hash of `Impact_Assessment.md` or `Amendment_Actions.csv`; it narrows what
the owner is asked. Owner acceptance of checkpoint 1 (CP1-A / CP1-B) remains
the workflow's human checkpoint and is not inferred here.

## A. Decided by an accepted source (owner ratifies with CP1-B; no separate choice)

| # | Resolution | Deciding source |
|---|---|---|
| Q1 | **O-B2.** A grammar must be *declared* per loop: DEL-02-03 OUT-001 requires "the grammar declared for that loop"; `adapter.yaml` is "Harness configuration authority only" (its own header) and is not PEC-owned, so O-C cannot carry PEC declarations; convention detection (O-A) makes coverage limits guesswork against PEC-ORI-006; D-PEC-78 O-A (owner verbatim: "D-PEC-78: O-A") confirmed, in the ruling record's words, the PEC-owned registry as "the long-term home and shape of PEC's service registry" for "which loop locators it chooses to serve". B2 over B1 because the registry stays strict and small (D-PEC-78: "Schema version 1 remains strict and versioned"). | DEL-02-03 SOW; `_harness/adapter.yaml` header; D-PEC-78 ruling §"D-PEC-78: O-A" |
| Q2 | **(b)** follows from Q1: `adapter.yaml` stays a parity-peer input only; DEL-02-07 is re-purposed, not removed, because the harness parity leg (SOW-020, DEL-03-04) still needs its `status_glob` population. | Q1; DEL-03-04 SOW TBD-003 |
| Q3 | **P-β.** P-α fails the no-second-execution-loop boundary and, under A2, sees no other application's sessions ("Do not point a new consumer at the running Chirality App's socket"). P-δ would drop PKG-06's Git-worktree half, which needs no Runtime and serves PRD outcome 3 and the D-PEC-57 intent. Deferral with the design note's three-part trigger keeps PEC-K-01 and PEC-K-03 intact. | Runtime `APPLICATION_CONSUMER_GUIDE.md`; D-GOV-20 / D-PEC-56 surviving behaviour 4; D-PEC-80 D owner-intent record; design note §5.3 |
| CP1-R | **R1** in the ledger's existing form: `OUT` with a bold `**Deferred**` note is the accepted convention (`**Deferred**, not permanent` on SOW-074 and SOW-086; `**Deferred**:` on SOW-090 and SOW-091). Retiring DEL-06-04 / DEL-07-02 / DEL-07-05 follows the scope-change contract's non-destructive rule (folders kept, `_STATUS.md` marked `RETIRED`) and is executed only at Gate 5 under the propagation plan. | `ScopeLedger.csv` rows 82–85; `workflows/scope-change/resources/contract.md` §Non-negotiable invariants |
| Q4 | **(a).** The shared method itself says completion is established from Git: "Its candidate records readiness and the PR URL; later Git/PR evidence establishes the actual merge" and "Do not require a later commit solely to write the final merge result back into its own candidate." Node IDs, states and PR numbers are identity and state, inside PEC-K-10; graph prose is not read. | `workflows/construct-local-work-graph/WORKFLOW.md` §3–4; PRD PEC-K-10, §7.1 DecisionRow |
| Q5 | **(a).** PRD §12 fixes P1 to "PEC's own build graph" and says "Generality is tested against a structurally different loop after self-ingestion"; live App/Piping ingest at P1 would contradict the accepted phase. Pinned fixture suites in three classes (receipt present; evidence-only; no AgentRuns record) test the parsers without a second live loop. | PRD §12 P1 row and closing paragraph; OI-010 |
| Q6 | **Re-express as premise, decision open.** PRD §16 is titled "Open product decisions (owner)": a scope change amends the decomposition and may not rule them; PRD §16 also records that "None of these blocks P0–P2", so leaving them open costs nothing. The PRD successor candidate states the changed premise (no daemon; no shared token registry; three validated ledgers) and each decision stays open for its own ruling. | PRD §16 heading and closing line; D-GOV-43 notice ("PEC revises its own text under its own instruments") |
| Q7 | **(b)**, an ordinary method choice attributed to the agent: graphs are committed on branches early in a PR sequence, so in-flight state lives on unintegrated refs; reading them by default would present unintegrated candidates as loop state. Default to the integration ref; local refs opt-in and labelled. | construct-local-work-graph §4; PEC-K-04 staleness by SHA |
| Q8 | **(a).** D-PEC-86 I-7 defers PEC's own migration; PEC's `LOOP_INIT.md` still selects from `## Remaining`, so its registry row declares the shape it actually writes. | D-PEC-86 §3 I-7; `projects/pec/loop/LOOP_INIT.md` §4 |
| Q9 | **Neither (a) nor (c): no change to SOW-058; drop Seq 72.** The accepted baseline method defines the unit as "one PEC loop-iteration orientation" with a "PEC-loop-only" population and excludes App and Piping by design; PRD §11 metric 1 compares pre-P1 with post-P1 on that unit. DEL-10-01 is `CHECKING` on that basis. Measuring shared-method loops is a *new* P2 measurement, not an amendment of SOW-058; if wanted it enters as its own item later. | DEL-10-01 `STEP0_COST_BASELINE_METHOD.md` §§1–2; PRD §11; D-PEC-72 acceptance |
| Q10 | **(a), and no PRD exit-test change.** The accepted P1 exit already reads "Parity-diff vs harness clean **or explained**". The harness observes `projects/pec` only through `self-check` (its `OBSERVABLE_PROJECTS` excludes PEC), so the P1 parity leg is `self-check` facts plus an explained census absence; that satisfies the accepted wording. The census leg over App/Piping arrives with P2 dashboards without rewording P1. | PRD §12 P1 row; `tools/practitioner_harness/harness.py` line 103; DEL-03-04 TBD-003 |
| CP1-D79 | **(b).** The D-PEC-79 handoff says any different byte "requires a successor candidate and another exact owner gate", and the ruling says application needs "authority that is separate from this preparation-only tranche". Both paths need an owner act; one successor v2.3 candidate at checkpoint 2/3 is one exact gate instead of two, and the adopted bytes remain the historical exact input. | D-PEC-79 `HANDOFF_STATE.md` §Adopted exact artifacts; `OWNER_RULING_2026-08-09.md` §Next gate |
| CP1-X | **ADD new DEL-02-08 / DEL-02-09; central receipts stay in SOW-013 / DEL-02-03.** The decomposition standard's artifact-kind granularity separates a Markdown graph parser from the JSON run-evidence and dependency-register parsers; DEL-02-04 and DEL-02-05 are `S` envelopes and DEL-02-03 is already `L` with a split warning in `ContextBudgetQA.csv`. | `docs/DECOMPOSITION_STANDARD.md` package-role rules; `Deliverables.csv`; `ContextBudgetQA.csv` DEL-02-03 |
| CP1-N | **Retain** IDs, names and paths (`ALLOW_RENUMBERING = false`; SCA-003 and SCA-004 precedent); label drift is recorded in each MODIFY description and any rename is a later PROJECT_SETUP act. | SCA-004 `Brief.md` parameters; scope-change contract |
| CP1-V | **Within D-PEC-78; no supersession.** The ruled option O-A itself prescribes the path: "Adding, removing, or changing a field's meaning requires a new schema version and a successor D-PEC migration packet. Version 1 is not silently widened." A strict, versioned schema v2 carrying feed profiles is exactly that new schema version with its own later D-PEC packet, which the Impact Assessment already records; the ruling's "Schema version 1 remains strict and versioned" is preserved. | D-PEC-78 `PACKET.md` §4.2 (ruled option O-A); ruling text |
| CP1-O | **OBJ-001;OBJ-002.** All seven existing PKG-02 parser deliverables carry exactly that set. | `Deliverables.csv` DEL-02-01..07 |

## B. Still the owner's, and why

| # | What remains | Why it cannot be resolved from the repository |
|---|---|---|
| CP1-A / CP1-B | Confirm the parsed change set and accept `Impact_Assessment.md` at SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`, with the Section A resolutions as the selected options (Seq 72 dropped at checkpoint 2). | The scope-change contract makes checkpoint 1 a human checkpoint by construction. |
| CP1-TM | TM-PEC-023 row selections, reduced from nine to seven live choices: Rows 4 and 7 (DEL-07-02, DEL-07-05) become moot under R1 because retired deliverables leave the union invariant. Row 3 (DEL-05-01) remains a choice, but its mapping option OBJ-004 is the only `DIRECT_ACCEPTED_LINK` on the surface, alongside its NONMAP and owner-replacement options. Rows 1, 2, 5, 6 carry only `INDIRECT_SUPERSESSION_CANDIDATE` mappings against a calibrated NONMAP whose rationale mirrors the decomposition's own recorded abstention; Rows 8 and 9 include `NEW_OWNER_ATTRIBUTION` options. Recommended selections per row will be presented at checkpoint 2 using mechanic M1 (mapping-notes table, no schema change). | The owner ruled on 2026-08-03: "every selection is mine to make in that session." and the surface states "No option is selected … A mapping is not valid merely because it appears". Preparation may recommend; it may not select. |

Everything in Section A is an agent resolution grounded in an accepted source;
if the owner reads any source differently, the Impact Assessment §12 delta
tables already carry the alternative action sets.

## C. Companion: the DEL-01-03 obligations, triaged the same way

Not part of SCA-005, but returned to the owner in the same slate. Triage record:
`execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/OBLIGATION_TRIAGE_DEL-01-03.md`
(SHA-256 `cc30ec4d954a7703a3b8e4f318f57331a1be6031488f55e67a1fa7bce6f19960`). Of 32 obligations: 6 are answered by the repository as it
stands, 9 are settled by an existing ruling or contract, 13 collapse into eight
bounded repairs of the merged D-PEC-85 slice (one live defect, O-2-2, plus
accounting, test-identity and evidence gaps), and 4 reduce to two owner
choices (how the three inquiry rows are closed; the acceptance route for the
slice). The eight repairs are drafted as proposal
`_DECISIONS/D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md`
so the owner rules on a package, not a list.
