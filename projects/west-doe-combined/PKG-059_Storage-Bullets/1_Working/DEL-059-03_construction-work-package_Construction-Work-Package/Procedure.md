# Procedure — Construction Work Package (DEL-059-03)

> Operational procedure to produce and execute the PKG-059 Storage Bullets EPC Construction Work Package. The CWP is itself an EPC document set; the steps below describe both how to author the CWP artifacts and how the CWP-governed construction work proceeds in the field. Source-grounded in the GATE-07 decomposition snapshot and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. Clause-level practice from `26020-Package_Requirements.docx` package heading 14 is not locally accessible; affected steps are marked `location TBD`.

## Purpose

To produce the Construction Work Package, Installation and Tie-in Workface Plan, and Construction Interface and Turnover Checklist for the Storage Bullets package, and to use those artifacts to install, inspect, pre-commission, and turn over 16 x 120,000 USG NGL storage bullets at 04-25, meeting API 2510 spacing and the GATE-07 declared interface set.

## Prerequisites

| Prerequisite | Source / Reason | Status |
|---|---|---|
| Accepted decomposition snapshot | `_REFERENCES.md` (GATE-07 snapshot) | Available |
| Package register row PKG-059 | GATE-07 `PACKAGE_REGISTER.csv` | Available |
| Deliverable register row DEL-059-03 | GATE-07 `DELIVERABLE_REGISTER.csv` | Available |
| Sibling EPC anchor deliverables in PKG-059 (Scope of Work, Package Datasheet) | DEL-059-01, DEL-059-02 | Sibling deliverables present in the package; their four-doc kits may not yet be issued |
| Vendor Engineered Equipment Package (DEL-059-04) data needed to finalize foundations, supports, EHT/insulation, tie-in geometry | DBM-Deepcut lines 1629, 1814 (open design-development items) | TBD — required before affected work-face release |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Primary local source | Available |
| `26020-Package_Requirements.docx` package heading 14 | Decomposition-cited package requirements text | Not locally accessible — location TBD |
| `_DEPENDENCIES.md` upstream / downstream declarations | Deliverable-local dependency record | No declared upstream / downstream at PREPARATION |
| Facility ITP, weld / NDE program, HSE / construction standards | Project execution baseline | location TBD |

## Steps

### Phase A — Author the CWP artifact set

1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, the GATE-07 decomposition snapshot (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`), and the DBM-Deepcut source slices identified in `Datasheet.md`.
2. Identify the bullet population and product service from the active source basis (DBM-Deepcut: 16 x 120,000 USG NGL bullets); record the Conflict Table entry against the workbook-era LPG/condensate description (`Guidance.md` CONF-001).
3. Construct the bullet field layout package: cluster map (<=6 per cluster), inter-bullet spacing, cluster-to-cluster spacing, and offsets to property line, flare, fired heaters, control / non-control buildings, process vessels, truck loading station, atmospheric tanks, spill containment, related pump skids, and unrelated rotating equipment (per `Specification.md` CWP-002).
4. Construct the civil scope package: foundation envelopes (vendor-data-dependent — TBD until DEL-059-04 issues design); grading and surface-control scheme per DBM-Deepcut line 2722.
5. Author the Installation and Tie-in Workface Plan covering: receipt and laydown, foundation and grading sequencing, bullet setting and alignment, piping tie-ins (NGL inlet from upstream treating/dehydration; NGL outlet to product/booster pumps and LACT to NRM NEBC Connector — DBM-Deepcut lines 73, 492, 1408), relief routing tie-in (TBD), drainage / containment tie-ins, E&I and beacon-group installation (DBM-Deepcut line 3262).
6. Author the Construction Interface and Turnover Checklist covering all PKG-059 declared interface types from GATE-07 `PACKAGE_REGISTER.csv` row PKG-059.
7. Identify and record the inspection regime (CWP-008): hydrotest / pressure test of new tie-in piping, NDE per facility ITP, vessel code-stamp and receipt-record verification. (ASSUMPTION; reconcile against `26020-Package_Requirements.docx` heading 14 — location TBD.)
8. Identify and record the pre-commissioning regime (CWP-009): line flushing, leak testing, dryness verification, inert purge before NGL introduction. (ASSUMPTION; location TBD.)
9. Identify and record the turnover dossier composition (CWP-010): signed ITP records, weld maps and NDE results, hydrotest certificates, vessel code documentation, vendor document handoff (interfacing with DEL-059-05), red-line as-builts, the Construction Interface and Turnover Checklist.
10. Cross-check terminology, units, and values against `Datasheet.md` and `Specification.md` (Step 5 consistency sweep in the four-documents method).
11. Capture unresolved items in the Conflict Table in `Guidance.md` rather than guessing.

### Phase B — Execute the CWP in the field

12. Release work-face fronts only after the controlling vendor data has been approved (CWP-014) and after the relevant interface checklist line items show no blocking holds.
13. Set foundations and complete grading / surface-control features per the civil scope package (CWP-003).
14. Receive, lay down, and set bullets in the field per the layout package (CWP-001, CWP-002). Confirm spacing by tape measure at set; record on the Construction Interface and Turnover Checklist.
15. Install tie-in piping for process inlet, product run-down to LACT and NRM NEBC Connector, relief routing (once finalized), and drainage / containment routes (CWP-004, CWP-005, CWP-006).
16. Install E&I scope: grounding / bonding, EHT where applicable, area lighting, I&C / control cabling, fire & gas / safety system, and the beacon group near the NGL Storage Area (CWP-007, CWP-011).
17. Execute the inspection regime (CWP-008): hydrotest / pressure test of tie-in piping, NDE, vessel record verification.
18. Execute the pre-commissioning regime (CWP-009): flush, leak test, dryness verification, inert purge.
19. Walk down all PKG-059 interface types on the Construction Interface and Turnover Checklist; close out holds (CWP-011).
20. Assemble the mechanical completion turnover dossier (CWP-010) and present it for review and acceptance under DEL-059-06.

## Verification

| Step | Check | Evidence |
|---|---|---|
| 3, 14 | API 2510 spacing met across the bullet field | Layout review record; field tape-measure record; final survey |
| 4, 13 | Civil grading slope and surface-control feature in place per design | Civil drawings, grading survey, photo record |
| 5, 15 | Each tie-in installed per the workface plan | Line walk-down sheets; punch list closure |
| 6, 16, 19 | All PKG-059 declared interface types tracked to closure | Signed Construction Interface and Turnover Checklist |
| 7, 17 | Tie-in piping inspections complete | ITP signoff; hydrotest certificates; NDE reports |
| 8, 18 | Pre-commissioning complete prior to NGL introduction | Pre-commissioning checklists; purge certificates |
| 9, 20 | Turnover dossier complete | Dossier index against CWP-010 list; acceptance signoff under DEL-059-06 |
| 12 | Vendor data approved before work-face release on dependent fronts | Vendor data approval log mapped to work-face release register |

## Records

The following records shall result from the procedure:

- Construction Work Package (this deliverable's primary artifact)
- Installation and Tie-in Workface Plan
- Construction Interface and Turnover Checklist (signed, closed)
- Signed ITP records, hydrotest certificates, NDE reports, vessel code documentation
- Pre-commissioning checklists and purge certificates
- Red-line as-built drawings
- Vendor data approval log feeding work-face release decisions
- Mechanical completion turnover dossier ready for DEL-059-06 review and acceptance

ASSUMPTION: Record naming, format, and retention should align with `26020-Package_Requirements.docx` package heading 14 once locally accessible (location TBD).
