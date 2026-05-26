# Guidance — DEL-057-03 Construction Work Package (PKG-057 Stabilizers)

## Purpose

This Construction Work Package (CWP) exists so the EPC Integrator can carry the vendor-supplied Inlet Stabilizer Packages from receipt through installation, tie-in, inspection, and turnover into the integrated facility. The decomposition (`DELIVERABLE_REGISTER.csv` row `DEL-057-03`) frames it as the EPC anchor deliverable that describes how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. It is the construction half of the EPC anchor trio (Scope of Work → Package Datasheet → Construction Work Package).

## Principles

- **Vendor/EPC split is load-bearing.** The Package Vendor owns engineering, design, fabrication, and vendor documentation; the EPC Integrator owns integration into the operating facility. The CWP must not silently absorb vendor design work or push integration scope back to the vendor (OBJ-004).
- **Source-fidelity over convention.** Construction values (e.g., minimum stabilizer column pressure 793 kPag; design pressures of 1724 kPag at the flash feed separator) carry through from the source scope without being rounded, generalized, or backfilled with generic construction practice (`SOW-0180`).
- **Three identical packages.** The 3 x 40% configuration is a deliberate redundancy choice from the source basis; install plans, sparing, and turnover must preserve that three-stream identity rather than treating the units as interchangeable inventory (`SOW-0179`).
- **Interfaces are the construction product.** PKG-057's applicable interface list (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports) is the de facto scope checklist; construction completeness is measured against that list.
- **Safety and regulatory carry-through.** Sour-service, relief/flare/blowdown, fire/gas/shutdown, and environmental compliance must remain visible in the tie-in design and turnover evidence (OBJ-009).
- **Open items are closed in the evidence record.** OBJ-010 binds this package to the open-item and handoff readiness evidence consumed by `DEL-057-06`.

## Considerations

- **By-Others scope is asymmetric.** `SOW-0180` lists interconnecting piping at skid edge, DCS integration, foundations, electrical power supply from plant MCC, and installation/erection as "By Others" relative to the Package Vendor. From the EPC Integrator's perspective these are *core* CWP scope items.
- **20 floating valve trays** in the stabilizer column drive both lift and tray-installation choices, internals protection during shipping, and post-installation inspection (`SOW-0179`). The CWP should make explicit which tray work, if any, happens in field versus pre-fabricated.
- **VFD-driven feed pumps and product cooler fans** create coordination between the Electrical Power, I&C/Control Cabling, and Fire & Gas/Safety Systems interfaces. Loop-check sequencing should reflect that (`SOW-0180`).
- **Approach temperature** (16.7 °C / 30 °F minimum at the feed/bottoms exchanger) is a process boundary the CWP must not violate when commissioning thermal loops (`SOW-0180`).
- **Retention time** (~15 minutes at the flash feed separator) constrains commissioning fill, drain, and PSV/relief testing sequencing (`SOW-0180`).
- **Constructability constraints** (lifts, lay-down, sequencing) are TBD pending vendor input from `DEL-057-04`. The CWP should be re-validated against vendor lift plans before construction execution.

## Trade-offs

- **Field-erect vs ship-as-skid.** Source describes the units as "Inlet Stabilizer Packages" suggesting skidded delivery. The CWP should not assume otherwise unless vendor input changes the delivery form. PROPOSAL: treat skidded delivery as the planning baseline; revisit when `DEL-057-04` lands.
- **Single common foundation vs three independent foundations.** Source does not specify (`SOW-0180` lists foundations as By Others, no layout constraint stated). PROPOSAL: independent foundations preserve the 3 x 40% availability intent; record decision when civil basis (OBJ-008 / DBM SEC-11) is extracted.
- **DCS integration timing.** DCS integration is EPC scope; it can be staged early (point-to-point pre-energization) or late (loop checks during commissioning). PROPOSAL: stage early to flush out interface defects before vendor commissioning support is on site.
- **Turnover packaging granularity.** One turnover dossier per skid, or one consolidated dossier with three appendices. PROPOSAL: per-skid dossiers preserve the 3 x 40% identity and align with `DEL-057-06` review evidence.

## Examples

- TBD — no worked construction examples are available from the local source set. Examples will be added when DBM SEC-08 (Utilities), SEC-11 (Civil), SEC-12 (Electrical), and SEC-13/14 (Controls/Instrumentation) source slices are extracted to `_REFERENCES.md` for this deliverable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | "Installation / erection" listed as "By Others" relative to the Package Vendor (`SOW-0180`), while the EPC Integrator deliverable description (`_CONTEXT.md`, register row) makes the EPC Integrator responsible for physical installation. Both are consistent when read as the EPC scoping the install — but the wording could be misread. | `SOW-0180` Scope notes (Package Vendor perspective) | `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row `DEL-057-03` (EPC Integrator perspective) | Datasheet Construction; Specification REQ-CWP-03 | EPC Integrator owns installation/erection scope; "By Others" in `SOW-0180` is read relative to the Package Vendor. | TBD |
| CONF-02 | OBJ-009 implies sour-service classification, but the local SOW slices do not assert sour service for the stabilizer feed explicitly. | OBJ-009 (DBM SEC-09/SEC-14) | `SOW-0178`..`SOW-0180` (no explicit sour-service statement) | Specification REQ-CWP-09; Datasheet "Sour-service applicability" | Treat sour service as ASSUMPTION until DBM SEC-09/SEC-14 slice is extracted; default-include sour-service controls in tie-in design. | TBD |
