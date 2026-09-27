# D-PEC-103 — First Scope of Work contracts for DEL-08-06 (agent tool-call query surface) and DEL-10-13 (reliance-advertisement gate) — proposal

Status: **DRAFT PROPOSAL / AWAITING_RULING**. **The number D-PEC-103 is provisional.** It becomes final only when HELP_HUMAN publishes this packet in `_DECISIONS/` with its register row. At `origin/main` `947075c9a` the register's last row is `D-PEC-101`.

Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN for the PEC loop, 2026-09-26 (session date):
- undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node K2;
- brief `briefs/K2P_FIRST_SOWS_PROPOSAL.md`, SHA-256 `5fcc3ef847d95743db804263410e360c070d87c0e7d5ff9ed49432c42d8ee133`;
- HELP_HUMAN's relayed directions of the same day, quoted under Provenance.

No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every check ran on `git archive` exports. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-103_first_sows_del_08_06_10_13_proposal_2026-09-26.md`.

**The act.** Create two new files with the exact bytes tabled below:
- `DEL-08-06/ScopeOfWork.md`;
- `DEL-10-13/ScopeOfWork.md`.

One bound script does this in one run, with no lifecycle change.

**Separate owner options:**
- add-on S, the `OPEN → INITIALIZED` status act (question 2), offered and not assumed;
- add-on M, `MEMORY.md` at closeout (question 3);
- add-on C8, the owner's constraint C-08 classification of DEL-10-13 (question 4). It writes a human-owned section and applies only on the owner's explicit selection.

## Provenance

- **Owner acts relied on.**
  - **Steering.** The owner's 2026-09-25 steering, recorded in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…5a6b`): "You can continue with all the open work you identified." The work graph turns it into node K2, "First SOWs for DEL-08-06 and DEL-10-13" (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`: `8296ad0c…b148` at `125cfacc1`; row `READY` at `947075c9a`).
  - **SCA-006.**
    - Checkpoint 2 (`D-PEC-97`, 2026-09-25) accepted `Propagation_Plan.md` (`f95d00d1…d7d8`). Its §B4 says: "New contracts: DEL-08-06 and DEL-10-13 receive first Scope of Work contracts after B1." Its §B6 places the tier-0 profile act "After DEL-08-06's first Scope of Work fixes the tool's shape".
    - Checkpoint 3 (2026-09-26) made decomposition revision 1.6 `current_basis` with PRD v2.4.
  - **`D-PEC-101`** (ruled "K4 with C; K1; V; Notes a; defaults", 2026-09-26; act merged in PR #976 at `ce934ac33`) created both folders at `OPEN` with their registers. Its findings 2, 3, 4 and 7 bear on this packet (see Findings).
  - **Precedents.**
    - `D-PEC-98` (ruled A + S + M): two new first contracts, a bound script, a fresh verifier, and add-on S on the `D-PEC-63` §3.2 pattern.
    - `D-PEC-100` (ruled A + B confirmed + M): the exact-bytes replacement pattern, pinned tree quotations, sibling-ID checks and the run-root guard.
- **HELP_HUMAN directions (relayed 2026-09-26; recorded here as evidence, not as rulings).**
  - "Add-on C8 is acceptable as an owner option: state plainly that the Tracking Mode section it writes is human-owned, so it applies only on the owner's explicit selection, and keep the contract true under either answer. Add-on S offered, not assumed; add-on M at closeout. List every qualified ID your candidates cite from S4/S1 targets (DEL-08-01, 08-03, 04-01, 04-03, 03-04, 04-05, 10-02) so those packets can keep them."
  - It also confirmed `origin/main` `947075c9a` or later as the check base.
  - The brief: the owner defers adopting `scope-of-work` `MODE=REVISE` in PEC, so adoption is not put to the owner.
- **Fence.** `projects/pec/AGENTS.md` (`df9196d1…5eb8`) §"Write Scopes And Fences" requires an owner-ruled D-PEC packet, naming exact paths, acts, verification and rollback, for every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the STATUS pointer. No earlier ruling opens the two targets.
- **Source state.**
  - Observation commit **`125cfacc1`** (`125cfacc10f664685cb91802a9166b1041f42a25`, the PR #979 merge, `origin/main` when preparation began). Both candidates say that every unanchored state claim is an observation there, and every tree quotation is read there.
  - Frontmatter pin **`189f205ff02df4111b33c20be441ce06e65ada7a`**, the SCA-006 checkpoint-3 acceptance commit and an ancestor of `origin/main`. These five files are byte-identical at the pin, at `125cfacc1` and at `947075c9a`: `SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv` and `docs/PRD.md`.
  - Checked again at **`947075c9a2164ab3f047c2019ce2d82719f25de7`** (PR #981 merge). Between `125cfacc1` and it, only the undertaking `WORK_GRAPH.md` and `returns/REVIEW_PR981_0{1,2,3}.md` changed in `projects/pec`, `_DomainEngines`, `tools`, `workflows` and `docs`. None is pinned.
  - All 17 pins of the act script hash as tabled at `947075c9a`. The checks ran on the branch head `6608f56a5`, which merges `947075c9a`.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`) was run from `projects/pec` with `--operation exact-correction-preparation` on all seven possible targets: both `ScopeOfWork.md`, both `_STATUS.md`, both `MEMORY.md`, and DEL-10-13 `_DEPENDENCIES.md`. Result: `ALLOW`, exit 0, ×7 (`evidence/run_main/reliance_hold_preflight.out`).

## Method

