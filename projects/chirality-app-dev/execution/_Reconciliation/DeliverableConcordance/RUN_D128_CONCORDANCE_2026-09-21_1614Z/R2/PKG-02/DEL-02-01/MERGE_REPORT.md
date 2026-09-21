# DEL-02-01 split merge report

Script: `R2/PKG-02/_scripts/merge_split.py` (split plan: `_BRIEFS/SPLIT_PLAN.md`).

| File | Rows | SHA-256 |
|---|---:|---|
| `DEL-02-01/A/DEL-02-01_claims.csv` (sealed half) | 41 | `5282a7a81f852ff84f4e49a78498e0b476c34373d8f5847e113f2966abe6e419` |
| `DEL-02-01/B/DEL-02-01_claims.csv` (sealed half) | 37 | `946575525f0e14d17ee139631e15c7f57173b1399607cd2e8f5f4641bb52a114` |
| `DEL-02-01/DEL-02-01_claims.csv` (merged ledger of record) | 78 | `5cf0d2620c90c337a3a5a110c2886c97891077fec08e609e9657d07e6772f360` |

Checks: identical header; no duplicate ClaimKey; units and run-local numbering in their half's range.

Validator on the merged ledger (full CLAIM_INDEX):

```
RULES errors none | warnings none
RESULT PASS errors=0 warnings=0
```
