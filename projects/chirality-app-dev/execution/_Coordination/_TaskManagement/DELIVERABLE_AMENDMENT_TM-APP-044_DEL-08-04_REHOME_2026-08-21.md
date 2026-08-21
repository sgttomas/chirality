# Deliverable-Amendment Package — TM-APP-044 Rehome to DEL-08-04

Date: `2026-08-21`

Status: `PREPARED_FOR_AGENT_0_ROUTING`

Prepared by: App TASK_MANAGEMENT

Route: Agent 0 → PKG-08 WORKING_ITEMS → DEL-08-04 owning production lane

This is a routed handoff package under TASK_MANAGEMENT Resolution Path 1.
It is decision support and exact amendment input, not the deliverable
amendment itself. TASK_MANAGEMENT has not edited the target deliverable.

## Authority and current-state basis

| Basis | SHA-256 / binding |
|---|---|
| `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/OWNER_RULING_2026-08-21_APP_PARKED_DECISION_SLATE.md` | `fb44a02cf9ebf31581c5fa2cb9bae82c06b6f66bf28eaed9c7bed4a494323a8d`; owner ruling 3 authorizes the rehome and preserves Root ownership |
| App product commit | `ac2cd801a06a0679bc86830c627218ccca78b658`; `fix(app): align Agent 0 bounded delegation rules` |
| `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_run_records/AGENT0_DIRECT_A2_HARNESS_REPAIR_2026-08-16.md` | `112a7701960ee66c4d752ee592d39fb12947949591c71b0d0954f970b023a0cc`; App harness repair complete for configured routes and root TM-ROOT-125 remains external |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PARALLEL_PRODUCT_NODES_INTEGRATION_2026-08-17/HANDOFF.md` | `9d512a8949cd6aa036ca39a58f5af9c545c30f8e0e385058881610c7b5f2b70b`; accepted App integration scope and explicit root residual |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PARALLEL_PRODUCT_NODES_INTEGRATION_2026-08-17/INTEGRATED_REVIEW.md` | `7837e46a0ac9e48fc8c9662cbb9d8ba3f363a4404b15b111188cf5385994ed39`; corrected integrated review `COMMIT-SAFE`, zero findings |
| `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` | `62c85b42200037f50da5563373eca7337c61c0209eece5e1d6b53cd2d02ed865`; Receipt 172 binds commit `ac2cd801a...`, checks, and TM-ROOT-125 as the external residual |
| `execution/_Coordination/_TaskManagement/REGISTER.csv` row `TM-ROOT-125` | file SHA-256 `6955ae0b1a606e7053e78ccf33258f3247eee6d4ef8133720a0dbeb939dc9978`; `OPEN`; Root-owned validator/test/HELP_HUMAN metadata alignment |
| Current DEL-08-04 `_STATUS.md` | `ca03802edc06bcfc5509d41382f42bf91062e9b9b9d0dc778d4b58670b26a8a0`; no TM-APP-044 residual yet appears under `## Remaining` |

## Calibration

The App-side implementation requested by the original TM-APP-044 concern is
already complete and integrated. The amendment must **not** request another
edit of `managed-delegation.ts`, `subagent-governance.ts`, or their landed
tests. The only live App residual supported by the evidence is cross-surface
validation/integration after the Root-owned TM-ROOT-125 alignment lands.

The App loop must not edit Root validator, instruction metadata, tests,
registers, or other Root surfaces. TM-ROOT-125 is an external dependency, not
an App work item.

## Exact target

`projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_STATUS.md`

### Proposed `## Remaining` addition — exact text

Insert the following bullet without removing or changing the existing
D-APP-103 decision-packet item:

```markdown
- After the Root loop lands its separately owned `TM-ROOT-125` metadata,
  validator, test, and `HELP_HUMAN` allowlist alignment, run and evidence the
  post-root cross-surface integration check against the already-landed App
  harness implementation at commit
  `ac2cd801a06a0679bc86830c627218ccca78b658`: confirm the configured
  Agent 0 route admits an allowlisted canonical `TASK` Agent 2 and an
  explicitly enabled ephemeral generalist, preserves fail-closed rejection
  for unsupported routes, and passes the affected Root validator/tests plus
  the App managed-delegation and subagent-governance checks. Root surfaces
  remain Root-owned; no duplicate App implementation or App-to-Root write is
  in scope.
```

