<!-- PACKET
id: P-15
cluster: CL-15
title: Execution-root scaffolding returns 501 on the live path
question: Should the live App scaffold execution roots from a decomposition again, or is scaffolding no longer an App operation?
recommended: A: compose the scaffold port; fix text
depends_on: P-04, P-13, P-09
decision_type: owner; engineering; WORKING_ITEMS (scope-change)
tier: GOVERNING
-->
# P-15 — Execution-root scaffolding returns 501 on the live path

Cluster CL-15 · live-path finding XPF-044 · draft by TASK D3 for HELP_HUMAN review; not a ruling.

**Question.** DEL-07-02 promises that the App builds a project's execution-root folders from an accepted decomposition, through `POST /api/harness/scaffold`. The route is still served, but on the live path it always answers 501 "adapter unavailable". No ruling or recorded direction drops the feature. Should it work again (code), or is scaffolding no longer an App operation (text and scope)?
- **P-15.a** (21 rows): the scaffold rows (DEL-07-02 and the decomposition SOW-024/025 rows).
- **P-15.b** (7 rows): two other services the live Runtime does not compose:
  - the CI wrapper's need for a Runtime binding (DEL-09-01);
  - provider-key storage and status (DEL-09-06).

## What we found
- `RuntimeService.scaffold` throws `ENGINE_UNAVAILABLE` 501 when no scaffold port is supplied (`projects/chirality-runtime/packages/core/src/runtime-service.ts:118,619-624`). The App-owned composition passes `undefined` in that position (`projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts:226`). [code]
- The scaffolding module still exists (`frontend/src/lib/harness/scaffold.ts`), but only tests use it. The adapter that joined it to the old in-process host was removed in the D-GOV-43 spike (`39c0bb6ab`; XPF-044). [code]
- Three statements do not address scaffolding:
  - D-GOV-43 lists what it retires: daemon, supplier admission, fixed-policy control, residency;
  - D-APP-127 names what it supersedes;
  - neither mentions scaffolding (`docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`; `_REGISTER.md` D-APP-127 row).

  Both DEL-07-02 blind workers and SOW-024.2 found no record dropping it. [GOVERNING]
- K-HIER-1 still names the "scaffold service" as its enforcement (`docs/CONTRACT.md` §1.1). [GOVERNING]
- DEL-09-06's key-storage rows fail for a similar reason: the live credential store's `set()` is offline (`app-owned-composition.ts:225`). They also turn on the Anthropic API-key UI, which is the subject of R4-Q6 (P-04). [code]

## Affected rows
<!-- COUNTS -->
**28 rows are decided in this packet** (PRIMARY); 8 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-15`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT | 1 | 1 |  |  |  | 2 |
| PKG-07 | 14 | 3 |  | 1 | 1 | 19 |
| PKG-09 |  | 3 | 1 | 3 |  | 7 |
| **Total** | **15** | **7** | **1** | **4** | **1** | **28** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-15.a: 21 rows — Written, not built 15, Partly built 4, Text out of date 1, To-do list out of step 1
- P-15.b: 7 rows — Partly built 3, Text out of date 3, Built differently 1

ALSO/CONTEXT members by Disposition: Built differently 2, Partly built 2, Written, not built 2, Governing texts disagree 1, Text out of date 1.

<!-- /COUNTS -->
All rows carry "no owner decision needed" as sealed. They are "Written, not built" or "Partly built" because the served route cannot run. The split is by deliverable (`R4/_work/SUBQ/P-15_subq.csv`, rule in `d3_subq_small.py`).

## Options
**A. Change the code.** Compose a scaffold port in the App-owned Runtime from the existing module, with its containment and instruction-root checks. *R5 would:* repair the stale rows now (e.g. `DEL-07-02#CLM-014.1`, `#STATE-1`). The 501 rows wait on a separate implementation brief, then are re-verified.

**B. Change the deliverable text.** Scaffolding moves to the agent-run `project-setup` workflow, and the App no longer serves it. *R5 would:* re-word DEL-07-02 accordingly. A scope-change handoff retires the route and adjusts SOW-024/025.

**C. Structural.** Retire DEL-07-02 or merge it into a workflow deliverable. This is a scope-change handoff to WORKING_ITEMS; R5 changes nothing structural.

**D. Defer.** Keep the rows held and add an honest `_STATUS` Remaining item.

For **P-15.b**: DEL-09-01 takes a text fix (the prerequisite "server bound to the Runtime service"). The DEL-09-06 key rows follow the P-04 answer on the Anthropic key path.

## HELP_HUMAN recommendation (draft)
**P-15.a: option A.**
- A served endpoint that always fails is a product defect, not a text defect.
- The logic already exists, so composing it is a bounded change.
- No ruling chose to drop it.

If the owner sees scaffolding as agent work under the Codex workflows, B plus C is the clean alternative. Then the route should be removed rather than left answering 501.

**P-15.b:** text fix for DEL-09-01; DEL-09-06 follows P-04.

## Who decides
The owner decides whether scaffolding stays an App operation. Composing the port is an engineering matter. The code to change is Runtime code (`runtime-service.ts` and `app-owned-composition.ts` under `projects/chirality-runtime/packages/`), so its implementation brief is issued in the **Runtime project loop**, with an App slice only if the App route or its tests change. That code change is outside this App run's write authority. Retiring the route or the deliverable is WORKING_ITEMS (scope-change). The text and scope-change parts are within your App authority.

## On ruling
1. HELP_HUMAN records the ruling in the consolidated R4 ruling record: the next free D-APP ID, with its register row.
2. The R5 tranche managers for PKG-07, PKG-09 and EXT (SOW rows) edit the P-15 PRIMARY key set in `PACKET_INDEX.csv`, by SubQ.
3. Under A, a `software-bounded-implementation` brief, issued in the Runtime project loop, composes the port, and the 501 rows wait on its landing and a fresh re-verification. Under B or C, a scope-change handoff goes to WORKING_ITEMS.
4. R6 backchecks every listed row. There is no lifecycle transition.

## Risks, contested rows and dependencies
- The fact sheet has no contested rows.
- A composed port must also meet the containment and instruction-root rows in P-13 (`DEL-07-02#CLM-004.1`, `#CLM-018`, `#CLM-024`).
- Dependencies:
  - **P-04:** the DEL-09-06 key rows;
  - **P-13:** containment;
  - **P-09:** `scaffold.ts` sits in the legacy harness folder.
