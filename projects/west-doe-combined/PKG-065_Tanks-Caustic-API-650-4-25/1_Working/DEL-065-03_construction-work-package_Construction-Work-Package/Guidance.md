# Guidance: DEL-065-03 — Construction Work Package (PKG-065)

## Purpose

The Construction Work Package exists to give the field execution team a single, source-grounded basis for installing and turning over the caustic-service atmospheric tanks at the 04-25 Deep Cut Gas Plant. It is the Gate-5 EPC anchor deliverable that converts the package Scope of Work (DEL-065-01) and Package Datasheet (DEL-065-02) into a buildable, inspectable, and turnover-ready field workscope.

## Principles

- **Source-grounded construction.** Construction details shall trace to the 4-25 DBM and to API-650 (where locally accessible). Generic "industry practice" shall not substitute for source basis.
- **Boundary discipline.** The CWP terminates at the package tie-in flanges and at the limits of EPC integrator scope. Vendor-internal mechanical scope is owned by DEL-065-04.
- **Caustic-service awareness.** Caustic NaOH service introduces material, drain, vent, and personnel-safety constraints that differ from condensate or produced-water tankage. Aluminum exclusion (3-25 DBM line 402) is a hard constraint analogously applied at 04-25.
- **Conservative inference, explicit TBDs.** When the 4-25 DBM is silent (coating selection, foundation type, exact tank count), the CWP records TBD rather than borrowing from the 03-25 Liquids Hub caustic basis without confirmation.

## Considerations

- The 4-25 DBM identifies two caustic-service tanks explicitly: a 400 bbl DSO storage tank and a 400 bbl spent caustic storage tank (lines 528, 530). Whether additional caustic-related tanks (fresh caustic, process water) are included in PKG-065 vs. embedded in the vendor caustic treating package (DEL-065-04) is a packaging decision that should be confirmed against the Tank Register before construction planning is finalized.
- Modified API-650 with 16 oz test pressure (line 518) is materially different from standard API-650 in vent-relief and seam-test treatment; the fabricator shall confirm clause-level applicability.
- The 4-25 DBM does not explicitly state the internal coating for caustic-service tanks. Devchem 253 is the produced-water basis (line 524) and shall not be assumed transferable to caustic service without coating-vendor confirmation.
- Site spacing rules (API 2510, NFPA 30 Table 22.4.2.1, OGAOM Sec. 9.6.15) are cited in the 4-25 DBM as table excerpts; full clause text is not in the local source set.

## Trade-offs

| Trade-off | Notes |
|---|---|
| Field-erected vs. shop-built tank | API-650 implies field-erection; size and access at 04-25 are consistent (ASSUMPTION). |
| Coating selection | Higher-cost caustic-resistant lining (e.g., baked phenolic) vs. uncoated stainless plate; selection deferred to detailed engineering. |
| Insulation/heat-trace circuit count | Redundant trace circuits (referenced for caustic drain at 3-25 DBM line 493) trade installed cost against winter operability. |
| Turnover granularity | Tank-by-tank turnover vs. tank-farm-block turnover affects scheduling vs. commissioning agility. |

## Examples

The 4-25 DBM's treatment of the produced-water tanks (lines 521-524) is the closest in-source analog: API-650 Modified, externally insulated and heated, internally coated, with at least one PVRV per tank. The CWP should mirror that level of detail for caustic-service tanks once coating selection is closed.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-01 | PKG-065 tank inventory not enumerated in 4-25 DBM caustic-treating section; 3-25 DBM enumerates four caustic-service tanks (fresh, spent, process water, H2O2) at 03-25, but 4-25 only mentions DSO and spent caustic. | 4-25 DBM lines 526-532 | 3-25 DBM lines 400-402 | Datasheet Attributes; Spec R-01..R-07 | PROPOSAL: Limit PKG-065 to DSO + spent caustic tanks at 04-25 unless tank register confirms additional scope. | TBD |
| CFL-02 | Tank coating for caustic service not specified in any locally accessible source. | 4-25 DBM (silent) | 3-25 DBM line 402 ("caustic tank material/coating details remain TBC") | Datasheet Construction; Spec R-10 | PROPOSAL: Hold coating selection as TBD; require vendor coating-system submittal during detailed engineering. | TBD |
| CFL-03 | Aluminum-exclusion rule is explicit at 03-25 but not restated at 04-25. | 3-25 DBM line 402 | 4-25 DBM (silent) | Spec R-05 | PROPOSAL: Apply aluminum-exclusion to all caustic-service material selection facility-wide. | TBD |
