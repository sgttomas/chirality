# Specification — DEL-060-01 Scope of Work (PKG-060 Tank Farm Pump Building 4-25)

> Normative requirements for the EPC Integrator Scope of Work deliverable. Requirements are derived from accessible sources in the GATE-07 snapshot and the 4-25 DBM. Where requirement text is implied by the source basis but exact clause text is unavailable, the requirement is labelled `ASSUMPTION` or marked `location TBD`.

## Scope

### In scope (what the Scope of Work shall cover)

The Scope of Work document for PKG-060 shall define, as the EPC Integrator's package-level scope statement:

- The package identity, workbook origin, discipline, and tracking number (PACKAGE_REGISTER row PKG-060; workbook row 85).
- The Package Vendor / EPC Integrator responsibility split (per PACKAGE_REGISTER ResponsibilityModel and OBJ-004).
- The tagged in-package equipment list (per SOW-0190, SOW-0191).
- The process function of in-package pumps (water transfer to 3-25 compressor station; condensate transfer to liquids hub; condensate recycle from produced-water tank skim; process water transfer; fresh caustic transfer) (SOW-0190, SOW-0191).
- Capacity / design throughput statements (SOW-0192).
- Driver/electrical service definition (SOW-0192).
- Building form (self-framing building erected at site) (SOW-0191).
- Applicable interface types (the 14 IFC rows in INTERFACE_REGISTER for PKG-060).
- By-others / boundary items (DCS integration, foundations, electrical supply to MCC) (SOW-0192).
- Whole-facility integration narrative (how the package ties into the 04-25 Deepcut facility and the 03-25 Liquids Hub / Compressor Station).
- Source-basis citations to PROJECT_DECOMP GATE-07 and to `26020-Package_Requirements.docx` heading 15 (and the bid doc `26020-01-PT-RFQ-18-002`).

### Out of scope (the Scope of Work shall NOT define)

