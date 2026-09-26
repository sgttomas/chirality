# B4 verifier verdict 01 — SCA-006 checkpoint-group-1 package

Verifier: fresh read-only TASK instance (Claude Code Agent tool, `subagent_type: pec-reviewer`, `model: opus`; host maps to claude-opus-5-5), dispatched by the B4 WORKING_ITEMS manager. Reviewed candidate: commit `e2855e552` (base `origin/main` `13df8b795`). The verdict text below is the verifier's hand-back, transcribed verbatim by the manager. It is model output, not an owner act.

---

**Verdict: PASS WITH MINOR.** Nothing blocks the SCA-006 checkpoint-group-1 package at candidate `e2855e552` (base `13df8b795`). Seven MINOR findings are listed below. Findings 1 to 5 change text the owner will read, and the owner accepts `Impact_Assessment.md` at its exact SHA-256. So repair them before the package reaches the owner. After the repair, recompute the IA hash and update it in `Decision_Log.md` row SCA006-CP1 and in `Handoff_State.md`.

**Basis I relied on** (recomputed with `shasum -a 256`, all match what the package records):
- Root `AGENTS.md` `c8ce87ef…0dffd`
- `projects/pec/AGENTS.md` `c9d3b44d…9ee197a`
- `agents/AGENT_TASK.md` `1a13a5b0…c57c8fb7`
- `workflows/scope-change/WORKFLOW.md` `58f5d1d5…a7a90`
- `workflows/scope-change/resources/contract.md` `4453a719…44d02`
- `workflows/scope-change/resources/method.md` `34187e83…d167f5`
- Brief B4 `87612aca…ae90`
- D-PEC-90 ruling `43a0c663…efab` and proposal `b04a8aa2…e147`
- D-PEC-91 `5d896204…3fbe`, D-PEC-94 `eb9793aa…5e81` (both at base), D-PEC-67 `c04f8ddd…d9a8`, D-PEC-70 `eff5f66b…91eb`
- PRD v2.3 `fff27a66…dc32`, SOFTWARE_DECOMP 1.5 `dc2b8479…9660`
- Registers and pointers, Root PRD_ROOT and CONTRACT, the SCA-005 files, the hold register and script, LOOP_INIT, `pec.yaml`, the Runtime docs, and the K03-A input all match as recorded.

## What checks out
- **Containment.** `git diff --name-only 13df8b795..e2855e552` touches only the six files in `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/`. No forbidden path is touched. `git diff --check` is clean and the working tree is clean.
- **Snapshot hashes.** Every hash in the Handoff table and in Decision_Log row SCA006-CP1 matches the committed bytes:
  - IA `c2ad7c41…a888a72`
  - CSV `a8e600e3…a902`
  - Brief `259448df…4f34`
  - JSON `b7b432a2…b128d`
  - Decision_Log `249bfb69…2107`
