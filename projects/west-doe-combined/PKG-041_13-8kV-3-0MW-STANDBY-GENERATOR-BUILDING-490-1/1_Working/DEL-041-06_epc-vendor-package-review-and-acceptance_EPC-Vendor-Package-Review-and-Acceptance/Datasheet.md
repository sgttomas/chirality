# Datasheet — DEL-041-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-041-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row `DEL-041-06` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-041` | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` |
| PackageName | 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` |
| Workbook Row | Packages row 43 | GATE-07 `DELIVERABLE_REGISTER.csv` Source column |
| WBS | 01 | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` |
| CoA tracking number | 26020-01-30-032 | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` |
| Discipline | Electrical | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` |
| Type | EPC Vendor Package Acceptance | GATE-07 `DELIVERABLE_REGISTER.csv` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` |
| CoversScopeItems | `SOW-0042` | GATE-07 `SCOPE_LEDGER.csv` row `SOW-0042` |
| SupportsObjectives (PACKAGE_HEURISTIC, ASSUMPTION) | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md` (package-grouped objective heuristic) |
| Status (at draft) | OPEN -> INITIALIZED (after this run) | `_STATUS.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable purpose | Vendor package review, integration acceptance, and handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | GATE-07 `DELIVERABLE_REGISTER.csv` row `DEL-041-06` |
| Acceptance basis (upstream artifacts) | `DEL-041-01_scope-of-work` (EPC Scope of Work); `DEL-041-02_package-datasheet` (EPC Package Datasheet); `DEL-041-03_construction-work-package` (EPC Construction Work Package); `DEL-041-04_vendor-engineered-equipment-package`; `DEL-041-05_vendor-document-turnover-package`. | GATE-07 `DELIVERABLE_REGISTER.csv`; GATE-07 `SCOPE_LEDGER.csv` row `SOW-0042` |
| Registered artifacts produced | `ART-9E33107762` Vendor document review and comment log; `ART-0E8BDED2A8` Vendor package acceptance and turnover checklist; `ART-53AD41FE27` Factory/shop test and inspection evidence | GATE-07 `ARTIFACT_REGISTER.csv` rows for `DEL-041-06` |
| Anticipated artifacts (free-text) | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` |
| Applicable interface types (acceptance scope) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | GATE-07 `INTERFACE_REGISTER.csv` rows `IFC-508C53EB72`, `IFC-1528C860A4`, `IFC-004BB1B385`, `IFC-134CB10F1D`, `IFC-8E23F09E7C`, `IFC-1E6785E532`, `IFC-FEEE41EDAA`, `IFC-7D36256CF5`, `IFC-5F7FE5FA2A`, `IFC-57828C08C8`, `IFC-B9452850B5`, `IFC-D0146B1F8C` |
| Package responsibility split | Package Vendor: package engineering, package design, vendor documentation, physical equipment package. EPC Integrator: integration into the functional process facility, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` |
| Coordination mode | DECLARED; no declared upstream/downstream edges at PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Nominal package title (per workbook) | 13.8kV, 3.0MW standby generator building (490-1) | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` (Workbook Packages row 43) |
| Facility emergency-power basis (current DBM) | LV (low-voltage) standby natural-gas generators on the LV MCC with transfer switch; 13.8 kV / 3 MW emergency-generator concept explicitly superseded. Generator count, rating, voltage allocation, and critical-load list remain TBD. | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 505; line 762 |
| Facility emergency-power architecture | TOU-typical low-voltage standby generator set with automatic transfer switch; vendor-supplied weather-protective outdoor enclosure; 1 m access walkway; overhead lift provisions per MLE confirmation; serves 04-25 and 03-25 critical loads. | DBM-Deepcut `4-25_Deepcut_DBM.md` lines 2074-2080 |
| Generator fuel basis | Less than 66 psig fuel-gas supply during normal operation for general-purpose classification; emergency-generator fuel-gas design flow 0.468 MMSCFD (13.2 e3m3/d); start-gas flow 3.6 MMSCFD for 30 seconds (TBC during detailed engineering); local fuel-gas particulate filter at the emergency generator. | DBM-Deepcut `4-25_Deepcut_DBM.md` lines 1848, 1866, 1870 |
| Open generator parameters | Make / model / rating, LV switchgear assignment, transfer switch configuration, fuel selection, battery/charger sizing, diesel storage (if selected), generator count are open. | DBM-Deepcut `4-25_Deepcut_DBM.md` line 1836; line 175 ("Standby generator count: TBD where the current basis supersedes a natural gas emergency generator with TOU standby generators on LV MCC with transfer switch.") |
| Approval-for-reliance authority | Human only (no agent approval). | Project governing invariant `K-AUTH-1` |
| Acceptance prerequisite states | `DEL-041-01`..`DEL-041-05` content available and stable; vendor submittals available. | TBD; no formal maturity threshold declared in `_DEPENDENCIES.md` beyond default INITIALIZED |
| Required acceptance-criteria source slices | Source-supported acceptance criteria for the standby-generator package (FAT, integration interfaces, turnover). | TBD; no package-specific acceptance criteria text found in accessible sources |

## Construction

| Construction element | Value | Source |
|---|---|---|
| Document form | Markdown deliverable folder with four-document kit plus registered evidence artifacts | `_CONTEXT.md`; `_REFERENCES.md` |
| Evidence artifacts to be assembled | Vendor document review and comment log (`ART-9E33107762`); vendor package acceptance and turnover checklist (`ART-0E8BDED2A8`); factory/shop test and inspection evidence (`ART-53AD41FE27`) | GATE-07 `ARTIFACT_REGISTER.csv` rows for `DEL-041-06` |
| Acceptance scope coverage | All twelve applicable PKG-041 interface types (see Attributes) must be covered by acceptance evidence. | GATE-07 `INTERFACE_REGISTER.csv` rows for `PKG-041` |
| Storage location | `<deliverable folder>/` and `<deliverable folder>/2_Evidence/` (ASSUMPTION: evidence subfolder convention; not yet created) | ASSUMPTION |
| Lifecycle gate | Acceptance documents are reviewed/approved by humans; agents propose, humans decide. | Governing invariant `K-AUTH-1` |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- GATE-07 snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (row `DEL-041-06`)
  - `PACKAGE_REGISTER.csv` (row `PKG-041`)
  - `ARTIFACT_REGISTER.csv` (rows `ART-9E33107762`, `ART-0E8BDED2A8`, `ART-53AD41FE27`)
  - `INTERFACE_REGISTER.csv` (12 rows for `PKG-041`)
  - `SCOPE_LEDGER.csv` (row `SOW-0042`)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 505, 762)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (lines 175, 1836, 1848, 1866, 1870, 2074-2080)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — not parsed in this run (binary; no package-specific slice extracted; `location TBD`)

## Missing / TBD

- `TBD`: source-specific acceptance criteria (factory/shop test, integration test) for the standby-generator package; not found in accessible source slices.
- `TBD`: vendor document register baseline for PKG-041 (from `DEL-041-05`).
- `TBD`: explicit prerequisite maturity for upstream EPC deliverables required to start acceptance.
- `CONFLICT`: Workbook package title ("13.8kV, 3.0MW STANDBY GENERATOR BUILDING") describes a 13.8 kV / 3 MW emergency-generator concept that both DBM-Comp_and_Liquids (line 505) and DBM-Deepcut (line 175) explicitly supersede with an LV (low-voltage) standby-generator architecture on the LV MCC with transfer switch. See `Guidance.md` Conflict Table `CONF-041-06-001`.
