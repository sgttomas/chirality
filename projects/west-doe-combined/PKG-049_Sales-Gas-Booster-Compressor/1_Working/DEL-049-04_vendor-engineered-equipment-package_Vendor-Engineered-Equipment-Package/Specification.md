# Specification: DEL-049-04 — Vendor Engineered Equipment Package

This specification defines the normative requirements for the **production
unit** "Vendor Engineered Equipment Package" of PKG-049 Sales Gas Booster
Compressor. It governs what the Package Vendor must engineer, design, document,
and supply, and how the EPC Integrator confirms the unit is acceptable for
integration. It does not redefine equipment-level requirements that the
Vendor's own datasheets carry under this unit.

## Scope

### In scope

- Package engineering of the sales gas booster compressor package described in SOW-0170, SOW-0171, SOW-0172 (`SCOPE_LEDGER.csv`).
- Package design (mechanical, structural-on-skid, piping-on-skid, on-skid utilities, on-skid I&C and electrical to the package interface points).
- Vendor documentation supporting the package (vendor design basis, vendor datasheets for major equipment listed in SOW-0171, vendor drawings, calculations as required by source standards — location TBD).
- Fabrication / supply of the physical equipment package.
- Vendor support to the EPC Integrator's integration review of the package.

### Out of scope (by EPC / Others — SOW-0172)

- Shipping of the package to site.
- Installation on piles.
- Tie-in piping outside the package boundary.
- Field electrical connections outside the package boundary.
- Mounting platform and stairs.
- EPC-led facility integration deliverables (DEL-049-01, DEL-049-02, DEL-049-03, DEL-049-06).

## Requirements

Requirements are grouped by the production-unit responsibilities recorded in
`PACKAGE_REGISTER.csv` (PKG-049 responsibility model) and OBJ-004.

### R1 — Package basis and authority

