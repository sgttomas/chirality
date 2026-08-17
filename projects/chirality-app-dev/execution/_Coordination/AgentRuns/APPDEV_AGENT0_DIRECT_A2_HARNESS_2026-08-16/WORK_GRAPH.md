# Work Graph

| Node | Owner | Depends on | Write scope | Fan-in gate |
|---|---|---|---|---|
| `A2-IMPLEMENT-01` | bounded implementation specialist | none | two harness source files and directly focused PKG-08 tests | focused behavior tests and exact scope |
| `A2-REVIEW-01` | fresh read-only software-code-review specialist | frozen `A2-IMPLEMENT-01` diff | none | `PASS` with no actionable finding |
| `A2-REMEDIATE-02` | bounded implementation specialist | integrated-review BLOCK finding 1 | managed-delegation source and focused test | canonical TASK class enforced; focused tests pass |
| `A2-REVIEW-02` | fresh read-only software-code-review specialist | frozen corrected full product/test diff | none | `PASS` with no actionable finding |
| `WI-FAN-IN` | WORKING_ITEMS manager | accepted implementation and review | DEL-08-04 state/run record and this run root | validated child returns, hygiene, handoff |

Execution is serialized. The review consumes 100% of the frozen product/test node diff.
