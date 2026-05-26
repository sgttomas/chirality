# Guidance — DEL-073-02 Package Datasheet (PKG-073 Amine Treating Unit)

## Purpose

This Package Datasheet exists so that the EPC Integrator can hand a third-party Package Vendor a single, source-grounded technical basis sufficient for the vendor to engineer, design, and document the Amine Treating Unit (ATU) and for the integrator to wire the package into the surrounding facility without re-deriving design intent. It is the EPC anchor between project decomposition truth and vendor execution for PKG-073.

Source: `_CONTEXT.md` §Scope; `DELIVERABLE_REGISTER.csv` row DEL-073-02.

## Principles

- **Source authority over convention.** Numeric and configuration values reflect the project Design Basis Memorandum (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`). When a value is not available there, mark it `TBD` rather than fill from generic amine-unit convention.
- **H₂S removal priority.** The package is sized and tuned for H₂S removal first; CO₂ slip is acceptable provided sales gas CO₂ stays ≤2 mol%.
- **Operate above the hydrate and HC-dewpoint margin.** Sour inlet gas approaches the absorber close to both hydrate and HC dewpoint; the ~6 °C margin convention drives inlet temperature control and motivates the absence of methanol injection in this area.
- **Carry interface facts on the datasheet.** By project convention (`_CONTEXT.md` Notes), interface facts are carried here as evidence rather than spun out as separate deliverables. The datasheet must therefore be sufficient for the integrator to drive `DEL-073-03` (construction work package) and `DEL-073-06` (review/acceptance).
- **Vendor scope vs. integrator scope is sharp.** The vendor owns engineering, design, vendor documentation, and the physical equipment package; the integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination (`PACKAGE_REGISTER.csv` row 49).

## Considerations

- **Solvent selection (MDEA).** MDEA enables selective H₂S removal with controlled CO₂ slip. The trade-off (see below) is sensitivity to CO₂/H₂S ratio, mercaptan, and amine quality.
- **Two 50% absorbers.** Sparing is 2 × 50%, not 2 × 100%. Turndown and maintenance windows must be planned accordingly; loss of one absorber halves capacity rather than maintaining full throughput.
- **Three × 57.5% charge pumps.** The unusual 3 × 57.5% configuration is a turndown/availability trade and constrains pump sizing/model selection; the model remains `TBC` and must be confirmed early in vendor engineering.
- **Reboiler skin temperature limit.** 350 °F heat-medium supply and skin <350 °F is mandatory to prevent MDEA degradation; vendor reboiler design must include heat-medium mixing valves.
- **Reflux accumulator high-CO₂ behavior.** For high-CO₂ acid gas, dilution-gas review is required for the reflux accumulator pressure-control path to the LP flare.
- **Waste streams are project-level.** Waste amine, HC drains, and acid gas exits leave the package boundary and must align with the facility's slop tank, produced-water storage, LP flare, and acid-gas compressor (PKG-046).
- **Sweet gas scrubber.** Not included as a separate item in the current basis; downstream TEG inlet filter/coalescer absorbs the carryover-protection role. Vendor should not propose adding a scrubber without surfacing it as a change.

## Trade-offs

| Decision | Pro | Con / Risk |
|---|---|---|
| MDEA over generic DEA / MEA | Selective H₂S, lower regeneration energy, CO₂ slip allowed | Sensitivity to CO₂/H₂S ratio shifts and mercaptan loading; performance margin in turndown `TBC` |
| 2 × 50% absorbers vs 2 × 100% | Lower capex/footprint | No single-train fallback at full rate |
| 3 × 57.5% charge pumps | Smaller individual machines, simpler maintenance | Non-standard sparing complicates pump model selection |
| Two water-wash stages in regenerator | Reduces amine loss in overheads | Additional stages may be required for amine-loss economics (`TBC`) |
| No methanol injection at inlet | Avoids contamination, simpler chemistry | Operations must hold the ~6 °C hydrate margin without chemical fallback |
| Carry interfaces on the datasheet | Single hand-off artifact for the vendor | Datasheet grows in scope; must be tightly versioned |

## Examples

- **Sweet gas spec example.** A vendor process simulation that returns 5 ppmv H₂S at the absorber outlet on the design feed does not meet R-PKG-073-02-002 (≤4 ppmv) and triggers a vendor design iteration.
- **High-CO₂ case example.** When CO₂ and H₂S are swapped from the design case (acid-gas-compressor "high-CO₂ case"), the reflux accumulator must still hold pressure within its control band to the LP flare; vendor must demonstrate this, including dilution gas review.
- **Sparing example.** With one of two absorbers offline, the unit produces approximately 50% of the design treated-gas rate; this is consistent with R-PKG-073-02-007 sparing, not a vendor failure.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-073-02-01 | `Datasheet.md` Construction lists "Sweet gas scrubber: Not included" while `4-25_Deepcut_DBM.md` Module 520 row also lists "1 sweet gas scrubber" in the equipment count. The `Amine Equipment and Design Requirements` table says the scrubber is NOT included as a separate item. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Module 520 row | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Amine Equipment and Design Requirements" — "Sweet gas scrubber" row | Datasheet Construction; Specification R-PKG-073-02-007 | PROPOSAL: follow "Amine Equipment and Design Requirements" (no separate sweet gas scrubber); treat Module 520 count as a residual carry-over | TBD |
| C-073-02-02 | Binary sources `26020-Package_Requirements.docx` heading 27 and `26020-Packages_Interfaces_4_export.xlsx` are referenced as authoritative but were not locally parsed in this run, so the interface schedule values and any package-specific clauses they carry remain `TBD`. | `_REFERENCES.md` | accessible sources (DBM) | Datasheet Conditions/Interfaces; Specification R-PKG-073-02-013; Standards table | PROPOSAL: extract these in a follow-on TASK with a docx/xlsx-parsing tool before Gate 5 | TBD |
| C-073-02-03 | Sparing for "3 × 57.5% amine charge pumps" totals 172.5%, which exceeds typical N+1 conventions; source basis does not justify the 172.5% rationale. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Amine Equipment and Design Requirements" | (no second source) | Datasheet Construction; Specification R-PKG-073-02-007 | PROPOSAL: carry as written from source; flag for vendor confirmation during engineering | TBD |
| C-073-02-04 | Objective associations (`OBJ-001`/`003`–`010`) inherited via `PACKAGE_HEURISTIC`; the GATE-07 objective-deliverable map was not directly inspected at the DEL-073-02 row in this run. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (not opened) | Datasheet Coverage | PROPOSAL: confirm via a TASK that opens the objective-deliverable map; if not directly mapped, retain as ASSUMPTION | TBD |
