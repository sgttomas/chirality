# Guidance: DEL-026-04 — Vendor Engineered Equipment Package (PKG-026 TXP-8300-2)

## Purpose

Provide directional guidance for producing and reviewing the Vendor Engineered Equipment Package for PKG-026. This production unit is the vendor-side counterpart to the EPC Integrator's Scope of Work (DEL-026-01) and Package Datasheet (DEL-026-02). It exists so that package engineering, design, fabrication/supply, and the physical equipment are owned and produced as a single coherent vendor work product. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-026-04.)

## Principles

1. **Vendor-owned envelope.** Package engineering, design, vendor documentation, and the physical equipment are vendor-owned. EPC Integrator owns facility integration. Do not blur this split. (Source: PACKAGE_REGISTER.csv PKG-026.)
2. **EPC anchors are authoritative.** The vendor work is bounded by DEL-026-01 SOW and DEL-026-02 Package Datasheet. Where vendor proposals deviate, surface the deviation rather than silently absorbing it.
3. **One production unit, two deliverable shapes.** The vendor produces (a) the physical equipment and (b) the design basis/datasheet set documenting it. Both are mandatory; neither substitutes for the other. (Source: `_CONTEXT.md` Anticipated Artifacts.)
4. **Source fidelity over convention.** Where DBM source slices state values (e.g., 6.9 kV neutral grounding at 100 A / 10 s), the vendor package shall conform. Do not generate transformer parameters from convention when source values exist.
5. **Documentation flow.** Vendor turnover documentation flows through DEL-026-05; integration acceptance flows through DEL-026-06. This production unit does not host either.

## Considerations

- **Voltage class allocation.** The package title carries three voltages (13.8/6.9/0.4 kV). Winding topology — two-winding (e.g., 13.8/6.9 or 13.8/0.4) with separate aux, or three-winding — is not confirmed in accessible sources. The vendor package must reconcile this against DEL-026-02 before fabrication. (TBD; see Conflict Table.)
- **Rating convention 20/26 MVA.** Dual rating is typical of ONAN/ONAF (self-cooled / forced-air-cooled) distribution transformers. Cooling class, ambient design temperature, and altitude derating are TBD in accessible sources. The vendor should not assume a cooling class without DEL-026-02 confirmation.
- **Grounding integration.** Each 6.9 kV transformer winding on site is grounded with a 100 A, 10 s NGR operating as a tripping system; each 600 V transformer is grounded via 5 A continuous HRG. If TXP-8300-2 includes a 6.9 kV or 0.4 kV-to-600 V winding, those grounding regimes apply at the integration boundary. (Source: `4-25_Deepcut_DBM.md` L2985; `3-25_Comp_and_Liquids_DBM.md` L734.)
- **Interface scope.** PKG-026 carries seven applicable interface types. Vendor design should anticipate EPC tie-ins for all of them and provide clear, dimensioned interface drawings.
- **Exclusions.** No package-specific exclusions are stated in source materials (PACKAGE_REGISTER.csv PKG-026: "TBD; no package-specific exclusions"). Treat the absence as an open item, not as silent permission.

## Trade-offs

- **Vendor standard product vs custom engineering.** A standard product reduces lead time but may force EPC re-work on interfaces. A custom-engineered transformer aligns precisely with DEL-026-02 but extends schedule. The vendor package design basis should declare which approach is taken.
- **Three-winding vs two transformers.** A single three-winding 20/26 MVA unit reduces footprint and tie-in count but concentrates outage risk. Two units (e.g., 13.8/6.9 plus 6.9/0.4) increase redundancy and complicate layout. Decision authority rests with DEL-026-02; surface the trade-off rather than pre-deciding.
- **Vendor scope of documentation.** Pushing detailed installation engineering into the vendor package can simplify EPC work but blurs the responsibility split. Default per PACKAGE_REGISTER.csv: integration stays with EPC.

## Examples

(Examples that would require source material not present in the locally accessible slices are omitted; values stated above are the source-grounded examples.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-026-04-001 | Winding topology for 13.8/6.9/0.4 kV not stated in accessible sources; could be three-winding or two-winding plus aux. | Package title (Workbook Packages row 28) | DBM electrical sections (`4-25_Deepcut_DBM.md` §"Medium-voltage services") do not enumerate TXP-8300-2 winding scheme | Datasheet Equipment Identity; Specification R-026-04-003, R-026-04-008 | Defer to DEL-026-02 Package Datasheet when issued; vendor confirms via factory submittals | TBD |
| CONF-026-04-002 | Cooling class and rating basis behind `20/26 MVA` notation not confirmed in accessible sources. | Package title | No DBM slice defines cooling class for TXP-8300-2 | Datasheet Equipment Identity; Specification R-026-04-003, R-026-04-008 | ASSUMPTION ONAN/ONAF flagged in Datasheet; defer to DEL-026-02 + vendor datasheet | TBD |
| CONF-026-04-003 | Site allocation of TXP-8300-2 (Comp/Liquids 03-25 vs Deepcut 04-25 electrical building) not confirmed. | `3-25_Comp_and_Liquids_DBM.md` lists feeders at 03-25 (no TXP-8300-2 by tag) | `4-25_Deepcut_DBM.md` enumerates 6.9 kV services without TXP-8300-2 by tag | Datasheet Conditions; Specification scope | Defer to DEL-026-01 SOW and DEL-026-02 Package Datasheet | TBD |
| CONF-026-04-004 | Governing transformer standards (IEC 60076 / IEEE C57 / CSA) not named in accessible sources. | DBM electrical sections cite project electrical specs and CEC generically | No source slice names a transformer construction/test standard | Specification Standards | Vendor proposes the governing standards set; EPC confirms via DEL-026-02/06 | TBD |

## Human Review Required (HRR)

- HRR-026-04-001 — Winding topology (per CONF-026-04-001) must be ruled by DEL-026-02 issue or by direct human ruling before vendor engineering can fix the technical envelope.
- HRR-026-04-002 — Cooling class and rating basis for `20/26 MVA` (per CONF-026-04-002) must be confirmed.
- HRR-026-04-003 — Site allocation and integration building (per CONF-026-04-003) must be confirmed for interface and tie-in planning.
- HRR-026-04-004 — Governing transformer construction/test standards set (per CONF-026-04-004) must be named.
