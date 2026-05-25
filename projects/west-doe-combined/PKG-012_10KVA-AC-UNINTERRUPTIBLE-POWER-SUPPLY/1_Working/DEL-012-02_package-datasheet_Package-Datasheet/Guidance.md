# Guidance: Package Datasheet

## Purpose

The Package Datasheet exists to give the Package Vendor and discipline engineering team an EPC Integrator-controlled handoff basis for the `PKG-012` 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package. It should preserve accepted Gate 7 package identity, responsibility boundaries, and interface facts while leaving unsupported technical values as `TBD`.

## Principles

- Preserve the vendor/EPC split exactly: the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: PACKAGE_REGISTER.csv row for PKG-012; PROJECT_DECOMP.md Intake Summary.
- Treat Workbook Packages row 14 as the underlying authoritative row cited by Gate 7, but do not add values that are not present in the accepted Gate 7 snapshot or deliverable-local context.
- Carry interface facts in the datasheet because Gate 7 intentionally treats them as evidence, not separate deliverables. Source: DELIVERABLE_REGISTER.csv row for DEL-012-02 and ARTIFACT_REGISTER.csv rows ART-846E14C8E7 through ART-D5709F2B4B.
- Use objectives OBJ-002, OBJ-004, OBJ-005, OBJ-008, OBJ-009, and OBJ-010 as context for why the datasheet matters. Do not treat the objectives as direct clause-level equipment requirements unless supported by a package source slice.

## Considerations

The accepted Gate 7 basis establishes that this is a vendor-owned Electrical package under WBS 02 with four applicable interface types: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. Those facts are enough to initialize the datasheet structure and interface matrix, but they are not enough to specify detailed UPS electrical ratings, battery autonomy, environmental conditions, testing criteria, installation details, or vendor document requirements.

The datasheet should therefore separate:

- Accepted Gate 7 facts, which can be stated directly.
- Directionally relevant objective context, which can frame the handoff.
- Missing package-specific criteria, which must remain `TBD` until source-supported.

## Trade-offs

| Topic | Guidance |
|---|---|
| Completeness vs. source fidelity | Prefer `TBD` over filling common UPS attributes from generic practice. |
| EPC Integrator control vs. vendor design ownership | State handoff needs and interface obligations, but do not assign vendor design work to the EPC Integrator. |
| Interface evidence vs. standalone deliverables | Keep interface facts inside the datasheet and associated package evidence; do not create new deliverable obligations in this document. |
| Objective traceability vs. requirements | Use objective mappings to explain relevance, not to create unsupported technical requirements. |

## Examples

| Example entry | Acceptable use |
|---|---|
| `Interface type: Electrical Power` | Source-supported because INTERFACE_REGISTER.csv lists it for PKG-012. |
| `Battery autonomy: TBD` | Correct because Gate 7 does not provide a supported value. |
| `UPS output voltage: TBD` | Correct because Gate 7 does not provide a supported value. |
| `Package Vendor owns design and equipment` | Source-supported by PACKAGE_REGISTER.csv row for PKG-012. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-012-02-001 | Detailed UPS electrical and battery criteria are required for a usable vendor handoff, but they are not present in accepted Gate 7 rows available to this run. | Gate 7 PACKAGE_REGISTER.csv / PKG-012 row and ARTIFACT_REGISTER.csv / DEL-012-02 rows define identity, roles, artifacts, and interfaces. | Workbook Packages row 14 and DBM-Comp_and_Liquids source slices are cited by Gate 7 but were not copied into the deliverable and were not reinterpreted under the runtime instruction. | Datasheet Attributes; Specification Standards and Requirements; Procedure Steps | Keep unsupported values as TBD until a source-supported package datasheet basis is provided or human ruling authorizes source-slice extraction. | TBD |
