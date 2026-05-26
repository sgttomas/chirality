# Specification: EPC Vendor Package Review and Acceptance

## Scope

This specification defines the EPC Integrator's obligations to review, accept, and turn over the Inlet Separators vendor package (PKG-083; equipment V-1600-2 and V-1700-2) into the West DOE facility. It covers vendor document review, integration acceptance, factory/shop test and inspection witnessing/review, and handoff/turnover readiness against the EPC Scope of Work (DEL-083-01), Package Datasheet (DEL-083-02), Construction Work Package (DEL-083-03), Vendor Engineered Equipment Package (DEL-083-04), and Vendor Document Turnover Package (DEL-083-05).

Excluded from this deliverable:
- Package vendor's internal engineering and design execution (owned by DEL-083-04).
- Vendor documentation production itself (owned by DEL-083-05).
- Facility-level commissioning beyond the package handoff boundary (TBD; not bounded in accessible sources).

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-083-06-01 | The EPC Integrator shall maintain a vendor document review and comment log capturing each vendor-issued document, review cycle, comments raised, vendor responses, and disposition. | ARTIFACT_REGISTER.csv, ART-AE2840AE44 |
| REQ-083-06-02 | The EPC Integrator shall verify that the vendor package delivers the required package deliverables: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. | 3-25_Comp_and_Liquids_DBM.md, Mechanical Packages |
| REQ-083-06-03 | The EPC Integrator shall verify that each delivered separator package matches the per-separator design basis: 40 MMSCFD gas; 556 m3/d condensate; 1,800 m3/d produced water; 2,743 mm diameter; 12,191 mm S/S length; ANSI 600#; 4,963 kPag design pressure; approximately 38 m3 slug handling; Devchem 253 internal coating. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| REQ-083-06-04 | The EPC Integrator shall confirm that internals are supplied as specified: Devchem 253 coating, manually adjustable weir, vertical/horizontal high-performance mesh/vane mist eliminators, and de-sanding provisions. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| REQ-083-06-05 | The EPC Integrator shall confirm flow distribution and controls: symmetric inlet piping; at least two parallel inlet pressure-control valves per package with balanced globe hardened trim and dP <= 5 psid; at least two parallel produced-water level-control valves per package. | 3-25_Comp_and_Liquids_DBM.md, Flow Distribution and Controls |
| REQ-083-06-06 | The EPC Integrator shall verify that materials, sour-service ratings, and cold-climate design (-40 deg C ambient) of the vendor package comply with the facility design basis. | 3-25_Comp_and_Liquids_DBM.md, Site Basis; Pressure Vessels |
| REQ-083-06-07 | The EPC Integrator shall verify integration at each applicable interface type: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv, PKG-083 |
| REQ-083-06-08 | The EPC Integrator shall review and accept factory/shop test and inspection evidence supplied by the vendor; specific FAT/inspection scope is TBD pending DEL-083-02 / DEL-083-04 issuance. | ARTIFACT_REGISTER.csv, ART-30486BD773; location TBD |
| REQ-083-06-09 | The EPC Integrator shall complete a vendor package acceptance and turnover checklist documenting acceptance of the vendor scope and readiness for facility integration. | ARTIFACT_REGISTER.csv, ART-27FC8B869F |
| REQ-083-06-10 | The EPC Integrator shall record the disposition of all TBD/TBC items raised during the vendor design basis review (e.g., normal high pressure TBC; building extent TBD; downstream methanol disposition TBD; inlet temperature reconciliation). | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation; Slug and Flowback Basis |
| REQ-083-06-11 | ASSUMPTION: The EPC Integrator shall coordinate handoff with DEL-083-05 (Vendor Document Turnover Package) so that turnover evidence references the same vendor document set; explicit ordering rule not stated in accessible sources. | _CONTEXT.md; sibling DEL-083-05 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx (heading 36) | Authoritative package requirements set for PKG-083 vendor package. | location TBD (.docx not locally readable as text) |
| 26020-02-PT-RFQ-17-003 Inlet Separators (RFQ basis) | Original RFQ vendor scope reference cited in PACKAGE_REGISTER. | location TBD (Bid Docs/Budgetary; not locally accessible as text) |
| Sour-service pressure-vessel codes | Pressure vessels shall be designed for the applicable pressure class, sour-service requirements, corrosion allowance, coating, manway access, internals removal, drainage, venting, inspection. Specific code citations TBD in current source slice. | 3-25_Comp_and_Liquids_DBM.md, Pressure Vessels; location TBD |
| NBCC / cold-climate basis | -40 deg C ambient minimum used as design basis where not superseded by process/vendor conditions. | 3-25_Comp_and_Liquids_DBM.md, Site Basis |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-083-06-01 | Inspection of review log artifact; sample audit of comment-to-disposition traceability. |
| REQ-083-06-02 | Document-by-document checklist against required package deliverable list; close-out only when each is received and reviewed. |
| REQ-083-06-03 | Review of vendor equipment datasheets against the per-separator basis table; deviation log raised for any departure. |
| REQ-083-06-04 | Review of internals general-arrangement drawings and material certifications. |
| REQ-083-06-05 | Review of P&ID extracts, control valve datasheets, and control narrative against the parallel-valve and dP requirements. |
| REQ-083-06-06 | Review of materials selection diagram, coating schedule, and cold-climate design package (heat tracing, building extent, instrument suitability). |
| REQ-083-06-07 | Interface-by-interface checklist using INTERFACE_REGISTER PKG-083 entries; signed tie-in list. |
| REQ-083-06-08 | Witness or review FAT records, hydrotest reports, NDE records, and shop inspection reports as supplied. |
| REQ-083-06-09 | Completed acceptance/turnover checklist signed by EPC Integrator with Package Vendor input. |
| REQ-083-06-10 | TBD/TBC disposition log appended to acceptance checklist. |
| REQ-083-06-11 | Cross-reference handoff record with DEL-083-05 turnover index. |

## Documentation

- Vendor document review and comment log (ART-AE2840AE44).
- Vendor package acceptance and turnover checklist (ART-27FC8B869F).
- Factory/shop test and inspection evidence (ART-30486BD773).
- TBD/TBC disposition log (subordinate to acceptance checklist).
- Signed interface tie-in list (subordinate to acceptance checklist).
