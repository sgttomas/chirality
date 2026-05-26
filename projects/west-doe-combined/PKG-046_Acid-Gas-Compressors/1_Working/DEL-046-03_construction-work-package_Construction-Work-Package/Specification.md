# Specification: DEL-046-03 — Construction Work Package (Acid Gas Compressors)

## Scope

This Specification governs the EPC Integrator's Construction Work Package for `PKG-046` Acid Gas Compressors at the 04-25 West Doe Deepcut Gas Plant. It defines the physical installation, mechanical hookup, inspection, turnover, and tie-in requirements for the two-operating-plus-one-spare acid gas injection compressor packages and associated suction scrubbers, aftercoolers, recycle and blowdown valves, packing-vent recovery interfaces, and acid-gas injection-pipeline tie-in point.

**In scope:** site receipt, off-loading, setting, mechanical/electrical/instrument hookup, ISBL piping to defined tie-in points, pre-commissioning checks, mechanical completion documentation, and EPC-to-Tourmaline turnover.

**Out of scope:** acid gas disposal well and reservoir; pipeline design and installation downstream of the facility tie-in (by others); 02-25 acid gas injection modifications (TBC, separate scope); vendor-engineered compressor package internal design (covered by `DEL-046-04`).

This deliverable covers `SOW-0047`, `SOW-0048`, `SOW-0049`, `SOW-0050` (per `_CONTEXT.md`).

## Requirements

### R-1 Field construction responsibility
Field construction of `PKG-046` shall be executed under Tourmaline field-construction scope per `4-25_Deepcut_DBM.md` SEC-01, including grading/piling/foundation work, module receipt and setting, mechanical hookup, shipped-loose installation, home-run cabling, electrical terminations, area lighting, and security/fencing within the PKG-046 footprint. Source: `4-25_Deepcut_DBM.md` SEC-01 Construction Responsibility.

### R-2 Module setting and mechanical hookup
The acid gas compressor packages shall be received as vendor-supplied modules (`DEL-046-04`), set on prepared foundations, and mechanically connected to ISBL process headers (acid gas suction header, acid gas injection discharge), aftercooler air supply, electrical feeders, control wiring, lube-oil systems, and packing-drain/vent header to the VRU suction (per `4-25_Deepcut_DBM.md` SEC-05). Module split count and shipped-loose component count: TBD (ASSUMPTION pending vendor packaging definition).

### R-3 Interconnecting piping
Interconnecting piping shall be installed to all ISBL/OSBL tie-in points defined in the package P&IDs and interface register. Responsibility for piping at each ISBL/OSBL tie-in shall be confirmed per tie-in; the default external-interface marker applies. Source: `4-25_Deepcut_DBM.md` SEC-01.

### R-4 Acid-gas service materials and venting
All sour-service materials, gasketing, and bolting shall conform to vendor specification and sour-service code requirements (NACE MR0175 / ISO 15156: **ASSUMPTION — standard practice for H2S service**; specific governing standard TBD). Packing drains and vents shall be routed to the common seal pot, with seal-pot vapour routed to the VRU suction header and liquids removed by local truck-out. Source: `4-25_Deepcut_DBM.md` SEC-05.

### R-5 Coolers and louver controls
Each compressor stage aftercooler shall be installed with actuated louver temperature control, automatic warm-air recirculation on low discharge temperature, and heat-medium freeze-prevention service. Source: `4-25_Deepcut_DBM.md` SEC-05.

### R-6 Recycle, blowdown, and isolation
The single fail-open blowdown valve downstream of the final aftercooler, the high-pressure and low-pressure recycle valves (fail open), and the documented exclusion of manual isolation on recycle valves (to minimize acid gas leakage points) shall be installed per the vendor mechanical drawings and the design basis. Source: `4-25_Deepcut_DBM.md` SEC-05.

### R-7 Acid-gas injection pipeline tie-in
The construction work package shall terminate the EPC scope at the facility tie-in to the acid gas injection pipeline. Pipeline assumed 3 in. NPS (TBC); design and installation downstream of the tie-in are excluded from this work package. Source: `4-25_Deepcut_DBM.md` SEC-05 Acid Gas Disposal Well Interface.

