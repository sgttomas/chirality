# Task Management Adoption Packet — PEC loop (Stage B, presented 2026-07-31)

Status: `PRESENTED — AWAITING LOOP OWNER RULING`
Prepared by: Root loop, HELP_HUMAN (Agent 0), per Stage-A workplan step 7.
This packet is coordination, never authority. Nothing below has effect
until the PEC loop's owner rules under its own instruments (the D-PEC packet route per D-GOV-32 Effect 3).
Decline and defer are lawful outcomes (K-TM-4); silence binds nothing.

## Basis

D-GOV-32 (adoption of the Task Management PRD Rev 2, subject SHA-256
`97e2ae65…f35d18`); K-TM-1..6 at `docs/CONTRACT.md` §1.14; the root
Stage-A precedent (Receipts 66–70): register + seed + first triage with
46/101 first-session closures, TASK_MANAGEMENT agent in lieu of entry
binding (root's own §14 ruling), resolution orchestration per workplan
Amendment 2.

## Proposed adoption (effective only on ruling of D-PEC-72)

1. **Register mint.** `_DomainEngines/pec/_TaskManagement/REGISTER.csv`, schema 1.0 (25 columns,
   `RegisterSchemaVersion` column 1, mandatory `Status`/`Disposition`,
   K-TM-6), IDs `TM-PEC-<seq>`. A coordination-surface subdirectory,
   not a SPEC §1.2 tool root. Owned and written only by this loop
   (K-TM-2/K-TM-3).
2. **Binding — Option A (recommended; the root pattern).** No entry
   binding: the loop invokes TASK_MANAGEMENT (`agents/AGENT_TASK_MANAGEMENT.md`)
   on demand or on an owner-scheduled routine; sessions record residue
   in receipts as today. `_DomainEngines/pec/LOOP_INIT.md` is not amended.
3. **Binding — Option B (PRD §14 pattern, if preferred).** Amend
   `_DomainEngines/pec/LOOP_INIT.md` so session entry reads open register rows and session close
   records dispositions or receipt residue. Exact text supplied on
   request; one loop-owned file, one loop ruling.
4. **Decision row.** D-PEC-72 in this loop's `_DECISIONS/_REGISTER.md`
   recording the ruling (adopt A / adopt B / amend / decline / defer),
   with this packet as subject.
5. **Migration.** No root rows are deferred against this adoption today; the step-5 notice (NOTICE_D-GOV-32_TASK_MANAGEMENT_ADOPTION.md, this surface) already records that adoption decided PEC PRD §16 decision 1 for the Action Item register class only. The register home sits beside the loop's standing surfaces per PRD §6.1 F-3 (the loop reads its own directory every session). Migration is by linked rows (PRD §6.2): the root
   row closes or cross-cites; this loop's row cites `SourceRef` back.
   No actor ever writes across registers.

## Fences carried

K-TM-1..6 in full; no work-discovery queue; no resolution surface;
rows carry no directives; no agent as accountable (A); registers never
gate; scanner projections gitignored (D-GOV-01). Adoption creates no
duty for any other loop.

## Root-side effects on this loop's ruling

Root register row TM-ROOT-100 closes `RESOLVED_BY_DECISION` citing D-PEC-72; the
deferred rows whose triggers reference this adoption wake for migration
review at the next root TASK_MANAGEMENT invocation.
