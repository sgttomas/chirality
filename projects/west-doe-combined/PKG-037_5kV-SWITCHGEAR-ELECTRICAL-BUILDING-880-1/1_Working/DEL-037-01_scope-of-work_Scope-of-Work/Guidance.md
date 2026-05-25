# Guidance: DEL-037-01_scope-of-work — Scope of Work

## Purpose

This guidance supports drafting and review of the `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)` EPC scope of work. The deliverable exists to turn the accepted decomposition basis for `SOW-0038` into a bounded vendor-owned Electrical package scope with clear interfaces, source basis, responsibility assignment, and whole-facility integration narrative.

## Principles

- Preserve the Gate 7 package identity exactly: `PKG-037`, "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)", Electrical, WBS 01, CoA tracking number `26020-01-30-028` (`PACKAGE_REGISTER.csv`, `PKG-037`).
- Treat the workbook row 39 and Gate 7 registers as the authoritative decomposition truth for package membership, scope item, and deliverable identity.
- Treat SEC-12 Electrical Basis (Deepcut DBM) as the source for general electrical-building, codes, system-voltage, grounding, and cable-system requirements; treat it as silent on the 880-1 building and on a 5 kV medium-voltage service class.
- Use `TBD` for package-specific design values not present in accessible sources. Do not infer bus voltage, switchgear rating, breaker count, building location, dimensions, foundations, HVAC capacity, or tagged equipment from the package name alone.
- Preserve the vendor-owned package responsibility model: Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration. Do not collapse the split into a single responsible party.

## Considerations

The 880-1 building tag in the package name is not enumerated in the accessible Deepcut DBM building designations table, which lists 800-1, 810-1, 820-1, 830-1, 840-1, 850-1, and 860-1 only. The scope of work should therefore carry the 880-1 tag from the workbook and treat building location, area assignment, and adjacency as `TBD` instead of placing the building near any specific process module.

The "5kV switchgear" label in the package name is not directly enumerated in the SEC-12 system-voltages table, which lists 13.8 kV, 6.9 kV, and 4.160 kV medium-voltage services. The medium-voltage cable basis uses a 5 kV insulation rating for 4.160 kV cable, which is an industry-typical convention. The scope of work should carry "5kV switchgear" as the package title and record bus voltage class, rating, and feeder origin as `TBD` pending owner ruling or vendor confirmation; it should not silently assert a 4.16 kV bus.

Because the package is electrical-building scope, the integration narrative should foreground the twelve declared interfaces and the SEC-12 electrical-buildings basis: prefabricated/modular construction, general-purpose area location, n + 1 HVAC, bottom cable entry, elevated on piles, TECK/ACIC wiring, EMT for adjacent panels, outdoor GFI receptacle, and equipment-removal door provisions. Detailed equipment selection, layout, and panel schedules belong to `DEL-037-02_package-datasheet` and `DEL-037-04_vendor-engineered-equipment-package`, not to this scope-of-work deliverable.

## Trade-offs

| Topic | Guidance |
|---|---|
| Early scope completeness vs source fidelity | Include the required EPC scope-of-work structure now, but leave unsupported design values as `TBD` until vendor data, detailed design, or owner ruling is accepted. |
| 880-1 location | Do not assume a process-area or unit adjacency; carry location as `TBD`. |
| 5kV switchgear voltage class | Treat as `TBD` with an `ASSUMPTION` that 5 kV class metal-clad switchgear typically serves 4.16 kV systems; require human ruling before closing this. |
| Responsibility assignment | Keep the vendor/integrator split explicit; do not narrow either party's scope without a ruling or a clear source change. |
| Standards depth | Cite SEC-12 codes paragraph at the scope-of-work level; defer clause-level requirements to the package datasheet and vendor specifications. |

## Examples

- Acceptable wording: "The package includes Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports; Area / Exterior Lighting; Utility Piping; Drain / Containment; and Grading / Site Drainage / Spill Containment interfaces, per Gate 7 interface register."
- Acceptable wording: "Building location, dimensions, foundation design, and tagged equipment are TBD pending detailed design; the accessible building designations table does not enumerate the 880-1 building."
- Acceptable wording: "Bus voltage and switchgear rating are TBD; the package title carries 5 kV from the workbook and the SEC-12 system-voltages table does not list a 5 kV medium-voltage service."
- Avoid: "The 880-1 building shall be located adjacent to [specific area]" without a cited source slice.
- Avoid: "The switchgear shall be rated 4.16 kV, [breaker count], [bus rating] A" without a cited source slice or human ruling.
- Avoid: "The package is EPC supplied" because the source defines a Package Vendor / EPC Integrator split for PKG-037.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-037-01-001 | The package name carries the 880-1 building tag, but the accessible building designations table does not enumerate an 880-1 building. | Workbook Packages row 39 / `PACKAGE_REGISTER.csv` row `PKG-037` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building designations table | Datasheet Identification / Attributes / Construction; Specification Scope / REQ-037-01-10; Procedure Steps | Carry the 880-1 tag from the workbook as identity-only and keep building location, area, and adjacency `TBD` until detailed design or owner ruling closes it. | TBD |
| HRR-037-01-002 | The package name carries "5kV switchgear", but the accessible SEC-12 system-voltages table enumerates 13.8 kV, 6.9 kV, and 4.160 kV medium-voltage services only; "5 kV" appears as a cable insulation rating for 4.160 kV cable. | Workbook Packages row 39 / `PACKAGE_REGISTER.csv` row `PKG-037` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 system-voltages table and medium-voltage cable table | Datasheet Attributes / Construction; Specification REQ-037-01-11; Procedure Steps | Carry "5kV switchgear" from the workbook as identity-only; treat bus voltage class and rating as `TBD`; record an ASSUMPTION that 5 kV class metal-clad switchgear typically serves 4.16 kV systems; require human ruling before assigning a bus voltage. | TBD |
| HRR-037-01-003 | No package-specific exclusions are stated in source materials for PKG-037. | `PACKAGE_REGISTER.csv` row `PKG-037` ("TBD; no package-specific exclusions stated in source materials") | (no second source) | Specification Scope / REQ-037-01-12; Procedure Records | Carry package-specific exclusions as `TBD`; close out only when stated by a source or by ruling. | TBD |
