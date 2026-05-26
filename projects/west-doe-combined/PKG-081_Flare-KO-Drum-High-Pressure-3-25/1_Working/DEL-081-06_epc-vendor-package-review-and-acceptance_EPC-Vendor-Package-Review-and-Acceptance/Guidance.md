# Guidance: DEL-081-06 — EPC Vendor Package Review and Acceptance

## Purpose

DEL-081-06 exists because PKG-081 (Flare KO Drum High Pressure 3-25) is a vendor-owned package within an EPC-integrated facility. The Package Vendor owns engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration. This deliverable is the EPC-side review and acceptance evidence that closes that responsibility loop and creates auditable handoff readiness. (Sources: `DELIVERABLE_REGISTER.csv` DEL-081-06 Notes; `PACKAGE_REGISTER.csv` PKG-081 Responsibility Model; `OBJECTIVE_REGISTER.csv` OBJ-004.)

## Principles

1. **Acceptance is not re-engineering.** The EPC Integrator reviews and accepts; it does not redo vendor engineering or rewrite vendor documents. (Source: OBJ-004; PKG-081 Responsibility Model.)
2. **The acceptance basis is the EPC trio.** EPC SOW, Package Datasheet, and Construction Work Package together define what "acceptable" means for this package. (Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-081-06.)
3. **Interfaces are the integration risk.** Most acceptance failure modes show up at the package boundary, not inside the vendor scope. Treat the ten declared interface categories as first-class review surfaces. (Source: `INTERFACE_REGISTER.csv` PKG-081 rows.)
4. **Carry safety, sour-service, and regulatory through.** OBJ-009 requires explicit visibility of sour-service, relief, flare/blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory items inside acceptance — not just inside the vendor scope. (Source: OBJ-009.)
5. **Open items are evidence, not failure.** Carrying the SOW-0074 scope-conflict open item through acceptance with a documented ruling is the correct outcome; silently resolving it is not. (Source: SOW-0074; OBJ-010.)
6. **Handoff readiness is the test.** Acceptance succeeds when downstream facility handoff (operability, maintainability, sparing, commissioning, turnover) is supported by evidence. (Source: OBJ-010.)

## Considerations

- **Source asymmetry.** The decomposition snapshot is locally accessible (CSV registers); the authoritative process mechanical requirements text is in `26020-Package_Requirements.docx` package heading 34, which is not text-accessible at draft time. Acceptance criteria sensitive to that text are `location TBD` until the source slice is extracted. (Source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv` PKG-081 Source References.)
- **Vendor input scope.** "Package Vendor input" in the responsibility line means the vendor supplies records, clarifications, and document submissions that feed EPC acceptance — it does not transfer acceptance authority to the vendor. (Source: `DELIVERABLE_REGISTER.csv` DEL-081-06.)
- **Cross-deliverable dependencies.** Acceptance materially depends on the maturity of DEL-081-01, DEL-081-02, DEL-081-03 (basis) and DEL-081-04, DEL-081-05 (vendor inputs). Acceptance evidence assembled before those siblings reach a usable state will require rework.
- **Interface owners.** Several interface categories (Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling) cross discipline boundaries; acceptance review must engage discipline reviewers, not just the mechanical lead. (Source: `INTERFACE_REGISTER.csv` PKG-081 rows; OBJ-005, OBJ-006.)
- **Sparing and isolation.** OBJ-010 calls out sparing, isolation, and winterization as handoff conditions; for an HP flare KO drum service these are typically meaningful and should be explicitly checked rather than assumed adequate.

## Trade-offs

- **Depth vs. timeliness.** Deeper clause-by-clause acceptance is more defensible but blocks on the unresolved `26020-Package_Requirements.docx` source slice. Pragmatic acceptance can proceed against the decomposition registers and the EPC trio with explicit `TBD` markers for clause-level checks, accepting the rework risk.
- **Open-item carry vs. defer.** Closing SOW-0074 (flare equipment in/out boundary) inside acceptance is faster but exceeds EPC authority (requires owner/engineering ruling). Carrying it as an open item is correct even though it delays sign-off.
- **Per-interface review vs. consolidated.** Per-interface evidence is heavier but supports OBJ-009 carry-through visibly; consolidated checks are lighter but make safety/interface gaps easier to miss.

## Examples

Source-grounded examples cannot be drawn from `26020-Package_Requirements.docx` package heading 34 at draft time (binary, location TBD). Examples from the decomposition:

- The PKG-081 Responsibility Model in `PACKAGE_REGISTER.csv` is itself a usable example of the responsibility language acceptance should preserve: "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration."
- SOW-0074 is the worked example for R-8: a scope conflict that must be tracked through acceptance with a ruling, not silently resolved.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-001 | Flare-system equipment is technically described in package requirements but listed as excluded in the DBM scope table; final in/out boundary requires owner/engineering ruling. | `SCOPE_LEDGER.csv` SOW-0074 (sourced to 26020-Package_Requirements.docx package heading 34, Scope notes and open items) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md scope table (location TBD; not re-read at draft time) | Specification R-1, R-3, R-8; Datasheet Conditions; Procedure Steps 2 and 7 | PROPOSAL: carry the package requirements description as in-scope for acceptance review, conditional on owner/engineering ruling per SOW-0074. | TBD |
