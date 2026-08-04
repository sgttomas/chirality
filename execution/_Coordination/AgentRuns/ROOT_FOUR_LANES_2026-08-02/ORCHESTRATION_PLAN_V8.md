# HELP_HUMAN orchestration plan — plan version 8

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL`

## Owner authority

Exact acceptance/application ruling:
`OWNER_RULING_2026-08-03_COV_POST_001_ACCEPT_APPLY.md`, SHA-256
`8a9c005aa219d6e19f58e164721368ad72418019960182379edf52d5327a9851`.

Accepted candidate SHA-256:
`23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`.
Accepted diff SHA-256:
`205edf58e8a461e049bccdd76100cb3921254b122db2d3957461dc58b5d5e92e`.

## Node

| Node | Agent 1 | Objective | Stop |
|---|---|---|---|
| S5 | SCOPE_CHANGE | Apply the exact accepted candidate to the one live decomposition path, validate exact containment/protected hashes, run a fresh read-only AUDIT_DECOMP backcheck of COV-POST-001, and return for human confirmation. | Stop before human confirmation, SCA-003 closure, `_LATEST.md`, DEL packet/N0, runtime/client/project, lifecycle/release/reliance, Task Management, or Git effect. |

## Frozen pre-application state

- live decomposition SHA-256:
  `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`;
- applied PRD SHA-256:
  `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`;
- `_ScopeChange/_LATEST.md` SHA-256:
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`;
- scope ledger SHA-256:
  `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`;
- deliverable register SHA-256:
  `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`;
- S4 return SHA-256:
  `8ba4c4f194ec2276021af8a49e087ff7bc009386e8802580409946ca0a4ca947`;
- S4 validation SHA-256:
  `feccaf181660b6bf06f4a92066108ff3678553e1bbca5d28c794bfda81b174af`.

## Fan-in acceptance

S5 fan-in is acceptable only if live decomposition becomes byte-identical to
the accepted candidate, every protected hash remains frozen, fresh audit
evidence independently closes or precisely retains COV-POST-001, and the
manager records that human Gate 1 confirmation remains unperformed. A PASS
audit is evidence for the human; it is not confirmation or closure.
