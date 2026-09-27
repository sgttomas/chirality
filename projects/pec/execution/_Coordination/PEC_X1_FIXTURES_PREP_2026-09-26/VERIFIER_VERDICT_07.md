# X1 preparation verdict 07

Reviewer: fresh read-only `pec-reviewer` TASK (agent `adb8715c05df8893e`, Opus 5.5 as reported by the host), verifying the repair delta `4f2e4f44a..c49817153` made for HELP_HUMAN's PR #996 review. Transcribed verbatim by WORKING_ITEMS; dispositions appended after the report.

Reviewed head: `c49817153`.

---

VERDICT: FAIL

The eight repairs HELP_HUMAN asked for are all done. Repair 1 added a new parser-output rule, and that rule conflicts with the corpus the packet itself pins and with the contracts' rule against silent omission. It is owner-facing text that Q3 recommends confirming, so I rate it blocking until the draft is repaired. The draft-only fix is small. No candidate byte and no act byte changed.

Reviewed HEAD: `c49817153119d5bb6dcf6111628e5c105e078006` (branch `claude/pec-x1-fixtures-proposal`; `origin/claude/pec-x1-fixtures-proposal` points at the same commit). Base: `4f2e4f44a`, which merges `6ab42ec4b` with `f0a6159c9`.

## Findings

**1. BLOCKING — the parser-output path rule fails faithful output of cited paths that no longer exist.**
- **Where:** `DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md` line 68 (the "Parser output (for the parser packets)" bullet) and line 409 (Q3, "checked instead as a path that resolves").
- **Condition:** the draft says path fields are checked as "a normalized path that resolves in the examined tree. A path field that does not resolve … fails."
- **Evidence from the pinned corpus:**
  - FC-2 DEL-12-01 `MEMORY.md` (pinned blob `7c683795c…` at `d61981ee2`) cites these at lines 11, 31 and 33, and none exists at `d61981ee2`:
    - `execution/_Coordination/DEV-001_DISPATCH_DEL-12-01.md`
    - `execution/PKG-12_Security, Privacy, and Private Data Handling/…/DEL-12-01_…/Specification.md` (it contains spaces)
    - `…/Guidance.md`
  - `git ls-tree` confirms that folder has no `Specification.md` or `Guidance.md`.
  - FC-1 DEL-08-01 (`15dcfee1`, line 103) cites `execution/_Coordination/DEV-001_DISPATCH_DEL-08-01.md`, which is also missing at `d61981ee2`.
  - The packet's own synthetic case SYN-MEM-08 (`links_in_each_form_*.md`) uses the relative link `../../../_Coordination/WorkGraphs/SYN-RUN-MEM-0821/SYN_GRAPH.md`. It can never resolve.
- **Impact:**
  - DEL-02-09 REQ-003 and DEL-02-08 REQ-007 require link targets to be emitted as normalized repository-relative paths. DEL-02-09 REQ-007 and DEL-02-08 REQ-009 prohibit silently omitting a field.
  - A parser that follows those rules would fail the no-source-text assertion, even for a single-token path with no word run at all. That contradicts the draft's own "single tokens … never trip it".
  - Resolving a project-relative citation such as `execution/…` also needs a normalization choice, which Limits (line 397) says "stay open".
  - Once confirmed, this threshold binds the parser packets: DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign it to this packet.
- **Remediation direction:** check path fields by type and shape (a normalized repository-relative path with no link text and no URL), not by whether the target exists. Alternatively, state that non-resolving cited paths are still emitted and exempt by type, or leave resolution to the parser packets. Update line 68 and Q3 to match.

**2. NON-BLOCKING — the return still carries values from before the repair.**
- **Where:** `returns/X1P_FIXTURES_PROPOSAL.md`.
- **Stale values:**
  - Line 11: the draft SHA-256 is given as `c43dbb9f…95e3`, the draft at `6e5622c24`. The actual draft is `7d4d3d3c865d0d6dc9734051fa79f74a79df4c9fc7a8b062086f0c41538c6e16`.
  - Line 12: `SHA256SUMS` "covers the 87 tracked files … `45854c55…49d5`". It now covers 110 files, and its SHA-256 is `b8e6649d0fec2a839610708f8368a2d1047b739216d6790e85158301ad098d8a`.
  - Line 6: "content base `6e5622c24`" is stale.
  - Line 90: "thresholds that DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign to this packet" still makes both thresholds TBD-assigned, against repair 2.
  - The check-results section cites only `run_main`, not `run_origin_main`.
- **Remediation direction:** refresh these values when the return is next touched.

**3. NON-BLOCKING — Limits still groups the copy threshold with the TBD-assigned items.**
- **Where:** draft line 397.
- **Condition:** it says "other than the golden format, pinned blobs and thresholds … DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign those". The plural takes in the copy threshold, which line 69 and Q3 now say no TBD assigns.
- **Remediation direction:** name the no-source-text threshold as the TBD-assigned item and list the copy threshold separately as the operational test of REQ-017 / REQ-014 / REQ-017.

