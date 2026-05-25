# Guidance: DEL-021-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-021` into a source-supported, field-executable construction basis. It should describe how the 6.9 kV switchgear equipment will be installed, built, inspected, turned over, and tied into the larger facility systems, while keeping EPC-owned facility integration distinct from vendor-owned package engineering and from Tourmaline field construction scope.

## Principles

- Preserve source spelling and identity. The package name is carried as "6.9kV SWITCHGEAR EQUIPMENT" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as the authoritative interface scope for the Construction Work Package; the CWP must address all six interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
- Keep responsibility unambiguous: Package Vendor designs and supplies; EPC Integrator integrates; Tourmaline Oil Corporation executes field construction (per DBM Construction Responsibility section).
- Ground the construction basis in the DBM SEC-12 Electrical Basis, the named project electrical specifications (`ELC-QAS-000001-001`, `ELC-QAS-000007-001`, `ELC-QAS-000003-001`), CSA C22.1-21, and the Gate 7 registers. Use `TBD` for anything not supported by the accessible source set.
- Do not invent installation sequences, lift plans, rigging studies, schedule, or quantities. These come from vendor data and detailed engineering and are properly carried as `TBD`.

## Considerations

The DBM electrical basis establishes the 6.9 kV service basis (three-phase, 60 Hz, low-resistance grounded) and the 100 A / 10 s neutral grounding resistor basis for each 6.9 kV transformer; the Construction Work Package should plan the grounding and protection tie-in against this basis. The DBM also lists "820-1 6.9kV Inlet / Sales Compressor Electrical Building" as a shop-fabricated electrical building and notes that electrical buildings are prefabricated modular structures with bottom-entry cabling on piles in general purpose areas. The CWP should reflect bottom-entry cabling and ground-grid bonding at two points, while leaving the specific PKG-021 building assignment as `TBD` because the accessible source set does not allocate PKG-021 to a specific structure.

The DBM Construction Responsibility section assigns field construction execution (off-loading, setting modules/equipment on foundations, mechanical hookup, electrical terminations, installation of home-run cables, installation of miscellaneous structural supports) to Tourmaline Oil Corporation. The CWP should describe this division of labor explicitly so that EPC Integrator coordination obligations and Tourmaline field-execution obligations are not conflated.

The DBM electrical studies table requires short-circuit, relay coordination/arc-flash, and load-flow studies to be completed prior to energization. The CWP should include these as gating conditions for energization rather than as construction-internal activities.

The package-specific Word requirements source did not produce a PKG-021 match during this run. Until that source slice (or a comparable PKG-021-specific construction document) is accessible, lineup quantity, ratings, equipment weights and dimensions, lift plans, rigging studies, installation sequencing, and schedule must remain `TBD`.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Lineup quantity / rating | Mark `TBD` pending package-specific source confirmation. | DBM Table 12-1 lists "Medium Voltage Switchgear, 1" but does not confirm PKG-021 allocation or rating. |
| Installation location | Identify Building 820-1 as DBM context, not a confirmed PKG-021 assignment. | DBM places 6.9 kV switchgear in the Inlet/Sales Compressor Electrical Building, but does not formally allocate PKG-021. |
| Sequencing / lift plans | Mark `TBD`; do not draft from convention. | Vendor equipment weights/dimensions and rigging study not in accessible source set. |
| Clause-level specification references | Cite specifications by document ID; mark clause locations `TBD`. | The project electrical/construction specifications are referenced by DBM Table 12-1 but the documents themselves are not in the accessible source set. |
| Tie-in scope for "Electrical Power" | Carry as connection from upstream 13.8 kV switchgear through step-down transformer to the 6.9 kV bus, per DBM Power System section. | DBM defines the radial distribution from 13.8 kV to 6.9 kV; package-specific feeder details remain TBD. |

## Examples

- Acceptable CWP entry: "All six `PKG-021` interfaces (`IFC-9D7DF96637`, `IFC-2ACD080082`, `IFC-B44478ADB6`, `IFC-FC8113A0CE`, `IFC-9E975838A2`, `IFC-A795E61D99`) shall be addressed in the tie-in workface plan and turnover checklist. Source: `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Equipment lift plan: TBD. No vendor lift drawing or rigging study in accessible source set."
- Not acceptable without new source: "PKG-021 comprises a four-section 6.9 kV switchgear lineup rated 1200 A located in Building 820-1." Each of these specifics requires a source slice not present in the current source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-021-03-001 | DBM places 6.9 kV switchgear inside the shop-fabricated "820-1 6.9kV Inlet / Sales Compressor Electrical Building," but Gate 7 registers do not formally allocate PKG-021 equipment to a specific building or skid. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Modular Buildings table; Electrical Buildings section | `PACKAGE_REGISTER.csv` row `PKG-021`; Workbook Packages row 23 | Datasheet Attributes; Datasheet Construction; Specification REQ-021-03-006; Procedure Steps | Treat the Building 820-1 placement as directional context; keep PKG-021 installation location `TBD` until vendor data or detailed engineering confirms it. | TBD |
| HRR-021-03-002 | DBM Table 12-1 records "Medium Voltage Switchgear, 1" without confirming whether this quantity applies to PKG-021 or to the broader 6.9 kV / 4.16 kV MV scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 | `PACKAGE_REGISTER.csv` row `PKG-021`; Workbook Packages row 23 | Datasheet Attributes; Specification REQ-021-03-008; Procedure Steps | Do not assign quantity to PKG-021 until confirmed; keep lineup configuration and ratings `TBD`. | TBD |
| HRR-021-03-003 | Field construction is assigned to Tourmaline Oil Corporation per the DBM Construction Responsibility section, but the EPC Integrator is the responsible party for this Construction Work Package per Gate 7 registers. The boundary between EPC integration deliverables and Tourmaline construction execution must be explicitly drawn. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section | `DELIVERABLE_REGISTER.csv` row `DEL-021-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-021` | Datasheet Identification; Specification REQ-021-03-002; Procedure Steps | EPC Integrator authors the CWP; Tourmaline executes per the CWP. Both responsibilities are recorded and not conflated. | TBD |
