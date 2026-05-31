# West Doe - Regulatory Submittal Document Change Impact Report

- **Report date:** 2026-05-28
- **Facilities covered:** West Doe Compressor Station and Liquids Hub (3-25); West Doe Deepcut Expansion (4-25)
- **Document sets covered:** `_Sources/3-25_Regulatory_Submittal/`; `_Sources/4-25_Regulatory_Submittal/`
- **Scope-change basis:** SCA-001 through SCA-006 for each facility, as summarized in `_Reports/West_Doe_Scope_Change_Amendments_Report_2.md`.

This is derivative planning material and a derivative planning report. It identifies likely regulatory submittal document changes and review needs. It does not replace source truth, accepted decomposition truth, regulatory professional review, discipline engineering review, or human rulings.

---

## Source Basis and Evidence Policy

This report is derivative planning material. It identifies likely regulatory submittal document changes and review needs from targeted evidence, and it does not replace source truth, accepted decomposition truth, regulatory professional review, discipline engineering review, or human rulings.

Evidence used:

- Primary planning source: `_Reports/West_Doe_Scope_Change_Amendments_Report_2.md`.
- Regulatory source indexes: `_Sources/3-25_Regulatory_Submittal/FILE_INDEX.md` and `_Sources/4-25_Regulatory_Submittal/FILE_INDEX.md`.
- Scope-change evidence roots:
  - `/Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/West_Doe_Comp_and_Liquids_DBM/_ScopeChange`
  - `/Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/West_Doe_Deepcut_DBM/_ScopeChange`
- Targeted SCA evidence files where present: `Amendment_Actions.csv`, `RUN_SUMMARY.md`, `Brief.md`, `Impact_Assessment.md`, `Decision_Log.md`, `Supersession_Delta.csv`, `Supersession_Map.csv`, and remediation manifests.
- Regulatory PDF keyword checks from temporary `pdftotext` extraction outside the repository at `/tmp/west_doe_reg_pdf_text.856HCq`; these extracts are not report artifacts and were not committed.

Impact status definitions:

- `Change Required`: direct or strongly evidenced contradiction with the post-SCA scope-change state.
- `Review Required`: plausible impact requiring discipline/regulatory review before deciding whether to revise.
- `No Change Expected`: no material scope-change impact identified from targeted evidence.

Classification method:

`SCA Driver -> Facility -> Affected System/Term -> Regulatory PDF(s) -> Required Regulatory Document Change`

Documents were classified by mapping SCA-001 through SCA-006 change families to the regulatory inventory, then checking targeted PDF text where useful. Where drawing PDFs had weak or no extractable text, impact classification uses document role, drawing title, and SCA evidence; those rows and notes label the basis as inferred from drawing scope.

## 3-25 Regulatory Submittal Impact Table

