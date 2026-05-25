# Guidance: Construction Work Package

## Purpose

The Construction Work Package turns the accepted `PKG-019` MV VFD package basis into construction-facing instructions, checks, and turnover evidence. Its purpose is to show how the vendor-supplied 4160V VFD that starts the inlet compressor motors (KM-2150 / KM-2250) will be physically installed, built, inspected, turned over, and tied into the facility electrical, grounding, controls, communications, structural, and maintenance-access systems.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-019-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-019`; `INTERFACE_REGISTER.csv` rows for `PKG-019`.

## Principles

- Keep package identity and source basis visible. The construction package should carry `PKG-019`, workbook row 21, WBS 02, CoA tracking number `26020-02-30-009`, Electrical discipline, and source references forward into the workface plan.
- Treat the Gate 7 registers as accepted decomposition truth for package identity, deliverable intent, artifacts, objectives, and interface labels.
- Treat DBM source slices as authority for facility-level electrical, MV starting-VFD basis, harmonic/reactive constraints, control/communication architecture, geotechnical, environmental, and standards constraints.
- Preserve the vendor-vs-EPC responsibility split. Package engineering, design, vendor documentation, and equipment are Package Vendor scope; facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination are EPC Integrator scope.
- Preserve uncertainty. VFD detailed ratings, harmonic/reactive mitigation, final geotechnical parameters, detailed electrical specifications, protection/coordination studies, and arc-flash inputs should remain `TBD` until accepted source material closes them.

## Considerations

The most important package-specific construction controls are the six declared interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. The DBM specifies that the 4160V MCC is fed from the 13.8 kV to 4.16 kV, 12 MVA transformer and serves the 4000V driven motors; the MCC provides field-fused contactors, motor protection relays, and an EtherNet port to the plant PLC central control panel. MV breaker control and MV protective relay are UPS-served (120 VAC / 125 VDC). These facts shape Electrical Power, I&C / Control Cabling, and Communications / Network tie-in detail and signoffs.

SCA-001 VE #34 fixes the starting-VFD basis (no soft starts) for KM-2150 and KM-2250; SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present, deferring harmonic and reactive-power mitigation to detailed electrical studies. The CWP should carry a clear verification hold for these studies rather than closing harmonic/reactive criteria from currently-available sources.

Construction planning should account for the broader 03-25 construction scope, including module setting, mechanical hookups, cabling, terminations, area lighting, fencing, security, and tie-in works. Only the portions that affect the MV VFD package or its declared interfaces should be carried into this deliverable as requirements.

Geotechnical data and detailed electrical specifications are not fully closed. The DBM requires the final geotechnical report before foundation design closure; foundation, anchorage, and structural support criteria for the VFD enclosure/skid should remain readiness-gated until that report and vendor equipment loads are accepted.

The -40 deg C minimum ambient basis governs exposed equipment, control panels, instrumentation, and field devices. Cold-weather installation, handling, and commissioning provisions for the VFD enclosure and its auxiliaries should be explicitly verified before energization.

Standards and regulatory references are not fully available in the current source set. The CWP should carry verification requirements for project electrical specifications, protection/coordination studies, harmonic studies, and arc-flash studies rather than claiming final compliance from unavailable citations.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Early CWP planning vs. vendor design certainty | Early CWP drafting helps define workface controls, but vendor VFD ratings, footprint, weight, cooling, and termination details may evolve. | Use `TBD` readiness gates and re-align with the vendor engineered equipment package before IFC release. |
| Harmonic/reactive mitigation vs. construction schedule | Detailed harmonic studies may not be complete when civil/structural work begins. | Keep harmonic-mitigation provisions (filter footprint, cabling allowances) as a verification hold; do not pour or close studies prematurely. |
| Package-local focus vs. facility integration | The MV VFD is a vendor package, but its function depends on the 4160V MCC, the driven motor, plant PLC EtherNet, and UPS-served MV control. | Keep interface signoffs explicit and avoid isolated workface closure. |
| Source-limited standards vs. construction readiness | The DBM references standards and regulatory content that are not fully available. | Require verification of current project specifications, electrical studies, and regulatory permits before IFC/field release. |
| EPC vs. Vendor scope at the boundary | Some construction-adjacent tasks (factory-fitted accessories, vendor commissioning) belong to the vendor. | Document the EPC/Vendor boundary at each interface in the checklist and turnover record. |

## Examples

TBD - no source-provided MV VFD installation example, vendor equipment data, or completed turnover checklist is available in the current deliverable source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-019-03-001 | The package title is "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" but the DBM describes the inlet compressor motor basis as 4,000 V, ~3,878 kW / 5,200 hp with a starting VFD; ratings between the package title and the source motor basis differ in nominal voltage (4160V vs 4000V) and horsepower (5000HP vs 5200hp). | `PACKAGE_REGISTER.csv` row `PKG-019`; `DELIVERABLE_REGISTER.csv` row `DEL-019-03_construction-work-package` | `3-25_Comp_and_Liquids_DBM.md` lines 324, 533 | `Datasheet.md` Identification/Attributes; `Specification.md` Scope, Requirements; `Procedure.md` Steps | Treat the package title as the package identity of record; carry exact VFD/motor ratings, voltages, and hp as `TBD` until vendor data and accepted electrical specifications resolve the 4160V/4000V and 5000HP/5200hp difference. | TBD |
| HRR-019-03-002 | Detailed VFD characteristics (topology, cooling, enclosure type, harmonic filter, output filter, bypass arrangement, input transformer, harmonic/reactive-mitigation values) are not present in accessible source slices. | `PACKAGE_REGISTER.csv` row `PKG-019`; `_REFERENCES.md` Missing/Deferred References | Missing vendor data and detailed electrical studies | `Datasheet.md` Construction; `Specification.md` Requirements, Standards, Verification; `Procedure.md` Steps, Verification | Carry detailed VFD characteristics and mitigation values as `TBD` until vendor engineered equipment package (`DEL-019-04`) and detailed electrical studies are accepted. | TBD |
| HRR-019-03-003 | Responsibility for the deliverable is EPC Integrator, but the package responsibility model splits package engineering/design/equipment to the Package Vendor and facility integration to the EPC Integrator. | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row `DEL-019-03` | `PACKAGE_REGISTER.csv` row `PKG-019` ResponsibilityModel | `Specification.md` Scope; `Procedure.md` Prerequisites, Steps | Treat EPC Integrator as deliverable owner; require human/project assignment for the EPC/Vendor construction-task split (field commissioning, factory-fitted accessories, witness points) before work release. | TBD |
