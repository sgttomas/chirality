# Guidance: DEL-049-04 — Vendor Engineered Equipment Package

## Purpose

This guidance frames how the Package Vendor and the EPC Integrator should
think about the Vendor Engineered Equipment Package as a production unit, so
that engineering, design, documentation, and supply work proceed against the
EPC anchors (DEL-049-01 Scope of Work, DEL-049-02 Package Datasheet) without
the Vendor inadvertently absorbing EPC-owned facility integration work, and
without the EPC inadvertently absorbing Vendor-owned package engineering work.

The split is set by `PACKAGE_REGISTER.csv` (PKG-049 responsibility model) and
OBJ-004: the Package Vendor owns package engineering, package design, vendor
documentation, and the physical equipment package; the EPC Integrator owns
integration into the facility, interfaces, tie-ins, constructability,
procurement/construction coordination, and facility-level integration.

## Principles

1. **Anchor to the EPC SoW and Package Datasheet.** The engineered package is
   developed *from* DEL-049-01 and DEL-049-02. When the Vendor sees a gap or a
   contradiction in those EPC anchors, surface it back to the EPC rather than
   resolving it silently inside the vendor design basis. (Authority: PKG-049
   responsibility model.)

2. **Do not redefine EPC-owned interfaces.** Each of the 13 interface types
   carried for PKG-049 in `INTERFACE_REGISTER.csv` is an EPC-owned termination
   conversation. The Vendor terminates them; the EPC defines what is on the
   other side.

3. **Honor source-stated equipment intent.** SOW-0171 names specific equipment
   choices (Ariel KBX/X compressor, API 661 intercoolers, 0.3 µm @ 99.97 %
   coalescer, etc.). These are not Vendor design freedom — they are the
   source-stated intent and should be preserved unless a formal change is
   negotiated with the EPC.

4. **Vendor-sized items remain vendor-sized.** SOW-0171 explicitly leaves the
   suction scrubber, packing vent/drain separation pot, seal-pot waste-oil
   transfer pump, and filter-coalescer sizing to the Vendor. The Vendor owns
   the sizing calculation under the design conditions in SOW-0172.

5. **Boundary-of-supply discipline.** SOW-0172 lists items that are "by others"
   (shipping, pile installation, tie-in piping, field electrical, mounting
   platform/stairs). Keep these visible in vendor documentation so the EPC
   construction work package (DEL-049-03) can pick them up.

6. **Vendor documentation feeds the vendor-document turnover deliverable.** The
   vendor document register, submittal flow, and turnover records live in
   DEL-049-05. Treat that deliverable as the documentation home; this unit
   produces the technical content.

## Considerations

- **Sour-service context.** PKG-049 sits inside a sour-service facility scope
  (OBJ-009). Materials, inspection, and sealing decisions in the vendor design
  basis should reflect this even where the SOW lines do not enumerate it.
  Mark such decisions explicitly so EPC review under DEL-049-06 can validate
  them. (ASSUMPTION until confirmed against the DBM source slice.)

- **No turndown.** SOW-0172 states "no turndown" against a 140 MMSCFD design
  capacity. Operating philosophy decisions (start/stop strategy, on-line
  spare strategy) need to be coordinated with controls and operations scope
  (OBJ-006, OBJ-010) rather than absorbed silently in vendor controls
  programming.

- **Electrical and I&C interfaces are facility-owned.** Electrical Power, EHT,
  Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, and
  Fire & Gas / Safety Systems are interfaces on PKG-049 but their facility
  side is the EPC's. The Vendor provides termination points, loads, signal
  lists, and cause-and-effect; the EPC supplies, routes, and integrates them.

- **Maintenance access and structural foundations.** Both are PKG-049
  interfaces. The Vendor sets on-skid geometry; the EPC's civil/structural
  scope (OBJ-008) closes the foundation and access design.

## Trade-offs

- **Vendor-standard package vs. project-specific engineering.** Reciprocating
  compressor packages tend toward vendor standardization. Where a vendor
  standard collides with a source-stated intent (e.g., API 661 intercoolers,
  band-lock-type QOC coalescer), surface the gap rather than substituting a
  standard alternative. (Authority: SOW-0171.)

- **In-skid vs. EPC-supplied utilities.** Some utility services (instrument
  air, fuel gas, drains, vents) may be wholly EPC-supplied at the package
  boundary or partially fabricated into the skid. The split must reconcile
  to the Utility Piping, Relief/Flare/Vent, Drain/Containment, and Building
  HVAC/Services interface entries for PKG-049. Specific split: TBD until
  DEL-049-02 is produced.

## Examples

No source-grounded worked examples are available inside this deliverable's
scope. Examples will be added when the upstream RFQ / package requirements
slices and DBM sections are pulled into `_REFERENCES.md`.

## Conflict Table (for human ruling)

None identified during Pass 1/2. The decomposition registers, `_CONTEXT.md`,
and the SOW-0169..0172 source rows are internally consistent. The principal
open item — "no turndown" against operability/availability expectations — is
flagged as a Consideration above, not as a register-level conflict.
