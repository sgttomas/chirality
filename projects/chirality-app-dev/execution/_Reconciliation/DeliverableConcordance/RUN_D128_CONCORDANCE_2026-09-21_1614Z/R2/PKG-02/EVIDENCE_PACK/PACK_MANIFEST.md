# Evidence pack manifest — PKG-02

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 wave 3; built by the PKG-02 WORKING_ITEMS
  manager under `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
  `<RUN>` = the run folder. No git was used to build items 3 and 4 (files read from the frozen tree).
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p <RUN>/R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv .`; SHA-256 equals the source and the shared manifest |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p <RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv .`; SHA-256 equals the source and the shared manifest |
| 3 | `REFERENCE_HASHES.csv` | 15 | `5f793e2e858155b0afe223ae95e14bf04dbda59f7fb8d5efd7fcc4ce4d711b96` | `python3 <RUN>/R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-02 --out <RUN>/R2/PKG-02/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 786 | `194d9f7b440fc283698a03c3339bbbda646b9c4e1eefef79244744642f3c3f0d` | `python3 <RUN>/R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-02 --out <RUN>/R2/PKG-02/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p <RUN>/R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv .`; SHA-256 equals the source and the shared manifest |

## Checks

- Items 1, 2, 5: `shasum -a 256` of the copy equals the source and the value in
  `<RUN>/R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the `DEL-02-*` rows equal the `DEL-02-*` rows of
  `<RUN>/R2/_shared/ALL_DELIVERABLES_CHECK/` (`diff`, no output).
- Script SHA-256 as recorded in the shared manifest: `reference_hashes.py`
  `9a2af186…7c30c`, `decision_hits.py` `0c452b6d…6bbfb`.

## Observations (reach facts only)

- All 15 `_REFERENCES.md` MATCH verdicts in PKG-02 (5 deliverables × CONTRACT, SPEC, PRD) fail to
  reproduce at the frozen basis (`Match = NO`). Each deliverable therefore carries REGISTER rows per
  `CONVENTIONS.md` §2.7.
- D-APP-127 application map: every PKG-02 carrier is `Revised = NO` except DEL-02-05 `_STATUS.md`
  (`YES`).
- REACHABILITY is import-based and module-level: a module is `LIVE` if any symbol is imported on a
  live chain. Workers confirm reach for the specific symbol from the actual entry point (some LIVE
  modules, e.g. retired Pipeline/Workbench/Portal presentation, are never rendered).
