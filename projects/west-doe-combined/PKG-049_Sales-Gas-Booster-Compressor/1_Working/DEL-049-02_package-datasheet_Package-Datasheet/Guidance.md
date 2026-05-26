# Guidance — DEL-049-02 Package Datasheet (Sales Gas Booster Compressor, PKG-049)

> Directional guidance for completing and using the EPC Package Datasheet
> handoff. Rationale is drawn from accessible source slices; missing rationale
> is marked `TBD`. Conflicts surfaced by Pass 2 cross-reference checks are
> recorded in the Conflict Table at the end of this document for human ruling.

## Purpose

This deliverable exists to give a third-party Package Vendor (and the
EPC Integrator's downstream interface disciplines) a single, source-anchored
technical handoff that defines the Sales Gas Booster Compressor package basis,
its process duty, its key sub-systems, and the package interfaces that govern
integration into the West Doe Deepcut facility. PACKAGE_REGISTER row 80
identifies PKG-049 as a separable reciprocating, induction-motor-driven booster
package whose function is to compress sweet sales gas before the sales gas
coalescer (F-3500-1) and the sales gas splitter for TC Energy pipeline
delivery.

`_CONTEXT.md` Notes is explicit that the package datasheet is the mandatory
Gate 5 EPC anchor and that interface facts are intentionally carried here as
evidence rather than as standalone deliverables. This shapes the guidance
below.

## Principles

- **Source over convention.** Values in the datasheet must come from the DBM
  Deepcut source slice (lines 932-969 for the booster and 1469-1483 for the
  filter/coalescer) or from the package-row sources. Conventional values from
  general reciprocating-compressor practice are not authoritative for this
  package.
- **One x 100%, no spare.** The configuration is intentionally a single
  package with no installed spare (DBM Deepcut §942, §951, §877). Reliability,
  maintenance, and turnaround planning must accept the implications of full
  facility shutdown of TCPL booster flow when the package is unavailable.
- **EPC owns integration; Vendor owns package.** The Scope_Split is explicit
  in PACKAGE_REGISTER.csv. The datasheet's purpose is to make the EPC/Vendor
  battery limit unambiguous, not to specify vendor internal design.
- **Carry interface evidence in this deliverable.** Per `_CONTEXT.md` Notes,
  do not factor interface evidence out into separate deliverables for this
  package; keep it inside this datasheet and its interface matrix.

## Considerations

### Driver and start-up

The motor is a 6,700 hp, 4 kV, 60 Hz induction machine with DOL+soft-start and
no driver speed turndown (DBM Deepcut §936). Implications:

- Capacity turndown must be handled by recycle and clearance-pocket strategy,
  not by speed.
- The recycle valve is sized for the worst-case initial start-up condition
  (100% capacity at minimum pipeline operating pressure and high suction
  pressure; DBM Deepcut §969). Recycle sizing therefore drives the recycle
  path piping and the aftercooler thermal margin.

### Cylinder and clearance-pocket optimization

DBM Deepcut §936 and §969 both flag the same downstream decision: evaluate a
larger high-efficiency cylinder on a two-throw design, and evaluate automated
clearance pockets versus standard manual VVCPs, during detailed engineering.
Guidance: handle these together as a single optimization (low compression
ratio + recycle minimization at high suction pressure) rather than as two
separate vendor decisions.

### Suction scrubber necessity

The two-phase suction scrubber is included by default (DBM Deepcut §963) but
its final need is to be evaluated due to very low inlet dewpoint (upstream
mol-sieve dehydration delivers <0.1 ppmv water; DBM Deepcut §950). Guidance:
retain the scrubber in the datasheet until detailed engineering ruling
explicitly removes it; document the rationale for either retention or
deletion. If retained, demister sizing must follow API-11P or vendor
vane-style sizing.

### Aftercooler and downstream F-3500-1

The aftercooler outlet temperature (35 deg C winter / 43.3 deg C summer; DBM
Deepcut §965) becomes F-3500-1's inlet condition. F-3500-1 is in the 350 fuel
gas module adjacent to the booster (DBM Deepcut §1471), so the aftercooler
performance, the inter-piece piping pressure drop, and the F-3500-1 clean-side
dP (<2 psid) all combine into the discharge-pressure margin between the
12,866 kPag compressor discharge and the ~11,376 kPag HP Sales Header 2
operating pressure.

### Sweet gas purge as external scope

DBM Deepcut §967 is explicit that manual sweet gas purge is NOT included in
the package. The datasheet must surface this exclusion in the interface
matrix so the EPC team plans the external supply (likely from the shared
fuel-gas / purge-gas system referenced in DBM Deepcut §1712 and §1830-§1831).

## Trade-offs

| Trade-off | Options | Notes |
|---|---|---|
| Cylinder design | Ariel KBK/4 as mapped (DBM Deepcut §936) vs. larger high-efficiency two-throw cylinder | Low compression ratio favors the two-throw evaluation; detailed engineering decision; balance capital cost, footprint, and recycle power. |
| Clearance pockets | Manual VVCP vs. automated fixed-volume vs. automated continuously variable | Drives power consumption and recycle at high suction pressure; choose with cylinder decision. |
| Suction scrubber | Retain default scrubber vs. delete due to upstream mol-sieve | <0.1 ppmv water suggests low duty; retain unless detailed engineering explicitly justifies removal. |
| Sparing | Confirmed: one x 100%, no installed spare (DBM Deepcut §951) | Operational consequence is facility-level: TCPL booster route lost on package outage; HP Sales Header 1 picks up flow under shutdown case (DBM Deepcut §1434, §1436). |
| Recycle fail position | Fail-closed assumption (DBM Deepcut §969) requires confirmation in detailed engineering | Confirm with HAZOP and start-up sequence design. |

## Examples — How to Use This Datasheet

- **Vendor RFQ packaging:** Combine Sections 1 and 2.1-2.5 of the
  Specification with the Datasheet to form the technical envelope for the
  RFQ. (The original RFQ source is
  `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx`, not locally
  accessible; resolution required to align language.) `location TBD`.
- **Integration HAZOP basis:** Use Datasheet "Interfaces" plus Specification
  §2.6 as the interface-list input.
- **Discipline coordination:** Each interface row in the matrix becomes a
  ticket to the responsible EPC discipline (Electrical, Civil/Structural,
  Process Piping, I&C, Fire & Gas, HVAC, Drains/Flare).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-001 | F-3500-1 design inlet flow differs between records: 100 MMSCFD vs. 140 MMSCFD. | DBM Deepcut §1476 (notes "Available design records differ between 100 MMSCFD and 140 MMSCFD") | DBM Deepcut §1808 (lists same item as open Deepcut DBM action: "resolve sales gas booster filter/coalescer design-flow conflict between 100 MMSCFD and 140 MMSCFD") | Datasheet Filter/Coalescer table; Specification REQ-049-02-SUB-11 | PROPOSAL: Adopt 140 MMSCFD to match the booster compressor design capacity (DBM Deepcut §934, §947) as the conservative basis pending detailed engineering. | TBD |
| CONF-002 | Suction temperature stated as 43 deg C service basis but the design table gives 35 deg C winter / 43.3 deg C summer. | DBM Deepcut §934 ("at 6,137 kPag (890 psig) and 43 deg C") | DBM Deepcut §945 ("43 deg C service basis; 35 deg C winter and 43.3 deg C summer in design table") | Datasheet Conditions table; Specification REQ-049-02-PROC-2 | PROPOSAL: Carry the 35 / 43.3 deg C envelope as the design envelope and treat the 43 deg C single value as a single-point service basis. | TBD |
| CONF-003 | Recycle valve fail position: §969 states "fail closed, to be confirmed during detailed engineering". | DBM Deepcut §969 (internal flag) | n/a (no contradictory source) | Specification REQ-049-02-SUB-5 | PROPOSAL: Carry fail-closed in datasheet with explicit "to be confirmed" marker; resolve during start-up sequence HAZOP. | TBD |
| CONF-004 | Sources `26020-Package_Requirements.docx` heading 4 and `26020-Packages_Interfaces_4_export.xlsx` are referenced by both the decomposition row and `_REFERENCES.md` but are not locally accessible as text. Detailed interface scope cannot be source-grounded from accessible slices. | `_REFERENCES.md` | `_CONTEXT.md` Source Reference | Specification §2.6, Datasheet "Interfaces" non-process rows | PROPOSAL: Hold non-process interface scope at `TBD` and dispatch a source-acquisition request to convert these files to readable form. | TBD |
