# Specification: DEL-024-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-024` (MV VFD - 2000 HP, 4160 V, 3-phase, 60 Hz, 4160 V VFD). It establishes what the Package Vendor shall produce, submit, and turn over as the controlled vendor documentation set for the package, and what the EPC Integrator shall review for interface and integration consistency. (Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-024-05`; `PACKAGE_REGISTER.csv` row `PKG-024`.)

**In scope.**
- Vendor document register for `PKG-024`.
- Vendor document submittals during execution (engineering, design, manufacturing, and test submittals issued by the Package Vendor).
- Source-required vendor documentation, when source materials list specific required documents for this package (`TBD` until source slice is accepted; see Requirement R-05).
- Turnover records (final accepted vendor document set used for handoff).
- Individual source document rows, carried as artifacts/evidence under this deliverable.

**Out of scope.**
- Vendor engineered equipment design, fabrication, and supply (covered by `DEL-024-04`).
- EPC integration review and acceptance decisions on the vendor package as a whole (covered by `DEL-024-06`).
- Construction installation and tie-in work (covered by `DEL-024-03`).
- Package scope of work definition (covered by `DEL-024-01`).
- Package datasheet content (covered by `DEL-024-02`).

## Requirements

| ID | Requirement | Basis |
|---|---|---|
| R-01 | The Package Vendor shall maintain a single vendor document register for `PKG-024` covering all vendor documents to be submitted, reviewed, and turned over. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-024-05` |
| R-02 | The vendor document register shall identify, at minimum, each vendor document by document number, title, revision, status, submittal date, and acceptance evidence. | ASSUMPTION (industry convention for Vendor Document Turnover deliverables) |
| R-03 | Vendor document submittals shall be issued through controlled revision and routed to the EPC Integrator for interface/integration review. | `DELIVERABLE_REGISTER.csv` rows `DEL-024-05`, `DEL-024-06` |
| R-04 | The EPC Integrator shall review vendor document submittals for interface and integration consistency against `DEL-024-01_scope-of-work` and `DEL-024-02_package-datasheet`; acceptance disposition is recorded as evidence under `DEL-024-06`. | `DELIVERABLE_REGISTER.csv` rows `DEL-024-01`, `DEL-024-02`, `DEL-024-05`, `DEL-024-06` |
| R-05 | When source materials list specific vendor documents required for `PKG-024`, the vendor document register shall include each such document and shall record acceptance evidence for it. Specific source-required list is `TBD` pending acceptance of a `PKG-024`-specific slice from `26020-Package_Requirements.docx` or equivalent. | `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` row `ART-66A1FEA60C` |
| R-06 | Vendor documents shall provide the interface evidence required by each applicable interface for `PKG-024`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-024` |
| R-07 | If the VFD or any VFD-fed motor for `PKG-024` is located in a Zone 2 area, vendor documents shall include marking and temperature-code evidence consistent with the area-classification drawing or fugitive-emissions study. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (VFD-fed motor / hazardous-area paragraph) |
| R-08 | The turnover record shall consist of the final accepted set of vendor documents, organized for handoff to the EPC Integrator. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-024-05` |
| R-09 | Individual source document rows referenced by the decomposition shall be carried as artifacts/evidence under this deliverable, not as separate deliverables. | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row `DEL-024-05` |
| R-10 | No requirement, design value, or content for a specific vendor document shall be inferred without source support; unsupported items shall be marked `TBD`. | `_REFERENCES.md`; method discipline |

## Standards

| Standard / Source | Role | Status |
|---|---|---|
| `26020-Package_Requirements.docx` | Candidate source for required vendor documentation list per package. | location TBD for `PKG-024`-specific slice; `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` row `ART-66A1FEA60C` |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Project design-basis manual; provides VFD-fed motor / hazardous-area constraints applicable to vendor document content. | accessible |
| `26020-Packages_Interfaces_4_export.xlsx` (Packages sheet row 26) | Confirms package identity, discipline, and interface applicability. | accessible via `PACKAGE_REGISTER.csv`; row preserved |
| External standards (e.g., NETA acceptance testing, IEC/NEMA VFD documentation) | May apply to required vendor document contents. | location TBD; not derived from accessible sources |

## Verification

| Requirement | Verification approach |
|---|---|
| R-01 | Inspection of the deliverable folder for a single, identifiable vendor document register. |
| R-02 | Inspection of the register schema for the minimum fields listed. |
| R-03 | Review of submittal transmittal records and revision history. |
| R-04 | Cross-reference register acceptance entries against `DEL-024-06` acceptance evidence. |
| R-05 | Once a `PKG-024`-specific source slice is accepted, gap analysis between source-required documents and the vendor document register. Until then, verification status is `TBD`. |
| R-06 | Cross-reference each applicable interface row in `INTERFACE_REGISTER.csv` to the vendor document(s) that carry the interface evidence. |
| R-07 | Inspection of vendor documents for area-classification marking and temperature-code evidence, where Zone 2 applicability is established by the EPC area-classification drawing. |
| R-08 | Inspection of the turnover record set for completeness against the accepted register. |
| R-09 | Inspection that no source document row appears as a separate deliverable folder elsewhere in `PKG-024`. |
| R-10 | Audit that all non-`TBD` content cites source slices; remaining items remain `TBD` or `ASSUMPTION`. |

## Documentation

The following artifacts are anticipated under this deliverable (per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row `DEL-024-05`):

- Vendor document register (single controlled file or workbook).
- Vendor document submittals (collected as received and revised).
- Source vendor document table rows, carried as artifacts/evidence.
- Turnover records (final accepted set).

Specific content lists, formats, and counts are `TBD` pending acceptance of a `PKG-024`-specific source slice from `26020-Package_Requirements.docx` or equivalent.
