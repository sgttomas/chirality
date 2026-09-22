<!-- PACKET
id: P-07
cluster: CL-07
title: Who is the actor on status transitions
question: Is a caller-supplied actor string enough to authorize human-gated lifecycle transitions, or must the human gate be carried by something the agent cannot assert?
recommended: B: text states the limit; P-14 decides mechanism
depends_on: P-09, P-14
decision_type: owner (incl. App governance amendment); engineering
tier: GOVERNING
-->
# P-07 — Who is the actor on status transitions

Cluster CL-07 · named question R4-Q3 · draft by TASK D3 for HELP_HUMAN review; not a ruling.

**Question.** Lifecycle transitions to human-gate states (CHECKING, ISSUED) are allowed when the actor is `HUMAN` and an approval SHA is given. Both the legacy `status_transition` tool and the live route take the actor as a string the caller supplies, so an agent can name itself `HUMAN`. Is that enough, or must the gate rest on something the agent cannot assert?

## What we found
- CONTRACT K-GATE-1 says human gates are non-delegable and need accountable human evidence. K-STATUS-2 says transitions are "actor-authorized", with approval-SHA evidence at human gates (`docs/CONTRACT.md:44,109`). [GOVERNING]
- D-APP-13 allowed MCP-driven CHECKING/ISSUED transitions "only with actor `HUMAN` and valid `approvalSha`", and ruled the SHA "required and sufficient" (`_DECISIONS/D-APP-13_RULING_2026-06-16.md:24-26`). It does not say who may assert `HUMAN`. [GOVERNING]
- D-APP-56 P19 replaced the old `startsWith('HUMAN')` check with an explicit actor allowlist. It called this "the product's core authority boundary" (`_DECISIONS/D-APP-56_RULING_2026-07-12.md:60`). The allowlist landed (`DEL-07-04#CLM-011.17`, "Matches"). The mapped value is still a string the caller asserts. [GOVERNING]
- The legacy tool's schema takes `actor: z.string().min(1)` straight from the agent's call (`frontend/src/lib/harness/mcp/read-tools.ts:1125-1136`). This is legacy harness code, and the live path registers no Chirality tools (P-09). [code]
- The live route reads `actor` from the request body (`frontend/src/app/api/working-root/deliverable/status/transition/route.ts:52-62`). XPF-043 records that the SHA is checked for format only. [code]
- A Codex agent in workspace-write mode can also edit `_STATUS.md` directly, bypassing both tool and route (`DOC:RELIANCE#3.6` notes). [run finding]
- `DEL-07-04#CLM-011.13` is marked "Governing texts disagree": D-APP-13 ("SHA sufficient") against unamended K-AUTH-1/K-GATE-1 (only humans approve). [run finding]

## Affected rows
<!-- COUNTS -->
**13 rows are decided in this packet** (PRIMARY); 0 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-07`.

| Package | Matches (`ALIGNED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|
| EXT |  | 4 |  |  | 4 |
| PKG-06 |  |  | 2 |  | 2 |
| PKG-07 | 1 | 5 |  | 1 | 7 |
| **Total** | **1** | **9** | **2** | **1** | **13** |

<!-- /COUNTS -->
All 13 rows are in DEL-07-04 (status transition), DEL-06-04 (write tools) and the reliance register (`DOC:RELIANCE` RB-LIFECYCLE, RB-HUMAN-GATE). Each states that a human gate is enforced. Four rows also cite R4-Q1, because the tool form of the gate exists only in legacy code.

## Options
**A. Accept the divergence.** The actor string plus approval SHA is enough; the gate rests on the human reviewing the record. *R5 would:* record the acceptance in the listed rows and cite D-APP-13. `DEL-07-04#CLM-011.13` then needs a governance amendment reconciling K-GATE-1 with D-APP-13.

**B. Change the deliverable text to state the limit.** The text would say that the actor is asserted, not verified, and that the human gate is procedural. The owner rules in P-14 whether a mechanism is added later. *R5 would:* edit the 13 rows to say so, marking the legacy tool as compatibility (per P-09).

**C. Change the code.** The gate would rest on a human act the agent cannot perform, such as a UI confirmation in the main process or a signed approval. *R5 would:* hold the rows until a separate implementation brief lands.

**D. Defer** until P-14 is ruled.

## HELP_HUMAN recommendation (draft)
Option B now, with the mechanism decided once in P-14.
- R4-Q3 as framed concerns the legacy tool, which the live path does not expose. Its fate follows P-09.
- The live route has the same weakness, and P-14 is where a live mechanism is chosen.
- Stating the limit honestly repairs the text without claiming a guarantee the product lacks.
- Accepting the divergence (A) would contradict D-APP-56 P19's own description of the actor check as the core authority boundary.

Left open: whether D-APP-13's "required and sufficient" still stands once the actor is known to be asserted. That is a governance-amendment question for `DEL-07-04#CLM-011.13`.

## Who decides
The owner decides the authority question, and any governance amendment of K-GATE-1 or K-STATUS-2 against D-APP-13. A code mechanism is an engineering matter, through a separate implementation brief.

## On ruling
1. HELP_HUMAN records the ruling in the consolidated R4 ruling record: the next free D-APP ID, with its register row.
2. The R5 tranche managers for PKG-07, PKG-06 and EXT (the reliance register) edit the P-07 PRIMARY key set in `PACKET_INDEX.csv`.
3. Any code goes to a separate `software-bounded-implementation` brief; under option C the rows wait on it.
4. R6 backchecks every listed row. There is no lifecycle transition.

## Risks, contested rows and dependencies
- The fact sheet has no contested rows.
- `DEL-07-04#CLM-011.17` is "Matches" at module level. Its note records that the value is still caller-asserted.
- Dependencies:
  - **P-14:** its live-route rows are the same mechanism; rule the two together.
  - **P-09:** decides whether the legacy tool itself is compatibility or history.
