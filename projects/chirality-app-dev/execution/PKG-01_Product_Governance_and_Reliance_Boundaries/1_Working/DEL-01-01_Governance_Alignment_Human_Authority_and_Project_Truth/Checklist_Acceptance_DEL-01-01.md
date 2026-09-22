# Acceptance Checklist — DEL-01-01

## Current applicability — 2026-09-22

This keyed review applies the settled D-GOV-43 / D-APP-127 direction, D-APP-131 execution (b), D-APP-132 retained controls and D-APP-118 facade retirement to every original check. It is current documentary disposition, not a new blanket PASS or product qualification. Authority references are repository-relative: Root `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`, App `execution/_Coordination/_DECISIONS/` rulings, current App `docs/harness/reliance_boundary_register.md`, and this deliverable's `ScopeOfWork.md`/`_STATUS.md`. Actual observed source hashes are in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/W00_03_GOVERNANCE_SOURCE_STATE.json`; final D-APP-38 integration is manager-owned. Live gaps below follow DEL-01-02 or DEL-01-03 current Remaining and their named register checks; none is closed by documentary consistency.

| Original check | Current disposition / obligation |
|---|---|
| C-01 | Register exists and has current per-boundary controls/gaps; the historical 13-row count is not a completeness proof for the current inventory. |
| C-02 | Prompt-only enforcement remains insufficient for a claimed reliance boundary; source instructions themselves do not establish host enforcement. Verify actual negative-test evidence for the surviving controls. |
| C-03 | D-GOV-43 accepts stock Codex-owned policy and configuration interfaces. The former opaque-SDK-default wording does not authorize overriding the user; current conditional guarantees and gaps are explicit in the register. |
| C-04 | REPAIRED: current register maps each boundary to accepted requirement/interface/named verification. Old hooks/settings-builder paths are compatibility evidence; live implementation qualification remains DEL-01-02 delivery. |
| C-05 | OPEN DELIVERY: authenticated human act, structural redaction, instruction protection and current Codex event/policy/delegation tests retain actual evidence gaps. Facade/fallback rollback support is retired by D-APP-118; no fallback-trigger owner decision remains. |
| C-06 | Current register category coverage is documentary coverage only; its domain, lifecycle, transcript, policy and instruction-control obligations survive the accepted host change. |
| C-07 | REPAIRED: lifecycle comes from DEL-01-02/_STATUS.md; register evidence is non-accepting and its old blanket CHECKING/PROPOSED labels are historical. |
| C-08 | Unknown outcomes stay explicit; stale reserved decisions are applied, not re-presented as TBD. Source observations are in W00_03_GOVERNANCE_SOURCE_STATE.json; final corpus registration is manager-owned. |
| C-09 | This current repair changes only dependency locator/notes carriers under the accepted scope; formal IDs, types, directions, statuses, satisfaction and source quotations remain intact. July no-write statement remains historical. |
| C-10 | INSP-03 assessments and July checklist results retain their dates. Current source dispositions here supersede their applicability without rewriting historical findings. |

## Preserved 2026-07-18 review (historical)

The original review below, including its headings, quoted sources, verdicts and counts, is preserved as dated evidence. Its obsolete subjects and open decisions have the current dispositions above.

## Header

