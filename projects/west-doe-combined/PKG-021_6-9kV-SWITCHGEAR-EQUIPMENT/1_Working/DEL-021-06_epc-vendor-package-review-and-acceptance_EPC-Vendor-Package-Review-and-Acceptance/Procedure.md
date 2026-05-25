# Procedure — DEL-021-06 EPC Vendor Package Review and Acceptance

## Purpose

Produce the EPC-Integrator-owned vendor package review, integration acceptance, and handoff-readiness evidence for PKG-021 (6.9 kV switchgear), in a form humans can sign and reviewers can audit.

## Prerequisites

| Prerequisite | Source | Status check |
|---|---|---|
| `DEL-021-01_scope-of-work` content exists and is sufficiently stable | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD — check `_STATUS.md` in sibling folder |
| `DEL-021-02_package-datasheet` content exists and is sufficiently stable | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD |
| `DEL-021-03_construction-work-package` content exists | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD |
| `DEL-021-04_vendor-engineered-equipment-package` vendor submittals available | GATE-07 `DELIVERABLE_REGISTER.csv` | TBD |
| `DEL-021-05_vendor-document-turnover-package` document register available | GATE-07 `ARTIFACT_REGISTER.csv` `ART-FA39AD509D` (currently `TBD vendor document register`) | TBD |
| Facility electrical design basis available for integration checks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (lines 2935, 2973, 2985) | OK |
| `_REFERENCES.md`, `_DEPENDENCIES.md`, `_CONTEXT.md` present | This deliverable folder | OK |
| Human reviewer designated for binding acceptance | `K-AUTH-1` | TBD |

## Steps

1. **Confirm acceptance ruler.** Read the latest accepted versions of `DEL-021-01` (Scope of Work), `DEL-021-02` (Package Datasheet), and `DEL-021-03` (Construction Work Package). Record their identifying snapshot/version in the review log header. If any is not yet stable, record as `TBD` and proceed only with the stable subset.
2. **Inventory vendor submittals.** Build the vendor submittal index from `DEL-021-05` (`ART-FA39AD509D` register, when available; otherwise vendor transmittals). One row per vendor document, with vendor doc number, revision, date, and EPC receipt date.
3. **Author the vendor document review and comment log (`ART-5D5CAC1D6D`).** For each indexed vendor document, record EPC review comments referencing specific clauses of the EPC Scope of Work / Package Datasheet / Construction Work Package and (where applicable) the DBM electrical basis. Each line includes a `disposition` field with allowed values: `accept`, `accept-with-comment`, `revise-and-resubmit`, `reject`, `TBD`. Agents may PROPOSE dispositions; only a human signs them.
4. **Verify interface coverage.** For each of the six applicable PKG-021 interface types in GATE-07 `INTERFACE_REGISTER.csv` (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), associate at least one accepted vendor document or test record. Gaps remain `TBD`.
5. **Author the vendor package acceptance and turnover checklist (`ART-4B01C09131`).** One row per acceptance criterion. Rows derive from: Specification REQ-021-06-01..-09; interface-coverage map from Step 4; facility electrical anchors (REQ-021-06-05..-07). Each row carries: criterion text, evidence pointer, disposition, human signer, date.
6. **Assemble factory/shop test and inspection evidence (`ART-E523401B0C`).** Collect vendor-supplied factory acceptance test (FAT) reports, routine test reports, inspection reports, and any third-party witness records. Tabulate by test type with pointer to underlying PDF/file. Items required by standards that are not locally accessible remain `TBD` (see Specification REQ-021-06-10 and Guidance Conflict Table `CONF-021-06-001`).
7. **Punch and closeout.** Aggregate all `TBD` / `revise-and-resubmit` / `reject` items into a punch list with target closeout dates. Closeout is achieved when every checklist row has a human-signed acceptable disposition or an explicitly accepted carry-forward.
8. **Promote.** When closeout is achieved, propose `_STATUS.md` transition (e.g., to `READY_FOR_REVIEW` or the project-defined accepted state) via the appropriate human-authorized path. Do not transition status automatically.

## Verification

| Verification check | Method | Pass criterion |
|---|---|---|
| Every Specification requirement (REQ-021-06-01..-09) is exercised in the checklist | Trace matrix from checklist rows to requirement IDs | 100% coverage; gaps recorded as `TBD` |
| Every applicable interface type has at least one accepted evidence row | Interface coverage map | 6 of 6 PKG-021 interface types covered or explicit `TBD` |
| Every accepted line cites source evidence | Audit sample (n>=10) of accepted lines | 100% citation present |
| No agent-issued binding acceptance | Audit signer field on every checklist row | Only human signers carry binding disposition |
| Facility electrical anchors verified | Trace from REQ-021-06-05..-07 to vendor data | Vendor data consistent with 6.9 kV / 3-phase / 60 Hz / 100 A 10 s grounding / modular building |

## Records

- `vendor-document-review-log` (`ART-5D5CAC1D6D`) — markdown or CSV; one row per vendor document review entry.
- `vendor-package-acceptance-and-turnover-checklist` (`ART-4B01C09131`) — markdown or CSV; one row per acceptance criterion.
- `factory-shop-test-and-inspection-evidence/` folder (`ART-E523401B0C`) — vendor-supplied test/inspection PDFs plus a manifest.
- Punch list and closeout log (subset of the checklist; explicit `open / closed` state).
- `_STATUS.md` history entries for each material lifecycle transition.
- Run records under `_run_records/` for each agent invocation that contributed to this deliverable.
