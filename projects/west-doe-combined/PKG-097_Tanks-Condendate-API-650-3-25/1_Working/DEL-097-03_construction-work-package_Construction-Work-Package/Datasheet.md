# Datasheet — DEL-097-03 Construction Work Package (Tanks, Condensate, API 650, 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-097-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-097` |
| PackageName | Tanks, Condensate (API 650) 3-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Package Source Heading | `26020-03-PT-19-006 - Tanks, Condensate` (heading 49 of `26020-Package_Requirements.docx`) |

## Attributes

Construction-relevant attributes of the package being installed, as drawn from the source slice:

| Attribute | Value | Source |
|---|---|---|
| Tank quantity | Four (4) tanks | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Basic Scope |
| Nominal capacity (each) | 3800 bbl | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Process service | C5+ Condensate Storage Tanks | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Basic Scope |
| Design / fabrication code | Modified API 650 | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Insulation | Non-insulated atmospheric tanks | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Blanket gas system | Per API 2000 | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Internal coating | Devchem 253 on floors, walls, roof | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Pressure / vacuum protection | PVRV (modulating relief) and EPRV (single worst-case relief) each tank | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Vapor recovery | VRU header connection at each tank | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Fill limit | Maximum fill 90% shutdown | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Fill rate basis | Tank nozzles sized so plant design capacity fills a single tank | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |
| Winter temperature maintenance | Recycle may be required (atmospheric tanks) | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` / Major Included Equipment |

## Conditions

Construction site / installation conditions:

| Condition | Value | Source |
|---|---|---|
| Site | West Doe Combined facility, 3-25 area | `_CONTEXT.md` (Package identity); decomposition PROJECT_DECOMP Gate 7 snapshot — ASSUMPTION (site coordinates not in source slice; location TBD) |
| Ambient design conditions | TBD | location TBD (not in PKG-097 source slice) |
| Seismic / wind design | TBD | location TBD (not in PKG-097 source slice) |
| Soil/foundation basis | TBD | location TBD (interfaces to PKG-002/PKG-006 — see _DEPENDENCIES.md when populated) |
| Containment berm required | ASSUMPTION (typical for atmospheric condensate storage) — confirm against PKG-006 | location TBD in PKG-097 source slice |

## Construction

Construction-package contents (what the EPC Construction Work Package must contain for this package), per `_CONTEXT.md` Anticipated Artifacts:

- Construction work package (master document; this deliverable)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Physical construction scope items derived from the source slice:

- Erection of four (4) modified API 650 atmospheric tanks (3800 bbl each).
- Internal coating application (Devchem 253) on floor, walls, and roof — ASSUMPTION: coating typically applied by tank fabricator; field touch-up scope TBD.
- Installation of PVRV and EPRV on each tank with venting routed to blanket-gas / VRU header per package design — connections per API 2000 (blanket gas system).
- Tie-in of blanket gas supply, VRU header, fill, suction, drain, and instrument nozzles — interface tags TBD (Interface source `26020-Packages_Interfaces.3.xlsx`).
- Installation of overfill protection / high-level shutdown to enforce 90% maximum fill limit.

## References

- `26020-Package_Requirements.docx`, §`26020-03-PT-19-006 - Tanks, Condensate` (package heading 49) — primary source slice
- `_CONTEXT.md` (DEL-097-03)
- `_REFERENCES.md` (DEL-097-03)
- Gate 7 PROJECT_DECOMP snapshot DELIVERABLE_REGISTER row for `DEL-097-03_construction-work-package`
- `26020-Packages_Interfaces.3.xlsx` — interface source referenced by PKG-097 (not opened in this pass; location TBD for specific construction tie-in rows)

## Epistemic Notes

- Non-trivial values are sourced from the PKG-097 slice of `26020-Package_Requirements.docx`.
- Items marked `TBD` or `ASSUMPTION` are not invented; they reflect that the PKG-097 source slice does not contain the value and other locally accessible sources have not been opened in this pass.
