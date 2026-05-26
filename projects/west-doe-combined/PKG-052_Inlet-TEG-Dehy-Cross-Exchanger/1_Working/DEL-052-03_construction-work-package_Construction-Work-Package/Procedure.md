# Procedure — DEL-052-03 Construction Work Package (Inlet / TEG Dehy Cross Exchanger)

**Interpretation:** This Procedure describes the steps required to **produce** the Construction Work Package deliverable (the CWP narrative, the installation/tie-in workface plan, and the construction interface/turnover checklist). Steps to execute construction in the field are downstream products of the CWP itself and are not redefined here.

## Purpose

Provide the EPC Integrator with a repeatable, source-grounded procedure for assembling the PKG-052 Construction Work Package (ART-2444495F85), the Installation and Tie-In Workface Plan (ART-F79E686395), and the Construction Interface and Turnover Checklist (ART-0E330BEA94), satisfying the requirements in `Specification.md` and the principles in `Guidance.md`.

## Prerequisites

### Upstream deliverables (declared and inferred)

- **DEL-052-01 (Scope of Work and Equipment List)** — required to lock the in-scope SOW set (SOW-0103..SOW-0106) and tagged equipment E-5718-1. ASSUMPTION: cross-deliverable handoff implied by PKG-052 deliverable ordering; not declared in `_DEPENDENCIES.md`.
- **DEL-052-02 (Package Datasheet / Vendor Handoff Basis)** — required to fix process conditions and pipe-class basis at tie-in interfaces. ASSUMPTION as above.
- **DEL-052-04 (Vendor Engineered Equipment Package)** — required for vendor general arrangement, anchor pattern, lift plan basis, certified drawings. ASSUMPTION as above.
- **DEL-052-05 (Vendor Document Turnover Package)** — required for installation manuals, U-1 / MDR, recommended inspection plans, vendor inspection records. Source: `Specification.md` R-CMN-2.

### Authoritative basis documents

