# Packet — Root LOOP_INIT consolidation and run boundary

- Date: 2026-09-05. Status: `PROPOSAL — AWAITING OWNER ITEM-BY-ITEM RULING`.
- Owner: Ryan Tufts. Scope: Root governance. Prepared by OpenAI GPT-6, primary `/root`; exact serving model ID unavailable in the session. Agent 0 role is not mechanically enforced. Judgments below are the agent's.
- Basis: freshly fetched `origin/main@49f9e148cbc5cc21b33368e071e33451ed1d1f33`; clean new branch `codex/root-loop-consolidation`. This is later than the handoff's PR #720 basis.
- Record home: `execution/_Coordination/`, following the 2026-08-02 assessment. Receipts 129–131 bind actual owner acts under `plans/steers/`; no new R-number or D-GOV ruling is minted for this unruled support packet. The intent/history **ruling candidate**, clearly unruled, is under `plans/steers/` for a later owner act.
- Candidate post-images are applied on this branch to LOOP_INIT and the root launcher. The new successor file is unselected. CURRENT_WORKPLAN, all `_LATEST.md` pointers, the idle plan, accepted scopes, registers, prior receipts, `projects/*`, `frontend/**` and runtime source are untouched.

## Preparation authority and scope

Current owner handoff (2026-09-05), excerpts transcribed verbatim as tasking evidence, not a ruling on candidate bytes:

> Two deliverables, one PR, human-gated. Do not rule anything yourself.

> Owner acts (rulings, `_LATEST.md` pointer moves, PR merges) are the owner's; you prepare, commit, push, and open a PR, and stop.

> Any edit under `init/`, `docs/`, `tools/`, `agents/`, `skills/`, or `.github/workflows/` is an instruction-surface change (D-GOV-21 M2) and needs a G4 tranche manifest in the same PR

This present task authorizes preparation and publication only. It is not execution under R17's stale basis gate, not Root product activation and not a ruling that R17 is superseded. Direct primary preparation is explicitly requested; no fictitious manager dispatch or mechanically enforced Agent 0 role is claimed.

## Verified entry state and handoff corrections

G0–G4 pass. The actual harness executable is `tools/practitioner_harness/harness.py`; the requested `tools/harness.py` path does not exist (attempt exited 2). Root `status --project root` succeeds: 53 INITIALIZED, no mismatches by G1; its decision section parses **no rows**, so it cannot stand in for the D-GOV register. Self-check exits 0 with 55 WARN, 4 REVIEW, 14 INFO, 1 NOT_APPLICABLE at entry; its scope list excludes Root execution. Neither command proves semantic acceptance or ledger validity.

Newest receipts: Root 131 (2026-09-03), App 244 (2026-09-05), Piping 130 (2026-09-05). Root register: 18 live (10 OPEN, 8 DEFERRED); the live REGISTER_CLOSED.csv has 109 archived. Accepted PRD is Revision 8, found at §10.5 rather than its historical proposal banner; decomposition is revision 1.3 with SCA-004 acceptance and application identified through `execution/_ScopeChange/_LATEST.md` and its records. 53 registered **and materialized**, 45 empty `Remaining`, seven with no such section, only DEL-02-06 with REM-002/003. No broad production activation is inferred from INITIALIZED; bounded historical activation/acceptance records do exist. The compatibility package preserves ten held markers; later R16-B substantively disposes Tier-0 and R17 preserves that act, leaving nine other holds. See the separation assessment for the distinction. The handoff's 46/45 counts and “never activated” absolute are not reliable.

The idle pointer still names the 127-line 2026-07-27 plan. Its addenda are dated history, not live authorization; the current handoff's register counts lag Receipt 131. R17's requested successor is absent at the basis. Its fixed-main basis gate is no longer satisfiable, its future “Receipt 131” is already occupied, and R18 closed TM-ROOT-122 while leaving TM-ROOT-106 unchanged. These are reported, not repaired by inventing successor authority. The separation assessment corrects the alleged runtime path-model gap.

## Method and exemplar

Read live D-APP-112 packet (full triage, item B, ordering and dry-run table), D-APP-112–115 records and current App LOOP_INIT. Adopt their method as a **proposal for Root**, not transferred App authority: POINT = discover at named source; MECH = explicit deterministic observation; KEEP = residual behavioral guard with cited reason and no adequate mechanical substitute; OWNER = carry actual owner speech verbatim; DROP = redundant/obsolete explanation. No source clause in Root LOOP_INIT or idle Step 0 is marked as verbatim owner speech; none is falsely labelled OWNER. Actual R17 speech is quoted unchanged below and in the history candidate. Headings/blank lines carry no separate instruction.

