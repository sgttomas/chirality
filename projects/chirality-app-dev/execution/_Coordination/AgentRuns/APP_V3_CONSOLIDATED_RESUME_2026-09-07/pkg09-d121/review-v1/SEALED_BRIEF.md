# Sealed brief — independent D121 three-carrier application review

RequestedBy: HELP_HUMAN through PKG09 WORKING_ITEMS

RunID: `APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg09-d121`

ParentInstanceID: `/root/app_pkg09`

ChildInstanceID: assigned by delegated harness

Role: ephemeral Agent 2 independent reviewer; role and nondelegation are instruction-asserted

Model: `gpt-5.6-sol`

Reasoning: `medium`

Objective: independently validate 100% of the resulting D121 three-carrier application against the accepted patch and retained pre/post identities. Return `PASS` only if the live carrier union exactly equals the accepted three-carrier postimage, the DEL-09-06 contract remains valid, and no collateral carrier change or authority overclaim exists.

AcceptedBasis:

- D121 ruling on observable `origin/main` `9428e4af44c91063f2188e31698e4c84d8549be9`, ruling SHA-256 `fa410ae195c74fab2ad3de7cb5d64e244a327905ea3d1f76849f6b51fb74caeb`.
- Design SHA-256 `c42f617eafd3cce21047d4cf5977fd058207ef55fd8b090b337b2422f62bc687`.
- Accepted patch SHA-256 `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32`.
- Correct pre/post identities in `../PREFLIGHT_AND_IDENTITIES_v2.json`; v1 is failed and prohibited.
- PKG02 application evidence under sibling path `../pkg02-cross-root/d121-carrier/` when available; PKG09 application evidence and live diff.
- Fresh reviewer-dispatch APP-HOLD: `ALLOW` for DEL-02-03 and DEL-09-06, register `c08a2948…cafc`, scan `b30a5461…f437`.

DeclaredReads: Root `AGENTS.md`; App `AGENTS.md` and loop entry; D121 ruling/design/accepted patch/application packet; all three live carriers and their Git diff; v1 failure notice and v2 identity/application records; PKG02 carrier evidence; SOW validation tools.

AllowedTools: read-only shell, SHA-256, `cmp`, `git diff`, `git apply --reverse --check`, configured Python `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python`, SOW validator and checklist derivation.

AllowedWriteTargets: exactly this `review-v1/` directory: `RETURN.md`, `CHECKS.json`, and `MANIFEST.json`.

EXCLUSIONS: no edits to carriers, MEMORY, run records, receipts, coordination outside this review directory, frontend/source/tests/build/processes, credentials, provider, protected fixture, supplier, Git state, lifecycle, publication, or release. Do not delegate.

AcceptanceCriteria:

1. Compute full hashes directly from bytes; do not manually infer or abbreviate identities in machine records.
2. Verify all three live hashes equal the corrected accepted postimages and byte-compare to retained postimage files.
3. Verify `git apply -p0 --reverse --check ACCEPTED.patch` succeeds over the complete carrier union and the carrier diff contains exactly the accepted `+12/-3` hunks.
4. Validate live DEL-09-06 as `SOW_V1` and derive exactly `DEL-09-06-AC-001` with `DEL-09-06-VER-001`.
5. Confirm lifecycle remains `IN_PROGRESS`, Checking Approval SHA remains `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, D121 source/proof remains held, and `inlinePdfPreview` has not been changed by this carrier tranche.
6. Confirm write containment and v1 failure/supersession are explicit.

Return contract: verdict, full identities, check results, findings, limitations and rerun triggers. A finding returns to the manager without repair. PASS validates the carrier application only; it does not activate source, prove native PDF capability, close lifecycle, or authorize release.
