# Procedure — DEL-064-03 Construction Work Package

Operational procedure for the EPC Integrator to **produce** the Construction Work Package for PKG-064 "Tanks, Water (API 650) 4-25" and for that Construction Work Package to drive field installation, tie-in, inspection, and turnover.

## Purpose

This procedure governs (a) the assembly of the Construction Work Package document set (production), and (b) the field execution sequence the assembled package directs (operational use). Both interpretations are in scope per the four-documents skill's procedure-interpretation rule.

## Prerequisites

- Accepted decomposition snapshot: `GATE-07_Final_Published_2026-05-24` (per `_REFERENCES.md`).
- Deliverable-local truth set: `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_STATUS.md` present.
- Authoritative source slices read: PACKAGE_REGISTER row PKG-064; DELIVERABLE_REGISTER row DEL-064-03; SCOPE_LEDGER rows SOW-0233 .. SOW-0236; INTERFACE_REGISTER PKG-064 rows; DBM-Deepcut SEC-01 Construction Responsibility; DBM-Deepcut SEC-02 Atmospheric Tank and General Plant Spacing; DBM-Deepcut equipment/tag table rows 99 and 102; DBM-Deepcut Produced Water Tank section as analogy.
- Anticipated artifacts (`_CONTEXT.md`): construction work package; installation and tie-in workface plan; construction interface and turnover checklist.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` (DECLARED mode). The vendor-engineered package (DEL-064-04), the package datasheet (DEL-064-02), and the scope of work (DEL-064-01) are implicit upstream inputs by package construction logic; ASSUMPTION pending dependency declaration.
- Plot plan: status TBD (DBM-Deepcut SEC-02). Set-out checks use DBM-Deepcut SEC-02 spacing tables as the governing acceptance basis until the plot plan is issued.

## Steps — Producing the Construction Work Package

1. **Confirm equipment scope.** Cross-walk PACKAGE_REGISTER PKG-064 and DBM-Deepcut equipment/tag table row 102 to confirm tags TK-5317-1 and TK-5318-1 belong to PKG-064. Record the Datasheet ASSUMPTION explicitly.
2. **Carry design basis.** Transcribe SOW-0235 design parameters (modified API 650; 32 oz design / 1.0 oz vacuum; external insulation; freeze-protection heating; LP fuel-gas blanket; non-sour clean treated water) and SOW-0236 site/operating conditions (-40 °C to 60 °C; atmospheric operating; design throughput TBD) into the Construction Work Package Datasheet section.
3. **Carry interface scope.** For each of the nine PKG-064 interface rows in INTERFACE_REGISTER.csv, open one entry in the construction interface and turnover checklist with: interface type, boundary point (TBD until plot plan / piping isometrics issued), responsible craft, tie-in window placeholder, and the verification evidence expected.
4. **Carry responsibility split.** Transcribe the DBM-Deepcut SEC-01 Construction Responsibility table rows into a responsibility-assignment register inside the Construction Work Package, calling out (a) the items "by others" per SOW-0236 (foundations, mounting, electrical/instrumentation, platforms, staircases) as items the Tourmaline field construction scope picks up, and (b) the ISBL/OSBL interconnecting-piping row as `Confirm-per-tie-in` (Conflict CFL-064-03-02).
5. **Assemble the installation and tie-in workface plan.** One workface plan entry per equipment tag (off-loading, setting on foundation, mechanical hookup, instrumentation/electrical hookup, insulation/heat-trace install, blanket-gas connection) plus one per interface row (tie-in execution and verification). Sequence the workface plan against the construction window (sequence detail TBD pending project schedule).
6. **Build the turnover checklist.** Combine: (i) per-tag construction acceptance lines drawn from Specification R-064-03-02, R-064-03-03, R-064-03-04; (ii) per-interface sign-off lines from Step 3; (iii) per-by-others-scope completion lines from Step 4. Each line cites the source basis.
7. **Resolve or escalate conflicts.** Confirm each Conflict Table entry (`Guidance.md`) has either an EPC Integrator ruling or a documented `TBD` carried forward.
8. **Internal QA.** Cross-document consistency check (Datasheet ↔ Specification ↔ Guidance ↔ Procedure) per the four-documents skill Pass 2 checks. Confirm: equipment tags identical across documents; numeric values (capacity, design pressure, temperature range) identical; standards identical.
9. **Publish and update status.** Issue the Construction Work Package as the production document set. The deliverable `_STATUS.md` advances per the project lifecycle (no automatic state advance beyond `INITIALIZED` is performed by this skill).

## Steps — Field Execution Directed by the Construction Work Package

10. **Mobilize and lay down.** Receive vendor-shipped tanks and shipped-loose items. Inspect against vendor packing list and the Datasheet equipment table.
11. **Civil readiness.** Confirm foundations, plinths, grade, drainage, and spill containment are complete and signed off (DBM-Deepcut SEC-01 Construction Responsibility — Tourmaline field construction scope).
12. **Set tanks.** Off-load and set TK-5317-1 and TK-5318-1 on foundations. Set-out survey verifies position against (a) project plot plan when issued, (b) DBM-Deepcut SEC-02 spacing tables (≥ 2.35 m between atmospheric tanks; ≥ 30.48 m from pressurized bullets; ≥ 25 m flare-to-atmospheric-water-tank when applicable). Deviations logged.
13. **Mechanical hookup.** Mechanical connection of tank nozzles to interconnecting piping per the Process Piping interface row (IFC-53CAD5DFB7). Install platforms and staircases (SOW-0236 "by others" item carried into Tourmaline field construction scope).
14. **Containment and drains.** Complete drain/containment tie-ins (IFC-18BD52EF1B) and grading/site-drainage/spill-containment provisions (IFC-73210D3073).
15. **Relief / blanket / vent.** Connect LP fuel-gas blanket and relief/flare/vent path (IFC-570DF70935) per SOW-0235.
16. **Structural / supports.** Complete miscellaneous structural supports (IFC-BB6B4BD965).
17. **Electrical and grounding.** Install grounding and bonding (IFC-20C8E797F3); install area / exterior lighting circuits (IFC-0FE674AE2E); install cathodic protection (IFC-54E4476E7C); install I&C / control cabling (IFC-715AD7086B). Terminate per Tourmaline field construction scope.
18. **Thermal protection.** Install external insulation and freeze-protection heating; energise heat trace and confirm functional operation (SOW-0235 freeze-protection requirement; site temperature range -40 °C minimum per SOW-0236).
19. **Pre-commissioning checks.** Execute the construction interface and turnover checklist line-by-line. Witness inspections by the Package Vendor and EPC Integrator as applicable.
20. **Turnover.** Package the completed checklist, deviation log, and supporting evidence into the turnover dossier and hand off to the EPC Vendor Package Review and Acceptance deliverable (DEL-064-06); ASSUMPTION on downstream consumer per Conflict-free dependency reading.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Equipment scope coverage | Cross-walk between PACKAGE_REGISTER / DBM equipment table and the Construction Work Package equipment list | All tags listed; ASSUMPTION on tag-to-package mapping recorded |
| Design basis traceability | Vendor nameplate vs. SOW-0235 | Match on modified API 650; 32 oz / 1.0 oz vacuum |
| Insulation & heating | Visual inspection + heat-trace functional test | All circuits energise; insulation continuous |
| Blanket gas | Pressure / leak check on LP fuel-gas blanket connection | No leaks; blanket pressure maintained |
| Interfaces (nine types) | Per-interface sign-off in turnover checklist | Every PKG-064 interface row has a checklist entry signed by responsible craft and EPC Integrator |
| Spacing | Set-out survey vs. DBM SEC-02 spacing tables (and project plot plan when issued) | All spacing items satisfied or deviation logged |
| Responsibility execution | Responsibility-assignment register cross-check vs. DBM SEC-01 | All rows assigned; ISBL/OSBL tie-in piping confirmed per tie-in |
| By-others scope | Field walk-down | Foundations, mounting, E/I, platforms, staircases complete (SOW-0236) |
| Cross-document consistency | Pass-2 sweep (terminology, values, standards) | No unresolved drift between Datasheet, Specification, Guidance, Procedure |

## Records

The Construction Work Package SHALL produce:

- The construction work package document set itself.
- The installation and tie-in workface plan (per `_CONTEXT.md` Anticipated Artifacts).
- The construction interface and turnover checklist (per `_CONTEXT.md` Anticipated Artifacts).
- A responsibility-assignment register (derived from DBM-Deepcut SEC-01 Construction Responsibility).
- A spacing deviation log (referenced to DBM-Deepcut SEC-02 spacing tables).
- A turnover dossier feeding DEL-064-06 (downstream consumer; ASSUMPTION pending dependency declaration).
- A Conflict Table disposition record (from `Guidance.md`).
