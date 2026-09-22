# Evidence pack manifest — PKG-04 (R2, wave 1)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-04 WORKING_ITEMS manager under
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Placeholders:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder.
- Rows exclude the header and the final `#END` record (present in every file).

| # | File | Rows | SHA-256 | Method |
|---|---|---|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp <RUN>/R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv .` — byte-for-byte; SHA-256 matches `_shared/EVIDENCE_PACK/PACK_MANIFEST.md` |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp <RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv .` — byte-for-byte; SHA-256 matches |
| 3 | `REFERENCE_HASHES.csv` | 15 | `dd6f38930564492621b1939ebb20183031f02aa2d582d3a3f394e879152abd48` | `python3 <RUN>/R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-04 --out <RUN>/R2/PKG-04/EVIDENCE_PACK/REFERENCE_HASHES.csv` (script SHA-256 `9a2af186dfc9b8ed4f71ba1e94c8e0990cb5ae329031072c640a17e3bdc7c30c`) |
| 4 | `DECISION_HITS.csv` | 474 | `89cf77099eb1895aec035e90fd7aee78d0838791937d44a1aa4495867a4f9aed` | `python3 <RUN>/R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-04 --out <RUN>/R2/PKG-04/EVIDENCE_PACK/DECISION_HITS.csv` (script SHA-256 `0c452b6da528c1a8613d1ce078d8d015539719f177c902a349c96d85cf06bbfb`) |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp <RUN>/R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv .` — byte-for-byte; SHA-256 matches |

## Checks

- Items 1, 2, 5: `shasum -a 256` of the copy equals the shared file and the shared manifest value.
- Items 3, 4: the `DEL-04-*` rows equal the `DEL-04-*` rows of `<RUN>/R2/_shared/ALL_DELIVERABLES_CHECK/`
  (`diff`, no differences).

## Package observations (mechanical)

- `REFERENCE_HASHES`: all 5 deliverables record CONTRACT, SPEC and PRD with verdict `MATCH`; none of the
  15 reproduces at the frozen basis (`Match = NO` for all 15).
- `DECISION_HITS`: DELIVERABLE 463 (DEL-04-01 246, 04-05 80, 04-02 60, 04-04 55, 04-03 22); REGISTER 5;
  RULING 6.
- `D-APP-127_APPLICATION_MAP`: no PKG-04 carrier cites D-APP-127 or D-GOV-43 (see the shared manifest).
