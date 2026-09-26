# Review 01 of PR #928 (D-PEC-96 proposal; D-PEC-78 §4.3 REVIEW), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `57db67a0ebc984d3723d026dac5cb13711c634b0`.
- **SHA-256 of the report text below (UTF-8):** `69edbbb34097129faabf781a906e8bba9620c24dd78c88e393cfa556d89683cf`.

## Report (verbatim)

## Review of PR #928 (D-PEC-96 registry schema v2 proposal) at head 57db67a0e

**Verdict: FAIL, on one small blocking finding in the work graph.**

The D-PEC-96 package itself passes the REVIEW that D-PEC-78 §4.3 requires. That covers the proposal, `apply_d96.py`, the postimages, the tests and the evidence. Every pinned hash and every claimed check result reproduced exactly. The only blocking defect is one stale graph state cell, which HELP_HUMAN wrote in the same PR. Fixing it takes one cell edit.

Basis:
- Head confirmed with `gh pr view 928`: `57db67a0ebc984d3723d026dac5cb13711c634b0`. PR is OPEN with 36 files.
- Base is `origin/main` `4d5f7b91102b…`.
- All reading was done from `git archive` exports in my scratchpad. The checkout was not modified.
- The PEC reliance-hold preflight (`candidate-validation`) returned ALLOW for the proposal and the registry targets. The holds register has no rows.

### Blocking

**B1. The R2 node's state is untrue.**
- **Where:** `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md:58`.
- **What:** R2's State cell still reads "READY — … a WORKING_ITEMS manager is dispatched after this graph update".
- **Why it is wrong:** the same PR's Order (line 76) says "Active: G1 … and R2". Line 112 records the R2 manager as running under brief B5 (`142d6be0…efb4`) on branch `claude/pec-sca006-cp2-package`, and that branch exists locally. The State column is the node's canonical state, so the graph now contradicts itself. The brief asked me to confirm the graph states are truthful.
- **Fix:** change R2 to `ACTIVE`, citing brief B5 and the returns path `returns/B5_*`.

### Non-blocking, ranked

1. **(Medium) PEC's actual shape cannot be expressed in the four-profile vocabulary, and the owner should be told.**
   - `projects/pec/AGENTS.md:241-248` keeps the 57 `## Remaining` sections as maintained records of open scope. "A Remaining item's own gate markers still bind that item", and items are updated under packets.
   - Under option A, no profile reads them. Proposal line 43 calls this only a consequence and says reading them would need an amendment.
   - `remaining-loop` cannot be added beside `shared-dev-loop` either, because it declares the ledger (S14) live.
   - **Suggest:** put this into owner question 2 or 3 explicitly. The owner should confirm that parked gate markers in the Remaining sections becoming invisible to PEC is acceptable.
2. **(Medium) Profiles that overlap or contradict each other are accepted, and this is not disclosed.**
   - The uniqueness rule is per profile ID, not per covered surface. I confirmed on the applied option-A tree that the adapter accepts both of these rows:
     - `remaining-loop` live plus `loop-receipts-ledger` historical, which declares S14 both live and historical;
     - `remaining-loop` plus `shared-dev-loop`, both live, which cover S6, S8 and S9 twice.
   - It also accepts a row whose profiles are all `historical` (no live profile).
   - **Suggest:** either add a disjointness rule and an at-least-one-live rule, or state in question 3 that parser deliverables resolve overlaps.
3. **(Low–Medium) The `agentruns-json` coverage text is narrower than PRD v2.3.**
   - The schema description (proposal line 110) pins the profile to `execution/_Coordination/AgentRuns/`.
   - PRD v2.3 §7.1 RunRecord reads `STATUS.json` and `RUNTIME_SUMMARY.json` "under `execution/**`".
   - PEC's only `WORK_GRAPH.json` is `execution/PKG-01_…/DEL-01-03_…/_run_records/P1_STORE_GUARD_01/WORK_GRAPH.json`. That is outside the pinned path, and it is not covered by PEC's row under A or A-R.
   - The design note's FX-PEC-0 includes that file.
   - The owner confirms this coverage text under question 3, so it should be aligned or disclosed.
