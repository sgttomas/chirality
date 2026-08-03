# Validation

Overall: `PASS FOR PARTIAL/HELD HANDOFF`

## Authority and state

| Check | Result |
|---|---|
| D-APP-90 packet preserved | PASS — SHA-256 `eda5303254f5d1fdf624bf49c1f6652735235f7ee59e899af6f284107d7b3c57` |
| Separate ruling | PASS — SHA-256 `cde0ff58190ef83e6ec78bb581cf70a96ee542d534efc35ed6a2324533f036b1` |
| Exact token and rider | PASS — verbatim in ruling |
| Register | PASS — one D-APP-90 row, `RULED (Option D — bounded comparative architecture proof)` |
| D-APP-91 | PASS — zero files and zero row |

## Basis and measurements

| Check | Result |
|---|---|
| Base/remote alignment | PASS — HEAD and `origin/main` both `7249281e1f84ba5abee3c31c2fea3736b22000d3` after safe no-overlap fast-forward |
| Current-tree fingerprint | PASS — 185 files, `ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4` independently reproduced |
| Basis manifest | PASS — 4 columns, 18 data rows; recorded source hashes reproduce |
| Measurement CSV | PASS — 13 columns, 3 rows |
| Reconciliation | PASS — `P=9`, `R=11`, B `E=20`, extraction-review population `61`, `BM=8`, MCI A/B/C `18/37/22 + U` |

## Sequencing and verification

| Check | Result |
|---|---|
| Committed-main Piping response | ABSENT — only inbound request and product-direction notice found at `origin/main@7249281e1…` |
| UI-delta lane | PASS — `HELD_BY_SEQUENCE`; no delta inferred |
| Three primary Agent 2 sessions | PASS — actual sessions completed with disjoint sole returns |
| Fresh adversarial attempt 1 | INTERRUPTED — no return, retained as provenance |
| Fresh adversarial R2 | PASS_WITH_REPAIRS — SHA-256 `e121834b923db38851313ec7dae57dfe30c6000f28cb2fac41268107006cf0ae` |
| Exact repairs | PASS — two stale seam references and four trailing spaces only |
| Post-repair stale exact phrases | PASS — zero in live manager artifacts |
| Post-repair trailing whitespace | PASS — zero across run Markdown/CSV |

## Preservation

- D-APP-89 accepted migration boundary preserved.
- D-APP-88 helper remains blocked/absent and a future parity-rerun advisory.
- Generic runtime, sandbox, identity, version, resume, and Bash remain
  `BLOCKED_BY_ROOT`; no Agent-2 Bash.
- Historical-relations CSV remains SHA-256
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`;
  the six D-APP-81 relations remain UNKNOWN.
- No product, PRD, decomposition, SCOPE_CHANGE, deliverable/status, Task
  Management, receipt/corpus, Root/Piping/PEC, completion-log, release,
  lifecycle, or publication write occurred.
- No build, package, test, dependency install, or post-sync Git operation was
  performed because this is a static derivative proof.
