# Procedure — DEL-053-04 Vendor Engineered Equipment Package (Flare KO Drum, Cryo)

> Operational procedure to **produce** the Vendor Engineered Equipment Package as a Package Vendor production unit anchored by the EPC Scope of Work (DEL-053-01) and EPC Package Datasheet (DEL-053-02). Use/operate procedures for the installed equipment are addressed by the vendor O&M manual delivered under DEL-053-05.

## Purpose

Define the bounded sequence by which the Package Vendor engineers, fabricates, tests, and turns over the cryogenic Flare KO Drum (V-4110-1) and electric immersion heater (H-4112-1) as a single engineered equipment package, with EPC Integrator review hooks supporting DEL-053-06 (EPC Review and Acceptance). [DELIVERABLE_REGISTER DEL-053-04; PACKAGE_REGISTER row 53]

## Prerequisites

### Inputs required from EPC Integrator
- EPC Scope of Work for the package — **DEL-053-01** (location TBD; not yet issued at decomposition snapshot).
- EPC Package Datasheet — **DEL-053-02**: governing design conditions, interface terminations, and applicable code/standard call-outs (location TBD; not yet issued at decomposition snapshot).
- Confirmation of non-sour service per project brief (or supersession). [SCOPE_LEDGER SOW-0070]
- Confirmation of cryogenic relief header arrangement (610 mm / 24 in / 304SS inlet; combined HP/cryo downstream routing). [DBM-Deepcut flare equipment and header tables]

### References
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- GATE-07 PROJECT_DECOMP snapshot registers (DELIVERABLE_REGISTER, PACKAGE_REGISTER, SCOPE_LEDGER row range SOW-0067…SOW-0070)
- DBM-Deepcut: Flare Equipment and Routing; Flare Header and Backpressure Basis; package equipment list rows 11-12

### Declared upstream dependencies (`_DEPENDENCIES.md`)
- None declared during PREPARATION. Vendor execution effectively depends on DEL-053-01 and DEL-053-02 being issued; surface as **NEEDS_HUMAN_RULING** if vendor engineering proceeds before DEL-053-02 is issued.

## Steps

1. **Receive and confirm inputs.** Vendor receives DEL-053-01 (EPC SOW) and DEL-053-02 (EPC Package Datasheet). Verify completeness of design conditions, interface schedule, and standards/code call-outs. Raise clarification requests for any TBD parameter. Maps to: R-053-04-05, R-053-04-08.
2. **Establish vendor package design basis.** Document service description, design conditions (P, T, MDMT, flow), MOC strategy, code/standard set (ASSUMPTION: ASME BPVC Sec VIII Div. 1 with CRN until DEL-053-02 confirms), and interface boundary. Maps to: R-053-04-01, R-053-04-04, R-053-04-07.
3. **Engineer drum V-4110-1.** Process sizing (separation, liquid hold-up, disengagement velocity), mechanical design (shell/heads, MOC, MDMT-compliant impact-tested materials), nozzle schedule with inlet aligned to the 610 mm / 304SS cryogenic header, internals selection (mist eliminator, vortex breaker, baffles). Maps to: R-053-04-01, R-053-04-03, R-053-04-04, R-053-04-05.
4. **Engineer immersion heater H-4112-1.** Duty (kW), sheath material/watt density, electrical class (V/phase/Hz), thermowell and over-temperature protection, controls interface; coordinate with drum internals and hold-up to avoid hot-spotting. **TBD** values resolved against DEL-053-02. Maps to: R-053-04-02, R-053-04-06.
5. **Integrate package.** Skid/structural arrangement, package boundary terminations (process inlet/outlet, electrical, I&C, drain), insulation strategy consistent with no-heat-trace policy for cryogenic flare headers (DBM-Deepcut). Maps to: R-053-04-08, R-053-04-10.
6. **EPC review milestone — drawings/datasheet/design basis.** Vendor issues equipment datasheet set, GA drawings, nozzle orientation, design basis, and calculation summaries for EPC Integrator review (feeds DEL-053-06). Resolve review comments before fabrication release.
7. **Fabricate.** Procurement of materials with MTRs; welding to qualified procedures (WPS/PQR); NDE per code; hydrotest; PMI where required; impact testing at MDMT; code stamping (U-stamp) and CRN registration where applicable. Maps to: R-053-04-04, R-053-04-07.
8. **Assemble heater and integrate.** Install immersion heater, internals, instrumentation, and controls; complete skid/structural assembly. Maps to: R-053-04-06.
9. **Factory acceptance test (FAT).** Dimensional inspection vs. approved drawings, heater electrical/control FAT, hydrotest record, internals confirmation, interface check vs. DEL-053-02. Maps to: verification table in `Specification.md`.
10. **Compile vendor turnover documentation.** Assemble vendor document package per DEL-053-05 (datasheets, calculations, code certificates, MTRs, NDE/hydrotest records, FAT reports, GA/fabrication drawings, surface prep/coating records, O&M manual, spare parts list).
11. **Surface preparation, coating, packaging, and shipment.** Per vendor spec aligned with DEL-053-02. Issue shipping release once EPC integrator accepts FAT and turnover package.
12. **Support EPC Review and Acceptance (DEL-053-06).** Provide responses to EPC review comments, field support during installation acceptance, and warranty handoff.

## Verification

| Verification | Method | Maps to Spec Req |
|---|---|---|
| Design basis completeness | EPC review of vendor design basis against DEL-053-02 | R-053-04-01, R-053-04-04, R-053-04-05, R-053-04-07, R-053-04-08 |
| Pressure containment | Hydrotest per ASME; code stamping; CRN where applicable | R-053-04-04, R-053-04-07 |
| Material conformance | MTRs; PMI; MDMT impact test records | R-053-04-04 |
| Heater FAT | Electrical performance, duty, control, over-temperature protection tests | R-053-04-06 |
| Dimensional / nozzle conformance | Dimensional inspection vs. approved vendor drawings | R-053-04-02, R-053-04-03, R-053-04-08 |
| Interface conformance | Check-list against DEL-053-02 interface matrix (process, relief, drain, electrical, EHT, grounding, I&C, maintenance access, structural) | R-053-04-08 |
| Insulation/heat-trace policy alignment | Vendor insulation submittal confirms no heat-trace on cryogenic flare service per DBM | R-053-04-10 |
| Documentation completeness | Vendor turnover package per DEL-053-05 register | All |

## Records

The following records shall result from execution of this procedure and be submitted under DEL-053-05 to support DEL-053-06:

- Vendor equipment datasheet set (drum, heater).
- Vendor package design basis.
- Pressure vessel calculations and code certificates (U-stamp; CRN where applicable).
- Fabrication drawings: GA, nozzle orientation, internals, skid/structural.
- Heater design package, including electrical and control documentation.
- MTRs; WPS/PQR records; NDE records; hydrotest record; impact-test records at MDMT.
- FAT report (heater and package).
- Dimensional inspection report.
- Surface preparation and coating records.
- O&M manual; spare parts list.
- Shipping release / preservation documentation.

## Notes

- All vendor-specific design values (drum dimensions, MAWP, MDMT, hold-up, heater kW/V, MOC) remain **TBD** until DEL-053-02 is issued. Do not commit fabrication scope based on decomposition prose alone.
- Code/standard call-outs (ASME BPVC Sec VIII Div. 1; CRN; CSA/CEC for heater) are **ASSUMPTION** at this pass; binding selection must be confirmed against DEL-053-02 and 26020-Package_Requirements.docx (location TBD in this run).
