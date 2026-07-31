# Root Governance Workplan — Task Management Stage A

Status: `ACTIVE — OWNER-GATED STEPS`
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
