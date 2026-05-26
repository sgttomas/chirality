# Procedure: DEL-080-03 — Construction Work Package (Inlet Compressors)

**Interpretation:** This procedure describes the steps to **produce** the Construction Work Package deliverable (planning artifact) and outlines the in-field construction sequence the CWP must direct. Field execution governance (HSE, permit-to-work, welding) is referenced rather than reproduced.

## Prerequisites

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (Source: `_REFERENCES.md`)
- Companion EPC anchors initialized/approved:
  - `DEL-080-01_scope-of-work` (Scope of Work)
  - `DEL-080-02_package-datasheet` (Package Datasheet)
  - (Source: DELIVERABLE_REGISTER.csv rows 360-361)
- Vendor package inputs available (when produced): `DEL-080-04_vendor-engineered-equipment-package` and `DEL-080-05_vendor-document-turnover-package`. (Source: DELIVERABLE_REGISTER.csv rows 363-364)
- Source basis read: `_Sources/26020-Package_Requirements.docx` (package heading 33); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (§inlet compression, §prime movers, §electrical); `SCOPE_LEDGER.csv` SOW-0119–SOW-0122; `INTERFACE_REGISTER.csv` PKG-080 rows.
- No declared upstream dependencies present in `_DEPENDENCIES.md` at PREPARATION (verify before issue). (Source: `_DEPENDENCIES.md`)
- Site civil/foundation basis, climatic loads, seismic basis, permit basis: TBD (not in accessible source slices).
- Project welding, NDE, pressure-test, HSE, and QA specifications: TBD (not in accessible source slices).

## Steps

### Phase A — Produce the CWP planning artifact

1. Confirm DEL-080-01 and DEL-080-02 scope and datasheet content against this CWP draft for consistency on equipment count (2), configuration (2 x 50%), pressures (~1275/6550 kPag), throughput (~80 MMSCFD combined), and sour-service basis (NACE). (Source: SCOPE_LEDGER.csv SOW-0120–SOW-0122)
2. Build the **installation and tie-in workface plan**:
   - List per-unit module delivery, set, and re-assembly tasks (three modules per package). (Source: DBM §inlet compression)
   - Define foundation acceptance criteria — TBD pending site civil basis.
   - Define alignment, grouting, and anchoring tasks.
3. Build the **construction interface and turnover checklist**:
   - One section per declared interface type (thirteen interfaces). (Source: INTERFACE_REGISTER.csv rows 512-524)
   - Each section contains: scope at boundary, responsible party (EPC Integrator vs. Package Vendor — Source: PACKAGE_REGISTER.csv row 66), pre-tie-in checks, tie-in execution, post-tie-in tests, and turnover signoff.
4. Cross-reference the workface plan and interface checklist back to Specification requirements R-1 through R-8.
5. Mark all gaps (R-9, R-10 and any per-step TBDs) explicitly. Do not infer values from generic convention.
6. Issue the CWP planning artifact for EPC Integrator review and for inclusion in DEL-080-06 acceptance evidence. (Source: DELIVERABLE_REGISTER.csv row 365)

### Phase B — Field execution sequence the CWP must direct

7. Site readiness: receive foundations, confirm grade and elevations, confirm utility availability. (TBD against site basis.)
8. Receive and inspect each vendor module: dimensional check, transport-damage inspection, MTR check for sour-service materials. (Source: SCOPE_LEDGER.csv SOW-0122)
9. Set and reassemble three modules per package into self-framing building; align and grout. (Source: DBM §inlet compression)
10. Execute tie-ins across the thirteen declared interfaces, in dependency order (typical: Structural / Foundations first; then Process Piping, Utility Piping, Relief / Flare / Vent, Drain / Containment; then Electrical Power, Grounding / Bonding, EHT; then I&C / Control Cabling; then Building HVAC / Services, Fire & Gas / Safety Systems, Area / Exterior Lighting, Maintenance Access). (Source for interface set: INTERFACE_REGISTER.csv rows 512-524; ASSUMPTION on sequencing.)
11. Electrical pre-energization: confirm 4,000 V supply to KM-2150 and KM-2250 from MCC-8200, starting VFD installation per SCA-001 VE #34, no soft start. (Source: DBM §electrical)
12. Pressure-test tie-in piping per project welding/NDE specification (specification TBD).
13. Mechanical completion: punchlist closeout, system walkdown, signoffs.
14. Turnover to commissioning/operations using the construction interface and turnover checklist; feed evidence into DEL-080-06. (Source: DELIVERABLE_REGISTER.csv row 365)

## Verification

| Step | Verification |
|---|---|
| 1 | Consistency check across DEL-080-01, DEL-080-02, DEL-080-03; same key values for unit count, configuration, pressures, throughput, sour-service. |
| 2 | Workface plan review against R-1, R-3, R-7, R-8. |
| 3 | Interface checklist completeness: thirteen rows present and signed off. |
| 4 | Requirement-to-step traceability matrix in the CWP. |
| 5 | Open-items log lists every TBD with owner and decision target. |
| 6 | Documented EPC Integrator review and acceptance of the CWP planning artifact. |
| 8 | Receiving inspection logs; MTR file. |
| 9 | Foundation, alignment, and grouting QC records. |
| 10 | Per-interface tie-in QC and walkdown sign-off. |
| 11 | Electrical pre-energization certificate; VFD installation certification. |
| 12 | Pressure-test certificates against project welding/NDE specification (TBD). |
| 13 | Mechanical completion certificate. |
| 14 | Turnover dossier and operations sign-off. |

## Records

Records the CWP shall require to be retained (anticipated artifacts per DELIVERABLE_REGISTER.csv row 362, plus ASSUMPTION-labeled standard EPC records):

- Construction work package document set. (Source: DELIVERABLE_REGISTER.csv row 362)
- Installation and tie-in workface plan. (Source: DELIVERABLE_REGISTER.csv row 362)
- Construction interface and turnover checklist (thirteen interface sections). (Source: DELIVERABLE_REGISTER.csv row 362; INTERFACE_REGISTER.csv rows 512-524)
- Receiving inspection logs, MTRs (ASSUMPTION).
- Foundation acceptance and grouting records (ASSUMPTION).
- Alignment and bolting records (ASSUMPTION).
- Weld logs and NDE reports for tie-in piping (ASSUMPTION).
- Pressure-test certificates (ASSUMPTION).
- Electrical pre-energization and protection-test records (ASSUMPTION).
- Mechanical completion certificate (ASSUMPTION).
- Turnover dossier to operations supporting DEL-080-06 acceptance. (Source: DELIVERABLE_REGISTER.csv row 365)
