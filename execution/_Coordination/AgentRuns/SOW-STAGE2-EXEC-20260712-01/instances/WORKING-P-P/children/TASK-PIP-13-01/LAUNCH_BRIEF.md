# TASK-PIP-13-01 Sealed Brief — v2

RequestedBy: `WORKING-P-P`
RunID: `SOW-STAGE2-EXEC-20260712-01`
ParentInstanceID: `WORKING-P-P`
ChildInstanceID: `TASK-PIP-13-01`
PackageID: `PKG-13`
DeliverableID: `DEL-13-01`
TaskSkill: `scope-of-work`
Mode: `VERIFY`

## Objective and accepted basis

Independently verify the byte-exact frozen `DEL-13-01` candidate and the
future atomic five-path replacement. Do not repair or delegate. Basis:
D-GOV-16 `7584718aa32b112e415331736d1a8e68c12ac176`;
`PILOT-VALIDATION-001`; P3/B1 accepted; current
`main@0d260eb024d8b8dada0df477b70ac880a6906ffa`; Stage-1 evidence
`31c35ea9798c29cd0af16b7089186f3942dcfcb1`.

## Effective TASK brief

WorkingRoot: `{REPO_ROOT}`
ScopePath: `{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-01/workspace`
DeliverablePath: same as `ScopePath`
ApplyEdits: `true`
AllowedWriteTargets:

- `{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-01/**`

DeclaredReads:

- the exact DEL-13-01 P3 row;
- live deliverable `projects/chirality-piping/execution/PKG-13_Physical Design Knowledge and Constraint Engine/1_Working/DEL-13-01_Design knowledge schema and provenance model/**` limited to the four sources, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `Dependencies.csv`;
- this child's `legacy_state/`, SOW-only `workspace/`, `stage1_evidence/`;
- accepted P3/P2 and active scope-of-work skill/tool package.

RuntimeOverrides:

- `MODE=VERIFY`
- `DELIVERABLE_PATH={ScopePath}`
- `LIVE_DELIVERABLE_PATH={REPO_ROOT}/projects/chirality-piping/execution/PKG-13_Physical Design Knowledge and Constraint Engine/1_Working/DEL-13-01_Design knowledge schema and provenance model`
- `DECOMPOSITION_BASIS=projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@0d260eb024d8b8dada0df477b70ac880a6906ffa`
- `FROZEN_CANDIDATE_BASIS=projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`
- `PROJECT_SCOPE_REFS=[SOW-067]`
- `PACKAGE_OBJECTIVE_REFS=[OBJ-014]`
- `SOURCE_STATE=IN_PROGRESS`
- `RENDER_HTML=true`

Expected candidate SHA-256:
`6c76b2c785acc56ee1e67aaba64930e457b8c2ca20d4d9e8b4156cebe579c43d`.

## Required checks and outputs

Read complete `agents/AGENT_TASK.md` and the live scope-of-work skill plus all
companions. Use only the skill-declared tools for SOW operations; read-only
hash, byte comparison, line counting, JSON/CSV parsing, and Git status
diagnostics are allowed. Do not invoke the converter.

Independently: prove live hashes/status equal P3 and `legacy_state`; validate
legacy-only as `LEGACY_FOUR_DOC`; validate exact target-only as `SOW_V1`;
reproduce map, parity, deterministic checklist twice, safe HTML twice, source
line coverage, target resolution, OUT/AC/VER grounding, Stage-1 identity,
status/control containment, and an exact future manifest containing only add
`ScopeOfWork.md` plus delete the four legacy files. Record distinct
schema/content, preservation/containment, and execution-substrate verdicts.

Write all generated evidence under `evidence/`, the TASK run record under
`workspace/_run_records/`, and terminal `RETURN.md` plus `STATUS.json` in this
child directory. The TASK run-record `scope-path` follows AGENT_TASK's required
resolved-absolute field; all other durable prose/structured paths use repo-
relative or tokenized form. Remove any temporary output. Any discrepancy is
terminal FAIL; do not repair.

EXCLUSIONS: project writes; candidate mutation; D-GOV-16 marker insertion;
conversion; dual overlay; Git writes; lifecycle/control/receipt/release/H1/H2;
ISSUED member; `.claude-worktrees/`; delegation.