- **Workflow.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`2bfa2c5f…dafb3`). Precedence is project → user → bundled, and no project or user workflow of that name exists.
  - Files: `WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`, `resources/checks.md` `44ab41ac…f188`, `resources/tools.md` `fbd07771…6cc5`. `resources/representation-migration.md` (`698957a5…3e3c3`) was not loaded.
  - Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`, ratified by D-GOV-16: "New deliverables use `SOW_V1`".
- **Mode.** `MODE=INIT` (no production contract exists for either deliverable), `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, `RENDER_HTML=false`. There is no evidence candidate, map, parity or finalizer. The authored contract is the production contract, and `MODE=VERIFY` is the independent check.
  - `preparation` is not re-run: `D-PEC-101` created both folders with the `preparation` skill scaffold.
  - Disclosure (one line): Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` (`8829ac84…64af`) added `scope-of-work` `MODE=REVISE`; the owner defers adopting it in PEC, and it is not relevant to a first contract.
- **Actors.**
  - Two Type 2 TASK drafters, one per deliverable, under `K2_DRAFTER_BRIEF.md` (`aefa51fafa07ed250fa161f10ac3f8d76e686164be8662916355562f8073aa40`, in this folder). Each wrote its candidate and its quote and claim files, and ran the self-checks.
  - WORKING_ITEMS wrote the brief, the verifiers, the act scripts and tests, and the add-on postimages. It integrated the drafts, bound the hashes and ran the checks.
  - Fresh read-only `pec-reviewer` TASKs ran `MODE=VERIFY` on each candidate and the packet review (`VERIFIER_VERDICT_NN.md`).
  - Models: Opus 5.5 (`claude-opus-5-5`) at `high` for every actor, per the brief.
- **Drafting rules** (the drafter brief).
  - Ground every definition in the register rows and PRD v2.4 text they cite.
  - Decide nothing the registers leave open: mark it `TBD` or `CON`.
  - Do not ground requirements on the current wording of contracts that the parallel S4 and S1 packets are revising.
  - Cite no other contract's local ID unless necessary.
  - Quote no text from the prior S2 contracts.
  - Pin every tree quotation to `125cfacc1`, and anchor every state claim to a named commit.
- **Tools** (`tools/scope_of_work/`, unchanged at `947075c9a`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py` `61a34722…0389`.

## What preparation found

### Lifecycle

- **Both deliverables are `OPEN`** at `125cfacc1` and at `947075c9a`: `_STATUS.md` `73e21846…2511` for DEL-08-06 and `c7a5705d…543b` for DEL-10-13. Each has one history line, "State set to OPEN (TASK+preparation)", from `D-PEC-101`. Neither is `CHECKING` or `ISSUED`.
- **The method never touches `_STATUS.md`.**
  - `WORKFLOW.md`: "Do not modify `_STATUS.md`, lifecycle state, underscore control files, …".
  - `checks.md` item 3: "`_STATUS.md` is byte-identical and its lifecycle state is unchanged".
- **What the standard and project-setup say.**
  - Standard §8: "`INITIALIZED` means that the deliverable's selected production contract exists and validates".
  - `project-setup`: recording `INITIALIZED` "is a separate authorized status act".
  - So writing a first contract makes each deliverable *eligible* for `INITIALIZED`, and nothing more.
- **No transition is assumed.** Option A changes no lifecycle state; the act script pins both `_STATUS.md` files. Add-on S (question 2) is the explicit, separate question, as in `D-PEC-98`.
- **Consequence without S.** Both deliverables stay `OPEN`, each holding a valid `SOW_V1` contract.

### The candidates

| | DEL-08-06 Agent tool-call query surface | DEL-10-13 Reliance-advertisement gate |
|---|---|---|
| Scope item / objective | `SOW-099` / `OBJ-001` (a mapped scope item of OBJ-001, DL-21) | `SOW-100` / `OBJ-001` (listed as an *instrument* of OBJ-001 in §3; stated no more strongly) |
| Type / envelope / phase | `BACKEND_FEATURE_SLICE` / M / P3; MEDIUM risk, coupled to OI-006 | `TEST_SUITE` / S / P1; LOW risk |
| Defined IDs | OUT 3, CLM 16, REQ 16, AC 17, VER 16, AX 13, TBD 8, CON 4 | OUT 2, CLM 16, REQ 18, AC 19, VER 18, AX 12, TBD 7, CON 4 |
| Outputs | tool definitions over the read API; the `agent` access-class binding; tests (the register's three-part artifact list) | the gate harness; the gate record (the register's "Gate harness + gate record") |
| Checklist items | 17 | 19 |
| Quotes / claims checked | 61 / 147 | 72 / 332 |
| Size / SHA-256 | 249 lines, `31d0aa6e9d77e345b1c7178acde16fbb099d510500130e58aafdbdd60212d036` | 252 lines, `23f6505e8832cea2212f64c61020fa4ec2f390822f0a9a3baf997285eefff182` |

Both follow the form of the most recent first contracts (`DEL-02-08`, `DEL-02-09`):
- the same frontmatter keys and the six required headings;
- "Identity of record / Placement in the work graph / Boundaries";
- REQ → AC → VER one-to-one;
- one acceptance criterion per matrix row;
- a closing `HUMAN_REVIEW` criterion for objective traceability and scope non-absorption.

**What the contracts require, in brief.**

- **DEL-08-06.** The contract fixes the tool's shape at contract level, which is what SCA-006 §B6 needs before the tier-0 profile act (K3):
  - **inputs:** only the query kinds the `agent` class admits (orientation, deltas, gate verdicts, decision-slate and presence reads), with the API's own parameters (REQ-001);
  - **outputs:** the versioned API response unchanged, with its citations, stamps, limitations, truncation statements, continuation and reliance envelope (REQ-002);
  - **paths:** PEC's own store only, through the versioned API (REQ-003);
  - **mode and side effects:** read-only, none (REQ-004);
  - **failure:** the file-fallback signal, and never silence as a claim (REQ-005);
  - **result schema:** the API's, versioned additively (REQ-006);
  - **human gates:** enabling is consumer-owned, and no tool is declared or invoked before the tier-0 act is effective (REQ-007);
  - **binding:** `agent`-class only, with no escalation (REQ-008);
  - **also:** labelling (REQ-009), graceful absence (REQ-010), pull only (REQ-011), content-minimal (REQ-012), locality (REQ-013), and boundary exclusions (REQ-014, REQ-015).
  - It chooses no token mechanism, harness, App or agent configuration, and declares or invokes nothing.
