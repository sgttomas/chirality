# Current-State Premise Check

**Check basis:** `c487b7dd57a378e2f74417118e78e7f61a161629`

**Tree:** `ff71da5d822902ddd04ff00523e21c88c8d66edf`

**Prior admitted basis:** `4214915d9fcfecdc2952626421bf50b0e5f7845b`

**Pre-SCA audit basis:** `fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`

## Deterministic results

| Check | Result |
|---|---|
| Prior admitted basis is an ancestor of current basis | `PASS` |
| SCA-APP-005 subject commit `16f7ed612...` is an ancestor of current basis | `PASS` |
| D-APP-48/49 subject paths are unchanged from `fb16e32...` | `PASS` |
| Packet broader premise paths unchanged | `30/31 PASS` |
| Sole broader-premise change | Piping `SOFTWARE_DECOMP.md` front-matter revision `0.9` to `0.10` |
| D-APP-48 ruling pin | `ee290e22a8c19d46fb8004114d2ede55b805fba4` |
| D-APP-48 live JSON pin | `55a066fdff6877d8aa2a49ce08a545ac98872848` |
| Both D-APP-48 pin objects resolve | `PASS` |
| Ruling pin is an ancestor of live JSON pin | `PASS` |
| App production source files importing `@chirality/harness-contract` | `67` |
| App test source files importing `@chirality/harness-contract` | `39` |
| Combined D-APP-48 / D-30 validator | `EXPECTED FAIL — source.commitSha mismatch` |

The sole changed file in the selected packet's 31-path broader premise set is
`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md`.
The exact diff changes only YAML front-matter `revision: 0.9` to
`revision: 0.10`; no D-30, D-31, DEC-063, runtime-client, contract, or
D-APP-48/49 substance changes.

The post-OD7 basis also lands the D-APP-75 effective-state closeout and the
Root-routed Piping mismatch notice. Those records preserve the no-repin,
non-client, and separately governed follow-on posture. They do not alter the
owner-selected F1/E1 effect.

This check validates identity and enumerated premises only. It does not rerun
the audit's builds or tests, prove runtime reliance, or decide semantic
ownership, lifecycle closure, facade retirement, or release.
