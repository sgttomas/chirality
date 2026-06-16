# Six-Node SCC Resolution Plan

**Date:** 2026-06-16
**Epistemic status:** ACTIVE PROPOSAL (non-governing)
**Product:** Chirality desktop harness and bundled agent operating system
**Supersedes as active queue:** `plans/PLAN_2026-06-13_runtime_completion.md`

This plan is the active app-dev tranche-selection surface for resolving the residual
six-node strict dependency SCC before any new broad runtime roadmap is selected.
The retired runtime completion plan remains historical evidence for already-landed
runtime work; it is not the active development queue.

This plan does not change product requirements, decomposition truth, runtime API,
source code, package/runtime requirements, provider scope, network policy,
release-readiness posture, lifecycle issuance, professional approval,
certification, sealing, authentication, or code-compliance posture. Project truth
remains in governed docs, decomposition and deliverable artifacts, source, tests,
evidence records, decision records, and git history. Humans decide all gates.

## Doctrine Adoption

This plan adopts the root doctrine in
`/Users/ryan/ai-env/projects/chirality/docs/CYCLE_DRIVEN_RESOLUTION.md`.

Active SCC work must follow this order:

1. Fix the graph objective and edge semantics before editing rows.
2. Treat the SCC as the objective signal of undecided ordering.
3. Apply agent-proposable `decompose` or `invert` moves before requesting human-gated
   `cut` or `merge` moves.
4. Keep unresolved cycle-participating edges non-gating for blocker queues, wave
   placement, schedule, priority, dispatch readiness, implementation-readiness, and
   project-wide closure claims.
5. Terminate every move tranche in a fresh immutable dependency-closure snapshot.

Cut and merge remain human-gated. Retiring an edge as out-of-objective is a `cut`,
even when the edge looks like interface, conformance, or handoff evidence.

## Current Evidence

Primary SCC evidence:

- `execution/_Reconciliation/DepClosure/_LATEST.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1820/Dependency_Closure_Report.md`
- `execution/_Reconciliation/RECON_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1825/SCC_Ruling_Package.md`
- `execution/_Reconciliation/RECON_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1825/SCC_Edge_Workbook.csv`
- `execution/_Coordination/_DECISIONS/D-APP-07_RULING_2026-06-16.md`

Current residual SCC membership:

| Node | Deliverable surface |
|---|---|
| `DEL-03-01` | AgentEnginePort and Engine Conformance Suite |
| `DEL-03-02` | Thin TurnEngine and Session Locking |
| `DEL-03-03` | Harness API and SSE Compatibility Adapter |
| `DEL-03-04` | Interrupt, Cancel, and Terminal Outcome Handling |
| `DEL-04-03` | SdkMessageMapper and Provider-Neutral Translation |
| `DEL-05-02` | HarnessEvent Schema and Append-Only JSONL |

The current DepClosure evidence reports one strict SCC of size 6 and 15 internal
cycle-participating active deliverable execution rows. `D-APP-07` rules that this
SCC blocks project-wide strict dependency-closure claims only; it does not unwind
already-landed bounded R5 work and does not approve dependency-register edits.

## Plan Maintenance

This plan is a selection instrument, not a history. When an item lands, compress
its row to one line with:

- `LANDED <date>`;
- tranche id, or commit when no tranche id exists;
- residual handoffs;
- validation pointer;
- a link to `plans/PLAN_COMPLETION_LOG.md`.

Move narrative detail to `plans/PLAN_COMPLETION_LOG.md`. Partially landed rows
keep remaining scope here and move landed detail to the log. Decision rows carry
only state, packet pointer, and ruling pointer.

## SCC Resolution Spine

Select the earliest unblocked item in this table unless regression repair is
needed for already-landed SCC/control-plane work or the human explicitly approves
a different tranche.

| # | Tranche | Scope | Acceptance / validation |
|---:|---|---|---|
| 1 | **SCC-SAFE-MOVES-001** | LANDED 2026-06-16. Applied six source-grounded `decompose` moves only; no cut, merge, out-of-objective retirement, decomposition-topology change, or closure claim. Detail: `plans/PLAN_COMPLETION_LOG.md`. | Validation: touched `Dependencies.csv` schema checks passed; fresh immutable snapshot `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/Dependency_Closure_Report.md` reports `Strict SCC count = 0`. Proceed to row 2. |
| 2 | **SCC-CLOSURE-AUDIT-001** | Review the fresh DepClosure snapshot from row 1, update `execution/_Reconciliation/DepClosure/_LATEST.md` if the snapshot is accepted, and record whether strict SCC count is now 0. | If `scc_count = 0`, proceed to row 4. If any SCC remains, proceed to row 3. No project-wide closure claim is allowed until evidence shows strict acyclicity. |
| 3 | **SCC-HUMAN-GATED-MOVES-001** | Prepare a decision packet for any remaining `cut`, `merge`, or objective-dependent move. The packet must name exact dependency IDs, current row text, proposed move, rationale, risk, and validation implication. | `_DECISIONS/_REGISTER.md` records the packet as `AWAITING_RULING`. No dependency-register cut/merge edits occur until a ruling record lands. |
| 4 | **SCC-CLOSEOUT-001** | Once a fresh DepClosure snapshot proves strict `scc_count = 0`, update control-plane handoff state and planning surfaces to record closure. | Closure evidence points to immutable snapshot; control surfaces stop carrying project-wide dependency-closure warning for this SCC. Frontend runtime tests remain skipped unless runtime source changed. |