- **Baseline.** `Pre_Change_Coverage.json` is byte-identical to the `coverage_summary.json` of `COV_SCA005_POSTSETUP_2026-09-25_1606`. `995af4f36` is an ancestor of the base. Between `995af4f36` and `13df8b795` nothing changed in `_Decomposition`, `_ScopeChange`, `docs/PRD.md`, `v2` or `PKG-*`, so reusing the baseline is justified. Counts 0/3/70 and 96 rows (70/18/8) confirmed.
- **Reliance-hold preflight.** `candidate-validation` returned `ALLOW` (exit 0) for all six snapshot files. The register has a header and no rows.
- **Strict register validator.** 0 errors, 0 warnings.
- **Packet validator.** `validate_scope_change_packet.py` fails only on missing PKG-00 packet files, as the Handoff says.
- **Action register.** `gen_actions.py` regenerated to a scratch path and `cmp` against the committed CSV is identical. `check_csv.py` reports 54 rows, 9 columns, 0 errors.
- **Counts.** 12 ADD / 42 MODIFY; 31 OTHER / 14 DELIVERABLE / 4 VOCAB_TERM / 3 PACKAGE / 2 OBJECTIVE; the IA cross-tab all confirmed.
- **Option deltas.** The option tags agree with the DQ-b (49), DQ-c (43), ENV-b (52) and BUD-b (54) arithmetic.
- **Revision 1.6 figures.** 100 scope items (74/18/8), 68 deliverables, 29 vocabulary terms (26 now), open issues 10 open / 3 resolved, 46 → 49 PRD requirements. The new IDs appear nowhere in `_Decomposition/`, `PKG-*` or `docs/`.
- **Line spot-checks.** Every one I checked matches at the base:
  - PRD: L5/L7, L74–75, L212, L279–286, §9.6 L345–353, L391–404, L413/L415, L513–516, L563–567.
  - `projects/pec/AGENTS.md`: L26–33, L40–43, L47–50, L180–189, L409.
  - SOFTWARE_DECOMP: L118, L335, L336, L382, L386, L388, L619, L642.
  - Root sources: Root AGENTS L54–55, N-1, K-AUTH-1, `pec.yaml` L81.
  - Every §7.1 SOW locus I sampled: DEL-04-01 L266/290/363/400, DEL-04-02 L225/252/363, DEL-08-01 L55/92/107/108, DEL-08-03 L229/256/257/274/286/321, DEL-04-03 L146/220, DEL-03-04 L248/249/296, DEL-08-04 L266/274/288/290/314, DEL-10-03 L191, DEL-00-03 L70/77, and the NOT_AFFECTED rows.
- **SOW population.** All 32 `ScopeOfWork.md` files are enumerated exactly once: 9 AFFECTED, 23 NOT_AFFECTED. DEL-04-01 is a fixed member. The addendum correction is applied: DEL-01-01 L90, DEL-02-03 L104 and DEL-04-03 L146 cite SOFTWARE_DECOMP §8.
- **Brief compliance.** All items are covered:
  - K-03, §8 with direct query and the access class, §16.6, the §9 envelope and budgets, the §12 gate, the K-02 gloss, and the DEL-04-01 and DEL-00-03 quotations.
  - The PEC-owned versus notice-only split (§7.4, §8.2).
  - How the change stays within D-GOV-01, N-1 and K-AUTH-1 (§8.1).
  - The owner question set: confirm the change set, accept the IA at its SHA, the genuine options, and R-C excluded.
  - Nothing asks the owner about CHECKING.
- **Honesty.**
  - SCA006-G1 is marked as HELP_HUMAN's interpretation, not owner text.
  - Every CP1 row is `AWAITING_OWNER`.
  - Both owner quotations are verbatim against D-PEC-90 L9–11 and D-PEC-94 L7.
  - Operational reliance is kept apart from L-A1, K-AUTH-1 and N-1 (§8.1, §9.4, Seq 38).
  - "Reliance begins at such a release, not now" is stated.
  - Both D-PEC-90 grant-item-2 notices exist (Root `execution/_Coordination/NOTICE_2026-09-25_D-PEC-90_…`; App `projects/chirality-app-dev/execution/_Coordination/NOTICE_…`).

## Findings

**1. MINOR: IA §10 misstates the P1 phase effect.** `Impact_Assessment.md` L451–452 says "P1 gains no mandatory scope". That is false for the recommended set:
- Seq 24/30 add SOW-097 (IN) to DEL-04-03.
- Seq 25/32 add SOW-098 (IN) to DEL-08-03, and DEL-08-03's envelope goes from S to M.
- Both deliverables have PhaseHint P1 in `Deliverables.csv`.

Repair: say that P1 deliverables DEL-04-03 and DEL-08-03 gain the envelope and budget scope. Only the reliance gate (DEL-10-13) is conditional on a release advertising reliance.

