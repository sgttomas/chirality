# Procedure: DEL-068-03 — Construction Work Package (TEG Dehydration Unit)

This procedure describes how the **EPC Integrator produces the CWP artifact set** (Construction Work Package, installation and tie-in workface plan, construction interface and turnover checklist) for PKG-068. Field-execution detail (rigging plans, welder qualifications, hydrotest packs) is performed under the issued CWP and is not duplicated here.

## Purpose

To produce, in a single auditable pass, a CWP artifact set for PKG-068 that:
- preserves the vendor/EPC responsibility split,
- covers every PKG-068 interface flagged YES in the Gate-07 Interface Register,
- explicitly claims all "by others" construction items from SOW-0240, and
- closes out with a signed turnover checklist traceable to DEL-068-05 and DEL-068-06.

[Source: DELIVERABLE_REGISTER.csv row 548 anticipated artifacts; PACKAGE_REGISTER.csv row 97; INTERFACE_REGISTER.csv]

## Prerequisites

### Upstream inputs
- `DEL-068-01_scope-of-work` — accepted EPC scope of work for PKG-068. [Source: SCOPE_LEDGER.csv siblings]
- `DEL-068-02_package-datasheet` — package process/mechanical parameters. [Source: SCOPE_LEDGER.csv siblings]
- `DEL-068-04_vendor-engineered-equipment-package` — vendor design and module general arrangement (for receipt envelope and tie-in points). [Source: SCOPE_LEDGER.csv siblings; ASSUMPTION: vendor GA available before CWP issue]
- Vendor document set referenced by `26020-Package_Requirements.docx` package heading 23. [Source: `_CONTEXT.md`]
- Gate-07 Interface Register, Package Register, Scope Ledger snapshots. [Source: `_REFERENCES.md`]
- 4-25 Deepcut DBM module table, common-equipment list, flare and heat-medium basis. [Source: `4-25_Deepcut_DBM.md` lines 1131–1133, 1360–1386, 2429, 2029]

### Declared upstream dependencies
None declared in `_DEPENDENCIES.md` during PREPARATION. ASSUMPTION: PKG-068 sibling deliverables DEL-068-01, DEL-068-02, DEL-068-04 are upstream content-wise; confirm via dependency-extract run.

### Tools / references
- Project piping specification (TBD — not in deliverable scope).
- Project electrical SLD and grounding/bonding standard (TBD).
- Hydrotest, NDE, and turnover procedures from project construction quality plan (TBD).

## Steps — CWP Production

### Step 1 — Confirm scope baseline
1.1. Open `_CONTEXT.md`, `PACKAGE_REGISTER.csv` row 97, `DELIVERABLE_REGISTER.csv` row 548, and SOW-0237..SOW-0240 in SCOPE_LEDGER.csv.
1.2. Confirm package identity, vendor/EPC responsibility split, included equipment list, and "by others" exclusions.
1.3. Record any deviation from those sources as a Conflict Table entry in `Guidance.md`.

### Step 2 — Enumerate interfaces and tie-ins
2.1. Extract all `YES` rows for PKG-068 from `INTERFACE_REGISTER.csv` (13 interface types listed in `Datasheet.md`).
2.2. For each interface, identify the facility-side termination and the package-side nozzle/termination from the vendor GA (DEL-068-04 deliverable). Where vendor GA is not yet available, mark `location TBD`.
2.3. Add tie-in destinations from the DBM: HP flare, LP flare, VRU, drain headers, heat medium 425 °F supply, amine absorber outlets, inlet/TEG cross-exchanger, mol-sieve dehydration. [Source: `4-25_Deepcut_DBM.md` lines 1113, 1191, 1193, 1214, 1360, 1375, 2029]

