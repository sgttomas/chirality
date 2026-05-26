# Guidance — DEL-070-02 Package Datasheet (Mole Sieve Drier Unit, NGL)

## Purpose

The Package Datasheet for PKG-070 exists to give the third-party Package Vendor (or discipline package engineer) a single, source-supported design-basis document so they can engineer and design the NGL molecular-sieve dehydration package without re-deriving the underlying Deepcut DBM. It is the EPC Integrator's evidence-bearing handoff: it carries the design conditions, sparing intent, regeneration architecture, and interface boundaries that are common to all downstream Gate 5 deliverables for this package (DEL-070-03 through DEL-070-06).

Per `_CONTEXT.md` Notes, the Package Datasheet also intentionally carries the package interface facts as evidence rather than ceding them to standalone interface deliverables — so its quality directly governs the integrity of vendor engineering, construction integration, and EPC acceptance downstream.

## Principles

1. **Source-anchored over convention.** Where the DBM-Deepcut §Current-Scope NGL Molecular-Sieve Dehydration provides a value, use that value. Do not substitute a process-gas mole-sieve value or a generic 3A-bed convention for the NGL service.
2. **Open items remain open.** Every TBC/TBR/TBD marker in the source slice should appear in the Package Datasheet. The Vendor needs to see what is still open so they can price it, schedule it, or push the question back. Silently closing TBCs into apparent design values is the most common source of integration risk on packaged units.
3. **Interfaces are first-class.** Because interface facts are carried here (not in a standalone interface deliverable), every interface in the source slice deserves an explicit row in the Package Datasheet with its counterparty service identified.
4. **No clause-level fabrication from binary sources.** The decomposition row cites `26020-Package_Requirements.docx` heading 24 and the packages workbook row 74. Neither is currently extracted to text. Do not generate clause-level requirements from those citations until the text is accessible.

## Considerations

### Service distinction

The Deepcut facility has two separate mole-sieve systems:
- a **process-gas** molecular-sieve unit (high-pressure sour-gas service ahead of cryogenic recovery), described in DBM-Deepcut §Molecular-Sieve Dehydration and Mercury Removal Basis (lines 1239-1296);
- the **NGL** molecular-sieve unit (this package, PKG-070), described in DBM-Deepcut §Current-Scope NGL Molecular-Sieve Dehydration (lines 1574-1623).

Designers and reviewers must keep these separate. Pressure class, sulphur tolerance, regeneration gas source, and downstream consumer are all different. For example: the process-gas mole-sieve system requires 900# flanges (DBM-Deepcut line 628); the NGL service flange basis is not stated in the available source slice and is `location TBD`.

### Sulphur co-adsorption and product spec risk

The DBM is explicit that the NGL mole sieve must adsorb minimal sulphur, because sulphur recycle during regeneration can produce off-spec product (DBM-Deepcut line 1578). Two design hooks follow from this: (a) flare-blowdown of regeneration gas on contamination, and (b) the alternate dedicated mole-sieve regeneration-gas compressor cylinder at the stabilizer overheads compressor, to be reviewed in detailed engineering. Both should be carried as required disclosures in the Package Datasheet.

### Regeneration architecture maturity

The regeneration gas service is the most maturity-limited part of the package basis. Sales gas is the planned source, but the existence and final source tie-in remain TBC; bed inlet temperature (460 deg F), regeneration gas flow range (3.5-5 MMSCFD), and BEU heater inside the NGL mole-sieve building are stated as design basis but explicitly carried as "to be confirmed rather than as a closed design claim" (DBM-Deepcut line 1617). Procurement should be expected to require these to close in detailed engineering, not at Gate 5.

### Sparing and lifecycle

The current basis uses no installed spare bed. If a five-year adsorbent lifecycle is required, a spare installed bed should be considered (DBM-Deepcut line 1598). The Package Datasheet should make this trade-off visible rather than presenting the 3-tower configuration as fully sparing-resolved.

### Outlet specification ambiguity

The DBM cites three different "water content" framings for the NGL outlet: <1 ppmv H2O expected, 7 ppmv H2O maximum, and <7 ppmw governing target TBC (DBM-Deepcut lines 1590-1592). Two are mass-based, one is volumetric, and the governing target is itself TBC. The Package Datasheet should reproduce all three and not silently choose one. See Conflict Table below.

## Trade-offs

| Trade-off | Options | Notes |
|---|---|---|
| Sparing | No installed spare (current basis) vs. installed spare bed | Driven by required adsorbent lifecycle; 3-year vs. 5-year. Source: DBM-Deepcut lines 1596, 1598. |
| Regeneration gas isolation | Shared sales-gas source vs. dedicated cylinder on stabilizer overheads compressor | Dedicated cylinder reduces sulphur-recycle exposure but adds vendor scope. Source: DBM-Deepcut line 1578. |
| Outlet filter type | P2 bag-filter (current basis) vs. alternative filter housing types | TBR; drain/filling provisions also TBR. Source: DBM-Deepcut line 1623. |
| Winter cooler operation | Plenum heating bundle vs. recirculation louvers only | Plenum bundle gives more freeze-protection margin; cost/maintenance trade-off. Source: DBM-Deepcut line 1619. |

## Examples

- **Example interface row to carry in the Package Datasheet:** "Regeneration gas inlet — sales gas, upstream of sales-gas compressors, 3.5 to 5 MMSCFD, source tie-in TBC (DBM-Deepcut line 1617)." Vendor sees both the design number and the maturity flag.
- **Example open-item disclosure:** "Adsorbent lifecycle: 3 years, vendor-defined, TBC; review sparing if 5-year lifecycle required (DBM-Deepcut lines 1596, 1598)."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-070-02-001 | Outlet water content target stated three ways (<1 ppmv expected, 7 ppmv max, <7 ppmw governing TBC). The volumetric vs. mass-based framing is inconsistent and the governing value is TBC. | DBM-Deepcut line 1590 (<1 ppmv H2O expected) | DBM-Deepcut lines 1591-1592 (7 ppmv max; <7 ppmw governing, TBC) | Datasheet §Conditions R-4; Specification R-4; Procedure verification step | PROPOSAL: carry all three values verbatim; treat <7 ppmw (TBC) as the governing handoff target until human/vendor closes the unit basis. | TBD |
| CONF-070-02-002 | Decomposition row cites `26020-Package_Requirements.docx` heading 24 and workbook row 74 as the package requirements basis, but neither is text-extracted; no clause-level requirements can be cited. | `_CONTEXT.md` Source Reference; decomposition row | Sources folder: only `.docx` and `.xlsx` binaries present | Specification §Standards; Datasheet §References | PROPOSAL: keep both citations as `location TBD` and surface this as a precondition to closing R-14. | TBD |
| CONF-070-02-003 | Sparing is described as "one bed in adsorption and one in regeneration" within a "3-tower" configuration; the role of the third tower (standby vs. staging) is not stated for the NGL service. | DBM-Deepcut line 1584 (3-tower) | DBM-Deepcut line 1598 (one in adsorption, one in regeneration) | Datasheet §Attributes (Bed sparing); Specification R-7; Guidance §Sparing | PROPOSAL: state configuration as 3-tower and call third-tower role TBC; require vendor to confirm in detailed engineering. | TBD |