### R-8 Tie-in planning and timing
Joint planning shall be conducted with Tourmaline and adjacent EPC packages for all tie-ins to existing or related facilities. Tie-in timing shall be coordinated with plant construction phasing. Source: `4-25_Deepcut_DBM.md` SEC-01.

### R-9 Pre-commissioning and mechanical completion
Pre-commissioning and mechanical completion shall include: hydrostatic / pneumatic testing per applicable code (test method and code TBD), instrument loop checks, motor solo-run and rotation verification, lube-oil flush, packing-vent integrity test, blowdown sequence verification, ESD function test, and electrical megger / continuity. Specific code/test parameters: TBD.

### R-10 Turnover package
EPC shall deliver a Construction Turnover Package to Tourmaline containing as-built redlines, ITR (Inspection and Test Records), punchlist with disposition, hydrotest certificates, cable schedules, loop check records, motor records, calibration records, and the construction interface and turnover checklist (per anticipated artifacts in `_CONTEXT.md`).

## Standards

| Standard | Applicability | Status |
|---|---|---|
| British Columbia Energy Regulator (BCER) permits — site alteration permit (Section 12.4) and waste discharge permit | Construction execution must be consistent with permit conditions | Permit amendment basis stated in `4-25_Deepcut_DBM.md` SEC-01 Permitting; detailed obligations TBD |
| NACE MR0175 / ISO 15156 — sour service material qualification | Materials for H2S-bearing acid gas service | **ASSUMPTION** (industry-standard for sour service); not explicitly named in accessible sources |
| ASME B31.3 — Process Piping | ISBL interconnecting piping installation, hydrotest, weld inspection | **ASSUMPTION**; not explicitly named in accessible sources |
| API STD 618 — Reciprocating Compressors for Petroleum, Chemical, and Gas Industry Services | Compressor package design basis (vendor); construction-side relevance is alignment/grouting/foundation tolerances | **ASSUMPTION**; not explicitly named in accessible sources |
| `26020-Package_Requirements.docx` — package heading 1 | Project-defined package construction requirements | location TBD (binary not text-extracted in scope of this drafting pass) |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 | Construction QA records; assignment matrix from `4-25_Deepcut_DBM.md` SEC-01 reconciled in the Construction Interface Checklist |
| R-2 | Module setting survey reports; mechanical hookup ITRs; punchlist closeout |
| R-3 | Piping isometric walkdowns vs. P&ID; ISBL/OSBL responsibility matrix sign-off |
| R-4 | Material test reports (MTRs) reconciled to sour-service spec (when finalized); packing-vent integrity test record |
| R-5 | Cooler bundle functional test; louver actuation test; heat-medium loop commissioning record |
| R-6 | Blowdown function test record; recycle valve fail-position bench test; cause-and-effect verification |
| R-7 | Tie-in walkdown; pipeline interface acceptance signature from downstream operator |
| R-8 | Tie-in plan document with timing concurred by Tourmaline |
| R-9 | Pre-commissioning ITR package; hydrotest certificate; loop check records |
| R-10 | Turnover package acceptance signature; punchlist status report |

## Documentation

The Construction Work Package shall produce, at minimum (per `_CONTEXT.md` anticipated artifacts):

- Construction Work Package (this document set, plus execution plan)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- ITR (Inspection and Test Record) compilation
- As-built redline package
- Punchlist with disposition

## Conflicts and Open Items

- Compressor model: Ariel KBT/6 vs. legacy KBK/6 reference unresolved (`4-25_Deepcut_DBM.md` SEC-05) — affects vendor package receipt verification.
- 5th-stage discharge pressure: 1,200 psig normal vs. 1,500 psig design-discharge reference unresolved — affects hydrotest pressure determination.
- 2 x 100% + 1 spare vs. 3 x 50% configuration unresolved — affects foundation layout and footprint.
- Code references in R-4, Standards table, and R-9 are ASSUMPTIONS; not stated in accessible sources.
- `26020-Package_Requirements.docx` content is TBD (not text-extracted).
