# D-APP-89 Option B — Implementation Validation

Status: `PARTIAL — IMPLEMENTATION/CENSUS PASS; DEPENDENCY-TREE RERUNS REQUIRED`

The worktree contains no installed Root or App dependency trees. The sealed
brief forbids installation/network access, so missing binaries are recorded as
reruns rather than bypassed.

## Passed

| Check | Result |
|---|---|
| Path-complete export mapping | PASS — all 11 consumed and all 13 retained code subpaths exist in Root and each facade file directly re-exports its counterpart |
| Zero ordinary facade consumers | PASS — 0 production/test files outside the dedicated rollback test |
| Dedicated rollback-test census | PASS — exactly 13 facade imports |
| `npm --prefix projects/chirality-app-dev/frontend run harness:validate:contract-deps` | PASS — facade purity, zero ordinary consumers, 13 rollback probes, root dependency/lock/TS/Next absence |
| App receipt contract | PASS — frozen through Receipt-52 |
| D-APP-38 authority corpus | PASS — v18, 8/8 MATCH, no drift |
| Practitioner App status | PASS — 53 `IN_PROGRESS`; no status finding |
| Registered `harness-self-check` | PASS, exit 0; pre-existing generated REVIEW/WARN findings retained |
| Registered `app-hold-integrity` | PASS — 0 held; register match |
| Full practitioner pytest | PASS — 349 passed in 16.82s |
| `git diff --check` | PASS |
| Explicit owned-path `validate_change_scope.py` | PASS — 124 implementation/evidence paths, 0 violations |

Registered normalized evidence is in `REGISTERED_CHECKS.json`. The check
selector returned `frontend-build`, `frontend-test`, `frontend-typecheck`,
`harness-self-check`, and `app-hold-integrity` for the affected paths.

## Rerun-required checks

| Exact command | Observed result | Rerun trigger |
|---|---|---|
| `npm --prefix runtime run build` | exit 127, `tsc: command not found` | provision the repository-pinned Root dependency tree without changing source bytes |
| `npm --prefix runtime run typecheck` | exit 127, `tsc: command not found` | same |
| `npm --prefix runtime test -- tests/contracts-and-project.test.ts` | exit 127, `vitest: command not found` | same |
| registered App `npm run test` | exit 127, `vitest: command not found` | provision the repository-pinned App dependency tree |
| registered App `npm run typecheck` | exit 127, `tsc: command not found` | same |
| registered App `npm run build` | exit 127, `next: command not found` | same, after Root contracts build emits package `dist` |
| `npm --prefix projects/chirality-app-dev/frontend run desktop:pack` | exit 127 at nested build, `next: command not found` | same; rerun only with its existing `--publish never` posture |
| focused App `frontend/src/__tests__/lib/harness-contract-rollback.test.ts` | unavailable because `vitest` is absent; covered by the failed full-test invocation | provision App tree, then run the full test command or this focused file |

No install, network, release, publication, provider, or arbitrary Bash action
was attempted. These failures do not weaken the required end state and do not
constitute passing evidence; manager fan-in must retain them as reruns.

## Preservation checks

- `frontend/packages/harness-contract/**` compatibility exports are unchanged.
- DEL-03-01 remains `IN_PROGRESS`; Checking Approval SHA remains
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`; dependencies are unchanged.
- No Root/Piping/PEC source was written.
- No decision packet/register, PRD, decomposition, Task Management, receipt,
  completion log, or Git state was written by this TASK.
- The six D-APP-81 historical relations remain untouched.

## Derivative and handoff status

This evidence package is derivative of the accepted D-APP-89 packet/ruling and
the live source tree. It is not a new authority snapshot. The next owner is
`WORKING_ITEMS` for independent read-only verification and fan-in. Facade
retirement remains a later owner gate after landed-tree validation and fresh
census evidence.
