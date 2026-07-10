# PEC Work Loop — team information-hub standing plan

> **Epistemic status: owner-directed standing plan.** Created 2026-07-09 from
> the owner direction recorded in D-PEC-54. It replaces the completed
> sponsor-demo stabilization plan as the ordering map for future PEC work.
> Accepted decisions and the live tree remain authoritative; this file is not a
> status ledger or an adoption act.

## Owner intent

PEC is to become a team-usable hub for critical project information flow. It
shall help project leadership maintain a sufficiently relevant and detailed
shared project state that others can rely upon without recurring N x N
coordination events.

The product spine is the recurring discipline declaration:

1. change that may affect other disciplines;
2. actual or potential budget, scope, or schedule change;
3. needs for information, resources, decisions, approval, or clarification;
4. actual or upcoming internal/external issuances and squad checks; and
5. development state and percent complete against rules of credit.

The gap between recorded state and the state needed to proceed is where
decisions occur. Decisions have consequences. The Planning foreground therefore
triages material information and assigns consequential change to the correct
relied-upon documentation or authoritative system, such as a SOW, DBM, MDL,
schedule basis, register, or controlled deliverable.

Reports, tasks, reminders, schedules, and agents support that information flow;
they do not define it. PEC remains factual-or-absent, source-visible, and
human-authorized.

## Loop protocol

0. **Discover.** Resolve the repo root; inspect git, receipts, registers,
   profile, candidate PRD, current SPEC/traceability status, and live checks.
   Verify every inherited claim against the live tree.
1. **Review the product gate.** The v1.0 PRD remains CANDIDATE until the owner
   adopts it or directs revisions. Do not infer adoption from its presence.
2. **Rebaseline before building.** After adoption, prepare an implementation
   rebaseline that classifies current prototype capability as retain,
   repurpose, retire, or build and names exact migration/data consequences.
3. **Fence source work.** Each implementation tranche requires an owner-ruled
   D-PEC packet with exact paths, acts, verification, rollback, and any data or
   authority implications.
4. **Preserve human gates.** Attestation, import acceptance/apply, decisions,
   approval, verification acceptance, artifact issue, and PRD adoption remain
   human acts.
5. **Execute branch-first.** Keep data isolated and backed up where an adopted
   tranche authorizes mutation. Never use demo state as a production migration
   assumption.
6. **Check and close.** Run work-type checks, record a minimal receipt, and
   surface unresolved product decisions rather than inventing them.

## Target sequence after PRD adoption

| Order | Tranche | Completion test |
|---|---|---|
| T0 | Product and authority rebaseline | Adopted PRD translated into SPEC, traceability, architecture/data-authority decisions, and a retain/repurpose/retire/build map |
| T1 | Team current-state foundation | Multi-user weekly declarations, attestation, coverage/currentness, source proposals, role views, snapshots, and reports work end to end |
| T2 | Decision and consequence placement | Decision gaps and outcomes produce explicit consequences and verified change obligations against relied-upon artifacts |
| T3 | Verification and longitudinal state | Period comparison, rules of credit, cross-source checks, conflicts, staleness, supersession, and propagation verification are operational |
| T4 | Selected integrations and spin-offs | EDMS/schedule/cost/collaboration and supporting workflows are added only with explicit authority mappings and demonstrated value |

## Parked work and owner gates

- Runtime implementation is parked until the owner reviews/adopts the candidate
  PRD and directs the rebaseline.
- The product decisions in PRD §20 remain open and must not be guessed where they
  materially affect the first production architecture or workflow.
- D-PEC-49 remains an unresolved legacy row. It is not an implementation mandate
  for the new product until reconciled during rebaselining.
- Sponsor-demo artifacts and databases remain demo state, not production truth.

## Live pointers

- Candidate product definition: `projects/pec/docs/PRD.md`
- Current prototype specification: `projects/pec/docs/SPEC.md`
- Current prototype traceability: `projects/pec/docs/TRACEABILITY.md`
- Current implementation handoff: `projects/pec/docs/STATUS.md`
- Authoring direction/fence: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-54_team_information_hub_prd.md`
- Decision registers: `_DomainEngines/_DECISIONS/_REGISTER.md` and
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- Profile: `_DomainEngines/profiles/pec.yaml`
- Loop handoff: `_DomainEngines/pec/LOOP_RECEIPTS.md`
