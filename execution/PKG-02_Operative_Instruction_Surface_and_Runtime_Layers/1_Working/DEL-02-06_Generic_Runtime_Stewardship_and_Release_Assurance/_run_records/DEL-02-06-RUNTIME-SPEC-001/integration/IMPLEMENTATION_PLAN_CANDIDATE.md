# Bounded implementation plan candidate

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Status: `PLANNING_ONLY_NOT_AUTHORIZED`
- Constraint: no implementation or executable check occurs in N4

## Preconditions before any implementation activation

1. Accountable human rules exact D1-D9 bytes and accepts a revised semantic
   contract containing them.
2. Accountable human accepts or rejects the N4 compatibility `DELTA` proposal
   and, if accepted, supplies the exact compatibility identity and binding.
3. N5 independently attempts to refute semantic completeness, source
   grounding, authority containment, evidence sufficiency, rollback honesty,
   and client boundaries; every finding is dispositioned without repair by N5.
4. Root identifies a lawful project-local software workflow profile and exact
   authorized checks. REQ-052 forbids inferring one or borrowing a client
   profile.
5. A later sealed activation binds exact source, contract, fixture, read,
   write, check, rollback, and return identities. Any basis drift returns to
   the owner under REQ-038.

## Candidate change sequence

| Stage | Candidate objective | Candidate Root loci from N1 | Required gate/evidence |
|---|---|---|---|
| P0 | freeze exact adopted contract, compatibility binding, corpus fixture schema, and D1-D9 records | no runtime path | semantic and compatibility acceptance |
| P1 | align or explicitly separate the four-terminal vocabulary and exact recovery/error envelopes | `runtime/packages/contracts/src/events.ts`, `runtime/packages/contracts/src/harness/event-schema.ts`, `runtime/packages/contracts/src/protocol.ts`, `runtime/packages/contracts/src/errors.ts` | exact contract-byte gate; positive/negative schema evidence |
| P2 | add corpus indexing, classification, single-writer ownership, idempotent compare-and-append, malformed preservation, audit, and transaction boundary | `runtime/packages/core/src/session-store.ts` plus a separately accepted recovery service locus, potentially `runtime/packages/core/src/runtime-service.ts` | D1/D3/D4/D7/D8; crash-boundary evidence |
| P3 | gate ordinary and governed Agent 1 admission; preserve no-replay and parity | `runtime/packages/core/src/turn-coordinator.ts`, `runtime/packages/core/src/agent1-run-coordinator.ts`, `runtime/packages/core/src/runtime-service.ts` | N3-R03/R05/R11/R12 evidence |
| P4 | reconcile durable local-turn attribution with explicit activation/drain posture | `runtime/packages/core/src/residency-coordinator.ts` | D5/D8; DA-01..06 evidence; no automatic model action |
| P5 | place reconciliation before socket readiness and classify every route/direct entry against the accepted retained-function set | `runtime/packages/daemon/src/runtime-daemon.ts` | D6; readiness-race and fail-closed evidence |
| P6 | expose truthful indeterminate/recovery inspection with no automatic retry | `runtime/packages/client/src/client.ts`, `runtime/packages/cli/src/cli.ts` | Root CLI/client conformance gate and exact machine behavior |
| P7 | run isolated Root evidence matrices and cutover/rollback rehearsals | `runtime/tests/daemon.test.ts`, `runtime/tests/turn-hardening.test.ts`, `runtime/tests/session-and-residency.test.ts`, plus only later-authorized fixtures | RR-01..18, DA-01..06, N3-R01..16; D9 |
| P8 | separately route App conformance/implementation under App authority | no Root-owned App write | App-owned accepted tranche and evidence |
| P9 | assemble immutable fan-in and ask for accountable-human cutover/release decisions | no inferred runtime/client write | exact manifests, findings, affected-client evidence, rollback and release gates |

These paths are candidate review loci from accepted N1 evidence, not an
authorized file list. A later brief must name exact files; any additional locus
or material scope requires a versioned amendment.

## Client and coordination partition

- Root CLI/generic client: `AFFECTED`; Root-owned implementation and
  conformance are separately gated.
- App: `AFFECTED`; all App writes, presentation, retained functions,
  conformance, migration, and acceptance remain App-owned.
- PEC v2: `UNRESOLVED`; no dispatch, work package, dependency, or closure veto
  until a PEC-owned exact ruling.
- Piping: `NOT_AFFECTED` on current evidence.
- Tier-0: `NOT_AFFECTED` as a client; any relationship record is an independent
  coordination act that cannot amend Root semantics.

## Required evidence fan-in

Later execution must retain N3-R01 through N3-R16, RR-01 through RR-18,
DA-01 through DA-06, the exactly-one-terminal corpus cases, the retained-route
census, and CO-01 through CO-07. Every result must bind exact contract, source,
fixture, runtime, and artifact hashes. `DESIGNED_NOT_EXECUTED` is never a pass.

## Stops

Stop and return to the owner on any unresolved D1-D9 value, basis drift,
malformed baseline, unclear write owner, absent lawful profile/check authority,
new client, PEC implication, dependency change, S1 interaction, authority
expansion, or evidence that the tranche exceeds Context Envelope M. No stage
authorizes the next, and no test result, implementation behavior, or source
proximity constitutes semantic acceptance.

REQ-027 is preserved: this first activation ends with specification,
read-only inventory fan-in, evidence design, and planning only, with no
implementation byte. REQ-035 preserves every later implementation,
client-migration, repin, lifecycle, export, release, publication, issuance, and
reliance gate. REQ-052 preserves the hold on software checks and implementation
until a lawful Root-local profile and exact checks are separately authorized.
