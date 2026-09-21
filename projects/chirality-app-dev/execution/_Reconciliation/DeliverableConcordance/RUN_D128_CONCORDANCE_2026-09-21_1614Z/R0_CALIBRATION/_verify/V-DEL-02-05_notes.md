# V shard — DEL-02-05 (R0 calibration, unit V)

Fresh evidence-only verifier. Basis: frozen tree at `00115c719`. Inputs: the 57 SELECTION rows
for DEL-02-05, the unit's claims, notes, reverse and reverse-notes files,
`SURFACES/HARNESS_capabilities.csv` (two rows), `CONVENTIONS_CANDIDATE.md`, and `RUN_BASIS.md`
§3 and §5. No ledger was edited. Git use was limited to read-only `log` and `show`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (non-ALIGNED, LOW/self-flag, reverse-notes) | 52 | 37 | 0 | 15 |
| b (ALIGNED sample) | 3 | 3 | 0 | 0 |
| c (CLAIMED_BY sample) | 2 | 1 | 0 | 1 |
| **Total** | **57** | **41** | **0** | **16** |

**What held up:**

- **Evidence locations.** Every cited test file and test-case name exists at the frozen tree
  (21 checked). Cited code line ranges hold to within a few lines.
- **Hosted-path gating.** `settings-view.tsx:31-35` gates the API-key, local-model and consent
  groups on the absence of `hosted`, and `shell-frame.tsx:379,404` always supplies `hosted`.
- **PostReleaseBasis = NO holds on every row.** `git show --name-only` on `da95ec194`,
  `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a` touches none of the cited App or Runtime files, as the
  reverse notes found. Within the evidence roots, `9ecbdecdf` touches nothing (execution tree only).
- **The D-APP-127 A2 rows** (SEC-1.3, SEC-1.5, SEC-2.1, SEC-2.3, SEC-2.4, CLM-013.2/.6/.8,
  CLM-017.2, CLM-020.3, CLM-023.2, REGISTER-1, STATE-1, STATE-2) match the ruling text. The SoW,
  `_CONTEXT.md` and `Dependencies.csv` were last committed on or before 2026-09-07, so the
  2026-09-12 tranche did not touch them.
- **REM-1.**
  - MechanicallyUnblocked = NO is correct under MR-2/MR-6: the Depends item DEL-04-05-V3-02 is
    still `NOT_SELECTABLE_UNTIL`.
  - CARRIER_PROPAGATION is supported by timing: `_STATUS.md` was last written 2026-09-12 01:55,
    and the login code landed later that day (02:50 to 12:44).

## (ii) Systematic patterns

1. **The governing sole-engine preamble was not applied to Anthropic API-key rows.** These rows
   are CONTESTED: CLM-003, CLM-009.1, CLM-010.1, CLM-010.2 and CLM-010.3.
   - The worker chose IMPLEMENTED_DIFFERENTLY with R4 because "PRD FR-030 and 7.7 still carry
     the Anthropic requirement".
   - GOVERNING `docs/PRD.md:15` and `docs/CONTRACT.md:15`, however, already declare
     Claude/Anthropic descriptions compatibility history that need not ship.
   - Under MR-11 (generalized), that supports STALE_SPECIFICATION / CODEX_SOLE_ENGINE with
     HumanDecisionNeeded NO.
   - Exception: rows that also restate K-KEY-1's four typed storage states keep R4. K-KEY-1 is
     still governing, so SEC-1.1, CLM-010.4 and CLM-013.3 are CONFIRMED.
   - Related inconsistency: the same typed-state content carries CODEX_SOLE_ENGINE on SEC-1.1
     and CREDENTIAL_CUSTODY on CLM-013.3.
