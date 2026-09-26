# Invocation-local D-GOV-33 federation preflight

Scope: PEC legacy-source retirement of the deliverable `_STATUS.md`
`## Remaining` population only (`task-management`, legacy-source retirement
invocation). Basis: fetched `origin/main`
`6281273fa7bd96b66703009e6325db2fa74815b3`. Run 2026-09-26 by the RR1
WORKING_ITEMS manager, from the repository root, CPython 3.13.7.

Command:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out projects/pec/execution/_Coordination/_TaskManagement/.candidates/TM_PEC_REMAINING_RETIREMENT_2026-09-26/federation.json
```

Exit 0. The output path was verified Git-ignored before the run
(`git check-ignore -v` → `.gitignore:95:projects/*/execution/_Coordination/_TaskManagement/.candidates/`).
The derived projection (SHA-256
`7d2e4e693d291308f461c4db41d3f9c4eeb5f628be477dffbf81c44dc1e77702`) is not
authority and is not committed.

Result: **COMPLETE** coverage across all 4 canonical tracked registers;
28 findings, 0 presented; register writes 0. Register positions:

| Register | OPEN | DEFERRED | ELEVATED | CLOSED (live) | Archived |
|---|---:|---:|---:|---:|---:|
| ROOT | 10 | 8 | 0 | 0 | 109 |
| APP | 7 | 14 | 0 | 0 | 34 |
| PIP | 7 | 32 | 0 | 1 | 12 |
| PEC | 8 | 1 | 0 | 0 | 16 |

Findings by class: `LOCAL_CLOSED_REMOTE_OPEN` 22 (Root `TM-ROOT-077`–`097`
against Piping `TM-PIP-002`–`022`, and `TM-ROOT-117` against `TM-APP-032`);
`MISSING_NOTICE` 5 (`TM-ROOT-003`–`006`, `TM-APP-036`);
`REMOTE_CLOSED_LOCAL_OPEN` 1 (`TM-ROOT-035` against `TM-APP-001`). **No
finding involves a PEC row.** They are reported, not resolved, and none is a
retirement disposition.

PEC register inputs (read-only): `REGISTER.csv` SHA-256
`634641f0b7bf2d1f53d74283cc5e5253fee49ee6292e58a74b751f477345376a`
(9 rows: 8 OPEN, 1 DEFERRED); `REGISTER_CLOSED.csv` SHA-256
`3c1349ba79ffb6eb0abc3502b0325da93ff28e7ecafd5498739a28ea0af11fd2`.

Local rows checked for duplication against the census population (no broad
harvest; only rows naming a census deliverable or its concern):

| Row | Relation to the census |
|---|---|
| `TM-PEC-004` DEL-04-01 feed-grammar boundary owner | Same deliverable as `DEL-04-01-REM-001`/`-002`; a boundary-ownership question, not the production obligation. Not a duplicate |
| `TM-PEC-005` limitation inventory and response-format seam | Same deliverable as `DEL-04-05-REM-*`; a home/shape question. Not a duplicate |
| `TM-PEC-018` run-record residue F7 and E-P26 | Touches DEL-03-02 run records; not a Remaining item |
| `TM-PEC-019` carried contract and REVIEW residuals | Names DEL-10-10, DEL-08-02, DEL-08-01, DEL-00-03; residuals handed by closed instruments, not Remaining items |
| `TM-PEC-024` DEL-01-05 inherited harness-FAIL baseline owner | Same deliverable as the frozen `DEL-01-05-REM-*` carrier; a baseline-ownership question. Not a duplicate |

No other open or deferred PEC row names a census key or deliverable concern.

Inputs and instruction hashes: Root `AGENTS.md`
`c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`;
`projects/pec/AGENTS.md`
`c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a`;
`workflows/task-management/WORKFLOW.md`
`d5e8eff5742326330c0f933dc322e07fbe6a2bb82ad151aadf803b001a02e654`,
`resources/contract.md`
`3162f7ed386bcac08c0e16c0feae3b7a7a5109ba4bf4f845acc66bd2d6dfd04e`,
`resources/method.md`
`d52403c983c92b1c65fe2b621d8c6bdc5c10e1fdb8c9ac99e95614137639c61e`.
