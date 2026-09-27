# Verifier verdict 02 — MODE=VERIFY, DEL-10-13 candidate (K2, provisional D-PEC-103)

- **Reviewer:** a fresh read-only `pec-reviewer` TASK (`claude-opus-5-5`, high), dispatched by WORKING_ITEMS. It authored nothing in the packet.
- **Reviewed:** candidate `23f6505e8832cea2212f64c61020fa4ec2f390822f0a9a3baf997285eefff182` at branch commit `3ed3b31aa`.
- **Transcription:** the report below is the reviewer's hand-back message as delivered, with the harness's indentation removed. The manager's dispositions follow it.

## Report

**Verdict: PASS WITH NOTES.** This is the independent MODE=VERIFY of the DEL-10-13 first Scope of Work contract (INIT, NO_STATUS_TOUCH). There are no blocking findings. Four non-blocking findings should be repaired before the packet goes to the owner. One of them is a state claim that is false under its natural reading and that the claims file does not cover.

**What was reviewed**
- Candidate: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/candidates/projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md` (called C below).
  - SHA-256 recomputed: `23f6505e8832cea2212f64c61020fa4ec2f390822f0a9a3baf997285eefff182`, which matches the brief. 252 lines.
  - ID counts: OUT 2, REQ 18, AC 19, VER 18, CLM 16, TBD 7, CON 4, AX 12, REM 0.
- Branch at `3ed3b31aa`. `origin/main` is now `ce99bc256`. Between `125cfacc1` and `origin/main` there are no changes to `_Decomposition`, `docs/PRD.md`, PKG-02/03/04/10, `_DECISIONS`, `_ScopeChange` or root `AGENTS.md`. `125cfacc1` descends from `3ed3b31aa`'s ancestry, and the pin `189f205ff` is an ancestor of `125cfacc1`.
- Read-only was kept. The worktree is clean (`git status --porcelain` shows 0 lines).
- Scratch work was in `.../scratchpad/k2v1013.DeGy/`.
- One slip: a single throwaway comparison file was written to `/tmp/x_<pid>` and deleted in the same command.

**1. Mode-applicable checks.md items**

Run on a `git archive 3ed3b31aa` export of `projects/pec`, `tools`, `workflows` and `docs`, with the candidate copied into place.

| Item | Result | Evidence |
|---|---|---|
| 1 (pilot variance) | PASS | Not needed: INIT of a new deliverable. `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md:187` says "New deliverables use `SOW_V1`". There is no `ScopeOfWork.md` on `125cfacc1` or `origin/main`. |
| 3 (`_STATUS.md` unchanged) | PASS | `_STATUS.md` SHA-256 is `c7a5705d…543b` at `125cfacc1`, `3ed3b31aa` and `origin/main`. State is `OPEN`. |
| 4 (validates) | PASS | `validate_scope_of_work.py` → `PASS format=SOW_V1`, exit 0. |
| 8 (OUT maps to scope/objective) | PASS | Both OUT rows carry `SOW-100 OBJ-001`. |
| 9 (AC maps to VER or review) | PASS | AC-001..018 each have one VER. AC-019 is HUMAN_REVIEW. |
| 13 (checklist content) | PASS | `derive_review_checklist.py`: 19 items, in source order, bound to the contract hash, matrix-linked VER. |
| 18 (repeatable, fails closed) | PASS | Two derivations are byte-identical (`b0b56b38…c8be`). Negative tests: a broken matrix gave `INVALID`, exit 1, no output; a dual-format folder gave `AMBIGUOUS`, exit 1, no output. |
| 19 (no bare upstream IDs) | PASS | The only ID-shaped tokens not defined locally are project IDs (SOW, OBJ, SCA, SHA-256). There are no qualified or bare upstream local IDs and no local ID of the sibling K2 deliverable. |
| 20 (matrix grouping) | PASS | One AC per row. |
| 21 (boundary owners) | PASS with note | See below. |
| 16 (finding classes) | Done | Findings below are classed as project-content unless stated. There are no schema findings; the substrate findings are listed. |

Item 21 detail:
- `check_boundary_owner_resolution.py --show-not-checkable`: 1 requirement checked, 0 NOT_CHECKABLE, 0 findings, exit 0.
- Hand check, requirement → excluded act → owner → claim:
  - **REQ-015** (C:151): all resolve in CLM-009 (C:114). That covers `DEL-03-04`, `DEL-04-05`, `DEL-04-03`, `DEL-10-02`, `DEL-02-01`..`09` (including the `DEL-02-07` reader), `DEL-10-11` and `DEL-08-06`.
  - **REQ-013** (C:149): release, tag, publish, advertise and pipeline acts go to the human owner. This is by interpretation and cited to CLM-010 and CON-004.
  - **REQ-016** (C:152): the C-08 classification goes to the owner (CLM-012, CON-001). Register amendment goes to an owner-ruled packet (CON-002). Lifecycle stays under `_STATUS.md` (CLM-016).
  - **REQ-017** (C:153): governed files are excluded via the PKG-10 exclusion in CLM-009 and PEC-K-06.
  - **REQ-002** (C:138): recording or explaining a disposition goes to TBD-005.
  - **Gap:** REQ-003's "author no seed" names no owner. See finding N2.

**2. Prep verifiers (reruns)**

| Verifier | Result | Exit |
|---|---|---|
| `verify_k2_quotes.py --tree <export> --gitdir <worktree> --prep <prep> --observation 125cfacc1 --only DEL-10-13` | `RESULT PASS 72/72` (70 quotes + FORBID + OBS; 0 dependency rows cite this contract) | 0 |
| `verify_k2_state_claims.py --only DEL-10-13` | `RESULT PASS 332/332` | 0 |
| `check_cited_ids.py --commit 125cfacc1` | `RESULT PASS 0/0` (the contract makes no qualified citations) | 0 |
| `scan_old_s2_text.py --prior ce934ac33 --current 125cfacc1` | `RESULT PASS stale=0 current=43` | 0 |

The verifiers are sound on both sides. I tested this on a copy of the prep folder:
- Changing the candidate side of Q02 gave FAIL "candidate=NO".
- Replacing Q05 with candidate-only text gave FAIL "source=NO".
- Changing a hash prefix (S252) and a count (S236) gave "git=NO". Changing the `candidate_text` of S35 gave "candidate=NO".

Limits of the verifiers (both check only what is listed):
- The quotes check covers only listed quotes. My own scan of quoted spans found one quotation that is not strictly verbatim (NOTE n1). The four dependency TargetName strings are unlisted as quotes but are covered by csv_cell claims.
- The claims check confirms that `candidate_text` is present in the candidate, not that the sentence says what the claim proves. That is how N1 got past it.

**3. Semantics**

These hold:
- Every quotation checked verbatim at `125cfacc1`. CLM-001's "reads in full" is exact: 576 characters, byte-equal to the `SOW-100` row. The PRD §12 paragraph and the PEC-ORI-007 blockquote are complete.
- The objective attribution is no stronger than the sources. `SOFTWARE_DECOMP.md` §3 lines 341–343 and the OBJ-001 row at line 347 list "instruments: SOW-058, SOW-059, SOW-063, SOW-100". The DL-21 wording is accurate. The contract's statement is C:43–55 and AC-019.
- The C-08 question is recorded as "not made at `125cfacc1`" (C:117, C:176, C:223). No requirement, criterion or verification refers to blocker arithmetic, successors or `_DEPENDENCIES.md` content.
- The `DEL-02-07` edge is recorded and not resolved (C:118, C:177). The C:118 wording matches D-PEC-101 finding 2.
- Release and advertisement acts stay outside the deliverable (REQ-012, REQ-013, CON-004, AX-005).
- CON-004's reading of Root `AGENTS.md` is labelled "an interpretation, not a ruling" (C:115) and is reasonable. It is supported by `projects/pec/AGENTS.md:382`: Git closeout "is not … release readiness".
- The gate composes evidence and discharges nothing (REQ-007, REQ-015, AX-002).
- The four contracts under revision in parallel (DEL-03-04, 04-03, 04-05, 10-02) are cited only as observations with hash prefixes, and CON-003 routes around their wording.
- There is no `## Remaining` section and no REM ID. There is no readiness, CHECKING, ISSUED or acceptance claim. The contract is lifecycle-neutral.

