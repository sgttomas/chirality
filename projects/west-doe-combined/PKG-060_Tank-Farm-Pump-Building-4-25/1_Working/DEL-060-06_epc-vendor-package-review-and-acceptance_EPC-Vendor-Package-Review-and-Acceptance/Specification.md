# Specification — DEL-060-06 EPC Vendor Package Review and Acceptance

## Scope

This Specification governs the EPC Integrator's review and acceptance of the vendor-engineered package(s) supplied under PKG-060 (Tank Farm Pump Building 4-25) for the 04-25 West Doe Deepcut expansion.

**In scope:**
- Review of vendor-supplied engineering documents against the PKG-060 EPC Scope of Work (DEL-060-01), Package Datasheet (DEL-060-02), and Construction Work Package (DEL-060-03).
- Verification of test and inspection evidence supplied by the vendor for the pump package (condensate transfer, water transfer, sour-water treatment, process water transfer, fresh caustic transfer per DBM line 2555).
- Verification of turnover documentation completeness against the Vendor Document Turnover Package (DEL-060-05).
- Formal package acceptance (sign-off) and handoff readiness confirmation to construction/commissioning.

**Out of scope:**
- Production of the vendor engineering itself (DEL-060-04).
- Construction execution work (covered under the EPC Construction Work Package and downstream commissioning).
- Acceptance of cross-facility utility interfaces beyond the package battery limits (governed by 03-25/04-25 shared utility basis, DBM SEC-01 line 95).
- Tank-farm bulk storage tanks/bullets themselves (the package title is the Pump Building; bullets, tanks, and dike walls fall under other deliverables/packages).

Source: `_CONTEXT.md` Scope; DBM 4-25_Deepcut_DBM.md SEC-01.

## Requirements

R1. The EPC Integrator SHALL verify that vendor-supplied engineering documents conform to the PKG-060 Package Datasheet (DEL-060-02) and EPC Scope of Work (DEL-060-01). Source: `_CONTEXT.md` scope (binding sibling deliverables).

R2. The EPC Integrator SHALL verify that the vendor package deliverable set includes, at minimum: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. Source: DBM SEC-09 line 617.

R3. The EPC Integrator SHALL verify that the package preserves clear scope boundaries among process vendor, electrical/controls systems, field construction, and cross-facility utility interfaces (shared fuel gas / instrument air between 03-25 and 04-25; tank-farm electrical building). Source: DBM SEC-01 line 95; DBM line 2816.

R4. The EPC Integrator SHALL verify that the package's control system interface replicates pump-package values and general alarms to the facility BPCS; final data maps, permissive logic, trip interfaces, and alarm priorities confirmed during vendor integration. Source: DBM SEC-12 line 810 (applied as precedent).

R5. The package design SHALL be verified against the design ambient envelope -40 deg C minimum to +35 deg C maximum, with the -40 deg C minimum governing exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor-specific condition applies. Source: DBM SEC-02 lines 197-198.

R6. The package design SHALL be verified against site environmental loading inputs: plant elevation 673 m AMSL; wind pressure q 1/50 = 0.40 kPa; maximum wind speed 138 km/h (TBC). Source: DBM SEC-02 lines 195, 200, 202.

R7. The EPC Integrator SHALL verify that minimum spacing between pressurized bullets and a pump skid taking suction from bullets is at least 3.05 m (10 ft) per API 2510, as applicable to pumps inside the tank farm. Source: DBM SEC-02 line 252.

R8. Sour-service material selection, corrosion allowance, and NACE MR0175 / ISO 15156 compliance SHALL be verified for wetted, pressure-containing, or process-exposed components in contact with H2S-bearing streams (condensate, sour water). Clause-level basis: TBD — `26020-Package_Requirements.docx` package heading 15 not locally accessible as readable text. ASSUMPTION: sour-service compliance is required given DBM SEC-01 (sour-gas facility) and SEC-05 (design H2S basis 1 mol% combined feed).

