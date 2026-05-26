# Procedure — DEL-047-04 Vendor Engineered Equipment Package (VRU 4-25)

This Procedure addresses the production of the vendor engineered equipment package (engineering through fabrication, factory verification, and shipment readiness). Site installation and operation are covered by DEL-047-03 Construction Work Package and downstream operations procedures and are referenced only at handoff.

## Prerequisites

- EPC Scope of Work (DEL-047-01) accepted and available. (Source: DELIVERABLE_REGISTER.csv.)
- EPC Package Datasheet (DEL-047-02) accepted and available, including resolution of CONF-01 (motor rating) and CONF-02 (single vs individual buildings) before vendor design freeze. (Source: Guidance.md Conflict Table.)
- Access to authoritative source documents: 26020-Package_Requirements.docx (package heading 2) and 26020-01-PT-RFQ-12-002_VRU_2_R0.docx. CURRENTLY MISSING in deliverable-local reference set (location TBD). (Source: _REFERENCES.md; PACKAGE_REGISTER.csv "Word Source Basis".)
- DBM 4-25 sections: "Vapour Recovery Unit" and "Interfaces, Controls, Safeguards, and Open Design Development" reviewed. (Source: DBM-Deepcut/4-25_Deepcut_DBM.md.)
- Applicable sour-service materials standard and Canadian pressure-equipment / electrical / area-classification standards identified. (ASSUMPTION; location TBD.)
- Resolution status of DBM-listed open VRU design items: motor driver rating, driver speed confirmation, VRU gas-source flows, MAWP and design temperatures, suction scrubber density/capacity review, cooler temperature-control requirements, VRU suction header to flare valve capacity. (Source: DBM 4-25, "Interfaces, Controls, Safeguards, and Open Design Development".)
- Declared upstream and downstream dependencies confirmed in _DEPENDENCIES.md (currently none declared; relationships above are implicit). (Source: _DEPENDENCIES.md.)

## Steps

1. **Receive and align inputs.** Receive the EPC Scope of Work and Package Datasheet. Reconcile to DBM 4-25 VRU design parameters; raise discrepancies (including any unresolved CONF-01, CONF-02, CONF-03 items) through the project interface process. (Source: DBM 4-25; Guidance Conflict Table.)
2. **Develop vendor package design basis.** Produce the vendor package design basis, including service definition (sour, lead-lag 2 x 100% VRU), design pressures (0.9 kPag suction, 483 kPag discharge), per-train capacity (1.5 MMSCFD TBC), composition, MAWP basis (≥ 552 kPag 1st discharge, ≥ 1,034 kPag 2nd discharge), and materials philosophy. (Source: DBM 4-25.) TBD items remain TBD; do not assign values absent source backing.
3. **Issue vendor datasheet set.** Issue datasheets for compressor (Ro-Flo 17S/217M two-stage rotary vane), 4,000 V VFD motor (rating per CONF-01 resolution), suction scrubbers, intercooler/aftercooler with warm-air recirculation louvers, recycle valve, make-up gas regulator, blowdown valves, mechanical seal system, controls, and building/skid. (Source: DBM 4-25.)
4. **Engineer controls and safeguards.** Implement the inlet-pressure setpoint actions (1/2/2.5/3/5/8/16 oz) per REQ-18; configure capacity-control recycle valve per REQ-5; configure make-up/blanket gas regulator per REQ-19; route package blowdown to LP flare per REQ-20; route primary seal vent to LP flare per REQ-7; provide manual sweet-gas purge connection per REQ-21. (Source: Specification.md; DBM 4-25.)
5. **Engineer interfaces.** Define interface terminations consistent with PKG-047 applicable interface types (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). Provide tie-in geometry, loading, and signal lists for EPC Integrator integration. (Source: PACKAGE_REGISTER.csv PKG-047.)
6. **Engineer building/structural and HVAC** per CONF-02 resolution (single building vs two individual buildings), including area classification and Fire & Gas zoning consistent with sour service. (Source: PACKAGE_REGISTER.csv; DBM 4-25.) ASSUMPTION pending CONF-02 resolution.
7. **Procure and fabricate** the package mechanical, electrical, and instrumentation components against approved datasheets and the design basis. Maintain MTR/certification chain for sour-service wetted parts. (ASSUMPTION; standards location TBD.)
8. **Factory assembly and pre-test inspection.** Complete package assembly; perform pre-test inspection covering fit-up, painting/coating, tagging, and termination point conformance. (Standard vendor practice; location TBD.)
9. **Factory testing.** Execute the verification matrix in Specification.md, including hydrostatic/pressure tests, performance/capacity test at design conditions, recycle valve sizing demonstration, seal barrier-fluid system functional test, VFD turndown demonstration, blowdown routing functional, and inlet-pressure setpoint logic functional. (Source: Specification.md Verification section.)
10. **Resolve test exceptions.** Document any deviations; reissue affected datasheets and retest as required. Items not resolvable from drafts or source remain TBD and shall be raised for project ruling.
11. **Prepare shipment package.** Preserve, package, and label the equipment for shipment. (Detailed shipping/preservation procedure TBD; defer to vendor practice and DEL-047-05 turnover content.)
12. **Handoff to DEL-047-03 / DEL-047-06.** Transfer the physical equipment package and design basis/datasheet set to the EPC Integrator for installation (DEL-047-03 Construction Work Package) and review/acceptance (DEL-047-06 EPC Vendor Package Review and Acceptance). Vendor documentation is handled under DEL-047-05 Vendor Document Turnover Package. (Source: DELIVERABLE_REGISTER.csv.)

## Verification

- All items in Specification.md "Verification" table executed and documented (capacity, MAWP, recycle valve sizing, seal integrity, setpoint logic, sour-service materials certification, intercooler condensation handling, VFD turndown, blowdown routing, interface conformance).
- All applicable inlet-pressure setpoint actions demonstrated functionally (REQ-18).
- Each interface type listed for PKG-047 verified by walk-down against the package as built (REQ-23).
- Open DBM design items consumed by this package (motor rating, driver speed, MAWP/temperatures, suction scrubber density/capacity, cooler temperature control, suction-to-flare valve capacity) closed or formally carried forward with documented status.
- All TBD items in the four documents either closed with source citation or escalated for human ruling.

## Records

- Vendor package design basis document.
- Vendor datasheet set (compressor, motor/VFD, scrubbers, coolers, valves, seals, controls, building/skid).
- Materials test reports (MTRs) for sour-service wetted components.
- Factory test reports for hydrostatic/pressure, performance, recycle valve, seal barrier-fluid, VFD turndown, blowdown, setpoint logic, and interface walk-downs.
- Punch list and deviation log with disposition.
- Shipment release record.

Vendor document register and submittals as turnover records are produced under DEL-047-05 Vendor Document Turnover Package; this Procedure produces only the engineering and factory-verification records listed above. (Source: DELIVERABLE_REGISTER.csv DEL-047-05.)
