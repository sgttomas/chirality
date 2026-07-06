# D-PEC-12 - PROPOSAL: L3 operation-proposal semantics for the import seam

**Status:** RULED (2026-07-05, with owner amendment; companion to tier-0 `D-T0-18`).
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

**Ruling:** RULED with owner amendment (Ryan Tufts), 2026-07-05 — O-B shape (adopt
with amendments stated in the ruling).

Owner ruling of record (verbatim, in-session, ruling both this packet and D-T0-18):

> 1. O-A advance.
> 2. The agent should have full agency, don't try to use semantics as a replacement
> for proper governance harnesses (more than just semantics) so focus on making a
> useful agent for now.
> Merge the PR first and then proceed accordingly.

Recorded interpretation of the amendment (the ruling text governs on any
disagreement): the binding gates are the MECHANICAL harnesses — the shipped RBAC
(`import.propose`/`import.accept`), hash+version-bound acceptance, staleness
refusal, transaction-atomic apply, append-only history/audit, the standing
fences, and the decision registers — not this packet's prose. Within those
harnesses the agent has FULL AGENCY across the proposal pathway (author, file,
dry-run, refresh, withdraw, and — when operating under an owner-provisioned or
demo/scratch actor basis — accept and apply through the same audited API).
Sections 1, 2, 4, 5, and 6 of the proposed semantics stand as working
conventions, not as new authority constraints; section 3's propose/accept role
split describes the shipped RBAC defaults, and the operating human basis
determines what the agent may lawfully drive end-to-end. Priority is a USEFUL
agent; governance-harness gaps found in practice come back as register rows,
not as prose restrictions invented mid-run.

**Status change:** AWAITING_RULING → RULED.
