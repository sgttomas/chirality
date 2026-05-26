# Specification — DEL-078-06: EPC Vendor Package Review and Acceptance

## Scope

This Specification governs the EPC Integrator's review and acceptance of the Pig Receivers (Inlet) 4-25 vendor package, leading to integration acceptance and handoff readiness for downstream construction, commissioning, and turnover.

In scope:
- Verification that the vendor-engineered equipment package (DEL-078-04) and the vendor document turnover package (DEL-078-05) conform to the EPC Scope of Work (DEL-078-01), Package Datasheet (DEL-078-02), and Construction Work Package (DEL-078-03).
- Production of: vendor document review log, package acceptance checklist, test/inspection evidence package, and turnover evidence package.
- Surfacing interface, integration, and source-conflict items to the EPC Integrator for ruling.

Out of scope:
- Originating equipment design (owned by Package Vendor under DEL-078-04).
- Originating vendor documentation (owned by Package Vendor under DEL-078-05).
- Construction execution (owned under DEL-078-03).
- Changing the Package Datasheet (DEL-078-02) or SOW (DEL-078-01).

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows DEL-078-01 through DEL-078-06.

## Requirements

### R1 — Acceptance Basis Anchored to EPC Triad

R1.1 The vendor package review SHALL be performed against the accepted-version EPC Scope of Work (DEL-078-01), Package Datasheet (DEL-078-02), and Construction Work Package (DEL-078-03). [Source: `_CONTEXT.md` Scope.]

R1.2 The review SHALL identify and record any deviation between vendor deliverables and the EPC triad. (ASSUMPTION on review structure; deliverable form derives from the four anticipated artifacts in `_CONTEXT.md`.)

### R2 — Vendor Document Review Log

R2.1 A document-by-document review log SHALL be produced covering all entries on the vendor document register provided by DEL-078-05. [Source: `_CONTEXT.md` Anticipated Artifacts.]

R2.2 Each entry SHALL record at minimum: vendor document number, revision, EPC reviewer, review code (e.g., Code 1/2/3 — exact coding TBD until owner standard confirmed), review date, disposition, and reference to the comment-disposition record.

R2.3 The review log SHALL be retained as turnover evidence.

### R3 — Package Acceptance Checklist

