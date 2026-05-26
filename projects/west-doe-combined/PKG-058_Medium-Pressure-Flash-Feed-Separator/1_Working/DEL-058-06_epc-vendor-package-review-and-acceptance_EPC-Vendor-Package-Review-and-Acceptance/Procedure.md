# Procedure — DEL-058-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes how the EPC Integrator **produces** the vendor-package review-and-acceptance evidence pack for PKG-058 Medium Pressure Flash Feed Separator (MPFF). It is not a procedure to operate the equipment.

## Prerequisites

- Accepted upstream snapshot available: `GATE-07_Final_Published_2026-05-24` (`_REFERENCES.md`, `_DEPENDENCIES.md`).
- Source slices accessible:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"MPFF Operating and Capacity Basis"; §"MPFF and Stabilizer Train Relationship"; equipment register rows 52-53; module table; Heat Medium Users and Duties table.
  - `_Sources/26020-Package_Requirements.docx` package heading 13 (binary source; section-level location TBD).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` row for PKG-058 (binary source; column-level location TBD).
- EPC anchor deliverables drafted or available for cross-reference: `DEL-058-01` (Scope of Work), `DEL-058-02` (Package Datasheet), `DEL-058-03` (Construction Work Package).
- Vendor production-unit deliverables available for review: `DEL-058-04` (Vendor Engineered Equipment Package), `DEL-058-05` (Vendor Document Turnover Package). (`_DEPENDENCIES.md` declares no formal upstream edges as of PREPARATION — ASSUMPTION that these are the de facto upstreams via package decomposition.)
- Heater-bundle disposition memo (retain / de-rate / remove) available or carried as an open item by the upstream process engineering owner.
- Reviewer assignments and access to the Vendor Document Index established.

## Steps

1. **Establish the acceptance register.** Create the vendor document review log seeded from the `26020-Package_Requirements.docx` heading 13 vendor-deliverable enumeration. Every listed deliverable becomes one row with disposition fields (`SUBMITTED`, `ACCEPTED`, `REJECTED`, `OPEN`). (Verifies `R-058-06-02`.)
2. **Map SOW coverage.** Build a traceability matrix linking `SOW-0139`, `SOW-0140`, `SOW-0141`, `SOW-0142` to the acceptance-checklist rows and to evidence artifacts. (Verifies `R-058-06-01`.)
3. **Review Package Datasheet alignment.** Reconcile `DEL-058-02` design and operating values with vendor-submitted Pressure Vessel Data Sheet, process datasheet, heat-medium duty calc, mechanical calc package, and (if retained) heat-exchanger datasheet for E-7120-1 / E-7320-1. Flag mismatches; defer numeric reconciliation to the values actually submitted (do not assert design values not yet in vendor docs). (Verifies `R-058-06-13`.)
4. **Walk the equipment scope.** Confirm that the vendor package supplies V-7110-1, V-7310-1, E-7120-1 (if retained), E-7320-1 (if retained), Mistex demister internals, automated blowdown valve, LP fuel-gas purge connection, and methanol-injection provision upstream of the MPFF inlet level/pressure control valve. (Verifies `R-058-06-03`.)
5. **Verify configuration to DBM-Deepcut.** Confirm ≥10-minute liquid residence between weir and NLL-interface, no internal coating, self-framing building configuration, and shop-assembly within modules 710-1 / 730-1. (Verifies `R-058-06-04`.)
6. **Confirm train coupling and sparing.** Inspect P&IDs and operating philosophy: each MPFF assigned to one stabilizer; MPFF out of service when its stabilizer is out of service; 2 x 100% normal sparing; no sparing for off-design line-pack maximum. (Verifies `R-058-06-05`.)
7. **Execute interface-by-interface acceptance.** For each MPFF physical interface — inlet liquid from inlet-separator liquid outlet header; overhead to SOC third-stage suction; liquid bottoms to stabilizer flash/feed; LP fuel-gas purge; methanol injection; relief / blowdown to flare; heat medium supply/return to E-7120-1 / E-7320-1; drains / containment; electrical power; EHT; grounding/bonding; I&C control cabling; maintenance access; structural / foundations / supports — complete an acceptance checklist row referencing the relevant vendor artifact and (where applicable) the `26020-Packages_Interfaces_4_export.xlsx` row for PKG-058. (Verifies `R-058-06-06`.)
8. **Vessel acceptance.** Review Pressure Vessel Data Sheet, mechanical calc package, hydrotest packages, and Pressure Equipment Registration Package for V-7110-1 and V-7310-1. Confirm jurisdictional registration acceptance (authority TBD — ASSUMPTION). (Verifies `R-058-06-07`.)
9. **Verify operating-condition envelope.** Reconcile vendor process datasheet against DBM-Deepcut: 1724 kPag expected normal / design pressure; 12.91 MMSCFD winter design two-phase inlet; 19.58 m3/h winter liquid inlet; 4.143 MMSCFD winter vapour inlet; 6.681 MMSCFD expected normal two-phase inlet; <15.3 m3/h expected normal liquid inlet. Carry forward source TBD/TBC values for low / expected-high pressure and post-HEX MPFF inlet temperatures with explicit owners. (Verifies `R-058-06-08`.)
10. **Verify heat-medium interface.** Confirm 762 kW (2.6 MM BTU/h) duty per bundle, 118 deg C / 245 deg F supply, 80 deg C / 175 deg F return. Compare against the legacy 350 deg F supply basis and confirm against the post-HEX thermal re-simulation outcome documented in vendor docs. (Verifies `R-058-06-09`.)
11. **Verify heater-bundle disposition reflection.** Attach the upstream heater-bundle disposition memo to the acceptance pack. If "retain", verify tube-sheet seal-weld requirements implementation. If "remove" or "de-rate", verify nozzle blinding / bypass piping. In all cases, verify that vessel nozzle provisions are preserved per source. (Verifies `R-058-06-10`.)
12. **Quality records audit.** Assemble Supplier Quality Plan, ITP execution evidence, MTRs, Inspection Release Certificate, and Manufacturing Record Book / Vendor Data Book covering both vessels and both bundles. (Verifies `R-058-06-11`.)
13. **Turnover readiness.** Confirm SPIR, Logistics / Shipping Plan, and Mechanical Equipment IOM Manual are present and accepted. Hand off the Construction Work Package interface to `DEL-058-03`. (Verifies `R-058-06-12`.)
14. **Open-items disposition.** Close or explicitly carry every DBM-Deepcut open item (heater bundle disposition, 350 deg F supply basis, tube-sheet seal-weld requirements, post-HEX inlet temperatures, methanol-injection retention, stabilizer sparing / operating split) and every reviewer-raised open item. Each item carries a named owner and a target date. (Verifies `R-058-06-14`.)
15. **Issue the acceptance package.** Compile the four acceptance artifacts (vendor document review log; package acceptance checklist; test/inspection evidence bundle; turnover evidence bundle) plus the open-items disposition log. Route for EPC Integrator human-authored sign-off per project governance. (Verifies `R-058-06-15`; satisfies `K-AUTH-1`.)

## Verification

- Every `26020-Package_Requirements.docx` heading 13 vendor-deliverable row appears in the vendor document review log with a disposition.
- Every MPFF interface (per Step 7 enumeration and `26020-Packages_Interfaces_4_export.xlsx` PKG-058 row) has an acceptance-checklist row with linked evidence.
- Every requirement `R-058-06-01` through `R-058-06-15` (Specification.md) is linked to at least one verification record.
- All numeric design values in the acceptance pack are either reconciled to a vendor submittal or carried as `TBD` with a named owner.
- All DBM-Deepcut open items (Step 14 enumeration) are closed or carried with explicit disposition.
- Human-authored EPC Integrator sign-off is present and dated.

## Records

- Vendor document review log (live register; archived at acceptance).
- Package acceptance checklist (SOW-, interface-, and artifact-indexed; signed).
- Test / inspection evidence bundle (FAT records, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, registration package, SPIR, IOM).
- Open-items disposition log (DBM-Deepcut open items + reviewer-raised items).
- Heater-bundle disposition memo (attached or referenced).
- EPC Integrator acceptance sign-off (human-authored; required for binding acceptance — `K-AUTH-1`).
