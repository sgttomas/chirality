# Specification — DEL-079-01 Scope of Work: Instrument Air Building (PKG-079)

## Scope

### In scope
- Definition of the EPC Integrator scope of work for the Instrument Air Building package (PKG-079, tracking 26020-01-39-001, tag 26020-01-PT-39-001), including the EPC integration of a vendor-supplied instrument air package into the whole 04-25 Deepcut facility. (Source: _CONTEXT.md; PACKAGE_REGISTER.csv; SOW-0131.)
- Carriage of the package identity, basic scope, major included equipment list, design/operating conditions, and ten declared package interfaces as the authoritative EPC anchor for downstream PKG-079 deliverables (Package Datasheet DEL-079-02, Construction Work Package DEL-079-03, Vendor Engineered Equipment Package DEL-079-04, Vendor Document Turnover DEL-079-05, EPC Vendor Package Review and Acceptance DEL-079-06). (Source: DELIVERABLE_REGISTER.csv rows DEL-079-01 .. DEL-079-06; SCOPE_LEDGER.csv SOW-0131..0134 deliverable mapping.)

### Out of scope (carried by other parties or other deliverables)
- Package engineering, package design, vendor documentation, and physical equipment supply — owned by Package Vendor (see DEL-079-04 and DEL-079-05). (Source: PACKAGE_REGISTER.csv responsibility model; OBJ-004.)
- Shipping of compressor packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs are explicitly "By Others" in the package requirements. They are carried in the EPC construction work package (DEL-079-03) and EPC interface scope, not authored by the Package Vendor. (Source: SOW-0134 Scope notes — By others.)
- Package-specific exclusions beyond the above are TBD; no package-specific exclusions are stated in source materials. (Source: PACKAGE_REGISTER.csv Exclusions = "TBD; no package-specific exclusions stated in source materials".)

## Requirements

### R1 — Vendor / EPC responsibility split (REQUIREMENT)
The Package Vendor shall own package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator shall own integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: PACKAGE_REGISTER.csv responsibility-model cell; OBJ-004.) Verification: see V1.

### R2 — Package basic scope (REQUIREMENT)
The instrument air package shall consist of: two (2) motor-driven oil-injected rotary screw air compressors, one (1) wet air receiver, two (2) dryer pre-filters, one (1) regenerative desiccant air dryer, one (1) after-filter, and one (1) dry air receiver (or two 50% capacity receivers). (Source: SOW-0132 = 26020-Package_Requirements.docx package heading 32 — Basic scope.) Verification: V2.

### R3 — Major equipment ratings (REQUIREMENT, from source)
- R3.1: Each instrument air compressor shall be oil-injected rotary screw, air-cooled, rated 1113 SCFM at 861 kPag (125 psig) discharge pressure, electric motor driven. (Source: SOW-0133.)
- R3.2: Each compressor motor shall be 250 HP electric, soft starter or VFD ready, with anti-condensation space heaters. Operating envelope: 200-250 HP, 600V/3PH/60Hz, TEFC, non-classified, speed TBD by vendor. (Source: SOW-0133; SOW-0134.)
- R3.3: Air dryer shall be 100% capacity, two tanks/towers (one operating, one regenerating), sized for two compressors and "leave"; size and capacity TBD by vendor. (Source: SOW-0133.)
- R3.4: One common after-filter shall be located downstream of the combined dryer outlets. (Source: SOW-0133.)
- R3.5: Wet air receiver, dryer pre-filters, and dry air receiver sizing TBD by vendor. (Source: SOW-0132; SOW-0133.)
Verification: V3.

### R4 — Design and operating pressures (REQUIREMENT)
- R4.1: All PSVs in the system shall be set at 948 kPag (137.5 psig). (Source: SOW-0133.)
- R4.2: Compressor maximum discharge / shutdown shall be 1000 kPag. (Source: SOW-0134.)
- R4.3: Maximum system design pressure shall be 1034 kPag (150 psig). (Source: SOW-0134.)
- R4.4: Minimum system pressure shall be 551 kPag (80 psig). (Source: SOW-0134.)
- R4.5: Facility shutdown pressure shall be 482 kPag (70 psig). (Source: SOW-0134.)
Verification: V4.

### R5 — Air quality (REQUIREMENT)
Delivered instrument air shall have a maximum water dewpoint of -73.3 °C at 1000 kPag. (Source: SOW-0133; SOW-0134.) Verification: V5.

### R6 — Capacity (REQUIREMENT)
Design throughput shall be 1113 SCFM at 861 kPag (125 psig). (Source: SOW-0134.) Verification: V6.

