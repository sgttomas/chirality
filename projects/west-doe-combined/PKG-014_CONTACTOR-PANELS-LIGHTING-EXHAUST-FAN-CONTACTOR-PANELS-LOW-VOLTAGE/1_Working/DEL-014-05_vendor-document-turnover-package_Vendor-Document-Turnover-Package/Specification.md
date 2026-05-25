# Specification: DEL-014-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-014` (CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE). It covers:

- the vendor document register,
- vendor document submittals,
- source-required vendor documentation (where source basis defines specific required vendor documents, those rows become artifacts under this deliverable), and
- turnover records.

Out of scope:

- Vendor engineering, design, fabrication, and the physical equipment package (covered by `DEL-014-04_vendor-engineered-equipment-package`).
- EPC review, acceptance, and handoff readiness evidence (covered by `DEL-014-06_epc-vendor-package-review-and-acceptance`).
- The EPC Package Scope of Work and Package Datasheet anchors (`DEL-014-01`, `DEL-014-02`).
- The EPC Construction Work Package (`DEL-014-03`).

## Requirements

| ID | Requirement | Basis | Status |
|---|---|---|---|
| R-1 | The Package Vendor shall produce and maintain a vendor document register for `PKG-014`. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (package-deliverable expectation) | ASSUMPTION (package-deliverable expectation generalized from DBM mechanical-packages paragraph) |
| R-2 | The vendor document register shall enumerate every vendor document submittal for `PKG-014`, including unique document identity, revision, status code, and submittal/acceptance timeline. | Package documentation discipline; specific field set TBD pending project document control standard | TBD (field-set not extracted) |
| R-3 | The vendor submittals shall cover the documentation required to evidence each declared package interface: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-014` | FACT (interface set); per-interface content TBD |
| R-4 | Source-required vendor documents identified in the source basis (e.g., `_Sources/26020-Package_Requirements.docx`) shall be produced and carried as artifacts under this deliverable. | `_REFERENCES.md`, Source Materials Referenced By Decomposition Row | ASSUMPTION; package-specific source slice not yet extracted |
| R-5 | A turnover record set shall accompany the package. Specific record types (e.g., FAT/SAT reports, test/inspection certificates, nameplate data, as-built marked drawings, spares list, warranty/maintenance documentation) are TBD pending the project's turnover standard. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05`; project turnover standard not in accessible references | TBD |
| R-6 | All submittals shall be issued through the EPC Integrator interface/integration review workflow. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05`, responsible party | FACT (workflow exists); mechanics TBD |
| R-7 | Vendor documentation shall remain consistent with the EPC Package Scope of Work (`DEL-014-01`) and Package Datasheet (`DEL-014-02`). | `DELIVERABLE_REGISTER.csv` rows `DEL-014-01`, `DEL-014-02` | FACT (boundary); execution TBD |
| R-8 | Individual source document rows shall be carried as artifacts/evidence under this deliverable and shall not be promoted to standalone deliverables. | `DELIVERABLE_REGISTER.csv` row `DEL-014-05`, notes | FACT |

## Standards

| Standard / source | Applicability | Location |
|---|---|---|
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages paragraph | Establishes general vendor document register expectation; applicability to PKG-014 is ASSUMPTION (best-effort) | line 617 |
| `_Sources/26020-Package_Requirements.docx` | Likely source for package-specific required vendor documents | location TBD; package-specific slice not extracted |
| Project document control standard | Governs submittal mechanics, status codes, numbering | location TBD; not present in accessible references |
| Project turnover standard | Governs turnover record set | location TBD; not present in accessible references |
| Applicable industry codes / standards for low-voltage contactor panels | Likely applicable | location TBD; no clause-level text accessible |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Confirm a vendor document register exists for `PKG-014` and is current. |
| R-2 | Inspect register fields against the required field set once the project document control standard is confirmed. |
| R-3 | Map each declared interface in `INTERFACE_REGISTER.csv` for `PKG-014` to at least one vendor submittal that addresses it; capture gaps as TBD. |
| R-4 | Cross-check submittal list against the source-required vendor document list once the `PKG-014` slice of `26020-Package_Requirements.docx` is extracted. |
| R-5 | Inspect turnover record set against the project turnover standard once available; otherwise record TBD. |
| R-6 | Confirm each submittal carries EPC review evidence. |
| R-7 | Compare vendor documentation against `DEL-014-01` SOW and `DEL-014-02` Package Datasheet for consistency. |
| R-8 | Confirm individual source document rows appear as artifacts under this deliverable rather than as siblings in the deliverable register. |

## Documentation

The following artifacts are anticipated:

- Vendor document register (single controlled document).
- Vendor document submittals (set; one per controlled document, multiple revisions).
- Source-required vendor documentation (artifacts created/carried when the source basis enumerates required vendor documents).
- Turnover records (set; specific record types TBD).

All artifacts are governed by `ARTIFACT_REGISTER.csv` rows for `DEL-014-05_vendor-document-turnover-package`.
