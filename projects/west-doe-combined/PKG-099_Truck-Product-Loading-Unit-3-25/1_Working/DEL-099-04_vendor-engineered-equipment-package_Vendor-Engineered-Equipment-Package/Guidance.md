# Guidance — Vendor Engineered Equipment Package (DEL-099-04)

> Directional document explaining *why* this deliverable exists, the principles a vendor and EPC reviewer should apply, and the trade-offs / known conflicts to flag for human ruling.

## Purpose

The 03-25 Liquids Hub treats and stores stabilized condensate (3,180 m³/d ≈ 20,000 bbl/d basis) and supports product truck loading as a major function of the hub (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 line 376; SEC-02 line 22). The Truck Product Loading Unit (three loading stations) is a discrete, vendor-engineered physical package within that hub. `DEL-099-04` exists so that an external Package Vendor can deliver an integrated engineered equipment package — design, fabrication, supply, and the equipment itself — that satisfies the EPC Integrator's Scope of Work (`DEL-099-01`) and Package Datasheet (`DEL-099-02`) for `PKG-099`, in a form ready for installation by `DEL-099-03` (Construction Work Package) and acceptance by `DEL-099-06`.

## Principles

1. **EPC drives, vendor delivers.** The vendor package is *anchored* by the EPC Scope of Work and Package Datasheet. The vendor designs to those documents; this `DEL-099-04` Specification is a placeholder source-grounded subset (DBM-derived) until the EPC anchors are issued.
2. **Source fidelity.** Every non-trivial value the vendor adopts must cite a source. Where the locally accessible DBM gives a value (e.g., 103 m³/h per station), use it; where it does not (e.g., tanker overfill scheme), mark `TBD` and resolve through the EPC anchors or a human ruling, not by vendor convention substituting for source.
3. **Modularization for site logistics.** The 03-25 site basis favours modularized, shop-assembled packages (DBM SEC-04 line 294 explicitly for compression; ASSUMPTION extended to loading skid). Vendor should plan for shop assembly and field hookup with clear interface flanges.
4. **Hub-level interface awareness.** The loading package is not a standalone deliverable; it ties into product condensate storage, the VRU vapour-return system, BPCS/ESD logic, F&G detection layout, and electrical distribution. The package must be designed so that those interfaces are documented and testable, not negotiated post-fabrication.
5. **Hazard discipline.** Stabilized C5+ condensate with residual mercaptan chemistry plus open tanker loading is a high-consequence operation. Overfill, grounding/bonding, area classification, and detector coverage are owner/EPC decisions that the vendor must honour, not optimize for cost.

## Considerations

- **Open EPC anchors.** Both `DEL-099-01` and `DEL-099-02` are currently `OPEN` (no issued content). Vendor design started in that state will rely on this DBM-derived Specification plus assumptions; assumptions must be flagged and revisited when the EPC anchors are issued. See Conflict Table CT-01.
- **Inaccessible cited sources.** The decomposition row cites `Workbook Packages row 98` and `26020-Package_Requirements.docx package heading 51`. Those files exist in `_Sources/` only as `.xlsx` / `.docx` binaries and are not text-readable in this run; any requirement that would have come from them is `TBD`. See Conflict Table CT-02.
- **Caustic and produced-water truck-out are separate.** Spent-caustic truck-out (DBM SEC-06 line 402) and produced-water vacuum-truck connections (DBM SEC-06 line 430) are *not* part of the Product Loading Unit. The vendor must not absorb that scope by analogy.
- **LACT scope boundary.** Sales condensate custody transfer through LACT is third-party NRM scope (DBM SEC-02 line 22; SEC-06 line 417). The product truck-loading stations are a separate disposition path; vendor must not confuse the two.
- **Cross-facility utilities.** Instrument air is supplied from 04-25 (SCA-006; DBM SEC-07 line 473); fuel gas and electrical likewise are shared. The vendor package consumes these utilities at the 03-25 battery limit; vendor must not assume local utility generation.
- **Detailed design defers many specifics.** Detector counts, ESD set points, drainage slopes, and material/coating details for several adjacent systems are explicitly carried as detailed-design items in the DBM. The vendor package design must be compatible with that progression rather than locking values prematurely.

## Trade-offs

- **Single-pump-per-station vs. shared loading manifold.** DBM fixes one loading pump per station (REQ-VEEP-003). This favours independent station availability over capital efficiency; vendor should preserve that arrangement.
- **Vapour-return tie-in pressure control.** Tighter vapour control reduces fugitives but tightens VRU suction-pressure operability margins (DBM SEC-06 line 438). Vendor should coordinate with VRU package vendor / EPC on suction-pressure setpoint envelope.
- **Pre-fabricated skid extent vs. field-erected piping.** Larger shop-built skids reduce field labour but constrain transport. With the 03-25 site already accepting transport-driven dis-assembly elsewhere (e.g., compressor packages split into three pieces, DBM line 294), the loading skid should align with the project's accepted modularization envelope.

## Examples

Example values directly from the DBM that the vendor should treat as fixed inputs unless superseded:

- Loading station duty: 103 m³/h at 345 kPad (DBM SEC-06 line 415).
- Loading stations: 3, each with dedicated pump (DBM SEC-06 lines 414, 526, 654).
- Product service: stabilized C5+ condensate, 20,000 bbl/d hub basis (DBM SEC-06 line 376).
- Site: LSD 03-25-80-15 W6M, elevation 673 m AMSL (DBM SEC-02 line 85).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | EPC anchor deliverables `DEL-099-01` (Scope of Work) and `DEL-099-02` (Package Datasheet) are `OPEN`; this `DEL-099-04` Specification is sourced from the DBM in their absence. When the anchors are issued, several REQ-VEEP-* items (especially 011–014, 016) will need to be re-aligned. | DBM `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 | Sibling deliverable `_STATUS.md` files for `DEL-099-01` and `DEL-099-02` (both OPEN, no drafted content) | `Specification.md` REQ-VEEP-011 to 014, 016; `Datasheet.md` Attributes | EPC Package Datasheet (`DEL-099-02`) once issued shall govern; until then DBM-derived values stand. | TBD |
| CT-02 | The decomposition row cites `Workbook Packages row 98` (`26020-Packages_Interfaces_4_export.xlsx`) and `26020-Package_Requirements.docx package heading 51`, but those source files are not text-accessible in this run. Content that would normally derive from them is currently `TBD`. | `_REFERENCES.md` cited source list | `_Sources/` directory listing — `.xlsx` / `.docx` binaries present but no text extraction available | `Datasheet.md` Attributes & Conditions (multiple TBDs); `Specification.md` REQ-VEEP-009, 011–014; `Standards` (CEC clause locations) | Run a `docx`/`xlsx` text extraction over the cited slices and re-draft against extracted content. | TBD |
| CT-03 | DBM SEC-06 line 415 specifies loading-station capacity as `103 m³/h at 345 kPad differential`; DBM SEC-06 line 412 specifies booster pumps as `165 m³/h at 35 m TDH per pump`. These are different machines (booster vs. loading), but the vendor hydraulic model must reconcile them so combined system curves are consistent. | DBM SEC-06 line 415 (loading) | DBM SEC-06 line 412 (booster) | `Specification.md` REQ-VEEP-002, 003; `Procedure.md` Verification | Treat as complementary, not in conflict; vendor must build a hydraulic model spanning booster → tank → loading-pump → station to demonstrate combined operability. | TBD (confirm reading) |
