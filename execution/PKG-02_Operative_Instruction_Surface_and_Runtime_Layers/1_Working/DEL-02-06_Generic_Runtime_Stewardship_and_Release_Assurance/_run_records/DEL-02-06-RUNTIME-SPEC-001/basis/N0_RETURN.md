# N0 disposition — basis and currency proof

Status: `REJECTED_INTERRUPTED_CHILD_RETURN — MANAGER EVIDENCE HOLD`

The bounded N0 Agent 2 did not produce a terminal return and was interrupted.
WORKING_ITEMS therefore does not accept an N0 child result. The manager's
independent Phase-1 checks are preserved in `BASIS_REPORT.json` and are
sufficient to hold every dependent node without inventing a child return.

## Verdict

`HOLD`. N1 through N6 may not release.

## Passing preconditions

- Repository HEAD matches the parent basis:
  `97678a841ef58345c73d3470ed8de57c9b1405d2`.
- The accepted `ScopeOfWork.md` hash matches
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- `_STATUS.md` remains `INITIALIZED` and records no earlier activation.
- No Root-local `software-workflow.json` exists; client profiles were not
  borrowed.
- `_DEPENDENCIES.md` declares no upstream or downstream edge.
- W1 writes remain confined to the exact deliverable-local run root.

## Blocking failures

1. The mandatory `accepted_inputs/` directory is absent. The activation cannot
   hash-verify or consume:
   `CANDIDATE_SET_MANIFEST.sha256`,
   `ROOT_COMPATIBILITY_POLICY_CANDIDATE.md`,
   `DEGRADED_MODE_CONTRACT_CANDIDATE.md`, `OPEN_ITEMS.csv`,
   `OWNER_SELECTION.md`, or `OWNER_GATE.md`.
2. The live decomposition at SHA-256
   `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`
   still self-labels revision 1.2 as `CANDIDATE — not accepted`, while the
   SCA-002 Decision Log at SHA-256
   `88b34598352c2b75159b24ccab86059d38dc38b1bd1f7de1f22cf6b552c8a794`
   records owner acceptance, application, Gate 5 execution, and revision 1.2
   as the accepted current basis. REQ-038 forbids treating that conflict as
   current proof. S1's independent AUDIT_DECOMP return at SHA-256
   `3d2a09dd35da0c26bc87a1e156c7b1a5e35fd7875ff9a39d4294b8d6a369a868`
   confirms structural coverage PASS and authority-state consistency FAIL.
3. The live `docs/PRD_ROOT.md` at SHA-256
   `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c`
   labels Revision 7 candidate and Revision 6 accepted while the Root handoff
   and live D-8 state say Revision 8 adopted. S1's current return at SHA-256
   `a003ec10bd7731cbd038e8b6c4df05ac897cf9f0ea58d2cbda8c889d10017b00`
   records this independent Gate-1 blocker and authorizes no reconciliation.
4. A fresh N0 Agent 2 terminal return remains required after those source
   failures are resolved. The interrupted run is provenance, not fan-in.

## Rerun

Restore or explicitly disposition the mandatory envelope through its owning
instrument, reconcile the PRD and decomposition currency text through their
owning instruments while preserving immutable candidate history, then dispatch
a fresh N0 with the same sealed objective and usable bounded non-shell file
tools. No accepted input may be reconstructed from memory.
