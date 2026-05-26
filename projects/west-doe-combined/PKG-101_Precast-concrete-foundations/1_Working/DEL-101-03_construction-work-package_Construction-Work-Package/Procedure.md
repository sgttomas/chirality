# Procedure — DEL-101-03 Construction Work Package (PKG-101 Precast Concrete Foundations)

This procedure describes the steps to **produce** the Construction Work Package (CWP) artifact set for PKG-101 (Precast concrete foundations). Operating the physical foundations is governed by issued discipline engineering and is not within this artifact's authoring scope.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- Confirm access to the Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER, ARTIFACT_REGISTER, INTERFACE_REGISTER).
- Confirm access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-11) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies in `_DEPENDENCIES.md`: none declared as of PREPARATION. The sibling deliverables DEL-101-01 (Scope of Work) and DEL-101-02 (Package Datasheet) are co-anchor deliverables for PKG-101 and should be consulted when issued.
- Geotechnical assessment report (external dependency per DBM-Deepcut SEC-11 §External Dependencies) — **TBD** pending report acceptance; do not commit final foundation-installation criteria prior.

## Steps

1. **Anchor the package identity.** Restate PKG-101 identity (workbook row 102, Structural discipline, EPC Integrator responsibility, scope item SOW-0257, objectives OBJ-001/008/010) from `_CONTEXT.md` and DELIVERABLE_REGISTER.
2. **Enumerate the three required artifacts.** Per ARTIFACT_REGISTER rows for DEL-101-03, draft outlines for:
   1. Construction work package (ART-384DBDF766)
   2. Installation and tie-in workface plan (ART-674B3EBE60)
   3. Construction interface and turnover checklist (ART-37A6123862)
3. **Frame foundation basis.** From DBM-Deepcut SEC-11 §Piles and Foundations, record the default driven-steel-pile basis and the named precast-concrete exceptions (transformer bearing foundations; compressor blocks on piles). Mark per-tag inventories and detailed arrangements as TBD until DEL-101-02 datasheet and discipline engineering are issued.
4. **Capture site/code basis.** From DBM-Deepcut SEC-11 §Governing Codes and §Buildings and DBM-Comp_and_Liquids §Site basis, record NBC, Canadian Foundation Engineering Manual, and the -40 deg C ambient as construction-method drivers.
5. **Develop the workface plan tie-in scope.** Address the two workbook-declared PKG-101 interfaces (Grading / Site Drainage / Spill Containment IFC-26343B703C; Structural / Foundations / Supports IFC-BED3DE4194). Identify counterparty owners during coordination (action item — owners not enumerated in current sources).
6. **Build the turnover checklist skeleton.** Cover: foundation survey/elevation acceptance; concrete strength and curing records; embed and anchor verification; cold-weather placement records; geotechnical-conformance check; for compressor foundations, dynamic-analysis acceptance hold-point release; oil-leak containment-arrangement acceptance.
7. **Register TBDs and conflicts.** Carry over the items in `Guidance.md` Conflict Table; for any per-tag or per-method gap not resolvable from sources, write TBD with provenance rather than inventing values.
8. **Cross-check against sibling deliverables.** When DEL-101-01 and DEL-101-02 are drafted/issued, reconcile tagged-equipment lists, interface owners, and engineering hold-points; raise any inconsistencies into the Conflict Table.
9. **Issue for review** to the EPC Integrator's construction lead and the structural discipline lead.

## Verification

| Check | Method |
|---|---|
| All three anticipated artifacts present in the CWP set | Document inventory against ARTIFACT_REGISTER rows for DEL-101-03 |
| Workface plan addresses both PKG-101 workbook interfaces | Cross-reference against INTERFACE_REGISTER lines 905-906 |
| Foundation basis reflects driven-steel-pile default and named precast exceptions only | Cross-reference against DBM-Deepcut SEC-11 §Piles and Foundations |
| Geotechnical-report dependency is reflected as a hold-point, not a closed value | Review against DBM-Comp_and_Liquids line 141 and DBM-Deepcut SEC-11 §External Dependencies |
| Compressor foundation release is gated on dynamic-analysis acceptance | Review hold-point register against DBM-Deepcut SEC-11 §Assumptions |
| -40 deg C site basis is reflected in concrete cold-weather method statement requirement | Review against DBM-Comp_and_Liquids line 145 |
| TBDs are surfaced (not invented) for per-tag inventories, anchor schedules, mix designs, ITP acceptance criteria | Review of Specification + Conflict Table entries |

## Records

- The CWP, workface plan, and turnover checklist documents themselves.
- Hold-point register linking compressor foundation release to dynamic-analysis acceptance and overall foundation-installation criteria to geotechnical-report acceptance.
- Coordination log identifying counterparty owners for the two PKG-101 workbook interfaces (owner identities — TBD).
- Inspection and Test Plans (ITPs), method statements, concrete placement and curing records — **TBD** pending issue of discipline engineering.
- Conflict Table entries from `Guidance.md` carried through to ruling.
