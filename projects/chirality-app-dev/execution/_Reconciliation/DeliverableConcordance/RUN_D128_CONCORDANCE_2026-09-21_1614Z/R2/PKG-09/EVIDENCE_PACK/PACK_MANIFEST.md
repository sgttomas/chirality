# Evidence pack manifest — PKG-09 (R2, wave 5)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-09 WORKING_ITEMS manager under
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Placeholders:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder. Commands run from `<RUN>`.
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv R2/PKG-09/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p R2/_shared/EVIDENCE_PACK/REACHABILITY.csv R2/PKG-09/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 21 | `b99bb2d37efa3163f0700ef9c06db6d87c4515a7f1ebc6785ea6db136d6477df` | `python3 R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-09 --out R2/PKG-09/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 1539 | `ddf7269681f3a4625079572d0313795ea457dca6c9e7b8452c1d0060b68b273a` | `python3 R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-09 --out R2/PKG-09/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv R2/PKG-09/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |

## Checks

- Items 1, 2, 5: byte-for-byte copies; `shasum -a 256` of source and copy are identical and equal the
  values in `R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the data rows of each `--package PKG-09` output are byte-identical (`cmp`) to the
  `DEL-09-*` rows of the corpus-wide check run in `R2/_shared/ALL_DELIVERABLES_CHECK/`.

## Content notes (for workers)

- **REFERENCE_HASHES:** 21 rows (7 deliverables × CONTRACT/SPEC/PRD), all `Match = NO`. DEL-09-01..06
  record `MATCH` for all three documents and none reproduces at the frozen basis — per CONVENTIONS §2.7
  one `REGISTER-n` row per deliverable, cited as `HASH-RECOMPUTE@00115c719`. DEL-09-07 records no
  verdict (`NOT_RECORDED`); check its `_REFERENCES.md` directly.
- **DECISION_HITS:** 1539 rows — DELIVERABLE 1498, RULING 25, REGISTER 16. Per deliverable: DEL-09-01 50,
  09-02 50, 09-03 74, 09-04 170, 09-05 84, 09-06 1088, 09-07 23 (DEL-09-06 is dominated by its
  `Evidence/` and `_run_records/` material; filter by `Path`).
- **D-APP-127_APPLICATION_MAP:** PKG-09 carriers citing D-APP-127/D-GOV-43 with the applied effect are the
  `_STATUS.md` of DEL-09-03, 09-04, 09-05, 09-06 and 09-07 (`YES`); every other PKG-09 carrier (all SoW,
  `_CONTEXT.md`, `Dependencies.csv`, `_REFERENCES.md`, and DEL-09-01/09-02 `_STATUS.md`) is `NO` or `ABSENT`.
- **REACHABILITY:** import-based and module-level, covering `frontend/src/**`, `frontend/electron/**` and
  Runtime `packages/*/src/**`. It does **not** classify build and packaging scripts (`frontend/scripts/**`,
  `electron-builder` config, `package.json` scripts, `.github/workflows/**`): their reach is established
  from the packaging entry (the `package.json` script that the release/packaging command runs) and stated
  in Notes. In-root workflow evidence is `projects/chirality-app-dev/.github/workflows/harness-premerge.yml`;
  the repository-root `.github/workflows/**` is outside the PKG-09 evidence roots and is not read. A re-export or one imported helper marks a whole module LIVE; confirm reach for the specific
  symbol from the actual entry point.
