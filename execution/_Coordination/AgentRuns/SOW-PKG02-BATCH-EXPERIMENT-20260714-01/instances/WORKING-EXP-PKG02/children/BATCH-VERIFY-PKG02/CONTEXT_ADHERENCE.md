# BATCH-VERIFY-PKG02 Context Adherence

Verdict: `PASS_WITH_RETAINED_EXECUTION_SUBSTRATE_FINDINGS`

The verifier processed `DEL-02-01` through `DEL-02-05` strictly in numeric
order and closed each successful member before beginning the next. Every
member independently re-read its frozen row, rehashed nine live inputs and
three accepted candidates before and after, copied two fresh disjoint source
kits, reproduced the evidence candidate twice, finalized it twice, and ran
the complete clean-bound verification and seven-negative matrix. No prior
member's path, refs, seed, hashes, candidate, or workspace were reused.

Native token count and context-window occupancy were not exposed by the
runtime and are not inferred from artifact volume. Observable proxies show no
late-position degradation:

| Position | Member | Mappings | Source lines | Negatives | Successful-pass duration (s) | Drift / contamination |
|---:|---|---:|---:|---:|---:|---|
| 1 | `DEL-02-01` | 35 | 427 | 7 | 0.873656 | none |
| 2 | `DEL-02-02` | 48 | 419 | 7 | 1.020579 | none |
| 3 | `DEL-02-03` | 29 | 383 | 7 | 1.010715 | none |
| 4 | `DEL-02-04` | 33 | 369 | 7 | 1.043070 | none |
| 5 | `DEL-02-05` | 41 | 455 | 7 | 1.014397 | none |

The final member has the largest source-line total and retains the same dual
reproduction, dual finalization, validation, map/parity, checklist/render,
semantic review, post-hash, and seven-negative evidence shape as every earlier
member. There is no observable omission, truncation, instruction loss,
cross-member contamination, task drift, or late-member abbreviation.

Three verifier-local harness assumptions failed during `DEL-02-01` and caused
three full restarts from its frozen row. They are preserved under
`retained_attempts/` and classified in `RETRY_001.md`: claim-map CSV column
names, checklist hash location, and the parity tool's intentional failed-report
emission. None touched a candidate or project file, weakened a gate, or
affected later members. The successful final pass had zero additional failure
or retry from positions 2 through 5.

