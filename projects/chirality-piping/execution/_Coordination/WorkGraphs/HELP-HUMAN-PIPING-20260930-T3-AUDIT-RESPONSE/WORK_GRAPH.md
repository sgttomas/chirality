# Work graph — T3 audit response

## Intent and selected route

- **Stable run identity:** `HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`.
- **Current phase:** preflight returns received; guard qualification and A0 preparation next. The owner directed “Proceed accordingly.”
  after the plan; actual manager/TASK launches are recorded as they occur.
- **Active role:** HELP_HUMAN, Agent 0, adopted at the owner's explicit request
  in the new conversation turn after the audit/merge handback. Earlier audit
  history and its limitations remain part of the record.
- **Owner steering:** “Adopt the role of agent `HELP_HUMAN` in the Agent 0 mode
  and plan out your execution of work with an effective agent delegation strategy.”
- **Host correction from the owner:** this session runs on an M3 MacBook Air
  with 16 GB unified memory. The earlier T3 work ran on an M5 Max MacBook Pro
  with 128 GB. Tests may run here with careful resource control; the earlier
  host's concurrency, caps, timings and available scratch must not be assumed.
- **Interpretation:** execute the bounded response to the merged T3 audit,
  building on A1 investigation, K6c and evidence closeout. Activation does not
  claim that implementation has started or that the whole T3 loop has resumed.
  See `Run/ACTIVATION.md` for the owner direction and initial grants.
- **Intended result:** independently dispose of the audit findings; close A1's
  published-bound assurance with evidence; complete K6c's memory estimate,
  deduplication and measurements; prepare the W1 limit decision and a usable
  handback to the continuing T3 work.
- **Priority:** correctness of the published guarantee, then a sound memory
  estimate and final measurements, then concise records closure. An inability
  to find a failing solver case alone does not close a proof gap.
- **Planning method:** `chirality-root:bundled:workflow:construct-local-work-graph`,
  from `workflows/construct-local-work-graph/WORKFLOW.md`. This is a run-specific
  graph, not a new reusable workflow or instruction amendment.
- **Checked basis:** main `3bddc2b05f6106e969c7cf43373b230845c7cc66`, the merge of
  audit PR #1064. No other open Piping T3 PR was found; the unrelated live-control
  PR #885 remains outside this undertaking. Refresh both facts before launch.
- **Parent undertaking:** `HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`, T3 row
  and audit-pause paragraph. This graph governs only the proposed audit response;
  it is not a competing current account of the full parent undertaking.

Aliases are repository-relative unless stated otherwise:

- `P`: `projects/chirality-piping`.
- `T3`: `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3`.
- `Run`: `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`.
- `FK`: `P/core/solver/frame_kernel`; `H`: `P/core/solver/performance_harness`;
  `VR`: `P/validation/benchmarks/numerical_robustness`.
- `<response-wt>`: the isolated runtime/worktree root to be identified at E0.
  It does not silently replace the M5 handoff's missing `<wt>` or `<VENV>`.

## Deliverable scope and dependencies

| Deliverable / basis | What exists | Contribution here | Nodes |
|---|---|---|---|
| DEL-04-01 — 3D frame stiffness kernel; its ScopeOfWork OUT-001 | K4/A1/A2 retained kernel and their accepted/historical design records | A1 proof/reachability disposition and, if warranted, a narrowly bounded retained-kernel repair | A0, A1, V1, D1, I1, V2, P1 |
| DEL-04-05 — Sparse solver performance harness; its ScopeOfWork OUT-001 | K6b H estimate and the existing I21 K6c brief | Complete K6c and produce reliable work/memory observations | K0, I21, T21, V21, P21, L0 |
| DEL-09-01 — Mechanics benchmark suite; its ScopeOfWork OUT-001 | R1/VP-ROBUST evidence, VR and its duplicated estimate | Independent oracles, admission replay and VR estimate consistency; precise maintained-path binding confirmed at B0 | V0, A0, V1, I21, T21, V21 |
| DEL-04-07 — Product solve integration; CLM-001/004 | Product/facade owns source, diagnostic and result handoff | D2/F2a consequence assessment and downstream handback; no F2a implementation in this response | A1, D1, L0, C0 |
| Parent T3 coordination and audit | #1064 records are merged; independent V0 review has returned | Post-merge audit review, additive errata, evidence inventory and recovery | V0, E0, N0, C0, F0 |

