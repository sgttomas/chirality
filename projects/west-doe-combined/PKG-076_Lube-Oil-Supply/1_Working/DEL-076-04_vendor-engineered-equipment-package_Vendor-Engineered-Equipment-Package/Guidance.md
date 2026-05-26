# Guidance — Vendor Engineered Equipment Package (DEL-076-04)

> Directional guidance for the Package Vendor and for the EPC Integrator's integration review. Rationale is drawn from DBM-Deepcut SEC-08 ("Utilities and Support Systems Basis", including "Lube Oil Storage and Pump Basis"), SEC-05 (Compression — lube-oil consumers), SEC-02 (Site/Layout), and SEC-16 (Packages register). Items not supported by accessible source are marked `TBD` or routed to the Conflict Table.

## Purpose

This deliverable exists because the PKG-076 Lube Oil Supply unit is a shared compressor-lubrication utility for the 04-25 Deep Cut Gas Plant and is procured as a vendor-engineered storage-and-pump package rather than EPC-engineered piecewise. The vendor brings packaged heated-storage and oil-transfer IP that the EPC Integrator integrates with the compressor frames (inlet/sales, stabilizer overheads, sales-gas booster, acid gas) and with the storage tank area. DEL-076-04 is the vendor's production unit; DEL-076-01 (SOW) and DEL-076-02 (Package Datasheet) are the upstream EPC inputs, and DEL-076-06 is the EPC review/acceptance deliverable (`_CONTEXT.md`; DELIVERABLE_REGISTER row 387 and adjacent PKG-076 rows).

## Principles

1. **Demand follows compressor lubrication policy.** The lube oil supply package exists to keep compressor frame day tanks filled (DBM SEC-08 L1835, L2068, L2070); compressor frames carry their own electric circulating lube oil heaters for quick start (SEC-05 L828, L928, L967). PKG-076 supplies; it does not perform on-frame circulation or quick-start heating.
2. **Heated storage is mandatory, not optional.** Both tanks are explicitly described as "heated" (SEC-08 L2067, L2069, L1835). At a site design ambient minimum of −40 °C (SEC-02 L198), unheated lube oil cannot be reliably transferred.
3. **Two services, segregated.** Cylinder lube oil (P-9240-1, 400 bbl) and crank-case lube oil (P-9250-1, 200 bbl) are physically and functionally segregated; the vendor must not cross-connect storage or pumping headers.
4. **Multi-grade cylinder oil capability is a forward-looking concern.** DBM L2072 explicitly states that multiple cylinder oils "may be required" across services (sulphur content, rich gas, H2S). The initial build may be single-grade, but layout and tankage decisions should not preclude future addition of a second cylinder-oil tank/grade.
5. **Intermittent pump duty, not continuous circulation.** Pump duty is "as needed" fill (SEC-08 L2068, L2070); vendors should not over-specify against continuous-duty heads or flows.
6. **Cold-climate package design.** −40 °C to +35 °C ambient envelope (DBM SEC-02 L198) governs winterization, package buildings, heat tracing, instrumentation, and motor selection.

## Considerations

- **Pump sparing.** The DBM Packages line item lists exactly one cylinder pump (P-9240-1) and one crank-case pump (P-9250-1) (SEC-16 L2602; SEC-08 L2068, L2070). For a utility that supports compressor lubrication across the SOC compressor train, single-pump basis carries availability risk. Vendor should propose sparing rationale (e.g., 2 × 100% per service, or shared stand-by); whether the EPC accepts a 1 × 100% basis remains **TBD** (see Conflict Table).
- **Tank tags absent from DBM.** The DBM identifies the two pump tags (P-9240-1, P-9250-1) but does not identify the two tank tags. Vendor should propose tank tags consistent with the 9240/9250 numbering family for clarity, subject to EPC tag-register acceptance.
- **Heating method.** Choice between electric trace, jacket, or hot-medium coil is not stated in DBM. Hot medium tie-in (SEC-08 utility summary L1832) is plausible if local supply exists; otherwise electric tracing is the typical default. Vendor should justify against energy cost, reliability, and oil-quality (avoid local overheating that degrades the oil).
- **Distribution piping scope split.** SEC-08 L1835 lists the principal interface as "Compressor packages and storage tank area." Whether long-distance distribution piping is in PKG-076 or in the compressor packages is **TBD** against the EPC layout and `26020-Package_Requirements.docx` h.30.
- **Used-oil and additional storage.** DBM SEC-08 L2072 explicitly notes "additional storage requirements remain TBD." Vendor should flag whether used / contaminated oil collection is in scope; current basis appears not to include it, which is a forward-looking gap.
- **Multi-oil grade differentiation.** Vendor should ask the EPC whether SOC inlet, sales, stabilizer overheads, acid gas, and sales-gas booster reciprocating compressor cylinders will use a common cylinder oil grade or differentiated grades (DBM SEC-08 L2072 — TBC).

