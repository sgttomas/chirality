# Guidance: DEL-016-03 — Construction Work Package (Transformer TXP-8200-1)

## Purpose

This Guidance document supports authors and reviewers of the PKG-016 Construction Work Package (CWP) — the EPC Integrator deliverable defining how the 3 MVA, 13.8 kV / 600 V step-down distribution transformer TXP-8200-1 is physically installed, terminated, tied in, inspected, and turned over to commissioning. It explains the rationale behind the Specification requirements and surfaces interpretive considerations that arise because much of the detailed design information is intentionally left for later phases in the accepted DBM.

## Principles

1. **EPC integration ownership.** PKG-016 is a vendor-owned package; the EPC Integrator owns facility-level integration: foundations, raceways, primary/secondary cabling tie-ins, grounding tie-in, area-classification compliance, and turnover. Vendor scope (transformer design, FAT) is explicitly excluded from this CWP.
2. **Source-bounded definition.** The DBM defines what is known (rating, voltages, source feeder, secondary MCC, ambient envelope, hazardous-area basis); it does not yet define detailed cable sizes, raceway routing, exact foundation dimensions, or the final electrical/construction specifications. CWP authors must respect that boundary and not promote ASSUMPTIONs to requirements.
3. **Coordination over invention.** The CWP should reference rather than restate adjacent EPC and vendor deliverables: `DEL-016-01` (SOW), `DEL-016-02` (Package Datasheet), `DEL-016-04` (Vendor Engineered Package), `DEL-016-05` (Vendor Document Turnover), `DEL-016-06` (EPC Vendor Acceptance), plus 04-25-side switchgear and the 600 V MCC scope.
4. **Tie-in discipline.** The DBM construction-scope summary lists module setting, mechanical hookups, home-run cabling, terminations, and demolition for tie-ins as construction-scope items. Each interface should appear in the tie-in register with a defined ownership boundary.
5. **Safety and hazardous-area discipline.** All field work near classified areas must be tracked against the current area-classification drawings; the DBM's Class I Zone 2 IIA/IIB general basis is not a substitute.

## Considerations

- **Indoor vs outdoor installation.** The DBM indicates that electrical buildings house MCCs, switchgear, and distribution equipment. Confirm the transformer's final location early — indoor installation drives building HVAC/heat-load coordination; outdoor (pad-mount) installation drives weatherization, fencing, and winterization.
- **600 V secondary grounding.** The facility 600 V system is HRG with a 5 A continuous resistor. The transformer secondary winding configuration and the location of the neutral grounding resistor must be confirmed with the vendor and integrated into the construction grounding scope.
- **347 V utilization.** The package title implies a Wye 600 V secondary (347 V line-to-neutral). The DBM tables only call out a 600 V, 3-phase, 3-wire HRG service, which is inconsistent with a true 4-wire 347 V utilization. See Conflict Table below.
- **Final geotechnical report.** Foundation design depends on the final geotechnical report (per DBM SEC-11). CWP execution sequencing must allow that input.
- **Cable separation.** The DBM mandates physical separation of 13.8 kV / 4.16 kV / 600 V power circuits from control/instrument circuits. Plan raceway and tray runs accordingly.
- **Detailed-design dependence.** Where detailed electrical and construction specifications are not yet accessible, CWP authors should reference the spec by document number with a `location TBD` marker rather than invent clause-level rules.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Detail now vs detail at IFC | Adding construction detail before detailed design closes risks rework. The CWP should specify *requirements and acceptance points*; the workface plan can mature later. |
| Vendor sequencing vs site readiness | Receipt and setting timing depend on vendor manufacturing schedule and foundation completion. Coordinate via the construction schedule and module-set plan. |
| Indoor vs outdoor siting | Indoor reduces weather exposure but increases building load and ventilation duty; outdoor reduces building footprint but increases winterization and security needs. |

## Examples

- Example tie-in entries for this transformer:
  - Primary 13.8 kV feeder from 04-25 Main Switchgear (cross-facility cable corridor).
  - Secondary 600 V feeder to MCC-8200 (LV MCC lineup).
  - Ground grid bonding to facility ground grid.
  - Building services (if indoor): HVAC duct/coordination, area lighting, heat tracing.

(Examples above are illustrative based on DBM SEC-12; specific cable IDs, lengths, and tray IDs are TBD pending detailed design.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| HRR-016-03-001 | Package title states "600/347 V" (implies a 4-wire Wye 600 V secondary). DBM SEC-12 "System Voltages" defines 600 V as 3-phase, 3-wire HRG with 5 A continuous resistor (incompatible with a continuously loaded 347 V line-to-neutral utilization). | Package title (`PACKAGE_REGISTER.csv` row 18; folder name) | DBM SEC-12 System Voltages and Incoming Power and Transformers | Datasheet (secondary voltage), Specification (R-CWP-05) | Treat 600 V, 3-phase, 3-wire HRG as authoritative for utilization; treat "347 V" in the package name as title-only identity unless vendor confirms a Wye-with-grounded-neutral utilization. | TBD |
| HRR-016-03-002 | Construction execution depends on detailed electrical and construction specifications that are not locally accessible. | Project Electrical/Construction Specifications (cited but not present) | DBM SEC-12 / SEC-15 | Specification Standards table; many `location TBD` markers in R-CWP-* | Defer clause-level acceptance criteria to detailed-design issue; keep CWP at requirement-plus-verification-hook level until specs are accepted. | TBD |
| HRR-016-03-003 | Indoor vs outdoor installation location of TXP-8200-1 is not explicitly stated in the DBM. | DBM SEC-12 "Electrical Buildings, Raceways…" | (absence of explicit location) | Datasheet "indoor/outdoor"; Specification R-CWP-01; CWP foundation, weatherization, and building-services scope | Confirm installation location during detailed design; CWP authors should not assume either without confirmation. | TBD |