Order is map → limits → protocol. Map names both control-plane discovery and product deliverables first; limits precede execution. The old LOOP_INIT is 132 lines, idle Step 0 lines 23–58. The candidate is under 100 lines (exact final size/hash in `AgentRuns/ROOT_LOOP_CONSOLIDATION_2026-09-05/ARTIFACTS.sha256` and validation record). It uses source pointers for policy, not another agent index or work queue.

## Item A — candidate entry and ordered work discovery

Review `execution/_Coordination/LOOP_INIT.md` as the exact branch post-image. Discover in this proposed order:

1. Owner steer of record (verify the actual ruling, scope, basis gate and pins).
2. Routed notices without a recorded disposition (attention; not an automatic action grant).
3. Register rows ruled for action (verify the ruling; OPEN/DEFERRED status is not authorization).
4. Accepted deliverable-local `## Remaining` work, with its scope/lifecycle/dependencies/gates/checks/write locus/return contract.

This names the two practical Root surfaces without changing the product definition. R17-D §2 currently says:

> make Root work discoverable only through accepted deliverable-local
> `Remaining` items;

R17-E says:

> Nothing absent from accepted deliverable `Remaining` scope is
> selectable.

**A requires an explicit owner amendment:** retain deliverable-only selection and engineering/evidence pressure for product work; allow separately owner-authorized control-plane acts to be discovered through the first three surfaces, without a second product queue or automatic register disposition. This is additional to B's PR-boundary change. No consolidation-only argument silently supersedes either sentence.

Gate classes: owner acts/routed notices releasing work must be on fetched `origin/main`; an ordinary predecessor may count on the run branch only with commit, passing checks and durable return and only where its consumer requires no owner acceptance or merged act. Present tasking permits explicitly requested candidate preparation; it does not prove any merged-act gate. R17's specific deliverable/evidence contracts remain the v3 product bar. First return must include Git state, receipt cursor, actual authority/census/checks, lawful lanes, exact parked releases and map deltas.

### Full clause triage

Line references L = basis LOOP_INIT, P = basis idle plan. Every behavioral clause is covered; compound clauses with distinct destinations are split. Original LOOP_INIT bytes are preserved in the run preimage; idle plan is unchanged.

