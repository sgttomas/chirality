## §4 Patterns (hand-written by the PKG-03 manager from the shard notes; evidence, not rulings)

1. **Event-contract AUTHORITY_CONFLICT cluster (CONTESTED, not refuted).** Every ledger found the same
   tension. D-GOV-43 amended K-EVENT-1/6, SPEC §11 and TYPES §7.4 (preserve upstream Codex methods and
   payloads); K-ENGINE-4, SPEC §10.3 and TYPES §7.1 (translate; no provider-shaped events) stay
   unamended. DEL-03-01 marks 7 rows AUTHORITY_CONFLICT (CLM-004.1, 004.6, 009.2, 009.7, 018.2, 022.1,
   022.5). The shard kept R0's CONTESTED grading: the rulebook also admits reading `codex.*` as
   Chirality-named categories with the upstream payload carried as adapter metadata, which D-APP-127
   would support under MR-11. DEL-03-02 CLM-009.10, DEL-03-03 CLM-003.6 (with SEE rows) and DEL-03-04
   CLM-022.4 were CONFIRMED as AUTHORITY_CONFLICT with plain R4; no named question fits. The shard also
   notes that DIRECTIVE §2.10 is higher-tier and on the neutrality side, but the unnamed D-GOV-43
   undercut still leaves the conflict. **R3 question:** frame this as a named R4 question (it
   recurs in PKG-06 wave 1 and R0 §8 item 3).
2. **Unamended SPEC §10.4 (route takes the lock and forwards to TurnEngine) against amended SPEC
   §17.1/§25.1 (routes are thin Runtime clients) is graded three ways across the package:**
   AUTHORITY_CONFLICT + R4-Q1 (DEL-03-04 CLM-010.4), IMPLEMENTED_DIFFERENTLY + R4-Q1 (DEL-03-03
   CLM-003.3, CONTESTED), folded into STALE_SPECIFICATION (DEL-03-04 CLM-003, CONTESTED), or argued
   away (DEL-03-02 CLM-009.3, outside the sample, flagged by the shard). These ledgers were sealed
   before RUN_BASIS Addendum 6 (R4-Q1 subject test); R3 re-derives R4-Q1 and should treat the §10.4
   clause once for the package.
3. **Dated history notes (§2.6 tie-break 3 vs MR-8 iv).** DEL-03-04 CLM-013.1, CLM-031 and STATE-3
   (dated reconciliation and MEMORY entries) and DEL-03-03 STATE-2 are CONTESTED between
   STALE_SPECIFICATION and "true of its date". The adopted tie-break did not close this case; the
   tie-break was applied correctly on present-tense MATCH restatements (DEL-03-01 CLM-016.3/004.7,
   DEL-03-04 REGISTER-2) and on Remaining items (DEL-03-03 REM-1, rule 2a).
4. **SoW self-declared "compatibility history".** DEL-03-02's SoW (L18-27, L37-38) says its SCA-APP-010
   section controls and older clauses are dated history. The worker graded those older clauses
   IMPLEMENTED_DIFFERENTLY; ACCEPTED_DIVERGENCE is also available under grading key 6 (CLM-008
   CONTESTED). "Or equivalent" requirements met by the Runtime TurnCoordinator (CLM-009.1) can be ALIGNED.
5. **Field-level refutations (10, all in CORRECTIONS.csv).**
   - DirectionEvidence (5, DEL-03-01): `CTX:` cites the deliverable's own `_STATUS.md`, which RUN_BASIS
     §5 classes as declared state, not CONTEXT. Proposed `GOV:D-APP-127`.
   - AuthorityTier (3): PRD-only rows tiered GOVERNANCE_INVARIANT (DEL-03-03 CLM-005.3, DEL-03-04
     CLM-004.1) and a SPEC §9.2 restatement tiered LOCAL_DESIGN (DEL-03-04 CLM-005).
   - AssessmentEvidence (1): DEL-03-04 CLM-009.12 keeps an INSP-03 PASS that rested on LEGACY_ONLY
     `turn-engine.ts` as STILL CURRENT; should be OVERTAKEN.
   - Notes (1): DEL-03-04 CLM-006 points to REGISTER-1 in prose, not `SEE:DEL-03-04#REGISTER-1`.
6. **What held.** All line anchors checked were exact or within tolerance; REACH tags were confirmed
   from entry points (no LIVE tag on unexecuted code was found; `turn-engine.ts`, the conformance suite
   and the harness-contract facade were correctly tagged LEGACY_ONLY / TEST_ONLY); PostReleaseBasis held
   everywhere; all 18 class-c capability responses CONFIRMED; no errata were filed by any worker.

## §5 Rerun and acceptance record

| Deliverable | Attempts | Ledger of record | Why |
|---|---|---|---|
| DEL-03-01 | one | `DEL-03-01` | 0 verdict-field refutations of 40 items (0.0%). 5 field-level (DirectionEvidence) in CORRECTIONS.csv. |
| DEL-03-02 | one | `DEL-03-02` | 0 REFUTED of 22 items. |
| DEL-03-03 | one | `DEL-03-03` | 0 verdict-field refutations of 31 items; 1 field-level (AuthorityTier). |
| DEL-03-04 | one | `DEL-03-04` | 0 verdict-field refutations of 28 items; 4 field-level. |

No structural failure; no rerun under RUN_BASIS Addendum 3. All four forward passes sealed after
Addenda 4 and 5 reached the workers and before Addendum 6 was adopted, so the R4-Q1 subject test was not
applied by workers or verifiers; R3 re-derives R4-Q1 from the REACH tags.
