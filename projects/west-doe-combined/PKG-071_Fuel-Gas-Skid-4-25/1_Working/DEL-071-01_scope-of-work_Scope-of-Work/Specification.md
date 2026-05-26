# Specification: DEL-071-01 — Scope of Work (PKG-071 Fuel Gas Skid 4-25)

## Scope

### In scope

This Scope of Work specification governs the EPC Integrator's articulation of the PKG-071 Fuel Gas Skid 4-25 package, covering:

- Package identity and function (single low-pressure fuel gas skid serving the 04-25 Deep Cut facility's low-pressure fuel gas system). Source: SCOPE_LEDGER SOW-0100; 26020-Package_Requirements.docx package heading 25.
- Major included equipment basis: 1 skid, 1 low-pressure fuel gas heater (SCR-driven, 600 V; skin-temperature thermocouple override), 1 low-pressure fuel gas scrubber (k = 0.35 imperial max + de-ration factor; vendor-designed). Source: SCOPE_LEDGER SOW-0101.
- Operating and design conditions (capacity, pressure, temperature ranges). Source: SCOPE_LEDGER SOW-0102.
- Vendor/EPC responsibility split as the authoritative responsibility model for the package. Source: PACKAGE_REGISTER.csv; SCOPE_LEDGER SOW-0099.
- Applicable interface types for whole-facility integration. Source: PACKAGE_REGISTER.csv.

### Out of scope (By Others, per source)

- Shipping packages to site.
- Installation.
- Tie-in piping.
- Electrical tie-in.

Source: SCOPE_LEDGER SOW-0102 — "By others" enumeration.

Also out of scope for this deliverable (delegated to sibling DEL-071-02..06 within the same package):

- Package datasheet (DEL-071-02).
- Construction work package (DEL-071-03).
- Vendor-engineered equipment package (DEL-071-04).
- Vendor document turnover package (DEL-071-05).
- EPC-vendor package review and acceptance (DEL-071-06).

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-071-01-01 | The Scope of Work SHALL identify the package as "Fuel Gas Skid 4-25", Workbook ID 71, WBS 01, Mechanical discipline. | PACKAGE_REGISTER.csv; Workbook Packages row 61 |
| REQ-071-01-02 | The Scope of Work SHALL state the package function as serving the low-pressure fuel gas system for the West Doe Deep Cut Facility. | SCOPE_LEDGER SOW-0100 |
| REQ-071-01-03 | The Scope of Work SHALL enumerate the major included equipment: 1 skid, 1 low-pressure fuel gas heater, 1 low-pressure fuel gas scrubber. | SCOPE_LEDGER SOW-0100, SOW-0101 |
| REQ-071-01-04 | The Scope of Work SHALL record the fuel gas heater control basis: SCR control panels at 600 V, located in the electrical building, with skin temperature thermocouple override on the heater. | SCOPE_LEDGER SOW-0101, SOW-0102 |
| REQ-071-01-05 | The Scope of Work SHALL record the fuel gas scrubber sizing basis: k-factor of 0.35 (imperial) maximum plus de-ration factor for operating pressure; vendor-designed. | SCOPE_LEDGER SOW-0101 |
| REQ-071-01-06 | The Scope of Work SHALL record design throughput as > 8.4 MMSCFD (237.5 e3m3/day); final flow TBD. | SCOPE_LEDGER SOW-0102 |
| REQ-071-01-07 | The Scope of Work SHALL record outlet gas temperature as 95 F (35 C) and operating pressure as 150 psig. | SCOPE_LEDGER SOW-0102 |
| REQ-071-01-08 | The Scope of Work SHALL record design pressure as 150 psig and design temperature range as -40 C to 35 C; MAWP TBD. | SCOPE_LEDGER SOW-0102 |
| REQ-071-01-09 | The Scope of Work SHALL record ambient temperature range as -19 C to 22.2 C. | SCOPE_LEDGER SOW-0102 |
| REQ-071-01-10 | The Scope of Work SHALL state the by-others exclusions: shipping to site, installation, tie-in piping, electrical tie-in. | SCOPE_LEDGER SOW-0102 |
| REQ-071-01-11 | The Scope of Work SHALL state the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, physical equipment package; EPC Integrator owns interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | PACKAGE_REGISTER.csv; ART-451A242BFC |
| REQ-071-01-12 | The Scope of Work SHALL list the applicable interface types: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv |
| REQ-071-01-13 | The Scope of Work SHALL cross-reference covered scope items SOW-0099, SOW-0100, SOW-0101, SOW-0102 and the supporting objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. | DELIVERABLE_REGISTER.csv |
| REQ-071-01-14 | The Scope of Work SHALL identify the package source basis as Workbook Packages row 61 and 26020-Package_Requirements.docx package heading 25. | DELIVERABLE_REGISTER.csv |
| REQ-071-01-15 | The Scope of Work SHALL be authored by the EPC Integrator. | DELIVERABLE_REGISTER.csv (ResponsibleParty) |

## Standards

| Standard / Reference | Applicability | Source |
|---|---|---|
| Source workbook (26020-Packages_Interfaces_4_export.xlsx) | Authoritative package register | `_REFERENCES.md`; PACKAGE_REGISTER.csv |
| 26020-Package_Requirements.docx, package heading 25 | Authoritative package requirements text for PKG-071 | `_REFERENCES.md`; DELIVERABLE_REGISTER.csv |
| Sour-service, codes, standards basis | Inherited via OBJ-009 (location TBD; specific codes not enumerated in PKG-071 source row) | OBJ-009; ASSUMPTION at the package level |
| ASME / PED pressure vessel codes for scrubber and heater | ASSUMPTION (typical for fuel-gas scrubbers and SCR-heated vessels at 150 psig); not stated in PKG-071 source row | ASSUMPTION; location TBD |

## Verification

| ReqID(s) | Verification Method | Acceptance Criterion |
|---|---|---|
| REQ-071-01-01..03, 13, 14 | Document review against PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv | Identity, function, equipment list, scope item IDs, source basis present verbatim or equivalent |
| REQ-071-01-04..09 | Tabular review of operating and design conditions against SCOPE_LEDGER SOW-0101, SOW-0102 | All listed parameters present with values or explicit TBD |
| REQ-071-01-10 | Inspection for explicit "By others" enumeration | Four by-others items present |
| REQ-071-01-11 | Inspection for responsibility-split statement | Both vendor and EPC responsibility lists present, matching PACKAGE_REGISTER.csv |
| REQ-071-01-12 | Inspection of applicable interface types list | Twelve interface types present |
| REQ-071-01-15 | EPC Integrator sign-off record | Human authorship and approval evidence (per K-AUTH-1) |

## Documentation

The Scope of Work artifact set this deliverable produces:

- ART-AC01900208 — Package scope of work (this artifact suite; SOW narrative).
- ART-31BC19483F — Tagged equipment and package identity list.
- ART-5369838D71 — Package function and whole-facility integration narrative.
- ART-451A242BFC — Package responsibility assignment record.
- ART-CD58F7CD21 — Detailed mechanical package scope extraction evidence (reference back to source slices used).

Source: ARTIFACT_REGISTER.csv (rows for DEL-071-01).