2. **The REF-006 "MATCH" notes were classed NOT_AUDITABLE, but the claim is checkable and now
   false.** These rows are CONTESTED: CLM-001, CLM-006, CLM-014 and CLM-021. CLM-027 is
   CONFIRMED with a note.
   - At `00115c719`, `docs/PRD.md` hashes to `17ca3f3c…`, but `_REFERENCES.md` still records
     expected = actual = `8649ccba…` with status MATCH. REF-002 (CONTRACT) and REF-003 (SPEC)
     also mismatch.
   - This is a **missed register defect**. The ledger has no REGISTER row for the stale
     `_REFERENCES.md` hash table.
   - AssessmentEvidence is also inconsistent. The assessment discussed REF-006 HASH_MISMATCH
     (`Assessment_INSP-03_DEL-02-05.md:45`). CLM-027 uses OVERTAKEN for that; CLM-001/006/014/021
     use NOT APPLICABLE.
3. **Conditional obligations and adapted contracts were forced into a divergence reading.**
   - **SEC-1.4, SEC-2.5, CLM-013.5 (role and posture labels).**
     - K-ROLE-2's label applies only if G-ROLE fails, which the worker could not establish.
     - `Opt-in Preview` appears only in the decomposition row and the SoW, not in
       CONTRACT/PRD.
     - D-APP-127 keeps the labelled fake states.
     - PARTIALLY_IMPLEMENTED / UNRECORDED_JUDGMENT versus UNKNOWN is a real ambiguity.
       Convention gap: there is no rule for a divergence whose trigger condition cannot be
       evaluated.
   - **CLM-013.4 (network postures).** STALE_SPECIFICATION with "remove or mark retired"
     overlooks the adaptation:
     - GOVERNING K-NET-1 (`CONTRACT.md:134`) keeps the three postures, read as the user's Codex
       configuration and sandbox choice shown in the composer.
     - The composer permission selector implements that (`chat-panel.tsx:119-139`).
     - The reading is contested: stale for the per-root form, implemented differently
       otherwise. The evidence citation misses the composer.
   - **CLM-010.10 (facade).** STALE_SPECIFICATION at HIGH confidence is overstated.
     - `@chirality/harness-contract` still exists as a deprecated re-export of the same type.
     - D-APP-118 (facade retirement) is AWAITING_RULING (`_REGISTER.md:135`).
     - The text is therefore not flatly false (MR-8). LatestDecision and HumanDecisionNeeded
       should cite D-APP-118.
   - **SEC-2.2 (Q7 account row).** The worker's own alternative has governing support: the
     D-APP-127 replacement at lines 113-117 says the account row acts on Codex's own login flow.
     CONTESTED.

**Minor convention issues** (recorded in ConventionIssue; no verdict change):

- **AuthorityTier "highest tier restated".** Rows citing SPEC/TYPES were tagged PRD instead of
  GOVERNANCE_INVARIANT: CLM-003, CLM-005 and CLM-010.1-3.
- **VER-001 (CLM-020.2)** was typed CONTEXT_CLAIM so that it could be NOT_AUDITABLE.
- **STATE-1** cites a CONTEXT record as its ImplementationEvidence.
- **SEC-3's** LatestDecision could name D-APP-109.
- **DirectionEvidence** is CONTEXT-only throughout, which is correct.
- No ACCEPTED_DIVERGENCE rows exist, so the MR-8 acknowledgement test did not arise.

**Class c.**

- **CAP-HARNESS-015 → CLM-010.5:** CONFIRMED.
- **CAP-HARNESS-013 → CLM-010.6:** CONTESTED.
  - The capability also persists the per-chat model/reasoning pair, the unsent permission and
    the interaction mode. R06 retry preservation owns none of these, so PARTIAL is equally
    defensible.
  - The capability-granularity rule does not say when a broader capability should be
    CLAIMED_BY rather than PARTIAL.

## (iii) Effort

- **Files read:** about 30.
  - Deliverable kit: SoW (full), `_STATUS.md`, `_CONTEXT.md`, `Dependencies.csv`,
    `_REFERENCES.md` and assessment greps.
  - Governing and context sources: D-APP-127 (lines 34-198), CONTRACT line greps, PRD greps,
    three CONTEXT records and the decision register.
  - About 15 frontend/Runtime source files, by line range.
  - Test-name greps over 11 test files, the gate transcript, and git show for four commits.
- **Context:** moderately tight. The ledger's 58 KB had to be reformatted before it could be
  read. Deduplicating shared evidence (settings-view gating, D-APP-127 sections) kept the
  budget workable.
