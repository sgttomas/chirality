# Procedure — DEL-105-03 Construction Work Package (Platforms)

**Interpretation:** This Procedure describes the steps required to **produce** the Construction Work Package deliverable for PKG-105 — the CWP narrative (`ART-B033D6C5F7`), the installation and tie-in workface plan (`ART-C143830D41`), and the construction interface and turnover checklist (`ART-BEC8A111DC`). Field execution of construction is a downstream product of the CWP itself and is not redefined here.

## Purpose

Provide the EPC Integrator with a repeatable, source-grounded procedure for assembling the PKG-105 Platforms Construction Work Package satisfying the requirements in `Specification.md` and the principles in `Guidance.md`.

## Prerequisites

### Upstream deliverables (inferred; not declared in `_DEPENDENCIES.md`)

- **DEL-105-01 (Scope of Work)** — required to lock the in-scope SOW boundary (SOW-0261) and the package identity / tagged-equipment list. ASSUMPTION: handoff implied by PKG-105 deliverable ordering; `_DEPENDENCIES.md` records "None declared during PREPARATION".
- **DEL-105-02 (Package Datasheet)** — required to fix platform tagging, equipment association, interface technical handoff data, and design-basis values needed for installation planning. ASSUMPTION as above.
- **DEL-105-04 (EPC / Structural Discipline Production Package)** — required for structural design basis, anchor patterns, lift / erection plan basis, coating spec, and certified drawings. ASSUMPTION as above; `DELIVERABLE_REGISTER.csv` DEL-105-04 explicitly records source-limited / open status.

### Authoritative basis documents

- Project decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` row `DEL-105-03_construction-work-package`
  - `PACKAGE_REGISTER.csv` row `PKG-105`
  - `SCOPE_LEDGER.csv` row `SOW-0261`
  - `ARTIFACT_REGISTER.csv` rows `ART-B033D6C5F7`, `ART-C143830D41`, `ART-BEC8A111DC`
  - `INTERFACE_REGISTER.csv` PKG-105 rows (`IFC-26E3DCAD56`, `IFC-07C472C58B`, `IFC-B7C0A01E38`)
  - `OBJECTIVE_SCOPE_MAP.csv` rows for PKG-105 (`OBJ-001`, `OBJ-005`, `OBJ-008`, `OBJ-010`)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`.
