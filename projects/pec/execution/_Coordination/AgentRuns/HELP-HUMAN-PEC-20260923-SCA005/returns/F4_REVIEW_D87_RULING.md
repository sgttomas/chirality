# F4 — independent review of the D-PEC-87 ruling record (PR #890)

Reviewer: fresh read-only TASK, dispatched by HELP_HUMAN for node G5 with host `subagent_type: pec-reviewer` (`model: opus`, reported as `claude-opus-5-5`, high effort per definition). The reviewer cannot write files; HELP_HUMAN transcribes its return here. Role identity is instruction-asserted.

## Cycle 1 — reviewed `1707258b547a1162d86c5572cbe25c26acdd8fc5` (base `3c3adae355739b2ad24acdb33d3b5422bb36db95`)

Verdict: **FAIL** (two MAJOR, three MINOR, five NOTE). Both MAJORs are record-accuracy findings, one an authority attribution and one an unrecorded review claim, fixable by rewording; the reviewer found the recording itself sound.

Passed: all quotes byte-identical to the owner's message; item 3 treated as discussion only; CHECKING neither granted, scheduled nor listed as an owner gate; product grant not enlarged (seven paths, unopened `__init__.py`, limits, model default all match the proposal); all eight preimages and the proposal hash `ba3d3e64…4569` match at base, HEAD and working tree; proposal bytes unchanged; register row column count matches neighbours; receipts validator exit 0; Examined-Through ancestor; Parent-Receipt `Receipt-181`; no lifecycle token in Pointers; decomposition registers `--strict` 0/0; `git diff --check` exit 0; five files exactly.

| Sev | Location | Finding | Disposition (HELP_HUMAN, cycle-1 repair commit) |
|---|---|---|---|
| MAJOR | ruling, publication clause | said the owner's approval authorized the `docs/STATUS.md` lines; the proposal contains no STATUS clause and D-PEC-85 set no such precedent | clause now limits the approval to the decision record and register row; STATUS/README lines stated separately as HELP_HUMAN present-current maintenance under the I-5 reading used at G3, with the clean-revert caveat |
| MAJOR | `RUN.md` G3 row | claimed "review PASS on the final head" of PR #888, but no review of `0d7435ec4` was recorded | the cycle-3 final-candidate confirmation of `0d7435ec4` (PASS) did occur in this session but had not been transcribed; it is now appended to `returns/F3_REVIEW_CP1_ACCEPTANCE.md` and the G3 row cites the full sequence |
| MINOR | `docs/STATUS.md`; `RUN.md` C2 row | L-1a described in terms that fit L-1b (tick tied to the slice landing) | STATUS now says L-1a authorizes the tick independently of the slice's completion; C2 row notes bundling is a work-organization choice |
| MINOR | Receipt 182 Checks | no exit code and no review verdict | exit codes recorded; points to this file for the verdict sequence |
| MINOR | `README.md` status line | "obligations awaiting owner disposition" now stale | refreshed under the same maintenance warrant |
| NOTE | `_REGISTER.md` D-PEC-87 row | stray ".;" | fixed |
| NOTE | `RUN.md` heading | line break rendered as double space | rendered as " / " |
| NOTE | `docs/STATUS.md` header | refresh note omitted the D-PEC-87 refresh | added |
| NOTE | ruling, L-1a history line | cites "this ruling" in addition to the reports and triage | no change; harmless, not an enlargement |
| NOTE | Receipt 182 Model-Attribution | reviewer's agent type unverifiable by the reviewer | reworded to state the dispatch used `subagent_type: pec-reviewer` and the model the host reported |

## Cycle 2 — backcheck of `4971e0e6ffe7b707cc976533403ec3d0e2495c1b`

Verdict: **PASS** (four NOTE; no MINOR or higher).

All ten cycle-1 dispositions confirmed present in the bytes, and the table above confirmed a faithful summary. Publication clause confined to the decision record and register row; STATUS/README warrant labelled as HELP_HUMAN maintenance, not an owner grant. No CHECKING or D-PEC-87 entry in the STATUS owner-gate list. Receipts validator VALID exit 0 and `--strict` registers exit 0, run in a scratch clone at `4971e0e6`; no lifecycle token in Receipt 182 Pointers; `git diff --check` exit 0; eight files exactly. The PR #888 cycle-3 transcription was checked against git: file counts, `Decision_Log.md` hash and commit timing are consistent, though the reviewer cannot itself confirm the review occurred.

| Sev | Finding | Disposition |
|---|---|---|
| NOTE | F3 cycle 3 rests only on HELP_HUMAN's late transcription | none; the section already states it was transcribed late |
| NOTE | `RUN.md` F3 row stopped at cycle 2 | cycle 3 added |
| NOTE | "wording" understated the two MAJORs | reworded here, in `RUN.md` G5 and in Receipt 182 |
| NOTE | STATUS/README warrant rests on HELP_HUMAN's own reading of D-PEC-86 I-5, now used three times | none now; raised with the owner as a question about a standing currency warrant |

## Cycle 3 — final-candidate confirmation

Requested for the head that carries this transcription; appended below when returned.
