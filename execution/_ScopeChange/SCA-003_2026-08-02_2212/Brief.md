---
amendment_id: SCA-003
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 1
created: 2026-08-02
status: GATE_1_PREPARED_BASIS_CONFLICT_BLOCKS_CONFIRMATION
accepted_basis_claim: execution/_ScopeChange/_LATEST.md identifies Root decomposition revision 1.2 as accepted
frozen_git_basis: 97678a841ef58345c73d3470ed8de57c9b1405d2
requested_by: Root owner through HELP_HUMAN run ROOT_FOUR_LANES_2026-08-02
allow_renumbering: false
---

# SCA-003 — Root product-delivery / App runtime-route intake

## Posture

This snapshot opens the owner-initiated `TM-ROOT-107` SOFTWARE scope-change
intake and records the deterministic portion of Gate 1. It changes no Root
product basis, decomposition, companion register, deliverable metadata,
runtime contract, App/Piping surface, or lifecycle state. `_LATEST.md` remains
unchanged and continues to identify SCA-002 because Gate 5 has not opened.

Gate 1 is not confirmed. The owner direction authorizes intake, not an
amendment or any of the five SCOPE_CHANGE gate decisions.

## Exact human-initiated request

Process
`execution/_Coordination/_TaskManagement/SCOPE_CHANGE_INTAKE_TM-ROOT-107_2026-08-02.md`
using exactly these two named inputs:

1. `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`
   at SHA-256
   `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`;
2. `execution/_Coordination/OWNER_INTENT_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`
   at SHA-256
   `9bbb67556765c6c83d6a35a1ace297e4d693d5169281c620dc9b2673229c7e03`.

Both hashes match current repository bytes. The first input is an ordinary
App coordination notice that grants no Root authority. The second is expressly
`COORDINATION, NOT AUTHORITY`, says it is not a PRD or scope input, and requires
a separate owner-initiated product-basis act for any such effect. Opening this
SCA is the owner-initiated assessment act; it does not silently transform
either coordination input into accepted Root product truth.

## Resolved runtime variables

| Field | Resolved value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `execution/` |
| `DECOMPOSITION_PATH` | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` |
| `SCOPE_CHANGE_ROOT` | `execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-003` (returned by `tools/query/scan_next_amendment_id.sh`) |
| `ALLOW_RENUMBERING` | `false` |
| Allowed writes at current gate | this SCA-003 snapshot and its bounded audit evidence only |

## Semantic section binding

Resolved by heading text, not section number:

| Semantic section | Bound heading / authoritative surface |
|---|---|
| Change Register | `Decision Log / Change Log` in the Root working surface |
| Unit Ledger | `Scope Ledger`; `chirality_root_scope_ledger_v1_0.csv` |
| Objectives | `Objectives`; `chirality_root_objective_register_v1_0.csv` |
| Primary Partitions | `Packages` |
| Secondary Entities | `Deliverables`; `chirality_root_deliverable_register_v1_0.csv` |
| Coverage Basis | `Coverage and Telemetry` plus forward/reverse registers |

## Gate-1 parse

The two inputs request an assessment, not an exact decomposition edit. They
identify affected concerns but provide no before/after value for any valid
`ADD`, `REMOVE`, `MODIFY`, `RECLASSIFY`, `MERGE`, or `SPLIT` action. Therefore
`Parsed_Actions.csv` contains zero atomic amendment rows.

The provisional evidence-based disposition is **NO DECOMPOSITION AMENDMENT
CURRENTLY SHOWN**:

- the accepted ledgers already allocate declared capability scope to
  `DEL-02-04`, path/containment conformance to `DEL-03-01`, generic runtime
  semantics and affected-client evidence to `DEL-02-06`, and downward variant
  specialization/non-weakening to `DEL-06-04`;
- DEL-02-06's accepted `ScopeOfWork.md` already carries compatibility identity,
  affected-client census, fail-closed behavior, recovery/replay, evidence, and
  later implementation/release gates; exact sandbox/native-tool semantics can
  be specified under a later bounded deliverable activation without changing
  decomposition topology or mappings;
- the D-APP-84 request for a successor to the former Root Bash/full-worktree
  paragraph is overtaken by the later owner act at commit `e012e5824`: Root
  development-time Bash/worktree containment is harness-owned and the copied
  App-harness paragraph was removed from `AGENTS.md`; the App-owned runtime
  policy remains App-owned;
- the product-delivery direction creates no Root product-basis delta by its own
  explicit terms, and the existing variant-service carrier already admits
  working-root specialization without transferring generic Root authority.

`Provisional_Disposition.csv` records the unit-by-unit reasoning. This is a
Gate-1 proposal only, not an accepted no-change ruling.

## Current-basis integrity blocker

The current state does not present one internally consistent accepted basis:

1. `_ScopeChange/_LATEST.md`, the SCA-002 application append, and the Root loop
   handoff identify decomposition revision 1.2 as accepted and applied.
2. The live decomposition at the exact SCA-002 applied SHA still labels itself
   `SCA-002 CANDIDATE`, `not accepted`, says all five SCOPE_CHANGE gates are
   pending, and says revision 1.1 remains accepted.
3. The Root loop handoff calls PRD Revision 8 accepted, while the live
   `docs/PRD_ROOT.md` header and document-control table still call Revision 7
   an adoption-ready candidate and Revision 6 the accepted predecessor. The
   D-8 row itself says `ADOPTED (Rev 8)`.

These are direct current-state contradictions, not merely stale historical
files. SCOPE_CHANGE may not silently choose one side or repair them under this
two-input intake. Gate 1 remains blocked pending an owner-directed antecedent
basis reconciliation or an explicit instruction that incorporates exact
repair actions into a separately bounded amendment.

## Exact Gate-1 question

After the basis contradiction is dispositioned, is the intended intake:

> confirm a zero-action/no-decomposition-change disposition because the
> existing carriers are sufficient and all exact generic-contract,
> activation, client, implementation, and release work remains behind its
> own instruments and gates?

If not, the owner must name the exact decomposition entity and requested field
or topology change so it can be parsed and validated without invention.