| File No. | File Name | Revision | Date | Current Contents | Impact Status | Change Driver(s) | Required Action Summary | Evidence Basis |
|---:|---|---|---|---|---|---|---|---|
| 1 | `1. By Tourmaline/03-25-080-15_SCHA Letter_Environmental Effects Assessment.pdf` | Not stated | 2025-01-31 | Schedule A / SCHA environmental effects assessment correspondence. | Review Required | C3-SCA002, C3-SCA004 | Confirm whether environmental/effects statements, affected equipment, or consultation attachments still reflect retired 3-25 stabilization/SOC/dehydration scope. | PDF text includes SOC/NGL terms; SCA report changes project basis. |
| 2 | `1. By Tourmaline/100120203_C5+ and Inlet Compressor_PE Report_BRFN.pdf` | Not stated | 2025-01-28 | PE notification/report package for C5+ and inlet compressor scope. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Review for affected C5+, inlet compressor, condensate treating, stabilization, and shared-utility basis before re-use. | File title; SCA evidence changes C5+/inlet compressor scope and downstream interfaces. |
| 3 | `1. By Tourmaline/100120203_C5+ and Inlet Compressor_PE Report_DRFN.pdf` | Not stated | 2025-01-28 | PE notification/report package for C5+ and inlet compressor scope. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Same technical review as file 2; confirm recipient-specific transmittal text remains valid. | File title; SCA evidence changes C5+/inlet compressor scope and downstream interfaces. |
| 4 | `1. By Tourmaline/100120203_C5+ and Inlet Compressor_PE Report_HRFN.pdf` | Not stated | 2025-01-28 | PE notification/report package for C5+ and inlet compressor scope. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Same technical review as file 2; confirm recipient-specific transmittal text remains valid. | File title; SCA evidence changes C5+/inlet compressor scope and downstream interfaces. |
| 5 | `1. By Tourmaline/100120203_C5+ and Inlet Compressor_PE Report_MLIB.pdf` | Not stated | 2025-01-28 | PE notification/report package for C5+ and inlet compressor scope. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Same technical review as file 2; confirm recipient-specific transmittal text remains valid. | File title; SCA evidence changes C5+/inlet compressor scope and downstream interfaces. |
| 6 | `1. By Tourmaline/100120203_C5+ and Inlet Compressor_PE Report_SFN.pdf` | Not stated | 2025-01-28 | PE notification/report package for C5+ and inlet compressor scope. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Same technical review as file 2; confirm recipient-specific transmittal text remains valid. | File title; SCA evidence changes C5+/inlet compressor scope and downstream interfaces. |
| 7 | `1. By Tourmaline/100120203_C5+ and Inlet Compressor_PE Report_WMFN.pdf` | Not stated | 2025-01-28 | PE notification/report package for C5+ and inlet compressor scope. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Same technical review as file 2; confirm recipient-specific transmittal text remains valid. | File title; SCA evidence changes C5+/inlet compressor scope and downstream interfaces. |
| 8 | `1. By Tourmaline/2024 Tourmaline Fugitive Emission Management Plan (Signed).pdf` | Signed | 2023-10-02 | Corporate fugitive emission management plan. | No Change Expected | None | No project-specific revision identified; keep as corporate supporting plan unless regulatory reviewer requests current signed version. | Targeted text has generic facility terms but no material SCA contradiction. |
| 9 | `1. By Tourmaline/3-25 West Doe Project Schedule.pdf` | Not stated | 2025-02-03 | One-page project schedule/objective summary. | Change Required | C3-SCA001, C3-SCA002 | Update scope/objective text to remove 3-25 dehydration/stabilization/SOC/heat-medium assumptions and align timing with transferred 4-25 stabilization scope. | PDF text includes "dehydration"; SCA-001/SCA-002 retire that local scope. |
| 10 | `1. By Tourmaline/BCER Project Description Form - 3-25 West Doe (2025-01-31).pdf` | Not stated | 2025-01-31 | BCER project description form for 3-25. | Change Required | C3-SCA001 through C3-SCA006 | Re-issue project description with current equipment list, process narrative, shared utilities, incinerator/flare boundary, LACT OUT, and 4-25 stabilization/SOC interface. | PDF text hits stabilizer/SOC/incinerator/instrument air; SCA report changes those bases. |
| 11 | `1. By Tourmaline/Tourmaline Plant Supervision Summary.pdf` | Not stated | 2017-07-05 | General plant supervision summary. | No Change Expected | None | No SCA-driven content change identified. | Generic operations support document; no targeted project-scope contradiction found. |
| 12 | `1. By Tourmaline/Tourmaline Sand Management Plan - Revisions July 26, 2017.pdf` | Revisions July 26, 2017 | 2021-10-12 | General sand management plan. | No Change Expected | None | No SCA-driven content change identified. | Generic plan; targeted text only shows incidental TEG term. |
| 13 | `1. By Tourmaline/West Doe Gathering (2025-02-03).pdf` | Not stated | 2025-02-03 | West Doe gathering-system context document. | Review Required | C3-SCA002, D4-SCA001 | Review system schematic/narrative for stabilization relocation, NGL terminology, and 3-25 VRU discharge to 4-25 SOC suction. | PDF text hits stabilization/NGL/LPG; cross-facility SCA changes gathering/process interfaces. |
| 14 | `BFD-242510-100_200_300 (3-25 Doe)_Block Flow Diagram_rA.pdf` | rA | 2024-11-22 | Block flow diagram. | Change Required | C3-SCA001 through C3-SCA006 | Revise blocks and interfaces for retired 3-25 dehydration/stabilizer/SOC/heat-medium, non-regenerative treating, VRU to 4-25 SOC, shared IA/fuel gas/power, and incinerator/flare boundary. | Inferred from drawing scope; targeted SCA evidence directly changes represented process blocks. |
| 15 | `CIV-242510-5001 & 5002 (3-25 Doe)_Plot  Plan_rC.pdf` | rC | 2024-11-22 | Civil plot plan set. | Change Required | C3-SCA001 through C3-SCA006 | Remove or relabel retired units/plot reservations, update incinerator/shared flare location/interface, LACT boundary, heat-medium/instrument-air assumptions, and affected package layout. | PDF text hits dehydration/stabilizer/SOC/heat medium/incinerator/LACT/IA; drawing impact inferred from scope. |
| 16 | `MFS-242510 (3-25 Doe)_P&ID_rA.pdf` | rA | 2024-12-10 | P&ID package. | Change Required | C3-SCA001 through C3-SCA006 | Revise process, utility, relief, control, shutdown, and interface sheets for all retired/relocated units and new shared utility/VRU/incinerator bases. | Inferred from drawing scope and targeted SCA process/interface changes. |
| 17 | `MSS-242510-1001 (3-25 Doe)_Metering Schematic_rA.pdf` | rA | 2024-12-06 | Metering schematic. | Review Required | C3-SCA001, C3-SCA003 | Confirm NRM connector and LACT OUT basis are reflected; revise only if metering/transfer points still imply on-site 3-25 LACT units. | SCA-001/SCA-003 change LACT and pipeline destination basis. |
| 18 | `PFD-242510 (3-25 Doe)_Process Flow Diagram_rA.pdf` | rA | 2024-11-22 | Process flow diagram package. | Change Required | C3-SCA001 through C3-SCA006 | Update process flow paths, material interfaces, utility ties, and removed equipment blocks; add/clarify 4-25 SOC and 4-25 IA interfaces. | Inferred from drawing scope; targeted SCA evidence changes represented process flows, with related text hits in linked reports. |
| 19 | `W242510-CIV-REP-000001-001 (3-25 Doe)_Surface Water Management Plan_rA.pdf` | rA | 2023-09-27 | Surface water management plan. | Review Required | C3-SCA001, C3-SCA002 | Check drainage/containment areas for retired dehydration/stabilizer/heat-medium/LACT units and added/retained incinerator/shared flare areas. | PDF text hits retired terms; physical layout changes may affect drainage assumptions. |
| 20 | `W242510-ELC-REP-000001-001 (3-25 Doe)_Light Assessment_rA.pdf` | rA | 2024-11-05 | Light assessment. | Review Required | C3-SCA001, C3-SCA002 | Update project description and lighting inventory if retired units or retained incinerator/flare/shared utility equipment change lighting sources. | PDF text contains old dehydration/stabilization/LACT/heat-medium narrative. |
| 21 | `W242510-ELC-REP-000002-001 (3-25 Doe)_Ground Permissive at Truck-Out_rA.pdf` | rA | 2024-11-12 | Ground permissive at truck-out philosophy. | Review Required | C3-SCA001, C3-SCA003 | Confirm truck-out scope and NRM LACT interface remain correct after LACT OUT and 480 V dry-type transformer decision. | PDF text hits LACT/truck-out/ground permissive; SCA changes LACT boundary. |
| 22 | `W242510-PRC-DBM-000001-001 (3-25 Doe)_DBM_rA.pdf` | rA | 2024-12-17 | Design basis memorandum. | Change Required | C3-SCA001 through C3-SCA006 | Rewrite DBM sections for removed/retired scope, process selection, shared utilities, 4-25 interfaces, flare/incinerator basis, horsepower, package roster, and supersession notes. | PDF text hits every major changed term; SCA report is DBM amendment basis. |
| 23 | `W242510-PRC-HMB-000001-001 (3-25 Doe)_HMB_rA.pdf` | rA | 2024-11-22 | Heat and material balance. | Change Required | C3-SCA001, C3-SCA002, C3-SCA006 | Recalculate HMB around removed stabilization/SOC/heat-medium/dehydration, non-regenerative treating, VRU discharge, and shared IA demands where represented. | PDF text hits SOC/incinerator/LACT/VRU/disulphide/spent caustic. |
| 24 | `W242510-PRC-REG-000001-001 (3-25 Doe)_Emissions Summary_rA.pdf` | rA | 2024-12-02 | Emissions summary. | Change Required | C3-SCA001 through C3-SCA006 | Recalculate emissions for removed heat-medium/stabilizer/SOC/dehydration sources, changed incinerator/feed basis, VRU routing, and shared utilities. | PDF text hits stabilizer/SOC/heat-medium/incinerator/flare/VRU. |
| 25 | `W242510-PRC-REP-000001-001 (3-25 Doe)_Non-Flare Connected PSV Summary_rA.pdf` | rA | 2023-09-13 | Non-flare connected PSV summary. | Change Required | C3-SCA001, C3-SCA002, C3-SCA003 | Remove retired equipment PSV entries, update relief/non-flare classification, and confirm current inlet separator/caustic/flare boundary PSV basis. | PDF text hits retired terms and flare/IA/LACT context. |
| 26 | `W242510-PRC-REP-000002-001 (3-25 Doe)_Inlet Separator Summary_rA.pdf` | rA | 2024-11-04 | Inlet separator summary. | Change Required | C3-SCA002, C3-SCA003 | Update to twin 9 ft x 40 ft horizontal 3-phase basis, plot for third as applicable, downstream 4-25 stabilization/SOC context, and current interface conditions. | SCA-002 changed separator sizing; PDF title identifies the affected inlet separator summary. |
| 27 | `W242510-PRC-REP-000003-001 (3-25 Doe)_Prime Mover List_rA.pdf` | rA | 2024-11-06 | Prime mover list. | Change Required | C3-SCA001, C3-SCA002, C3-SCA003, C3-SCA006 | Remove or reclassify retired prime movers, update inlet-compressor drive/VFD basis, standby generator strategy, and local IA/heat-medium equipment. | PDF text hits heat medium/LACT/VFD/VRU; SCA changes prime mover assumptions. |
| 28 | `W242510-PRC-REP-000004-001 (3-25 Doe)_Facility Shutdown & Blowdown Philosophy_rA.pdf` | rA | 2024-11-26 | Shutdown and blowdown philosophy. | Change Required | C3-SCA001 through C3-SCA006 | Update shutdown/blowdown scenarios, cause/effect assumptions, relief/blowdown destination, retired units, shared IA/power, and 4-25 SOC interface. | PDF text hits all major changed systems; flare/blowdown packages affected. |
| 29 | `W242510-PRC-REP-000005-001 (3-25 Doe)_Flare Stack Data Submission_rA.pdf` | rA | 2024-11-26 | Flare stack data submission. | Change Required | C3-SCA001, C3-SCA002, C3-SCA003 | Recalculate flare/incinerator loads and update shared flare/incinerator boundary, retired relief sources, and non-regenerative caustic/incinerator feed basis. | PDF text hits caustic regeneration, incinerator, flare, depropanizer/LPG, stabilizer/SOC. |
| 30 | `W242510-PRC-REP-000007-001 (3-25 Doe)_DEOS_rB.pdf` | rB | 2024-11-12 | DEOS report. | Review Required | C3-SCA001, C3-SCA002, C3-SCA003 | Confirm whether DEOS is limited to retained gas dehydration or incorrectly includes retired condensate dehydration/caustic-regeneration/incinerator assumptions. | PDF text hits dehydration/SOC/incinerator/flare/VRU. |
| 31 | `W242510-PRC-REP-000008-001 (3-25 Doe)_Safety and Loss Management_rA.pdf` | rA | 2023-09-27 | Safety and loss management report. | Review Required | C3-SCA001 through C3-SCA006 | Update safety narrative if retired/relocated units, shared utilities, flare/incinerator, or shutdown/blowdown changes alter safeguards or responsibilities. | PDF text includes stale process narrative; SCA changes hazardous systems. |
| 32 | `W242510-PRJ-LST-000003-001 (3-25 Doe)_HAZMAT List_rA.pdf` | rA | 2024-11-18 | Hazardous materials list. | Change Required | C3-SCA001, C3-SCA002, C3-SCA006 | Remove/adjust chemicals tied to retired condensate dehydration, heat-medium and local IA systems; confirm spent caustic/DSO basis under non-regenerative treating. | PDF text hits heat medium, TEG, spent caustic, IA dryer desiccant. |
| 33 | `W242510-PRJ-QAP-000001-001 (3-25 Doe)_QAP & Validation Report_rA.pdf` | rA | 2023-10-13 | QAP and validation report. | Review Required | C3-SCA004, C3-SCA005 | Confirm validation package lists and references include the SCA-004 package roster and SCA-005 retired-KTY cleanup where relevant. | SCA-004/SCA-005 add/clean derivative package structures. |
| 34 | `W242510-PRJ-REP-000001-001 (3-25 Doe)_Secondary Containment Plan_rA.pdf` | rA | 2023-09-27 | Secondary containment plan. | Change Required | C3-SCA001, C3-SCA002 | Update containment volumes/areas and material list for removed units, LACT boundary, non-regenerative caustic, spent caustic/DSO, and retained tanks. | PDF text hits dehydration/stabilizer/SOC/heat-medium/incinerator/LACT/spent caustic. |
| 35 | `W242510-PRJ-REP-000002-001 (3-25 Doe)_Adopted Codes & Standards_rA.pdf` | rA | 2024-11-04 | Adopted codes and standards. | Review Required | C3-SCA001 through C3-SCA006 | Review standards list for retired package standards and added/shared package standards; update if the document enumerates equipment-specific code bases. | PDF text includes stale scope terms; package roster changed. |
| 36 | `W242510-PRJ-REP-000003-001 (3-25 Doe)_Facility Security and Fire Protection_rA.pdf` | rA | 2024-11-04 | Facility security and fire protection. | Review Required | C3-SCA001 through C3-SCA006 | Confirm fire/security coverage reflects current equipment layout, deleted units, shared incinerator/flare responsibility, and tank/chemical changes. | PDF text includes stale process terms; physical hazard inventory changed. |
| 37 | `W242510-PRJ-REP-000004-001(3-25 Doe)_HAZID Study Report_rA.pdf` | rA | 2024-12-11 | HAZID study report. | Change Required | C3-SCA001 through C3-SCA006 | Reconcile HAZID nodes/scenarios and referenced documents with retired units, new interfaces, non-regenerative treating, shared flare/incinerator, and changed utilities. | PDF text references DEOS, inlet separator, flare data, LPG, spent caustic, ground permissive. |
| 38 | `W242510-PRJ-REP-000005-001 (3-25 Doe)_Prelim Consequence Assessment_rA.pdf` | rA | 2023-10-13 | Preliminary consequence assessment. | Change Required | C3-SCA001 through C3-SCA006 | Re-run scenario basis for removed/relocated equipment, changed relief/incinerator loads, changed hazardous inventory, and current shutdown/blowdown assumptions. | PDF text includes old dehydration/stabilization/LACT/heat-medium narrative. |
| 39 | `W242510-PRJ-REP-000006-001 (3-25 Doe)_Noise Impact Assessment_r2.pdf` | r2 | 2025-01-14 | Noise impact assessment. | Change Required | C3-SCA001 through C3-SCA006, D4-SCA001 | Rebuild noise model inventory to remove retired local units, update 4-25 shifted sources/interfaces, IA consolidation, incinerator location, and current equipment counts. | PDF text contains old 3-25 stabilizer/heat-medium/IA/LACT and 4-25 VRU/incinerator source entries. |

