---
amendment_id: SCA-006
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-25
status: awaiting_checkpoint_1_acceptance
authority: D-PEC-90 R-A grant item 3 and D-PEC-94 (Gate 1 opened by owner direction; precondition D-PEC-92 met)
workflow: chirality-root:bundled:workflow:scope-change
---

# SCA-006 — PEC reliance amendment (checkpoint-group-1 brief)

## Human initiation

SCA-006 writes the owner's D-PEC-90 direction into PEC's product definition
and instructions. The owner's words, recorded in
`execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md`:

> D-PEC-90: R-A.

> agents may eventually query PEC directly, yes.  Through tool calls.

R-A's grant item 3 authorizes HELP_HUMAN to "prepare the exact PRD and
`projects/pec/AGENTS.md` amendment as the next PEC scope change once SCA-005
checkpoint 2 is accepted, including the direct-query access text above."
SCA-005 checkpoint 2 was accepted on 2026-09-25 (`D-PEC-92`). The owner's
`D-PEC-94` direction ("You can continue with all the open work you
identified. …", verbatim in `Decision_Log.md`) placed "the D-PEC-90 reliance
amendment" in the post-SCA-005 work graph as node R1. The D-PEC-91 ruling's
carry-forward note puts response-size budgets for agent consumers in this
amendment.

The owner has **not** accepted checkpoint group 1. The owner acts this
package relies on are the R-A ruling with its direct-query answer, D-PEC-92
and D-PEC-94. Reading them as opening SCA-006 at Gate 1 is HELP_HUMAN's
interpretation, carried by brief B4, not owner text.

## Normalized parameters

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution/` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5 `current_basis`, SHA-256 `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`) |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-006` (PEC-qualified) |
| `ALLOW_RENUMBERING` | `false` |
| `ALLOWED_PROPAGATION_WRITES` | SOFTWARE default (decomposition + affected `_CONTEXT.md`/`_STATUS.md`), only after checkpoint-2 acceptance; PRD and AGENTS.md per the accepted checkpoint-2 text |
| Pointer posture for a later checkpoint 3 | `ACCEPTED_PREDECESSOR` (`_ScopeChange/_LATEST.md` names SCA-005) |
| Current stage | checkpoint group 1 (method parts A and B) prepared; awaiting owner |

## Semantic section binding (by heading text)

| Semantic section | Bound heading in `SOFTWARE_DECOMP.md` |
|---|---|
| Change Register | `## 11. Decision Log` and `## 12. Revision History (Phase 7 change summary)` (plus `## Gate Log`) |
| Unit Ledger | `## 6. Scope Ledger` → authoritative `ScopeLedger.csv` |
| Objectives | `## 3. Objectives (Phase 3)` and the ledger `ObjectiveIDs` column |
| Primary Partitions | `## 4. Packages (Phase 4)` |
| Secondary Entities | `## 5. Deliverables (Phase 5)` → authoritative `Deliverables.csv` |
| Vocabulary Map | `## 9. Vocabulary Map (seeded at Phase 2)` |
| Coverage basis / telemetry | `## 7. Coverage & Telemetry (Phase 6)`, `## 8. Context Budget QA (Phase 6)` → `ContextBudgetQA.csv`; pre-change `audit-decomp` output |
| Constraints / open issues | `### 1.3 Hard constraints (identified at intake)`, `## 10. Open Issues` |

Every binding resolved at the first rank; none was resolved by position.

## The change as parsed (PROPOSED)

`Amendment_Actions.csv` records **54 PROPOSED atomic actions** for the
recommended set DQ-a + ENV-a + BUD-a + GATE-a + INS-a:

| Change element | Seq | Summary |
|---|---|---|
| PEC-K-03 | 1, 11, 13, 18 | verify-before-rely → operational reliance within the declared pin, coverage and tier, with file fallback; "non-authoritative" kept in the authority sense; pull-oriented, consumer-owned use kept; §15 lineage and C3 follow |
| §8 and direct query | 2–4, 7, 9, 10, 12, 20–23, 26, 28, 31, 41 | agents act on PEC data and may query directly through tool calls; a read-only `agent` access class; PEC-API-007 tool-call surface (P3); §16.6 premise widened, decision still open |
| §9 envelope and budgets | 5, 6, 24, 25, 30, 32, 33, 36, 37, 39, 40 | PEC-ORI-007 reliance envelope; PEC-API-006 response-size budgets (D-PEC-91 carry-forward) |
| §12 gate | 8, 27, 29, 35 | a standing gate before any release advertises reliance: parity, coverage honesty, envelope, parser fixtures, kill test |
| `projects/pec/AGENTS.md` | 14–17 | K-02 gloss and related instruction loci, carried as an instruction tranche |
| Telemetry and traceability | 19, 34, 38, 42, 43 | §1.2, PKG-08 charter, the `operational reliance` term, counts, revision 1.6 after checkpoint 3 |
| Derivative advisories | 44–54 | 9 Scope of Work contracts, the DEL-00-03 SPEC and three EvidenceQuotes, re-quoted later by their owners |

Counts: 12 ADD, 42 MODIFY; 31 OTHER, 14 DELIVERABLE, 4 VOCAB_TERM,
3 PACKAGE, 2 OBJECTIVE. Part-A validation: 54/54 PASS (Impact Assessment
Annex A). Option deltas are in Impact Assessment §13. The per-deliverable
Scope of Work population is §7.1: 9 AFFECTED, 23 NOT_AFFECTED of 32.

Exact amendment prose is deliberately absent; it belongs to checkpoint
group 2.

## Brief addenda received in-session (HELP_HUMAN messages; not owner acts)

1. "the Impact_Assessment must enumerate the affected Scope of Work
   population explicitly, deliverable by deliverable. Do not use 'where
   affected'. The work graph now gates its SOW batch S4 on exactly that set."
   It named candidates DEL-04-01, DEL-04-02 (CLM-016 L225), DEL-08-01 (CLM-004
   L92), DEL-08-03 (REQ-005 L256), the §8-citing DEL-01-01, DEL-01-05,
   DEL-02-03, DEL-04-02, DEL-04-03, DEL-08-01, DEL-08-04, and DEL-01-06 on its
   own evidence. Each was to be classified `AFFECTED` or `NOT_AFFECTED`, citing
   the SOW line and the PRD text that SCA-006 changes.
2. A correction to the first addendum:
   - DEL-01-01 L90, DEL-02-03 L104 and DEL-04-03 L146 cite `SOFTWARE_DECOMP.md`
     §8, not PRD §8.
   - The genuine PRD §8 references are DEL-01-05 L66, DEL-04-02 L363,
     DEL-08-01 L92, DEL-08-03 L229 and DEL-08-04 L274.
   - DEL-04-01 is a fixed member of the affected set.

Both are applied in Impact Assessment §7.1. The child inventory checked every
line number they give; all match. It found one more: DEL-08-04 L290 also cites
`SOFTWARE_DECOMP.md` §8.

## Pre-change baseline

`Pre_Change_Coverage.json` is a byte copy of the latest audit,
`_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/coverage_summary.json`.
No fresh audit was run. Every audit input is byte-identical between the
audited commit `995af4f36` and `origin/main` `13df8b795` (Impact Assessment
§2.1).

## Write boundary of this run

Written:
- this snapshot folder (`Brief.md`, `Impact_Assessment.md`,
  `Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Decision_Log.md`,
  `Handoff_State.md`);
- the manager's return and verifier verdicts under
  `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`.

Not written:
- `_ScopeChange/_LATEST.md`, `_Evaluation/DecompCoverage/_LATEST.md` or
  `_ScopeChange/checkpoint_snapshots/`;
- any decomposition file or register, `docs/PRD.md` or
  `projects/pec/AGENTS.md`;
- any `ScopeOfWork.md`, SPEC, `_CONTEXT.md` or `_STATUS.md`;
- `_DECISIONS/**`, the work graph, `docs/STATUS.md`, `README.md` or `v2/**`;
- any Root, App, Runtime or tier-0 path.

No pre-change audit folder was created. The checkpoint-1 decision snapshot is
not created; it follows owner acceptance.

## Instruction and method basis

| File | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `workflows/scope-change/WORKFLOW.md` | `58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90` |
| `workflows/scope-change/resources/contract.md` | `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02` |
| `workflows/scope-change/resources/method.md` | `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5` |
| Brief B4 (HELP_HUMAN scratchpad, not in the repository) | `87612acaa41fb3975a87fddd6a97803a4968e0f0d1d1df837ce0373e82d0ae90` |
| Work graph as read (PR #919 branch commit `5570fd0953f69dd8c23e0e7ae43501a31cad8947`) | `f78484a79a923b09d5acb9ee964ebf07acaa5d8234f9de36e1738593fc60c329` |
| D-PEC-90 ruling / proposal | `43a0c663c1a57a95001f0470cabb0d36bab098754867ecfe6c30127e7de5efab` / `b04a8aa25c1d402fb03f6f15b6fb1eb27a0110e5cd3f3ded1db3717649a5e147` |
| D-PEC-91 ruling | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| D-PEC-94 record | `eb9793aaaf3b618c911f34db43220d8bf5bf7093fafb0ac9c375a5f6456a5e81` |
| D-PEC-67 record | `c04f8ddd90cfe4ca3ecdabad8f48b4820c9952c9c4515655dc8ed21304d9d9a8` |

The manager read only its own role file. `workflows/audit-decomp/WORKFLOW.md`
(`4aaa7e10…e3e6`) was consulted only to confirm the baseline's method
identity; no audit-decomp child ran. The SCA-005 checkpoint-1 package form,
taken from commit `9c7ae80d0`, was mirrored where the method is silent.

## Gate boundary

This package changes no PRD, instruction, decomposition truth, companion
register, accepted pointer, deliverable metadata or content, dependency
register, source, lifecycle, Task Management row, decision, receipt or
foreign-loop surface. It changes no access class. It asks nothing about
CHECKING, ISSUED or acceptance of any deliverable.
