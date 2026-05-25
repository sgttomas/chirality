# Guidance: Construction Work Package

## Purpose

The Construction Work Package exists to turn the accepted PKG-022 5kV switchgear equipment scope into construction-facing installation, tie-in, inspection, and turnover evidence without confusing EPC integration responsibilities with Package Vendor design and equipment-package responsibilities.

## Principles

- Preserve the Gate 7 responsibility boundary. Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package delivery; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
- Treat the package as electrical construction work. The relevant Gate 7 interface types are Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- Use the Construction Work Package to coordinate installation and handoff evidence, not to create vendor design criteria unsupported by source slices.
- Carry unsupported source-dependent details as TBD until source slices, vendor documents, or human rulings are available.
- Apply declared dependency blockers only when they are explicitly recorded. None were declared during PREPARATION for this deliverable.

## Considerations

| Topic | Guidance |
|---|---|
| Electrical Power | Include planning/checklist coverage for 5kV power-interface readiness, cable routing/tie-in prerequisites, energization boundaries, and turnover evidence. Specific cable IDs, switchgear lineups, relay settings, testing steps, and energization sequence are TBD. |
| Grounding / Bonding | Include planning/checklist coverage for grounding and bonding interfaces. Specific grid tie points, conductor sizes, test values, and inspection forms are TBD. |
| I&C / Control Cabling | Include coordination coverage for control-cabling interfaces to package or facility systems. Specific termination schedules, loop checks, and control-system dependencies are TBD. |
| Communications / Network | Include coordination coverage for communications/network interfaces where required by the package. Specific network architecture, addressing, fiber/copper media, and test criteria are TBD. |
| Maintenance Access | Include constructability and turnover checks confirming access is not blocked by installation sequencing or adjacent systems. Detailed access envelopes are TBD. |
| Structural / Foundations / Supports | Include installation readiness checks for foundations, supports, anchorage, housekeeping pads, embeds, or other supports as applicable. Specific civil/structural criteria are TBD. |
| Safety, regulatory, and turnover | OBJ-009 and OBJ-010 provide directionally relevant context for safety/compliance and handoff readiness, but source-backed details remain TBD. |

## Trade-offs

- A more detailed construction package would be easier to execute in the field, but adding unsupported installation values would violate source fidelity. The current package should remain conservative until source-supported construction details are available.
- A broader dependency list might reveal real sequencing needs, but coordination mode is DECLARED. Undeclared relationships should be handled as open coordination items, not blockers.
- Vendor documents may be necessary for complete installation instructions, but the EPC package should avoid rewriting or superseding vendor-owned package engineering.

## Examples

| Example item | Treatment |
|---|---|
| "Verify grounding interface readiness" | Acceptable as a planning/checklist line because Grounding / Bonding is an accepted Gate 7 interface type. Specific resistance limits remain TBD. |
| "Install switchgear per vendor manual section X" | TBD until the vendor manual or source slice is available. |
| "EPC shall design switchgear internals" | Not acceptable; Gate 7 assigns package engineering/design to the Package Vendor. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-001 | Detailed construction source slices are not locally resolved, but the four-document kit must be initialized. | _REFERENCES.md, Missing / Deferred References | User task instruction, Expected result | Datasheet Conditions; Specification Requirements; Procedure Steps | Use Gate 7 and deliverable-local files for Phase 2.2, keep source-dependent construction details TBD. | TBD |
| HR-002 | Electrical installation standards, vendor installation manuals, and commissioning/energization requirements are not available in the deliverable-local source set. | _REFERENCES.md, Missing / Deferred References | DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package` requires construction installation/inspection/turnover package | Specification Standards; Procedure Verification | Do not infer clause-level requirements; require human/source resolution before detailed construction release. | TBD |
