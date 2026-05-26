# Guidance — DEL-097-01 Scope of Work

Directional rationale for authoring the EPC Scope of Work for `PKG-097` "Tanks, Condendate (API 650) 3-25". This document is not a specification; it explains intent and trade-offs and surfaces conflicts that must be ruled by a human.

## Purpose

This deliverable exists to give the Package Vendor a single, EPC-issued statement of what `PKG-097` is, what it must do in the 03-25 Liquids Hub, where its boundaries are, and which decomposition scope items (`SOW-0201`..`SOW-0204`) it carries. It is the Gate-5 EPC anchor for the package and the upstream basis for `DEL-097-02_package-datasheet`, `DEL-097-03_construction-work-package`, and the downstream vendor-package and acceptance deliverables. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows 492–497.)

## Principles

1. **Workbook + Word + DBM, in that order, for what the package is.** The workbook row (`PACKAGE_REGISTER.csv` row 88) sets the package identity and Vendor/EPC split. `26020-Package_Requirements.docx` heading 49 (as extracted into `SCOPE_LEDGER.csv` `SOW-0202`/`SOW-0203`/`SOW-0204`) supplies the equipment basis, conditions, and exclusions. The 03-25 DBM supplies the facility context (where the tanks sit, what they receive, where their product goes). Do not promote DBM-level narrative into binding package requirements unless the same fact is also present in the workbook or Word source.

2. **EPC speaks scope; Vendor speaks design.** The Scope of Work shall not pre-engineer the tanks. Wall thickness, nozzle schedules, anchor design, foundation pattern, electrical actuation details and similar are Vendor-engineering content and belong in vendor design output (`DEL-097-04`). The Scope of Work fixes what must be true at the boundary: count, size, code, conditions, fittings, coating, interfaces, and exclusions.

3. **Carry interfaces explicitly; defer interface facts to the datasheet.** Nine package-level interfaces are declared in `INTERFACE_REGISTER.csv` for `PKG-097`. The Scope of Work lists them by interface type. The interface fact rows (tie-in points, sizes, ratings, owners) are intentionally carried in `DEL-097-02_package-datasheet` (per `DELIVERABLE_REGISTER.csv` row 493 note). This prevents duplication and divergence.