| Field | Value |
|---|---|
| Purpose | Verify that each P0 reliance boundary referenced by this deliverable has a documented non-prompt-only enforcement surface or an openly recorded gap, and that unknowns and dependency rows are handled per governance. |
| Authority | D-APP-65 disposition 4 — owner-authorized production tranche unlocking the D-APP-56 R4-P48 documentation deferral. |
| Source requirements | DEL-01-01-REQ-006 (also REQ-008, REQ-010) (`ScopeOfWork.md` CLM-009); DIRECTIVE §2.9; CONTRACT K-RELIANCE-1/K-RELIANCE-2; `docs/PLAN.md` R0/R1; construction per CLM-016 step 8. |
| Date of verdicts | 2026-07-18 |
| Verdict status | All verdicts below are agent findings, not owner acceptance. Per CONTRACT K-AUTH-1, no approval, certification, sign-off, or issuance is rendered by this artifact. |
| Author | N6a docs-author child, RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18` |

## Checklist

| # | Check | Verdict (2026-07-18) | Evidence |
|---|---|---|---|
| C-01 | The reliance-boundary register required by K-RELIANCE-1 exists. | PASS | `docs/harness/reliance_boundary_register.md` exists and is populated (13 boundary rows). This supersedes the historical INSP-03 finding of a missing register (see `Assessment_INSP-03_DEL-01-01.md` REQ-006 PARTIAL and its D-APP-56 R5 P43 annotation: "ADQ-02 subsequently materialized and test-guarded `docs/harness/reliance_boundary_register.md`"). |
| C-02 | Every P0 boundary row forbids prompt-only enforcement. | PASS | Register rows RB-ENGINE through RB-FALLBACK each record `PromptOnlyAllowed=NO`; register Cross-Check Record row "P0 prompt-only exclusion: PASS". Independently spot-verified against the register table on 2026-07-18. |
| C-03 | Every P0 boundary row forbids opaque SDK-default-only enforcement (K-RELIANCE-2). | PASS | Each row records `SDKDefaultOnlyAllowed=NO`; register Cross-Check Record row "P0 opaque SDK-default-only exclusion: PASS". |
| C-04 | Each boundary names a concrete non-prompt enforcement surface. | PASS | Every row lists code/hook/API/test surfaces (e.g. RB-FILESYSTEM: `tool-path-policy.ts`, `chirality-hooks.ts`; RB-SETTINGS: `sdk-options-builder.ts` `settingSources`; RB-AUDIT: `session-events.ts`, `events.jsonl`), plus the register's Enforcement Matrix. |
| C-05 | Validation coverage per boundary. | OPEN (2 recorded gaps, both documented) | RB-HUMAN-GATE `ValidationID=TBD` (approval is a human act; "Runtime checks can collect evidence only") and RB-FALLBACK carries `TBD` for fallback-trigger review. Both are recorded in the register itself with residual risk, satisfying REQ-006's "documented enforcement plan **or an open gap**" disjunct; they are carried here as OPEN, not failures. |
| C-06 | Register categories cover the K-RELIANCE-1 inventory (safety, audit, filesystem, lifecycle, transcript, settings, subagent, human-gate). | PASS | Register Cross-Check Record: "Required boundary categories present: PASS" — engine, audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, tool-surface, hook, redaction, fallback rows all present. |
| C-07 | Register status is honestly represented (not treated as accepted truth). | PASS | Register Status table: "CHECKING evidence only; not ISSUED"; every row `DecisionStatus=PROPOSED`. This checklist relies on it as documented evidence, not as owner acceptance. |
| C-08 | Unknowns are marked `TBD`/`ASSUMPTION`/`PROPOSAL`/source warning/human-ruling-needed (REQ-008). | PASS | Register uses explicit `TBD` and residual-risk rows; this artifact set uses OPEN verdicts and `Table_Conflict_Source_Warnings_DEL-01-01.md` for conflicts; no unsupported claim was promoted to fact. |
| C-09 | Dependency rows are not satisfied, retired, or mutated by this tranche (REQ-010; CLM-004 condition). | PASS | This run wrote no changes to `Dependencies.csv` or `_DEPENDENCIES.md`; the 12-row register status recorded in `Assessment_INSP-03_DEL-01-01.md` is unchanged by this documentation production. |
| C-10 | Historical REQ-006 PARTIAL / REQ-010 FAIL findings are treated as historical, not current truth. | PASS | `Assessment_INSP-03_DEL-01-01.md` D-APP-56 R5 P43 annotation (2026-07-12): those conclusions "are not current truth" at the live state; no assessment verdict was altered by this tranche. |

## Summary

- 9 PASS, 1 OPEN (C-05: two register-documented validation gaps — RB-HUMAN-GATE
  by design, RB-FALLBACK trigger review pending), 0 FAIL.
- REQ-006 verification condition is met: every P0 reliance boundary has a
  documented non-prompt-only enforcement surface, and the two residual gaps are
  open and recorded rather than hidden.
