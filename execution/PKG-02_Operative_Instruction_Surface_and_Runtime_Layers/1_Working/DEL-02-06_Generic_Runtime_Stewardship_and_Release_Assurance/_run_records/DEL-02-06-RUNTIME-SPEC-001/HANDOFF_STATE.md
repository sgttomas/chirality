# Handoff state — DEL-02-06 accepted-turn recovery first activation

Status: `HELD_AT_N0`

| Field | Value |
|---|---|
| RunID | `DEL-02-06-RUNTIME-SPEC-001` |
| Package / deliverable | `PKG-02` / `DEL-02-06` only |
| Accepted upstream repository | `origin/main@97678a841ef58345c73d3470ed8de57c9b1405d2` |
| Accepted Scope of Work | SHA-256 `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`; validator `SOW_V1`, valid, zero issues |
| Work graph | `WORK_GRAPH.json`, plan version 2, `MIXED`, parsed as valid JSON; N0 interrupted/rejected, N1–N6 held |
| Accepted child returns | None |
| Derivative-package state | `INCOMPLETE_HELD`; planning records are derivative and do not substitute for decomposition truth or accepted source packets |
| Runtime/client effect | None |
| Lifecycle effect | None; `_STATUS.md` remains `INITIALIZED` and was not written |
| Closure verdict | `NOT_CLOSED`; no runtime change or executable restart/replay evidence exists |

## Produced under the authorized first-activation boundary

- exact activation/basis/authority/exclusion record;
- versioned, dependency-complete N0–N6 work graph;
- sealed Agent 2 briefs with disjoint writes and explicit holds;
- versioned read-only recovery-surface amendment;
- source-cited provisional recovery requirements, candidate affected surfaces,
  later implementation sequence, and restart/replay evidence plan;
- basis report proving the current N0 hold.

The recovery plan is in `MANAGER_RECOVERY_CHANGE_PLAN.md`. It proposes sixteen
requirements and ten executable evidence scenarios, including recovery before
socket/admission/model activation, repeated-restart idempotence, crash between
event and status persistence, exactly one terminal per accepted turn, stable
drain accounting, fail-closed malformed/contradictory logs, no prompt replay,
and redacted evidence.

## Current affected-surface verdict

The read-only manager census identifies Root candidate implementation seams in
`SessionStore`, a proposed new Root accepted-turn reconciler,
`RuntimeService`, `RuntimeDaemon`, shared terminal predicates where needed,
and Root runtime tests. `TurnCoordinator` and `ResidencyCoordinator` require
caller/invariant review but are not presumed write targets. App's runtime host
is an observed composition surface only; N2 did not run, so App, PEC, Piping,
Tier-0, and any other client are not classified `AFFECTED` by this activation.
No client write is authorized.

## Blockers

1. All six mandatory hash-verified authoring-envelope inputs named by the
   accepted Scope of Work are absent from the RunID's `accepted_inputs/`.
2. The live decomposition self-labels v1.2 as candidate/not accepted while the
   SCA-002 Decision Log records it accepted, applied, and Gate-5 validated.
   REQ-038 prevents activation fan-out on that contradictory currency proof.
   S1 independently confirms structural coverage PASS but authority-state
   consistency FAIL in AUDIT_DECOMP return SHA-256
   `3d2a09dd35da0c26bc87a1e156c7b1a5e35fd7875ff9a39d4294b8d6a369a868`.
3. The live Root PRD labels Revision 7 candidate and Revision 6 accepted while
   the Root handoff and live D-8 state say Revision 8 adopted. S1's current
   return (SHA-256
   `a003ec10bd7731cbd038e8b6c4df05ac897cf9f0ea58d2cbda8c889d10017b00`)
   records this as a separate Gate-1 authority-currency blocker and authorizes
   no reconciliation.
4. The N0 Agent 2 did not return; WORKING_ITEMS rejected the interrupted run
   and preserved only manager evidence. A fresh N0 remains mandatory.
5. No Root-local `software-workflow.json` exists. This is correct for the
   first planning activation but blocks every later software check or
   implementation activation under REQ-052.
6. Executable amendment remains held on S1 and a separately sealed Root
   implementation activation. The terminal recovery class, payload, event
   identity, duplicate-history policy, and compatibility-epoch disposition
   remain human-gated semantic choices.

## Rerun requirements

1. Through the owning instruments, restore or explicitly disposition the six
   exact authoring-envelope inputs and reconcile the live decomposition
   and PRD currency text with the accepted records, preserving immutable
   candidate history. Do not reconstruct accepted inputs from memory or
   present implementation bytes.
2. Dispatch a fresh N0 under the existing sealed brief with usable bounded
   non-shell reads/writes. Release N1–N3 only if every N0 check passes.
3. Complete N1/N2/N3 fan-out, N4 integration, fresh N5 refutation, and N6
   owner handoff before requesting semantic acceptance.
4. Obtain an exact human semantic ruling and S1 disposition; adopt a lawful
   Root software-workflow profile and exact registered checks; then seal a
   later Root implementation activation.
5. Closure still requires the applied Root change, executable restart/replay
   proof, exact SHAs, owner acceptance, and a later TASK_MANAGEMENT session.

## Next decision/gate

Immediate owner/Agent-0 gate: disposition the missing accepted-input packet
and route the separately gated current-facing PRD/decomposition acceptance-
status reconciliation identified by S1, preserving immutable SCA-002 and PRD
candidate history; then authorize a fresh N0 rerun on the same bounded graph.
No implementation choice is ripe before that fan-in. The later semantic/
implementation gate must rule the recovery terminal and compatibility posture
against the completed planning package.

## Telemetry and preservation

This was a single-deliverable bounded planning activation, not a multi-member
migration batch or adopted long-running activation, so no runtime telemetry
ledger was required. The collaboration runtime exposed no trustworthy token
or context-occupancy measure. The interrupted N0 attempt is named explicitly;
no complete child return or accepted fan-in is claimed.