4. **Atmospheric, non-insulated condensate product tanks — do not mirror the produced-water-tank specification.** The DBM separately describes produced-water tanks as "API-650 Modified atmospheric tanks, externally insulated and heated" with the Devchem 253 internal coating (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`). The `PKG-097` source says the condensate product tanks are *non-insulated* and that *a recycle may be required* to hold temperature in winter (`SCOPE_LEDGER.csv` `SOW-0203`). The Scope of Work must preserve that distinction.

5. **Preserve workbook spelling.** The workbook records the package name as "Tanks, Condendate (API 650) 3-25" (`PACKAGE_REGISTER.csv` row 88). The Scope of Work shall use that exact name when referring to the package. Body text describing the service may use "condensate" as a normal word.

## Considerations

- **Count alignment with the DBM.** The DBM total condensate-storage basis for the 03-25 Liquids Hub is eleven (11) 3,800 bbl condensate tanks (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling). `PKG-097` supplies four (4) 3,800 bbl Condensate Product Storage Tanks per `SCOPE_LEDGER.csv` `SOW-0202`. The two values are *not* contradictory at face value — the package likely supplies the product-condensate subset of the DBM tank inventory ("four product condensate tanks" per the DBM functional allocation). The Scope of Work should therefore *not* claim `PKG-097` provides the full Liquids-Hub condensate tank set, and should locate `PKG-097` against the DBM functional allocation. See Conflict Table CT-097-01-B.

- **Truncated source enumeration.** The extracted `SOW-0203` per-tank fittings list ends with "tank." indicating the workbook excerpt is truncated. The Scope of Work shall enumerate the fittings present in the source (PVRV, EPRV, VRU header connection, blanket-gas connection) and mark the remainder `TBD` pending re-extraction of `26020-Package_Requirements.docx` heading 49.

- **Modified API 650.** The "modified" qualifier is present in the source but the modifying clauses are not enumerated in the available extract. Vendor-issued design basis must record the specific deviations.

- **Objective traceability is ASSUMPTION-grade.** The supports-objective set (`OBJ-002`..`OBJ-010`) for this deliverable was assigned by the package-grouping heuristic per `_CONTEXT.md`; treat it as directionally relevant context, not as a hard binding requirement, until a human confirms.

## Trade-offs

- **Detail vs. duplication.** Putting interface tie-in facts in the Scope of Work would duplicate the Package Datasheet. Decision: list interface types only; defer facts to `DEL-097-02`.
- **Restating vs. referencing scope-ledger items.** Restating `SOW-0202`/`SOW-0203`/`SOW-0204` verbatim risks drift; pure references risk a Vendor reading the Scope of Work without context. Decision: paraphrase normatively in `Specification.md` *and* cite the `SOW-####` ID, so the chain back to source is one hop.
- **Including DBM site-basis numbers.** The -40 °C facility design minimum ambient and winter recycle considerations are facility-wide DBM facts that materially affect this package. Including them improves Vendor understanding but risks turning the Scope of Work into a mini-DBM. Decision: include only the conditions explicitly tied in `SOW-0204` plus a one-paragraph integration narrative pointing at the DBM.

## Examples

Example normative clauses for the Scope of Work (derived from `SCOPE_LEDGER.csv`):

- "Supply four (4) 3,800 bbl Condensate Product Storage Tanks designed and fabricated to modified API 650 (`SOW-0202`, `SOW-0203`)."
- "Tanks shall be non-insulated atmospheric tanks; a recycle may be required to maintain temperature during winter (`SOW-0203`)."
- "Each tank shall include a PVRV, an EPRV sized for the single worst-case relief event, a VRU header connection, and a blanket-gas connection; blanket-gas system per API 2000 (`SOW-0203`)."
- "Operating conditions: pressure atmospheric (ambient); temperature 0 °C to 40 °C. Design conditions: pressure 32 oz test; temperature -40 °C to 60 °C (`SOW-0204`)."
- "By Others: foundations; at-site mounting; electrical / instrumentation; platforms; staircases (`SOW-0204`)."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-097-01-A | Tank insulation status: `SOW-0203` says non-insulated atmospheric tanks for `PKG-097`; the DBM describes the produced-water-tank set as "API-650 Modified atmospheric tanks, externally insulated and heated" with Devchem 253 coating. Risk that the Vendor mistakes the DBM produced-water-tank description as a model for the condensate product tanks. | `SCOPE_LEDGER.csv` `SOW-0203`; `26020-Package_Requirements.docx` heading 49 | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-water tank description | Specification REQ-097-01-05; Datasheet Construction / Equipment Scope | The Word package source (`SOW-0203`) governs for `PKG-097`: condensate product tanks are non-insulated. The DBM "externally insulated and heated" applies to produced-water tanks only. | TBD |
| CT-097-01-B | Tank count alignment with DBM: `PKG-097` Basic scope = four (4) tanks; DBM Liquids-Hub basis = eleven (11) 3,800 bbl condensate tanks (with functional allocation of two sour inlet, four sour, four product, one slop). | `SCOPE_LEDGER.csv` `SOW-0202`; `PACKAGE_REGISTER.csv` row 88 | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling | Specification REQ-097-01-02; Datasheet Attributes; integration narrative | `PKG-097` provides the four product-condensate tanks subset of the eleven-tank DBM inventory. Sour-condensate, sour-inlet, and slop tanks are supplied by different package(s) or future scope. | TBD |
| CT-097-01-C | Per-tank fittings list truncation: `SOW-0203` enumeration ends mid-sentence ("...tank."). Additional fittings may exist in `26020-Package_Requirements.docx` heading 49 beyond PVRV / EPRV / VRU header / blanket-gas connection. | `SCOPE_LEDGER.csv` `SOW-0203` (truncated) | `26020-Package_Requirements.docx` heading 49 (binary; not slice-extracted) | Specification REQ-097-01-08; Datasheet Attributes (Per-tank fittings) | Re-extract heading 49 of the Word source and replace the `TBD` marker with the complete fittings list. Until then, the Scope of Work shall name only the four fittings from the available extract and carry an explicit `TBD`. | TBD |
| CT-097-01-D | Insulation vs. winter temperature maintenance: `SOW-0203` calls the tanks non-insulated but allows that "a recycle may be required to maintain a certain temperature during winter." This is internally consistent but operationally significant; the facility design minimum ambient is -40 °C (DBM Site Basis). | `SCOPE_LEDGER.csv` `SOW-0203` | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis | Specification REQ-097-01-05, REQ-097-01-11..REQ-097-01-12; Guidance Principles | Treat as a vendor design responsibility under modified API 650 with EPC-supplied recycle interface; not a Scope-of-Work conflict per se but flagged so the recycle interface is not lost across deliverables. | TBD |
