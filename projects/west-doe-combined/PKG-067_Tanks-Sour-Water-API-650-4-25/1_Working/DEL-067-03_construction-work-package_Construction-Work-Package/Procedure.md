# Procedure — DEL-067-03 Construction Work Package (Tanks, Sour Water (API 650) 4-25)

**Interpretation:** This Procedure describes the steps required to **produce** the Construction Work Package deliverable (the CWP narrative, the installation/tie-in workface plan, and the construction interface/turnover checklist). Steps to execute construction in the field are downstream products of the CWP itself and are not redefined here.

## Purpose

Provide the EPC Integrator with a repeatable, source-grounded procedure for assembling the PKG-067 Construction Work Package (ART-EE79CD3464), the Installation and Tie-In Workface Plan (ART-FE1E5417F6), and the Construction Interface and Turnover Checklist (ART-09F3991C52), satisfying the requirements in `Specification.md` and the principles in `Guidance.md`.

## Prerequisites

### Upstream deliverables (declared and inferred)

- **DEL-067-01 (Scope of Work)** — required to lock the in-scope SOW set (SOW-0225..SOW-0228) and the package boundary. ASSUMPTION: cross-deliverable handoff implied by PKG-067 deliverable ordering; not declared in `_DEPENDENCIES.md` (which records "None declared during PREPARATION").
- **DEL-067-02 (Package Datasheet / Vendor Handoff Basis)** — required to fix process conditions, tank tags/count, design SG, heating/insulation extent, blanket/VRU applicability, and pipe-class basis at tie-in interfaces. ASSUMPTION as above; explicitly named as resolution path for SOW-0228 open items.
- **DEL-067-04 (Vendor Engineered Equipment Package)** — required for vendor general arrangement, anchor pattern, lift / erection plan basis, certified drawings, coating spec, PVRV/EPRV data, and weld maps. ASSUMPTION as above.
- **DEL-067-05 (Vendor Document Turnover Package)** — required for installation manuals, API 650 tank data report, recommended inspection plans, and vendor inspection records. Source: `Specification.md` R-CMN-2.

### Authoritative basis documents

