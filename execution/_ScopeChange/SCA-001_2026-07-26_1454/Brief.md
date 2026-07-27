# SCA-001 — Root Runtime Stewardship Intake

Status: `GATE_1_OPEN_AWAITING_OWNER_CONFIRMATION`
Amendment ID: `SCA-001`
Date: `2026-07-26`
Managing agent: `SCOPE_CHANGE`
Decomposition variant: `SOFTWARE`
Context root: `execution/`
Allow renumbering: `false`

## Human-initiated request

The owner selected OD-2 Option A:

> SELECT OD-2 OPTION A: reaffirm the Root-owner/App-and-PEC-client boundary;
> after PR #360 merges, stage the minimal Root PRD amendment candidate and open
> Root SCOPE_CHANGE intake, without adopting PRD bytes or pre-approving any
> SCOPE_CHANGE gate.

The owner further required the Root PRD candidate to arrive with a runnable
deterministic concordance check for every `TRANSCRIBED` sentence and stated:

> No other OD is accepted by this message. OD-4 through OD-7 remain live gates.

This intake therefore opens Gate 1 only. It does not treat OD-2 selection as
Gate 1 confirmation, does not adopt a PRD amendment, and does not accept OD-4.

## Resolved current basis

| Field | Resolved value |
|---|---|
| Accepted decomposition | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` |
| Decomposition revision | `v1.0` |
| Decomposition acceptance | D-GOV-25; `AcceptedCandidateSHA ec62af0700e530c1640698fa406398cb1cb45d29` |
| Current working-tree basis | `918bb48b8fcee66c031d0d6d4040a46089f96067` |
| Current adopted PRD | `docs/PRD_ROOT.md` |
| Current PRD SHA-256 | `82f7ea2944e791f12de3a191cbe209a8e8ed90420b82af25ccb5df43d4cc94b3` |
| Runtime authority source | `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` |
| Runtime authority SHA-256 | `a6a4fc4f0c8136f0cdf25eab155c98a03276248776ed9ff779df6c4b88523f11` |
| Scope-change root | `execution/_ScopeChange/` |
| Next available amendment ID | `SCA-001` |

The PRD amendment authorized for staging by OD-2 is not yet adopted. Every
parsed action in this intake is therefore
`CONTINGENT_ON_PRD_ADOPTION`. Gate 2 may not open until:

1. the owner explicitly confirms this Gate 1 intake; and
2. exact Root PRD amendment bytes are separately adopted through their owning
   instrument.

## Semantic section binding

Bindings were resolved by heading text as required:

| Semantic section | Bound heading / surface |
|---|---|
| Change Register | `## 13. Decision Log / Change Log` and revision notes in the working surface |
| Unit Ledger | `## 10. Scope Ledger`; authoritative rows in `chirality_root_scope_ledger_v1_0.csv` |
| Objectives | `## 7. Objectives`; authoritative mappings in the ledger and `chirality_root_objective_register_v1_0.csv` |
| Primary Partitions | `## 8. Packages` |
| Secondary Entities | `## 9. Deliverables`; authoritative rows in `chirality_root_deliverable_register_v1_0.csv` |
| Coverage Basis | `## 11. Coverage and Telemetry`, the forward/reverse registers, and the Gate 1 `AUDIT_DECOMP` snapshot |

## Intake interpretation boundary

The requested effect is to establish a standing Root decomposition carrier for
continuing stewardship and assurance of the Root-owned generic runtime after
the PRD makes that duty a product commitment. Gate 1 does not decide whether
that carrier is a new deliverable, a modification of an existing deliverable,
or a combined topology amendment. That choice belongs to the impact and exact
amendment gates and must be derived from the adopted PRD rather than invented
here.

No package, deliverable, objective, dependency, estimate, schedule, PRD,
governance, or product file is modified by this intake.