| ID | Basis lines | Clause | Disposition | Justification / surviving home |
|---|---|---|---|---|
| L01 | 3 | Resume this directory’s Root loop | POINT | §1 identifies the Root coordination map; no extra role narrative. |
| L02 | 4–5 | Goal/intent pointer; read exact target | POINT | §1 retains CURRENT_WORKPLAN and exact target; C proposes intent-only target. |
| L03 | 5–6 | Widest lawful tranche; human gates | KEEP | Selection/limits retain this non-mechanical behavior; R17-E supports bounded pressure. |
| L04 | 8–10 | Orientation; live sources govern; derivatives carry no authority | KEEP | Header and live-source recheck retain stale-map protection evidenced by Receipt 131. |
| L05 | 14 | Resolve REPO_ROOT and work there | MECH | Step 0 cd/git resolution; §1 establishes relative-path anchor. |
| L06 | 15–16 | Read AGENTS and selected role | POINT | §1 points to both actual packages; role routing stays in AGENTS. |
| L07 | 17 | Resolve coordination directory | POINT | §1 uses explicit repo-relative coordination paths. |
| L08 | 18–19 | Root execution/working-root identity | POINT | SPEC §0.2 and D-GOV-21; no paraphrased replacement path model. |
| L09 | 20–23 | Accepted PRD/decomposition and registered passing guards before materialization | MECH | G0–G4 commands, with accepted-source map retained. G0 checks recorded registration, not semantic acceptance. |
| L10 | 23–24 | Until gate closes confirm only control records | DROP | Obsolete condition at materialized 53-deliverable basis; G0 takes over live observation. |
| L11 | 28–31 | Read pointer/target, run plan Step 0, newest receipt before selection | MECH | Pointer and latest-header extraction move to LOOP_INIT Step 0; C relocates protocol without changing idle history. |
| L12 | 33–34 | Never select by mtime/order/older newest-plan language | MECH | Exact Target parser has no fallback selection. |
| L13 | 34–36 | Bad/missing/escaping pointer stops with defect | KEEP | Map names the stop; Step 0 checks shape, containment and existence. Operational failures must remain visible. |
| L14 | 38–40 | Plan intent/protocol/constraints/gates/pointers; receipt is context, not truth | POINT | Intent at target; protocol here subject to C ruling; authority/evidence in CONTRACT and AGENTS. No duplicate exposition. |
| L15 | 44–46 | First return: branch/worktree/cleanliness/divergence | KEEP | First-return contract, mechanically supported by Git commands. |
| L16 | 47 | First return: Root and relevant App/Piping receipts | KEEP | Full relevant receipt read and return required; Root latest extraction avoids arbitrary tail truncation. |
| L17 | 48 | First return: live decisions and directions | KEEP | Required with sources; status does not parse Root decisions. |
| L18 | 49 | First return: widest lawful lanes | KEEP | Required with authority and write scope, not just labels. |
| L19 | 50–51 | First return: parked lanes and releases | KEEP | Exact owner acts/predecessors remain explicit. |
| L20 | 53 | Only human decisions left: slate and stop | KEEP | First-return and terminal protocol; absent validator cannot replace judgment. |
| L21 | 57–58 | Human acts never manufactured or inferred | POINT | K-AUTH-1/2 in limits; full doctrine stays in CONTRACT. |
| L22 | 59–61 | Reopen cited sources; live wins; record delta | KEEP | Step 0 rule answers actual stale idle plan and Receipt 131 handoff counts. |
| L23 | 62–63 | Preserve canon/history; owning amendment path | POINT | Limits point to owning amendment paths and authority documents. |
| L24 | 64–65 | Git/report artifacts are not semantic acceptance | POINT | Header, owner-act gate class and CONTRACT; duplicate examples removed. |
| L25 | 69–73 | AGENTS delegation and per-manager responsibility list | POINT | AGENTS + selected package; avoids a second agent index. |
| L26 | 75–79 | Actual pre-dispatch work graph at AgentRuns path | POINT | Map and AGENTS declared-scope/durable-evidence contract. |
| L27 | 81–82 | Actual runtime run only; no placeholders/briefs-as-execution | KEEP | Explicit no-fake-child sentence; AGENTS has executable-mechanism requirement. |
| L28 | 82–85 | Full work-graph/notice/amendment/return/handoff field list | POINT | Actual AGENTS and HELP_HUMAN contract instead of duplicating schema. |
| L29 | 87–90 | Native delegation only with sealed scopes/evidence; defer/fallback; parent mediation | POINT | Live AGENTS D-GOV-35 class and calibration supersede older equivalence phrasing; no invented stronger enforcement. |
| L30 | 92–94 | Project children in project; root cross-project fan-in | POINT | AGENTS/selected role path bounds; Root has no foreign-write grant. |
| L31 | 98 | Tranche-specific plan fences | POINT | Applicable current owner steer holds tranche fences; C keeps plans intent-only. |
| L32 | 100 | New/amended human ruling stop | POINT | Limits K-AUTH-1/2. |
| L33 | 101 | Scope expansion/substantive change stop | KEEP | Limits preserve unresolved scope/consequential gate; already authorized preparation is not stopped again. |
| L34 | 102 | Lifecycle acceptance/issuance stop | POINT | Limits + SPEC lifecycle and CONTRACT. |
| L35 | 103 | Authority/ownership/shared-write conflict stop | KEEP | No deterministic command settles semantic conflicts. |
| L36 | 104 | Stage-2 authorization stop | KEEP | Explicit Stage-2 gate stays; no new meaning inferred. |
| L37 | 105 | Consequential uncertainty stop | KEEP | Ambiguous gates stay owner-class. |
| L38 | 107–108 | No foreign working-root writes from Root control records | POINT | Limits + SPEC §0.2/D-GOV-21. |
| L39 | 108–109 | Project pilots: accepted variance/path-bounded activation | POINT | Limits preserves owning-loop accepted variance and activation pointer. |
| L40 | 110–113 | Root M1–M7/G0–G4; separate M2 instruction tranche | POINT | D-GOV-21/ownership/guards map; limits explicitly keeps independent M2 and G4. |
| L41 | 117–120 | After lawful tranche run plan/profile checks | MECH | Closeout commands plus affected-profile requirements; no stale plan checklist. |
| L42 | 121–123 | Minimal receipt: unique owner directions, pointers/gates/checks/blockers | KEEP | Existing form manually inspected; no fabricated validator contract. |
| L43 | 124–125 | Explicit upstream/derivative/closure/rerun/blocker handoff | POINT | AGENTS governance integration rules; terminal sentence retains required fields. |
| L44 | 126–129 | CHANGE; default human PR; optional owner proxy; K-MERGE-1 | POINT | CHANGE and PRD §5.3.1 remain authority; B proposes stricter never-self-merge run policy. |
| L45 | 131–132 | Per-run steer applies but never overrides gates/canon | KEEP | Last sentence retains rule and adds historical-section lookup. |
| P01 | 25–26 | Idle Step 0 before selection/dispatch | MECH | One LOOP_INIT Step 0; no second plan protocol. |
| P02 | 28–29 | Resolve root and CURRENT_WORKPLAN | MECH | Step 0 resolver and exact Target read. |
| P03 | 29–30 | Require target this exact idle plan | DROP | Self-referential idle restriction cannot survive C successor selection; exact pointer resolution remains. |
| P04 | 30–32 | Missing/malformed/escape/wrong/missing target stop | MECH | Exact pointer shape/containment/existence; C owner selection supplies expected target, no guessed successor. |
| P05 | 33–34 | Branch/detached, cleanliness, divergence | MECH | Git commands and first return. |
| P06 | 34–36 | Unrelated changes external; no false synchronized claim | POINT | AGENTS/CHANGE file-state discipline; first-return actual refs remain mandatory. |
| P07 | 37–39 | Handoff/newest Root/relevant project receipts | POINT | Map plus full-read instruction; latest Root header command. |
| P08 | 39–41 | Reopen authority/snapshots/directions; live wins | KEEP | Same single Step 0 stale-map rule as L22; consolidated once. |
| P09 | 42–44 | Re-derive PRD/decomposition/census/bounded lanes from committed sources | MECH | Root status/G1 and source map; first return requires live acceptance verification, not status banner inference. |
| P10 | 44–46 | Stale count/pointer/lifecycle/authority defects reported | KEEP | First-return deltas; no automatic rewriting of accepted snapshots. |
| P11 | 47–52 | G0–G4 commands | MECH | Exact five live scripts retained in loop. |
| P12 | 53 | Stop on BLOCK/operational error | KEEP | Required-command failure stop; guard loop propagates each failure. |
| P13 | 54–56 | No released lane: slate and stop | KEEP | Selection/first return; no work invented from attention rows. |
| P14 | 56–58 | Idle plan grants no production/activation/lifecycle/scope/implementation/publication/release/reliance | POINT | Candidate intent-only target grants nothing; CONTRACT and owning instruments hold substantive gates. |

