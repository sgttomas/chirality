# Step 0 Evidence

Date: 2026-09-04
Candidate revision: R6 / remediation R2
Execution class: delegated-harness-native ephemeral Agent 2
Role calibration: role not mechanically enforced; governed-workflow role
evidence instruction-asserted; K-SUBAGENT/non-delegation instruction+config
asserted, not mechanism-proven; no descendant launched

## Isolation and basis

- Canonical repository used only as the worktree source:
  `/Users/ryan/.codex/worktrees/85d6/chirality`.
- Isolated remediation preparation worktree:
  `/private/tmp/chirality-app-v3-app-hold-bootstrap-20260904/remediation/implementer-r2`.
- Local branch:
  `codex/app-hold-dapp104-remediation-candidate-r2-2026-09-04`.
- Exact preparation basis and `origin/main` at worktree creation:
  `287b82f16c0d3970bac71e40b0e41fdd50569b08` (PR #700 merge).
- A read-only `git ls-remote --refs origin refs/heads/main` returned exactly
  one matching ref at that SHA before any R2 write.
- The worktree was clean before candidate preparation.
- Before any write, all 61 R4 live-manifest paths were revalidated against
  exact current main: eight MODIFY preimages and regular-file kinds matched,
  all 52 ADD paths were absent, and the dynamic receipt path was a regular
  file. D-APP-104 remained free; target/SOW, pointer, authority, cursor, and
  approval-history checks also matched. The R4 static patch then applied
  conflict-free to the clean current basis.

## Governing inputs

Read before implementation: root `AGENTS.md`;
`AGENT_HELPS_HUMANS.md`; App `AGENTS.md`;
`loop/LOOP_INIT.md`; the standing plan selected from committed HEAD,
`loop/WORKPLAN_2026-09-03_app_dev_loop.md`; live APP-HOLD tool, register,
tests, fixtures and README; the decision register and D-APP-75/79/81
precedents; the receipt contract; the full approved R4 candidate; immutable
R3 preparation PASS, preserved application return/commit, and failed
post-application R1 report; and the frozen SCA-APP-009 Gate-3/4/5 materials.

## Live preimage

- Receipt validator: `VALID`. The physical ledger tail is `Receipt-225`
  (`Parent-Receipt: Receipt-224`). The validator's legacy summary text says
  "frozen through Receipt-52"; that pre-existing summary defect is reported,
  not treated as the cursor.
- Authority corpus: v20, all members `MATCH`, no drift.
- APP-HOLD scan: 53 contracts, zero held, header-only preimage register,
  register parity `PASS`.
- Known `DEL-03-01` ordinary dispatch check: `ALLOW`.
- Unknown `DEL-09-07` ordinary dispatch check: fail closed, exit 2.
- Live decomposition SHA-256:
  `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`.
- Live companion-register SHA-256:
  `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`.
- Live `_ScopeChange/_LATEST.md` SHA-256:
  `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`.
- Highest live App decision ID: `D-APP-103`; `D-APP-104` was free.

## Historical authorization identity

- Preparation PASS SHA-256:
  `ef68c9b8d883029278d5ade347a66bc09a80178462c0932088cb562d74de714d`.
- Preserved application commit:
  `92ef9b3c62dcf28184956a17685dd51f89a1332e`, with sole parent
  `77ea8aa68affdb0485134b23d55303c362a312ac`.
- Applicator return SHA-256:
  `abed6d76e8a5d58152a86798cd3e1b9b38a9192e65ae9fccac109c2e2fe34955`.
- Post-application FAIL report SHA-256:
  `8257d40edb46709cd16b5a4f7511cba3c5d78d246ac67d7c186c58b6fadbc9d1`.
- Artifact-remediation R1 independent review SHA-256:
  `39e43788ea83d1f44d8526976bd2e0c850af2d1a1209d8f151c6b20296fb909e`.
  Its zero-BLOCKER/two-MAJOR verdict is closed only by the R6 renderer/FIFO
  byte repair and a newly reconstructed lawful `AWAITING_OWNER` future-tree
  simulation; neither reviewer-reported tree hash is reused.
- Prior exact owner answer: `Yes`, dated 2026-09-04, for approval root
  `4f0f72d14ffbabd1fd9e5ed47d911fd95cbf3ffe98c32a1b0b5d966572e7c139`
  and artifact digest
  `091817d7107f91b9175470b6c6a6403240c52dcb2e86a180d282b6fddeae622c`.
  Those identities are historical evidence and do not authorize this
  replacement candidate.

## Frozen SCA facts independently reverified

- Gate-3 decomposition candidate SHA-256:
  `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`.
- Gate-3 companion candidate SHA-256:
  `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`.
- Gate-4 `FUTURE_WRITE_SET.csv` fixes the exact target folder as
  `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/`
  and fixes the five PREPARATION-owned structural filenames.
- That target folder was absent on the preparation basis.
- A committed-HEAD search and read-only search over the frozen SCA evidence
  found no earlier conflicting definition of either stable entry-path token.

## Authority boundary

Ryan Tufts authorized exact-candidate preparation only. No application,
D-APP-104 ruling, live decision-register change, live receipt, SCA authority
postimage, pointer movement, PREPARATION dispatch, scaffold, contract,
product/frontend, Root, plans, Task Management, lifecycle, reliance or
release act occurred in this preparation.
