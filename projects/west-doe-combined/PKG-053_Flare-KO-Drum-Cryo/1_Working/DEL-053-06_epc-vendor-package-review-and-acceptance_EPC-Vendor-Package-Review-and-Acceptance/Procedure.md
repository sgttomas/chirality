# Procedure — DEL-053-06: EPC Vendor Package Review and Acceptance (Flare KO Drum (Cryo))

## Purpose

This procedure operationalizes the EPC Integrator's review, integration acceptance, and handoff-readiness determination for the Package Vendor's engineered Flare KO Drum (Cryo) package (PKG-053). It produces the acceptance evidence set required by `Specification.md` (REQ-053-06-01 through REQ-053-06-12). Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-053-06.

## Prerequisites

### Upstream deliverables (within PKG-053) available or in-progress

- DEL-053-01 Scope of Work
- DEL-053-02 Package Datasheet
- DEL-053-03 Construction Work Package
- DEL-053-04 Vendor Engineered Equipment Package
- DEL-053-05 Vendor Document Turnover Package

Source: `DELIVERABLE_REGISTER.csv` PKG-053 rows.

### Declared upstream/downstream dependencies

- None declared during PREPARATION. Source: `_DEPENDENCIES.md`. Dependency edges become active when `Dependencies.csv` is generated.

### Required references on hand for reviewers

- `4-25_Deepcut_DBM.md` (cryogenic flare system context)
- Workbook Packages row 53 (vendor responsibility split, interface list) — access TBD
- `26020-Package_Requirements.docx` package heading 8 — access TBD
- EPC source-of-truth deliverables (DEL-053-01, -02, -03)
- Vendor submittals listed in DEL-053-05

### Reviewer competencies

- Mechanical (pressure vessel / cryogenic service)
- Process / Flare system design
- Electrical (for H-4112-1 immersion heater)
- I&C (for instrumentation tie-ins)
- Construction / Turnover

## Steps

### Step 1 — Assemble the EPC acceptance datum

1.1 Collect controlled copies of DEL-053-01, DEL-053-02, DEL-053-03.
1.2 Confirm each is at an acceptance-ready revision (semantically ready or later, per project lifecycle).
1.3 If any controlling EPC deliverable is not acceptance-ready, halt and escalate; acceptance against an unstable datum is not valid. Source: `Specification.md` REQ-053-06-03.

### Step 2 — Inventory the vendor submittals (REQ-053-06-01)

2.1 Pull the vendor document register from DEL-053-05.
2.2 Reconcile against the document list required by DEL-053-02 (Package Datasheet) and DEL-053-01 (SoW) document deliverable clauses.
2.3 Open a Vendor Document Review Log with one row per submittal: ID, title, revision, vendor-stated status, EPC review code, reviewer, date, comments.
2.4 Flag missing required documents; route to vendor for submittal.

### Step 3 — Verify equipment identity and service classification (REQ-053-06-04, REQ-053-06-05)

3.1 Confirm vendor documents identify V-4110-1 (cryogenic flare KO drum) and H-4112-1 (immersion heater) with correct tag numbers. Source: `SCOPE_LEDGER.csv` SOW-0069; `4-25_Deepcut_DBM.md` §Equipment Schedule row 11.
3.2 Confirm the package service classification (cryogenic; relief below -45.5 degC; non-sour) is reflected in vendor design conditions, materials, and MDMT. Source: `SCOPE_LEDGER.csv` SOW-0070; `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.
3.3 Record results on Package Acceptance Checklist rows for REQ-053-06-04 and REQ-053-06-05.

### Step 4 — Verify mechanical / pressure-vessel design (REQ-053-06-04, REQ-053-06-09)

4.1 Review vendor design report, calculations, and vessel datasheet against DEL-053-02 attribute table.
4.2 Confirm code of construction (ASSUMPTION: ASME BPVC Section VIII; confirm via DEL-053-02), MDMT, impact testing, and material certifications consistent with cryogenic service.
4.3 Review NDE reports, hydrostatic/pressure test charts, and MTRs.
4.4 Specific test list: `TBD` pending DEL-053-02 inspection/test plan.
4.5 Record results on Package Acceptance Checklist rows for REQ-053-06-04 and REQ-053-06-09.

### Step 5 — Verify relief-system fit (REQ-053-06-06, REQ-053-06-07)

5.1 Confirm 610 mm (24 in) cryogenic relief-header inlet sizing and connection orientation match EPC P&ID and tie-in isometrics. Source: `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.
5.2 Confirm vendor design backpressure inputs are consistent with project HP/cryo design basis (preliminary built-up ~695 kPag at peak coincident blowdown; PSV maximum total backpressure target < 1172 kPag). Document accepted deviations if any. Source: `4-25_Deepcut_DBM.md` §Flare Radiation Criteria preface.
5.3 Record results on Package Acceptance Checklist rows for REQ-053-06-06 and REQ-053-06-07.

