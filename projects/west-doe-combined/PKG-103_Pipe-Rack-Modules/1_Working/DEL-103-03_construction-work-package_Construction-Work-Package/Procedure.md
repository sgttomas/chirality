# Procedure — DEL-103-03 Construction Work Package (PKG-103 Pipe Rack Modules)

> Operational procedure to **produce** the Construction Work Package artifact and to govern its **use** during field execution. Values absent from accessible sources are marked `TBD`.

## Purpose

Define the steps the EPC Integrator follows to (A) author the PKG-103 Construction Work Package and supporting artifacts and (B) execute the package in the field through inspection, testing, turnover, and facility tie-in.

## Prerequisites

### Upstream inputs

- Accepted Gate 7 PROJECT_DECOMP snapshot (`_Decomposition/.../GATE-07_Final_Published_2026-05-24`). (`_REFERENCES.md`)
- PKG-103 Scope of Work (`DEL-103-01`) and PKG-103 EPC Package Datasheet (`DEL-103-02`). (`DELIVERABLE_REGISTER.csv`) — **ASSUMPTION**: declared `_DEPENDENCIES.md` carries no upstream entries; package-level sibling reliance is inferred.
- Final geotechnical report. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 688) — **location TBD** (not in accessible source set).
- Issued plot plan and 3D model snapshot for rack-supported commodity confirmation. (`PACKAGE_REGISTER.csv`) — **location TBD**.
- Issued area-classification drawings. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722) — **location TBD**.

### Required references

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- DBM Comp_and_Liquids and DBM Deepcut design basis.
- Gate 7 registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.

### Resources

- EPC Integrator construction engineering, QA/QC, and field execution organizations.
- Heavy-lift / crane logistics for module setting.
- Cold-weather work-permit and winter-construction equipment.

## Steps

### Part A — Authoring the Construction Work Package

1. **Confirm scope and identity.** Reconcile deliverable identity (DEL-103-03), parent package (PKG-103), CoA tracking (26020-03-36-003), WBS (03), and discipline (Structural) against `_CONTEXT.md` and `PACKAGE_REGISTER.csv`.
2. **Enumerate interface work fronts.** Build the interface table from `INTERFACE_REGISTER.csv` PKG-103 rows (nine declared interfaces). Each interface becomes a turnover-checklist column.
3. **Confirm rack-supported commodities.** Compare rack-supported commodity lists against the issued plot plan and 3D model. Resolve discrepancies before release. (`PACKAGE_REGISTER.csv`)
4. **Build the installation and tie-in workface plan.** Sequence: site grading and drainage → foundations (post final geotechnical report) → module delivery and off-loading → module setting on foundations → mechanical hookup → electrical/EHT/I&C/Communications terminations → tie-ins → ITT → turnover. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 688, 696, 700; `DBM-Deepcut/4-25_Deepcut_DBM.md` lines 111-114)
5. **Build the construction interface and turnover checklist.** One row per declared interface (REQ-CWP-8). Acceptance criteria per row are `TBD` pending detailed engineering and project ITT specs.
6. **Apply skid-edge isolation rule.** Verify each rack-to-module/unit/building interconnect places isolation at the skid edge. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 2454)
7. **Apply area-classification rule.** Default rack work to general-purpose non-hazardous; mark and re-class where issued classification drawings impose hazardous-area requirements. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722)
8. **Apply cold-climate provisions.** Embed -40 deg C ambient considerations into work-permit defaults, foundation frost protection, road/access seasonality, and module-set windows. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 145, 696)
9. **Label epistemic state.** Mark every value not supported by accessible sources as `TBD` or **ASSUMPTION** rather than inventing values.
10. **EPC Integrator review and approval.** Per Gate 6 disposition, the EPC Integrator is the sole design authority for the rack and the rack modules and signs off the package. (`INTERFACE_REGISTER.csv`)

### Part B — Executing the Construction Work Package in the field

11. **Civil and foundation work.** Execute grading, drainage, and foundations against the foundation design closed from the final geotechnical report. Record QC. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 688, 700)
12. **Module delivery, off-loading, setting.** Execute module setting per heavy-lift plan. Record set-tolerance and elevation QC. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 113) Acceptance tolerances `TBD`.
13. **Mechanical hookup.** Execute interconnecting piping field fit-up, welding, NDE, and hydrotest per project specs. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 114) Specific NDE/hydrotest acceptance levels `TBD`.
14. **Electrical, EHT, I&C, Communications.** Execute raceway, cable pull, termination, EHT installation/commissioning, and continuity tests per project E&I specs. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145; interfaces IFC-3268483707, IFC-489CEA5AA8, IFC-FC76A7E07D, IFC-38D5605A15) Specific acceptance criteria `TBD`.
15. **Tie-ins to upstream/downstream systems.** Execute facility tie-ins per the workface plan; coordinate with adjacent packages and confirm skid-edge isolation closed. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 2454)
16. **Inspection and testing (ITT).** Execute ITT per checklist; record each result. (REQ-CWP-11) Acceptance criteria `TBD`.
17. **Walkdown against issued documents.** Walk down completed work against plot plan, 3D model, area-classification drawings, and interface register. Close punch items.
18. **Turnover.** Execute the construction interface and turnover checklist; obtain receiving-organization sign-off per interface.

## Verification

| Step | Verification |
|---|---|
| 1-2 | Identity and interface enumeration cross-checked against `_CONTEXT.md` and Gate 7 registers |
| 3 | Plot-plan and 3D-model confirmation recorded prior to release |
| 4-5 | Workface plan and turnover checklist reviewed for completeness across nine interface types |
| 6 | Skid-edge isolation present at every rack-to-module/unit/building interconnect (walkdown) |
| 7 | Field area-classification markings consistent with issued drawings |
| 8 | Cold-weather work permits and frost-protection records present |
| 9 | Epistemic-label audit: no invented values |
| 10 | EPC Integrator approval block signed |
| 11-15 | Discipline-specific QC records (foundation, set, weld/NDE/hydrotest, electrical continuity, EHT commissioning) |
| 16 | ITT records signed by EPC Integrator construction QA |
| 17 | Walkdown punch list closed |
| 18 | Turnover checklist fully signed by receiving organizations |

## Records

The deliverable produces and retains:

1. Construction Work Package (root document).
2. Installation and tie-in workface plan.
3. Construction interface and turnover checklist (covering all nine PKG-103 interface types).

Construction execution generates and retains (forms and templates `TBD`, not in accessible sources):

- Foundation QC records traceable to geotechnical report and design loads.
- Module setting / elevation / tolerance records.
- Weld maps, NDE reports, hydrotest packs.
- Cable schedules, termination records, megger / continuity records, EHT commissioning records.
- Area-classification walkdown reports.
- Punch lists and closure records.
- Turnover certificates per interface.
