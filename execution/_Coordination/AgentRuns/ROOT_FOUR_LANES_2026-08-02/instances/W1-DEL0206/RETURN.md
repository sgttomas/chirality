# W1 WORKING_ITEMS return — DEL-02-06 accepted-turn recovery

Status: `HELD_AT_N0 — VALIDATED MANAGER RETURN`

## Coverage

- Package: `PKG-02` only.
- Deliverable: `DEL-02-06` only.
- Run: `DEL-02-06-RUNTIME-SPEC-001` under parent
  `ROOT_FOUR_LANES_2026-08-02`, plan version 2.
- Authority exercised: REQ-027 specification, read-only inventory, evidence
  design, and change planning only.

## Durable return

- Activation record:
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/ACTIVATION_RECORD.md`.
- Validated work graph: same run root, `WORK_GRAPH.json`.
- Exact recovery and evidence plan: same run root,
  `MANAGER_RECOVERY_CHANGE_PLAN.md`.
- N0 manager evidence: same run root, `basis/BASIS_REPORT.json` and
  `basis/N0_RETURN.md`.
- Handoff: same run root, `HANDOFF_STATE.md`.

## Fan-in disposition

No child return is accepted. The N0 child did not terminate with its required
files; WORKING_ITEMS interrupted and rejected it. Independent manager checks
found substantive N0 failures, so N1–N6 correctly remain held:

1. the six mandatory hash-verified authoring-envelope inputs are absent;
2. the live v1.2 decomposition text says candidate/not accepted while the
   SCA-002 Decision Log records accepted/applied/Gate-5-validated state.

S1 independently confirms that conflict: AUDIT_DECOMP structural coverage
passes while authority-state consistency fails (return SHA-256
`3d2a09dd35da0c26bc87a1e156c7b1a5e35fd7875ff9a39d4294b8d6a369a868`).
S1 also proves a second N0 blocker: live `docs/PRD_ROOT.md` still labels
Revision 7 candidate and Revision 6 accepted while the Root handoff and live
D-8 state say Revision 8 adopted. S1's current return SHA-256 is
`a003ec10bd7731cbd038e8b6c4df05ac897cf9f0ea58d2cbda8c889d10017b00`;
it authorizes no reconciliation.

The graph itself is complete and validated for version, selection authority,
posture, N0–N6 nodes, edges, concurrency, disjoint writes, integration owner,
fan-in gates, holds, escalation points, return sequencing, and telemetry
limitation. Both JSON artifacts parse. The accepted `ScopeOfWork.md` validates
as `SOW_V1`, valid, with zero issues.

## Recovery requirements and affected surfaces

The provisional manager plan records REC-001 through REC-016. It requires a
startup barrier before socket exposure, admission, or model activation;
crash-safe/idempotent reconciliation of every persisted `turn.accepted`
without a terminal; exactly one terminal; no provider/model/prompt replay;
stable session/drain accounting; fail-closed malformed or contradictory
history; append-only/redacted evidence; and explicit compatibility review.

Candidate Root surfaces are `session-store.ts`, a new accepted-turn
reconciler, `runtime-service.ts`, `runtime-daemon.ts`, shared terminal
predicates only where necessary, and Root runtime tests. `turn-coordinator.ts`
and `residency-coordinator.ts` require exact invariant/caller review. No App,
PEC, Piping, Tier-0, register, lifecycle, contract, runtime, or release surface
was written. No client is formally classified affected because N2 is held.

## Implementation and executable evidence plan

The plan defines a later six-step implementation/review sequence and ten
restart/replay scenarios: initial orphan recovery; repeated restarts; injected
crash between terminal/status persistence; mixed project/session histories;
malformed/duplicate/failing stores; startup-barrier races; residency drain
ordering; redaction; canonical-log replay; and repeated clean-checkout check
selection. No scenario was executed because REQ-027 and REQ-052 forbid it in
this activation.

## Current verdict, blockers, and next gate

Verdict: `HELD_AT_N0`, not activated for implementation and not closed.

Immediate next gate: the owner/Agent 0 coordinates the owning instruments to
restore or explicitly disposition the mandatory accepted-input packet and
route separately gated current-facing PRD/decomposition acceptance-status
reconciliation while preserving immutable candidate history, then reruns
fresh N0. After N0–N6 complete, the owner must rule the recovery terminal/
payload/identity, duplicate-history posture, and compatibility-epoch effect;
S1 and a lawful Root software-workflow profile must precede any sealed
implementation activation.

Task Management row closure remains excluded and requires its own later
session after applied bytes and executable restart/replay evidence are
accepted.

## Validation and preservation

- `ScopeOfWork.md`: `SOW_V1`, valid, zero issues.
- `WORK_GRAPH.json`: JSON parse PASS.
- `basis/BASIS_REPORT.json`: JSON parse PASS.
- W1-owned candidate whitespace: PASS.
- Runtime/client/lifecycle/decomposition/register write count: zero.
- Commit/push/merge: none.

Derivative status: `INCOMPLETE_HELD`. Rerun requirements and exact blockers
are authoritative only as this manager handoff; they do not amend
decomposition or Scope-of-Work truth.
