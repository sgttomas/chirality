# Guidance — DEL-055-06 EPC Vendor Package Review and Acceptance

> Directional guidance for executing the EPC Integrator vendor package review and
> acceptance for the Low-Pressure Flare KO Drum (PKG-055). Sources cited where
> available; assumptions explicitly labeled.

## Purpose

This deliverable is the EPC Integrator's documented evidence that the Package
Vendor's engineered equipment and turnover documents satisfy the project's
scope, datasheet, and construction commitments for the LP Flare KO Drum package,
and that the package is acceptable for integration into the facility and for
turnover to operations. (`_CONTEXT.md` Scope.)

## Principles

- **EPC Integrator authority.** The EPC Integrator owns the acceptance decision;
  the Package Vendor provides input but does not self-certify acceptance.
  (`_CONTEXT.md` ResponsibleParty.)
- **Trace every acceptance to a SoW item.** Acceptance criteria are anchored to
  SOW-0083..0086 and PKG-055 objectives (OBJECTIVE_SCOPE_MAP.csv, GATE-07
  snapshot). Acceptance without traceability is rejected.
- **Source-anchored evidence.** Acceptance is based on vendor evidence records
  (test reports, NDE, FAT/SAT, certified drawings), not on vendor narrative.
- **No premature acceptance.** Open punchlist items affecting safety, code
  compliance, or commissioning prevent acceptance until closed. (ASSUMPTION.)
- **Fire-safe siting is non-negotiable.** Flare-and-KO-drum spacing constraints
  in OGAOM Sec. 9.6.15 and the OGPFR thermal-radiation limits govern layout
  acceptance. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.)

## Considerations

- **Plot plan dependency.** The governing plot plan drawing is CIV-235633-5002,
  identified by the DBM as not yet available; coordinate-level layout acceptance
  is TBD until the plot plan is issued. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  Sec. "Site basis" / "Flare and Incinerator Spacing".)
- **Source extraction gap.** The primary package requirements source
  (`26020-Package_Requirements.docx` heading 10) and the package interfaces row
  (`26020-Packages_Interfaces_4_export.xlsx` row 57) are binary office files and
  were not locally readable when this deliverable was drafted. Acceptance
  criteria that depend on those sources remain TBD until the source slices are
  extracted into a readable form.
- **Vendor identity TBD.** Package Vendor identity, scope split, and submittal
  register granularity are not yet captured in `_CONTEXT.md` and remain TBD.
- **Interface ownership.** Review must explicitly confirm the boundary at the
  package skid edge: vessel + skid scope (vendor) vs. tie-ins, structural
  foundations, and grounding (EPC). (ASSUMPTION; source location TBD.)

## Trade-offs

- **Strict checklist vs. risk-based review.** A line-item checklist gives full
  coverage but can dilute attention to high-risk items (relief sizing, vessel
  certification). Risk-based review focuses attention but can miss compliance
  items. The recommended approach is a baseline checklist with explicit
  high-risk flags. (ASSUMPTION; not source-derived.)
- **Conditional acceptance vs. hold.** Conditional acceptance with punchlist
  unblocks downstream construction sequencing; outright hold preserves leverage
  with the vendor. Choice is project-dependent. (ASSUMPTION.)

## Examples

- A vendor submits a pressure-test record showing hydro at 1.3 x MAWP held for
  30 min with no pressure drop and acceptable joint inspection. The reviewer
  cross-references the test pressure to the certified vessel datasheet and the
  ASME stamp record, logs the submittal in the review log, and updates the
  acceptance checklist for the vessel pressure-test line. (Illustrative;
  specific values TBD pending vendor datasheet.)
- A vendor submits an as-built skid layout that places the KO drum 8 m from
  scrub vegetation along the south fence. The reviewer flags non-compliance
  with the >= 10 m flare-tanks-to-vegetation spacing rule (OGAOM Sec. 9.6.15
  via DBM) and rejects the submittal pending re-layout or compensating
  measures.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-06-01 | Vendor identity, vendor scope split, and detailed acceptance criteria for the LP Flare KO Drum package are not captured in any locally readable source. | `_CONTEXT.md` (silent) | `_Sources/26020-Package_Requirements.docx` heading 10 (binary; not locally readable) | Datasheet (Identification, Attributes); Specification (REQ-06-08) | Extract heading 10 to markdown and re-run four-documents pass 2 | TBD |
| CT-06-02 | Governing code basis for the LP Flare KO Drum vessel (ASME Sec VIII Div 1) and tie-in piping (ASME B31.3) is assumed by industry convention but not cited in a locally readable source. | DBM-Deepcut (silent on package-level code basis) | `_Sources/26020-Package_Requirements.docx` heading 10 (not locally readable) | Specification (Standards, REQ-06-03) | Confirm via source extraction or vendor datasheet | TBD |
| CT-06-03 | Layout acceptance cannot be finalized; governing plot plan CIV-235633-5002 is identified by the DBM as not yet available. | DBM-Deepcut Sec. "Site basis" / "Flare and Incinerator Spacing" | (no counter-source) | Specification (REQ-06-05); Procedure layout-acceptance step | Defer layout acceptance until plot plan issued | TBD |