`P/execution/_DAG/_LATEST.md` points to DAG-011. Relevant local execution
dependency records were inspected: DEL-04-05 and DEL-09-01 name DEL-04-01 as
an upstream prerequisite at SEMANTIC_READY with satisfaction TBD; DEL-04-07's
corresponding edge has satisfaction PENDING. Neither graph ancestry nor the
audit merge satisfies these edges. B0 must check the latest currency audit and
the specific evidence needed by this bounded undertaking. No project-deliverable
readiness or dependency-satisfaction verdict is made by this plan. Discovery
and diagnosis can establish the missing evidence without asserting completion.

Retain outside this response: F2a/S-I/F2b/F3 implementation; the parent's other
T3-close obligations; KF3-B1's lambda-split decision; KF2's dense-screen change;
the owner's provisional dense/lane ceilings and PHYS-R4 decisions; public
release, engineering acceptance and unrelated project work. They keep their
existing homes and holds.

## Agent 0 and delegation

I retain cross-lane alignment, the graph, Git/index operations, PR integration,
the host slot and communication with the owner. Managers integrate their
children's findings and proposed changes logically; only Agent 0 changes refs,
stages, commits, pushes or merges. Children may read Git, including `git show`
and `git archive`, but may not fetch, reset, checkout, merge or use intent-to-add.

| Planned agent | Role | Bounded responsibility | Return and write boundary |
|---|---|---|---|
| ROOT | HELP_HUMAN / Agent 0 | Coordinate this response; resolve routine in-scope choices; prepare reserved decisions for the human; integrate gated PRs | This graph, sealed briefs, central decision/host records and Git operations; old ROOT_RULINGS remains read-only |
| DESIGN | HELPS_HUMANS / Agent 1 | Develop A1's proof/reachability question into a verified design basis and assess D2 consequences | Own design drafts under `Run/instances/DESIGN/`; no product edits or independent approval of its own proposal |
| DELIVERY | WORKING_ITEMS / Agent 1 | Recover the environment/evidence, manage K6c and any selected A1 implementation, reconcile returns | Own management records under `Run/instances/DELIVERY/`; children receive exclusive write fences; graph changes return to ROOT |
| AUDIT-REVIEW | Fresh TASK, directly under ROOT | Challenge all four audit findings, prioritize A1, reproduce arithmetic and assess stated limits | Own `Run/instances/AUDIT-REVIEW/`; repository/source read-only; may refute or narrow this audit |
| A1-DIAGNOSIS | TASK under DESIGN | Construct valid unmutated source cases, compare with an independent exact oracle and classify reachability | Own scratch/probe and `Run/instances/A1-DIAGNOSIS/`; no production patch during diagnosis |
| I21-K6C | TASK under DELIVERY | Execute the existing K6c brief in stages, beginning with checkpoint 0 | Existing I21 write set, with a sealed basis/addendum; FK/retained excluded |
| A1-IMPLEMENTATION | TASK under DELIVERY, only if D1 selects a repair | Implement the accepted A1 basis and discriminating tests | Exact retained/test/consumer paths sealed after design; no blanket VR or H access |
| ENV-EVIDENCE / RECORDS | Bounded TASKs under DELIVERY, sequential where practical | Runtime inventory/recovery and additive replay/process/evidence records | Own run folders; approved recovery targets only; no deletion of original work |
| DESIGN-VERIFY, A1-REVIEW, K6C-REVIEW, FINAL-REVIEW | Fresh TASK per independent review scope, directly under ROOT | Independently check the design or complete frozen candidate they did not author | Read-only source and independent scratch; each writes only its review folder |

Reviewers are not the authors or implementers of their reviewed outputs.
The current Agent 0 authored the audit and therefore cannot supply its
independent review. Managers may critique work but their integration checks do
not replace independent review. A reviewer may confirm fixes to its own initial
findings; a different slice gets a fresh reviewer. Same-model independence is
not reported as model diversity.