- **DEL-10-13.**
  - **One evaluation per candidate:** a harness that, for one release candidate and the scope it serves, evaluates the five PRD §12 conditions over evidence produced by their owners (REQ-001):
    - parity (DEL-03-04), clean or each difference explained by a recorded DriftFinding disposition (REQ-002);
    - coverage honesty under seeded unparseable and stale feeds (DEL-04-05; REQ-003);
    - the reliance envelope (DEL-04-03 under SOW-097; REQ-004);
    - the fixture suites of the PKG-02 deliverables its ACTIVE rows name (REQ-005);
    - the kill test (DEL-10-02; REQ-006).
  - **Composition only:** the harness composes evidence and implements none of the producing behaviours (REQ-007).
  - **Candidate binding and verdict:** evidence is bound to the exact candidate, and absence counts as not passed (REQ-008, REQ-009).
  - **The gate record:** it carries the references and verdict (REQ-010) and is deterministic (REQ-011). It declares itself evidence for a release act: it is not the advertisement, the release, an acceptance or a ruling, and it is never citable as authority (REQ-012).
  - **Invocation and duties:** the harness is invocable by a release act and performs none (REQ-013), and it creates no consumer duty (REQ-014).
  - **Exclusions:** boundary exclusions (REQ-015); no C-08, register or lifecycle write (REQ-016); writes only its own records (REQ-017).

**Open matters recorded, not decided.**

| Contract item | What is open | Where it resolves |
|---|---|---|
| 08-06 TBD-002 | Token mechanism and `agent` credentials (OI-006, PRD §16.6) | the §16.6 owner ruling; delivered through DEL-08-01's access path |
| 08-06 TBD-007 | Content of the tier-0 profile entry | the K3 tier-0 act (after this contract, before any tool is declared or invoked) |
| 08-06 TBD-008 | Transport / any loopback listener | §16.9 (OI-009 / SOW-083) |
| 08-06 CON-001 | The DEL-08-01, DEL-08-03 and DEL-04-01 contracts predate SCA-006. DEL-08-01's delivers exactly owner, harness and admin, so REQ-008 has no conforming upstream contract until S4 | S4 rebuilds; ordering is the graph's and owner's |
| 08-06 CON-002 | Whether authoring tool definitions as source and exercising them in PEC's own tests before K3 counts as "declared or invoked" | owner, at K3 or in the production packet |
| 08-06 CON-003 | Dependency coverage: the `agent` class also admits deltas, gate verdicts, decision-slate and presence reads, which have no edges; `D-PEC-101` finding 3 left the DEL-04-03 edge as an amend | the dependency-register owning workflow |
| 08-06 CON-004 | Whether gate-verdict, decision-slate and presence responses carry the reliance envelope | under DEL-04-03, DEL-08-03 and the API schema |
| 10-13 CON-001 | The C-08 standing-node classification: "not made at `125cfacc1`"; every requirement holds under either answer | owner classification (question 4, add-on C8) or a later instrument |
| 10-13 CON-002 | Whether DEL-02-07's suite is among "the PKG-02 parser fixture suites" (`D-PEC-101` finding 2). REQ-005 composes what the ACTIVE rows name at evaluation time, so it holds either way | an owner-ruled dependency-register amend |
| 10-13 CON-003 | The contracts of DEL-03-04, DEL-04-03, DEL-04-05 and DEL-10-02 predate the gate; DEL-04-03's lacks SOW-097. Missing evidence counts as not passed | S4 and S1; ordering is the graph's and owner's |
| 10-13 CON-004 | No accepted release process for PEC v2, and no defined act of "advertising". The contract's reading that release and advertisement are the owner's acts is labelled an interpretation | owner, before any reliance-advertising release |
| TBD (others) | ResponsibleParty; tool-definition representation; operation mapping; numeric budgets (Phase 1); fallback representation without a response (08-06). Release-candidate identity and scope; evidence-access method; gate-record form and location; DriftFinding-disposition owner; seeded-case set; "every response" extent (10-13) | production within the REQs, or the named owner |

### Qualified IDs cited from contracts under parallel revision (for the S4 and S1 packets)

- **None.** Neither candidate contains a qualified citation `DEL-NN-NN/PFX-NNN` of any other contract. `check_cited_ids.py` reports `RESULT PASS 0/0`, and neither candidate cites the other's local IDs.
- **The S4 and S1 packets have no local ID to keep for K2.**
- The candidates do read those contracts as **observations at `125cfacc1`**, anchored by hash. These stay true after S4 or S1 rewrites them, because each names its commit:

| Candidate | Contract read (node) | What it records at `125cfacc1` |
|---|---|---|
| DEL-08-06 | DEL-08-01 (S4) | SHA-256 prefix `8ac1dc050efb`; quotes "The delivered access-class set shall be exactly owner, harness, and admin" (Q34); does not contain "`agent` access class" (CON-001) |
| DEL-08-06 | DEL-08-03 (S4), DEL-04-01 (S4) | SHA-256 prefixes `013c615a0c91`, `6f4e8c66a571` |
| DEL-10-13 | DEL-03-04 (S4), DEL-04-03 (S4), DEL-04-05 (S1), DEL-10-02 (S1) | SHA-256 prefixes `e007f5307fce`, `6ec7432bf8cf`, `933c012cf16b`, `99730e4e85ce`; none contains "reliance-advertisement", "DEL-10-13", "SOW-100", "SOW-097" or the `189f205ff` pin (CON-003) |
| DEL-10-13 | DEL-10-02 (S1) | quotes "No accepted source establishes a release process, pipeline, or CI system for the PEC v2 build" (Q37; CON-004) |
| DEL-10-13 | DEL-02-07 (S2, applied) | quotes two current `D-PEC-100` postimage phrases (Q55, Q56); prefix `3d1220872c55` |

