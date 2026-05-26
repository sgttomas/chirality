# Specification — DEL-105-03 Construction Work Package (Platforms)

## Scope

### In scope

This Construction Work Package (CWP) covers the physical installation, construction, inspection, tie-in, and turnover of the workbook-defined Structural package "Platforms" (PKG-105, CoA `26020-01-36-005`, WBS 01) under SOW-0261. The CWP set comprises three artifacts:

- `ART-B033D6C5F7` — Construction work package narrative
- `ART-C143830D41` — Installation and tie-in workface plan
- `ART-BEC8A111DC` — Construction interface and turnover checklist

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-105-03; `ARTIFACT_REGISTER.csv` DEL-105-03 rows; `SCOPE_LEDGER.csv` SOW-0261.

### Out of scope

- Vendor engineering and detailed structural design of the platform structures themselves; carried by DEL-105-04 (EPC / Structural Discipline Production Package). Source: `DELIVERABLE_REGISTER.csv` DEL-105-04.
- Package datasheet and vendor handoff technical content; carried by DEL-105-02. Source: `DELIVERABLE_REGISTER.csv` DEL-105-02.
- Whole-facility scope-of-work narrative and tagged equipment identity for the package; carried by DEL-105-01. Source: `DELIVERABLE_REGISTER.csv` DEL-105-01.
- Field execution of construction (the CWP plans construction; the field work is the downstream product of the CWP).

## Requirements

Requirement IDs use the pattern `R-<area>-<n>`. Every requirement cites its source slice.

### R-SCO — Scope and boundary

