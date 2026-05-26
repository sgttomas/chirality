# Procedure: DEL-053-01_scope-of-work — Scope of Work

## Purpose

Define the working procedure to produce and verify the `PKG-053 — Flare KO Drum (Cryo)` EPC scope-of-work deliverable.

## Prerequisites

- Accepted Gate 7 decomposition snapshot dated 2026-05-24.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 register rows for `PKG-053`, `DEL-053-01_scope-of-work`, and `SOW-0067` through `SOW-0070`.
- Accessible DBM source slice: `4-25_Deepcut_DBM.md`, especially SEC-01 (facility identity), SEC-02 (flare and incinerator spacing), and SEC-09 (Flare Systems, Drains, Tagged Equipment).
- Word source heading: `26020-Package_Requirements.docx`, package heading 8 (Flare KO Drum (Cryo)) — reference pointer; detailed slices not copied into deliverable-local references.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Declared downstream dependencies: none declared in `_DEPENDENCIES.md` (the Package Datasheet DEL-053-02 and downstream construction/vendor production units are implicit consumers per `DELIVERABLE_REGISTER.csv`).

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` (DEL-053-01_scope-of-work).
2. Confirm package identity against `PACKAGE_REGISTER.csv`: `PKG-053`, Flare KO Drum (Cryo), Mechanical, WBS 01, CoA tracking number `26020-01-17-001`.
3. Confirm SOW-0067 through SOW-0070 against `SCOPE_LEDGER.csv` and retain the package as a distinct flat project package.
4. Build the scope-of-work outline with these minimum sections: package identity, source basis, package function, scope inclusions, exclusions/deferred items, tagged equipment, interfaces, responsibility assignment, verification, records, and open/TBD items.
5. Populate tagged equipment from `4-25_Deepcut_DBM.md` SEC-09 (Flare Systems narrative and Tagged Equipment table): V-4110-1 (cryogenic flare KO drum) and H-4112-1 (electric immersion heater).
6. Populate package function and integration narrative from `4-25_Deepcut_DBM.md` SEC-09 Flare Systems: cryogenic-unit reliefs and molecular-sieve-dehydrated streams relieving below -45.5 deg C connect via a 610 mm (24 in) relief header to V-4110-1; cryogenic flare header combines with HP flare downstream of both KO drums before the common HP/cryo stack.
7. Populate interface content from `INTERFACE_REGISTER.csv` for PKG-053: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.
8. Populate drain basis from `4-25_Deepcut_DBM.md` SEC-09 Drains (Cryogenic drain row): segregated cryogenic flare header at 300# ANSI minimum, no heat tracing because water is not expected (mole-sieve dehydrated, less than 0.1 ppm H2O), personnel protection insulation only in accessible areas.
9. Populate spacing basis from `4-25_Deepcut_DBM.md` SEC-02 Flare and Incinerator Spacing: 10 m (32 ft) between flare KO drums and vegetation or other fire hazards (OGAOM Sec. 9.6.15).
10. Populate responsibility split from `PACKAGE_REGISTER.csv` PKG-053: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Use the source wording verbatim where practical.
11. Mark `TBD` for drum sizing, MAWP, MDMT, materials, nozzle schedule, immersion heater rating and control philosophy, instrumentation specification, structural/foundation loads, and tie-in coordinates. Route these items explicitly to DEL-053-02 (Package Datasheet) and downstream vendor/construction packages.
12. Carry the non-sour service basis from `SCOPE_LEDGER.csv` SOW-0070 but flag service classification for source-basis re-confirmation at the Package Datasheet stage.
13. Check the scope narrative against the supported objectives (OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010) only as directionally relevant context from the accepted objective maps (ASSUMPTION; package-grouping heuristic).
14. Add a human-ruling item for each unresolved responsibility, design-basis, or service-classification gap that blocks final issue.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable and package identifiers match `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. |
| Tagged equipment check | V-4110-1 and H-4112-1 are present and match `4-25_Deepcut_DBM.md` SEC-09 Flare Systems and Tagged Equipment table. |
| Service basis check | The "below -45.5 deg C" PSV threshold and the "molecular-sieve-dehydrated" condition are explicitly stated and cited to SEC-09 Flare Systems. |
| Interface check | All nine declared interface types are present and no unsupported interface type is added. |
| Battery limit check | Upstream tie-in (cryogenic relief header to V-4110-1) and downstream tie-in (cryogenic header combine with HP flare header before common stack) are both explicitly described. |
| Source fidelity check | Header sizing, drain class, heat-tracing exclusion, and spacing values cite `4-25_Deepcut_DBM.md` SEC-02 / SEC-09; package-specific drum/heater design values not found in sources remain `TBD`. |
| Responsibility check | Package Vendor vs EPC Integrator split uses `PACKAGE_REGISTER.csv` PKG-053 wording. |
| Dependency check | No blockers are asserted because no declared upstream dependencies exist; downstream Package Datasheet routing is recorded. |
| Cross-document check | Datasheet attributes, Specification requirements, Guidance considerations, and Procedure steps use consistent package name, identifiers, tags (V-4110-1; H-4112-1), interfaces, and `TBD` items. |

## Records

- Completed scope-of-work deliverable.
- Tagged equipment and package identity list.
- Source basis list.
- Interface summary covering the nine declared interface types.
- Responsibility assignment record.
- `TBD` and human-ruling list (drum design values, heater rating/control, service classification re-confirmation).
- Routing record showing which `TBD` items are handed to DEL-053-02 Package Datasheet and to downstream construction/vendor production units.
