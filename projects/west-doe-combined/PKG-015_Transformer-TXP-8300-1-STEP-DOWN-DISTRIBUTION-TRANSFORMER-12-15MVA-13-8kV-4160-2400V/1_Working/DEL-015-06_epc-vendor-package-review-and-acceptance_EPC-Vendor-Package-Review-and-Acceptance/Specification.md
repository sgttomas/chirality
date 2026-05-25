# Specification — DEL-015-06 EPC Vendor Package Review and Acceptance

## Scope

This specification defines the EPC Integrator's review and acceptance work for the PKG-015 vendor-engineered step-down distribution transformer package (Transformer TXP-8300-1, nameplated 12/15MVA, 13.8kV/4160/2400V). Deliverable scope includes vendor document review, integration acceptance against EPC basis documents, and handoff readiness against the EPC Scope of Work (DEL-015-01), Package Datasheet (DEL-015-02), and Construction Work Package (DEL-015-03). [Source: DELIVERABLE_REGISTER.csv row DEL-015-06; `_CONTEXT.md`]

Excluded: original generation of the Package Vendor's engineered equipment package (covered by DEL-015-04) and the vendor document turnover content itself (covered by DEL-015-05). EPC review of those artifacts is in scope; their authorship is not. [Source: DELIVERABLE_REGISTER.csv rows DEL-015-04, DEL-015-05]

## Requirements

| ReqID | Requirement | Source / Basis |
|---|---|---|
| REQ-015-06-01 | A vendor document review log shall be maintained for PKG-015, recording each vendor-submitted document, revision, reviewer disposition, and resolution status. | `_CONTEXT.md` anticipated artifact; DELIVERABLE_REGISTER.csv row DEL-015-06 |
| REQ-015-06-02 | A package acceptance checklist shall be produced and signed-off, traceable to the EPC SOW (DEL-015-01), Package Datasheet (DEL-015-02), and Construction Work Package (DEL-015-03). | DELIVERABLE_REGISTER.csv rows DEL-015-01/02/03/06 |
| REQ-015-06-03 | Test and inspection evidence shall be collected and retained for the vendor-furnished transformer package (including factory acceptance, on-site electrical inspection, insulation/dielectric, and grounding/bonding records). Specific test list governed by the EPC SoW / Package Datasheet — clause-level basis `location TBD`. | `_CONTEXT.md` anticipated artifact; ASSUMPTION for test categories |
| REQ-015-06-04 | Turnover evidence shall be assembled covering vendor document turnover (DEL-015-05) completeness and integration acceptance under DEL-015-03. | DELIVERABLE_REGISTER.csv rows DEL-015-03 and DEL-015-05; `_CONTEXT.md` |
| REQ-015-06-05 | Integration interfaces shall be verified against the package's seven declared interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Each interface shall have an explicit disposition in the acceptance checklist. | INTERFACE_REGISTER.csv (7 rows for PKG-015); PACKAGE_REGISTER.csv row PKG-015 |
| REQ-015-06-06 | Vendor transformer primary connection shall be verified consistent with the facility 13.8 kV, 3 phase, 3 wire, 60 Hz LRG service feeding 03-25 from the 04-25 main switchgear. | DBM 3-25, lines 732, 740 |
| REQ-015-06-07 | Vendor transformer secondary at the 4160V class shall be verified consistent with the facility 4,160 V, 3 phase, 3 wire, 60 Hz LRG service and the documented 4160V MCC feed (DBM "13.8 kV to 4.16 kV, 12 MVA transformer" line). | DBM 3-25, lines 733, 744 |
| REQ-015-06-08 | The 2400 V tap identified in the package name shall be reconciled against the EPC SoW and Package Datasheet, since the accessible DBM source slice does not describe a 2400 V service or load. Reconciliation outcome shall be recorded; until then this acceptance criterion remains `TBD`. | CONFLICT (Guidance HRR-015-06-001); DBM 3-25 line 733 (no 2400 V service in MV table) |
| REQ-015-06-09 | MVA rating reconciliation: the package name indicates 12/15 MVA (ONAN/ONAF or equivalent dual rating implied), while the DBM cites a single 12 MVA value for the 13.8 kV / 4.16 kV transformer. Vendor rating basis shall be confirmed against the EPC SoW and Package Datasheet; recorded as `TBD` until reconciled. | CONFLICT (Guidance HRR-015-06-002); DBM 3-25 line 744 |
| REQ-015-06-10 | Vendor transformer and accessories subject to outdoor or exposed installation shall be verified for the project low-temperature basis: -40 deg C minimum to +35 deg C maximum ambient; -40 deg C governs exposed equipment unless a more severe condition applies. | DBM 3-25, lines 96, 100-101, 145, 686 |
| REQ-015-06-11 | Cable separation and routing for primary, secondary, and control/instrument cabling shall be verified against the project separation requirement that power circuits at 13.8 kV, 4,160 V, and 600 V be separated from control and instrument circuits by distance, shielding, or routing. | DBM 3-25, line 768 |
| REQ-015-06-12 | Grounding/bonding interface acceptance shall verify the vendor design meets project electrical specifications and the declared Grounding / Bonding interface. Specific clause basis `location TBD` from accessible sources. | INTERFACE_REGISTER.csv row PKG-015 Grounding / Bonding; ASSUMPTION for clause source |
| REQ-015-06-13 | Acceptance shall not be issued before the EPC-side basis deliverables (DEL-015-01, DEL-015-02, DEL-015-03) reach a state permitting reliance. Specific maturity gate: `TBD` (no explicit gate stated in source). Default maturity threshold per `_DEPENDENCIES.md` is `INITIALIZED`. | ASSUMPTION; `_DEPENDENCIES.md` default maturity threshold |

