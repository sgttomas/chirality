<!-- PACKET
id: P-14
cluster: CL-14
title: Human gate on the live status-transition route
question: On the live path, is the human gate for lifecycle transitions documented as a procedural limit, or built so an agent cannot perform it?
recommended: D — text now; mechanism C when a transition UI returns
depends_on: P-07, P-09, P-06
decision_type: owner; engineering
tier: GOVERNING
-->
# P-14 — Human gate on the live status-transition route

Cluster CL-14 · live-path finding XPF-043 (related to R4-Q3, P-07) · draft by TASK D3 for HELP_HUMAN review; not a ruling.

**Question.** The live transition route accepts an actor and an approval SHA from whoever calls it. The only screens that call it (Workbench and Pipeline) are no longer shown. Should the product (A) document the human gate honestly as procedural, or (C) gain a mechanism an agent cannot perform?

## What we found
- Human gates are non-delegable (K-GATE-1). Transitions to human-gate states need approval-SHA evidence (K-STATUS-2) (`docs/CONTRACT.md:44,109`). [GOVERNING]
- The route takes `actor` and `approvalSha` from the request body (`frontend/src/app/api/working-root/deliverable/status/transition/route.ts:52-62`). XPF-043 records that the SHA is checked for format only. [code]
- The only UI callers of the transition client are `components/workbench/workbench-surface.tsx` and `components/pipeline/pipeline-surface.tsx` (via `lib/workspace/deliverable-api.ts:226`). Neither is rendered: every route renders the dialogue shell (`components/woven-dialogue/woven-dialogue-route.tsx:18`, `void legacy`). [code]
- SCA-APP-010 and D-APP-108 permit retiring the Workbench and Pipeline presentation while keeping the code (`R3/RUNWIDE_CALLS.md` (e)). No ruling moves the human gate elsewhere. [GOVERNING]
- Most of the 13 PRIMARY rows are text defects that need no ruling. Examples:
  - `DEL-07-04#REGISTER-2` and `#CLM-008` name modules that never existed;
  - `DEL-07-06#CLM-018` and `#CLM-025` still say "REF-006 is MATCH" (REF-006 is the recorded SHA-256 of the App `docs/PRD.md` in `_REFERENCES.md`, which no longer matches the PRD at the frozen commit);
  - `DEL-07-04#CLM-011.4` predates the SPEC §4.3 human-authorized reversals. [run finding]
- The substance, a gate enforced on the live path, sits mostly in the 44 ALSO rows (DEL-07-04, DEL-06-04). Those are decided in P-07 and P-09. [run finding]

## Affected rows
<!-- COUNTS -->
**13 rows are decided in this packet** (PRIMARY); 44 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-14`.

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Total |
|---|---:|---:|---:|
| PKG-01 | 2 |  | 2 |
| PKG-07 | 4 | 6 | 10 |
| PKG-10 | 1 |  | 1 |
| **Total** | **7** | **6** | **13** |

ALSO/CONTEXT members by Disposition: Partly built 22, Governing texts disagree 7, Text out of date 6, Written, not built 6, Built differently 2, Verification out of date 1.

<!-- /COUNTS -->
The 13 PRIMARY rows state gate, parser, schema-fixture or containment facts about the status and scanner surfaces. They all carry "no owner decision needed" (`HumanDecisionNeeded = NO`). Their repair is text, except the three "Partly built" rows that describe the gate itself (`DEL-01-03#CLM-004`, `DEL-07-03#CLM-017`, `DEL-10-05#CLM-009.1`). Those three follow the A/C answer.

## Options
**A. Change the deliverable text.** Correct the false facts. State that the live route's actor and SHA are caller-asserted, and that the gate is a human procedure. *R5 would:* edit the 13 PRIMARY rows. The ALSO rows follow P-07 and P-09.

**B. Accept the divergence.** Rule that the caller-asserted gate is sufficient. *R5 would:* record the acceptance in the gate rows.

**C. Change the code.** Add a live human-only confirmation, for example a main-process dialog or signed approval, and check the approval SHA against content. *R5 would:* repair the stale text now. The gate rows wait on a separate implementation brief. D-APP-66 (SHA revalidation) is prior art.

**D. Defer** the mechanism. Repair the text now and reopen when a transition UI returns to the live shell.

## HELP_HUMAN recommendation (draft)
Option D: repair the text now (as in A), and record C as the mechanism to build if a transition UI returns to the live shell.
- No live screen performs transitions today, so no user relies on a live gate.
- The honest repair is to say so, and to correct the false facts.
- A code gate built now would guard an entry point no shipped screen uses.

Left open: whether the reliance register (RB-LIFECYCLE, RB-HUMAN-GATE) should list the direct `_STATUS.md` edit a Codex agent can make as a residual risk. That depends on P-09.b and P-13.

## Who decides
The owner decides whether the gate may be procedural. A code mechanism is an engineering matter, through a separate implementation brief. None of this is outside the App's authority.

## On ruling
1. HELP_HUMAN records the ruling in the consolidated R4 ruling record: the next free D-APP ID, with its register row.
2. The R5 tranche managers for PKG-07, PKG-01 and PKG-10 edit the P-14 PRIMARY key set in `PACKET_INDEX.csv`.
3. Under C, a `software-bounded-implementation` brief follows, and the three gate rows wait on it.
4. R6 backchecks every listed row. There is no lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-06-04#CLM-027` (ALSO; decided in P-09) was refuted by S1-112: "Text out of date" or "Built differently".
- Dependencies:
  - **P-07:** the same mechanism as the legacy tool; rule the two together.
  - **P-09:** whether the legacy tool is compatibility or history.
  - **P-06:** R4-Q4 covers the retired Pipeline surface. D-APP-108 already permits unmounting the Workbench and Pipeline presentation.