Neither candidate names DEL-08-02, DEL-08-04 or DEL-10-03 other than by deliverable ID and register text. DEL-08-02 is read only and nothing in this packet prompts about its lifecycle.

### D-PEC-100 currency and external anchors

- **Old S2 text.** `scan_old_s2_text.py` compares against the prior S2 contracts at `ce934ac33` (the `D-PEC-100` preimages) and the current ones at `125cfacc1`. It finds `stale=0`, and 43 spans that match current S2 postimage text (`evidence/run_main/scan_old_s2_text.out`). One of DEL-08-06's drafting phrases matched text D-PEC-100 had dropped from DEL-02-06; the drafter reworded it before integration.
- **Dependency anchors.** Of the 285 `Dependencies.csv` rows at `125cfacc1`, none has an `EvidenceFile` that is either target contract (`verify_k2_quotes.py`: "DEP rows citing this contract: 0", for both). **No dependency row goes stale**, and this packet writes no `Dependencies.csv`.
- **Part B carry-forwards.** The brief names none for node K2, and the `D-PEC-99` exhibit assigns none to DEL-08-06 or DEL-10-13. There is no landing table.

### Findings beyond the brief (disclosed)

1. **DEL-10-13 and constraint C-08** (`D-PEC-101` findings 4 and 7).
   - Evidence for classifying it standing:
     - the register row calls the deliverable a "Standing gate" that is "re-proved at each such release" and consumes no internals "(as DEL-10-02)";
     - PRD §12 titles it a "Standing reliance-advertisement gate";
     - `D-PEC-62`'s C-08 set is DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03 and DEL-10-10.
   - Classifying it changes one-shot blocker arithmetic and is the owner's. Question 4 offers it as add-on C8. The contract stays true either way.
2. **DEL-08-06 CON-002 is an authority question for K3.** Does producing tool definitions and testing them inside PEC before the tier-0 act count as declaring or invoking a tool? The contract bars declaring to, registering in and invoking by any profile, harness, App or agent configuration, and leaves the source-and-tests question to the owner.
3. **Ordering against S4 and S1.**
   - DEL-08-06's `agent`-class binding and DEL-10-13's envelope condition have no conforming upstream contract until DEL-08-01 and DEL-04-03 are rebuilt in S4.
   - This affects when production can start, not the contract bytes.
   - The contracts rely only on register and PRD text, and record the upstream gaps as `CON`.
4. **Possible dependency amends.** DEL-08-06 → DEL-04-03 (`D-PEC-101` finding 3; CON-003) and DEL-10-13 → DEL-02-07 (finding 2; CON-002) are left for an owner-ruled register amend. This packet writes no register.
5. **No release process** exists for PEC v2 (DEL-10-13 CON-004). Before any release that advertises reliance, the owner may want to name who performs the release and advertisement act.
6. **Existing inconsistency, observed and not acted on.** The DEL-10-02 contract calls C-08's force "unconfirmed", while `D-PEC-62`'s ruling text and DEL-10-02's `_DEPENDENCIES.md` say it is owner-confirmed. The DEL-10-13 contract relies on neither reading. The DEL-10-02 wording belongs to S1.
7. **`pec.yaml` header.** L3 "Candidate only … awaiting owner ruling" is stale; SCA-006 §B6 already records this for the K3 act. `pec.yaml` lists `projects/pec/execution/**/ScopeOfWork.md` among its protected write paths, which is consistent with this packet's fence.

## Options

- **A — write the two exact contracts, no lifecycle change (recommended).** One act on **2 product paths**, both created. Nothing is modified or removed. No `_STATUS.md`, register, context, reference, dependency or `MEMORY.md` file is touched. Add-ons S, M and C8 are independent of one another.
- **A + S** — as A; then, outside the scope-of-work run, the `OPEN → INITIALIZED` status act on both deliverables (2 modified paths), on the `D-PEC-63` §3.2 / `D-PEC-98` pattern.
- **A + M** (combinable) — as A, plus two new `MEMORY.md` files at the undertaking's closeout (2 created paths).
- **A + C8** (combinable) — as A, plus the owner's C-08 classification of DEL-10-13, recorded in its `_DEPENDENCIES.md` (1 modified path, human-owned section).
- **Amend** — for example:
  - write only one contract (they cite each other only by deliverable ID, so either can land alone);
  - resolve a `CON` now;
  - add a dependency edge;
  - change a requirement.
- **Defer** — nothing opens. DEL-08-06 stays without a contract, and K3 (the tier-0 profile act) cannot follow.

A split that writes the contracts without their open items is not offered: the method requires substantive ambiguity to be marked `CONFLICT`.

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once** under `chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`). Paths are relative to `projects/pec/execution/`.

