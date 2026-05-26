# Guidance — DEL-051-02 Package Datasheet (Process Heat Medium Unit)

## Purpose

The Package Datasheet is the mandatory EPC Integrator technical handoff artifact for the Process Heat Medium Unit. It collects the package data required for a third-party vendor or specialist discipline group to engineer and design the package. It also serves as the EPC anchor point that interface facts attach to as evidence, rather than spawning a proliferation of standalone interface deliverables. [`_CONTEXT.md` → Scope, Notes]

## Principles

- **Single anchor.** Carry the equipment list, design conditions, and interface declarations for PKG-051 in this datasheet so downstream consumers cite one authoritative source. [`_CONTEXT.md` → Notes]
- **Source fidelity.** All values originate from `26020-Package_Requirements.docx` (heading 6) and `26020-Packages_Interfaces_4_export.xlsx` (row ID# 51). Where the source text is silent or truncated, the datasheet records `TBD` rather than guessing.
- **Closed-loop integrity.** The system is a closed hot/cold-loop with mixing; design and operation choices must preserve loop integrity, fluid life, and expansion-tank fill discipline. [docx → Basic Scope]
- **Vendor-bounded detail.** Several quantities (expansion-tank size/capacity, vendor deliverables list, interface coordination notes, pump operating temperature) are deliberately left for vendor confirmation; the datasheet must remain stable when the vendor confirms.

## Considerations

- **Expansion-tank fill at high temperature.** The 85%-max fill limit at 274 °C bounds the cold charge volume and the working fluid inventory; this drives expansion-tank sizing once vendor heat-up profile and bulk volume are known. [docx → Major Included Equipment]
- **NPSHR-driven operating pressure.** The expansion tank operating pressure range (125–240 kPag) is set by the selected pump's NPSHR. Final pressure cannot be pinned until pump curves are committed. [docx]
- **3 × 66% pump configuration.** Implies one pump as installed spare; coordination with electrical, control, and maintenance interfaces matters for changeover philosophy. [docx + xlsx interfaces row]
- **Bulk temperature 260 °C.** Drives material selection, insulation, fluid degradation control, and relief sizing. The available source does not list materials of construction or insulation spec — recorded as TBD.
- **Fluid identity.** Source text reads "Petro Canada Peterotherm" — likely "Petro-Canada Petrotherm." This is recorded as ASSUMPTION on spelling and added to the Conflict Table.
- **Interface scope discipline.** The 10 interfaces marked applicable in the xlsx row are the canonical declared interface set. Adding or removing an interface requires updating the upstream xlsx and re-syncing this datasheet.

## Trade-offs

- **Carrying interfaces here vs. spinning standalone interface deliverables.** Carrying them here keeps the EPC handoff coherent and reduces deliverable count, at the cost of making this document the bottleneck for interface change traffic. The decomposition explicitly accepts this trade-off. [`_CONTEXT.md` → Notes]
- **Vendor-advised parameters vs. EPC-fixed parameters.** Leaving expansion-tank size and pump operating temperature to vendor preserves design flexibility but requires disciplined TBD tracking and vendor-data-in review.
- **Hot/cold-loop mixing vs. single-loop control.** Mixing gives optimum supply temperature to varied users (per docx) at the cost of additional valves, controls, and tuning complexity.

## Examples

- The xlsx interface row provides the canonical example of how an interface declaration looks for this package: marked "X" entries become required EPC coordination items; blank entries are out of scope unless a future revision marks them. [xlsx row ID# 51]
- The docx Basic Scope text is the canonical example of process-function framing: closed loop, hot/cold loops, mixing, multi-user heat supply. [docx → Basic Scope]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Heat-medium fluid name spelling — docx reads "Peterotherm"; widely known Petro-Canada brand is "Petrotherm". | `26020-Package_Requirements.docx` → Major Included Equipment | Vendor (Petro-Canada) product naming convention (not in local source set) | Datasheet → Construction; Specification → REQ-051-02-14 | Treat as "Petrotherm" with ASSUMPTION label until vendor datasheet confirms. | TBD |
| CONF-02 | Pump operating temperature is truncated in docx ("Operating pressure 695 Kpag (100 Psig) and temp."). | docx → Major Included Equipment | None available locally | Datasheet → Conditions; Specification → REQ-051-02-11 | Mark TBD; resolve from a complete copy of the source or vendor pump datasheet. | TBD |
| CONF-03 | Vendor Engineering Deliverables and Interface Coordination Notes sections are empty / "TBD." in docx. | docx → Vendor Engineering Deliverables; Interface Coordination Notes | None | Datasheet → Vendor Engineering Deliverables / Interface Coordination Notes; Specification → REQ-051-02-16, -17 | Hold as TBD; populate from vendor scope-of-supply and interface coordination meetings. | TBD |
| CONF-04 | Decomposition notes objective associations (OBJ-001, -004 to -010) by package-grouping heuristic; deliverable-level mapping not confirmed. | `_CONTEXT.md` → Supports Objectives | `_Decomposition/.../OBJECTIVE_DELIVERABLE_MAP.csv` (not read in this pass) | Guidance → Purpose; cross-cutting | Treat objectives as ASSUMPTION (best-effort mapping) per PACKAGE_HEURISTIC. | TBD |
