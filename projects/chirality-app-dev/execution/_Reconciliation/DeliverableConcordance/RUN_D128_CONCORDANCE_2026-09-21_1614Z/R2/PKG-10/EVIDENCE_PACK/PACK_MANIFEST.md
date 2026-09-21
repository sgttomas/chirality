# Evidence pack manifest — PKG-10 (R2, wave 1)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-10 WORKING_ITEMS manager under
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`).
- **Placeholders:** `<FROZEN_TREE>` = the frozen checkout; `<RUN>` = the run folder. Commands run from `<RUN>`.
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---:|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | `cp -p R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv R2/PKG-10/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | `cp -p R2/_shared/EVIDENCE_PACK/REACHABILITY.csv R2/PKG-10/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 15 | `63a5c1c07dd8f2b4d50491210314069c8d9db83a742f2a79d18d79e4f371eec8` | `python3 R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-10 --out R2/PKG-10/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 470 | `0a431c5b5a0b82c3c771ccbd66a091c48e43362f3fdfce77d9e8b705bb798b0a` | `python3 R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-10 --out R2/PKG-10/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | `cp -p R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv R2/PKG-10/EVIDENCE_PACK/` — SHA-256 equals the shared manifest value |

## Checks

- Items 1, 2, 5: byte-for-byte copies; `shasum -a 256` of source and copy are identical and equal the
  values in `R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md`.
- Items 3, 4: the data rows of each `--package PKG-10` output are identical to the `DEL-10-*` rows of the
  corpus-wide check run in `R2/_shared/ALL_DELIVERABLES_CHECK/` (script comparison, True for both).

## Content notes (for workers)

- **REFERENCE_HASHES:** all 15 rows (5 deliverables × CONTRACT/SPEC/PRD) have `Match = NO` — no recorded
  `_REFERENCES.md` hash reproduces at the frozen basis. Per CONVENTIONS §2.7 this is one `REGISTER-n` row per
  deliverable, cited as `HASH-RECOMPUTE@00115c719`.
- **DECISION_HITS:** 470 rows — DELIVERABLE 460, RULING 7, REGISTER 3. Per deliverable: DEL-10-01 106,
  10-02 56, 10-03 111, 10-04 119, 10-05 78.
- **D-APP-127_APPLICATION_MAP:** no PKG-10 carrier cites D-APP-127 or D-GOV-43 (all 25 rows `NO`).
- **REACHABILITY:** the domain profile contract types live in `projects/chirality-runtime/packages/contracts/src/harness/`
  (LIVE by module map); the domain registry, domain tools, headless preview runner and PEC bridge client sit under
  `frontend/src/lib/harness/**` (check each module's row: several are LEGACY_ONLY). Module-level map, not
  symbol-level; see the shared manifest's known limits.
