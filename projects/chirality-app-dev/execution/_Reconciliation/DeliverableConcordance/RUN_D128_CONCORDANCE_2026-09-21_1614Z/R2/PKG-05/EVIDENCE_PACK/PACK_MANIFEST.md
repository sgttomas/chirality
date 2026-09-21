# Evidence pack manifest — PKG-05 (R2, wave 2)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-05 WORKING_ITEMS manager under
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Placeholders:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder. Commands run from `<RUN>`.
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv R2/PKG-05/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p R2/_shared/EVIDENCE_PACK/REACHABILITY.csv R2/PKG-05/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 15 | `7b1e407f1249e09e8777b12777ec65d3ae35bd3e3bec6bb067199df09c11c572` | `python3 R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-05 --out R2/PKG-05/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 474 | `8abec7b3c6ce5e852672a5ab46e5d168c4f5d09fbdc6e4280d7f2fd11d203331` | `python3 R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-05 --out R2/PKG-05/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv R2/PKG-05/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |

## Checks

- Items 1, 2, 5: byte-for-byte copies; `shasum -a 256` of source and copy are identical and equal the
  values in `R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the data rows of each `--package PKG-05` output are byte-identical (`cmp`) to the
  `DEL-05-*` rows of the corpus-wide check run in `R2/_shared/ALL_DELIVERABLES_CHECK/`.

## Content notes (for workers)

- **REFERENCE_HASHES:** all 15 rows (5 deliverables × CONTRACT/SPEC/PRD) have `Match = NO` — every
  recorded `_REFERENCES.md` MATCH hash fails to reproduce at the frozen basis. Per CONVENTIONS §2.7
  this is one `REGISTER-n` row per deliverable, cited as `HASH-RECOMPUTE@00115c719`.
- **DECISION_HITS:** 474 rows — DELIVERABLE 447, RULING 18, REGISTER 9. Per deliverable: DEL-05-01 94,
  05-02 124, 05-03 100, 05-04 66, 05-05 90.
- **D-APP-127_APPLICATION_MAP:** the only PKG-05 carrier citing D-APP-127/D-GOV-43 with the applied
  effect is `DEL-05-02/_STATUS.md` (`YES`); every other PKG-05 carrier is `NO` or `ABSENT`.
- **REACHABILITY:** import-based and module-level (see the shared manifest's known limits). A re-export
  or one imported helper marks a whole module LIVE; some LIVE modules are never rendered or executed.
  Treat it as a starting hint and confirm reach for the specific symbol from the actual entry point.
