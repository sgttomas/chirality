# SCA-APP-012 — Post-acceptance status records (exact post-images)

These are acceptance-conditional items 4 and 5 in `ACCEPTANCE_CONDITIONAL_EDITS.csv`. None of these edits is applied before group-3 acceptance. `Evidence/Group3/group3_finalize.py` applies them, together with E26 and `_LATEST.md`, and this file is rendered from its constants (`--render`; `--check` confirms it).

**Slot rule.** Three slots are filled, and nothing else changes.
- `{APPLICATION_DATE}` is the date of the group-3 decision folder `checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/`.
- `{OWNER_ACT_VERBATIM}` is the owner's words exactly as quoted (after `> `) in that folder's `DECISION.md`. Any `"` inside them is kept.
- `{UTC}` (Handoff_State.md only) is the suffix of `_PostAcceptanceValidation/SCA-APP-012_{UTC}/`.

These post-images fit a plain acceptance of this package. If the owner amends or returns group 3, they do not apply, and the records return to the owner's act.

## 1. `Brief.md`, line 3 (status line)

Before: the line starting with `**Status:** `CHECKPOINT_GROUP_2_ACCEPTED` —` (the group-2 status line; its wording after that prefix may be updated while the candidate is integrated).

After (exact line):

```text
**Status:** `CHECKPOINT_GROUP_3_ACCEPTED` — the owner accepted checkpoint group 1 on 2026-09-27 ("Accept SCA-APP-012 group 1: R-b, W-b, P-keep (keeping the two pages, as recommended), defaults."; `../checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`), checkpoint group 2 on 2026-09-27 ("Accept SCA-APP-012 group 2: T-a, Q-a."; `../checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`) and checkpoint group 3 on {APPLICATION_DATE} ("{OWNER_ACT_VERBATIM}"; `../checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/`). Revision 4 of this brief is bound at SHA-256 `3924974af3cd4ffe81169b6f8654657e9e880181d8a217747158255ad8c56d49` (the bytes before this status line changed). This folder is the active snapshot named by `_LATEST.md`.
```

## 2. `Decision_Log.md`, the G3 row

Before: the one line starting with `| G3 | — | Checkpoint group 3 |`.

After (exact line):

```text
| G3-ACCEPT | {APPLICATION_DATE} | Checkpoint group 3 | "{OWNER_ACT_VERBATIM}" | Audited poststate accepted with the code candidate (Q-a); E26, `_LATEST.md` and these records applied by `Evidence/Group3/group3_finalize.py` as listed in `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` | `checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/` |
```

## 3. `Handoff_State.md`

Before: a file whose first line is `# SCA-APP-012 — Handoff State (group-3 CANDIDATE)`.

After: the whole file replaced by `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md` with the three slots filled.
