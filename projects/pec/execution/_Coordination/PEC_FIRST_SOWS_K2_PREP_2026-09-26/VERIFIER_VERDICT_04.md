# Verifier verdict 04 — backcheck of the repair round (K2, provisional D-PEC-103)

- **Reviewer:** a fresh read-only `pec-reviewer` TASK (`claude-opus-5-5`, high), dispatched by WORKING_ITEMS. It authored nothing in the packet and wrote none of verdicts 01–03.
- **Reviewed:** branch `claude/pec-k2-first-sows-proposal` at `196074cdf` (candidates `120b61c0…632d` and `02fc0c16…3a1d`).
- **Transcription:** the report below is the reviewer's hand-back message as delivered, with the harness's indentation removed. The manager's dispositions follow it.

## Report

**Verdict 04 (backcheck of the K2 / provisional D-PEC-103 repairs): PASS WITH NOTES.**

Nothing blocks. B-1 is fully repaired. Four NON-BLOCKING items remain, and three of them are one-line text fixes. Two of those three change candidate bytes, so both candidates would need rehashing and rebinding. The fourth is `SHA256SUMS`, which still has to be generated before publication.

I reviewed branch `claude/pec-k2-first-sows-proposal` at `196074cdf` in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep`. `origin/main` after fetch is `e548d4cfa`, an ancestor of HEAD. I authored nothing and modified nothing: the worktree is clean. My scratch directory `k2bc04.1cilZH` was created with `mktemp -d` and has been deleted. The reliance-hold preflight (`candidate-validation`) gave `ALLOW` on both targets.

## What I verified

**Hashes (all recomputed with `shasum -a 256`, all match the draft)**
- Candidates: `120b61c0…632d` (249 lines) and `02fc0c16…3a1d` (253 lines).
- Scripts: `apply_k2.py` `7d99f3ff…563d`, `apply_k2_c8.py` `3fd1e53b…23d4`, `test_apply_k2.py` `4594c8bb…3df7`, `check_cited_ids.py` `70dfdc62…71c5`, `run_k2_checks.sh` `6e1276e6…d58c`. The quotes, claims and old-S2 verifiers are unchanged.
- Other files: the brief `5fcc3ef8…e133`, both S postimages, and the C8 postimage `609aa807…5693`.
- The tools, the workflow, `checks.md`, the standard, the holds file and the preflight script all match at `origin/main`.
- The ID counts in the draft (draft:89) match both candidates.

**Script bindings**
- `apply_k2.py` `TARGETS` holds exactly the two repaired hashes, matching the draft's grant table (draft:207–208) and draft:93.
- `apply_k2_c8.py` pins DEL-10-13 at `02fc0c16…`.

**Full runner, rerun by me:** `TMPDIR=<mine> zsh run_k2_checks.sh <wt> 196074cdf… <prep> <mine>/out 125cfacc1` gave **OVERALL PASS, exit 0**.
- Quotes 137/137, state claims 482/482, cited IDs 0/0, old S2 text stale=0 (43 current), fault injection 19/19.
- Checklists `a8e63dc9…d34f` (17 items = 17 AC) and `e3d43d16…9107` (19 = 19).
- Strict registers: exit 1, 0 errors, 26 `XRG-013` warnings, identical before A, after A and after C8.
- Every committed file under `evidence/run_main/` matches my rerun after normalising temp paths. The only differences are the basis-commit line of `SUMMARY.out` and one temp path in `test_apply_k2.out`.

**Independent tool run:** I made my own `git archive` export with both candidates copied into place.
- `validate_scope_of_work.py` gives `PASS format=SOW_V1` for both.
- `derive_review_checklist.py`, run twice, is byte-identical and gives the hashes above.
- `check_boundary_owner_resolution.py --show-not-checkable`: 1 checked, 0 NOT_CHECKABLE, 0 failing, exit 0 for each.

**Pins and containment**
- All 17 pins hold at `origin/main` `e548d4cfa`, at HEAD and at `125cfacc1`. At `189f205ff` the five decomposition/PRD files and `pec.yaml` are equal.
- Both targets are absent at `origin/main` and at HEAD. The register's last row is still D-PEC-101, and no D-PEC-102–104 file exists on `origin/main`.
- `git diff --name-status origin/main...HEAD` shows only the prep folder plus `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2P_FIRST_SOWS_PROPOSAL.md`. No production file is touched.
- The draft's change lists for `125cfacc1..947075c9a` and `947075c9a..e548d4cfa` (draft:42–43) are exact.

**Dispositions true in the bytes**
- **B-1: gone.**
  - "File-fallback signal and no claim" now applies only where no API response exists: REQ-005 L149, AC-005 L166, VER-005 L200.
  - Any API response, including a degraded or check-failing one, passes through unchanged, and the text states the surface "shall neither strip claims from it nor add a signal of its own".
  - REQ-002, AC-002 and AX-005 are now consistent with it, and no text requires stripping claims.
- **NB-1, NB-2 (quote Q60, claim S139; `pec.yaml` L82 is under `human_gates`), N-1, N-2, N-3 (Q61 verbatim from PRD L230) and N-5:** done.
- **NB-3:** incomplete (see NB-A below).
- **DEL-10-13 N1, N3, N4 and n1–n7:** done.
  - N1: S334 confirms `_CONTEXT.md` at `125cfacc1` has no "v2.4".
  - N4: Q71 matches the DEL-10-02 contract L295 verbatim, and Q48 matches the full D-PEC-62 L214–215 clause.
- **N2:** decides nothing about who seeds in REQ-003, AC-003, VER-003 and TBD-006, but see NB-B below.
- **REQ-004's extra sentence** (at least one absent, degraded or failing case) stays within PEC-ORI-007: it only exercises ORI-007's own conditional element.
- **Verdict 03 items:**
  - The draft now quotes SPEC §5.1 exactly (SPEC.md:448, :460).
  - The runner assertions (N3), the fault cases a12 and c5–c7 (N4), the S1 labels (N5), the notice hash (N6), the `e548d4cfa` recheck (N7) and the ordering sentence at draft:284 (N8) are all present.

**Open matters still open**
- OI-006, K3, C-08 and the DEL-02-07 edge remain undecided.
- Both contracts are true with or without add-ons S and C8, because every state claim is anchored to `125cfacc1`.
- CHECKING appears only in the Limits section (draft:415); nothing prompts about it.

## NON-BLOCKING

**NB-A. The NB-3 repair missed one place, and its disposition is untrue in the bytes.**
- Evidence: DEL-08-06 candidate L182 (CON-003) still says "REQ-001 declares a tool only for a kind the API serves".
- This is the authoring sense of "declare" that NB-3 removed from REQ-001. It also sits against L21 ("without declaring or invoking any tool") and against CON-002's open question.
- The disposition at `VERIFIER_VERDICT_01.md:148` says "'declare' remains only for fields inside a definition and in the tier-0 sense", which this line contradicts.
- Repair: change it to "REQ-001 admits a tool definition only for a kind the API serves". Then rehash, rebind `apply_k2.py` `TARGETS`, update draft:93 and draft:207, and rerun.

**NB-B. N2 is only partly neutral: REQ-017 closes off one branch of TBD-006 that REQ-003 leaves open.**
- Evidence: DEL-10-13 REQ-003 L139, AC-003 L158 and VER-003 L199 let the harness seed feeds if TBD-006 (L128), once fixed, assigns seeding to this deliverable.
- But REQ-017 L153 ("shall write only its own gate records"), AC-017 L172 ("its only writes are gate records") and VER-017 L213 forbid writing any seeded inputs.
- So the contract text still decides that this deliverable cannot seed by writing feeds.
- Repair, either:
  - add to REQ-017, AC-017 and VER-017 "and, only where TBD-006 as fixed assigns seeding to this deliverable, the seeded inputs it names, outside governed files"; or
  - state in TBD-006 that such an assignment would need a revision of this contract.

**NB-C. The draft's QA 21 table still uses the owner phrase that NB-2 removed.**
- Evidence: draft:348 gives "advertising reliance: the human release act after the §12 gate".
- This table is the hand record that verdict 01's N-6 disposition relies on.
- Repair: "the separate owner act after the §12 gate (the `pec.yaml` human gate, CLM-013)".

**NB-D. `SHA256SUMS` does not exist yet.**
- Evidence: the file is absent at `196074cdf`, while draft:490 says "hashes in `SHA256SUMS`". Verdict 03's NB-1 disposition ("repaired at publication") is therefore still pending.
- Repair: generate it over the tracked prep files at the final head before the PR and return, or reword draft:490 until then.

## NOTES

1. **DEL-08-06 REQ-005 L149 cites the wrong TBD.** It names TBD-006 as the home of "what such a response signals", but TBD-006 (L136) covers only how the signal is represented when there is no response. Cite CON-004 alone, or widen TBD-006.
2. **Is a refusal an "API response"?** REQ-005 L149, REQ-008 L152, AC-008 L169 and VER-005 L200 leave it implicit whether an access-class refusal that the service sends back counts as "no API response to the query". The pass-through branch says to add no signal of its own; the refusal branch requires one. Add a clause such as "a refusal is not an API response to the query".
3. **DEL-08-06 CLM-012 L110 states an interpretation as fact.** It says the advertisement decision falls under `pec.yaml`'s "release" gate ("the release gate the tier-0 profile keeps"). DEL-10-13 CLM-010 L115 labels the parallel reading "an interpretation, not a ruling". Label the DEL-08-06 reading the same way, for consistency.
4. **DEL-10-13 matrix row L238 is stale.** Its evidence expectation does not list the new VER-004 cases: a degraded response missing the signal, and evidence with no absent, degraded or failing case.
5. **DEL-10-13 TBD-007 L129 vs REQ-004 L140.** TBD-007 says no accepted source fixes the extent of evidence, but REQ-004 now sets a minimum. Suggest adding "beyond the minimum REQ-004 sets".
6. **DEL-10-13 AC-018 L173 and VER-018 L214 require an "executing test" for every VER**, including VER-010's "review every field's type" (L206). This is the same inconsistency that was repaired in DEL-08-06 as N-1 (AC-016 "executing test or review record"). Align the two contracts.
7. **DEL-10-13 REQ-010 L146 and VER-010 L206:** "no field … can hold … prose copied from the evidence" cannot be guaranteed for the free-text reason field that REQ-009 and REQ-010 require. Suggest enumerated reasons, or dropping "can".
8. **Draft:140 is stale:** it still says "at evaluation time", while the repaired REQ-005 says "at the commit of the candidate under evaluation".
9. **Draft:188 vs draft:284:** "Add-ons S, M and C8 are independent of one another" sits against the ordering at draft:284 (C8 after A, not concurrent with S). Suggest "independently selectable".
10. **Draft:373–374 overstates:** "all repaired by the author" is not true of verdict 01's N-4, N-6 and N-7, which were recorded, not repaired. Suggest "actionable findings repaired; N-4, N-6, N-7 recorded".
11. **`VERIFIER_VERDICT_02.md:143` names the wrong quote:** it says "Q46 text replaced in place", but the change in `quotes/DEL-10-13.json` is to Q48. Correct it to Q48.
12. **Confirmation for draft:3:** it observes the register at `947075c9a`; the statement also holds at `e548d4cfa`, and the draft could say so.

## Relevant paths
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/DRAFT_D-PEC-103_first_sows_del_08_06_10_13_proposal.md`
- `…/PEC_FIRST_SOWS_K2_PREP_2026-09-26/candidates/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md`
- `…/PEC_FIRST_SOWS_K2_PREP_2026-09-26/candidates/projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md`
- `…/PEC_FIRST_SOWS_K2_PREP_2026-09-26/VERIFIER_VERDICT_01.md`, `VERIFIER_VERDICT_02.md`, `apply_k2.py`, `apply_k2_c8.py`, `run_k2_checks.sh`, `test_apply_k2.py`