R9. The vendor document turnover SHALL satisfy the turnover content list defined in DEL-060-05 (Vendor Document Turnover Package). Specific turnover content list — TBD pending DEL-060-05 initialization.

R10. The EPC Integrator SHALL record test and inspection evidence for the pump package: factory acceptance tests, hydrotest, NDE, performance/run-in tests, mechanical run, vibration, and instrument loop checks (where executed at the vendor). Specific FAT and witness/hold-point definitions — TBD: location TBD in `26020-Package_Requirements.docx` heading 15.

R11. Final acceptance SHALL be documented in a signed package acceptance checklist and a vendor document review log. Source: `_CONTEXT.md` Anticipated Artifacts.

## Standards

| Standard / Code Family | Applicability | Status |
|---|---|---|
| BC OGC / BC Energy Regulator rules | Site is in BC; facility regulatory context | ASSUMPTION: applicable; clause-level basis `location TBD` |
| ASME B31.3 (Process Piping) | Process piping within pump package and tie-ins | ASSUMPTION: likely applicable; `location TBD` |
| ASME BPVC Section VIII | Any pressure vessels in package (e.g., suction strainers, pulsation bottles) | ASSUMPTION: likely applicable if such items exist; `location TBD` |
| NACE MR0175 / ISO 15156 | Sour-service materials given H2S exposure on condensate and sour-water duties | ASSUMPTION: applicable for sour-service wetted components; `location TBD` |
| API 610 / API 674 / API 675 | Centrifugal and reciprocating/metering pumps | ASSUMPTION: API 610 likely applicable to radial centrifugal water/process-water/sour-water/caustic pumps (DBM lines 2619-2622); `location TBD` |
| API 2510 | Pressurized LPG storage spacing (informs tank farm spacing R7) | DBM SEC-02 line 252 (referenced) |
| CSA Z662 | If any in-package or tie-in piping classifies as pipeline | TBD; `location TBD` |
| CSA Z276 / NFPA 58 | LPG / NGL handling (if package interfaces with NGL bullets) | ASSUMPTION: may apply at tank-farm interfaces; `location TBD` |
| Vendor proprietary standards | Vendor-declared in their document register | TBD pending vendor turnover |

The authoritative list of applicable standards for PKG-060 acceptance is `TBD — location TBD` until the `26020-Package_Requirements.docx` package heading 15 slice is accessible as readable text.

## Verification

| Req | Verification approach |
|---|---|
| R1 | Side-by-side review of vendor documents against DEL-060-01 and DEL-060-02; recorded in vendor document review log. |
| R2 | Document register completeness audit against the DBM SEC-09 required content list. |
| R3 | Interface review against EPC Scope of Work tie-in list and the facility utility interface basis (incl. shared 03-25/04-25 utilities). |
| R4 | Controls integration review against facility BPCS/UCS map; resolved data-map review at vendor integration meeting. |
| R5 | Inspection of vendor datasheets, motor and bearing temperature ratings, lubrication, seal, and package-building heating/insulation/heat-tracing scope for the -40 deg C design ambient. |
| R6 | Verification of structural, anchor, and exposure ratings against site wind/elevation inputs. |
| R7 | Plot plan / general arrangement review confirming bullet-to-pump-skid spacing meets API 2510 (3.05 m / 10 ft). |
| R8 | Material certification review and sour-service compliance verification (NACE MR0175 / ISO 15156 traceability) for wetted components. |
| R9 | Turnover index audit against DEL-060-05 turnover content list. |
| R10 | FAT/ITR review; witness/hold-point sign-offs collected (including any required mechanical run / vibration / performance curve verification). |
| R11 | Acceptance checklist completed and signed; review log finalized. |

## Documentation

Anticipated documentation artifacts produced by this deliverable (per `_CONTEXT.md`):

- Vendor Document Review Log
- Package Acceptance Checklist
- Test/Inspection Evidence Index
- Turnover Evidence Index
- (Optional) Punch List of open items at conditional acceptance
