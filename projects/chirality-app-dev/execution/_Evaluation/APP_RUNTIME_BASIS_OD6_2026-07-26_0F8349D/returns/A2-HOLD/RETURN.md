# A2-HOLD terminal return

- **Basis:** `0f8349d90f58c1e6b3339263f5aafaf36e783a7e`
- **Verdict:** `PASS_WITH_WARNINGS`
- **Mode:** read-only ephemeral Agent 2
- **Repository writes:** none

## Held population

An independent scan found 53 contracts and exactly six references to the
unresolvable object `416b29033bbacb0bc3648d84033272b7ab4e6e11`.
The scan-derived set exactly matches `APP_HOLD_REGISTER.csv`:

| Deliverable | Package |
|---|---|
| `DEL-02-01` | `PKG-02` |
| `DEL-02-02` | `PKG-02` |
| `DEL-02-04` | `PKG-02` |
| `DEL-05-04` | `PKG-05` |
| `DEL-08-02` | `PKG-08` |
| `DEL-08-03` | `PKG-08` |

## Concordance

- D-APP-75 binds reliance, dispatch, checking promotion, and
  accepted-dependency consumption regardless of entry path.
- Live App instructions carry the same universal obligation.
- Every register row is `HELD`, uses `entry_path_scope=ANY`, has
  `repin_posture=NO_REPIN`, and cites D-APP-75.
- The live tool recomputes the population from all 53 contracts and blocks
  register drift.
- No ScopeOfWork repin occurred between the pre-application and accepted
  bases.
- The frozen proposal validates 22/22 hashes. Live tool and register bytes
  match the candidate. The only live/candidate difference is the
  owner-approved placement correction to the live test file, SHA-256
  `2d8d846b9aa9db7b47023a8f6af76649530e0a3c308fad7367c065a8f0bdcd2b`.
- The application and merge commits are ancestors of the accepted basis.

## Deterministic operation checks

All four operations against `DEL-02-01` returned exit 3 and
`BLOCK_APP_HOLD`, across WORKING_ITEMS, direct-human, API/other-workflow, and
resumed-session labels. A clear target returned `ALLOW`. A mixed fan-in
containing a clear and held target returned aggregate `BLOCK_APP_HOLD`.
An attempted exception input was rejected because no exception CLI exists.

The full live suite passed 12/12.

```text
HEAD=0f8349d90f58c1e6b3339263f5aafaf36e783a7e
contracts=53
held=6
register_match=true
register_sha256=52e331c44372815c842f402c3ca34cdfb1b3a2436c21a4526b2d9eeaf545fd21
scan_fingerprint=2164a7954d0125d8a001b65472d152b591c4f7ca93b22bc893eb74e418db98aa
```

## Enforcement distinctions and warnings

The prohibition is authoritative across App-loop entry paths. The
deterministic preflight blocks when invoked; fan-in enforcement remains a
managerial obligation rather than a universal product interceptor. The
always-check integrity entry validates corpus/register parity but does not
carry selected-target or operation context. Entry-path text is recorded but
not authenticated; it cannot release a held target because the verdict is
entry-path independent.

D-APP-75 still says `EffectiveCommit: PENDING_PR_MERGE` and
`APPLICATION_CLOSEOUT_CANDIDATE`, despite PR #363 having merged. This is
record-closeout residue, not an enforcement failure.

No persisted real-workflow post-application preflight/fan-in result was found
outside tests and proposals. The mechanics are proven; later operational
compliance still needs evidence.

## Rerun triggers

Rerun before each governed operation and at fan-in; after any HEAD,
ScopeOfWork, register, tool, instruction, workflow-profile, or object-store
change; and after App SCOPE_CHANGE, repin, hold amendment, or hold retirement.