| Item | Path | Preimage | Postimage SHA-256 |
|---|---|---|---|
| A | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md` | absent (new file) | `31d0aa6e9d77e345b1c7178acde16fbb099d510500130e58aafdbdd60212d036` |
| A | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md` | absent (new file) | `23f6505e8832cea2212f64c61020fa4ec2f390822f0a9a3baf997285eefff182` |
| S (if selected) | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/_STATUS.md` | `73e21846186b3ab46d4d11042ecb2bb00d0c69a0d7b4fa70734c75e65a892511` | `75366b6b8a0050c520ab583be927da3960d21df0b8cd3011668b2047db89a127` (`{D}` = 2026-09-26) |
| S (if selected) | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_STATUS.md` | `c7a5705d7203a26f525317e85fa068d29cfeb49b8686eab1b5cd3e782e22543b` | `3771d5262b8f9044a3dbed81af0032a155ec12e876ec90c1f8253a8e5237e567` (`{D}` = 2026-09-26) |
| M (if selected) | `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/MEMORY.md` | absent (new file) | template instance with slots (below) |
| M (if selected) | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/MEMORY.md` | absent (new file) | template instance with slots (below) |
| C8 (if selected) | `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md` | `5087e581b00557cac9c245c543d0a690ed2a9fc992a96d8e60769f8a44baeb63` | `609aa807710feef11bf8506324cb2a79996f3d6ce5a6eb623ec9516e3ac65693` |

The A postimages are the exact candidate files, copied byte for byte into the run root as `candidates/…`. They have no date slot.

Read-only files the act re-verifies and never writes (SHA-256 at `125cfacc1` and at `947075c9a`; the first five equal at the pin `189f205ff`):

- `_Decomposition/SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`
- `_Decomposition/Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`
- `_Decomposition/ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`
- `_Decomposition/ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`
- `projects/pec/docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `_DomainEngines/profiles/pec.yaml` (repository-relative) `6858d567ee27bae9b832115a40a41b106a9a2a58a62d661ca0e0c2acff9b314f`
- DEL-08-06: `_STATUS.md` `73e21846…2511`, `Dependencies.csv` `10d7b0d8…5050`, `_CONTEXT.md` `90074877…36cc`, `_REFERENCES.md` `9f19e3a6…987e`, `_DEPENDENCIES.md` `6aa230b1…01fd`
- DEL-10-13: `_STATUS.md` `c7a5705d…543b`, `Dependencies.csv` `334b9edc…6e7a`, `_CONTEXT.md` `5efdf4a1…8035`, `_REFERENCES.md` `c0070ada…1656`, `_DEPENDENCIES.md` `5087e581…eb63`

(The full hashes are in `apply_k2.py`.)

### Add-on S — status act (only if question 2 selects it)

**Actor and separation.** The scope-of-work run returns first, and its `NO_STATUS_TOUCH` covers everything it does. Afterwards, outside that run, WORKING_ITEMS dispatches one generic-shell TASK with no workflow selected (`D-PEC-63` §3.2; history label `TASK+status-advance`). Its only write targets are the two `_STATUS.md` paths.

For each deliverable, the TASK runs the command below from the repository root, and only if both conditions hold:
- `validate_scope_of_work.py` on that deliverable prints `PASS format=SOW_V1`;
- the act's independent verifier has passed.

```text
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface" INITIALIZED "TASK+status-advance"
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate" INITIALIZED "TASK+status-advance"
```

**Slot rule.**
- The only varying bytes are the act date `{D}`: in `**Last Updated:** {D}`, and in the appended line `- {D} — State set to INITIALIZED (TASK+status-advance)`.
- `**Current State:**` becomes `INITIALIZED`; every other byte is unchanged.
- Prototype: `write_status.sh` `0bf835f5…ece3`, exit 0 ×2 (`evidence/addon_S_prototype.out`; postimages in `addons/S/`). The tool is forward-only.

### Add-on M — MEMORY files (only if question 3 selects it)

At the undertaking's closeout (graph node M1), WORKING_ITEMS creates the two `MEMORY.md` paths tabled above. Each is `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` row:

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | First Scope of Work contract written under D-PEC-103 (graph node K2). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-103 ruling record> |
```

The slots `{D}` and `{PR}` and the two link targets are fixed at closeout. The verifier checks that no other byte departs from the template.

### Add-on C8 — the owner's C-08 classification of DEL-10-13 (only if question 4 selects it)

**What it writes, and why it needs the owner.** The one added line goes in the **"Dependency Tracking Mode" section, which is human-owned** under `docs/SPEC.md` §5.1 ("humans or the coordinating workflow, ordinarily `project-setup`, maintain them"; "Agent-owned sections never overwrite human-owned sections"). The classification it records is the owner's: `D-PEC-101` finding 4 says classifying DEL-10-13 as standing "changes one-shot blocker arithmetic and is an owner classification". So C8 **applies only on the owner's explicit selection**, as the owner's own classification; WORKING_ITEMS only transcribes it into the human-owned section.
- Without an explicit C8 answer, nothing is written and DEL-10-13 stays unclassified.
- A "decline" answer also writes nothing, and the classification remains the owner's to make later.

The postimage (`addons/C8/…/_DEPENDENCIES.md`) inserts exactly this line after the section's "- **Notes:** …" line and changes no other byte:

```text
- **Standing obligation (constraint C-08):** STANDING node — it gates releases, not successors, and is excluded from one-shot COMPLETE/UNBLOCKED arithmetic (owner-classified under `D-PEC-103`).
```

**Placement (a conservative choice).** The five `D-PEC-62` C-08 nodes (DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10) carry a separate `## Standing obligation (constraint C-08)` section in their legacy-heading files, and `D-PEC-101` finding 7 speaks of "the C-08 section".
- DEL-10-13's file uses the D-GOV-46 §5.2 heading schema. That schema binds `preparation`, `dependency-extract` and `project-setup` when they create a file or add a missing section; it does not forbid another heading in an existing file.
- This packet nonetheless adds no heading: a bullet inside the existing human-owned Tracking Mode section records the same classification without departing from the §5.2 headings. An amend could instead add the legacy-style section.
- The Run Notes bullet saying `D-PEC-101` did not classify the deliverable stays, and stays true.

**Effects checked.** No tool reads the annotation.
- `validate_decomposition_registers.py --strict`, `analyze_dep_closure.py`, the harness and the receipts validator give output identical to the pre-act run after C8 (`evidence/run_main/*_postC8.*`).
- The DEL-10-13 contract is true under either answer (its CON-001, AX-007 and REQ-016).

