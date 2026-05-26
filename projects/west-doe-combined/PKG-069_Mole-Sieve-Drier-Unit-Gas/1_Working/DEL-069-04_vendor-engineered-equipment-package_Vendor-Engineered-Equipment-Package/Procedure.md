# Procedure — DEL-069-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, Gas)

## Purpose

This procedure describes the steps to **produce** the Vendor Engineered Equipment Package deliverable (vendor engineering, design, datasheet set, fabrication/supply leading to the physical equipment package), as required by `_CONTEXT.md` Anticipated Artifacts and the Specification requirements R-1 through R-18.

## Prerequisites

- DEL-069-01 Scope of Work (EPC Integrator) issued to vendor — package scope, tagged equipment list, boundaries.  Status: TBD (not locally extracted).
- DEL-069-02 Package Datasheet (EPC Integrator) issued to vendor — process conditions, interface requirements matrix, source-supported equipment and design criteria.  Status: TBD (not locally extracted).
- 4-25 Deepcut DBM SEC-06 (Molecular-Sieve Dehydration and Mercury Removal Basis) available to vendor as design basis reference. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies in `_DEPENDENCIES.md`: none declared (context-only; not blockers).

## Steps

### Step 1 — Receive and confirm EPC inputs
1.1 Receive DEL-069-01 SoW and DEL-069-02 Package Datasheet from EPC Integrator.
1.2 Confirm receipt, log document numbers/revisions in the vendor document register (input to DEL-069-05).
1.3 Reconcile EPC-stated process conditions against 4-25 Deepcut DBM SEC-06 values; raise clarifications for any disagreement (e.g., inlet pressure 1078 psig TBC, inlet temperatures TBC).
1.4 Acknowledge open Conflict Table items C-1 through C-4 (see `Guidance.md`) and confirm resolution path with EPC Integrator.

### Step 2 — Develop vendor package design basis
2.1 Establish design inlet conditions (pressure, temperature, flow, water content) per R-4.
2.2 Establish outlet specification per R-3, including the contractually required outlet value (resolve C-3).
2.3 Establish adsorbent selection per R-1 (3A mandatory; silica gel protective layer).
2.4 Establish configuration per R-2 (3 vessels; two adsorbing, one regen/cooling; downflow).
2.5 Establish cycle table per R-5 (adsorption 54 h preliminary; regeneration 7.6 h total; min 12 h standby).
2.6 Establish regeneration set-points per R-9; document chosen heater temperature basis (resolve C-1).
2.7 Establish turndown envelope per R-15 (2:1; single-bed minimum stable flow).
2.8 Issue vendor package design basis document. Records: design basis revision, calculations file, sources cited.

### Step 3 — Develop vendor datasheet set
3.1 Adsorber vessels (3 ea), regeneration gas compressor (2x100%), regen heater (BEU), regen aerial cooler, regen scrubber, inlet filter/coalescers (2x100%), mole-sieve dust filter (1x100%), MRU vessel (1x100% + reserved space), MRU dust filter (1x100%).
3.2 Each datasheet SHALL cite SEC-06 values and identify TBC/TBD items.
3.3 Issue vendor datasheet set.

### Step 4 — Design and fabrication preparation
4.1 Vessel design (R-1, R-5, R-6, R-14: 900# flange class; 9.5 ft ID basis; bed-fill provisions; internals).
4.2 Mechanical layout: multilevel outdoor module for mole-sieve equipment; independent module/building for inlet filter/coalescers; indoor regen scrubber; preserve reserved space for future second MRU vessel.
4.3 Piping design to B31.3 (ASSUMPTION pending standards confirmation), 900# rating for mole-sieve system.
4.4 Instrumentation and control narrative: regen sequencing; BAHX 66 degC online-bed protection trip (R-7); operator-initiated HMI blowdown only with regen-compressor reverse-rotation bypass (R-11); regeneration recycle normal vs. alternate path (R-10).
4.5 MRU specification: sulphur-impregnated activated carbon; >=6 yr media life; inlet ~100 ug Hg/Nm3, outlet <= 0.01 ug Hg/Nm3 (R-12).
4.6 Dust filter specification: 1x100% each (mole-sieve and MRU), manual bypass, clean dP 2 psid (R-13).
4.7 Dry-out header tie-in per R-17 with EPC Integrator confirmation of MAWP.

### Step 5 — Vendor QA and FAT
5.1 Pressure-vessel inspection per applicable code (ASME BPVC Sec. VIII Div. 1 assumed; confirm in vendor design basis).
5.2 Regeneration-compressor FAT (performance curve, mechanical run, recycle path).
5.3 Heater and aerial-cooler shop testing.
5.4 Control-loop FAT including BAHX online-bed temperature trip and blowdown rate-limit verification.
5.5 Documentation: FAT reports issued as inputs to DEL-069-05 Vendor Document Turnover Package.

### Step 6 — Delivery and integration interface
6.1 Issue final shipping documentation, MTRs, lift plans (input to DEL-069-03 Construction Work Package and DEL-069-05).
6.2 Coordinate with EPC Integrator (DEL-069-06 review and acceptance) for site receipt and integration.

## Verification

| Step | Verification |
|---|---|
| Step 1 | EPC document register entries; clarification log closed |
| Step 2 | Design basis document accepted by EPC Integrator; Conflict Table items dispositioned (resolves C-1, C-3) |
| Step 3 | Datasheet set reviewed against SEC-06; all TBCs flagged |
| Step 4 | Vendor 3D model / GA drawing review; P&ID review; SIS / cause-and-effect review (R-7, R-11) |
| Step 5 | FAT reports signed; outlet moisture demonstration plan agreed; MRU media documentation in place |
| Step 6 | Shipping/turnover records issued to DEL-069-05; integration acceptance via DEL-069-06 |

## Records

- Vendor package design basis document (issued, revision-controlled)
- Vendor datasheet set (per equipment item)
- Vessel MTRs, code stamps, pressure-test certificates
- FAT reports (vessels, compressor, heater, cooler, scrubber, dust filters, MRU)
- Control-loop / cause-and-effect verification records
- Clarification log with EPC Integrator
- Shipping and receipt records (handed to DEL-069-03 / DEL-069-05)
- Source-traceability log identifying SEC-06 references and items carried as TBC/TBD