**2. MINOR: the GATE-b option deltas are incomplete.** §13.4 (L519–527) and the §7.1 "Under other options" column say only DEL-04-05 becomes AFFECTED. But GATE-b rewrites the §12 P1 exit test (PRD L413), and four more SOWs quote that row verbatim:
- DEL-10-02 L125
- DEL-10-10 L137
- DEL-03-06 L373
- DEL-10-11 L185

The §7.1 rows L277, L279, L280 and the grouped row L283 mark them "same" or tie them only to metric 5. The count of 55 also leaves out a group-S advisory for DEL-04-05's SOW. Since §13 claims the owner "can switch at checkpoint 1 without a re-run", fix the GATE-b population and action count.

**3. MINOR: the EvidenceQuote refresh set is incomplete.**
- `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/Dependencies.csv` row DEP-09-06-004 quotes the DEL-08-03 `Deliverables.csv` Description ("Machine-first response envelope carrying citations.").
- Seq 32 changes that Description.
- IA §7.2 L298, §9.1 L391–392 and CSV Seq 54 name only DEP-09-06-003, DEP-10-03-003 and DEP-10-12-004.

Repair: add DEP-09-06-004 under BUD-a, conditional on the checkpoint-2 wording, and update the "three" counts in §1, §6 and §12.

**4. MINOR: candidate binding SB-1 cites the wrong locator.** IA L409 attributes "If it injects PEC data, verify-before-rely is an interface precondition" to `OD7-G3_APPLICATIONS/D-PEC-67/sections/05_K03-A/ACCEPTED_INPUT.md`. That file (L20–21) reads "If a consumer injects PEC data, verify-before-rely is an interface precondition; it does not require injection." The quoted string exists only in `docs/PRD.md` L212 and its PRD predecessors. Repair: cite the PRD row adopted by D-PEC-67 (or quote the ACCEPTED_INPUT wording), so that checkpoint 2's `Supersession_Delta.csv` gets an exact original value.

**5. MINOR: the IA misdescribes the work graph.**
- IA L285–289 says "The graph's S4 batch (K-03-bound) is DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04 and DEL-04-03", and that the graph lists DEL-01-06 in S4.
- The graph as recorded (`5570fd095`, L55) has S4 = DEL-04-01, DEL-08-04, DEL-01-06.
- The merged graph on `origin/main` (L64) says S4 is "The set that checkpoint 2 fixes" with a candidate list, and moves DEL-01-06 to S2 after G1.

Neither version says what the IA says. Repair: call it the proposed S4 set, and cite the graph revision it is compared against.

