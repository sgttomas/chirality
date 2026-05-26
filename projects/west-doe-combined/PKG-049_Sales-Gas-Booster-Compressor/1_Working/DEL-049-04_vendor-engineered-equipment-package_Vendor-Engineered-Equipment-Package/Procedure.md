# Procedure: DEL-049-04 — Vendor Engineered Equipment Package

This procedure describes how to **produce** the Vendor Engineered Equipment
Package production unit for PKG-049, anchored on the EPC Scope of Work
(DEL-049-01) and EPC Package Datasheet (DEL-049-02), and how to verify it is
ready for EPC Integrator review under DEL-049-06. Operation/maintenance of the
delivered package is governed downstream by vendor O&M manuals (produced under
DEL-049-05) and is out of this procedure's scope.

## Prerequisites

Inputs (declared upstream is currently "none" in `_DEPENDENCIES.md`; the items
below are the source-stated authority anchors and should be promoted to
declared upstreams when they exist):

- DEL-049-01 Scope of Work (EPC Integrator) — package scope, tagged equipment, function, source basis, boundaries, integration narrative.
- DEL-049-02 Package Datasheet (EPC Integrator) — technical handoff data, package interface requirements matrix, source-supported equipment and design criteria.
- Source rows SOW-0169, SOW-0170, SOW-0171, SOW-0172 in `SCOPE_LEDGER.csv`.
- PKG-049 row in `PACKAGE_REGISTER.csv` (responsibility model, applicable interface types).
- PKG-049 rows in `INTERFACE_REGISTER.csv` (13 applicable interface types).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.

References required to be opened by the Vendor before sizing/material decisions:

- `26020-Package_Requirements.docx` package heading 4 — process mechanical package requirements (location TBD inside this deliverable's scope).
- `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` — RFQ source (location TBD inside this deliverable's scope).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — design-basis sections relevant to sour service, compression, electrical, controls, utilities, safety (location TBD inside this deliverable's scope).

## Steps

### Step 1 — Ingest EPC anchors

1. Read DEL-049-01 (Scope of Work) and capture the package's stated function, boundary, and integration narrative.
2. Read DEL-049-02 (Package Datasheet) and capture process conditions, equipment list, and interface termination requirements.
3. Reconcile against SOW-0169..SOW-0172. Flag any disagreement back to the EPC; do **not** silently resolve.

### Step 2 — Establish the vendor package design basis

1. Lock the process design conditions from SOW-0172 (R2 in `Specification.md`): 140 MMSCFD, 6,137 kPag suction / 12,866 kPag discharge, 110 °F summer inlet, 0.61 SG suction-scrubber liquid assumption.
2. Lock the major-equipment list from SOW-0171 (R3 in `Specification.md`): Ariel KBX/X compressor, 8-pole induction motor (DOL + soft-start), API 661 forced-air intercoolers (per stage), two-phase mesh/vane suction scrubbers (per stage), two-phase packing vent / drain separation pot at ≥101 kPag, seal-pot waste-oil transfer pump, 0.3 µm @ 99.97 % filter coalescer at 100 MMSCFD with band-lock QOC.
3. Define sour-service material and inspection posture from the DBM (ASSUMPTION until confirmed against the DBM section; location TBD).
4. Document boundary-of-supply explicitly per SOW-0172 (shipping, pile installation, tie-in piping, field electrical, mounting platform/stairs are "by others").

### Step 3 — Engineer the package

1. Size vendor-designed items (suction scrubbers, packing vent/drain separation pot, seal-pot waste-oil transfer pump, filter coalescer) against the design conditions in Step 2.1.
2. Lay out the skid with on-skid piping, on-skid utilities, on-skid electrical, and on-skid I&C terminating at the 13 interface types listed for PKG-049 in `INTERFACE_REGISTER.csv`.
3. Produce equipment-level datasheets for each major equipment item in Step 2.2.
4. Produce GA drawings, P&IDs, and termination drawings consistent with the EPC Package Datasheet's interface matrix.
5. Produce calculations supporting sizing, vessel design, vibration/pulsation analysis (typical for reciprocating compressors — ASSUMPTION until confirmed against the RFQ/DBM), and electrical/I&C loads.

### Step 4 — Vendor documentation

1. Compile the vendor package design basis document covering process, mechanical, structural-on-skid, on-skid electrical, on-skid I&C, and safety provisions.
2. Compile the equipment datasheet set for the major equipment in Step 2.2.
3. Hand the document register and submittal package to DEL-049-05 (Vendor Document Turnover Package) per its register convention.

### Step 5 — Fabricate and supply

1. Issue the engineered package for fabrication per the locked design basis.
2. Execute Vendor QA/QC against the standards in `Specification.md` §Standards (API 661 for intercoolers; NEMA MG 1 for the driver) and any additional standards confirmed during Step 2.3.
3. Witness/hold-point coordination and FAT scope: TBD — requires the RFQ slice (location TBD).

### Step 6 — Submit for EPC integration review

1. Provide the engineered package, vendor design basis, equipment datasheets, calculations, drawings, and FAT records to the EPC Integrator under DEL-049-06.
2. Address EPC review comments; revise vendor documents through the DEL-049-05 register.
3. Coordinate construction-side handoff items (shipping, pile installation, tie-in piping, field electrical, mounting platform/stairs) with DEL-049-03 (Construction Work Package).

## Verification

| Check | Method | Reference |
|---|---|---|
| Package consistent with EPC SoW and Package Datasheet | EPC Integrator review against DEL-049-01 and DEL-049-02 | `Specification.md` R1 |
| Process conditions correct | Cross-check vendor design basis vs SOW-0172 | `Specification.md` R2 |
| Equipment composition correct | Vendor datasheet review vs SOW-0171 | `Specification.md` R3 |
| All 13 interfaces terminated and matched to the EPC Package Datasheet | Interface matrix walkdown | `Specification.md` R4 |
| Vendor documentation complete | Vendor document register completeness check under DEL-049-05 | `Specification.md` R5 |
| Boundary-of-supply correct | Boundary matrix in vendor documentation vs SOW-0172 | `Specification.md` R6 |
| Standards applied (API 661, NEMA MG 1; additional sour-service codes) | Code/standard traceability matrix | `Specification.md` §Standards |

## Records

The successful execution of this procedure should produce, at minimum:

- Vendor package design basis document.
- Equipment datasheet set for the items in SOW-0171.
- GA / P&ID / termination / interface drawings.
- Sizing and design calculations (including pulsation/vibration analysis — ASSUMPTION).
- FAT records and inspection certificates (scope TBD).
- Vendor document register entries (delivered to DEL-049-05).
- EPC Integrator review evidence (captured under DEL-049-06).
- The fabricated, supplied physical equipment package itself.
