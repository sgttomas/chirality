# Procedure: DEL-018-01_scope-of-work — Scope of Work

## Purpose

Define the working procedure to produce and verify the `PKG-018 — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD` EPC scope-of-work deliverable.

## Prerequisites

- Accepted Gate 7 decomposition snapshot dated 2026-05-24.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 register rows for `PKG-018`, `DEL-018-01_scope-of-work`, and `SOW-0019`.
- Interface rows for PKG-018 in `INTERFACE_REGISTER.csv` (six declared interface types).
- Artifact rows for DEL-018-01_scope-of-work in `ARTIFACT_REGISTER.csv` (four expected artifacts).
- Accessible DBM source slice: `3-25_Comp_and_Liquids_DBM.md`, Electrical sections (Medium-voltage service; 4160V MCC; SCA-001 VE #34 and VE #37; BPCS/RIO platform; cable separation).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Declared downstream dependencies: none declared in `_DEPENDENCIES.md`.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` (DEL-018-01_scope-of-work).
2. Confirm package identity against `PACKAGE_REGISTER.csv`: `PKG-018`, MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD, Electrical, WBS 02, CoA tracking number `26020-02-30-009`.
3. Confirm SOW-0019 against `SCOPE_LEDGER.csv` and retain PKG-018 as a distinct flat project package.
4. Build the scope-of-work outline with these minimum sections: package identity, source basis, package function, scope inclusions, exclusions/deferred items, six declared interfaces, EPC vs Package Vendor responsibility split, integration narrative, verification, records, and open/TBD items.
5. Populate interface content from `INTERFACE_REGISTER.csv`: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
6. Populate medium-voltage service basis from `3-25_Comp_and_Liquids_DBM.md` Electrical SEC: 4,160 V, 3-phase, 3-wire, 60 Hz, LRG; inverter-drive motor class 250 - 5,500 hp.
7. Populate VFD context from SCA-001 VE #34 (starting VFDs for KM-2150 / KM-2250) and SCA-001 VE #37 (capacitor bank removal where VFDs present); record harmonic and reactive-power mitigation as detailed-design items.
8. Populate controls integration narrative from the BPCS/RIO platform basis (Allen-Bradley ControlLogix; Flex5000 RIO; PRP).
9. Insert `TBD` for tagged-equipment IDs (motor tag, drive tag), drive topology, sizing, harmonic mitigation, transformer arrangement, drive cooling, enclosure rating, and tie-in coordinates.
10. Record responsibility assignment exactly per `PACKAGE_REGISTER.csv` PKG-018: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration.
11. Check the scope narrative against OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 only as directionally relevant context from the accepted objective maps.
12. Add a human-ruling entry for each unresolved tag association, interface-split change, or exclusion question that blocks final issue.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable and package identifiers match `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. |
| Interface check | All six declared interface types are included; no unsupported interface type is added. |
| Source fidelity check | Medium-voltage service, MCC, VFD, BPCS/RIO, and cable-separation requirements cite `3-25_Comp_and_Liquids_DBM.md`; package-specific values not found in sources remain `TBD`. |
| Responsibility check | EPC vs Package Vendor split matches `PACKAGE_REGISTER.csv` PKG-018 verbatim. |
| Dependency check | No blockers are asserted because no declared upstream dependencies exist. |
| Tag association check | Tagged-equipment IDs remain `TBD`; any SCA-001 VE #34 association to PKG-018 is flagged as ASSUMPTION pending human ruling. |
| Cross-document check | Datasheet attributes, Specification requirements, Guidance considerations, and Procedure steps use consistent package name, identifiers, interfaces, and `TBD` items. |

## Records

- Completed scope-of-work deliverable.
- Source basis list (Gate 7 registers + DBM Electrical sections).
- Interface summary covering all six declared interfaces.
- EPC vs Package Vendor responsibility assignment record.
- `TBD` and human-ruling list (including tag association, exclusions, and any interface-split changes).
- Review/approval evidence at vendor handoff (DEL-018-02) for tagged-equipment IDs and any closed `TBD` items.
