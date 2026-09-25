# _CONTEXT — DEL-02-08

| Field | Value |
|---|---|
| DeliverableID | DEL-02-08 |
| Canonical name | Work-graph parser |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-095 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Content-minimal parser for `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; integration ref by default, local branch refs opt-in and labelled unintegrated; cited PR numbers resolved to local merge commits by read-only plumbing, unresolved-locally reported, never guessed. Node states are declared activity, never liveness; graph prose is never extracted.

## Anticipated artifacts

Parser + pinned golden-by-reference fixture suites for the three fixture classes (FC-1 receipt present; FC-2 evidence-only; FC-3 no AgentRuns record) + synthetic grammar-edge fixtures

## Envelope notes

M: a new grammar plus profile-driven discovery, PR-to-merge-commit resolution inputs and three pinned fixture classes; kept one cohesive parser slice

## Provenance

Scaffolded under `D-PEC-93` (2026-09-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.5 (`current_basis`,
SCA-005 successor; deliverable added by A-19). Fields templated
deterministically from `Deliverables.csv`; this file restates register truth
and is not an independent authority.
