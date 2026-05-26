# Guidance — DEL-103-03 Construction Work Package (PKG-103 Pipe Rack Modules)

> Directional guidance for authors and reviewers of the PKG-103 Construction Work Package. Rationale draws on accessible source slices; otherwise marked `TBD` or labeled **ASSUMPTION**.

## Purpose

The Construction Work Package translates PKG-103 scope (`DEL-103-01`) and the EPC Package Datasheet (`DEL-103-02`) into a field-executable plan for installing, hooking up, inspecting, turning over, and tying in the pipe rack modules to the larger facility. PKG-103 is a Mandatory Gate 5 EPC anchor deliverable defined by user instruction (`_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv`).

## Principles

1. **Source-grounded execution.** Construction decisions trace to the design basis (DBM Comp_and_Liquids; DBM Deepcut), workbook packages row 104, and the Gate 7 decomposition snapshot. Decomposition narrative routes; sources determine content. (Authority hierarchy from `four-documents/SKILL.md`)
2. **EPC Integrator ownership of rack design and construction.** Gate 6 disposition: pipe racks and pipe rack modules are designed exclusively by the EPC Integrator. Construction-planning trade-offs should not assume vendor-package ownership of the rack itself. (`INTERFACE_REGISTER.csv`)
3. **Modular delivery and field set.** Treat modules as fabricated upstream, shipped, off-loaded, and set on foundations under field construction scope. Workface planning should reflect crane/heavy-lift logistics, not loose-stick construction. (`DBM-Deepcut/4-25_Deepcut_DBM.md` lines 111-114)
4. **Skid-edge isolation discipline.** Place isolation between the rack and the module/unit/building, not deep inside the served system. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 2454)
5. **Cold-climate first.** Plan around -40 deg C minimum ambient and winter access for delivery, foundation work, and tie-ins. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 145, 696)
6. **Area-classification fidelity.** Default outdoor racks to general-purpose non-hazardous, but always defer to issued classification drawings where present. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722)
7. **Confirm rack-supported commodities against plot plan and model.** A repeated note across the package register and every interface row warrants treating this confirmation as a release gate. (`PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv`)

## Considerations

- **Foundations precede modules.** The final geotechnical report is required before foundation design closure; construction sequencing must respect that dependency. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 688)
- **Nine interface types in scope.** Each declared interface (Process Piping; Utility Piping; Relief/Flare/Vent; Electrical Power; EHT; I&C/Control Cabling; Communications/Network; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports) is a distinct turnover work-front. Plan distinct ITT and turnover checklists per interface. (`INTERFACE_REGISTER.csv`)
- **EHT scope is detailed-design-driven.** Specific rack-supported lines requiring electrical heat tracing emerge from detailed design; carry the EHT work front but acknowledge content is `TBD` until detail engineering closes. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145)
- **PKG-103 anchor role.** Because PKG-103 is the structural backbone supporting interconnects across many process modules, its construction work package should explicitly identify which downstream packages depend on rack readiness for their own tie-ins. Specific downstream identifications are `TBD` (not declared in `_DEPENDENCIES.md`).
- **Source binaries not extracted.** `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` are present in `_Sources/` but were not parsed during this drafting pass; values that would require them remain `TBD`.

## Trade-offs

| Trade-off | Notes |
|---|---|
| Module pre-assembly vs. field fit-up | Pre-assembly reduces field hours but raises lift weight/size and freight risk. Source default favors modular setting on foundations. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 113) |
| Winter vs. summer setting windows | Winter setting accommodates schedule but requires winter-specific provisions (cold-weather permits, frost-protected foundations); summer setting compresses tie-in window before freeze-up. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145) |
| Skid-edge vs. inboard isolation | Skid-edge isolation simplifies module pre-commissioning and turnover; inboard isolation may reduce valve count but complicates module independence. Source direction favors skid-edge. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 2454) |

## Examples

- Mechanical-hookup example: when a process module is set adjacent to a pipe rack, interconnecting piping is field-fit between skid-edge isolation on the module and the rack header, with welds inspected per project NDE specs (NDE spec `TBD`).
- Turnover checklist example per interface type: for Electrical Power (IFC-3268483707), record raceway continuity, cable pull and termination records, megger results, and tie-in to upstream power distribution package — specific acceptance criteria `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Rack design responsibility: package-register `Responsibility` field states "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources," while interface-register Gate 6 disposition states "pipe racks and pipe rack modules are designed exclusively by the EPC Integrator." | `PACKAGE_REGISTER.csv` PKG-103 row | `INTERFACE_REGISTER.csv` IFC-1B5D83EC66 (and all eight other PKG-103 interface rows) | Datasheet: Responsible Party / Design ownership; Specification REQ-CWP-12; Guidance Principle 2 | Treat Gate 6 disposition (EPC Integrator only) as authoritative for PKG-103 rack design and rack-construction execution, because it is the more recent and PKG-103-specific disposition. | TBD |
| C-002 | EHT scope and acceptance criteria: design basis names EHT as a winterization driver but accessible sources do not enumerate which rack-supported lines require EHT nor the acceptance criteria. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145 | (no positive enumeration in accessible sources) | Specification REQ-CWP-10; Procedure EHT steps | Carry REQ-CWP-10 as a work-front shape; mark specific line lists and criteria `TBD` pending detailed engineering. | TBD |
| C-003 | Objective association granularity: `_CONTEXT.md` lists seven supporting objectives at the deliverable level; `OBJECTIVE_DELIVERABLE_MAP.csv` rows are package-grouped (every DEL-103-* maps to the same objectives). | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped) | Datasheet Identification; objective-traceability claims | Per `four-documents` skill default `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`, record the seven objectives as **ASSUMPTION (best-effort mapping)** rather than hard requirements. | TBD |
