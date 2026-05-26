# Specification — DEL-079-06 EPC Vendor Package Review and Acceptance

## Scope

### In Scope
- EPC Integrator review of the Package Vendor's engineered equipment package (DEL-079-04) and Vendor Document Turnover Package (DEL-079-05) against the EPC Scope of Work (DEL-079-01), EPC Package Datasheet (DEL-079-02), and EPC Construction Work Package (DEL-079-03). Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER PKG-079 rows.
- Production of vendor document review log, package acceptance checklist, test/inspection evidence record, and turnover evidence record for the PKG-079 Instrument Air Building. Source: `_CONTEXT.md` Anticipated Artifacts.
- Closure of the ten declared PKG-079 interface facts before acceptance. Source: INTERFACE_REGISTER IFC-E7D3353482 .. IFC-0EC9E5E722.

### Out of Scope
- Package engineering, package design, fabrication, and vendor documentation authorship (owned by Package Vendor under DEL-079-04 / DEL-079-05). Source: SCOPE_LEDGER SOW-0131; PACKAGE_REGISTER PKG-079 ownership note.
- Shipping compressor packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs. These are explicitly "by others" relative to vendor scope and are handled as EPC construction items, not vendor acceptance items. Source: SCOPE_LEDGER SOW-0134.
- Authorship of the four upstream EPC anchor deliverables (DEL-079-01/02/03) — those are inputs, not outputs of this deliverable. Source: DELIVERABLE_REGISTER PKG-079.

## Requirements

R1. **Acceptance basis traceability.** Every acceptance entry SHALL cite the upstream item it satisfies: a SOW-0131..SOW-0134 row, an EPC Package Datasheet requirement (DEL-079-02), or an EPC Construction Work Package interface/turnover item (DEL-079-03). Source: SCOPE_LEDGER; DELIVERABLE_REGISTER PKG-079.

R2. **Equipment count and rating verification.** The package acceptance checklist SHALL verify, against vendor data, the equipment counts and ratings stated in SOW-0132 and SOW-0133: 2 x oil-injected rotary screw IA compressors each rated 1113 SCFM at 861 kPag (125 psig) discharge, driven by 250 HP electric motors with soft-start or VFD-ready and anti-condensation space heaters; 1 wet receiver; 2 dryer pre-filters; 1 regenerative desiccant dryer (two towers, 100% capacity); 1 common after-filter; 1 dry receiver (or 2 x 50%). Source: SCOPE_LEDGER SOW-0132, SOW-0133.

R3. **Pressure and dew-point verification.** Acceptance SHALL include verification that:
- all package PSVs are set at 948 kPag (137.5 psig);
- delivered instrument air has a maximum water dew point of -73.3 °C at 1000 kPag;
- compressor maximum discharge pressure / shutdown is 1000 kPag;
- maximum system design pressure is 1034 kPag (150 psig);
- minimum system pressure is 551 kPag (80 psig);
- facility shutdown pressure is 482 kPag (70 psig);
- design temperature envelope is -40 °C to 38 °C.
Source: SCOPE_LEDGER SOW-0133, SOW-0134.

R4. **Electrical driver verification.** Acceptance SHALL verify electric motor compliance with 200-250 HP, 600 V / 3 PH / 60 Hz, TEFC, non-classified, soft-start or VFD-ready; with vendor-determined speed. Source: SCOPE_LEDGER SOW-0134.

R5. **Interface closure.** Each of the ten PKG-079 declared interface types (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) SHALL have a corresponding acceptance checklist entry indicating closure status (closed / open / waived with reason) before package acceptance is recorded. Source: INTERFACE_REGISTER PKG-079 rows; ARTIFACT_REGISTER DEL-079-02 interface-fact entries.

