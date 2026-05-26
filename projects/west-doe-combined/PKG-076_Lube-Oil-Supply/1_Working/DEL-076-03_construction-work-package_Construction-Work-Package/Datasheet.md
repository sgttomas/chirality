# Datasheet — DEL-076-03 Construction Work Package (Lube Oil Supply, PKG-076)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-076-03_construction-work-package | `_CONTEXT.md` Identity |
| Name | Construction Work Package | `_CONTEXT.md` Identity |
| ParentPackage | PKG-076 — Lube Oil Supply | PACKAGE_REGISTER.csv row 70 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER row 70 |
| Type | EPC Construction Work Package | DELIVERABLE_REGISTER.csv row 386 |
| ResponsibleParty | EPC Integrator | DELIVERABLE_REGISTER.csv row 386 |
| Facility | West Doe Deepcut — Storage Tank Area | SCOPE_LEDGER SOW-0136 (heading 30 Basic scope) |
| ParentWorkbookRow | 70 | PACKAGE_REGISTER.csv row 70 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Lube oil supply to compressor packages on site | SCOPE_LEDGER SOW-0136 |
| Major equipment count | Two (2) lube oil transfer pumps + one (1) horizontal storage tank (split, two services) | SCOPE_LEDGER SOW-0137 |
| Equipment tag P-9240-1 | Cylinder Lube Oil Transfer Pump — fills frame day tanks with cylinder lube oil from 400 bbl heated tank section | SCOPE_LEDGER SOW-0137 |
| Equipment tag P-9250-1 | Crankcase Lube Oil Transfer Pump — fills frame day tanks with crankcase lube oil from 200 bbl heated tank section | SCOPE_LEDGER SOW-0137 |
| Storage tank | Horizontal, split in middle to store both lube oils (crankcase and compressor cylinder/packing) | SCOPE_LEDGER SOW-0137 |
| Driver type | Electric motor driven (No Toshiba motors) | SCOPE_LEDGER SOW-0137 / SOW-0138 |
| Service classification | Sweet and sour service | SCOPE_LEDGER SOW-0137 |
| Procurement/install ownership split | Package supply by Package Vendor; "Shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs" — By Others (EPC Integrator scope) | SCOPE_LEDGER SOW-0138 |

## Conditions

| Item | Value | Source |
|---|---|---|
| Operating conditions (pump service) | Low / atmospheric | SCOPE_LEDGER SOW-0138 |
| Operating temperature | Ambient to heated tank temperature | SCOPE_LEDGER SOW-0138 |
| Design conditions (pump service) | Low / atmospheric | SCOPE_LEDGER SOW-0138 |
| Design temperature | Ambient to heated tank temperature | SCOPE_LEDGER SOW-0138 |
| Site / area classification | TBD (not stated in available decomposition source slice; resolve from 26020-Package_Requirements.docx heading 30 when accessible) | location TBD |
| Seismic / wind loads | TBD | location TBD |

## Construction (Construction-Work-Package Scope Attributes)

The Construction Work Package describes how PKG-076 is physically installed, built, inspected, turned over, and tied into the larger facility systems (`_CONTEXT.md` Scope).

| Construction Element | Description | Source |
|---|---|---|
| Foundation / supports | Pile foundations under the lube oil package; supplied/installed by EPC Integrator (By Others scope) | SCOPE_LEDGER SOW-0138; PACKAGE_REGISTER row 70 (Structural / Foundations / Supports interface) |
| Mounting platform & stairs | EPC Integrator scope (By Others) | SCOPE_LEDGER SOW-0138 |
| Tie-in piping | EPC Integrator scope (By Others); applicable interfaces include Utility Piping and Drain / Containment | SCOPE_LEDGER SOW-0138; INTERFACE_REGISTER IFC-B592C2D9F7, IFC-09EA6BEDB8 |
| Electrical connections | EPC Integrator scope (By Others); Electrical Power and Grounding / Bonding interfaces apply | SCOPE_LEDGER SOW-0138; INTERFACE_REGISTER IFC-4D53A7E70E, IFC-7117284B73 |
| Area / exterior lighting | EPC Integrator interface scope | INTERFACE_REGISTER IFC-986D504634 |
| I&C / control cabling | EPC Integrator interface scope | INTERFACE_REGISTER IFC-8C17CDE23B |
| Maintenance access | EPC Integrator interface scope | INTERFACE_REGISTER IFC-6D43DAF029 |
| Package shipping & receipt | EPC Integrator scope (By Others) | SCOPE_LEDGER SOW-0138 |
| Hydrotest / leak test of tie-ins | TBD — derive from EPC piping spec when accessible | location TBD |
| Lift plan & rigging | ASSUMPTION: required for tank and pump skid setting; specifics TBD pending vendor weights | ASSUMPTION |
| Turnover record / system handover | Anticipated artifact: construction interface and turnover checklist | `_CONTEXT.md` Anticipated Artifacts |

## Anticipated Artifacts (this deliverable produces)

- Construction work package (master document)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Source: `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row 386.

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts
- `_REFERENCES.md` — authoritative basis pointers
- `_DEPENDENCIES.md` — coordination view (no declared upstreams at PREPARATION)
- DELIVERABLE_REGISTER.csv (GATE-07_Final_Published_2026-05-24) row 386
- PACKAGE_REGISTER.csv (GATE-07) row 70
- SCOPE_LEDGER.csv (GATE-07) rows SOW-0135 / SOW-0136 / SOW-0137 / SOW-0138
- INTERFACE_REGISTER.csv (GATE-07) IFC-B592C2D9F7, IFC-09EA6BEDB8, IFC-4D53A7E70E, IFC-7117284B73, IFC-986D504634, IFC-8C17CDE23B, IFC-6D43DAF029, IFC-ACA2756AA0
- Workbook Packages row 70; 26020-Package_Requirements.docx package heading 30 (cited via decomposition; deliverable-local source slice not yet extracted — location TBD)
