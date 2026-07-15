# WORKING-P2-PKG05 Preflight Reproduction

Status: `PASS`

Basis: accepted W-P2 preflight and synchronized
`main@eaad463c0d481f6f1654e6adb5ee718f566176e9`.

| Check | Result |
|---|---|
| Exact package population | 5/5 (`DEL-05-01..05`) |
| Frozen physical source lines | 1,292/1,292 |
| Accepted P2 manifest rows | 5/5 reproduced |
| Expected live bindings | 45/45 reproduced |
| Lifecycle | 5/5 `IN_PROGRESS`; zero pilot; zero ISSUED |
| Format | 5/5 exact `LEGACY_FOUR_DOC`; zero live SOW |
| Source/control hash drift | zero |
| Scope-of-Work deterministic tests | 21 passed |
| Candidate/project writes during preflight | zero |

Member totals: `DEL-05-01` 291; `DEL-05-02` 176; `DEL-05-03` 234;
`DEL-05-04` 269; `DEL-05-05` 322. The authoritative row details remain the
accepted `P2_MANIFEST.tsv` and `EXPECTED_LIVE_BINDINGS.tsv`; this reproduction
does not replace that immutable upstream truth.
