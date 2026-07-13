# Deterministic Reproducibility

| Artifact pair | SHA-256 | Verdict |
|---|---|---|
| `CLAIM_MAP_1.csv` / `CLAIM_MAP_2.csv` | `8655dfbcee182cc4e97a348f0816068c5160d759dfc8b29fe47f7b02a946759c` | byte-identical PASS |
| `PARITY_1.json` / `PARITY_2.json` | `eb3e7a6bd1050bec2c47c50cc11dc743470c65a4458770d07904c87e5b2c382f` | byte-identical PASS |
| `PARITY_1.md` / `PARITY_2.md` | `c67141790d454364a5cc0f31d2a7cc0da196143b80d2e0e265a3784410c704d7` | byte-identical PASS |
| `REVIEW_CHECKLIST_1.json` / `REVIEW_CHECKLIST_2.json` | `7b5658adaab6a771788db8dc2ec9f2667cc8452b0b25914554694b704e734913` | byte-identical PASS |
| `ScopeOfWork_1.html` / `ScopeOfWork_2.html` | `0676f9d1df204825d4f5a481173c10c21a6f6682c9a4ba967c8fc2339c8413fe` | byte-identical PASS |

The HTML contains canonical candidate SHA-256 metadata and a derivative-view notice. It contains no script tag, `src=`, `href=`, or external resource reference. Checklist derivation against invalid `LEGACY_FOUR_DOC` input exited 1 and created no output artifact.

Verdict: `PASS`.
