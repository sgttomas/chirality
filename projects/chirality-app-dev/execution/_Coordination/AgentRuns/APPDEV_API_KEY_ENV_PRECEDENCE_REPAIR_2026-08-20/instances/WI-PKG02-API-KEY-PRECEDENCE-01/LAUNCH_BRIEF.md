# WI-PKG02-API-KEY-PRECEDENCE-01 — Sealed Launch Brief v1

- **RequestedBy:** HELP_HUMAN / owner-authorized cross-package repair
- **RunID:** `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- **ParentInstanceID:** `HELP_HUMAN`
- **InstanceID:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **Role:** WORKING_ITEMS (Agent 1)
- **PackageID:** `PKG-02`
- **Package path:** `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State`
- **Selected deliverable:** `DEL-02-05`
- **Selection authority:** HUMAN+AGENT_0
- **Owner direction:** "I authorize you to open the cross-package repair for
  reversed environment-key precedence and stack that work in PR #586 before I
  merge it."
- **Accepted basis:** `6710ee6354debc201f6a454e2802897026cd4b38`
  (PR #586 head at selection)
- **Branch:** `codex/app-api-key-precedence-20260820`
- **Brief version:** 1
- **Posture:** serialized dependant; no execution before accepted N1 handoff

## Objective

After Agent 0 accepts the terminal N1 / PKG-04 handoff, verify the repaired
runtime and renderer-facing API-key status behavior against
`DEL-02-05-R03`: UI safeStorage first, `ANTHROPIC_API_KEY` second, and
`CHIRALITY_ANTHROPIC_API_KEY` third. Repair only stale or incomplete PKG-02
evidence/state and close only what the accepted contract and checks prove.

## Dependency and release gate

- Required predecessor: accepted terminal return from
  `WI-PKG04-API-KEY-PRECEDENCE-01` (N1).
- Agent 0 must relay that accepted handoff before implementation, product-test,
  deliverable-state, or substantive evidence writes begin.
- Before consuming the predecessor or dispatching any child, rerun APP-HOLD-1
  for `DEL-02-05` with the exact applicable operation and require `ALLOW`.
- Until released, work is limited to read-only inspection plus this instance's
  control-plane brief/status records.

## Declared reads

- Root and App agent doctrine, committed loop plan, Receipt 180, frozen
  orchestration plan and work graph, software workflow profile, and registered
  validation documents.
- The complete DEL-02-05 kit, status, dependencies, assessment, memory, and
  run records.
- DEL-04-05 RQ-001 accepted contract and the N1 terminal return when relayed.
- API-key storage, IPC/status, settings UI, provider-key store/runtime resolver,
  and their focused tests.
- Relevant authority clauses in `docs/PRD.md`, `docs/SPEC.md`, and
  `docs/CONTRACT.md`.

## Allowed tools

- Read-only repository inspection and deterministic shell checks.
- `apply_patch` only after dependency release, and only within the write targets
  below.
- A fresh read-only `TASK + software-code-review` child after the candidate
  diff is frozen, if executable or substantive acceptance evidence is added.

## Allowed write targets

- This instance's `LAUNCH_BRIEF.md`, `STATUS.json`, and terminal `RETURN.md`.
- After accepted N1 release only:
  `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Assessment_INSP-03_DEL-02-05.md`,
  `_STATUS.md`, `MEMORY.md`, and one new `_run_records/**` record as required by
  truthful calibration.
- A focused PKG-02 UI/status regression test may be added or refined only if
  post-N1 inspection proves the existing suite cannot directly evidence R03;
  the N1-owned storage test and all production source remain read-only.

## Exclusions

- No write to `frontend/electron/api-key-storage.ts` or any other production
  source.
- No write to the N1-owned API-key-storage regression test.
- No PKG-04 or PKG-09 deliverable-state/evidence write.
- No lifecycle transition, issuance, Checking Approval SHA change, provider or
  network expansion, credential-storage redesign, dependency/lockfile change,
  signing, notarization, publication, distribution, release claim, RunAtLoad,
  owner-machine deployment, decision register, receipt, shared completion log,
  shared fan-in, commit, push, or PR action.
- Anything newly discovered outside this node is reported upward and not
  silently absorbed.

## Expected outputs

1. Direct R03 evidence for the fixed runtime/status behavior, including the
   both-environment-keys case and UI/status source behavior without key
   disclosure.
2. Truthfully calibrated DEL-02-05 assessment/state, preserving
   `IN_PROGRESS` lifecycle and Checking Approval SHA unless separately ruled.
3. Exact check evidence and a terminal package return naming accepted outputs,
   blockers, reruns, derivative status, and the requested N3 release action.

## Acceptance criteria

- The accepted N1 handoff is present and its relevant changed bytes are
  preserved.
- R03 is directly proven as UI safeStorage > `ANTHROPIC_API_KEY` >
  `CHIRALITY_ANTHROPIC_API_KEY`; status remains `ui | env | none` and never
  exposes key material.
- Focused API-key UI/status tests pass; affected and full registered frontend
  gates pass; repository self-check and practitioner-harness pytest pass;
  APP-HOLD, scope containment, parse/schema, whitespace, and diff hygiene pass.
- A fresh read-only review returns PASS with zero actionable findings when the
  review condition applies.
- `_STATUS.md ## Remaining`, lifecycle, and Checking Approval SHA are changed
  only where evidence and authority permit; an empty Remaining section is not
  used to invent new scope.

## Escalation conditions

Escalate to Agent 0 on missing/unaccepted N1 handoff, APP-HOLD denial or
register mismatch, contract disagreement, required production-source or
N1-owned-test edits, lifecycle/approval-SHA implications, check failure that
cannot be remediated inside PKG-02, or any newly discovered cross-package
target.
