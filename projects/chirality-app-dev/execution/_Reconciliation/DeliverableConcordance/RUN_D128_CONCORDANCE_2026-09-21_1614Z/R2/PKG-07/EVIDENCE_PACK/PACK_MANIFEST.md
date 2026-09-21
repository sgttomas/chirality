# Evidence pack manifest — PKG-07 (R2, wave 3)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-07 WORKING_ITEMS manager under
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Placeholders:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder. Commands run from `<RUN>`.
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv R2/PKG-07/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p R2/_shared/EVIDENCE_PACK/REACHABILITY.csv R2/PKG-07/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 18 | `60345dbf84fb9671b78c618cd9d869f86622841f5dc360d621edc62f5b9c98c7` | `python3 R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-07 --out R2/PKG-07/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 341 | `1cccda49745c6beb477b5e6dd331ac272799bf52f297c1e9a200a42d8f5fa35b` | `python3 R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-07 --out R2/PKG-07/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv R2/PKG-07/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |

## Checks

- Items 1, 2, 5: byte-for-byte copies; `shasum -a 256` of source and copy are identical and equal the
  values in `R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the `DEL-07-*` data rows of each `--package PKG-07` output are byte-identical (`cmp`) to
  the `DEL-07-*` rows of the corpus-wide check in `R2/_shared/ALL_DELIVERABLES_CHECK/`.

## Content notes (for workers)

- **REFERENCE_HASHES:** all 18 rows (6 deliverables × CONTRACT/SPEC/PRD) record `MATCH` and have
  `Match = NO` — no recorded hash reproduces at the frozen basis. Per CONVENTIONS §2.7 this is one
  `REGISTER-n` row per deliverable, cited as `HASH-RECOMPUTE@00115c719`.
- **DECISION_HITS:** 341 rows — DELIVERABLE 332, RULING 5, REGISTER 4. Per deliverable: DEL-07-01 74,
  07-03 74, 07-04 73, 07-05 46, 07-06 40, 07-02 34.
- **D-APP-127_APPLICATION_MAP:** in every PKG-07 deliverable **no carrier** (`_STATUS.md`,
  `ScopeOfWork.md`, `_CONTEXT.md`, `Dependencies.csv`, `_REFERENCES.md`) is `Revised = YES`; all 30 are `NO`.
- **REACHABILITY:** module-level and import-based (see the shared manifest's known limits). A re-export
  or one imported helper marks a whole module LIVE, and some LIVE-tagged modules (for example retired
  Pipeline / Workbench / Portal presentation) are never rendered. Treat it as a starting hint: confirm
  reach **for the specific symbol** from the actual entry point (the rendered page, the executed route
  handler, the packaged runtime-service entry) before tagging `REACH=LIVE`, and say in Notes when your
  reading differs from the map or from a capability file.
