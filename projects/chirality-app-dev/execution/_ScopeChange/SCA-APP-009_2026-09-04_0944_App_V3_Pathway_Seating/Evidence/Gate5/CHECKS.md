# SCA-APP-009 Gate-5 Checks

**Date:** 2026-09-04
**Basis:** `aa8554542e3d6d09a925f69e1114bea8e18532f8`

| Check | Result |
| --- | --- |
| Basis, clean start, fast-forward ancestry | PASS |
| Authority/pointer preimages and collision scan | PASS |
| Root live-baseline postimage `e747795d...` | PASS |
| Decomposition postimage `e46084ab...` | PASS |
| Companion-register postimage `e47fced6...` | PASS |
| Actual-worktree APP-HOLD dispatch admission | PASS |
| Five-file DEL-09-07 scaffold path/hash/type parity | PASS |
| Normalized candidate and 42-stage topology | PASS |
| Independent combined review `c69aa66f...` | PASS |
| Authority corpus v20 status | PASS |
| App receipt ledger validation | PASS |
| `harness-self-check` | PASS |
| `app-hold-integrity` | PASS |
| `harness-pytest` | PASS |
| Combined `tools/practitioner_harness tools/validation` pytest | PASS |
| Root governance G0/G1/G2/G3/G4 live validators | PASS |
| Candidate whitespace | PASS |
| `git diff --check` | PASS |
| Exact 50 changed pre-pointer paths, including supplemental root pin | PASS |
| SCA-APP-008 tree and recursive identity | PASS |
| Live `_LATEST.md` remains protected preimage | PASS |
| Product/frontend/runtime byte changes | PASS — none |
| Harness premerge product/runtime workflow | SKIPPED — no product, frontend, or runtime byte changed; not selected by the registered path rules |

The full practitioner harness passed with all 350 tests. The combined routed
suite passed with all 670 tests. Existing non-blocking self-check findings are
unchanged and outside this transaction.
