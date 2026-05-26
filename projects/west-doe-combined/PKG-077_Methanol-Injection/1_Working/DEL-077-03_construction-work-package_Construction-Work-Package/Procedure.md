# Procedure — DEL-077-03 Construction Work Package (Methanol Injection)

> Interpretation: this procedure describes steps to **produce** the CWP deliverable (the document set) and a high-level outline of the construction execution it governs. Detailed field execution procedures are downstream artifacts produced under the CWP itself.

## Purpose

Produce the EPC Integrator's Construction Work Package for PKG-077 Methanol Injection, comprising:

- Construction work package narrative (ART-D62FFA7E43)
- Installation and tie-in workface plan (ART-F3B0D2F531)
- Construction interface and turnover checklist (ART-EC659AD03C)

Source: `ARTIFACT_REGISTER.csv` DEL-077-03 rows.

## Prerequisites

### Deliverable-local prerequisites
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` initialized (present at PREPARATION).
- This deliverable's `_STATUS.md` is in an editable state (`OPEN` or `INITIALIZED`).

### Upstream deliverable prerequisites (ASSUMPTION — not in declared `_DEPENDENCIES.md`)
- DEL-077-01 Scope of Work (defines package scope, tagged equipment list, integration narrative).
- DEL-077-02 Package Datasheet (vendor-handoff technical basis).
- DEL-077-04 Vendor Engineered Equipment Package (vendor design and physical equipment).
- DEL-077-05 Vendor Document Turnover Package (installation/inspection vendor documentation).

### Reference prerequisites
- GATE-07 PROJECT_DECOMP snapshot accessible at decomposition path (confirmed in `_REFERENCES.md`).
- DBM-Deepcut/4-25_Deepcut_DBM.md and 26020-Package_Requirements.docx — required for source-grounded code/standard/utility detail. **Status: not deliverable-local; values dependent on these sources are marked `TBD (location TBD)`.**

## Steps

### Phase A — Produce the CWP deliverable

**Step A-1: Confirm package identity and scope**
- Re-read `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row DEL-077-03.
- Re-read `PACKAGE_REGISTER.csv` row PKG-077 and `SCOPE_LEDGER.csv` row SOW-0143.
- Capture any scope disposition issue (e.g., Gate 6 Cryogenic Unit absorption note) and surface to human ruling. (See Guidance Conflict Table CFT-001.)
- Verification: identity table in Datasheet matches register values.

**Step A-2: Enumerate applicable interfaces**
- Pull all PKG-077 rows from `INTERFACE_REGISTER.csv` with Applicable=YES.
- Record IFC IDs in the construction interface and turnover checklist (one row per interface).
- Verification: 13 IFC rows present and each row mapped to a planned tie-in.

**Step A-3: Draft the construction work package narrative (ART-D62FFA7E43)**
- Describe how the vendor-supplied package will be received, set, installed, inspected, tied in, and turned over.
- Reference the vendor documentation set from DEL-077-05 for installation methods; do not duplicate vendor content.
- Verification: narrative covers receipt, setting, tie-ins, inspection, mechanical completion, turnover.

**Step A-4: Draft the installation and tie-in workface plan (ART-F3B0D2F531)**
- Break installation into workface packs (foundations and supports; equipment setting; piping tie-ins; electrical/EHT/grounding; I&C and F&G; insulation/heat-tracing; commissioning support).
- Sequence packs against site-wide construction logic (sequencing detail: TBD — driven by overall project schedule).
- Verification: each interface type from Step A-2 appears in at least one workface pack.

**Step A-5: Draft the construction interface and turnover checklist (ART-EC659AD03C)**
- One row per interface (Step A-2) with: interface owner, tie-in location, installation method, inspection requirement, turnover sign-off.
- Add mechanical completion criteria and punch-list controls.
- Verification: all 13 IFC IDs covered; turnover sign-offs assigned.

**Step A-6: Apply Pass 2 cross-document consistency sweep**
- Run the Specification ↔ Datasheet ↔ Guidance ↔ Procedure consistency checks (Step 5 of `four-documents` SKILL.md).
- Resolve from drafts where possible; otherwise mark `TBD` or add to the Conflict Table in Guidance.
- Verification: no contradictory values across documents; conflicts captured.

**Step A-7: Update `_STATUS.md` (safe update)**
- If current state is `OPEN` and `RUN_PASSES` includes Pass 1 or 2, advance to `INITIALIZED` with provenance `TASK+four-documents`.
- Verification: state advanced exactly once; history line appended.

**Step A-8: Persist run record**
- Write `_run_records/TASK_RUN_<timestamp>.md` per `AGENT_TASK.md` Step 5.
- Verification: run record present with required frontmatter and headings.

### Phase B — Govern construction execution (downstream — informational outline)

**Step B-1:** Mobilize EPC construction crew; verify vendor documentation set is available (DEL-077-05).
**Step B-2:** Install foundations, supports, and containment per civil packages (interface IFC-A96044F713, IFC-4DE6A3A2ED).
**Step B-3:** Receive and set the vendor-supplied Methanol Injection package.
**Step B-4:** Execute process piping, utility piping, relief/flare/vent, and drain tie-ins; pressure-test per project test plan (test plan location TBD).
**Step B-5:** Execute electrical power, EHT, grounding/bonding, area-lighting tie-ins (interfaces IFC-4269247DFA, IFC-897BE87E57, IFC-4848032D8D, IFC-739B6603B5).
**Step B-6:** Execute I&C cabling, F&G, and building HVAC/services tie-ins (interfaces IFC-1E031D5EF9, IFC-2176B4EB34, IFC-F8D351A2A3).
**Step B-7:** Walkdowns, inspection records, and punch-list compilation.
**Step B-8:** Mechanical completion declaration; turnover package compilation and signoff.
**Step B-9:** Handoff to commissioning with controlled open items dispositioned per OBJ-010.

## Verification

| Verification | What it Confirms |
|---|---|
| Identity check (Step A-1) | Datasheet identity matches register |
| Interface coverage (Step A-2 / A-5) | All 13 PKG-077 interfaces represented in the checklist |
| Cross-doc consistency (Step A-6) | Terminology, values, and requirements aligned across the four documents |
| Status update (Step A-7) | `_STATUS.md` advanced safely and traceably |
| Run record (Step A-8) | Auditable run-record file persisted |
| Field walkdowns (Step B-7) | Construction conforms to specification |
| Mechanical completion (Step B-8) | Turnover prerequisites complete |

## Records

- The four deliverable documents: Datasheet, Specification, Guidance, Procedure.
- Construction work package narrative (ART-D62FFA7E43).
- Installation and tie-in workface plan (ART-F3B0D2F531).
- Construction interface and turnover checklist (ART-EC659AD03C).
- Updated `_STATUS.md` with history entry.
- Run record in `_run_records/`.
- Downstream (Phase B): inspection records, pressure-test records, mechanical-completion certificate, punch-list closure log, turnover package. Format/location TBD.
