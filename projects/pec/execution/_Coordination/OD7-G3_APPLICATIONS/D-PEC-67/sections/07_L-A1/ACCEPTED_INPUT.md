# OD7-G3 L-A1 — DEL-00-01 Reliance Prohibition Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED OR BINDING
**Candidate gate:** `OD7-G3-L-A1`
**Provisional PEC carrier:** `D-PEC-67`
**Held target:** `DEL-00-01` `ScopeOfWork.md` clauses `CLM-005` and `REQ-004`

## Exact candidate prohibition

Until a separately accepted correction to both `CLM-005` and `REQ-004` is
applied and its release is recorded, no session, agent, manager, specialist,
workflow, dispatch path, fan-in, review, promotion, consumer, or implementation
may rely on, dispatch for production, promote, or consume those two clauses as
current PEC v2 requirements.

The prohibition applies regardless of entry path. It does not prohibit:

- reading the clauses as historical evidence;
- preparing or reviewing an exact correction;
- running deterministic checks over candidate bytes; or
- citing D-PEC-58 and the accepted PEC PRD as the controlling basis.

There is no runtime exception mechanism. An override requires a later,
separately proposed, exactly accepted, pre-effective PEC-loop amendment.

## Enforcement candidate

If accepted, the authoritative PEC-loop record must be consulted by
WORKING_ITEMS at dispatch preflight. A dispatch that includes the held clauses
as production requirements must fail. Fan-in must reject a return that relies
on them. REVIEW and any other entry path must consult the same record before
reliance or promotion.

Required deterministic tests:

1. negative — a brief that relies on `CLM-005` or `REQ-004` for production is
   blocked;
2. negative — a return that promotes the retired adapter allocation is
   rejected at fan-in;
3. positive — a correction brief limited to replacing the held clauses is
   admitted; and
4. positive — historical read-only citation without production reliance is
   admitted.

## Release condition

Release requires all of:

1. exact owner acceptance of the correction candidate;
2. application of both corrected clauses;
3. deterministic proof that the live clauses match the accepted correction;
4. proof that no accepted PEC requirement re-adopts the retired allocation;
   and
5. a separately recorded PEC-loop release act.

## Conditional write surfaces

- PEC decision record and register
- PEC coordination hold/register surface selected by the owning workflow
- WORKING_ITEMS preflight/validation surface only through a separately
  authorized exact application tranche
- receipt and handoff surfaces

This candidate is separate from `L-A2`. Accepting the correction does not
silently bind or release this prohibition.