### Proposed `## History` addition — exact text

Insert the following newest history entry:

```markdown
- 2026-08-21 - Owner rehomed the TM-APP-044 residual to DEL-08-04. The
  App-side harness code and tests already landed at
  `ac2cd801a06a0679bc86830c627218ccca78b658` and were integrated under
  Receipt 172; the only added Remaining work is post-root cross-surface
  validation/integration after the Root-owned `TM-ROOT-125` alignment lands.
  No duplicate App implementation, Root write, lifecycle change, or Checking
  Approval SHA change is authorized.
```

## Nine-domain completeness scan

| Domain | Routed treatment |
|---|---|
| Action Item | Rehome only the evidence-supported post-root integration residual; do not duplicate the landed App implementation. |
| Assignment | PKG-08 WORKING_ITEMS is R/S for the DEL-08-04 amendment and later App-side validation node; Root's owning loop is C/I for the TM-ROOT-125 dependency; A remains human-only. |
| Prioritization | Preserve TM-APP-044 `MEDIUM`; basis is the 2026-08-16 promotion plus the 2026-08-21 owner rehome ruling. This package creates no execution priority by itself. |
| Deliverables | Amendment lands only in DEL-08-04 `_STATUS.md`; no other deliverable or Root surface is a write target. |
| Work | Apply the exact Remaining/History text. Later, after TM-ROOT-125 lands, execute the bounded cross-surface checks and any App-local integration repair actually exposed by those checks. |
| Planning | Sequence: (1) apply and hash-bind the DEL-08-04 amendment; (2) await committed Root TM-ROOT-125 completion evidence; (3) select and run the App validation/integration node; (4) bind results to DEL-08-04. The Root dependency remains non-App work. |
| Approval | The owner ruling authorizes this rehome. Any Root implementation and any lifecycle, release, or Checking Approval SHA effect remain with their owning instruments. |
| Checking | At amendment time: exact-text/diff/containment and App status validation. At execution time: affected Root validator/tests, focused App `managed-delegation` and `harness-subagent-governance` tests, and a configured-route cross-surface check showing allowed TASK/generalist admission and unsupported-route rejection. WORKING_ITEMS must record exact commands and results. |
| Decisions | No new D-APP decision is required to apply the amendment. This package cites the 2026-08-21 owner ruling and creates no decision or foreign-loop authority. |

## Acceptance checks for the amendment application

1. Before dispatch or reliance, PKG-08 WORKING_ITEMS runs the mandatory
   APP-HOLD-1 preflight from `projects/chirality-app-dev` for target
   `DEL-08-04`, using the declared DEL-08-04 entry path, and records a pass.
2. Only the target DEL-08-04 `_STATUS.md` is changed by the amendment node,
   apart from that node's ordinary package-local evidence surfaces.
3. The two exact text blocks above are present.
4. Existing `## Remaining` content, lifecycle state, directive,
   authorization basis, and Checking Approval SHA remain unchanged.
5. The resulting target bytes and the owning closeout evidence are SHA-256
   bound.
6. The route returns the amended path, resulting SHA-256, and evidence path
   to Agent 0 for TASK_MANAGEMENT closure echo.

## Handoff state

- Upstream accepted evidence: App commit `ac2cd801a...`, Receipt 172, and the
  owner ruling SHA listed above.
- Derivative-package status: this amendment package is a derivative
  coordination artifact; it does not replace DEL-08-04 or Root authority.
- Closure verdict: `TM-APP-044 OPEN — AMENDMENT NOT YET APPLIED`.
- Rerun requirement: none for package preparation; amendment application and
  later post-root validation have the checks stated above.
- Remaining blocker: Root `TM-ROOT-125` is still `OPEN`; that blocks the later
  cross-surface validation, not the DEL-08-04 amendment itself.
