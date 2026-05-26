# Specification: DEL-085-06 — EPC Vendor Package Review and Acceptance

## Scope

This specification defines the EPC Integrator's normative requirements for reviewing the High Pressure flare stack vendor package (PKG-085), confirming its integration into facility 03-25 (including the shared 03-25/04-25 flare interface), and accepting it for turnover. The deliverable covers the four anticipated artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence (`_CONTEXT.md`).

**Covered SOW items:** SOW-0087, SOW-0088, SOW-0089, SOW-0090 (`_CONTEXT.md`).

**In scope:**
- Vendor document set review against the EPC Scope of Work, Package Datasheet (`DEL-085-02`), and Construction Work Package (`DEL-085-03`).
- Acceptance of the vendor-engineered equipment package (`DEL-085-04`) and vendor document turnover (`DEL-085-05`) as integrated deliverables.
- Verification of interface compatibility with shared 03-25/04-25 flare and incinerator systems.
- Acceptance of foundation, anchorage, and site-condition compliance for stack elements.

**Excluded:**
- Vendor-internal design verification of the sonic burner sizing methodology (vendor responsibility; EPC verifies acceptance criteria, not vendor calculations).
- Permit-final emissions tabulation (DBM source explicitly states current basis is not permit-final — DBM L555).
- Final flare studies (DBM L548 — required input, not produced here).

## Requirements

### R-01 — Vendor document set completeness

The vendor document set turned over under `DEL-085-05` SHALL be reviewed for completeness against the package datasheet (`DEL-085-02`) and EPC SOW (`DEL-085-01`). The review log SHALL record document ID, revision, review disposition, and date.
*Source basis:* `_CONTEXT.md` anticipated artifacts; ASSUMPTION — specific document index not derivable from accessible sources (`location TBD` in `26020-Package_Requirements.docx` heading 38).

### R-02 — Stack geometry conformance

The HP/Cryo stack as delivered SHALL conform to nominal geometry of 660 mm OD × 60,957 mm tall, sonic burner configuration. Any deviation requires documented engineering disposition and EPC Integrator concurrence.
*Source:* `3-25_Comp_and_Liquids_DBM.md` L499.

### R-03 — Relief header sizing conformance

HP and LP relief headers integrated to the stack SHALL be 508 mm (20 in) as carried in the current source basis. Deviations SHALL be flagged in the review log with downstream impact on KO drum manifolding to V-4100-2 / V-4150-2 (HP) and V-3900-2 (LP).
*Source:* `3-25_Comp_and_Liquids_DBM.md` L497, L499.

### R-04 — Shared-interface allocation resolution

Acceptance SHALL NOT proceed without a recorded interface ruling on the 03-25/04-25 service split for the HP/Cryo and LP dual stack and the incinerator. If unresolved at time of review, the interface item SHALL be carried as an open acceptance condition tied to a human ruling.
*Source:* `3-25_Comp_and_Liquids_DBM.md` L56, L547.

### R-05 — Site/ambient compliance

Package components, including controls and field devices, SHALL be qualified for -40 °C to +35 °C unless a stricter package basis applies. Cold-exposure qualification evidence SHALL be in the acceptance evidence set.
*Source:* `3-25_Comp_and_Liquids_DBM.md` L96, L145.

### R-06 — Foundation and anchorage acceptance

Foundations and anchorage for stack/structural elements SHALL be accepted against the final geotechnical report, equipment loads, snow/wind/seismic criteria, vibration, settlement, and maintenance access. Vendor-supplied loads SHALL be reconciled with the as-built foundation design.
*Source:* `3-25_Comp_and_Liquids_DBM.md` L700.

### R-07 — KO drum and transfer pump turnover

HP KO drums V-4100-2 and V-4150-2 with transfer pumps P-4100-2 and P-4150-2 (1 × 100 % each), and LP KO drum V-3900-2 with pump P-3900-2, SHALL have inspection and functional test evidence in the turnover package where they fall within the EPC scope envelope of the flare package.
*Source:* `3-25_Comp_and_Liquids_DBM.md` L497, L499, L550.

### R-08 — Test/inspection evidence

The acceptance evidence set SHALL include factory acceptance test (FAT) records, weld inspection records, NDE records appropriate for the service class, hydrostatic/pneumatic test records as applicable, pilot/ignition/burner functional verification, and instrumentation loop checks.
*Source basis:* `_CONTEXT.md` (anticipated artifacts); ASSUMPTION — exact test list per vendor package not derivable from accessible sources (`location TBD` in `26020-Package_Requirements.docx`).

### R-09 — Flare loads and study dependency

Acceptance for permit/operations readiness SHALL be conditional on completion of final flare relief and blowdown studies; the current source basis is explicitly not final.
*Source:* `3-25_Comp_and_Liquids_DBM.md` L548, L555.

### R-10 — Review log, checklist, and turnover index

The deliverable SHALL produce: (a) a vendor document review log indexed by vendor document ID; (b) a package acceptance checklist mapped to requirements R-01 through R-09; (c) collated test/inspection evidence; (d) turnover evidence package indexed for handoff to operations.
*Source:* `_CONTEXT.md` anticipated artifacts.

## Standards

| Standard / governing reference | Applicability | Location |
|---|---|---|
| `_Sources/26020-Package_Requirements.docx` heading 38 | Package-specific requirements for PKG-085 vendor package | **location TBD** (binary source; clause-level text not accessed) |
| `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 58 | Package interface register entry | **location TBD** (binary source; row-level text not accessed) |
| ASME / API flare and pressure relief codes | Applicable to vendor design and EPC acceptance verification | **location TBD** — ASSUMPTION: likely applicable; clause-level references not available in accessible sources |
| Project geotechnical report | Foundation/anchorage acceptance basis | **location TBD** |
| Final flare study | Acceptance basis for permit/operations readiness | **location TBD** (DBM L548 indicates required) |

## Verification

| Requirement | Verification approach | Evidence type |
|---|---|---|
| R-01 | Document-by-document review against datasheet/SOW index | Review log entries |
| R-02 | Dimensional check of as-delivered stack vs nominal | Inspection record |
| R-03 | Header size check at vendor/EPC interface points | Inspection / isometric check |
| R-04 | Interface ruling reference attached to acceptance record | Interface ruling document |
| R-05 | Review of vendor cold-weather qualification certificates | Vendor certs |
| R-06 | Review of foundation design and reconciliation with vendor loads | Civil/structural sign-off |
| R-07 | FAT and field-test records for KO drums and pumps | Test reports |
| R-08 | Records present in turnover index | Inspection of evidence set |
| R-09 | Statement of flare-study status attached as acceptance condition | Open-item register entry |
| R-10 | Existence and completeness check on the four artifacts | Final acceptance review |

## Documentation

Required artifacts produced by this deliverable (`_CONTEXT.md`):

- Vendor document review log
- Package acceptance checklist (mapped to R-01..R-09)
- Test/inspection evidence package
- Turnover evidence package

Inputs consumed (from sibling deliverables in PKG-085):

- `DEL-085-01` Scope of Work
- `DEL-085-02` Package Datasheet
- `DEL-085-03` Construction Work Package
- `DEL-085-04` Vendor Engineered Equipment Package
- `DEL-085-05` Vendor Document Turnover Package