### Step 3 — Build the work-package outline
3.1. Section the CWP into: General; Receiving & Storage; Foundations & Supports; Module Setting & Alignment; Mechanical Tie-ins; Electrical & EHT; I&C; Safety Systems (F&G, ESD, relief/flare/drain); Inspection & NDE; Hydrotest; Pre-commissioning; Mechanical Completion & Turnover.
3.2. For each section, write scope, references, prerequisites, hold points, and acceptance criteria.
3.3. Cross-walk each `R-CWP-068-03-*` requirement from `Specification.md` to one or more CWP sections; ensure no requirement is unmapped.

### Step 4 — Build the installation and tie-in workface plan
4.1. Sequence workfronts using shop-vs-site distinction (Module 570 = Shop per `4-25_Deepcut_DBM.md` line 2795).
4.2. Define heavy-lift / set sequence with adjacent module dependencies (Module 520 shares amine equipment).
4.3. Define tie-in workfaces grouped by discipline and test pack; align with hydrotest boundary breaks.
4.4. Add common-equipment isolation provisions to the workface plan so future maintenance bypass requirements are physically buildable. [Source: `4-25_Deepcut_DBM.md` line 2429]

### Step 5 — Build the construction interface and turnover checklist
5.1. Create checklist sections for: receipt inspection, set & alignment, grout, mechanical tie-ins, electrical tie-ins, I&C loop checks, F&G loop checks, hydrotest, NDE, punchlist closure, mechanical completion (MC), pre-commissioning, turnover to commissioning.
5.2. Map checklist items to vendor-document turnover entries (DEL-068-05) and to the EPC vendor package acceptance gate (DEL-068-06).
5.3. Define sign-off responsibilities (EPC Construction Manager; QC; vendor representative for vendor-witnessed items; Owner representative for turnover acceptance).

### Step 6 — Quality and source check
6.1. Verify every value used (design pressure, design temperature, heat-medium temperature, module assignments) traces to a cited source. Replace unsourced values with `TBD` or `ASSUMPTION` labels.
6.2. Run the cross-document consistency check (Datasheet ↔ Specification ↔ Guidance ↔ Procedure terms and values).
6.3. Update the `Conflict Table` in `Guidance.md` if any unresolved discrepancy remains.

### Step 7 — Issue for review
7.1. Issue CWP for review with status `IFR` (Issued for Review). [ASSUMPTION: project follows standard IFR/IFC document control; confirm]
7.2. Capture vendor and Owner comments; resolve and re-issue.
7.3. Issue `IFC` (Issued for Construction) only after TEG contactor sparing/configuration is closed in detailed engineering (per Conflict Table CFL-068-03-02). [Source: `4-25_Deepcut_DBM.md` lines 1222, 1237, 1386]

## Verification

| Check | Pass condition |
|---|---|
| Interface coverage | All 13 `YES` PKG-068 interface rows traced to one or more CWP sections; zero unmapped. |
| By-others coverage | SOW-0240 "By others" items (interconnecting piping, foundations, electrical to burner control panel) explicitly addressed in CWP. |
| Requirement coverage | Each `R-CWP-068-03-*` requirement mapped to at least one CWP section and one acceptance test. |
| Source grounding | Every non-trivial value has a `Source:` annotation; unsourced values converted to `TBD` or `ASSUMPTION`. |
| Conflict closure | All Conflict Table rows in `Guidance.md` either resolved (with ruling) or marked as holds blocking IFC. |
| Common-equipment provisions | Isolation, drain, blind, and maintenance access provisions visible in CWP and workface plan. [Source: `4-25_Deepcut_DBM.md` line 2429] |
| Turnover traceability | Turnover checklist references DEL-068-05 vendor-document turnover and DEL-068-06 acceptance. |

## Records

Outputs produced by executing this procedure:
- `Construction Work Package` (the controlling artifact, traceable to `R-CWP-068-03-*`).
- `Installation and tie-in workface plan` — sequence + workfront definitions.
- `Construction interface and turnover checklist` — sign-off record.
- Updated `Conflict Table` in `Guidance.md` with ruled or held items.
- Hydrotest packs, NDE records, alignment records, grout certifications, F&G loop check sheets, MC and turnover sign-off sheets (generated under the issued CWP during field execution; referenced here but not produced by this deliverable).