- Vendor package engineering, package design, or vendor documentation content (Package Vendor's scope — see DEL-060-04 and DEL-060-05).
- Detailed datasheet content (carried in DEL-060-02 Package Datasheet).
- Construction sequence, tie-in workface, or turnover detail (carried in DEL-060-03 Construction Work Package).
- DCS integration, foundations, or MCC electrical supply (by others per SOW-0192).
- Any package outside PKG-060 (no cross-package edits).

## Requirements

### REQ-SOW-060-01-001 — Package identity disclosure

The Scope of Work shall identify PKG-060 by package ID, workbook row (85), tracking number (`26020-01-18-001`), facility (04-25 Deepcut), WBS (01), and discipline (Mechanical).
Source: GATE-07 PACKAGE_REGISTER.csv (PKG-060 row).

### REQ-SOW-060-01-002 — Responsibility model

The Scope of Work shall state the Package Vendor / EPC Integrator split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration review.
Source: PACKAGE_REGISTER.csv ResponsibilityModel; OBJ-004; SOW-0189.

### REQ-SOW-060-01-003 — Tagged equipment list

The Scope of Work shall enumerate, at minimum, the equipment tags and configurations defined in SOW-0191:

- (2x) Water Transfer Pumps P-9290-1, P-9293-1 — radial centrifugal; single mechanical seal; 218 m3/d at TBC TDH; 7.64 kW.
- (2x) Condensate Transfer Pumps P-9210-1, P-9220-1 — axial-flow multi-stage horizontal centrifugal; API-682 14/52 seal plan; 24 m3/h at TBC TDH; 2 x 150%.
- (1x) Condensate Recycle Pump P-9200-1 — diaphragm positive-displacement Hydrocell; sealless; discharge pulsation dampener; inlet strainer; 20 m3/h at TBC TDH.
- (2x) 100% Process Water Transfer pumps — radial centrifugal; vendor-designed.
- (2x) 100% Fresh Caustic Transfer pumps — radial centrifugal; vendor-designed; corrosive service; no aluminium; flow + density control.

Source: SOW-0191; cross-reference DBM-Deepcut Product Pumps (lines ~1667-1679).

### REQ-SOW-060-01-004 — Process function statements

The Scope of Work shall describe the process function of each pump per SOW-0190:

- Water transfer pumps: pull water from the produced-water tanks and push to the 3-25 compressor station.
- Condensate transfer pumps: transfer condensate to the downstream liquids hub at 350 kPad (50 psid) differential.
- Condensate recycle pump: recycle condensate from the produced-water tank condensate skim.

ASSUMPTION: process-water transfer pump and fresh-caustic transfer pump process functions are stated as "vendor to design" — narrative function text is referenced to the 26020-Package_Requirements.docx heading 15 (`location TBD`).

### REQ-SOW-060-01-005 — Capacity and design throughput statements

The Scope of Work shall state the capacity / design throughput per SOW-0192:

- Water Pump: 218 m3/d at TBC TDH; each sized to 100% capacity.
- Condensate Transfer Pump: 24 m3/h at TBC TDH; each sized to 150% facility design flow of combined condensate product.
- Condensate Recycle Pump: 20 m3/h at TBC TDH; sized to 100% capacity.

Operating conditions and design conditions are TBC per SOW-0192.

### REQ-SOW-060-01-006 — Driver / electrical basis

The Scope of Work shall state: all pumps driven by 575V / 3PH / 60Hz motors; starting method DOL or VFD with local H-O-A or On-Off control; electric motor fed from 600V MCC; motors sized for inlet stabilizer composition density at -40 deg C startup.
Source: SOW-0192; DBM-Deepcut Product Pumps (line ~1679).

### REQ-SOW-060-01-007 — Building form

The Scope of Work shall record the building form: self-framing building erected at site.
Source: SOW-0191.

### REQ-SOW-060-01-008 — Boundary and "by others" items

The Scope of Work shall list the explicit "by others" boundary items per SOW-0192:

- DCS integration (by others).
- Foundations (by others).
- Electrical supply to MCC (by others).

### REQ-SOW-060-01-009 — Applicable interface types

The Scope of Work shall enumerate the applicable interface types for PKG-060 (14 interface rows from INTERFACE_REGISTER):

Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

NOTE: Grading / Site Drainage / Spill Containment is absent from the 14 IFC rows for PKG-060 but present for sibling PKG-091 (3-25). Whether the omission is intentional is `TBD`.

### REQ-SOW-060-01-010 — Whole-facility integration narrative

The Scope of Work shall describe how PKG-060 integrates into the 04-25 facility and into the 03-25 Liquids Hub interface:

- Condensate transfer route to the 3-25 Liquids Hub (DBM-Deepcut SEC, line 452).
- Produced water route via new water pipeline to the 3-25 Liquids Hub (DBM-Deepcut, lines 504, 506).
- Tank farm pump module physical grouping and its relation to the tank farm electrical building (DBM lines 2816-2817).

### REQ-SOW-060-01-011 — Source-basis citations

The Scope of Work shall cite as source basis:

- Workbook Packages row 85.
- `26020-Package_Requirements.docx` package heading 15.
- Bid Doc `26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx` (location `TBD` — not locally accessible).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` (Product Pumps and Process Units sections).
- GATE-07 PROJECT_DECOMP snapshot registers.

## Standards

| Standard / Code | Relevance | Source basis |
|---|---|---|
| API-682 (mechanical seals — 14/52 seal plan) | Condensate transfer pump seal plan | SOW-0191 |
| `26020-Package_Requirements.docx` heading 15 | Governing package-requirements clause-set | PACKAGE_REGISTER (location TBD — native text not accessible) |
| 4-25 DBM (`DBM-Deepcut/4-25_Deepcut_DBM.md`) | Facility design basis | DBM file present in `_Sources/` |
| Additional regulatory / sour-service / fire & gas / drain & containment codes per OBJ-009 | Sour-service safety and compliance | OBJ-009; specific code list `TBD` until DEL-060-02 Datasheet establishes detail |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-SOW-060-01-001 | Document review against PACKAGE_REGISTER PKG-060 row |
| REQ-SOW-060-01-002 | Document review against OBJ-004 wording and PACKAGE_REGISTER ResponsibilityModel |
| REQ-SOW-060-01-003 | Document review against SOW-0191 tag list; cross-check with DBM Product Pumps subsection |
| REQ-SOW-060-01-004 | Document review against SOW-0190 process-function statements |
| REQ-SOW-060-01-005 | Document review against SOW-0192 capacity statements |
| REQ-SOW-060-01-006 | Document review against SOW-0192 driver/electrical statements |
| REQ-SOW-060-01-007 | Document review against SOW-0191 building form statement |
| REQ-SOW-060-01-008 | Document review against SOW-0192 by-others list |
| REQ-SOW-060-01-009 | Document review against INTERFACE_REGISTER 14 IFC rows for PKG-060 |
| REQ-SOW-060-01-010 | Cross-document consistency check with DBM-Deepcut narrative (condensate transfer, produced water transfer) and with sibling deliverables in PKG-060 |
| REQ-SOW-060-01-011 | Citation completeness audit of the produced Scope of Work document |

## Documentation (anticipated artifacts)

Per `_CONTEXT.md` Anticipated Artifacts:

- Package scope of work.
- Tagged equipment and package identity list.
- Package function and integration narrative.
- Responsibility assignment record.

Downstream consumers of the Scope of Work (per SCOPE_LEDGER OwnersDeliverables column):

- DEL-060-02 Package Datasheet.
- DEL-060-03 Construction Work Package.
- DEL-060-04 Vendor Engineered Equipment Package.
- DEL-060-05 Vendor Document Turnover Package.
- DEL-060-06 EPC Vendor Package Review and Acceptance.
