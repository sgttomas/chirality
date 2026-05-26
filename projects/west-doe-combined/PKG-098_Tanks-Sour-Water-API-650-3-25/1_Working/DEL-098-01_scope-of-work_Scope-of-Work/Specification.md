# Specification — DEL-098-01 Scope of Work

> Normative specification for the EPC Integrator Scope of Work for PKG-098 Tanks, Sour Water (API 650) 3-25.

## Scope

### Included

The Scope of Work shall define and bound the EPC Integrator package scope for PKG-098, comprising:

1. Three (3) × 3,800 bbl Sour Produced Water Storage Tanks — TK-9030-2, TK-9040-2, TK-9050-2 (Item 1). [Source: Package Requirements §`26020-03-PT-19-007` Major Included Equipment]
2. Two (2) × 3,800 bbl Sour Inlet Produced Water Storage Tanks — TK-9010-2, TK-9020-2 (Item 2). [Source: same]
3. Two (2) × 3,800 bbl Produced Water Storage Tanks — TK-9010-1, TK-9020-1 (Item 3). [Source: same]

The Scope of Work shall state, for the equipment above:
- Package function and process role within the 03-25 Liquids Hub produced-water subsystem. [DBM §"produced-water system"; §"liquids hub equipment basis"]
- Tagged equipment and package identity list (per Datasheet).
- Source basis (`26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx`) and EPC integration narrative.
- Boundaries between the package vendor scope and EPC/by-others scope.
- Responsibility assignment record for interfaces requiring EPC-vs-vendor allocation.

Coverage of scope items: SOW-0221, SOW-0222, SOW-0223, SOW-0224 (per `OBJECTIVE_SCOPE_MAP.csv` and `_CONTEXT.md`).

### Excluded (By Others)

Per Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items: "By others: Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase etc." The Scope of Work shall record these exclusions explicitly.

## Requirements

R-1. The Scope of Work shall identify each tank by tag, quantity, and stated process function as listed in the authoritative package source. [Source: Package Requirements §`26020-03-PT-19-007` Major Included Equipment]

R-2. The Scope of Work shall require design and fabrication to **modified API 650**. [Source: Package Requirements §`26020-03-PT-19-007` Major Included Equipment; DBM §"produced-water system"]

R-3. The Scope of Work shall record the following common technical basis (applicable to Items 1–3 per source):
- Internal coating: Devchem 253 on floor, walls, and roof.
- External insulation with electric heating.
- Kennilworth-type HCL float skim system, one per tank.
[Source: Package Requirements §`26020-03-PT-19-007` Major Included Equipment]

R-4. The Scope of Work shall record the operating and design envelope from the source:
- Operating: Atmospheric pressure; 10 °C operating temperature (Items 1 and 3); operating temperature TBD for Item 2.
- Design: 32 oz test pressure; -40 °C minimum and 60 °C maximum design temperature.
[Source: Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items]

R-5. The Scope of Work shall identify capacity / design throughput by reference to Appendix A of the source RFQ. Numerical values are not stated in the locally accessible source slice → carry forward as **location TBD** until Appendix A is accessible. [Source: Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items]

R-6. The Scope of Work shall enumerate the package's physical interface applicability matrix exactly as stated in the source (Process Piping: Yes; Utility Piping: No; Relief/Flare/Vent: Yes; Drain/Containment: Yes; Electrical Power: No; Area/Exterior Lighting: Yes; EHT: No; Grounding/Bonding: Yes; Cathodic Protection: Yes; I&C/Control Cabling: Yes; Communications/Network: No; Building HVAC/Services: No; Fire & Gas/Safety Systems: No; Maintenance Access: No; Grading/Site Drainage/Spill Containment: Yes; Structural/Foundations/Supports: Yes; Product Loading: No; Pipeline/Pigging: No). The interface source identifier `26020-Packages_Interfaces.3.xlsx` shall be carried. [Source: Package Requirements §`26020-03-PT-19-007` Physical Interface Summary; per source the source workbook is not locally accessible → location TBD for cell-level evidence; column M (row 93) cited for Area/Exterior Lighting]

R-7. The Scope of Work shall declare scope exclusions consistent with Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items (foundations, on-site mounting, E&I, platforms, staircases — by others).

