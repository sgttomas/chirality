# D-APP-114 — Handoff hygiene: DAG control pointer, Remaining markers, one stale reference, two loop clauses, and retirement of the workplan overlay

Status: RULED (owner direction in chat 2026-09-05)

Owner: Ryan Tufts

Date: 2026-09-05

## Owner directions (verbatim)

<!-- BEGIN OWNER DIRECTION VERBATIM -->
make that small repair now, commit, and merge via PR.  And can you clean up the rough edges in the same PR?  If you need clarification from me, ask for it.
<!-- END OWNER DIRECTION VERBATIM -->

Asked how the stale focus text in `loop/WORKPLAN_2026-09-04_app_dev_loop.md` should be handled (mint a 2026-09-05 overlay; leave it as a receipt-recorded delta; retire the overlay entirely), the owner selected:

<!-- BEGIN OWNER DIRECTION VERBATIM -->
Retire the overlay entirely
<!-- END OWNER DIRECTION VERBATIM -->

## Effect (HELP_HUMAN's reading; the owner may amend by reply)

1. **DAG control pointer.** `PKG-00/1_Working/DAG_CLOSURE_CONTROL.md` names `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034` as the current closure snapshot (it had named the 2026-07-11 snapshot after the D-APP-111 pointer move) and carries one section recording the D-APP-109/110/111 sequence.
2. **Remaining markers normalized, no scope change:** DEL-05-05 and DEL-08-04 packet-preparation items marked `SELECTABLE` with the clause that no packet file exists yet; DEL-03-01 packet item marked `SELECTABLE`, with routing of the D-APP-76 Root ruling request named as an owner-granted Root write (`NOT_SELECTABLE_UNTIL: owner grants Root write scope`); DEL-09-04 daemon-deploy item marked `NOT_SELECTABLE_UNTIL: owner act`. One dated history line per carrier.
3. **Stale reference.** DEL-09-02-V3-01 `Depends` now records that the AT-053 evidence item DEL-01-01-V3-01 landed (Receipt 209) instead of citing it as open.
4. **Two loop clauses** in `loop/LOOP_INIT.md`: the product-source checks row notes that build, premerge, and render-bar runs need host escalation per `AGENTS.md` where the sandbox denies them; the A1 re-stage bullet names the receipt's `Checks` record as the declaration's home. Candidate SHA-256 `cdbf6e685ecb4d754cbf0028e42cc8ad3bb467c473ebdf08cd59df93b7ae5bcf`.
5. **Workplan overlay retired.** The seven `loop/WORKPLAN_*.md` files are moved byte-identically (`git mv`, hashes below) to `plans/workplans/`, the historical archive, so the committed-HEAD loader finds no plan and the loop runs on the deliverables alone under D-APP-106. No file is edited or deleted; ruled plans stay immutable at their new path. The `WORKPLAN_2026-09-04` overlay's owner-intent and parked-lane text is not lost: the intent is carried by the rulings it cited and the parked lanes by the items' own markers. The §2 archive pointer in `loop/LOOP_INIT.md` names the new location.

Moved files (SHA-256 unchanged):

    90269a0b87829aa551eb6768e1c3fff56e56c456b0c468707181a49a8bb9a646  WORKPLAN_2026-07-04_app_dev_loop.md
    7cfd2066697b0613c1c32eefd991554f1d7215cfbf459825224ebee728cbceb7  WORKPLAN_2026-07-10_app_dev_loop.md
    51b887ecb49072b1185aaae057e8845863d134645fdec51bb58ca4e5df76ddd0  WORKPLAN_2026-07-17_app_dev_loop.md
    bbe65869f96ae415cbb64c0019a4943f160df676d7739adc42b8871536753ea0  WORKPLAN_2026-07-18_app_dev_loop.md
    d94a01911365773c6d2423880d949738e96f9afd31373bd24c57f1960ebf8ee8  WORKPLAN_2026-07-18b_app_dev_loop.md
    d7210fe68ec832b91c553d982fb34c48ff7257e9bd028cfc0571e411f5c514ac  WORKPLAN_2026-09-03_app_dev_loop.md
    9e2373b190bd1cafeb4b49df04c0d6fcf8982b825188a4bb2362d5326c712f44  WORKPLAN_2026-09-04_app_dev_loop.md

## What this ruling does not do

No fence, check, pointer-target, product, lifecycle, dependency-register, or release change. No item is added, removed, widened, or narrowed; the markers state what the items already said in prose. Selection of any seated item remains a later act under `loop/LOOP_INIT.md`.

## Attribution

Transcribed and applied by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) acting as HELP_HUMAN (Agent 0) in an untyped Claude Code session. Role not mechanically enforced.
