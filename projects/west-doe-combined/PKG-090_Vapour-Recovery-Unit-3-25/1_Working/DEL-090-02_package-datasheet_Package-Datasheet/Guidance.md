# Guidance — DEL-090-02 Package Datasheet (Vapour Recovery Unit 3-25)

> Directional guidance for preparing and using the EPC Package Datasheet for the 3-25 VRU. Drawn from the 3-25 Comp_and_Liquids DBM and the decomposition row for DEL-090-02. Rationale that cannot be substantiated from accessible source is marked `TBD`.

## Purpose

The Package Datasheet exists so that a third-party vendor (or discipline package engineer) can engineer and design the 3-25 VRU package against a stable, traceable EPC-Integrator-controlled basis. It is the technical companion to the package Scope of Work (DEL-090-01) and the upstream anchor for the Construction Work Package (DEL-090-03), the Vendor Engineered Equipment Package (DEL-090-04), the Vendor Document Turnover Package (DEL-090-05), and EPC Vendor Package Review and Acceptance (DEL-090-06).

## Principles

1. **Source authority over convention.** When the 3-25 DBM states a fact (count, configuration, driver type, recycle path, fuel-gas blanket, suction-header behavior, discharge routing), the datasheet reflects that fact. Generic compressor-package convention is not authority.
2. **Carry interface facts here, not in standalone deliverables.** Per `_CONTEXT.md` "Notes", interface facts for the VRU are intentionally evidenced inside this datasheet (Section R-7.2 of `Specification.md`). The interface requirements matrix is the place where suction, discharge, utilities, flare, and drain interfaces are made explicit.
3. **Supersession discipline.** Do not reintroduce removed scope (local 03-25 SOC, local 03-25 condensate stabilization, local 03-25 instrument-air compressors, 03-25 heat-medium). The DBM lists these as removed/superseded under the current SCA basis.
4. **Honest gaps.** Where the accessible source slice does not state a design value (suction/discharge pressure, capacity, composition envelope, tag list), leave `TBD` with `location TBD`. Do not invent or back-calculate values from generic VRU practice.
5. **Sour-service awareness.** Methyl mercaptan toxicity context applies to vents, purge, and analyzer planning. Carry this awareness into the vendor handoff even where exact numbers are pending.

## Considerations

- **Discharge interface to 04-25.** Discharge routing to the 04-25 SOC suction is governed by SCA-002. The vendor needs the 04-25 SOC suction pressure envelope and tie-in tag to size compression staging and discharge controls. These values are not present in the accessible DBM slice and should be confirmed from the 04-25 SOC datasheet or the inter-facility interface document before vendor issue.
- **Recycle valve fail action.** DBM SEC-05 indicates compressor recycle valves are expected to fail open with final failure action TBC. The VRU-specific recycle fail action is not isolated in the accessible source slice and is captured as `TBD` in Specification R-3.4.
- **Suction-header LP-flare bypass.** The V-ball bypass on the VRU suction header is operated by VRU suction pressure. The setpoint, valve size, and Cv profile depend on the LP-flare header capacity and the VRU turndown envelope; both are detail-design items, not datasheet values.
- **Free-drain / slope to flare KO.** The DBM directs free-drain or slope toward the flare KO interface but leaves the physical routing to detailed design. The datasheet should specify the requirement, not the geometry.
- **Make-up / blanket fuel gas.** LP fuel-gas pressure envelope is documented in DBM SEC-07; the regulator setpoint and turndown match-up belong in detailed design.
- **Sour-water and produced-water tank vapours.** VRU suction includes produced-water tank vapour service. Vapour composition envelope (H2S, mercaptans, water) is the controlling input for materials selection and is not in the accessible DBM slice — flag as `TBD`.

## Trade-offs

| Trade-off | Direction taken in datasheet | Rationale |
|---|---|---|
| Local 03-25 SOC vs. routing to 04-25 SOC | Route VRU discharge to 04-25 SOC suction | SCA-002 supersedes local SOC; DBM SEC-01 |
| Local 03-25 instrument-air vs. centralized 04-25 IA | Centralized from 04-25 | SCA-006; DBM SEC-07 |
| Specify detailed valve setpoints vs. interface intent | Specify interface intent only | Setpoints are detail-design outputs; datasheet stays at the EPC-handoff level |
| Carry interface facts in this datasheet vs. as separate deliverables | Carry here | `_CONTEXT.md` Notes; package decomposition policy |
| Use generic VRU convention to fill TBD values | Do not — leave `TBD` | Source-authority and honest-gap principles |

## Examples

Two illustrative examples from the source set, used to anchor the datasheet's interface language:

1. **Discharge tie-in description (illustrative):** "VRU discharge routes to the 04-25 SOC suction in accordance with SCA-002." (Wording supported by DBM SEC-01 and SEC-06.)
2. **Suction-header behavior (illustrative):** "VRU suction header includes an LP-flare bypass V-ball valve operated by VRU suction pressure and shall free-drain or slope to the flare KO interface." (Wording supported by DBM SEC-06.)

These illustrate the level at which the datasheet states facts; downstream documents add detail.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-090-02-01 | Recycle-valve final fail action for VRU is not isolated in accessible source. DBM SEC-05 states compressor recycle valves "expected to fail open; final failure action remains TBC." VRU-specific behavior may or may not match. | `3-25_Comp_and_Liquids_DBM.md` SEC-05 (inlet compression recycle) | DBM SEC-06 (Vapour Recovery — no explicit fail-action) | Specification R-3.4; Datasheet "Recycle valve fail action" | PROPOSAL: carry as `TBD` until VRU-specific fail action is confirmed against vendor recommendation and SIL/HAZOP review. | TBD |
| C-090-02-02 | Decomposition source pointer cites `26020-Package_Requirements.docx` heading 43 and `26020-Packages_Interfaces_4_export.xlsx` as primary package-requirement sources, but neither is locally accessible as text. The DBM is accessible; the 26020 documents are not. | Decomposition row (DEL-090-02) | `_REFERENCES.md` (lists 26020 sources without local text accessibility) | All requirement statements that would otherwise be backed by 26020 content | PROPOSAL: ground requirements in DBM where DBM speaks; mark all 26020-derived specifics as `TBD` / `location TBD` until the source slice is accessible. | TBD |
| C-090-02-03 | Objective association (OBJ-002 through OBJ-010) is recorded in `_CONTEXT.md` via the package-heuristic mode rather than from an explicit deliverable-ID-to-objective mapping. | `_CONTEXT.md` "Supports Objectives" | Decomposition snapshot `OBJECTIVE_DELIVERABLE_MAP.csv` (mapping granularity not verified) | Datasheet "Scope Items and Objectives Covered" | PROPOSAL: retain the association as ASSUMPTION (best-effort, package heuristic) per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`; confirm at human review. | TBD |
