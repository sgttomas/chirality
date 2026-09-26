---
amendment_id: SCA-006
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_checkpoint_group: 3
status: checkpoint_3_prepared_awaiting_owner
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
| SCA006-CP2 | 2 | Exact amendment and propagation plan (PRD v2.4 candidate, decomposition revision 1.6 text, AGENTS.md text, supersession bindings) | `ACCEPTED` (2026-09-25); Q-CP2-1 `SELECTED (a)`; Q-CP2-2 `SELECTED (a)` | owner act verbatim below; snapshot `../checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`; register row `D-PEC-97` (Q-CP2-2 (a)) |
| SCA006-G2-A1 | 2 (amendment) | The `AGENTS.md` Remaining-sections correction rides the checkpoint-3 instruction tranche | `DIRECTED` (2026-09-26); `HUNK APPROVED` (2026-09-26) | owner acts verbatim below; `../checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`; hunk `AGENTS_MD_AMENDMENT1_DIFF.md` §3; approved postimage `projects/pec/AGENTS.md` `4400c4e9…139c` |
| SCA006-CP3-EDITION | 3 | Scope-change method edition for checkpoint 3: the pinned edition (`contract.md` `4453a719…`, `method.md` `34187e83…`) or the Root wave-2A revision | `SELECTED PINNED` (2026-09-26) | owner act verbatim below; `../checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/` |
| SCA006-CP3 | 3 | Audited poststate acceptance, pointer moves | `PREPARED / AWAITING_OWNER` (2026-09-26) | SCA006-CP2 accepted 2026-09-25; package hashes in §"SCA006-CP3 — package prepared (not a decision)"; question set `RUN_SUMMARY.md` §9 |

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
- No notice has been sent to Root, the App or Runtime. Under the accepted
  plan (§A4.3), HELP_HUMAN writes the three notices in the checkpoint-3
  instruction-tranche PR (graph node R4).
- The checkpoint-2 acceptance added the group-2 decision snapshot
  (`../checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`), the
  amendment-qualified pointer `../SCA-006_GROUP-2_AUTHORIZED.md`, and PEC
  decision-register row `D-PEC-97`.
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