R3.1 A package acceptance checklist SHALL be produced and SHALL trace acceptance evidence to each requirement of the Package Datasheet (DEL-078-02) and to each scope element of the SOW (DEL-078-01). [Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` rows DEL-078-01/02.]

R3.2 The checklist SHALL cover, at minimum, the following technical items derived from accessible DBM source [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pig Receiving]:
- Inlet pipeline OD of 610 mm (24 in.) at the pig receiver interface.
- Skid-mounted upstream isolation valves or ESDVs are full port for pigging.
- Barred tees are installed to prevent pigs entering facility piping.
- LP fuel gas connection for sweet-gas purge of pig receiver before opening.
- Pig receiver vent connection to HP flare system.
- Full-port piggable ESDV with position transmitters on the inlet skid.
- Design pressure consistent with upstream inlet pipeline MAWP (and 1,360 psig downstream of inlet separator inlet PCV — verify pig receiver design pressure aligns with the upstream side).

R3.3 The checklist SHALL record the equipment population accepted, including tag IDs. The current roster basis is `PR-1010-1`, `PR-1020-1`, `PR-1030-1` (3 units) per package line-item row 61; the DBM body narrates one 24" pig receiver. CONFLICT — see `Guidance.md`. Accepted population SHALL reflect human ruling.

### R4 — Test, Inspection, and FAT Evidence

R4.1 The acceptance package SHALL include evidence of the test/inspection program executed by the vendor and witnessed/reviewed by the EPC Integrator. Required evidence categories SHALL include at minimum:
- Hydrostatic / pneumatic pressure test records — TBD specific basis (vendor procedure + owner standard).
- NDE records (RT/UT/MT/PT as required by the governing fabrication code) — TBD which apply; ASSUMPTION ASME B31.3 is the governing piping code pending confirmation.
- Material certifications (CMTRs) for pressure-retaining components.
- PMI records where alloy verification is required — TBD applicability.
- Welding documentation (WPS/PQR/WPQ records).
- FAT report including functional checks of pig handling, kicker line, closure mechanism, interlocks (where applicable), and instrumentation loop checks.

R4.2 Each item SHALL be traceable to a vendor-document number and revision on the review log (R2).

### R5 — Turnover Evidence

R5.1 Turnover evidence SHALL include, at minimum:
- Mechanical Completion (MC) checklist / certificate.
- Punch list (A/B/C items per owner taxonomy — exact taxonomy TBD).
- Final vendor data book index and storage location.
- Redline as-built drawings (where applicable at vendor scope boundary).
- Spare-parts list confirmation.
- Lifting and rigging records (where required).
- Handover from EPC Integrator construction to commissioning, with signatures.

R5.2 Turnover evidence SHALL link each item to the package acceptance checklist (R3) and to the vendor document review log (R2).

### R6 — Interface and Integration Acceptance

R6.1 Interface acceptance SHALL confirm:
- Inlet pipeline tie-in geometry, pressure class, and isolation arrangement.
- Vent header tie-in to HP flare (pressure, sizing, slope, drainage to flare KO).
- LP fuel-gas supply connection (pressure, purge volume, isolation).
- Barred-tee transition into downstream facility piping.
- Skid grounding, structural anchorage, and area classification compliance — TBD criteria.

R6.2 Open interface items previously identified in the DBM body SHALL be tracked to closure or escalated as Needs Human Ruling. Reference: "Inlet pipeline final configuration, detailed tie-ins, and any second inlet pipeline pig receiver/isolation requirements are TBD." [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.]

### R7 — Source Fidelity and Provenance

R7.1 Each acceptance entry SHALL cite the source artifact and revision relied upon for acceptance.

R7.2 Where source material is unavailable, the entry SHALL be marked `TBD` with a stated unblock action; acceptance SHALL NOT proceed against unsourced claims.

## Standards

The following standards are likely applicable. Each is recorded with `location TBD` because the source text is not locally accessible as document slices.

| Standard | Likely role | Source / Status |
|---|---|---|
| ASME B31.3 — Process Piping | Governing piping/fabrication code for pig receiver and associated piping (ASSUMPTION) | Not present in accessible source slice; location TBD. |
| ASME BPVC Section VIII Div. 1 or 2 | Pressure-vessel design for the pig receiver barrel (ASSUMPTION) | location TBD. |
| ASME Section IX | Welding qualifications referenced by R4 (ASSUMPTION) | location TBD. |
| NACE MR0175 / ISO 15156 | Sour service materials selection (sour gas service stated in DBM) | DBM identifies sour service; specific standard reference is ASSUMPTION; location TBD. |
| API 6D (or API 1104, ASME B16.34 as applicable) | Closure and isolation valve design (ASSUMPTION) | location TBD. |
| CSA Z662 | Pipeline tie-in code (Canadian jurisdiction, ASSUMPTION) | DBM situates facility in BC; specific CSA Z662 applicability is ASSUMPTION; location TBD. |
| Owner / EPC project specifications | Local supplements (welding, NDE, coatings, area classification, document review codes) | TBD — owner spec set not in accessible slice. |

## Verification

| Requirement | Verification Approach | Verification Evidence |
|---|---|---|
| R1 — Acceptance basis | Document review against DEL-078-01/02/03 | Review log + checklist signed by EPC Integrator |
| R2 — Document review log | 100% coverage check against vendor document register (DEL-078-05) | Review log completeness audit |
| R3 — Package acceptance checklist | Item-by-item walkdown and document verification | Checklist with citations to source documents |
| R4 — Test/inspection | Witness/review of vendor records; spot-check of CMTRs and NDE | Test records, NDE reports, FAT report |
| R5 — Turnover evidence | Verification at handover gate | MC certificate, punch list, vendor data book index |
| R6 — Interfaces | Walkdown vs. P&ID/isometric/area classification drawings | Interface acceptance record |
| R7 — Source fidelity | Audit of citation completeness on each acceptance entry | Cited-source coverage report |

## Documentation

Required outputs:
- `vendor-document-review-log` (CSV or table)
- `package-acceptance-checklist`
- `test-and-inspection-evidence` package (folder of records + index)
- `turnover-evidence` package (MC, punch list, vendor data book index)
- `interface-acceptance-record`
- Acceptance memo (final acceptance summary; references all of the above; signed by EPC Integrator).

[Source: `_CONTEXT.md` Anticipated Artifacts; supplemented by ASSUMPTION on internal structure.]
