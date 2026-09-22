# Evidence pack manifest — PKG-08

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 wave 1; built by the PKG-08 WORKING_ITEMS
  manager under `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
  `<RUN>` = the run folder. No git was used to build items 3 and 4 (files read from the frozen tree).
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p <RUN>/R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv .`; SHA-256 equals the shared manifest |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p <RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv .`; SHA-256 equals the shared manifest |
| 3 | `REFERENCE_HASHES.csv` | 15 | `ac8afbf68a77fdf651d664763e68113dff79d769fd1b612adb3dd800eca8f77b` | `python3 <RUN>/R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-08 --out <RUN>/R2/PKG-08/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 516 | `f5b5413ae8d3fc06fe928cc58c4a8e8db3d4bb853ab0ff8eb298b56a6a865b63` | `python3 <RUN>/R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-08 --out <RUN>/R2/PKG-08/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p <RUN>/R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv .`; SHA-256 equals the shared manifest |

## Checks

- Items 1, 2, 5: `shasum -a 256` of the copy equals the source and the value in
  `<RUN>/R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the `DEL-08-*` rows equal the `DEL-08-*` rows of
  `<RUN>/R2/_shared/ALL_DELIVERABLES_CHECK/` (`diff`, no output).
- Script SHA-256 as recorded in the shared manifest: `reference_hashes.py`
  `9a2af186…7c30c`, `decision_hits.py` `0c452b6d…6bbfb`.

## Observation

All 15 `_REFERENCES.md` MATCH verdicts in PKG-08 (5 deliverables × CONTRACT, SPEC, PRD) fail to
reproduce at the frozen basis (`Match = NO`). Each deliverable therefore carries REGISTER rows
per `CONVENTIONS.md` §2.7.
