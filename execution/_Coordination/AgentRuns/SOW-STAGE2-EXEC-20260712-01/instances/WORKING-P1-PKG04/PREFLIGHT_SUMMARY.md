# PKG-04 Preflight Reproduction

Binding rows: `54`; mismatches: `0`.
Physical legacy source lines: `1368`; expected `1,368`; verdict: `PASS`.

| Member | Physical lines | Batch |
|---|---:|---:|
| DEL-04-01 | 245 | 1 |
| DEL-04-02 | 199 | 1 |
| DEL-04-03 | 216 | 1 |
| DEL-04-04 | 200 | 1 |
| DEL-04-05 | 232 | 1 |
| DEL-04-06 | 276 | 2 |

Batch 1 is `DEL-04-01..05`, five members and 1,092 lines. Batch 2 is
`DEL-04-06`, one member and 276 lines. This is the minimum consecutive
numeric partition under the five-member/2,053-line limits.

Every source, status, context, reference, dependency-summary, and
dependency-register hash is reproduced row-for-row in
`LIVE_BINDING_REPRODUCTION.tsv`.
