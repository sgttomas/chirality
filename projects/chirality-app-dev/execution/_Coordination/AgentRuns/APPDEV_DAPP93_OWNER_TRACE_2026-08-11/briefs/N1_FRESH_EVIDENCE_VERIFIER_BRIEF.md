# Sealed brief — D-APP-93 owner trace evidence verifier

- RequestedBy: `WORKING_ITEMS-DAPP93-OWNER-TRACE-20260811`
- RunID: `APPDEV_DAPP93_OWNER_TRACE_2026-08-11`
- ParentInstanceID: `WORKING_ITEMS-DAPP93-OWNER-TRACE-20260811`
- ChildInstanceID: `A2-DAPP93-OWNER-TRACE-VERIFY-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- Objective: independently verify the copied evidence/record identities, the facts-only execution record, exact required cleanup paragraph, and scoped DEL-09-04 coordination updates; return PASS or BLOCK without repair.
- AcceptedBasis: owner direction carried in this activation; branch base `f1e311fb7ab1c2a0800b1d32c59445368428dee9`; immutable imported identity manifest.
- Dependencies: M0 exact-copy PASS and M1 authoring complete.
- EXCLUSIONS: no evidence or source-record edits; no packet/product/runtime/source/foreign-loop/decision-register/receipt/Git writes; no lifecycle, closure, acceptance, remedy, or disposition act; no delegation.
- DeclaredReads: this run root; DEL-09-04 `_STATUS.md`, `MEMORY.md`, and `_run_records/R7_DAPP93_OWNER_TRACE_EVIDENCE_2026-08-11.md`; external source copies only as needed to re-hash against the manifest.
- AllowedTools: read-only shell commands (`shasum`, `wc`, `rg`, `sed`, `git diff`, `git status`) and one `apply_patch` creating only the return.
- AllowedWriteTargets: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_OWNER_TRACE_2026-08-11/returns/N1_VERIFIER_RETURN.md`.
- ExpectedOutputs: written terminal return with coverage, exact identity table/result, facts/claim checks, verbatim-paragraph result, containment check, limitations, and `PASS_DAPP93_OWNER_TRACE_EVIDENCE` or concrete BLOCK.
- AcceptanceCriteria: 11/11 imported hashes exact; matching helper snapshots treated expected; required headline facts supported; exact seven-line paragraph byte-for-byte within execution record; LLDB `PASS=false` scope limit explicit; 12/12 rebuild basis attributed without reinterpretation; DEL-09-04 remains IN_PROGRESS and Checking Approval SHA unchanged; evidence disposition reserved to owner; changed paths contained.
- Escalation: any mismatch or unsupported/disposition-shaped statement returns BLOCK. Do not repair.
