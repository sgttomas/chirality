# Specification: DEL-071-04 Vendor Engineered Equipment Package

## Scope

This specification covers the Package Vendor's production unit for PKG-071 (Fuel Gas Skid 4-25): the engineering, design, fabrication/supply, and physical equipment package developed from the EPC Scope of Work (DEL-071-01) and the EPC Package Datasheet (DEL-071-02). It defines what the vendor shall deliver as the skid-mounted Low-Pressure Fuel Gas package serving the low-pressure fuel gas system for the West Doe Deep Cut Facility.

In scope:
- Engineering and design of the skid-mounted package including the heater, scrubber, structural skid, package piping, package electrical and I&C, and package safety provisions.
- Fabrication or supply of the physical equipment package suitable for shipment and field installation.
- Vendor package design basis and the vendor datasheet set required to support the EPC Integrator's facility-level integration.

Out of scope (by others, per source):
- Shipping packages to site.
- Installation and tie-in piping at site.
- Electrical tie-in at site.
- Whole-facility integration, interface design beyond the package terminations, and procurement/construction coordination at the facility level (EPC Integrator responsibility under DEL-071-06).

## Requirements

| ID | Requirement | Source | Disposition |
|---|---|---|---|
| REQ-071-04-01 | The package shall be a single skid-mounted Low-Pressure Fuel Gas Package comprising one (1) low-pressure fuel gas heater and one (1) low-pressure fuel gas scrubber. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0100; SOW-0101 | FACT |
| REQ-071-04-02 | A skid shall be provided for the system to be mounted on. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101 | FACT |
| REQ-071-04-03 | The fuel gas heater shall be controlled by SCR (600 V). SCR heater control panels are located in the electrical building (panels themselves are not within the skid). | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101; SOW-0102 | FACT |
| REQ-071-04-04 | The heater shall include skin-temperature thermocouple override control. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101 | FACT |
| REQ-071-04-05 | The fuel gas scrubber shall be sized using a k factor of 0.35 (imperial) maximum, plus a de-ration factor for operating pressure; vendor to design. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101 | FACT |
| REQ-071-04-06 | The package shall be designed for a required process flow > 8.4 MMSCFD (237.5 e3m3/day) with outlet gas heated to 95 F (35 C). Final flow is TBD by detailed engineering / EPC Package Datasheet. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 | FACT (final flow TBD) |
| REQ-071-04-07 | Operating Pressure: 150 psig. Design Pressure: 150 psig. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 | FACT |
| REQ-071-04-08 | Ambient Temperature range: -19 C to 22.2 C. Design Temperature range: -40 C to 35 C. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 | FACT |
| REQ-071-04-09 | MAWP shall be established by the vendor in detailed engineering. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 | TBD |
| REQ-071-04-10 | Heater capacity shall be established by the vendor based on the EPC Package Datasheet design flow, temperature rise, and fuel-gas heating value. | Gate 7 `SCOPE_LEDGER.csv`, SOW-0101 | TBD |
| REQ-071-04-11 | The package shall provide terminations supporting the twelve declared facility interfaces: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | Gate 7 `INTERFACE_REGISTER.csv`, PKG-071 rows | FACT |
| REQ-071-04-12 | The package design and equipment shall be developed from the EPC Scope of Work (DEL-071-01) and the EPC Package Datasheet (DEL-071-02). The EPC Package Datasheet governs vendor-facing technical inputs. | `_CONTEXT.md`, Scope; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-04 | FACT |
| REQ-071-04-13 | Vendor documentation shall be produced and handed over under DEL-071-05 (Vendor Document Turnover Package). The list of vendor documents and submittals is governed by source vendor documentation requirements and the EPC Package Datasheet. | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-071-05; PKG-071 PACKAGE_REGISTER row | FACT (specific document list TBD) |
| REQ-071-04-14 | Package-specific exclusions beyond the "by others" items in REQ-071-04-15 are not stated in the accessible source materials. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-071 (Exclusions column) | TBD |
| REQ-071-04-15 | The vendor scope shall exclude shipping packages to site, installation, tie-in piping, and electrical tie-in at site (by others). | Gate 7 `SCOPE_LEDGER.csv`, SOW-0102 | FACT |

## Standards

- Governing project Design Basis Memorandum: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (West Doe 4-25 deepcut basis; the package serves the low-pressure fuel gas system referenced throughout the DBM).
- 26020-Package_Requirements.docx package heading 25 — package-specific requirements; clause-level text not locally accessible (binary source). Vendor-facing requirements derived from the EPC Package Datasheet (DEL-071-02) shall take precedence at vendor-handoff.
- 26020-01-PT-RFQ-23-001_FG_Skid_2.docx — vendor RFQ basis referenced by the package register; not locally accessible at this run.
- Specific codes (e.g., ASME pressure vessel codes for the scrubber, applicable electrical and heater standards for SCR control, hazardous-area classification standards) are ASSUMPTION: likely applicable to mechanical/electrical packages of this type; exact clauses TBD pending vendor RFQ content and EPC Package Datasheet review. Location: TBD.

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-071-04-01, -02, -03, -04, -05 | Vendor design review and equipment inspection against the EPC Package Datasheet and 26020-Package_Requirements.docx package heading 25. |
| REQ-071-04-06, -07, -08, -09, -10 | Process and mechanical design review; vendor datasheet check; pressure-test certificates and nameplate verification at fabrication. |
| REQ-071-04-11 | Interface termination check against `INTERFACE_REGISTER.csv` PKG-071 rows and the EPC Package Datasheet interface matrix; turnover under DEL-071-05 and acceptance under DEL-071-06. |
| REQ-071-04-12 | Design basis review confirming the vendor package traces back to DEL-071-01 and DEL-071-02. |
| REQ-071-04-13 | Vendor document register completeness check under DEL-071-05. |
| REQ-071-04-14, -15 | Scope confirmation against the EPC Scope of Work and PACKAGE_REGISTER PKG-071 Exclusions field. |

## Documentation

Anticipated artifacts produced under this deliverable:
- Vendor engineered physical equipment package (the skid and its mounted equipment).
- Vendor package design basis (process, mechanical, structural, electrical, I&C) supporting the equipment as built.
- Vendor datasheet set for the heater, scrubber, and skid as needed to support EPC Integrator review and turnover.

Documentation handed over downstream:
- The vendor document register and submittals are produced and tracked under DEL-071-05 (Vendor Document Turnover Package).
- EPC Integrator review evidence is produced under DEL-071-06 (EPC Vendor Package Review and Acceptance).
