# SCA-APP-012 checkpoint group 2 — accepted exact amendment and propagation plan

Recorded 2026-09-27 by WORKING_ITEMS, a bounded Claude Code subagent. The
coordinating session relayed the owner's act. This record faithfully
transcribes that act under K-AUTH-1. It is not a new request for the same
decision, and it claims no inspection the owner did not perform.

## What the owner had in front of them

The coordinating session reports that the owner was given the group-2 package
at commit `a4295f9ed61204ab76af3a9164a03fc0c4772c6f`. That is revision 2: the
first package (`68127fa8e`, `4c572475f`) plus the fixes N1–N9 from the
independent review of `4c572475f`, which found no blocking issue.

The coordinating session also reports, as its own statement and not the
owner's words, that the owner gave the act **while a confirmation review of
`4c572475f..a4295f9ed` was still running**. The coordinating session undertook
to bring any finding of that review to the owner.

The package's top section is "Checkpoint group 2 — what you are asked to
decide" in
`SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Propagation_Plan.md`.
It contains:
- "What accepting group 2 authorizes";
- "Points to note before you decide", items 1–5;
- "The change in one screen";
- "Choices that remain", choices T and Q.

Its §12 lists the revision-2 corrections N1–N9. The exact text is
`Amendment_Preview.md`, and the register is `Amendment_Actions.csv`. Both are
bound in `ACCEPTED_MANIFEST.csv`.

## The owner's act (verbatim)

Typed in the chat on 2026-09-27, as relayed verbatim by the coordinating
session:

> Accept SCA-APP-012 group 2: T-a, Q-a.

The owner gave no corrections.

## Interpretation (recording role's reading, not owner text)

| Item | Effect |
|---|---|
| Exact amendment | The 80 edits in `Amendment_Preview.md`, generated from `Evidence/Group2/amendment_edits.py`, in 12 files. 79 are written into the group-3 candidate. E26 (`{APPLICATION_DATE}`) is acceptance-conditional and waits for group-3 acceptance |
| Register | `Amendment_Actions.csv`: 24 rows (23 MODIFY, 1 ADD); `ScopeChanging` YES on 15; `SupersessionBindingPresent` YES on 14. This is the authoritative action register |
| Supersession | The 22 rows of `Supersession_Delta.csv`, accumulated onto the SCA-APP-011 map at group 3 |
| T-a | This amendment writes the exact text of all 12 files at group-3 preparation, within the write boundary of `Propagation_Plan.md` §2 |
| Q-a | Group 3 reviews the written scope-text candidate together with the code candidate of `Propagation_Plan.md` §4. After group-3 acceptance, one change lands both |
| Revision 2 | The corrections N1–N9 of `Propagation_Plan.md` §12, including the hardened `--candidate` gate (N5) and the code-specification details N1–N4. Only E05 changed in the exact text |
| Points to note | Items 1–5 of "Points to note before you decide": basis refresh G1B-01, the sweep additions within accepted rows, the three controlling sections, the two fixed test names, and the superseded SCA-APP-011 DEL-07-02 text |
| Unchanged from group 1 | BASE, S, R-b, W-b, P-keep; the defaults L-lib, S-tool and E; the KG-033 acknowledgment |

## What this acceptance authorizes and does not authorize

It authorizes checkpoint-group-3 preparation from this snapshot:
- writing the group-3 candidate with
  `build_amendment_preview.py --candidate` (every edit except E26);
- generating the candidate `Supersession_Map.csv`, `Post_Change_Coverage.json`,
  `RUN_SUMMARY.md` and `Handoff_State.md` in the SCA folder;
- the post-change validation and the independent review;
- preparing the code change of `Propagation_Plan.md` §4 for the joint group-3
  review (Q-a).

It does not:
- apply E26;
- move `_LATEST.md` or any other pointer;
- change any `_STATUS.md`, lifecycle state, `Dependencies.csv` or the Task
  Management register;
- merge the code change;
- authorize any release.

Each of those waits for checkpoint group 3 or a later owning workflow.
`_LATEST.md` stays on SCA-APP-011 until group-3 acceptance.

## Basis

At the act (branch head `a4295f9ed` on `origin/main` `974bf7da4`):
- decomposition v3.2 (SHA-256
  `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876`);
- companion register (SHA-256
  `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`);
- `_LATEST.md` naming SCA-APP-011 (SHA-256
  `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637`);
- the accepted group-1 snapshot `checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`
  (`DECISION.md` `0bc05586…6abe`; `ACCEPTED_MANIFEST.csv` `86b0f7cb…7056`).

Every edited file's preimage hash is recorded in
`Evidence/Group2/PREIMAGE_POSTIMAGE.csv`, and all equal the current tree.

Group-3 pointer posture: `ACCEPTED_PREDECESSOR` (SCA-APP-011).
