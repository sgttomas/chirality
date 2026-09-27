# Verifier verdict 03 — MODE=VERIFY on DEL-03-04 and DEL-10-03, and packet review (S4P preparation)

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by the S4P WORKING_ITEMS manager in the foreground. It authored nothing in the packet. Its final report is transcribed below verbatim from its hand-back message.
- **Reviewed head:** `396c6f744`. Repairs follow in the next commit; dispositions are at the end.

## Report (verbatim)

## pec-reviewer verdict: S4P packet (provisional D-PEC-102), head 396c6f744

**Overall verdict: PASS WITH NOTES.** Nothing blocks. There are 3 NON-BLOCKING findings and 5 NOTES.

- **Part A (`MODE=VERIFY` on DEL-03-04 and DEL-10-03):** both contracts pass the mode-applicable items (1, 3, 4, 8, 9, 13, 16, 18–21). One of the non-blocking findings is a claim that is no longer true in the DEL-10-03 candidate (N1).
- **Part B (packet review):** hashes, pins, the act script, the checks and the negative controls all reproduce exactly. There are two small factual errors in the draft (N2, N3).
- I modified no file and ran no mutating git command. The worktree is clean and HEAD is still 396c6f744 (the same as the remote branch head). Per the brief, I did not flag the absence of `SHA256SUMS` or of the manager's return.

Finding labels: **[schema]** a structural or format problem; **[project-content]** a problem in what a file says; **[substrate]** the execution environment.

### Findings

**N1. NON-BLOCKING [project-content]: the DEL-10-03 candidate says its framing comes from "this run's brief", which is no longer true.**
- Where: `PREP/candidates/projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md` L42–43: "That framing is directed by this run's brief under `D-PEC-63`, whose directing sentence reads, verbatim:"
- The sentence is carried unchanged from the prior contract (L30–31 at 125cfacc1). The run that authors these bytes is now the S4 run, and its brief (`DRAFTER_BRIEF.md`) does not direct that framing.
- DEL-03-04 fixed the identical sentence (candidate L41–43: "was directed on 2026-07-25 by the brief of the run that authored this deliverable's first contract under `D-PEC-63`").
- Repair: use the DEL-03-04 wording in DEL-10-03. This changes the postimage hash, so after the edit:
  - update the grant table (draft L274) and the candidate table (L108);
  - re-render `apply_s4p.py` with `build_apply_s4p.py` and re-bind its hash (L325);
  - update the DEL-10-03 checklist hash (L509);
  - update any affected quote or claim entries, re-run `run_s4p_checks.sh`, then have DEL-10-03 re-verified.
- Nothing else in DEL-10-03 depends on the sentence: the quotation and its durable home, `BATCH_B2_FANIN.md`, are correct.

