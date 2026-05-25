# Guidance: DEL-011-02_package-datasheet - Package Datasheet

## Purpose

The package datasheet exists to convert the accepted package/decomposition basis for `PKG-011` into a source-grounded technical handoff for vendor or discipline package engineering. It should be detailed enough for vendor design initiation and EPC integration review, while avoiding unsupported final ratings, settings, or configuration choices that belong to detailed electrical studies or vendor submittals.

## Principles

- Use the Gate 7 registers for identity, responsibility split, deliverable purpose, artifact expectations, and interface facts.
- Use DBM SEC-12 electrical basis slices for electrical system, voltage, incoming feed, MCC, area classification, building/raceway, grounding/bonding, and study requirements.
- Treat project electrical specifications listed in the DBM as governing standards, but do not derive clause-level requirements from them until their bodies are locally available.
- Keep package-specific values as `TBD` when the accessible source set does not provide them.
- Preserve the EPC/vendor split: the EPC Integrator authors the datasheet and integration basis; the Package Vendor develops the engineered equipment package and vendor documentation.

## Considerations

The package name is "4160V SWITCHGEAR EQUIPMENT", while the 03-25 DBM source slice describes a "4160V MCC" serving large 4000V motors. The current deliverable should carry both terms carefully: use the package name for the workbook/Gate 7 package identity and use "4160V MCC" only where citing the DBM source basis.

The 03-25 electrical system is supplied from 04-25, so the datasheet should not be written as an isolated facility package. It should expose incoming power, grounding/bonding, control cabling, communications/network, maintenance access, and structural/foundation interfaces for integration.

The 03-25 source records harmonic/reactive-power mitigation as a detailed-study item. The 04-25 electrical basis likewise requires electrical studies before final equipment ratings and suitability are finalized. Treat final bus, breaker, interrupting, arc-flash, relay, VFD, and enclosure details as engineering closeout items unless accepted source evidence becomes available.

## Trade-offs

| Topic | Direction |
|---|---|
| Early vendor handoff versus final engineering certainty | Provide the source-supported basis now, but mark final values and settings as `TBD` pending studies/vendor data. |
| Package identity versus DBM terminology | Preserve `4160V SWITCHGEAR EQUIPMENT` as package identity and cite `4160V MCC` only as the DBM source term. |
| Interface completeness versus overclaiming | Include all Gate 7 interface facts, but do not add undeclared interface types as blockers or requirements. |
| Standards listing versus clause extraction | List available DBM standards/specifications; defer clause-level obligations until project specification bodies are accessible. |

## Examples

Example acceptable datasheet wording:

> The package shall carry the 4,160 V, 3 phase, 3 wire, 60 Hz, low-resistance grounded service basis for process AC inverter-drive motors from 250 hp to 5,500 hp. Final ratings and protection settings are TBD pending detailed electrical studies.

Example wording to avoid:

> The package is fully rated for a specific interrupting current.

Reason: the accessible source slices require short-circuit and related studies before finalizing equipment ratings and suitability, but do not provide the final interrupting rating.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-011-02-001 | Package identity says 4160V switchgear equipment; DBM source basis describes a 4160V MCC. | `PACKAGE_REGISTER.csv`, `PKG-011` | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC | Datasheet Attributes; Specification Requirements; Procedure Steps | Treat workbook/Gate 7 package name as package identity and DBM 4160V MCC as source technical basis until human confirms whether the package should be titled switchgear, MCC, or both. | TBD |
