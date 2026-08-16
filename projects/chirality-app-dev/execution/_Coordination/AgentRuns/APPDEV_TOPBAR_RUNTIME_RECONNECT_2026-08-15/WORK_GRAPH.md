# Frozen work graph v1

| Node | Role / method | Depends on | Writes | Return gate |
|---|---|---|---|---|
| `A2-PKG02-RECONNECT-IMPLEMENT-01` | Agent 2 `TASK + software-bounded-implementation` | accepted activation | `projects/chirality-app-dev/frontend/**` only | source, component/render and behavior tests, focused evidence, scope proof |
| `A2-PKG02-RECONNECT-REVIEW-01` | fresh Agent 2 `TASK + software-code-review` | accepted implementation return and frozen diff | none | `COMMIT-SAFE` or `BLOCK`, actionable findings and residual risk |
| `A1-PKG02-RECONNECT-01` | WORKING_ITEMS fan-in | `COMMIT-SAFE` review | selected deliverable closeout files and managed run root | required checks, rationale attribution, exact residual removal, handoff |

Concurrency: none; serialized because the reviewer consumes the frozen implementation diff. Integration owner: `A2-PKG02-RECONNECT-IMPLEMENT-01` for product files, then the manager for deliverable/coordination closeout. Escalation: public-contract expansion, new runtime semantics, fast-reject boundary hit, scope drift, or review `BLOCK`.
