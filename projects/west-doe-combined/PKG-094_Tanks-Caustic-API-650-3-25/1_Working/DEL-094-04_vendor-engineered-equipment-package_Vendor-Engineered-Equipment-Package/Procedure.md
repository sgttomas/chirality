# Procedure: DEL-094-04 — Vendor Engineered Equipment Package

This procedure describes how the Package Vendor produces and delivers the engineered equipment package, and how downstream EPC review consumes it. It interprets "Procedure" in both modes (produce the deliverable artifact; use/operate it via the vendor design basis and datasheet set).

## Prerequisites

- EPC-issued Scope of Work — `DEL-094-01_scope-of-work_Scope-of-Work` (declared upstream — TBD; no declared upstream in `_DEPENDENCIES.md` as of PREPARATION).
- EPC-issued Package Datasheet — `DEL-094-02_package-datasheet_Package-Datasheet` (ASSUMPTION: required as design input).
- Accessible references:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (locally accessible).
  - Workbook Packages row 86 (location TBD).
  - 26020-Package_Requirements.docx heading 46 (location TBD).
- Site basis: -40 deg C minimum ambient; 03-25 Liquids Hub configuration per DBM.

## Steps

### Step 1 — Confirm package scope and design inputs
1. Receive EPC SOW (DEL-094-01) and Package Datasheet (DEL-094-02).
2. Cross-walk EPC inputs to SOW items SOW-0193..0196.
3. Record any TBD/TBC items that block vendor design.

### Step 2 — Establish vendor design basis
1. Adopt site basis (-40 deg C minimum ambient; winterization implications).
2. Adopt caustic service basis: 50 wt% NaOH/H2O, SG 1.75 (TBC; carry forward until EPC confirms).
3. Adopt code family: API 650 per package title; specify edition and appendices once EPC confirms (TBD).
4. Adopt material/coating positions for caustic service consistent with DBM (no aluminum in caustic building); specific MOC and coating selection (TBD pending vendor metallurgical review and EPC ruling — see Guidance Conflict Table C-03).

### Step 3 — Equipment list and datasheets
1. List the tanks within vendor scope per the final tank register (the DBM-current count is 400 bbl fresh-caustic, spent-caustic, caustic process-water, and H2O2 tanks; quantities to be confirmed against the EPC Package Datasheet — TBD).
2. Issue vendor datasheets for each tank covering identification, design conditions, materials, coatings, insulation, heating, nozzles, vents, and instrumentation.
3. Issue ancillary equipment datasheets (heaters, agitators, transfer pumps, etc.) only where they are part of the vendor scope per the EPC SOW.

### Step 4 — Engineering and code compliance
1. Perform API 650 mechanical design per confirmed edition/appendices.
2. Apply -40 deg C minimum design temperature impact studies (impact testing, material toughness verification).
3. Design heating, insulation, and heat tracing concept (redundancy per EPC ruling).
4. Design vent/blanket interfaces:
   - Fresh caustic tank: LP fuel-gas blanket; not connected to VRU.
   - Spent caustic tank: vent to incinerator header through a flame arrestor; truck-out connection.
5. Confirm drain interfaces to 300# ANSI minimum at 121 deg C / 250 deg F (TBC); coordinate with EPC piping interface.
6. Confirm "no aluminum in the caustic building" prohibition is reflected in the BOM and all package-mounted items.

### Step 5 — Fabrication and supply
1. Procure plate, structural material, internals, and accessories per approved datasheets.
2. Maintain MTRs and weld procedure qualification records.
3. Fabricate per approved drawings; perform NDE and hydrotest per API 650 and project specification.
4. Apply internal coating (when applicable) per approved coating spec; record DFT and holiday test results.
5. Apply external insulation and heat tracing per design.
6. Prepare for shipment (loose items inventoried, lifting points identified).

### Step 6 — Vendor design basis and datasheet set issue
1. Compile vendor design basis document (process basis, material basis, code basis, site basis, interface basis).
2. Compile vendor datasheet set (one datasheet per equipment item).
3. Issue to EPC for review.

### Step 7 — Handoff to downstream deliverables
1. Provide vendor document register inputs to DEL-094-05 (Vendor Document Turnover Package).
2. Provide as-fabricated drawings and code documentation to DEL-094-03 (Construction Work Package) and DEL-094-06 (EPC Vendor Package Review and Acceptance).
3. Coordinate any open TBD/TBC items via the Guidance Conflict Table for EPC ruling.

## Verification

| Step | Check |
|---|---|
| 1 | EPC inputs received; SOW item cross-walk recorded. |
| 2 | Vendor design basis covers site, service, code, and material/coating positions; TBC items flagged. |
| 3 | Datasheet set complete for all vendor-scope equipment; aligned to final tank register. |
| 4 | API 650 design report complete; vent/blanket/drain interfaces aligned with DBM; aluminum prohibition observed. |
| 5 | MTRs, NDE, hydrotest, coating, insulation, heat-tracing records complete. |
| 6 | Vendor design basis and datasheet set issued; review comments closed. |
| 7 | Handoff records to DEL-094-03/05/06 issued; open items entered in Conflict Table. |

## Records

- Vendor design basis document.
- Vendor datasheet set.
- API 650 design reports and tank nameplate records.
- MTRs, NDE reports, hydrotest records.
- Coating system records (specification, application, DFT, holiday).
- Insulation/heat-tracing as-built records.
- BOM and material acceptance records (including aluminum-exclusion check for caustic building).
- Shipment records and turnover inputs to DEL-094-05.
- Conflict Table dispositions (entries C-01..C-07 in `Guidance.md`).
