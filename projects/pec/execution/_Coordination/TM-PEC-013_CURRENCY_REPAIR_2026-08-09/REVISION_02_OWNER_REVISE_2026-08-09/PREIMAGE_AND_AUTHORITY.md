# TM-PEC-013 revision 02 preimage and authority reproduction

**Owner ruling, verbatim (2026-08-09):**

> REVIEW findings: REVISE all eight. Authorize one bounded WORKING_ITEMS repair
> and PEER_REVIEW rerun confined to the cited SOW/SPEC claims and regenerated
> review evidence; preserve lifecycle, dependencies, source, and all unrelated
> content.

This revision addresses only the six findings routed to DEL-02-07, DEL-03-01,
and DEL-04-01: RF-001 and RF-002 for each deliverable. The two DEL-00-03
findings are outside this WORKING_ITEMS repair.

## SOW preimages

| Deliverable | Review snapshot | Preimage SHA-256 | Finding IDs |
|---|---|---|---|
| DEL-02-07 | `REV_DEL-02-07_2026-08-09_2031` | `d2f898c1bc5b9b3798fe9c5b4961019c9f88366fc36e44c25c51bc878947391f` | RF-001; RF-002 |
| DEL-03-01 | `REV_DEL-03-01_2026-08-09_2040` | `b2569e56927459f93865cbe4642bddbfbee96814aa79ed6b39cb3b3721246f64` | RF-001; RF-002 |
| DEL-04-01 | `REV_DEL-04-01_2026-08-09_2050` | `21e696ce8ccaad88f852f6a91a4bc575c1e46601b5d3e026978a49164f2c9d89` | RF-001; RF-002 |

## Preserved live evidence

| Surface | SHA-256 |
|---|---|
| DEL-02-07 `Dependencies.csv` | `00b5a872ca0a62c9246591d513af11637e3e15dc764824fd28b7d8219f3c3ee3` |
| DEL-03-01 `Dependencies.csv` | `5f68759d07cc001e139fc351e33748ef7f03ba5ba9cd7ed77a6182ad8161bd65` |
| DEL-04-01 `Dependencies.csv` | `2daee4e76382186657c52b01caf5c4435c8d6a501c6d2b305c9b1c9703a916e4` |
| DEL-02-07 `_STATUS.md` | `c26d6861c1f07ee33c8fec6c74d126270d619955da1068c853a4b0132c2a8792` |
| DEL-03-01 `_STATUS.md` | `f8816dcaa48f3ca980f1b6db51129efb5d3a5095d0120fbf4698878e9b9121b5` |
| DEL-04-01 `_STATUS.md` | `7c9902184deeb30b80728979fd76c710a23396ba549c144bc713134e51a94dd1` |
| DEL-10-01 `_STATUS.md` | `3309a68a1180b7fdf40722e5e63cc468a4f76fcf484b98799f700743a63ab5f2` |
| DEL-10-01 `STEP0_COST_BASELINE.md` | `0aa5dd22d397026d88dfd8af1613163dd2de01ef3264024438034e54a1f5d02d` |
| DEL-10-01 `STEP0_COST_BASELINE_METHOD.md` | `5756d6cf1b7293a7db8dcf1ce968d443dcb7214867216f5013ee018a493a0c59` |

PEC reliance-hold preflight returned `ALLOW` for
`dispatch-for-production` on all three deliverables. No SOW repair had been
applied when these hashes were reproduced.
