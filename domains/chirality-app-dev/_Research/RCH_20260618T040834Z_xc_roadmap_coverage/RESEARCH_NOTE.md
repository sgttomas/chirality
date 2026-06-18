# Research Note - Roadmap R0-R7 Acceptance Coverage (chirality-app-dev)

Status: DERIVATIVE_RESEARCH_PACKET

## Question
For each roadmap phase R0-R7 in `projects/chirality-app-dev/docs/PLAN.md` §4, which acceptance
criteria are MET by landed work vs still OPEN? Confirm R0-R6 landed status against the live tree
and the prior completion log. Identify the single largest remaining roadmap gap and whether it is
code, evidence, or a human ruling.

## Accepted Basis
- Accepted basis: live execution tree + git HEAD `aaf9348a209cf5bfc4510cc231617aaddbef35df` of
  `projects/chirality-app-dev`.
- Retrieval snapshot `SRCIDX_20260616T043733Z` (STALE, CONTENT_DRIFT, 49/660 artifacts changed) —
  used for DISCOVERY only.
- Roadmap authority: `docs/PLAN.md` §4 (R0-R7). Completion narrative: `plans/PLAN_COMPLETION_LOG.md`.
  Decision authority: `execution/_Coordination/_DECISIONS/_REGISTER.md`.

## Short Answer
R0-R6 are substantially LANDED and verified against the live tree: the runtime spine (AgentEnginePort,
TurnEngine, engine conformance), R1 opt-in `agentSdk` adapter, R2 read surface + Chirality MCP, R3
write surface + hooks + mutating MCP, R4 bash policy, R5 executable governed subagent bridge, and the
R6 extensibility/MCP-boundary program (closed). The full frontend suite is green (54 files / 383 tests,
:RUN). R7 (Domain Engine Profiles = PKG-10) is explicitly a FUTURE AMENDMENT and ALL its acceptance
criteria are OPEN. The single largest remaining roadmap gap is a HUMAN RULING, not code or evidence:
D-APP-18 (bounded default-provider cutover) is the only AWAITING_RULING decision; it blocks making
`agentSdk` the default. The LP-04 live packaged read-tool proof already PASSED, retiring the last
technical unknown, but the proof does not itself authorize the cutover.

## Evidence
Per-phase acceptance verdict (live-verified; see `Evidence_Map.csv`):

| Phase | Verdict | Key live evidence |
|---|---|---|
| R0 Scope/probe/reliance-boundary | MET (with doc-naming gap) | CONTRACT.md K-* invariants, PKG-01, runtime_engine_contract.md; first-adapter probe proven through STAB/LP. Named `runtime_scope.md`/`reliance_boundary_register.md` files absent (AM-001). |
| R1 First-adapter/contract/TurnEngine/audit | MET | engine-conformance.ts (7 tests RUN green); turn-engine.ts; runtime.ts default=`stub`, agentSdk opt-in (D-APP-12 Option B hold). |
| R2 Read surface + Chirality MCP | MET | permission-overlay.ts; chirality read MCP; descriptor registry. |
| R3 Write surface + hooks | MET | chirality-hooks.ts (Pre/PostToolUse); tool-path-policy.ts; STAB-04 mutating MCP (status_transition/deps_write) with human-gate. |
| R4 Bash + budgeting + context mirror | MET | tool-shell-policy.ts deny-by-default + timeout (D-APP-04). Caveat: no dedicated test file (noted limitation). |
| R5 Governed subagent runtime | MET | subagent-bridge.ts `v2.executable-r5` / D-APP-10 Option C; fail-closed preflight; subagent + governance tests RUN green (12). |
| R6 Extensibility/MCP boundary | MET (program closed) | R6-01..03,05 landed, R6-04 deferred; tool_catalog.md + adding_a_tool.md + collision invariant. |
| R7 Domain Engine Profiles | OPEN (all criteria) | PLAN.md:277 "Future Amendment"; PKG-10 exists but 3_Issued is placeholder only; not authorized. |

Lifecycle: 53 deliverables all `Current State: IN_PROGRESS`; `2_Checking` empty; `3_Issued` dirs hold
only `_Archive`/README placeholders. Zero deliverables traversed the human-gated CHECKING->ISSUED path.

## Interpretation
The roadmap's *engineering* surface R0-R6 is complete and test-proven; the SDK adapter even passed a
live packaged read-tool proof (LP-04). What remains is governance, not implementation: (1) the single
open ruling D-APP-18 gating the default-provider cutover, and (2) R7, which is intentionally out of
scope until a governed amendment + human ruling. The deliverable lifecycle (everything IN_PROGRESS,
nothing ISSUED) is a separate governance observation, not a roadmap-acceptance blocker.

## Caveats
- Retrieval snapshot STALE; all phase verdicts re-verified against the LIVE tree (LIVE_TREE rows).
- R4 shell policy has no dedicated `tool-shell-policy.test.ts`; its module is :READ-verified and only
  :RUN-covered transitively by the aggregate suite.
- PLAN §R0 names two `docs/harness/*.md` files that do not exist; the substance landed elsewhere (AM-001).
- "Substantially landed" for R0-R6 is the PLAN's own controlling characterization (PLAN.md:62-66);
  per-criterion exhaustive trace of every PLAN bullet was not performed for already-closed programs.

## Open Questions
- Should landed+proven deliverables begin formal CHECKING->ISSUED advancement, or is IN_PROGRESS the
  intended steady state? (human-gated; see Open_Questions.csv)
- Does the D-APP-18 ruling, once made, also unblock any deferred R6-04 module organization?

## Handoff / Next Action
- Route D-APP-18 to the human project authority — it is the single largest remaining roadmap gap.
- Route AM-001 (R0 doc-naming reconciliation) and AM-002 (lifecycle advancement question) to SCOPE_CHANGE.
- No accepted truth was modified. RESEARCHER recommends only.
