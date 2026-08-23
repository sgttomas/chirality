# Launch Brief — N3 SCOPE_CHANGE

- Parent: `HELP_HUMAN`, run `ROOT_V3_PHASE0_2026-08-22`
- Accepted basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Objective: perform only SCA-004 Gate-1 assessment and release-pathway DAG
  preparation exactly as owner-directed; no decomposition amendment or pointer
  update.
- Construction: named Agent 1 `SCOPE_CHANGE`; it must dispatch one bounded
  `AUDIT_DEP_CLOSURE` Agent 2 after drafting the graph.
- Content write targets: only
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/` and
  `execution/_Coordination/NOTICE_2026-08-22_ROOT_SCA-004_V3_RELEASE_PATHWAY_DAG.md`.
- Control-plane writes: `STATUS.json` and `RETURN.md` in this instance folder.

## Required context

Read the owner steer/G0 record, `agents/AGENT_SCOPE_CHANGE.md`, Root SOFTWARE
decomposition and live deliverable folders, SCA-002 accepted snapshot, SCA-003
four-state handoff form, current `_LATEST.md`, Revision 3.1 as non-governing
input, Root PRD/contract/types/spec surfaces needed to trace impact, DEL-02-06
SOW and acceptance package, cited Task Management rows, and
`docs/CYCLE_DRIVEN_RESOLUTION.md`.

## Output and acceptance contract

Produce every N3 item in the steer with status `AWAITING_OWNER_ACCEPTANCE`.
The graph must cover live Root deliverables plus explicitly typed App notice
edges, enumerate all SCCs and proposed cycle moves, and keep unresolved
cycle-participating edges non-gating. Dispatch the dedicated audit against
this graph and include its durable return and verdict inside the SCA folder.
Because the owner's write fence is narrower than the audit package's default
tool-root output, the audit brief must record the human override and write
only inside the SCA folder; it must not touch `execution/_Evaluation/` or its
pointer. Recheck graph resolution and `_LATEST.md` hash. Return exact paths,
checks, blockers, derivative status, and next owner.

Brief amendment: version 2 at `../../amendments/N3/2.md` adds the mandatory
fresh SOFTWARE Gate-1 `AUDIT_DECOMP` baseline and fixed `AuditState` repair;
objective, Gate posture, authority, and content write scope are unchanged.
