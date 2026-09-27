# SCA-APP-012 checkpoint group 3 — accepted audited poststate, with the code candidate

Recorded 2026-09-27 by WORKING_ITEMS, a bounded Claude Code subagent. The
coordinating session relayed the owner's act. This record faithfully
transcribes that act under K-AUTH-1. It is not a new request for the same
decision, and it claims no inspection the owner did not perform.

## What the owner had in front of them

The coordinating session reports that the owner accepted the candidate on
PR #1020 at commit `ac67109d931eb5a4609bc5ad7c656ac938f6f15b` (branch
`claude/brave-goodall-wj3hok`). That branch merges `origin/main`; the merged
commits change only `projects/pec/**` and `projects/chirality-piping/**`. Its
App content equals the evidence tree `974bf7da4..eb4470a22`: the scope text,
the code change and the group-3 evidence. The coordinating session also
reports that the independent group-3 review and its confirmation found no
blocking finding.

The group-3 presentation is
`SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/RUN_SUMMARY.md`
at that commit. Its top section is "Checkpoint group 3 — what you will be asked
to decide". It lists what acceptance authorizes, in order: the decision
folder, E26 with `_LATEST.md` and the status records in one finalize run, the
post-acceptance record, one merged PR, and the post-acceptance handoffs. It
reports no group-3 correction and no basis refresh of an edited file.

## The owner's act (verbatim)

Typed in the chat on 2026-09-27, as relayed verbatim by the coordinating
session:

> I accept SCA-APP-012 checkpoint group 3

The owner gave no corrections.

## Interpretation (recording role's reading, not owner text)

| Item | Effect |
|---|---|
| Audited poststate | The integrated candidate at `ac67109d9` is accepted: the scope text (79 of 80 edits in 12 files, E26 withheld) and the code change of `Propagation_Plan.md` §4, reviewed jointly (Q-a). The candidate files, the evidence and the code records are bound by hash in `ACCEPTED_MANIFEST.csv` |
| Corrections | None. There is no group-3 correction and no basis refresh of an edited file |
| Acceptance-conditional list | `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` is applied exactly, in order: this folder first, then `Evidence/Group3/group3_finalize.py` with `{APPLICATION_DATE}` = `2026-09-27` and the owner's act above, then the `_PostAcceptanceValidation/` record |
| Plain acceptance | The plain-acceptance post-images in `Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md` and `HANDOFF_STATE_POSTIMAGE.md` apply |
| Supersession | The 22 `Supersession_Delta.csv` bindings take effect, through the accumulated `Supersession_Map.csv`, when `_LATEST.md` names this snapshot |
| Closure | The verdict stays `OPEN_PENDING_DERIVATIVE_CLOSURE` until the downstream handoffs complete |

## What this acceptance authorizes and does not authorize

It authorizes:
- this decision folder;
- E26, the `_LATEST.md` move to SCA-APP-012 and the status records, through
  `Evidence/Group3/group3_finalize.py`;
- the `_PostAcceptanceValidation/` record;
- updating the code records from "awaiting acceptance" to accepted;
- one PR landing the scope text and the code together, once CI and review
  have no blocking finding (the standing Git authorization governs the merge
  mechanics);
- the downstream handoffs: `project-setup` in `INCREMENTAL` mode,
  `dependency-extract` with `analyze_dep_closure` (DX-01, DX-02, DX-03,
  DX-05), `audit-decomp`, `audit-scope-closure` and the TM-APP-051 note.

It does not authorize:
- any lifecycle transition or `_STATUS.md` change;
- any dependency-register or Task Management write in this change;
- any edit not on the acceptance-conditional list;
- any release, signing, publication or reliance claim.

## Basis

- Accepted group-1 snapshot `checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`
  (`DECISION.md` `0bc055869d3b29f6fc719ad8eb376f580073eaabafd5f75faa1978d10cbc6abe`).
- Accepted group-2 snapshot `checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`
  (`DECISION.md` `d828e975c3e0d313a49d0b65980462047b506342586c3260af860f4cc3d5d428`,
  `ACCEPTED_MANIFEST.csv` `0574aca5909331732e5791eea8ef023cd6b2fb5f1a7f45f024acb8443cce6ac9`).
- `_LATEST.md` before the move names SCA-APP-011 (SHA-256
  `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637`).
- Evidence base: `origin/main` `974bf7da4`; PR branch head `ac67109d9`.
