# Guidance — DEL-023-01 Scope of Work (PKG-023)

Directional guidance for the author/reviewer of the EPC Integrator Scope of Work for PKG-023 "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD". Intent: keep the Scope of Work source-anchored, preserve the vendor/integrator boundary, and surface — not paper over — open questions about the package's driven service and electrical context.

## Purpose

The Scope of Work is the EPC Integrator's anchor for PKG-023. It establishes the package's identity, function, boundary against the rest of the facility, and the integrator-vs-vendor responsibility split that downstream Gate 5 deliverables (Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Vendor Package Review and Acceptance) inherit.

## Principles

1. **Source authority over decomposition prose.** The Gate 7 registers carry the package identity and interfaces; the Deepcut DBM carries facility-level electrical design rules. Where they disagree, follow the rule from the DBM-cited slice and surface the discrepancy in the Conflict Table.
2. **Title is not a specification.** "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" is a workbook title only. Do not derive harmonic class, topology, cooling method, or bypass arrangement from the title.
3. **Boundary discipline.** PKG-023's Scope of Work defines what crosses the package boundary; it does not author vendor internal design. Push interface details into the Package Datasheet, not into this deliverable.
4. **Mandatory anchor.** PKG-023 is a Gate 5 mandatory anchor; the four EPC anchor deliverables (SoW, Package Datasheet, Construction Work Package, EPC Vendor Package Review and Acceptance) must be self-consistent.

## Considerations

- The Deepcut DBM does not assign a 1,500 HP MV VFD to a specific service. Where the DBM names MV motors with VFDs, it cites the inlet/sales compressor "Starting VFD with synchronous transfer" arrangement at 6,700 HP — not 1,500 HP. The 1,500 HP MV VFD therefore appears to be a separate, smaller MV-motor service whose driven equipment is not identified in the accessible DBM slice (HRR-023-01-001).
- The DBM explicitly leaves "VFD and soft-starter requirements for 4.16 kV motors" as TBD (lines 2957 and 3088). Treat this as the governing posture: do not specify MV VFD topology or harmonic mitigation in this deliverable.
- Six interface types apply (Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports). Each becomes a downstream evidence row in the Package Datasheet (ART-8D962CC45B, ART-BB516ED96F, ART-9C4D132089, and three more rows).
- The 4,160 V source for PKG-023 is almost certainly the 4160V Switchgear Equipment package (PKG-011) — ASSUMPTION pending confirmation. Do not hard-code feeder identification until confirmed.

## Trade-offs

- **Specificity vs source fidelity.** A SoW that names topology, harmonic class, or driven service prematurely binds the vendor without source backing. Defer to the Package Datasheet.
- **Integrator scope creep.** Listing "vendor-internal" obligations (e.g., gate-driver redundancy, cabinet IP rating) in this SoW erodes the vendor's package-engineering ownership. Keep those in the vendor handoff (Package Datasheet) and the Vendor Engineered Equipment Package.
- **Interface verbosity vs traceability.** Six interface types invite an exhaustive table; better to enumerate types here and route per-interface facts to the Package Datasheet where each carries a distinct ART-/IFC- ID.

## Examples

- "PKG-023 receives 4,160 V, 3-phase, 60 Hz power and supplies VFD-conditioned 4,160 V output to a single 1,500 HP nameplate motor (driven service TBD per HRR-023-01-001). The package is supplied as a vendor-engineered MV VFD lineup; the EPC Integrator provides incoming power, grounding, control and communications cabling, foundation/support, and maintenance access as defined in the Package Datasheet."
- (Counter-example, do NOT write:) "PKG-023 shall be a 24-pulse air-cooled diode-front-end NPC topology with active harmonic filter to IEEE 519 at PCC." — not supported by any accessible source slice.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-023-01-001 | Workbook title identifies PKG-023 as a 1,500 HP MV VFD, but accessible Deepcut DBM slice does not name any 1,500 HP MV motor service. The DBM only describes a 6,700 HP "Starting VFD" for inlet/sales compressors and 600 V VFDs in the 600 V MCC lineup. | Workbook Packages row 25 (title) | `4-25_Deepcut_DBM.md` lines 877, 893, 932-942, 2957-2961, 3088 | Datasheet Attributes; Specification REQ-023-01-009; Guidance Principles | Treat 1,500 HP / 4,160 V as the title-supplied package identity only; keep driven service `TBD` and decline to derive topology/harmonics until a source slice naming the driven service is accepted. | TBD |
| HRR-023-01-002 | Package quantity, installed-spare, and redundancy basis are not stated in available source materials. | `PACKAGE_REGISTER.csv` (silent) | `4-25_Deepcut_DBM.md` (silent on this package) | Datasheet Attributes; Specification REQ-023-01-010 | Record quantity / spare basis as `TBD`; do not assume "1 x 100%". | TBD |
| HRR-023-01-003 | The "4160V VFD" qualifier in the title is ambiguous: it can mean (a) the VFD section is supplied from 4,160 V and outputs 4,160 V (MV-in / MV-out), or (b) the VFD lineup is part of the 4,160 V switchgear/MCC family. | Workbook Packages row 25 (title) | DBM line 2957 (4.16 kV MCC class) | Datasheet Attributes; Specification REQ-023-01-001, REQ-023-01-012 | Adopt interpretation (a) — MV-in / MV-out standalone MV VFD lineup — consistent with the package being a discrete vendor-engineered VFD package rather than an MCC section. Mark ASSUMPTION. | TBD |
| HRR-023-01-004 | Upstream 4,160 V feeder identification is not declared in `_DEPENDENCIES.md`. | `_DEPENDENCIES.md` (no declared upstream) | `PKG-011 4160V SWITCHGEAR EQUIPMENT` exists in Gate 7 registers | Specification REQ-023-01-012; Procedure Prerequisites | Propose PKG-011 as the source switchgear; declare upstream dependency on PKG-011 once human confirms. | TBD |
