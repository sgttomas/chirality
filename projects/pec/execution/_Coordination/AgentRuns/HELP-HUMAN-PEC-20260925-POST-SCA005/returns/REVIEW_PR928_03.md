# Review 03 of PR #928 (backcheck of D-PEC-96 revision 3; D-PEC-78 §4.3 REVIEW), transcribed

- **Reviewer:** the same read-only `pec-reviewer` as reviews 01 and 02 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `d640e94c0bfd91b0ea2b4643f98384ec509c16a6`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8):** `128a97ebf0ddf7f5540bec9a7e3fb11affdd4405a65f295c931d728e8ddeff66`.

## Report (verbatim)

## Backcheck of PR #928 at head `d640e94c0bfd91b0ea2b4643f98384ec509c16a6` (D-PEC-96 revision 3)

**Verdict: PASS. There are no blocking findings.**

Review 02's blocking finding B1 is fixed, and its non-blocking findings 1, 3 and 5 are resolved. HELP_HUMAN's repair of finding 2 (graph recovery section) is also in. Nothing else changed unexpectedly between revisions 2 and 3.

Basis and method:
- Head confirmed with `gh pr view 928 --json headRefOid`; the PR is OPEN.
- `origin/main` is now `283835358` (PR #931). The head's update-branch merge has parents `05b69962a` and `283835358`.
- From `56a626c3b` to `283835358`, the only change under `projects/pec` is the two Root wave-2A notices, `NOTICE_2026-09-26_WORKFLOW_WAVE2A_{EXECUTION,CLOSURE}.md`. Nothing under `v2/**` changed.
- Everything was read from `git archive` exports in `…/scratchpad/rev3.K51P/`. The checkout was not touched.
- The reliance-hold preflight (`candidate-validation`) returned ALLOW.

### Blocking
None.

### Non-blocking (all low)
1. **The revision-3 note undercounts review 02's non-blocking findings.** Proposal L5 says review 02 raised "one blocking finding and three non-blocking ones". It raised five. Number 2, the graph, was HELP_HUMAN's to fix. Number 4, the meaning of `live`, needed no change. The table does address the three that were the preparer's.
2. **The M11 description for option A is slightly inexact.** The proposal says M11 "swaps only the profile identifier, keeping basis and state".
   - For A, `default_profiles_swapped_to_remaining_loop` also cuts the row down to its first entry. It has to, because `remaining-loop` would overlap `remaining-items` and the ledger.
   - The mutation is still meaningful: it produces a valid config that only the default-equality test catches.
3. **The graph's recovery section is behind again.**
   - It says "Checked basis: `origin/main` `56a626c3b`", but the PR now includes `283835358`.
   - It does not record PEC's receipt or disposition of the two wave-2A notices that the merge brought into `execution/_Coordination/`.
   - The notices' one consequence for this PR, the retired `software-bounded-implementation` workflow, is handled in the proposal.

### What I verified

**1. B1 is fixed.**
- `mutate_d96.py` hashes to `8d3d2fb3…fe45`. It is option-aware (`--pec-row migrated|remaining`), and any mutation that fails to apply is caught and reported `NOT_APPLIED`, which sets the result to FAIL.
- I ran it on my own exports of current `origin/main` `283835358`:
  - **Option A:** exit 0, 19/19 CAUGHT, `RESULT PASS`. Output byte-equal to `evidence/mutate_optionA.out`.
  - **Option A-R:** exit 0, 19/19 CAUGHT, `RESULT PASS`. Output byte-equal to `evidence/mutate_optionAR.out`.
- The A-R variants are meaningful:
  - M11 changes `remaining-loop` to `shared-dev-loop` with the same basis and state. The loader accepts that config, so only the default-equality test can catch it, and it does.
  - M19 makes the only profile `historical`. The at-least-one-live rule and the default test both catch it.
- `NOT_APPLIED` fails the run. On an unapplied v1 tree the runner reported 18 `NOT_APPLIED`, including M19 (`KeyError: 'feed_profiles'`), exited 1 and printed `RESULT FAIL`.
- Running A-R variants against an A tree also fails: M11 is a no-op there, SURVIVES, and the run prints `RESULT FAIL`. A wrong option flag cannot produce a false pass.
- The verification table now states the expectation for each option.

**2. Review-02 non-blocking findings.**
- **Finding 1, rollback: resolved.** The ruling record and every register row are never reverted. A rollback is recorded as a new row and record under the register header's convention. Other records that rode the act PR may only be added to.
- **Finding 3, A-R and PEC's JSON evidence: resolved.** Question 2 now says A-R leaves `DEL-01-03/_run_records/P1_STORE_GUARD_01/WORK_GRAPH.json` unread. It offers `remaining-loop` with `agentruns-json` historical as a valid "Other" answer. My earlier probe confirmed the adapter accepts that pair.
- **Finding 5, numbering: resolved.** The revision-2 history table now uses review 01's numbers (1–4, 6–8).

**3. The workflow change follows the basis.**
- `ea5009d05` (Root wave 2A, which is in `7f33b4dd5`) deleted `workflows/software-bounded-implementation/`. It moved its rules into `construct-local-work-graph` as implementation-node requirements.
- That workflow hashes to `3e197c9d…9dc3` at `7f33b4dd5` and is unchanged at `283835358`. Its lines 62–63 require the brief fields the grant now lists: objective, basis, write fence, exclusions, acceptance criteria and checks.
- The execution notice hashes to `d194b1b5…4383`.

**4. No unexpected changes.**
- `apply_d96.py` (`b314213a…6dd4`), the template, both builder scripts and every postimage are byte-unchanged from `c39d27d92`.
- Revision 3 touched only these files:
  - the proposal;
  - `mutate_d96.py`;
  - the evidence files: `CHECKS_SUMMARY.txt`, the new mutation outputs and A-R verbose run, the timestamps in `optionAR_vs_optionA.diff`, and a rename of the A diff with identical content;
  - `SHA256SUMS`;
  - the return;
  - the register row;
  - the graph.
- The proposal word-diff shows only the revision note, the basis-commit strings, the mutation-evidence row, the rollback text, the question-2 A-R note, the evidence table and two basis-table rows.
- All 43 basis-table hashes match at `7f33b4dd5` and are unchanged at `283835358`.

**Reproduction on `283835358`.** Scratch git repos with alternates, `read-tree` and `update-ref`; Python 3.13.7, `PYTHONDONTWRITEBYTECODE=1`.

| Run | Result |
|---|---|
| `--check-only` | exit 0, tree unchanged |
| Option A | exit 0; report equals `evidence/actA.report.txt`; all 11 files byte-equal to `postimages/optionA_v2/**` |
| Option A-R | exit 0; report equals `actAR.report.txt`; both override files match |
| Reruns (A and A-R) | exit 1, "nothing written" |
| Must-remain drift, preimage drift | each exit 1, "nothing written" |

Registered checks:

| Check | Base | A | A-R |
|---|---|---|---|
| `v2-api-contract` | 6 OK | 6 OK | 6 OK |
| `v2-loop-registry` | 12 OK | 17 OK | 17 OK |
| `v2-store-guard` | 13 OK | 13 OK | 13 OK |
| enforcement | 28 OK | 28 OK | 28 OK |
| `v2-core-posture` | PASS, `88f590c0…` | PASS, `dd7e1dda…` | PASS, `dd7e1dda…` |
| `harness-self-check` | exit 0 | exit 0 | exit 0 |

The harness stdout hash is `e5f9ff70…` in all three cases.

**5. Publication fidelity.**
- The proposal hashes to `2f7d9875…afc4`, equal to the `D-PEC-96_DRAFT.md` entry in `SHA256SUMS`.
- `shasum -c` passes for all 30 other entries.
- The only files not listed are `.gitattributes` and `SHA256SUMS` itself.
- Return report hashes, each taken over the verbatim text with the trailing newline stripped:
  - revision 3: `700f22e0…0faf`, matches;
  - revision 1: `1ea79afc…` and revision 2: `7365abe1…`, both still intact.

**6. Register, graph and hygiene.**
- **Register row:** 6 columns and accurate. It gives the revision-3 proposal hash, the act script, the mutation-runner hash, and that revisions 1 and 2 were superseded before any ruling.
- **Graph:**
  - The G1 row is truthful: revision 3, runner option-aware, under backcheck.
  - The recovery line now cites reviews 01 and 02.
  - The graph is acyclic. See non-blocking 3 for the stale basis line.
- **Hygiene:**
  - `git diff --check origin/main...d640e94c0`: clean. No path outside `projects/pec` differs from main.
  - `validate_pec_loop_receipts.py`: VALID.
  - `validate_decomposition_registers.py --strict projects/pec/execution`: 0 errors and 0 warnings.
  - The harness self-check at the head: exit 0, output identical to base.

## HELP_HUMAN disposition

The verdict is PASS, with no blocking findings. This completes the D-PEC-78 §4.3 REVIEW on the revision-3 bytes, and the PR merges at the reviewed content with this file added.

- **Findings 1 and 2** concern wording in the proposal. They are disclosed to the owner with the presentation, and the proposal bytes stay as reviewed.
- **Finding 3:** the graph's basis line, and PEC's disposition of the two Root wave-2A notices, are recorded in HELP_HUMAN's next graph update.
