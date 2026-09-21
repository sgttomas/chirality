# Evidence pack manifest — PKG-06 (R2, wave 1)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-06 WORKING_ITEMS manager under
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Placeholders:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder. Commands run from `<RUN>`.
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv R2/PKG-06/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p R2/_shared/EVIDENCE_PACK/REACHABILITY.csv R2/PKG-06/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 18 | `4c58819b4a5e2b7340ad7884f1eb56b519ff791f716a399a45beb40df5c23fa1` | `python3 R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-06 --out R2/PKG-06/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 504 | `367b5820e9ad78455521088eaccd0796c4453513f0bb53d08153122201570508` | `python3 R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-06 --out R2/PKG-06/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv R2/PKG-06/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |

## Checks

- Items 1, 2, 5: byte-for-byte copies; `shasum -a 256` of source and copy are identical and equal the
  values in `R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the data rows of each `--package PKG-06` output are byte-identical (`cmp`) to the
  `DEL-06-*` rows of the corpus-wide check run in `R2/_shared/ALL_DELIVERABLES_CHECK/`.

## Content notes (for workers)

- **REFERENCE_HASHES:** all 18 rows (6 deliverables × CONTRACT/SPEC/PRD) have `Match = NO` — every
  recorded `_REFERENCES.md` MATCH hash fails to reproduce at the frozen basis. Per CONVENTIONS §2.7
  this is one `REGISTER-n` row per deliverable, cited as `HASH-RECOMPUTE@00115c719`.
- **DECISION_HITS:** 504 rows — DELIVERABLE 494, RULING 8, REGISTER 2. Per deliverable: DEL-06-01 83,
  06-02 86, 06-03 113, 06-04 59, 06-05 98, 06-06 65.
- **D-APP-127_APPLICATION_MAP:** no PKG-06 carrier cites D-APP-127 or D-GOV-43 (all `NO`/`ABSENT`).
- **REACHABILITY:** all 43 LEGACY_ONLY modules sit under `frontend/src/lib/harness`, which is the main
  implementation area for this package (tool surface, permission overlay, hooks). See the shared
  manifest's known limits (module-level, not symbol-level; unmarked type-only imports count as edges).
