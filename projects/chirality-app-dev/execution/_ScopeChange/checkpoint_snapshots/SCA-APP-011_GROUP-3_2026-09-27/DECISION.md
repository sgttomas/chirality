# SCA-APP-011 checkpoint group 3 — accepted audited poststate, with the code candidate

Recorded 2026-09-27 by WORKING_ITEMS, a bounded Claude Code subagent. The
coordinating session relayed the owner's act. This record faithfully
transcribes that act under K-AUTH-1. It is not a new request for the same
decision, and it claims no inspection the owner did not perform.

## What the owner had in front of them

The coordinating session reports that the owner replied to two things:
- the group-3 presentation,
  `SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/RUN_SUMMARY.md`
  at commit `d48c785c5cb116a1614bf70784b2a116eca7f814` (branch
  `claude/brave-goodall-wj3hok`);
- draft PR #995.

The presentation's top section is "Checkpoint group 3 — what you will be asked
to decide". It lists what acceptance authorizes, in order: the decision
folder, E47, `_LATEST.md`, the Runtime notice, the status records, one merged
PR, and the post-acceptance handoffs. It also presents the corrections G3C-01
and G3B-01 (`Evidence/Group3/G3_CORRECTIONS.md`), and it records the
independent review of `3d8ead912` with no blocking findings.

## The owner's act (verbatim)

Typed in the chat on 2026-09-27:

> I accept SCA-APP-011 checkpoint group 3

The owner gave no corrections.

## Interpretation (recording role's reading, not owner text)

| Item | Effect |
|---|---|
| Audited poststate | The integrated candidate at `d48c785c5` is accepted. That is the scope text (126 edits in 16 files) and the code change of `Propagation_Plan.md` §4, reviewed jointly (Q-a). The candidate files and evidence are bound by hash in `ACCEPTED_MANIFEST.csv` |
| G3C-01 | Accepted. It reopens and replaces one sentence of accepted edit E13 in the DEL-07-04 Scope of Work (line 24) |
| G3B-01 | Accepted. It refreshes the App SPEC basis after main changed an unrelated paragraph; there is no text change |
| Acceptance-conditional list | `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` is applied exactly, in order, from its templates, with `{APPLICATION_DATE}` = `2026-09-27` |
| Plain acceptance | The plain-acceptance post-images in `Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md` and `HANDOFF_STATE_POSTIMAGE.md` apply |
| Closure | The verdict stays `OPEN_PENDING_DERIVATIVE_CLOSURE` until the downstream handoffs complete |

## What this acceptance authorizes and does not authorize

It authorizes:
- this decision folder;
- E47 through `Evidence/Group3/group3_corrections.py --finalize`;
- the `_LATEST.md` move to SCA-APP-011;
- the Runtime notice;
- the status records and the `_PostAcceptanceValidation/` record;
- one PR landing the scope text and the code together, once CI and review
  have no blocking finding (the standing Git authorization governs the merge
  mechanics);
- the downstream handoffs: `project-setup` in `INCREMENTAL` mode,
  `dependency-extract` with `analyze_dep_closure`, `audit-decomp` and
  `audit-scope-closure`.

It does not authorize:
- any lifecycle transition or `_STATUS.md` change;
- any dependency-register write in this change;
- any edit not on the acceptance-conditional list;
- any release, signing, publication or reliance claim.

## Basis

- Accepted group-1 snapshot `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/`
  (`DECISION.md` `412c78c28db13c245b8c8ebb58ad418c73fb63182dbb4ccfb085343dae449fa9`).
- Accepted group-2 snapshot `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/`
  (`DECISION.md` `0b1a2b24f8b60a8d86694f34c35a2c4918308c99f0e1d58afad3ae289c4673eb`,
  `ACCEPTED_MANIFEST.csv` `ef3129871c9d8971d5c47e36a5c2973bf24366c847b58daad73ec5adaf261c7e`).
- `_LATEST.md` before the move names SCA-APP-010 (SHA-256
  `6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3`).
- Integration base: `origin/main` `4087a4f8c`.
