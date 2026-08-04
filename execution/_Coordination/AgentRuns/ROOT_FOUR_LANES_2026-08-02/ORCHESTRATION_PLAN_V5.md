# HELP_HUMAN orchestration plan — plan version 5

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Selection authority: `HUMAN`
Posture: `MIXED`
Parent plan: `ORCHESTRATION_PLAN.md` SHA-256
`5d84ae468c6bb64607052c6b100674a237d1cd146b25d8b84838728dc4855737`
Parent terminal graph: `WORK_GRAPH.json` SHA-256
`a7bd5a1fb61e8f387b6921952f6fc9aba88379cf9633a334fde27185e2a720d2`

## Reason for a new immutable plan surface

Plan version 4 and its terminal graph are hash-pinned by the completed E2
Option A package. They remain unchanged. This version adds the next independent
Pi evidence-hold step without mutating those accepted provenance anchors.

## Current gates preserved

- S2 remains at exact paired-candidate acceptance/application. No live PRD or
  decomposition write is authorized.
- W2 remains at packet-blueprint readiness. Packet instantiation, acceptance,
  live `accepted_inputs/`, and N0-R2 remain held on applied S2 evidence and the
  later exact packet owner gate.
- Pi `0.82.0` remains a preferred candidate under evidence hold. D-APP-72 / Pi
  `0.80.10` remains operative; no identity is selected or superseded.
- PR #491 remains open and unmerged; Task Management closure remains excluded.

## Added node H2 — PIA-U10 identity proposal

Agent 1 `HELPS_HUMANS` prepares the exact candidate implementation-identity
options and a versioned collision-proof identity schema required by PIA-U10.
This is a design proposal, not implementation or acceptance.

Allowed writes are confined to:

- `execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/identity_proposal/`;
- `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/H2-PI-IDENTITY/`.

Required outputs are `BASIS.json`, `ROOT_PI082_IDENTITY_OPTIONS.md`,
`CANDIDATE_IDENTITY.schema.json`, `IDENTITY_FIELD_MATRIX.csv`,
`ARTIFACT_MANIFEST.csv`, `RETURN.md`, and `STATUS.json`. Options must cover at
least Root-wrapper canonical, App-host explicit registration, converged Root
concrete adapter, and continue-hold. The schema must distinguish upstream
package identity from Chirality implementation family and bind source/build,
capability profile, registration, policy, client composition, packaging, and
rollback identities without silently making mutable evidence a registry key.

## Holds and fan-in

- H2 may inspect Root and App sources read-only but may not write `projects/*`,
  runtime/source/dependency/lock/decision/decomposition/register/lifecycle,
  release, or Git surfaces.
- H2 does not select an option, dispatch proof work, or create a dedicated
  agent/skill/tool.
- HELP_HUMAN accepts the return only if every option is non-inferred,
  tradeoffs and affected instruments are explicit, the JSON schema validates,
  collision cases are specified, and all current authority/no-effect
  boundaries remain intact.
- Fan-in terminates at human G1 selection of one validation target, amendment
  of the proposal, or continuation of the hold. A G1 choice is not Pi approval.
