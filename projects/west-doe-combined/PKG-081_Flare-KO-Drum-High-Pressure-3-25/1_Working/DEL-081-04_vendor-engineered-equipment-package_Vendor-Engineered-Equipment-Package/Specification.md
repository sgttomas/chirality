# Specification: DEL-081-04 — Vendor Engineered Equipment Package (Flare KO Drum, High Pressure, 3-25)

> Normative requirements the Package Vendor production unit must satisfy. Requirements are derived from the EPC Scope of Work (DEL-081-01, TBD), the EPC Package Datasheet (DEL-081-02, TBD), and locally accessible DBM source slices. Requirements not yet anchored to issued source artifacts are marked **ASSUMPTION** or **TBD**.

## Scope

### In Scope
- Engineering, design, fabrication/supply, and physical assembly of the high-pressure flare knockout drum (HP KO drum) vendor package for the 03-25 facility under PKG-081.
- Vendor package design basis and datasheet set covering the supplied equipment, including the KO drum vessel, internals (if any), associated transfer pump(s) `P-4100-2` / `P-4150-2` (1 x 100 percent per KO drum) `[SourcePath: _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md; SectionRef: SEC-09 Sparing Philosophy]`, instrumentation, local piping/valves within package battery limits, structural steel/skidding (if any), and electrical/instrument terminations at the package interface.
- Vendor-side integration interface to the HP relief header (508 mm / 20 inch in current source basis) `[SourcePath: same DBM; SectionRef: Flare and Blowdown]` and to the HP/Cryo flare stack downstream.
- Vendor coordination with the EPC Integrator integration review.

### Out of Scope
- Issue of the EPC Scope of Work, Package Datasheet, and Construction Work Package (handled by DEL-081-01, DEL-081-02, DEL-081-03).
- Site civil/foundation construction beyond the vendor-supplied skid (covered by Construction Work Package).
- HP flare stack design and procurement (separate scope).
- LP flare KO drum service (separate package — DBM identifies V-3900-2 / P-3900-2 as LP service).
- Vendor document turnover compilation (DEL-081-05) and EPC vendor-package review/acceptance (DEL-081-06).

## Requirements

### R-1 — Service definition
The package shall be engineered for high-pressure flare knockout service receiving HP relief from the HP relief header and discharging vapor to the HP/Cryo flare stack, with separated liquids routed to a transfer pump for truck-out or transfer to slop. `[SourcePath: _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md; SectionRef: Flare and Blowdown]`

### R-2 — Equipment tag identity
The package shall be supplied to the equipment tag specified in the EPC Package Datasheet — one of `V-4100-2` (compressor area) or `V-4150-2` (tank farm). **NEEDS_HUMAN_RULING.** `[SourcePath: same DBM; SectionRef: Flare and Blowdown]`

### R-3 — Design pressure and temperature
Vessel and packaged components shall meet the design pressure and design temperature stated in the EPC Package Datasheet (DEL-081-02). **TBD** until DEL-081-02 is issued. `[location TBD]`

### R-4 — Relief load and sizing
Vessel sizing (vapor handling, droplet separation, liquid hold-up) shall accommodate the rated HP relief load assigned to this drum by the final flare studies, with staggered blowdown assumed to limit maximum relief. `[SourcePath: DBM; SectionRef: Flare and Blowdown — staggered blowdown required; final basis in W242510-PRC-REP-000003-001, location TBD]`

### R-5 — Header interface
Inlet and outlet nozzles shall be compatible with HP relief and HP flare header sizing (current source basis 508 mm / 20 inch). Final nozzle sizes and ratings per Package Datasheet. `[SourcePath: DBM; SectionRef: Flare and Blowdown]` `[location TBD for ratings]`

### R-6 — Transfer pump
The package shall include the associated KO drum transfer pump (`P-4100-2` or `P-4150-2`) sized to truck-out or transfer separated liquids to slop, supplied as 1 x 100 percent per KO drum. `[SourcePath: DBM; SectionRef: SEC-09 Sparing Philosophy + Flare and Blowdown]`

