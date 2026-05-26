# Datasheet — DEL-097-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-097-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-097` | `_CONTEXT.md` |
| PackageName | Tanks, Condensate (API 650) 3-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Source Reference | Workbook Packages row 88; `26020-Package_Requirements.docx` package heading 49 (`26020-03-PT-19-006 - Tanks, Condensate`) | `_CONTEXT.md`; source slice extracted from `26020-Package_Requirements.docx` heading "26020-03-PT-19-006 - Tanks, Condensate" |

## Attributes

The deliverable is an EPC-Integrator-led acceptance record set for the sweet product condensate (API 650) tank package supplied by the Package Vendor for the 03-25 West Doe Liquids Hub tank farm. It collects vendor document review outcomes, integration acceptance findings, test/inspection evidence, and turnover readiness evidence against the EPC Scope of Work (`DEL-097-01`), Package Datasheet (`DEL-097-02`), and Construction Work Package (`DEL-097-03`).

| Attribute | Value | Source |
|---|---|---|
| Acceptance target package | Tanks, Condensate (API 650) 3-25 — C5+ Condensate Product Storage | `26020-Package_Requirements.docx` heading 49 Basic Scope |
| Subject equipment count | Four (4) × 3,800 bbl Condensate Product Storage Tanks | `26020-Package_Requirements.docx` heading 49 Basic Scope / Major Included Equipment |
| Process function | C5+ Condensate (sweet, product) storage | `26020-Package_Requirements.docx` heading 49 Basic Scope |
| Tank construction basis | Modified API 650, non-insulated atmospheric tanks; blanket gas system per API 2000; internal coating (Devchem 253) on floors, walls, roof | `26020-Package_Requirements.docx` heading 49 Major Included Equipment |
| Pressure relief features (per tank) | PVRV for vacuum or modulating pressure relief; EPRV designed for single worst-case relief | `26020-Package_Requirements.docx` heading 49 Major Included Equipment |
| Vapour interface | VRU header connection per tank; blanket gas connection per tank | `26020-Package_Requirements.docx` heading 49 Major Included Equipment |
| Fill limit | Maximum fill 90 % shutdown | `26020-Package_Requirements.docx` heading 49 Major Included Equipment |
| Fill rate basis | Tank nozzles sized so plant design capacity can fill a single tank | `26020-Package_Requirements.docx` heading 49 Major Included Equipment |
| Capacity / design throughput (preliminary) | 94,940 kg/h / 3,187 Am3/d | `26020-Package_Requirements.docx` heading 49 Scope Notes (Preliminary Design conditions) |
| Operating pressure | Atmospheric (ambient) | `26020-Package_Requirements.docx` heading 49 Scope Notes |
| Operating temperature | 0 °C (min) and 40 °C (max) | `26020-Package_Requirements.docx` heading 49 Scope Notes |
| Design pressure | 32 oz test pressure | `26020-Package_Requirements.docx` heading 49 Scope Notes |
| Design temperature | -40 °C (min) and 60 °C (max) | `26020-Package_Requirements.docx` heading 49 Scope Notes |
| Winter recycle | Recycle may be required to maintain a certain temperature during winter | `26020-Package_Requirements.docx` heading 49 Major Included Equipment |
| Excluded scope ("By others") | Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. | `26020-Package_Requirements.docx` heading 49 Scope Notes / Open Items |
| Hub context — total condensate tanks | Eleven 3,800 bbl condensate tanks across hub: 2 sour inlet + 4 sour + 4 product + 1 slop | DBM `3-25_Comp_and_Liquids_DBM.md` SEC "Condensate Storage and Product Handling" (line 406) |
| Vendor responsibility split | Vendor engineers/designs/supplies; EPC reviews/accepts/integrates | OBJ-004; `DEL-097-04` register row |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sweet C5+ stabilized condensate (product) | `26020-Package_Requirements.docx` heading 49 Basic Scope; DBM line 406 ("four product condensate tanks") |
| Hub condensate basis | 3,180 m3/d (20,000 bbl/d) stabilized condensate at the Liquids Hub | DBM line 376 |
| Ambient minimum (site) | -40 °C governs exposed equipment, packages, panels, instrumentation | DBM Site Basis (declared in DBM site basis section) |
| Vapour disposition | Tank vapours collected via VRU header (2 × 100 % VRU compressors; routed to 04-25 SOC under SCA-002) | DBM lines 436, 442; `26020-Package_Requirements.docx` heading 49 Physical Interface Summary (Relief / Flare / Vent: Yes) |
| Downstream product route | Booster pumps transfer product to LACT pump/interface system; LACT is third-party NRM scope (facility provides tie-in only) | DBM line 417 |

