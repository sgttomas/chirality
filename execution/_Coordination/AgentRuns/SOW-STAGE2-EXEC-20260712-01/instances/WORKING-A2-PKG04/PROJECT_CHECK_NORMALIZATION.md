# WORKING-A2-PKG04 Generated Evidence Normalization

Disposition: `PASS — EXACT REVERSIBLE GENERATED-EVIDENCE REPAIR`.

Only generated execution evidence was normalized. The captured checkout-root
literal was replaced by `~`; the captured machine temp-root literal was
replaced by `${TMPDIR}`. Candidate, source, control, map, parity, checklist,
render, verdict, and project bytes were not changed.

## Project-check records

| File | Pre SHA-256 / bytes | Substitutions | Post SHA-256 / bytes | Reverse proof |
|---|---|---:|---|---|
| `PROJECT_CHECKS.json` | `e17fa3e0eea8f5a10776803b75f8cdaa0a0eb505228499de07ca66d15294e2c7` / 47,004 | 5 checkout + 2 temp | `3085b985940acec4522c82efa8bbaf45813054eee70f2b0c3407815ed8c96111` / 46,746 | exact prehash |
| `PROJECT_CHECKS_PREMERGE.json` | `be979967c8bb7ddc95ce4331aa6cd3179c754bcb818329d9874338888de25237` / 13,853 | 23 checkout + 4 temp | `86882598985845db4709d1383eec7d4ffe858d62004cef88057c586767ac58e9` / 12,869 | exact prehash |

Both postimages parse as JSON, contain zero checkout/temp-root occurrences,
and reverse in memory to their exact preimage hashes. The first record retains
its five PASS checks and initial frontend-premerge execution-substrate FAIL;
the second retains the server-backed frontend-premerge PASS.

## TASK run records

Exactly 28 checkout-root substitutions were applied across nine generated
TASK run records. Each postimage reverses in memory to its exact prehash, and
its direct child manifest now binds the postimage. VERIFY-DEL-04-02's original
manifest omitted its run-record row; the missing row was added during this
evidence-only binding repair.

| Child | Pre SHA-256 | Post SHA-256 / bytes | Count |
|---|---|---|---:|
| AUTHOR-DEL-04-02 | `6c4a0f810adcefc6bd023a24f9e2cf0f06fad581ad507afdbfe46c5465b7e5ce` | `fccb14d1a8b82810189793bc242b2b041fc2c88ed06f0cfe54e2b083fc5e5311` / 3,945 | 3 |
| AUTHOR-DEL-04-03 | `c0b48b0563a69049fa6df819eac876de39c34f4d5f03a158841459222cedf0fa` | `1635b544ae465cc20fdb396e3b9a67c63f2a4bbc83d44cf47e3c54274f038127` / 4,331 | 3 |
| AUTHOR-DEL-04-04 | `9eda8636c2954497c22ea2c0169ef6df37764dd3f6255438a56fbfbe8889a068` | `02a62d9366099a8e46855df82a973d6adb2da1922649b277929872a16c05f275` / 4,250 | 3 |
| AUTHOR-DEL-04-05 | `07ac3a56b400aa336ad3503c519b59190f330b76c1266169fbf05f0f30e53ebf` | `341f443aa275202fc8769ef70929a98ee59a554b402c6103ccbdbfe7bb794d29` / 4,291 | 3 |
| VERIFY-DEL-04-01 | `6f95d2ea22ee3be0a562e6801ed331aaeeee165b27316e4757ff85637ae95acb` | `aa4af74c2738a569bfabb8b33e505f9eed0908151244b767f05104612c9019bf` / 3,858 | 4 |
| VERIFY-DEL-04-02 | `1be294266e379395fa4777b1bb63b596d2a1e76a55ce220b6b0a3f39aaafcb0d` | `5851cb56dd1eccb7254c2b83895c93370df369b48f16c58e6d218165ada14a4b` / 2,823 | 3 |
| VERIFY-DEL-04-03 | `872670f3c70dbbfad333a4e3872e31bb35891ea73c5003c141d28896416f15fa` | `b73640fc6ef80c0fe005fe6cf2c7c38d773993e18812f618e49b43b535043144` / 2,820 | 3 |
| VERIFY-DEL-04-04 | `05e3b9077889eab9fb1f0df0ffab22129fc3e2efcae03991909d1b8b2711ee37` | `736bb1d4390be69a66bf001fcb70150af850426a63d4ad515397786c009ebc50` / 2,987 | 3 |
| VERIFY-DEL-04-05 | `6334c4f910e8fbbbdb3713ad9500aa0fadf1a2e919b9874e573aa504c5f917cc` | `0a211d5e9ed368f0720973a88e79275e2939fa2625a3c0fa40c3d8c9b8facea3` / 3,627 | 3 |

No normalization changed acceptance semantics. The exact immutable source and
control literals intentionally left unchanged are separately inventoried.
