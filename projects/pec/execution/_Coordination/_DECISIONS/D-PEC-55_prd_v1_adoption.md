# D-PEC-55 — RULED: adopt PRD v1.0 and deprecate the v0.4 product framing

**Status:** RULED 2026-07-10 — owner adoption act; documentation-only fence
**Decision ID:** D-PEC-55
**Structure precedent:** `D-PEC-54_team_information_hub_prd.md` (direct owner
instruction, ruled behavior, exact fence, verification/rollback, and bounded ruling)

## Owner direction

Owner direction of record (Ryan Tufts, in-session, 2026-07-10):

> "adopt the v1.0 candidate PRD now and deprecate the v0.4 PRD in the manner
> intended."

"The manner intended" is the supersession path the candidate itself declared
(`docs/PRD.md` header: "Intended supersession | PRD v0.4 product framing upon
adoption") and the gate D-PEC-54 left open ("Adoption of PRD v1.0 and runtime
implementation remain owner acts"). This packet closes the adoption gate. It does
not execute or authorize the T0 rebaseline.

## Ruled behavior

1. `docs/PRD.md` v1.0 (team information hub) is **adopted** as the product
   definition of record for PEC, effective 2026-07-10.
2. The PRD v0.4 product framing is **deprecated and superseded**. The historical
   v0.4 requirement catalogue remains preserved in Git at
   `7e8312172:projects/pec/docs/PRD.md` and remains citable as the prototype
   baseline; it no longer states the product PEC is to become.
3. `SPEC.md` and `TRACEABILITY.md` remain the **implemented prototype baseline**
   documentation (v0.4-derived). Adoption does not create any claim of v1.0
   conformance by the current application. They stand until the T0
   product-and-authority rebaseline (per
   `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md`) replaces
   them under its own owner-ruled packet.
4. Status/basis notices in `PRD.md`, `SPEC.md`, `TRACEABILITY.md`, `STATUS.md`,
   and `README.md` are updated from "candidate / adoption open" to
   "adopted 2026-07-10 (D-PEC-55) / rebaseline pending".
5. The standing plan's product gate (loop protocol step 1) is recorded as
   satisfied; the next owner gate is direction to execute T0.
6. Runtime implementation remains parked. No requirement in PRD v1.0 becomes an
   implementation mandate by this adoption alone; each tranche still requires
   its own D-PEC packet (workplan step 3). The PRD §20 open product decisions
   remain open and must not be guessed.

## Exact fence

- `projects/pec/docs/PRD.md` (header status/supersession fields and basis notes only)
- `projects/pec/docs/SPEC.md` (historical-basis notice only)
- `projects/pec/docs/TRACEABILITY.md` (prototype-baseline notice only)
- `projects/pec/docs/STATUS.md` (product-direction note only)
- `projects/pec/README.md` (PRD references only)
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-55_prd_v1_adoption.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md` (gate-state notes only)
- `_DomainEngines/pec/LOOP_RECEIPTS.md`

No runtime source, dependency, database, demo input, report, requirement text,
or external system change is authorized by this row. The PRD v1.0 requirement
content itself is not modified — only its status fields and basis notes.

## Verification and rollback

- Verify no `docs/` or `README.md` surface still describes v1.0 as a candidate
  or adoption as open.
- Verify the v0.4 Git object `7e8312172:projects/pec/docs/PRD.md` resolves.
- Verify SPEC/TRACEABILITY still clearly disclaim v1.0 conformance of the
  current application.
- Run self-check, coordination check, and `git diff --check`.
- Roll back by reverting the documentation/coordination commit; no data rollback
  exists.

## Human ruling

**RULED (adoption):** PRD v1.0 is adopted and the v0.4 product framing is
deprecated, per the quoted direct owner instruction. The T0 rebaseline and all
runtime implementation remain future owner-gated acts.
