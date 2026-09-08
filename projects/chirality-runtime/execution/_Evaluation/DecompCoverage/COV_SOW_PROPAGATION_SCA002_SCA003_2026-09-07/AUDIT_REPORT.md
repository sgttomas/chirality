# Independent Runtime SOW Propagation Poststate Audit

Verdict: `PASS`

This independent, nondelegating `AUDIT_DECOMP` run audited the exact Runtime SOW propagation poststate on Git basis `35249accf139f52478d029458946e50ed25ee5dc`. A PASS is derivative closure evidence for the separate owner poststate confirmation; it does not accept Gate 5.

## Binding identities

- Owner decision subject: `360fd1ac7378072f972daf2fe4da237e1ac1903dcc20bda3a2760eb35162319a`.
- Approved Runtime patch: `dac1cd0868325fa0a074922da50acefd6900a53be530ddd00cc879bd5bfad482`.
- DEL-02-06 live postimage: `2e66ee8681800307f5675db63c9870413bb6148bc5cace8e3423ac89b4eeaefe` (55,622 bytes).
- DEL-02-09 live postimage: `0d154c0067da5a9152c46497bead5cd16cfe3fc524a0bc0648c103b32822fd3e` (15,980 bytes).
- Addendum manifest: `efb4011fa2a777d096ec15d50964234a8aef218a3bed1971c5a817d21a7dc6d0`; all 9 declared members independently rehashed to their recorded SHA-256 and byte counts.
- Runtime pointer: `ee7afdbdc4e9654795922dab4d1d938e1bdadfb64fa9f871a68b71853169afea`.
- Application evidence manifest: `9b60f6a40f4b1bae58c28821a60dbca3c0ceda57cdb0b166c0b4bab32ba25b1c`; all 3 declared members independently rehashed to their recorded SHA-256 and byte counts.

## Checks

1. **Exact preimage and postimage — PASS.** Git `HEAD` yields DEL-02-06 preimage `e87e567f7be38e6a98a2c15ee44dd7f5c2e7ebdf72628155ea18a62e539aaa54` and DEL-02-09 preimage `5e46d0a1538618d69b4e9ae6368b5a71dc96aeb4bc4d2d9c46a6d0b23cbcc46e`. The live files equal the reviewed postimage identities above. The scoped live diff passes `git apply --check --reverse --whitespace=error-all`, proving exact reverse applicability to those main preimages. The approved patch identity is independently bound by the owner grant, application journal, bindings, and prewrite evidence.
2. **Runtime write set — PASS.** The tracked Runtime diff contains exactly DEL-02-06 `ScopeOfWork.md`, DEL-02-09 `ScopeOfWork.md`, and `_ScopeChange/_LATEST.md`; the only Runtime untracked application state is the immutable propagation addendum plus coordination evidence. No source or other canonical deliverable is changed. App project modifications are separately authorized sibling state and excluded from this Runtime verdict.
3. **SOW structure and whitespace — PASS.** `validate_scope_of_work.py --json` reports `SOW_V1`, `valid: true`, and zero issues for both SOWs. Scoped `git diff --check` and reverse application with `--whitespace=error-all` pass.
4. **Clause boundary — PASS.** The main-to-live diff changes only DEL-02-06 `CLM-003` and `REQ-010`, and DEL-02-09 `REQ-001` and `REQ-002`.
5. **Authority attribution — PASS.** DEL-02-06 attributes the narrow account-only authority to D-GOV-36 alone and states that D-GOV-39 only recognizes the exact owning-accepted, accepted-published Runtime successor without admitting or expanding the exception. DEL-02-09 preserves the D-GOV-36 custody/authentication basis and assigns D-GOV-39 only the narrow recognition role.
6. **Runtime and project boundaries — PASS.** Both SOWs preserve project authorization and prerequisites. Account-only operations require accepted caller and operation authority, active `HOST-P1`, current account/supplier generations, and compatible `ACCOUNT-WIRE-V1`/`POLICY-R1` capability/version results. Runtime retains supplier identity and readiness ownership; no client obtains runtime credential or supervisor custody.
7. **Atomic identity and fail-closed semantics — PASS.** Both SOWs require one atomic current supplier snapshot carrying the stable opaque nonsecret account/user identifier and provider-selected-workspace identity. Partial, stale, absent, errored, mismatched, or unqualified identity keeps `binding:{state:"unavailable",reason:"canonical-identity-producer-unavailable"}` and `hostedReady:false`; fallback, mixed-version claims, project/no-folder execution, credential exposure, and private-supervisor access remain prohibited.
8. **Conservation — PASS.** `RUNTIME_SCOPE_LEDGER.csv` contains exactly one `SOW-104` row, seven carrier IDs, and objectives `OBJ-001`, `OBJ-002`, `OBJ-004`, `OBJ-007`. The seven carrier SOWs contain 66 unique qualified requirements in aggregate (52 + 8 + 0 + 6 + 0 + 0 + 0). The postimages preserve nine held bindings plus the separately disposed R16-B marker, historical basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, and compatibility identity `root-runtime-1` epoch 1.
9. **Historical snapshot immutability — PASS.** SCA-002 manifest SHA-256 remains `8865716ba1fb55188658ae39ae9cef06ef17290b0801552621e93faee76aeda3`; all 13 members match. SCA-003 manifest SHA-256 remains `ce84376323a5d213c8a6dadcbf47534ecba407a9128543250f55e4b13eaaaa48`; all 16 members match.
10. **Active semantic snapshot — PASS.** `_ScopeChange/_LATEST.md` still names `SCA-003_2026-09-07_1616/` as the latest semantic snapshot and explicitly describes the new addendum as propagation state with independent audit and owner confirmation pending.
11. **Manifest integrity — PASS.** All nine addendum members and all three application-evidence members match their recorded hashes and sizes; the two manifest hashes match the sealed brief.
12. **No-effect boundary — PASS.** The audited poststate makes no source, supplier/account operation, credential, implementation, dependency, estimate, schedule, lifecycle, hold, fixture, hosted-readiness, release, publication, or concordance change. App sibling modifications are authorized excluded state. The addendum and pointer truthfully leave independent owner confirmation and cross-project concordance pending.

No blocker, warning, or informational discrepancy was found in the sealed scope.
