# Datasheet: DEL-049-04 — Vendor Engineered Equipment Package

> Production unit: vendor-engineered physical equipment package and accompanying
> vendor design basis and datasheet set for the Sales Gas Booster Compressor
> package (PKG-049). This datasheet describes the **Vendor Production Unit
> itself** — i.e., the engineered package as a deliverable — not the as-built
> equipment specification (which the Vendor produces inside the unit).

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-049-04_vendor-engineered-equipment-package` | `_CONTEXT.md` (Identity) |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-049` | `_CONTEXT.md` |
| Parent Package Name | Sales Gas Booster Compressor | `_CONTEXT.md` |
| Workbook Row | 80 | `PACKAGE_REGISTER.csv` (PKG-049) |
| WBS / Facility Code | 01 | `PACKAGE_REGISTER.csv` (PKG-049) |
| CoA Tracking Number | `26020-01-12-004` | `PACKAGE_REGISTER.csv` (PKG-049) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | SOW-0169, SOW-0170, SOW-0171, SOW-0172 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (ASSUMPTION: package-grouped mapping) |

## Attributes (Production-Unit Scope)

| Attribute | Value | Source |
|---|---|---|
| Production Unit Function | Engineer, design, fabricate / supply, and deliver the physical sales gas booster compressor package, and produce the supporting vendor design basis and datasheet set. | `DELIVERABLE_REGISTER.csv` (DEL-049-04); `_CONTEXT.md` |
| Authority Anchors (inputs) | EPC Scope of Work (DEL-049-01) and EPC Package Datasheet (DEL-049-02) | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` (DEL-049-04) |
| Vendor-Owned Activities | Package engineering, package design, vendor documentation, physical equipment package supply | `PACKAGE_REGISTER.csv` (PKG-049 responsibility model); OBJ-004 |
| EPC-Owned Activities (outside this unit) | Integration into the facility, interface coordination, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` (PKG-049); OBJ-004 |
| Coordination Mode (dependencies) | DECLARED; no upstream/downstream declared during PREPARATION | `_DEPENDENCIES.md` |

## Process Conditions (Authoritative Source Values)

These values come from the workbook/package source for PKG-049 (SOW-0172) and
frame the engineered package the Vendor must deliver. They are reproduced here
as datasheet attributes of the production unit; the Vendor's internal
equipment datasheets are produced inside the unit.

| Parameter | Value | Source |
|---|---|---|
| Process function | Sweet sales gas from sales gas booster header is compressed, then routed to the sales gas coalescer and on to the sales gas splitter. | SOW-0170 |
| Service / fluid | Sweet sales gas (export service downstream of treating) | SOW-0170 |
| Design capacity | 3,962 e3m3/day (140 MMSCFD); no turndown | SOW-0172 |
| Suction design pressure | 6,137 kPag (890 psig) | SOW-0172 |
| Discharge design pressure | 12,866 kPag (1,866 psig) | SOW-0172 |
| Inlet operating temperature (summer) | 110 °F (43.3 °C) | SOW-0172 |
| Suction scrubber inlet liquid density (design assumption) | 0.61 SG | SOW-0172 |
| Driver type | Electric induction motor, 8-pole, 1,000 kW (1,340 HP), 4,000 V / 3 PH / 60 Hz, 891 rpm fixed speed; TEFC or WPII; non-sparking bidirectional cooling fan; NEMA MG 1 | SOW-0172; SOW-0171 |
| Driver start | DOL driver with soft-start | SOW-0171 |

## Construction (Major Included Equipment in the Engineered Package)

Per SOW-0171, the engineered package the Vendor produces includes at least:

| Item | Source-stated description | Source |
|---|---|---|
| Reciprocating compressor | Ariel KBX/X reciprocating compressor; all cylinders dedicated | SOW-0171 |
| Compressor driver motor | 8-pole induction motor, 4,000 V / 3 PH / 60 Hz, 891 rpm | SOW-0171 |
| Intercooler | Forced-air intercooler after each cylinder stage, mounted on common frame; API 661; horizontal air-flow type, single fan; automated louver control | SOW-0171 |
| Suction scrubbers | Suction scrubber after each cylinder booster stage; two-phase with vertical-flow mesh/vane; vendor to design size and capacity | SOW-0171 |
| Packing vent / drain separation pot | Two-phase, design pressure 101 kPag; vendor to design size and capacity | SOW-0171 |
| Seal-pot waste-oil transfer pump | Vendor to design size and capacity | SOW-0171 |
| Filter coalescer | 0.3 microns at 99.97 %, with band-lock-type QOC; 100 MMSCFD design flow | SOW-0171 |

### Boundary / "By Others" Items (Not in the Engineered Package)

| Item | Owner | Source |
|---|---|---|
| Shipping of compressor package to site | EPC / Others | SOW-0172 |
| Installation on piles | EPC / Others | SOW-0172 |
| Tie-in piping | EPC / Others | SOW-0172 |
| Electrical connections (field) | EPC / Others | SOW-0172 |
| Mounting platform and stairs | EPC / Others | SOW-0172 |

## Interfaces Visible at the Package Boundary

The PKG-049 row carries the following applicable interface types; the
engineered package must terminate cleanly at each one. Detail is owned by the
EPC Package Datasheet (DEL-049-02); this unit consumes that datasheet.

- Process Piping (`IFC-6F3284BD09`)
- Utility Piping (`IFC-6D861B0A1E`)
- Relief / Flare / Vent (`IFC-4F859320AC`)
- Drain / Containment (`IFC-B0428E17A6`)
- Electrical Power (`IFC-045BB63672`)
- EHT (`IFC-7C1CF9DE6E`)
- Grounding / Bonding (`IFC-C2A8925032`)
- Area / Exterior Lighting (`IFC-8441C470C8`)
- I&C / Control Cabling (`IFC-6007E8A9BD`)
- Building HVAC / Services (`IFC-EC18998BA7`)
- Fire & Gas / Safety Systems (`IFC-A788573557`)
- Maintenance Access (`IFC-CB5E4C28C1`)
- Structural / Foundations / Supports (`IFC-A0F211EA28`)

Source: `INTERFACE_REGISTER.csv` (PKG-049 rows).

## Anticipated Artifacts (from Production Unit)

- Vendor engineered physical equipment package (the package itself, fabricated and supplied).
- Vendor package design basis and datasheet set.

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` (DEL-049-04 anticipated artifacts).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot `2026-05-24`:
  - `PROJECT_DECOMP.md`
  - `DELIVERABLE_REGISTER.csv`
  - `PACKAGE_REGISTER.csv`
  - `SCOPE_LEDGER.csv` (SOW-0169..SOW-0172)
  - `OBJECTIVE_REGISTER.csv` (OBJ-001, OBJ-003..OBJ-010)
  - `INTERFACE_REGISTER.csv` (PKG-049 rows)
  - `ARTIFACT_REGISTER.csv` (PKG-049 rows)
- Upstream source materials referenced by the decomposition row (not opened in this run): `26020-Package_Requirements.docx` package heading 4; `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md`. Location TBD inside this deliverable's scope.

## Notes

- Objective associations are recorded as **ASSUMPTION (package-heuristic, best-effort)** per `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`.
- This deliverable is the **vendor production unit** itself; per `_CONTEXT.md` Notes it is "framed as a vendor package production unit anchored by the EPC Scope of Work and Package Datasheet." Equipment-level datasheets are vendor-produced artifacts inside the unit, not this file.