### Step 6 — Per-interface integration acceptance (REQ-053-06-08)

6.1 For each PKG-053 interface type, complete a discrete Interface Acceptance Log row:
- Process Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power (including H-4112-1 supply)
- EHT (electrical heat tracing — note: cryogenic flare header is NOT heat traced per DBM; verify scope of EHT on adjacent systems only)
- Grounding / Bonding
- I&C / Control Cabling
- Maintenance Access
- Structural / Foundations / Supports

Source: `PACKAGE_REGISTER.csv` PKG-053; `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.

6.2 Each row records: interface description, governing drawing/document, vendor reference, EPC reference, status (Accept / Accept with conditions / Punchlist / Reject), and reviewer signature.

### Step 7 — Verify electrical/heater scope for H-4112-1 (REQ-053-06-09)

7.1 Verify area classification, heater kW rating, watt-density, sheath material, control philosophy, and interlocks for the immersion heater.
7.2 Specific values: `TBD` pending DEL-053-02.
7.3 Record results on Package Acceptance Checklist row.

### Step 8 — Vendor document review (REQ-053-06-01)

8.1 Complete the EPC review code for each submittal in the Vendor Document Review Log.
8.2 Route review comments back to vendor; track to closure.
8.3 Confirm final-revision documents are loaded into project document control.

### Step 9 — Construction Work Package readiness (REQ-053-06-10)

9.1 Confirm rigging, foundations, and tie-in isometrics in DEL-053-03 align with the as-fabricated vendor package.
9.2 Confirm turnover checklist in DEL-053-03 is populated and executable at delivery.
9.3 Record results on Package Acceptance Checklist row for REQ-053-06-10.

### Step 10 — Disposition and Acceptance Report (REQ-053-06-11, REQ-053-06-12)

10.1 For each checklist line, assign disposition: Accept / Accept with conditions / Punchlist / Reject.
10.2 Open a Punchlist Log for any items that defer resolution beyond acceptance.
10.3 Issue an Acceptance Report cover memo summarizing: scope of review, dispositions, open punchlist items, integration acceptance statement, statement preserving Package Vendor warranty and responsibility (REQ-053-06-12).
10.4 Route for EPC Integrator approval signatures (human-authored; agents do not sign acceptance). Source: governance K-AUTH-1.

### Step 11 — Turnover (REQ-053-06-10)

11.1 Compile turnover evidence package: signed checklist, signed interface log, vendor test/inspection records, vendor document final-revision set, MTRs, hydrotest charts, NDE reports, punchlist log, Acceptance Report cover memo.
11.2 Hand off to the commissioning function per project turnover procedure.

## Verification

| Step | Verification |
|---|---|
| 1 | All three EPC datum documents present and at acceptance-ready revision |
| 2 | Vendor Document Review Log row count matches vendor document register count plus EPC additions |
| 3 | V-4110-1 and H-4112-1 identified; cryogenic non-sour classification recorded |
| 4 | Mechanical/pressure-vessel checklist rows closed with reviewer signatures |
| 5 | Relief-header sizing and backpressure consistency confirmed or deviation accepted |
| 6 | Interface Acceptance Log has one signed row per PKG-053 interface type |
| 7 | Electrical/heater checklist row closed (or TBD documented with path to closure) |
| 8 | All vendor documents have a final EPC review code; comments closed |
| 9 | Construction Work Package readiness row closed |
| 10 | Acceptance Report issued and signed by authorized EPC Integrator personnel |
| 11 | Turnover evidence package transmittal recorded |

## Records

- Vendor Document Review Log
- Package Acceptance Checklist (with traceability columns linking each row to SoW clause, Datasheet attribute, and CWP step)
- Interface Acceptance Log (one signed row per PKG-053 interface type)
- Test / Inspection Evidence Package (MTRs, NDE reports, hydrotest charts, ITP signoffs)
- Turnover Evidence Package (signed checklists, transmittal record)
- Acceptance Report (cover memo)
- Punchlist Log (when applicable)

All records are EPC-controlled documents stored under the project document control system and reflected in the deliverable folder turnover evidence set. Source: `_CONTEXT.md` Anticipated Artifacts; `Specification.md` Documentation.
