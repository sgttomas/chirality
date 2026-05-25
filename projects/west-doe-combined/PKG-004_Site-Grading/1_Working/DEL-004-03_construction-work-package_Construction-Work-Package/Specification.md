# Specification: DEL-004-03 Construction Work Package

## Scope

This specification governs the Phase 2.2 construction work package kit for DEL-004-03, the EPC Integrator construction work package for PKG-004 Site Grading under WBS 02.

The construction work package covers the construction-facing basis for physically installing, building, inspecting, turning over, and tying the Site Grading package into the larger 03-25 facility systems. It must include the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.

Exclusions and limits:

- Issued-for-construction drawings, construction quantities, detailed grading elevations, survey control, method statements, inspection test plans, and construction sequence dates are TBD in the accessible source set.
- No separate vendor-package ownership model is inferred for PKG-004; responsibility is EPC Integrator or discipline subcontractor as assigned.
- Pipeline and third-party work outside facility tie-ins is excluded unless specifically stated as facility-side work in accepted project sources.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-004-03-001 | The CWP must identify PKG-004 as the Site Grading package, WBS 02, Civil discipline, tied to SOW-0004 and Workbook Packages row 5. | Check CWP cover sheet and package index against PACKAGE_REGISTER.csv and SCOPE_LEDGER.csv. |
| REQ-004-03-002 | The CWP must include, or explicitly reference, a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | Check deliverable table of contents against ARTIFACT_REGISTER.csv rows for DEL-004-03. |
| REQ-004-03-003 | The CWP must address the declared interfaces: Drain / Containment and Grading / Site Drainage / Spill Containment. | Check interface matrix against INTERFACE_REGISTER.csv rows IFC-FA26BF6895 and IFC-D2D12F4CA2. |
| REQ-004-03-004 | The CWP must carry the DBM civil design coverage for grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security where these are affected by site grading. | Check construction scope matrix against DBM SEC-11 Site and Civil Conditions. |
| REQ-004-03-005 | The CWP must prevent uncontrolled offsite discharge and protect process areas through surface-water management provisions supported by the current DBM basis. | Check drainage controls and turnover checklist against DBM SEC-11 Surface Water and Drainage. |
| REQ-004-03-006 | The CWP must route process-contaminated drainage to appropriate drain or containment systems rather than to surface-water discharge. | Check drain/containment tie-in checklist against DBM SEC-11 Surface Water and Drainage. |
| REQ-004-03-007 | The CWP must retain the current hydrology uncertainty: NBCC 2020 Dawson Creek IDF data is a proxy pending site-specific update, and final hydrology inputs remain a closure item. | Check assumptions/open-items register against DBM SEC-02 Site-Specific Design Data. |
| REQ-004-03-008 | The CWP must retain preliminary geotechnical status and require the final geotechnical report before foundation-related grading/foundation closure. | Check prerequisites and open-items register against DBM SEC-02 Geotechnical and Seismic Basis and SEC-11 Site and Civil Conditions. |
| REQ-004-03-009 | The CWP must account for road/access needs for construction, module delivery, operations, maintenance, emergency response, truck-loading traffic, and winter operation where affected by grading. | Check access plan and temporary/permanent road provisions against DBM SEC-11 Roads and Access. |
| REQ-004-03-010 | The CWP must identify unavailable construction details as TBD rather than treating decomposition summaries as issued construction criteria. | Review all quantities, elevations, limits, construction sequence steps, and inspection criteria for source citations or TBD status. |

## Standards

| Standard / governing content | Status in accessible sources | Application |
|---|---|---|
| NBCC | Referenced as governing civil/structural content and as basis for Dawson Creek IDF proxy. Full standard text not available in deliverable-local source set. | Use as cited standard; clause-level requirements are TBD pending standards register/source access. |
| Final geotechnical report | Required before foundation design closure; not available in current source set. | Treat as prerequisite/open item for grading/foundation closure. |
| Site data and civil drawings | Listed as governing civil/structural content; detailed drawings are not available in current deliverable source set. | Treat as required inputs before IFC CWP completion. |
| Surface-water management basis | DBM SEC-11 provides governing requirements. | Apply to drainage, containment segregation, and turnover checks. |
| Environmental/regulatory content | DBM states BCER permits, water regulations, consultation/notification, and waste management permit as governing topics; details remain partially TBD. | Carry as coordination/open items where construction grading affects permit or discharge controls. |

## Verification

| Verification area | Acceptance basis |
|---|---|
| Identity and scope | DEL-004-03, PKG-004, SOW-0004, WBS 02, Civil, Workbook row 5 all appear consistently. |
| Interface completeness | Drain / Containment and Grading / Site Drainage / Spill Containment are included in the CWP interface checklist. |
| Source traceability | Each non-trivial construction requirement cites Gate 7 snapshot registers or DBM SEC-02/SEC-11 source slices. |
| Missing construction data | Unsupported values remain marked TBD. |
| Hydrology and geotechnical maturity | Proxy hydrology and preliminary geotechnical status are visible as open constraints. |
| Cross-document consistency | Datasheet attributes, specification requirements, guidance considerations, and procedure checks use the same package identity, interfaces, and TBD treatment. |

## Documentation

Required CWP documentation for this deliverable:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Interface matrix covering Drain / Containment and Grading / Site Drainage / Spill Containment.
- Assumptions and open-items register for final hydrology, final geotechnical report, civil drawings, workface limits, construction quantities, and inspection/turnover criteria.

Source basis:

- DELIVERABLE_REGISTER.csv, DEL-004-03 row.
- PACKAGE_REGISTER.csv, PKG-004 row.
- SCOPE_LEDGER.csv, SOW-0004 row.
- INTERFACE_REGISTER.csv, PKG-004 rows.
- ARTIFACT_REGISTER.csv, DEL-004-03 rows.
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Construction Scope Summary, SEC-02, and SEC-11.