## Trade-offs

| Trade-off | Direction | Source |
|---|---|---|
| Single 400 bbl cylinder oil tank vs. two smaller tanks for multi-grade flexibility | Single tank is the DBM basis (L2067); vendor proposal of two smaller tanks is acceptable if multi-grade need (L2072) is confirmed early. | DBM SEC-08 L2067, L2072 |
| 1 × 100% pumps vs. 2 × 100% pumps per service | 1 × 100% is the DBM line-item basis (SEC-16 L2602); 2 × 100% improves availability for compressor lubrication. Vendor proposal acceptable with availability rationale. | DBM SEC-08 L2068, L2070; SEC-16 L2602 |
| Electric tank heating vs. heat-medium coil | Not specified in DBM; electric is typical default for storage-tank-area utility. Vendor selection acceptable if vendor justifies against oil-degradation risk and energy cost. | ASSUMPTION; DBM SEC-08 L1832 (heat-medium availability) |
| Atmospheric (API 650) tank vs. pressurized vessel | Atmospheric heated tank is consistent with the SEC-08 description and the general use of API 650 for the other site bulk storage tanks (e.g., caustic, condensate per SEC-16 L2556, L2557). Pressurized vessel is not justified by the basis. | ASSUMPTION; DBM SEC-08 L2067, L2069 |

## Examples

- **Compressor frame day-tank refill.** SEC-05 L828 establishes that "supplemental lube-oil pump provisions" may be required at the compressor frame based on compressor manufacturer requirements, and that "An electric circulating lube-oil heater shall maintain frame oil temperature for quick start." The PKG-076 vendor should treat the compressor frame day tanks as terminal points and not duplicate frame-side heating or circulation.
- **Cylinder-oil grade differentiation.** DBM SEC-08 L2072 states: "Multiple compressor cylinder oils may be required due to sulphur content, rich gas, and H2S. Manufacturer recommended cylinder oil types remain TBC during FEED for inlet gas, sales gas, stabilizer overheads, acid gas, and sales gas booster reciprocating compressor applications." The vendor should design tank-area piping such that a second cylinder-oil tank can be added downstream without re-piping the existing 400 bbl tank.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-001 | Authoritative package-requirements text is `26020-Package_Requirements.docx` h.30, but the .docx is not locally parseable. Drafts are anchored on DBM SEC-08 / SEC-16. | `_CONTEXT.md` (Source Reference) | DBM-Deepcut SEC-08, SEC-16 | All four documents | Treat DBM SEC-08 / SEC-16 as proximate authority pending source extraction of `26020-Package_Requirements.docx` h.30; mark divergences as `location TBD`. | TBD |
| C-002 | DBM Packages line item (SEC-16 L2602) lists exactly 2 pumps (1 per service) with no spares; this is a single-point-of-failure basis for a compressor-lubrication utility. | DBM SEC-16 L2602 | DBM SEC-08 L2068, L2070 (no spares mentioned) | Datasheet (Construction); Specification R-2.3, R-2.4, R-2.5 | Allow vendor to propose 2 × 100% per service with availability rationale; if EPC retains 1 × 100% basis, document the operational risk and define an on-site spare-pump policy. | TBD |
| C-003 | Tank tags for cylinder lube oil tank and crank-case lube oil tank are not stated in DBM (SEC-08 L2065–L2070); only the pump tags P-9240-1 and P-9250-1 are stated. | DBM SEC-08 L2065–L2070 | DBM SEC-16 L2602 (pump tags only) | Datasheet (Construction); Specification R-2.1, R-2.2 | Vendor to propose tank tags consistent with the 9240 / 9250 family; EPC tag-register to confirm. | TBD |
| C-004 | Cylinder-oil grade differentiation across compressor services is "TBC" in DBM L2072 but has direct implications for whether the package supports one grade or multiple grades in the initial build. | DBM SEC-08 L2072 | Compressor-vendor data (not yet available) | Specification R-1.4, R-2.1; Guidance "Multi-grade cylinder oil capability" | Initial build per current DBM (one cylinder-oil grade, 400 bbl); layout to reserve area for a future second cylinder-oil tank. Vendor to flag if compressor-manufacturer rulings during detailed design require multi-grade at build time. | TBD |
| C-005 | "Additional storage requirements remain TBD" (DBM SEC-08 L2072) is open — likely includes used / contaminated oil collection and additional cylinder-oil grades. | DBM SEC-08 L2072 | (no second source) | Datasheet (Open / TBD); Specification §Scope (out-of-scope listing) | Treat used-oil collection as out of PKG-076 scope unless EPC explicitly adds it; vendor to highlight as recommended optional scope. | TBD |
