# Guidance: DEL-024-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-024` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD" package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned MV VFD design work (topology, cells, isolation transformer, output filter, cooling) with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for the driven motor identity/service, harmonic mitigation, installation location, building assignment, area classification, communications protocol, and support details until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: MV service voltage and grounding regime, electrical-building housing possibilities, grounding/bonding rules, MV cable basis, cable tray/conduit routing, and Zone 2 VFD-fed motor temperature-code rules.

## Considerations

The DBM electrical design basis supports the facility 4.160 kV three-phase three-wire 60 Hz low-resistance-grounded service for process AC inverter-drive motors rated 250 hp up to 5,500 hp. A 2000 hp 4160 V VFD-driven motor falls within that service basis. The DBM also states that VFD and soft-starter requirements for 4.16 kV motors are `TBD`, so the package-specific VFD topology, harmonic mitigation, and reactive-power treatment should not be asserted by the EPC datasheet beyond what source supports.

The workbook row and Gate 7 registers support the existence and interface profile of the package (six interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports), but not detailed MV VFD performance values or driven-load identity. The package-specific Word requirements source did not produce a PKG-024 match during this run; therefore, vendor-facing datasheet content should remain conservative until the missing detailed requirements are resolved.

The Comp and Liquids DBM source describes 4160V MCC patterns and starting VFDs in detail for specific inlet compressor motors (KM-2150/KM-2250 at 5,200 hp / 4,000 V). PKG-024 is rated 2000 hp at 4160 V and does not match the KM-2150/KM-2250 starting VFD description by rating or voltage. The datasheet should not borrow that motor-specific basis as if it applied to PKG-024; it should use the DBM only at the level of generic 4.16 kV MCC/VFD facility patterns.

Grounding and bonding are applicable interface topics. The DBM source contains facility grounding basis (two-point grounding for major electrical equipment; separate copper ground conductors per CEC sizing for transformers, panelboards, and three-phase motors larger than 100 hp). The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing or connection details.

Maintenance access is an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The datasheet should require electrical routing and physical placement to preserve maintenance access, but detailed clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Driven motor identity and service | Mark `TBD` pending source confirmation. | The workbook name identifies a 2000 hp 4160 V drive but does not name a driven motor tag, process service, or duty; no DBM slice ties this drive to a process equipment item. |
| MV VFD topology and harmonic mitigation | Defer to detailed electrical studies and vendor selection; do not specify in datasheet. | DBM states 4.16 kV VFD/soft-starter requirements are `TBD` and that harmonic/reactive-power mitigation is determined by detailed electrical studies. |
| Installation location | Identify electrical-building housing as possible context, not a confirmed location. | DBM states electrical buildings may house MV VFDs but does not assign PKG-024. |
| Standalone vs MCC-integrated arrangement | Leave to vendor design and detailed electrical study. | The DBM's 4.16 kV MCC paragraph does not state whether 4.16 kV VFDs are MCC-integrated or standalone; the 600 V VFD rule (MCC-integrated, no standalone except dedicated to large motors) is voltage-specific and does not transfer. |
| Standards | List CEC, NEMA MG1, area classification, and project electrical specifications as governing bases with locations `TBD`. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 26 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Driven motor tag, service, and process duty: `TBD`. No package-specific source slice available."
- Not acceptable without new source: "PKG-024 drives inlet compressor KM-2150 via a starting VFD." The accessible source set ties KM-2150/KM-2250 to 4,000 V 5,200 hp starting VFDs, not to a 4160 V 2000 hp VFD package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-024-02-001 | Workbook PKG-024 names a 2000 hp 4160 V VFD but no accessible source slice identifies the driven motor, process service, or duty. | Workbook Packages row 26; `PACKAGE_REGISTER.csv` row `PKG-024` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical and equipment-list sections | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat driven motor identity/service as `TBD` until vendor data or process-electrical alignment confirms it. | TBD |
| HRR-024-02-002 | DBM states 4.16 kV VFD/soft-starter requirements are `TBD`; topology, harmonic mitigation, and isolation-transformer arrangement for PKG-024 are unresolved. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph | Datasheet Attributes; Specification Requirements; Guidance Trade-offs | Defer to detailed electrical studies and vendor selection; do not assert package-specific VFD topology or filtering in datasheet. | TBD |
| HRR-024-02-003 | Whether PKG-024 is standalone or integrated into the 4160 V MCC lineup is unspecified; DBM rules for standalone vs MCC-integrated VFDs apply at 600 V, not 4.16 kV. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 600 V MCC/VFD paragraph (line ~2959) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph (lines ~752-756) | Datasheet Construction; Specification Requirements; Procedure Steps | Leave standalone vs MCC-integrated arrangement as `TBD` for vendor and detailed electrical study. | TBD |
