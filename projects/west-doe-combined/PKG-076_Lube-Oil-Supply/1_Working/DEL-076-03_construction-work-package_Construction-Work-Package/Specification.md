# Specification — DEL-076-03 Construction Work Package (Lube Oil Supply, PKG-076)

## Scope

### In scope

This Construction Work Package specifies how PKG-076 (Lube Oil Supply) is physically installed, built, inspected, turned over, and tied into the larger West Doe Deepcut facility (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER row 386). The package consists of two electric-motor-driven lube oil transfer pumps (P-9240-1 cylinder lube oil; P-9250-1 crankcase lube oil) and a horizontal split storage tank serving the Storage Tank Area of the Deepcut facility (SCOPE_LEDGER SOW-0137).

EPC Integrator scope explicitly includes (SCOPE_LEDGER SOW-0138 "By others" relative to vendor):
- Shipping the vendor-supplied package to site
- Installation of the package on piles (foundations and pile installation)
- Tie-in piping (Utility Piping; Drain / Containment interfaces — INTERFACE_REGISTER IFC-B592C2D9F7, IFC-09EA6BEDB8)
- Electrical connections (Electrical Power; Grounding / Bonding interfaces — IFC-4D53A7E70E, IFC-7117284B73)
- Mounting platform and stairs
- Area / exterior lighting integration (IFC-986D504634)
- I&C / control cabling integration (IFC-8C17CDE23B)
- Maintenance access provisions (IFC-6D43DAF029)
- Structural / foundations / supports (IFC-ACA2756AA0)

### Out of scope

- Package engineering, package design, vendor documentation, and physical equipment supply — owned by the Package Vendor (PACKAGE_REGISTER row 70 responsibility model; OBJ-004).
- Compressor frame day tanks themselves (consumers of lube oil, not part of this package) — ASSUMPTION based on SOW-0137 wording.

## Requirements

Requirements are derived from accessible decomposition-extracted source slices (heading 30 of 26020-Package_Requirements.docx as captured in SCOPE_LEDGER) and the GATE-07 Interface Register. Lower-level numerical install criteria (torque values, hydrotest pressures, area classification) are marked `TBD` pending direct access to the source .docx and EPC discipline specifications.

| ReqID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-CWP-01 | Package shall be installed on pile foundations sized for vendor-provided equipment loads. | SCOPE_LEDGER SOW-0138; INTERFACE_REGISTER IFC-ACA2756AA0 | Foundation acceptance inspection and pile completion records (see Procedure §Verification). |
| REQ-CWP-02 | Tie-in piping shall connect package suction/discharge to upstream/downstream facility utility piping per piping class TBD. | SCOPE_LEDGER SOW-0138; IFC-B592C2D9F7 | Piping inspection records; hydrotest at piping class pressure (value TBD). |
| REQ-CWP-03 | Containment and drainage provisions shall be installed to handle lube oil spills consistent with site drain/containment design. | IFC-09EA6BEDB8 | Containment inspection; drain routing verification. |
| REQ-CWP-04 | Electrical connections to the two electric-motor-driven pumps shall be installed and energized in accordance with the facility electrical basis. | SCOPE_LEDGER SOW-0137 (electric motor driven); SOW-0138 (electrical connections By Others); IFC-4D53A7E70E | Loop check; megger and continuity tests; energization checklist. |
| REQ-CWP-05 | Motors used in installation shall not be Toshiba (vendor-specified exclusion). | SCOPE_LEDGER SOW-0138 ("Driver: No Toshiba motors") | Equipment receipt inspection — motor nameplate verification. |
| REQ-CWP-06 | Grounding and bonding shall be installed for the pump skids, storage tank, and any associated piping per facility grounding basis. | IFC-7117284B73 | Ground resistance test; bonding continuity test. |
| REQ-CWP-07 | Area / exterior lighting around the lube oil package shall meet facility lighting standard for the Storage Tank Area. | IFC-986D504634 | Lighting layout walk-down. |
| REQ-CWP-08 | I&C / control cabling shall be installed and terminated to interface lube oil pump controls with the facility control system. | IFC-8C17CDE23B | Loop check; control system point-to-point verification. |
| REQ-CWP-09 | Maintenance access (platform, stairs, clearances) shall be installed to permit pump and tank maintenance. | SCOPE_LEDGER SOW-0138 (mounting platform and stairs); IFC-6D43DAF029 | Access walk-down against vendor maintenance access requirements. |
| REQ-CWP-10 | Installation shall maintain sour-service integrity (materials and joints suitable for sweet and sour service). | SCOPE_LEDGER SOW-0137 (sweet and sour service); OBJ-009 | Materials traceability; weld inspection per applicable codes (specific codes TBD — location TBD). |
| REQ-CWP-11 | A construction interface and turnover checklist shall be produced and signed off for handover to commissioning. | `_CONTEXT.md` Anticipated Artifacts; OBJ-010 | Signed turnover checklist. |
| REQ-CWP-12 | Operating and design conditions assumed during installation: low / atmospheric pressure service; ambient to heated tank temperature. | SCOPE_LEDGER SOW-0138 | Design condition cross-check during turnover. |

## Standards

Governing standards have not been fully enumerated in the locally accessible source slices. Likely-applicable standard families (ASSUMPTION pending source confirmation):

- ASME B31.3 — Process piping (ASSUMPTION; location TBD)
- Provincial Alberta safety codes for electrical (Canadian Electrical Code) (ASSUMPTION; location TBD)
- Sour-service materials standards (e.g., NACE MR0175 / ISO 15156) — implied by "sweet and sour service" classification (ASSUMPTION; SCOPE_LEDGER SOW-0137; location TBD)
- 4-25 DBM Deepcut and project regulatory/codes basis (OBJ-009 source slices in OBJECTIVE_REGISTER row 10) — referenced; deliverable-local slices not yet extracted.

Resolve specific standard citations from `_REFERENCES.md → Shared Source Root` (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-15 Regulatory, Codes, and Standards Basis) during Pass 3 enrichment.

## Verification

Verification approach is captured per requirement in the requirements table. Aggregate verification deliverables:

- Foundation/pile completion records
- Piping inspection and hydrotest records
- Electrical loop check, megger, ground resistance test records
- Controls loop check and point-to-point records
- Maintenance access walk-down report
- Signed construction interface and turnover checklist

## Documentation

Deliverable shall produce (`_CONTEXT.md` Anticipated Artifacts):

- Construction work package (master)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Supports objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (`_CONTEXT.md` Supports Objectives; OBJECTIVE_DELIVERABLE_MAP rows 308, 1222, …).
