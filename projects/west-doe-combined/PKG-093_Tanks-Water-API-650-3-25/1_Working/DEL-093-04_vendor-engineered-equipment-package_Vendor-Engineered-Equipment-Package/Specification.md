# Specification — DEL-093-04 Vendor Engineered Equipment Package (Tanks, Water (API 650) 3-25)

## Scope

This Specification governs the **Package Vendor's** engineered design and fabricated physical equipment for `PKG-093` (Tanks, Water (API 650) 3-25), produced from the EPC Scope of Work (`DEL-093-01`) and Package Datasheet (`DEL-093-02`).

**In scope (Package Vendor):**
- Detailed mechanical engineering and design of the API 650 Modified atmospheric produced-water storage tanks listed under SOW-0230, SOW-0231, SOW-0232.
- Fabrication, supply, and shop testing of the physical equipment package.
- Vendor design basis and datasheets supporting the engineered equipment.
- Vendor-side integration interfaces to facility VRU suction, blanket gas (LP fuel gas), insulation/heating, internal coating, and skim system.

**Out of scope (carried by others / EPC Integrator):**
- Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. (per SOW-0232 "By others").
- Construction Work Package (`DEL-093-03`).
- Vendor document turnover (`DEL-093-05`).
- EPC integration review and acceptance evidence (`DEL-093-06`).
- Broader 03-25 Liquids Hub produced-water tank population beyond the SOW-0230/0231 Item No. 1 tanks and the SOW-0232 Item No. 2 scope (ASSUMPTION; see Datasheet).

## Requirements

| Req-ID | Statement | Authority | Notes |
|---|---|---|---|
| REQ-093-04-001 | The vendor engineered package shall comprise two (2) 3,800 bbl Sweet Produced Water Storage Tanks, tagged `TK-9060-2` and `TK-9070-2` (Item No. 1). | `SCOPE_LEDGER.csv` SOW-0230 (26020-Package_Requirements.docx package heading 45, Basic scope) | Mandatory item count and tag identity. |
| REQ-093-04-002 | Item No. 2 tank(s) shall be supplied per SOW-0232; quantity, capacity, and process duty `TBD` from source. | `SCOPE_LEDGER.csv` SOW-0232 | TBD pending source clarification. |
| REQ-093-04-003 | Tanks shall be designed and fabricated to API 650 Modified. | SOW-0231; `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | "Modified" clauses in `26020-Package_Requirements.docx` heading 45; clause-level location TBD. |
| REQ-093-04-004 | Tank pressure class shall be atmospheric; design/test pressure shall be 32 oz. | SOW-0232 | Interpretation of "32 oz test pressure" (design vs hydrotest) flagged in Guidance Conflict Table CONF-093-04-03. |
| REQ-093-04-005 | Tank design temperature shall accommodate -40 °C (min) and 60 °C (max). | SOW-0232; `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (line 96) | Materials/fittings qualified to -40 °C MDMT. ASSUMPTION: MDMT equals minimum ambient unless detailed design overrides. |
| REQ-093-04-006 | Each tank shall be externally insulated and externally heated to prevent freezing. | SOW-0231 | Heat-tracing/insulation interface to EPC scope. |
| REQ-093-04-007 | Each tank shall be blanketed with LP fuel gas for winter vacuum prevention per API 2000. | SOW-0231 | API 2000 edition `location TBD` (Guidance CONF-093-04-05). |
| REQ-093-04-008 | Each tank shall have a Devchem 253 internal coating on floors, walls, and roof. | SOW-0231; `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | Coating qualified for produced-water service. |
| REQ-093-04-009 | Each tank shall include a Kennilworth-type HCL float skim system, one per tank, with float design SG ≤ 0.67. | SOW-0231 | Skim system is part of vendor equipment scope. |
| REQ-093-04-010 | Service fluid is non-sour produced water. | SOW-0231 | NACE sour-service provisions are NOT triggered for Item No. 1. |
| REQ-093-04-011 | Item No. 1 design flow shall accommodate 15,300 kg/h, 3,584 Am³/d from the compressor station plus 240 Am³/d from cryo. | SOW-0232 | Item No. 2 design flow `TBD`. |
| REQ-093-04-012 | Item No. 1 operating temperature shall be 5 °C; Item No. 2 operating temperature `TBD`. | SOW-0232 | |
| REQ-093-04-013 | Tank design SG shall be 1.25 TBC (per facility basis); pump fluid SG basis is 1.18; the SG discrepancy shall be closed during detailed design. | `3-25_Comp_and_Liquids_DBM.md` §SEC-03 (line 176), §SEC-06 (line 421) | See Guidance CONF-093-04-01. |
| REQ-093-04-014 | Vendor equipment scope shall exclude foundations, on-site mounting, electrical/instrumentation, platforms, and staircase. | SOW-0232 ("By others") | EPC Integrator scope boundary. |
| REQ-093-04-015 | Vendor shall produce a design basis and datasheet set supporting the engineered equipment. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row DEL-093-04 | Documentation accompanies physical scope; turnover register is `DEL-093-05`. |
| REQ-093-04-016 | Vendor design shall provide a compatible interface to the facility VRU suction for tank vapours. | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (lines 436, 422) | Interface coordination only; VRU package is not vendor scope. |

## Standards

| Standard | Application | Location |
|---|---|---|
| API 650 (Modified) | Atmospheric storage tank design and fabrication | SOW-0231; `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421); "Modified" clause set location TBD |
| API 2000 | Tank vent sizing / vacuum protection (blanket-gas basis) | SOW-0231 (edition location TBD) |
| `26020-Package_Requirements.docx` heading 45 | Source package requirements document (mechanical packages) | Local DOCX slice not extracted; SOW rows used as proxy |

