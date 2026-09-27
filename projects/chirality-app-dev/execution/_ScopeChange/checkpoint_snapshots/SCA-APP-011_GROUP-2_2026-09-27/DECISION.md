# SCA-APP-011 checkpoint group 2 — accepted exact amendment and propagation plan

Recorded 2026-09-27 by WORKING_ITEMS, a bounded Claude Code subagent. The
coordinating session relayed the owner's act. This record faithfully
transcribes that act under K-AUTH-1. It is not a new request for the same
decision, and it claims no inspection the owner did not perform.

## What the owner had in front of them

The coordinating session reports that the owner was given the group-2 package
at commit `b0295688cab484ee1c3756dd04c04ba6302e05d8`. That is revision 2
(`b20e1d87e`, the fixes from the independent group-2 review) plus the
coordinator's follow-through commit. The coordinator reports that the
independent reviewer confirmed that revision with no blocking findings.

The package's top section is "Checkpoint group 2 — what you are asked to
decide" in
`SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/Propagation_Plan.md`.
It contains:
- "What accepting group 2 authorizes";
- "Corrections in revision 2", items 1–5;
- "The change in one screen";
- "Choices that remain", choices W and Q.

The exact text is `Amendment_Preview.md`, and the register is
`Amendment_Actions.csv`. Both are bound in `ACCEPTED_MANIFEST.csv`.

## The owner's act (verbatim)

Typed in the chat on 2026-09-27:

> Accept SCA-APP-011 group 2: W-a, Q-a, with the revision-2 corrections and row 29.

## Interpretation (recording role's reading, not owner text)

| Item | Effect |
|---|---|
| Exact amendment | The 127 edits in `Amendment_Preview.md`, generated from `Evidence/Group2/amendment_edits.py`, in 16 files. 126 are written into the group-3 candidate. E47 (`{APPLICATION_DATE}`) is acceptance-conditional and waits for group-3 acceptance |
| Register | `Amendment_Actions.csv`: 29 rows (28 MODIFY, 1 ADD); `ScopeChanging` YES on 23; `SupersessionBindingPresent` YES on 15. This is the authoritative action register |
| Supersession | The 18 rows of `Supersession_Delta.csv`, accumulated onto the SCA-APP-010 map at group 3 |
| W-a | This amendment writes the exact text of all 16 files at group-3 preparation, within the write boundary of `Propagation_Plan.md` §2 |
| Q-a | Group 3 reviews the written scope-text candidate together with the rebased code candidate (`Propagation_Plan.md` §4). After group-3 acceptance, one change lands both |
| Revision-2 corrections | Items 1–5 of "Corrections in revision 2": (1) the M-a truth correction on tool ownership, (2) the missed scaffold-route obligations, (3) stale text, (4) Journey 7.3, (5) the candidate/finalize procedure. Item 1 follows the accepted M-a substance with corrected wording. Live exposure of the read tools (`status_read`, `deps_read`, scaffold preview) is DEL-06-03's open work. `status_transition` and `deps_write` remain retained, governed operations with no live registration, and any live registration of them is governed by DEL-06-04-REQ-010. `Decision_Log.md` G1-NOTE-1 records the correction; the group-1 snapshot is unchanged |
| Row 29 | **Reopened group-1 item, decided by this act.** Register row 29 (MODIFY DEL-07-01, `ScopeChanging` YES, no supersession binding, no intake row) extends the impact set accepted at group 1. This act reopens that part of group 1 and accepts DEL-07-01 into the amendment, limited to edits E125–E127. Those edits remove the retired scaffold and contract routes from DEL-07-01's list of root consumers. Its root-validation obligation is unchanged |
| Unchanged from group 1 | BASE, DQ-R, S-c; D restate; set L excluded; E no change; scaffold library kept |

The owner gave no other correction.

## What this acceptance authorizes and does not authorize

It authorizes checkpoint-group-3 preparation from this snapshot:
- writing the group-3 candidate with
  `build_amendment_preview.py --candidate` (every edit except E47);
- generating the candidate `Supersession_Map.csv`, `Post_Change_Coverage.json`,
  `RUN_SUMMARY.md` and `Handoff_State.md` in the SCA folder;
- the post-change validation and the independent review;
- preparing the code change of `Propagation_Plan.md` §4 for the joint group-3
  review (Q-a).

It does not:
- apply E47;
- move `_LATEST.md` or any other pointer;
- send the Runtime notice;
- change any `_STATUS.md`, lifecycle state or `Dependencies.csv`;
- merge the code change;
- authorize any release.

Each of those waits for checkpoint group 3 or a later owning workflow.
`_LATEST.md` stays on SCA-APP-010 until group-3 acceptance.

## Basis

At the act:
- decomposition v3.2 (SHA-256
  `9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6`);
- companion register (SHA-256
  `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`);
- `_LATEST.md` naming SCA-APP-010 (SHA-256
  `6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3`);
- the accepted group-1 snapshot `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`
  (`DECISION.md` `412c78c2…9fa9`; `ACCEPTED_MANIFEST.csv` `d7f96a8b…3e545`).

Every edited file's preimage hash is recorded in
`Evidence/Group2/PREIMAGE_POSTIMAGE.csv`.

Group-3 pointer posture: `ACCEPTED_PREDECESSOR` (SCA-APP-010).
