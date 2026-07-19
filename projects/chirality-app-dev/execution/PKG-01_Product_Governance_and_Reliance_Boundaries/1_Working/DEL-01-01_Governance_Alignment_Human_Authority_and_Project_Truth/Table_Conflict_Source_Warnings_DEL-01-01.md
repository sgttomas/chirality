# Conflict / Source-Warning Table — DEL-01-01

## Header

| Field | Value |
|---|---|
| Purpose | Record, for human ruling, the cases where source records disagree or source hashes are unaccepted. Conflicts are surfaced, not resolved (CONTRACT K-CONFLICT-1); no ruling is rendered by this artifact. |
| Authority | D-APP-65 disposition 4 — owner-authorized production tranche unlocking the D-APP-56 R4-P48 documentation deferral. |
| Source requirements | `ScopeOfWork.md` CLM-012 (conflict/source-warning table), CLM-011 historical-warning-handling row; DEL-01-01-REQ-008; CONTRACT K-CONFLICT-1/K-INVENT-1. |
| Date of entries | 2026-07-18 |
| Verdict status | All entries are agent findings, not owner acceptance. Per CONTRACT K-AUTH-1, no approval, certification, sign-off, issuance, or conflict ruling is rendered by this artifact. |
| Author | N6a docs-author child, RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18` |

## Open Conflicts (human ruling needed)

| Conflict ID | Status | Conflict | Source A | Source B | Additional records | Impact | Proposed handling (PROPOSAL — not a ruling) | Human ruling |
|---|---|---|---|---|---|---|---|---|
| DEL-01-01-C002 | OPEN (carried) | Dispatch path used package label `PKG-01_Governance_and_Product_Boundaries`, but the deliverable folder, `_CONTEXT.md`, and SOFTWARE_DECOMP v3.2 use `PKG-01_Product_Governance_and_Reliance_Boundaries`. | TASK dispatch assignment path (historical) | Deliverable folder path; `_CONTEXT.md`; SOFTWARE_DECOMP v3.2 package table | `ScopeOfWork.md` CLM-025 (original entry); D-APP-56 R4-P48 ruling on R002 (stable IDs and live path control for execution) | Run records and identification sections | Continue using stable IDs `PKG-01`/`DEL-01-01` and the live folder path; correct or retire the stale dispatch label if it still exists anywhere. | TBD |
| DEL-01-01-C003 | OPEN (new 2026-07-18) | The source records for REF-006 `docs/PRD.md` hash status disagree. The D-APP-65 T3 launch brief (`.../AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/LAUNCH_BRIEF_DOCS_DEL-01-01_T3.md`, artifact 7 spec) directs that a **live** REF-006 `HASH_MISMATCH` be carried; the historical assessment records a mismatch at its review SHA; the live reference register records `MATCH`. | Launch brief artifact-7 instruction ("MUST carry the live REF-006 `HASH_MISMATCH` on `docs/PRD.md`"); `Assessment_INSP-03_DEL-01-01.md` line 45 (HASH_MISMATCH at Reviewed SHA `e2e9806c...`: expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`) | `_REFERENCES.md` line 12: REF-006 Expected = Actual = `d95d826a10b2ddf3ff375d0dc60c03d98580c0129f7cdcb4433ae29b06220808`, Status `MATCH` (D-APP-38 corpus reconciliation, per `ScopeOfWork.md` CLM-003/CLM-010/CLM-026 R001) | FACT (live check, 2026-07-18): read-only SHA-256 of `docs/PRD.md` computed by this run = `d95d826a10b2ddf3ff375d0dc60c03d98580c0129f7cdcb4433ae29b06220808`, equal to the `_REFERENCES.md` expected value. This observation is recorded as evidence for the ruling; it does not itself close the conflict. | Until ruled, PRD-cited verdicts in this artifact set are treated as source-warning-limited, and no issue-readiness reliance is claimed on REF-006 (CLM-011 reference-integrity row). | Human to rule which record posture controls for REF-006: (a) the `_REFERENCES.md` MATCH under the D-APP-38 corpus snapshot, or (b) the brief's live-mismatch characterization; and whether the historical INSP-03 mismatch needs any further annotation. Resolution was explicitly out of scope for this tranche and none is rendered here. | TBD |

## Source Warnings (visible; no ruling strictly required)

| Warning ID | Status | Warning | Records | Handling |
|---|---|---|---|---|
| DEL-01-01-W-01 | OPEN | Stale kit prose: `ScopeOfWork.md` CLM-008, CLM-016 step 1, and CLM-022 still instruct keeping `ResponsibleParty=TBD`, while CLM-002, CLM-015, CLM-026 R003, `_CONTEXT.md`, and `_STATUS.md` (2026-07-18 History) record the D-APP-65 assignment to Ryan Tufts (K-AUTH-1, demonstrator scope). | `ScopeOfWork.md`; `_CONTEXT.md`; `_STATUS.md` | Later dated records control; quoted historical text left byte-intact by this tranche. A future kit reconciliation may align the prose. |
| DEL-01-01-W-02 | NOTED | The decomposition DEL-01-01 row (line 280) anticipates five artifacts; `ScopeOfWork.md` CLM-012 requires seven (adds the runtime-audit checklist and this table). | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` line 280; `ScopeOfWork.md` CLM-012 | Anticipated-artifact fields are non-exhaustive planning fields; the accepted SOW governs. No ruling requested. |

## Closed Historical Conflicts

| Conflict ID | Status | Record |
|---|---|---|
| DEL-01-01-C001 | CLOSED | Historical REF-006 PRD hash warning superseded by the D-APP-38 corpus snapshot per `ScopeOfWork.md` CLM-025 closing note and CLM-026 R001. Retained as history; note that its subject matter re-surfaces as the record-level disagreement now carried OPEN as C003 above. |

## Summary

- 2 OPEN conflicts for human ruling (C002 carried; C003 new — the REF-006
  record disagreement, carried unresolved per the launch brief).
- 2 source warnings (W-01 stale kit prose; W-02 artifact-count note).
- 1 closed historical conflict retained for traceability.