## Safe-Move Rules For Row 1

`SCC-SAFE-MOVES-001` may edit dependency rows only when the move is a source-grounded
`decompose` or `invert` under the cycle-driven doctrine.

Allowed move types:

- `decompose`: split a coarse deliverable-to-deliverable edge into a more precise
  non-strict evidence/interface target, such as a documented contract, fixture,
  compatibility surface, or already-landed implementation seam, while preserving the
  original evidence in `Notes`.
- `invert`: reverse a dependency only when the row is demonstrably recording evidence
  flow, handoff wording, or validation consumption rather than execution precedence.

Not allowed without a later human ruling:

- `cut`: retiring an edge, marking an edge out-of-objective, or changing a row solely
  to remove it from the strict graph.
- `merge`: treating multiple deliverables as one indivisible work unit.
- decomposition package changes, new deliverable IDs, package topology changes, or
  project-wide closure claims.

Rows currently participating in the SCC:

| Dependency ID | Current graph edge | Current row character | First-tranche treatment |
|---|---|---|---|
| `DEP-03-01-005` | `DEL-03-01 -> DEL-03-03` | Conformance / interface evidence | Candidate decompose only; cut requires ruling. |
| `DEP-03-02-006` | `DEL-03-02 -> DEL-03-01` | Engine boundary interface | Preserve unless a narrower contract target is source-grounded. |
| `DEP-03-02-007` | `DEL-03-02 -> DEL-05-02` | Runtime event persistence interface | Preserve unless a narrower event-writer contract target is source-grounded. |
| `DEP-03-02-008` | `DEL-03-03 -> DEL-03-02` | SSE compatibility / lifecycle handoff | Candidate decompose or invert only if source evidence supports it. |
| `DEP-03-02-009` | `DEL-03-04 -> DEL-03-02` | Lock cleanup / cancellation boundary | Preserve unless decomposed into a narrower lifecycle-boundary target. |
| `DEP-03-03-006` | `DEL-03-03 -> DEL-03-02` | TurnEngine lifecycle delegation | Candidate decompose only if the current TurnEngine boundary is the precise target. |
| `DEP-03-03-007` | `DEL-03-03 -> DEL-03-04` | Interrupt/cancel ownership boundary | Preserve unless decomposed into a documented terminal-outcome contract target. |
| `DEP-03-04-006` | `DEL-03-04 -> DEL-03-01` | Runtime boundary prerequisite | Preserve as a hard prerequisite unless evidence proves a safe decompose/invert move. |
| `DEP-03-04-007` | `DEL-03-04 -> DEL-03-02` | Active-turn locking prerequisite | Preserve as a hard prerequisite unless evidence proves a safe decompose/invert move. |
| `DEP-03-04-009` | `DEL-03-04 -> DEL-05-02` | HarnessEvent writer prerequisite | Preserve as a hard prerequisite unless evidence proves a safe decompose/invert move. |
| `DEP-04-03-008` | `DEL-04-03 -> DEL-03-01` | Engine contract ownership boundary | Candidate decompose only; cut requires ruling. |
| `DEP-04-03-009` | `DEL-04-03 -> DEL-03-03` | Browser event-name compatibility | Candidate decompose only; cut requires ruling. |
| `DEP-04-03-010` | `DEL-05-02 -> DEL-04-03` | Mapper-to-event-log handoff | Candidate decompose or invert only if source evidence supports it. |
| `DEP-05-02-011` | `DEL-05-02 -> DEL-03-03` | HarnessEvent / UIEvent separation | Candidate decompose only if a precise UI/runtime contract target exists. |
| `DEP-05-02-012` | `DEL-05-02 -> DEL-04-03` | SDK-message mapper interface | Preserve unless decomposed into a precise mapper contract target. |

If row 1 cannot reduce the SCC without a cut or merge, stop after recording that
finding and proceed to `SCC-HUMAN-GATED-MOVES-001`.

## Guardrails

- Do not treat `docs/PLAN.md` as the active queue; it remains strategic roadmap
  context.
- Do not revive the retired runtime completion plan as a work queue.
- Do not expose new runtime, write/edit/bash/network/subagent, provider, Pi, package,
  dependency, or desktop-wrapper behavior under this SCC plan.
- Do not implement Pi adapter, fork, import, sidecar, runtime-floor migration, or spike
  work. Pi remains pattern corpus/reference only after `D-APP-01` and `D-APP-02`.
- Do not implement concrete non-Anthropic providers or provider routing under this plan.
- Do not turn runtime events, SDK transcripts, completion logs, handoff prose, closure
  snapshots, or coordination state files into project-truth substitutes.
- Do not recreate `execution/_Coordination/NEXT_INSTANCE_STATE.md`.
- Do not advance release-readiness, lifecycle, professional, certification, sealing,
  authentication, or code-compliance claims.
