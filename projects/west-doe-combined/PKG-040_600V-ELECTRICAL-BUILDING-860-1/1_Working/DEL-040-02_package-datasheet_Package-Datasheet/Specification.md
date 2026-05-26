# Specification — DEL-040-02 Package Datasheet (PKG-040 600V Electrical Building 860-1)

> Normative requirements that the Package Datasheet, when issued to the package vendor and discipline package engineer, must convey.
> All requirements are source-grounded; missing values are marked `TBD`; inferences are labelled `ASSUMPTION`.

## Scope

This specification governs the **content** of the Package Datasheet for PKG-040 (600V Electrical Building 860-1) — the EPC Integrator's technical handoff to the Package Vendor and downstream discipline package engineering. It does not specify the physical electrical building itself; it specifies the information set the EPC Integrator must publish for that building to be designed, fabricated, integrated, and accepted.

**Included:**
- Required identification, scope, boundary, and ownership statements.
- Required design-condition fields traceable to the project DBMs.
- Required interface set (the 12 interface types registered for this package).
- Required pointers to governing codes and standards.
- Required documentation deliverable list.

**Excluded:**
- Vendor-internal design choices (the package vendor decides component selection within the envelope).
- Construction work-package content (DEL-040-03).
- Vendor document register and turnover content (DEL-040-05).
- Vendor package review/acceptance content (DEL-040-06).

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-040-02..06 rows.

## Requirements

### R1 — Identification (mandatory fields)

The datasheet MUST identify the package by: DeliverableID, Package ID, Workbook Equipment Code, Building Tag, Building Function, Discipline, WBS, Responsible Party, and Package Vendor / EPC Integrator scope split. Values for this package are listed in `Datasheet.md` § Identification.
- Source: `PACKAGE_REGISTER.csv` row 42; `_CONTEXT.md`.

### R2 — Scope and ownership statement

The datasheet MUST state Package Vendor ownership (package engineering, package design, vendor documentation, physical equipment package) and EPC Integrator ownership (integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration).
- Source: `PACKAGE_REGISTER.csv` row 42.

### R3 — Area classification and siting

The datasheet MUST specify that the electrical building is sited in a **general purpose (non-hazardous) area** for convenient power distribution.
- Source: `4-25_Deepcut_DBM.md` Electrical Buildings; Area Classification.
- Verification: V-AC.

### R4 — Building HVAC

The datasheet MUST require **n+1 HVAC** sized so that failure or maintenance shutdown of one HVAC unit does not affect building heating and cooling.
- Source: `4-25_Deepcut_DBM.md` Electrical Buildings.
- Verification: V-HVAC.

### R5 — Cable entry and elevation

The datasheet MUST require **bottom entry** for incoming and outgoing power cables and that the building be **elevated on piles** to provide under-building tray space to the 600 V MCC main incoming section. Outgoing cables from 600 V MCCs to facility loads MUST also be bottom entry.
- Source: `4-25_Deepcut_DBM.md` Electrical Buildings.
- Verification: V-CABLE-ENTRY.

### R6 — Wiring and raceway methods inside the building

The datasheet MUST require TECK and ACIC cables for building wiring; EMT conduit between adjacent equipment (e.g., control panel to contactor panel); and an outdoor GFI receptacle for exterior maintenance.
- Source: `4-25_Deepcut_DBM.md` Electrical Buildings.
- Verification: V-WIRING.

### R7 — Equipment access

Equipment doors MUST be sized for, or include removable transom sections that allow, removal of the **largest equipment** housed in the building.
- Source: `4-25_Deepcut_DBM.md` Electrical Buildings.
- Verification: V-DOOR.

### R8 — Building heaters

Electric building heaters MUST be **600 V, 3 phase** rated.
- Source: `4-25_Deepcut_DBM.md` (explicit clause).
- Verification: V-HEATER.

### R9 — System voltages housed

The datasheet MUST identify the service voltages the building must support, drawn from the System Voltages table: 600 V 3φ/3W high-resistance grounded (5 A continuous resistor), 208/120 V 3φ/4W solidly grounded (from 600 V step-down), and UPS 120 VAC / 125 VDC.
- Source: `4-25_Deepcut_DBM.md` System Voltages.
- Verification: V-VOLT.

### R10 — Grounding and bonding

The datasheet MUST require: two-point direct connection of major electrical equipment to the ground grid; provision of a ground well at the electrical building for maintenance/operational testing with bolted ground connections at test points; 5 A high-resistance grounding of each 600 V transformer feeding the building's MCC, with ground-fault protection on 600 V systems set to alarm-only.
- Source: `4-25_Deepcut_DBM.md` Grounding and Bonding.
- Verification: V-GND.

### R11 — Standby power tie-in

The datasheet MUST identify the standby-power tie-in point at the 600 V MCC via transfer switch. Specific generator count, rating, transfer-switch type, and load-shedding/critical-load list MAY be carried as `TBD` pending electrical studies.
- Source: `4-25_Deepcut_DBM.md` Standby Power; `3-25_Comp_and_Liquids_DBM.md` 600V MCC and Standby Power.
- Verification: V-STBY.

### R12 — Interface set (12 interface types)

The datasheet MUST publish the full interface set registered for PKG-040 with one row per interface type: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, Structural / Foundations / Supports. The IDs in `INTERFACE_REGISTER.csv` rows 262–273 MUST be carried as evidence pointers.
- Source: `PACKAGE_REGISTER.csv` row 42 ApplicableInterfaceTypes; `INTERFACE_REGISTER.csv` rows 262–273.
- Verification: V-IFC.

### R13 — Foundations and anchorage

