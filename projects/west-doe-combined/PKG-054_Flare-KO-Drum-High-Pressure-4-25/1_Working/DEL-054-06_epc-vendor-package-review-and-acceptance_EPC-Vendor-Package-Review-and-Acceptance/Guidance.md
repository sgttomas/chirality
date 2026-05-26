# Guidance — DEL-054-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's binding evidence that the Package Vendor's engineered package and turnover documentation for the HP Flare KO Drum (HP) (`26020-01-PT-17-002`, `V-4100-1` + `P-4100-1`) satisfy the EPC anchor deliverables — Scope of Work (`DEL-054-01`), Package Datasheet (`DEL-054-02`), and Construction Work Package (`DEL-054-03`) — and are ready for integration into the broader 4-25 West Doe Deepcut HP flare system.

Source: `26020-Package_Requirements.docx` Heading 9 ("Location / Status", "Basic Scope"); `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

## Principles

- **Acceptance is integrator-led, not vendor-self-certified.** `_CONTEXT.md` and the decomposition register assign EPC Integrator as the lead responsible party with Package Vendor input.
- **Evidence is anchored to the source's enumerated artifacts.** The Heading 9 "Vendor Engineering Deliverables" list is the canonical artifact set. Acceptance does not invent new artifact requirements; it confirms the presence and adequacy of those artifacts.
- **Interface evidence follows the Heading 9 Physical Interface Summary.** Only interfaces marked `Yes` for `26020-01-PT-17-002` are in scope.
- **Numeric design values come from vendor submittals.** Until the vendor's `MEC-009`, `PRO-014`, `PRO-017`, `PRO-018`, etc., are accepted, numeric values remain `TBD` in this evidence pack rather than being asserted from decomposition prose. (ASSUMPTION — typical EPC practice; aligns with source Heading 9 deliverables list.)

## Considerations

- **HP/Cryo header tie-in.** Source notes that the HP flare header ties into the cryogenic flare header downstream of the HP KO drum before the common HP/Cryo flare stack. Acceptance must confirm this configuration in as-built P&IDs and isos, including downstream-impact considerations on the Cryo Flare KO Drum package (`26020-01-PT-17-001`, separate scope).
- **Outdoor EHT requirement.** Heat tracing and insulation of outdoor HP flare headers is an explicit source requirement. The acceptance pack must trace EHT design (`ELE-018`), schedule (`PIP-020`), and heat tracing interface (`PIP-021`) through to energization records.
- **Pressure equipment registration.** Source lists `REG-022` Pressure Equipment Registration Package — acceptance is contingent on registration acceptance by the applicable jurisdictional authority. (ASSUMPTION — authority identity, e.g., ABSA, not stated in source Heading 9.)
- **Transfer pump scope.** `P-4100-1` is a rotating-equipment sub-scope. Treat its acceptance evidence (FAT, NPSH, seal/lube, motor starting) as a dedicated subsection of the acceptance pack rather than mixed with vessel evidence.
- **Truck-out provision.** Source includes "truck-out provision" in Major Included Equipment. Acceptance evidence should confirm the physical and procedural provision (likely via IOM, GA drawings `MEC-016`, and Construction Work Package handoff).

## Trade-offs

- **Depth of vendor re-engineering review vs. timeline.** EPC Integrator review must be deep enough to find configuration mismatches against `DEL-054-02` but cannot substitute for vendor engineering. The default disposition for purely vendor-engineering details with consistent source-grounded inputs is "accepted on evidence" rather than re-derivation.
- **Open-items closure vs. carryover.** Items that cannot be closed before package handoff should be explicitly carried with named owners rather than left silent; this preserves traceability into commissioning.
- **Single acceptance bundle vs. staged acceptance.** A staged approach (engineering acceptance → fabrication acceptance → turnover acceptance) aligns with the artifact maturity progression in Heading 9. (ASSUMPTION — staging not mandated in source.)

## Examples

The Heading 9 "Vendor Engineering Deliverables" enumeration groups vendor artifacts by function (Core vendor documents; Core package engineering; Rotating equipment / pumps; Static pressure equipment; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls interfaces). The acceptance checklist should mirror this grouping so reviewers can audit one functional area at a time.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | No conflicts surfaced between the Heading 9 source slice and the decomposition register at Pass 1/2. | — | — | — | — | TBD |
