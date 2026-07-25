# Latest Scope Change

| Field | Value |
|---|---|
| AmendmentID | `SCA-002` |
| Snapshot | `execution/_ScopeChange/SCA-002_2026-07-25_1042/` |
| Variant | `SOFTWARE` |
| Status | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** |
| CurrentGate | Gate 5 — Confirmed / Closed |
| AcceptedBasis | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.2 (`current_basis`) |
| Authority | `D-PEC-64` (+ §4.3 owner amendments #1 and #2; propagation-plan amendment v2.1) |
| DecompositionTruthState | `COMPLETE` — Gate-3-approved exact text applied and validated |
| DerivativePackageState | `COMPLETE` — **scoped to decomposition-local surfaces**; see the `OI-B` deferral below |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — released to `PROJECT_SETUP`, not executed by SCOPE_CHANGE |
| MetadataAlignmentState | `NOT_REQUIRED` |
| AuditState | **`NON_BLOCKING_PASS`** — final pass `COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257`, 0 blockers / 0 warnings |
| ReadyForNextPhase | `REGEN_ONLY` |
| ClosureVerdict | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** |

**Gate state: Gates 1–5 are owner-ruled.** Gate 5 confirmation received
**2026-07-25**; the owner selected verbatim:

> "Accept revision 1.2 (Recommended)" — "Revision 1.2 becomes current_basis;
> SCA-002 closes CLOSED_FOR_SCOPE_CHANGE_ONLY with frozen downstream
> obligations; PROJECT_SETUP resumes for the closure commit and the D-PEC-63
> re-pins. The three disclosures (two-pass audit, SOW-064 fix, assertion-9
> restatement) are accepted as recorded."

Revision 1.2 is the accepted `current_basis`. **SCA-002 is closed.**

Scope width **O-A wave-minimum**. 20 IN ledger rows and 17 deliverables gained
objective mappings; IN items without objective mapping 31 → 11; deliverables
without objective mapping 26 → 9; all 32 Phase 2.2 wave members now carry a
non-empty `SupportsObjectives` set (wave-unmapped 17 → 0).

`PROJECT_SETUP` is the owning workflow and resumes now per `D-PEC-64` §2.4. The scoped closure commit is `PROJECT_SETUP`'s under §3.6(b);
**SCOPE_CHANGE performed no git operation.** The complete handoff file list is
in `Handoff_State.md` §9.

Deferred obligation: **OI-B** — all 64 deliverable `_REFERENCES.md` still pin
"revision 1.1" (fence-excluded by §3.3).
