# Brief — D1: release, owner check, lifecycle and done-declaration packets (RUN_D128, R4)

Follow `<RUN>/R4/BRIEFS/D_COMMON_DRAFTER.md` in full. Your packets (fact sheets in
`<RUN>/R4/_work/FACTS/`):

| Packet | Cluster | Notes |
|---|---|---|
| P-01 | CL-01 owner-deferred DEL-06-02 keys | Present **both workers' verdicts side by side** for `DEL-06-02#CLM-005` and `#CLM-032`: worker A = ledger of record `R2/PKG-06/DEL-06-02_A`, worker B = `R2/PKG-06/DEL-06-02_B` (Disposition, CauseTag, HDN, one-line reasoning each, from their ledgers and notes), plus the surrounding claim text at the frozen tree and the code both relied on. RUN_BASIS Addendum 5: the owner deferred these to decide after reviewing context. Options are the two readings (and any third reading the evidence supports). |
| P-02 | CL-02 owner check | A **short** packet on what remains `UNKNOWN` after the owner check. Read `<RUN>/R3/OWNER_CHECK.md`, `<RUN>/R3/OWNER_CHECK_APPLIED.md` and Addendum 13. Say plainly which rows the owner's testimony decided, which stay UNKNOWN (with the owner's belief noted) and what that means for repair (e.g. deliverable text that requires a *kept record* still lacks one). Include a **two-line plain explanation of "attestation" and "SBOM"** (the owner did not recognise the terms): a build attestation is a signed, machine-checkable statement of how and from what a release file was built; an SBOM (software bill of materials) is a published list of every component and version inside the release. Include the "Noted rows for R4 attention" from OWNER_CHECK_APPLIED.md. Note that the OC-20 conversion-wave records sit in Root `execution/`, outside this run's evidence roots. |
| P-03 | CL-03 release signing posture and G6a | `R3/RUNWIDE_CALLS.md` call (f). Include the restored-R4 AUTHORITY_CONFLICT rows `DEL-09-04#CLM-022` and `#CLM-023.3` (verifiers read them as needing no owner decision; R3 kept the Disposition and restored `R4`), with the spot-check's two readings of `#CLM-022` (S2-031). |
| P-23 | CL-23 open lifecycle gates and v3 release scope | Normal open human gates and release-scope rows. No lifecycle transition may come from R4/R5. |
| P-24 | CL-24 done-declaration Q-01..Q-13 | 0 PRIMARY rows; 34 CONTEXT members. The questions are **CONTEXT** (D-APP-129 ruling B; `<RUN>/R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md`). **List Q-01..Q-13**, each with the question in plain words and the evidence R2 and R3 found (keys and paths), **for the owner to address as the owner chooses**. The Options section offers ways to address them (confirm the declaration, amend it, leave it as CONTEXT, or take questions up in later packets); recommendation stays a draft. |
| P-EX | CL-EX exceptions | File `P-EX_exceptions.md`. Three EXT rows; each gets its own short question. |

Read `<RUN>/R3/OWNER_CHECK_APPLIED.md` before P-02 and P-03 (the owner-check application is
complete when you start).