## Construction (Acceptance Evidence Items)

These are the categories of evidence the acceptance record captures. Specific tank construction values reside in `DEL-097-02 Package Datasheet`; this deliverable verifies them, it does not redefine them.

| Evidence Item | Description | Source/Driver |
|---|---|---|
| Vendor document review log | Review status per item against Vendor Document Turnover Package (`DEL-097-05`) and against the vendor engineering deliverable list at `26020-Package_Requirements.docx` heading 49 ("Vendor Engineering Deliverables") | `26020-Package_Requirements.docx` heading 49 Vendor Engineering Deliverables; OBJ-010 |
| Package acceptance checklist | EPC verification that vendor scope conforms to SOW, Datasheet, and CWP | OBJ-004; `_CONTEXT.md` Anticipated Artifacts |
| Test and inspection evidence | API 650 hydrotest, NDE, coating verification (Devchem 253), pressure/vacuum relief (PVRV/EPRV) function, blanket gas system function, winter-recycle provisions verification | `26020-Package_Requirements.docx` heading 49 Major Included Equipment; ASSUMPTION on clause-level API 650 acceptance tests — clause-level details `location TBD` |
| Turnover evidence | Mechanical completion, punch lists, commissioning records, custody handoff to facility operations | OBJ-010 |
| Integration interface acceptance | Tie-ins per `26020-Package_Requirements.docx` heading 49 Physical Interface Summary marked **Yes**: Process Piping; Relief / Flare / Vent; Drain / Containment; Area / Exterior Lighting; Grounding / Bonding; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `26020-Package_Requirements.docx` heading 49 Physical Interface Summary; OBJ-005, OBJ-006, OBJ-008 |
| Non-conformance and open-item closure | Documented dispositions for vendor NCRs and EPC-identified gaps; closure of the heading-49 "Interface Coordination Notes" item currently marked **TBD** in source | `26020-Package_Requirements.docx` heading 49 Interface Coordination Notes; OBJ-010 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Sources/26020-Package_Requirements.docx` heading 49 (`26020-03-PT-19-006 - Tanks, Condensate`) — source slice extracted (Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes)
- DBM `3-25_Comp_and_Liquids_DBM.md` — sections on Facility Overview, Condensate and Produced-Water Receipts, Condensate Storage and Product Handling (line 406-417), VRU and Vapour Handling (line 436-442), Site Basis
- Decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` rows `DEL-097-01` … `DEL-097-06`
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC mapping for `PKG-097`)

## TBD / ASSUMPTION Inventory

- `TBD`: API 650 clause-level test/inspection acceptance criteria — API 650 standard text is not in local source set.
- `TBD`: API 2000 clause-level blanket gas / pressure-vacuum venting acceptance criteria — API 2000 standard text is not in local source set.
- `TBD`: Source field "Interface Coordination Notes" in `26020-Package_Requirements.docx` heading 49 explicitly states "TBD." Acceptance cannot close until coordination notes are provided or explicitly carried over.
- `ASSUMPTION`: Vendor document review log structure mirrors the "Vendor Engineering Deliverables" table at heading 49 (Core vendor documents, Core package engineering, Storage tanks, Relief/flare/vent design, Process piping interfaces, Drainage/containment interfaces, Electrical/lighting/EHT/grounding, Cathodic protection interfaces, Instrumentation and controls interfaces, Structural/foundations/supports/access, Civil grading/spill containment interfaces).
- `ASSUMPTION` (PACKAGE_HEURISTIC): Objectives `OBJ-002` … `OBJ-010` apply via the package-grouping mapping; not deliverable-ID-explicit.
- `ASSUMPTION`: Sweet (product) service classification — heading 49 names the package "Condensate" (no sour qualifier) and DBM line 406 differentiates sour vs product condensate tanks; this package corresponds to the product service group. Sour service applies only via residual H2S exposure pathways; not explicitly stated for product tanks in the heading-49 slice.
