# Evidence pack manifest — R2 scope extension (EXT)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the EXT WORKING_ITEMS manager under
  D-APP-129 ruling D and `BRIEFS/R2_EXT_MANAGER.md` step 2; format per `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Scope:** extension units cut across packages, so items 3 and 4 are built with `--all`
  (all 54 deliverables) instead of `--package`.
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | byte-for-byte copy of `<RUN>/R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv`; SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | byte-for-byte copy of `<RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv`; SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 162 | `b155451494e8c8f3de887b9f54f6bf0e6e9ce2520237afa62baafcae2f6186d3` | `python3 _scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --all --out <RUN>/R2/EXT/EVIDENCE_PACK/REFERENCE_HASHES.csv` (run from `<RUN>/R2`; script SHA-256 `9a2af186dfc9b8ed4f71ba1e94c8e0990cb5ae329031072c640a17e3bdc7c30c`). Equals `_shared/ALL_DELIVERABLES_CHECK/REFERENCE_HASHES.csv` byte-for-byte |
| 4 | `DECISION_HITS.csv` | 6,084 | `95da0296bd8dc4c92a4917735f1bbfacf1958a9e15c2b1267dc5004ad8c5f525` | `python3 _scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --all --out <RUN>/R2/EXT/EVIDENCE_PACK/DECISION_HITS.csv` (run from `<RUN>/R2`; script SHA-256 `0c452b6da528c1a8613d1ce078d8d015539719f177c902a349c96d85cf06bbfb`). Equals `_shared/ALL_DELIVERABLES_CHECK/DECISION_HITS.csv` byte-for-byte |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | byte-for-byte copy of `<RUN>/R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv`; SHA-256 equals the shared manifest value |

Preflight: `<RUN>/R2/EXT/PREFLIGHT/<DEL-ID>.json`, 54 files, verdict `ALLOW` for all 54.
