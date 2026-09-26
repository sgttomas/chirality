# D-PEC-96 A — Loop-Registry Schema v2 Act Handoff State

**Act date:** 2026-09-26
**Coordinator:** WORKING_ITEMS (Type 1), graph node G1 (the act) of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`
**Branch / basis:** `claude/pec-d96-registry-act` from `origin/main` `f90320c1d110cad75d04c96c91a595b7eb244498`
**Publication:** through its own PR under the standing Git authorization of 2026-09-12. This act does not merge it.

## D-PEC-96 item ledger

| Item | State after this act |
|---|---|
| Schema version 2 (`v2/config/loops.schema.json`) | DONE: exact postimage |
| Default instance, PEC's row migrated (question 2) | DONE: `shared-dev-loop` v1 live; `loop-receipts-ledger` v1 historical; `agentruns-json` v1 historical |
| Closed three-profile vocabulary, surfaces, coherence rules (question 3) | DONE: adapter `FEED_PROFILE_VERSIONS` / `FEED_PROFILE_SURFACES`; disjoint surfaces and at least one live profile enforced at load |
| Version-1 files rejected (question 4) | DONE: loader accepts only `schema_version` 2; `schema_version_1.json` fixture created (byte-identical to the version-1 default) |
| `RegisteredLoop.feed_profiles` port field, `FeedProfile`, `FeedProfileState` | DONE |
| Tests (12 → 19) and fixtures | DONE: `v2-loop-registry` Ran 19, OK |
| Finite verification | DONE: see `VALIDATION.md`; mutation 19/19 CAUGHT, RESULT PASS |
| DEL-01-06 `MEMORY.md` (question 5) | CREATED from the template, no run row. The undertaking's closeout (graph node M1) writes the row |
| Independent verifier | See "Verification" below |

## Verification

One fresh read-only `pec-reviewer` (Opus 5.5, high) applies the proposal's
"Independent verifier" section and `.agents/skills/software-code-review/SKILL.md`
(`ee085d58…8bca`). It includes a same-day reproduction on a fresh `git archive`
export of `f90320c1d` and a containment check. Verdicts are saved as
`VERIFIER_VERDICT_NN.md` in this run root. The final state is recorded in the
return file `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/G2_D96_REGISTRY_ACT.md`.

- **Verdict 01** (candidate `a8e6fd959`): **PASS WITH NOTES**, with no BLOCKING
  findings. It reproduced the act on a fresh `git archive` export of
  `f90320c1d` with byte-identical output, reran every check with the same
  results (mutation 19/19 CAUGHT, byte-identical to this run's output), and
  found containment clean.
  - N1 (non-blocking): `MANIFEST.md` misstated the act-script time. Repaired.
  - N2 (note): `RUN.md` was substituted without disclosure. Repaired by
    disclosure in `MANIFEST.md`.
  - N3 and N6 are notes on bound bytes. They are carried below as residuals 9 and 10.
  - N4 (`origin/main` moved) is carried as residual 11.
  - N5 (the brief's hash cannot be recomputed from the repository) needs no action.
- **Backcheck** of the N1/N2 repairs, in `VERIFIER_VERDICT_02.md` (final report, candidate `9839a0e19`, the update-branch merge; the interim report on `02ae9e2a0`/`f3ee68225` is `VERIFIER_VERDICT_02_INTERIM.md`): **PASS WITH NOTES**. B4 (two return statements overtaken by events) needs no edit. It found no blocking or non-blocking defects; N1 and N2 are repaired and containment holds.
  - B1: `MANIFEST.md` now labels the timing sentence as the manager's statement, and the act command line has been added to `checks/COMMANDS.txt` after the fact.
  - B2: the typo in the verdict-01 header note is fixed.
  - B3: no action needed. These are dispatch facts the manager attests.

## Residuals (recorded, not repaired here)

1. **Stale "declares `remaining-loop` now" sentences.** They are in the SOW-094 Notes cell,
   the DEL-01-06 description and DEL-01-06 `_CONTEXT.md`, and the vocabulary
   example in `SOFTWARE_DECOMP.md` §9 still names `remaining-loop`. As the
   proposal and the ruling direct, they go to graph node S2 (the DEL-01-06 SOW
   rebuild) and to a later PEC scope change. The SCA-006 post-change audit
   (open PR #943, COV-083) also flags them. This act writes none of them.
2. **DEL-01-06 SOW currency.** The accepted contract (`5fdcfd96…a2fa8`) still says
   "strict version-1". The new tests check behaviour that revision 1.5 requires
   but that the revision-1.4 contract does not state (REQ-007 lags) until S2 lands.
3. **DEL-01-06 Gate 5 HOLD stands.** DEL-01-06 stays `INITIALIZED`. The
   SELF_CHECK evidence (RF-001, RF-002; registry 12/12) is now historical
   evidence about superseded bytes. Any Gate 5 re-entry is the owner's own act.
4. **R-05 / FX-PEC-0.** They rest on the lapsed `remaining-loop` premise and are carried
   to graph node X1, as the proposal states.
5. **Path-normalization residual (proposal finding 3).** It is inherited and unchanged: the rule
   still accepts `projects/./pec/x`, `projects//pec/x`, a trailing `/`, a
   leading space and `C:x`. Tightening it is a small later amendment.
