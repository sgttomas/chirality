# D-PEC-12 - PROPOSAL: L3 operation-proposal semantics for the import seam

**Status:** AWAITING_RULING (companion to tier-0 `D-T0-18`; rules together).
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-12
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the D-PEC-06/07/08 packet pattern and the residual-row
convention in `_REGISTER.md`.

## Why

The profile open issue says: "L3 operation-proposal semantics overlap PEC
native lifecycles and need a future ruling before any proposal-shaped apply
path." The D-PEC-08 tranche built the apply path for imports; this packet
fixes the semantics so L3 (tier-0 D-T0-18) can be ruled without ambiguity.
Owner direction opening this preparation (2026-07-05, verbatim): "I want to
get to L3."

## Proposed semantics (what O-A of D-T0-18 would adopt)

1. **Single record of authority.** The in-app `import_proposal` record IS the
   operation proposal. A coordination-side artifact under
   `_DomainEngines/proposals/pec/` is authored per agent-initiated proposal as
   a governance mirror only — it cites the `IPR-` ref and source SHA-256 and
   confers no authority. No dual lifecycle: the app record's state governs.
2. **Scope.** The five §16 import contracts (mdl, rail, decisions, risks,
   schedule) — `engine_checkable` risk class — and nothing else. Any other
   operation family needs its own row.
3. **Who does what.** Agent (under `import.propose` authority basis granted by
   the operating human's session or a service identity the owner provisions):
   author mapping, file proposal, run/refresh dry-run, author the mirror
   artifact, withdraw own proposals. Human only: accept (hash+version echo),
   apply, `force` (never agent-set), reject-any. This restates the shipped
   code's RBAC; L3 changes no permission.
4. **Residency (D-T0-14 CLOSED stands).** The agent proposes from
   owner-provided files. Dry-run/apply reports are visible to the agent at
   count level plus row-level errors for the owner-provided rows themselves;
   the agent does not otherwise read instance content absent a
   D-PEC-01-style enumerated basis. No instance content to external models
   (RV-12 rider unchanged).
5. **Evidence convention.** Each L3 evidence run captures an immutable
   `PEC_<date>_L3-evidence-NN/` snapshot (D-T0-13 convention): proposal
   mirror, report JSON, history/audit extract for the `IPR-` record,
   export-and-compare result.
6. **Profile edits riding the ruling PR.** `integration_level:
   "OPERATION_PROPOSAL"`; annotate the L3-semantics open issue RESOLVED
   (imports scope) with a pointer here; add an `import.propose` seam note to
   `deterministic_tools` (`import.csv` entry note updated to reference the
   proposal pathway as the preferred route); validator re-run; index row and
   live pins consciously updated.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Adopt these semantics as written. | D-T0-18 O-A becomes executable in one PR + first evidence run. |
| O-B | Adopt with owner amendments (state them in the ruling). | Amended text is recorded verbatim; execution follows the amended text. |
| O-C | Defer. | L3 stays blocked on semantics regardless of D-T0-18. |

## Recommendation (non-binding)

O-A. The semantics add no new authority anywhere: they name the shipped
mechanism as the L3 mechanism and keep every gate human.

## Human ruling

**Ruling:** _pending._
