# Governance Consistency Notes — DEL-01-01

## Current applicability — 2026-09-22

This keyed review applies the settled D-GOV-43 / D-APP-127 direction, D-APP-131 execution (b), D-APP-132 retained controls and D-APP-118 facade retirement to every original check. It is current documentary disposition, not a new blanket PASS or product qualification. Authority references are repository-relative: Root `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`, App `execution/_Coordination/_DECISIONS/` rulings, current App `docs/harness/reliance_boundary_register.md`, and this deliverable's `ScopeOfWork.md`/`_STATUS.md`. Actual observed source hashes are in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/W00_03_GOVERNANCE_SOURCE_STATE.json`; final D-APP-38 integration is manager-owned. Live gaps below follow DEL-01-02 or DEL-01-03 current Remaining and their named register checks; none is closed by documentary consistency.

| Original check | Current disposition / obligation |
|---|---|
| N-01 | Authority order remains applicable; accepted D-GOV-43 and D-APP-127 specialize the old SDK subjects. No lower-level historical PASS overrides them. |
| N-02 | Project truth remains governed project files plus accepted Git history. Shared Codex resources and userData runtime evidence are allowed convenience/runtime state, not project truth. |
| N-03 | Human-only acceptance and professional reliance remain live controls; the actor-identity enforcement gap remains open in RB-HUMAN-GATE. |
| N-04 | Lifecycle vocabulary and approval evidence remain applicable. Current DEL-01-01 state is read from _STATUS.md; the historic CHECKING admission is not current lifecycle. |
| N-05 | REPAIRED: canonical audit locus is Runtime-owned userData under K-EVENT-4; project-local .chirality/sessions is compatibility history. D-GOV-43 / D-APP-127 supersede the old locus. |
| N-06 | REPAIRED: stock Codex App Server is the sole qualified MVP engine; shared settings/resources and user-selected approval/sandbox policy replace SDK/key-aware/Pi-default direction. D-GOV-43 / D-APP-127. |
| N-07 | REPAIRED: preserve full Codex protocol and every notification, including unfamiliar events; named event indexes remain compatibility evidence rather than a filtering allowlist. Current live preservation/replay checks remain in DEL-01-02. |
| N-08 | Register existence is verified at docs/harness/reliance_boundary_register.md; current rows distinguish conditional policy, native service interfaces and still-missing enforcement. Existence is not qualification. |
| N-09 | Retired PKG-08 stays retired. Native configured Codex capabilities are permitted by D-GOV-43; independent App expansions and domain apply retain their own accepted scope gates. |
| N-10 | REPAIRED: C002 applies the already ruled stable-ID/live-path decision; C003 distinguishes historical hash observations from current D-APP-38 source state. See current conflict table below; no repeated owner prompt. |
| N-11 | REPAIRED: current ScopeOfWork.md/_CONTEXT.md name the accepted ResponsibleParty per D-APP-65/68. The dated TBD warning is historical and does not undo that assignment. |

## Observed current source disagreements

The current App `docs/DIRECTIVE.md` still contains pre-replatform wording: §2.3 names project-local `.chirality/sessions` and an SDK-schema import boundary; §2.8 names Claude/key-aware defaults, an opt-in Pi path and Chirality-owned fixed permission mechanics; §8 names one opt-in per-user daemon. Those statements are not consistent with the accepted D-GOV-43 / D-APP-127 current host direction. Their current application is resolved by the later accepted direction: Runtime-owned userData evidence, the complete stock Codex protocol, shared user configuration, user-selected policy and App-owned host process. D-APP-118 retires the facade support obligation. This local review records the disagreement instead of asserting that all current document bytes are mutually consistent.

Correction path: the owning App/Root authority-document process propagates the already accepted direction into those governing carriers and regenerates their affected contract/source evidence; the manager owns current D-APP-38 source registration. This is existing authority-carrier work, not a new owner decision or a reason to restore the superseded mechanisms. The seven local artifacts now apply the settled direction; no governing document or instruction is amended by this local repair. A current hash registration identifies bytes and does not alone prove semantic consistency.

## Preserved 2026-07-18 review (historical)

The original review below, including its headings, quoted sources, verdicts and counts, is preserved as dated evidence. Its obsolete subjects and open decisions have the current dispositions above.

## Header

