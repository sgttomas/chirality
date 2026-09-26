# Review 02 of PR #928 (D-PEC-96 revision 2; D-PEC-78 §4.3 REVIEW), transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `c39d27d928b4126a43487261092377f02adc91b8`.
- **SHA-256 of the report text below (UTF-8):** `fbe560c4fa8fa4b47ce355d7630ef1911440fb0819491a8ab53f3258acc42a32`.

## Report (verbatim)

## Re-review of PR #928 at head `c39d27d928b4126a43487261092377f02adc91b8` (D-PEC-96 revision 2)

**Verdict: FAIL, on one blocking finding that revision 2 introduced.** Under option A-R the bound mutation step crashes, so the verification the packet requires cannot pass.

- Option A, the recommended one, reproduces byte for byte and passes every check, including 19 of 19 mutations.
- Review-01 findings 1–4 and 6–8 are genuinely resolved, not just disclosed.
- B1 (R2 now ACTIVE) and finding 5 (register row) are fixed.

Basis and method:
- Head confirmed with `gh pr view 928 --json headRefOid`; the PR is OPEN.
- `origin/main` is `56a626c3b`. The PR's merge-base is still `4d5f7b911`, and `git diff --stat 4d5f7b911 56a626c3b -- projects/pec` is empty.
- I read everything from `git archive` exports in my scratchpad: `…/scratchpad/rev2.pQpX/`. The checkout was not touched.
- The PEC reliance-hold preflight (`candidate-validation`) returned ALLOW. The holds register has no rows.

### Blocking

**B1. `mutate_d96.py` crashes under option A-R, so A-R's required verification cannot be met.**
- **Where:** `projects/pec/execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/mutate_d96.py`, the `MUTATIONS` entry `"M19 default drops remaining-items"`, which is `edit_json(DEFAULT, lambda d: d["loops"][0]["feed_profiles"].pop(1))`.
- **Requirement it breaks:** the proposal's Finite verification table (`D-PEC-96_…proposal_2026-09-25.md`, "Mutation evidence" row) requires "M1–M19 each CAUGHT; `RESULT PASS`" for whichever option is ruled.
- **Evidence:**
  - On my option-A-R tree (`apply_d96.py --pec-row remaining` on an export of `56a626c3b`), the runner stops with `IndexError: pop index out of range` at M19. It exits 1 with a traceback and prints no `RESULT` line. The A-R default has only one profile entry.
  - With M19 removed, M1–M18 are all caught on A-R and it ends `RESULT PASS`.
  - The preparer ran mutations only on the A clone (`evidence/mutate_d96.out`).
  - Revision 1's mutation set did not have this problem.
  - M11 on A-R is caught only because the `basis` string differs, which makes it a weak mutation there.
- **Why it is blocking:** A-R is one of the options offered for the ruling, and D-PEC-78 §4.3 has the owner accept exact test and verification bytes after REVIEW. A ruling for A-R would bind a verification step that fails at the act and forces a re-ruling.
- **Fix, either of:**
  - Make the runner option-aware, for example `--pec-row remaining`. For A-R, use an M19 variant that fits it, such as dropping `status-remaining` from `remaining-loop`, and preferably an M11 variant that changes the profile set, not just the basis.
  - Or state the expectation per option in the verification table (A: M1–M19; A-R: M1–M18 plus the A-R variant).

  Then re-hash `mutate_d96.py` in the proposal and in `SHA256SUMS`, and run the A-R mutation set into the evidence.

### Non-blocking, ranked

1. **(Low–Medium) Rollback lets HELP_HUMAN revert the owner's ruling record.**
   - Rollback says HELP_HUMAN's records that rode the act PR "are reverted with it, or kept by a partial revert; that is HELP_HUMAN's choice".
   - That choice could revert the owner's ruling record and the D-PEC-96 register row.
   - The register header says a ruled row is not reopened; residual work gets a new row.
   - **Suggest:** state that the ruling record and register rows are never reverted, and that a rollback records itself as a new row or record.
2. **(Low) The graph's recovery section is partly stale.** `WORK_GRAPH.md` ~L101–111:
   - "Checked basis: `origin/main` `4d5f7b911` (PR #926 merged)" is stale; `origin/main` is `56a626c3b`, although nothing under `projects/pec` changed.
   - The G1 active-operations line still reads "the read-only TASK handed back, and its draft is published in the sixth PR". It does not mention review 01 (`returns/REVIEW_PR928_01.md`), the return to the preparer, or the revision-2 hand-back.
   - The G1 table row itself is accurate.