| ID | Requirement | Source |
|---|---|---|
| R1.1 | The engineered package SHALL be developed from and remain consistent with the EPC Scope of Work (DEL-049-01) and EPC Package Datasheet (DEL-049-02). | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` (DEL-049-04 description) |
| R1.2 | Where the EPC Package Datasheet defines an interface requirement, the engineered package SHALL terminate that interface as defined; the Vendor SHALL NOT redefine EPC-owned interface scope. | OBJ-004; `PACKAGE_REGISTER.csv` (PKG-049 responsibility model) |

### R2 — Process design conditions

| ID | Requirement | Source |
|---|---|---|
| R2.1 | The package SHALL be designed for a process capacity of 3,962 e3m3/day (140 MMSCFD); no turndown. | SOW-0172 |
| R2.2 | Suction design pressure SHALL be 6,137 kPag (890 psig). | SOW-0172 |
| R2.3 | Discharge design pressure SHALL be 12,866 kPag (1,866 psig). | SOW-0172 |
| R2.4 | Summer inlet operating temperature SHALL be 110 °F (43.3 °C); other ambient/operating ranges TBD from upstream source documents (`location TBD`). | SOW-0172 |
| R2.5 | Suction scrubber inlet liquid density SHALL be designed against the 0.61 SG assumption stated in the source. | SOW-0172 |

### R3 — Major equipment composition

| ID | Requirement | Source |
|---|---|---|
| R3.1 | The package SHALL include an Ariel KBX/X reciprocating compressor with all cylinders dedicated. | SOW-0171 |
| R3.2 | The compressor SHALL be driven by an 8-pole induction motor rated 4,000 V / 3 PH / 60 Hz, 891 rpm, 1,000 kW (1,340 HP), TEFC or WPII, non-sparking bidirectional cooling fan, conforming to NEMA MG 1. | SOW-0171; SOW-0172 |
| R3.3 | The driver SHALL use a DOL configuration with soft-start. | SOW-0171 |
| R3.4 | The package SHALL include a forced-air intercooler after each cylinder stage, mounted on a common frame, designed per API 661, horizontal-air-flow type, single-fan, with automated louver control. | SOW-0171 |
| R3.5 | The package SHALL include a two-phase vertical-flow mesh/vane suction scrubber after each cylinder booster stage; size and capacity SHALL be vendor-designed. | SOW-0171 |
| R3.6 | The package SHALL include a two-phase packing vent / drain separation pot designed for at least 101 kPag; size and capacity SHALL be vendor-designed. | SOW-0171 |
| R3.7 | The package SHALL include a seal-pot waste-oil transfer pump; size and capacity SHALL be vendor-designed. | SOW-0171 |
| R3.8 | The package SHALL include a filter coalescer rated for 0.3 micron at 99.97 %, with a band-lock-type QOC, sized for 100 MMSCFD design flow. | SOW-0171 |

### R4 — Interfaces at the package boundary

| ID | Requirement | Source |
|---|---|---|
| R4.1 | The package SHALL terminate cleanly at each PKG-049 applicable interface type listed in `INTERFACE_REGISTER.csv`: Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports. | `INTERFACE_REGISTER.csv` (PKG-049) |
| R4.2 | Termination point details (size, rating, location, signal list, load schedule) SHALL be taken from the EPC Package Datasheet (DEL-049-02). Specific values TBD until DEL-049-02 is produced. | `_CONTEXT.md`; OBJ-004 |

### R5 — Vendor documentation

| ID | Requirement | Source |
|---|---|---|
| R5.1 | The Vendor SHALL produce a vendor package design basis covering process, mechanical, structural-on-skid, on-skid electrical, on-skid I&C, and safety provisions consistent with R2 and R3. | `_CONTEXT.md` Anticipated Artifacts; OBJ-010 |
| R5.2 | The Vendor SHALL produce equipment-level datasheets for the major equipment listed in R3. | `_CONTEXT.md` Anticipated Artifacts; SOW-0171 |
| R5.3 | The Vendor document register, submittal schedule, and turnover documentation are produced under DEL-049-05 (Vendor Document Turnover Package); this unit SHALL supply the required content to that deliverable. | `DELIVERABLE_REGISTER.csv` (DEL-049-05) |

### R6 — Boundary exclusions

| ID | Requirement | Source |
|---|---|---|
| R6.1 | Shipping, pile installation, tie-in piping, field electrical connections, and mounting platform/stairs SHALL be excluded from the engineered-package scope and identified as "by others" in vendor documentation. | SOW-0172 |

## Standards

The following standards are explicitly invoked by source material; full clause
text was not opened in this run (`location TBD`).

| Standard | Application | Source |
|---|---|---|
| API 661 | Air-cooled heat exchangers (intercoolers, R3.4). | SOW-0171 |
| NEMA MG 1 | Motors (driver, R3.2). | SOW-0172 |

Additional standards likely apply (sour-service practice per OBJ-009 — e.g.,
NACE; pressure-vessel and piping codes — e.g., ASME). These are
**ASSUMPTION: likely applicable** and SHALL be confirmed from the upstream
package requirements document and DBM before being added as normative.

## Verification

| Req | Verification approach |
|---|---|
| R1.1, R1.2 | Documented review by EPC Integrator under DEL-049-06 against DEL-049-01 and DEL-049-02. |
| R2.1–R2.5 | Vendor design basis review and equipment datasheet cross-check by EPC Integrator. |
| R3.1–R3.8 | Vendor datasheet and drawing review; factory inspection/test records consistent with the standards in §Standards. |
| R4.1, R4.2 | Interface matrix walkdown against `INTERFACE_REGISTER.csv` (PKG-049) and DEL-049-02 termination details. |
| R5.1–R5.3 | Vendor document register completeness check under DEL-049-05; content traceability check under DEL-049-06. |
| R6.1 | Boundary-of-supply matrix in vendor documentation, confirmed against SOW-0172. |

Detailed acceptance criteria, witness/hold points, and FAT scope: **TBD** —
requires the upstream RFQ / package requirements document slices (location TBD).

## Documentation

Per `_CONTEXT.md` Anticipated Artifacts, the production unit SHALL deliver:

1. The vendor-engineered physical equipment package (the package itself).
2. The vendor package design basis and datasheet set.

Additional vendor-document submittals and turnover records are governed by
DEL-049-05.
