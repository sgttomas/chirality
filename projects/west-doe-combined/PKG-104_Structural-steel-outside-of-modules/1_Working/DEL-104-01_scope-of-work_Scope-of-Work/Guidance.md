# Guidance: DEL-104-01_scope-of-work — Scope of Work

> Directional guidance for authoring the `PKG-104` Scope of Work. The Scope of
> Work is the EPC Integrator's anchor narrative for the package and is the
> upstream input for the package datasheet, construction work package, and
> discipline production package.

## Purpose

`PKG-104` carries the workbook-defined Structural package "Structural steel -
outside of modules" under WBS 01 (Source: `PACKAGE_REGISTER.csv` row
`PKG-104`). The Scope of Work deliverable exists to:

- declare the package boundary and identity in EPC terms;
- record the package function and integration into the whole facility;
- enumerate the source-supported tagged equipment basis (or carry it as
  `TBD` when source does not support it);
- assign responsibility consistent with the workbook record and the project's
  responsibility model (Source: `PACKAGE_REGISTER.csv` Responsibility note).

Supported objectives per the decomposition package-heuristic mapping:
`OBJ-001` (04-25 Deepcut facility process scope) and `OBJ-008` (civil,
structural, site, buildings, foundations, grading, containment, access,
pipe rack, platform, construction support) (Source: `_CONTEXT.md`;
`OBJECTIVE_REGISTER.csv`).

## Principles

1. **Source primacy.** Workbook Packages row 105 and DBM-Deepcut SEC-11 are the
   authoritative sources for package identity and structural basis. Do not
   substitute decomposition prose for source content.
2. **Boundary by exclusion.** The package title "Structural steel - outside of
   modules" implies that module-internal structural steel is carried inside
   the module packages, not here (**ASSUMPTION** until source confirms).
   Pipe racks and pipe rack modules are explicitly the EPC Integrator's
   responsibility under `PKG-103` per the Gate 6 disposition recorded in the
   `INTERFACE_REGISTER.csv` notes on `PKG-103` interfaces.
3. **Standards consistency.** Steel design is per CAN/CSA-S16; materials are
   CSA G40.20/G40.21 (350W W-flange/HSS; 300W channels/plates/angles); loading
   per National Building Code of Canada. Use these without restating them as
   deliverable-specific values (DBM-Deepcut SEC-11).
4. **Foundation default.** Driven steel piles are the project default for
   buildings, equipment, towers, tanks, modules, pipe racks, and similar
   structures. Note this in the integration narrative; do not invent
   site-specific pile design parameters (those are `TBD` pending geotechnical
   report) (DBM-Deepcut SEC-11 "Piles and Foundations").
5. **Interface fidelity.** Only the two physical interfaces recorded in the
   workbook for `PKG-104` are first-order facts:
   "Grading / Site Drainage / Spill Containment" and
   "Structural / Foundations / Supports" (`INTERFACE_REGISTER.csv`).
6. **Epistemic discipline.** Mark unsourced values `TBD`; mark inferred
   values `ASSUMPTION`. Do not silently resolve them (K-PROV-1).

## Considerations

- The package's responsibility record is intentionally cautious: EPC Integrator
  vs discipline-subcontractor responsibility is source-dependent, and no
  separate vendor-package ownership model is inferred (`PACKAGE_REGISTER.csv`).
  Authors should preserve this caution.
- Major tagged equipment is not enumerated for `PKG-104` in the available
  decomposition records; treat the tagged-equipment list as `TBD` until the
  workbook row 105 detail is extracted from
  `_Sources/26020-Packages_Interfaces_4_export.xlsx` or `26020-Package_Requirements.docx`.
- Site loading (-40 deg C minimum ambient) affects metallurgy and detailing
  for exposed structural steel (DBM-Comp_and_Liquids SEC-04 line 145); call
  this out in the integration narrative where exposure is implied.
- Geotechnical parameters (bearing capacity, LPILE curves, dynamic criteria,
  pavement design) are all `TBD` pending geotechnical report (DBM-Deepcut
  SEC-11 lines 2687-2697); do not surface preliminary numbers as design values.

## Trade-offs

- **Specificity vs. source fidelity.** It is tempting to describe specific
  outside-of-modules structures (transformer bases, equipment supports,
  platforms, access steel, etc.). Only call out structures that the source
  text supports. DBM-Deepcut SEC-11 mentions: "structural steel transformer
  bases" (line 2949) and the pig receiver "structural steel non-enclosed skid"
  (line 585) — these are within scope of the project's structural steel basis
  but their package allocation (PKG-104 vs other packages) is not explicit in
  the available source slices. Treat such allocation as `ASSUMPTION` or `TBD`.
- **Responsibility framing.** A definitive EPC vs subcontractor split would
  be useful downstream but is not source-supported. Carry the workbook's
  cautious framing rather than over-committing.

## Examples (source-supported)

- Transformer bases — "Large oil-filled transformers shall be spaced in
  accordance with CEC requirements. They will generally be installed on
  structural steel transformer bases."
  (DBM-Deepcut SEC-11 line 2949). Allocation to `PKG-104` is **ASSUMPTION**.
- Pig receiver skid — "The plant inlet pipeline gas enters through one 610 mm
  OD (24 in.) pig receiver on a dedicated structural steel non-enclosed
  skid." (DBM-Deepcut line 585). Allocation to `PKG-104` is **ASSUMPTION**;
  may instead belong to inlet receiving package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-104-01-01 | Tagged equipment list for `PKG-104` is required by anticipated-artifact `ART-6192616307` but no tagged equipment for `PKG-104` is enumerated in the accessible `PACKAGE_REGISTER.csv` slice or in DBM-Deepcut SEC-11. | `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` `ART-6192616307` | `PACKAGE_REGISTER.csv` row `PKG-104` (no tagged-equipment column populated); DBM-Deepcut SEC-11 | Datasheet "Attributes" (Tagged major equipment); Specification REQ-104-01-08 | Carry as `TBD` and request workbook row 105 extraction from `26020-Packages_Interfaces_4_export.xlsx`. | TBD |
| CONF-104-01-02 | Package responsibility: `_CONTEXT.md` lists ResponsibleParty = EPC Integrator, while `PACKAGE_REGISTER.csv` records "EPC Integrator or discipline subcontractor responsibility is source-dependent". | `_CONTEXT.md` Identity | `PACKAGE_REGISTER.csv` Responsibility column | Datasheet Identification; Specification REQ-104-01-06; Procedure Step "Responsibility record" | Prefer `PACKAGE_REGISTER.csv` framing (broader, source-faithful) and treat `_CONTEXT.md` value as drafting ownership rather than execution ownership. | TBD |
| CONF-104-01-03 | Scope boundary against module-internal structural steel: the package title implies "outside of modules" but no source slice explicitly states which structural steel items are inside vs. outside modules. | Package title (`PACKAGE_REGISTER.csv` `PKG-104`) | DBM-Deepcut SEC-11 (does not partition steel by module membership) | Specification "Out of Scope"; Guidance "Boundary by exclusion" | Carry the inside-vs-outside boundary as **ASSUMPTION** and request explicit confirmation during Gate 5 disposition. | TBD |
| CONF-104-01-04 | Allocation of source-named structural steel items (transformer bases, pig receiver skid) to `PKG-104` is not explicit in the source slices. | DBM-Deepcut SEC-11 lines 2949, 585 | `PACKAGE_REGISTER.csv` row `PKG-104` (no item-level allocation column) | Guidance "Examples"; Datasheet "Construction" | Treat allocation as **ASSUMPTION** pending Integrator package allocation ruling. | TBD |
