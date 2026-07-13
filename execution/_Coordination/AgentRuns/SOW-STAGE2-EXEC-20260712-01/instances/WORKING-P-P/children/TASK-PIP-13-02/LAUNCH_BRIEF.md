# TASK-PIP-13-02 Sealed Brief — v2

RequestedBy: `WORKING-P-P`; RunID: `SOW-STAGE2-EXEC-20260712-01`;
ParentInstanceID: `WORKING-P-P`; ChildInstanceID: `TASK-PIP-13-02`;
PackageID: `PKG-13`; DeliverableID: `DEL-13-02`; TaskSkill:
`scope-of-work`; Mode: `VERIFY`.

Objective: independently verify the exact frozen DEL-13-02 candidate and
future atomic five-path replacement without repair or delegation. Accepted
basis is D-GOV-16 `7584718aa32b112e415331736d1a8e68c12ac176`,
`PILOT-VALIDATION-001`, accepted P3/B1,
`main@0d260eb024d8b8dada0df477b70ac880a6906ffa`, and Stage-1 commit
`31c35ea9798c29cd0af16b7089186f3942dcfcb1`.

ScopePath and DeliverablePath:
`{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-P/children/TASK-PIP-13-02/workspace`.
ApplyEdits: true. AllowedWriteTargets: this exact child directory recursively.

Declared reads are the exact DEL-13-02 P3 row; the live deliverable's four
sources, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and
`Dependencies.csv`; this child's `legacy_state/`, SOW-only `workspace/`, and
`stage1_evidence/`; accepted P3/P2; and the live skill/tool package.

RuntimeOverrides: `MODE=VERIFY`; `DELIVERABLE_PATH={ScopePath}`;
live deliverable `projects/chirality-piping/execution/PKG-13_Physical Design Knowledge and Constraint Engine/1_Working/DEL-13-02_Constraint entity and provenance model`;
current decomposition basis `SOFTWARE_DECOMP.md@0d260eb024d8b8dada0df477b70ac880a6906ffa`;
frozen candidate basis `SOFTWARE_DECOMP.md@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`;
`PROJECT_SCOPE_REFS=[SOW-068,SOW-067]`;
`PACKAGE_OBJECTIVE_REFS=[OBJ-014,OBJ-018]`; `SOURCE_STATE=IN_PROGRESS`;
`RENDER_HTML=true`.

Expected candidate SHA-256:
`43d9ea2fa0e4fa95c4906fb8f7abffabe7c23a92d7bbc6ea4a4c9f430293c6d8`.

Read complete AGENT_TASK and scope-of-work package. Use skill tools only for
SOW operations plus read-only hash/byte/line/parse/status diagnostics; never
invoke converter. Prove live/P3/legacy-copy equality; legacy-only
`LEGACY_FOUR_DOC`; exact target-only `SOW_V1`; map, parity, checklist twice,
safe HTML twice, source-line/target/OUT-AC-VER grounding, Stage-1 identity,
status/control containment, and exact five-path future manifest. Separate
schema/content, preservation/containment, and substrate verdicts.

Write `evidence/**`, `workspace/_run_records/**`, `RETURN.md`, and terminal
`STATUS.json` only in this child directory; use portable paths outside the
AGENT_TASK-required absolute run-record `scope-path`, and remove temp output.
Any discrepancy FAILS without repair. Exclude project/candidate/Git/
lifecycle/control/receipt/release/H1/H2/ISSUED writes, marker insertion,
conversion, dual overlay, `.claude-worktrees/`, and delegation.
