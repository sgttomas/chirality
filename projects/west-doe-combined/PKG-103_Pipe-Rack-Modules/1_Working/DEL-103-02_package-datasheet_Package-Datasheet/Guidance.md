# Guidance — DEL-103-02 Package Datasheet (PKG-103 Pipe Rack Modules)

> Directional document. Records intent, rationale, considerations, trade-offs, and (when applicable) a Conflict Table for human ruling.

## Purpose

The Package Datasheet exists as the EPC Integrator's mandatory technical handoff so that a third-party vendor or discipline subcontractor can engineer and design the pipe-rack-module package without re-deriving facility-level basis information. Per `_CONTEXT.md` and the decomposition row, interface facts are intentionally **carried as evidence inside this deliverable** rather than spun out as standalone interface deliverables — concentrating them here is deliberate so the vendor receives a single, source-anchored package datum set.

## Principles

1. **Source fidelity first.** Every non-trivial datasheet attribute is anchored to a DBM source slice. Where the underlying source artifact (package-requirements workbook, interfaces export) is not locally accessible as text, the corresponding fields are recorded as `TBD` rather than guessed.
2. **Decomposition routes, sources determine.** The decomposition row identifies *what* the package is and *who owns it*; numerical / clause-level content comes from DBM source slices and the workbook sources (when accessible).
3. **Modular separation of concerns.** Datasheet (descriptive), Specification (normative), Guidance (directional), Procedure (operational). Cross-document terminology and values are aligned (see consistency sweep below).
4. **Evidence concentration is deliberate.** Interface, electrical, classification, grounding, and skid-edge convention facts are intentionally carried in the Datasheet rather than promoted to separate interface deliverables.

## Considerations

- The two DBM variants (`3-25_Comp_and_Liquids_DBM.md`, `4-25_Deepcut_DBM.md`) are jointly relevant to the West Doe combined project. Pipe-rack content in the Deep Cut DBM is materially richer (cable tray, heat tracing, grounding, beacons, skid-edge conventions); the Comp & Liquids DBM corroborates hazardous-area classification, civil/structural enumeration, and foundation design factors. There are no contradictions between the two DBM variants on pipe-rack content within the slices read this pass.
- Outdoor pipe racks default to general-purpose / non-hazardous, but detailed area-classification drawings override this default — vendors must consult those drawings before equipment selection.
- Default foundation basis is driven steel piles, but final design parameters depend on the geotechnical report. The geotechnical report is **not** in `_Sources` and is `TBD`. Pile design assumptions cannot be promoted to FACT until that report is accessible.
- The package's quantitative envelope (module count, dimensions, tonnage, weight) is the principal data class missing from this pass because both the `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` are not text-accessible. Restoring those sources to a markdown form is the highest-leverage next step.
- Setting modules on foundations is identified in the Deep Cut DBM as Tourmaline field construction scope; carrying that as an ASSUMPTION on PKG-103 is appropriate until the EPC contract terms are confirmed.

## Trade-offs

| Trade-off | Direction Taken Here | Rationale |
|---|---|---|
| Concentrate interface facts in the Datasheet vs. spin out standalone interface deliverables | Concentrate (per `_CONTEXT.md` Notes) | Vendor receives a single source-anchored handoff; reduces fragmentation; aligns with Gate 5 EPC anchor intent. |
| Cite DBM source slices in the Datasheet vs. only summarize | Cite | Preserves traceability into the GATE-07 source set; enables surgical re-issue when DBM slices change. |
| Mark missing quantitative fields TBD vs. invent values | Mark TBD | K-PROV-1 invariant — no governed claim without provenance. |
| Use the package-grouping heuristic for objectives vs. assert direct objective ownership | Use heuristic, label ASSUMPTION | Decomposition uses package-grouped objective mapping; explicit deliverable-level mapping is not present. |
| Treat construction-execution sequencing in this deliverable vs. defer to DEL-103-03 | Defer | Separation of concerns; CWP is the home for construction execution. |

## Examples

- **Cable tray sizing example.** When sizing main cable tray runs in the shop, the vendor shall include at least 30% future growth capacity (DBM Deepcut L3023). Field-run cable tray (between main racks, tank farm, and electrical buildings) is the exception, not the rule (L2999).
- **Skid-edge example.** For a typical (non-flare) skid-edge connection from the pipe rack into a process module, the convention is: skid-edge block valve, 1 in. vent valve on the pipe-rack side, and a spectacle blind (DBM Deepcut L2454–L2455).
- **Heat-tracing example.** Heat-traced lines from two adjacent pipe racks should be combined where possible and wired to pipe-rack junction boxes in conduit; home-run cables are field-installed as needed (DBM Deepcut L3047).

## Conflict Table (for human ruling)

> No source-vs-source or source-vs-decomposition conflicts were observed in the slices read this pass. The table is provided for HRR compliance; populate when conflicts emerge in later passes.

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| — | None observed in this pass | — | — | — | — | TBD |

**Potential future entries to watch:**
- If the geotechnical report (when accessible) constrains foundation basis differently from the DBM default of driven steel piles (DBM Deepcut L2740), record the deviation here.
- If `26020-Package_Requirements.docx` (when text-accessible) specifies module-count / weight values that disagree with later EPC discipline production package values, record the deviation here.
- If detailed area-classification drawings reclassify any outdoor pipe-rack zone away from "general purpose," record the deviation against R-DS-03.
