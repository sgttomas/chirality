# Guidance — DEL-052-02 Package Datasheet (PKG-052 Inlet / TEG Dehy Cross Exchanger)

## Purpose

The Package Datasheet for PKG-052 exists so that third-party vendor or discipline package engineering and design teams can produce the engineered, fabricated, and turned-over Inlet / TEG Dehy Cross Exchanger package (E-5718-1) without having to re-derive the EPC Integrator's facility-integration intent from the underlying decomposition or the source workbook and design-basis memoranda.

It is the **EPC Integrator's handoff basis** — the single authoritative collection of: package identity, tagged equipment, process function, source-supported design data, interface scope, and responsibility split.

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 337.

## Principles

1. **Source fidelity over convenience.** The Datasheet must restate what the design-basis memorandum (DBM-Deepcut) and the workbook/Word package requirements actually say. When sources disagree (see Conflict Table), the Datasheet must surface the disagreement rather than silently choose.
2. **Responsibility split is non-negotiable.** Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. The Datasheet must never read as if EPC Integrator is specifying internal vendor design choices that are vendor scope (e.g., tube count, baffle layout).
3. **Interface scope is bounded by the package register.** Only the interface types declared in PACKAGE_REGISTER.csv row 62 for PKG-052 belong in the interface requirements matrix. Adding interface types not declared upstream would silently widen scope.
4. **TBD is a first-class state.** Missing values are recorded as `TBD` with the gap visible. Inventing plausible numbers is worse than admitting the gap.
5. **Decomposition routes; sources decide.** The decomposition entry and `_CONTEXT.md` route the deliverable to the right scope; they do not substitute for source content.

## Considerations

- **Warm-side stream identity** (see Conflict Table CONF-1) drives the thermal design and downstream P&ID; resolving it is a prerequisite to issuing the Datasheet to a vendor for engineered design.
- **TEMA classification** appears as "TEMA 'R' BEM" in PACKAGE_REGISTER.csv row 62 while the DBM section uses a less specific phrase ("BEM type described in the DBM source"). The register row is treated as the more specific statement, but vendor confirmation against the actual DBM text section is recommended.
- **Standards basis** (TEMA, ASME, jurisdictional pressure-equipment code) is implicit in the equipment class and design pressure but not explicitly cited in the accessible source slices. The Datasheet flags this as `location TBD` rather than asserting a code list as fact.
- **Module/system context.** The exchanger appears in Module 520 equipment lists (DBM line 1131) alongside amine inlet coalescers, amine absorbers, sweet gas scrubber, and TEG dehydration equipment. This provides plot/integration context but is not itself a Datasheet field.
- **Process condition envelope.** Facility-level inlet conditions (300 MMSCFD design vapour, 1,300 psig MAOP basis, 625/1,130 psig downstream compressor suction/discharge) provide an envelope for the cold-side stream but do not directly supply exchanger-specific operating temperatures and per-stream mass flows. Those remain `TBD`.

## Trade-offs

| Trade-off | Direction | Rationale |
|---|---|---|
| Warm-side = TEG-contactor overhead vs. warm-sweet gas from amine | Defer to human ruling | Both appear in source; both have plausible heat-integration logic. The Datasheet must not pick. |
| Specify code list (ASME VIII, TEMA, CSA B51) vs. leave `TBD` | Leave `TBD` until 26020-Package_Requirements.docx heading 7 is accessible | Avoid asserting an unverified code basis that could mislead a vendor RFQ. |
| Record decomposition narrative as design data vs. mark as source-derived | Source-derived only | Decomposition prose is summary, not requirement; per skill authority hierarchy. |
| Include vendor-internal mechanical detail (tube layout, materials) vs. defer to vendor | Defer | Vendor scope per PACKAGE_REGISTER row 62 responsibility split. |

## Examples

- **Datasheet "Duty" cell** correctly cites `PACKAGE_REGISTER.csv row 62` for `5,514.3 kW (18.82 MMBTU/hr)` rather than re-stating the value without provenance.
- **Datasheet "Tube-side fluid" cell** is labeled `ASSUMPTION` because the DBM process narrative implies sour gas as the cold-side service but does not explicitly assign tube/shell sides.
- **Interface matrix "I&C / Control Cabling" row** lists the responsibility split and tie-in as `TBD` rather than fabricating a loop list that the DBM does not provide.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-1 | Warm-side stream identity is stated two different ways. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger" line 606 — "dehydrated overhead gas from the TEG contactor" | DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger" line 606; PACKAGE_REGISTER.csv row 62 Description — "warm sweet gas leaving the amine sweetening unit" | Datasheet Process Function; Datasheet Design Attributes (Shell-side fluid); Specification R-3, R-5; Procedure Step "Resolve warm-side identity" | PROPOSAL: dehydrated TEG-contactor overhead (consistent with Module 520 grouping and DBM process narrative lines 1119-1120, 1193 placing the cross-exchanger downstream of the TEG contactor). | TBD |
| CONF-2 | TEMA type granularity. | PACKAGE_REGISTER.csv row 62 — "TEMA 'R' BEM" | DBM §"Inlet / TEG Dehy Cross Exchanger" — generic "BEM type described in the DBM source" | Datasheet Design Attributes (TEMA type) | PROPOSAL: accept "TEMA 'R' BEM" from register row as more specific. | TBD |
| CONF-3 | Code-of-construction basis is implicit. | Datasheet design pressure 1,415 psig and equipment class imply ASME BPVC VIII Div. 1 and CSA B51 | No explicit code list in accessible source slices | Specification Standards | PROPOSAL: leave standards table as `location TBD` until 26020-Package_Requirements.docx heading 7 is converted to markdown. | TBD |