## Verification

| Req-ID | Verification Approach |
|---|---|
| REQ-093-04-001, 002 | Bill of materials / equipment list check against SOW rows; tag verification. |
| REQ-093-04-003 | Vendor design documentation review against API 650 Modified clauses; weld, materials, and details certification. |
| REQ-093-04-004 | Shop hydrostatic / leak test record; vent and vacuum-protection sizing calculation review. |
| REQ-093-04-005 | Material MTRs for MDMT; impact testing records as required. |
| REQ-093-04-006 | Insulation/heating design documents; thermal calculation; vendor heater specification cross-check. |
| REQ-093-04-007 | Blanket-gas regulator specification and API 2000 sizing calculation. |
| REQ-093-04-008 | Coating Procedure Qualification Record (PQR); coating thickness and adhesion inspection records. |
| REQ-093-04-009 | Skim system fabrication and float SG verification. |
| REQ-093-04-010 | Material selection rationale; documentation confirming sour-service NACE provisions are NOT triggered. |
| REQ-093-04-011, 012 | Process design calculation showing nozzle sizing, overflow, and level basis matches the stated flows. |
| REQ-093-04-013 | Detailed-design memo reconciling tank design SG vs pump fluid SG. |
| REQ-093-04-014 | Interface drawing review confirming "by others" items are excluded from vendor BOM. |
| REQ-093-04-015 | Document register check (vendor datasheet set + design basis). |
| REQ-093-04-016 | Interface point list / P&ID extract showing tank vapour outlet routing to facility VRU suction. |

## Documentation

Vendor shall deliver the engineered package documentation set required for EPC review (`DEL-093-06`) and turnover (`DEL-093-05`):

- Vendor design basis.
- Vendor datasheets for each tank (Item No. 1 set; Item No. 2 TBD).
- General arrangement / outline drawings.
- API 650 Modified design calculations and weld/material details.
- Vent and vacuum-protection (API 2000) calculations.
- Coating procedure qualification and inspection plan (Devchem 253).
- Insulation/heating design documents.
- Shop fabrication and test records (hydrotest, NDE, coating).
- Material certifications (MTRs) for plate, nozzles, fittings.
- Skim system documentation (Kennilworth-type; float SG ≤ 0.67).
- Interface drawings: VRU, blanket gas, level instrumentation, vacuum-truck connection.

The detailed deliverable list is finalized via `DEL-093-05_vendor-document-turnover-package`.