### Receipt limitation

There is no Root receipt validator. DEL-04-11 is its accepted carrier, not an implementation. The candidate says to inspect and append in the existing form; it introduces no pseudo-machine grammar, required receipt-chain fields or invented validation result. Manual append-only/preimage checks and truthful citations remain necessary. Implementing DEL-04-11 would need its own accepted work selection and independent M2 authority for tools. Do not copy App’s field-level validator claims into Root.

## Item B — exact R17 run-boundary supersession proposed

Source: `plans/steers/chirality_app_v3_r17_pathway_seating_steer_root_2026-08-27.md`, N1. Exact clause (including punctuation):

> - require one branch, one PR, one receipt, and owner merge per iteration;

Proposed owner ruling: supersede **only that clause** with:

> One branch per run, cut from origin/main. Each iteration has one commit and one receipt, pushed after closeout. Independent lawful nodes may execute concurrently under disjoint scopes; dependent nodes may execute in later iterations on that branch when the consuming gate requires neither owner acceptance nor a merged act. Open one PR when lawful advancement reaches its terminus or the next step requires a merged act. Never self-merge; the owner reviews and merges or rejects. Rejected work is re-derived from current main on a fresh run, never treated as accepted predecessor evidence.

This supports persistence within approved scope, not stacked PRs or self-acceptance. It preserves R17’s failed-check repair and deliverable engineering/evidence requirements. Never-self-merge is an intentional stricter Root-loop default than PRD §5.3.1; only a later explicit owner direction could change that boundary, never agent inference. The candidate’s run-branch predecessor rule depends on this ruling. C’s protocol relocation and A’s control-plane exception require their own rulings; approving B alone supplies neither.

## Item C — preserve D-7 pointer, change its target's role

