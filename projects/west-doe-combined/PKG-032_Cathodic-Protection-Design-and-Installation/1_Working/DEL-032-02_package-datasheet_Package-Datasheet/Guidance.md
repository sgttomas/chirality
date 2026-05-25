# Guidance: DEL-032-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-032` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the Cathodic Protection Design and Installation package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "Cathodic Protection Design and Installation" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned CP design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for CP system type, protected-asset list, rectifier rating, anode count, test-station scheme, monitoring/control signal counts, and installation locations until a source-supported package-specific basis is available.
- Do not silently reconcile the two DBM positions on CP scope. Surface the difference and route it for human ruling.

## Considerations

The Deepcut DBM (4-25) explicitly excludes cathodic protection engineering and supply from the facility design scope and assigns CP engineering/supply to the owner, with the facility design responsible only for supporting owner CP interfaces. The Comp & Liquids DBM (3-25) identifies cathodic protection as part of the electrical design scope. These two positions are not the same.

Because `PKG-032` is a workbook-defined vendor-owned Electrical package under WBS 03 with CoA 26020-03-30-023, the workbook treats CP as an engineered package regardless of the DBM scope-position language. The package's vendor-owned posture is consistent with either DBM position: in the Deepcut frame the vendor would be the owner-engaged CP supplier; in the Comp & Liquids frame the vendor would deliver CP as part of the facility electrical scope.

CP bonding must be coordinated with the facility grounding basis to avoid stray-current and ground-loop conflicts. The DBM electrical sections support facility grounding/bonding requirements in general but do not specify CP-grounding coordination details for this package.

The I&C / Control Cabling and Communications / Network interfaces support remote monitoring of rectifiers, reference cells, and test stations. Detailed signal counts, protocols, addressing, and rack/cabinet assignments are TBD until vendor data is available.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Facility-scope position (owner vs. EPC) | Carry both DBM positions and route to human ruling. | The Deepcut and Comp & Liquids DBMs disagree on whether CP engineering/supply is in facility scope. |
| CP system type | Mark `TBD` pending vendor data and confirmed protected-asset list. | No accessible source slice specifies impressed-current vs. sacrificial-anode for this package. |
| Protected-asset list | Mark `TBD`; do not enumerate from inference. | No accessible source slice enumerates buried piping, tanks, or structures included in this package. |
| Standards | List CEC, project electrical specifications, and industry CP standards (NACE/AMPP) as governing bases with locations TBD; mark industry CP standards as ASSUMPTION. | DBM references CEC and project electrical bases; CP industry standards are reasonable assumption but are not cited in the accessible source slices. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network. Source: Workbook Packages row 34 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Rectifier rating: TBD. No package-specific source slice available."
- Acceptable scope-position entry: "Deepcut DBM excludes CP engineering/supply from facility design (owner interface). Comp & Liquids DBM includes CP in electrical design scope. Routed to human ruling."
- Not acceptable without new source: "CP system is impressed-current with N rectifiers protecting M km of buried piping." The accessible source set does not establish this.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-032-02-001 | The two facility DBMs take opposite positions on CP scope: Deepcut excludes CP engineering and supply from facility design (owner interface only); Comp & Liquids includes CP in the electrical design scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Cathodic Protection" section and SEC-12 assumptions table row "Cathodic protection" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical scope paragraph ("Lighting, receptacles, electric heat tracing, building heaters, and cathodic protection are part of the electrical design scope.") | Datasheet Attributes/Conditions; Specification Scope/Requirements; Procedure Steps | Carry both positions in the Datasheet and Guidance; route to human ruling to confirm which DBM governs `PKG-032` and whether the package is owner-engaged or fully in facility electrical scope. | TBD |
| HRR-032-02-002 | No accessible package-specific source slice defines CP system type, protected-asset list, rectifier rating, anode count, or test-station scheme for `PKG-032`. | `_REFERENCES.md`; `_Sources/26020-Package_Requirements.docx` (no PKG-032-specific match accessible in this run) | Workbook Packages row 34 (existence and interfaces only) | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Keep all CP-specific technical parameters `TBD` until vendor data or a package-specific source slice is accepted. | TBD |
