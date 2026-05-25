# Guidance: DEL-020-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable produces the EPC-Integrator review and acceptance evidence for the PKG-020 (13.8kV SWITCHGEAR EQUIPMENT) vendor package. Its purpose is to:

- demonstrate that the Package Vendor's engineered equipment package and vendor documentation conform to the EPC Scope of Work, Package Datasheet, and Construction Work Package for PKG-020;
- reconcile every PKG-020 interface (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) with facility-level integration requirements; and
- gate facility-level acceptance/turnover of the 13.8 kV main switchgear, which the DBM defines as the plant main power distribution center. (Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Power System.)

## Principles

- **EPC-Integrator-led, vendor-supported.** Reviewer authority sits with the EPC Integrator (responsible party for this deliverable per `DELIVERABLE_REGISTER.csv`). The Package Vendor supports by providing submittals, test records, and clarifications. (`_CONTEXT.md`.)
- **Source-grounded acceptance.** Every acceptance decision must trace to a governing source: the EPC SoW/Datasheet/CWP (project-internal), the governing standards (CSA C22.1-21 and Tourmaline electrical specifications), or completed electrical studies. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.)
- **Interface-first reconciliation.** The PKG-020 interface register defines six interface types that must be individually verified, not bundled. (`INTERFACE_REGISTER.csv` rows for `PKG-020`.)
- **Studies precede acceptance.** Hazardous-area-classification, load, short-circuit, relay-coordination/arc-flash, and load-flow studies must be completed before equipment ratings, protection settings, and arc-flash labels can be accepted. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.)
- **Certification non-negotiable.** Only new, current-design, NRTL-certified equipment may be accepted. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.)

## Considerations

- **Bus-sizing claim.** The DBM requires the 13.8 kV switchgear bus to be sized for the full facility scope. Acceptance should confirm that the vendor package bus rating is at least the load determined by the project load and load-flow studies, plus margin per Tourmaline electrical-design specification. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.)
- **Housing assignment.** The DBM contemplates a "810-1 13.8kV Switchgear Electrical Building" as the housing module. The vendor package must be physically and structurally compatible with that building's interior envelope, cable-tray and conduit routing, and maintenance access. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph and module list.)
- **Distribution-architecture conformance.** The DBM lists explicit downstream electrical buildings fed from the 13.8 kV switchgear (6.9 kV Inlet/Sales; 4.16 kV Acid Gas/Overheads; 600 V Acid Gas; 600 V Sales/Overheads; 4.16 kV/600 V General Area/Tank Farm). The vendor package's feeder count, ratings, and protection coordination should be checked against this radial-distribution basis. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Power System.)
- **Specification access.** The clause-level acceptance criteria from ELC-QAS-000007-001 and ELC-QAS-000003-001 are `location TBD` in this run. Detailed acceptance checklists should be regenerated once those specifications are made locally accessible.
- **Deviation register.** The DBM requires formal Tourmaline approval for any deviation/exception from applicable codes and standards. Acceptance should not be granted while deviations remain unapproved.

## Trade-offs

- **Depth of FAT/SAT witness.** Witnessing every FAT activity increases assurance but adds schedule and cost. Decision basis (witness scope) should follow ELC-QAS-000007-001 once accessed; default to witnessing high-impact tests (e.g., bus-bar dielectric, breaker functional, relay logic, primary-injection per cubicle).
- **Acceptance-status taxonomy.** A coarser status taxonomy (e.g., A/B/C/Rev) eases reviewer load but loses nuance; a finer taxonomy improves traceability but increases review time. Default to project document-control taxonomy (TBD) rather than inventing one here.
- **Acceptance gating.** Hard-gating acceptance on completion of all electrical studies maximizes safety/integration confidence but may compress vendor schedule. Recommend hard-gating REQ-020-06-04 (no exceptions) but allowing conditional acceptance of non-rating items in parallel.

## Examples

- **Bus-rating acceptance line item.** "Confirm vendor switchgear bus continuous current rating ≥ facility load (per load-study output, dated YYYY-MM-DD) × applicable design margin; reviewer initials; FAT bus-bar temperature-rise record reviewed." (Pattern; numeric values `location TBD` pending load study.)
- **Interface line item — Grounding/Bonding.** "Confirm two-point ground connection to facility ground grid; copper ground conductor sizing per CEC; vendor drawing GND-XXXX-001 reviewed; field installation inspected." (Source basis: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs; `INTERFACE_REGISTER.csv` `IFC-F3098CE7CD`.)
- **Turnover evidence cross-reference.** "DEL-020-05 turnover-index entry VDT-PKG-020-NNN matched to vendor manual VM-PKG-020-NNN; mechanical-completion sign-off attached." (Pattern; numbering scheme TBD.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CNF-020-06-01 | Vendor document review-status taxonomy and EPC document-control numbering are not defined in any locally accessible source. | `_CONTEXT.md` anticipated artifacts (silent on taxonomy) | None | Specification REQ-020-06-02, REQ-020-06-11 | Adopt project document-control procedure once available; do not invent a taxonomy here. | TBD |
| CNF-020-06-02 | FAT/SAT witness scope is not defined in accessible sources; ELC-QAS-000007-001 is referenced but its clause text is not accessible. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 | ELC-QAS-000007-001 (not accessible) | Specification REQ-020-06-07; Procedure Step 6 | Default to witnessing high-impact tests pending specification access; reopen on specification ingestion. | TBD |
| CNF-020-06-03 | Facility turnover procedure is not locally accessible. | `_CONTEXT.md` anticipated artifacts | None | Specification REQ-020-06-08; Procedure Step 7 | Reconcile against `DEL-020-05` turnover index pending procedure access. | TBD |
