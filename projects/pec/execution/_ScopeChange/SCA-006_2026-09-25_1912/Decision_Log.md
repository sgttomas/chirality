---
amendment_id: SCA-006
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_checkpoint_group: 2
status: checkpoint_2_package_prepared_awaiting_owner
---

# SCA-006 Decision Log

Only decisions that actually occurred are recorded as decided. Every other
row is `AWAITING_OWNER`, `PREPARATION AUTHORIZED` or `NOT_STARTED`. Agent
recommendations are not rulings. The owner accepted checkpoint group 1 on
2026-09-25 by the exact SHA-256 values quoted in row SCA006-CP1. A file
cannot quote its own hash, so the Impact Assessment and action-register
hashes are quoted here and in the run return.

| DecisionRef | Checkpoint | Decision | Status | Authority |
|---|---|---|---|---|
| SCA006-G1 | Gate 1 intake | Open SCA-006 (SOFTWARE variant) under `chirality-root:bundled:workflow:scope-change` to amend PEC's reliance text: PRD PEC-K-03, §8 (agents, access classes, direct query through tool calls), §9 reliance envelope and response-size budgets, §12 reliance gate, and the `projects/pec/AGENTS.md` K-02 gloss | `OPENED BY OWNER DIRECTION` | `D-PEC-90` R-A grant item 3 and the owner's direct-query answer (verbatim below); `D-PEC-94` direction (verbatim below); precondition met by `D-PEC-92` (SCA-005 checkpoint 2 accepted 2026-09-25) |
| SCA006-CP1 | 1 | Confirm or modify the parsed change set (`Amendment_Actions.csv`, SHA-256 `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891`, 54 PROPOSED actions) and accept `Impact_Assessment.md` at SHA-256 `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691`, together with the owner items below | `ACCEPTED` (2026-09-25) | owner act verbatim below; snapshot `../checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/` |
| SCA006-CP1-DQ | 1 | Direct query through tool calls: (a) specify now with a read-only `agent` access class; (b) specify now, riding the `harness` class; (c) defer behind a new §16 access-class decision | `SELECTED (a)` | owner act 2026-09-25 (verbatim below) |
| SCA006-CP1-ENV | 1 | Reliance envelope: (a) new PEC-ORI-007 mapped to DEL-04-03; (b) fold into PEC-ORI-003 | `SELECTED (a)` | owner act 2026-09-25 (verbatim below) |
| SCA006-CP1-BUD | 1 | Response-size budgets: (a) new PEC-API-006 mapped to DEL-08-03, numeric values confirmed at P1; (b) fold into PEC-API-004 | `SELECTED (a)` | owner act 2026-09-25 (verbatim below) |
| SCA006-CP1-GATE | 1 | Reliance gate: (a) standing gate for any release that advertises operational reliance, with SOW-100 and a new DEL-10-13; (b) bind to the P1 exit test and extend existing deliverables | `SELECTED (a)` | owner act 2026-09-25 (verbatim below) |
| SCA006-CP1-INS | 1 | `projects/pec/AGENTS.md` route: (a) carried at checkpoint 3 as an instruction tranche with its own manifest and notices; (b) a separate instruction tranche after checkpoint 3 | `SELECTED (a)` | owner act 2026-09-25 (verbatim below) |
| SCA006-CP1-RC | 1 | Confirm that R-C (PEC output citable as authority) stays excluded | `CONFIRMED EXCLUDED` | owner act 2026-09-25 (verbatim below) |
| SCA006-CP2 | 2 | Exact amendment and propagation plan (PRD v2.4 candidate, decomposition revision 1.6 text, AGENTS.md text, supersession bindings) | `PREPARED / AWAITING_OWNER` | SCA006-CP1 accepted 2026-09-25; package hashes in §"SCA006-CP2 — package prepared (not a decision)"; question set in `Propagation_Plan.md` §"Checkpoint-2 owner question set" (Q-CP2-A, Q-CP2-1, Q-CP2-2) |
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
(SHA-256 `eb9793aaaf3b618c911f34db43220d8bf5bf7093fafb0ac9c375a5f6456a5e81` at base `13df8b795`; `b6814e902c23f24020337ab925a7c287b66b5ee485785bee07b042e25e1e5a6b` after its owner-confirmation section merged at `bec8bdd65`, with the direction below unchanged):

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

