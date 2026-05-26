# Procedure — DEL-055-02 Package Datasheet (PKG-055 LP Flare KO Drum 4-25)

## Purpose

Operational steps to **produce** the EPC Integrator Package Datasheet for PKG-055 (LP Flare KO Drum, 4-25), suitable as a vendor engineering handoff. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-055-02.

## Prerequisites

### Inputs required (FACT)

- `_CONTEXT.md` deliverable identity and scope.
- `_REFERENCES.md` reference list (decomposition snapshot and source basis).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — accessible primary technical basis for the 04-25 LP flare system.
- Gate 7 PROJECT_DECOMP snapshot registers: `PACKAGE_REGISTER.csv` row 57, `DELIVERABLE_REGISTER.csv` row DEL-055-02, `OBJECTIVE_DELIVERABLE_MAP.csv` (8 explicit objectives).
- DEL-055-01 EPC Scope of Work (sibling deliverable) — provides the package scope and tagged equipment baseline.

### Inputs deferred (TBD)

- `26020-Package_Requirements.docx` package heading 10 — binary, not locally extracted (location TBD).
- `26020-Packages_Interfaces_4_export.xlsx` Packages row 57 — binary, not locally extracted (location TBD).
- Aspen Flare System Analyzer detailed-design output — TBD at DBM stage.
- Governing OGPFR regulatory text — not in package.

### Declared dependencies

- Upstream: none declared during PREPARATION (`_DEPENDENCIES.md`). Functionally, DEL-055-01 (EPC SOW) is the upstream anchor by package convention; record as ASSUMPTION until human-confirmed.
- Downstream: none declared during PREPARATION. Functionally, DEL-055-04 (Vendor Engineered Equipment Package) is the principal downstream consumer; ASSUMPTION pending confirmation.

## Steps

### Step 1 — Establish identity block

Populate the Datasheet "Identification" section from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row 57 (vendor package number 26020-01-17-003).

### Step 2 — Populate equipment list

Extract V-3900-1 and P-3900-1 entries from the DBM equipment-list table. Confirm quantities (1 each) and tag formats against the equipment-detail table in the DBM.

### Step 3 — Define process service

Write the package function from the DBM "Low-pressure flare" row: liquid knock-out for the LP flare relief header, ahead of the LP flare element on the common HP/cryo stack. List the LP source connections enumerated in the DBM narrative (amine regen, TEG flash, VRU, seal-pot, mole-sieve regen, pressurized caustic drain).

### Step 4 — Capture header/stack data

Transcribe directly from the DBM "Low-pressure flare," "Flare Header Materials," and "LP stack" rows: header size 508 mm (20 in); material SA-106; listed 324 mm; lengths 270 m / 50 m; piggy-back element on common stack; air-assist blower; Ringelmann criterion. Mark LP element OD as TBD.

### Step 5 — Record relief case and backpressure status

Note that relief volumes, actual backpressures, LP stack element OD, opacity scenarios, air-assist basis, and shared 03-25/04-25 allocation are TBD pending detailed-design Aspen Flare System Analyzer output. Cite the DBM flare-system summary row.

### Step 6 — Record pilot, purge, and fuel-gas requirements

Cite DBM "LP Flare Pilot" and "LP Flare Header Purge" estimate tables as source-level estimates; mark site-specific pilot/purge values TBC. State R7 supplemental fuel gas LHV ≥ 20 MJ/Sm³ requirement.

### Step 7 — Apply spacing and radiation criteria

Populate spacing distances from the DBM spacing table (10 m KO drum / vegetation, OGAOM 9.6.15) and stack-radiation flux values (9 / 5 kW/m², OGPFR), flagging OGPFR values as PROPOSAL pending regulatory verification (Conflict C-02 in `Guidance.md`).

### Step 8 — Build interface requirements matrix

Create one row for each of the ten interface types in `PACKAGE_REGISTER.csv` row 57: Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports. Use TBD entries where source coverage is incomplete (in particular EHT/freeze-protection on LP headers — Conflict C-01).

### Step 9 — Capture construction scope

Identify the equipment as the `390-1 LP Flare KO Drum Module` (shop-built). Record the Package Vendor / EPC Integrator responsibility split from `PACKAGE_REGISTER.csv` row 57.

### Step 10 — Surface vessel/pump mechanical detail

For each mechanical-detail field not closed at DBM (internal coating, MAWP/MDMT, corrosion allowance, demister/internals, nozzle schedule, pump hydraulic data), enter `TBD — pending 26020-Package_Requirements.docx heading 10 extraction and EPC SOW (DEL-055-01)`.

### Step 11 — Enumerate references

Populate the References section with: the DBM Deepcut path, the binary Word and Excel sources (location TBD), the budgetary HP PDF (commercial go-by only, not LP design authority — Conflict C-03), and the Gate 7 snapshot registers.

### Step 12 — Surface conflicts and TBDs

Carry forward the Conflict Table from `Guidance.md` and the enumerated TBDs into a closing "Open Items" section on the datasheet. Each TBD must carry a source pointer or an explicit `location TBD`.

## Verification

| Check | Pass criterion |
|---|---|
| Equipment identity matches DBM | V-3900-1 and P-3900-1 present with correct facility tag |
| Header data matches DBM | SA-106, 508 mm (20 in), 270 m / 50 m, 324 mm listed |
| All ten interface types present | Each row exists, even if TBD |
| Spacing values cite OGAOM/OGPFR with verification flag | OGPFR caveat note carried |
| Open items each cite source or `location TBD` | No bare TBDs without provenance |
| References match `_REFERENCES.md` | Paths and section refs consistent |
| No requirement value invented from decomposition prose | All non-trivial values trace to DBM or marked TBD |
| Package-vendor / EPC-integrator split correctly stated | Matches `PACKAGE_REGISTER.csv` row 57 |

## Records

The completed Package Datasheet supersedes draft revisions and becomes:

- the vendor handoff basis for DEL-055-04 (Vendor Engineered Equipment Package),
- the package interface evidence carrier for PKG-055 (per `_CONTEXT.md` Notes),
- an input to DEL-055-06 (EPC Vendor Package Review and Acceptance) checks, and
- a record retained against `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (explicit mapping in `OBJECTIVE_DELIVERABLE_MAP.csv`).

A revision log shall be maintained on the datasheet recording each TBD closure as binary sources are extracted and detailed-engineering analyses are issued.