4. **(Low) The quote of §B6 is truncated.**
   - Proposal line 14 stops before §B6's last sentence: "D-PEC-86 I-7 (PEC's own migration) stays deferred; migration later is one owner-gated row change (Q8)."
   - The premise-lapse argument still holds. CP3 was recorded at `c9e5cd87d` (2026-09-25 14:56) and D-PEC-94 at `a7d1f1fe2` (18:49), and D-PEC-94 exercised I-7.
   - Option A still departs from the letter of the CP2-accepted §B6 and of SCA005-CP1-Q8 (a). Owner question 2 should say that in one sentence.
5. **(Low) The register row understates the grant.**
   - `_REGISTER.md:113` says "Opens exactly 11 `projects/pec/v2/**` paths".
   - It omits the fenced administrative paths the proposal also grants: the run root `DEL-01-06/_run_records/D-PEC-96_REGISTRY_V2/**` and the optional `MEMORY.md`.
6. **(Low) The containment check is worded too tightly.**
   - Proposal line 422 requires exactly the 11 paths, plus the run root and optional `MEMORY.md`, and "nothing else".
   - The D-PEC-95 act PR also carried HELP_HUMAN's register row and return (graph U1 row). The check should say whether such records ride in the act PR or in a separate one.
7. **(Low) The HOLD is cited from the wrong file.**
   - Proposal line 59 cites `_STATUS.md` (`20e6db02…`) for the Gate 5 HOLD and its phrase "does not accept the produced artifacts".
   - `_STATUS.md` contains no HOLD text. Both the HOLD and the phrase are in DEL-01-06 `_REVIEW.md:45-48`.
8. **(Low) Test and schema nits.**
   - No test covers the claim that "No failure message echoes a document value". Key names are echoed, as they were in v1, and the proposal discloses this.
   - No test covers a non-string `state` or `profile`. My probes show both are rejected correctly anyway.
   - The schema `$id` is the same in v1 and v2.
   - The per-row profile uniqueness and the `basis` path rule are stated only in prose. JSON Schema cannot express keyed uniqueness, so this is acceptable.
9. **(Info) Adding profiles within schema v2 is disclosed.** Treating a new profile or version as a change "within schema v2" widens the accepted value set without a version bump. That sits close to D-PEC-78 §4.2's "not silently widened", but question 3 discloses it and offers the alternative.

### Answers to the brief's questions

**Premises**
- The PEC-row migration premise is correct. Q8 (a)'s reason, quoted in the resolution note, rests on I-7 deferral and Remaining-based selection. D-PEC-94 ended both after CP3.
- Asking it as a separate owner question is right: SOW-094's Notes and Q8 (a) both require "its own ruling".
- "No scope change needed" is sound for the scope statements. SOW-077/094 fix no profile, and PRD v2.3 §16.3 names none. The departure is from Notes, plan and decision text, which is item 4 above.
- The four-profile vocabulary comes from accepted text: the `SOFTWARE_DECOMP.md:630` term ("e.g.") and the design note's "Example profiles". Closing it is new, and the proposal discloses that honestly (finding 2, question 3).

**Design**
- Rejecting version 1 is justified. Reading v1 would require defaulting a profile, which AC-003 and REQ-003 forbid ("silently defaulted"). D-PEC-78 allows dual reading only "if needed", and nothing needs it: there is no consumer and no store.
- The core stays stdlib-only. `software-workflow.json` and `service_core_posture.json` are unchanged, and the selector picks all five checks.
- I read all 11 postimages in full, plus the A-R overrides. The port postimage equals the tabled block, and the three JSON blocks in the proposal equal the written bytes.

**Reproduction**

The scratch repo was an export of `4d5f7b911` with alternates, `read-tree` and `update-ref`. Python 3.13.7, `PYTHONDONTWRITEBYTECODE=1`.

