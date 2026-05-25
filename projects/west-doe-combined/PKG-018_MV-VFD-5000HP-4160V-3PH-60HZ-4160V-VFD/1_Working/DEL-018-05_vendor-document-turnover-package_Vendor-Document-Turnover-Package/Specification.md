# Specification — DEL-018-05 Vendor Document Turnover Package

## Scope

### Included
- A single Package Vendor deliverable comprising:
  - the vendor document register for `PKG-018` (MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD),
  - controlled vendor document submittals,
  - source-required vendor documentation carried as artifact evidence where available,
  - turnover records to the EPC Integrator.
- EPC Integrator interface/integration review of the documentation set.

Sources: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row `DEL-018-05`.

### Excluded
- Engineering, design, fabrication, and the physical equipment package itself — owned by `DEL-018-04` (Vendor Engineered Equipment Package). Source: `DELIVERABLE_REGISTER.csv` row `DEL-018-04`.
- EPC review/acceptance and turnover-readiness evidence — owned by `DEL-018-06` (EPC Vendor Package Review and Acceptance). Source: `DELIVERABLE_REGISTER.csv` row `DEL-018-06`.
- Facility-level integration and interfaces themselves — owned by EPC Integrator at the package boundary. Source: `PACKAGE_REGISTER.csv` row `PKG-018`.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-1 | The deliverable shall be issued as a single Package Vendor production unit covering vendor document register, submittals, source-required vendor documentation, and turnover records. | `DELIVERABLE_REGISTER.csv` (Description/Type, row `DEL-018-05`); `_CONTEXT.md` Scope |
| R-2 | The vendor document register shall include, at minimum, the package-document classes called out in the source mechanical-packages organization basis: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating/design envelopes, sparing philosophy, materials/coating basis, maintenance access, shipped-loose item lists, and the vendor document register itself. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (mechanical-packages organization paragraph) |
| R-3 | Submitted vendor documents shall be consistent with the `PKG-018` package identity: equipment tag `26020-02-30-009`, MV VFD - 5000HP, 4160V, 3φ, 60 Hz, 4160V VFD, WBS `02`, Electrical discipline. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| R-4 | The submitted documentation shall reflect the medium-voltage service basis (4,160 V, 3φ, 3-wire, 60 Hz LRG) and the AC inverter-drive motor range (250 hp to 5,500 hp). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Medium-voltage service row) |
| R-5 | Where the driven-equipment basis is the 5,200 hp / 3,878 kW, 4,000 V, 3φ, 60 Hz NEMA MG1 inverter-duty inlet compressor motor and a starting VFD is required under SCA-001 VE #34, vendor documentation shall identify driven-equipment electrical interface assumptions and SCA traceability. CONFLICT: package title says "5000HP, 4160V" but source body says 5,200 hp / 4,000 V — surfaced in `Guidance.md` Conflict Table. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electric Driver and Starting Basis; Electric-Drive Compression Basis) |
| R-6 | Vendor documentation shall address harmonic and reactive-power mitigation context: SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present; final mitigation is set by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| R-7 | Vendor documentation shall reflect site environmental conditions: -40 °C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process/vendor condition applies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (site basis paragraph) |
| R-8 | Each registered vendor document shall have provenance to its source-required basis (where a source row exists), recorded as evidence in the document register. | `DELIVERABLE_REGISTER.csv` Notes column ("individual source document rows remain artifacts/evidence") |
| R-9 | The submitted documentation set shall support the package interface types: Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. | `PACKAGE_REGISTER.csv` row `PKG-018` (Applicable interface types) |
| R-10 | Turnover records shall demonstrate handoff of the documentation set to the EPC Integrator for `DEL-018-06` review/acceptance. | `DELIVERABLE_REGISTER.csv` rows `DEL-018-05` and `DEL-018-06` |
| R-11 | ASSUMPTION: Document numbering, revision control, and submittal-status conventions follow `PKG-018/26020-Package_Requirements.docx`. Exact clause-level requirements are TBD pending access to that source slice. | `_REFERENCES.md` Missing/Deferred; package folder contains `26020-Package_Requirements.docx` (not extracted) — `location TBD` |

## Standards

| Standard / Authority | Applicability | Source |
|---|---|---|
| NEMA MG1 | Driven motor compliance (context for the VFD package, drives whose docs the VFD turnover must align with). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electric Driver and Starting Basis) |
| SCA-001 VE #34 | Establishes starting VFD requirement for KM-2150/KM-2250. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| SCA-001 VE #37 | Removes capacitor banks from MCC-8200 synchronous bus where VFDs are present. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| `26020-Package_Requirements.docx` | Governing project package-requirements document; clause locations TBD (file present at package root; no slice accessible in this run). | `PKG-018/26020-Package_Requirements.docx` (`location TBD`) |
| Other industry standards (e.g., IEEE 519 for harmonics; IEC/CSA enclosure standards) | ASSUMPTION: likely applicable to an MV VFD vendor documentation set, but not enumerated in accessible source slices for `PKG-018`. | ASSUMPTION |

## Verification

| Req | Verification approach |
|---|---|
| R-1 | Confirm a single Package Vendor turnover dossier exists with register + submittals + turnover record. |
| R-2 | Audit the vendor document register against the source's enumerated package-document classes. |
| R-3 | Check each submitted document header against `PKG-018` identity (tag, voltage, frequency, phases, hp, WBS, discipline). |
| R-4 | Confirm electrical scope documents cite the 4,160 V LRG basis and the 250–5,500 hp inverter-drive motor envelope. |
| R-5 | Confirm vendor docs identify driven-equipment electrical interface assumptions and SCA-001 VE #34 traceability; flag for HRR resolution of the 5,000 vs 5,200 hp / 4,160 V vs 4,000 V mismatch. |
| R-6 | Confirm capacitor-bank/harmonic mitigation narrative is present and consistent with SCA-001 VE #37. |
| R-7 | Confirm environmental design statements include -40 °C minimum ambient. |
| R-8 | Spot-check register entries against source row provenance; entries lacking source rows marked accordingly. |
| R-9 | Confirm interface-type coverage in the register (drawings, datasheets, tie-in lists). |
| R-10 | Confirm turnover record (signed/acknowledged) exists and references `DEL-018-06` handoff. |
| R-11 | Resolve when `26020-Package_Requirements.docx` slice is accessible; compare submittal conventions. |

## Documentation

Required artifacts produced by this deliverable:

- Vendor document register (indexed list of all vendor documents for `PKG-018`).
- Vendor document submittals (controlled set, revisioned).
- Source vendor document rows carried as artifact evidence where available.
- Turnover records (handoff to EPC Integrator).

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-018-05`.
