# Specification — DEL-068-01 Scope of Work (PKG-068 TEG Dehydration Unit)

## Scope

This Scope of Work (SOW) defines the EPC Integrator's binding scope statement for procuring, integrating, and delivering the TEG Dehydration Unit package (PKG-068, Workbook row 97, package tag 26020-01-22-001 / 26020-01-PT-22-001) within the West Doe 04-25 Deepcut expansion facility.

In scope:

- The package identity, tagged equipment list, package function, source basis, package boundaries, and whole-facility integration narrative for PKG-068, as identified in `PACKAGE_REGISTER.csv` row PKG-068 and `DELIVERABLE_REGISTER.csv` row DEL-068-01.
- Definition of the EPC Integrator's facility-side scope: integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (`PACKAGE_REGISTER.csv` row PKG-068).
- Definition of the Package Vendor's package-side scope: package engineering, package design, vendor documentation, and the physical equipment package (`PACKAGE_REGISTER.csv` row PKG-068).
- Coverage of SOW items SOW-0237, SOW-0238, SOW-0239, SOW-0240 (`_CONTEXT.md`).

Out of scope (this deliverable):

- The Package Datasheet itself (DEL-068-02), Construction Work Package (DEL-068-03), Vendor Engineered Equipment Package (DEL-068-04), Vendor Document Turnover Package (DEL-068-05), and EPC Vendor Package Review and Acceptance (DEL-068-06) — produced as sibling deliverables in PKG-068.
- Detailed process design values; these are carried in the Package Datasheet (DEL-068-02). Values cited in this SOW are for scope framing only.

## Requirements

### R-068-01-01 — Package Identity and Tag Schedule (FACT)

The EPC Integrator shall identify the TEG Dehydration Unit as PKG-068, workbook package tag 26020-01-22-001 (source identifier 26020-01-PT-22-001), Workbook row 97, discipline Mechanical, WBS 01. Source: `PACKAGE_REGISTER.csv` row PKG-068.

Verification: cross-check against `PACKAGE_REGISTER.csv` row PKG-068.

### R-068-01-02 — Tagged Equipment List (FACT)

The EPC SOW shall list the following package equipment for vendor supply: Inlet Air Cooler, Filter Coalescer, TEG Contactor, Glycol Flash Tank, Glycol Reboiler/Still Column, Glycol Circulation Pumps, Glycol Particulate Filters, Glycol Charcoal Filter, Gas/Glycol Exchanger, Air/Glycol Exchanger, Fuel Gas Scrubber, TEG Make-up Tank, Burner Control Panel. Source: `PACKAGE_REGISTER.csv` row PKG-068 scope statement.

Individual tag numbers per equipment item shall be issued in the Package Datasheet (DEL-068-02); item-level tag numbers are TBD here.

Verification: line-item check against PACKAGE_REGISTER row 97 scope text.

### R-068-01-03 — Package Function (FACT)

The package shall provide process-gas TEG dehydration of sweet, water-saturated natural gas downstream of amine treating and upstream of molecular-sieve dehydration. Source: DBM-Deepcut SEC-06 "Process-Gas TEG Dehydration Basis", l.1187–1193; package basis l.1102–1113.

Verification: trace SOW function statement to DBM SEC-06 process description.

### R-068-01-04 — Vendor Scope Assignment (FACT)

The Package Vendor shall be responsible for package engineering, package design, vendor documentation, and the physical equipment package. Source: `PACKAGE_REGISTER.csv` row PKG-068 description.

Verification: SOW responsibility matrix lists each item under Package Vendor.

### R-068-01-05 — EPC Integrator Scope Assignment (FACT)

The EPC Integrator shall be responsible for integrating the package into the whole process facility, covering interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row PKG-068 description.

Verification: SOW responsibility matrix lists each item under EPC Integrator.

### R-068-01-06 — Applicable Interface Types (FACT)