---

## 4-25 Regulatory Submittal Impact Table

| File No. | File Name | Revision | Date | Current Contents | Impact Status | Change Driver(s) | Required Action Summary | Evidence Basis |
|---:|---|---|---|---|---|---|---|---|
| 1 | `006810-NIA-000 (4-25 Doe)_Noise Impact Assessment_r0.pdf` | r0 | 2023-11-30 | Noise impact assessment. | Change Required | D4-SCA001 through D4-SCA006, C3-SCA002 | Rebuild acoustic inventory and scenarios for LPG-to-NGL, depropanizer removal, stabilizer/SOC consolidation, IA consolidation, heat medium changes, and shared incinerator. | PDF text hits LPG/NGL/depropanizer/stabilizer/SOC/IA/heat medium/incinerator. |
| 2 | `1. By Tourmaline/02-25-080-15W6_Revision Letter_Pre-Con Env Assessment_26Sep2023.pdf` | Revision letter | 2023-09-26 | Pre-construction environmental assessment revision letter. | Review Required | D4-SCA001, D4-SCA003 | Confirm environmental revision letter remains accurate after NGL/current-scope and depropanizer decisions. | PDF text hits SOC/NGL/TEG; SCA changes current facility scope. |
| 3 | `1. By Tourmaline/2-25 Project Description Form Final Draft_V2-20231102.pdf` | V2 | 2023-11-02 | Project description form. | Change Required | D4-SCA001, D4-SCA002, D4-SCA006 | Update project description for NGL rather than LPG, depropanizer removal, current stabilizer/SOC scope, shared incinerator, and instrument air serving both facilities. | PDF text hits LPG/flare/truck-out; SCA changes scope. |
| 4 | `1. By Tourmaline/2024 Tourmaline Fugitive Emission Management Plan (Al Signed).pdf` | Signed | 2023-10-02 | Corporate fugitive emission management plan. | No Change Expected | None | No project-specific revision identified; retain unless a newer signed corporate plan is required. | Generic corporate plan; no material SCA contradiction found. |
| 5 | `1. By Tourmaline/8-33 to West Doe Map.pdf` | Not stated | 2023-09-28 | Route/context map. | No Change Expected | None | No SCA-driven map change identified. | No targeted scope-change contradiction found. |
| 6 | `1. By Tourmaline/Tourmaline Plant Supervision Plan.pdf` | Not stated | 2017-07-05 | Plant supervision plan. | No Change Expected | None | No SCA-driven content change identified. | Generic operations plan. |
| 7 | `1. By Tourmaline/Tourmaline Sand Management Plan - Revisions July 26, 2017.pdf` | Revisions July 26, 2017 | 2021-10-12 | Sand management plan. | No Change Expected | None | No SCA-driven content change identified. | Generic plan; targeted text only shows incidental TEG term. |
| 8 | `1. By Tourmaline/West Doe Gas Plant Proliferation Review.pdf` | Not stated | 2017-06-23 | Gas plant proliferation review. | Review Required | D4-SCA001, C3-SCA002 | Confirm proliferation/expansion conclusions remain valid with 4-25 now receiving 3-25 stabilization/SOC and IA service. | Document role; SCA evidence changes cross-facility development basis. |
| 9 | `1. By Tourmaline/West Doe Gathering System Schematic.pdf` | Not stated | 2023-10-05 | Gathering system schematic. | Review Required | D4-SCA001, C3-SCA002 | Review schematic for stabilization consolidation, NGL terminology, and 3-25 VRU-to-4-25 SOC interface. | PDF text hits stabilization/NGL; SCA changes gathering/process routing. |
| 10 | `1. By Tourmaline/West Doe Project Schedule.pdf` | Not stated | 2023-10-17 | Project schedule. | Review Required | D4-SCA001 through D4-SCA006 | Confirm milestone/scope language remains current after depropanizer removal, package roster changes, and shared utility decisions. | Targeted SCA package and scope evidence may affect schedule content. |
| 11 | `100118719_FAC_2 25-80-15W6 (4-25 Doe)_PE Report.pdf` | Not stated | 2023-10-31 | Facility PE report. | Review Required | D4-SCA001 through D4-SCA006 | Engineering sign-off package should be checked for old LPG/depropanizer, heat-medium, IA, incinerator, and stabilizer/SOC assumptions. | File role; targeted SCA evidence changes the engineered facility basis. |
| 12 | `BFD-235633-100_200_5100 (4-25 Doe)_Block Flow Diagram_rC.pdf` | rC | 2023-10-26 | Block flow diagram. | Change Required | D4-SCA001 through D4-SCA006 | Revise process blocks for NGL current scope, depropanizer removal, non-regenerative treating, IA consolidation, heat medium, mole sieve, stabilizer/SOC, and shared incinerator. | Inferred from drawing scope and targeted SCA process changes. |
| 13 | `CIV-235633-5001 (4-25 Doe)_Plot Plan_rK.pdf` | rK | 2024-10-24 | Civil plot plan sheet. | Change Required | D4-SCA001 through D4-SCA006 | Update layout for removed depropanizer/LPG future scope, current NGL packages, stabilizer/SOC consolidation, IA building, heat-medium configuration, and incinerator interface. | Inferred from drawing scope and targeted SCA package/equipment changes. |
| 14 | `CIV-235633-5002 (4-25 Doe)_Plot Plan_rK.pdf` | rK | 2025-04-21 | Civil plot plan package. | Change Required | D4-SCA001 through D4-SCA006 | Same plot-plan update as file 13; also check current rK sheet set for late partial updates against SCA-006 IA basis. | PDF text hits stabilizer/SOC/heat medium/incinerator/IA/LPG/depropanizer/mole sieve. |
| 15 | `MFS-235633 (4-25 Doe)_P&ID_rA.pdf` | rA | 2023-10-27 | P&ID package. | Change Required | D4-SCA001 through D4-SCA006 | Revise process, utility, relief, controls, and interface sheets for all current NGL, stabilizer/SOC, heat medium, IA, incinerator, and electrical decisions. | Inferred from drawing scope and targeted SCA process/interface changes. |
| 16 | `MSS-235633-1001 (4-25 Doe)_Metering Schematic_rB.pdf` | rB | 2025-04-21 | Metering schematic. | Review Required | D4-SCA001, D4-SCA003 | Confirm product/metering labels reflect NGL rather than LPG/C3-C4/depropanizer framing and no retired product stream remains. | SCA normalizes LPG to NGL and removes depropanizer. |
| 17 | `PFD-235633 (4-25 Doe)_Process Flow Diagram_rB.pdf` | rB | 2023-10-26 | Process flow diagram package. | Change Required | D4-SCA001 through D4-SCA006 | Update all flow paths and balances for NGL, removed depropanizer, stabilizer/SOC consolidation, inlet HEX, heat medium, TEG/mole sieve, IA, and incinerator basis. | Inferred from drawing scope and targeted SCA process changes. |
| 18 | `W235633-CIV-REP-000001-001 (4-25 Doe)_Surface Water Management Plan_rB.pdf` | rB | 2023-09-27 | Surface water management plan. | Review Required | D4-SCA001, D4-SCA004 | Check drainage/containment assumptions for current NGL/stabilizer/IA/heat-medium package layout and removed LPG/depropanizer scope. | PDF text hits LPG/NGL/heat medium/mole sieve; physical layout changed. |
| 19 | `W235633-ELC-REP-000001-001 (4-25 Doe)_Light Assessment_rC.pdf` | rC | 2023-09-26 | Light assessment. | Review Required | D4-SCA001, D4-SCA004, D4-SCA006 | Update lighting inventory and project description if package layout or current equipment differs from the submitted assessment. | PDF text hits LPG/NGL/heat medium/mole sieve and old process narrative. |
| 20 | `W235633-ELC-REP-000002-001 (4-25 Doe)_Ground Permissive at Truck-Out_rB.pdf` | rB | 2023-09-26 | Ground permissive at truck-out philosophy. | Review Required | D4-SCA001, D4-SCA003 | Confirm truck-out/product terminology and product streams reflect NGL current scope and not LPG/depropanizer framing. | PDF text hits LPG/NGL/truck-out; product scope changed. |
| 21 | `W235633-PRC-DBM-000001-001 (4-25 Doe)_Design Basis Memorandum_rA.pdf` | rA | 2023-10-23 | Design basis memorandum. | Change Required | D4-SCA001 through D4-SCA006 | Rewrite DBM sections for current NGL, depropanizer removal, non-regenerative treating, stabilizer/SOC scope, heat medium, TEG/mole sieve, IA, incinerator, electrical, and package roster. | PDF text hits every major changed term; SCA report is DBM amendment basis. |
| 22 | `W235633-PRC-HMB-000001-001 (4-25 Doe)_HMB Winter_rC.pdf` | rC | 2023-10-24 | Winter HMB. | Change Required | D4-SCA001 through D4-SCA006 | Recalculate winter HMB for NGL, no depropanizer, non-regenerative treating, changed heat medium, TEG/mole sieve, IA demand, and incinerator feed. | PDF text hits LPG, SOC, incinerator, VRU, TEG, spent caustic. |
| 23 | `W235633-PRC-HMB-000002-001 (4-25 Doe)_HMB Summer_rC.pdf` | rC | 2023-10-24 | Summer HMB. | Change Required | D4-SCA001 through D4-SCA006 | Same as winter HMB, with summer operating basis and heat/refrigeration balance reviewed separately. | PDF text hits LPG, SOC, incinerator, VRU, TEG, spent caustic. |
| 24 | `W235633-PRC-REG-000001-001 (4-25 Doe)_Emissions Summary_rB.pdf` | rB | 2024-10-23 | Emissions summary. | Change Required | D4-SCA001 through D4-SCA006 | Recalculate emissions for removed depropanizer/LPG equipment, NGL treating, heat medium, IA, incinerator, stabilizer/SOC, flare, and equipment roster. | PDF text hits stabilizer/SOC/heat medium/incinerator/LPG/depropanizer/mole sieve. |
| 25 | `W235633-PRC-REP-000001-001 (4-25 Doe)_Non-Flare Connected PSV Summary_rA.pdf` | rA | 2023-09-29 | Non-flare connected PSV summary. | Change Required | D4-SCA001 through D4-SCA006 | Remove retired depropanizer/LPG PSV basis and update current NGL, stabilizer/SOC, heat medium, IA, and relief/non-flare classification. | PDF text hits depropanizer/LPG/NGL/heat medium/IA/PSV-relevant terms. |
| 26 | `W235633-PRC-REP-000002-001 (4-25 Doe)_Inlet Separator Summary.pdf` | Not stated | 2023-09-29 | Inlet separator summary. | Change Required | D4-SCA001, D4-SCA005 | Update to current two 9 ft x 40 ft installed separators, future third plot, and inlet-separator HEX / MPFF preheat relationship. | SCA-001 changed separator sizing; SCA-005 registers the inlet-separator HEX subject. |
| 27 | `W235633-PRC-REP-000003-001 (4-25 Doe)_Prime Mover List_rC.pdf` | rC | 2023-03-01 | Prime mover list. | Change Required | D4-SCA001, D4-SCA006 | Update drivers/motors for current stabilizer/SOC, heat medium, TEG/mole sieve, instrument air, VFD, capacitor-bank removal, and standby power basis; remove depropanizer/LPG equipment if present. | PDF text hits LPG/NGL/stabilizer/heat medium/VFD/mole sieve. |
| 28 | `W235633-PRC-REP-000004-001 (4-25 Doe)_Plant Shutdown & Blowdown Philosophy_rB.pdf` | rB | 2023-09-29 | Shutdown and blowdown philosophy. | Change Required | D4-SCA001 through D4-SCA006 | Update shutdown/blowdown causes, relief destinations, current NGL process, depropanizer removal, heat medium, IA, and incinerator/shared interface responsibilities. | PDF text hits depropanizer/LPG/NGL/heat medium/incinerator/IA. |
| 29 | `W235633-PRC-REP-000005-001 (4-25 Doe)_Flare Stack Data Submission_rA.pdf` | rA | 2023-10-27 | Flare stack data submission. | Change Required | D4-SCA001, D4-SCA002, D4-SCA003 | Recalculate flare/incinerator loads and feed basis; remove caustic-regeneration/depropanizer relief bases; identify 3-25 physical incinerator location. | PDF text hits caustic regeneration/incinerator/flare/LPG/depropanizer/mole sieve. |
| 30 | `W235633-PRC-REP-000007-001 (4-25 Doe)_DEOS_rB.pdf` | rB | 2023-10-25 | DEOS report. | Review Required | D4-SCA001, D4-SCA005 | Confirm whether DEOS is limited to retained dehydration equipment and does not carry obsolete LPG/depropanizer/non-current incinerator assumptions. | PDF text hits dehy/SOC/incinerator/flare/VRU/TEG. |
| 31 | `W235633-PRC-REP-000008-001 (4-25 Doe)_Safety & Loss Management_rA.pdf` | rA | 2023-09-27 | Safety and loss management report. | Review Required | D4-SCA001 through D4-SCA006 | Update safety narrative if NGL/depropanizer removal, shared incinerator, IA, heat medium, or shutdown/blowdown changes alter safeguards or responsibilities. | PDF text hits LPG/NGL/stabilization/SOC/heat medium/flare/mole sieve. |
| 32 | `W235633-PRJ-LST-000003-001 (4-25 Doe)_HAZMAT List_rC.pdf` | rC | 2023-09-27 | Hazardous materials list. | Change Required | D4-SCA001 through D4-SCA006 | Replace LPG/depropanizer-related chemicals with current NGL/DSO/spent caustic basis; update heat medium, IA dryer, TEG/mole sieve consumables. | PDF text hits LPG/NGL/heat medium/IA/TEG/mole sieve/spent caustic. |
| 33 | `W235633-PRJ-QAP-000001-001 (4-25 Doe)_QAP & Validation Report_rA.pdf` | rA | 2023-10-19 | QAP and validation report. | Review Required | D4-SCA004, D4-SCA005 | Confirm validation package lists and references include SCA-004 package roster and SCA-005 content remediation. | SCA-004/SCA-005 add/clean derivative package structures. |
| 34 | `W235633-PRJ-REP-000001-001 (4-25 Doe)_Secondary Containment Plan_rB.pdf` | rB | 2023-09-27 | Secondary containment plan. | Change Required | D4-SCA001 through D4-SCA006 | Update containment basis for NGL instead of LPG, no depropanizer, non-regenerative caustic, DSO/spent caustic, heat medium, and package layout changes. | PDF text hits depropanizer/LPG/NGL/heat medium/incinerator/spent caustic. |
| 35 | `W235633-PRJ-REP-000002-001 (4-25 Doe)_Adopted Codes & Standards_rB.pdf` | rB | 2023-09-27 | Adopted codes and standards. | Review Required | D4-SCA001 through D4-SCA006 | Review standards list for retired depropanizer/LPG standards and current NGL, heat-medium, mole sieve, IA, incinerator, and electrical package standards. | PDF text includes stale scope terms and affected package categories. |
| 36 | `W235633-PRJ-REP-000003-001 (4-25 Doe)_Facility Security & Fire Protection_rC.pdf` | rC | 2023-09-27 | Facility security and fire protection. | Review Required | D4-SCA001 through D4-SCA006 | Confirm fire/security coverage reflects current equipment layout, hazardous inventory, and shared incinerator/utility responsibility. | PDF text includes LPG/NGL/heat medium/flare/mole sieve terms. |
| 37 | `W235633-PRJ-REP-000004-001 (4-25 Doe)_HAZID Study Report_r0.pdf` | r0 | 2023-10-05 | HAZID study report. | Change Required | D4-SCA001 through D4-SCA006 | Reconcile HAZID nodes/scenarios and referenced documents with depropanizer removal, NGL basis, non-regenerative caustic, IA, heat medium, mole sieve, and shared incinerator. | PDF text hits every major changed term including depropanizer/LPG/incinerator/IA/heat medium/mole sieve. |
| 38 | `W235633-PRJ-REP-000005-001 (4-25 Doe)_Prelim Consequence Assessment_rA.pdf` | rA | 2023-10-13 | Preliminary consequence assessment. | Change Required | D4-SCA001 through D4-SCA006 | Re-run consequence basis for removed/changed equipment, changed inventory, shared incinerator, relief/blowdown, and utility interfaces. | PDF text includes LPG/NGL/heat medium/mole sieve/stabilization terms. |
| 39 | `W235633-PRJ-REP-000006-001 (4-25 Doe)_Design Change Summary_rB.pdf` | rB | 2023-09-27 | Design change summary. | Change Required | D4-SCA001 through D4-SCA006 | Rewrite change summary to capture all SCA decisions: depropanizer out, NGL current scope, stabilizer/SOC consolidation, instrument air serving both facilities, heat medium, HEX, mole sieve, incinerator, and standby/VFD/capacitor electrical changes. | PDF text hits depropanizer/LPG/NGL/heat medium/incinerator/LACT/plot-related terms. |