3. **(Low) A-R still leaves PEC's JSON run evidence unread.** A-R's `remaining-loop`-only row does not cover PEC's one `WORK_GRAPH.json` (DEL-01-03 `_run_records/P1_STORE_GUARD_01/`), which FX-PEC-0 includes.
   - The table allows `remaining-loop` together with `agentruns-json` historical.
   - Question 2 "Other" permits it, but A-R as offered reproduces review-01 point 3 for that branch. One sentence in question 2 would make this visible.
4. **(Low) The meaning of `live` for `remaining-items` is a judgement call.**
   - The schema defines `live` as "the loop currently writes this generation".
   - D-PEC-94 says the Remaining sections "receive no new entries"; they are only updated under packets.
   - The proposal argues for `live`, and question 3 (b) offers `historical`, so the owner is informed. No change is needed if the owner accepts (a).
5. **(Nit) The review points are numbered differently.** The proposal's revision table (L7–15) numbers the points 1–7, while review 01 numbered them 1–4 and 6–8. Its "5 Containment" is review finding 6, and so on. Traceability would be clearer with the review's numbers.

### Resolution of review-01 findings (verified against source)

**1. Remaining sections: resolved.**
- `remaining-items` covers only `status-remaining`, and its description says "never as a work-selection signal". It brings no ledger (its surfaces are `status-remaining` only).
- Justification:
  - PRD v2.3 §7.1: remaining items are "a per-loop optional field, read only where the loop's feed profile declares it".
  - O-B2 expects that "a genuinely new layout needs a new profile … code plus a packet".
  - `projects/pec/AGENTS.md` L241–248 keeps the sections as binding records.
- The profile is disclosed as new: finding 2 and question 4.
- PEC's row declares it `live` with basis `projects/pec/AGENTS.md`, with alternatives in question 3.

**2. Coherence: resolved.**
- `FEED_PROFILE_SURFACES` matches the proposal's surface table and each schema option's "Surfaces:" list, and a test checks it.
- The adapter rejects overlapping surfaces at the later entry's `.profile`, and rejects a row with no live profile at `feed_profiles`.
- My probes gave these results:

| Row | Result |
|---|---|
| `remaining-loop` + `agentruns-json` historical | accepted |
| `shared-dev-loop` + ledger historical | accepted |
| `remaining-loop` historical + `shared-dev-loop` live | rejected, located at the second entry |
| ledger live + ledger historical | rejected (test) |
| two live lifecycle readers | rejected (test) |
| Remaining read twice | rejected (test) |
| all historical | rejected (test) |

- Mutations M14–M17 kill these checks and all are caught.

**3. `agentruns-json`: resolved.**
- Its coverage is now "anywhere under the loop's execution/ tree", which matches PRD §7.1 RunRecord (`execution/**`) and DependencyEdge.
- PEC's row declares it `historical`, which covers the one `WORK_GRAPH.json`. I confirmed there is no `STATUS.json` or `RUNTIME_SUMMARY.json`.
- The basis ("by implication") is disclosed.

**4. The §B6 quote: resolved.** It is now quoted in full, and question 2 states the departure from its letter and from Q8 (a).

**6. Containment: resolved.** The row lists HELP_HUMAN's records and `STATUS`/`README`, and allows a separate PR.

**7. HOLD citation: resolved.** It now cites `_REVIEW.md` L45–48, which I checked.

**8. Nits: resolved.**
- There are now non-string `state` and `null` `profile` cases.
- `test_failures_do_not_echo_document_values` covers 6 fields, and M18 is caught.
- The `$id` is now `…loops.schema.v2.json` and a test pins it.
- The suite runs 17 tests, and the invalid-feed-profiles test has 24 sub-cases.

### Reproduction

Everything below ran on an export of `56a626c3b` set up as a scratch git repo with alternates, `read-tree` and `update-ref`. Python 3.13.7, `PYTHONDONTWRITEBYTECODE=1`.

