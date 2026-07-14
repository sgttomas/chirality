# PKG-02 Batch Conversion Experiment Charter

Status: `ACTIVE`
Parent: `HELP_HUMAN`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`
Basis: synchronized `main@3efa950aa981f9d3491bab2ab3b3319a5a2c6d5c`

## Question

Can one package-level batch author and one fresh package-level batch verifier
process five related deliverables at the same sufficient quality as PKG-01 and
the accepted App bar, without context-length failure, cross-member
contamination, or task drift?

“Sufficient” means faithful representation replacement: evidence-rich source
parity, exact deterministic clean finalization, valid clean `SOW_V1`, complete
source-line preservation and current hash binding, conservative
scope/objective mapping, deterministic checklist/render output, fail-closed
negative states, exact atomic replacement and inverse rollback, unchanged
status/control inputs, and no new semantic obligation or lifecycle meaning.
It is not substantive engineering-content approval.

## Frozen scope

- Package: Piping `PKG-02_Domain Model, Units, and Core Schemas`.
- Members: `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`.
- Exact live paths, frozen hashes, scope refs, objective refs, and decomposition
  basis are reproduced from the accepted revised P1 manifest at
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv`.
- PKG-00, PKG-01, and every other package are excluded from writes.

## Experiment graph

1. `WORKING-EXP-PKG02` freezes live inputs and dispatches exactly one
   `BATCH-AUTHOR-PKG02` Agent 2.
2. The author processes five members in numeric order, creating separate
   evidence and clean production candidates, finalization reports, full member
   evidence, and ordered runtime/drift telemetry.
3. After author acceptance, one fresh `BATCH-VERIFY-PKG02` Agent 2 independently
   reconstructs and verifies all five in numeric order without repair.
4. WORKING_ITEMS validates both returns, performs package checks and exact
   apply/rollback simulations, and returns a package snapshot.
5. A separate RECONCILIATION manager independently compares quality and
   runtime/failure properties with PKG-01 and the accepted App bar.

## Context and drift observations

Each batch child records per member: sequence position, start/end time,
frozen-input recheck, tool stages, evidence/production hashes, mapping and
source-line totals, failures/retries/remediations, scope violations, unresolved
items, and whether state from an earlier member was incorrectly reused. The
return explicitly addresses omission, truncation, instruction loss,
cross-member contamination, and task drift. If native token/context occupancy
is unavailable, that limitation is recorded and artifact completeness,
position trends, and sequencing serve as observable proxies.

## Writes

Only this run root:

- `candidates/PIP-PKG02/**`
- `instances/WORKING-EXP-PKG02/**`
- `instances/RECON-EXP-PKG02/**`
- `snapshots/package/**` and `snapshots/reconciliation/**`
- run-local telemetry, notices, amendments, work graph, and handoff

All `projects/**`, the active Stage-2 plan/run, project loops, instructions,
skills, Git integration, lifecycle, H1/H2, release, and retirement surfaces are
read-only or excluded. Pre-existing domain-audit paths and
`.claude-worktrees/**` remain outside scope and must not be inspected or
touched.

## Pass condition

PASS requires 5/5 author and 5/5 verifier results inside exactly two Agent-2
sessions; evidence-rich and clean artifacts for every member; complete mapping
and line coverage; exact finalization binding; byte-stable deterministic
outputs; zero unclassified source loss, semantic expansion, contamination,
project write, blocker, waiver, or unknown; exact 25-row replacement and
inverse rollback; package checks; and an independent reconciliation verdict
on sufficient quality, runtime/failure behavior, and context/task adherence.

Any failure is retained as experimental evidence. Repair may not silently
change the experiment model.