- Project decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` row `DEL-052-03`
  - `PACKAGE_REGISTER.csv` row `PKG-052`
  - `SCOPE_LEDGER.csv` rows `SOW-0103..SOW-0106`
  - `ARTIFACT_REGISTER.csv` rows `ART-2444495F85`, `ART-F79E686395`, `ART-0E330BEA94`
  - `INTERFACE_REGISTER.csv` PKG-052 (9 rows)
  - `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003..OBJ-010`
- Deliverable-local files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`.
- Project source materials (location TBD — not deliverable-local for clause-level citation):
  - `26020-Package_Requirements.docx` package heading 7
  - `26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx`
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` (notably SEC-15 sour-service basis)

### Tooling / role prerequisites

- EPC Integrator is the accountable producer of this deliverable. Source: `DELIVERABLE_REGISTER.csv` DEL-052-03.
- Project P&IDs, line list, area plot plan, civil foundation drawings, electrical schematics. Specific document identifiers: TBD (location TBD).

## Steps

### Step 1 — Lock scope basis (R-SCO, R-RESP)
1. Confirm in-scope SOW set (SOW-0103..SOW-0106) against `DEL-052-01` and `SCOPE_LEDGER.csv`.
2. Confirm tagged equipment E-5718-1 (TEMA 'R' BEM, duty 5514.3 kW / 18.82 MMBTU/hr) against `SOW-0105`.
3. Lock the vendor/EPC split per `PACKAGE_REGISTER.csv` PKG-052 ResponsibilityModel.

### Step 2 — Inventory the 9 PKG-052 interfaces (R-INT-1)
1. Enumerate the 9 interface rows from `INTERFACE_REGISTER.csv` for PKG-052:
   IFC-E97F55B211 (Process Piping), IFC-A891689774 (Utility Piping), IFC-DDB08C1331 (Drain/Containment), IFC-C3CE1B5E7D (EHT), IFC-398F6BFCE1 (Grounding/Bonding), IFC-F79647C246 (Area/Exterior Lighting), IFC-94006D4790 (I&C / Control Cabling), IFC-0D3B12DEF3 (Maintenance Access), IFC-A40EC04E30 (Structural / Foundations / Supports).
2. Create one row per interface in the construction interface and turnover checklist (ART-0E330BEA94) with placeholders for: tie-in location, owner, installation method, inspection requirement, turnover sign-off.
3. Flag the absences (no Relief/Flare/Vent, Electrical Power, Fire & Gas, or Building HVAC rows) per Guidance §Considerations and Conflict Table entries CFT-001, CFT-002; do not invent rows.

### Step 3 — Resolve "by others" handoffs (R-INT-4, R-CIV-2, R-ELE-2, R-INS-2)
1. For each "by others" item per `SOW-0106` (interconnecting piping, DCS integration, foundations, electrical supply to MCC):
   a. Identify the owning package / EPC scope.
   b. Define the handoff state (acceptance criteria) required from the owner before PKG-052 tie-in can proceed.
   c. Record handoff in the construction interface and turnover checklist.

### Step 4 — Assemble the Construction Work Package narrative (ART-2444495F85)
1. Populate Identification block from `Datasheet.md` §Identification.
2. Populate Operating/Design Conditions block from `Datasheet.md` §Conditions (carry the m³/hr transcription caveat from CFT-003 as a footnote until confirmed against vendor RFQ).
3. Restate Specification requirements (R-RESP, R-SCO, R-INT, R-CIV, R-ELE, R-INS, R-UTL, R-SAF, R-CMN, R-ART) as executable construction sections.
4. Cross-reference vendor data via DEL-052-04 / DEL-052-05; mark vendor-data dependencies that are not yet available as `Pending Vendor Issue` rather than inferring values.

### Step 5 — Assemble the Installation and Tie-In Workface Plan (ART-F79E686395)
1. Decompose the work into workface units. At minimum, separate the **sour-side** workface unit (inlet-separator → exchanger → inlet-compressor lines) and the **sweet-side** workface unit (amine-unit-side lines) per Guidance §Considerations (sour-side vs. sweet-side tie-in distinction).
2. For each workface unit, specify: pre-requisite acceptance (e.g., foundation acceptance for setting), material control (PMI receipt, hardness control plan for sour service per R-SAF-1), weld procedures and inspection (visual, NDE, PWHT where required), pressure-test plan (hydrotest default; alternative-test rationale TBD per Guidance §Trade-offs), insulation and EHT plan (per Guidance §Considerations — winterization at -40 °C ambient).
3. Sequence equipment setting after foundation acceptance (R-CIV-2).
4. Specific line-list and pipe-class data: pull from DEL-052-02 / DEL-052-04. Where not yet available, leave as `Pending Vendor / DEL-052-02 Issue` rather than inventing values.

### Step 6 — Assemble the Construction Interface and Turnover Checklist (ART-0E330BEA94)
1. One row per interface from Step 2 (9 rows minimum).
2. Add mechanical-completion criteria rows per R-CMN-1 (punch-list closure, vendor MDR / U-1 receipt, hydrotest record, code-stamp verification, EHT continuity, grounding tests, loop checks).
3. Add maintenance-access and winterization walkdown rows per R-CMN-3.
4. Add open-item disposition section per OBJ-010 (controlled open-item closure into commissioning).

### Step 7 — Apply sour-service and pressure-equipment rigor (R-SAF, R-CMN)
1. Reflect PMI-at-receipt, weld-hardness control, hydrotest plan, code-stamp verification, sour-service walkdown into the CWP narrative and checklist (R-SAF-1).
2. Identify jurisdictional pressure-equipment registration / inspection path. Specific authority and registration identifier: TBD (location TBD — DBM-Deepcut SEC-15 not deliverable-local).
3. Confirm PSV / relief routing assumption per CFT-001 against P&IDs before construction lock-in; record disposition in the checklist.

### Step 8 — Cross-document consistency check (skill QA)
1. Verify identifiers used in Procedure match those in `Datasheet.md`, `Specification.md`, `Guidance.md` (DEL-052-03, PKG-052, E-5718-1, ART-2444495F85, ART-F79E686395, ART-0E330BEA94, 9 IFC IDs).
2. Verify numeric values (design pressure 9756 kPag, design temperature 66 °C, ambient -40 °C / +35 °C, duty 5514.3 kW / 18.82 MMBTU/hr) match `Datasheet.md` §Conditions.
3. Verify Conflict Table items (CFT-001..CFT-004) are reflected in the procedural disposition steps and not silently resolved.

### Step 9 — Submit for review and acceptance (R-CMN, OBJ-010)
1. Issue Construction Work Package narrative, Installation and Tie-In Workface Plan, and Construction Interface and Turnover Checklist as a single tranche to EPC Integrator review.
2. Coordinate with DEL-052-06 (EPC vendor-package review and acceptance) for cross-acceptance of vendor-package-dependent sections. ASSUMPTION: cross-deliverable handoff implied by PKG-052 deliverable ordering.
3. On acceptance, the deliverable is eligible for Gate 5 status advancement per project gating (specific gate rules: TBD — not deliverable-local).

## Verification

| Step | Verification |
|---|---|
| Step 1 | SOW IDs and tagged equipment exactly match `SCOPE_LEDGER.csv` and `PACKAGE_REGISTER.csv` |
| Step 2 | 9 interface rows present in checklist; IFC IDs match `INTERFACE_REGISTER.csv` PKG-052 |
| Step 3 | Each "by others" item from SOW-0106 has an owner and handoff acceptance recorded |
| Step 4 | CWP narrative present (ART-2444495F85) covering all Specification requirements |
| Step 5 | Workface plan present (ART-F79E686395) with sour-side and sweet-side units separated; sour-service controls (PMI, hardness, hydrotest) explicit |
| Step 6 | Checklist present (ART-0E330BEA94) with mechanical-completion, walkdown, and open-item rows |
| Step 7 | Sour-service controls visible; PSV/relief assumption (CFT-001) explicitly dispositioned |
| Step 8 | Cross-document identifiers and values consistent; no Conflict Table item silently resolved |
| Step 9 | Tranche reviewed and accepted; record archived |

## Records

- Construction Work Package narrative (ART-2444495F85) — produced.
- Installation and Tie-In Workface Plan (ART-F79E686395) — produced.
- Construction Interface and Turnover Checklist (ART-0E330BEA94) — produced.
- Mechanical-completion / turnover package: punch-list closure record, vessel MDR / U-1 receipt, hydrotest record(s), PMI receipt records, weld-hardness records, code-stamp verification, EHT continuity test record, grounding test record, loop-check record, maintenance-access walkdown, winterization walkdown. Specific record format and retention: TBD (location TBD).
- Open-item register at commissioning handoff, per OBJ-010.
- Conflict Table dispositions (CFT-001..CFT-004) reflected in CWP narrative and/or checklist.

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- `Datasheet.md`, `Specification.md`, `Guidance.md` (this deliverable)
- `DELIVERABLE_REGISTER.csv` DEL-052-03, `PACKAGE_REGISTER.csv` PKG-052, `SCOPE_LEDGER.csv` SOW-0103..SOW-0106, `ARTIFACT_REGISTER.csv` DEL-052-03, `INTERFACE_REGISTER.csv` PKG-052, `OBJECTIVE_REGISTER.csv` OBJ-001/OBJ-003..OBJ-010
- 26020-Package_Requirements.docx package heading 7 (location TBD; binary `.docx` under `_Sources/`)
- 26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx (location TBD)
- DBM-Deepcut/4-25_Deepcut_DBM.md (location TBD)
