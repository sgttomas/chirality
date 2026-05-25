# Guidance: Construction Work Package

## Purpose

The Construction Work Package turns the accepted `PKG-020` 13.8 kV switchgear package basis into construction-facing instructions, checks, and turnover evidence. Its purpose is to show how the vendor-supplied 13.8 kV switchgear lineup - the plant main power distribution center for the 04-25 West Doe Deepcut expansion - will be physically installed, built, inspected, turned over, and tied into the facility electrical, grounding, controls, communications, structural, and maintenance-access systems.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-020-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-020`; `INTERFACE_REGISTER.csv` rows for `PKG-020`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System, Grounding and Bonding, Electrical Buildings, and Cable Specifications sections.

## Principles

- Keep package identity and source basis visible. The construction package should carry `PKG-020`, workbook row 22, WBS 01, CoA tracking number `26020-01-30-011`, Electrical discipline, and source references forward into the workface plan.
- Treat the Gate 7 registers as accepted decomposition truth for package identity, deliverable intent, artifacts, objectives, and interface labels.
- Treat DBM source slices (Power System, Grounding and Bonding, Electrical Buildings, Cable Specifications) as authority for facility-level electrical basis, utility-side feed, radial distribution, grounding architecture, MV cable basis, and standby-power scope decisions.
- Preserve the vendor-vs-EPC responsibility split. Package engineering, design, vendor documentation, and equipment are Package Vendor scope; facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination are EPC Integrator scope.
- Preserve uncertainty. Switchgear detailed ratings (bus continuous, short-circuit interrupting/withstand, BIL, breaker type, arc-resistant rating), lineup count, foundation/structural detailing, utility metering/protection split, protection coordination and arc-flash inputs should remain `TBD` until accepted source material closes them.

## Considerations

The most important package-specific construction controls are the six declared interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.

The DBM Power System section establishes the 13.8 kV switchgear as the plant main power distribution center: fed from a 25/13.8 kV, 50 MVA utility-supplied transformer (utility voltage 25 kV TBC) and radially distributing through downstream step-down transformers to the 6.9 kV, 4.16 kV, and 600 V electrical buildings. The 13.8 kV bus is to be sized for the full facility scope. This is the dominant Electrical Power interface fact for the CWP. The switchgear is identified in the source equipment list as part of Electrical Building 810-1 ("13.8kV Switchgear Electrical Building"), shop-fabricated.

Grounding architecture is concrete in the source: the utility transformer has a 200 A, 10 s neutral grounding resistor (tripping system); the plant ground grid uses driven piles interconnected by a #2/0 green insulated main grounding conductor in the highest-voltage carrying tray; major electrical equipment is connected to the grid at two points. The CWP must carry these as installed/witnessed acceptance items.

MV control and protection are UPS-served (120 VAC / 125 VDC). This shapes I&C tie-in detail: routing, labeling, and verification of MV breaker control and protective relay circuits must align with the UPS distribution served by the dedicated UPS packages (e.g., `PKG-013` 100A DC UPS and equivalent AC UPS).

The MV cable basis is fixed in the source for the 13.8 kV class: three-conductor copper TECK, 15 kV, 133% insulation, shielded. CWP termination, test, and acceptance criteria should reference this basis.

A material scope decision in the source is that the previously-contemplated centralized 13.8 kV emergency generator is eliminated; standby power is at the 600 V MCC level. The CWP should not carry a 13.8 kV emergency-generator tie-in scope; this is a common point of confusion if older facility narratives are reused.

Construction responsibility is assigned to Tourmaline Oil Corporation: construction management, foundations, module setting, mechanical hookups, cable installation, electrical terminations, area lighting, fencing, and tie-in works fall within Tourmaline field construction scope. EPC Integrator owns facility integration and interface management.

Geotechnical and detailed electrical specifications are not fully closed in the accessible source set; foundation, anchorage, frost, settlement, and structural-support criteria for switchgear lineups and Electrical Building 810-1 should remain readiness-gated until vendor equipment loads and geotechnical inputs are accepted. Likewise, protection coordination, arc-flash, and standby-power scope split must remain verification holds until detailed electrical studies are accepted.

Cold-weather provisions matter for a Northern BC site; the -40 deg C minimum ambient basis governs exposed equipment, control panels, instrumentation, and field devices. Switchgear enclosure heating, anti-condensation provisions, and commissioning sequencing should be explicitly verified before energization.

Standards and regulatory references not present in the workspace should be carried as verification requirements (CEC, project electrical specifications, utility coordination agreements), not asserted as closed.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Early CWP planning vs. vendor design certainty | Early CWP drafting helps define workface controls, but vendor switchgear ratings, lineup count, footprint, weight, breaker selection, and termination details may evolve. | Use `TBD` readiness gates and re-align with the vendor engineered equipment package (`DEL-020-04`) before IFC release. |
| Utility coordination vs. construction schedule | Utility voltage is 25 kV (TBC) and the BC Hydro interface scope split is not closed in the accessible source. | Carry utility metering/protection/isolation as a `TBD` readiness gate; do not close utility-tie scope from currently-available sources alone. |
| Protection / arc-flash studies vs. construction schedule | Detailed protection-coordination and arc-flash studies may not be complete when field installation begins. | Keep protection settings, arc-flash boundaries, and acceptance criteria as a verification hold; do not energize without accepted studies. |
| Package-local focus vs. facility integration | The 13.8 kV switchgear is a vendor package, but its function depends on the utility-side transformer, all downstream step-down transformers and electrical buildings, the plant ground grid, plant control, and UPS-served MV control. | Keep interface signoffs explicit and avoid isolated workface closure. |
| Source-limited standards vs. construction readiness | The DBM references standards and regulatory content that are not fully available. | Require verification of current project specifications, electrical studies, utility agreements, and regulatory permits before IFC/field release. |
| EPC vs. Vendor scope at the boundary | Some construction-adjacent tasks (factory-fitted accessories, vendor commissioning, energization witness) belong to the vendor; Tourmaline owns most field construction. | Document the EPC/Vendor and Tourmaline-field-construction boundary at each interface in the checklist and turnover record. |
| Reuse of older facility narratives | Older narratives may include a centralized 13.8 kV emergency generator. | The current basis removes that scope; CWP shall not include a 13.8 kV emergency-generator tie-in. |

## Examples

TBD - no source-provided 13.8 kV switchgear installation example, vendor equipment data, or completed turnover checklist is available in the current deliverable source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-020-03-001 | Utility supply voltage is stated as 25 kV but marked "TBC". Utility interface scope (metering, protection, isolation, telemetry) is not closed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System (line 2917) | No utility coordination agreement in the accessible source set | `Datasheet.md` Attributes; `Specification.md` Scope / CWP-REQ-004 / CWP-REQ-011; `Procedure.md` Steps | Carry utility voltage as 25 kV (TBC); treat utility interface scope split as a `TBD` readiness gate until utility coordination is accepted. | TBD |
| HRR-020-03-002 | Detailed switchgear characteristics (bus continuous rating, short-circuit interrupting/withstand, BIL, lineup count, breaker count, breaker type, arc-resistant rating, accessories) are not present in accessible source slices. | `PACKAGE_REGISTER.csv` row `PKG-020`; `_REFERENCES.md` Missing/Deferred References | Missing vendor data and detailed electrical studies | `Datasheet.md` Construction; `Specification.md` Requirements, Standards, Verification; `Procedure.md` Steps, Verification | Carry detailed switchgear characteristics as `TBD` until the vendor engineered equipment package (`DEL-020-04`) and detailed electrical studies are accepted. | TBD |
| HRR-020-03-003 | Responsibility for the deliverable is EPC Integrator, but the package responsibility model splits package engineering/design/equipment to the Package Vendor and facility integration to the EPC Integrator, while field construction is assigned to Tourmaline Oil Corporation. | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row `DEL-020-03` | `PACKAGE_REGISTER.csv` row `PKG-020` ResponsibilityModel; `4-25_Deepcut_DBM.md` Construction Responsibility (lines 101-127) | `Specification.md` Scope; `Procedure.md` Prerequisites, Steps | Treat EPC Integrator as deliverable owner, Tourmaline as field construction executor, and Package Vendor as package supplier; require project assignment of the EPC/Vendor/Tourmaline task split (field commissioning, factory-fitted accessories, witness points) before work release. | TBD |
| HRR-020-03-004 | Equipment list shows "Medium Voltage Switchgear" qty 1 (`ELC-QAS-000007-001`) and a "13.8kV Switchgear Electrical Building" (Building 810-1). The exact allocation of that lineup count and building to PKG-020 is not formally confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2811, 2880 | No formal PKG-020-specific equipment list in accessible sources | `Datasheet.md` Attributes (Equipment quantity, Building / location); `Procedure.md` Steps | Treat the 1 MV switchgear lineup and Electrical Building 810-1 allocation as ASSUMPTION until the vendor engineered equipment package and IFC equipment list confirm. | TBD |
| HRR-020-03-005 | The DBM removes the centralized 13.8 kV emergency-generator concept, but legacy facility narratives may still imply such a tie-in. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2080, 2943 | Legacy narratives / older project docs (not in this source set) | `Specification.md` Exclusions / CWP-REQ-016; `Procedure.md` Steps | Treat the current DBM as authoritative: no 13.8 kV emergency-generator tie-in is in CWP scope. Surface for human ruling if a downstream consumer asks for that scope. | TBD |
