# Agent 0 Direct Agent 2 Harness Repair — 2026-08-16

Run: `APPDEV_AGENT0_DIRECT_A2_HARNESS_2026-08-16`

## Outcome

The App harness now admits an Agent 0 to an allowlisted canonical `TASK` Agent 2 only when the child instruction resolves to Agent Type 2 and `AGENT_CLASS: TASK`; missing or non-TASK class metadata fails closed. It admits an ephemeral generalist only when the parent instruction explicitly sets `allow_generalist_agent2: true`. Named Agent 1 dispatch, Agent 1 child rules, dedicated Agent 2 qualification, allowlist enforcement, tool/scope gates, and Agent 2 non-delegation remain fail-closed.

The current root `HELP_HUMAN` metadata does not yet expose either direct route. TM-ROOT-125 owns that coordinated validator/frontmatter alignment; this App repair does not bypass or synthesize it.

## Evidence

- Focused Vitest after canonical-class remediation: PASS, 2 files / 30 tests.
- Fresh read-only review of 100% of the corrected frozen four-file product/test diff: PASS, zero actionable findings; prior TASK-class BLOCK resolved.
- Exact node scope validation: PASS, zero violations.
- APP-HOLD integrity scan: PASS, 53 contracts, 0 held, register matched.
- Root harness self-check: exit 0 with existing baseline findings.
- `git diff --check` for the four-file node: PASS.
- Registered check selection names `frontend-test`, `frontend-typecheck`, `app-hold-integrity`, and `harness-self-check`; this node claims only the focused tests and narrow deterministic checks above. Consolidated closeout still owes the registered full frontend test and typecheck.

## Governance disposition

D-APP-64 is not applicable: this was a deterministic governance-contract repair with no UI, product-disposition choice, owner-class boundary, provider/network change, or lifecycle/release act. The separately gated decision-replay Remaining item was not selected or changed.
