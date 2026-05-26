# Specification: DEL-090-06 — EPC Vendor Package Review and Acceptance

> Normative requirements for the EPC Integrator's review and acceptance of the PKG-090 VRU 3-25 vendor package. Requirements are derived from accessible source slices in the Gate 7 snapshot and `_CONTEXT.md`. Where derivation requires text not in the accessible source slices, requirements are labelled `ASSUMPTION` or `TBD`.

## Scope

### In scope

- EPC Integrator review of the Package Vendor's engineered equipment package (DEL-090-04) and turnover documentation (DEL-090-05) against:
  - the EPC Scope of Work for the package (DEL-090-01),
  - the EPC Package Datasheet (DEL-090-02), and
  - the EPC Construction Work Package (DEL-090-03).
  - Source: `_CONTEXT.md` Scope.
- Recording of vendor document review and comments (ART-08602095B0).
- Recording of acceptance and turnover decisions (ART-2BE816FC33).
- Recording of factory/shop test and inspection evidence (ART-63586A61E0).
- Verification that integration-side scope items called out in SOW-0252 ("By others") are coordinated by the EPC Integrator: shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs. Source: SOW-0252.

### Out of scope

- Vendor-side engineering, design, and equipment production (DEL-090-04 owner: Package Vendor). Source: SOW-0249.
- Vendor document turnover production (DEL-090-05 owner: Package Vendor). Source: `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Field installation work itself (separate construction workflow under DEL-090-03 execution).

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-090-06-001 | The EPC Integrator SHALL review every vendor-issued document against the EPC Scope of Work (DEL-090-01), Package Datasheet (DEL-090-02), and Construction Work Package (DEL-090-03), and record disposition (accept / accept-with-comment / reject) in the Vendor Document Review and Comment Log (ART-08602095B0). | `_CONTEXT.md` Scope; ART-08602095B0 |
| REQ-090-06-002 | The EPC Integrator SHALL verify the as-supplied compressor configuration matches SOW-0250: two (2) complete 100%-capacity VRU compressor packages in lead-lag, sour service, both housed in one building. | SOW-0250 |
| REQ-090-06-003 | The EPC Integrator SHALL verify the compressor make/model matches SOW-0251: Ro-Flo 12S/212M, two-stage rotary vane positive displacement, four (4) compressor stage units total (Stage 1 + Stage 2 per train, two trains). | SOW-0251 |
| REQ-090-06-004 | The EPC Integrator SHALL verify sour-service material compliance and NACE designation for the supplied package, given service composition 0.4588 mol% H2S and 0.4314 mol% CO2. | SOW-0251 |
| REQ-090-06-005 | The EPC Integrator SHALL verify each compressor stage is equipped with a dual mechanical pressurized barrier seal (Plan 53 type), using fuel gas, with seal alarms and primary vent routed to LP flare. | SOW-0251 |
| REQ-090-06-006 | The EPC Integrator SHALL verify each train has one (1) 200 HP, 600 V, 3-phase, 60 Hz, VFD-ready motor driving both Stage 1 and Stage 2; cooler motors SHALL be VFD-ready and 600 V. | SOW-0251; SOW-0252 |
| REQ-090-06-007 | The EPC Integrator SHALL verify the package design conditions match SOW-0252: design suction 0.9 kPag (2 oz/in²); design discharge 483 kPag (70 psig); design capacity 28 e3m³/d (1 MMSCFD); design temperature 102 °C. | SOW-0252 |
| REQ-090-06-008 | The EPC Integrator SHALL verify the package operating points match SOW-0252: 1st-stage intercooler outlet 48.9 °C; 2nd-stage aftercooler outlet 60.0 °C; 1st-stage dewpoint 45.6 °C; 2nd-stage dewpoint 53.2 °C; expected flow per unit 0.510 MMSCFD. | SOW-0252 |
| REQ-090-06-009 | The EPC Integrator SHALL maintain a package acceptance and turnover checklist (ART-2BE816FC33) capturing acceptance status of every required artifact in the Vendor Document Turnover Package (DEL-090-05). | `_CONTEXT.md` anticipated artifacts; ART-2BE816FC33 |
| REQ-090-06-010 | The EPC Integrator SHALL retain factory/shop test and inspection evidence (ART-63586A61E0) for each compressor stage and for the package as a whole. Detailed test list is `TBD` until source-slice content from `26020-Package_Requirements.docx package heading 43` is locally accessible. | ART-63586A61E0 |
| REQ-090-06-011 | The EPC Integrator SHALL coordinate the integration-side ("By others") scope from SOW-0252 — shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs — and SHALL not accept the vendor package until these interfaces are demonstrably ready. | SOW-0252 |
| REQ-090-06-012 | Package acceptance SHALL NOT be issued until DEL-090-05 (Vendor Document Turnover Package) is closed and DEL-090-03 (Construction Work Package) verification confirms field readiness. ASSUMPTION (lifecycle-derived; not directly stated in the accessible source slices). | ASSUMPTION; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| NACE (sour-service material standard, edition `TBD`) | Materials of construction for sour service per SOW-0251. | location TBD — driven by source SOW-0251 statement "NACE designation applies"; specific NACE document not stated. |
| Seal API Plan 53 (referenced as "Plan 53 type" in SOW-0251) | Compressor mechanical seal arrangement. | location TBD — API standard edition not stated in accessible source slice. |
| `26020-Package_Requirements.docx` package heading 43 | Authoritative package-level requirements. | location TBD — binary source not locally accessible at this run. |

## Verification

| Verification ID | Approach | Verifies |
|---|---|---|
| VER-090-06-001 | Document-by-document review against the EPC document list, with dispositions recorded in ART-08602095B0. | REQ-090-06-001 |
| VER-090-06-002 | Comparison of vendor package datasheet against SOW-0250 / SOW-0251 / SOW-0252 line items. | REQ-090-06-002 .. REQ-090-06-008 |
| VER-090-06-003 | Materials/welder/NACE certificate review. | REQ-090-06-004 |
| VER-090-06-004 | Seal arrangement drawing and seal-system P&ID review; alarm/flare routing verification. | REQ-090-06-005 |
| VER-090-06-005 | Motor and VFD datasheet review; cooler motor datasheet review. | REQ-090-06-006 |
| VER-090-06-006 | Witness or review of factory/shop tests; collection of test records in ART-63586A61E0. | REQ-090-06-010 |
| VER-090-06-007 | Acceptance checklist sign-off in ART-2BE816FC33; turnover gate against DEL-090-05 closure. | REQ-090-06-009, REQ-090-06-012 |
| VER-090-06-008 | Integration-readiness walkdown of "By others" interfaces. | REQ-090-06-011 |

## Documentation

The deliverable produces the following documentation, per `_CONTEXT.md` and `ARTIFACT_REGISTER.csv`:

- Vendor document review and comment log (ART-08602095B0).
- Vendor package acceptance and turnover checklist (ART-2BE816FC33).
- Factory/shop test and inspection evidence (ART-63586A61E0).
- Turnover evidence package (linkage to DEL-090-05 outputs).