## Dispositions (WORKING_ITEMS)

Nothing blocks. WORKING_ITEMS made the wording repairs below itself: exact one-phrase replacements, each asserted to occur once, disclosed in the proposal and backchecked in verdict 05. The candidates are now DEL-08-06 `aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826` (249 lines) and DEL-10-13 `c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633` (253 lines); both act scripts are rebound. The quote and claim files are unchanged: quotes 137/137, claims 482/482, cited IDs 0/0 and old-S2 stale=0 rerun clean.

| Finding | Disposition |
|---|---|
| NB-A | **Repaired.** DEL-08-06 CON-003: "REQ-001 admits a tool definition only for a kind the API serves." |
| NB-B | **Repaired** (second option). DEL-10-13 TBD-006 adds: "An assignment of seeding to this deliverable would need a revision of this contract, because REQ-017 limits its writes to its own gate records." REQ-017 is unchanged. |
| NB-C | **Repaired** in the draft's QA 21 table. |
| NB-D | **Repaired.** `SHA256SUMS` is generated over the tracked prep files at the final head. |
| Note 1 | **Repaired.** DEL-08-06 REQ-005 cites CON-004 alone. |
| Note 2 | **Repaired.** DEL-08-06 REQ-005: "(a refusal the service returns is not an API response to the query)". |
| Note 3 | **Repaired.** DEL-08-06 CLM-012 labels the release-gate reading "as an interpretation and not a ruling". |
| Note 4 | **Repaired.** DEL-10-13 matrix row for AC-004 lists the degraded-without-signal and no-degraded-case evidence. |
| Note 5 | **Repaired.** DEL-10-13 TBD-007: "beyond the minimum REQ-004 sets". |
| Note 6 | **Repaired.** DEL-10-13 AC-018 and VER-018: "executing test or review record". |
| Note 7 | Recorded, not changed: the reason field is the harness's own statement, and whether reasons are enumerated is a production choice within REQ-009/REQ-010; VER-010 checks for prose copied from evidence. |
| Notes 8–10, 12 | **Repaired** in the draft. |
| Note 11 | **Repaired.** Verdict 02's disposition now says Q48. |
