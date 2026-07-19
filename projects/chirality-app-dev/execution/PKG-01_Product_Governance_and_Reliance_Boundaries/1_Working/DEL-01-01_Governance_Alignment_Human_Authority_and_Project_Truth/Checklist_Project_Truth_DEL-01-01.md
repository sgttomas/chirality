# Project-Truth Checklist — DEL-01-01

## Header

| Field | Value |
|---|---|
| Purpose | Verify that reliance-relevant facts land in versioned project files under the working root plus accepted git history, and that runtime state, chat, SDK transcripts, UI state, caches, model context, API keys, and hidden memory are not treated as project truth unless imported through governance. |
| Authority | D-APP-65 disposition 4 — owner-authorized production tranche unlocking the D-APP-56 R4-P48 documentation deferral. |
| Source requirements | DEL-01-01-REQ-004 (`ScopeOfWork.md` CLM-009); DIRECTIVE §2.1/2.2/2.6; `docs/TYPES.md` §1.7 Project Truth; construction per CLM-005 and CLM-016 step 5. |
| Date of verdicts | 2026-07-18 |
| Verdict status | All verdicts below are agent findings, not owner acceptance. Per CONTRACT K-AUTH-1, no approval, certification, sign-off, or issuance is rendered by this artifact. |
| Author | N6a docs-author child, RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18` |

## Checklist

| # | Check | Verdict (2026-07-18) | Evidence |
|---|---|---|---|
| T-01 | Filesystem-is-the-database posture is stated and binding. | PASS | `docs/DIRECTIVE.md` §2.1; `docs/CONTRACT.md` K-FS-1 ("Project truth lives in plain files under the working root and accepted git history, not in hidden app state, chats, SDK transcripts, model context, or vendor systems"). |
| T-02 | Git is the event store for accepted project truth; unversioned decisions do not exist for reliance. | PASS | `docs/DIRECTIVE.md` §2.2 ("If a decision is not in a versioned file, it does not exist for purposes of reliance"); `docs/CONTRACT.md` K-GIT-1; `docs/PRD.md` §2 core thesis and §5 principles 1-2. |
| T-03 | No hidden memory may become authoritative; convenience state must be explicitly non-authoritative. | PASS | `docs/DIRECTIVE.md` §2.6; `docs/CONTRACT.md` K-NOMEM-1; `docs/SPEC.md` §1.3 (runtime configuration state is non-authoritative unless imported); `docs/PRD.md` FR-042 (toolkit presets non-authoritative). |
| T-04 | Canonical vocabulary defines Project Truth to exclude transcripts/chat/UI/keys/caches. | PASS | `docs/TYPES.md` §1.7: "Runtime transcripts, chat drafts, UI state, API keys, SDK transcripts, and caches are not project truth unless a governed process imports relevant content into project files." |
| T-05 | API keys are excluded from project files, events, and logs. | PASS | `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` §16.2; `docs/PRD.md` FR-031. |
| T-06 | Accepted decisions bind to git SHA or equivalent immutable evidence. | PASS | `docs/DIRECTIVE.md` §2.4 ("Approvals bind to specific content and must be traceable to a git SHA"); `docs/CONTRACT.md` K-AUTH-2; live example: `_STATUS.md` line 7 records `Checking Approval SHA: 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`. |
| T-07 | Storage-location practice in this deliverable conforms: reliance-relevant facts of this tranche land in versioned files. | PASS | The seven artifacts, the run record (`_run_records/TASK_RUN_2026-07-18_DAPP65_docs_production.md`), the `_STATUS.md` Remaining/History update, and the `ScopeOfWork.md` R004 closure note are all plain files inside the deliverable folder / coordination root, entering git history via the T3 tranche commit. Nothing produced here is represented only in chat, runtime, or transcript state. |
| T-08 | SDK transcripts and runtime logs are declared non-truth unless imported. | PASS | `docs/DIRECTIVE.md` §2.2 (session logs "are not a substitute for accepted project-state files"), §4.2 out-of-scope list; `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` §8.4; `docs/PRD.md` §3.2 Non-Goals. |
| T-09 | Deliverable-local lifecycle/dependency truth stays in its canonical files. | PASS | `docs/CONTRACT.md` K-STATUS-1 (`_STATUS.md` canonical) and K-DEP-1 (`_DEPENDENCIES.md` + `Dependencies.csv` authoritative, aggregation on-demand); this tranche mutated no dependency row (CLM-004 dependency-register condition observed). |
| T-10 | Governed-import path exists for external/runtime facts that matter for reliance. | PASS | `docs/DIRECTIVE.md` §2.6 and CLM-024 example row ("Record or import the relevant detail into Chirality `HarnessEvent` form or a governed project artifact before treating it as reliance evidence"). |

## Summary

- 10 PASS, 0 FAIL, 0 OPEN.
- REQ-004 verification condition (claims and storage locations verified) is met
  at the governance-document level, and this tranche's own outputs conform to the
  project-truth rule they verify.