- **R-SCO-1.** The CWP shall identify the package by its workbook identifiers (PackageName "Platforms", Workbook ID# 105, CoA `26020-01-36-005`, WBS 01, Discipline Structural). Source: Workbook Packages ID# 105; `PACKAGE_REGISTER.csv` PKG-105.
- **R-SCO-2.** The CWP shall record SOW-0261 as the in-scope scope-of-work line. Source: `SCOPE_LEDGER.csv` SOW-0261.
- **R-SCO-3.** The CWP shall reference the package-level Gate 7 decomposition snapshot as the authoritative basis. Source: `_REFERENCES.md`.

### R-RESP — Responsibility

- **R-RESP-1.** The CWP shall name the EPC Integrator as the accountable producer of the package; downstream discipline-subcontractor assignment for execution remains source-dependent. Source: `DELIVERABLE_REGISTER.csv` DEL-105-03 ResponsibleParty; `PACKAGE_REGISTER.csv` PKG-105 ResponsibilityModel.
- **R-RESP-2.** The CWP shall reflect that no separate vendor-package ownership model is inferred for PKG-105. Source: `PACKAGE_REGISTER.csv` PKG-105.

### R-INT — Interfaces

- **R-INT-1.** The CWP shall plan tie-ins for the three workbook-marked physical interfaces for PKG-105:
  1. Area / Exterior Lighting (`IFC-26E3DCAD56`),
  2. Grading / Site Drainage / Spill Containment (`IFC-07C472C58B`),
  3. Structural / Foundations / Supports (`IFC-B7C0A01E38`).
  Source: Workbook Packages ID# 105 marked columns; `INTERFACE_REGISTER.csv` PKG-105.
- **R-INT-2.** For each interface, the construction interface and turnover checklist (`ART-BEC8A111DC`) shall record: counterparty/owner, tie-in location, installation method, inspection requirement, and turnover sign-off. Source: artifact description in `ARTIFACT_REGISTER.csv` `ART-BEC8A111DC`.
- **R-INT-3.** The CWP shall carry the Gate 6 disposition for the Interface Review Note: "Platform-to-equipment tie-ins should be confirmed by layout/model; the EPC Integrator owns these tie-ins through the overall 3D model and integrated P&ID set." Source: `INTERFACE_REGISTER.csv` PKG-105 InterfaceReviewNotes; `PACKAGE_REGISTER.csv` PKG-105 InterfaceReviewNotes.
- **R-INT-4.** Interfaces not marked in the workbook for PKG-105 (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Cathodic Protection, I&C/Control Cabling, Communications/Network, Building HVAC/Services, Fire & Gas, Maintenance Access, Product Loading, Pipeline/Pigging) are out of scope for this CWP unless added by a later decomposition update. Source: Workbook Packages ID# 105 (blank columns).

### R-STR — Structural execution basis

- **R-STR-1.** The CWP shall identify the structural design basis documents (drawings, code references, anchor patterns, lift / erection plan basis) on which field execution depends. ASSUMPTION: detailed basis documents are TBD (location TBD) at this stage because `26020-Package_Requirements.docx` contains no Platforms / `26020-01-36-005` section. Resolution path: DEL-105-02 (Package Datasheet) and DEL-105-04 (Discipline Production Package).
- **R-STR-2.** The CWP shall plan foundation installation and acceptance prior to platform erection. Source: standard construction sequencing for structural foundations / supports interface (`IFC-B7C0A01E38`). ASSUMPTION at the source-slice level (no clause cited).

### R-CMN — Mechanical completion / turnover

- **R-CMN-1.** The construction interface and turnover checklist shall be completed and signed for each interface before mechanical completion. Source: `ARTIFACT_REGISTER.csv` `ART-BEC8A111DC` description ("turnover evidence").
- **R-CMN-2.** Installation records (anchor torque/verification, weld and bolt records as applicable, NDE where applicable, coating QA where applicable) shall be produced and turned over. ASSUMPTION: specific record set determined by DEL-105-04 design output (record types not stated in PKG-105 source materials).
- **R-CMN-3.** Grading / site drainage / spill containment continuity around platforms (per `IFC-07C472C58B`) shall be verified and recorded as part of mechanical completion. Source: `INTERFACE_REGISTER.csv` `IFC-07C472C58B`.
- **R-CMN-4.** Area / exterior lighting installation and acceptance around platforms (per `IFC-26E3DCAD56`) shall be verified and recorded. Source: `INTERFACE_REGISTER.csv` `IFC-26E3DCAD56`.

### R-ART — Artifact existence

- **R-ART-1.** All three artifacts (`ART-B033D6C5F7`, `ART-C143830D41`, `ART-BEC8A111DC`) shall exist and be produced under this deliverable. Source: `ARTIFACT_REGISTER.csv` DEL-105-03.

## Standards

| Standard / basis | Applicability | Citation |
|---|---|---|
| Workbook Packages row ID# 105 (CoA `26020-01-36-005`) | Authoritative scope and interface basis | `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` |
| Project decomposition Gate 7 snapshot | Authoritative deliverable / scope / artifact / interface / objective basis | `_REFERENCES.md`; `GATE-07_Final_Published_2026-05-24/*.csv` |
| DBM-Deepcut design basis memo | Project structural design basis context | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Platforms-specific section: location TBD (no match on review) |
| `26020-Package_Requirements.docx` | Equipment-package basis where applicable | No section for Platforms / `26020-01-36-005` located on review; treated as not applicable to this row |
| Project structural codes (e.g., national building code, AISC, etc.) | ASSUMPTION: likely applicable to platform structural design and installation; specific codes are TBD (location TBD); resolution path is DEL-105-04 |  |

## Verification

| Requirement | Verification approach |
|---|---|
| R-SCO-1, R-SCO-2, R-SCO-3 | CWP narrative content check against workbook row and decomposition registers. |
| R-RESP-1, R-RESP-2 | CWP narrative content check; responsibility assignment record on file. |
| R-INT-1, R-INT-4 | Row-by-row check of `ART-BEC8A111DC` against `INTERFACE_REGISTER.csv` PKG-105 set. |
| R-INT-2 | Per-row completeness audit (counterparty, location, method, inspection, sign-off). |
| R-INT-3 | Disposition statement present in CWP narrative and in the interface review row(s). |
| R-STR-1, R-STR-2 | Workface plan (`ART-C143830D41`) shows foundation-before-erection sequencing; basis documents referenced (or `TBD` carried with resolution route). |
| R-CMN-1..R-CMN-4 | Turnover package complete; per-interface sign-off; lighting and drainage acceptance records present. |
| R-ART-1 | Artifact-folder inventory check against `ARTIFACT_REGISTER.csv` DEL-105-03. |

## Documentation

Required artifacts (per `ARTIFACT_REGISTER.csv` DEL-105-03):

- `ART-B033D6C5F7` — Construction work package narrative.
- `ART-C143830D41` — Installation and tie-in workface plan.
- `ART-BEC8A111DC` — Construction interface and turnover checklist.

Supporting records (per R-CMN; record-type list is ASSUMPTION pending DEL-105-04):

- Foundation acceptance record(s) for each platform.
- Platform erection / anchor verification records.
- Coating / galvanization QA records (if applicable; TBD per DEL-105-04).
- Grading and spill-containment continuity-of-protection records for the platform footprint.
- Area / exterior lighting installation and acceptance records around platforms.
- Mechanical completion punch-list closure record.
- Signed turnover package.
