---
amendment_id: SCA-005
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_checkpoint_group: 1
status: checkpoint_1_awaiting_owner
---

# SCA-005 Decision Log

Only decisions that actually occurred are recorded as decided. Every other
row is `AWAITING_OWNER` or `NOT_STARTED`. Agent recommendations are not
rulings.

| DecisionRef | Checkpoint | Decision | Status | Authority |
|---|---|---|---|---|
| SCA005-G1 | Gate 1 intake | Open SCA-005 (SOFTWARE variant) under `chirality-root:bundled:workflow:scope-change` to rebaseline PEC's feed model | `OPENED BY OWNER DIRECTION` | Owner direction, 2026-09-23 (verbatim below); recorded in D-PEC-86 §1 |
| SCA005-CP1 | 1 | Confirm or modify the parsed change set (`Amendment_Actions.csv`, SHA-256 `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2`, 76 PROPOSED actions) and accept `Impact_Assessment.md` at SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`, together with the owner items below | `AWAITING_OWNER` | — |
| SCA005-CP1-Q1 | 1 | Feed model (O-A / O-B2 / O-B1 / O-C) | `AWAITING_OWNER` | design note recommends O-B2 |
| SCA005-CP1-Q2 | 1 | `adapter.yaml` / SOW-017 / DEL-02-07 fate | `AWAITING_OWNER` | recommends (b) parity-peer input only |
| SCA005-CP1-Q3 | 1 | Presence and streams under A2 | `AWAITING_OWNER` | recommends P-β |
| SCA005-CP1-R | 1 | P-β deferral representation (R1 Deferred OUT + retire / R2 keep IN) | `AWAITING_OWNER` | manager recommends R1 |
| SCA005-CP1-Q4 | 1 | Orientation semantics over graph node states incl. Git-derived terminal completion | `AWAITING_OWNER` | recommends (a) |
| SCA005-CP1-Q5 | 1 | When the external trials enter (three fixture classes) | `AWAITING_OWNER` | recommends (a) P1 pinned parser fixture suites only |
| SCA005-CP1-Q6 | 1 | A2 effects on PRD §16.2/16.6/16.8/16.9 | `AWAITING_OWNER` | recommends re-express, decisions still open |
| SCA005-CP1-Q7 | 1 | Ref scope for in-flight graphs | `AWAITING_OWNER` | recommends (b) |
| SCA005-CP1-Q8 | 1 | PEC's own registry row now vs after migration | `AWAITING_OWNER` | recommends (a) `remaining-loop` now |
| SCA005-CP1-Q9 | 1 | Step-0 baseline loops | `AWAITING_OWNER` | design note (a); manager (c) because DEL-10-01 is CHECKING with an accepted pre-P1 baseline |
| SCA005-CP1-Q10 | 1 | P1 parity comparable set | `AWAITING_OWNER` | recommends (c) |
| SCA005-CP1-D79 | 1 | D-PEC-79 path: (a) apply then amend / (b) carry into one successor candidate | `AWAITING_OWNER` | recommends (b); either needs checkpoint-2 acceptance |
| SCA005-CP1-TM | 1 | TM-PEC-023 nine rows carried as candidate MODIFYs, no option selected; rows 1/4/7 behind Q3 | `AWAITING_OWNER` | recommends confirm |
| SCA005-CP1-X | 1 | New feed items: ADD-new vs extend-existing; receipts in SOW-013 vs new item | `AWAITING_OWNER` | manager recommends ADD-new, receipts in SOW-013 |
| SCA005-CP1-N | 1 | Retain names/paths of DEL-02-03/04/06/07 | `AWAITING_OWNER` | manager recommends retain |
| SCA005-CP1-V | 1 | Whether a strict, versioned registry schema v2 is within D-PEC-78 O-A / D-PEC-79 "strict-version-1" | `AWAITING_OWNER` | manager recommends confirm as supplementary extension |
| SCA005-CP1-O | 1 | OBJ-001;OBJ-002 for SOW-095/096 and DEL-02-08/09 | `AWAITING_OWNER` | manager recommends confirm (DL-17 precedent) |
| SCA005-CP2 | 2 | Exact amendment and propagation plan (incl. PRD successor candidate and TM-PEC-023 row selections) | `NOT_STARTED` | requires SCA005-CP1 acceptance |
| SCA005-CP3 | 3 | Audited poststate acceptance, pointer moves | `NOT_STARTED` | requires SCA005-CP2 acceptance |

## SCA005-G1 — owner direction of record (verbatim)

Owner, 2026-09-23 (as transcribed in D-PEC-86 §1):

> Proceed with SCA-005 and what follows in your recommendations.  You are
> Agent 0, so consider effective delegation to your Type 1 and Type 2
> instances.  Use `opus-5.5` models on `high` reasoning for all subagents.  You
> can continue working within your capacity of HELP_HUMAN, anticipating my
> needs and those of the agents under you.

D-PEC-86 §3 I-1 interprets this (Agent 0 interpretation, not owner text) as
opening SCA-005 at Gate 1 and authorizing preparation of the complete
checkpoint-group-1 package, with checkpoint groups 1–3 remaining owner
acceptances.

## Non-decisions recorded for clarity

- No option of any owner question above has been selected.
- No TM-PEC-023 mapping or non-mapping disposition has been selected.
- The D-PEC-79 postimage has not been applied and no PRD byte has changed.
- No decomposition, register, pointer, `checkpoint_snapshots/`, SOW,
  `_CONTEXT.md`, `_STATUS.md`, `v2/**` or foreign surface has changed.
- The checkpoint-1 decision snapshot will be written under
  `_ScopeChange/checkpoint_snapshots/` only after the owner's acceptance.

Companion (2026-09-24): `Checkpoint1_Resolution_Note.md` records, per question, the accepted source that decides it and narrows the owner's live choices to CP1-A/CP1-B and the TM-PEC-023 row selections. It selects nothing; the rows above remain `AWAITING_OWNER` until the owner's act.
