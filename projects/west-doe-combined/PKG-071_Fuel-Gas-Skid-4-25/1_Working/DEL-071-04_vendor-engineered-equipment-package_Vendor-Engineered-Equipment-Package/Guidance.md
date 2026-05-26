# Guidance: DEL-071-04 Vendor Engineered Equipment Package

## Purpose

This deliverable exists because the Fuel Gas Skid 4-25 is a vendor-responsible Mechanical package: the Package Vendor owns engineering, design, fabrication/supply, and the physical equipment package, while the EPC Integrator owns whole-facility integration. The four-document kit here orients the vendor work to the EPC inputs (Scope of Work, Package Datasheet) and to the facility-level integration and acceptance work performed by the EPC Integrator (Construction Work Package, Vendor Document Turnover, EPC Review and Acceptance).

## Principles

- The Package Vendor's design basis must be traceable to the EPC Package Datasheet (DEL-071-02); the EPC Package Datasheet governs vendor-facing technical inputs to this package.
- Source-supported facts (equipment list, control concept, operating and design conditions, interface types) are treated as binding for the vendor scope; values declared TBD in the source remain TBD in this kit until the vendor establishes them in detailed engineering.
- The package serves the low-pressure fuel gas system that supports many facility services across the West Doe 4-25 deepcut plant (blanket gas, purge, sweep, stripping, supplemental fuel). The package design should preserve availability and operability of these downstream services.

## Considerations

- The Fuel Gas Skid 4-25 (PKG-071) and the Fuel Gas Skid 3-25 (PKG-084) are companion packages serving the 4-25 and 3-25 plants respectively. Shared fuel-gas and instrument-air arrangements between 03-25 and 04-25 are described in the DBM; the vendor work for PKG-071 should not assume sharing beyond what the EPC Package Datasheet states.
- The heater control panels (SCR, 600 V) reside in the electrical building (by-others location), not on the skid. Vendor's heater design must accommodate field cabling and termination to remote SCR panels.
- Scrubber sizing is governed by a k-factor (0.35 imperial max) with operating-pressure de-ration; the vendor is responsible for selecting equipment that meets the EPC Package Datasheet flow and gas-quality basis.
- The package must terminate twelve interface types declared in the Gate 7 INTERFACE_REGISTER. Interface mechanical termination details (locations, sizes, ratings) follow from the EPC Package Datasheet.

## Trade-offs

- Heater capacity sizing trades off design-margin against capital cost; capacity is TBD pending EPC Package Datasheet flow and heating-value confirmation. ASSUMPTION: heating value comparable to the companion 3-25 package basis (1040 BTU/SCF) unless DEL-071-02 states otherwise.
- Scrubber internals selection (mesh, vane, etc.) trades off liquid removal efficiency against pressure drop; vendor judgement governs within the k-factor envelope.
- Single skid vs. multi-skid splits trade off shipping and constructability against fabrication economy; the source basis specifies a single skid.

## Examples

- Process-side fuel-gas demand examples from the DBM include: low-pressure fuel gas for pig-receiver sweet-gas purge before opening; MPFF purge and sour-gas sweep; stabilizer flash/feed separator drive and sweep gas; amine and TEG surge-tank blanket and purge; sales-gas splitter / buyback gas connections; caustic and DSO tank blanketing; VRU make-up/blanket gas at ~2 oz setpoint; incinerator supplemental fuel. These illustrate the breadth of downstream services the LP fuel-gas package supports, motivating reliability and adequate capacity in the heater and scrubber.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | No source conflicts identified in this Pass 2 sweep. Heating value and final flow are TBD in the source rather than conflicting. | n/a | n/a | n/a | n/a | n/a |
