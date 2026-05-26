# Procedure — DEL-065-04 Vendor Engineered Equipment Package

This procedure describes steps to **produce** the vendor-engineered equipment package and the design-basis artifact set for PKG-065. (Source: `_CONTEXT.md` Type "Vendor Package Production Unit".)

## Purpose

Provide a repeatable workflow for the Package Vendor to convert the EPC Scope of Work (DEL-065-01) and EPC Package Datasheet (DEL-065-02) into a fabricated, documented, modified-API-650 caustic tank package (two 400 bbl tanks) ready for EPC Integrator acceptance (DEL-065-06).

## Prerequisites

### Inputs that MUST be available before starting

- DEL-065-01 — EPC Scope of Work for PKG-065 (Source: `_CONTEXT.md`).
- DEL-065-02 — EPC Package Datasheet for PKG-065 (Source: `_CONTEXT.md`).
- Workbook Packages row 87 / `26020-Package_Requirements.docx` package heading 20 reference set (Source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv` row 87).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for process basis (Source: `_REFERENCES.md`; `OBJECTIVE_PACKAGE_MAP.csv` Word Source Basis).

### Declared upstream dependencies

`_DEPENDENCIES.md` declares **none** for this deliverable as of 2026-05-24 (PREPARATION). The companion-deliverable list in SOW-0197 implies that DEL-065-01 and DEL-065-02 are practical prerequisites; that relationship is an **ASSUMPTION** until declared.

### References

- All references in `_REFERENCES.md`.
- Modified API 650.
- Subordinate vendor standards (welding, NDE, coating) — vendor's own QMS.

## Steps

### Step 1 — Ingest EPC handoff

1.1 Receive DEL-065-01 (EPC Scope of Work) and DEL-065-02 (EPC Package Datasheet).
1.2 Reconcile against `26020-Package_Requirements.docx` pkg heading 20 (via SCOPE_LEDGER SOW-0197-0200). Flag any deltas to the EPC Integrator before proceeding.
1.3 Capture site min ambient temperature, throughput / flow values, fresh-caustic tank design pressure, and any modifications to API 650 from DEL-065-02 — these are the source-silent items the vendor cannot resolve unilaterally (per Guidance Conflict Table CONF-01..05).

### Step 2 — Establish vendor design basis

2.1 Construct the vendor package design basis covering both tanks (Item 1 spent caustic TK-6780-1; Item 2 fresh caustic):
- Code of construction: modified API 650 (incorporate modifications received in Step 1.3).
- Nominal capacity: 400 bbl each.
- Design pressure: 32 oz / 1.0 oz vacuum for Item 1; Item 2 per EPC confirmation (CONF-01).
- Design temperature minimum: site min ambient per EPC confirmation.
- Heater on Item 1 sized for ≥ 32.2 °C (90 °F). Item 2 heater per EPC confirmation (CONF-04).
- Material of construction: vendor proposal with caustic-service justification (CONF-05).
2.2 Document each assumption and each "vendor-proposed" choice with rationale and the corresponding source slice (or "EPC confirmation pending").

### Step 3 — Detailed design

3.1 Produce mechanical calculation packages for both tanks per modified API 650 (shell, bottom, roof, anchorage interface points, nozzles).
3.2 Design heater for TK-6780-1 (duty, control approach, integration with package I&C interface).
3.3 Generate vendor datasheets, GA drawings, nozzle schedules, instrument schedules, and interface termination drawings (matching the nine PKG-065 interface types — see Datasheet §Interfaces).
3.4 Internal vendor design review and sign-off.

### Step 4 — Procurement, fabrication, and FAT

4.1 Material procurement against the MOC selection accepted under DEL-065-06.
4.2 Fabrication per modified API 650 with NDE and inspection per vendor QMS.
4.3 Heater factory assembly and functional test.
4.4 Hydrotest / leak test per code.
4.5 Factory Acceptance Test (FAT) including dimensional, weld, coating (if used), and heater functional checks.

### Step 5 — Vendor documentation assembly (feeds DEL-065-05)

5.1 Assemble the vendor document data book: design basis, calculations, mill certs, NDE reports, hydrotest records, coating/lining records (if used), FAT records, O&M manual, recommended spares.
5.2 Hand off documentation set to DEL-065-05 Vendor Document Turnover Package.

### Step 6 — Ship and support EPC Integrator acceptance (DEL-065-06)

6.1 Ship the equipment package to the site under the EPC Integrator's logistics direction. (Site mounting/foundations are By Others per SOW-0200; vendor does not perform installation.)
6.2 Support EPC Integrator review and acceptance under DEL-065-06; close out punch items.

## Verification

| Step | Verification Check | Acceptance Criterion |
|---|---|---|
| 1 | EPC handoff reconciliation completed | Written acknowledgement of all CONF-01..05 dispositions before Step 2 closes |
| 2 | Vendor design basis approved internally and (where required) by EPC Integrator | Signed design basis document |
| 3 | Modified API 650 calculation package complete | Calc set passes internal review and third-party check where mandated |
| 4 | Fabrication, NDE, hydrotest passed | Inspection records, hydrotest certificate, FAT report |
| 5 | Vendor data book complete | All required artifacts present per DEL-065-05 contents list |
| 6 | EPC Integrator acceptance | DEL-065-06 acceptance record issued |

## Records

The procedure produces (each becomes evidence for downstream deliverables):

- Vendor package design basis (covers ART-5507339ADA).
- Modified API 650 mechanical calculation packages (Item 1, Item 2).
- Vendor datasheets, GA drawings, nozzle/instrument schedules.
- Material certificates and traceability records.
- NDE reports.
- Hydrotest / leak test certificates.
- Heater design and FAT records.
- Coating/lining qualification (if used).
- FAT report.
- O&M manual; recommended spares list.
- Interface compliance matrix (nine PKG-065 interface types).
- Vendor documentation transmittal to DEL-065-05.
- EPC Integrator acceptance record (closed out under DEL-065-06).

Where a record's content depends on values not in the local source slice (e.g., site min ambient, throughput), the record SHALL cite the issuing EPC Integrator document (DEL-065-02 revision) as the value source rather than vendor invention.
