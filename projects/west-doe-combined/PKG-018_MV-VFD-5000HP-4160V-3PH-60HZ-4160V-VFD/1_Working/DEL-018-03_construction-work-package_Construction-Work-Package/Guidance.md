# Guidance: DEL-018-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-018` into an EPC-owned, source-supported description of how the MV VFD package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. It should let field construction execute the installation and tie-in workface plan and let commissioning accept turnover, while keeping vendor-owned package engineering with the Package Vendor.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat the six workbook interface `X` facts as construction-checklist evidence within this Construction Work Package, not as separate deliverables.
- Keep vendor-owned package engineering and design with the Package Vendor; the Construction Work Package describes EPC-side installation and integration only.
- Use `TBD` for VFD ratings, topology, harmonic mitigation, cooling, enclosure, bypass, weights, dimensions, modular split, lift plan, foundation loads, cable schedules, installation location, pre-energization checks, and commissioning hold points until a source-supported package-specific basis or vendor data is accepted.
- Use the DBM construction scope as the controlling facility construction basis and align the workface plan to it (mechanical hookups, home-run cabling, terminations, pipe supports, tie-ins, module offloading and setting).
- Use SCA-001 VE #34 (starting VFDs for KM-2150/KM-2250) and SCA-001 VE #37 (capacitor banks removed from synchronous bus on MCC-8200 where VFDs are present) only where the DBM cites them; do not extend their force beyond the cited source.

## Considerations

The DBM identifies the 4160V MCC as providing field-fused contactors, motor protection relays, and EtherNet communication to the plant PLC central control panel. The Construction Work Package should organize VFD tie-in work around that MCC interface, including power, control, and communications terminations.

The DBM facility construction scope is broad (grading, foundations, modules, home-run cabling, terminations, etc.). The Construction Work Package should scope installation and tie-in work for PKG-018 within this construction basis rather than redefining it.

Grounding and bonding are applicable as both a construction installation activity and a tie-in coordination activity. The Construction Work Package should require coordination with facility grounding basis (two-point ground-grid connection for major equipment, separate CEC-sized copper ground conductors for certain electrical equipment) without overstating package-specific conductor sizing details that the source does not provide.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint. The Construction Work Package should require physical placement, cable tray, and conduit routing that preserve maintenance access; detailed clearances remain `TBD` until detailed design or vendor data is issued.

The accessible source set does not contain a package-specific lift plan, modular split, foundation load schedule, harmonic study output, or commissioning hold-point list for PKG-018. The Construction Work Package should not invent these.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| VFD topology / harmonic mitigation | Defer to detailed electrical studies; do not specify mitigation in the construction package. | DBM explicitly leaves harmonic and reactive-power mitigation to detailed studies; SCA-001 VE #37 only removes capacitor banks where VFDs are present. |
| Modular split / lift plan | Mark `TBD`; align to vendor general arrangement and module drawings when issued. | No accessible source slice defines PKG-018 modular split, weights, or lift requirements. |
| Installation location | Identify electrical-building housing as possible context, not a confirmed location. | DBM permits electrical-building housing for MV equipment but does not locate PKG-018. |
| Pre-energization / commissioning hold points | Carry as `TBD`; coordinate with vendor commissioning plan and EPC commissioning procedures. | No accessible source slice defines hold points for this package. |
| Standards | List CEC, NEMA MG1 (motor basis), area classification, project electrical/construction specifications, and SCA-001 actions as governing bases with locations TBD. | DBM cites these bases but detailed clauses/specifications are not available in the deliverable folder. |
| Motor allocation assumption | Treat the inlet-compressor (KM-2150/KM-2250) starting-VFD basis as the most likely served load (ASSUMPTION); confirm before issue for construction. | The 4000 V, ~5,200 hp inverter-duty motors with starting VFDs under SCA-001 VE #34 are the only accessible source-identified loads that match the package title closely, but PKG-018 → KM-2150/KM-2250 allocation is not confirmed in source. |

## Examples

- Acceptable construction-package entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 20 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Lift plan and modular split: TBD pending vendor general arrangement and module drawings."
- Acceptable tie-in entry: "VFD output and control wiring shall terminate at the 4160V MCC field-fused contactor and motor protection relay; EtherNet/PRP communication shall terminate to the plant PLC central control panel per detailed design (source: DBM 4160V MCC section)."
- Not acceptable without new source: "Install harmonic filters rated X MVAR at MCC-8200." The accessible source set does not establish this scope.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-018-03-001 | Package title states "MV VFD - 5000HP, 4160V" but DBM-identified inverter-duty motors are 4,000 V / ~5,200 hp (KM-2150, KM-2250). Voltage/horsepower allocation between the package title and the only accessible source-identified loads is not confirmed. | Workbook Packages row 20; `PACKAGE_REGISTER.csv` row `PKG-018` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, inlet compressor motor and 4160V MCC sections | Datasheet Attributes; Specification Requirements; Procedure Steps | Treat the inlet-compressor starting-VFD basis under SCA-001 VE #34 as the most likely served load (ASSUMPTION); preserve workbook ratings (5000 HP / 4160 V) as package title until vendor data or detailed electrical design resolves the allocation. | TBD |
| HRR-018-03-002 | The Construction Work Package needs a vendor general arrangement, modular split, lift plan, foundation loads, and commissioning hold points to be fully issuable for construction, but no accessible source slice provides these for PKG-018. | `_REFERENCES.md` source set | `_Sources/26020-Package_Requirements.docx` (no accessible PKG-018 construction match identified during this run) | Datasheet Construction; Specification Requirements; Procedure Steps | Carry these as `TBD` and gate issue-for-construction on vendor documentation and EPC detailed design output. | TBD |
