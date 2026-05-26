# Guidance — DEL-067-02 Package Datasheet (PKG-067 Tanks, Sour Water (API 650) 4-25)

## Purpose

The Package Datasheet exists so that a third-party tank vendor (and the supporting EPC disciplines who integrate the tanks into the facility) can engineer, design, fabricate, and accept the sour/produced water storage tanks against a single, source-grounded technical handoff. It is the principal "Gate 5 EPC anchor" technical document for PKG-067 alongside the Scope of Work, the Construction Work Package, and the EPC Vendor Package Review and Acceptance deliverables (DELIVERABLE_REGISTER rows 528-533).

The datasheet does not introduce new design — it carries the West Doe Deepcut DBM and the package row from the workbook into a vendor-actionable form. Where the source basis is silent, the datasheet marks TBD rather than inventing values.

## Principles

1. **Source-anchored, not convention-anchored.** Every non-trivial value is traceable to the West Doe Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) or to the GATE-07 decomposition registers. Industry default values are explicitly labeled ASSUMPTION when used.
2. **Sour-service first.** "Sour water" in the package title and "produced water" in the equipment list refer to the same physical service. The vapour space and emergency-relief disposition must be designed on the assumption that H2S can be present, even when bulk-phase H2S is low.
3. **Vendor scope vs. EPC scope is interface-bounded.** The vendor delivers the tanks and tank-mounted appurtenances; the EPC Integrator delivers foundations, containment, area lighting, cathodic protection, grounding, tie-in piping past the tank flanges, I&C cabling, grading, and site drainage. The Datasheet Interface Requirements Matrix is the contractual boundary control.
4. **Datasheet is a technical handoff, not a design report.** Sizing rationale lives in the DBM; this datasheet captures the bounded data the vendor needs to design and fabricate. Conflicts surface here; resolutions live upstream in the DBM and downstream in detailed engineering.
5. **Cold-climate and remote-site assumptions are non-negotiable.** Insulation, heating, blanket gas, and winter vacuum prevention are explicit requirements of this service per the DBM and must not be value-engineered out.

## Considerations

- **Tank pair labeled two ways.** PACKAGE_REGISTER row 94 names the package "Tanks, Sour Water (API 650)" while the equipment list (TK-9010-1, TK-9020-1) and DBM Process Storage Areas table use "Produced Water Storage Tank." The Datasheet treats them as a single service with two names. A human ruling on naming is captured in `_run_records/` for downstream consistency.
- **PVRV vent disposition.** Source basis explicitly states "at least one PVRV per tank" and that EPRV sizing is to be reviewed (DBM line 524). Whether tank vents route to atmosphere, to a low-pressure flare header, or to a vapour-recovery destination is not stated in the produced-water source slice. Detailed engineering must close this before vendor RFQ release; treat the boundary as TBD in the datasheet, not as a vendor option.
- **Inlet stream composition is open-ended.** DBM line 508 lists trace contaminants and explicitly says the list is not comprehensive. The vendor cannot be expected to qualify materials against an unbounded list; the datasheet should require the vendor to state material/coating compatibility against the named contaminants and flag any further constraints rather than absorb undefined risk.
- **Design SG 1.25 vs. operating SG 1.0–1.18.** The conservative design SG of 1.25 (TBC) governs tank structural design; pump/operating calculations use lower numbers. Carry both numbers in the datasheet to avoid silent narrowing during vendor review.
- **Truck-out is a flexibility provision, not the normal disposition.** Normal disposition is pipeline transfer to 03-25; trucking is emergency/local handling (DBM lines 493, 504). Sizing of truck-out connections (vacuum truck 2.75 m³/min; B-train 55 m³ in 20 min) is for emergency capacity and should not be treated as a continuous operating mode.
- **Plot spacing tradeoffs.** NFPA 30 tank-to-tank spacing of 2.35 m (DBM line 268) is generous for atmospheric water tanks but the dominant separation constraints will be from flare (25 m), fired heater (25 m), and public road (80 m). Layout coordination with the broader 04-25 plot plan is required.
- **Source extraction gap.** `26020-Package_Requirements.docx` package heading 22 is referenced as a source but the binary `.docx` is not locally extracted to readable form. Any package-specific text expected to come from that source is currently TBD and should be filled during a subsequent pass once the source is extracted.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Tank vent to atmosphere vs. to flare/vent header | Atmospheric vent is simpler and cheaper but may be unacceptable if sour vapours are credible. Flare-header routing requires upstream relief-header capacity verification and may force header upgrades. Decision pending sour-vapour isolation philosophy review (DBM line 524). |
| Single PVRV vs. PVRV + EPRV | DBM requires "at least one PVRV"; EPRV sizing pending. Adding an EPRV protects against fire-case overpressure and may be required by code review — the cost is incremental relief sizing and possible additional vent piping. |
| Insulation/heating granularity | Source mandates externally insulated and heated tanks. Choice of heat-trace electrical vs. heating-medium (steam/glycol) coil affects utility-routing complexity and reliability; defer to detailed engineering, not vendor preference. |
| Internal coating life vs. inspection cycle | Devchem 253 lining is specified (DBM line 524). Coating-system warranty, holiday-test acceptance, and inspection access provisions trade up-front cost against in-service inspection intervals. |
| 2 tanks vs. 2 + spare | DBM basis is two tanks with 8.9 days storage at 380 bbl/d — generous. Adding a spare reduces availability risk but is not in the package row 94 equipment count and would expand scope outside the EPC handoff. |