### Actual launch mechanism and supplied context

Use Codex native `collaboration.spawn_agent` descendants under D-GOV-35, not
new user-owned chats. Managers may dispatch bounded TASK descendants within
the granted slots; Type 2 agents do not delegate. A written brief and an
executing child are recorded as different facts. Actual initial IDs and sealed
brief hashes are in `Run/launches/01_INITIAL.json` and `02_ENV_EVIDENCE.json`.

Every launch starts fresh (`fork_turns="none"`) with its complete sealed brief:
purpose, exact base SHA, Root/project/own-role instructions, selected method
origins, relevant design/rulings, accepted inputs, explicit read/write targets,
check commands, resource limits, stops and return contract. Load only the role
and skills needed for that assignment. Inherit the configured model unless
the owner directs an override; do not infer model diversity or another engine.

Record actual parent/child IDs, source-qualified selections, paths and hashes,
launch mechanism, supplied brief, actual model information available from the
host, enforcement limits, returns and changed candidates in the run evidence.
The role bodies of both managers were deliberately consulted for this planning
task; `PLANNING_BASIS.json` records that wider consultation.

Scopes in prompts are not per-agent OS sandboxes. The native agents share the
filesystem. Separate worktrees/scratch, exclusive ownership and checked diffs
provide practical isolation; actual host permissions remain the outer boundary.
Do not describe an unenforced write fence as an enforced capability restriction.

### Concurrency and scheduling

- Maximum initially: Agent 0, two managers, and **two active TASKs** (five
  agents total). Keep spare slots for replacement/review; do not fill capacity
  merely because it exists. Managers stay lightweight; only one TASK may hold
  the heavy-work slot. Idle managers need no polling work.
- First wave after activation: AUDIT-REVIEW and ENV-EVIDENCE. I21 checkpoint 0
  takes the next available TASK slot.
  DESIGN reads and prepares questions while the audit premise is independently
  checked. These tasks need no heavy build.
- Second wave: A1 diagnosis/design, K6c derivation/test planning and additive
  records work. K6c source implementation may overlap A1 implementation after
  D1 establishes the design impact. Rotate a finished task's slot
  to its independent reviewer instead of accumulating idle authors.
- **One global heavy-work slot on the M3 Air.** Start with one cargo job at
  `-j 1`, `RUST_TEST_THREADS=1`, the pinned toolchain/offline/locked settings, and a
  target owned by the slice. Timed measurements exclude other builds and
  heavy Python. Lightweight independent reading can continue.
- Use one pytest worker and similarly conservative JavaScript test workers
  through supported runner options where relevant. Record these host adaptations
  explicitly; preserve test inventory, assertions, tolerances and required gates.
  Do not use the previous host's `-n auto`, load-average thresholds, 8/16-GiB
  runner caps or concurrent-build practices without a new host derivation.
- Before each grant, check the memory guard actually covers the new targets,
  available memory and existing host jobs. Never materialize a dense matrix
  with 10,000 or more members. Keep original worktrees/targets intact.
- E0 defines a conservative operating budget for this host. Start observation
  processes with at most a 2-GiB cap unless the measured admission calculation
  supports another value; account separately for heap, RSS, physical footprint,
  the OS and the owner's other applications. This is a proposed host protection
  setting, not an engineering criterion or a proved memory bound. Preserve at
  least the earlier 35% available-memory reserve and stop own process groups
  on guard/pressure events; do not kill unrelated applications or retry blindly.
- Ascend through tiny/10/100-member cases, then 1,000 members only after measured
  projections pass. Run each larger case alone. The 10,000-member W1 tier is
  **conditional**, not pre-admitted: final formulas, M3 measurements and current
  headroom must support it with margin. A named resource refusal remains a
  refusal, never a passing numerical result. Preserve the independent binary
  backstop; do not force a scale run through an estimate-bypass switch.
- M5 figures remain historical evidence. Establish a same-M3 base/candidate
  comparison for platform tests and any performance claim; do not presume the
  M5's three platform failures or its measured rho apply here. Record load and
  thermal context, and use interleaved runs for timing comparisons.
