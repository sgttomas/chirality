# TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01 — Sealed Launch Brief

- **RequestedBy:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **RunID:** `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- **ParentInstanceID:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **ChildInstanceID:** `TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01`
- **Role:** TASK / Agent 2 (no delegation)
- **TaskSkill:** `software-bounded-implementation`
- **TaskProfile:** `NONE`
- **ApplyEdits:** `true`
- **PackageID:** `PKG-02`
- **DeliverableIDs:** `DEL-02-05`
- **ScopePath:** `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback`
- **PROFILE_PATH:** `projects/chirality-app-dev/software-workflow.json`

## Objective

Repair the DEL-02-05 R03 IPC/status consumer so it validates and consumes the
daemon credential store's accepted non-secret `source: ui | env | none`
field, removes local environment-based source re-inference, and preserves
unavailable/store/remove/provider-isolation and non-disclosure behavior.

## Accepted basis and dependency

- Git basis: `6710ee6354debc201f6a454e2802897026cd4b38`.
- Accepted amended N1 handoff:
  `instances/WI-PKG04-API-KEY-PRECEDENCE-01/HANDOFF_STATE_V2.md`.
- Read-only N1 identities:
  - `frontend/electron/api-key-storage.ts` SHA-256
    `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db`
  - `frontend/src/__tests__/electron/api-key-storage.test.ts` SHA-256
    `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4`
- APP-HOLD dispatch and accepted-dependency-consumption: `ALLOW` for
  DEL-02-05.
- Governing amendment:
  `amendments/WI-PKG02-API-KEY-PRECEDENCE-01/v2.md`.

## Declared reads

Root/App instructions; WORKING_ITEMS and TASK contracts; the complete
DEL-02-05 kit; amended N1 return/handoff; `api-key-storage.ts` and its tests;
`api-key-ipc.ts`, preload/main callers, settings UI, IPC and settings tests;
PRD FR-030, SPEC 12.3/16.2, CONTRACT K-KEY-1; workflow profile and validation
docs; `software-bounded-implementation` skill and companions.

## AllowedWriteTargets

- `projects/chirality-app-dev/frontend/electron/api-key-ipc.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-ipc.test.ts`
- This child instance's `STATUS.json` and `RETURN.md`.

## EXCLUSIONS

No N1 storage source/test edit; no settings UI or preload/main edit unless the
sealed objective proves impossible (return blocker instead); no runtime/**,
public/root contract, provider/network, credential storage, error semantic,
dependency/lockfile, deliverable status/memory/evidence, lifecycle, approval
SHA, shared fan-in/receipt/log, Git, push, PR, merge, release, or delegation
action. Do not expose or log credential material.

## AcceptanceCriteria

1. `credentialStatusResult` consumes the daemon-owned source and does not read
   Anthropic or oMLX environment variables to infer it.
2. Simultaneous safeStorage/UI and environment credentials report `ui`;
   canonical-only and compatibility-alias-only environment cases report
   `env`; no source reports `none`.
3. Invalid/missing daemon source fails safely without credential disclosure;
   structured daemon-unavailable status, store/remove behavior, unsupported
   providers, and oMLX isolation are preserved.
4. Focused storage + IPC + settings-view Vitest pass; registered
   `frontend-test`, `frontend-typecheck`, and `frontend-build` pass.
5. Exact-path scope validation and whitespace checks pass; N1 accepted hashes
   remain byte-identical.

## ExpectedReturn

Return exact changed paths and behavior, tests/checks with counts and
normalized evidence, changed-path containment, N1 hash preservation,
unresolved risks/blockers, and confirmation of no Git/lifecycle/shared-surface
action. Persist terminal `STATUS.json` and `RETURN.md` in this instance.

## Escalation

Stop and report if correctness requires any excluded path, a runtime/public
contract change, new provider behavior, N1 source/test modification, or a
human/Agent-0 decision.
