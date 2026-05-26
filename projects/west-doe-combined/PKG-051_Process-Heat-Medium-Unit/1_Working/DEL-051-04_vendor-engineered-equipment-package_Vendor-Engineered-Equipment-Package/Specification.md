# Specification — DEL-051-04 Vendor Engineered Equipment Package (PKG-051 Process Heat Medium Unit)

## Scope

This specification governs the Package Vendor's engineered scope of supply for the Process Heat Medium Unit (PKG-051) as the package-vendor production unit dispatched by the EPC Scope of Work (DEL-051-01) and Package Datasheet (DEL-051-02).

In scope (per `_CONTEXT.md` and SCOPE_LEDGER SOW-0165..0168):
- Package engineering, package design, vendor documentation, and the physical equipment package for the Process Heat Medium Unit.
- Supply Pump Module: expansion tank and heat medium circulation pumps.
- Medium Heater Module: medium heater, heater blower, air intake pre-heater.
- Closed-loop heat medium delivery to the EPC's process-user interface points.

Excluded from the Vendor Package (by-others per `SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Scope notes and open items, via SCOPE_LEDGER SOW-0168):
- Interconnecting piping outside the vendor skid battery limits.
- DCS integration.
- Foundations.
- Mounting buildings at site.
- Electrical supply from MCC.
- Platforms, stairs, etc.

## Requirements

### R-1 Modular configuration
The vendor shall supply the package as two modules — Supply Pump Module and Medium Heater Module — populated per the equipment list in Datasheet §Attributes. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SOW-0166.)

### R-2 Pump duty and configuration (workbook basis)
The vendor shall supply three (3) single-stage vertical inline heat medium pumps in 3 x 66% configuration with the design pressure 2413 kPag (350 psig) and operating pressure 695 kPag (100 psig) as stated in Datasheet §Conditions. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Major included equipment, via SOW-0167.)

ASSUMPTION: "design pressure ... and temp." in the source is interpreted as design pressure 2413 kPag and design temperature 274 deg C; the source text fragments these two parameters and the design-temperature value (274 deg C) appears later in the slice. Vendor shall confirm both.

### R-3 Expansion tank
The vendor shall supply one (1) horizontal expansion tank with size and capacity advised by vendor, sized such that expansion volume at 274 deg C fills the expansion tank to a maximum of 85%. Operating pressure 125 to 240 kPag (18 to 23 psig) depending on heat medium NPSHR. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Major included equipment, via SOW-0167.)

### R-4 Heat medium fluid
The vendor shall supply the package compatible with Petro Canada Peterotherm as the heat medium transfer fluid, with maximum bulk temperature 260 deg C (500 deg F) and assumed start-up temperature 20 deg C (68 deg F). (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Major included equipment, via SOW-0167.)

CONFLICT: DBM-Deepcut §"Heat Medium Basis" specifies Brenntag Petrotherm at single unified loop 220 deg C / 428 deg F maximum normal operating temperature with maximum bulk fluid temperature 599 deg F (315 deg C). See Conflict Table in `Guidance.md` (`SourcePath`: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `SectionRef`: lines 1947-1959).

### R-5 Loop arrangement (workbook basis)
The package shall be configured for a hot loop / cold loop arrangement enabling mixing of hot and cold heat medium to deliver optimum supply to process users. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SOW-0166.)

CONFLICT: DBM-Deepcut retires hot/cold loop segregation in favour of a single unified loop with a single pump module and single expansion tank. See Conflict Table.

### R-6 Heater module
The vendor shall supply one (1) medium heater, one (1) heater blower, and one (1) air intake pre-heater. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SOW-0166.)

ASSUMPTION: Heater type, fuel basis, duty, draft type, and burner arrangement are not stated in the accessible source slice for PKG-051. Detailed heater requirements: TBD. DBM-Deepcut (line 1998) characterizes the heat medium heater as an API-560 natural-draft cabin-style direct-fired thermal-fluid heater with 1.25 x winter steady-state design duty, listed here as candidate basis pending Conflict Table resolution.

### R-7 Total heat medium throughput
The package shall be configured for a total heat medium supply of approximately 151.6 m3/day. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Scope notes and open items, via SOW-0168.) Verification of this throughput against any updated facility-level demand basis: TBD.

### R-8 Vendor documentation
The vendor shall supply the vendor package design basis and datasheet set listed in `_CONTEXT.md` §Anticipated Artifacts. Detailed document list, format, and turnover schedule: governed by DEL-051-05 (Vendor Document Turnover Package); TBD content in this specification.

### R-9 Battery-limit exclusions
The vendor shall design the package consistent with the by-others exclusions stated in Scope (Specification §Scope), i.e., interconnecting piping, DCS integration, foundations, site mounting buildings, electrical MCC supply, and platforms/stairs are not part of the vendor scope. (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Scope notes and open items, via SOW-0168.)

### R-10 Interface compatibility
The package shall be deliverable with interfaces compatible with the PKG-051 applicable interface types listed in PACKAGE_REGISTER row PKG-051: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. (`SourcePath`: `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`; `SectionRef`: row PKG-051.)

## Standards

| Standard | Applicability | Source |
|---|---|---|
| API-560 | Direct-fired thermal-fluid heater design (candidate basis) | DBM-Deepcut line 1998 (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`); ASSUMPTION: likely applicable, pending Conflict Table resolution |
| Pressure-vessel design code | Expansion tank, heater coil pressure-containing components | TBD — not stated in accessible source slices for PKG-051; ASSUMPTION: ASME BPVC Section VIII applicable (jurisdictional default for vendor-engineered pressure equipment); confirmation TBD |
| Pump standard | Heat medium pumps | TBD — not stated in accessible source slices |
| Material/metallurgy | Hot-oil service materials | TBD — not stated in accessible source slices |
| Electrical area classification | Package electrical | TBD — DBM-Deepcut line 2000 indicates "General Purpose" for the heater area; package-wide area classification TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 | Vendor general-arrangement drawings and equipment list review by EPC Integrator |
| R-2 | Vendor pump datasheet and curve review; hydraulic verification against R-7 throughput |
| R-3 | Vendor expansion-tank datasheet; sizing calculation review |
| R-4 | Vendor fluid selection statement and MSDS; confirmation against design temperature |
| R-5 | Vendor P&ID review (loop arrangement) — pending Conflict Table ruling |
| R-6 | Vendor heater datasheet, performance prediction, and burner/blower selection |
| R-7 | Vendor heat & material balance demonstrating ≥ 151.6 m3/day capability |
| R-8 | Cross-reference verification against DEL-051-05 turnover package |
| R-9 | Vendor scope-of-supply matrix vs by-others exclusions |
| R-10 | Vendor interface tie-in schedule cross-checked against PKG-051 INTERFACE_REGISTER rows |

## Documentation

Anticipated artifacts (`_CONTEXT.md` §Anticipated Artifacts):
- Vendor engineered physical equipment package (the deliverable itself).
- Vendor package design basis and datasheet set.

Additional documentation deliverables: governed by DEL-051-05 (Vendor Document Turnover Package). TBD here.
