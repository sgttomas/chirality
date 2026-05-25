# Guidance: DEL-023-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists to consolidate the Package Vendor's documentation deliverables for `PKG-023` (MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD) into a single register-plus-submittals-plus-turnover-records set that the EPC Integrator can review for integration sufficiency and that downstream construction/turnover activities can rely on. It is the documentation companion to the vendor's engineered-equipment deliverable (`DEL-023-04`) and the input to EPC vendor-package review/acceptance (`DEL-023-06`).

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat vendor documentation as vendor-authored evidence; the EPC role is interface/integration review, not authorship.
- Treat the vendor document register itself as `TBD`-content for now: `ARTIFACT_REGISTER.csv` row `ART-950E899C01` explicitly labels the vendor document register as "Vendor Documentation Gap Evidence" because detailed vendor-document requirements are not present in the current source material for this package.
- Keep the turnover deliverable distinct from the vendor equipment package deliverable (`DEL-023-04`) and from EPC review/acceptance evidence (`DEL-023-06`).
- Use DBM electrical basis only at the level it supports for MV VFDs: 4.16 kV voltage service basis, electrical-building eligibility, plant-PLC integration convention for MV MCC equipment (ASSUMPTION for MV VFD applicability), and Zone 2 marking/temperature-code requirements for VFD-fed motors.

## Considerations

The DBM electrical design basis treats 4.16 kV, 3-phase, 3-wire, 60 Hz, low-resistance-grounded service as the medium-voltage service for AC inverter-drive motors rated 250 hp up to 5,500 hp; the PKG-023 1500 HP / 4160 V MV VFD package falls inside that voltage-class envelope. DBM also states that medium-voltage VFDs may be housed in prefabricated electrical buildings and that 4.16 kV motor starting (VFD and soft-starter requirements) is "TBD" at the DBM level. This means the vendor documentation should resolve, in the vendor's own documents, the package-specific drive topology, starting method, line/load filtering, harmonics, cooling, and protection that DBM leaves open.

The DBM electrical section requires MV MCC equipment to provide an Ethernet communication port to the plant PLC central control panel. Whether the analogous MV VFD package is required to provide a PLC Ethernet integration as part of its documented control architecture is not explicitly stated for VFD packages in the accessible DBM slice and is treated as an ASSUMPTION; the vendor documentation should still include control/communication architecture evidence consistent with this integration pattern.

For VFD-fed motors in Zone 2 areas, DBM requires marking and a temperature code lower than the area-classification value. The area classification of PKG-023 is not stated in the accessible source set. The vendor documentation should accommodate this requirement once the package area classification is determined.

Because no accessible package-specific source slice defines the required vendor document index, transmittal/document-control numbering, or turnover record list, the deliverable should be structured to receive that content rather than to invent it. Conservative best practice is to define the register, transmittal log, and turnover record placeholders in this deliverable and have the vendor populate them under EPC document-control review.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Vendor document index content | Leave detailed register rows `TBD` and structure the deliverable to receive them. | `ARTIFACT_REGISTER.csv` row `ART-950E899C01` explicitly flags the register content as gap evidence. |
| Submittal numbering / document control convention | Treat as a project document-control inheritance; do not invent a numbering scheme. | No accessible project document-control procedure was located. |
| Turnover record list | Leave the specific list of turnover artifacts (FAT, SAT, mill certs, calibration, drive tuning, IOM, spares, as-builts) `TBD`. | No source-confirmed list for this package. |
| MV VFD PLC integration | Treat the plant-PLC Ethernet integration pattern as an ASSUMPTION for MV VFDs (DBM states it for MV MCC equipment explicitly). | Avoids overstating DBM beyond its accessible text. |
| Area classification | Treat as `TBD`; surface as a precondition to resolving Zone 2 marking and T-code requirements. | DBM requires marking when classified; PKG-023 area classification is not in the accessible source set. |

## Examples

- Acceptable register entry: "Vendor general arrangement drawing - TBD vendor doc number - Rev. 0 - submitted YYYY-MM-DD - EPC disposition: pending. Source: vendor submittal." (placeholder structure; rows themselves remain TBD).
- Acceptable source-gap entry: "Turnover record list: TBD. No package-specific list available in `_Sources/`."
- Not acceptable without new source: "Vendor shall submit the following 27 documents: ..." invented from convention without source.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-023-05-001 | The vendor document register for PKG-023 has no source-defined content; the Gate 7 artifact register explicitly flags this as a gap, but the deliverable is still required to "carry" a vendor document register. | `ARTIFACT_REGISTER.csv` row `ART-950E899C01` (Vendor Documentation Gap Evidence) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-023-05_vendor-document-turnover-package` | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Carry the deliverable as a register-shell + TBD content. Defer detailed register rows until either the vendor's package documentation list or a project document-control standard is accepted as source. | TBD |
| HRR-023-05-002 | DBM requires MV MCC equipment to expose an Ethernet communication port to the plant PLC; whether the same integration convention is required of MV VFD packages is not explicitly stated for VFDs in the accessible DBM slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV / 4.16 kV MCC paragraphs | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD paragraphs (no explicit PLC-comm statement for MV VFDs) | Datasheet Conditions; Specification REQ-023-05-008; Guidance Considerations | Treat MV VFD plant-PLC Ethernet integration as ASSUMPTION until DBM or project I&C standard is confirmed; vendor documentation should include control/communication architecture evidence. | TBD |
| HRR-023-05-003 | Area classification of PKG-023 is not stated in the accessible source set; DBM requires Zone-2 marking and temperature-code-lower-than-classification for VFD-fed motors when classified. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD/area-classification paragraph | Project area-classification drawing / fugitive-emissions study (not accessible) | Datasheet Conditions; Specification REQ-023-05-009 | Mark area classification as `TBD`; require vendor documentation to include marking/T-code evidence appropriate to the resolved classification. | TBD |
