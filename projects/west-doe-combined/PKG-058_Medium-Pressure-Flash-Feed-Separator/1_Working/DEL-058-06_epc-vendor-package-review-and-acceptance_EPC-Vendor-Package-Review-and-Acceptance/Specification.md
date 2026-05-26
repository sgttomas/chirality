# Specification — DEL-058-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
This deliverable specifies the EPC Integrator's review-and-acceptance work product for PKG-058 Medium Pressure Flash Feed Separator (MPFF) — covering separators V-7110-1, V-7310-1 and HCL heater bundles E-7120-1, E-7320-1 within shop-assembled modules 710-1 and 730-1. It defines the evidence the EPC Integrator must produce to demonstrate that the Package Vendor's `DEL-058-04` Vendor Engineered Equipment Package and `DEL-058-05` Vendor Document Turnover Package satisfy the EPC Scope of Work (`DEL-058-01`), Package Datasheet (`DEL-058-02`), and Construction Work Package (`DEL-058-03`).

Sources: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"MPFF Operating and Capacity Basis", §"MPFF and Stabilizer Train Relationship"; `26020-Package_Requirements.docx` package heading 13 (binary; section-level location TBD); `DELIVERABLE_REGISTER.csv` row `DEL-058-06`.

### Out of scope
- Authoring or modifying the vendor-side engineering deliverables themselves; those are `DEL-058-04` / `DEL-058-05` outputs.
- Acceptance of upstream inlet separator packages (e.g., PKG-046 / PKG-057) or downstream inlet stabilizer packages; those are separate packages.
- Disposition of the MPFF HCL heater bundle retention / de-rate / removal decision; that decision is an upstream design ruling carried in DBM-Deepcut "Open Items" and is out of scope of this acceptance deliverable except to verify that whichever disposition is chosen is reflected in the vendor package.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| `R-058-06-01` | The acceptance evidence MUST cover all SOW items mapped to this deliverable: `SOW-0139`, `SOW-0140`, `SOW-0141`, `SOW-0142`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| `R-058-06-02` | The vendor document review log MUST enumerate every vendor engineering deliverable listed in `26020-Package_Requirements.docx` package heading 13 for the MPFF package, and record disposition (accepted / rejected / open) for each. | `26020-Package_Requirements.docx` package heading 13 (location TBD at section level — binary source) |
| `R-058-06-03` | The package acceptance checklist MUST verify that the vendor package supplies: two MPFF separators (V-7110-1, V-7310-1), two MPFF HCL heater bundles (E-7120-1, E-7320-1) if the retention disposition is "retain", Mistex demister internals, automated blowdown valve, LP fuel-gas purge connection, and methanol-injection provision upstream of the MPFF inlet level/pressure control valve. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; equipment register rows 52-53; Heat Medium Users table |
| `R-058-06-04` | The acceptance evidence MUST confirm package configuration to match DBM-Deepcut: ≥10-minute liquid residence time between weir height and NLL-interface; no internal coating; self-framing building enclosing instrumentation and one end of vessel (consistent with inlet separator package configuration). | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| `R-058-06-05` | The acceptance evidence MUST confirm train coupling and sparing: each MPFF assigned to one stabilizer with the MPFF out of service when its stabilizer is out of service; 2 x 100% normal sparing; no sparing for off-design line-pack maximum. | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" |
| `R-058-06-06` | The acceptance evidence MUST cover each physical interface for the MPFF package: inlet liquid from inlet-separator liquid outlet header; overhead vapour pressure-regulated to SOC third-stage suction; liquid bottoms to downstream stabilizer flash/feed separator; LP fuel-gas purge supply from downstream of the fuel-gas scrubber; methanol injection; relief / blowdown to flare; heat medium supply and return to the HCL heater bundles; drains / containment; electrical power; EHT; grounding / bonding; I&C control cabling; maintenance access; structural / foundations / supports. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"Heat Medium Users and Duties"; `26020-Packages_Interfaces_4_export.xlsx` package row for PKG-058 (column-level location TBD — binary source) |
| `R-058-06-07` | The acceptance evidence MUST include pressure-vessel registration and pressure-test evidence for V-7110-1 and V-7310-1: Pressure Equipment Registration Package, Pressure Vessel Data Sheet, mechanical calc package, and Hydrotest / Pressure Test Packages. | `26020-Package_Requirements.docx` package heading 13 (location TBD); ASSUMPTION based on the standard EPC vendor package artifact set for static pressure equipment |
| `R-058-06-08` | The acceptance evidence MUST verify operating conditions per separator (winter design case): total two-phase inlet 12.91 MMSCFD; liquid inlet 19.58 m3/h; vapour inlet 4.143 MMSCFD; operating pressure 1724 kPag (expected normal and design); expected normal two-phase inlet 6.681 MMSCFD; expected normal liquid inlet <15.3 m3/h. Low and expected-high pressure values, and post-HEX MPFF inlet temperatures, remain `TBD/TBC` in the source and MUST be confirmed against vendor process datasheets. | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| `R-058-06-09` | The acceptance evidence MUST verify heat-medium interface conditions for each E-7120-1 / E-7320-1: 762 kW (2.6 MM BTU/h) duty; supply 118 deg C / 245 deg F; return 80 deg C / 175 deg F. The legacy 350 deg F supply basis is superseded and MUST be confirmed against the post-HEX thermal re-simulation outcome. | DBM-Deepcut §"Heat Medium Users and Duties"; §"MPFF Operating and Capacity Basis" |
| `R-058-06-10` | The acceptance evidence MUST verify that whichever heater-bundle disposition (retain / de-rate / remove) is selected upstream is correctly reflected in the vendor package — including tube-sheet seal-weld requirements if retained, and preserved vessel nozzle provisions until disposition is confirmed. | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| `R-058-06-11` | Quality records MUST be assembled: Supplier Quality Plan, ITP execution evidence, Material Test Reports / Certificates, Inspection Release Certificate, and Manufacturing Record Book / Vendor Data Book covering both vessels and both heater bundles. | `26020-Package_Requirements.docx` package heading 13 (location TBD); ASSUMPTION based on the standard EPC vendor package artifact set |
| `R-058-06-12` | Turnover MUST include the SPIR, Logistics / Shipping Plan, and Mechanical Equipment IOM Manual for the MPFF package. | `26020-Package_Requirements.docx` package heading 13 (location TBD); ASSUMPTION based on the standard EPC vendor package artifact set |
| `R-058-06-13` | Numeric design/operating values used in acceptance MUST be traceable to the Package Vendor's submitted Pressure Vessel Data Sheet, process datasheet, and heat-medium duty calc. Specific numeric values not in the DBM source slice (e.g., vessel design pressure / temperature / sizing, materials of construction, slug / residence sizing parameters) remain `TBD` until those vendor submittals are accepted. | DBM-Deepcut §"MPFF Operating and Capacity Basis" (records TBD/TBC where source is silent) |
| `R-058-06-14` | Open items recorded in the source ("MPFF Operating and Capacity Basis" — heater bundle disposition, 350 deg F supply basis, tube-sheet seal-weld requirements, post-HEX inlet temperatures, methanol-injection retention; "MPFF and Stabilizer Train Relationship" — stabilizer sparing / operating split) MUST be closed or carried with explicit disposition in the acceptance record. | DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"MPFF and Stabilizer Train Relationship" |
| `R-058-06-15` | EPC Integrator acceptance is binding only when human-authored sign-off is recorded. No agent may certify acceptance (`K-AUTH-1`). | `docs/CONTRACT.md` K-AUTH-1 (governing invariant) |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Provincial pressure equipment registration regime applicable to the project (typically ABSA in Alberta) | Required for the Pressure Equipment Registration Package for V-7110-1 and V-7310-1. | location TBD — authority identity not stated in accessible source slices; ASSUMPTION based on project location and typical jurisdictional regime. |
| Pressure vessel design code (ASME BPVC Section VIII or CSA B51 as applicable) | Governs the Pressure Vessel Data Sheet, mechanical calc package, and acceptance of vessels V-7110-1 and V-7310-1. | location TBD — not stated in DBM-Deepcut MPFF slice; ASSUMPTION typical to scope. |
| Heat-exchanger design code (e.g., ASME BPVC Section VIII Div. 1; TEMA for shell-and-tube U-bundle/BKU bundles) | Governs the HCL heater bundle E-7120-1 / E-7320-1 if retained (U-bundle / BKU-type per source). | location TBD — bundle code not stated explicitly; ASSUMPTION based on the U-bundle/BKU description in DBM-Deepcut §"MPFF Operating and Capacity Basis". |
| Electrical area classification, EHT, and grounding/bonding standards applicable to the 4-25 facility | Governs EHT design, energization records, grounding/bonding, and area-classification compliance for the MPFF package electrical scope. | location TBD — not enumerated in accessible MPFF source slices; standards inherited from project electrical basis. |