**4. NON-BLOCKING — the new rerun allowance is not carried through Rollback and Finite verification.**
- **Where:** grant (line 204) and "Second run" (line 322) against Rollback "During execution" (line 377) and Finite verification row 1.
- **Conditions:**
  - Rollback says "Under A alone, a failed act or later check leaves nothing to keep; discard the branch or worktree". The grant says the rolled-back run "is recorded in the run root" and may be rerun.
  - Under A + L, L's `_STATUS.md` changes are committed before the act. On a rerun, row 1's precondition "the three `_STATUS.md` at their tabled preimages" cannot hold, and the draft does not say how rows 1 and 1a apply to a rerun.
  - An exit 1 at preflight with a target not at its preimage (drift) is not stated as consuming or not consuming the grant.
- **What is consistent:** the act semantics themselves match. Exit 1 comes either from a preflight failure with nothing written or after a full rollback. Exit 2 means an incomplete rollback. A second run after success is refused, because the new directory exists and targets are off their preimages.
- **Remediation direction:** align the Rollback wording, and add one sentence on rows 1 and 1a for a rerun under A + L.

**5. NON-BLOCKING — the Preparation evidence list omits the new folder.** Draft around line 436 lists `evidence/` with `run_main/` but not `evidence/run_origin_main/`. Line 186 does cite it.

**6. INFORMATIONAL.**
- An ignored, untracked `__pycache__/apply_x1p.cpython-313.pyc` (00:31) sits in the prep folder. It is not covered by `SHA256SUMS` and I did not create it.
- Three pinned Piping blobs have `## Remaining TBDs` headings: FC-1 DEL-08-01, FC-2 DEL-10-04 and FC-2 DEL-12-01. The suite reads them only as whole blobs for grounding and copy checks, not as sections. The FX-PEC-0 bullet speaks only of PEC blobs. Disclosing this is optional; it predates the delta.
- The path example "lines 53, 105 and 175" is accurate. Line 176 contains the path as well.

## Per-item table

| # | Repair | Status | Evidence |
|---|---|---|---|
| 1 | No-source-text path treatment | Done (introduced finding 1) | The single-token path claim is gone. Body lines 65–68 and Q3 cover goldens, manifests and parser output. `git rev-parse d61981ee2:<DEL-08-01 MEMORY path>` = `15dcfee1a37d…`; the path appears at lines 53, 105, 175 (and 176). In the test module, `json_text_runs` (line 206) skips `.path`/`.tree` leaves, and it is called only by the copy check (line 485). The golden check does not exempt them. Only the pinned MANIFEST has such leaves, and those values are pinned paths and tree locators checked through Git. |
| 2 | TBD scope wording | Done (finding 3 residual; return line 90 stale) | Contract texts at `f0a6159c9` (unchanged since `6c6cc1b00`): DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign the threshold to "their own packet". DEL-02-08 TBD-006 says "fixed by no accepted source". DEL-02-08 REQ-017, DEL-02-09 REQ-014 and DEL-02-03 REQ-017 each say "contain no text copied from another loop's files". Body line 62/69 and Q3 state this plainly. |
| 3 | Runner whitespace | Done | `tr` replaced by `paste -sd ' ' -`. No trailing whitespace in any committed or rerun evidence file. `shasum -a 256 -c SHA256SUMS`: all OK. `SHA256SUMS` covers exactly the tracked files. `git diff --check origin/main...HEAD` and `4f2e4f44a HEAD`: clean. |
| 4 | Pin currency | Done | All 17 pins and 2 templates equal at their commits and are ancestors of `f0a6159c9`. All unchanged at `6c6cc1b00`. At `f0a6159c9` only `FX-PEC-0.graph` differs: `8e32fc0fd` against pinned `bf0b0c626`. Draft line 152 and return line 94 match this. |
| 5 | Remove the retired-word scan | Done | The runner's hygiene check no longer has the word check. The draft's offer is replaced by line 111. The Limits bullet now includes preparation aids. `grep -i remaining` finds nothing in any candidate or in `software-workflow.json`. The only aid hits are `claims/quotes.json`, checked by `verify_x1p_claims.py`. That script only confirms that four quoted strings occur verbatim in `WORK_GRAPH.md`, `Impact_Assessment.md` and `Propagation_Plan.md` at `6c6cc1b00` and in the draft. It reads no `_STATUS.md` and looks for no section, so reading it as a fidelity check and not a section scan is correct. The drafter briefs' historical instruction is not a scan. |
| 6 | Single-run semantics | Done (finding 4 residual) | Grant line 204 and "Second run" line 322 match `apply_x1p.template.py`: preflight exit 1 writes nothing; rollback exit 1 restores the preimages and leaves no temporary file; exit 2 means incomplete rollback. |
| 7 | COMMON copy | Done | `briefs/COMMON_PREP_RULES_2026-09-26.md` SHA-256 `51b70e46…b311`, and `cmp` shows it identical to scratchpad `acts2/COMMON.md`. Cited in the draft status line and in return line 3. Only this PR branch has the file. |
| 8 | Scratch fallback when TMPDIR is unset | Done | All four aids fall back to `.scratch/` beside the script: `run_x1p_checks.sh` (line 10), `run_fixture_suite.sh` (line 10), `negative_controls_x1p.py` (line 13, `mkdtemp(dir=…)`) and `test_apply_x1p.py` (line 30, `TemporaryDirectory(dir=…)`; `os` is imported). No `/tmp` literal remains. The runner passes `TMPDIR="$SCRATCH"` to its children. I ran a copy of `run_fixture_suite.sh` in my directory with `env -u TMPDIR`: 10 tests OK, scratch created under `fb/.scratch` and removed, nothing written to `/private/tmp`. |

