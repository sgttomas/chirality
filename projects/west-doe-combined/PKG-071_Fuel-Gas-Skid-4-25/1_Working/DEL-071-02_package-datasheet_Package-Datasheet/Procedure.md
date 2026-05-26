# Procedure — DEL-071-02 Package Datasheet (Fuel Gas Skid 4-25)

Interpretation: this Procedure describes the steps to **produce** the EPC Package Datasheet artifact for `PKG-071` (and to keep it usable for vendor handoff). It is not a procedure for operating the skid.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (`_REFERENCES.md`).
- Deliverable folder is initialized per the minimum viable fileset: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (all present).
- Source root `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/` is accessible.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` ("None declared during PREPARATION"). Logical upstream is the workbook row 61 / package-requirements heading 25 already extracted into SCOPE_LEDGER.
- The companion deliverable `DEL-071-01_scope-of-work` should be drafted in parallel (it shares the same source basis and provides the package narrative context).

## Steps

### Step 1 — Confirm package identity and ownership
1. Read PACKAGE_REGISTER.csv row 61 and the `_CONTEXT.md` Identity block.
2. Verify package ID `PKG-071`, workbook 71/row 61, WBS 01, CoA 26020-01-23-001, discipline Mechanical.
3. Record Package Vendor vs. EPC Integrator responsibility text verbatim (from row 61) in the datasheet identity block.

### Step 2 — Extract package function and major equipment
1. Read SCOPE_LEDGER.csv `SOW-0100` (Basic scope) and `SOW-0101` (Major included equipment).
2. Copy the package configuration (1 skid; LP fuel gas heater; LP fuel gas scrubber), function statement, and per-equipment basis into the Datasheet's "Attributes" block.
3. Mark heater capacity as TBD; record the SCR (600 V) control and skin-thermocouple override note exactly as written.
4. Record the scrubber k-factor sizing basis (0.35 imperial max + pressure de-ration; vendor to design).

### Step 3 — Capture conditions
1. From SCOPE_LEDGER `SOW-0102`, populate the Datasheet "Conditions" block with each numeric value (design flow > 8.4 MMSCFD / 237.5 e3m3/day; outlet 95 F / 35 C; operating P = 150 psig; ambient -19/+22.2 C; design P = 150 psig; design T = -40/+35 C).
2. Preserve TBDs: heater capacity, final flow, MAWP.
3. Record the SCR power note (600 V, electrical building) and the by-others list.

### Step 4 — Build the interface matrix
1. Filter INTERFACE_REGISTER.csv on `Package=PKG-071`; expect 12 rows (rows 453-464), all `Applicable=YES`.
2. For each row, copy the interface type and `IFC-*` ID into the Datasheet matrix.
3. Cross-check the count against the `Applicable Interfaces` cell in PACKAGE_REGISTER row 61 (lists the 12 interface types).

### Step 5 — Assemble vendor handoff basis
1. Compose a brief narrative tying identity + function + conditions + interfaces into a single coherent handoff statement (Datasheet section "Vendor handoff" or equivalent header in `Datasheet.md`).
2. List every TBD so the vendor sees the open-item set in one place.

### Step 6 — Cross-check consistency
1. Walk every numeric value in the Datasheet against `SOW-0099`..`SOW-0102` and confirm verbatim match.
2. Walk every interface ID against INTERFACE_REGISTER.
3. Walk Datasheet headers against Specification requirements R-1..R-12; each requirement should map to a populated Datasheet section or an explicit TBD.

### Step 7 — Record provenance
1. Every numeric value, every interface row, and every quoted clause MUST carry an inline citation (CSV file + row, or source-doc + section).
2. For any value supported only by inference, label `ASSUMPTION:` in-line.

### Step 8 — Update status and run record
1. If `_STATUS.md` is in `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
2. Write the TASK run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md`.

## Verification

| Check | How |
|---|---|
| All four documents exist in `{DELIVERABLE_PATH}` | `ls Datasheet.md Specification.md Guidance.md Procedure.md` |
| Default schema sections present in each document | Visual inspection / heading grep |
| Every numeric value cites a source | grep for `[SOW-` / CSV row references / `26020-Package_Requirements.docx heading 25` |
| Interface matrix has 12 rows matching INTERFACE_REGISTER for `PKG-071` | Row count = 12; each `IFC-*` ID present |
| TBDs preserved (not silently resolved) | grep `TBD` in `Datasheet.md` returns at least: heater capacity, final flow, MAWP |
| `_STATUS.md` only moved `OPEN -> INITIALIZED` (no regression) | Inspect `_STATUS.md` History |
| No writes outside `{DELIVERABLE_PATH}` | Run record `Applied Changes` block |

## Records

The following records remain in the deliverable folder after a successful run:
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`
- `_STATUS.md` updated to `INITIALIZED` (when prior state was `OPEN`)
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md`
