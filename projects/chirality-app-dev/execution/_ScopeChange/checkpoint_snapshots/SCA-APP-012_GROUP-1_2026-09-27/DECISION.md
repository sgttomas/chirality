# SCA-APP-012 checkpoint group 1 — accepted proposed change and impact

Recorded 2026-09-27 by WORKING_ITEMS, a bounded Claude Code subagent. The
coordinating session relayed the owner's act. This record faithfully
transcribes that act under K-AUTH-1. It is not a new request for the same
decision, and it claims no inspection the owner did not perform.

## What the owner had in front of them

The coordinating session reports that it sent the owner revision 4 of
`SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Impact_Assessment.md`
(commit `4f2d79ec9710a13f6a86c7dce82592406618ff2a`; the same bytes were later
rebased as `47a62467481a9b853f90ec6285ade4605dde92fe`). Its top section,
"For the owner: checkpoint group 1", includes:
- "What accepting group 1 authorizes" (BASE, S, the choices and the
  defaults, group-2 drafting);
- "One departure from what you approved", which states that the approved
  proposal listed the `/workbench` and `/pipeline` pages for retirement and
  that the recommended P-keep departs from it;
- the choices R, W and P, and the defaults L-lib, S-tool and E;
- "One point to acknowledge" (the PRD §6.4 preconditions and KG-033).

The coordinating session also reports that the owner asked for an explanation
of each recommendation and received it before answering. That report is the
coordinating session's, not the owner's words. It is recorded so that the
P-keep departure is shown to have been accepted knowingly.

## The owner's act (verbatim)

Relayed verbatim by the coordinating session from the Claude Code
conversation of 2026-09-27:

> Accept SCA-APP-012 group 1: R-b, W-b, P-keep (keeping the two pages, as recommended), defaults.

The owner gave no corrections.

## Interpretation (recording role's reading, not owner text)

The act uses the suggested-reply form of the package. Under the package's own
acceptance section, it covers these items, and no others:

| Item | Effect |
|---|---|
| BASE | Intake rows 1–18 accepted as the basis for group 2: retire the loop-first compatibility UI (the shells, the role-directory panel, the discarded `legacy` prop, the `?legacy=1` link and its only test), `DeliverablesProvider` and `GET /api/working-root/scope`; record the separate owner decision that PRD KG-033, PRD §6.4, SPEC §17.9 and D-APP-74 L107 require; correct the PRD, SPEC and PLAN passages that still call the loop-first shell live; restate DEL-02-03-REQ-010, the DEL-07-03 scope-route mentions and the DEL-08-03 API label |
| S | Intake rows 19–21: no App-side scaffold entry and no write-capable scaffold tool is planned (DEL-07-02, DEL-06-03 CLM-031, SPEC §14.2, PRD goal 17, §6.1, FR-119 and §8.13) |
| R-b | Intake row 22: DEL-02-03-REQ-009 retired as history, with the routing wording only it carried; DEP-02-03-009 expected to retire at re-extraction (DX-01). R-a (rows 23–25) not selected |
| W-b | Intake rows 26–27: the unmounted flat-file workflow view, its detail and test, and `GET /api/working-root/workflow` with its store, contract and test are retired; the read route joins every API-preservation clause the scope route joins. W-a (row 28) and W-c not selected |
| P-keep | `/workbench` and `/pipeline` stay as unlisted URL-compatibility entries into the dialogue shell; only their dead `legacy` element goes. P-r and P-d (rows 29–35) not selected. This departs from the approved proposal, which listed both pages for retirement; the owner's words "keeping the two pages, as recommended" accept that departure. D-APP-108 Q3 stands |
| Defaults: L-lib | Both portal helpers (`lib/portal/agent-matrix-launch.ts`, `agent-matrix-cells.ts`) are deleted; registry case 1 of `agent-matrix-cells.test.ts` is ported into `persona-resolution.test.ts`; a new role-picker guard test for `chat-panel.tsx` L2124 is added (Impact Assessment §3.3, §3.4) |
| Defaults: S-tool | SPEC §14.2 `mcp__chirality__scaffold` and PRD goal 17, §6.1, FR-119 and §8.13 narrowed to the read-only scaffold preview (row 21) |
| Defaults: E | No change to CONTRACT or companion-register wording |
| KG-033 acknowledgment | Unchanged from the package: the retirement does not wait for the packaged Desktop evidence of the dialogue shell, which stays open under its current owners |

This yields **24 register rows at group 2** (intake rows 1–22 and 26–27: 23
MODIFY, 1 ADD). Topology stays 10 packages / 52 deliverables / 84 scope items
/ 10 objectives. The dependency expected outcomes (DX-01, DX-02, DX-03,
DX-05; DX-04 applies only under P-x), the TM-APP-051 handoff and the code
specification (Impact Assessment §15, under W-b and P-keep) go to the group-2
propagation plan, not the register.

## What this acceptance authorizes and does not authorize

It authorizes the preparation of the checkpoint-group-2 package only:
- the exact amendment text;
- the propagation plan and write boundary, with the code specification;
- `Amendment_Actions.csv`;
- `Supersession_Delta.csv`.

It applies no change to any of the following:
- the decomposition or the companion register;
- the PRD, SPEC or PLAN;
- any Scope of Work, `_CONTEXT.md`, `_STATUS.md` or dependency register;
- the Task Management register;
- `_LATEST.md`;
- code.

It authorizes no lifecycle, dependency, release or merge act. The code
removal waits for checkpoint group 3, as in SCA-APP-011.

## Basis

Upstream at the act (package basis `adc8bdae18b2e1e48dcf01a304cc055d2cbf84e0`):
- accepted decomposition v3.2 (SHA-256
  `cf6e56ebb1474d30a45dd3973dcb449d8aab30a84d731649336091afd2321876`);
- companion register (SHA-256
  `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`);
- active pointer `_LATEST.md` naming SCA-APP-011,
  `OPEN_PENDING_DERIVATIVE_CLOSURE` (SHA-256
  `904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637`).

These remain current during group-2 preparation. The group-2 package is
prepared at `origin/main` `830913331` (PRs #1015 and #1016). Every input
hashed in the accepted `Brief.md` is byte-identical there; the one change to
a register the baseline reads is recorded as basis refresh G1B-01 in
`Handoff_State.md` and the SCA-APP-012 `Decision_Log.md`.
