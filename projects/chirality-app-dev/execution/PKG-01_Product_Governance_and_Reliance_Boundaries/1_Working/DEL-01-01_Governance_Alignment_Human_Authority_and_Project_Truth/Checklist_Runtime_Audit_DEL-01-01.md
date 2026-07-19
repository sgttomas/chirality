# Runtime-Audit Boundary Checklist — DEL-01-01

## Header

| Field | Value |
|---|---|
| Purpose | Verify that `.chirality/sessions/<sessionId>/events.jsonl` is the canonical Chirality runtime audit mirror, that SDK transcripts remain secondary unless imported into `HarnessEvent` form, and that runtime events support audit/replay without approving or issuing deliverables. |
| Authority | D-APP-65 disposition 4 — owner-authorized production tranche unlocking the D-APP-56 R4-P48 documentation deferral. |
| Source requirements | DEL-01-01-REQ-005 (`ScopeOfWork.md` CLM-009); DIRECTIVE §2.3; `docs/SPEC.md` §8-10; PRD session/audit requirements; construction per CLM-005 and CLM-016 step 6. |
| Date of verdicts | 2026-07-18 |
| Verdict status | All verdicts below are agent findings, not owner acceptance. Per CONTRACT K-AUTH-1, no approval, certification, sign-off, or issuance is rendered by this artifact. |
| Author | N6a docs-author child, RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18` |

## Checklist

| # | Check | Verdict (2026-07-18) | Evidence |
|---|---|---|---|
| A-01 | `events.jsonl` is named canonical in every governing layer. | PASS | `docs/DIRECTIVE.md` §2.3 ("The canonical Chirality runtime audit mirror is `.chirality/sessions/<sessionId>/events.jsonl`"); `docs/CONTRACT.md` K-EVENT-4; `docs/SPEC.md` §8.2/§8.4; `docs/TYPES.md` §1.8 and §7.2; `docs/PRD.md` §3.1 goal 18. |
| A-02 | SDK transcripts are secondary unless imported into `HarnessEvent` form. | PASS | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` §8.4 ("SDK transcripts are secondary runtime state unless imported into `HarnessEvent` form"); `docs/TYPES.md` §7.2 (`sdkTranscriptPath` "Secondary to Chirality audit events"); `docs/harness/reliance_boundary_register.md` RB-TRANSCRIPT row. |
| A-03 | Runtime events explain work and do not approve, issue, or prove compliance. | PASS | `docs/DIRECTIVE.md` §2.3 ("Runtime events do not make a deliverable approved, issued, code-compliant, externally validated, or safe for reliance"); `docs/PRD.md` §5 principle 3; `ScopeOfWork.md` CLM-004 runtime-audit condition. |
| A-04 | Accepted input persists before model/SDK execution (recoverable turn evidence). | PASS | `docs/CONTRACT.md` K-EVENT-2; `docs/SPEC.md` §10.1 ("persist `turn.accepted` before adapter/model execution"); `docs/PRD.md` FR-021. |
| A-05 | Every accepted turn ends in a durable terminal event. | PASS | `docs/CONTRACT.md` K-EVENT-3; `docs/SPEC.md` §10.1; `docs/PRD.md` FR-022. |
| A-06 | Replay tolerates malformed trailing lines and preserves valid prior events. | PASS | `docs/CONTRACT.md` K-EVENT-5; `docs/SPEC.md` §9.2; `docs/PRD.md` FR-073. |
| A-07 | Events exclude secrets; large payloads go to artifacts. | PASS | `docs/CONTRACT.md` K-EVENT-6/K-EVENT-7; `docs/SPEC.md` §9.2; register RB-REDACTION row. |
| A-08 | UI events and persisted events are separate contracts (audit richness does not leak into UI contract or vice versa). | PASS | `docs/CONTRACT.md` K-EVENT-1; `docs/SPEC.md` §9 vs §11; `docs/TYPES.md` §7.3-7.4; `docs/PRD.md` FR-074. |
| A-09 | Event schema/category inventories are mutually consistent across SPEC, TYPES, and register test index. | PASS | `docs/SPEC.md` §9.1/§9.3-9.4 identical to `docs/TYPES.md` §7.3; Section 9 validation IDs in `docs/SPEC.md` §19.3 all represented in `docs/harness/reliance_boundary_register.md` Test Index ("All 16 IDs... represented in the source manifest"). |
| A-10 | Audit-mirror enforcement is non-prompt-only. | PASS | Register RB-AUDIT row: enforcement surfaces `event-schema.ts`, `session-events.ts`, `sdk-message-mapper.ts`, `.chirality/sessions/<sessionId>/events.jsonl`; `PromptOnlyAllowed=NO`; validation IDs `section9.adapter_turn_engine_event_log`, `section9.session_event_replay`, and others. Verified at document level; test execution is not part of this DOC_UPDATE tranche. |

## Summary

- 10 PASS, 0 FAIL, 0 OPEN.
- REQ-005 verification condition (`events.jsonl` canonical, SDK transcripts
  secondary unless imported) is confirmed at the governance-document and
  register level. The known residual (SDK transcript placement/resume not yet
  fully governed) remains recorded where it belongs — the reliance register's
  residual-risk table — and does not contradict canonicality.
