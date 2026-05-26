# Specification — DEL-077-02 Package Datasheet (PKG-077 Methanol Injection)

> Normative document. Requirements derived from accessible sources; inferred items labeled `ASSUMPTION`; missing items marked `TBD`.

## Scope

This specification governs the **EPC Package Datasheet** for the PKG-077 Methanol Injection package at the 4-25 Deepcut facility. It specifies what the EPC Integrator's package datasheet shall contain so that a third-party (vendor or discipline) can perform package engineering and design.

**Includes:**
- Required content of the Package Datasheet artifact for PKG-077.
- Package interface requirements matrix carried as evidence within this datasheet (per `_CONTEXT.md` Notes: "interface facts are intentionally carried here as evidence rather than standalone deliverables").
- Equipment identification, design conditions, and injection-point inventory.

**Excludes:**
- Vendor-internal package engineering and design (Package Vendor scope under DEL-077-04).
- Construction work package contents (DEL-077-03).
- Procurement, contracting, and commercial terms.
- Detailed P&IDs, layout drawings, or stress/thermal calculations (referenced; not produced here).

## Requirements

### R-1 Identification (mandatory)
The Package Datasheet shall identify the package by `PackageID = PKG-077`, `Name = Methanol Injection`, `Discipline = Mechanical`, `WBS = 01`, and the source workbook reference `Workbook Packages row 72`. Source: PACKAGE_REGISTER.csv (PKG-077).

### R-2 Function statement (mandatory)
The Package Datasheet shall state the package function as **temporary/transient hydrate suppression** via methanol injection. The datasheet shall explicitly note that the facility provides **no continuous hydrate suppression in raw inlet gas piping**. Source: DBM-Deepcut L428.

### R-3 Injection-point inventory (mandatory)
The Package Datasheet shall list every methanol injection point in the facility, including at minimum: BAHX pass inlet headers (each pass) upstream of strainers; J-T valve inlet; inlet separators upstream of PCV; inlet separators upstream of HCL and water dump valves; acid gas compressor package; MPFF feed-system injection for transient operation. Source: DBM-Deepcut L1328, L630, L674.

### R-4 Operating-mode requirement
The package shall be designed and operated to inject into **one point at a time**. Source: DBM-Deepcut L1328.

### R-5 Equipment list with tags (mandatory)
The Package Datasheet shall list package equipment with tag numbers, descriptions, and quantities. Minimum content: `TK-6395-1 METHANOL STORAGE TANK (Qty 1)` and `P-6396-1 METHANOL PUMP (Qty 1)`. Source: DBM-Deepcut L2605, L2606, L2379.

### R-6 Storage and pump basis
- Methanol storage shall be specified as an **atmospheric double-walled tank** located adjacent to the expander building. Source: DBM-Deepcut L1329.
- The injection pump shall be specified as a **triplex reciprocating** pump. Source: DBM-Deepcut L1329.
- Design specific gravity of methanol in the tank: **1.00 (pure methanol)** — recorded as **TBC** in source; the datasheet shall carry the same TBC qualifier until confirmed. Source: DBM-Deepcut L1329, L1392.

### R-7 Capacities and rates (TBD carry-through)
The Package Datasheet shall record per-point methanol injection capacities and overall injection rates. Where source values are TBC/TBD (e.g., per-point capacities, J-T-mode injection rates, acid-gas-compressor injection details, methanol tank SG), the datasheet shall carry the **TBD** marker with a forward reference to the resolving design action. Source: DBM-Deepcut L1328, L1351, L1392.

### R-8 Interface requirements matrix (mandatory)
The Package Datasheet shall include a package interface requirements matrix covering the interface types declared for PKG-077 in PACKAGE_REGISTER.csv:
Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. Source: PACKAGE_REGISTER.csv (PKG-077).

### R-9 Design temperature consistency at downstream interfaces
The Package Datasheet shall reflect that downstream BAHX equipment carries a maximum design temperature of **150 degF (66 degC)**, and that injection-system materials and warm-up controls at BAHX pass inlets shall be consistent with this limit. Source: DBM-Deepcut L1324.

### R-10 Responsibility split
The Package Datasheet shall identify the responsibility split for PKG-077: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns facility-level integration and interfaces. Source: PACKAGE_REGISTER.csv (PKG-077); `_CONTEXT.md`.

### R-11 Objective traceability (ASSUMPTION — package-grouping heuristic)
The Package Datasheet shall reference its supporting objectives `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010`. **ASSUMPTION:** association is by package-grouping heuristic (OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC) — directionally relevant, not a confirmed deliverable-level mapping. Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (DEL-077-02).

### R-12 SOW traceability
The Package Datasheet shall reference `SOW-0143` as the scope item covered. Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (DEL-077-02).

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| ALPEMA 3rd Edition (downstream BAHX) | Governs BAHX downstream of injection points; relevant for material/temperature compatibility. | DBM-Deepcut L1324 |
| ASME U Stamp; BC CRN (downstream BAHX) | Pressure-vessel certification of downstream BAHX. | DBM-Deepcut L1324 |
| Project specifications referenced by `26020-Package_Requirements.docx` | Package-level vendor requirements basis. | **location TBD** (source not accessible as text) |
| Manufacturer standard practices with vendor exceptions | Applies to BAHX; methanol-package vendor std practices: **TBD**. | DBM-Deepcut L1324 |

## Verification

| Req | Verification Approach |
|---|---|
| R-1, R-10, R-11, R-12 | Documentation review against PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, `_CONTEXT.md`. |
| R-2, R-3, R-4 | Trace each statement and injection-point row in the datasheet to the cited DBM-Deepcut slice. |
| R-5 | Cross-check tag list against DBM-Deepcut Equipment List rows 54-55 and Sparing table. |
| R-6 | Confirm tank/pump descriptors and SG TBC qualifier are present and match source phrasing. |
| R-7 | Confirm every source-TBC/TBD value is carried as TBD in datasheet (no inferred numbers). |
| R-8 | Compare interface matrix rows to PACKAGE_REGISTER.csv interface-type list for PKG-077. |
| R-9 | Confirm 150 degF (66 degC) limit appears in interface/conditions section. |

## Documentation (anticipated artifacts)

- Package technical datasheet (this deliverable artifact: `Datasheet.md`).
- Vendor engineering handoff basis section.
- Package interface requirements matrix (embedded; per `_CONTEXT.md`).
- Source-supported equipment list and design criteria.

Source: `_CONTEXT.md` Anticipated Artifacts.
