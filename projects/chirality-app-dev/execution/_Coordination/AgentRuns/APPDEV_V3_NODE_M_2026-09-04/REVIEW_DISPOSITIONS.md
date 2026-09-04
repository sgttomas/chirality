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
