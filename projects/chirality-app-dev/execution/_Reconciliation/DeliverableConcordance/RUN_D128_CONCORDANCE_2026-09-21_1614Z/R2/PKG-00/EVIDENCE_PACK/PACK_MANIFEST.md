# Evidence pack manifest — PKG-00 (R2)

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`; built by the PKG-00 WORKING_ITEMS manager per
  `BRIEFS/R2_PACKAGE_MANAGER.md` step 2 and `CONVENTIONS.md` §9.
- **Basis:** frozen reading tree at `00115c71931bcae79909602d653740d3bb72dfa1` (`<FROZEN_TREE>`);
  `git -C <FROZEN_TREE> rev-parse HEAD` confirmed the SHA before the build.
- **Package deliverables:** DEL-00-01, DEL-00-02. Preflight `ALLOW` for both (`../PREFLIGHT/`).
- Rows exclude the header and the `#END` record.

| # | File | Rows | SHA-256 | Method |
|---|---|---|---|---|
| 1 | `TOUCHED_PATHS.csv` | 69 | `18f595da378395cad97bb77cbf9c2c7f0380a972044e03c6218d87c841b23ddc` | Byte copy of `<RUN>/R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv`; SHA-256 equals the shared manifest value |
| 2 | `REACHABILITY.csv` | 348 | `42726d9cd708e4b45e126171dec6f99b5165964ff4b8796dc40b346e8994e40c` | Byte copy of the shared file; SHA-256 equals the shared manifest value |
| 3 | `REFERENCE_HASHES.csv` | 6 | `51d58489ead5942e2d34143611d2ee61eaa20d6631a0a0e308272ec80d1f535e` | `python3 <RUN>/R2/_scripts/reference_hashes.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-00 --out <RUN>/R2/PKG-00/EVIDENCE_PACK/REFERENCE_HASHES.csv` |
| 4 | `DECISION_HITS.csv` | 69 | `3b857b32401668a1bcd7015795d4044f14bf4b06525797369e97a04a99e71b6a` | `python3 <RUN>/R2/_scripts/decision_hits.py --frozen <FROZEN_TREE> --inventory <RUN>/R1_INVENTORY/DELIVERABLE_INVENTORY.csv --package PKG-00 --out <RUN>/R2/PKG-00/EVIDENCE_PACK/DECISION_HITS.csv` |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | 270 | `bfd808e713f4d0a272e20e5f2783c2a5dbd61ba831810a86509cee6908b94dec` | Byte copy of the shared file; SHA-256 equals the shared manifest value |

**Cross-check.** The `DEL-00-*` rows of items 3 and 4 equal the `DEL-00-*` rows of
`<RUN>/R2/_shared/ALL_DELIVERABLES_CHECK/` (verified by `diff`).

**Observations for workers (evidence, not dispositions).**
- Item 3: neither deliverable's `_REFERENCES.md` records a CONTRACT, SPEC or PRD hash
  (`NOT_RECORDED` for all 6 rows), so no MATCH-hash REGISTER rows arise from item 3.
- Item 4: no `D-APP-127` or `D-GOV-43` hit in either deliverable; the most frequent hits are
  D-APP-56, D-APP-65 (DEL-00-02), D-APP-55, D-APP-68, D-APP-19, D-APP-54; register/ruling hits
  D-APP-55, D-APP-79, D-APP-80.
- Item 5: every carrier of both deliverables is `NO` for D-APP-127/D-GOV-43 application;
  `Dependencies.csv` is `ABSENT` (both use `_DEPENDENCIES.md`).