- If a required scale run or full gate cannot fit safely, preserve completed
  work and prepare a pinned run packet for a suitable host, potentially the M5.
  Obtaining access is a human coordination matter; it is not an available remote
  capability today. Leave that gate outstanding instead of weakening it.
- A1 and K6c may prepare disjoint changes concurrently. K6c's final formula,
  measurements and limits must cover the final A1 kernel, or a checked proof
  that A1 changes no relevant allocation/work behavior. If both need VR,
  ROOT assigns one writer and serializes that shared delta before proceeding.

## Work

Execution states below distinguish activation from actual dispatch. Prerequisites express required results,
not inferred project-DAG satisfaction. A resource or decision hold is recorded
as BLOCKED only when the corresponding execution node is activated and its
specific missing input is established.

| ID / owner / outcome | Deliverables and write scope | Needs / why | Completion check | State |
|---|---|---|---|---|
| PLAN — ROOT: recoverable execution plan | New graph and `Run/PLANNING_BASIS.json` only | Current owner role/planning direction | Acyclic route, explicit owners, bounded scope and launch status | COMPLETE as a planning artifact; not execution acceptance |
| B0 — ROOT + DELIVERY: seal response basis | Run brief/ownership/dependency records | Refresh main, existing agents/PRs, relevant DAG currency and parent holds | Exact source/instruction basis; no competing writers; deliverable mappings justified; legacy I/RV identifiers checked | COMPLETE for bounded investigative basis: 58 rows structurally agree; source-binding/pointer/VR-accounting limits retained in DELIVERY return; no dependency promotion |
| V0 — AUDIT-REVIEW: independently assess #1064 | Audit read-only; own review folder | B0 frozen audit/source basis | Each finding confirmed, narrowed or refuted; A1 arithmetic and reachability limits assessed; no retrospective claim of pre-merge review | COMPLETE: independent review accepted for fan-in; AUD-REV-N1 routed to N0; `Run/decisions/01_FIRST_WAVE.md` |
| E0 — ENV-EVIDENCE: executable host and preserved inputs | Own runtime inventory and explicitly scoped copies | B0; M3 Air 16-GB constraint | Distinguish M5 resources from local replacements; guard and memory admission verified; toolchain/venv/targets identified; same-host baseline planned; raw evidence recovered or missing items inventoried | ACTIVE overall: eight small live guard fixtures and one tiny direct compile completed; v2/controller repairs independently closed; B02 exposed a zombie/reaped-child sample race and v3 source repair returned and independent backcheck is active; broader environment/command qualification remains open |
| K0 — I21-K6C: checkpoint-0 derivation | H/VR/FK read-only; K6c plan and evidence draft | B0, existing I21 brief | Complete live-allocation phase table, corrected formula candidate, dedup design, admission/reproduction plan and tests | ACTIVE SOURCE CLOSURE: initial checkpoint returned with 36 admissions reproduced; I21 resumed for K0-S1/S2 against pinned Rust sources; L1/V1 and final formula remain open |
| A0 — A1-DIAGNOSIS: determine realized-input consequences | FK/proof read-only; independent probes and oracle | V0; E0 for Rust runs | Valid-source probes and independent truth; confirmed defect or explicit unclosed proof question; exact reproducer and limits | PARTIAL B RETURNED: ROOT compile succeeded; B01 clean with 37 honest rows; B02 guard-failed despite honest forensic rows; B03–B16/all C remain unrun; resume awaits guard repair/qualification |
| A1 — DESIGN: propose A1 closure | Design addendum and D2 consequence draft in own run folder | V0, A0 | Complete error transfer through both coupling directions, zero scales and thresholds; remedy or proved exclusion; alternatives and tradeoffs | PLANNED |
| V1 — DESIGN-VERIFY: verify proposed basis | Own independent proof/probe records | Frozen A1 proposal | Every material claim checked independently; failures returned with evidence | PLANNED |
| D1 — ROOT / human where reserved: select warranted course | New response decision record; no old ruling rewrite | V1 and concrete consequences | In-scope decisions recorded; human decides reserved contract/scope/availability/acceptance changes; design basis explicitly selected before repair | PLANNED |
| I1 — A1-IMPLEMENTATION: bounded repair if needed | FK retained/tests and exactly declared consumer changes | D1, E0; exclusive files | Implementation matches selected basis; oracle/boundary tests and reverted-fix mutant discriminate; outcomes/work/allocations reported | PLANNED; may become not-needed only by evidenced D1 disposition |
| V2/P1 — A1-REVIEW then ROOT: integrate A1 closure | Full frozen A1 diff and its records | I1, or D1's justified non-code closure | Independent review; applicable tests, exact-head CI/full-SHA dispatch, Mac DEC-025 and GEN-8 for repair; merge identity verified | PLANNED |
| I21 — I21-K6C: estimate and dedup implementation | Existing brief's H/VR/test/record fence | K0 accepted, E0; D1 impact understood and shared files assigned | Single estimate definition; corrected terms/regenerated counts; regression tests and mutants; no FK edit | PLANNED; provisional preparation can overlap I1 |
| T21 — I21-K6C: final measurement and admission evidence | K6c records; owned target/scratch | P1 or its justified no-code disposition; final I21 tree; quiet host slot; each size admitted from M3 evidence | Final kernel phase model checked; original admissions replayed; required six sparse/W1 10,000-member cases and prefixes/repeats recorded on a host that can safely admit them; any unrun case remains open | PLANNED; M3 feasibility not established |
| V21/P21 — K6C-REVIEW then ROOT: integrate K6c | Full frozen estimate/dedup/evidence diff | T21 | Independent phase derivation/checks; VR suite and kill matrix; applicable exact-head CI/full-SHA dispatch, DEC-025, GEN-8; merge verified | PLANNED |
| N0 — RECORDS: close replay/process/evidence notes | New errata/inventory under own run records | V0, E0 evidence results | Five manifest bases stated; Git exceptions separated; preserved/missing raw inputs explicit; no fabricated reconstruction or immutable rewrite | ADDITIVE NOTE PREPARED: `Run/REPLAY_AND_PROCESS_ERRATA.md`; originals unavailable for now, safe fresh evidence authorized; independent slice review active |
| L0 — ROOT with DELIVERY analysis: W1 limits and F2a inputs | Evidence-based limit proposal/operational decision and handback | P1, P21 final compatible basis | Limits trace to final measurements/derivation; owner-held dense/lane ceilings unchanged; F2a assurance inputs and remaining holds explicit | PLANNED |
| C0 — DELIVERY, ROOT integrates: bounded closeout | Selected deliverable comparisons, warranted docs, one central receipt and terse MEMORY rows | Technical integrations, N0, L0 | Bounded reconciliation; conditional Task Management only for genuinely unallocated concerns; no required work hidden by transfer | PLANNED |
| V99/F0 — FINAL-REVIEW then ROOT: final response PR | Complete records/graph/closeout diff | C0 and all reserved decisions satisfied | Fresh independent final review, applicable records CI/GEN-8, current-main check, final PR merged; parent continuation handback explicit | PLANNED |