---

## 3-25 Detailed Document Change Notes

### 1. `03-25-080-15_SCHA Letter_Environmental Effects Assessment.pdf`
- **Why this document is impacted:** The assessment correspondence may rely on pre-SCA project descriptions or equipment lists.
- **Specific expected revisions:** Review environmental effects, footprint, emissions/noise attachments, and consultation attachments for retired 3-25 stabilization/SOC/dehydration and current shared-incinerator basis.
- **Evidence used:** PDF text extraction found SOC/NGL terminology; SCA-002 and SCA-004 changed process scope and package structure.
- **Review caveats:** Regulatory counsel/environmental lead should decide whether a revision letter is enough.

### 2. `100120203_C5+ and Inlet Compressor_PE Report_BRFN.pdf`
- **Why this document is impacted:** This BRFN PE report is explicitly tied to C5+ and inlet compressor scope, which changed materially.
- **Specific expected revisions:** Align the common technical content for non-regenerative treating, no 3-25 stabilizers/SOC/heat medium, inlet separator/compressor basis, VRU-to-4-25 SOC routing, and shared utilities.
- **Evidence used:** The regulatory PDF title identifies C5+ and inlet compressor scope; C3-SCA001, C3-SCA002, and C3-SCA003 modify the affected scope basis.
- **Review caveats:** Confirm whether recipient-specific consultation records require a revision letter or a full replaced attachment.

### 3. `100120203_C5+ and Inlet Compressor_PE Report_DRFN.pdf`
- **Why this document is impacted:** This DRFN PE report is explicitly tied to C5+ and inlet compressor scope, which changed materially.
- **Specific expected revisions:** Align the common technical content for non-regenerative treating, no 3-25 stabilizers/SOC/heat medium, inlet separator/compressor basis, VRU-to-4-25 SOC routing, and shared utilities.
- **Evidence used:** The regulatory PDF title identifies C5+ and inlet compressor scope; C3-SCA001, C3-SCA002, and C3-SCA003 modify the affected scope basis.
- **Review caveats:** Confirm whether recipient-specific consultation records require a revision letter or a full replaced attachment.

