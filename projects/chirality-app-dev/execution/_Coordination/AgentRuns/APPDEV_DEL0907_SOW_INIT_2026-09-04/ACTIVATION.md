# DEL-09-07 Scope of Work initialization

PROJECT_SETUP Phase 2.2, owner-directed continuation under D-APP-107 after
PR #709 merged. Basis: `740569598f9d00440636b8ea25264127f418e4ec`;
handoff cursor: Receipt-229. Accepted decomposition is the live SCA-APP-009
postimage; source scope `SOW-080`, objective `OBJ-008`.

Work graph: PROJECT_SETUP → TASK `scope-of-work` INIT author → fresh TASK
`scope-of-work` VERIFY → PROJECT_SETUP fan-in → HELP_HUMAN publication.
Author and verifier write disjoint local evidence; production writing is
exclusive to the author. No semantic pipeline or lifecycle act is selected.

Write scope: DEL-09-07 `ScopeOfWork.md`, its `_run_records/`, this AgentRuns
directory, and one append-only loop receipt. The five scaffold files remain
byte-identical. The contract is drafted for owner consideration; structural
validation and CLEAR admission do not constitute content acceptance.

Execution uses delegated-harness-native Codex/OpenAI/GPT-6 family per session
instructions; exact backend model identifier is unavailable. Role is not
mechanically enforced, evidence is instruction-asserted, and non-delegation
is instruction/config asserted, not mechanism-proven.

## Step 0

Clean task worktree from origin/main at the basis above. Receipt validator
VALID; current corpus v20 reports no drift; committed selected plan is
`loop/WORKPLAN_2026-09-04_app_dev_loop.md`, read through `git show HEAD:`.
The pinned completion-reference SHA matches the plan. D-APP-107 records the
applicable direction. INIT dispatch returned ALLOW/SOW_INITIALIZATION before
the child launch. Default python3 lacked PyYAML for self-check; the existing
`/private/tmp/chirality-piping-dec093-venv/bin/python` ran it successfully.
No frontend path is in scope; its gates are inapplicable.

The D-APP-107 handoff's integration-pending language is dated history: PR
#709 is merged at this basis. Frozen scaffold references also retain their
pre-pointer context; the draft binds accepted live sources explicitly.

LOOP_INIT's example `harness.py status --project projects/chirality-app-dev`
is rejected by the current CLI. Retrying with its accepted `--project app-dev`
selector succeeds and reports DEL-09-07 as the sole OPEN deliverable. This
instruction discrepancy is reported only; its source is outside this tranche.