R-8. The Scope of Work shall record the vendor engineering deliverables families required of the package vendor as enumerated in Package Requirements §`26020-03-PT-19-007` Vendor Engineering Deliverables: Core vendor documents (PRQ-/DOC-/QLT-/PRQ- series), Core package engineering (MEC-001/002/003/006/014/016/017/018/021/022/023/024/025), Storage tanks (MEC-005, MEC-011), Relief/flare/vent design (PRO-014/015/016/017/018), Process piping interfaces (PRO-008; PIP-003/004/006/007/008/009/017/018/024/025/028), Drainage/containment interfaces (PRO-023, CIV-014), Electrical/lighting/EHT/grounding (ELE-017/012/019), Cathodic protection interfaces (PLN-015/016), Instrumentation and controls interfaces (INS-002/003/005/006/008/009/010/011/016/017/018/025/029; CTL-003/005/006/026), Structural/foundations/supports/access (STR-001/002/004/005/006/011/012/013/014/020), Civil grading/spill containment interfaces (CIV-003/004/015/019). [Source: Package Requirements §`26020-03-PT-19-007` Vendor Engineering Deliverables]

R-9. The Scope of Work shall identify the package source basis as `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx`. [Source: Package Requirements §`26020-03-PT-19-007` Location/Status table]

R-10. The Scope of Work shall record the responsibility assignment between EPC Integrator and Package Vendor for each "Yes" interface in R-6. The specific assignment rules are not stated in the accessible source slice → mark **ASSUMPTION** when proposed, and resolve through DEL-098-02 (Package Datasheet) and Interface Coordination Notes (currently TBD per source). [Source: Package Requirements §`26020-03-PT-19-007` Interface Coordination Notes = "TBD."]

R-11. The Scope of Work shall integrate the package into the facility narrative by reference to the 03-25 Liquids Hub produced-water subsystem and VRU/H2O2 coordination boundaries. [Source: DBM §"facility receives Doe field sour wellstream fluids…"; §"Liquids Hub also receives stabilized condensate…"; §"produced-water system"]

## Standards

| Standard | Applicability | Status / Source |
|---|---|---|
| API 650 (Modified) | Tank design and fabrication | Cited in Package Requirements §`26020-03-PT-19-007` Major Included Equipment; clause-level requirements not in locally accessible source slice → **location TBD** for clause references |
| Provincial regulatory basis (BC) for produced-water handling | Facility integration context | DBM §"Province of British Columbia owns water resources…"; **ASSUMPTION** for direct applicability to package scope deliverables |
| Sour-service material requirements | Cited at facility level | DBM §"Pressure vessels shall be designed for the applicable pressure class, sour-service requirements…"; ASSUMPTION that the same sour-service envelope applies to tank shell material; specific NACE/ISO references not in accessible slice → **location TBD** |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1, R-3, R-4 | Cross-check Scope-of-Work text against the source slice; verify each tank tag, quantity, and design condition appears verbatim or with traceable transformation. |
| R-2 | Confirm "modified API 650" language present; flag any deviation to "API 650" unmodified as non-conformance. |
| R-5 | Confirm capacity/throughput is either (a) populated from Appendix A when accessible, or (b) carried as `location TBD` with explicit reference to Appendix A. |
| R-6 | Match interface applicability matrix line-by-line with source table. |
| R-7 | Confirm exclusions ("by others") clause is present and unmodified. |
| R-8 | Audit Vendor Engineering Deliverables list against source enumeration; flag additions/omissions. |
| R-9 | Confirm Source Basis (`26020-03-PT-RFQ-19-007`) is cited. |
| R-10 | Confirm responsibility assignment table exists and labels unresolved assignments as TBD pending Interface Coordination Notes resolution. |
| R-11 | Confirm integration narrative cites the Liquids Hub produced-water subsystem with DBM source attribution. |

## Documentation

Anticipated artifacts to be produced as part of this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Package scope of work (narrative).
- Tagged equipment and package identity list (table form, mirroring Datasheet identification).
- Package function and integration narrative.
- Responsibility assignment record.

Cross-reference: DEL-098-02 (Package Datasheet) carries the technical interface evidence; DEL-098-03 (Construction Work Package) describes installation/tie-in; DEL-098-04/05 are vendor production-unit deliverables; DEL-098-06 is EPC vendor package review and acceptance.
