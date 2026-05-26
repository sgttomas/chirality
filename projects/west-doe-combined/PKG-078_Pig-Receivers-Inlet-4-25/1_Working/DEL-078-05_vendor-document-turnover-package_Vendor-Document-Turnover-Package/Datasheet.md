# Datasheet — DEL-078-05 Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-078-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-078` | `_CONTEXT.md` |
| PackageName | Pig Receivers (Inlet) 4-25 | `_CONTEXT.md` |
| Package tag | `26020-01-PT-35-001 - Pig Receivers (Inlet)` | `_Sources/26020-Package_Requirements.docx`, heading 1 (para 393) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Document Turnover | `_CONTEXT.md` |
| ResponsibleParty | Package Vendor (vendor documentation); EPC Integrator interface/integration review | `_CONTEXT.md`; DELIVERABLE_REGISTER row 436 |

## Attributes (Scope-of-supply context this turnover documents)

| Attribute | Value | Source |
|---|---|---|
| Quantity of pig receiver assemblies | 3 (PR-1010/1020/1030-1) | `_Sources/26020-Package_Requirements.docx` 26020-01-PT-35-001 / Major Included Equipment |
| Nominal size | 610 mm OD (24") | same |
| Skid type | Dedicated structural steel non-enclosed skid; one per receiver | same |
| Isolation | All skid-mounted isolation or ESDV | same |
| Protection package | HIPPS package per receiver skid, with ESDVs upstream of the pig receiver | same |
| HIPPS control | Pressure control valve + outlet pressure transmitter, PID control to keep inlet separator below applicable pressure | same |
| HIPPS shutdown | Pneumatic hi-low shutoff shutdown valve, plus redundant shutdown valve with pneumatic hi-low | same |
| Service | Sour service; design 1.0 mol% (H2S basis, ASSUMPTION — source states "1.0 mol%" without species label) | same |
| Purge | Sweet gas purge downstream of manual isolation valve, for sour gas purge or barrel purge prior to opening for pig retrieval | same |
| Vent | Vent line to HP flare system | same |
| Process function | Plant inlet pipeline gas enters the facility through the pig receivers and moves into the inlet separators | same / Basic Scope |
| Physical interface source | `26020-Packages_Interfaces.3.xlsx` (referenced by source) | same / Physical Interface Summary |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Process role | Plant inlet, upstream of inlet separators | `_Sources/26020-Package_Requirements.docx` (Basic Scope) |
| Service classification | Sour service (1.0 mol% basis) | same |
| Vent destination | HP flare header | same |
| Operating/design pressure, temperature, fluid composition | TBD | not stated in source slice |

## Construction (Document Turnover Composition)

This deliverable is a **document set** about the supplied equipment. It does not specify the equipment construction itself (that is `DEL-078-04`). The turnover package is composed of the artifact classes below.

| Component | Description | Source |
|---|---|---|
| Vendor document register | Master index of vendor-supplied documents for this package, with revision and status | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row 436 Primary Artifact column |
| Vendor document submittals | Issued vendor documents (drawings, calculations, datasheets, manuals, certifications) per the register | same |
| Source-required vendor document artifacts | Vendor documents enumerated in source `Vendor Engineering Deliverables` for this package | `_Sources/26020-Package_Requirements.docx` 26020-01-PT-35-001 / Vendor Engineering Deliverables (section present but empty in source) — list TBD |
| Turnover records | Receipt, transmittal, acceptance, and as-built/as-shipped evidence | `_CONTEXT.md`; DELIVERABLE_REGISTER row 436 |

### Mandatory document classes (ASSUMPTION pending source resolution)

The `Vendor Engineering Deliverables` heading exists in the source for `26020-01-PT-35-001` but its body is empty in the available slice. Until the source is amended or another package-level vendor-deliverables list is provided, the specific required document classes for this package are `TBD`. Conventional vendor turnover document classes typically include:

- General arrangement / outline drawings — ASSUMPTION
- P&IDs (vendor scope) — ASSUMPTION
- Mechanical datasheets for major components (receiver barrel, ESDVs, HIPPS valves, transmitters) — ASSUMPTION
- HIPPS SIL verification and proof-test documentation — ASSUMPTION
- Pressure vessel code stamps / U-1A or equivalent — ASSUMPTION (jurisdiction TBD)
- Welding records, NDE reports, hydrotest records — ASSUMPTION
- Material test reports (MTRs) for pressure-containing components — ASSUMPTION
- Operating and maintenance manuals — ASSUMPTION
- Spare parts list — ASSUMPTION
- Inspection and test plan (ITP) executed records — ASSUMPTION

Each of the above must be confirmed against the source `Vendor Engineering Deliverables` list once populated, or against the project's EPC vendor documentation standard (location TBD).

## References

- `_Sources/26020-Package_Requirements.docx`, heading 1 `26020-01-PT-35-001 - Pig Receivers (Inlet)` (paragraph 393) — package scope basis.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — interface source referenced by the package scope (slice TBD).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- DELIVERABLE_REGISTER row 436, GATE-07_Final_Published_2026-05-24 snapshot.
