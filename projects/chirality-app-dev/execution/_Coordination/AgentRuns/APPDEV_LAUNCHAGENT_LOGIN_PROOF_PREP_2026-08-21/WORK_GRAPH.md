# Work graph v1

- Selection authority: owner `PREPARE-THEN-OWNER` ruling relayed by Agent 0.
- Posture: `MIXED`, one implementation node followed by one fresh read-only
  review node over 100% of the frozen product diff.
- Package owner: `WI-PKG09-LOGIN-PROOF-PREP-01` owns exactly PKG-09, narrowed
  to DEL-09-04.
- Integration owner: the WORKING_ITEMS manager owns DEL-09-04 state and final
  fan-in records. Agent 0 owns tranche integration and shared receipt surfaces.

| Node | Objective | Depends on | Write owner | Checks / gate |
|---|---|---|---|---|
| N1 `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-01` | Build the smallest fail-closed prepare/capture harness and focused tests for a later login-session proof. | none | frontend script/test plus TASK run record only | focused tests, affected registered checks, scope containment |
| N2 `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-01` | Fresh `software-code-review` of 100% frozen N1 product diff. | N1 accepted | read-only; runtime-owned return only | PASS with zero actionable findings |
| N3 manager fan-in | Write minimal owner procedure, deliverable evidence/state, manager return, and handoff. | N1 and N2 accepted | manager-only governed records | typecheck, full Vitest, build, applicable static/script checks, practitioner gates |

- Edge: `N1 -> N2 -> N3`; no concurrent writes.
- Escalation points: any need to alter the owner/default LaunchAgent, perform
  logout/login, bootstrap the prepared proof job before logout, mutate the CLI
  launcher, broaden provider/network/release scope, or cross the declared write
  boundary returns upward and stops the affected node.
- Future proof boundary: preparation checks prove only harness readiness. The
  owner-scheduled logout/login and subsequent capture remain unexecuted.
