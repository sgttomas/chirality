# Procedure — DEL-041-06 EPC Vendor Package Review and Acceptance

## Purpose

Produce the EPC-Integrator-owned vendor package review, integration acceptance, and handoff-readiness evidence for PKG-041 (standby-generator building, per Workbook Packages row 43; LV standby per current DBM), in a form humans can sign and reviewers can audit.

## Prerequisites

| Prerequisite | Source | Status check |
|---|---|---|
| `DEL-041-01_scope-of-work` content exists and is sufficiently stable | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD — check sibling `_STATUS.md` |
| `DEL-041-02_package-datasheet` content exists and is sufficiently stable | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD |
| `DEL-041-03_construction-work-package` content exists | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD |
| `DEL-041-04_vendor-engineered-equipment-package` vendor submittals available | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD |
| `DEL-041-05_vendor-document-turnover-package` document register available | GATE-07 `ARTIFACT_REGISTER.csv` (PKG-041 vendor document register) | TBD |
| Human ruling on `CONF-041-06-001` (workbook title vs. DBM-superseded LV standby architecture) | Guidance Conflict Table | TBD — blocks REQ-041-06-05 closure |
| Facility utility design basis available for integration checks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (lines 175, 1836, 1848, 1866, 1870, 2074-2080); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 505, 762) | OK |
| `_REFERENCES.md`, `_DEPENDENCIES.md`, `_CONTEXT.md` present | This deliverable folder | OK |
| Human reviewer designated for binding acceptance | `K-AUTH-1` | TBD |

## Steps

1. **Confirm acceptance ruler.** Read the latest accepted versions of `DEL-041-01` (Scope of Work), `DEL-041-02` (Package Datasheet), and `DEL-041-03` (Construction Work Package). Record their identifying snapshot/version in the review log header. If any is not yet stable, record as `TBD` and proceed only with the stable subset.
2. **Resolve electrical-architecture baseline.** Request human ruling on `CONF-041-06-001` (workbook 13.8 kV / 3 MW title vs. DBM-superseded LV standby on LV MCC). Until ruled, mark REQ-041-06-05-derived rows as `TBD; blocked by CONF-041-06-001`.
3. **Inventory vendor submittals.** Build the vendor submittal index from `DEL-041-05` (vendor document register, when available; otherwise vendor transmittals). One row per vendor document, with vendor doc number, revision, date, and EPC receipt date.
4. **Author the vendor document review and comment log (`ART-9E33107762`).** For each indexed vendor document, record EPC review comments referencing specific clauses of the EPC Scope of Work / Package Datasheet / Construction Work Package and (where applicable) the DBM utility basis. Each line includes a `disposition` field with allowed values: `accept`, `accept-with-comment`, `revise-and-resubmit`, `reject`, `TBD`. Agents may PROPOSE dispositions; only a human signs them.
5. **Verify interface coverage.** For each of the twelve applicable PKG-041 interface types in GATE-07 `INTERFACE_REGISTER.csv` (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports), associate at least one accepted vendor document or test record. Gaps remain `TBD`.
6. **Author the vendor package acceptance and turnover checklist (`ART-0E8BDED2A8`).** One row per acceptance criterion. Rows derive from: Specification REQ-041-06-01..-10; interface-coverage map from Step 5; facility utility anchors (REQ-041-06-05..-07); open-parameter tracker (REQ-041-06-08). Each row carries: criterion text, evidence pointer, disposition, human signer, date.
7. **Assemble factory/shop test and inspection evidence (`ART-53AD41FE27`).** Collect vendor-supplied factory acceptance test (FAT) reports (engine/generator run, load bank, fuel-system pressure tests), routine test reports, inspection reports, and any third-party witness records. Tabulate by test type with pointer to underlying PDF/file. Items required by standards that are not locally accessible remain `TBD` (see Specification REQ-041-06-11 and Guidance `CONF-041-06-002`).
8. **Track open vendor parameters.** Maintain a parameter tracker for: generator make/model/rating, LV switchgear assignment, transfer switch configuration, fuel selection (natural gas vs. diesel), battery/charger sizing, diesel storage if selected, generator count, overhead lift provision confirmation. Close items only when vendor data is received and reviewed.
9. **Punch and closeout.** Aggregate all `TBD` / `revise-and-resubmit` / `reject` items into a punch list with target closeout dates. Closeout is achieved when every checklist row has a human-signed acceptable disposition or an explicitly accepted carry-forward.
10. **Promote.** When closeout is achieved, propose `_STATUS.md` transition (e.g., to `READY_FOR_REVIEW` or the project-defined accepted state) via the appropriate human-authorized path. Do not transition status automatically.

## Verification

| Verification check | Method | Pass criterion |
|---|---|---|
| Every Specification requirement (REQ-041-06-01..-10) is exercised in the checklist | Trace matrix from checklist rows to requirement IDs | 100% coverage; gaps recorded as `TBD` |
| Every applicable interface type has at least one accepted evidence row | Interface coverage map | 12 of 12 PKG-041 interface types covered or explicit `TBD` |
| Every accepted line cites source evidence | Audit sample (n>=10) of accepted lines | 100% citation present |
| No agent-issued binding acceptance | Audit signer field on every checklist row | Only human signers carry binding disposition |
| Facility utility anchors verified | Trace from REQ-041-06-05..-07 to vendor data | Vendor data consistent with the ruled electrical architecture (per `CONF-041-06-001`), DBM fuel-gas interface values, and enclosure expectations |
| Every open vendor parameter resolved or carried | Parameter tracker | Every item is `closed` (with vendor reference) or `TBD` on the punch list |

## Records

- `vendor-document-review-log` (`ART-9E33107762`) — markdown or CSV; one row per vendor document review entry.
- `vendor-package-acceptance-and-turnover-checklist` (`ART-0E8BDED2A8`) — markdown or CSV; one row per acceptance criterion.
- `factory-shop-test-and-inspection-evidence/` folder (`ART-53AD41FE27`) — vendor-supplied test/inspection PDFs plus a manifest.
- Open-parameter tracker (subset of the checklist; explicit `open / closed` state).
- Punch list and closeout log (subset of the checklist; explicit `open / closed` state).
- `_STATUS.md` history entries for each material lifecycle transition.
- Run records under `_run_records/` for each agent invocation that contributed to this deliverable.