6. **Harness baseline drift from the prototype.** The prototype's `WARN=124` became `WARN=126` at
   `f90320c1d` without this act. Output is identical before and after the act.
7. **Strict register validator.** D-GOV-48's 26 pre-existing `XRG-013` warnings
   make `--strict` exit 1 on PEC. This act changes no register. Output is identical
   before and after.
8. **Loop records.** The work graph, central receipt, `docs/STATUS.md` and
   `README.md` (D-PEC-88), and any register-row status wording after merge
   belong to HELP_HUMAN. This act writes none of them.
9. **Adapter stricter than the schema text (verdict 01 N3).** This is in the bound bytes and is mostly
   inherited from version 1. Each case fails closed:
   - The adapter rejects `2.0` and `1.0`, which JSON Schema `integer` admits.
   - `loop_id` uniqueness and `loop_init_path` normalization are enforced but
     not stated in the schema.
   - The unknown-field location names the key, which the packet permits.

   The home for this is a later packet or the S2 rebuild, alongside residual 5.
10. **Probe-removal assertion (verdict 01 N6).** In the bound test bytes, the
    `test_overlapping_profiles_are_rejected_with_location` probe-removal
    assertion checks `FEED_PROFILE_VERSIONS` only. `mock.patch.dict` restores
    both maps, so this is not a defect. If the test is revised later, add the
    same assertion for `FEED_PROFILE_SURFACES`.
11. **Basis movement (verdict 01 N4).** During the act, `origin/main` moved to
    `53145aaeb` (PR #947, a Root change workflow and a PEC notice that defers
    action). That change is disjoint from this candidate and merges cleanly. CI
    and review must cover the actual merge candidate. If CI reports "Update the
    PR base", that is reported to HELP_HUMAN, not repaired here.

## Execution disclosures

- **Brief.** `G2_D96_REGISTRY_ACT.md` (HELP_HUMAN session scratchpad, not in
  the repository), SHA-256
  `e9dadc1a5a783d5a87597dc98659d6e1ca495a14d5071363d13e66e828594541`, verified
  before work began.
- **Instruction sources read.**

  | Source | SHA-256 |
  |---|---|
  | Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
  | `CLAUDE.md` | `336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49` |
  | `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
  | `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
  | the ruling | `852057f0…399e` |
  | the proposal | `4506597b…180e` |
  | the D-PEC-94 record (a basis citation) | `b6814e90…6a6b` |
  | the MEMORY template | `5a9564f4…6a5a` |

  The D-PEC-95 run root `_Coordination/CURRENCY_REV15_D95_2026-09-25/` was
  read as the format precedent. No other role's instructions were consulted.
- **Tools used.**

  | Tool | SHA-256 |
  |---|---|
  | `tools/software_workflow/run_registered_checks.py` | `665a4ac1…c766` |
  | `tools/software_workflow/select_affected_checks.py` | `43a1e5b5…7144` |
  | `tools/practitioner_harness/harness.py` | `01a9b954…61f3` |
  | `tools/validation/validate_pec_loop_receipts.py` | `8eb62995…bad9` |
  | `tools/validation/validate_decomposition_registers.py` | `869df1d5…57ee` |
  | `execution/_Scripts/pec_reliance_hold.py` | `b1712e4b…cd0e` |
- **Act-script executor.** The administrative grant assigns the run to one
  WORKING_ITEMS instance. This manager ran it once. No author TASK was
  dispatched, because the bytes are bound.
- **`--check-only`.** The script's non-writing check mode ran once before the
  act. It is recorded in `apply_d96_check_only.out` and wrote nothing.
- **Command form.** The proposal passes `--repo "$(git rev-parse --show-toplevel)"`.
  This run passed the literal absolute path, which is equal to that output. The host's
  worktree-isolation guard refuses a command substitution there.
- **Check helpers.** The manager wrote `run_checks.sh`, `post_checks.sh` and
  `containment.py` for this run. They are read-only against the product tree, and they
  are committed here so the verifier and later readers can rerun them.
- **Model identity.** The host reports the serving model as Opus 5.5
  (`claude-opus-5-5`). The role and the `high` reasoning effort are
  instruction-asserted.
