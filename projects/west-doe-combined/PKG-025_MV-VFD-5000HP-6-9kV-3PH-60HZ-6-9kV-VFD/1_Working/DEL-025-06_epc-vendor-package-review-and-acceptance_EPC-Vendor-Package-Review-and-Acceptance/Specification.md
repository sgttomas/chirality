# Specification — EPC Vendor Package Review and Acceptance (DEL-025-06)

## Scope

This deliverable specifies the EPC Integrator's review and acceptance of the PKG-025 MV VFD (5000 HP, 6.9 kV, 3-phase, 60 Hz) vendor package. It applies to:

- vendor-engineered equipment package (`DEL-025-04`),
- vendor document turnover package (`DEL-025-05`),
- vendor evidence that supports objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`.

Acceptance is evaluated against the EPC Scope of Work (`DEL-025-01`), Package Datasheet (`DEL-025-02`), and Construction Work Package (`DEL-025-03`). Sources: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv`.

Out of scope:
- Vendor internal design choices that do not affect facility interfaces or contractual scope.
- Re-derivation of facility design basis (covered by DBM and DEL-025-02).
- Authoring of vendor engineering content (`DEL-025-04` author is the Package Vendor).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-025-06-01 | Every artifact in `DEL-025-05` (Vendor Document Turnover Package) shall be logged in the vendor document review log with reviewer, review date, comments, and disposition (accepted / accepted-with-comments / rejected). | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION (standard EPC document-control practice) |
| REQ-025-06-02 | The package acceptance checklist shall map each `DEL-025-01` SOW requirement, each `DEL-025-02` Datasheet line, and each `DEL-025-03` CWP interface/turnover item to acceptance evidence. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` (DEL-025-01..03) |
| REQ-025-06-03 | Acceptance shall confirm the vendor equipment package matches the facility MV system context (6.9 kV, 3-phase, 60 Hz, low-resistance grounded; inverter-drive motor service ≥5,500 hp) or document and route any deviation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Medium-voltage services (line 2935); see Guidance Conflict Table CFT-1 (5000 HP vs ≥5,500 hp) |
| REQ-025-06-04 | Acceptance shall confirm physical and functional fit with the prefabricated MV electrical building housing MV VFDs alongside MV switchgear, MV MCCs, RVSS, UPS, distribution transformers, and PLC panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical buildings (line 2973) |
| REQ-025-06-05 | Acceptance shall verify package interface coverage for the applicable interface types declared for PKG-025: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` (PKG-025) Applicable interface types |
| REQ-025-06-06 | Test and inspection evidence (FAT, routine, inspection, NCR resolutions) shall be provided by the Package Vendor and verified for completeness and applicability by the EPC Integrator before acceptance. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION (industry-standard FAT/SAT practice) |
| REQ-025-06-07 | Turnover evidence shall demonstrate that all turnover items defined in the `DEL-025-03` Construction Work Package are complete, signed, and indexed. | `DELIVERABLE_REGISTER.csv` DEL-025-03 |
| REQ-025-06-08 | Acceptance decisions shall be recorded with a binding human signature; agent-generated drafts are not acceptance decisions. | ASSUMPTION (Chirality governance K-AUTH-1); no project-source citation |
| REQ-025-06-09 | The acceptance record set shall remain version-controlled with traceability to the accepted vendor revision identifiers and to the accepted EPC anchor deliverable revisions. | ASSUMPTION (standard EPC document control); `location TBD` |

Detail-level acceptance values (specific witness points, hold points, pass thresholds, document classes, NCR escalation paths) are `TBD` until vendor-specific or facility-specific procurement specifications are accepted into the source set.

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Project Design Basis Memorandum (DBM) — Deepcut | Facility electrical context for MV VFD (6.9 kV / inverter-drive motor service / electrical-building housing) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| `26020-Package_Requirements.docx` | Package-class requirements (presumed applicable to PKG-025) | `_Sources/` (binary; not opened this pass) — `location TBD` |
| IEEE / NEMA / IEC standards for MV adjustable-speed drives (e.g., IEEE 519, NEMA ICS 7, IEC 61800-series) | Likely applicable to vendor engineering and FAT scope | ASSUMPTION; not cited in accessible project sources — `location TBD` |
| BC Hydro / utility interconnection requirements | Power-quality compliance at the utility interface | ASSUMPTION; only utility-transformer grounding is cited (`4-25_Deepcut_DBM.md` line 2985) — clause-level VFD coverage `location TBD` |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-025-06-01 | Review of the vendor document review log against the `DEL-025-05` document register: 100% coverage check. |
| REQ-025-06-02 | Trace matrix audit: SOW → checklist line; Datasheet line → checklist line; CWP turnover item → checklist line. |
| REQ-025-06-03 | Datasheet-vs-vendor comparison; surface any HP or MV-service mismatch through the Conflict Table. |
| REQ-025-06-04 | Layout / building integration review against MV electrical-building drawings (TBD; DBM only describes building contents qualitatively). |
| REQ-025-06-05 | Interface walkdown using the interface types declared in `PACKAGE_REGISTER.csv` (PKG-025); confirm each interface has an accepted definition in `DEL-025-02` and an accepted physical/contractual interface owner. |
| REQ-025-06-06 | Inspection of FAT/inspection reports and NCR closures provided in `DEL-025-05`. |
| REQ-025-06-07 | Confirmation that every `DEL-025-03` CWP turnover line is signed and filed. |
| REQ-025-06-08 | Human-signed acceptance record present (per governance). |
| REQ-025-06-09 | Document-control audit: vendor revision IDs and EPC deliverable revision IDs cross-referenced in the acceptance record. |

## Documentation

Required output artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test / inspection evidence index
- Turnover evidence index
- Human-signed acceptance decision record (per REQ-025-06-08)
