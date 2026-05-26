# Specification — DEL-046-06 EPC Vendor Package Review and Acceptance

## Scope

This Specification governs the EPC Integrator's review and acceptance of the vendor-engineered package(s) supplied under PKG-046 (Acid Gas Compressors) for the 03-25 West Doe Compressor Station and Liquids Hub.

**In scope:**
- Review of vendor-supplied engineering documents against the PKG-046 EPC Scope of Work (DEL-046-01), Package Datasheet (DEL-046-02), and Construction Work Package (DEL-046-03).
- Verification of test and inspection evidence supplied by the vendor.
- Verification of turnover documentation completeness against the Vendor Document Turnover Package (DEL-046-05).
- Formal package acceptance (sign-off) and handoff readiness confirmation to construction/commissioning.

**Out of scope:**
- Production of the vendor engineering itself (DEL-046-04).
- Construction execution work (covered under the EPC Construction Work Package and downstream commissioning).
- Acceptance of cross-facility utility interfaces beyond the package battery limits (governed by the 03-25/04-25 utility interface basis, DBM SEC-01 lines 56, 68).

Source: `_CONTEXT.md` Scope; DBM 3-25_Comp_and_Liquids_DBM.md SEC-01.

## Requirements

R1. The EPC Integrator SHALL verify that vendor-supplied engineering documents conform to the PKG-046 Package Datasheet (DEL-046-02) and the EPC Scope of Work (DEL-046-01). Source: `_CONTEXT.md` scope (binding sibling deliverables).

R2. The EPC Integrator SHALL verify that the vendor package deliverable set includes, at minimum: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. Source: DBM SEC-09 line 617.

R3. The EPC Integrator SHALL verify that the package preserves clear scope boundaries among process vendors, electrical/controls systems, field construction, and cross-facility utility interfaces. Source: DBM SEC-09 line 617.

R4. The EPC Integrator SHALL verify that the package's control system interface is consistent with the facility BPCS integration basis: standalone Unit Control Systems with replication of values and general alarms to BPCS; final data maps, permissive logic, trip interfaces, and alarm priorities confirmed during vendor integration. Source: DBM SEC-12 line 810.

R5. The package design SHALL be verified against the design ambient envelope -40 deg C to +35 deg C, unless a more severe process or vendor-specific condition applies. The -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices. Source: DBM SEC-02 (lines 96, 145).

R6. Acid-gas-service material selection, corrosion allowance, sour-service compliance (e.g., NACE MR0175 / ISO 15156) — TBD: `26020-Package_Requirements.docx` package heading 1 slice not locally accessible as readable text. ASSUMPTION: sour-service compliance is required given DBM SEC-05 sour-gas H2S basis (~0.296 mol% in inlet-compressor composition).

R7. The vendor document turnover SHALL satisfy the turnover content list defined in DEL-046-05 (Vendor Document Turnover Package). Specific turnover content list — TBD pending DEL-046-05 initialization.

R8. The EPC Integrator SHALL record test and inspection evidence (factory acceptance tests, hydrotest, NDE, performance/run-in tests, instrument loop checks where executed at the vendor). Specific FAT and witness/hold-point definitions — TBD: location TBD in `26020-Package_Requirements.docx`.

R9. Final acceptance SHALL be documented in a signed package acceptance checklist and a vendor document review log. Source: `_CONTEXT.md` Anticipated Artifacts.

## Standards

| Standard / Code Family | Applicability | Status |
|---|---|---|
| BC OGC / BC Energy Regulator rules | Site is in BC; applicable per DBM SEC-13/14 regulatory context | ASSUMPTION: applicable; clause-level requirements `location TBD` |
| ASME B31.3 (Process Piping) | Process piping within package | ASSUMPTION: likely applicable; `location TBD` |
| ASME BPVC Section VIII | Pressure vessels in package | ASSUMPTION: likely applicable; `location TBD` (DBM SEC-09 line 611 references pressure-class and sour-service design) |
| NACE MR0175 / ISO 15156 | Sour-service materials given H2S exposure | ASSUMPTION: likely applicable; `location TBD` |
| API 618 / API 11P | Reciprocating compressors (precedent: DBM SEC-05 inlet compressors) | ASSUMPTION: likely applicable if package equipment includes reciprocating compression; `location TBD` |
| CSA Z662 | If any in-package or tie-in piping classifies as pipeline | TBD; `location TBD` |
| Vendor proprietary standards | Vendor-declared in their document register | TBD pending vendor turnover |

The authoritative list of applicable standards for PKG-046 acceptance is `TBD — location TBD` until the `26020-Package_Requirements.docx` package heading 1 slice is accessible as readable text.

## Verification

| Req | Verification approach |
|---|---|
| R1 | Side-by-side review of vendor documents against DEL-046-01 and DEL-046-02; recorded in vendor document review log. |
| R2 | Document register completeness audit against the DBM SEC-09 required content list. |
| R3 | Interface review against EPC Scope of Work tie-in list and the facility utility interface basis. |
| R4 | Controls integration review against facility BPCS/UCS map; resolved data-map review at vendor integration meeting. |
| R5 | Inspection of vendor datasheets and package-building heating/insulation/heat-tracing scope for the design ambient envelope. |
| R6 | Material certification review and sour-service compliance verification (NACE/MR0175 traceability). Specific procedures: TBD. |
| R7 | Turnover index audit against DEL-046-05 turnover content list. |
| R8 | FAT/ITR review; witness/hold-point sign-offs collected. |
| R9 | Acceptance checklist completed and signed; review log finalized. |

## Documentation

Anticipated documentation artifacts produced by this deliverable (per `_CONTEXT.md`):

- Vendor Document Review Log
- Package Acceptance Checklist
- Test/Inspection Evidence Index
- Turnover Evidence Index
- (Optional) Punch List of open items at conditional acceptance
