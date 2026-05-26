# Procedure: DEL-082-04 — Vendor Engineered Equipment Package (Flare KO Drum, Low Pressure, 3-25)

## Purpose

This procedure describes how to produce the Vendor Engineered Equipment Package deliverable: the sequence the Package Vendor follows to engineer, design, fabricate/supply, and document the V-3900-2 LP flare KO drum and the P-3900-2 transfer pump under the EPC Integrator's envelope, and the sequence the EPC Integrator follows to feed the vendor and verify acceptance hooks (the formal acceptance step is owned by DEL-082-06).

Procedure interpretation: this is primarily a **produce-the-deliverable** procedure. Operating procedures for V-3900-2 in service are out of scope (those follow from facility commissioning and turnover, supported by DEL-082-05).

## Prerequisites

| Prerequisite | Source / Status |
|---|---|
| EPC Scope of Work (DEL-082-01) issued at acceptable maturity | Peer deliverable — current state TBD; required before vendor commits engineering |
| EPC Package Datasheet (DEL-082-02) issued at acceptable maturity | Peer deliverable — current state TBD; required as the controlling vendor input (codes, design pressure/temperature, materials, relief load) |
| Accepted 03-25 DBM tag and service basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Flare and Blowdown §; Sparing Philosophy §) |
| Access to Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 | Referenced in DBM line 501; not locally accessible — EPC Integrator to provide |
| Vendor selection and contract execution | Out of scope of this procedure; ASSUMPTION that a vendor is engaged |
| Sour-service ruling on facility wetted parts | Working ASSUMPTION sour pending confirmation on DEL-082-02 |

## Steps

### Step 1 — Establish vendor inputs (EPC Integrator)
1.1 Issue DEL-082-01 (Scope of Work) and DEL-082-02 (Package Datasheet) to the vendor at an acceptable maturity.
1.2 Provide the accepted LP relief load case from the blowdown philosophy (W242510-PRC-REP-000003-001) — values TBD until the philosophy is sliced.
1.3 Confirm sour-service applicability and any NACE MR0175 / ISO 15156 requirements.
1.4 Confirm governing pressure vessel and relief codes (TBD per DEL-082-02).

### Step 2 — Vendor design basis (Vendor)
2.1 Produce the vendor package design basis statement covering: services routed (TEG regen, VRU, compressor seal-pot per DBM line 499), design pressure/temperature, governing codes, materials, sour-service treatment, relief load case, and staggered-blowdown profile.
2.2 Confirm tag basis: V-3900-2 (drum) and P-3900-2 (pump), 1 x 100 percent pump sparing per DBM line 584.
2.3 Confirm interface envelope: LP relief inlet (header carried as 508 mm / 20 inch — drum nozzle size by vendor sizing), vapor outlet to LP flare stack, liquid outlet to slop via P-3900-2.

### Step 3 — Vendor engineering and sizing (Vendor)
3.1 Size the drum (diameter, length, holdup volume, vapor space, demister selection) against the LP relief load case from Step 1.2.
3.2 Size and select the transfer pump P-3900-2 against slop-routing conditions provided by EPC.
3.3 Develop nozzle schedule, instrument schedule (level, pressure, temperature; relief and isolation), and valve list.
3.4 Develop materials of construction, including sour-service qualification when applicable.
3.5 Develop package general arrangement, P&ID, and structural/skid concept.

### Step 4 — Vendor datasheet set and engineering documentation (Vendor)
4.1 Issue the drum datasheet, pump datasheet, instrument datasheet list, and valve list.
4.2 Issue GA drawings, P&ID(s), nozzle orientation drawing, and weight/CoG data.
4.3 Issue the inspection and test plan (ITP) per governing code.
4.4 Compile preliminary operation and maintenance data feeding DEL-082-05 (Vendor Document Turnover Package).

### Step 5 — Fabrication / supply (Vendor)
5.1 Procure materials per the qualified specifications.
5.2 Fabricate, inspect, and code-stamp the drum per the ITP and governing code.
5.3 Assemble the package (drum, pump, instruments, valving, skid if applicable).
5.4 Perform factory acceptance testing per the ITP.

### Step 6 — Handoff to EPC Integrator (Vendor with EPC review interface)
6.1 Submit the as-built vendor design basis and datasheet set.
6.2 Submit ITP records, code certification (e.g., U-stamp or equivalent), and material certifications.
6.3 Deliver the physical equipment package and supporting turnover documentation set to seed DEL-082-05.
6.4 Support EPC Integrator review activities owned by DEL-082-06 (formal acceptance is not performed inside this deliverable).

## Verification

| Step | Verification Check |
|---|---|
| Step 1 | EPC issuance log shows DEL-082-01 and DEL-082-02 at the required maturity before vendor engineering begins |
| Step 2 | Vendor design basis references DBM line 499 service list and DBM line 584 pump sparing; tags match the accepted basis |
| Step 3 | Vendor sizing calculations are traceable to the LP relief load case supplied in Step 1.2; nozzle sizing supports the staggered-blowdown profile |
| Step 4 | Datasheet set, drawings, and ITP are complete and consistent with the design basis |
| Step 5 | ITP records, code certification, and material certifications are present and traceable |
| Step 6 | Handoff log demonstrates that all artifacts required for DEL-082-05 turnover and DEL-082-06 acceptance are present |

## Records

| Record | Owner | Destination |
|---|---|---|
| Vendor package design basis | Vendor | Vendor turnover package (DEL-082-05) |
| Drum datasheet, pump datasheet, instrument and valve lists | Vendor | DEL-082-05 |
| GA, P&ID, nozzle and orientation drawings, weight data | Vendor | DEL-082-05 |
| Inspection and test plan (ITP) and execution records | Vendor | DEL-082-05 |
| Code certification (e.g., U-stamp), material certifications | Vendor | DEL-082-05 |
| Factory acceptance test report | Vendor | DEL-082-05 |
| EPC Integrator review interface notes (informal during this deliverable; formal in DEL-082-06) | EPC Integrator | DEL-082-06 |
| Physical equipment package delivered to site | Vendor | Site / construction (DEL-082-03) |
