# Review dispositions — APPDEV_V3_NODE_M_2026-09-04

## Round 1 over `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c`

Immutable review:
`instances/M2_REVIEWER/REVIEW_NODE_M_R1.md`
(SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4`).

Verdict: **FAIL** — no BLOCKER findings and three MAJOR findings. All three
findings are accepted and remediated in the round-2 candidate.

| Finding | Severity | Disposition | Remediation | Required fresh verification |
|---|---|---|---|---|
| M-R1-F1 | MAJOR | ACCEPTED / REMEDIATED | Removed the false `[click]` explanation and all three markers from A15. The record now states that the owner typed each reply in plain text through the mobile fallback. Every question and the exact answer `Yes, so authorized.` are preserved; ruling substance is unchanged. Receipt 220 carries the same corrected interaction provenance. | Confirm no `[click]` token remains in A15; compare all three questions and answers with the sealed owner-direction brief; confirm no ruling-semantic change. |
| M-R1-F2 | MAJOR | ACCEPTED / REMEDIATED | Retagged DEL-09-05-V3-02 as `NOT_SELECTABLE_UNTIL` owner-installed Syft `v1.18.1` is observable. Preserved A15's prospective authorization, A14's historical validity, the alternative owner re-pin language, and the fact that no host act occurred. The existing 2026-09-04 History line and Receipt 220 now agree with the parked state. | Confirm discovery cannot select V3-02 while Syft is absent and that no unrelated DEL-09-05 item semantics changed. |
| M-R1-F3 | MAJOR | ACCEPTED / REMEDIATED | Filed the round-1 report verbatim under `instances/M2_REVIEWER/`; replaced the false `not_run` posture with an explicit round-1 FAIL record; updated `CHECKS.json`, `RETURN.md`, `HANDOFF_STATE.md`, Receipt 220, and the manifest; added this disposition record and the sealed round-2 handoff. No second receipt was added. | Verify the filed report SHA-256 and byte identity, every closeout pointer and manifest member, the unchanged Receipt 220 cursor/parent, and that the candidate claims only `REVIEW_READY_R2` pending a fresh review. |

No product, `frontend/`, host, Root, lifecycle, Checking Approval SHA,
register, decomposition, SCOPE_CHANGE, or other out-of-scope byte was changed
to disposition these findings.

## Round 2 over `4fa170341700e491dff8c72ce1229ba84735f073`

Immutable review:
`instances/M3_REVIEWER/REVIEW_NODE_M_R2.md`
(SHA-256 `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4`).

Verdict: **FAIL** — no BLOCKER findings and two MAJOR findings. Both findings
are accepted and remediated in the round-3 candidate.

| Finding | Severity | Disposition | Remediation | Required fresh verification |
|---|---|---|---|---|
| M-R2-F1 | MAJOR | ACCEPTED / REMEDIATED | Made DEL-09-06-V3-04's Return and Removed-when clauses nonce-only. The gate and Depends clauses continue to select a per-response nonce with dynamic rendering; hash/SRI is not selected. Middleware versus packaged-handler header attachment and all other exact nonce implementation details remain open. V3-03 and every unrelated item are unchanged. | Confirm that every live V3-04 closure clause is nonce-only, no hash alternative remains, and no exact implementation form is prescribed. Reconfirm the V3-03 byte fence. |
| M-R2-F2 | MAJOR | ACCEPTED / REMEDIATED | Added `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.md`, and launch/status/return records for M1, M2, and M3; filed the R2 report verbatim; and added this disposition plus the sealed R3 handoff. M1's received launch brief remains verbatim. M2 metadata is explicitly a source-calibrated non-verbatim reconstruction. M3 metadata is an accurate structured rendering of the actual dispatch, not a byte-verbatim prompt claim. The immutable review reports govern. No event was invented, and no child pushed, opened a PR, merged, changed product bytes, or performed a host act. | Verify both report byte identities; compare the recorded basis, freezes, worktrees, read/write bounds, verdicts, and hashes with the immutable reports and supervisor evidence; confirm evidence-calibration labels; verify complete manifest membership and closeout pointers. |

The complete round-1 and round-2 history is preserved. No second receipt is
added; Receipt 220 retains its original cursor and parent. Fresh round-3
review remains required before manager fan-in.

## Round 3 over `52998709c5c19bc5c3df3944735593299d60be56`

Immutable review:
`instances/M4_REVIEWER/REVIEW_NODE_M_R3.md`
(SHA-256 `2c5ceb0c930f566b9f375d2f8f8b1f62b9123f55e175a438d37fcf9e160a8802`).

Verdict: **FAIL** — no BLOCKER findings and one MAJOR finding. The finding is
accepted and remediated in the round-4 candidate.

| Finding | Severity | Disposition | Remediation | Required fresh verification |
|---|---|---|---|---|
| M-R3-F1 | MAJOR | ACCEPTED / REMEDIATED | Identified M1–M4 and the planned M5 reviewer as `delegated-harness-native`. Every Agent-2 role statement is now expressly `role not mechanically enforced`, with governed-workflow role evidence `instruction-asserted`. K-SUBAGENT/non-delegation is instruction+config asserted, not mechanism-proven; no descendants were observed. Unbounded `no delegation` and boolean-mechanism implications were removed or qualified in mutable orchestration/child records. M1's contemporaneous sealed launch brief and all three immutable review reports remain byte-unchanged and are governed by adjacent calibration records. | Confirm those exact calibration terms across `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.md`, M1/M2/M3/M4 status and return records, reconstructed reviewer launch records, `CHECKS.json`, top-level `RETURN.md`, `HANDOFF_STATE.md`, Receipt 220, and the round-4 handoff. Verify the sealed M1 brief and all immutable reports remain byte-identical. |

No second receipt is added; Receipt 220 retains its original cursor and
parent. No product, `frontend/`, host, Root, lifecycle, Checking Approval SHA,
register, decomposition, SCOPE_CHANGE, push, PR, or merge act occurred. Fresh
round-4 review remains required before manager fan-in.

## Round 4 over `c3c3b628203ccc949d3ee3b3573a96b45f472278`

Immutable review:
`instances/M5_REVIEWER/REVIEW_NODE_M_R4.md`
(SHA-256 `ceb24881cf877fce9771c2b7dc9c820c8d34aed9d079f42ec6cee0f9392fd47a`).

Verdict: **FAIL** — no BLOCKER findings and one MAJOR finding. The finding is
accepted and remediated in the round-5 candidate.

| Finding | Severity | Disposition | Remediation | Required fresh verification |
|---|---|---|---|---|
| M-R4-F1 | MAJOR | ACCEPTED / REMEDIATED | Advanced M1's live status to `review_ready_r5` with the actual R4 freeze/verdict/hash; made its return enumerate all four filed immutable prior-review reports; filed M5's calibrated launch/status/return and the verbatim R4 report; and changed every mutable current-state pointer to the active `REVIEW_R5_HANDOFF.md`. The sealed R2, R3, and R4 handoffs remain unchanged and are identified only as spent historical dispatch contracts. Receipt 220 remains byte-preserved earlier evidence; append-only corrective Receipt 221 identifies its stale-pointer delta and the current R5 surfaces. Orchestration, work graph, checks, return, handoff, manifest, and Receipt 221 now agree. | Verify M1 status and timeline, all four prior-report identities, M1/top-level report descriptions, M1–M5 child records, Receipt 220 byte preservation, Receipt 221 structure, and that `REVIEW_R5_HANDOFF.md` is the only active next-review pointer. Scan mutable records for stale R3/R4/current-review language and vague `both` report counts. |

The R5 candidate contains the four filed prior reports and the sealed R5
launch/handoff, but it cannot contain the future round-5 verdict/report. If
round 5 passes, its immutable report and final narrative closeout may be
filed after PASS under the standing narrative-only evidence rule without
changing ruling or deliverable bytes. No product, `frontend/`, host, Root,
lifecycle, Checking Approval SHA, register, decomposition, SCOPE_CHANGE,
push, PR, merge, or release act occurred. Fresh round-5 review remains
required before manager fan-in.
