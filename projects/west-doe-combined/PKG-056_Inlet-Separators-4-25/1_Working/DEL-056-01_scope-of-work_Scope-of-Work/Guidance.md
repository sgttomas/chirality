# Guidance — DEL-056-01 Scope of Work (PKG-056 Inlet Separators 4-25)

## Purpose

The Scope of Work is the EPC Integrator's anchor deliverable for `PKG-056 Inlet Separators 4-25`. It establishes a shared, source-grounded definition of what the package *is*, what it *does*, where its *boundaries* are, and how it *integrates* into the West Doe Deepcut (04-25) facility. Downstream EPC and vendor deliverables (`DEL-056-02` through `DEL-056-06`) inherit identity, scope, and integration framing from this document; they should not re-derive these facts independently. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows 372–377.)

## Principles

1. **Identity before design.** The Scope of Work fixes package identity and tagged equipment first; design values belong in `DEL-056-02 Package Datasheet`. (Source: `DELIVERABLE_REGISTER.csv` rows 372–373.)
2. **Source-grounded.** Every non-trivial claim cites Workbook Packages row 68, `26020-Package_Requirements.docx`, the RFQ, or the Deepcut DBM — or is labelled `TBD`/`ASSUMPTION`. (Source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv` row 68.)
3. **Boundary discipline.** Vendor authority covers package engineering, design, vendor documentation, and physical equipment. EPC Integrator authority covers facility-level integration, interfaces, tie-ins, and constructability. Crossing these boundaries triggers a scope conflict. (Source: `PACKAGE_REGISTER.csv` row 68.)
4. **Preserve unresolved conflicts.** Where current authority disagrees with legacy project references (notably the installed-quantity question), the conflict is preserved, not silently resolved. (Source: `4-25_Deepcut_DBM.md` §Inlet separator system.)
5. **Unit-level isolation by default.** Parallel inlet separator packages are isolated on a unit basis so a unit can be removed from service while others continue to operate. (Source: `4-25_Deepcut_DBM.md` line ~2408.)

## Considerations

- **Quantity conflict.** Current DBM body carries two installed horizontal three-phase HP inlet separators (each 9 ft ID x 40 ft S/S) with plot space for a third; legacy references describe four inlet separator packages. The DBM equipment listing (rows 2540, 2596–2597) names only `V-1600-1` and `V-1700-1`. The Scope of Work should adopt the two-installed-plus-future-provision basis while flagging the conflict (see Conflict Table). (Source: `4-25_Deepcut_DBM.md` §Inlet separator system; rows 2540, 2596–2597.)
- **Slug-handling sizing.** Per-separator slug capacity is unresolved between 31.8 m3 and 33.9 m3. Upstream pipeline holdup is ~67 m3, with assumed six-hour processing by downstream MPFF/SOC/stabilizer. Downstream availability is a precondition for inlet separation duty. (Source: `4-25_Deepcut_DBM.md` §Inlet separator system.)
- **Drive-gas integration.** Sales gas immediately upstream of the splitter is the drive-gas source (alternate: inlet compressor discharge). Drive-gas enters upstream of plant inlet gas meters and must be separately metered to each inlet separator package. (Source: `4-25_Deepcut_DBM.md` line ~811.)
- **Inlet protection.** Inlet shut-ESDV pressure shutdown basis is 1360 psig; delivery-point ESDV pressure shutdown is TBC. A HIPPS may be required if inlet pipeline MAOP exceeds facility inlet design pressure. (Source: `4-25_Deepcut_DBM.md` line ~809.)
- **Interface scope.** The package crosses eleven interface types (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). The Scope of Work should not enumerate detailed interface design; it should establish that all eleven are in play and route detailed interface facts to `DEL-056-02`. (Source: `PACKAGE_REGISTER.csv` row 68.)

## Trade-offs

- **Two installed vs. plot-for-three.** Selecting "two installed plus future provision" minimizes current capital and constructability scope while preserving expansion optionality, at the cost of carrying the legacy four-package reference as an unresolved conflict.
- **Vendor-led vs. EPC-led integration detail.** The package register places package engineering with the vendor; deeper integration detail (tie-ins, constructability) is EPC-led. Pushing integration detail into vendor scope risks weakening EPC integration ownership; pushing equipment design detail into EPC scope risks duplicating vendor work.

## Examples

Examples are not extracted in this draft because the available DBM slice does not yield illustrative SOW-language examples that can be cited at clause level without opening `26020-Package_Requirements.docx`. (TBD — to be added if/when the Word source is rendered locally.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-056-01-01 | Installed inlet separator count | `4-25_Deepcut_DBM.md` §Inlet separator system: two installed (V-1600-1, V-1700-1) plus plot space for a third | `4-25_Deepcut_DBM.md` §Inlet separator system: legacy four-package references; line ~2352 "Inlet Separators 4" capacity row | Datasheet Attributes; Spec R1.2, R1.3; Guidance Considerations | Adopt two installed plus future provision (current DBM body authority); preserve legacy four-package references in narrative as unresolved | TBD |
| C-056-01-02 | Per-separator slug capacity | `4-25_Deepcut_DBM.md` §Inlet separator system: 31.8 m3 | `4-25_Deepcut_DBM.md` §Inlet separator system: 33.9 m3 | Datasheet Attributes; Spec R2.2 | Carry as TBD pending detailed engineering | TBD |
| C-056-01-03 | Package name vs. equipment label | `_CONTEXT.md`/`PACKAGE_REGISTER.csv` row 68: "Inlet Separators 4-25" | `4-25_Deepcut_DBM.md` row 2540: "Inlet Separators 2" (V-1700-1 / V-1600-1) | Datasheet Identification; Spec R1.1, R1.2 | Treat "Inlet Separators 4-25" as the package register name and "Inlet Separators 2" as the DBM equipment-group label for the same physical units; do not rename | TBD |
| C-056-01-04 | RFQ document name "Inlet Separators 2" vs. package name | `PACKAGE_REGISTER.csv` row 68: RFQ filename `26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` | `_CONTEXT.md`: PackageName "Inlet Separators 4-25" | Datasheet References; Spec R3.2 | Carry both; package register is authoritative for package name, RFQ filename is preserved as the source identifier | TBD |