- Before 2026-09-25's checkpoint-1 acceptance, no option had been selected. The selections now recorded are the owner's (section below).
- No PRD, `projects/pec/AGENTS.md`, decomposition, decomposition-register,
  Scope of Work, SPEC, `_CONTEXT.md`, `_STATUS.md`, `v2/**` or foreign-surface
  byte has changed.
- The checkpoint-1 acceptance added the group-1 decision snapshot and the
  amendment-qualified pointer `../SCA-006_GROUP-1_AUTHORIZED.md`.
  `_ScopeChange/_LATEST.md` still names SCA-005. The PEC decision-register
  row `D-PEC-90` gained a pointer to this scope change.
- No access class has changed. No consumer has adopted anything. The
  `D-PEC-67` L-A1 reliance-hold control is untouched.
- No notice has been sent to Root, the App or Runtime; notices are graph node
  R4, after checkpoint 3.
- The checkpoint-1 decision snapshot was written after the owner's acceptance,
  at `../checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`.

## SCA006-CP1 — owner act (verbatim), 2026-09-25

> SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded

HELP_HUMAN recorded this under K-AUTH-1. The interpretation and bounds are in
`../checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md`. Before the
act, the owner asked for the DQ (a) and (b) implications, and HELP_HUMAN
explained them in chat, recommending (a). This log's hash at the owner's act
was `8a01bd653eca52bb8ffae947ffce28d83d7da6beaf690b35c72563f88615547a`.

## SCA006-CP2 — package prepared (not a decision)

Prepared 2026-09-25 by WORKING_ITEMS (node R2 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`) under brief `B5_SCA006_CHECKPOINT2.md` (HELP_HUMAN scratchpad; SHA-256 `142d6be0b0f44c459e895d067081a004df8fa229ac455349e4cc8b26e8abefb4`). No owner decision is recorded here: every checkpoint-2 question is `AWAITING_OWNER`. The recommendations (Q-CP2-A accept; Q-CP2-1 (a), the I1 corrections ride the instruction tranche; Q-CP2-2 (a), the group-2 snapshot with a D-PEC register row is the Lane A packet) are the manager's, not rulings. Nothing is applied: live decomposition revision 1.5, its registers, PRD v2.3, `projects/pec/AGENTS.md`, every SOW, SPEC, `_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv`, `v2/**`, the tier-0 profile, both `_LATEST.md` pointers and the checkpoint snapshots are byte-unchanged. `Propagation_Plan.md` cannot quote its own hash; it is quoted here. Package hashes (acceptance slots at their defaults):

| Artifact | SHA-256 |
|---|---|
| `Amendment_Preview.md` | `3a665e5b1e533baa3465069380d42b5563e49b668c2f1184242177052df5f6ac` |
| `Propagation_Plan.md` | `22e56f40a0ceff93e3a7923b1608dfea9bcd82b3f7e1fe9a55024e71483338c6` |
| `Amendment_Actions_CP2.csv` | `6e57aa610cfc491f2fa9173a58dde5d4e1d815bb4a38831448200a9fbc5379af` |
| `Supersession_Delta.csv` | `028fb4e021e1f565d5c7d9eab275ec94e9d3baf9d19606d887fb24d78b39d4fc` |
| `PRD_V2_4_SUCCESSOR_DIFF.md` | `a743a5273c66dc679a99888c4dc2b865a318dab64fcaaa7768ecb71f35696a4c` |
| `AGENTS_MD_CANDIDATE_DIFF.md` | `7c57a1b2c02c872fae6f778beeddf7f812809d469b504e34d1e6f79bbb48a158` |
| `CP2_CANDIDATE/docs/PRD.md` | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `CP2_CANDIDATE/AGENTS.candidate.md` | `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` |
| `CP2_CANDIDATE/AGENTS.candidate_without_I1.md` | `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188` |
| `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` | `4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71` |
| `CP2_CANDIDATE/_Decomposition/ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `CP2_CANDIDATE/_Decomposition/Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |

Independent verification: `B5_VERIFIER_VERDICT_NN.md` in `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`.