Recommended candidate: `execution/_Coordination/WORKPLAN_2026-08-27_root_v3_rc.md` (R17's requested filename, prepared 2026-09-05). It carries proposed standing purpose, the pinned v3 completion-reference meaning, and owner-only successor selection. It carries no state, lane list, commands, or receipt protocol. Exact post-image is on the branch but is **UNSELECTED**.

The proposed pointer post-image is preserved separately at `AgentRuns/ROOT_LOOP_CONSOLIDATION_2026-09-05/CURRENT_WORKPLAN_CANDIDATE.md`; no live pointer is moved. It preserves the deterministic Target form and names the successor. D-7, G1 adapter and practitioner fixture remain untouched. Historical idle bytes remain unchanged, as R17 explicitly requires. The three addenda including all four 2026-08-02 lanes are carried byte-for-byte as dated quotation in `plans/steers/root_loop_intent_history_ruling_candidate_2026-09-05.md`. This is a draft ruling form without an owner act, not a fabricated D-APP-115 equivalent ruling.

**C requires explicit owner amendment of R17 N1 and R17-E's location requirement:** place currentness/protocol/checks/pressure in LOOP_INIT and applicable instruments rather than reproducing them in the successor. A/B must be settled before accepting the complete revised protocol. At adoption, the owner also directs removal of the candidate-only header/status labels from the reviewed entry and selected target; those labels are not changed to accepted here. Owner separately selects the successor and moves CURRENT_WORKPLAN; merge alone is not represented here as that selection. A refreshed seating steer must rebase R17's dated basis/receipt references and seat outstanding DEL-02-06–12 product contracts before a normal v3 production run. This PR does not perform R17 N0/N2–N4 pathway seating or claim that task complete.

Unselected alternative: retire CURRENT_WORKPLAN outright. Cost: PRD_ROOT D-7 amendment via D-1/owner decision; adapter `coordination` contract and G1 expectations; practitioner fixture/loader expectations; root entrypoint references; G4 coverage for protected paths; root acceptance and downstream derivative/export disposition. Deleting a pointer as “hygiene” is not lawful adoption of this alternative.

## Item D — root launcher repairs and M2/G4

Exact diff: `init/dev-loop-init-prompt.md` only. §2 points to Root LOOP_INIT discovery rather than declaring a plan to open lanes; §5 points to Piping's live loop without embedding its plan-loader choice; §6 drops the retired App standing-plan claim and points to its live loop. Project launchers, project content and concurrent Piping/PEC rewrites are untouched. These pointer repairs can be ruled independently now and remain true under the accepted or candidate Root entry text.

Manifest: `docs/governance_harness/tranche_manifests/ROOT-LOOP-CONSOLIDATION-20260905.yaml`, independent M2 authorization = current task's explicit item D preparation and G4 direction; owner merge pending, self_merge false. Declares launcher and manifest itself. M6 none-required rationale: changes only this repository's root launcher catalog, no shared agent/skill/canon changes, no project mirror adoption asserted; no `agents/` change-notice rule triggered. Owner may route follow-on coordination at acceptance; no foreign-loop writes are made here.

## Dry-run acceptance and validation

Fresh read-only native child gets only frozen candidate text plus execution constraints, no handoff or parent analysis. It follows that text's discovery pointers; parent concurrently completes the separation record. Launch terms, candidate identity, native child identity, complete returned finding inventories, friction dispositions and final coverage verdict are retained in the run evidence. If behavior misses the first-return contract, revise and use another fresh child; no remembered response counts as a fresh trial. See `DRY_RUN_ACCEPTANCE.md` and `VALIDATION.md` there for actual outcomes (not assumed passes).

Required battery: instruction entrypoints; candidate whitespace versus origin/main; G0–G4; live-path practitioner self-check; affected tests versus origin/main; committed-range G4 with --added-manifests-only. Frontend/runtime builds are not pertinent to this documentation/control-plane-only diff. Manual no-foreign-write, no-pointer-write, exact old receipt prefix and source/candidate hash checks supplement the machine checks.

## Ruling slate and handoff

- D can be ruled now by exact diff. A's map/triage/check design can be reviewed now; accepting its full selection protocol needs the explicit R17 control-plane exception.
- B is itself the exact supersession decision, not a task needing a prior supersession. A's run-branch gate class and full run protocol depend on B.
- C is reviewable now; effective target selection needs the owner’s R17 protocol-location amendment and separate pointer act. A–C should be settled as one coherent adoption set if the owner wants the entire post-image.
- The separation assessment asks whether to retain current Root identity while naming practical surfaces, commission a bounded runtime separation design, or initiate broader PRD/decomposition retirement analysis. No option is selected by this packet.

Closure: `CANDIDATE_COMPLETE_FOR_OWNER_REVIEW` only after the recorded dry run and checks pass; no governed acceptance, Root production phase, pointer move or R17 seating closure. Accepted upstream is pinned main plus cited accepted PRD/decomposition/owner acts. These records and run evidence are derivative decision support, never decomposition truth. Root handoff narrative is deliberately not rewritten; this new run's handoff and next receipt carry current deltas. Export/mirror regeneration is deferred until adoption of instruction bytes; no release is claimed. On main drift or owner amendments, recheck authority, intersections, entry behavior and required validation. Next owner: Ryan Tufts.