## What I checked
- Read the brief, Root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`, and the full `git diff 4f2e4f44a HEAD`.
- **Scope of the delta:** 39 files, all under the prep folder or `AgentRuns/.../briefs|returns`. `origin/main...HEAD` touches only X1 coordination paths.
- **No candidate or act change:**
  - The delta does not touch `candidates/`, `apply_x1p.py`, `build_apply_x1p.py` or `apply_x1p.template.py`.
  - `apply_x1p.py` SHA-256 is `452ff66af71b7d3de9814301a8e45ca070137d5e577b4e73c202b713d2102428`.
  - Regenerating it with `build_apply_x1p.py` into my directory at `6c6cc1b00`, `f0a6159c9` and HEAD gives byte-identical output (`cmp`).
  - The `software-workflow.json` preimage `8ec9ba6d…` is still current at `f0a6159c9`.
- **Aid hashes:** the draft's aid table matches the live bytes (`test_apply_x1p.py` `5585a6f1…`, `run_x1p_checks.sh` `88193621…`, `run_fixture_suite.sh` `5ffca7d4…`, `negative_controls_x1p.py` `5a9ccf10…5c1a`; the other aids are unchanged).
- **Full rerun:** `zsh <prep>/run_x1p_checks.sh <worktree> f0a6159c9 <prep> <mydir>/out_f0a` exited 0 in 3m16s, OVERALL PASS:
  - act 0/0/rerun refused 1; containment 34 creates and 1 modify;
  - 6 registered checks exit 0; `v2-parsers` 10 tests OK;
  - bindings 442/442; pins 19/19; claims and quotes 67/67;
  - strict, harness and receipts identical before and after (strict exit 1);
  - hygiene PASS; fault injection 11/11; negative controls 20/20.
  - The summary matches the committed `evidence/run_origin_main/SUMMARY.out` line for line. Other outputs differ only in scratch paths and timings.
- Checked the new text for consistency with Limits, Q3, the verifier checklist, Finite verification, Rollback and the return (findings 1–5).

My directory: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1r4.QHmmBn` (contains `build_6c6cc1b00/`, `build_f0a6159c9/`, `build_HEAD/`, `out_f0a/`, `run_f0a.log`, `fb/`). I wrote nothing in any worktree, did no checkout, used no network, and made no repairs.

Key paths:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/X1P_FIXTURES_PROPOSAL.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/COMMON_PREP_RULES_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/candidates/projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py`

---

## Dispositions (WORKING_ITEMS)

1. **BLOCKING — repaired.** In the parser-output rule (body) and in Q3, a path field is now exempt from the word count by its type and checked by shape: one normalized repository-relative path, no link text, no URL. Whether the file exists is explicitly not checked. The draft cites the pinned FC-2 DEL-12-01 and FC-1 DEL-08-01 examples, the synthetic link targets, and the contract rules requiring emission (DEL-02-09 REQ-003, DEL-02-08 REQ-007) and forbidding silent omission (DEL-02-09 REQ-007, DEL-02-08 REQ-009). Normalization stays each parser's declared choice.
2. **Repaired.** The return is refreshed with the new head, draft hash, `SHA256SUMS` count and hash, the corrected threshold scope, and both evidence runs.
3. **Repaired.** The Limits bullet now names two settlements. The first is the golden format, pinned blobs and no-source-text threshold (TBD-assigned for DEL-02-03 and DEL-02-09, proposed for DEL-02-08). The second is the no-copied-text threshold, which no TBD assigns (the operational test of DEL-02-08 REQ-017, DEL-02-09 REQ-014 and DEL-02-03 REQ-017).
4. **Repaired.** Rollback "During execution" now carries the rerun allowance. It states that a preflight exit 1 writes and consumes nothing and that drift is routed to the owner. Under A alone, the branch is discarded only if the act is abandoned, after the failure is recorded. Row 1a now says that on a rerun it is not repeated and row 1's `_STATUS.md` precondition becomes the tabled add-on L postimages.
5. **Repaired.** The Preparation evidence list names `evidence/run_origin_main/`.
6. **Informational, noted.** The ignored `__pycache__` is untracked and outside `SHA256SUMS`. It came from importing the act module in a hash listing and is not a deliverable. The Piping blobs' own headings are read only as whole blobs for grounding and copy checks; nothing reads them as sections or scans for them.
