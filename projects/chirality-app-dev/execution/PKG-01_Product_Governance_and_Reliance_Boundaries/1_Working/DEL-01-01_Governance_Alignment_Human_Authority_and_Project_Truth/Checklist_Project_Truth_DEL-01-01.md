# Project-Truth Checklist — DEL-01-01

## Current applicability — 2026-09-22

This keyed review applies the settled D-GOV-43 / D-APP-127 direction, D-APP-131 execution (b), D-APP-132 retained controls and D-APP-118 facade retirement to every original check. It is current documentary disposition, not a new blanket PASS or product qualification. Authority references are repository-relative: Root `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`, App `execution/_Coordination/_DECISIONS/` rulings, current App `docs/harness/reliance_boundary_register.md`, and this deliverable's `ScopeOfWork.md`/`_STATUS.md`. Actual observed source hashes are in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/W00_03_GOVERNANCE_SOURCE_STATE.json`; final D-APP-38 integration is manager-owned. Live gaps below follow DEL-01-02 or DEL-01-03 current Remaining and their named register checks; none is closed by documentary consistency.

| Original check | Current disposition / obligation |
|---|---|
| T-01 | Project truth remains governed plain project files plus accepted Git history; Runtime-owned userData and shared Codex state do not silently become project truth. |
| T-02 | Accepted decisions remain recorded and bound to reviewable project evidence; chat-only statements cannot substitute for the governed record. |
| T-03 | Shared Codex settings, memory and threads are permitted as native resources under D-GOV-43 item 5. Their availability does not confer project authority, and Chirality must not veto them. |
| T-04 | Runtime transcripts, caches, model context and UI convenience state remain distinct from accepted project truth, regardless of native provider or storage locus. |
| T-05 | Chirality authentication is separated and custodied by Codex; secret exclusion remains required. Actual raw-stream structural redaction is an open RB-REDACTION delivery gap, not proved by this checklist. |
| T-06 | Existing approval SHA and lifecycle history are preserved byte-for-value. Current content repair is not a new human approval. |
| T-07 | Current results reside in these seven project files and W00_03 evidence. They are uncommitted author outputs until parent integration; no accepted Git status is fabricated. |
| T-08 | Native transcripts/runtime logs are retained as complete audit evidence, not project truth. The old SDK-only import mechanism does not constrain full Codex event preservation. |
| T-09 | _STATUS.md and canonical dependency registers retain their authority; current changes do not satisfy or retire a formal edge or change lifecycle. |
| T-10 | When runtime/external material is relied upon as project truth it must enter governed project records. D-GOV-43 item 5 does not make a generalized import feature a prerequisite for native memory/thread support. |

## Preserved 2026-07-18 review (historical)

The original review below, including its headings, quoted sources, verdicts and counts, is preserved as dated evidence. Its obsolete subjects and open decisions have the current dispositions above.

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
