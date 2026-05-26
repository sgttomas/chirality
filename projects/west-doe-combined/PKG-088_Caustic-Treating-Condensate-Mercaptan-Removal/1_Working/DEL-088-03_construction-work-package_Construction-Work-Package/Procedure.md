# Procedure — DEL-088-03 Construction Work Package

> Operational procedure for **producing** the EPC Construction Work Package artifact set for PKG-088 (Caustic Treating, Condensate Mercaptan Removal). The procedure for **executing** the construction works themselves is internal to the Construction Work Package artifact and is not duplicated here.

## Purpose

Produce a complete, source-grounded Construction Work Package, an installation and tie-in workface plan, and a construction interface and turnover checklist for PKG-088, sufficient for issue-for-construction (IFC) review by the EPC Integrator. (Source: `_CONTEXT.md` Anticipated Artifacts.)

## Prerequisites

### Inputs (upstream)
- **DEL-088-01 — Scope of Work.** Required for boundary, equipment list, and integration narrative. ASSUMPTION: implicit upstream dependency (not declared in `_DEPENDENCIES.md`).
- **DEL-088-02 — Package Datasheet.** Required for package technical basis and interface requirements matrix. ASSUMPTION: implicit upstream dependency.
- **Project DBM** — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (scope inclusions, construction scope summary, condensate mercaptan treating, drains, instrument air, mechanical packages).
- **Source document** — `_Sources/26020-Package_Requirements.docx` package heading 41 (clause-level requirements; `location TBD` until extracted).
- **PKG-088 register row** — `PACKAGE_REGISTER.csv` (interface types, boundaries, tag).
- **Plot plan, equipment list, geotechnical report** — referenced but not yet locally accessible; carry as TBD inputs.

### Outputs
- Construction work package document set.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

### Skill/Tool prerequisites
- Engineering judgement bounded by source materials.
- HAZOP / hazard review forum (per R9) before commissioning sections close.

## Steps

### S1 — Establish package-execution scope from upstream deliverables
1. Read DEL-088-01 SoW and DEL-088-02 Datasheet (when issued).
2. Extract the equipment list, tag numbers, package boundary, and interface matrix.
3. Record the construction-execution scope as the intersection of (a) the EPC Integrator boundaries in `PACKAGE_REGISTER.csv` PKG-088 and (b) the construction scope summary in the DBM.

### S2 — Build the field tie-in list
1. For each of the 13 interface types declared for PKG-088, identify the tie-in flange/location, owning discipline, scope handoff point, and execution sequence.
2. Cross-reference the DBM coordination items at line 619 (MCC, RIO, heat tracing, HVAC, F&G, drain/vent tie-ins) into the tie-in list.
3. Annotate every tie-in with its source authority (DEL-088-01, DEL-088-02, DBM, or source clause).

### S3 — Resolve modularization and offloading sequence
1. Confirm the vendor's shop/field split once DEL-088-04 vendor package basis is available; until then, carry both a fully modular and a field-built sequence.
2. Identify crane class, road access, and offloading positions; align with plot plan and access road basis when those become available. (`location TBD` for plot plan.)
3. Record assumed modular split as ASSUMPTION until DEL-088-04 issues a vendor basis.

### S4 — Compile caustic-specific construction provisions
1. Carry forward the aluminum exclusion in the caustic building (R3) into material take-off review checks.
2. Carry the 300# minimum ANSI rating for caustic drain headers and the embrittlement-aware material selection note (R4) into piping specs and inspection holds.
3. Carry the atmospheric 32 oz caustic tank construction provisions (LP fuel-gas blanket, heating, insulation, flame-arrestor venting; fresh-caustic not on VRU) (R5) as tank-installation work-pack scope.

### S5 — Compile utility and electrical/I&C tie-in scope
1. Plan IA distribution to caustic oxidation demand (214 SCFM TBC) consistent with 04-25 supply per SCA-006.
2. Plan LP fuel-gas distribution to caustic treating overhead dilution per the DBM utility section.
3. Carry the field-construction wiring practice for local control stations (R, per DBM): hard-wired back to the MCC starter circuit.

### S6 — Construction interface and turnover checklist
1. Build a checklist that lists, per interface type, the predecessor activity, the inspection/test hold, the responsible party, and the completion record.
2. Include geotechnical-report acceptance as a foundation/pile release prerequisite (R10).
3. Include the formal hazard review for purge and analyzer maintenance (R9) as a commissioning release prerequisite.
4. Include the construction work package register alignment with plot plan and equipment list as an IFC release prerequisite (R8).

### S7 — Reconcile source clauses and close TBDs
1. When the source slice from `26020-Package_Requirements.docx` heading 41 is available, walk every clause against the work-package draft and close `location TBD` entries.
2. Update the Conflict Table in `Guidance.md` for any clause that disagrees with the DBM-derived requirements.

### S8 — Internal QA and IFC release
1. Verify the artifact set against R1 (completeness), R2 (interface coverage), and R8 (register alignment).
2. Confirm all source-grounded values have provenance (SourcePath + SectionRef or `location TBD`).
3. Submit to EPC Integrator review for IFC sign-off.

## Verification

| Verification Item | Method | Evidence |
|---|---|---|
| All anticipated artifacts produced (R1) | Document checklist against `_CONTEXT.md` Anticipated Artifacts | Signed completeness sheet |
| Interface coverage (R2) | Traceability table interface-type-to-tie-in entries | Tie-in list with 13/13 coverage |
| Caustic material discipline (R3, R5) | Material take-off review; tank inspection record | Inspection sign-off |
| Drain system spec (R4) | Piping ISO review; HAZOP segregation outcome | HAZOP minutes; piping spec confirmation |
| Utility tie-in (R6) | IA/LP fuel-gas loop checks | Commissioning checklist |
| Modularization plan (R7) | Vendor scope confirmation; lift study | Vendor confirmation memo; lift plan |
| Register alignment (R8) | Cross-check work package register against plot plan + equipment list before IFC | IFC release log |
| Hazard review closure (R9) | Hazard review minutes | Signed minutes |
| Geotechnical confirmation (R10) | Geotechnical report reference recorded against foundation release | Foundation release record |
| Source-clause reconciliation (R11) | Walk-through log against `26020-Package_Requirements.docx` heading 41 | Source-clause reconciliation log |

## Records

The procedure shall produce, retain, and pass to the EPC Integrator turnover library:

- Final Construction Work Package document set (IFC-stamped).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist (completed).
- Field tie-in list (closed).
- Hazard review minutes for purge/analyzer practices.
- Source-clause reconciliation log (R11).
- Conflict Table dispositions (from `Guidance.md`) recorded with human rulings.
- Pre-IFC alignment evidence (work package register vs. plot plan vs. equipment list).