The intended critical sequence is V0 -> A0 -> A1 -> V1 -> D1 -> I1/P1 ->
T21 -> V21/P21 -> L0 -> C0 -> V99/F0. E0 and K0 begin alongside V0; I21
preparation overlaps A1 work as its input stability permits. N0 is independent
records work once its factual inputs exist. Any newly required production work
returns to this graph rather than disappearing into closeout.

## Briefing, reviews and integration

Before launch ROOT seals each manager brief; each manager seals its TASK brief
within the granted authority. Each return names the exact head/tree, files
changed, commands/results, evidence hashes, open questions and next condition.
Verify that an authorized launch actually started; a sent/queued message is
not proof of execution. Track returned statuses and ignore duplicate handbacks.

Use `software-defect-diagnosis` for A0 and `software-code-review` for bounded
software reviews when those tasks begin. Read their current bodies and retain
their actual origins then. The catalog was consulted for this plan; only the
selected graph workflow was loaded. Select `chirality-root:bundled:workflow:bounded-reconciliation`
at C0 and load only the resources needed then.

Keep PRs coherent: an early records/plan/audit-review packet; A1 design/closure
PR(s) as its decision requires; a separate K6c repair PR; one final bounded
closeout PR. Include the documentary consequences with the slice that causes
them. Do not create a later commit solely to restate a final merge result.