### R-7 — Materials of construction
Materials shall be selected for the served stream classification, including sour-service compliance where the served headers carry sour fluids. **ASSUMPTION: sour-service applicability is likely.** Confirm against EPC Package Datasheet and project materials specification. `[SourcePath: DBM; SectionRef: Isolation philosophy / sour service discussion (line ~607)]`

### R-8 — Codes and standards
The package shall conform to the standards listed in the Standards section below as called up by the EPC Package Datasheet. **location TBD** at clause level until DEL-081-02 issues.

### R-9 — Instrumentation
The package shall include level (high/low/high-high), pressure, and temperature instrumentation as required by the EPC Package Datasheet, with safe failure modes and protocol/wiring per project instrumentation specification. `[location TBD]`

### R-10 — Isolation, drains, vents
Vent and drain connections shall route to the correct flare, drain, or closed system based on pressure, sour-service, and contamination class. Spectacle blinds, paddle blinds, or removable spool provisions shall be incorporated where positive isolation is required for intrusive maintenance. `[SourcePath: DBM; SectionRef: Isolation philosophy paragraph at line ~607]`

### R-11 — Documentation deliverables
The vendor shall produce a complete vendor package design basis and datasheet set covering all supplied equipment, suitable for downstream consumption by DEL-081-05 (Vendor Document Turnover Package) and DEL-081-06 (EPC Vendor Package Review and Acceptance). `[SourcePath: _CONTEXT.md; SectionRef: Anticipated Artifacts]`

### R-12 — Integration review
The vendor shall support the EPC Integrator integration review, including interface verification (process, mechanical, electrical, instrumentation, civil tie-ins). `[SourcePath: _CONTEXT.md; SectionRef: ResponsibleParty]`

## Standards

| Standard / Document | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 34 | Governing package requirements for PKG-081 | `_Sources/26020-Package_Requirements.docx` (heading 34 text not extracted in this run — **location TBD** at clause level) |
| 3-25 Comp_and_Liquids DBM, Flare and Blowdown / SEC-09 / Isolation Philosophy sections | Facility design basis for HP flare/KO services | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| EPC Package Datasheet for PKG-081 (DEL-081-02) | Project-specific design conditions and ratings | Not yet issued — **location TBD** |
| EPC Scope of Work for PKG-081 (DEL-081-01) | Scope envelope and split | Not yet issued — **location TBD** |
| Pressure vessel code (e.g., ASME BPVC Section VIII, or equivalent jurisdictional code) | Vessel design | **ASSUMPTION**; confirm in EPC Package Datasheet |
| Applicable flare/relief design standards (e.g., API 521, API 537) | Relief and flare service design basis | **ASSUMPTION**; confirm in EPC Package Datasheet and final flare studies |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1, R-2 | Design review against Package Datasheet; nameplate inspection |
| R-3 | Vessel design calculations review; pressure test certification; material certification |
| R-4 | Sizing calculation review against flare-study relief case; demonstration of staggered blowdown assumption used |
| R-5 | Nozzle schedule review; flange rating audit; alignment with HP header tie-in drawings |
| R-6 | Pump performance test (vendor witness); installation per package P&ID; sparing confirmation |
| R-7 | Material test reports (MTRs); sour-service NACE conformance certificates where applicable |
| R-8 | Code stamp / certification documents; jurisdictional registration where required |
| R-9 | I/O list review; loop checks; FAT |
| R-10 | P&ID review; isolation/blind list verification |
| R-11 | Documentation completeness check against turnover index (DEL-081-05 acceptance) |
| R-12 | EPC integration review sign-off (DEL-081-06) |

## Documentation

The vendor production unit shall deliver:

- Vendor engineered physical equipment package (as-supplied)
- Vendor package design basis
- Vendor package datasheet set (vessel, pump, instruments, electrical, structural)
- Calculation set (vessel design, pump sizing, relief sizing acceptance)
- General arrangement drawings, P&ID, isometrics for package-internal piping
- Material test reports and code certification
- FAT records
- Operating and maintenance manuals
- Spare parts list
- Vendor data ready for the Vendor Document Turnover Package (DEL-081-05)

(Source: `_CONTEXT.md` Anticipated Artifacts; standard vendor-package documentation set as **ASSUMPTION** until EPC Package Datasheet enumerates the exact list.)
