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
  - The registry source packet (G1) has no predecessor and proceeds whenever it is ready. The derivative review and the fixtures come after SOW currency.
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

| Deliverable / basis | What existed at graph construction (2026-09-25) | What this undertaking changes | Nodes |
|---|---|---|---|
| Decomposition pointers and `_COORDINATION.md` (the SCA-005 handoff files stay unchanged under the P ruling) | Revision 1.5 accepted. The pointers still carry the pre-setup audit reading; `_COORDINATION.md` names revision 1.4 | Present-current text | N1 |
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
| N1 Records currency | Both `_LATEST.md` pointers; `_COORDINATION.md` present-current lines, item 14 and the human-owned Notes line. Under P the SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` stay byte-identical, and item 14 records them as superseded for current state (WORKING_ITEMS) | `D-PEC-95` ruled P + R | Texts match the live audit and revision; validators unchanged; review | COMPLETE — act merged as PR #924 (`abfd0897b`); run root `CURRENCY_REV15_D95_2026-09-25/`; both pointers and `_COORDINATION.md` current, SCA-005 handoff files unchanged |
| N2 Re-pin contexts and references to revision 1.5 | 42 `_CONTEXT.md` and 64 `_REFERENCES.md` anchor lines; add-on R also rewrites the four retired deliverables' "covers" bullet (WORKING_ITEMS) | `D-PEC-95` ruled P + R | Strict registers 0/0; every file names revision 1.5; review | COMPLETE — act merged as PR #924 (`abfd0897b`); run root `CURRENCY_REV15_D95_2026-09-25/`; 66/66 contexts and 66/66 references name revision 1.5 |
| N3 Evidence-quote refresh | 19 rows in 10 `Dependencies.csv` (WORKING_ITEMS) | `D-PEC-95` ruled P + R; exact new quotes verbatim in the cited files | Every ACTIVE EvidenceQuote verbatim; strict 0/0; closure unchanged | COMPLETE — act merged as PR #924 (`abfd0897b`); run root `CURRENCY_REV15_D95_2026-09-25/`; 111/111 active execution quotes verbatim; strict registers 0/0; closure `bd73806c…187a` unchanged |
| U1 Currency act PR | N1–N3 and T1: one `gen_d95.py --option P --retired-covers` run from run root `CURRENCY_REV15_D95_{D}/`, the proposal's verification and a fresh verifier, with T1 riding along (WORKING_ITEMS) | `D-PEC-95` ruling and register row on `origin/main` | PR merged after review and CI | COMPLETE — PR #924 merged as `abfd0897b`. Two verifier verdicts PASS WITH NOTES, no blocking finding. HELP_HUMAN re-checked: 115 postimages equal P, 4 equal R, 0 mismatch; containment is 119 product + 2 register + run root + return |
| R1 SCA-006 checkpoint 1: reliance amendment intake and impact | Snapshot folder `_ScopeChange/SCA-006_<date>/` only. It assesses PRD PEC-K-03, §8 (agents, access classes, direct query through tool calls), §9 reliance envelope and §12 release gate; response-size budgets; the `projects/pec/AGENTS.md` K-02 gloss; and the explicit list of affected SOWs and ADR/SPEC rows (WORKING_ITEMS, `scope-change`) | `D-PEC-90` R-A. Path basis: `D-PEC-90` grant item 3 ("prepare the exact PRD and `projects/pec/AGENTS.md` amendment as the next PEC scope change once SCA-005 checkpoint 2 is accepted"), whose precondition `D-PEC-92` met. *Interpretation:* like `D-PEC-86` for SCA-005, this covers writing the checkpoint-1 snapshot folder. Method: `chirality-root:bundled:workflow:scope-change` | Owner accepts checkpoint 1 | COMPLETE — owner accepted checkpoint 1 on 2026-09-25 (DQ a, ENV a, BUD a, GATE a, INS a, R-C excluded); snapshot `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`, pointer `_ScopeChange/SCA-006_GROUP-1_AUTHORIZED.md` |
| R2 SCA-006 checkpoint 2: exact amendment and propagation | PRD v2.4 candidate; the affected SOW and ADR/SPEC set fixed as exact rows (WORKING_ITEMS) | R1 accepted | Owner accepts checkpoint 2, which fixes the S4 set | ACTIVE — a WORKING_ITEMS manager is preparing the checkpoint-2 package under brief `briefs/B5_SCA006_CHECKPOINT2.md` (`142d6be0…efb4`), on branch `claude/pec-sca006-cp2-package`; returns go under `returns/B5_*` |
| R3 SCA-006 checkpoint 3: apply and audit | Lane A writes per the accepted plan (WORKING_ITEMS) | R2 accepted | Owner accepts checkpoint 3 | PLANNED |
| R4 Reliance notices | Root and App notices, per the `D-PEC-90` grant. A Runtime notice only if the checkpoint-2 plan names one (HELP_HUMAN) | R3 | Notices merged | PLANNED |
| S1 SOW currency: review class outside the S4 set | Review-class SOWs from SCA-005 §B4 that SCA-006 does not name as affected, plus the 5 housekeeping-only (pins, false revision-1.1 claims) (WORKING_ITEMS with REVIEW or artifact gates) | U1; the latest SCA-006 affected-SOW list (R1's, replaced by R2's once accepted), whose members stay out of S1; packet per batch | Each SOW validator-clean and reviewed | READY — packet preparation; U1 and R1 are met. The accepted §7.1 AFFECTED set (9) stays out |
| S2 SOW currency: rebuild class outside the S4 set | DEL-01-01, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07; DEL-01-06 after G1 (WORKING_ITEMS) | U1; R1 (the affected list, as for S1 and S3); packet(s); parser carry-forward (CON-001 cases for RETIRED, node states, run tokens). A member of the latest SCA-006 affected list moves to S4 | Same | READY — packet preparation for the six named; DEL-01-06 waits for G1 |
| S3 First SOWs for DEL-02-08 and DEL-02-09 | Their `ScopeOfWork.md`, via preparation → Scope of Work (WORKING_ITEMS) | U1; R1 (the affected list, as for S1 and S2); packet. S2's parser carry-forward context informs it, but S3 is not blocked on S2 | Same | READY — packet preparation; U1 and R1 are met |
| S4 SOWs whose quoted PRD text SCA-006 changes | The set that checkpoint 2 fixes. The accepted SCA-006 checkpoint-1 Impact Assessment §7.1 lists DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04 and DEL-04-03, with DEL-03-04, DEL-10-03 and DEL-00-03 AFFECTED at review level. §7.1 routes those three to "S1 or D1", but this graph holds them until R3 as well (DEL-00-03 through D1). That is a more conservative choice, and R2 records it. §7.1 classifies DEL-01-01, DEL-01-05, DEL-02-03 and DEL-01-06 NOT_AFFECTED. DEL-04-01 is a fixed member: the `D-PEC-90` proposal names its CLM-016/AX-007 as a locus, and grant item 1 bars rebuilding it around verify-before-rely. Other candidates, from a grep of the SOWs: quoting PEC-K-03 or verify-before-rely, DEL-04-02, DEL-08-01 and DEL-08-03; citing PRD §8, DEL-01-05, DEL-04-02, DEL-08-01, DEL-08-03 and DEL-08-04. (DEL-01-01, DEL-02-03 and DEL-04-03 cite `SOFTWARE_DECOMP.md` §8, not PRD §8. Checkpoint 1 classes DEL-04-03 AFFECTED anyway, for its scope growth.) DEL-04-02 is `current` under SCA-005 §B4 but is included because of CLM-016. A SOW that R2 drops from the R1 list returns to S1 or S2; a SOW that R2 adds after S1 or S2 processed it is reopened here (WORKING_ITEMS) | R3; packet, or the accepted checkpoint-2 propagation plan where it binds exact rows | Same | PLANNED |
| G1 Registry source packet | `v2/config/loops.json`, `loops.schema.json`, `RegisteredLoop` port and tests (WORKING_ITEMS) | Packet (F-PEC-1); VER-001/VER-003 rerun | v2 checks pass; review | ACTIVE — `D-PEC-96` is being revised to revision 3. Review 02 found option A fully reproducible and review 01 resolved, but the mutation runner crashes under A-R. Brief `briefs/G1_REGISTRY_SOURCE_PROPOSAL.md`; return `returns/G1_REGISTRY_SOURCE_PROPOSAL.md`. The accepted SCA-006 checkpoint 1 classes DEL-01-06 NOT_AFFECTED |
| D1 Derivative premise review | DEL-00-01 ADRs, DEL-00-03 SPEC (WORKING_ITEMS with owning workflows) | Packet binding exact bytes (outside default surfaces); after R3 for K-03 text | Owner rules the packet; premise-only amendments merged | PLANNED |
| X1 P1 fixture suites | DEL-02-03, DEL-02-08, DEL-02-09 fixture classes (receipt present, evidence-only, no AgentRuns record) (WORKING_ITEMS) | S2, S3 (and R3 if DEL-02-03 moves to S4); v2 packet (SCA-005 Propagation_Plan §B7) | Fixtures committed under the ruled packet | PLANNED |
| T1 TM-PEC-023 disposition | Task Management register row, which is default-writable (WORKING_ITEMS, `task-management`) | Owner disposition: `D-PEC-95` ruling ("confirm TM-PEC-023"), on the basis of the amendment-1 selections, the checkpoint-2-accepted §B8 (`D-PEC-92`) and checkpoint 3, as `task-management` and Root `docs/CONTRACT.md` K-TM-3 require. A TASK does not write the row | Row closed and archived on the owner's confirmation; `taskmgmt validate` passes | COMPLETE — closed `RESOLVED_BY_DECISION` and archived in PR #924; live register 9 rows (8 `OPEN`, 1 `DEFERRED`), archive 16 |
| I1 `AGENTS.md` residual corrections | `projects/pec/AGENTS.md` (HELPS_HUMANS) | Instruction tranche with manifest | Validators pass; notice | PLANNED — may ride R3's instruction change |
| C1 Bounded closeout | Affected deliverables and records (HELP_HUMAN) | All substantive PRs merged | `bounded-reconciliation` comparisons; warranted edits | PLANNED |
| M1 Record the run | Central `RECEIPT.md`; MEMORY rows named by the governing packets (HELP_HUMAN) | C1 | Receipt and rows written | PLANNED |
| F1 Final PR | Integrated undertaking (HELP_HUMAN) | M1 and all checks | Final PR merged | PLANNED |

**Order.**
- Done: U1 (with N1–N3 and T1), and R1.
- Active: G1 (`D-PEC-96` published for review) and R2 (SCA-006 checkpoint-2 preparation).
- Ready now: S1–S3 packet preparation.
- After U1 and R1: S1, S2 and S3. Their membership follows the latest SCA-006 affected-SOW list (R1's, replaced by R2's once accepted).
- After G1: DEL-01-06 in S2.
- After R3: S4, D1 and I1.
- After S2 and S3: X1.
- Then C1 → M1 → F1.

The dependencies are acyclic, and the named inputs, not this listing, decide when a node is ready.

**Carried from `D-PEC-95` preparation.**
- 11 active dependency rows cite a deliverable `ScopeOfWork.md`. The S packets reuse `gen_d95.py`'s quote-currency check, so that SOW work does not leave those quotes stale again.
- DEP-10-05-004's warrant is weaker after the refresh: its cited cell no longer names orientation reads. Moving its evidence to SOW-085 would change `EvidenceFile` and `SourceRef`, so it is left for a later dependency packet and was not prepared. The owner accepted the row as prepared (`D-PEC-95` ruling).
- SCA-005 Propagation_Plan §B1 counts "40" `_CONTEXT.md` files. The correct figure is 42 (COV-072 in the checkpoint-3 audit), which `D-PEC-95` uses.

**Carried from SCA-006 checkpoint-1 preparation (for R2).**
- New deliverables DEL-08-06 and DEL-10-13 (selected set) need PROJECT_SETUP and first Scope of Work contracts.
- The tier-0 profile `pec.yaml` L81 needs its own act before any PEC tool surface is declared or invoked.
- The `projects/pec/AGENTS.md` change is carried as an instruction tranche at checkpoint 3 (INS-a, selected); I1 may ride it.
- The manager recommends naming a Runtime notice in the checkpoint-2 plan (R4).
- SCA-006 Impact Assessment §2.1 says its audited inputs equal the pre-change state byte for byte. That stopped being exact when the `D-PEC-95` act changed 119 derivative paths. Three of those paths are also in SCA-006's `AffectedFiles`: DEL-04-03 and DEL-08-03 `_CONTEXT.md` (Seq 30, 32) and DEL-10-12 `Dependencies.csv` (Seq 54). But `D-PEC-95` changed only their anchor lines and DEP-10-12-003, so no text SCA-006 amends changed. R2 states this explicitly (group-1 `DECISION.md` baseline note).
- SCA-006's pre-change baseline, `COV_SCA005_POSTSETUP_2026-09-25_1606`, predates the `D-PEC-95` act, so it still carries COV-068/069/072/073. The first audit to observe the post-`D-PEC-95` state is SCA-006's post-change audit (R3). R2/R3 must not re-report those findings as SCA-006 effects.

## Current state and recovery

- **Checked basis:** `origin/main` `56a626c3b` (PR #927, which changed nothing under `projects/pec` after PR #926's `4d5f7b911`).
- **Next work:**
  - Review `D-PEC-96`, then bring it to the owner.
  - Receive the SCA-006 checkpoint-2 package (R2), then review it and present it.
  - Prepare the S1–S3 Scope of Work packets.
  - Each fenced packet comes to the owner to rule on.
- **Local or unmerged work:** this graph's sixth PR (branch `claude/pec-d96-registry-proposal`). It publishes `D-PEC-96`.
- **Active operations and ownership:**
  - The SCA-006 checkpoint-1 manager handed back (`returns/B4_SCA006_CHECKPOINT1.md`); its scratch helpers are named in the SCA-006 `Handoff_State.md` (not hashed, and not in the repository).
  - The U1 act manager handed back (`returns/U1_D95_CURRENCY_ACT.md`, brief `briefs/U1_D95_CURRENCY_ACT.md`); nothing is running from it.
  - G1: the read-only preparer's draft is published in the sixth PR. Review 01 (`returns/REVIEW_PR928_01.md`) sent it back for revision 2. Review 02 (`returns/REVIEW_PR928_02.md`) found an A-R mutation crash, so the preparer is making revision 3.
  - R2: a WORKING_ITEMS manager, brief `B5_SCA006_CHECKPOINT2.md` (`142d6be0…efb4`), in its own worktree on branch `claude/pec-sca006-cp2-package`. Returns go under `returns/B5_*`.
- **Graph maintainer:** HELP_HUMAN.
- **Earlier run:** `HELP-HUMAN-PEC-20260923-SCA005`, under PEC's former loop; its `RUN.md` is history. The owner's CHECKING reservation for DEL-01-03 stands, and nothing here prompts for it.

| Completed work / node | What changed and was checked | Unresolved consequence |
|---|---|---|
| Graph PR #919, review 01 | Review 01 blocked on SOW sequencing. Repaired: S4 is gated on the SCA-006 affected set, DEL-04-02/08-01/08-03 are added as candidates, and DEL-01-06 is relabelled as waiting on G1. Seven non-blocking findings also repaired. Transcription: `returns/REVIEW_PR919_01.md` | None: review 02 passed at `ae4ddc447` (`returns/REVIEW_PR919_02.md`), and PR #919 merged as `7562c4434`. Its non-blocking findings are fixed in this graph's second PR |
| `D-PEC-95` preparation (N1–N3, T1) | TASK draft, generator and prototype evidence published. Brief `briefs/H9_D95_CURRENCY_PROPOSAL.md`; return `returns/H9_D95_CURRENCY_PROPOSAL.md`. The generator's check-only run on `bec8bdd65` passed, with no preimage drift | Resolved: PR #921 merged as `325629882` after review 01 PASS (`returns/REVIEW_PR921_01.md`), and the owner ruled P + R. Review 01's findings 3, 4, 5 and 7 are repaired in this graph's third PR; findings 1, 2 and 8 went to the owner with the presentation |
| SCA-006 checkpoint-1 package (R1) | Six snapshot files under `_ScopeChange/SCA-006_2026-09-25_1912/`: 54 PROPOSED actions, and all 32 SOWs classified (9 AFFECTED). Verifier PASS on round 03; PR #922 merged as `b1145955e`, with branch updated and package bytes unchanged. The owner accepted it 2026-09-25 (recommended set) | R2 checkpoint-2 preparation |
| U1 currency act (N1–N3, T1) | PR #924 merged as `abfd0897b`. 119 P + R paths byte-identical to the tabled postimages; TM-PEC-023 archived; strict registers 0/0; closure unchanged; verifier PASS WITH NOTES ×2 (run root `VERIFIER_VERDICT_01.md`, `_02.md`) | None |
| SCA-006 checkpoint-1 acceptance record | PR #926 merged as `4d5f7b911`. Group-1 snapshot and pointer; reviews 01 FAIL, 02 FAIL and 03 PASS, with every finding repaired (`returns/REVIEW_PR926_0{1,2,3}.md`) | None |

## Owner-direction evidence and D-PEC-88 trace

- 2026-09-25, owner, verbatim: "re: D-PEC-88 confirmed yes it carries over". This confirms the carry-over that `D-PEC-94` recorded as HELP_HUMAN's interpretation. The record of this act is the owner-confirmation section added to `D-PEC-94` in this graph's first PR.
- 2026-09-25, owner, verbatim: "D-PEC-95: P+R (don't append); accept 10-05-004 as prepared; confirm TM-PEC-023; no re-audit; include; defaults". The record is `_DECISIONS/D-PEC-95_RULING_2026-09-25.md`.
- 2026-09-25, owner, verbatim: "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded". HELP_HUMAN's account: the act followed HELP_HUMAN's explanation of the DQ (a)/(b) implications, which the owner asked for. The record is `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md`.
- STATUS/README changes made under `D-PEC-88` in this undertaking are listed here and carried into the central receipt at closeout:
  - First PR: `docs/STATUS.md` now points the open-work paragraph at this graph.
  - First PR, review repair: the `docs/STATUS.md` SCA-005 paragraph heading no longer calls SCA-005 active.
  - Second PR: that heading is re-wrapped, and the owner-gates list names `D-PEC-95` as awaiting ruling.
  - Third PR: the `docs/STATUS.md` owner-gates list records the `D-PEC-95` P + R ruling and SCA-006 checkpoint 1 as awaiting the owner. The STATUS and `README.md` reliance paragraphs now name SCA-006 as the amending scope change. The STATUS pointer sentence now says the `D-PEC-95` act updates the pointers and `_COORDINATION.md`, and that the SCA-005 handoff files stay as accepted.
  - Fourth PR: the `docs/STATUS.md` owner-gates list records the `D-PEC-95` act as done and lists what stays open. The Task Management paragraph records TM-PEC-023 closed, with 9 live and 16 archived rows. `README.md` records the revision-1.5 re-pin and the TM-PEC-023 closure.
  - Fifth PR:
    - `docs/STATUS.md` records the SCA-006 checkpoint-1 acceptance, in the owner-gates list and the reliance paragraph.
    - It corrects the SOW-037 / DEL-07-04 sentence to past tense (SCA-005 applied).
    - It annotates the TM-PEC-023 historical sentence with the closure.
    - `README.md` records the checkpoint-1 acceptance and rephrases the SCA-004 closeout sentence (PR #925 review 01, findings 1, 2 and 8).
    - Review repair (PR #926 review 01): STATUS and README say checkpoint-2 preparation is "authorized", not "in preparation". STATUS names SCA-005 in the "Checkpoint 2 carried a note" sentence.
  - Sixth PR: the `docs/STATUS.md` owner-gates list names `D-PEC-96` as awaiting ruling.