### 4. `100120203_C5+ and Inlet Compressor_PE Report_HRFN.pdf`
- **Why this document is impacted:** This HRFN PE report is explicitly tied to C5+ and inlet compressor scope, which changed materially.
- **Specific expected revisions:** Align the common technical content for non-regenerative treating, no 3-25 stabilizers/SOC/heat medium, inlet separator/compressor basis, VRU-to-4-25 SOC routing, and shared utilities.
- **Evidence used:** The regulatory PDF title identifies C5+ and inlet compressor scope; C3-SCA001, C3-SCA002, and C3-SCA003 modify the affected scope basis.
- **Review caveats:** Confirm whether recipient-specific consultation records require a revision letter or a full replaced attachment.

### 5. `100120203_C5+ and Inlet Compressor_PE Report_MLIB.pdf`
- **Why this document is impacted:** This MLIB PE report is explicitly tied to C5+ and inlet compressor scope, which changed materially.
- **Specific expected revisions:** Align the common technical content for non-regenerative treating, no 3-25 stabilizers/SOC/heat medium, inlet separator/compressor basis, VRU-to-4-25 SOC routing, and shared utilities.
- **Evidence used:** The regulatory PDF title identifies C5+ and inlet compressor scope; C3-SCA001, C3-SCA002, and C3-SCA003 modify the affected scope basis.
- **Review caveats:** Confirm whether recipient-specific consultation records require a revision letter or a full replaced attachment.

### 6. `100120203_C5+ and Inlet Compressor_PE Report_SFN.pdf`
- **Why this document is impacted:** This SFN PE report is explicitly tied to C5+ and inlet compressor scope, which changed materially.
- **Specific expected revisions:** Align the common technical content for non-regenerative treating, no 3-25 stabilizers/SOC/heat medium, inlet separator/compressor basis, VRU-to-4-25 SOC routing, and shared utilities.
- **Evidence used:** The regulatory PDF title identifies C5+ and inlet compressor scope; C3-SCA001, C3-SCA002, and C3-SCA003 modify the affected scope basis.
- **Review caveats:** Confirm whether recipient-specific consultation records require a revision letter or a full replaced attachment.

### 7. `100120203_C5+ and Inlet Compressor_PE Report_WMFN.pdf`
- **Why this document is impacted:** This WMFN PE report is explicitly tied to C5+ and inlet compressor scope, which changed materially.
- **Specific expected revisions:** Align the common technical content for non-regenerative treating, no 3-25 stabilizers/SOC/heat medium, inlet separator/compressor basis, VRU-to-4-25 SOC routing, and shared utilities.
- **Evidence used:** The regulatory PDF title identifies C5+ and inlet compressor scope; C3-SCA001, C3-SCA002, and C3-SCA003 modify the affected scope basis.
- **Review caveats:** Confirm whether recipient-specific consultation records require a revision letter or a full replaced attachment.

### 9. `3-25 West Doe Project Schedule.pdf`
- **Why this document is impacted:** The schedule/objective text still references dehydration.
- **Specific expected revisions:** Remove 3-25 condensate dehydration and local stabilization/SOC implications; identify any 4-25 dependency for stabilization/SOC interfaces if the schedule lists them.
- **Evidence used:** PDF text extraction found "dehydration"; C3-SCA001 and C3-SCA002 retire local dehydration/stabilizer/SOC scope.
- **Review caveats:** Confirm whether this is a regulatory schedule or informational attachment before re-issuing.

### 10. `BCER Project Description Form - 3-25 West Doe (2025-01-31).pdf`
- **Why this document is impacted:** It is the primary regulatory project scope form and contains multiple superseded scope elements.
- **Specific expected revisions:** Update equipment list, process narrative, phase description, shared utilities, incinerator/flare location and service, LACT OUT, and 4-25 stabilization/SOC interface.
- **Evidence used:** PDF text hits stabilizer, SOC, incinerator, instrument air, inlet separator, truck-out; SCA-001 through SCA-006 change these bases.
- **Review caveats:** BCER form fields may require a formal amendment rather than a narrative appendix.

### 13. `West Doe Gathering (2025-02-03).pdf`
- **Why this document is impacted:** It contains gathering and process-interface context using stabilization/NGL/LPG terminology.
- **Specific expected revisions:** Review 3-25/4-25 flow routes, product terminology, and stabilization/SOC routing; update if the schematic implies local 3-25 stabilization or obsolete LPG framing.
- **Evidence used:** PDF text hits stabilization, NGL, and LPG; SCA-002 and D4-SCA001 modify the cross-facility routing.
- **Review caveats:** Some gathering context may remain unchanged if it is upstream-only.

### 14. `BFD-242510-100_200_300 (3-25 Doe)_Block Flow Diagram_rA.pdf`
- **Why this document is impacted:** Block diagrams are directly invalidated by removed and rerouted process blocks.
- **Specific expected revisions:** Remove 3-25 condensate dehydration, stabilizer, SOC, heat-medium blocks; show non-regenerative treating, 4-25 SOC suction interface, 4-25 IA supply, shared flare/incinerator basis, and LACT OUT boundary.
- **Evidence used:** SCA process decisions; drawing role and linked report text.
- **Review caveats:** Drawing text extraction is limited; confirm visually against original CAD/PDF.

### 15. `CIV-242510-5001 & 5002 (3-25 Doe)_Plot Plan_rC.pdf`
- **Why this document is impacted:** The plot plan still includes or references retired/changed physical equipment.
- **Specific expected revisions:** Remove/flag retired local units and cancelled future condensate dehydration plot space; show retained incinerator/shared flare and current utility/package locations.
- **Evidence used:** PDF text hits dehydration, stabilizer, SOC, heat medium, incinerator, LACT, instrument air, LPG/depropanizer terms; C3-SCA001 through C3-SCA006 alter the represented scope.
- **Review caveats:** CAD layer/source drawing review is required for final layout change.

### 16. `MFS-242510 (3-25 Doe)_P&ID_rA.pdf`
- **Why this document is impacted:** P&IDs carry the detailed process, utility, control, shutdown, and relief interfaces changed by the SCAs.
- **Specific expected revisions:** Remove retired process systems, update caustic treating, VRU discharge, shared IA/fuel gas/power, flare/incinerator, relief, shutdown, and LACT boundary sheets.
- **Evidence used:** The regulatory PDF is the 3-25 P&ID package; C3-SCA001 through C3-SCA006 alter systems shown on P&IDs.
- **Review caveats:** Requires discipline drawing list and line-by-line P&ID revision, not only narrative edits.

### 17. `MSS-242510-1001 (3-25 Doe)_Metering Schematic_rA.pdf`
- **Why this document is impacted:** Metering may still imply on-site LACT units or superseded transfer points.
- **Specific expected revisions:** Confirm NRM NEBC Connector and LACT OUT routing; update metering nodes if LACT or product transfer boundaries changed.
- **Evidence used:** The regulatory PDF is the 3-25 metering schematic; C3-SCA001 confirms LACT OUT and C3-SCA003 names the NRM NEBC Connector.
- **Review caveats:** May become no-change if schematic is upstream/gas-only.

### 18. `PFD-242510 (3-25 Doe)_Process Flow Diagram_rA.pdf`
- **Why this document is impacted:** The flow diagram must reflect retired and rerouted process systems.
- **Specific expected revisions:** Update equipment blocks, stream routes, 4-25 SOC suction tie-in, shared utility arrows, inlet separator basis, and incinerator/flare streams.
- **Evidence used:** The regulatory PDF is the 3-25 process flow diagram package; C3-SCA001 through C3-SCA006 alter represented process decisions.
- **Review caveats:** Flow values must be reconciled with revised HMB before final drawing issue.

### 19. `Surface Water Management Plan_rA.pdf`
- **Why this document is impacted:** Physical equipment and containment/drainage areas changed.
- **Specific expected revisions:** Check runoff, grading, drainage and containment assumptions for deleted units, retained incinerator/flare, and current tank/package layout.
- **Evidence used:** PDF text hits dehydration/stabilization/heat medium/LACT; SCA-001/SCA-002 alter physical scope.
- **Review caveats:** Requires civil layout confirmation before classifying exact changes.

### 20. `Light Assessment_rA.pdf`
- **Why this document is impacted:** The assessment narrative includes stale process/equipment scope and the lighting inventory may include deleted units.
- **Specific expected revisions:** Remove or update references to local dehydration/stabilization/LACT/heat-medium systems; verify lighting sources for retained incinerator/shared utilities.
- **Evidence used:** PDF text hits old scope terms; C3-SCA001 and C3-SCA002 remove or relocate several equipment bases that can affect the lighting inventory.
- **Review caveats:** If lighting fixtures did not move, only narrative revisions may be required.

### 21. `Ground Permissive at Truck-Out_rA.pdf`
- **Why this document is impacted:** The document is tied to truck-out and LACT-related electrical boundaries.
- **Specific expected revisions:** Confirm truck-out scope, LACT OUT boundary, NRM interface, and 480 V dry-type transformer implications.
- **Evidence used:** PDF text hits LACT/truck-out; SCA-001/SCA-003 change LACT and connector basis.
- **Review caveats:** Final revision depends on whether the ground permissive applies only to retained truck-out systems.

### 22. `W242510-PRC-DBM-000001-001 (3-25 Doe)_DBM_rA.pdf`
- **Why this document is impacted:** It is the central design basis and contains all major superseded scope families.
- **Specific expected revisions:** Rewrite process, utility, flare/incinerator, electrical, package roster, equipment list, objective, and supersession sections.
- **Evidence used:** PDF text hits every major SCA term; SCA report is DBM amendment basis.
- **Review caveats:** DBM should be revised before dependent regulatory reports are finalized.

### 23. `W242510-PRC-HMB-000001-001 (3-25 Doe)_HMB_rA.pdf`
- **Why this document is impacted:** Material balances change when stabilization/SOC/heat-medium/dehydration are removed or relocated.
- **Specific expected revisions:** Remove retired units and recalculate streams around inlet separation, condensate treating, VRU, shared incinerator, and 4-25 SOC interface.
- **Evidence used:** PDF text hits SOC/incinerator/LACT/VRU/spent caustic; SCA-002 reroutes flows.
- **Review caveats:** Requires process engineering recalculation.

