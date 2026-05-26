# Procedure — DEL-051-03 Construction Work Package (PKG-051 Process Heat Medium Unit)

**Interpretation:** This procedure describes how to **produce** the Construction Work Package deliverable artifact set (the CWP document, the installation and tie-in workface plan, and the construction interface and turnover checklist). Field execution procedures (mechanical hookup work instructions, lift plans, etc.) are produced **inside** the CWP under this procedure, not by this procedure itself.

## Purpose

Produce a Construction Work Package for PKG-051 (Process Heat Medium Unit) that is source-grounded in the accepted GATE-07 PROJECT_DECOMP snapshot and the locally accessible DBM material, sized for EPC Integrator field execution, and ready for review by DEL-051-06 (EPC Vendor Package Review and Acceptance).

## Prerequisites

- Accepted decomposition snapshot: GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP).
- Deliverable-local files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Locally accessible source slices:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Heat Medium Basis, §1945; Utility Systems §1822; Cross-discipline coordination line 619; PSV/Pop tank line 2002; ASME Section I rule line 2435; Seal-welded tubes line 2503).
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Construction Scope Summary line 73; geotechnical placeholder line 141; appendix note line 933).
- Sibling deliverables for cross-reference (read-only): DEL-051-01 Scope of Work, DEL-051-02 Package Datasheet, DEL-051-04 Vendor Engineered Equipment Package.
- Declared upstream dependencies: **None declared** in `_DEPENDENCIES.md` at the time of this procedure. Production should anticipate that DEL-051-02 (Package Datasheet) and DEL-051-04 (Vendor Engineered Equipment Package) will become functional upstreams once their content stabilizes; the CWP should reference them as soon as those artifacts mature.
- Binary sources not locally machine-readable: `26020-Package_Requirements.docx` (package heading 6) and `26020-Packages_Interfaces_4_export.xlsx` (Packages row 79). Content from these is TBD until extracted.

## Steps

1. **Confirm scope and identity.**
   - Read `_CONTEXT.md` and confirm DeliverableID, ParentPackageID, ResponsibleParty.
   - Confirm the scope sentence matches decomposition row 440 (Construction Work Package, EPC Integrator).
2. **Pull source slices.**
   - Extract the Heat Medium Basis section (DBM-Deepcut 4-25 §"Heat Medium Basis", lines 1945-2010).
   - Extract construction scope, geotechnical, and -40 deg C ambient basis from DBM-Comp_and_Liquids 3-25 (lines 73, 141, 696).
   - Note the appendix conflict (line 933) and capture as conflict CT-001 in `Guidance.md`.
3. **Define the CWP outline.**
   - Sections: (a) package identity and scope, (b) installation workface plan, (c) field tie-in list, (d) inspection and test plan (ITP), (e) interface and turnover checklist, (f) open items and TBC register.
4. **Author the installation workface plan.**
   - Foundations (heater, pump module, pop tank).
   - Steel/pipe rack.
   - Mechanical install (heater set, pump module set, pop tank set, expansion tank set).
   - Piping (HM supply/return headers and laterals to users).
   - Electrical (MCC connections, pump motor cable terminations, BMS power).
   - Controls and F&G (BMS, ESD, fire/gas detectors per DBM-Deepcut 4-25 line 3256).
   - Heat tracing and lagging (ASSUMPTION: extent TBC).
5. **Author the field tie-in list.**
   - One row per HM supply lateral to each user (TEG regenerator at 425 deg F, amine reboiler at 350 deg F, deethanizer reboiler at 350 deg F, MPFF heater if retained, mole-sieve heater if retained, stabilizer reboiler) per DBM-Deepcut 4-25 lines 1177, 1214, 1336, 674, 1617, 706.
   - One row per HM return lateral.
   - Pop tank PSV discharge connections.
   - Fuel gas supply tie-in to HM heater (DBM-Deepcut 4-25 line 1830).
   - Flare/drain/vent tie-ins.
   - Electrical and controls tie-ins.
6. **Author the ITP and inspection plan.**
   - Hydrostatic test at >= 350 psig (R-051-03-03).
   - Seal-welded tube verification on shipped-loose HM bundles (R-051-03-04).
   - PSV walk-down: no block valves on inlet/outlet (R-051-03-06).
   - Pop tank level switch loop check (R-051-03-05).
   - Cold-start motor demonstration (R-051-03-07).
   - Fire/gas detector loop check per building (R-051-03-08).
7. **Author the construction interface and turnover checklist.**
   - One line per ITP item, one line per tie-in, one line per loop check.
   - Sign-off columns for EPC Integrator field, EPC Integrator engineering, Package Vendor, and Operations (commissioning interface).
8. **Cross-check against sibling deliverables.**
   - Confirm SOW item coverage (SOW-0165..0168) matches DEL-051-01.
   - Confirm equipment list and design conditions match DEL-051-02 once it exists; raise CT entries for mismatches.
9. **Register open items and TBD.**
   - Heater sparing ruling, pump sparing ruling, circulation rate, fluid vendor rating, pop-tank SG, package physical location (CT-001), 26020 binary source content.
10. **Issue CWP for review.**
    - Hand off to DEL-051-06 (EPC Vendor Package Review and Acceptance) when the CWP set is complete and all TBD items are visibly registered.

## Verification

- All four CWP content sections (workface plan, tie-in list, ITP, turnover checklist) exist and are populated.
- Every Specification requirement (R-051-03-01..R-051-03-11) has at least one corresponding ITP or turnover-checklist row.
- Every locally accessible source slice cited in `Datasheet.md` and `Specification.md` is reachable at the cited file path.
- All TBD and CONFLICT items are surfaced in the CWP open-items register and in `Guidance.md` Conflict Table.
- No information was invented to fill TBD; placeholders are explicit.

## Records

- This deliverable folder: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, updated `_STATUS.md`, and the run record under `_run_records/`.
- Downstream CWP execution records (ITP sign-offs, hydrostatic test records, PSV witness, loop checks, turnover sign-off) will be generated during construction execution and are not produced by this deliverable.
