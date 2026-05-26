# Guidance — DEL-065-01 Scope of Work — Tanks, Caustic (API 650) 4-25 (PKG-065)

## Purpose

PKG-065 "Tanks, Caustic (API 650) 4-25" is a workbook-defined vendor-responsible Mechanical package (Workbook Packages row 87) that supplies the two atmospheric caustic storage tanks supporting the 4-25 Deep Cut Gas Plant non-regenerative NGL mercaptan treating system. This Scope of Work is the EPC Integrator's authoritative package-scope anchor: it states what is in the Package Vendor's supply, what the EPC Integrator integrates, and what is explicitly by-others. It is the upstream basis for sibling deliverables DEL-065-02 (Package Datasheet), DEL-065-03 (Construction Work Package), DEL-065-04 (Vendor Engineered Equipment Package), DEL-065-05 (Vendor Document Turnover Package), and DEL-065-06 (EPC Vendor Package Review and Acceptance).

## Principles

1. **Workbook row 87 is authoritative for package identity and the responsibility split.** Source: PACKAGE_REGISTER row PKG-065. Workbook package rows are not merged across duplicate tracking numbers (SOW-0197 governance note).
2. **The active caustic treating basis is non-regenerative.** Source: DBM-Deepcut/4-25_Deepcut_DBM.md. Spent caustic leaves the site by truck for off-site disposal; there is no active on-site regeneration column.
3. **The package supplies tanks only.** Foundations, site mounting, electrical/instrumentation, platforms, and staircase are by-others (SOW-0200). Scope creep into these by-others items must be rejected.
4. **Caustic is a materials and integrity-critical service.** Polymer or other caustic-compatible materials; no aluminum in the caustic building; SS insulation cladding in exposure areas; indoor installation due to freezing/crystallization risk. Source: DBM-Deepcut.
5. **Tank vent/blanket routing is asymmetric.** Spent tank vents to the incinerator with flame arrestor and LP fuel-gas blanket; fresh tank uses LP fuel-gas blanket but must NOT be connected to the VRU header (to avoid VRU-vapour contamination of fresh caustic). Source: DBM-Deepcut.
6. **EPC Integrator owns interface delivery and integration.** Applicable interface types (PACKAGE_REGISTER): Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.

## Considerations

- **Tag completeness.** Source slices currently assert `TK-6780-1` (spent) but not the fresh-tank tag. The fresh-tank tag should be issued during EPC tag-assignment; until then it is `TBD` in artifacts.
- **Flow rates are TBD per SOW-0200.** Process design loop (caustic regeneration rate, contactor circulation, blowdown to spent tank) must be confirmed by EPC before vendor sizing of nozzles and heater duties.
- **Pressurized caustic drain drum (`V-6940-1`).** DBM-Deepcut describes it as a separate vessel routing to the spent caustic tank. Its package assignment is `TBD` and is not asserted as part of PKG-065 by SOW-0197 to SOW-0200; treat as cross-package interface.
- **`.docx`/`.xlsx` source slices not directly read in this pass.** Requirements derived from `26020-Package_Requirements.docx package heading 20` and the workbook are sourced via the GATE-07 SCOPE_LEDGER/PACKAGE_REGISTER extraction. Items that exist only in those binary sources but were not surfaced in the extraction remain `TBD` here.
- **Safety showers, building floor material, shower count/location** are noted in DBM-Deepcut as detailed-engineering TBDs; they affect the caustic building inside which the tanks are installed (not the tank package itself), but they are integration considerations for the EPC.

## Trade-offs

- **Indoor installation vs site footprint.** Caustic freezing/crystallization risk drives the indoor decision (DBM-Deepcut). Outdoor placement would reduce building cost but is rejected on integrity/safety grounds.
- **Polymer vs metallic tank material.** Polymer is caustic-compatible at concentration but limits temperature, mechanical handling, and seismic/fire response; metallic tanks (e.g., nickel-bearing SS) widen temperature range but increase cost. The DBM commits to "polymer or other caustic-compatible material" and leaves the selection as a detailed-engineering TBD; this SoW preserves that latitude.
- **Heater design ownership.** SOW-0199 commits heater design to the vendor for the spent caustic tank; this avoids EPC having to specify heat-up time, watt density, and element materials, at the cost of a vendor-defined heater interface to the EPC electrical scope.

## Examples

(Source-supported examples only.)
- Spent caustic routing example (DBM-Deepcut): pressurized caustic drain drum demister; NGL vapours up to stabilizer overheads compressor first-stage suction; remaining caustic level-controlled to spent caustic tank; vapours from spent tank and DSO off-gas to incinerator at 3-25 with upstream KO drum.
- Fresh caustic example (DBM-Deepcut): 1 x 400 bbl tank, atmospheric, heated, insulated, truck-in capable, fuel-gas blanketed, isolated from VRU header.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-065-01-01 | Fresh caustic tank tag is asserted in DBM as "1 x 400 bbl tank" but no tag number is supplied in SOW-0198/0199/0200. | SCOPE_LEDGER SOW-0198/SOW-0199 (no fresh-tag) | DBM-Deepcut/4-25_Deepcut_DBM.md (functional description only) | Datasheet Identification table; Specification REQ-065-01-02 sibling | Issue a tag during EPC tag-assignment; keep `TBD` until then. | TBD |
| CFT-065-01-02 | Pressurized caustic drain drum `V-6940-1` package assignment. DBM-Deepcut treats it as a discrete vessel separate from the storage tanks; SCOPE_LEDGER SOW-0197 to SOW-0200 do not enumerate it inside PKG-065. | SOW-0197 to SOW-0200 (no V-6940-1) | DBM-Deepcut/4-25_Deepcut_DBM.md (V-6940-1 named as Pressurized Caustic Drain Drum) | Datasheet Attributes; Specification Scope (out of scope) | Keep V-6940-1 OUT of PKG-065 and surface as cross-package interface to the unit responsible for SOC/drain-drum scope. | TBD |
| CFT-065-01-03 | `26020-Package_Requirements.docx package heading 20` is cited as a source slice but is a binary `.docx` not directly read in this run. Some requirements relayed only via SCOPE_LEDGER extraction. | SCOPE_LEDGER SOW-0198 to SOW-0200 | Original `.docx` (not directly read) | All requirements derived from heading 20 | Confirm `.docx` extraction is complete or extract the heading to markdown for future passes. | TBD |
