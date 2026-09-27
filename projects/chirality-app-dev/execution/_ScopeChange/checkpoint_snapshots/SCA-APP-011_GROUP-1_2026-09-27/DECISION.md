# SCA-APP-011 checkpoint group 1 — accepted proposed change and impact

Recorded 2026-09-27 by WORKING_ITEMS, a bounded Claude Code subagent. The
coordinating session relayed the owner's act. This record faithfully
transcribes that act under K-AUTH-1. It is not a new request for the same
decision, and it claims no inspection the owner did not perform.

## What the owner had in front of them

The coordinating session reports that it sent the owner revision 2 of
`SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/Impact_Assessment.md`
(candidate commit `7874316cb3bef8f7e9409ff902198b2e49712853`). Its top section,
"Please accept, correct or return group 1", lists what acceptance covers.

The owner had already answered choices A, B, D and S earlier the same day
through the AskUserQuestion tool. Those answers are recorded verbatim in that
snapshot's `Brief.md`, section "Owner's stated selections":
- A: "Rescope it (Recommended)"
- B: "Exclude it (Recommended)"
- D: "Restate them (Recommended)"
- S: "Remove the route too"

## The owner's act (verbatim)

Typed in the Claude Code chat on 2026-09-27:

> I accept SCA-APP-011 checkpoint group 1

The owner gave no corrections.

## Interpretation (recording role's reading, not owner text)

The owner accepted without corrections. Under the package's own acceptance
section, the acceptance therefore covers these items, and no others:

| Item | Effect |
|---|---|
| BASE | Intake rows 1–19 accepted as the basis for group 2 |
| DQ-R | Intake row 20: DEL-02-02 rescoped by MODIFY; DQ-X (rows 21–27) not selected |
| S-c | Intake rows 33–40: `POST /api/harness/scaffold` retired with its client function and App port member |
| D | Restate PRD FR-011/FR-012, Journey 7.5 and success metric 7 as presentation-neutral dispatch semantics |
| L | Set L (rows 28–32) excluded; the loop-first shell stays |
| E | No change to CONTRACT or companion-register enforcement wording |
| M-a | Name the library and the Chirality tool contracts as the interface; state that live Codex exposure is DEL-06-03's open work; name the Root tools as today's agent path |
| S-lib | The App scaffold library `frontend/src/lib/harness/scaffold.ts` and its tests are kept |

This yields 28 register rows at group 2 (27 MODIFY, 1 ADD). Topology stays
10 packages / 52 deliverables / 84 scope items / 10 objectives.

## What this acceptance authorizes and does not authorize

It authorizes the preparation of the checkpoint-group-2 package only:
- the exact amendment text;
- the propagation plan and write boundary;
- `Amendment_Actions.csv`;
- `Supersession_Delta.csv`.

It applies no change to any of the following:
- the decomposition or the companion register;
- the PRD, SPEC or PLAN;
- any Scope of Work, `_CONTEXT.md`, `_STATUS.md` or dependency register;
- `_LATEST.md`;
- code.

It authorizes no lifecycle, dependency, release or merge act. The code
removal merges only after checkpoint group 3 is accepted, as the owner's
direction of 2026-09-27 set out.

## Basis

Upstream at the act:
- accepted decomposition v3.2 (SHA-256
  `9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6`);
- companion register (SHA-256
  `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`);
- active pointer `_LATEST.md` naming SCA-APP-010 (SHA-256
  `6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3`).

These remain current during group-2 preparation.