### 24. `W242510-PRC-REG-000001-001 (3-25 Doe)_Emissions Summary_rA.pdf`
- **Why this document is impacted:** Emission sources and rates are directly affected by removed/changed equipment.
- **Specific expected revisions:** Recalculate emissions inventory for retired heat-medium/stabilization/SOC/dehydration, updated incinerator feed, VRU routing, and shared utilities.
- **Evidence used:** PDF text hits emissions-relevant changed equipment; C3-SCA001 through C3-SCA006 alter equipment, utility, flare/incinerator, and emissions bases.
- **Review caveats:** Should follow updated PFD/HMB and flare/incinerator basis.

### 25. `Non-Flare Connected PSV Summary_rA.pdf`
- **Why this document is impacted:** Relief devices tied to retired systems or changed flare boundaries may be obsolete.
- **Specific expected revisions:** Delete retired equipment PSVs, update non-flare/flare-connected status, and verify inlet separator and caustic treating relief basis.
- **Evidence used:** PDF text hits retired systems and flare/IA/LACT terms; C3-SCA001, C3-SCA002, and C3-SCA003 alter the PSV and relief-source basis.
- **Review caveats:** Requires P&ID and relief-device list review.

### 26. `Inlet Separator Summary_rA.pdf`
- **Why this document is impacted:** SCA-002 changes inlet separator sizing and downstream context.
- **Specific expected revisions:** Update to twin 9 ft x 40 ft horizontal 3-phase separators, plot for a third if applicable, and current downstream stabilization/SOC interface.
- **Evidence used:** The regulatory PDF is the 3-25 inlet separator summary; C3-SCA002 defines the changed separator basis and the PDF title identifies the affected separator document.
- **Review caveats:** Confirm final separator design pressure/temperature against revised PFD/P&ID.

### 27. `Prime Mover List_rA.pdf`
- **Why this document is impacted:** Prime movers and electrical starting strategies changed.
- **Specific expected revisions:** Update inlet compressor horsepower/VFD basis, delete retired heat-medium/local IA items, and align standby generator strategy.
- **Evidence used:** PDF text hits VFD/heat-medium/LACT/VRU; SCA-001/SCA-003 change VFD and horsepower.
- **Review caveats:** Electrical studies may be needed for final motor/driver ratings.

### 28. `Facility Shutdown & Blowdown Philosophy_rA.pdf`
- **Why this document is impacted:** Shutdown and blowdown logic depends on the current equipment and relief network.
- **Specific expected revisions:** Remove retired units, update blowdown destinations, shared IA/power failure modes, incinerator/flare boundary, and VRU/SOC interface handling.
- **Evidence used:** PDF text hits all major changed systems; C3-SCA001 through C3-SCA006 alter shutdown, blowdown, relief, utility, and interface assumptions.
- **Review caveats:** Should be revised with P&ID and cause/effect updates.

### 29. `Flare Stack Data Submission_rA.pdf`
- **Why this document is impacted:** Flare and incinerator loads are directly affected by retired units and non-regenerative caustic.
- **Specific expected revisions:** Recalculate flare loads, remove retired relief sources, update shared incinerator location/feed/flow basis, and reflect non-regenerative caustic streams.
- **Evidence used:** PDF text hits caustic regeneration/incinerator/flare/depropanizer/LPG terms; SCA-003 resolves flare boundary.
- **Review caveats:** Requires relief/blowdown calculation package.

### 30. `DEOS_rB.pdf`
- **Why this document is impacted:** It may mix retained gas dehydration with retired condensate dehydration or incinerator assumptions.
- **Specific expected revisions:** Confirm scope of the DEOS; remove retired condensate-dehydration or caustic-regeneration references if present.
- **Evidence used:** PDF text hits dehydration/SOC/incinerator/flare/VRU; C3-SCA001, C3-SCA002, and C3-SCA003 alter retained dehydration, incinerator, flare, and VRU context.
- **Review caveats:** May be no-change if it only covers retained gas dehydration.

### 31. `Safety and Loss Management_rA.pdf`
- **Why this document is impacted:** Hazard controls and responsibilities may change with deleted and shared systems.
- **Specific expected revisions:** Review and update safeguards, shared-asset responsibility, emergency isolation, and process narrative.
- **Evidence used:** PDF text has stale process narrative; SCA changes hazardous systems.
- **Review caveats:** May depend on revised HAZID and shutdown/blowdown philosophy.

### 32. `HAZMAT List_rA.pdf`
- **Why this document is impacted:** Chemical and waste inventories change with retired systems and non-regenerative treating.
- **Specific expected revisions:** Remove heat-medium/dehydration/local IA consumables if no longer applicable; confirm spent caustic, DSO, TEG, and tank inventories.
- **Evidence used:** PDF text hits spent caustic, heat medium, TEG, IA dryer desiccant; C3-SCA001, C3-SCA002, and C3-SCA006 alter the material inventory basis.
- **Review caveats:** Final quantities require updated HMB and tank list.

### 33. `QAP & Validation Report_rA.pdf`
- **Why this document is impacted:** The package/decomposition structure changed through SCA-004/SCA-005.
- **Specific expected revisions:** Check validation references, package roster, and retired-KTY cleanup status.
- **Evidence used:** The regulatory PDF is the 3-25 QAP and validation report; C3-SCA004 and C3-SCA005 change package roster and cleanup validation context.
- **Review caveats:** May be an administrative revision only.

### 34. `Secondary Containment Plan_rA.pdf`
- **Why this document is impacted:** Containment areas and inventories are affected by retired equipment and changed tank/chemical basis.
- **Specific expected revisions:** Update containment areas, volumes, tank services, spent caustic/DSO handling, and deleted LACT/dehydration/heat-medium equipment.
- **Evidence used:** PDF text hits dehydration/stabilizer/SOC/heat-medium/LACT/spent caustic; C3-SCA001 and C3-SCA002 alter containment-relevant equipment and material bases.
- **Review caveats:** Requires final tank list and plot plan.

### 35. `Adopted Codes & Standards_rA.pdf`
- **Why this document is impacted:** Equipment-specific codes may be stale after package roster changes.
- **Specific expected revisions:** Review for retired-unit standards and added/current package standards.
- **Evidence used:** SCA package roster changes and PDF stale terms.
- **Review caveats:** May be no-change if document is generic and not package-specific.

### 36. `Facility Security and Fire Protection_rA.pdf`
- **Why this document is impacted:** Physical layout, inventory, and shared incinerator/flare responsibility changed.
- **Specific expected revisions:** Review firewater/extinguishing, separation, access, hazardous inventory, shared asset responsibility, and response assumptions.
- **Evidence used:** PDF text includes stale scope terms; SCA changes physical hazard basis.
- **Review caveats:** Requires updated plot and HAZMAT list.

### 37. `HAZID Study Report_rA.pdf`
- **Why this document is impacted:** HAZID scenarios are based on superseded equipment and process interfaces.
- **Specific expected revisions:** Update nodes, scenarios, recommendations, referenced documents, and risk register for all SCA decisions.
- **Evidence used:** PDF references inlet separator, flare data, DEOS, LPG/spent caustic/ground permissive; SCA changes these bases.
- **Review caveats:** Requires facilitated review or formal addendum.

### 38. `Prelim Consequence Assessment_rA.pdf`
- **Why this document is impacted:** Consequence scenarios depend on current inventory, equipment, and relief/blowdown basis.
- **Specific expected revisions:** Reassess scenarios for retired equipment, shared flare/incinerator, changed chemicals, and utility failure modes.
- **Evidence used:** PDF text includes old dehydration/stabilization/LACT/heat-medium narrative; C3-SCA001 through C3-SCA006 alter consequence-relevant process, utility, and relief bases.
- **Review caveats:** Should follow revised HAZID and flare/blowdown data.

### 39. `Noise Impact Assessment_r2.pdf`
- **Why this document is impacted:** The noise model includes retired and shifted equipment sources.
- **Specific expected revisions:** Remove retired 3-25 stabilizer/heat-medium/local IA/LACT sources, update VRU/compressor/incinerator/shared equipment, and reconcile 4-25 shifted sources.
- **Evidence used:** PDF text lists 3-25 stabilizers, heat-medium, IA, LACT, VRU, 4-25 incinerator and VRU sources; C3-SCA001, C3-SCA002, and C3-SCA006 alter noise-source and utility assumptions.
- **Review caveats:** Requires acoustic model update and regulatory noise specialist review.

---

## 4-25 Detailed Document Change Notes

### 1. `006810-NIA-000 (4-25 Doe)_Noise Impact Assessment_r0.pdf`
- **Why this document is impacted:** It contains many superseded equipment/source terms.
- **Specific expected revisions:** Rebuild noise source inventory for NGL current scope, removed depropanizer, current stabilizer/SOC, heat medium, IA, mole sieve/TEG, and shared incinerator.
- **Evidence used:** PDF text hits LPG/NGL/depropanizer/stabilizer/SOC/IA/heat medium/incinerator; D4-SCA001 through D4-SCA006 alter noise-source and process/equipment bases.
- **Review caveats:** Requires acoustic model re-run.

### 2. `02-25-080-15W6_Revision Letter_Pre-Con Env Assessment_26Sep2023.pdf`
- **Why this document is impacted:** Environmental assessment revision may rely on pre-SCA 4-25 scope.
- **Specific expected revisions:** Review for LPG/depropanizer/future-scope framing, NGL current scope, and shifted stabilization/SOC/IA assumptions.
- **Evidence used:** PDF text hits SOC/NGL/TEG.
- **Review caveats:** Environmental lead should decide whether a letter addendum is enough.

