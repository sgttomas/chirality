# Author Checks — DEL-08-05

| Check | Evidence | Verdict |
|---|---|---|
| Exact accepted row | A3 manifest row binds APP / PKG-08 / WORKING-A3-PKG08 / DEL-08-05, live path, 9 frozen hashes, 10 dependency rows, SOW-063, OBJ-003 and OBJ-007, decomposition basis, candidate/evidence paths, and replacement delta | PASS |
| Live format/lifecycle | Exactly four legacy production files, no live `ScopeOfWork.md`, `_STATUS.md` states `IN_PROGRESS`, and the row declares non-ISSUED | PASS |
| Seed exactness | `SOURCE_HASHES.tsv` and `SEED_TRACE.tsv`: 9/9 hashes and byte counts match the accepted row/live files | PASS |
| Conversion authority | Exact `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`; isolated conversion; package PKG-08 | PASS |
| Schema/format | Duplicate validator reports `MIGRATION_DUAL`, valid=true, zero issues | PASS |
| Marker closure | 35 begin markers, 35 end markers, and 35 claim-map data rows | PASS |
| Line/hash/target binding | Parity checks 35/35 with no issues; claim map binds every marker to source file/range/hash, defined target ID, and target SHA `8a1f1214aebf3d7c8b1a4dfb4fad71b0142e311e663573b6d60a21d0d8ca2167` | PASS |
| Content authority | Only OUT-001, AC-001, and VER-001 were authored; each is bounded to DEL-08-05 identity, SOW-063, OBJ-003/OBJ-007, and preserved legacy statements | PASS |
| Matrix closure | OUT-001 → CLM-010 → AC-001 → VER-001 with SOW-063, OBJ-003, OBJ-007 | PASS |
| Checklist | One AC exactly once in source order; exact text, qualified ID, candidate hash, line/section, OUT-001, and VER-001 binding; duplicate runs byte-identical | PASS |
| Rendering | Duplicate HTML byte-identical at SHA-256 `ac0585daf21e066d799e161be837056b47e4ae5f3a4d5573ec69b3927c83a6d7`; no script or external-resource reference | PASS |
| Negative fixtures | Partial and wrong-authority dual validation fail; invalid/unauthorized checklist and render fail without output artifacts | PASS |
| Candidate exactness | Workspace and authorized candidate copies are byte-identical at SHA-256 `8a1f1214aebf3d7c8b1a4dfb4fad71b0142e311e663573b6d60a21d0d8ca2167` | PASS |
| Lifecycle preservation | Live and workspace `_STATUS.md` remain SHA-256 `2bfcbeb181ef5278f71bfee665061de199b3db9a7d367900d646a5b80b2989e1` | PASS |
| Portability | Authored evidence uses repository-relative paths; immutable source literals separately inventoried | PASS |

Overall author verdict: **PASS**.