**N2. NON-BLOCKING [project-content]: the draft's list of what changed in `projects/pec` after 125cfacc1 is incomplete.**
- Where: `PREP/DRAFT_D-PEC-102_s4_sow_currency_proposal.md` L47–49 says `projects/pec` changed "only in" the PR #981 and PR #982 records.
- `git diff --name-status 125cfacc1 3488a236a -- projects/pec` also shows `M projects/pec/docs/STATUS.md`, from commit 5bb7b23f1 (PR #982, "STATUS retirement bullet").
- Repair: add `docs/STATUS.md` to the PR #982 bullet. No pinned file is affected.

**N3. NON-BLOCKING [project-content]: one abbreviated hash in the Method section is wrong.**
- Where: draft L57 gives `resources/tools.md` as `fbd07771…6cc5`.
- The actual SHA-256 at 125cfacc1 and 3488a236a is `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7`, which ends `…5cc7`.
- The error is copied from the D-PEC-100 proposal (L25), which has the same typo. That is historical and should not be edited.
- Repair: change it to `fbd07771…5cc7`.

**Notes (no repair needed unless you want the wording tidied):**

1. **Count of contracts quoting old S2 text (draft L211).** The draft says "Of the 13 contracts outside S2 that `D-PEC-100` said quote old S2 text". The D-PEC-100 proposal (L97) says "fifteen": thirteen plus DEL-02-08 and DEL-02-09. The brief also says 15. Suggested wording: "Of the fifteen (thirteen, plus DEL-02-08/09)". The draft could also say that DEL-04-02's two D-PEC-100 flags were scanner artefacts (its own CLM text), as it already says for DEL-10-03.
2. **origin/main has moved.** It is now `e548d4cfa` (PR #984, which changed only a piping `WORK_GRAPH.md`). All 16 pre/postimage hashes and all 19 pins are unchanged there. A full `run_s4p_checks.sh` run at e548d4cfa gives OVERALL PASS, and the script rendered at e548d4cfa differs only in its comment line. You may want to refresh the named check commit at publication.
3. **The DEL-10-11 consequence has no destination (draft L222).**
   - The table says "no current node" but names nowhere for the fix to go. Suggest HELP_HUMAN records it in the work graph for a later DEL-10-11 currency pass.
   - Precision: both stale quotations of DEL-03-04 `CON-001` and `CON-005` are in DEL-10-11 `CLM-014` (L185). The quotations in `CLM-013` (L171: `REQ-003`, `REQ-007`, `REQ-013`) stay verbatim.
4. **DEL-10-03 acceptance-criteria order.** AC-011 and AC-012 come before AC-009 and AC-010, both in the list (L395–398) and in the matrix (L459–462). The derived checklist therefore runs in that order too. This is valid and the checklist is correct; it is only unusual.
5. **REVISE is mentioned three times** (L42, L66, L443), matching the D-PEC-100 pattern (L16, L27, L273). It is not put to the owner, so the substance meets the brief.

### Part A: `MODE=VERIFY` on DEL-03-04 and DEL-10-03 (both PASS)

**Checklist items (both contracts):**
- **1:** both are `SOW_V1`, with no pilot variance and no dual-format markers.
- **3:** `_STATUS.md` hashes to its pin at 125cfacc1, 3488a236a and e548d4cfa. Both deliverables are `INITIALIZED`.
- **4:** `PASS format=SOW_V1`.
- **8/9:** every matrix row carries its SOW and OBJ references, and every acceptance criterion has a `VER-*` or `HUMAN_REVIEW`.
- **13/18:** the checklists re-derive byte-identically and match the draft's hashes (`1a86fa42…`, `f6db15bf…`). They carry 19 and 12 criteria, each once.
- **16:** findings above are labelled schema, project-content or substrate.
- **19:** 0 bare undefined ID tokens outside blockquotes.
- **20:** 0 matrix rows group more than one acceptance criterion.
- **21:** the boundary tool reports exit 0 with no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`. I checked the hand resolution in the draft (L391–392) against CLM-010/015/017 and CLM-008/016.

**Kept IDs:**
- Diffing each ID against 125cfacc1 shows no ID retired or reused in either contract.
- DEL-03-04's changed set matches its AX-012 list exactly. `CON-004` is byte-identical, so its external citations from DEL-01-01 and DEL-02-07 stay valid, and the new `CON-007` carries the third DriftFinding producer.
- DEL-10-03's changed set matches its AX-012 list. `OUT-001` and `REQ-007` are byte-identical (DEL-10-02 `CLM-012` quotes them).

**Claims and quotations I checked against sources at 125cfacc1:**
- PRD v2.4:
  - the §12 standing reliance-advertisement gate paragraph (L451–461), verbatim;
  - the §12 P1 row (L446);
  - the §8 access classes and the `agent` definition (L310–315);
  - the text of `PEC-API-007` (L385) and `PEC-K-03` (L230);
  - §15, the D-PEC-90 bullet (L567).
- Register rows:
  - SOW-100 statement and Notes;
  - SOW-003, SOW-099, SOW-017;
  - the DEL-10-13 description ("composes DEL-03-04 parity…");
  - the DEL-08-06 description;
  - the PKG-10 and PKG-03 §4 rows;
  - `DEP-10-13-003`, `DEP-10-03-003` and `DEP-03-04-003` (including that its `EvidenceQuote` was empty as seeded at 3660288a5);
  - `[E-P88]` is absent from the gate exhibit, and `[E-P28]` is present with the quoted cells.
- SCA records:
  - SCA-006 Propagation_Plan §B4 rows (L295, L305–306);
  - SCA-006 Impact_Assessment §7.1 rows (L299, L301, L327) and the SCA-005 residue at L490;
  - SCA-005 §B4 classes and the ticks for the unresolvable `@3623b958b` pin and the false revision-1.1 claim (DEL-03-04 and DEL-10-03 only). `3623b958b` resolves to no commit.
- Upstream and sibling IDs:
  - `DEL-01-01/REQ-001` (sixteen types), `/TBD-003`, `/CON-008`;
  - `DEL-01-05/TBD-003..005`;
  - `DEL-02-07/CON-006`;
  - `DEL-08-02/OUT-001`, `/REQ-001`, `/CLM-002`, `/TBD-004`, and DEL-08-02 is `CHECKING`;
  - the DEL-08-01 postimage `OUT-001`, `OUT-002`, `REQ-002`, `CLM-001`, `CON-002`.
- Environment facts:
  - `harness.py` `OBSERVABLE_PROJECTS` and the tuples around it (L89–103), and the `next` and `run-validations` subcommands;
  - canary `schema.json` SHA-256 `0a4e4273…5c67`, added by e9fec7fff (an ancestor of 125cfacc1), with `api_schema_version` 1;
  - no `v2/` path names parity, a server, a socket or a token;
  - `_SEMANTIC.md` is 0 bytes;
  - the Deliverables row for DEL-10-03 is identical at 65955cceb and 125cfacc1;
  - PhaseHints for every deliverable the two contracts name.

**Semantics (both contracts):**
- No scope is added beyond the ledger, register or PRD. REQ-016 (DEL-03-04) and REQ-013–015 (DEL-10-03) are boundaries or restatements grounded in SOW-017, SOW-003 and `PEC-API-007`.
- Open questions stay open as `CON` items: the gate's force, "explained", the third producer, tool-call enumeration and the tier-0 invocation question.
- Nothing is built around verify-before-rely. Reliance is stated only after the §12 gate, and never as authority.
- No `## Remaining` surface is read or presented. There are no CHECKING, ISSUED or acceptance claims.

### Part B: packet review

**Hashes:**
- All 8 preimages match at 125cfacc1, 3488a236a and e548d4cfa, and all 8 postimages equal the candidate bytes.
- All 19 pins match at all three commits. The first five also match at 189f205ff, which is an ancestor of origin/main (PR #954).
- The draft's basis hashes match except N3. Among them: Root `AGENTS.md`, the agent files, `_LATEST.md`, the SCA-006 and SCA-005 plans, the D-PEC-90/94/96/98/99/100/101 rulings, the exhibit, the register, the workflow files, the standard, the tools, the reliance script and holds file, the template, and the notices.
- The brief copy hashes to `d00a739a…`, `DRAFTER_BRIEF.md` to `d795dbca…`, and every check aid to its tabled hash.

**Candidate table:** lines, per-prefix ID counts, checklist item counts and quote/claim counts all recompute for all eight. 740 quote checks and 1138 claims both hold. No ID is retired in any of the eight.

**Act script `apply_s4p.py`:**
- Hash `29a905c7…0e640`.
- Diffed against the D-PEC-100 run-root `apply_s2p.py`: only the docstring, targets, pins, temporary suffix `.s4ptmp` and run-root prefix `SOW_CURRENCY_S4_` differ. The loops.json pins were dropped, which is appropriate here.
- The run-root guard refuses the prep folder itself. Rollback and inventory logic is identical to the precedent.
- Re-rendering from the template in scratch reproduces the exact hash at 125cfacc1; at 3488a236a and e548d4cfa only the comment line differs.
- `test_apply_s4p.py` differs from the precedent only in names, and all 9 cases pass.

**Draft structure and content:**
- The section headings match the D-PEC-100 proposal, with S4-appropriate substitutions.
- Options, with A recommended; exact grant; finite verification; independent verifier; administrative grant; rollback; limits: all present.
- Owner questions: Part B reading, the two readings, add-on M and models are present. Nothing prompts the owner about CHECKING.
- Lifecycle: all eight are `INITIALIZED`; DEL-00-03 is `CHECKING` and not touched. No `MEMORY.md` exists in any of the eight folders, and the template has `{{DEL-ID}}` and `## Runs`.
- DEL-04-01 `_REVIEW.md` disclosure: accurate. It is a `PEER_REVIEW` of 2026-08-09, gates 1–4 complete, Gate 5 not entered, RF-001 and RF-002 marked REVISE and RESOLVED against `6f4e8c66…`.

**Downstream consequences:**
- My own blockquote-level check against the postimages finds exactly the draft's three consequences:
  - DEL-04-05 quotations of DEL-04-01 `REQ-001` and `CON-004`;
  - DEL-04-05 quotation of DEL-04-03 `CON-003`;
  - DEL-10-11 quotations of DEL-03-04 `CON-001` and `CON-005`.
- Kept quotations: DEL-04-05's of DEL-04-03 `REQ-001`/`005`/`008` and DEL-04-01 `REQ-006`; DEL-10-11's of DEL-03-04 `REQ-003`/`007`/`013`, `CON-004`, `TBD-005`.
- The STALE lines in the heuristic scan that I spot-checked are artefacts: DEL-10-02 AX-005, DEL-04-05 CLM-009 and DEL-03-02 CLM-007 are each that contract's own text, not quotations.
- All three ACTIVE dependency quotes (DEP-08-04-004, DEP-08-04-006, DEP-08-05-005) are verbatim in the postimages.

**Part B landing:** I spot-checked the line numbers in the landing table (L172–176) against the postimages, and the DEL-04-03-REM-002 correction (3) text in AX-010.

**Containment:** `git diff --name-status origin/main...HEAD` lists only the prep folder and the brief copy under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`.

### Commands run (exit codes and results)

1. `git fetch origin main` → exit 0. origin/main is `e548d4cfa`. The merge base with HEAD is 125cfacc1, and 3488a236a is an ancestor.
2. Hash recomputation with `git show <c>:<path> | shasum -a 256` for the 16 grant hashes and 19 pins at 125cfacc1, 3488a236a, origin/main and 189f205ff → all match (the first five pins also at 189f205ff).
3. `TMPDIR=<mine> run_s4p_checks.sh <repo> 3488a236a PREP <out_3488> 125cfacc1` → exit 0, OVERALL PASS.
   - Lines: `quotes: RESULT PASS 740/740`, `state claims: RESULT PASS 1138/1138`, `sibling and external IDs: RESULT PASS 54/54`, `SUMMARY stale=13 kept=25` (informational), `S2 … stale=0 kept=2`, strict exit 1 with 0 errors and 26 warnings (identical before and after), harness and receipts exit 0 (identical), `active_execution_quotes_verbatim 127/127`, `fault injection: RESULT PASS 9/9`.
   - Compared with `PREP/evidence/run_main/`: every file is identical except `containment.out`, `receipts_pre.out` and `receipts_post.out`, which differ only in the export path.
4. The same runner at `e548d4cfa` → exit 0, OVERALL PASS, same result lines.
5. `TMPDIR=<mine> negative_controls.sh <repo> 3488a236a PREP` → exit 0, `RESULT PASS negative controls`, 6 of 6 tripped. Output is byte-identical to `PREP/evidence/negative_controls.out`.
6. `build_apply_s4p.py` on scratch copies at the three commits → 125cfacc1 gives `29a905c7…` (identical to the bound script); the other two differ in the comment line only.
7. `pec_reliance_hold.py` with `exact-correction-preparation` and with `candidate-validation` on the 8 targets, run from a 125cfacc1 export → `ALLOW`, exit 0 ×8 each. The register has a header and no rows.

### Scratch
My directory is `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4prev.fBQ70G`. It keeps `out_3488/`, `out_e548/` and `neg_3488.out`. I deleted only the export copies inside it.

## Disposition (WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| N1 NON-BLOCKING (DEL-10-03 "this run's brief") | Repaired with the DEL-03-04 wording ("was directed on 2026-07-25 by the brief of the run that authored this deliverable's first contract under `D-PEC-63`"), backed by two claims at `774317e30` (the first contract's commit, 2026-07-25). Re-hashed, act script re-rendered, checks rerun; re-verified in verdict 04 |
| N2 NON-BLOCKING (STATUS.md omitted) | Repaired: the source-state bullet names `docs/STATUS.md` (PR #982) |
| N3 NON-BLOCKING (`tools.md` hash) | Repaired: `fbd07771…5cc7` |
| Note 1 (fifteen) | Repaired: "Of the fifteen contracts (thirteen, plus DEL-02-08/09)", and DEL-04-02's two flags are named as its own text |
| Note 2 (origin/main moved) | Repaired: the draft names the final check commit |
| Note 3 (DEL-10-11 destination; CLM-014) | Repaired: the consequence row names DEL-10-11 `CLM-014` and suggests the graph record it for a later DEL-10-11 currency pass |
| Note 4 (AC order) | Recorded; valid, no change |
| Note 5 (REVISE mentions) | Recorded; no change (disclosure, provenance of the brief rule, limit) |
