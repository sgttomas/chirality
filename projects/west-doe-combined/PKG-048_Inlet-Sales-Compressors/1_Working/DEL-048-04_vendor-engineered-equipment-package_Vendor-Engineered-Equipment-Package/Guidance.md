# Guidance: DEL-048-04 — Vendor Engineered Equipment Package

> Directional guidance for the Inlet / Sales Compressors vendor-engineered equipment package. Rationale is drawn from the Gate-07 PROJECT_DECOMP snapshot and the package context; clause-level rationale from `26020-Package_Requirements.docx` and the RFQ is TBD pending source-slice extraction.

## Purpose

This deliverable exists to anchor the Package Vendor's engineering, design, fabrication, and supply of the physical inlet/sales compressor package developed from the EPC package Scope of Work (DEL-048-01) and Package Datasheet (DEL-048-02). It carries the engineered package itself into a state that can be turned over (DEL-048-05) and reviewed/accepted by the EPC Integrator (DEL-048-06). [`_CONTEXT.md`; PACKAGE_REGISTER PKG-048]

## Principles

- **Vendor owns the package; EPC Integrator owns facility integration.** The Package Vendor is responsible for package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator is responsible for integrating the package into the process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Maintain this boundary in all engineered outputs. [PACKAGE_REGISTER PKG-048]
- **Package Datasheet and SOW are upstream truth.** The vendor-engineered package must be developed *from* the EPC package Scope of Work and the Package Datasheet (sibling deliverables DEL-048-01 and DEL-048-02). Do not introduce package-level requirements that have not flowed through those deliverables. [`_CONTEXT.md` (Scope); ASSUMPTION on declared upstream — `_DEPENDENCIES.md` lists none, but the role description names SOW + Datasheet as the basis.]
- **Sized for 120%.** Each compressor shall be sized for 120%; treat this as the binding sizing margin for capacity-related design decisions. [SOW-0116]
- **No turndown.** The design need not accommodate turndown; do not over-engineer for low-flow operability. [SOW-0118]
- **Interface set is a design constraint, not a wish-list.** The PKG-048 applicable interface types (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports) must each be addressed in the vendor design. [PACKAGE_REGISTER PKG-048]

## Considerations

- **Two services on one package.** Inlet (single-stage) and sales (double-stage) share a common air cooler frame with bundle-level pneumatic temperature control. Coordinate cooler bundle sizing and louver-control logic so that one service is not penalized by the other. [SOW-0117]
- **Driver rating ambiguity.** Two driver ratings appear in the source extracts: 5,000 kW (6,700 HP) basic and 5,220 kW (7,000 HP) at design (each with "~10% excess at design"). See Conflict Table. The vendor should treat 5,220 kW (7,000 HP) as the bounding design rating unless directed otherwise.
- **Motor preference is directional.** "Preferred WEG motor, KBZ Frame, 6,700 hp" expresses a preference, not a hard exclusion; equivalent compliant alternatives should be evaluated against the explicit electrical and mechanical requirements. [SOW-0118; ASSUMPTION on "preferred" interpretation]
- **By-others items must be designed for.** Shipping fit-up, pile mounting, tie-in piping, electrical terminations, and external platforms/stairs are out of vendor scope but in scope to design for (interfaces and structural connection points). [SOW-0118]
- **Source-slice gaps.** Materials of construction, area classification, process gas composition, ambient/site design conditions, and noise/vibration limits are not present in the decomposition extract and must be resolved from `26020-Package_Requirements.docx` and the RFQ before final engineering. [TBD]

## Trade-offs

- **Common air cooler vs. dedicated coolers.** Source mandates one common air cooler frame per package (SOW-0117). This trades capital savings and footprint for control-coupling complexity between services; bundle-level pneumatic control mitigates but does not eliminate this.
- **TEFC vs. WPII enclosure.** Either is permitted (SOW-0118). TEFC favors dirty/exposed environments; WPII favors larger machines with adequate ventilation. Vendor selects based on site/area assumptions (TBD).
- **Compliance via NEMA MG 1 only.** SOW-0118 cites NEMA MG 1; whether IEC equivalents are also acceptable is not stated. [TBD]

## Examples

> No worked examples are present in the available source extracts. Worked examples are intentionally omitted to avoid invention.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-001 | Per-unit driver rating: 5,000 kW (6,700 HP) "basic scope" vs 5,220 kW (7,000 HP) "design conditions". Both qualified with "includes ~10% excess at design". | SCOPE_LEDGER SOW-0117 (Major included equipment) | SCOPE_LEDGER SOW-0118 (Scope notes and open items) | Datasheet Attributes (Driver rating); Specification REQ-2 | PROPOSAL: treat 5,220 kW (7,000 HP) as the bounding design rating per SOW-0118; treat 5,000 kW (6,700 HP) as nominal basic-scope figure per SOW-0117. Both retained pending source-slice review of `26020-Package_Requirements.docx`. | TBD |
| CONF-002 | Declared upstream dependencies on DEL-048-01 (SOW) and DEL-048-02 (Package Datasheet) implied by role description ("developed from the EPC package Scope of Work and Package Datasheet") but `_DEPENDENCIES.md` declares none. | `_CONTEXT.md` Scope; PACKAGE_REGISTER PKG-048 | `_DEPENDENCIES.md` (Declared Upstream: None) | `_DEPENDENCIES.md` | PROPOSAL: declare DEL-048-01 and DEL-048-02 as upstream dependencies via `TASK + dependency-extract`. Do not edit `_DEPENDENCIES.md` from this skill. | TBD |