### 3. `2-25 Project Description Form Final Draft_V2-20231102.pdf`
- **Why this document is impacted:** Project description forms must match current process scope.
- **Specific expected revisions:** Replace LPG/depropanizer/future framing with current NGL scope; add/confirm shared incinerator and instrument air serving both facilities.
- **Evidence used:** PDF text hits LPG/flare/truck-out; SCA-001/SCA-002/SCA-006 change these bases.
- **Review caveats:** Confirm BCER form version requirements.

### 8. `West Doe Gas Plant Proliferation Review.pdf`
- **Why this document is impacted:** Facility proliferation conclusions may be affected by shifted/consolidated scope.
- **Specific expected revisions:** Review conclusions against 4-25 receiving 3-25 stabilizer/SOC functions and consolidated IA.
- **Evidence used:** The regulatory PDF is the West Doe gas plant proliferation review; D4-SCA001 and C3-SCA002 create cross-facility scope changes relevant to its role.
- **Review caveats:** May remain unchanged if only high-level historic context.

### 9. `West Doe Gathering System Schematic.pdf`
- **Why this document is impacted:** Gathering/process routing changed at the 3-25/4-25 interface.
- **Specific expected revisions:** Update stabilization, NGL terminology, and 3-25 VRU to 4-25 SOC routing if shown.
- **Evidence used:** PDF text hits stabilization/NGL; D4-SCA001 and C3-SCA002 alter the 4-25 NGL basis and the cross-facility stabilization/SOC interface.
- **Review caveats:** Upstream gathering-only portions may not change.

### 10. `West Doe Project Schedule.pdf`
- **Why this document is impacted:** Schedule may still reflect removed/renamed scope and package sequence.
- **Specific expected revisions:** Review scope labels, package milestones, and dependencies for depropanizer removal, NGL current scope, and IA/stabilizer consolidation.
- **Evidence used:** The regulatory PDF is the 4-25 project schedule; D4-SCA001 through D4-SCA006 alter package and sequencing assumptions.
- **Review caveats:** Administrative schedule revision may be sufficient.

### 11. `100118719_FAC_2 25-80-15W6 (4-25 Doe)_PE Report.pdf`
- **Why this document is impacted:** It supports the engineered facility application and may contain superseded design basis.
- **Specific expected revisions:** Review against all major 4-25 SCA changes before re-use.
- **Evidence used:** The regulatory PDF is the 4-25 facility PE report; D4-SCA001 through D4-SCA006 alter the technical scope basis it supports.
- **Review caveats:** Engineer-of-record should determine re-seal/re-issue requirements.

### 12. `BFD-235633-100_200_5100 (4-25 Doe)_Block Flow Diagram_rC.pdf`
- **Why this document is impacted:** Block flow changed materially.
- **Specific expected revisions:** Remove depropanizer/LPG blocks, show current NGL treating/storage/loading, stabilizer/SOC, heat medium, IA, mole sieve/TEG, and incinerator interfaces.
- **Evidence used:** The regulatory PDF is the 4-25 block flow diagram; D4-SCA001 through D4-SCA006 alter represented process blocks and interfaces.
- **Review caveats:** Confirm current balances before issuing.

### 13. `CIV-235633-5001 (4-25 Doe)_Plot Plan_rK.pdf`
- **Why this document is impacted:** Current equipment layout changed or requires confirmation after multiple SCAs, and this plot-plan sheet is part of the physical layout control set.
- **Specific expected revisions:** Remove or flag depropanizer/LPG future equipment if still shown, show current NGL/stabilizer/SOC/IA/heat-medium package locations, and clarify the shared incinerator relationship to the 3-25 location.
- **Evidence used:** The regulatory PDF is a plot-plan sheet; D4-SCA001 through D4-SCA006 alter equipment roster, utility, and incinerator layout assumptions. Text extraction was sparse, so drawing-role inference is used.
- **Review caveats:** CAD source review is required before deciding whether sheet 5001 needs graphical revision or only supersession notation.

### 14. `CIV-235633-5002 (4-25 Doe)_Plot Plan_rK.pdf`
- **Why this document is impacted:** Current equipment layout changed or requires confirmation after multiple SCAs, and this plot-plan sheet includes extracted stale process and utility terms.
- **Specific expected revisions:** Remove or flag depropanizer/LPG future equipment if still shown, show current NGL/stabilizer/SOC/IA/heat-medium package locations, and clarify the shared incinerator relationship to the 3-25 location.
- **Evidence used:** PDF text extraction found stabilizer, SOC, heat medium, incinerator, IA, LPG, depropanizer, and mole sieve terms; D4-SCA001 through D4-SCA006 modify those bases.
- **Review caveats:** CAD source review is required before issuing a revised sheet; coordinate sheet 5002 with sheet 5001.

### 15. `MFS-235633 (4-25 Doe)_P&ID_rA.pdf`
- **Why this document is impacted:** P&IDs carry all detailed process/utility/relief/control changes.
- **Specific expected revisions:** Revise all affected sheets for NGL, no depropanizer, non-regenerative caustic, stabilizer/SOC, inlet HEX, heat medium, TEG/mole sieve, IA, incinerator and electrical changes.
- **Evidence used:** The regulatory PDF is the 4-25 P&ID package; D4-SCA001 through D4-SCA006 alter systems shown on P&IDs.
- **Review caveats:** Requires discipline drawing-by-drawing review.

### 16. `MSS-235633-1001 (4-25 Doe)_Metering Schematic_rB.pdf`
- **Why this document is impacted:** Product nomenclature and product transfer bases changed.
- **Specific expected revisions:** Confirm all LPG/C3-C4/depropanizer metering labels are replaced or retired and NGL basis is current.
- **Evidence used:** The regulatory PDF is the 4-25 metering schematic; D4-SCA001 and D4-SCA003 alter product terminology and transfer/metering basis.
- **Review caveats:** May be no-change if it only covers unaffected utility/gas metering.

### 17. `PFD-235633 (4-25 Doe)_Process Flow Diagram_rB.pdf`
- **Why this document is impacted:** Flow paths and equipment bases changed throughout the process.
- **Specific expected revisions:** Update all process flows for NGL, removed depropanizer, non-regenerative caustic, stabilizer/SOC, inlet HEX, heat medium, TEG/mole sieve, IA, and incinerator basis.
- **Evidence used:** The regulatory PDF is the 4-25 process flow diagram package; D4-SCA001 through D4-SCA006 alter represented process flows and utility interfaces.
- **Review caveats:** Coordinate with revised winter/summer HMBs.

### 18. `Surface Water Management Plan_rB.pdf`
- **Why this document is impacted:** Layout and containment assumptions may change.
- **Specific expected revisions:** Review drainage/containment around NGL, heat-medium, IA, stabilizer/SOC and removed depropanizer/LPG areas.
- **Evidence used:** PDF text hits LPG/NGL/heat medium/mole sieve; D4-SCA001 and D4-SCA002 alter layout and drainage-relevant equipment bases.
- **Review caveats:** Requires revised plot plan.

### 19. `Light Assessment_rC.pdf`
- **Why this document is impacted:** Lighting inventory and narrative may include changed/removed equipment.
- **Specific expected revisions:** Update lighting sources and project narrative for current 4-25 package layout.
- **Evidence used:** PDF text hits LPG/NGL/heat medium/mole sieve; D4-SCA001 and D4-SCA006 alter package layout and lighting-source assumptions.
- **Review caveats:** If fixtures unchanged, narrative-only update may be sufficient.

### 20. `Ground Permissive at Truck-Out_rB.pdf`
- **Why this document is impacted:** Product loading/truck-out terminology may be stale after NGL/LPG changes.
- **Specific expected revisions:** Review product labels, truck-out interlocks, and grounding philosophy against current NGL loading scope.
- **Evidence used:** PDF text hits LPG/NGL/truck-out; D4-SCA001 and D4-SCA003 alter product terminology and transfer/loading basis.
- **Review caveats:** May remain unchanged if grounding hardware is product-agnostic.

### 21. `W235633-PRC-DBM-000001-001 (4-25 Doe)_Design Basis Memorandum_rA.pdf`
- **Why this document is impacted:** It contains all major superseded 4-25 basis items.
- **Specific expected revisions:** Rewrite DBM sections for NGL scope, depropanizer removal, non-regenerative treating, stabilization/SOC, heat medium, inlet HEX, TEG/mole sieve, IA, incinerator, electrical, and package roster.
- **Evidence used:** PDF text hits every major changed term; SCA report is DBM amendment basis.
- **Review caveats:** Should precede dependent regulatory report revisions.

### 22. `W235633-PRC-HMB-000001-001 (4-25 Doe)_HMB Winter_rC.pdf`
- **Why this document is impacted:** The winter material balance changes with depropanizer removal, NGL treating, heat medium, IA, and stabilizer/SOC decisions.
- **Specific expected revisions:** Recalculate the winter case for the current process configuration, NGL product basis, DSO/spent-caustic waste basis, stabilizer/SOC loads, inlet HEX relationship, heat-medium loads, and incinerator/flare feed basis.
- **Evidence used:** The winter HMB regulatory PDF text hits LPG, SOC, incinerator, VRU, TEG, and spent caustic; D4-SCA001 through D4-SCA006 alter those process bases.
- **Review caveats:** Winter operating assumptions should be checked separately from summer assumptions before dependent emissions and flare calculations are revised.

### 23. `W235633-PRC-HMB-000002-001 (4-25 Doe)_HMB Summer_rC.pdf`
- **Why this document is impacted:** The summer material balance changes with depropanizer removal, NGL treating, heat medium, IA, and stabilizer/SOC decisions.
- **Specific expected revisions:** Recalculate the summer case for the current process configuration, NGL product basis, DSO/spent-caustic waste basis, stabilizer/SOC loads, inlet HEX relationship, heat-medium loads, and incinerator/flare feed basis.
- **Evidence used:** The summer HMB regulatory PDF text hits LPG, SOC, incinerator, VRU, TEG, and spent caustic; D4-SCA001 through D4-SCA006 alter those process bases.
- **Review caveats:** Summer operating assumptions should be checked separately from winter assumptions before dependent emissions and flare calculations are revised.