| Check | Result |
|---|---|
| Preimages | The 10 preimages and 6 must-remain hashes match; the fixture and `MEMORY.md` are absent; the path-list hash is `b5db12e5…c73c` |
| Script and tables | The `apply_d96.py` pinned tables equal the proposal's grant table (11 rows) and must-remain table; the A/A-R differences are exactly `loops.json` `6e1321e3…` and the test file `586fcd5e…`; the script's head and tail equal the template |
| `--check-only` | exit 0, tree unchanged |
| Option A | exit 0; report equals `evidence/actA.report.txt`; all 11 files byte-equal to `postimages/optionA_v2/**`; the schema, both `loops.json` and the port equal the proposal's code blocks; the diff equals `evidence/optionA_vs_56a626c3b.diff` apart from hunk order and index abbreviations (same line multiset, 773 lines) |
| Option A-R | exit 0; report equals `actAR.report.txt`; both override files match |

Registered checks:

| Check | Base | A | A-R |
|---|---|---|---|
| `v2-api-contract` | 6 OK | 6 OK | 6 OK |
| `v2-loop-registry` | 12 OK | 17 OK | 17 OK |
| `v2-store-guard` | 13 OK | 13 OK | 13 OK |
| enforcement | 28 OK | 28 OK | 28 OK |
| `v2-core-posture` | PASS, 0 findings, core tree `88f590c0…` | PASS, `dd7e1dda…` | PASS, `dd7e1dda…` |
| `harness-self-check` | exit 0 | exit 0 | exit 0 |

The harness stdout hash is `e5f9ff70…d110` in all three cases.

Fail-closed:
- Reruns of A and of A-R: exit 1, tree unchanged.
- Drift in `service_core_posture.json`, drift in the adapter, and an existing `schema_version_1.json`: each exits 1 with "nothing written".

Mutations:
- On A: `mutate_d96.py` exits 0 with 19 of 19 caught; the output is byte-equal to `evidence/mutate_d96.out`.
- On A-R: it crashes (B1).

### Grant, containment, rollback, questions and hashes
- The 11 paths and 6 must-remain files are unchanged from revision 1.
- The new postimage hashes match the grant table.
- `apply_d96.py` is `b314213a…6dd4`; `mutate_d96.py` is `c438e7ac…6ad7`; `build_json_postimages.py` is `f3dfb9c8…998b`.
- All 42 basis-table hashes match at `56a626c3b`. The verifier skill did change in PR #927 (`06c27b1b…` → `ee085d58…`), as stated.
- The seven owner questions are genuinely the owner's. The limits grant no lifecycle, SOW, PRD or decomposition change and no CHECKING prompt.

### Publication fidelity
- The proposal hashes to `4655e757…8da7` (753 lines), equal to the `D-PEC-96_DRAFT.md` entry in `SHA256SUMS`.
- `shasum -c` passes for all 27 other entries.
- The only files not in `SHA256SUMS` are `.gitattributes` and `SHA256SUMS` itself.
- The revision-2 report hash `7365abe1…0945` matches the text after "### Revision-2 report (verbatim)" with the trailing newline stripped, the same convention as before. The revision-1 report hash `1ea79afc…` is still intact.

### Register, graph and hygiene
- **Register row:** 6 columns and accurate. It names the run root and the MEMORY option, the revision-2 hashes, and that revision 1 was superseded.
- **Graph:**
  - The R2 row is ACTIVE with brief B5, and the G1 row reflects revision 2. The graph is still acyclic.
  - The recovery section is partly stale (non-blocking 2).
  - There is no new STATUS or README change, so the D-PEC-88 trace needs no new entry.
- **Hygiene:**
  - `git diff --check origin/main...c39d27d92`: clean. No path outside `projects/pec` changed.
  - `validate_pec_loop_receipts.py`: VALID.
  - `validate_decomposition_registers.py --strict projects/pec/execution`: 0 errors and 0 warnings.
  - The harness self-check at the head: exit 0, output identical to base.

## HELP_HUMAN disposition

The verdict is FAIL, on B1: the `mutate_d96.py` M19 step crashes on an A-R tree.

- **B1 and non-blocking 1, 3 and 5** go to the G1 preparer for revision 3. They are the rollback rule for the ruling record and register rows, the A-R `agentruns-json` sentence in question 2, and the revision-table numbering.
- **Non-blocking 2**, the graph recovery section, is repaired by HELP_HUMAN.
- **Non-blocking 4**, `live` versus `historical` for `remaining-items`, stays with the owner through question 3.

Revision 3 replaces revision 2 in this PR, and it is re-reviewed before the owner rules.
