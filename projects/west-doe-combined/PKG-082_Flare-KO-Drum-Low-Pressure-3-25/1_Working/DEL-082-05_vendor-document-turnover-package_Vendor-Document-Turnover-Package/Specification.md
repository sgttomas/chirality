# Specification — DEL-082-05 Vendor Document Turnover Package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-082 Flare KO Drum (Low Pressure) 3-25`. The deliverable is a Package Vendor responsibility with EPC Integrator interface/integration review (ref. `_CONTEXT.md`).

**In scope:**
- Vendor document register for the LP flare KO drum package (`V-3900-2`) and transfer pump (`P-3900-2`).
- Vendor document submittals across the full source-enumerated artifact list (see `Datasheet.md`, Construction section).
- Source-required vendor documentation rows captured as artifacts/evidence.
- Turnover records: Manufacturing Record Book / Vendor Data Book, FAT/SAT records, IOM, as-built drawings.
- EPC Integrator review of submittals against the EPC Scope of Work, Package Datasheet, and Construction Work Package.

**Out of scope:**
- LP flare stack engineering and turnover documentation (boundary at KO drum outlet flange per source). [Source: 26020-Package_Requirements.docx §26020-02-PT-17-002 Scope Notes]
- Production of separate deliverables for individual source vendor-document rows; those rows remain artifacts/evidence within this single deliverable (ref. `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv DEL-082-05 row).
- Engineering, fabrication, and supply of the physical equipment (covered by `DEL-082-04 Vendor Engineered Equipment Package`).
- EPC acceptance gating (covered by `DEL-082-06 EPC Vendor Package Review and Acceptance`).

## Requirements

| ReqID | Requirement | Basis |
|---|---|---|
| REQ-082-05-001 | Vendor SHALL produce and maintain a Vendor Document Index (`PRQ-009`) listing every controlled submittal for the package. | Source: 26020-Package_Requirements.docx §26020-02-PT-17-002 Vendor Engineering Deliverables (Core vendor documents) |
| REQ-082-05-002 | Vendor SHALL apply a Vendor Document Control Procedure (`DOC-008`) governing revision, transmittal, and acceptance workflow. | Source: same |
| REQ-082-05-003 | Vendor SHALL submit a Supplier Quality Plan (`QLT-006`) and Inspection and Test Plan (`QLT-003`) prior to fabrication activities subject to hold/witness points. | Source: same |
| REQ-082-05-004 | Vendor SHALL submit Material Test Reports/Certificates (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021`) as part of turnover. | Source: same |
| REQ-082-05-005 | Vendor SHALL submit a Logistics / Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`), and Final Vendor Data Book (`PRQ-016`). | Source: same |
| REQ-082-05-006 | The submittal set SHALL include the source-enumerated engineering documents for: core package engineering (MEC-001/002/003/006/014/016/017/018/021/022/023/024/025), rotating equipment/pumps (MEC-004/007/019, PRO-013, ELE-011), static pressure equipment (MEC-005/009, REG-022), and relief/flare/vent design (PRO-014/015/016/017/018). | Source: same |
| REQ-082-05-007 | The submittal set SHALL include process piping interface documents (PRO-008, PIP-003/004/006/007/008/009/017/018/024/025/028) and drainage/containment interface documents (PRO-023, CIV-014). | Source: same |
| REQ-082-05-008 | The submittal set SHALL include electrical, lighting, EHT, and grounding documents (ELE-002/003/014/015/016/020/027/028/029/030/017/018/012/019; PIP-020/021). | Source: same |
| REQ-082-05-009 | The submittal set SHALL include instrumentation and controls interface documents (INS-002/003/005/006/008/009/010/011/016/017/018/025/029; CTL-003/005/006/026). | Source: same |
| REQ-082-05-010 | The submittal set SHALL include structural, foundations, supports, and access documents (STR-001/002/004/005/006/011/012/013/014/020). | Source: same |
| REQ-082-05-011 | The Pressure Equipment Registration Package (`REG-022`) SHALL be submitted for the LP flare KO drum vessel `V-3900-2`. | Source: 26020-Package_Requirements.docx §26020-02-PT-17-002 (Static pressure equipment) + Major Included Equipment |
| REQ-082-05-012 | Boundary documentation (P&IDs, tie-in lists) SHALL show the package boundary at the KO drum outlet flange; LP flare stack documents are excluded. | Source: 26020-Package_Requirements.docx §26020-02-PT-17-002 Scope Notes / Open Items |
| REQ-082-05-013 | Blowdown valve specification details SHALL be confirmed and the corresponding instrument/valve data sheets (INS-017, INS-016, PIP-018) revised during detailed engineering. | Source: 26020-Package_Requirements.docx §26020-02-PT-17-002 Scope Notes / Open Items ("Blowdown valve details require confirmation during detailed engineering") |
| REQ-082-05-014 | All applicable physical interface types marked "Yes" in the source interface table SHALL be supported by submitted documents (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Area/Exterior Lighting; EHT; Grounding/Bonding; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports). | Source: 26020-Package_Requirements.docx §26020-02-PT-17-002 Physical Interface Summary |
| REQ-082-05-015 | EPC Integrator SHALL perform interface/integration review of each transmittal; review records (review log entries, comments, dispositions) feed `DEL-082-06`. | Basis: `_CONTEXT.md` ResponsibleParty; ASSUMPTION on the precise review workflow (governing EPC procedure not locally accessible — location TBD). |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Provincial pressure equipment registration regime (REG-022 invocation implies jurisdictional pressure-vessel code; likely ABSA/ASME Section VIII for a Western-Canada site) | LP flare KO drum `V-3900-2` registration | **location TBD** (specific code citation not present in accessible source slice) — ASSUMPTION |
| Project EPC documentation control standard | Governs vendor document transmittal interface | **location TBD** |
| Project FAT/SAT acceptance criteria | Governs FAT/SAT documents (MEC-021/022; ELE-029/030) | **location TBD** |

## Verification

| ReqID | Verification Method | Evidence Document(s) |
|---|---|---|
| REQ-082-05-001 | EPC review of submitted index | `PRQ-009` Vendor Document Index |
| REQ-082-05-002 | EPC review of procedure document | `DOC-008` Vendor Document Control Procedure |
| REQ-082-05-003 | EPC review and witness/hold-point execution per ITP | `QLT-006`, `QLT-003` |
| REQ-082-05-004 | Turnover review against ITP and ship-loose list | `QLT-013`, `QLT-020`, `QLT-021` |
| REQ-082-05-005 | Logistics review at shipment; SPIR review at turnover | `PRQ-013`, `PRQ-015`, `PRQ-016` |
| REQ-082-05-006 to 010 | Completeness check of submittal set against Vendor Document Index | Each enumerated document |
| REQ-082-05-011 | Jurisdictional registration acceptance | `REG-022` |
| REQ-082-05-012 | Drawing review confirming boundary at KO drum outlet flange | P&IDs (`PRO-008`), Tie-In List (`PIP-004`) |
| REQ-082-05-013 | Detailed-engineering close-out of TBD item | Updated `INS-017`/`INS-016`/`PIP-018`; resolution entry in `MEMORY.md` |
| REQ-082-05-014 | Cross-check submitted documents against source interface "Yes" rows | Interface coverage matrix |
| REQ-082-05-015 | EPC review log evidence in `DEL-082-06` | EPC review log |

## Documentation

The anticipated artifacts for this deliverable (per `_CONTEXT.md`) are:

- Vendor document register (instantiated as `PRQ-009` Vendor Document Index plus an EPC-side register view)
- Vendor document submittals (the full source-enumerated set in `Datasheet.md`)
- Source vendor document table rows as artifacts where available
- Turnover records (`QLT-020`, `QLT-021`, `PRQ-016`, MEC-022/023, ELE-030, IOM `MEC-025`, as-builts `PIP-028`/`INS-029`)