- Project decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` row `DEL-067-03`
  - `PACKAGE_REGISTER.csv` row `PKG-067`
  - `SCOPE_LEDGER.csv` rows `SOW-0225..SOW-0228`
  - `ARTIFACT_REGISTER.csv` rows `ART-EE79CD3464`, `ART-FE1E5417F6`, `ART-09F3991C52`
  - `INTERFACE_REGISTER.csv` PKG-067 (9 rows)
  - `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003..OBJ-010`
- Deliverable-local files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`.
- Project source materials (location TBD — not deliverable-local for clause-level citation):
  - `26020-Package_Requirements.docx` package heading 22
  - `26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` (3-25 sour-water analog)
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` (notably the sour-service basis section)

### Tooling / role prerequisites

- EPC Integrator is the accountable producer of this deliverable. Source: `DELIVERABLE_REGISTER.csv` DEL-067-03; `_CONTEXT.md`.
- Project P&IDs, line list, area plot plan, civil foundation and containment drawings, electrical schematics, CP design, coating spec. Specific document identifiers: TBD (location TBD).

## Steps

### Step 1 — Lock scope basis (R-SCO, R-RESP)

1. Confirm coverage of SOW-0225..SOW-0228 against DEL-067-01.
2. Confirm the vendor/EPC split per PKG-067 ResponsibilityModel and OBJ-004.
3. Record the open-item set from SOW-0228 (service naming, tank count, tags, source headers, design SG, heating/insulation extent, VRU/blanket gas applicability, 3-25 design-basis applicability) as a release-for-construction prerequisite list, owned by DEL-067-02 / DEL-067-04 for resolution.

**Output:** CWP §1 (Scope and Boundary); release-for-construction prerequisite list.

### Step 2 — Build interface tie-in matrix (R-INT)

1. Pull the 9 PKG-067 rows from `INTERFACE_REGISTER.csv`: Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports.
2. For each interface: enter a row in the Construction Interface and Turnover Checklist (ART-09F3991C52) with owner, tie-in location, installation method, inspection requirement, and turnover sign-off (R-INT-2).
3. Add explicit rows for SOW-0227 features that cross interfaces: PVRV/EPRV (under Relief/Flare/Vent); LP fuel-gas blanket (under Process Piping or Relief/Flare/Vent — pending §R-INT-4 / §R-UTL-1 resolution); VRU suction/header (under Process Piping if applicable per SOW-0228); internal coating (under Process Piping inspection scope); CP (Cathodic Protection); EHT where required (planned against facility electrical scope per CFT-001).

**Output:** Populated construction interface / turnover checklist (ART-09F3991C52, draft).

### Step 3 — Sequence the workface plan (R-CIV, R-SAF, R-CMN)

1. Define the construction sequence:
   1. Civil grading and secondary containment (berm / drainage / liner) construction.
   2. Tank foundation (ring wall or slab) installation and acceptance.
   3. Tank erection / setting (field-erected vs. shop-fabricated per vendor — TBD per DEL-067-04).
   4. Weld-out, NDE, PMI, and hardness verification (sour-service rigor per R-SAF-1).
   5. Hydrostatic test per API 650.
   6. Internal coating application after hydrotest dry-out (R-SAF-3); surface prep, DFT, holiday, cure QA.
   7. External insulation and EHT installation where required (per resolved SOW-0228 extent).
   8. PVRV/EPRV installation; blanket-gas system tie-in and leak test; VRU tie-in (if applicable).
   9. Tank instrumentation installation and loop checks; I&C cabling termination.
   10. Cathodic protection installation, reference-cell verification, isolation checks.
   11. Grounding/bonding installation and test; area-lighting installation and acceptance.
   12. Containment closure and final spill-response walkdown.
   13. Mechanical completion walkdown; punch-list; turnover to commissioning.
2. Identify sequence-critical handoffs (foundation acceptance before erection; hydrotest before coating; coating before insulation/EHT close-out; instrument loop check before commissioning handoff).
3. Document SOW-0228 open-item resolution dates as upstream gates against the sequence.

**Output:** Installation and tie-in workface plan (ART-FE1E5417F6, draft).

### Step 4 — Assemble the CWP narrative (R-ART-1, R-CMN)

1. Draft CWP narrative covering: scope, boundary, responsibility, sequence, interface tie-in matrix, sour-service rigor plan, coating plan, hydrotest plan (per API 650), CP plan, EHT plan (conditional), PVRV/EPRV/blanket/VRU plan, containment plan, mechanical completion criteria, and turnover record set.
2. Reference all applicable provenance: `SCOPE_LEDGER.csv` rows, `INTERFACE_REGISTER.csv` rows, `OBJECTIVE_REGISTER.csv` rows, and the project source documents (API 650, DBM-Deepcut sour-service basis, 26020 package requirements, 3-25 analog RFQ where applicable).
3. Mark every value not resolvable from deliverable-local sources as `TBD (location TBD)` and route to DEL-067-02 / DEL-067-04 / DEL-067-05 for resolution.

**Output:** Construction work package narrative (ART-EE79CD3464, draft).

### Step 5 — Cross-document consistency sweep

1. Confirm Datasheet, Specification, Guidance, and Procedure agree on: tank tags (TK-9010-1, TK-9020-1 expected; confirmation TBD); tank count (2); the 9-interface set; the 4-SOW coverage set; the 9-objective set; the artifact triplet; the SOW-0228 open-item list.
2. Resolve any inconsistencies in favor of `SCOPE_LEDGER.csv` / `INTERFACE_REGISTER.csv` / `ARTIFACT_REGISTER.csv` / `OBJECTIVE_REGISTER.csv` text.
3. Where resolution requires a value not deliverable-local, prefer `TBD` and add a Conflict Table entry in `Guidance.md`.

### Step 6 — Record-set sign-off

1. Confirm artifact identifiers and storage locations:
   - ART-EE79CD3464 — Construction work package narrative.
   - ART-FE1E5417F6 — Installation and tie-in workface plan.
   - ART-09F3991C52 — Construction interface and turnover checklist.
2. Identify mechanical-completion record set per R-CMN-1..R-CMN-4: API 650 tank data reports, hydrotest records, weld maps and NDE reports, PMI records, hardness records, coating QA records, CP commissioning records, EHT continuity records (where applicable), PVRV/EPRV verification records, blanket-gas leak-test records, containment acceptance records, instrument loop-check records.
3. Confirm SOW-0228 open-item closure log is referenced as a prerequisite to mechanical completion (R-CMN-4).

## Verification

| Verification | Method |
|---|---|
| All four artifacts present | Folder inventory check against `ARTIFACT_REGISTER.csv` |
| All 9 interfaces planned with turnover entries | Row-by-row review of ART-09F3991C52 against `INTERFACE_REGISTER.csv` PKG-067 |
| SOW-0228 open items tracked to closure | Open-item log entries cross-checked against `SCOPE_LEDGER.csv` SOW-0228 |
| Sour-service rigor evidence present | Records: PMI, weld hardness, hydrotest per API 650, coating QA, code/standard compliance |
| Mechanical completion criteria satisfied | Punch-list closure record; turnover package signed by EPC Integrator and accepted by commissioning |
| Cross-document consistency | Manual diff of Datasheet / Specification / Guidance / Procedure against each other and against registers |

## Records

- Construction work package narrative (ART-EE79CD3464)
- Installation and tie-in workface plan (ART-FE1E5417F6)
- Construction interface and turnover checklist (ART-09F3991C52)
- SOW-0228 open-item closure log (release-for-construction prerequisites)
- Mechanical completion / turnover package:
  - API 650 tank data reports for TK-9010-1 and TK-9020-1
  - Hydrostatic test records (per API 650)
  - Weld maps and NDE reports
  - PMI and weld-hardness records
  - Internal coating QA records (DFT, holiday, cure)
  - External insulation and EHT installation/commissioning records (where required)
  - PVRV/EPRV verification records
  - LP fuel-gas blanket leak-test records
  - VRU tie-in records (if applicable)
  - Cathodic Protection installation and reference-cell records
  - Grounding/bonding and area-lighting acceptance records
  - Instrumentation loop-check records
  - Secondary-containment acceptance and spill-response walkdown records
  - Punch-list closure log
