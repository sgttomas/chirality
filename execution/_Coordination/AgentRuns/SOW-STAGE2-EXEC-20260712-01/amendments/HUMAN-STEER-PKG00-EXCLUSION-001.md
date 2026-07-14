# Human Steer — Piping PKG-00 Exclusion and Dependency Direction

Recorded: 2026-07-13
Applies to: `SOW-STAGE2-EXEC-20260712-01`
Status: `ACTIVE — CONSEQUENTIAL PLAN AMENDMENT`

## Human ruling

The human ruled that Piping `PKG-00` is not a package to be converted in this
project. It is retained governance and architecture-basis context that was
packaged only so its information could be infused throughout the actual
packages.

For this Stage-2 project:

1. exclude all eight Piping `PKG-00` members from conversion, integration,
   rollback, closure-population, legacy-retirement, and H1/H2 counts;
2. begin ordinary Piping conversion at `PKG-01` and continue normally;
3. require every actual Piping package (`PKG-01` through `PKG-17`) to depend
   on or incorporate applicable `PKG-00` governance/architecture-basis
   context; and
4. keep the direction one-way: nothing in `PKG-00` may depend on another
   package or deliverable.

## Quantitative effect

- Frozen two-project source census: unchanged at 154 tracked members.
- Stage-2 conversion population: 146 members (154 less eight retained
  Piping `PKG-00` governance-context members).
- Verified pilots: 10.
- Ordinary conversion waves: 135 members (previously 143).
- Isolated ISSUED H1 member: 1 (`DEL-01-01`).
- P1 ordinary scope: 22 members across Piping `PKG-01` through `PKG-04`,
  excluding `DEL-01-01`, split 3/5/8/6, with 198 expected live bindings.

## Disposition of prior P1 preflight

`ORCHESTRATOR-P1-B0` and `snapshots/W_P1/preflight/` remain immutable failed
predecessor evidence. Their `DECISION_REQUIRED` verdict accurately recorded
that the original 30-member contract expected eight nonexistent PKG-00
`Dependencies.csv` registers. This ruling resolves that decision by removing
PKG-00 from the conversion population, not by waiving a required binding or
creating dependency truth.

The revised preflight is a versioned successor, `ORCHESTRATOR-P1-B0-R1`, and
writes only `snapshots/W_P1/preflight-r1/**` plus its own instance record.

## Authority and fences

This human ruling authorizes the planning and execution-population amendment.
It does not authorize edits to decomposition truth, DAG rows, deliverable
content, lifecycle, or PKG-00 files. Existing project evidence must be checked
for consistency with the one-way dependency rule; any contradiction returns
as a separate decision request rather than being silently repaired.

H1 and H2 remain unapproved. The existing ISSUED fence on `DEL-01-01`, CHANGE
ownership of Git integration, immutable-snapshot rules, and all other
Stage-2 constraints remain active.