## Examples

- **Source-grounded design value (good):** "Maximum normal fill = 90% of tank volume, thermal expansion review required" — cited to DBM line 519, carried as Specification R3.
- **Conservative explicit assumption (acceptable):** "Tank design SG = 1.25 (TBC)" — value carried from DBM line 508 with the DBM's own TBC qualifier preserved.
- **TBD over guessing (good):** PVRV vent destination is TBD pending Relief/Flare/Vent interface resolution rather than asserting a default route.
- **Undocumented value (avoid):** Stating a specific containment volume or a specific insulation thickness without source — the datasheet keeps these TBD until the source supports them.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| C-067-02-01 | Package name "Tanks, Sour Water (API 650)" vs. tank-tag label "PRODUCED WATER STORAGE TANK" for the same TK-9010-1/TK-9020-1 pair | PACKAGE_REGISTER row 94 (Package_Name) | PACKAGE_REGISTER row 94 (equipment list line 2627); 4-25_Deepcut_DBM.md line 493 (Process Storage Areas) | Datasheet § Identification, § Equipment List; Specification § Scope; this package's title | PROPOSAL: treat "sour water" (package name) and "produced water" (tank-tag and DBM body) as synonymous for this service in PKG-067; carry both names in downstream documents until naming is normalized | TBD |
| C-067-02-02 | PVRV vent disposition not specified in source (atmospheric vs. flare/vent header) | DBM line 524 (PVRV requirement, EPRV TBR) | PACKAGE_REGISTER row 94 (Relief/Flare/Vent listed as applicable interface) | Specification R7, R10; Datasheet § Interface Requirements Matrix | PROPOSAL: TBD pending sour-vapour isolation philosophy review; do not pre-select disposition in datasheet | TBD |
| C-067-02-03 | Tank inlet/contents list is explicitly non-exhaustive | DBM line 508 ("list is not comprehensive and is to be confirmed") | (no second source — gap, not contradiction) | Specification R11; Datasheet § Conditions | PROPOSAL: require vendor to state material/coating compatibility against the named contaminants and flag anything further; do not fix a closed contaminant list in the datasheet | TBD |
| C-067-02-04 | 26020-Package_Requirements.docx package heading 22 not locally extracted | _CONTEXT.md / PACKAGE_REGISTER row 94 cite it as a source | `_Sources/26020-Package_Requirements.docx` present as binary; readable extraction absent | All sections (any value that would come from this source is TBD) | PROPOSAL: extract the Word source as part of a later enrichment pass and re-run four-documents to integrate | TBD |