| Field | Value |
|---|---|
| Purpose | Compare the governing document set (`docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md`) using the authority order in `docs/DIRECTIVE.md` §0 and the invariant catalog in `docs/CONTRACT.md`, and record actual conflicts rather than silently resolving them. |
| Authority | D-APP-65 disposition 4 — owner-authorized production tranche unlocking the D-APP-56 R4-P48 documentation deferral. |
| Source requirements | DEL-01-01-REQ-001 (`ScopeOfWork.md` CLM-009); construction per CLM-005 and CLM-016 step 3. |
| Date of verdicts | 2026-07-18 |
| Verdict status | All verdicts below are agent findings, not owner acceptance. Per CONTRACT K-AUTH-1, no approval, certification, sign-off, or issuance is rendered by this artifact. |
| Author | N6a docs-author child, RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18` |

## Method

Each governing document was read in full at the live tree state on 2026-07-18 and
compared pairwise along the authority order of `docs/DIRECTIVE.md` §0 (DIRECTIVE →
CONTRACT → SPEC → TYPES → PLAN → PRD → agent instructions / accepted execution
records). Invariant families owned or co-owned by PKG-01 were checked against
their DIRECTIVE basis and downstream restatements. Conflicts are recorded, not
resolved; resolution paths are proposals only.

## Consistency Notes

| # | Check (higher-authority source vs lower) | Verdict (2026-07-18) | Evidence |
|---|---|---|---|
| N-01 | Authority order is stated once and not contradicted downstream. | PASS | `docs/DIRECTIVE.md` §0 (seven-step order); `docs/PLAN.md` "Control-Plane Boundary" defers to DIRECTIVE/CONTRACT/SPEC/TYPES for intent, invariants, mechanics, vocabulary; `docs/PRD.md` establishes direction without claiming to erase higher authority (DIRECTIVE §0: "The PRD establishes vNext product direction, but it does not erase the authority of the directive, contract, specification, vocabulary..."). |
| N-02 | Project-truth invariants (K-FS-1, K-GIT-1, K-NOMEM-1) trace to DIRECTIVE intent. | PASS | `docs/CONTRACT.md` §1.1 vs `docs/DIRECTIVE.md` §2.1, §2.2, §2.6; restated in `docs/TYPES.md` §1.7 and `docs/PRD.md` §5 principles 1-3, 6. No divergence in meaning found. |
| N-03 | Human-authority invariants (K-AUTH-1/2, K-BIND-1, K-GATE-1, K-PROF-1) trace to DIRECTIVE §2.4 and §3. | PASS | `docs/CONTRACT.md` §1.2 vs `docs/DIRECTIVE.md` §2.4 ("Agents propose; humans approve"), §3.2 (engineer-of-record decision rights). `docs/CONTRACT.md` §4 records no retired invariants, so all remain binding. |
| N-04 | Lifecycle contract is consistent between SPEC and TYPES. | PASS | `docs/SPEC.md` §4.2-4.4 and `docs/TYPES.md` §5 state the identical state chain, the same two human-authorized reversal transitions, the same regime (not percentage-complete) framing, and the same `## Remaining` adoption (SPEC §4.1, owner-adopted 2026-07-10). |
| N-05 | Runtime-audit boundary is consistent across DIRECTIVE/CONTRACT/SPEC/TYPES/PRD. | PASS | `docs/DIRECTIVE.md` §2.3; `docs/CONTRACT.md` K-EVENT-4, K-SDK-3; `docs/SPEC.md` §8.4; `docs/TYPES.md` §1.8; `docs/PRD.md` §3.1 goal 18. All name `.chirality/sessions/<sessionId>/events.jsonl` as canonical with SDK transcripts secondary. |
| N-06 | Provider-adapter posture (K-ENGINE-3/K-ENGINE-6, D-APP-18 key-aware default) is stated consistently. | PASS | `docs/DIRECTIVE.md` §2.8; `docs/CONTRACT.md` K-ENGINE-3/K-ENGINE-6; `docs/SPEC.md` §10.3, §12.1; `docs/PLAN.md` §2 and §12; `docs/PRD.md` §2 and FR-027. All carry the same D-APP-18 Option A wording (real `agentSdk` when a key is configured, else `stub`). |
| N-07 | `HarnessEvent` shape and event-category inventories match between TYPES and SPEC. | PASS | `docs/TYPES.md` §7.3 vs `docs/SPEC.md` §9.1, §9.3-9.4 — identical type target and identical initial/later category lists. |
| N-08 | Reliance-boundary rule (K-RELIANCE-1/2) traces to DIRECTIVE §2.9 and is operationalized. | PASS | `docs/CONTRACT.md` K-RELIANCE-1/K-RELIANCE-2 vs `docs/DIRECTIVE.md` §2.9; operational surface exists at `docs/harness/reliance_boundary_register.md` (see `Checklist_Acceptance_DEL-01-01.md`). |
| N-09 | Retired-scope discipline (K-RETIRED-1, PKG-08) is consistent. | PASS | `docs/CONTRACT.md` K-RETIRED-1; `docs/PLAN.md` §9 and §11; `docs/PRD.md` §3.2 Non-Goals and §6.4. No document reactivates retired scope. |
| N-10 | Lower-authority conflicts with higher-authority sources. | OPEN (2 recorded) | No conflict was found **among the six governing documents themselves** in the sections reviewed. Two record-level conflicts/warnings involving deliverable-local and dispatch records remain open and are carried in `Table_Conflict_Source_Warnings_DEL-01-01.md` (C002 dispatch-label mismatch; C003 REF-006 record disagreement). |
| N-11 | Deliverable-kit internal staleness. | OPEN (note) | `ScopeOfWork.md` CLM-008 ("ResponsibleParty remains `TBD`..."), CLM-016 step 1 ("`ResponsibleParty=TBD`"), and CLM-022 ("Keep `ResponsibleParty` as `TBD`...") predate the 2026-07-18 D-APP-65 assignment recorded in CLM-002, CLM-015, CLM-026 R003, and `_STATUS.md`. The later dated records control; the stale quoted text is historical and is not edited by this tranche (quoted records stay byte-intact). Recorded as a source warning (W-01) in the conflict table. |

## Summary

- 9 PASS, 2 OPEN (N-10 conflict carriage; N-11 stale-kit-text warning), 0 FAIL.
- No conflict between any two of the six governing documents was identified in
  the sections reviewed. The authority order itself is uncontested across the set.
- Open items are record-level (dispatch label, REF-006 record disagreement,
  stale kit prose) and are carried for human ruling in
  `Table_Conflict_Source_Warnings_DEL-01-01.md` per CONTRACT K-CONFLICT-1.
