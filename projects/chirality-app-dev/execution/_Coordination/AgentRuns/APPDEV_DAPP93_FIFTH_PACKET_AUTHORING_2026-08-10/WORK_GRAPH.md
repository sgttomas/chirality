# Frozen work graph v1 — D-APP-93 fifth packet-authoring lineage

Status: `FROZEN BEFORE N1 DISPATCH`

Selection authority: owner direction, 2026-08-10. Posture:
`SUPERVISED_MANY_TO_MANY`, serialized because every downstream node consumes
the accepted return of its predecessor.

## Nodes and gates

| Node | Agent | Objective | Writes | Release gate |
|---|---|---|---|---|
| M0 | WORKING_ITEMS | freeze exact allowlists/briefs; resolve, hash, syntax-check, and harmlessly execute every frozen shell form | activation, graph, allowlists, briefs, scratch, preflight, runtime ledger | every probe has its documented expected exit/behavior |
| N1 | fresh Agent 2 generalist | six-stage taint clearance of the six cited files and 80-row ledger | `taint_clearance/**`, `returns/N1_*` | manager independently accepts all six criteria |
| M1 | WORKING_ITEMS | validate N1, allowlist compliance, telemetry, hashes, zero-hit scan, provenance, and structure | `validation/N1_MANAGER_VALIDATION.md` | explicit `PASS — N1 ACCEPTED` |
| N2 | fresh Agent 2 generalist | author a wholly new packet from the accepted ledger/source basis; index and terminal return | `packet/**`, `returns/N2_*` | manager accepts completeness, alignment, hard zero-identity criterion, and containment |
| M2 | WORKING_ITEMS | validate author fan-in and freeze all packet bytes | `validation/N2_MANAGER_VALIDATION.md`, `freeze/**` | immutable packet inventory and approval token recorded |
| N3 | fresh Agent 2 generalist | verify the frozen packet read-only, without repair | `verification/**`, `returns/N3_*` | fresh substantive `PASS` and unchanged packet inventory |
| M3 | WORKING_ITEMS | validate verifier fan-in and close exactly at approval gate | manager return, handoff, runtime summary, receipt-ready facts, final inventory | exact hash/token returned; no execution |

Edges: `M0 -> N1 -> M1 -> N2 -> M2 -> N3 -> M3`. No node may be
released on a partial predecessor return. A post-freeze packet mutation
invalidates N3 and requires a new freeze plus fresh verifier within this
lineage; no packet repair may be performed by N3.

## Exact path allowlists

- N1: `allowlists/N1_READ_ALLOWLIST.txt`
- N2: `allowlists/N2_READ_ALLOWLIST.txt`
- N3: `allowlists/N3_READ_ALLOWLIST.txt`
- all nodes: `allowlists/ABSOLUTE_READ_WRITE_EXCLUSIONS.txt`
- salvage exception: `allowlists/SALVAGE_FILES.txt`
- frozen shell forms: `allowlists/FROZEN_COMMAND_FORMS.md`

Every brief incorporates these files by exact path and SHA after M0 freeze.
Before dispatch and at fan-in, the manager checks every declared/read-reported
search command for explicit file operands or an allowed root plus exclusions.
No recursive command may target `projects/chirality-app-dev` or `AgentRuns`.

## Pacing and telemetry

- N1 stages: 4, 5, 8, 8, 5, and 4 minutes; total expected 34 minutes.
  First checkpoint no earlier than minute 4; later checkpoint interval 8
  minutes. Durable outputs are one named stage file per stage.
- N2 stages: 8, 10, 12, 8, 5, and 4 minutes; total expected 47 minutes.
  First checkpoint no earlier than minute 8; later checkpoint interval 12
  minutes. Durable outputs are packet components and terminal return.
- N3 stages: 6, 8, 8, and 5 minutes; total expected 27 minutes. First
  checkpoint no earlier than minute 6; later checkpoint interval 8 minutes.
- At every checkpoint, record durable file count and bytes since the previous
  checkpoint. Quietness alone is not a failure. Interrupt only after a full
  checkpoint interval with zero new durable output. Native token/context
  occupancy is recorded as unavailable when the runtime does not expose it.

## Escalation

Any tool-probe failure blocks before N1. Any hash, identity, provenance,
structure, allowlist, packet completeness, freeze, verifier, or historical
preservation failure blocks this lineage and holds all dependants. No silent
repair, tool substitution after dispatch, packet execution, or sixth lineage.
