# Guidance — DEL-067-01 Scope of Work

> Directional guidance for authoring the EPC Scope of Work for PKG-067 "Tanks, Sour Water (API 650) 4-25". Grounded in `_CONTEXT.md`, the GATE-07 PROJECT_DECOMP snapshot, `26020-Package_Requirements.docx` heading "26020-01-PT-19-005 - Tanks, Sour Water", and `DBM-Deepcut/4-25_Deepcut_DBM.md`. Inferences are labeled `ASSUMPTION`.

## Purpose

This deliverable is the mandatory Gate-5 EPC Integrator anchor scope-of-work for PKG-067 (`DELIVERABLE_REGISTER.csv` row 528). It bounds the package for downstream production units (Package Datasheet DEL-067-02, Construction Work Package DEL-067-03, Vendor Engineered Equipment Package DEL-067-04, Vendor Document Turnover DEL-067-05, Vendor Package Review and Acceptance DEL-067-06). Its job is to fix the package identity, function, source basis, and responsibility split so vendors and integrators read the same scope.

## Principles

1. **Source-anchored, not invented.** Every package-defining statement (tags, capacity, governing standard, service composition) must trace to `26020-Package_Requirements.docx` paragraph 281 or the DBM Produced Water section. Unknown values are explicit `TBD` or `TBC`; convenient generic conventions are not substituted for source language.
2. **Boundary-first, not design-first.** The SOW defines what the package is and where it begins and ends; it does not preempt vendor sizing or detailed-engineering decisions reserved by DBM line 524 and line 1714.
3. **Integration narrative is mandatory.** Per `DELIVERABLE_REGISTER.csv` row 528, the SOW must include a whole-facility integration narrative — not just a tag list.
4. **Responsibility split is governed by package register.** The exact wording from `PACKAGE_REGISTER.csv` row 94 governance note should be the basis of the responsibility section; do not paraphrase in a way that shifts responsibility.

## Considerations

- **Two-tank pair drives narrative.** The 4-25 sour-water service is sized as two tanks (DBM row 2559) sized 2 x 2,000 bbl (DBM line 493). The SOW should reflect the pair as a system, not as two independent items.
- **Cross-package coupling is heavy.** Produced-water transfer pumps live in PKG-060 (Tank Farm Pump Building 4-25), not PKG-067 (DBM line 2555). The SOW must keep pump scope out of PKG-067 while documenting the suction interface.
- **VRU + blanket gas coupling.** Vapour management couples PKG-067 to the VRU package (DBM line 1683) and to the LP fuel gas blanket system; both belong in the integration narrative, not in package requirements.
- **Source ambiguity around "sour".** The package label uses "Sour Water" while DBM and the package requirements doc use "produced water" with the qualifier that the service may include sour vapours and trace H2S (DBM lines 508, 524). The SOW should mirror DBM language and not introduce a stricter "sour-rated" envelope unsupported by source.
- **3-25 analog basis.** PACKAGE_REGISTER row 94 explicitly cites the 3-25 sour water RFQ package (`26020-03-PT-19-007`) as the analog. Use analog cautiously: cite as analog, not as 4-25 source.
- **Permitting overhang.** DBM line 133 notes that further BCER permit amendments are required "for the truck rack and sour water treating once sufficient detail is available." The SOW should note this as a permitting watch item, not a package commitment.

## Trade-offs

- **Specificity vs. vendor design freedom.** Sizing (tank diameter/height, capacity at maximum operating level, EPRV sizing) is intentionally `TBD` per DBM line 524 and line 1714. Resist locking these in the SOW — they belong in the Package Datasheet and vendor package.
- **Interface enumeration vs. interface fact.** The SOW should list interface *types* (per PACKAGE_REGISTER row 94) and defer interface *facts* (line numbers, tag handoffs, signal lists) to DEL-067-02 Package Datasheet (per `DELIVERABLE_REGISTER.csv` row 529).
- **Composition coverage.** DBM line 508 explicitly states the trace-contaminant list is non-exhaustive and TBC. The SOW should reproduce that language verbatim rather than presenting a closed list.

## Examples

- **Tag list example (R-067-01-01):** "The package comprises two API 650 modified atmospheric produced-water / sour-water storage tanks, expected tags `TK-9010-1` and `TK-9020-1`, in 4-25 (Deepcut) service." Source: `26020-Package_Requirements.docx` paragraph 281.
- **Integration narrative example (R-067-01-04):** "Produced water is collected from the inlet separator system and from package drain headers (NGL water-wash recycle, mole-sieve inlet coalescer, regeneration-gas scrubber, compressor stage-1 scrubber, and 300# ANSI produced-water drain header sources) and is buffered in `TK-9010-1` / `TK-9020-1`. Stored water is transferred by the 2 x 100% produced-water transfer pumps located in Tank Farm Pump Building 2 (PKG-060) to the new produced-water pipeline that delivers to the 03-25 Liquids Hub (60 m3/d continuous average; ~240 m3/d batch). Tank vapours are managed by an LP fuel gas blanket and routed to the VRU header where applicable." Sources: DBM lines 502–510, 521, 524, 1683, 2555; `26020-Package_Requirements.docx` paragraph 281.
- **Responsibility example (R-067-01-07):** "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration." Source: `PACKAGE_REGISTER.csv` row 94 governance note.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-067-01-A | "Modified API 650" qualifier asserted for sour-water tanks by analogy with condensate tanks; not explicit in the sour-water package source text. | `26020-Package_Requirements.docx` paragraph 281 ("API 650 modified atmospheric") | DBM line 1646 (condensate tank specification "Modified API 650") | Datasheet R-067-01-02; Specification R-067-01-02 | Treat `26020-Package_Requirements.docx` paragraph 281 as authority for sour-water tanks; record DBM line 1646 as analog corroboration; flag clause-level "modified" content as `TBD`. | TBD |
| CT-067-01-B | Capacity per tank (2,000 bbl) is taken from the facility-level produced-water table; not restated in the package heading. | DBM line 493 (facility table) | `26020-Package_Requirements.docx` paragraph 281 (silent on capacity) | Datasheet "Attributes" capacity row | Use DBM line 493 facility value pending Package Datasheet (DEL-067-02) confirmation; mark "Capacity at maximum operating level" as TBC. | TBD |
| CT-067-01-C | Service label "Sour Water" (package title) vs. "produced water" (DBM and package source body). | `_CONTEXT.md` PackageName; `DELIVERABLE_REGISTER.csv` row 528 | DBM lines 502–510; `26020-Package_Requirements.docx` paragraph 279 | Datasheet "Attributes — Operating Service Fluid"; Specification R-067-01-03; Guidance "Considerations" bullet on source ambiguity | Use "produced-water / sour-water" combined label per `26020-Package_Requirements.docx` paragraph 279; preserve both terms. | TBD |
| CT-067-01-D | Objective association (`OBJ-001`, `OBJ-003`–`OBJ-010`) recorded at the deliverable level via PACKAGE_HEURISTIC; not from an explicit deliverable-ID-level mapping. | `_CONTEXT.md` "Supports Objectives"; `DELIVERABLE_REGISTER.csv` row 528 objective column | `OBJECTIVE_DELIVERABLE_MAP.csv` (mapping granularity TBC) | Datasheet "Identification" Supported Objectives row | Carry as ASSUMPTION (best-effort mapping) per skill rule; do not treat as hard objectives until human confirms. | TBD |