### R7 — Design temperature (REQUIREMENT)
Equipment shall be suitable for design temperature range -40 °C to 38 °C. (Source: SOW-0134.) Verification: V7.

### R8 — Package interfaces (REQUIREMENT)
The EPC Scope of Work shall preserve and carry the following ten facility-level interface types as interface obligations between the vendor package and the facility: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. (Source: INTERFACE_REGISTER.csv rows IFC-* for PKG-079; PACKAGE_REGISTER.csv applicable_interface_types.) Verification: V8.

### R9 — "By Others" scope assignment (REQUIREMENT)
The following are explicitly outside the Package Vendor's package supply and are assigned to the EPC Integrator (and/or other site parties): shipping of compressor packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs. (Source: SOW-0134 Scope notes — By others.) Verification: V9.

### R10 — Coverage of declared scope items (REQUIREMENT)
This Scope of Work shall carry SOW-0131, SOW-0132, SOW-0133, and SOW-0134 from the workbook and the package requirements document. (Source: _CONTEXT.md; SCOPE_LEDGER.csv.) Verification: V10.

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Project standards for sour-service, fire-and-gas, environmental, regulatory, codes (per OBJ-009) | Applicable to PKG-079 to the extent that instrument air system supports safety/shutdown functions | Location TBD — DBM-Deepcut/4-25_Deepcut_DBM.md SEC-14, SEC-15 cited in OBJECTIVE_REGISTER.csv OBJ-009; slice not re-read in this pass |
| Electrical area classification reference | Compressor motors stated "non-classified" in SOW-0134 implies an unclassified location; underlying area-classification document is TBD | Location TBD |
| Pressure equipment / PSV code | Implied by PSV set pressure requirement in R4.1; specific code reference not stated in available source slice | TBD |

ASSUMPTION: No code/standard clauses are derived in this pass beyond what is explicitly named in source. Standard clause-level requirements require dedicated source slice reads (candidate for Pass 3 enrichment).

## Verification

| ID | Verifies | Method |
|---|---|---|
| V1 | R1 | Responsibility assignment record exists in this deliverable; reviewed against PACKAGE_REGISTER.csv responsibility-model cell at acceptance. |
| V2 | R2 | Package vendor deliverable equipment list (DEL-079-04) reconciled against SOW-0132 equipment count and types. |
| V3 | R3 | Datasheet attribute table reconciled against vendor proposal and Package Datasheet (DEL-079-02). |
| V4 | R4 | Pressure schedule cross-checked against vendor P&ID, PSV schedule, and shutdown logic; values transcribed from SOW-0133/0134. |
| V5 | R5 | Vendor performance test record at delivery point shows dewpoint <= -73.3 °C @ 1000 kPag. |
| V6 | R6 | Vendor compressor performance curves confirm 1113 SCFM @ 861 kPag aggregate capacity. |
| V7 | R7 | Vendor equipment temperature ratings cover -40 °C to 38 °C. |
| V8 | R8 | Interface register entries IFC-E7D3353482, IFC-FBA5A1ED78, IFC-47DC520AA2, IFC-CD84DBE736, IFC-3B18C99DFD, IFC-C4F92A698B, IFC-75F0F21CEA, IFC-E10830EA2F, IFC-5BB5161DC0, IFC-0EC9E5E722 are each carried into the Package Datasheet (DEL-079-02) and Construction Work Package (DEL-079-03). |
| V9 | R9 | EPC Construction Work Package (DEL-079-03) shows shipping, piles, tie-in piping, electrical connections, mounting platform/stairs scope assignment. |
| V10 | R10 | Traceability matrix to SOW-0131..0134 included in EPC Vendor Package Review and Acceptance (DEL-079-06). |

## Documentation

Required documentation artifacts for this deliverable (per _CONTEXT.md anticipated artifacts):
- Package Scope of Work narrative (this deliverable set).
- Tagged equipment and package identity list (Datasheet.md Attributes section).
- Package function and integration narrative (Scope above; Guidance.md).
- Responsibility assignment record (R1; Guidance.md ownership split section).

Companion EPC deliverables (anticipated, not produced here):
- DEL-079-02 Package Datasheet — carries interface facts and design data as evidence.
- DEL-079-03 Construction Work Package — installation and tie-in plan.
- DEL-079-04 Vendor Engineered Equipment Package — vendor-produced.
- DEL-079-05 Vendor Document Turnover Package — vendor-produced.
- DEL-079-06 EPC Vendor Package Review and Acceptance — review record.

(Source: DELIVERABLE_REGISTER.csv PKG-079 rows.)