**6. MINOR: the package basis is behind `origin/main`.** `origin/main` has moved to `bec8bdd65` (PR #919 and #920 merged). Since the base `13df8b795`:
- D-PEC-94 gained an "Owner confirmation" addendum (new hash; the package pins `eb9793aa…`).
- `_DECISIONS/_REGISTER.md` changed (Handoff L59 pins `031adae3…`).
- The work graph was repaired. Brief L152 records the superseded `5570fd0` bytes `f78484a7…`; `origin/main` has `f669ebe5…`.
- No PRD, `projects/pec/AGENTS.md`, SOW or decomposition file cited by the IA changed.

Repair: rebase or merge `main`, re-verify, and record the drift and its lack of material impact in the Handoff and return. Leave the historical pins labelled as base-commit pins.

**7. MINOR: Annex A overstates what the script validated.** IA L133–134 and L596 present "54/54 PASS" as deterministic validation, and Annex A's Basis column lists line ranges. For about 20 rows `gen_actions.py` (L273–274) emits only "locus by cited line (see Annex B)": those rows PASS on enum and file existence alone. Their loci are backed by Annex B and the child's `verify_quotes.py` (264 checks), not by that script; my spot-checks found them correct. Repair: say which rows the script checks mechanically and which rest on the quote verifier and Annex B.

**8. NOTE: the manager's classification differs from the child inventory's.** The A1 inventory's `SOW_POPULATION.csv` (`5829902f…`) classes 7 SOWs AFFECTED. The IA has 9: it adds DEL-04-03 (scope growth) and DEL-00-03 (review level). IA L83 cites the child file as support without saying the manager overrode it. Disclose the override.

**9. NOTE: the DEL-00-03 rationale is imprecise.** IA L272 grounds DEL-00-03 as AFFECTED on CLM-004 L70 and CLM-006 L77. L70 quotes a `Deliverables.csv` cell SCA-006 does not change, and L77 quotes §1.4 intake posture, which IA §14 (L554–556) keeps as history. Both quotes stay verbatim. The review-level classification holds only through the stale 46-requirement premise; say so.

**10. NOTE: Brief.md claims files the candidate does not yet contain.** Brief.md L120–127 lists the manager return and verifier verdicts under `returns/` as written. They are not in `e2855e552`. Make sure the follow-up commit adds them, or reword.

**11. NOTE: the Runtime notice differs from the graph.** IA §7.4 L323 and §12 L477 recommend a Runtime notice. Graph R4 on `origin/main` sends one "only if the checkpoint-2 plan names one". This is consistent only if checkpoint 2 names it; flag it for the checkpoint-2 plan.

**12. NOTE: a Handoff field value is off-enum.** Handoff L30 sets `DecompositionTruthState = UNCHANGED_REVISION_1_5`, which is outside the contract's enum (`INCOMPLETE`/`COMPLETE`). It follows the SCA-005 checkpoint-1 precedent and is disclosed, so this is acceptable. The Handoff also has no explicit blockers field; the only blocker is owner acceptance, which the "Next owning actor" row already implies.

I modified no repository file and no Git state.

---

## Manager dispositions (B4 WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| 1 | Repaired: IA §10 now says P1 deliverables DEL-04-03 and DEL-08-03 gain scope; only DEL-10-13 is conditional |
| 2 | Repaired: §7.1 rows for DEL-10-02, DEL-10-10, DEL-10-11 and DEL-08-04 carry GATE-b effects; DEL-03-06 split out of the grouped row (12 remain); §13.4 now shows +5 advisories, 60 actions with DQ-a, and 14 AFFECTED. Seq 8 now states that GATE-a adds its own §12 row or paragraph and leaves the P1 row unedited |
| 3 | Repaired: DEP-09-06-004 added to Seq 54 (conditional on BUD-a wording) and to IA §6, §7.2, §9.1 and §12; the counts now say four cells in three registers |
| 4 | Repaired: SB-1 cites the PEC-K-03 row in `docs/PRD.md` L212 (bytes adopted by D-PEC-67) and quotes the ACCEPTED_INPUT L20–21 wording separately |
| 5 | Repaired: §7.1 now presents a "Proposed S4 set" compared against the graph at `bec8bdd65` (`f669ebe5…`), lists the grep candidates found not affected, and notes that DEL-01-06 is in S2 after G1 |
| 6 | Repaired: `origin/main` `bec8bdd65` merged into the branch; IA §2.2, Brief ("Basis commit") and Handoff record the drift (D-PEC-94, `_REGISTER.md`, work graph, STATUS/RUN/review records, Root research files) as not material; base pins stay labelled as base pins |
| 7 | Repaired: IA §3 and Annex A distinguish the rows the script checks mechanically from the 18 rows whose loci rest on Annex B and the quote verifier |
| 8 | Repaired: the override is disclosed in IA §2 and §7.1 |
| 9 | Repaired: the DEL-00-03 row says "review level, premise only" and states that both quotes stay verbatim |
| 10 | Met by the return commit, which adds the return and both verdict files |
| 11 | Repaired: IA §7.4, §8.2 and §12 follow graph R4 (Runtime notice only if checkpoint 2 names one), with the manager recommending that it be named |
| 12 | Accepted as disclosed (SCA-005 precedent); Handoff now has an explicit `Blockers` row |
