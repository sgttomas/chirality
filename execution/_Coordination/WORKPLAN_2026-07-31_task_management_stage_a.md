# Root Governance Workplan — Task Management Stage A

Status: `CLOSED 2026-07-31 — see the Closure note; successor: WORKPLAN_2026-07-27_root_idle.md`
Date: 2026-07-31
Supervising role: `HELP_HUMAN`
Predecessor: `execution/_Coordination/WORKPLAN_2026-07-27_root_idle.md` (posture preserved for everything outside this plan's steps)

## Basis

D-GOV-32 (`docs/governance_harness/_DECISIONS/D-GOV-32_task_management_prd_adoption.md`)
adopted the Chirality Task Management PRD, Revision 2
(`plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md`, subject
SHA-256 `97e2ae6525ecbfdc52ff22aee85e1182a751c1090c2aa2f52faaf9e080f35d18`,
candidate commit `584319dc9`, effective at PR #423 merge `c1156837f`; the
record merged at PR #424, `1c80a2bc1`). The PRD bytes govern product
content; D-GOV-32 governs adoption status; its Effect 2 enumerates the
Stage-A obligations this workplan sequences. Supporting (non-governing)
review: `plans/chirality_task_management_architecture_review_2026-07-31.html`.

Owner sequencing direction of record (2026-07-31, in-session, verbatim):

> I defer to your judgment on the best sequence and manner to proceed.

and, on ensuring the other loops are not forgotten:

> Then we should ensure all loops are updated accordingly, or I'm likely
> to forget and - ironically - there's no TM to record the need for it in
> the future.

Under that direction this plan includes the accelerated Stage-B drafting
(step 7). Every consequential act below remains individually owner-gated;
this plan authorizes sequencing, not outcomes.

## Steps

Execute in order; each ruled step publishes via human-gated PR per the
PRD_ROOT Rev 7 §5.3.1 merge-gate policy (no self-merge without an express
bounded owner grant given in-session).

0. **Backfill** `PublicationSHA`/`EffectiveSHA` in the D-GOV-32 record
   from the PR #424 merge (`1c80a2bc1`), per the established convention.
1. **CONTRACT tranche.** Draft the K-TM-1..6 rows (PRD §10) for
   `docs/CONTRACT.md` as a human-gated governed tranche; present for
   owner ruling before merge.
2. **Mint the program register.**
   `execution/_Coordination/_TaskManagement/REGISTER.csv` per PRD §6.3
   (`RegisterSchemaVersion` column 1; `TM-ROOT-<seq>` IDs;
   `Status`/`Disposition` mandatory; `SourceSha`/`EvidenceSha` per
   K-AUTH-2). A `_Coordination/` subdirectory — NOT a SPEC §1.2 tool
   root. Optional non-authoritative per-item MD summaries only in the
   `_DEPENDENCIES.md`-over-CSV pattern.
3. **Seed as candidate rows** (drafting; rows are adopted only at the
   owner triage session, K-TM-3): the measured backlog (~115 items; PRD
   §5.1 and review §02 — the 29 `TRACKED_OPEN` notices plus 3
   unregistered ones, the 07-28 tandem review §09 ranked actions and §08
   held-open questions, horizon `FINDINGS.csv` open rows, piping D-45,
   open packet questions, `TP-EXPORT-006` TBD rows, handoff blockers),
   **plus one row per unadopted loop** (App-dev, Piping, PEC) recording
   that loop's pending TM adoption, so the rollout itself is
   register-tracked. Every seeded row cites source path and SHA.
4. **Reader binding.** Amend `execution/_Coordination/LOOP_INIT.md` so
   root session entry reads open register rows (redirecting the existing
   parked-lanes enumeration step at the register) and session close
   records dispositions or receipts residue (PRD §14). One loop-owned
   file; present for owner ruling.
5. **PEC §16-1 notice.** Route the coordination notice to
   `projects/pec/execution/_Coordination/` per D-GOV-32 Effect 3
   (coordination, never authority).
6. **First owner triage session.** Present open rows grouped by the nine
   domains with proposed dispositions per PRD §7; the owner rules;
   record dispositions with evidence citations. PRD §19.1: if the seed
   remains untriaged after two root-loop sessions, the falsification
   clause fires — this step is not deferrable ceremony.
7. **Stage-B acceleration (owner-directed).** Draft per-loop adoption
   packets — for each of App-dev, Piping, PEC: that loop's own
   `LOOP_INIT`/receipt-contract binding amendment, register minting
   under its coordination surface (PEC's beside its loop surfaces in
   `_DomainEngines/pec/`), and a decision-register row (D-APP-* /
   piping D-* / D-PEC-*) — route the standard as coordination notices
   to each loop's surface, and present the three packets for per-loop
   owner rulings. Publication per ruled packet via human-gated PR.
   Until a loop's ruling lands it remains unbound and its program-
   register row stays OPEN (F-APP-5 / F-PIP-5 / D-GOV-32 Effect 4).
8. **Optional, time-permitting:** `taskmgmt` v0 (scan/validate per PRD
   §9) as a human-gated tools tranche under `tools/taskmgmt/`. Deferrable
   without harm — the register is file-native (K-TM-4).

## Fences

All PRD fences bind: no work-discovery queue; no resolution surface; no
writes to other loops' registers or instruments except through their own
ruled packets (step 7); no agent-instruction changes in this phase;
scanner outputs only as rebuildable gitignored projections (D-GOV-01);
`SOFTWARE_DECOMP` for the service is deliberately deferred until two
loops have run registers through real sessions (PRD §23.4). If the tree
contradicts this plan, the tree governs — surface the discrepancy.

## Closure condition

Steps 0–6 complete with owner rulings recorded; step 7 packets presented
(rulings may trail per loop); receipts appended per `LOOP_INIT` closeout;
successor posture (continued Stage B / idle) selected at the applicable
gate. Then repoint `CURRENT_WORKPLAN.md` per the successor-selection
rule.

## Authority and closeout

This is a coordination surface, not authority. D-GOV-32, the adopted PRD,
live standards, decisions, accepted snapshots, Git state, and current
human direction govern. Git closeout does not constitute semantic
acceptance.

## Amendment 1 — 2026-07-31 — Step 4 superseded: TASK_MANAGEMENT agent in lieu of reader binding (owner-ruled)

After steps 0–3 executed (D-GOV-32 backfill at PR #426; K-TM-1..6 into
`docs/CONTRACT.md` §1.14 at PR #428; register minted and seeded with 100
candidate rows at PR #429), the owner reviewed the presented step-4
reader-binding draft and counter-proposed a standalone agent for the Task
Management role instead of loop-entry consumption. On the supervising
session's assessment, the owner ruled (2026-07-31, in-session, 188 bytes
UTF-8, SHA-256
`043339d7c7e880af3a546e0e2280c944cfa96be81a434ebf43f8f0845c26e433`):

<!-- BEGIN OWNER RULING VERBATIM -->
I won't forget to do task management because I can schedule it on a routine.

Allow me to reverse my rulings around agent changes to allow for this.

Merge PR #429 and proceed accordingly.
<!-- END OWNER RULING VERBATIM -->

Effects on this plan:

1. **Step 4 is superseded.** No `LOOP_INIT.md` reader binding is made; no
   informational pointer line either (the owner's scheduling routine is the
   read cadence). This is the root loop exercising the PRD §14
   adopt/amend/decline clause by its own ruling — the PRD bytes are not
   amended. Session entry and closeout remain exactly as `LOOP_INIT.md`
   states today.
2. **Fence relaxation, exactly bounded.** The "no agent-instruction changes
   in this phase" fence (and the PRD §17 Stage-A "zero agent-file changes"
   posture) is relaxed by the owner ruling above for precisely one package:
   `agents/AGENT_TASK_MANAGEMENT.md` plus its `AGENTS.md` index row and the
   agent-index change notices that rule requires. No other agent-instruction
   change is authorized by this amendment.
3. **TASK_MANAGEMENT (Agent 1)** is added to the live index: invoked on
   demand or on a human-scheduled routine, never bound to loop entry; owns
   only the invoking loop's register home; all dispositions remain owner
   acts (K-TM-1..6). Skills, tools, and script automation may augment it
   later through their own governed tranches; for now, just the agent.
4. **Steps 5–8 are unchanged**, including the step-6 first owner triage
   session and the PRD §19.1 falsification clock (seed triaged within two
   root-loop sessions). Step 6 is expected to run as the new agent's first
   invocation.

## Amendment 2 — 2026-07-31 — TASK_MANAGEMENT resolves ruled items through the nine domains (owner-directed)

Before PR #430 merged, the owner refined the TASK_MANAGEMENT design
(2026-07-31, in-session, 223 bytes UTF-8, SHA-256
`9d46dded314e40bc93a408c35da66debf5ee5a842b60be6e3c6ed9f45c904f7d`):

<!-- BEGIN OWNER DIRECTION VERBATIM -->
TASK_MANAGEMENT agents should invoke the nine steps to resolve the action item through delegation to a deliverable amendment, scope change, TASK agent or other specialist Agent 2 instances, or in rare cases directly itself.
<!-- END OWNER DIRECTION VERBATIM -->

Incorporated into `agents/AGENT_TASK_MANAGEMENT.md` (same unmerged PR #430
package; the presented HEAD supersedes the earlier one) as mode 6
"Resolution orchestration" plus a §Resolution paths section, with two
doctrine-conformant readings recorded:

1. **Nine domains as per-item steps.** The nine domains are worked in
   order as a completeness scan for each owner-ruled item. This preserves
   the adopted PRD §4 posture (lenses, "not any kind of sequence or
   specific workflow" for loops): the sequence lives inside the treatment
   of one item, and no loop-level workflow, queue, or gate is created.
2. **Sibling instruments by routed handoff.** Deliverable amendments and
   scope changes are owned by sibling Agent 1 managers; root doctrine has
   Agent 1 delegating only to Agent 2/TASK. TASK_MANAGEMENT therefore
   prepares and routes those packages (amendment package to the owning
   production lane; SCA intake to SCOPE_CHANGE's declared gate) rather
   than commanding sibling managers. Bounded work dispatches to TASK /
   named Agent 2 specialists / sealed ephemeral generalists. Direct
   execution stays rare: an explicit in-session owner grant naming item
   and write target, recorded in closeout evidence.

Resolution remains development-loop-owned (the PRD §1 owner direction of
record): the loop, through this invoked manager and its instruments,
resolves; the register still records only disposition and evidence and
gates nothing.

## Closure note — 2026-07-31

The closure condition is met as owner-modified: steps 0–6 complete with
rulings recorded and merged (PRs #426, #428, #429, #430, #433; Receipts
66–70); step 7 packets presented on all three loop surfaces (PR #434,
Receipt 71) with per-loop rulings deliberately trailing to the individual
development loops (owner direction of record, Receipt 72); step 8 shipped
(PR #435, Receipt 72). `HANDOFF_STATE.md` thinned to the four-field form
per the same ruling. Successor posture: idle
(`WORKPLAN_2026-07-27_root_idle.md`, resumed by dated addendum);
`CURRENT_WORKPLAN.md` repointed in the closure tranche (Receipt 73).
Stage-B activity continues in the development loops and is tracked by
register rows TM-ROOT-098/099/100.