**Mechanics.**
- One run of `apply_k2_c8.py`, after `apply_k2.py`.
- Preflight pins: the target's preimage, the DEL-10-13 contract's postimage, DEL-10-13 `Dependencies.csv` and `Deliverables.csv`. `_STATUS.md` is not pinned, because S may already have run.
- The write set is exactly the one modified file.
- **Ordering.** C8 pins DEL-10-13's option-A postimage, so it runs only after A has written that contract; an amend that writes only DEL-08-06 excludes C8. Any single-contract amend needs a rebuilt, re-hashed `apply_k2.py`. C8 and S must not run concurrently (C8's inventory check would fail and roll back); run them one after the other.
- **If the final packet number is not 103**, the one token `D-PEC-103` in the line changes. The postimage hash and `apply_k2_c8.py` are then rebuilt, and the verifier checks that the diff is that token.

## Generation method (binding)

The A bytes come from one run of `apply_k2.py`, **SHA-256 `557b73eec48ccd1c2c058b28ef86685d4d7b9ff592333cbb49921d8de7028589`**. The C8 bytes, if selected, come from one run of `apply_k2_c8.py`, **SHA-256 `0b162a74a4068da154f1c77ddf1fdd77151ba9186155fe08632cfff2443aa1ba`**. Both are stdlib-only Python, prepared with CPython 3.13.7. They are copied byte for byte into the run root with the candidate files and the C8 postimage:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_INIT_K2_{D}/apply_k2.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_INIT_K2_{D}/candidates [--check-only]
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_INIT_K2_{D}/apply_k2_c8.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_INIT_K2_{D}/addons/C8 [--check-only]
```

**Failure semantics (`apply_k2.py`).**
- **Preflight.** Any failure exits 1 before any byte is written. The script checks that:
  - both candidates hash to their postimages;
  - both targets and their temporary siblings are absent, and their folders are present;
  - all 17 pinned files hash as tabled;
  - if the script's directory lies below `projects/pec/`, it lies below a run root (`projects/pec/execution/_Coordination/SOW_INIT_K2_*`). A copy placed directly in `projects/pec` is refused, which closes the gap noted in PR #964 review 01.
- **Write.** Each file is written to a temporary sibling (`…ScopeOfWork.md.k2tmp`), hash-checked and renamed into place.
  - If a later step fails (I/O error, hash mismatch, post-write inventory mismatch, changed pinned file), the script removes every temporary file and every target it created, and exits 1.
  - On exit 1 no target or temporary file remains; exit 2 would report an incomplete clean-up.
- **Write set.** The script inventories every file under `projects/pec` (path and SHA-256) before and after, except its own directory (the run root). It requires the difference to be exactly the two targets, created, with nothing modified or removed. It also re-checks every pin after the write.
- **Second run.** It fails preflight. The script never touches `_STATUS.md`, `MEMORY.md` or `_DEPENDENCIES.md`.

`apply_k2_c8.py` has the same guard, inventory and rollback. It restores the preimage bytes on any post-write failure.

The check aids, which are not bound:

| Aid | SHA-256 | Role |
|---|---|---|
| `test_apply_k2.py` | `f6893e8206c6b41c12099466ed82fe76d5a049f40e0796b64cb22998ae2831a0` | fault injection, 15 cases (11 A, 4 C8) |
| `verify_k2_quotes.py` | `50343b9fdc83530e09b4b60ab1a878a4566f551aa52d2a755277a39415f64642` | two-sided quote check, raw dependency quotes, forbidden phrase, observation commit |
| `verify_k2_state_claims.py` | `8c7146f2d4a5fabf8aa6849cdbbb52f3f5342bed8ba5e871d1493d0408b35b29` | commit-anchored state claims, each also matched in the candidate |
| `check_cited_ids.py` | `0389f1dcdf1890bd3830cea115b52d4ced353a25924c737143bceaa6e9ab6335` | qualified citations resolve at the observation commit, labelled by node |
| `scan_old_s2_text.py` | `b4043dfb52cad1274ed5751e699301dccf587b05e18173130997c1111df2f78a` | no prior-S2 text dropped by `D-PEC-100` |
| `run_k2_checks.sh` | `670b284c4494100ac659e8342c28480f66d4aa32b0180ad7995d49385aa9cdd6` | runs every check on pre/post exports (the rerun method) |

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`, on the act branch. Record each command, exit code and output in the run root. `run_k2_checks.sh` runs rows 2–11 on `git archive` exports of one commit and is the rerun method.

