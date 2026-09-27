# SCA-APP-011 — Post-acceptance status records (exact post-images)

This is acceptance-conditional item 5 in `ACCEPTANCE_CONDITIONAL_EDITS.csv`.
None of these edits is applied before group-3 acceptance.

**Slot rule.** Two slots are filled, and nothing else changes.
- `{APPLICATION_DATE}` is the date of the group-3 decision folder
  `checkpoint_snapshots/SCA-APP-011_GROUP-3_{APPLICATION_DATE}/`.
- `{OWNER_ACT_VERBATIM}` is the owner's words exactly as quoted in that
  folder's `DECISION.md`. Any `"` inside them is kept.

These post-images fit a plain acceptance of this package. If the owner
amends or returns group 3, they do not apply, and the records return to the
owner's act.

## 1. `Brief.md`, line 3 (status line)

Before (exact line):

```text
**Status:** `CHECKPOINT_GROUP_2_ACCEPTED` — the owner accepted checkpoint group 1 on 2026-09-27 ("I accept SCA-APP-011 checkpoint group 1"; `../checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`) and checkpoint group 2 on 2026-09-27 ("Accept SCA-APP-011 group 2: W-a, Q-a, with the revision-2 corrections and row 29."; `../checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`). The group-3 candidate is ready for the owner's decision (`RUN_SUMMARY.md`); nothing is accepted as the active poststate and `_LATEST.md` is unchanged.
```

After (exact line):

```text
**Status:** `CHECKPOINT_GROUP_3_ACCEPTED` — the owner accepted checkpoint group 1 on 2026-09-27 ("I accept SCA-APP-011 checkpoint group 1"; `../checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`), checkpoint group 2 on 2026-09-27 ("Accept SCA-APP-011 group 2: W-a, Q-a, with the revision-2 corrections and row 29."; `../checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`) and checkpoint group 3 on {APPLICATION_DATE} ("{OWNER_ACT_VERBATIM}"; `../checkpoint_snapshots/SCA-APP-011_GROUP-3_{APPLICATION_DATE}/`). This folder is the active snapshot named by `_LATEST.md`.
```

## 2. `Decision_Log.md`, the G3 row

Before (exact line):

```text
| G3 | — | Checkpoint group 3 | Awaiting owner: the candidate poststate and `RUN_SUMMARY.md` (presentation at top), reviewed jointly with the code candidate (Q-a) | — | — |
```

After (exact line):

```text
| G3-ACCEPT | {APPLICATION_DATE} | Checkpoint group 3 | "{OWNER_ACT_VERBATIM}" | Audited poststate accepted with the code candidate (Q-a), including correction G3C-01 and basis refresh G3B-01; E47, `_LATEST.md`, the Runtime notice and these records applied as listed in `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` | `checkpoint_snapshots/SCA-APP-011_GROUP-3_{APPLICATION_DATE}/` |
```

## 3. `Handoff_State.md`

Replace the whole file with `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md`,
filling the slots above. The file also has a third slot, `{UTC}`: the name
suffix of the `_PostAcceptanceValidation/SCA-APP-011_{UTC}/` record.
