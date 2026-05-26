# Procedure — DEL-059-04 Vendor Engineered Equipment Package

> Operational procedure to produce the deliverable (a vendor-engineered NGL storage-bullet package) and to perform the EPC Integrator's integration review touchpoints owned by this deliverable. Source-grounded steps cite the DBM and `_CONTEXT.md`; judgment points are marked `TBD`.

## Purpose

Provide a repeatable, auditable sequence for the Package Vendor to engineer, design, fabricate/supply, and deliver the PKG-059 NGL storage-bullet package, with explicit EPC Integrator integration touchpoints.

## Prerequisites

Inputs required before initiating the procedure:

- Accepted `DEL-059-01_scope-of-work` (Scope of Work). Status: declared upstream is **not yet declared** in `_DEPENDENCIES.md` (ASSUMPTION pending declaration).
- Accepted `DEL-059-02_package-datasheet` (Package Datasheet). Status: not yet declared in `_DEPENDENCIES.md` (ASSUMPTION).
- Access to the upstream basis: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (NGL storage and spacing basis).
- Access to project-wide mechanical-package basis: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.
- `26020-Package_Requirements.docx` package heading 14 — extracted to a markdown source slice. Status: `TBD` (not yet extracted).
- API 2510 standard text. Status: `location TBD`.
- Governing pressure-vessel code confirmation (proposed ASME Section VIII). Status: `TBD` (see Guidance Conflict C-1).
- EPC-issued battery-limit definitions for utilities, electrical/instrumentation, civil interfaces.

## Steps

### Step 1 — Vendor kick-off and basis confirmation

1.1 Vendor receives the accepted SOW (`DEL-059-01`) and Package Datasheet (`DEL-059-02`) from the EPC Integrator.
1.2 Vendor and EPC Integrator hold a kick-off meeting to confirm:
- 16 x 120,000 USG bullet configuration basis [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448].
- C3+ NGL product service (not C3/C4 split) [Source: lines 1627-1629].
- Production-rate and storage-duration basis (15,400 bbl/d, 2.5 days) [Source: line 448].
- Governing pressure-vessel code (resolves Conflict C-1; **TBD** until ruled).
- No truck/rail distribution scope [Source: line 446].
1.3 Vendor records the confirmed basis in the kick-off minutes (vendor deliverable).

### Step 2 — Design development (the deferred basis work)

The DBM explicitly defers detailed bullet design parameters to this step. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1629, 1814.]

2.1 Develop and submit, for EPC Integrator review:
- Design pressure and temperature (TBD inputs from process; values from source: not stated).
- Materials of construction (TBD; ASSUMPTION pending source confirmation).
- Corrosion allowance (TBD).
- Insulation/heat-trace requirements (TBD; condensate-tank insulation approach in DBM is not directly applicable — see Datasheet "Conditions").
- Nozzle schedule and orientation.
- Internals (if any).
- External loads (wind, seismic, equipment, piping).
- Relief and depressurization scenarios and loads [package deliverable per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617].

### Step 3 — Layout proposal against API 2510

3.1 Produce a cluster-layout proposal compliant with API 2510 spacing requirements quoted in the DBM:
- <=6 bullets per cluster [line 249]
- >=15.24 m (50 ft) between clusters [line 250]
- >=3.05 m (10 ft) bullet-to-pump-skid [line 252]
- >=15.24 m (50 ft) bullet-to-rotating-equipment unrelated to bullets [line 253]
- >=15.24 m (50 ft) bullet-to-control/process buildings [line 254]
- >=30.48 m (100 ft) bullet-to-unrelated-buildings [line 255]
- >=15.24 m (50 ft) bullet-to-process-vessel [line 256]
- >=15.24 m (50 ft) bullet-to-truck-loading-station [line 257]
- >=15.24 m (50 ft) bullet-loading-connection-to-ignition-source [line 258]
- >=38.1 m (125 ft) bullet-to-property-line [line 259]
- >=30.48 m (100 ft) bullet-to-atmospheric-tank [line 265]
- >=3.05 m (10 ft) bullet-to-spill-containment [line 266]
- >=30.48 m (100 ft) bullet-to-flare [line 284]
- >=15.24 m (50 ft) bullet-to-fired-heater [line 299]

3.2 Identify drainage and containment interface points consistent with sloped grading away from pipe rack/process areas. [Source: line 2722.]
3.3 EPC Integrator reviews layout proposal and records acceptance or required changes.

### Step 4 — Vendor document register population

4.1 Vendor produces the package deliverables enumerated in the project-wide mechanical-package basis: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers. [Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.]
4.2 Each document is logged in the master vendor document register with revision status.

### Step 5 — Fabrication and shop testing

5.1 Fabricate per accepted design package and governing pressure-vessel code (TBD; see Step 1.2 ruling).
5.2 Perform shop testing per code requirements (hydrotest, NDE, etc.; specific scope TBD).
5.3 Apply surface preparation and coatings per accepted materials/coating basis (TBD details).
5.4 Prepare shipped-loose items list.

### Step 6 — Delivery and field tie-in support

6.1 Deliver bullets and shipped-loose items to site per accepted logistics plan (TBD).
6.2 Provide field tie-in lists and vendor-assist for installation interfaces (civil foundations, piping, electrical/instrumentation, drainage).

### Step 7 — Hand-off to turnover and acceptance

7.1 Compile the complete vendor document turnover package and transmit to the turnover deliverable (`DEL-059-05`).
7.2 Support the EPC Integrator's review-and-acceptance deliverable (`DEL-059-06`) by responding to comments and providing as-built and certification evidence.

## Verification

| Step | Verification check | Evidence |
|---|---|---|
| 1 | Kick-off minutes record confirmed basis and Conflict C-1 ruling | Signed minutes filed in vendor document register |
| 2 | Design-development submission reviewed by EPC Integrator | Stamped/reviewed transmittals; review-comment log closed |
| 3 | Layout proposal checks every API 2510 spacing item enumerated in Step 3.1 | Layout compliance matrix; EPC acceptance record |
| 4 | All deliverables in the project-wide list (R-5.1) appear in the vendor document register | Vendor document register completeness audit |
| 5 | Pressure-vessel code stamping/registration | Code-stamp records; NDE reports; hydrotest records |
| 6 | Delivery and field tie-in match the field tie-in list | Receiving inspection records; field-tie-in punch list |
| 7 | Turnover package accepted by `DEL-059-05`; acceptance recorded by `DEL-059-06` | Acceptance records on the respective deliverables |

## Records

The procedure shall produce the following records (vendor or EPC Integrator owns as noted):

- Kick-off meeting minutes with Conflict C-1 ruling (vendor)
- Design-development transmittals and EPC review-comment log (vendor / EPC)
- Layout proposal and API 2510 compliance matrix (vendor / EPC)
- Vendor document register (master) (vendor)
- Fabrication code-stamp records, NDE reports, hydrotest records (vendor)
- Surface-preparation and coating QA records (vendor)
- Shipped-loose items list and receiving inspection records (vendor / site)
- Field tie-in list and punch list (vendor / site)
- Turnover-package transmittal to `DEL-059-05` (vendor)
- Acceptance record from `DEL-059-06` (EPC Integrator)