**NON-BLOCKING findings**

- **N1 (project content; state claim).** C:40–41 says "At `125cfacc1` the deliverable-local `_CONTEXT.md` and `_REFERENCES.md` name revision 1.6 and PRD v2.4."
  - `_CONTEXT.md` at `125cfacc1` names revision 1.6 but never PRD v2.4. Only `_REFERENCES.md:6` does.
  - The claims only check `_CONTEXT` for rev 1.6 (S20) and `_REFERENCES` for both (S21, S22).
  - Repair: write "`_CONTEXT.md` names revision 1.6, and `_REFERENCES.md` names revision 1.6 and PRD v2.4".

- **N2 (project content; boundary owner and a small decision by assumption).**
  - REQ-003 (C:139) "The harness shall author no seed", AC-003 "the harness contains no seeding path" (C:158) and VER-003 (C:198) bar the gate from seeding. The exclusion names no owner and no TBD.
  - The sources leave this open. `SOW-100` has the gate "prove … complete coverage statements under seeded feed failures". The `DEL-04-05` row (`Deliverables.csv`) says nothing about seeding.
  - TBD-003 (C:125) also lets the harness invoke producing mechanisms "against the candidate", which for coverage would need seeded inputs from someone.
  - Repair, either:
    - name the owner (for example `DEL-04-05`, per the register's "DEL-04-05 coverage honesty under seeded feed failures", cited to CLM-005 or CLM-009); or
    - widen TBD-006 to cover who produces seeded-feed evidence, and drop the flat prohibition, or tie it to that TBD.

- **N3 (project content; scope precision).**
  - PEC-ORI-007 (PRD line 331) requires the file-fallback signal only "whenever PEC is absent, degraded or failing its own checks". REQ-004 (C:140) carries that condition in its list.
  - AC-004 (C:159) "all four envelope elements on each covered response" and VER-004 (C:199) "one response lacks each element in turn … fail in every other case" drop the condition. Read literally, a healthy response without the fallback signal would fail, which goes beyond PEC-ORI-007.
  - Repair: make the fourth element conditional in AC-004 and VER-004, for example by removing the signal from a degraded-state response. Optionally require the evidence to include a degraded or absent case.

- **N4 (project content; quotation excerpt).**
  - CLM-012 (C:117) says "the `D-PEC-62` ruling confirmed 'the C-08 standing-node exclusion from one-shot blocker arithmetic'". The full ruling clause (D-PEC-62 lines 212–215) is "the flags-as-flags reading of ruling 4 is confirmed, including the C-08 standing-node exclusion …". D-PEC-62 §1(4) (lines 27–31) says that reading leaves the "C-08 standing-node set" among the recorded-but-unresolved, non-gating annotations.
  - The `DEL-10-02` contract at `125cfacc1` (CON-001, line 295) reads the C-08 force as unconfirmed. D-PEC-101 finding 4 and the D-PEC-62 Status line read it as owner-confirmed.
  - The excerpt picks one reading of a disputed record. Nothing depends on it, because the contract is neutral on C-08.
  - Repair: quote the full clause, or add one sentence noting that the `DEL-10-02` contract reads it differently.

**NOTEs**
- **n1.** AX-004 (C:220) puts "Re-proved at each such release" in quotation marks with a capital R. The source (`Deliverables.csv`) has lower case. It also cites CLM-002, but the PRD wording is "each release that advertises"; the "such" wording is the register's. Lower-case it and cite CLM-005 alone.
- **n2.** REQ-003 turns the PRD's "complete coverage statements" into "explicit statement of the measurement limitation … none silently omitted". That is defensible via PEC-ORI-006, but consider keeping the word "complete" verbatim.
- **n3.** REQ-005 and AC-005 make this deliverable's `Dependencies.csv` rows (which AX-008 calls "provenance, not authority") the working list of suites, read "at evaluation time", at an unstated commit. It is consistent with D-PEC-101 finding 2 treating inclusion as an edge amendment. Consider stating which commit's register is read.
- **n4.** REQ-008 (C:144) "A gate record shall bind one candidate only" sits awkwardly with REQ-013 (C:149), which requires a not-evaluated record for an invocation that lacks a candidate. Consider "at most one".
- **n5.** VER-010 (C:205) "review every field's type for capacity to hold … prose" conflicts with the reason field that REQ-009 and REQ-010 require. Consider limiting it to prose copied from evidence.
- **n6.** AX-008 (C:224) "makes the upstream *contracts* the reliable inputs" reads against CON-003's choice not to rely on their wording. Consider "the available inputs".
- **n7 (cosmetic).** C:191 is an overlong unwrapped line. There is no trailing whitespace, no tab, and the final newline is present.

**4. Add-on C8 (and add-on S)**

- **C8.** The postimage (`609aa807…3693`) adds one bullet under "Dependency Tracking Mode". Nothing in the contract becomes false whether C8 is applied or not:
  - The statements about C-08 and `_DEPENDENCIES.md` are anchored at `125cfacc1`: CLM-012 "carries no such section at `125cfacc1`", "not made at `125cfacc1`" (C:117, 176, 223), and CLM-006's declared-section quotes.
  - CON-001 says the owner records it "through its own instrument", which is true under D-PEC-103.
  - No requirement, criterion or verification method depends on the classification.
  - The quoted Run Notes line ("… that `D-PEC-101` does not make") stays true.
  - Informational, about the add-on and not the contract: the `DEL-10-02` and `DEL-03-04` precedent is a separate `## Standing obligation (constraint C-08)` section plus a C-08 rule line in Run Notes. C8 uses an inline bullet instead, and D-PEC-101 finding 7 refers to "the C-08 section".
- **Add-on S** (`_STATUS.md` OPEN → INITIALIZED). The contract also stays true, because CLM-016 and AX-012 are observations at `125cfacc1` and AX-012 speaks only of "the run that authored this document".

**Hashes relied on**

| File | SHA-256 |
|---|---|
| `quotes/DEL-10-13.json` | `dc3c3861…a2d1` |
| `claims/DEL-10-13.json` | `6bb391c8…28cc` |
| `verify_k2_quotes.py` | `50343b9f…4642` |
| `verify_k2_state_claims.py` | `8c7146f2…5b29` |
| `check_cited_ids.py` | `0389f1dc…6335` |
| `scan_old_s2_text.py` | `b4043dfb…78a` |
| `K2_DRAFTER_BRIEF.md` | `aefa51fa…aa40` |
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4…c2b` |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ac…188` |
| Derived checklist | `b0b56b38…c8be` |

Pin facts S02–S11 recomputed and matching: `SOFTWARE_DECOMP.md` `9374c21f…8eb1`, `Deliverables.csv` `94ee5d18…9805`, `ScopeLedger.csv` `1d24a4b8…916e`, `ContextBudgetQA.csv` `93b0bb07…4c7c`, `docs/PRD.md` `ae49b806…3fbe`.

## Dispositions (WORKING_ITEMS)

Pending. Repairs are routed to the DEL-10-13 drafter, followed by a backcheck; this section is completed after the backcheck.
