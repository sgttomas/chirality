# Datasheet — DEL-096-06 EPC Vendor Package Review and Acceptance (PKG-096 Tanks, Sour Condendate (API 650))

> Descriptive index of the EPC Integrator's vendor-package review-and-acceptance evidence set for PKG-096. The deliverable artifact itself is a controlled review/acceptance dossier; this datasheet identifies the dossier, the package under review, and the inputs the dossier evaluates against.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-096-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` Identity |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` Identity |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-096` | `_CONTEXT.md` Identity |
| Package Name | Tanks, Sour Condendate (API 650) | `_CONTEXT.md` Identity |
| Workbook row | Packages row 92 | `_CONTEXT.md` Source Reference |
| Package heading | `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate" | `_CONTEXT.md` Source Reference; package heading text |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` Identity |
| Covers Scope Items | SOW-0217, SOW-0218, SOW-0219, SOW-0220 | `_CONTEXT.md` Covers Scope Items |
| Supports Objectives | OBJ-002 through OBJ-010 (PACKAGE_HEURISTIC — **ASSUMPTION (best-effort mapping)**) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` confirms OBJ-002..OBJ-010 are mapped to `DEL-096-06` |

## Attributes

### Subject Under Review — Package Identity

| Attribute | Value | Source |
|---|---|---|
| Tagged equipment | TK-9110-2, TK-9120-2 | Package heading "Tanks, Sour Condensate" — Basic Scope / Major Included Equipment |
| Quantity & size | Two (2) 3800 bbl Sour Inlet Condensate Storage Tanks | Package heading — Basic Scope |
| Process function | Sour C5+ Condensate Storage Tanks | Package heading — Basic Scope |
| Location | 3-25 West Doe Liquids Hub tank farm | Package heading — Location / Status |
| Source basis (RFQ) | `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` (location TBD — RFQ not locally accessible) | Package heading — Source Basis |

### Subject Under Review — Code, Service, Protective Design

| Attribute | Value | Source |
|---|---|---|
| Design & fabrication code | Modified API 650 | Package heading — Major Included Equipment |
| Service | Sour service (H2S present); NACE compliant | Package heading — Major Included Equipment |
| Blanket gas system | Blanket gas system per API 2000 | Package heading — Major Included Equipment |
| Internal coating | Devchem 253 on floors, walls, roofs | Package heading — Major Included Equipment |
| Insulation | Non-insulated | Package heading — Major Included Equipment |
| Pressure relief / venting | PVRV (vacuum or modulating pressure relief), EPRV (emergency relief), VRU header connection | Package heading — Major Included Equipment |
| Fill protection | Maximum fill 90% shutdown; nozzles sized so plant design capacity can fill a single tank | Package heading — Major Included Equipment / Scope Notes |

### Subject Under Review — Conditions

| Attribute | Value | Source |
|---|---|---|
| Design pressure | 32 oz test pressure | Package heading — Scope Notes / Open Items |
| Design temperature | -40 °C (min) / 60 °C (max) | Package heading — Scope Notes / Open Items |
| Operating pressure | Atmospheric | Package heading — Scope Notes / Open Items |
| Operating temperature | Ambient (Item No. 1) | Package heading — Scope Notes / Open Items |
| Design flow (Item No. 1) | 27,606 kg/h / 919 Am3/d | Package heading — Scope Notes / Open Items |
| By Others (out of vendor scope) | Foundations; mounting tanks at site; electrical/instrumentation; platforms; staircase | Package heading — Scope Notes / Open Items |

## Conditions

### Review-and-Acceptance Dossier Conditions

| Condition | Value | Source |
|---|---|---|
| Review lead | EPC Integrator | `_CONTEXT.md` ResponsibleParty |
| Vendor input | Package Vendor provides documents and clarifications for review | `_CONTEXT.md` ResponsibleParty; `_CONTEXT.md` Scope |
| Acceptance basis | EPC Scope of Work (DEL-096-01), Package Datasheet (DEL-096-02), Construction Work Package (DEL-096-03) | `_CONTEXT.md` Scope (acceptance "against the EPC Scope of Work, Package Datasheet, and Construction Work Package") |
| Vendor inputs under review | Vendor Engineered Equipment Package (DEL-096-04), Vendor Document Turnover Package (DEL-096-05) | ASSUMPTION (best-effort mapping): identifiers inferred from sibling deliverables in `PKG-096` and from `_CONTEXT.md` Scope (vendor package review & integration acceptance) |

## Construction

### Anticipated Artifacts (dossier contents)

| Artifact | Description | Source |
|---|---|---|
| Vendor document review log | Per-document review record (received, reviewed, status, comments, dispositions) for vendor submittals | `_CONTEXT.md` Anticipated Artifacts |
| Package acceptance checklist | Item-by-item acceptance checklist against SOW, Package Datasheet, and Construction Work Package | `_CONTEXT.md` Anticipated Artifacts |
| Test/inspection evidence | Witnessed/reviewed FAT, ITP step records, inspection releases, MTRs | `_CONTEXT.md` Anticipated Artifacts; package heading — Vendor Engineering Deliverables (QLT-003, QLT-013, QLT-020, MEC-021, MEC-022) |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book, IOM, as-builts as available | `_CONTEXT.md` Anticipated Artifacts; package heading — Vendor Engineering Deliverables (QLT-021, MEC-023, MEC-025, PRQ-016) |

### Vendor-Engineering Inputs Subject to Review (from package heading "Vendor Engineering Deliverables")

The vendor engineering deliverable IDs that the EPC review-and-acceptance dossier evaluates include (non-exhaustive — full list in package heading):

- Core vendor documents: `PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`
- Core package engineering: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-014`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`
- Storage tanks: `MEC-005`, `MEC-011`
- Relief / flare / vent: `PRO-014`, `PRO-015`, `PRO-016`, `PRO-017`, `PRO-018`
- Process piping interfaces: `PRO-008`, `PIP-003`, `PIP-004`, `PIP-006`, `PIP-007`, `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`, `PIP-028`

Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Vendor Engineering Deliverables.

### Interface Applicability Driving Integration Acceptance

The EPC integration-acceptance review SHALL confirm vendor handling of each "Yes" interface from the package heading's Physical Interface Summary:

- Process Piping (Yes); Relief / Flare / Vent (Yes); Drain / Containment (Yes); Area / Exterior Lighting (Yes); Grounding / Bonding (Yes); Cathodic Protection (Yes); I&C / Control Cabling (Yes); Grading / Site Drainage / Spill Containment (Yes); Structural / Foundations / Supports (Yes)
- "No" interfaces (not applicable per source): Utility Piping; Electrical Power; EHT; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Product Loading; Pipeline / Pigging

Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Physical Interface Summary.

## References

- `_CONTEXT.md` — identity, scope, anticipated artifacts (this deliverable folder)
- `_REFERENCES.md` — authoritative reference list (this deliverable folder)
- `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" (located via search in `_Sources/26020-Package_Requirements.docx`)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv` — objective association
- `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` — **location TBD** (not locally accessible)
- Sibling deliverables (acceptance basis): `DEL-096-01` Scope of Work, `DEL-096-02` Package Datasheet, `DEL-096-03` Construction Work Package, `DEL-096-04` Vendor Engineered Equipment Package, `DEL-096-05` Vendor Document Turnover Package
