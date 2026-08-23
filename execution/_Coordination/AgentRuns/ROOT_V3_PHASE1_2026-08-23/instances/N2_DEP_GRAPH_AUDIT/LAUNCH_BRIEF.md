# Sealed launch brief — N2 graph and dependency-closure audit

## Identity and authority

- **Role:** bounded Agent 2 generalist executing the Phase 1 graph rerun and `AUDIT_DEP_CLOSURE` semantics; read `agents/AGENT_AUDIT_DEP_CLOSURE.md` and record the steer-authorized output-location override.
- **Role enforcement:** instruction-asserted; do not delegate or create another orchestration layer.
- **Dependency:** start only after HELP_HUMAN provides the accepted N1 commit and fresh-review result.
- **Authority:** Phase 1 steer SHA-256 `2bbd449330b25d2ab88cec4097d3e224b95305954d30196e94fbd21c21062452`, executing only approved `Propagation_Plan.md` §5.

## Objective

From the accepted revision-1.3 decomposition plus the committed N1 live folders, re-derive the objective-relative Root work graph, recompute SCCs, and produce a fresh dependency-closure audit. The seven initialized-empty dependency containers are expected post-INIT state, not defects. All output is derivative and must declare rerun after accepted SOWs and dependency extraction.

## Required reads

Read `AGENTS.md`, this brief, the Phase 1 steer, `Propagation_Plan.md`, `docs/CYCLE_DRIVEN_RESOLUTION.md`, `agents/AGENT_AUDIT_DEP_CLOSURE.md`, all seven live decomposition surfaces, every live Root deliverable folder's dependency metadata/registers needed for the audit, N1 return/review, and the preserved Gate-1 graph/audit baseline. Do not treat absent extracted dependencies in the seven new folders as violations.

## Project-content write ownership

Exactly these new folders:

- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/DEP_GRAPH_POST_GATE5/`
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DEP_CLOSURE_POST_GATE5/`

Control-plane return ownership is limited to this instance directory's `RETURN.md` and `STATUS.json`. The human steer overrides the dedicated agent's default `_Evaluation/DepClosure` output location for this run; do not write or update that default tool root or pointer.

## Output contract

Graph folder: deterministic `WORK_GRAPH.json`, `DAG.md`, an SCC report, and enough decision/summary/hash evidence to satisfy the steer. Node set is 53 live deliverables plus packages. Edges must be evidence-based and objective-relative. Cycle-participating edges are non-gating until resolved. A cut or merge is human-gated: record SCC evidence and stop the affected step; do not decide it.

Audit folder: fresh AUDIT_DEP_CLOSURE return, decision log, summary, machine-readable evidence and hashes. Compare pre-existing folders against the prior audit; expected result is 53 deliverables present, seven OPEN with initialized-empty declared dependencies, and zero unresolved closure violations among pre-existing folders versus prior audit. Cite exact evidence for every finding.

Both packages cite SCA-004 accepted snapshot/pointer, all seven revision-1.3 identities, the N1 commit and output hashes, and state they must be re-derived after dependency extraction and SOW acceptance.

## Stops and acceptance

Never write live decomposition, pointer, folder metadata, existing SCA files, TM, SOWs, dependencies, estimates, schedules, tools, runtime, projects, or any other path. Stop for identity drift, needed out-of-scope write, or human-gated cut/merge. Unlimited repair applies inside declared output folders only. Raw logs must be normalized or gzip preimages. Do not commit.

Return exact files and SHA-256 values; 53+package node-set proof; SCC/cycle disposition; audit verdict and pre-existing-closure comparison; derivative/rerun statement; protected-surface proof; `git diff --check` and whitespace result; blockers; `RETURN.md`; terminal `STATUS.json`.