Reviews/checks cover actual candidates. Any merge-resolution or later change
gets the affected recheck and reviewer confirmation. Immediately before merge,
verify main and the candidate; integrate and re-gate affected changes when
needed. No force pushes or protection bypass. The owner-directed #1064 merge
with review outstanding is not carried forward as a general review waiver.
Independently review this planning packet before merging it.

Consequential choices go to the human as concrete proposals: narrowing the
guaranteed domain, changing published contracts/standing, changing accepted
criteria, unresolved ownership conflicts, or scope expansion. ROOT handles
routine implementation choices within the existing brief and authority.
Do not add a human checkpoint merely because a test needs repair.

Stop the affected path and report on a false publication, unexpected change to
accepted outcomes, surviving required mutant, memory peak above the final bound,
unapproved write, conflicting writer or absent required host protection.
Independent work may continue. Never relax a protected oracle/tolerance to pass.

## Current state and recovery

- **Current graph ref:** `codex/piping-t3-audit-response-plan-20260930` (local
  response coordination branch, not merged).
- **Graph maintainer:** HELP_HUMAN Agent 0 in this chat; managers return proposed
  state changes for one serialized integration.
- **Active operations:** I21 source closure and guard v3 independent backcheck occupy the
  two TASK slots. No heavy job is active. ROOT's one permitted host retry built
  the A0 probe in 3.82 s after the child attempt timed out before process creation.
  B01 completed; B02 stopped on a zombie/reaped-child identity race. Its exact
  latch was resolved only after fresh absence/group checks; no remaining B or
  C case ran. DESIGN is drafting closure options without a child or selection.
- **Next safe action:** independently review and qualify the bounded guard exit
  handling repair, then explicitly retry B02 and finish the B controls before
  the separate C extension. I21 continues source accounting; L1 stays unapplied
  and uncompiled. Preserve every prior refusal and sealed artifact.
- **New owner evidence direction:** M5 originals are unavailable for now. Safe
  recreated inputs and new M3 runs are authorized and must carry new provenance;
  they do not impersonate historical logs. See decision 03. Recovery remains
  low priority unless a discrepancy makes it necessary.
- **Shared surfaces:** this graph and response control records belong to ROOT.
  `T3/ROOT_RULINGS_V1.md` and earlier hash-bound audit/T3 evidence remain
  read-only under the owner's existing instruction. Proposed dispositions go
  in new response records for explicit integration by their owning authority.
- **Close condition:** the bounded response's required nodes, review and
  decisions are complete and its final PR has merged. This does not close all
  T3, implement F2a, issue deliverables, or release the product.
- **Deferred work:** KF3-B1 and dense-screen questions retain the parent T3
  owners; provisional ceilings/PHYS-R4 retain the owner's decision; all parent
  T3-close obligations remain at their historical loci. AUD-T3-01 remains open
  until D1/P1 evidence closes it. Missing old evidence stays explicitly missing
  until recovered or dispositioned; new reruns are not old logs.

| Completed result | Evidence | Remaining consequence |
|---|---|---|
| Audit packet integrated | PR #1064, merge `3bddc2b05f6106e969c7cf43373b230845c7cc66` | V0 independently confirms the audit with qualifications and one replay NOTE; A1 proof closure and source/design acceptance remain open |
| HELP_HUMAN role and response plan prepared | This graph and `Run/PLANNING_BASIS.json` | Managers and bounded TASKs launched with recorded returns; no project readiness or governed acceptance is implied |
| Host constraint corrected | Owner: M3 Air 16 GB here, M5 Max 128 GB previously. Read-only `memory_pressure -Q` reported 17,179,869,184 bytes total and 56% system-wide memory free during planning; `sysctl` query was denied by the sandbox | One snapshot is not sustained headroom or admission for a heavy run; E0 must establish the operating budget and guard |
