# Procedure — DEL-096-03 Construction Work Package (PKG-096 Tanks, Sour Condensate API 650)

> Operational document. Describes how to **produce** the Construction Work Package deliverable and the high-level sequence by which the package will be physically constructed and turned over. Items marked `TBD` require project-execution-standard rulings.

## Purpose

Provide the steps to assemble the EPC Integrator's Construction Work Package for PKG-096 — including the installation and tie-in workface plan and the construction interface / turnover checklist — and to record evidence of construction completion ready for handover.

## Prerequisites

### Upstream inputs required

- Authoritative source slice: `26020-Package_Requirements.docx` H1 #48 "26020-03-PT-19-005 - Tanks, Sour Condensate" (read).
- Package register row PKG-096 (`PACKAGE_REGISTER.csv`).
- Deliverable register row DEL-096-03 (`DELIVERABLE_REGISTER.csv`).
- Interface register entries for PKG-096 (from `INTERFACE_REGISTER.csv`) — **read TBD**.
- Objective-deliverable mapping row(s) for DEL-096-03 (from `OBJECTIVE_DELIVERABLE_MAP.csv`) — **read TBD**.
- Vendor deliverables expected before construction can be planned in detail (per `26020-Package_Requirements.docx` H1 #48, Vendor Engineering Deliverables):
  - MEC-016 Equipment General Arrangement Drawing
  - MEC-017 Equipment Installation / Setting Drawings
  - MEC-018 Lifting / Handling Study
  - PIP-004 Tie-In List / Tie-In Scope Sheets
  - PIP-007 Piping Plans and Sections
  - PIP-024 Hydrotest / Pressure Test Packages
  - MEC-025 Mechanical Equipment IOM Manual
  - QLT-003 Inspection and Test Plan (ITP)

### Declared dependencies

`_DEPENDENCIES.md` declares no upstream or downstream dependencies at this time (PREPARATION default). See Conflict Table entry CFL-096-03-03 in `Guidance.md` — running `TASK + dependency-extract` is recommended before construction execution.

### Required references

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable).
- API 650 (modified) and API 2000 — **location TBD**.
- NACE sour-service standards — **location TBD** (ASSUMPTION: MR0175 family).

## Steps

### Phase A — Produce the Construction Work Package document

1. **Read the source slice.** Confirm scope, equipment list, design conditions, applicable interface types, and "By Others" list from `26020-Package_Requirements.docx` H1 #48.
2. **Capture identification and conditions.** Transcribe equipment tags, capacities, codes, coating, design pressure/temperature, design flows, and fill limit into the construction work package's "Equipment Summary" section. (Cross-checks `Datasheet.md`.)
3. **Enumerate EPC construction scope.** From the source's "By Others" list (foundations, mounting, electrical/instrumentation, platforms, staircase), build the EPC scope breakdown; cross-reference applicable interface types.
4. **Map interfaces.** For each of the nine applicable interface types, create a numbered interface ticket placeholder linked to the corresponding `INTERFACE_REGISTER.csv` row. **Detail mapping TBD pending interface-register read.**
5. **Bind quality and inspection.** Reference vendor QLT-003 ITP and any project ITRs governing field welds, NDE, coating, hydrotest, and electrical/instrument loop checks.
6. **Compile the Construction Work Package document.** Assemble sections: Scope, Equipment Summary, EPC Scope Breakdown, Interface List, Inspection & Test Strategy, Hold Points, Risks, References. **Document filename TBD.**

### Phase B — Produce the Installation and Tie-In Workface Plan

7. **Sequence the work.** Define foundation → underground utilities (CP anodes, grounding grid, drains) → tank arrival → tank setting (per MEC-018 lifting study) → coating verification → above-ground tie-ins (process piping, relief/flare, blanket gas) → I&C → lighting → grading/containment final → testing → turnover.
8. **Identify hold points and witness points.** At minimum: foundation pre-pour; tank setting completion; weld map sign-off; hydrotest; PVRV/EPRV bench-test acceptance; loop check; high-level shutdown functional test; containment volume verification.
9. **Allocate workfaces.** Group steps into workface packages with manpower, equipment, prerequisites, and durations. **Detail TBD per project workface-planning standard.**

### Phase C — Produce the Construction Interface and Turnover Checklist

10. **One row per applicable interface (nine rows).** Columns: interface type; counter-package / scope reference; pre-tie-in checks; tie-in execution checks; post-tie-in verification; signature blocks (EPC, vendor, operations).
11. **Add turnover gates.** Mechanical completion; pre-commissioning; commissioning readiness; operations acceptance.

### Phase D — Execute, Inspect, and Hand Over

12. Execute construction per the workface plan; record ITRs against the ITP.
13. Witness hold points; collect and bind evidence.
14. Walk down each interface ticket; close per checklist (Phase C).
15. Compile the turnover dossier; obtain Operations sign-off; transmit to the Owner with a complete vendor data book reference.

## Verification

| Verification | How |
|---|---|
| All nine applicable interfaces signed off | Inspect completed interface turnover checklist (Phase C). |
| Hydrotest passed | Hydrotest/pressure test record per PIP-024. |
| Coating integrity | DFT and holiday test records; vendor sign-off on any touch-up. |
| Relief devices proven | PVRV/EPRV bench-test certs; tie-in pressure test; VRU header continuity. |
| Blanket gas system commissioned | Leak test record; functional test per API 2000. |
| High-level shutdown functional | Loop check + functional test record (R-096-03-07). |
| Sour-service / NACE preserved | Material certs and weld map review; NDE per ITP. |
| Containment functional | Volume calculation + drainage as-built review. |
| Document deliverables complete | All three artifacts (work package, workface plan, interface/turnover checklist) present and approved. |

## Records

Required records resulting from this procedure:

- The Construction Work Package document (Phase A output).
- The Installation and Tie-In Workface Plan (Phase B output).
- The Construction Interface and Turnover Checklist, completed and signed (Phase C output).
- Inspection and Test Records (ITRs) per QLT-003 ITP.
- Hold-point sign-off sheets.
- Hydrotest / pressure test packages (PIP-024-based) — completed.
- Coating DFT/holiday test records.
- Relief device bench-test certificates (PVRV, EPRV).
- Blanket-gas commissioning leak/function test record.
- I&C loop check records.
- Grounding / bonding continuity test records.
- Cathodic protection commissioning record.
- Lighting energization / lux survey record.
- High-level shutdown functional test record.
- Containment volume verification calculation and as-built.
- Turnover dossier signed by EPC, vendor, and Operations.