### 24. `Emissions Summary_rB.pdf`
- **Why this document is impacted:** Emission sources and rates changed materially.
- **Specific expected revisions:** Recalculate source inventory for current NGL, no depropanizer, non-regenerative caustic, heat medium, IA, incinerator, flare and stabilizer/SOC basis.
- **Evidence used:** PDF text hits changed emissions sources; D4-SCA001 through D4-SCA006 alter equipment, utility, incinerator, flare, and emissions bases.
- **Review caveats:** Must follow revised HMB, flare data, and equipment list.

### 25. `Non-Flare Connected PSV Summary_rA.pdf`
- **Why this document is impacted:** Relief basis may include retired or renamed systems.
- **Specific expected revisions:** Remove retired depropanizer/LPG entries, update NGL/stabilizer/SOC/heat-medium/IA PSV basis, and confirm flare/non-flare destinations.
- **Evidence used:** PDF text hits depropanizer/LPG/NGL/IA/heat medium; D4-SCA001 through D4-SCA006 alter PSV and relief-source bases.
- **Review caveats:** Requires revised P&IDs and relief register.

### 26. `Inlet Separator Summary.pdf`
- **Why this document is impacted:** Inlet separator basis and HEX subject changed.
- **Specific expected revisions:** Update installed count/sizing, future third plot, liquid outlet heater, and downstream MPFF/stabilizer interface.
- **Evidence used:** The regulatory PDF is the 4-25 inlet separator summary; D4-SCA001 changes the separator basis and D4-SCA005 registers the inlet-separator HEX subject.
- **Review caveats:** Confirm final heat source for HEX.

### 27. `Prime Mover List_rC.pdf`
- **Why this document is impacted:** Driver/motor lists change with VFD, IA, heat medium and process-scope changes.
- **Specific expected revisions:** Update motors/drivers for current stabilizer/SOC, heat medium, TEG/mole sieve, instrument air, VFD, capacitor-bank removal and standby power basis; remove depropanizer/LPG items.
- **Evidence used:** PDF text hits LPG/NGL/stabilizer/heat medium/VFD/mole sieve; D4-SCA001 and D4-SCA006 alter prime-mover, drive, and electrical assumptions.
- **Review caveats:** Final electrical studies may change ratings.

### 28. `Plant Shutdown & Blowdown Philosophy_rB.pdf`
- **Why this document is impacted:** Shutdown/blowdown basis depends on current equipment, relief and utility configuration.
- **Specific expected revisions:** Update shutdown/blowdown paths and logic for NGL, no depropanizer, heat medium, IA, incinerator, and stabilizer/SOC scope.
- **Evidence used:** PDF text hits depropanizer/LPG/NGL/heat medium/incinerator/IA; D4-SCA001 through D4-SCA006 alter shutdown, blowdown, relief, utility, and interface assumptions.
- **Review caveats:** Coordinate with revised P&IDs and flare data.

### 29. `Flare Stack Data Submission_rA.pdf`
- **Why this document is impacted:** Relief and incinerator loads changed.
- **Specific expected revisions:** Remove caustic-regeneration/depropanizer relief bases, update incinerator feed and location, and recalculate flare load cases.
- **Evidence used:** SCA-002 Supersession_Delta and PDF text hits caustic regeneration/incinerator/LPG/depropanizer.
- **Review caveats:** Requires process/relief engineer signoff.

### 30. `DEOS_rB.pdf`
- **Why this document is impacted:** It may contain dehydration or incinerator assumptions affected by SCAs.
- **Specific expected revisions:** Confirm retained dehydration scope and remove obsolete LPG/depropanizer or caustic-regeneration/incinerator statements if present.
- **Evidence used:** PDF text hits dehy/SOC/incinerator/flare/VRU/TEG.
- **Review caveats:** May be no-change if strictly limited to retained equipment.

### 31. `Safety & Loss Management_rA.pdf`
- **Why this document is impacted:** Safety responsibilities and safeguards may change with shared and retired systems.
- **Specific expected revisions:** Review safety narrative, safeguards, shared incinerator operation, IA failure modes, heat medium changes, and current NGL hazards.
- **Evidence used:** PDF text hits LPG/NGL/stabilization/SOC/heat medium/flare/mole sieve; D4-SCA001 through D4-SCA006 alter safety-relevant process and utility bases.
- **Review caveats:** Should follow updated HAZID.

### 32. `HAZMAT List_rC.pdf`
- **Why this document is impacted:** Hazardous materials inventory is directly affected by NGL, non-regenerative caustic, heat medium, TEG/mole sieve and IA changes.
- **Specific expected revisions:** Replace LPG/depropanizer-specific entries, update NGL/DSO/spent-caustic, heat-medium, TEG, mole sieve and IA consumables.
- **Evidence used:** PDF text hits LPG/NGL/heat medium/IA/TEG/mole sieve/spent caustic; D4-SCA001 through D4-SCA006 alter the material inventory basis.
- **Review caveats:** Final quantities require updated HMB and tank lists.

### 33. `QAP & Validation Report_rA.pdf`
- **Why this document is impacted:** Package/decomposition structure changed through SCA-004/SCA-005.
- **Specific expected revisions:** Check validation references, package roster, and remediation status.
- **Evidence used:** The regulatory PDF is the 4-25 QAP and validation report; D4-SCA004 and D4-SCA005 change package roster and remediation validation context.
- **Review caveats:** Likely administrative unless report embeds technical package lists.

### 34. `Secondary Containment Plan_rB.pdf`
- **Why this document is impacted:** Containment assumptions change with product, tank and chemical scope.
- **Specific expected revisions:** Update containment around current NGL/DSO/spent caustic, heat medium, tanks, removed depropanizer/LPG, and shared incinerator interface.
- **Evidence used:** PDF text hits depropanizer/LPG/NGL/heat medium/incinerator/spent caustic; D4-SCA001 through D4-SCA006 alter containment-relevant equipment and material bases.
- **Review caveats:** Requires revised plot and HAZMAT list.

### 35. `Adopted Codes & Standards_rB.pdf`
- **Why this document is impacted:** Equipment-specific standards may need current package alignment.
- **Specific expected revisions:** Review standards for retired depropanizer/LPG systems and current NGL, heat medium, mole sieve, IA, incinerator and electrical packages.
- **Evidence used:** PDF text includes stale scope terms; D4-SCA001 through D4-SCA006 and the package roster changes alter the standards-review basis.
- **Review caveats:** May be no-change if standards are generic.

### 36. `Facility Security & Fire Protection_rC.pdf`
- **Why this document is impacted:** Layout, hazardous inventory and shared asset responsibility changed.
- **Specific expected revisions:** Review fire/security coverage for NGL/tanks, heat medium, IA, incinerator, removed depropanizer, and changed package layout.
- **Evidence used:** PDF text hits LPG/NGL/heat medium/flare/mole sieve; D4-SCA001 through D4-SCA006 alter hazardous inventory, fire-protection, and layout assumptions.
- **Review caveats:** Requires updated HAZMAT, plot and consequence basis.

### 37. `HAZID Study Report_r0.pdf`
- **Why this document is impacted:** HAZID scope and scenarios changed materially.
- **Specific expected revisions:** Reconcile nodes, scenarios, recommendations, document references and risk rankings with all SCA decisions.
- **Evidence used:** PDF text hits all major changed terms.
- **Review caveats:** Requires formal HAZID addendum or revalidation workshop.

### 38. `Prelim Consequence Assessment_rA.pdf`
- **Why this document is impacted:** Consequence scenarios depend on current equipment, inventory, relief and incinerator basis.
- **Specific expected revisions:** Re-run scenario basis for NGL, no depropanizer, current heat medium/IA, shared incinerator and changed relief/blowdown.
- **Evidence used:** PDF text hits LPG/NGL/heat medium/mole sieve/stabilization; D4-SCA001 through D4-SCA006 alter consequence-relevant process, utility, and relief bases.
- **Review caveats:** Should follow revised HAZID and flare data.

### 39. `Design Change Summary_rB.pdf`
- **Why this document is impacted:** The submitted design change summary predates the full SCA chain.
- **Specific expected revisions:** Replace with or append a consolidated SCA-001 through SCA-006 change summary covering product, process, instrument air serving both facilities, incinerator, standby/VFD/capacitor electrical changes, and package-structure changes.
- **Evidence used:** PDF text hits depropanizer/LPG/NGL/heat medium/incinerator/LACT/mole sieve.
- **Review caveats:** This may become the control document for the regulatory amendment package; use clear revision traceability.

---

## Evidence Limits and Open Review Items

- PDF text extraction was sufficient for most narrative reports, but drawing PDFs should be checked visually against CAD/source drawings before final revision instructions are issued.
- Several package deliverables identify missing source slices, especially vendor RFQ/DOCX references. This report uses the package context as derivative planning evidence, not as authoritative vendor-source truth.
- SCA evidence establishes scope decisions but does not supply all recalculated values. HMB, emissions, flare, noise, PSV, consequence and shutdown/blowdown documents require discipline recalculation.
- Incinerator operational responsibility remains an open coordination item on the 4-25 side and should be resolved before final flare/incinerator regulatory submissions.
- TEG contactor sparing and NGL regeneration gas/source details remain open or conflict-marked in 4-25 SCA-005 evidence and related package deliverables; regulatory reports should preserve those as review items until ruled.
- The no-change classifications apply only to the SCA-driven scope review performed here. They do not certify currency, signature status, regulatory sufficiency, or document-control validity.