Prepared 2026-09-25 by WORKING_ITEMS (node R2 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`) under brief `B5_SCA006_CHECKPOINT2.md` (HELP_HUMAN scratchpad; SHA-256 `142d6be0b0f44c459e895d067081a004df8fa229ac455349e4cc8b26e8abefb4`). No owner decision is recorded here: every checkpoint-2 question was `AWAITING_OWNER` at preparation (pre-acceptance; the owner accepted on 2026-09-25, below). The recommendations (Q-CP2-A accept; Q-CP2-1 (a), the I1 corrections ride the instruction tranche; Q-CP2-2 (a), the group-2 snapshot with a D-PEC register row is the Lane A packet) are the manager's, not rulings. Nothing is applied: live decomposition revision 1.5, its registers, PRD v2.3, `projects/pec/AGENTS.md`, every SOW, SPEC, `_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv`, `v2/**`, the tier-0 profile, both `_LATEST.md` pointers and the checkpoint snapshots are byte-unchanged. `Propagation_Plan.md` cannot quote its own hash; it is quoted here. Package hashes (acceptance slots at their defaults):

| Artifact | SHA-256 |
|---|---|
| `Amendment_Preview.md` | `737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4` |
| `Propagation_Plan.md` | `f95d00d154610d44a37d4aeabfae3fff29aac6c0a0c016bb1241810ebc87d7d8` |
| `Amendment_Actions_CP2.csv` | `d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de` |
| `Supersession_Delta.csv` | `e69f97814294ccd993fceff12cdf992623156c33ca4993adb103b61774e5977b` |
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

## SCA006-CP2 — owner act (verbatim), 2026-09-25

> SCA-006 CP2: accept; Q1 a; Q2 a

HELP_HUMAN recorded this under K-AUTH-1. The interpretation and bounds are in
`../checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md`, and register
row `D-PEC-97` makes that snapshot the Lane A packet. At the owner's act, this
log's hash was `dc6e89fe74059e9a016cbcd69b0019dc567a7048062c626c83daa6225d5b170e`.

## Group-2 amendment 1 and the checkpoint-3 edition — owner acts (verbatim), 2026-09-26

> Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them.

> revision 4: drop remaining-items and remaining-loop; yes, ride checkpoint 3.  SCA-006 pinned.

HELP_HUMAN recorded these under K-AUTH-1. The interpretation and bounds are
in `../checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md`.

## SCA006-G2-A1 — hunk approval, owner act (verbatim), 2026-09-26

> approve hunk

HELP_HUMAN presented the owner with the exact 12-line replacement paragraph
(applied `projects/pec/AGENTS.md` L261–272, verbatim), the dropped clause
("its graph accounts for the Remaining items it touches") and the reason it
was dropped, and the audit's COV-083 observation (the decomposition's
"declares `remaining-loop` now" text, recorded as a known follow-up). The
owner approved after seeing all of it. The approved postimage is
`projects/pec/AGENTS.md` SHA-256
`4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`; the hunk
is `AGENTS_MD_AMENDMENT1_DIFF.md` §3. HELP_HUMAN transcription under
K-AUTH-1: HELP_HUMAN relayed the act to WORKING_ITEMS (brief B6), which wrote
this section at HELP_HUMAN's direction. This satisfies amendment 1's
pre-merge approval gate for the hunk. It accepts nothing else: checkpoint 3
remains the owner's.

## SCA006-CP3 — package prepared (not a decision)

Prepared 2026-09-26 by WORKING_ITEMS under brief B6 (`8bdc7181…2df4`, work-graph
node R3), on the pinned scope-change edition. No owner decision on checkpoint 3
is recorded here: Q-CP3-A, Q-CP3-1 and Q-CP3-2 (`RUN_SUMMARY.md` §9) are
`AWAITING_OWNER`, and the recommendations are the manager's, not rulings. The
live poststate is applied as a candidate. Both `_LATEST.md` pointers are
unchanged, and no `_STATUS.md` or lifecycle changed. Hashes at preparation:

| Artifact | SHA-256 |
|---|---|
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (pre-acceptance form) | `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59` |
| `ScopeLedger.csv` / `Deliverables.csv` / `ContextBudgetQA.csv` / `Companion_Inventory.csv` | `1d24a4b8…e916e` / `94ee5d18…9805` / `93b0bb07…7c7c` / `1597ceec…8662` |
| `projects/pec/docs/PRD.md` (v2.4) | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `projects/pec/AGENTS.md` (hunk approved) | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| tranche manifest `PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml` | `2b29af181947ba0ed75cd83a286c56a2863802d1d6a7e5b3ca9ab82330cdee74` |
| `RUN_SUMMARY.md` (question set §9) | `690b4923e7e7f7e62c25a6db35540e0e6b8bcd1276fbaa69dc078cf2b70c9b62` |
| `AGENTS_MD_AMENDMENT1_DIFF.md` | `8b2386415b79f7666c5561873d8ce7b8a753d805c5e4bfbd1800fa5824206d4f` |
| `Supersession_Map.csv` / `Post_Change_Coverage.json` | `010ce5c4…ab92` / `b9a068c0…09cf0` |
| C4.3 review `CP3_EVIDENCE/C4_3_REVIEW.md` | `1ee6fe93c03a32cc98adbfa0825de074e5e5a9c3a91fbafe7c76f64cd04d7035` |
| audit `COV_SCA006_POSTCHANGE_2026-09-26_0051/RUN_SUMMARY.md` | `f97bde4e087d8da764d98f582c3f54c852bae332e1e0d2695ab5899adedd6499` |

Independent verification: `B6_VERIFIER_VERDICT_NN.md` in
`execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`.
