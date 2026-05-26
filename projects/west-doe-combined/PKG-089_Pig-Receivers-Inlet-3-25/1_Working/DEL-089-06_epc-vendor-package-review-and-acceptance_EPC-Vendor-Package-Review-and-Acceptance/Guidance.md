# Guidance — DEL-089-06 EPC Vendor Package Review and Acceptance (PKG-089)

## Purpose

Provide direction to the EPC Integrator (and reviewing operating authority) on how to perform the review-and-acceptance of the PKG-089 vendor pig-receiver package such that the resulting acceptance record is auditable, source-grounded, and aligned with the 03-25 facility DBM basis.

## Principles

- **Acceptance is integrative, not duplicative.** The vendor owns design correctness within its scope; the EPC Integrator confirms the package meets the EPC SOW and the facility's DBM-derived interface basis (DBM 3-25 SEC-04 — Inlet Pipeline Interface and Pigging).
- **Source authority over convention.** Where DBM 3-25 SEC-04 specifies a configuration (single combined three-phase receiver, non-enclosed structural skid, sweet-gas purge, HP flare vent, full-port piggable ESDV with position transmitters), that is the acceptance datum. Generic vendor conventions do not override it.
- **Explicit handling of TBD/TBC.** Receiver size, delivery-point ESDV shutdown pressure, and final inlet pipeline configuration are open in the current DBM. Acceptance shall not silently close these; each must be carried as a hold point until detailed engineering provides the value.
- **Human approval is binding (K-AUTH-1).** The Integrator's acceptance proposal is reviewed and approved by the responsible operating authority. Agents and tools propose; humans accept.

## Considerations

- **Sour service.** The 03-25 inlet is sour. Material selection, NDE coverage (PWHT/PMI where applicable), and gasket selection should be reviewed against sour-service requirements. Specific clause-level requirements: **location TBD** (CSA Z662 cited in DBM for outlet; receiver applicability is `ASSUMPTION: likely applicable`).
- **Pigging and flowback transients.** The DBM places no explicit pigging slug volume beyond separator slug handling; frac flowback is the governing transient liquid case. Review of vendor receiver volume, barrel L/D, and trap-door operability should be consistent with operator-managed pigging cadence rather than a worst-case slug capture.
- **Interface boundary.** Plant inlet boundary is the first aboveground flange within the lease boundary. Verify the vendor's terminal flange matches the Doe field pipeline contractor's handoff flange spec (size, rating, face).
- **Purge and flare interfaces.** Confirm sweet-gas purge supply pressure and HP flare backpressure assumptions in the vendor design match the as-installed utility headers. Mismatches drive RFIs, not field rework.
- **ESDV functional class.** Full-port + piggable + position transmitters is non-negotiable per DBM. Trim selection and actuator sizing remain vendor-engineered; review hydrotest, stroke, and fail-safe direction records.

## Trade-offs

- **Schedule vs. completeness of TBD closure.** Accepting the package before detailed engineering closes receiver size and delivery-point ESDV shutdown pressure creates rework risk; deferring until full closure may delay turnover. The acceptance checklist should carry explicit conditional-acceptance language tied to those hold points.
- **Conservative NDE vs. cost.** Sour service argues for elevated NDE coverage; without an accessible clause-level standard slice (`location TBD`), default to the more conservative governing code referenced for adjacent piping (CSA Z662) until the project NDE spec is confirmed.
- **Single combined receiver vs. service-specific receivers.** DBM is explicit: single combined three-phase receiver. Do not entertain vendor proposals for split/duplicate receivers without a documented SCA-equivalent variance.

## Examples

- *Acceptable disposition:* Vendor GA shows full-port piggable inlet ESDV with two redundant position transmitters and fail-close action; reviewer accepts with a hold-point note pending delivery-point ESDV shutdown pressure resolution.
- *Conflict requiring escalation:* Vendor proposes enclosed building over the receiver skid. DBM 3-25 SEC-04 specifies a non-enclosed structural steel skid. Reviewer rejects and routes to human authority for variance disposition.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Receiver size is "TBD" in DBM; vendor will need a sized barrel to fabricate | DBM 3-25 SEC-04 (size TBD) | Vendor GA (TBD — not in scope here) | Datasheet attributes; Spec R-2.4 | Detailed-engineering hold point; size derived from detailed flow/pigging study | TBD |
| C-02 | Delivery-point ESDV shutdown pressure is TBC; inlet separator ESDV shutdown is 635 psig | DBM 3-25 SEC-04 ("Delivery-point ESDV shutdown pressure still TBC") | DBM 3-25 SEC-04 (635 psig at inlet separator ESDV) | Datasheet attributes; Spec R-2.5 | Confirm delivery-point shutdown in detailed design; carry 635 psig only as upstream reference, not as receiver setpoint | TBD |
| C-03 | Applicable governing code for receiver (CSA Z662 vs. ASME piping/vessel) not explicitly bounded in DBM | DBM 3-25 SEC-04 (CSA Z662 cited for outlet pipeline) | Project EPC SOW / QA plan (`location TBD`) | Spec Standards table; R-4.1 | Confirm code matrix in EPC SOW/QA before acceptance | TBD |
