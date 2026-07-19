# Governance Consistency Notes — DEL-01-01

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