| Run | Result |
|---|---|
| `--check-only` | exit 0, 11 RENDER |
| Act, option A | exit 0. Report byte-equal to `evidence/actA.report.txt`. All 11 files byte-equal to `postimages/optionA_v2/**`. Diff equal to `optionA_vs_abfd0897b.diff` apart from hunk order and index-hash length |
| Checks before → after | api 6 OK → 6 OK; registry 12 → **16 OK**; store 13 → 13 OK; enforcement 28 → 28 OK; posture PASS both times, core tree `88f590c0…c016` → `dd7e1dda…6e5a`, config and workflow hashes unchanged |
| `harness-self-check` | exit 0, stdout `e5f9ff70…d110` both before and after (also identical at the PR head) |
| Rerun on the applied tree | exit 1, preimage mismatch, tree unchanged |
| Drift | must-remain drift, preimage drift and an existing create-target each exit 1 with nothing written |
| A-R | exit 0; report equals `actAR.report.txt`; differs from A in exactly `loops.json` and the test file, both equal to the overrides; registry 16 OK; other checks pass |
| `mutate_d96.py` | exit 0, output byte-equal to `evidence/mutate_d96.out`, 13/13 caught |
| Basis and `loop_init_path` | all exist |
| Non-ASCII scan | 0 bytes |

**Grant, rollback and limits**
- The 11 preimages and 6 must-remain hashes match `4d5f7b911`. Nothing under `v2/**` changed after `abfd0897b`.
- The path-list hash `b5db12e5…c73c` recomputes.
- The only other code importing the registry is inside the grant.
- The run root under `_run_records/` is appropriate: it is a fenced path, granted explicitly, following the D-PEC-75/77 precedent.
- The MEMORY question follows `projects/pec/AGENTS.md`.
- Nothing grants a lifecycle, SOW, PRD or decomposition change, and nothing prompts about CHECKING.

**Publication fidelity**
- The proposal hashes to `f4861119…7d87` (587 lines), equal to `D-PEC-96_DRAFT.md` in `SHA256SUMS`.
- `shasum -c` passes for all 28 other entries.
- `.gitattributes` is the only unlisted file besides `SHA256SUMS` itself.
- The return's report hash `1ea79afc…fcc9` matches the text after "## Report (verbatim)" with the final newline stripped.
- The G1 brief hashes to `084eadd8…fca1`; B5 hashes to `142d6be0…efb4`.
- The basis table checks out: all 39 hashes match at `abfd0897b`, and only the register and graph have changed since.

**Register, graph and STATUS**
- The register row has 6 columns and its hashes are right; see finding 5.
- The graph is acyclic.
- The G1 row is truthful. The R2 row is not (B1).
- The PR #926 completed-row verdicts (FAIL, FAIL, PASS) match the transcriptions.
- The STATUS line is true.
- The D-PEC-88 trace is complete: STATUS is the only STATUS/README change, and README is untouched.

**Hygiene**
- `git diff --check 4d5f7b911...57db67a0e`: clean.
- `validate_pec_loop_receipts.py`: VALID, exit 0.
- `validate_decomposition_registers.py --strict projects/pec/execution`: 0 errors and 0 warnings.

### Files
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- Scratch reproduction trees: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/rev.jtpN/`
  - `actA/`, `actAR/`, `drift/`, `head/`
  - `posture_*.json`, `harness2_*.txt`, `mut.out`

## HELP_HUMAN disposition

The verdict is FAIL, on the one blocking finding, B1, in HELP_HUMAN's own graph text.

- **B1** is repaired: R2 is now ACTIVE, with brief B5 and its returns path.
- **Finding 5** is repaired: the register row now names the run root and the optional `MEMORY.md`.
- **Findings 1–4, 6, 7 and 8:** the package is otherwise reproducible. Findings 1–3 are design points the owner should not have to rule around, and findings 4, 6, 7 and 8 are small corrections to the proposal text. The proposal bytes are the preparer's, so HELP_HUMAN returned all of them to the G1 preparer for a revised draft, not for disclosure only.
- **Finding 9** is disclosed in the proposal's question 3, and stays with the owner.

The revised draft replaces the published one in this PR, and it gets a fresh review before the owner rules.
