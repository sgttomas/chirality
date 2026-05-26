# Datasheet — DEL-080-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-080-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` Identity |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-080` (Inlet Compressors, WBS 02) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-080 |
| Workbook Row | Packages row 66 | `_CONTEXT.md` Source Reference |
| Package Tracking No. | `26020-02-12-001 - Inlet Compressors` | `PACKAGE_REGISTER.csv` PKG-080 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0119`, `SOW-0120`, `SOW-0121`, `SOW-0122` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance subject | Vendor-engineered inlet compressor package (PKG-080) — two identical parallel sour inlet gas reciprocating compressor packages | `SCOPE_LEDGER.csv` SOW-0120 |
| Equipment population | Two (2) Ariel KBZ/6 separable reciprocating compressor packages, two-stage compression with intercooling and aftercooling; modular self-framing buildings; piping; instrumentation; electrical; HVAC; package auxiliaries | `SCOPE_LEDGER.csv` SOW-0121 |
| Configuration | 2 x 50% with no dedicated spare | `SCOPE_LEDGER.csv` SOW-0122 |
| Acceptance review basis | EPC Scope of Work (DEL-080-01), Package Datasheet (DEL-080-02), Construction Work Package (DEL-080-03), Vendor Engineered Equipment Package (DEL-080-04), Vendor Document Turnover Package (DEL-080-05) | `_CONTEXT.md` Scope; `SCOPE_LEDGER.csv` SOW-0119 (deliverable chain) |
| Vendor/EPC split | Package Vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | `PACKAGE_REGISTER.csv` PKG-080; `OBJ-004` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Process service | Sour inlet natural gas (NACE-compliant materials and seals required) | `SCOPE_LEDGER.csv` SOW-0122 |
| Combined throughput | Approximately 80 MMSCFD (40 MMSCFD per unit) | `SCOPE_LEDGER.csv` SOW-0122 |
| Suction pressure (approx.) | ~1275 kPag | `SCOPE_LEDGER.csv` SOW-0122 |
| Discharge pressure (approx.) | ~6550 kPag | `SCOPE_LEDGER.csv` SOW-0122 |
| Sparing | No dedicated spare | `SCOPE_LEDGER.csv` SOW-0122 |
| Applicable interface envelope | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` PKG-080 interface set |

## Construction (Artifacts Produced)

| Artifact | Description | Source |
|---|---|---|
| Vendor document review log | Item-by-item dispositions of vendor documents in the turnover package (DEL-080-05) against EPC SoW and Package Datasheet | `_CONTEXT.md` Anticipated Artifacts |
| Package acceptance checklist | Structured EPC acceptance evidence covering scope, interfaces, vendor documents, test/inspection, and outstanding items | `_CONTEXT.md` Anticipated Artifacts |
| Test/inspection evidence | Witness/hold-point records, ITR/ITP completion records, NCR closeouts, FAT and SAT evidence (as applicable) | `_CONTEXT.md` Anticipated Artifacts; OBJ-010 |
| Turnover evidence | Mechanical completion, system turnover, and open-item closure evidence supporting facility handoff readiness | `_CONTEXT.md` Anticipated Artifacts; OBJ-010 |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot: `.../_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `PACKAGE_REGISTER.csv` row PKG-080
- `DELIVERABLE_REGISTER.csv` row DEL-080-06
- `SCOPE_LEDGER.csv` rows SOW-0119, SOW-0120, SOW-0121, SOW-0122
- `OBJECTIVE_REGISTER.csv` rows OBJ-002 through OBJ-010
- Workbook Packages row 66 (location TBD locally; cited via decomposition extract)
- `26020-Package_Requirements.docx` package heading 33 (Inlet Compressors) — local source slice not copied to this deliverable; cited via decomposition extract (`_REFERENCES.md` Missing / Deferred References)
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — referenced by PKG-080 register row; local slice not copied to this deliverable