## Verification

| Req ID | Verification Approach |
|---|---|
| `R-058-06-01` | Traceability matrix mapping each SOW item to acceptance-checklist rows and to evidence artifacts. |
| `R-058-06-02` | Document-by-document review log inspection; every `26020-Package_Requirements.docx` heading 13 vendor deliverable carries a tracked disposition. |
| `R-058-06-03` | Walk-down and as-built/IFC drawing review against the equipment register, the Mistex internals / no-coating requirement, blowdown valve presence, LP fuel-gas purge tie-in, and methanol injection point. |
| `R-058-06-04` | Mechanical layout review (residence-time calc evidence; weir-to-NLL geometry; building / enclosure GA drawings). |
| `R-058-06-05` | Train coupling and sparing review against P&IDs and operating philosophy; cross-check with the stabilizer package configuration. |
| `R-058-06-06` | Interface-by-interface checklist; each interface row references the relevant vendor artifact and (where present) the `26020-Packages_Interfaces_4_export.xlsx` row for PKG-058. |
| `R-058-06-07` | Hydrotest packages signed off; Pressure Equipment Registration Package accepted by registration authority; Pressure Vessel Data Sheet reconciled with as-built. |
| `R-058-06-08` | Reconciliation of vendor process datasheet against DBM-Deepcut operating/design table; explicit TBD/TBC carry-forward where the source itself is unresolved. |
| `R-058-06-09` | Heat-medium duty reconciliation: 762 kW per bundle, 118/80 deg C supply/return; post-HEX thermal re-simulation outcome confirmed in vendor docs. |
| `R-058-06-10` | Heater-bundle disposition memo from upstream engineering attached; vendor package documented as consistent with selected disposition. |
| `R-058-06-11` | Quality records audit; Inspection Release Certificate issued; MRB / VDB compiled and accepted for both vessels and both bundles. |
| `R-058-06-12` | Receipt inspection records; SPIR provided and accepted; IOM in turnover bundle. |
| `R-058-06-13` | Reconciliation table between EPC Package Datasheet (`DEL-058-02`) values and vendor-submitted values; TBD entries flagged with owners. |
| `R-058-06-14` | Open-items log carried into commissioning with explicit closure or carryover noted for each DBM-Deepcut open item. |
| `R-058-06-15` | Human sign-off record present, dated, and traceable to a named EPC Integrator authority. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist (SOW-, interface-, and artifact-indexed).
- Test / inspection evidence bundle (FAT, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, registration package, SPIR, IOM).
- Open-items disposition log (covering DBM-Deepcut open items called out above and any reviewer-raised items).
- EPC Integrator human-authored acceptance sign-off (required for binding acceptance per `K-AUTH-1`).

Standards-related and numeric design values that depend on vendor submittals carry `TBD` placeholders until the Package Vendor deliverables are accepted.