The datasheet MUST require equipment-specific foundation and anchorage design for the building, based on the project geotechnical report, equipment loads, snow/wind/seismic, frost protection, vibration, settlement, and maintenance access.
- Source: `3-25_Comp_and_Liquids_DBM.md` Foundations.
- Verification: V-FDN.

### R14 — Construction mode

The datasheet MUST state the building is **shop-fabricated (prefabricated, modular)**.
- Source: `4-25_Deepcut_DBM.md` Electrical Buildings; Building list (`Shop`).
- Verification: V-SHOP.

### R15 — Building color schedule

The datasheet MUST require flashing, doors, and trim color **Cloverdale #2593 "Safety Green"** per project building color schedule (unless the project formally revises the schedule).
- Source: `4-25_Deepcut_DBM.md` Buildings color schedule.
- Verification: V-COLOR.

### R16 — TBD discipline values

Where the datasheet would otherwise need values not present in the source set (e.g., per-bucket MCC count, transformer kVA, panelboard quantities, exterior lighting fixture schedule, fire & gas detector layout), it MUST mark them `TBD` rather than invent values, and identify the downstream task expected to resolve each (detailed electrical engineering, vendor proposal, etc.).
- Source: Skill four-documents non-negotiable constraints (no-invention rule); deliverable-local epistemic policy.
- Verification: V-TBD.

## Standards (governing)

The following codes and standards govern the technical content the datasheet must reflect. Specific clause references are kept at the source-document level; clause-level location is `TBD` where not in the locally accessible slice.

| Standard / Authority | Use | Source slice |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Primary electrical design / installation compliance basis. | `4-25_Deepcut_DBM.md` Governing Codes |
| BC provincial and local electrical codes; BC electrical inspection authority | Jurisdictional compliance and inspection. | `4-25_Deepcut_DBM.md` Governing Codes |
| CSA, API, IEEE, ISA, NEMA | Equipment standards (specific clause `location TBD`). | `4-25_Deepcut_DBM.md` Governing Codes |
| WorkSafeBC, Technical Safety BC, BCER | Regulatory authorities. | `4-25_Deepcut_DBM.md` Governing Codes |
| Third-party certification — CSA, ULc, FM, ETL, or equivalent NRTL | All supplied electrical equipment must be third-party certified. | `4-25_Deepcut_DBM.md` Governing Codes |
| API RP 505 | Area classification (general facility basis; building itself sited in GP area). | `3-25_Comp_and_Liquids_DBM.md` Area Classification |
| OGAOM Sec. 9.6.15 | Spacing between fired heaters and control room or electrical buildings (25 m / 82 ft). | `4-25_Deepcut_DBM.md` Electrical Equipment Spacing |
| CEC spacing (MCC to process equipment 7.5 m) | Layout siting constraint relevant where this building sits adjacent to process. | `4-25_Deepcut_DBM.md` Electrical Equipment Spacing |

Deviations from applicable codes and standards require formal approval by the project owner (Tourmaline Oil Corp.) per `4-25_Deepcut_DBM.md` Governing Codes.

## Verification

| ID | Method | Evidence |
|---|---|---|
| V-AC | Inspection — site plan / area classification drawing review. | Approved area classification drawing showing 860-1 in GP area. |
| V-HVAC | Vendor HVAC sizing calc + factory test. | n+1 HVAC sizing calculation; FAT log. |
| V-CABLE-ENTRY | Vendor general arrangement (GA) drawing review; field walkdown. | GA drawing showing bottom entry; field walkdown record. |
| V-WIRING | Vendor wiring schedule and bill of materials review; field check. | Cable schedule; receptacle location plan. |
| V-DOOR | Vendor GA drawing review against largest housed equipment outline. | GA drawing; equipment-removal plan. |
| V-HEATER | Vendor data sheet review; nameplate inspection. | Heater data sheet; nameplate photos. |
| V-VOLT | Single-line diagram review. | Approved single-line for the building. |
| V-GND | Grounding plan and ground-well drawing review; megger/ground resistance test. | Grounding plan; commissioning test record. |
| V-STBY | Single-line + transfer-switch wiring review; ATS functional test. | Single-line; ATS test record. |
| V-IFC | Interface matrix completeness check against `INTERFACE_REGISTER.csv` rows 262–273. | Interface matrix exported from datasheet. |
| V-FDN | Civil/structural calculation package review. | Foundation design calc per geotech report. |
| V-SHOP | Verification that vendor proposal is shop-fabricated modular package. | Vendor proposal narrative; FAT plan. |
| V-COLOR | Vendor finish schedule review. | Vendor finish schedule referencing Cloverdale #2593. |
| V-TBD | QA audit confirming no invented values; each TBD has an owner. | TBD register inside the datasheet. |

## Documentation

The Package Datasheet, when complete, shall serve as the source basis for and shall reference the following anticipated artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Package technical datasheet (this `Datasheet.md`, populated to vendor-issue level).
- Vendor engineering handoff basis (consolidated references).
- Package interface requirements matrix (12 interfaces from `INTERFACE_REGISTER.csv`).
- Source-supported equipment and design criteria summary.

Downstream documentation linkages (consumers of this datasheet) — informational, not requirements created here:
- DEL-040-03 Construction Work Package consumes the boundary, foundation, and interface statements.
- DEL-040-04 Vendor Engineered Equipment Package consumes the technical envelope and the interface matrix.
- DEL-040-05 Vendor Document Turnover Package frames its register against the artifacts this datasheet anchors.
- DEL-040-06 EPC Vendor Package Review and Acceptance evaluates vendor deliverables against this datasheet's requirements.

Source: `DELIVERABLE_REGISTER.csv` PKG-040 rows.