## Standards

| Standard / Reference | Applicability | Source |
|---|---|---|
| Project electrical specifications and detailed design | Govern transformer installation, cable separation, grounding, and bonding compliance. | DBM 3-25, line 768 |
| CEC and area classification standards | Govern electrical safety, classification, and clearance verification of installed package. | ASSUMPTION (typical for Canadian process facility electrical work); clause `location TBD` from accessible sources |
| IEEE / CSA transformer standards (e.g., IEEE C57 series, CSA C88) | Likely applicable to transformer rating, testing, and acceptance criteria. | ASSUMPTION: standards are not cited in accessible DBM slice; clause `location TBD` |
| Voltage / grounding basis (DBM 3-25) | Governs vendor electrical compatibility checks at 13.8 kV LRG primary and 4,160 V LRG secondary. | DBM 3-25, lines 732, 733 |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-015-06-01 | Inspection of the review log for completeness against the vendor document register (DEL-015-05). |
| REQ-015-06-02 | Traceability audit of acceptance checklist rows to DEL-015-01/02/03 entries. |
| REQ-015-06-03 | Examination of FAT, SAT, on-site inspection, dielectric, and grounding/bonding records. |
| REQ-015-06-04 | Turnover dossier completeness review against DEL-015-05 register and DEL-015-03 turnover gates. |
| REQ-015-06-05 | Interface-by-interface verification against the seven INTERFACE_REGISTER.csv rows for PKG-015. |
| REQ-015-06-06 | Document review: vendor primary nameplate and protection coordination consistent with 13.8 kV LRG service. |
| REQ-015-06-07 | Document review: vendor secondary at 4160V class consistent with facility 4,160 V LRG service and feed to 4160V MCC. |
| REQ-015-06-08 | Reconciliation review and human ruling on the 2400 V tap. |
| REQ-015-06-09 | Reconciliation review and human ruling on the 12/15 MVA rating. |
| REQ-015-06-10 | Vendor environmental ratings review against -40 deg C minimum / +35 deg C maximum ambient. |
| REQ-015-06-11 | Cable schedule and tray/conduit layout review for power-vs-control separation. |
| REQ-015-06-12 | Grounding/bonding drawing and test record review. |
| REQ-015-06-13 | Status check of upstream EPC deliverables before acceptance issuance. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log (PKG-015 entries with revision and disposition history).
- Package acceptance checklist (signed, organized by basis deliverable and by declared interface).
- Test/inspection evidence file (FAT/SAT, dielectric, grounding/bonding, on-site inspection).
- Turnover evidence file (mechanical-complete, energization-readiness, handover-to-operations as defined by DEL-015-03).

Supporting working records (recommended; ASSUMPTION):

- Review meeting minutes for PKG-015 vendor reviews.
- Non-conformance / open-item log with disposition (including the 2400 V tap and 12/15 MVA reconciliations).
- Cross-reference matrix linking vendor documents to acceptance criteria and to declared interfaces.
