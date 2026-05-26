# Procedure — DEL-075-03 Construction Work Package (PKG-075 Cryogenic Unit "Deepcut")

This procedure describes how to **produce** the Construction Work Package artifact set for PKG-075 (Construction Work Package, installation and tie-in workface plan, construction interface and turnover checklist) and how its outputs are **used** to execute the field work.

## Prerequisites

- Accepted decomposition snapshot: GATE-07 Final Published 2026-05-24 (`_REFERENCES.md`).
- _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md present in deliverable folder (verified).
- Authoritative source slice: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Construction Responsibility, Interfaces, §2 Layout/Spacing) — locally accessible.
- 26020-Package_Requirements.docx package heading 29 — location TBD as text; obtain and slice before requirements R-8/R-9 can be closed.
- Logical upstream deliverables (not formally declared in `_DEPENDENCIES.md`): DEL-075-01 (Scope of Work), DEL-075-02 (Package Datasheet), DEL-075-04 (Vendor Engineered Equipment Package), DEL-075-05 (Vendor Document Turnover).
- Project HSE, permit-to-work, and QA/QC governance documents — TBD (not localized in accessible sources).

## Steps

### Step 1 — Confirm package identity and split of authority
- Confirm tag `26020-01-PT-28-001`, vendor-vs-EPC split per PACKAGE_REGISTER.csv row 52.
- Record the construction-responsibility split per DBM lines 101–127.
- Verification: split-of-authority table in Datasheet matches PACKAGE_REGISTER and DBM.

### Step 2 — Build the tie-in register
- Enumerate every interface family from PACKAGE_REGISTER.csv row 52 (12 families listed in Specification R-1).
- For each tie-in, assign per-tie-in responsibility (EPC Integrator / Tourmaline / Package Vendor / external). Flag external-interface items per DBM lines 117 and 174 as "responsibility to be confirmed per tie-in."
- Run joint tie-in planning sessions (DBM line 127); record outcomes against the register.
- Verification: every interface family has at least one tie-in row; every external-interface row has a named owner or an explicit TBD with action assignee and date.

### Step 3 — Constructability and layout coordination
- Cross-check the construction sequence against DBM §2 (layout and spacing basis, line 182) and §2.6 (interfaces, line 308).
- Confirm access routes, maintainability envelopes, hazardous-area separation, emergency response access (DBM line 233, lines 315–319).
- Verification: a constructability review record exists, signed by EPC and Tourmaline construction representatives.

### Step 4 — Define inspection, NDE, and testing scope
- Populate the Inspection and Test Plan (ITP), NDE schedule, hydrotest/leak-test plan, and cleanliness/dry-out scope.
- Source: 26020-Package_Requirements.docx heading 29 (location TBD); applicable jurisdictional pressure-vessel/piping codes (TBD).
- Verification: ITP and NDE schedule exist and are referenced from the CWP; gaps are marked TBD with owner and required-by date.

### Step 5 — Build the installation and tie-in workface plan
- Sequence: receiving, off-load, set, hookup, terminations, instrument hookup, loop checks, leak/pressure test, cleanliness/dry-out, energization readiness, MC walkdown.
- Reference DBM lines 111–125 for the field-scope skeleton.
- Verification: workface plan exists; activities reference SOW-0063..SOW-0066 coverage.

### Step 6 — Build the construction interface and turnover checklist
- Define mechanical-completion (MC) acceptance criteria, punch-list classes, turnover record set (weld maps, NDE reports, hydrotest records, loop checks, electrical termination records).
- Define handover to commissioning organization.
- Verification: checklist exists; records set is enumerated; handover signatures are defined.

### Step 7 — Issue, review, and update
- Issue the CWP package (CWP narrative, tie-in register, workface plan, turnover checklist) for EPC Integrator review and Tourmaline construction concurrence.
- Treat the workface plan and tie-in register as living documents and re-issue at each layout/P&ID/vendor-drawing milestone (per joint-planning progressive basis, DBM line 127).
- Verification: review record stored; revision history maintained.

### Step 8 — Execute and capture records (field use of the CWP)
- Tourmaline field-construction executes per the workface plan and DBM construction-responsibility table.
- EPC Integrator manages interfaces and tie-ins; Package Vendor supports per vendor scope.
- Records produced per Step 6 are filed into the turnover record set.
- Verification: turnover checklist signed, all required records present.

## Verification

| Check | Pass criterion |
|---|---|
| All four documents present | Datasheet, Specification, Guidance, Procedure exist in deliverable folder |
| Split-of-authority recorded | Datasheet "Attributes" rows for Package Vendor scope and EPC Integrator scope match PACKAGE_REGISTER.csv row 52 |
| Tie-in coverage | Tie-in register covers all 12 interface families from PACKAGE_REGISTER.csv row 52 |
| DBM construction-responsibility traceability | Each Tourmaline-scope row in Datasheet "Construction" cites a DBM line in the range 107–125 |
| Workface plan present | Anticipated artifact "installation and tie-in workface plan" exists or is explicitly scheduled |
| Turnover checklist present | Anticipated artifact "construction interface and turnover checklist" exists or is explicitly scheduled |
| Source-grounding | Every non-TBD requirement cites a source location; TBDs name the missing source and required-by date |

## Records

- Construction Work Package (CWP) narrative document.
- Tie-in register / isolation matrix.
- Installation and tie-in workface plan.
- Constructability review record.
- Inspection and Test Plan (ITP); NDE schedule; hydrotest/leak-test packs (specific content TBD pending package-requirements docx slice).
- Mechanical Completion (MC) walkdown punch list.
- Construction interface and turnover checklist (signed at handover).
- Turnover record set: weld maps, NDE reports, hydrotest records, instrument calibration certs, loop checks, electrical termination records (specific list TBD pending source).
- Revision history for all living documents (workface plan, tie-in register).