The SOW shall declare the following interface types as applicable to PKG-068 and assign each to the responsible party: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. Source: `PACKAGE_REGISTER.csv` row PKG-068 `interfaces` column.

Per-interface design data shall be carried in the Package Datasheet (DEL-068-02).

Verification: each interface type appears in the SOW interface section with a named responsible party.

### R-068-01-07 — Whole-Facility Integration Narrative (FACT/ASSUMPTION)

The SOW shall include a whole-facility integration narrative placing the TEG unit between amine treating (upstream) and molecular-sieve dehydration (downstream), with rich-TEG flash gas routed to the stabilizer overheads compressor (SOC) first-stage suction and still overheads routed to the VRU. Source: DBM-Deepcut SEC-06 l.1187–1193 (process description); l.1223 (flash gas to SOC); l.1227 (still overheads to VRU); SEC-04 l.842 (SOC interfaces include TEG glycol flash).

Verification: narrative is consistent with DBM SEC-06 process description and SEC-04 SOC interfaces list.

### R-068-01-08 — Source Basis Citation (FACT)

The SOW shall cite as authoritative source basis: 26020-Package_Requirements.docx package heading 23; Bid Docs/Budgetary/26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx; and the West Doe Deepcut DBM SEC-06. Source: `PACKAGE_REGISTER.csv` row PKG-068 `word_source_basis` column; `_REFERENCES.md`.

Where the RFQ or Word source slice is not locally accessible, the citation shall mark `location TBD` (see Conflict / TBD register in `Guidance.md`).

Verification: SOW source-basis section enumerates the three sources and flags non-accessible items.

### R-068-01-09 — Coverage of SOW Items (FACT)

The SOW shall cover SOW-0237, SOW-0238, SOW-0239, SOW-0240. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-068-01.

Verification: SOW item-coverage table lists all four IDs.

### R-068-01-10 — Objective Traceability (FACT)

The SOW shall record support of OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (explicit deliverable-level rows in `OBJECTIVE_DELIVERABLE_MAP.csv`).

Verification: SOW objective-traceability table lists all nine OBJ IDs.

### R-068-01-11 — Exclusions Statement (TBD)

The SOW shall include an explicit exclusions section. Source basis (`PACKAGE_REGISTER.csv` row PKG-068 `exclusions` column) records "TBD; no package-specific exclusions stated in source materials"; the EPC Integrator shall confirm package-level exclusions during early-design review and update the SOW.

Verification: SOW exclusions section is present; any item left TBD is flagged for human ruling.

## Standards

The TEG Dehydration Unit package design is governed by the broader facility standards basis (jurisdictional codes, ABSA, CSA, API, ASME) referenced by the West Doe Deepcut DBM and the package source documents. No package-specific governing code list is enumerated in the locally accessible sources for PKG-068; the governing standards list is `TBD` pending review of the RFQ and Word package source slice (location TBD; not in `_Sources/`).

## Verification

| Requirement | Verification approach | Evidence target |
|---|---|---|
| R-068-01-01 | Document review against PACKAGE_REGISTER row PKG-068 | SOW identity section |
| R-068-01-02 | Line-item check vs. PACKAGE_REGISTER row 97 scope | SOW equipment list |
| R-068-01-03 | Trace to DBM SEC-06 process description | SOW function statement |
| R-068-01-04, -05 | Responsibility matrix review | SOW responsibility matrix |
| R-068-01-06 | Interface section completeness check | SOW interfaces section |
| R-068-01-07 | Narrative review vs. DBM SEC-06 / SEC-04 | SOW integration narrative |
| R-068-01-08 | Source citation review; TBD flags audited | SOW source basis section |
| R-068-01-09 | Item-coverage table check | SOW SOW-item coverage table |
| R-068-01-10 | Objective table check vs. OBJECTIVE_DELIVERABLE_MAP | SOW objective table |
| R-068-01-11 | Exclusions section presence + TBD audit | SOW exclusions section |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Package scope of work
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record
