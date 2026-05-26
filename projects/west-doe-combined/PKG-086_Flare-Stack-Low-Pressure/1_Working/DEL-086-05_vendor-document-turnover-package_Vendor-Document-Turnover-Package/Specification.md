# Specification: DEL-086-05_vendor-document-turnover-package — Vendor Document Turnover Package

> Normative requirements for the Package Vendor's document deliverables and turnover for PKG-086 (Flare Stack — Low Pressure). Requirements are grounded in the Gate 7 PROJECT_DECOMP snapshot, the locally accessible 4-25 Deepcut DBM, and the deliverable's `_CONTEXT.md`. Items not yet anchorable to a copied source slice are labeled `ASSUMPTION` or `TBD`.

## Scope

In scope:
- The vendor document register, document submittals, source-required vendor documentation, and turnover records for the PKG-086 LP flare stack package (`_CONTEXT.md` Scope).
- EPC Integrator interface/integration review of the vendor document set (`DELIVERABLE_REGISTER.csv` ResponsibleParty).
- Document coverage for the equipment defined in `SCOPE_LEDGER.csv` SOW-0093: LP flare stack, air-assist blower, pilot, pilot proving, auto-ignition, supplemental fuel gas/dilution gas provisions, stack interface details.

Out of scope:
- Authorship of the EPC Scope of Work (DEL-086-01), Package Datasheet (DEL-086-02), Construction Work Package (DEL-086-03), Vendor Engineered Equipment Package physical design (DEL-086-04), and EPC review/acceptance authorship (DEL-086-06).
- Stand-alone treatment of individual source-required vendor document rows as separate deliverables (`DELIVERABLE_REGISTER.csv` Notes: rows remain artifacts/evidence, not separate deliverables).

## Requirements