| Check | Command | Required result |
|---|---|---|
| 1. Preconditions | ruling and register row on fetched `origin/main`; `apply_k2.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `CHECK preflight passed`; `ALLOW` everywhere; on any pin mismatch, stop and route to the owner (no re-pin is pre-authorized) |
| 2. Contract validity | `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` ×2 | `PASS format=SOW_V1` ×2 |
| 3. Checklist | `python3 tools/scope_of_work/derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, each twice | exit 0; 17 and 19 items; reruns byte-identical; equal to the prepared `d9eae773…4c21` and `b0b56b38…c8be` |
| 4. Boundary owners (QA 21) | `python3 tools/scope_of_work/check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×2 | exit 0; 1 requirement checked and 0 failing each; 0 `NOT_CHECKABLE`; the non-deliverable owners resolved by hand as tabled below |
| 5. Quote fidelity | `python3 <run root>/verify_k2_quotes.py --tree . --gitdir . --prep <run root> --observation 125cfacc1` | `RESULT PASS 133/133` (both sides; tree quotations read at `125cfacc1`; 0 dependency rows cite either contract) |
| 6. State claims | `python3 <run root>/verify_k2_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 479/479` |
| 7. Cited IDs and old S2 text | `check_cited_ids.py --commit 125cfacc1`; `scan_old_s2_text.py --prior ce934ac33 --current 125cfacc1` | `RESULT PASS 0/0`; `stale=0` |
| 8. Lifecycle preserved (A) | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty under A; under S exactly the two tabled postimages |
| 9. Strict registers (D-GOV-48) | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution`, before and after | exit code and output **identical** to the pre-act run (at `947075c9a` + branch: exit 1, 0 errors, 26 pre-existing `XRG-013` warnings, owner-deferred) |
| 10. Closure and every-PR checks | `analyze_dep_closure.py projects/pec/execution`; `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | summary and outputs identical before and after A (and after C8) |
| 11. C8 (if selected) | `apply_k2_c8.py --check-only`, then apply | exit 0; write set exactly the one `_DEPENDENCIES.md`; row 9 and 10 outputs unchanged |
| 12. Containment | `git diff --name-status origin/main...HEAD` | the two created contracts; S's two `_STATUS.md`, M's two `MEMORY.md` and C8's `_DEPENDENCIES.md` only if selected; the run root and HELP_HUMAN's records under `execution/_Coordination/**`; nothing else |
| 13. Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. The act changes no decomposition truth, register or topology; C8 is an annotation that no tool reads.

QA 21 hand resolution (exclusions whose owners are not deliverables; the tool checks the deliverable owners):

| Contract | Requirement → owners | Cited claim |
|---|---|---|
| DEL-08-06 | REQ-014 → 23 deliverable owners (tool-checked) | CLM-011 |
| DEL-08-06 | REQ-015 → token mechanism: the §16.6 owner ruling; profile entry: the tier-0 owner; enabling: the consumer; advertising reliance: the human release act after the §12 gate; API schema fields: the later D-PEC source packet (§B8) | CLM-012, CLM-013, CLM-002 |
| DEL-10-13 | REQ-015 → deliverable owners (tool-checked) | CLM-009 |
| DEL-10-13 | REQ-013 → release, tagging, publishing and advertisement acts: the human owner (labelled interpretation) | CLM-010 |
| DEL-10-13 | REQ-016 → C-08 classification: the owner; register amends: an owner-ruled packet; lifecycle: `_STATUS.md` | CLM-012, CLM-013, CLM-016 |
| DEL-10-13 | REQ-017 → the evidence owners | CLM-009 |

### Independent verifier

The method's independent verification is a separate `MODE=VERIFY` run, read-only on production content, by a TASK that authored nothing. The preparation verdicts are in this folder (`VERIFIER_VERDICT_NN.md`, each with the manager's dispositions). A fresh one runs again at the act. It returns a verdict; defects return to the author, and the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`, the run-root scripts hash as bound, and the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **`MODE=VERIFY`.** The mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21), including the QA 21 hand resolution.
4. **Semantics.**
   - Every claim is true at the commit it names, or at `125cfacc1`, and every quotation is verbatim.
   - No requirement adds scope beyond the deliverable's ledger row, its `Deliverables.csv` row and PRD v2.4.
   - Every open item is `TBD` or `CON`; OI-006, the K3 act, the C-08 classification and the DEL-02-07 edge are not decided.
   - The objective attributions are no stronger than the sources.
   - No `## Remaining` section is read or presented as a surface.
5. **Containment and lifecycle**, as in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act and the checks, and C8 and M if selected. S, if selected, is one separate generic-shell TASK. The manager runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/SOW_INIT_K2_{D}/`, in the default-writable fence, holds:
  - `apply_k2.py` and `apply_k2_c8.py` (exact bytes), `candidates/`, `addons/`, `quotes/`, `claims/`, the check aids and all outputs;
  - `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md`;
  - `VERIFIER_VERDICT_NN.md`.

  No `_run_records/` entry is written in either deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under `D-PEC-88`. `_Evaluation/**`, the registers and `Dependencies.csv` stay closed. Of the `_DEPENDENCIES.md` files, only DEL-10-13's opens, and only under C8.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning, unless the owner states otherwise. Role identity is instruction-asserted.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the scripts leave no target or temporary file (A), or the preimage (C8). If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR:
  - removes the two created contracts, and M's two files if created;
  - restores the two `_STATUS.md` preimages if S ran (`write_status.sh` blocks backward moves, so file revert is the only walk-back, per `D-PEC-63` §6);
  - restores the DEL-10-13 `_DEPENDENCIES.md` preimage if C8 ran.

  History is preserved:
  - The ruling record and register row are never reverted; a rollback is its own register row and record.
  - The run root stays as non-current evidence, with a rollback note.
  - No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A with any of S, M or C8, or an amendment, grants none of the following:

- any `v2/**`, `software-workflow.json` or `docs/PRD.md` write, or any source, tool definition, harness, fixture or test file. The contracts state future production only.
- any `_Decomposition/**` or `_ScopeChange/**` write, or any register write: no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv` or `Dependencies.csv` change, no dependency edge, and no action on the D-GOV-48 warnings. No `_DEPENDENCIES.md` change other than C8's one line, and only if selected.
- any `_CONTEXT.md`, `_REFERENCES.md` or `_SEMANTIC.md` write, or any file of another deliverable. The S4 and S1 contracts are not touched.
- any lifecycle change other than add-on S's single `OPEN → INITIALIZED` per deliverable, and none under A. No `## Remaining` entry is written or read.
- `CHECKING`, `ISSUED`, artifact acceptance, a REVIEW gate act, or any readiness, release or reliance claim. `CHECKING` is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it.
- a tier-0 profile act, a `_DomainEngines/**` write, or the declaration, registration or invocation of any tool (K3 is its own act).
- a token-mechanism decision (OI-006), or a resolution of any `CON` item.
- a registry or D-PEC-96 act, a Task Management disposition, an audit run, a pointer move, or an edit of the `D-PEC-99` exhibit.
- a foreign, Root or instruction-surface write, including `projects/pec/AGENTS.md`.
- adoption of `scope-of-work` `MODE=REVISE` or any other new Root mode.
- a schedule reading. Blocker output stays advisory.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**, the two exact first contracts in one act.
2. **Add-on S — record `INITIALIZED` for both deliverables.** A separate TASK does it outside the scope-of-work run, after the contracts validate and pass independent verification.
   - Recommendation: **S**. Standard §8 defines `INITIALIZED` as exactly this condition, and `D-PEC-98` ruled the same act for DEL-02-08 and DEL-02-09.
   - Choose "A without S" to keep the act lifecycle-neutral.
   - Without an answer, **no status act is performed**.
3. **Add-on M — MEMORY files.** Create both `MEMORY.md` files at closeout (recommended), or record the run only in the graph and central receipt. `projects/pec/AGENTS.md` allows either on your decision.
4. **Add-on C8 — classify DEL-10-13 as a constraint C-08 standing node.** It is excluded from one-shot COMPLETE/UNBLOCKED arithmetic and gates releases, not successors, like DEL-10-02 and DEL-03-04.
   - C8 writes one line in the **human-owned** Tracking Mode section of DEL-10-13's `_DEPENDENCIES.md`. It therefore **applies only if you explicitly select it**.
   - Recommendation: **C8**. The accepted register row calls the deliverable a "Standing gate … re-proved at each such release", consuming no internals "(as DEL-10-02)", and PRD §12 calls it a standing gate.
   - Choose "decline" (or give no answer) to leave the classification unmade. Nothing is then written, and the contract stays true either way.
5. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran on `git archive` exports in `mktemp -d` directories under the session scratchpad, never on a checkout. Interpreter: Python 3.13.7 (CPython); local date 2026-09-26.

The final run is `evidence/run_main/SUMMARY.out`, from `run_k2_checks.sh` on the branch head `6608f56a5`, which merges `origin/main` `947075c9a`. Every raw output is beside it:

```text
basis commit: 6608f56a51cf5b6e66543f02019d15b8845bc587
python: Python 3.13.7
PASS reliance preflight: ALLOW x7
PASS act A: check-only 0, apply 0, rerun refuses 1
PASS containment: 2 new files, both ScopeOfWork.md
PASS validate DEL-08-06
PASS checklist DEL-08-06 (rerun byte-identical)
PASS boundary DEL-08-06 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS validate DEL-10-13
PASS checklist DEL-10-13 (rerun byte-identical)
PASS boundary DEL-10-13 (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)
PASS quotes: RESULT PASS 133/133 (INFO DEL-08-06 DEP rows citing this contract: 0 INFO DEL-10-13 DEP rows citing this contract: 0 )
PASS state claims: RESULT PASS 479/479
PASS cited IDs: RESULT PASS 0/0
PASS old S2 text: RESULT PASS stale=0 current=43
PASS strict identical pre/postA, export root normalized
PASS harness identical pre/postA, export root normalized
PASS receipts identical pre/postA, export root normalized
PASS closure_summary identical pre/postA, export root normalized
PASS add-on C8: check-only 0, apply 0, rerun refuses 1
PASS containment after C8: 2 new contracts + 1 modified _DEPENDENCIES.md
PASS strict identical pre/postC8, export root normalized
PASS harness identical pre/postC8, export root normalized
PASS receipts identical pre/postC8, export root normalized
PASS closure_summary identical pre/postC8, export root normalized
PASS whitespace
PASS fault injection: RESULT PASS 15/15
OVERALL PASS
```

Strict registers: exit 1, 0 errors, 26 warnings (the pre-existing `XRG-013` set), identical before and after. Closure: 0 SCCs and 0 bidirectional pairs; the summary is identical before and after.

Preparation artifacts, all in this prep folder (hashes in `SHA256SUMS`):
- `candidates/…/ScopeOfWork.md` ×2 (postimages as tabled);
- `quotes/DEL-*.json` ×2 and `claims/DEL-*.json` ×2 (the verifier inputs);
- `addons/S/` (S postimages) and `addons/C8/` (C8 postimage);
- `apply_k2.py` and `apply_k2_c8.py` (bound), `test_apply_k2.py`, `verify_k2_quotes.py`, `verify_k2_state_claims.py`, `check_cited_ids.py`, `scan_old_s2_text.py`, `run_k2_checks.sh`;
- `K2_DRAFTER_BRIEF.md`;
- `evidence/` (every check output, the reliance preflight, the checklists and the S prototype);
- `VERIFIER_VERDICT_NN.md` (the preparation verdicts, with dispositions).

Basis at `125cfacc1` (unchanged at `947075c9a` unless noted):

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `9ae4bea2…9665` / `1a13a5b0…8fb7` / `df9196d1…5eb8` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` / `_LATEST.md` | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` / `768ae4c4…a771` |
| `docs/PRD.md` (v2.4) | `ae49b806…3fbe` |
| SCA-006 `Propagation_Plan.md` / `Impact_Assessment.md` | `f95d00d1…d7d8` / `93253b7d…b691` |
| `D-PEC-101` proposal / ruling; `D-PEC-62`; `_REGISTER.md` | `7ad17606…a095` / `baa4fc09…ba28` / `4aa1b83b…8924` / `33b43ae8…5a2f` |
| `_DomainEngines/profiles/pec.yaml` | `6858d567…314f` |
| Work graph (at `125cfacc1`; changed at `947075c9a`, not pinned) | `8296ad0c…b148` |
| `write_status.sh` / `MEMORY_TEMPLATE.md` / `validate_decomposition_registers.py` | `0bf835f5…ece3` / `5a9564f4…6a5a` / `300a321f…ee20` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d931…cbc` / `b1712e4b…cd0e` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, node K2 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with two TASK drafters and fresh read-only reviewers as described under Method. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The roles and the `high` reasoning effort are instruction-asserted.
