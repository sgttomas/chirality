# Specification — DEL-053-03 Construction Work Package (Flare KO Drum, Cryo)

## Scope

This Specification defines the normative content and acceptance basis for the Construction Work Package (CWP) for `PKG-053 Flare KO Drum (Cryo)` at the 04-25 Deepcut facility.

**In scope:** physical installation, tie-in, inspection, pre-commissioning, mechanical completion, and turnover-readiness documentation for vessel `V-4110-1` (Cryo Flare K.O. Drum), heater `H-4112-1` (Cryo Flare K.O. Drum Immersion Heater), and shop module `410-1 HP / Cryo Flare KO Drum Module`.

**Out of scope:** vendor engineering and fabrication of the equipment package (carried by `DEL-053-04 Vendor Engineered Equipment Package`); scope of work narrative (`DEL-053-01`); package datasheet (`DEL-053-02`); vendor document turnover (`DEL-053-05`); EPC review and acceptance (`DEL-053-06`); design of the common HP/cryo flare stack (a shared 03-25/04-25 system).

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-09 Flare; `_CONTEXT.md`; deliverable register row `DEL-053-03_construction-work-package`.

## Requirements

### R1 — Installation Workface Plan (REQUIRED)

The CWP SHALL include an installation workface plan describing setting, levelling, grouting, and anchoring of module `410-1` and installation of `V-4110-1` and `H-4112-1`. Lift studies SHALL be included for components exceeding mobile-crane capacity at the planned location. ASSUMPTION: governing lift-study threshold is `TBD` pending construction execution contractor selection.

### R2 — Tie-In Register (REQUIRED)

The CWP SHALL include a complete tie-in register for the package. At minimum:

- Cryogenic relief header inlet: 610 mm (24 in), 304SS — Source: DBM-Deepcut §Flare Header and Backpressure Basis.
- Combined HP/cryo outlet header: 762 mm (30 in), 304SS — Source: DBM-Deepcut §Flare Header and Backpressure Basis.
- Immersion-heater electrical supply, control wiring, and instrument-air, vent, and drain interfaces — exact list `location TBD` pending IFC P&IDs.

### R3 — Welding, NDE, and Pressure-Test Plan (REQUIRED)

Welding procedures, NDE coverage, and pressure-test acceptance criteria SHALL be specified for vessel and piping. Governing code clauses are **location TBD** — accessible source slices do not enumerate the piping/vessel code for this package. PROPOSAL: ASME B31.3 for piping and ASME BPVC Sec VIII Div 1 for vessel, pending human ruling.

### R4 — Inspection and Test Plan (REQUIRED)

The CWP SHALL include an ITP covering: vessel receipt inspection (dimensional, nameplate, MTR review), NDE record review, vessel and piping hydrostatic / pneumatic test, immersion-heater electrical commissioning (continuity, insulation resistance, control-loop function), instrument-loop checkout, and PSV installation verification.

### R5 — Pre-Commissioning (REQUIRED)

The CWP SHALL define pre-commissioning steps including cleaning and drying for cryogenic service. Cryogenic relief headers are NOT heat traced because water is not expected in this system (DBM-Deepcut §SEC-09 Flare). The CWP SHALL specify dryness acceptance criteria (specific dewpoint and method `location TBD`).

### R6 — Construction Interface Management (REQUIRED)

The CWP SHALL identify and manage construction interfaces with:

- `PKG-054 Flare KO Drum (HP)` — `V-4100-1`, `P-4100-1`. Module `410-1 HP / Cryo Flare KO Drum Module` is co-mounted (Source: DBM-Deepcut §Modularization). ASSUMPTION: package split mounts both KO drum sets on a single shop module; coordination of build and turnover with `DEL-054-03` is required.
- Common HP/cryo flare stack physically at 03-25 (Source: DBM-Deepcut §SEC-09). Tie-in scope across facility boundary requires interface agreement; ownership and split `location TBD`.
- Civil/structural, electrical heat-trace exclusion zone (cryogenic header SHALL NOT be heat traced), and instrument-air supply.

