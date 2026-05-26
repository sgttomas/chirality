# Guidance: DEL-082-04 — Vendor Engineered Equipment Package (Flare KO Drum, Low Pressure, 3-25)

## Purpose

This guidance explains why the Vendor Engineered Equipment Package deliverable exists, the principles that govern vendor production within the PKG-082 envelope, the considerations that shape successful execution, the trade-offs the vendor and the EPC Integrator should consciously balance, and illustrative examples drawn from the accessible source basis.

The deliverable exists because the LP flare KO drum (V-3900-2) and its transfer pump (P-3900-2) are vendor-engineered equipment items that the EPC Integrator does not design internally. The EPC Integrator defines the package envelope through the Scope of Work (DEL-082-01) and the Package Datasheet (DEL-082-02); the vendor closes the engineering loop by producing a code-compliant, sized, fabricated, and documented package that the EPC Integrator can review (DEL-082-06), receive turnover documentation for (DEL-082-05), and integrate into the 03-25 facility.

## Principles

1. **EPC anchors the envelope; vendor closes the engineering.** The EPC Scope of Work and Package Datasheet set the boundary conditions (service, tags, relief loads, materials, codes). The vendor is responsible for engineering inside that envelope. (Source: `_CONTEXT.md` Scope.)
2. **Source basis governs over convention.** Where the accepted 03-25 DBM names a value (e.g., V-3900-2 tag, P-3900-2 sparing 1 x 100 percent, LP relief services list), that value is authoritative. (Source: DBM line 499, 584.)
3. **The drum is one node in a coordinated relief system.** Staggered blowdown is required to limit maximum relief; the LP KO drum cannot be designed in isolation from the system relief profile. (Source: DBM line 501.)
4. **Mark unknowns explicitly.** Drum sizing, design pressure/temperature, materials, and code basis are TBD until the EPC Package Datasheet (DEL-082-02) and the external blowdown philosophy W242510-PRC-REP-000003-001 are accepted/sliced. Do not invent values.
5. **Vendor documentation feeds DEL-082-05.** Engineering deliverables produced here become the seed of the turnover package; treat documentation discipline as a first-class requirement, not an afterthought.

## Considerations

- **Sour service** is the working assumption for the 03-25 facility (DBM line 607). Vendor material selection should be planned for NACE MR0175 / ISO 15156 compliance pending EPC datasheet confirmation.
- **Shared LP flare stack** with HP/Cryo dual stack means the vendor must accept the LP flare back-pressure envelope set by the EPC Integrator; back-pressure is not a vendor-set value. (Source: DBM line 497, 499.)
- **Header size vs. drum nozzle size** are distinct. The 20 inch / 508 mm value applies to the LP relief header (DBM line 499); the drum's inlet nozzle is a vendor sizing output, not a copy of the header size.
- **External blowdown philosophy access.** W242510-PRC-REP-000003-001 is referenced but not locally accessible (DBM line 501). Vendor sizing inputs should be requested explicitly from the EPC Integrator rather than assumed.
- **Pump scope.** The transfer pump P-3900-2 is part of the vendor scope; coordination with EPC mechanical/electrical disciplines (motor supply, MCC location, suction NPSH) is necessary.
- **Slop routing terminus.** The pump discharges to slop (DBM line 499); the slop receiver tag and elevation must be coordinated with the EPC Integrator — TBD at this draft.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Drum size vs. site footprint | Larger drums simplify level control and offer more vapor disengagement headroom; site footprint and structural cost favor smaller drums. The relief load case sets the floor. |
| Skidded vs. field-erected | Skidded reduces site labor and improves vendor QC; field-erected may be necessary if the relief volume exceeds shippable diameters. (ASSUMPTION pending size resolution.) |
| Carbon steel vs. sour-service-qualified material | CS is lower cost; sour-service qualification adds material and inspection cost but is required if H2S exposure crosses NACE thresholds. Treat as sour until proven otherwise. |
| Demister selection | Wire-mesh demisters are lower cost; vane-pack demisters handle higher velocity ranges and fouling. Service is TEG/VRU/seal-pot — fouling potential is non-trivial; vendor to justify. (ASSUMPTION.) |
| Single-pump 1 x 100 percent vs. spared | Source basis is 1 x 100 percent (DBM line 584); a spare is out of basis. Operability trade-off (single point of failure for liquid evacuation) is accepted at the system level. |

## Examples

- **Example: service list grounding.** The Specification R1 statement that V-3900-2 receives TEG regeneration, VRU, and compressor seal-pot LP relief is taken directly from DBM line 499; the vendor should not add or remove services without EPC ruling.
- **Example: sparing.** The Specification R3 statement that P-3900-2 is 1 x 100 percent is taken directly from DBM line 584; a vendor proposal of 2 x 100 percent would require an SCA (scope change action), not a vendor preference.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | LP relief header carried as 508 mm / 20 inch in DBM; drum inlet nozzle size not stated. Decomposition narrative does not resolve the drum nozzle sizing pathway. | DBM `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 499 | `_CONTEXT.md` (silent on nozzle sizing) | Datasheet Attributes; Specification R9 | Vendor sizes drum nozzles per relief load; header size is informational only | TBD |
| C-02 | Blowdown philosophy W242510-PRC-REP-000003-001 is referenced by DBM line 501 but not locally accessible. DBM line 529 also notes a cross-reference conflict where the same document number appears in a prime-mover/emissions context. | DBM line 501 | DBM line 529 | Specification R5, R6; Procedure Step 2 | EPC Integrator to provide the LP relief load case to the vendor via DEL-082-02; document number cross-reference flagged for ruling | TBD |