- Project source materials:
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` ID# 105 (CoA `26020-01-36-005`).
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no Platforms-specific section located on review — location TBD).
  - `_Sources/26020-Package_Requirements.docx` (no Platforms / `26020-01-36-005` section — not applicable to this row).

### Tooling / role prerequisites

- EPC Integrator is the accountable producer (per `DELIVERABLE_REGISTER.csv` DEL-105-03 / `_CONTEXT.md`).
- Project 3D model snapshot identifier (for platform-to-equipment tie-in confirmation per `INTERFACE_REGISTER.csv` PKG-105 InterfaceReviewNotes) — specific snapshot ID: TBD (location TBD).
- Integrated P&ID set revision identifier — TBD (location TBD).

## Steps

### Step 1 — Lock scope basis (R-SCO, R-RESP)

1. Confirm coverage of SOW-0261 against DEL-105-01 (Scope of Work) output.
2. Confirm package identity (PackageName "Platforms"; Workbook ID# 105; CoA `26020-01-36-005`; WBS 01; Discipline Structural) against `PACKAGE_REGISTER.csv` PKG-105 and Workbook Packages ID# 105.
3. Record EPC Integrator as accountable producer; flag that no separate vendor-package ownership model is inferred for PKG-105.

**Output:** CWP narrative §1 (Scope, Identity, Responsibility).

### Step 2 — Build interface tie-in matrix (R-INT)

1. Pull the three PKG-105 interface rows from `INTERFACE_REGISTER.csv`: Area / Exterior Lighting (`IFC-26E3DCAD56`), Grading / Site Drainage / Spill Containment (`IFC-07C472C58B`), Structural / Foundations / Supports (`IFC-B7C0A01E38`).
2. For each interface, enter a row in the construction interface and turnover checklist (`ART-BEC8A111DC`) with: counterparty package / owner, tie-in location (referencing the 3D model snapshot), installation method, inspection requirement, and turnover sign-off (R-INT-2).
3. Record the Gate 6 disposition that the EPC Integrator owns platform-to-equipment tie-ins through the overall 3D model and integrated P&ID set (R-INT-3).
4. Explicitly note that no other workbook interface columns are marked for PKG-105 and that no further interface rows are planned for this CWP (R-INT-4).

**Output:** Populated construction interface and turnover checklist (`ART-BEC8A111DC`, draft).

### Step 3 — Sequence the workface plan (R-STR, R-CMN)

1. Define the construction sequence (ASSUMPTION-based standard sequencing in the absence of a project-specific procedure):
   1. Confirm the structural design basis from DEL-105-04 (drawings, anchor pattern, coating spec, member list).
   2. Site preparation around the platform footprint; protect existing grading / drainage / spill containment (`IFC-07C472C58B`).
   3. Foundation installation (piles, pads, or anchor blocks per DEL-105-04 design) and acceptance.
   4. Platform structural erection (lift plan per DEL-105-04 lift/erection basis); anchor verification.
   5. Welding, bolting, and field connection completion; NDE where required by DEL-105-04 / governing code.
   6. Coating / galvanization touch-up after erection (per DEL-105-04 coating spec).
   7. Area / exterior lighting installation around / on platforms and acceptance (`IFC-26E3DCAD56`).
   8. Grading / drainage / spill-containment restoration and continuity verification around the platform footprint (`IFC-07C472C58B`).
   9. Platform-to-equipment tie-in confirmation against the 3D model snapshot and integrated P&ID set (per Gate 6 disposition).
   10. Mechanical completion walkdown; punch-list closure; turnover to commissioning.
2. Identify sequence-critical handoffs (DEL-105-04 design release before foundation; foundation acceptance before erection; erection and anchor verification before lighting and tie-in confirmation; containment continuity verification before mechanical completion).
3. Record open items (platform count, equipment tags, coating spec, code-clause basis) as release-for-construction prerequisites routed to DEL-105-02 and DEL-105-04 for closure.

**Output:** Installation and tie-in workface plan (`ART-C143830D41`, draft).

### Step 4 — Assemble the CWP narrative (R-ART-1, R-CMN)

1. Draft the CWP narrative covering: scope and identity, responsibility, the three-interface tie-in plan, the workface sequence, the QA / inspection plan (anchored on the EPC Integrator's structural QA program — specific procedure IDs TBD), the mechanical completion criteria, and the turnover record set.
2. Reference all provenance: `SCOPE_LEDGER.csv` SOW-0261; `INTERFACE_REGISTER.csv` PKG-105 rows; `OBJECTIVE_SCOPE_MAP.csv` PKG-105 rows; `ARTIFACT_REGISTER.csv` DEL-105-03 rows; Workbook Packages ID# 105.
3. Mark every value not resolvable from deliverable-local sources as `TBD (location TBD)` and route to DEL-105-02 / DEL-105-04 for resolution. Do not invent values.

**Output:** Construction work package narrative (`ART-B033D6C5F7`, draft).

### Step 5 — Cross-document consistency sweep

1. Confirm Datasheet, Specification, Guidance, and Procedure agree on: package identity fields; the three-interface set; SOW-0261 coverage; the four-objective set; the artifact triplet; the carried Gate 6 disposition; the open-item list.
2. Resolve any inconsistency in favor of `SCOPE_LEDGER.csv` / `INTERFACE_REGISTER.csv` / `ARTIFACT_REGISTER.csv` / `OBJECTIVE_SCOPE_MAP.csv` / `PACKAGE_REGISTER.csv` text.
3. Where resolution requires a value not deliverable-local, prefer `TBD` and add (or update) a Conflict Table entry in `Guidance.md`.

### Step 6 — Record-set sign-off

1. Confirm artifact identifiers and storage locations:
   - `ART-B033D6C5F7` — Construction work package narrative.
   - `ART-C143830D41` — Installation and tie-in workface plan.
   - `ART-BEC8A111DC` — Construction interface and turnover checklist.
2. Confirm the mechanical-completion record set per R-CMN-1..R-CMN-4 is enumerated and routed to the relevant inspection / commissioning groups.
3. Confirm the open-item closure log (CFT-105-03-002 items: platform count, tags, coating, code basis) is referenced as a release-for-construction prerequisite.

## Verification

| Verification | Method |
|---|---|
| All three artifacts present | Folder inventory check against `ARTIFACT_REGISTER.csv` DEL-105-03 |
| Three-interface plan complete | Row-by-row review of `ART-BEC8A111DC` against `INTERFACE_REGISTER.csv` PKG-105 (3 rows) |
| Gate 6 disposition carried | Disposition text present in CWP narrative and interface checklist |
| Workface sequence honors structural-design dependency | Sequence in `ART-C143830D41` shows DEL-105-04 design release before foundation; foundation acceptance before erection |
| Containment continuity preserved | Containment / drainage continuity record present in turnover package |
| Lighting acceptance recorded | Area / exterior lighting acceptance record present in turnover package |
| Cross-document consistency | Manual diff of Datasheet / Specification / Guidance / Procedure against each other and against the Gate 7 registers |
| Open items routed | CFT entries in `Guidance.md` Conflict Table reference DEL-105-02 / DEL-105-04 resolution path |

## Records

- Construction work package narrative (`ART-B033D6C5F7`)
- Installation and tie-in workface plan (`ART-C143830D41`)
- Construction interface and turnover checklist (`ART-BEC8A111DC`)
- Open-item closure log (release-for-construction prerequisites: platform count, tags, coating spec, code basis)
- Mechanical completion / turnover package:
  - Foundation acceptance record(s)
  - Platform erection and anchor verification records
  - Field connection (weld / bolt) and NDE records (where required by DEL-105-04 / code)
  - Coating / galvanization QA records (per DEL-105-04 coating spec)
  - Area / exterior lighting installation and acceptance records around platforms
  - Grading / drainage / spill-containment continuity-of-protection records
  - Platform-to-equipment tie-in confirmation record (against named 3D model snapshot)
  - Mechanical completion punch-list closure log
  - Signed turnover package
