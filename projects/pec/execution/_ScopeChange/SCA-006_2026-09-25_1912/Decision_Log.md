---
amendment_id: SCA-006
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_checkpoint_group: 1
status: checkpoint_1_awaiting_owner
---

# SCA-006 Decision Log

Only decisions that actually occurred are recorded as decided. Every other
row is `AWAITING_OWNER` or `NOT_STARTED`. Agent recommendations are not
rulings. The owner accepts checkpoint group 1, if at all, by the exact
SHA-256 values quoted in row SCA006-CP1 (a file cannot quote its own hash;
the Impact Assessment and action-register hashes are quoted here and in the
run return).

| DecisionRef | Checkpoint | Decision | Status | Authority |
|---|---|---|---|---|
| SCA006-G1 | Gate 1 intake | Open SCA-006 (SOFTWARE variant) under `chirality-root:bundled:workflow:scope-change` to amend PEC's reliance text: PRD PEC-K-03, §8 (agents, access classes, direct query through tool calls), §9 reliance envelope and response-size budgets, §12 reliance gate, and the `projects/pec/AGENTS.md` K-02 gloss | `OPENED BY OWNER DIRECTION` | `D-PEC-90` R-A grant item 3 and the owner's direct-query answer (verbatim below); `D-PEC-94` direction (verbatim below); precondition met by `D-PEC-92` (SCA-005 checkpoint 2 accepted 2026-09-25) |
| SCA006-CP1 | 1 | Confirm or modify the parsed change set (`Amendment_Actions.csv`, SHA-256 `a8e600e3ea3969d2421d4bd670e599b73ad2535b1d7364214d7e6ddef548a902`, 54 PROPOSED actions) and accept `Impact_Assessment.md` at SHA-256 `c2ad7c417c96c87fb8c96fb0b0e6fb7474abb675ec0366b8daa7ba32fd888a72`, together with the owner items below | `AWAITING_OWNER` | — |
| SCA006-CP1-DQ | 1 | Direct query through tool calls: (a) specify now with a read-only `agent` access class; (b) specify now, riding the `harness` class; (c) defer behind a new §16 access-class decision | `AWAITING_OWNER` | manager recommends (a) |
| SCA006-CP1-ENV | 1 | Reliance envelope: (a) new PEC-ORI-007 mapped to DEL-04-03; (b) fold into PEC-ORI-003 | `AWAITING_OWNER` | manager recommends (a) |
| SCA006-CP1-BUD | 1 | Response-size budgets: (a) new PEC-API-006 mapped to DEL-08-03, numeric values confirmed at P1; (b) fold into PEC-API-004 | `AWAITING_OWNER` | manager recommends (a) |
| SCA006-CP1-GATE | 1 | Reliance gate: (a) standing gate for any release that advertises operational reliance, with SOW-100 and a new DEL-10-13; (b) bind to the P1 exit test and extend existing deliverables | `AWAITING_OWNER` | manager recommends (a) |
| SCA006-CP1-INS | 1 | `projects/pec/AGENTS.md` route: (a) carried at checkpoint 3 as an instruction tranche with its own manifest and notices; (b) a separate instruction tranche after checkpoint 3 | `AWAITING_OWNER` | manager recommends (a) |
| SCA006-CP1-RC | 1 | Confirm that R-C (PEC output citable as authority) stays excluded | `AWAITING_OWNER` | excluded under `D-PEC-90` (the owner selected R-A); the confirmation records it for this amendment |
| SCA006-CP2 | 2 | Exact amendment and propagation plan (PRD v2.4 candidate, decomposition revision 1.6 text, AGENTS.md text, supersession bindings) | `NOT_STARTED` | requires SCA006-CP1 acceptance |
| SCA006-CP3 | 3 | Audited poststate acceptance, pointer moves | `NOT_STARTED` | requires SCA006-CP2 acceptance |

## SCA006-G1 — owner directions of record (verbatim)

Owner, 2026-09-25, as transcribed in
`execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md`
(SHA-256 `43a0c663c1a57a95001f0470cabb0d36bab098754867ecfe6c30127e7de5efab`):

> D-PEC-90: R-A.

> agents may eventually query PEC directly, yes.  Through tool calls.

The selected R-A grant, item 3, in the ruling's words: "prepare the exact
PRD and `projects/pec/AGENTS.md` amendment as the next PEC scope change once
SCA-005 checkpoint 2 is accepted, including the direct-query access text
above."

Owner, 2026-09-25, as transcribed in
`execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md`
(SHA-256 `eb9793aaaf3b618c911f34db43220d8bf5bf7093fafb0ac9c375a5f6456a5e81`):

> You can continue with all the open work you identified.  Start with the loop migration, then use the loops for organizing the remaining work into a work graph to help plan and orchestrate the implementation.  You are now HELP_HUMAN in the Agent 0 role.  Read your instructions if you need a refresher and carry on.

HELP_HUMAN's list preceding that direction names "the D-PEC-90 reliance
amendment" (D-PEC-94 record).

**Interpretation, not owner text.** The owner did not say "open SCA-006" in
those words. Opening it at Gate 1 is HELP_HUMAN's reading of the R-A grant
and the D-PEC-94 direction, carried by work-graph node R1 and brief B4. The
grant's precondition is met: SCA-005 checkpoint group 2 was accepted on
2026-09-25 (`D-PEC-92`; `_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md`).
Checkpoint groups 1–3 remain the owner's acceptances.

## Non-decisions recorded for clarity

- No option of any owner question above has been selected.
- No PRD, `projects/pec/AGENTS.md`, decomposition, register, pointer,
  `checkpoint_snapshots/`, Scope of Work, SPEC, `_CONTEXT.md`, `_STATUS.md`,
  `v2/**` or foreign-surface byte has changed.
- No access class has changed. No consumer has adopted anything. The
  `D-PEC-67` L-A1 reliance-hold control is untouched.
- No notice has been sent to Root, the App or Runtime; notices are graph node
  R4, after checkpoint 3.
- The checkpoint-1 decision snapshot will be written under
  `_ScopeChange/checkpoint_snapshots/` only after the owner's acceptance.