R6. **Vendor document review.** The vendor document review log SHALL include at minimum the source-required vendor documents listed under DEL-079-05 (Vendor Document Index, Vendor Document Control Procedure, Supplier Quality Plan, and the remaining vendor document categories produced by the vendor under DEL-079-05). Each row SHALL record review status (accepted / accepted with comments / rejected) and any comment-resolution reference. Source: ARTIFACT_REGISTER DEL-079-05 (ART-95A888C02E, ART-33E3E7FE46, ART-F8BF3DB9AA, ART-D103DDD65D, ART-CACD5074F8, …); SOW-0131..SOW-0134.

R7. **Test/inspection evidence retention.** Acceptance SHALL include or reference factory acceptance test (FAT), pre-shipment inspection, and any site acceptance test (SAT) records for the package — specifically including PSV setting evidence, dew-point performance evidence, and motor commissioning evidence. ASSUMPTION: specific FAT/SAT protocols and witness requirements not stated in accessible sources; mark `TBD` until vendor data or DEL-079-02 datasheet specifies. Source: SCOPE_LEDGER SOW-0133 (PSV, dew point).

R8. **Turnover evidence alignment.** Turnover evidence SHALL align to the construction interface and turnover checklist produced under DEL-079-03 (ART-10C3D82526) so that EPC-side commissioning can proceed without rework. Source: ARTIFACT_REGISTER ART-10C3D82526.

R9. **Source fidelity and labeling.** All acceptance claims SHALL cite the SOW row, interface ID, artifact ID, or vendor document ID they verify. Inferences not directly supported by accessible source slices SHALL be labeled `ASSUMPTION`; unknowns SHALL be marked `TBD`.

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| Workbook Packages row 69 (PKG-079 authoritative basis) | Package identity, vendor/EPC responsibility split, applicable interface set | PACKAGE_REGISTER PKG-079; INTERFACE_REGISTER PKG-079 |
| `26020-Package_Requirements.docx` package heading 32 | Major included equipment, scope notes, operating/design conditions | location TBD (raw doc not in deliverable folder); SCOPE_LEDGER SOW-0132..SOW-0134 |
| `26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` (Bid Docs/Budgetary) | Source RFQ for the Instrument Air Building package; vendor bid basis | location TBD; PACKAGE_REGISTER PKG-079 Word Source Basis |
| `DBM-Deepcut/4-25_Deepcut_DBM.md` | Design Basis Memorandum slice for the instrument air system | location TBD; PACKAGE_REGISTER PKG-079 Word Source Basis |
| Applicable codes for rotary-screw compressed-air packages, PSV setting/verification, electrical motor classification, and pressure vessel certification | Acceptance verification evidence | TBD — not enumerated in accessible source slices; ASSUMPTION: vendor data sheets identify governing standards |

## Verification

| Requirement | Verification Method |
|---|---|
| R1 | Inspection of acceptance checklist for SOW / DEL-079-02 / DEL-079-03 trace columns. |
| R2 | Document review of vendor general arrangement, equipment list, motor data sheets, and compressor performance curves. |
| R3 | Document review of vendor PSV data sheet (set pressure), dryer performance curve / FAT report (dew point), and compressor data sheet (discharge/shutdown pressures). |
| R4 | Document review of motor data sheet and electrical SLD; verification against EPC Package Datasheet electrical interface. |
| R5 | Inspection of acceptance checklist for one closure row per IFC-* ID listed in INTERFACE_REGISTER for PKG-079. |
| R6 | Inspection of vendor document review log; reconciliation against the vendor document register produced under DEL-079-05. |
| R7 | Inspection of FAT/SAT records retained or referenced; PSV calibration certificates; dew-point test record. |
| R8 | Cross-check turnover evidence against ART-10C3D82526 construction interface/turnover checklist. |
| R9 | Editorial review of acceptance artifacts for citation labels and TBD/ASSUMPTION markers. |

## Documentation

The following artifacts SHALL be produced and retained in this deliverable folder (source: `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log.
- Package acceptance checklist (with rows for SOW-0131..SOW-0134, the ten PKG-079 interfaces, and the equipment count/condition rows from R2..R4).
- Test/inspection evidence record (FAT/SAT references; PSV/dew-point/motor evidence).
- Turnover evidence record (aligned to DEL-079-03 ART-10C3D82526).
