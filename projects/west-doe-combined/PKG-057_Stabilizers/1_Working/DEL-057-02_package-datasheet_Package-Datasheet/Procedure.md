# Procedure: DEL-057-02_package-datasheet — Package Datasheet (PKG-057 Stabilizers)

> Operational document. Describes the steps to **produce** this deliverable (the Package Datasheet artifact). Where source judgment is required, items are marked `TBD`.

## Purpose

Produce a source-grounded EPC Package Datasheet for `PKG-057` Stabilizers that satisfies the Specification (`Specification.md`) and is suitable as the Gate-5 technical handoff to a third-party vendor or downstream discipline (`_CONTEXT.md`).

## Prerequisites

### Declared upstream dependencies
- None declared in `_DEPENDENCIES.md` during PREPARATION.

### Required reference materials (from `_REFERENCES.md`)
- Gate-07 Final Published PROJECT_DECOMP snapshot (authoritative basis).
- `PACKAGE_REGISTER.csv` row `PKG-057`.
- `DELIVERABLE_REGISTER.csv` row `DEL-057-02_package-datasheet`.
- `SCOPE_LEDGER.csv` rows `SOW-0177`, `SOW-0178`, `SOW-0179`, `SOW-0180`.
- `INTERFACE_REGISTER.csv` rows scoped to `PKG-057`.
- Workbook Packages row 82 (`26020-Packages_Interfaces_4_export.xlsx`) — to be opened for any `location TBD` resolution.
- `26020-Package_Requirements.docx` package heading 12 — to be opened for full BOM, complete process narrative, and any code list.
- `Bid Docs/Budgetary/26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx` — RFQ basis to consult for vendor-data expectations.
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — design-basis context (sour-gas service, facility integration).

### Tooling / environment prerequisites
- Read access to the deliverable folder and the shared `_Sources` root.
- Ability to open `.docx`/`.xlsx` binaries (TBD: which converter/viewer is normative for this project).

## Steps

### Step 1 — Initialize identity
1. Read `_CONTEXT.md` Identity table.
2. Populate `Datasheet.md > Identification` with `DeliverableID`, parent package, WBS, workbook tracking number, discipline, type, responsible party, and source basis.
3. Verify against `PACKAGE_REGISTER.csv` row `PKG-057`.

### Step 2 — Populate package attributes
1. From `SCOPE_LEDGER.csv` SOW-0177, capture the ownership split and add to `Datasheet.md > Attributes`.
2. From SOW-0178 and SOW-0179, capture package count (3), configuration (3 x 40%), design throughput (1,272 m3/d / 8,000 bbl/d), and turndown (3:1).
3. From SOW-0180, capture `By others` exclusions.

### Step 3 — Populate operating and design conditions
1. From SOW-0180, transcribe operating conditions for Flash Feed Separator, Feed/Bottoms Exchangers, and Stabilizer Column into `Datasheet.md > Conditions > Operating Conditions`.
2. From SOW-0180, transcribe design conditions (including 16.7 °C minimum approach and 130% product cooler sizing) into `Datasheet.md > Conditions > Design Conditions`.
3. From SOW-0180, transcribe driver/motor configuration (Feed Pumps and Product Cooler Fan: electric, VFD-compatible).

### Step 4 — Populate construction (equipment list)
1. From SOW-0179, capture the major equipment list (trayed reboiled distillation columns; 20 floating valve trays; 1 LIT; 1 TIT).
2. From SOW-0178, capture the additional equipment named in the process function narrative (stabilizer flash feed separator; basket strainers; stabilizer feed pumps; feed/bottoms exchanger).
3. From SOW-0180, add the Stabilizer Product Cooler (sized at 130%).
4. Mark the remainder of the BOM as `TBD` with `location TBD` until `26020-Package_Requirements.docx` package heading 12 is opened.

### Step 5 — Build the interface requirements matrix
1. Filter `INTERFACE_REGISTER.csv` to rows scoped to `PKG-057` (`ParentPackageID = PKG-057`).
2. For each row, record `InterfaceID`, `Interface Type`, and `Required` status.
3. Confirm 13 rows are present and all marked `Required = YES`.

### Step 6 — Populate references
1. Reproduce the reference list from `_REFERENCES.md` and PACKAGE_REGISTER.csv `Word Source Basis`.
2. For each reference whose slice was not opened in this pass, mark `location TBD`.

### Step 7 — Cross-check against the Specification
1. Walk each requirement R-DS-01 through R-DS-11 in `Specification.md` and confirm `Datasheet.md` satisfies it (or that the gap is captured as `TBD`).
2. Update the Conflict Table in `Guidance.md` if new contradictions are uncovered.

### Step 8 — Open source binaries (when authorized)
1. Open `26020-Package_Requirements.docx` package heading 12; resolve `CONF-001` (truncated SOW-0178 narrative) and `CONF-003` (full BOM).
2. Open `26020-Packages_Interfaces_4_export.xlsx` workbook row 82; confirm interface scope is identical to INTERFACE_REGISTER.csv extract.
3. Open `26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`; pick up RFQ vendor-data expectations.
4. Open `4-25_Deepcut_DBM.md`; confirm sour-service/code applicability and resolve `CONF-002`.
5. Step is `TBD` in the current pass — performed once binaries are accessible.

## Verification

| Verification Check | How |
|---|---|
| All 13 PKG-057 interfaces present | Count rows in `Datasheet.md > Package Interface Requirements Matrix`; equals 13. |
| Numeric values consistent | 1,272 m3/d ↔ 8,000 bbl/d; 3:1 turndown; 3 x 40%; 345 kPag, 1724 kPag, 793 kPag; 30.6 °C, 60 °C, 71 °C, 16.7 °C; 130% — match SOW-0180 exactly. |
| Ownership split matches PACKAGE_REGISTER | Datasheet ownership paragraph aligns with PACKAGE_REGISTER.csv PKG-057 description. |
| By-others list complete | Five items from SOW-0180 reproduced in datasheet. |
| Specification coverage | R-DS-01 … R-DS-11 each map to a populated datasheet section or an explicit `TBD`. |
| Conflict Table reviewed | `Guidance.md > Conflict Table` has open items resolved or escalated for human ruling. |
| Source citations present | Every non-trivial value cites a SOW item, register row, workbook row, or document heading. |

## Records

Evidence/documents that should result from a successful execution of this procedure:

- `Datasheet.md` — fully populated per Steps 1–6, cross-checked per Step 7.
- `Specification.md` — unmodified by this procedure (drafted in parallel); referenced for verification.
- `Guidance.md` — updated Conflict Table reflecting any open items.
- `_run_records/TASK_RUN_<timestamp>.md` — run record for the producing TASK invocation (per `agents/AGENT_TASK.md`).
- `_STATUS.md` — safe state update from `OPEN` to `INITIALIZED` when Pass 1/2 ran (per skill `four-documents` Step 7).
- (Future) Source-binary read evidence: notes on which `.docx`/`.xlsx` slices were opened to resolve `TBD` items and Conflict Table entries.
