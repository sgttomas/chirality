# Specification — DEL-097-03 Construction Work Package (Tanks, Condensate, API 650, 3-25)

## Scope

This Construction Work Package (CWP) specification governs how the PKG-097 condensate-storage tank package — four (4) 3800 bbl modified API 650 atmospheric tanks in C5+ condensate service at the 3-25 area — is physically installed, inspected, tied into adjacent facility systems, and turned over to commissioning.

**Covers:**

- Field erection / installation of the four condensate tanks and their integral package items (PVRV, EPRV, VRU header connection, blanket gas connection, internal coating verification, fill-rate / fill-limit instrumentation tie-ins).
- Tie-ins between PKG-097 and adjacent facility systems (fill lines, suction/transfer lines, blanket gas supply, VRU header, drains, instrumentation, electrical, fire/safety).
- Construction QA/QC: weld inspection, hydrotest, coating inspection, calibration, and punch-listing.
- Mechanical completion and turnover to commissioning.

**Excludes:**

- Vendor engineering, fabrication, and shop testing of the tank package itself — covered by `DEL-097-04_vendor-engineered-equipment-package`.
- Earthworks, foundations, and containment berms — covered under PKG-002 / PKG-006 (ASSUMPTION based on objective grouping; explicit interface row TBD).
- Process operating procedures and long-term operations — out of CWP scope.
- Vendor document turnover content — covered by `DEL-097-05_vendor-document-turnover-package`.

## Requirements

Requirements are derived from the PKG-097 source slice (`26020-Package_Requirements.docx` §`26020-03-PT-19-006`) and from `_CONTEXT.md` (Anticipated Artifacts). Inferences are labeled.

### R-1 Construction Work Package contents (mandatory)

The deliverable shall include, at minimum:

- R-1.1 A construction work package master document covering installation method, sequencing, resources, and QA/QC.
- R-1.2 An installation and tie-in workface plan covering each tank and each external interface.
- R-1.3 A construction interface and turnover checklist covering mechanical completion and handover to commissioning.

Source: `_CONTEXT.md` Anticipated Artifacts; reinforced by Gate 7 DELIVERABLE_REGISTER row for `DEL-097-03`.

### R-2 Tank installation conformance

- R-2.1 Each of the four (4) 3800 bbl condensate tanks shall be erected in accordance with modified API 650. (Source: PKG-097 §`26020-03-PT-19-006`.) The specific deltas vs. base API 650 are not enumerated in the PKG-097 source slice — **location TBD**.
- R-2.2 Internal coating (Devchem 253) on floor, walls, and roof shall be inspected for continuity and cure prior to mechanical completion. (Source: PKG-097 §`26020-03-PT-19-006`.)
- R-2.3 Blanket gas system tie-ins shall conform to API 2000. (Source: PKG-097 §`26020-03-PT-19-006` — "blanket gas system per API 2000".) Specific API 2000 clauses are **location TBD**.

### R-3 Relief / venting tie-ins

- R-3.1 Each tank's PVRV and EPRV shall be installed, oriented, and pressure-tested per the vendor package documentation; PVRV is for vacuum / modulating pressure relief and EPRV is for the single worst-case relief case. (Source: PKG-097 §`26020-03-PT-19-006`.)
- R-3.2 Each tank's VRU header connection shall be tied to the facility VRU header. (Source: PKG-097 §`26020-03-PT-19-006`.) Interface tag list **TBD** (interface source `26020-Packages_Interfaces.3.xlsx` not opened in this pass).

### R-4 Fill and overfill controls

- R-4.1 Overfill protection / high-level shutdown shall enforce a 90% maximum fill limit. (Source: PKG-097 §`26020-03-PT-19-006`.)
- R-4.2 Fill nozzles and associated piping shall be installed such that plant design capacity can fill a single tank without exceeding the design fill rate. (Source: PKG-097 §`26020-03-PT-19-006`.) Numeric fill-rate value: **location TBD**.

### R-5 Construction QA/QC

- R-5.1 Welding, NDE, and hydrotest shall be performed per modified API 650 acceptance criteria. (Source: PKG-097 §`26020-03-PT-19-006`, referencing modified API 650.) Specific clause references — **location TBD**.
- R-5.2 Coating inspection (DFT, holiday testing, cure) shall be performed for the internal Devchem 253 system. (ASSUMPTION based on coating-manufacturer standard practice; PKG-097 source slice does not state inspection method.)
- R-5.3 Calibration / strapping of each tank shall be completed prior to commissioning. (ASSUMPTION: standard for custody-relevant storage; not stated in PKG-097 source slice.)

### R-6 Turnover and mechanical completion

- R-6.1 A construction interface and turnover checklist shall be completed and signed for each tank and each tie-in. (Source: `_CONTEXT.md` Anticipated Artifacts.)
- R-6.2 Punch-list closure and mechanical completion certificate are required before the package is released to commissioning. (ASSUMPTION: EPC standard practice; specific gate criteria **location TBD**.)

### R-7 Interfaces

- R-7.1 The CWP shall reference and align with PKG-097 physical interface rows in `26020-Packages_Interfaces.3.xlsx` — specific rows **TBD**.
- R-7.2 The CWP shall coordinate with civil (foundations / containment) and balance-of-plant scopes — ASSUMPTION (objective grouping OBJ-002…OBJ-010 places this package alongside civil scopes); explicit upstream interface rows **TBD** until `Dependencies.csv` is generated.

## Standards

| Standard | Applicability | Locally Accessible? |
|---|---|---|
| API 650 (modified) | Tank fabrication and field erection | Standard text not present in `_Sources` (location TBD). Source reference: PKG-097 source slice. |
| API 2000 | Blanket gas / venting system | Standard text not present in `_Sources` (location TBD). Source reference: PKG-097 source slice. |
| Site / EPC welding & NDE specifications | R-5.1 | TBD (not present in PKG-097 source slice). |
| Coating manufacturer (Devchem 253) installation data | R-2.2, R-5.2 | TBD (location not in PKG-097 source slice). |

## Verification

| Req | Verification approach |
|---|---|
| R-1.1–R-1.3 | Document review against CWP-required content list. |
| R-2.1 | Inspection records (weld NDE, hydrotest, dimensional) per modified API 650. |
| R-2.2 | Coating QC reports (DFT, holiday testing, cure log). |
| R-2.3 | Blanket-gas system commissioning test report referencing API 2000. |
| R-3.1 | Relief device installation / set-pressure / function-test records. |
| R-3.2 | VRU tie-in punch-list signoff and leak test record. |
| R-4.1 | Loop check and SIL/SIF function test for high-level shutdown. |
| R-4.2 | Hydraulic check vs. plant design fill rate (calc or witness). |
| R-5.1 | NDE reports, hydrotest certificate. |
| R-5.2 | Coating inspection reports. |
| R-5.3 | Tank strapping / calibration certificate. |
| R-6.1, R-6.2 | Signed turnover / mechanical completion package. |
| R-7.1, R-7.2 | Interface punch list reconciled against `26020-Packages_Interfaces.3.xlsx`. |

## Documentation

The deliverable produces (per `_CONTEXT.md` Anticipated Artifacts):

- Construction work package (master)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Supporting records (referenced, produced during execution):

- NDE / weld / hydrotest records (R-5.1)
- Coating QC records (R-2.2, R-5.2)
- Calibration / strapping certificates (R-5.3)
- Relief device installation & function-test records (R-3.1)
- Mechanical completion / turnover certificates (R-6)
