# Sealed TASK review brief v1
RequestedBy: WORKING_ITEMS PKG02
CHIRALITY_INSTRUCTION_ROOT: {REPO_ROOT}
WorkingRoot: {REPO_ROOT}/projects/chirality-app-dev
ScopePath: {WORKING_ROOT}/execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-03/instances/pkg02_fields/reviewer
TaskSkill: software-code-review
ApplyEdits: false
ImplementationBrief: ../AUTHOR_BRIEF_v1.md and ../AUTHOR_AMENDMENT_v1.1.md
AcceptedBasis: root/project AGENTS, AGENT_TASK, software skill/profile, DEL02-04 SOW/Remaining, manager RATIONALE_v1, iteration3 approved plan and pinned target section12 plus5.10.
DiffBasis: manager FROZEN_SOURCE.diff and SOURCE_FREEZE.json; exactly module and existing lib test versus50b70f47.
AllowedWriteTargets: {ScopePath}/** (review evidence only; never source)
VerificationEvidence: author/COMMANDS.json and RETURN.md, input verification and source freeze
PROFILE_PATH: {WORKING_ROOT}/software-workflow.json
AllowedTools: read-only shell/repository scope/check-selection helpers; bounded evidence writer; APP-HOLD. No installs/network/source edits/children; no global check execution (parent owns).
ExpectedReturn: independently trace100% frozen diff through callers and contracts; source-scope check first, actual APP-HOLD dispatch/reliance DEL-02-04 before effect. PASS or actionable findings with path/line/reproduction/impact and residuals; durable TASK run record and REVIEW_RETURN.md. No lifecycle acceptance. Parent commits only after required full gates.
ReviewFocus: old caller types and legacy behavior; missing versus invalid-present; all view/width literals; arrays/maps malformed/prototype keys, deterministic eviction, identity byte preservation, root seed exactly once with isolated exceptions, timestamp validity; no activeChatRoot serialization; clear project vs app state, roundtrip and old-writer rollback limit; no stored convenience hint authority. Assess tests independently, not merely implementation-mirroring. Required old fields remain. Fresh context required; author dialogue not provided.
EXCLUSIONS: product writes, dependencies/carriers/shared records, lifecycle/owner/Root/pointers, delegated children, global tests/build, UI render claims. No temporary writes outside ScopePath.

Source freeze exact diff SHA256: 97221639751812c04b783ac60345491e860f5dfdac6b08ac13bde5770bf3ecc6
Additional required boundary: read-time recovery/import never overwrites throwing, malformed, empty-existing or foreign-schema current storage. Explicit write API remains separate. Check precise helper overload returns against existing typed callers. Author focused tests30PASS is evidence to audit, not a presumed finding-free result.
