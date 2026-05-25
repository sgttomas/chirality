# Specification: DEL-016-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-016` (Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V). It covers:

- the vendor document register,
- vendor document submittals,
- source-required vendor documentation (where source basis defines specific required vendor documents, those rows become artifacts under this deliverable), and
- turnover records.

Out of scope:

- Vendor engineering, design, fabrication, and the physical equipment package (covered by `DEL-016-04_vendor-engineered-equipment-package`).
- EPC review, acceptance, and handoff readiness evidence (covered by `DEL-016-06_epc-vendor-package-review-and-acceptance`).
- The EPC Package Scope of Work and Package Datasheet anchors (`DEL-016-01`, `DEL-016-02`).
- The EPC Construction Work Package (`DEL-016-03`).

## Requirements

| ID | Requirement | Basis | Status |
|---|---|---|---|
| R-1 | The Package Vendor shall produce and maintain a vendor document register for `PKG-016` (TXP-8200-1). | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (package-deliverable expectation) | ASSUMPTION (package-deliverable expectation generalized from DBM mechanical-packages paragraph) |
| R-2 | The vendor document register shall enumerate every vendor document submittal for `PKG-016`, including unique document identity, revision, status code, and submittal/acceptance timeline. | Package documentation discipline; specific field set TBD pending project document control standard | TBD (field-set not extracted) |
| R-3 | The vendor submittals shall cover the documentation required to evidence each declared package interface: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-016` | FACT (interface set); per-interface content TBD |
| R-4 | Source-required vendor documents identified in the source basis (e.g., `_Sources/26020-Package_Requirements.docx`) shall be produced and carried as artifacts under this deliverable. | `_REFERENCES.md`, Source Materials Referenced By Decomposition Row | ASSUMPTION; package-specific source slice not yet extracted |
| R-5 | A turnover record set shall accompany the package. Likely record types for a medium-voltage step-down distribution transformer include factory routine and type test reports (ratio, polarity, no-load loss, load loss, impedance, insulation resistance, dielectric/impulse where applicable), nameplate data, as-built marked drawings, spares list, oil test certificate (if liquid-filled) or dry-type insulation certificate, warranty/maintenance documentation, and an operating and maintenance manual. The exact list is TBD pending the project turnover standard. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`; transformer convention; project turnover standard not in accessible references | TBD (specific list); record-type seed is ASSUMPTION |
| R-6 | All submittals shall be issued through the EPC Integrator interface/integration review workflow. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`, responsible party | FACT (workflow exists); mechanics TBD |
| R-7 | Vendor documentation shall remain consistent with the EPC Package Scope of Work (`DEL-016-01`) and Package Datasheet (`DEL-016-02`), including the 13.8 kV / 600 V / 3 MVA service basis as carried in the DBM 03-25 incoming power section. | `DELIVERABLE_REGISTER.csv` rows `DEL-016-01`, `DEL-016-02`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 745 | FACT (boundary); execution TBD |
| R-8 | Individual source document rows shall be carried as artifacts/evidence under this deliverable and shall not be promoted to standalone deliverables. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`, notes | FACT |

## Standards

| Standard / source | Applicability | Location |
|---|---|---|
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages paragraph | Establishes general vendor document register expectation; applicability to PKG-016 Electrical is ASSUMPTION (best-effort) | line 617 |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers | Establishes the 13.8 kV / 600 V / 3 MVA transformer service identity feeding the LV MCC | lines 738-748 |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, LV service basis | 600 V, 3-phase, 3-wire, 60 Hz, HRG with 5A continuous resistor — relevant to neutral grounding documentation | line 734 |
| `_Sources/26020-Package_Requirements.docx` | Likely source for package-specific required vendor documents | location TBD; package-specific slice not extracted |
| Project document control standard | Governs submittal mechanics, status codes, numbering | location TBD; not present in accessible references |
| Project turnover standard | Governs turnover record set | location TBD; not present in accessible references |
| Applicable industry codes / standards for medium-voltage distribution transformers (e.g., IEEE C57 series, CSA C9 / C802 in Canadian context, NEMA TR / ST) | Likely applicable | location TBD; no clause-level text accessible in references |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Confirm a vendor document register exists for `PKG-016` and is current. |
| R-2 | Inspect register fields against the required field set once the project document control standard is confirmed. |
| R-3 | Map each declared interface in `INTERFACE_REGISTER.csv` for `PKG-016` to at least one vendor submittal that addresses it; capture gaps as TBD. |
| R-4 | Cross-check submittal list against the source-required vendor document list once the `PKG-016` slice of `26020-Package_Requirements.docx` is extracted. |
| R-5 | Inspect turnover record set against the project turnover standard once available; otherwise record TBD. |
| R-6 | Confirm each submittal carries EPC review evidence. |
| R-7 | Compare vendor documentation against `DEL-016-01` SOW and `DEL-016-02` Package Datasheet for consistency, including transformer service identity (13.8 kV / 600 V / 3 MVA). |
| R-8 | Confirm individual source document rows appear as artifacts under this deliverable rather than as siblings in the deliverable register. |

## Documentation

The following artifacts are anticipated:

- Vendor document register (single controlled document).
- Vendor document submittals (set; one per controlled document, multiple revisions).
- Source-required vendor documentation (artifacts created/carried when the source basis enumerates required vendor documents).
- Turnover records (set; specific record types TBD).

All artifacts are governed by `ARTIFACT_REGISTER.csv` rows for `DEL-016-05_vendor-document-turnover-package`.
