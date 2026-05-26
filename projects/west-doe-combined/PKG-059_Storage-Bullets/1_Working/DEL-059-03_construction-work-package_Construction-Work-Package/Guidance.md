# Guidance — Construction Work Package (DEL-059-03)

> Directional guidance for the PKG-059 Storage Bullets EPC Construction Work Package. Guidance complements the normative `Specification.md` and the operational `Procedure.md`. Where the active source basis disagrees with the workbook-era package description, the disagreements are captured in the Conflict Table for human ruling.

## Purpose

The Construction Work Package exists to translate the EPC Integrator's package scope of work and package datasheet for the NGL storage bullet field into an executable construction plan: an installation sequence, the inspection and pre-commissioning regime, the interface and turnover discipline, and the documentation set required for handoff and acceptance. The CWP is the EPC Integrator's anchor for "how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems" (DELIVERABLE_REGISTER row DEL-059-03).

## Principles

- **EPC Integrator owns facility-level integration.** Bullet engineering, design, fabrication, and the physical equipment package are Package Vendor scope. The CWP is the boundary discipline that makes the vendor package land cleanly in the 04-25 facility (GATE-07 `PACKAGE_REGISTER.csv` row PKG-059 responsibility text).
- **Source-grounded layout.** The bullet field layout shall meet API 2510 spacing as captured in DBM-Deepcut. Spacing is not a design choice; it is a regulatory and code-driven invariant (DBM-Deepcut lines 245-266, 284, 299).
- **Containment by grading.** The NGL storage area depends on a designed grading scheme (berm, slope, or surface-control feature) for spill control and pool-fire mitigation. Civil scope is a first-class CWP discipline, not an add-on (DBM-Deepcut line 2722).
- **Tie-in completeness.** All PKG-059 declared interface types in GATE-07 (Process Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) shall be tracked to closure in the Construction Interface and Turnover Checklist.
- **Respect open design-development items.** Bullet detailed design parameters are explicitly an open design-development item in the DBM (lines 1629, 1814). Work-face release for affected fronts shall wait on vendor data approval rather than proceed on assumption.
- **Avoid overclaiming the package requirements document.** `26020-Package_Requirements.docx` package heading 14 is referenced by the decomposition but was not locally readable at drafting time. Clause-level requirement statements are deferred and marked `location TBD`. Do not derive precise clause text from decomposition prose.

## Considerations

- **Workbook-era versus DBM-era scope.** `_CONTEXT.md` and the workbook describe "two unstable condensate storage bullets and sixteen LPG product storage bullets for C5 condensate and LPG product storage." The current DBM basis is "16 x 120,000 USG NGL storage bullets" and explicitly retires the C3/C4 LPG storage concept along with the depropanizer (DBM-Deepcut lines 1627-1629). The CWP currently follows the DBM as the active design basis; the inconsistency is logged for ruling.
- **Adjacent atmospheric storage area.** Condensate product storage (4 x 3,800 bbl tanks; DBM-Deepcut line 1639) and produced-water tanks (TK-9010-1, TK-9020-1; DBM-Deepcut line 2627) are nearby but in separate packages. Interface management is by spacing and by drainage continuity, not by combined construction scope.
- **Flare relief routing.** API 2510 enforces a 30.48 m (100 ft) flare-to-bullet spacing (DBM-Deepcut line 284); the actual relief header (HP, LP, or combined) is determined by relief load analysis under detailed design and is not stated for bullets in the available source slice.
- **Spacing-term retention.** The DBM retains LPG-named spacing rows under API 2510 as a code-application convention even though the current product slate is NGL. Use the spacing values as stated; do not infer that the storage service is LPG.
- **Modularization.** No bullet shop-module entry was found in the DBM modularization table at the slice reviewed; the working assumption is field-set bullets. Confirm with the vendor package.

## Trade-offs

- **Sequencing piping tie-ins versus mechanical completion of bullets.** Bringing the field to mechanical completion before piping tie-ins reduces double-handling but defers leak detection on package boundaries. Workface planning should balance these two ITP milestones rather than serialize them in either direction.
- **Civil grading early versus late.** Early grading sets spill-control surfaces but constrains laydown and mobile-crane standing for bullet setting. The Installation and Tie-in Workface Plan should explicitly choose this sequence and document the rationale.
- **In-line inspection versus survey-based confirmation of API 2510 spacing.** Field tape-measure verification at set is cheap and immediate; final survey records are more defensible. Use both, not one.

## Examples

Where source-grounded examples are not available, no example is offered.

- API 2510 spacing values that drive bullet field layout: see DBM-Deepcut Sec. Pressurized Bullet Spacing (lines 245-266) and adjacent Flare/Heater spacing rows (lines 284, 299).
- Open design-development list applicable to this CWP: DBM-Deepcut line 1814 ("develop the detailed design basis for 16 x 120,000 USG NGL storage bullets").

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-001 | Bullet population and product service. Workbook/`_CONTEXT.md` say "two unstable condensate storage bullets and sixteen LPG product storage bullets for C5 condensate and LPG product storage". DBM says 16 x 120,000 USG NGL storage bullets, replacing the retired C3/C4 LPG storage concept. | `_CONTEXT.md` Scope; GATE-07 `PACKAGE_REGISTER.csv` row PKG-059 Process Function (workbook-derived) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 448, 492, 1627-1629 | `Datasheet.md` Attributes; `Specification.md` CWP-001, CWP-002, scope; `Guidance.md` Considerations | PROPOSAL: Treat the DBM as the active design basis (16 x 120,000 USG NGL bullets) and update `_CONTEXT.md` Scope to align in a later supervised change. CWP-001/002 currently follow the DBM. | TBD |
| CONF-002 | Bullet equipment tags are not enumerated in the available DBM source slice. The equipment-tag tables (DBM-Deepcut lines 2557-2627) list condensate (API 650) tanks (TK-9110-1...TK-9150-1) and produced-water tanks (TK-9010-1, TK-9020-1) but do not list bullet tags. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` equipment tag tables (lines 2557, 2625, 2627) | (none) | `Datasheet.md` Attributes (Bullet tags = TBD) | PROPOSAL: Carry bullet tags as `TBD` until vendor package data or a deeper DBM slice supplies them. | TBD |
| CONF-003 | Construction inspection and turnover requirements (CWP-008, CWP-009, CWP-010) reflect standard EPC practice rather than cited clauses, because `26020-Package_Requirements.docx` package heading 14 was not locally readable at drafting time. | `Specification.md` CWP-008, CWP-009, CWP-010 (ASSUMPTION-labelled) | `26020-Package_Requirements.docx` package heading 14 (not locally available; location TBD) | `Specification.md` Requirements; `Procedure.md` Steps | PROPOSAL: Reconcile clause-by-clause against `26020-Package_Requirements.docx` heading 14 once the document is locally accessible; promote ASSUMPTIONs to cited requirements at that time. | TBD |
| CONF-004 | Flare header routing for bullet relief is not specified in the available source slice; bullet-to-flare spacing is fixed at 30.48 m by API 2510 but header selection (HP, LP, combined) is not stated. | `Specification.md` CWP-006 (location TBD) | DBM-Deepcut line 284 (spacing only) | `Specification.md` CWP-006; `Datasheet.md` relief tie-in row | PROPOSAL: Carry relief routing as `TBD` and resolve during detailed-design / relief-load-model review. | TBD |
