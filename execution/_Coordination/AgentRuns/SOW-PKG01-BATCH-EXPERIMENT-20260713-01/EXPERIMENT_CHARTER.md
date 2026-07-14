# PKG-01 Batch Conversion Experiment Charter

Status: `ACTIVE`
Parent: `HELP_HUMAN`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`
Basis: synchronized `main@ef461cfdb3a4b135dc670b04f646eca3eac47712`

## Question

Can one package-level batch author and one fresh package-level batch verifier
produce the same sufficient representation-migration evidence as the accepted
per-deliverable App execution, without context-length failure or task drift?

"Sufficient" means faithful representation replacement: valid `SOW_V1`,
complete source-line preservation and current hash binding, conservative
scope/objective mapping, deterministic checklist/render output, fail-closed
negative states, exact atomic replacement and inverse rollback, unchanged
status/control inputs, and no new semantic obligation or lifecycle meaning.
It is not a substantive engineering-content approval.

## Frozen scope

- Package: Piping `PKG-01_Governance, IP Boundary, and Professional Responsibility`.
- Members: `DEL-01-02`, `DEL-01-03`, `DEL-01-04` only.
- Exact membership, live paths, hashes, scope refs, objective refs, and
  decomposition basis come from the accepted revised P1 manifest at
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv`.
- `DEL-01-01` and all PKG-00 members are excluded.

## Experiment graph

1. `WORKING-EXP-PKG01` freezes inputs and dispatches `BATCH-AUTHOR-PKG01`.
2. One author session processes the three members in numeric order, creates
   three candidate files, complete member evidence, and batch progress/drift
   telemetry.
3. After author acceptance, one fresh `BATCH-VERIFY-PKG01` session reconstructs
   and verifies all three independently in numeric order without repair.
4. WORKING_ITEMS validates both batch returns, runs package checks and exact
   apply/rollback simulations, and returns package evidence.
5. A separate RECONCILIATION manager independently assesses coverage,
   provenance, equality to the sufficient-quality contract, and context/task
   adherence.

## Context and drift observations

Each batch child must record, per member: start/end sequence, frozen-input
recheck, tool stages completed, candidate/evidence hashes, failures/retries,
scope violations, unresolved items, and whether earlier member state was
mistakenly reused. The return must explicitly identify omission, truncation,
instruction loss, cross-member contamination, or task drift. Lack of native
token telemetry is recorded as a measurement limitation; artifact completeness
and sequencing are the observable proxies.

## Writes

Only this run root:

- `candidates/PIP-PKG01/**`
- `instances/WORKING-EXP-PKG01/**`
- `instances/RECON-EXP-PKG01/**`
- `snapshots/package/**` and `snapshots/reconciliation/**`
- root run `WORK_GRAPH.json` and terminal `HANDOFF_STATE.md`

All `projects/**`, current Stage-2 run/plan files, project loop files,
instructions, skills, Git state, lifecycle, H1/H2, integration, release, and
retirement surfaces are read-only or excluded. The four unrelated domain-audit
paths and `.claude-worktrees/**` remain outside scope and must not be inspected
or touched.

## Pass condition

PASS requires 3/3 author results and 3/3 verifier results inside exactly two
Agent-2 sessions; complete mapping and line coverage for every member; byte-
stable repeated deterministic outputs; zero unclassified source loss, semantic
expansion, cross-member contamination, project write, blocker, waiver, or
unknown; exact 15-row replacement and inverse rollback; package checks; and an
independent reconciliation verdict on quality and context/task adherence.

Any failure is retained as experimental evidence. No repair may silently
change the experiment model.