| Req ID | Requirement | Basis / Source |
|---|---|---|
| R-086-05-01 | The Package Vendor shall produce and maintain a vendor document register that uniquely indexes every vendor-issued document for PKG-086 and records its revision state. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on register structure (`location TBD` in 26020 heading 39) |
| R-086-05-02 | The vendor document set shall include all documentation explicitly required by the source basis (26020-Package_Requirements.docx package heading 39) for PKG-086. The explicit list is `TBD` until the source slice is copied locally. | `_REFERENCES.md`; source slice `location TBD` |
| R-086-05-03 | The vendor document set shall cover, at minimum, the equipment scope in SOW-0093: LP flare stack, air-assist blower, pilot, pilot proving, auto-ignition, supplemental fuel gas/dilution gas provisions, and stack interface details. | `SCOPE_LEDGER.csv` SOW-0093 |
| R-086-05-04 | Vendor documentation shall record materials of construction for the LP flare stack consistent with the design-basis material (SA-106), and material certifications (MTRs) shall be included in the turnover record. | `4-25_Deepcut_DBM.md` LP flare materials table (line 2042); ASSUMPTION on MTR inclusion |
| R-086-05-05 | Vendor calculations shall demonstrate compliance with the thermal-radiation flux limits in the DBM: <=9 kW/m2 inside the flare blackened-area boundary and <=5 kW/m2 outside the boundary, per OGPFR Appendix 1, Schedule 1, Sec. 2. The DBM notes OGPFR is an external regulatory reference; vendor calculations shall verify against the governing regulation. | `4-25_Deepcut_DBM.md` lines 285-289 |
| R-086-05-06 | Vendor documentation shall be consistent with the spacing requirements applied at the facility per OGAOM Sec. 9.6.15 (e.g., 25 m to nearest plant equipment, 80 m to public road or property line) so that vendor stack height, radiation, and dispersion calculations are reconcilable with the facility plot. | `4-25_Deepcut_DBM.md` lines 280-287 |
| R-086-05-07 | Vendor documentation shall identify supplemental fuel gas provisions consistent with the DBM requirement that any blended gas to a flare have LHV >=20 MJ/Sm3, and shall describe air-assist (smokeless) capacity targeted to Ringelmann 1 at approximately 5% (TBC) of the emergency design case flare loads. | `4-25_Deepcut_DBM.md` lines 2031-2033 |
| R-086-05-08 | Vendor submittals shall include LP flare pilot and purge gas type and source identification. The DBM lists "LP flare stack pilot and purge gas: TBC" — vendor documentation shall close this `TBC`. | `4-25_Deepcut_DBM.md` line 1892 |
| R-086-05-09 | The vendor document register and submittal workflow shall accommodate EPC Integrator interface/integration review prior to acceptance and turnover. Review evidence is consumed by DEL-086-06. | `DELIVERABLE_REGISTER.csv` ResponsibleParty; DEL-086-06 description |
| R-086-05-10 | Turnover records shall evidence transmittal of the complete vendor document set to the EPC Integrator and the end client, including revision state at handover and outstanding hold items. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on hold-item field (`location TBD`) |
| R-086-05-11 | Sour-service applicability of vendor documentation (material selection statements, NACE conformance, certification scope) shall be addressed where the PKG-086 service is sour. Definitive sour-service designation for PKG-086 is `ASSUMPTION: likely applies` pending source confirmation. | OBJ-009 (`OBJECTIVE_REGISTER.csv`); source clause `location TBD` |
| R-086-05-12 | Vendor documents shall preserve provenance: each vendor-issued document shall record vendor identity, document number, revision, date, and the EPC contract/package reference. | ASSUMPTION (standard project documentation hygiene); `location TBD` |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| OGAOM Sec. 9.6.15 | Flare spacing requirements driving vendor radiation/dispersion calculations | `4-25_Deepcut_DBM.md` line 280; standard text `location TBD` |
| OGPFR Appendix 1, Schedule 1, Sec. 2 | Thermal-radiation flux limits at flare boundaries | `4-25_Deepcut_DBM.md` lines 285-289; standard text `location TBD` |
| API 2510 | Spacing between flare and pressurized bullets | `4-25_Deepcut_DBM.md` line 284; standard text `location TBD` |
| NACE MR0175 / ISO 15156 | Sour-service materials selection (where applicable) | ASSUMPTION via OBJ-009; standard text `location TBD` |
| 26020-Package_Requirements.docx package heading 39 | Project-specific vendor document content requirements | `_REFERENCES.md`; source slice `location TBD` |
| Facility document-numbering / turnover convention | Document register format, transmittal protocol | TBD — `location TBD` |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-086-05-01 | Inspection of the vendor document register against the Package Vendor's contracted document list; completeness check by EPC Integrator. |
| R-086-05-02 | Cross-check of vendor submittals against the source-required list extracted from 26020 heading 39 (verification pending source slice copy). |
| R-086-05-03 | Mapping of submittals to SOW-0093 equipment items in the EPC review log (DEL-086-06). |
| R-086-05-04 | Inspection of MTRs and material statements against the SA-106 basis. |
| R-086-05-05 | Review of vendor radiation calculations against DBM kW/m2 limits; cross-check against the governing regulation. |
| R-086-05-06 | Reconciliation of vendor stack/radiation calculations against the facility plot plan spacing applied per the DBM table. |
| R-086-05-07 | Review of supplemental fuel gas and air-assist blower sizing documents; verification of LHV and Ringelmann basis. |
| R-086-05-08 | Review of pilot and purge gas datasheet/PFD vendor submittal; confirmation that the DBM `TBC` is closed. |
| R-086-05-09 | EPC Integrator review log (DEL-086-06) recording status of every vendor document. |
| R-086-05-10 | Inspection of signed turnover transmittals and revision-at-handover record. |
| R-086-05-11 | Review of vendor material/sour-service statements against confirmed sour-service designation. |
| R-086-05-12 | Inspection of metadata fields on each vendor document. |

## Documentation

Required deliverable artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document register (master index)
- Vendor document submittals (full set)
- Source-required vendor documentation (per 26020 heading 39 — `location TBD`)
- Turnover records (transmittals, revision-at-handover record, outstanding items log)

Linked artifacts produced by sibling deliverables and consumed here as inputs/outputs:
- EPC Scope of Work (DEL-086-01) — defines vendor responsibility scope
- Package Datasheet (DEL-086-02) — defines vendor technical handoff content
- EPC Vendor Package Review and Acceptance (DEL-086-06) — consumes vendor document set