### R7 — Site Spacing Compliance (REQUIRED)

Equipment placement SHALL comply with site-spacing criteria (DBM-Deepcut §SEC-04 Flare and Incinerator Spacing, OGAOM 9.6.15):

- Distance from flare tanks / KO drums to vegetation or other fire hazards: ≥10 m (32 ft).
- Distance from flare to public road or property line: ≥80 m (262.5 ft).
- Distance from flare to atmospheric condensate tanks: ≥50 m (164 ft).

Verification SHALL be by walk-down against IFC plot plan with civil dimensions captured in the turnover dossier.

### R8 — Turnover Documentation (REQUIRED)

The CWP SHALL deliver a turnover dossier supporting Mechanical Completion (MC), Ready-for-Commissioning (RFC), and Ready-for-Start-Up (RFSU) gates with traceable punchlist closeout to feed `DEL-053-06 EPC Vendor Package Review and Acceptance`.

### R9 — Foundation and Anchorage (REQUIRED)

Foundations SHALL be designed and verified for final geotechnical report values, equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access (DBM-Deepcut §SEC-04 Foundations). Tall vessels and flare-system elements require equipment-specific anchorage checks; certified foundation drawings and anchor-bolt pull-test records SHALL be in the turnover dossier.

## Standards

| Standard / Reference | Scope of Applicability | Status |
|---|---|---|
| OGAOM Sec. 9.6.15 | Flare/KO drum spacing to vegetation, roads, tanks | Cited in DBM-Deepcut §SEC-04 |
| BCER Oil and Gas Processing Facility Regulation, Appendix 1, Schedule 1, Sec. 2 / Sec. 7(4) | Flare radiation limits at grade and inside/outside boundary | Cited in DBM-Deepcut §SEC-09; not directly applicable to KO drum CWP except where adjacent equipment placement is governed |
| ASME B31.3 — Process Piping | Pressure piping construction and acceptance | PROPOSAL (location TBD — not in accessible source slice) |
| ASME BPVC Sec VIII Div 1 — Pressure Vessels | Vessel construction and acceptance | PROPOSAL (location TBD — not in accessible source slice) |
| `26020-Package_Requirements.docx` — heading 8 | EPC package requirements specific to PKG-053 | location TBD — binary source not read in this run |

## Verification

| Req | Verification Method | Verification Evidence (Records) |
|---|---|---|
| R1 | Workface plan review; field walk-down at installation | Approved workface plan; daily field reports |
| R2 | Tie-in register cross-check against IFC P&IDs | Tie-in punch closeout register |
| R3 | NDE records review; pressure-test certification | NDE log, hydrotest certificate |
| R4 | ITP sign-off | Signed ITP entries; vendor inspection reports |
| R5 | Dryness measurement; cleanliness sign-off | Dewpoint record; cleanliness certificate |
| R6 | Interface walk-down with PKG-054 and 03-25 stack interface owner | Interface register sign-off |
| R7 | Plot-plan walk-down vs IFC | Dimensional verification record |
| R8 | MC / RFC / RFSU gate review | Turnover dossier; punchlist closeout log |
| R9 | Foundation as-built and anchor-bolt pull tests | Foundation as-built; pull-test records |

## Documentation

The Construction Work Package SHALL deliver:

- Installation workface plan and lift plans
- Tie-in register and tie-in punchlist
- Welding procedure register and NDE plan and records
- Inspection and Test Plan (ITP) with signed entries
- Pre-commissioning procedures and cleanliness/dryness records
- Construction interface register (with PKG-054 and 03-25 stack)
- Foundation as-built and anchor pull-test records
- Mechanical Completion / RFC / RFSU turnover dossier (the anticipated artifacts named in `_CONTEXT.md`: construction work package; installation and tie-in workface plan; construction interface and turnover checklist)
