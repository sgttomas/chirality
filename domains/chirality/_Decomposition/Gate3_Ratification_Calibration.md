# Gate 3 Dense Ratification Calibration Note

Generated: 2026-06-15T02:19:06Z

This note records the Gate 3 dense-ratification basis after category boundary refinement. It is not a Gate 3 acceptance record.

The default cosine threshold remains `0.75`. Under that threshold every Category remains blocking because query-to-atom cosine scores for this corpus/model sit well below `0.75` even after scope refinement. The threshold therefore behaves as an uncalibrated diagnostic, not as a usable pass/fail floor for this source_v2 index.

Gate 3 can close only after the human explicitly accepts a calibrated dense-ratification basis or directs further refinement. No atom text was split or edited in this refinement.

| CategoryID | Mapped IN | Dense recall | Cosine p05 | Cosine median | Cosine max | Default verdict |
|---|---:|---:|---:|---:|---:|---|
| `CAT-001` | 2182 | 0.6132 | 0.4296 | 0.5344 | 0.7360 | SCOPE_REFINEMENT_NEEDED |
| `CAT-002` | 1110 | 0.3459 | 0.4365 | 0.5384 | 0.8260 | SCOPE_REFINEMENT_NEEDED |
| `CAT-003` | 2281 | 0.5085 | 0.4304 | 0.5385 | 0.7567 | SCOPE_REFINEMENT_NEEDED |
| `CAT-004` | 2635 | 0.4205 | 0.4231 | 0.5192 | 0.7563 | SCOPE_REFINEMENT_NEEDED |
| `CAT-005` | 149 | 0.3691 | 0.4912 | 0.6198 | 0.7285 | SCOPE_REFINEMENT_NEEDED |
| `CAT-006` | 2567 | 0.5793 | 0.4384 | 0.5333 | 0.7320 | SCOPE_REFINEMENT_NEEDED |
| `CAT-007` | 2118 | 0.4320 | 0.4608 | 0.5754 | 0.7693 | SCOPE_REFINEMENT_NEEDED |
| `CAT-008` | 3319 | 0.5673 | 0.4307 | 0.5255 | 0.7788 | SCOPE_REFINEMENT_NEEDED |
| `CAT-009` | 1691 | 0.3897 | 0.4174 | 0.5255 | 0.6941 | SCOPE_REFINEMENT_NEEDED |
| `CAT-010` | 1316 | 0.5228 | 0.4521 | 0.5667 | 0.7973 | SCOPE_REFINEMENT_NEEDED |
| `CAT-011` | 35 | 0.1429 | 0.4046 | 0.4799 | 0.7405 | SCOPE_REFINEMENT_NEEDED |

Proposed calibrated basis for human review:

- Treat dense cosine as corpus-relative evidence over `LEDGER_ATOM` chunks, not as a universal absolute semantic-similarity threshold.
- Keep the 11-category flat partition and primary-function boundary rules as the controlling semantic decision surface.
- Use BM25/dense recall and cosine distribution outliers to guide spot review, while requiring explicit human acceptance before replacing the default `0.75` closure threshold.
