# OD-7 Maintenance Routing Evaluation Protocol

Status: FROZEN_FOR_EXECUTION
EvaluationID: `CHIRALITY_PROGRAM_OD7_MAINTENANCE_2026-07-26_EF164C20`
Manager: `EVALUATION` (Agent 1)
AcceptedBasisCommit: `ef164c20c8a903a7ecff9450f677938a4111392f`
ExecutionRoot: `{REPO_ROOT}/execution`
DerivativeStatus: non-authoritative evaluation package

## Purpose and decision criteria

Determine, from the accepted basis, which OD-7 maintenance observations from
the Chirality Program architecture review remain current, which are already
closed or superseded, and the smallest lawful route for every remaining item.
The evaluation separates:

1. verified current defects from observations and unknowns;
2. mechanical closeout from consequential owner judgment;
3. owning authority and write surface;
4. dependency order and disjoint write scopes;
5. required coordination notices from authoritative amendments; and
6. immediate routes from explicit later work.

No score is requested or produced. A recommendation is decision-ready only
when it cites current-basis evidence, names the owning instrument, preserves
unresolved evidence as `UNKNOWN`, and does not reopen a closed item.

## Accepted inputs

- Current repository bytes at `ef164c20c8a903a7ecff9450f677938a4111392f`.
- The accepted derivative program-review package:
  `execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/`.
- Current governance registers, loop records, profiles, notices, and project
  instructions only to the extent needed to verify the enumerated questions.

The previous package supplies issue lineage, not current truth. Current basis
bytes govern status and routing.

## Questions in scope

- Root: D-GOV-27 `EffectiveSHA`; `CURRENT_WORKPLAN`; Root ScopeOfWork `TBD`
  claims; and confirmation that OI-011 and README C-4 are closed and must not
  be reopened.
- App: D-APP-75 effective-state residue; demonstrated detector claims;
  `RB-PEC-ADAPTER`; required App notices and receiving-loop routing.
- Tier 0 and PEC: D-T0-23 successor/residual; PEC daemon/auth/event-contract
  decisions; `pec.yaml` posture; PEC-K-03/K-11 external-owner annotation; and
  the exact PEC notice set.
- Piping: D-30, D-31, DEC-063 and the receiving-loop state for relevant
  notices.
- Cross-surface: smallest lawful instruments, mechanical-versus-consequential
  classification, dependency-valid ordering, disjoint write scopes, unknowns,
  and rerun triggers.

PEC and resource governance remain optional services. Method reform, semantic
parity, implementation, and new product scope are excluded.

## Toolbelt and fan-out

The owner-authorized toolbelt is:

- deterministic Git/path/text/CSV/hash checks over the accepted basis;
- four bounded, read-only Agent 2 generalists, dispatched concurrently after
  this protocol is frozen:
  - `A2-ROOT-RECORDS`;
  - `A2-APP-RECORDS`;
  - `A2-T0-PEC`;
  - `A2-PIPING`;
- Agent 1 validation, non-averaged synthesis, routing analysis, and final
  deterministic package checks.

Each child receives the same basis commit and issue-lineage package, a
surface-bounded context, read-only tools, no write target outside its return
file, and a required evidence-linked return schema. The four scopes are
independent shared reads. Children do not communicate or delegate.

## Required child-return schema

Each return must record:

- dispatch ID and basis commit;
- files inspected;
- one row per assigned issue with:
  `Issue`, `CurrentStatus`, `Claim`, `EvidenceRefs`, `OwningAuthority`,
  `SmallestInstrument`, `DecisionClass`, `Dependencies`, `WriteScope`,
  `RequiredNotices`, `Unknowns`, and `RerunTrigger`;
- explicit confirmation of items found closed/superseded;
- limitations and escalation conditions;
- actual engine/provider/model when known, otherwise `UNKNOWN`.

Allowed `CurrentStatus` values are `OPEN_DEFECT`, `OPEN_OBSERVATION`,
`CLOSED`, `SUPERSEDED`, and `UNKNOWN`. Allowed `DecisionClass` values are
`MECHANICAL`, `OWNER_DECISION`, `COORDINATION_ONLY`, and `NONE`.

## Fan-in acceptance

A child return is admitted only if:

1. its basis equals the accepted basis;
2. every assigned issue is dispositioned;
3. every factual claim has a current-basis file-and-anchor reference;
4. closed and superseded conclusions cite the closing evidence;
5. missing evidence remains `UNKNOWN`;
6. proposed writes are routed, not performed; and
7. the return does not introduce method reform, parity work, implementation,
   mandatory PEC/resource governance, or new product scope.

Conflicts are preserved and adjudicated against current bytes; they are not
averaged.

## Package outputs

All writes are confined to:
`execution/_Evaluation/CHIRALITY_PROGRAM_OD7_MAINTENANCE_2026-07-26_EF164C20/`

Required artifacts:

- `EVALUATION_PROTOCOL.md`
- `BASIS_MANIFEST.csv`
- `returns/<DispatchID>/RETURN.md`
- `FANIN_VALIDATION.md`
- `FINDINGS.csv`
- `OWNER_ROUTING_ALTERNATIVES.md`
- `ACTION_GRAPH.csv`
- `EVALUATION_REPORT.md`
- `HANDOFF.md`
- `ARTIFACT_HASHES.sha256`

## Closure and rerun rules

This package closes evaluation only; it authorizes no remediation. Closure
requires all four returns admitted or an explicit recorded waiver, every
finding evidence-linked, CSV and hash validation, package-only writes,
`git diff --check`, explicit decision and action routes, and visible unknowns.

Rerun is required if the accepted basis changes before an owner acts on a
finding, if an cited authority is amended, if a receiving loop records a new
notice disposition, or if a supposedly closed item is contradicted by later
current-basis evidence.
