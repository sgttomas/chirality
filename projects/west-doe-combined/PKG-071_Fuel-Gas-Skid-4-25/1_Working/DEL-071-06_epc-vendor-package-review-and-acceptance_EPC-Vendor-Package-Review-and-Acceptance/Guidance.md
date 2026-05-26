# Guidance — DEL-071-06 EPC Vendor Package Review and Acceptance

## Purpose

This guidance explains why the EPC Vendor Package Review and Acceptance deliverable exists and how the EPC Integrator should approach reviewing the Fuel Gas Skid 4-25 vendor package. It is the EPC Integrator's evidence that the vendor package conforms with the EPC Scope of Work, Package Datasheet, and Construction Work Package, and that the package is ready for integration handoff (source: _CONTEXT.md; DELIVERABLE_REGISTER.csv row 335).

## Principles

- **Acceptance is not certification.** The EPC Integrator records review and acceptance evidence. Final certification of code-regulated items remains with the qualified authority. (ASSUMPTION: aligns with K-AUTH-1 governance posture.)
- **Source-anchored conformance.** Every accepted requirement must trace to an accessible source slice — either the EPC SOW / Package Datasheet / CWP for this package, or the 04-25 Deepcut DBM where those documents are themselves grounded.
- **Open items remain open.** Unresolved interface items (e.g., shared 03-25/04-25 demand split, acid-gas dilution case inclusion — see Conflict Table) must be carried as TBD on the acceptance checklist; do not silently resolve them at acceptance time.
- **Shared utility before standalone skid.** The fuel-gas skid is part of a shared 03-25/04-25 utility system (4-25_Deepcut_DBM.md sec. Fuel Gas Basis). Acceptance must explicitly check the package boundary against both 04-25 internal users and the 03-25 cross-facility supply interface.

## Considerations

- **Cross-facility utility coupling.** The fuel-gas system supplies users at 04-25 and is shared with 03-25; the demand split and boundary isolation philosophy are not finalized in the current basis (DBM sec. Fuel Gas Basis). Acceptance should confirm that vendor design margin envelopes the maximum plausible combined-facility demand.
- **Demand envelope.** The DBM lists individual buyback components (start gas 3.6 MMSCFD; heat-medium heater 3.90 MMSCFD; TEG stripping 0.30 MMSCFD; compressor packing 0.15 MMSCFD) with a total marked TBC and an acid-gas dilution worst case up to 23.8 MMSCFD whose inclusion is TBD (DBM sec. Emergency Buyback and Purge). Acceptance should verify the vendor's design margin against whichever total DEL-071-02 ultimately publishes.
- **Site-driven design.** The -40 deg C minimum ambient governs exposed equipment, panels, instrumentation, and field devices unless a stricter package-specific basis applies; site basis also drives snow, wind, and elevation loads (DBM sec. 2.2 Site Data Basis). Acceptance should specifically inspect winterization, electric heat tracing, panel ratings, and structural design loads.
- **Regulator philosophy.** The DBM requires 2 x 100% regulator sparing, individual isolation, outlet test connections, and a distinct quick-acting start-gas regulator type (DBM sec. Fuel Gas Equipment and Controls). Acceptance should specifically verify these features in vendor P&IDs and instrument indexes.
- **Emergency-generator classification.** The < 66 psig limit at the emergency-generator supply is electrical-classification driven; design and start-gas flows must coexist in the piping/vessel sizing (DBM sec. Fuel Gas Equipment and Controls). Acceptance should verify the supply pressure regulator(s) and stress-case sizing.
- **Hazard basis.** Sweet-gas purge supply touches methyl-mercaptan toxicity (IDLH 150 ppmv) and odour considerations; a formal hazard review is required before finalizing purge and analyzer maintenance practices (DBM sec. Emergency Buyback and Purge). Acceptance should confirm that this hazard review either exists or is captured as an open item.
- **Sibling deliverable maturity.** DEL-071-01, DEL-071-02, DEL-071-03, DEL-071-04, DEL-071-05 are also currently OPEN (PKG-071 1_Working folder inspection). Acceptance evidence cannot be finalized before those acceptance-basis documents are themselves at INITIALIZED or later maturity.

## Trade-offs

- **Strict conformance vs. interface flexibility.** Where the DBM carries unresolved items (shared demand split; acid-gas dilution sizing), strict conformance is impossible. The Integrator should prefer documenting the gap over forcing closure.
- **Vendor scope vs. EPC scope at the skid edge.** The shared fuel-gas/instrument-air building basis (DBM sec. Fuel Gas Basis) means several interface decisions sit outside the vendor's battery limit. Acceptance should not absorb work that the SOW assigns outside the vendor's scope.
- **Document review depth.** TBD — the depth of vendor document review (e.g., full calculation re-check vs. document-completeness check) is a judgment call that should be governed by DEL-071-01.

## Examples

- An acceptance checklist line for REQ-5 may read: "Vendor inlet rating envelopes J-T-mode high supply pressure 2895 kPag and water content < 0.1 ppmv H2O: ACCEPTED — vendor doc VND-XYZ rev 0, Table 3. (Source: DEL-071-02 sec. Interfaces; vendor doc location TBD.)"
- An open-items entry for REQ-13 may read: "Shared 03-25/04-25 fuel-gas demand split: TBD pending human ruling per Conflict Table CONFLICT-1."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-1 | Shared 03-25/04-25 fuel-gas demand split and facility-boundary isolation philosophy not finalized | 4-25_Deepcut_DBM.md sec. Fuel Gas Basis (basis does not close the demand split) | _CONTEXT.md / decomposition row 335 (PKG-071 packaged as a single skid at 04-25) | Datasheet (Attributes); Specification REQ-5, REQ-13; Procedure step 4 | PROPOSAL: hold acceptance of cross-facility demand allocation until DEL-071-02 publishes a closed split | TBD |
| CONFLICT-2 | Acid-gas-compressor worst-case dilution-gas case (up to 23.8 MMSCFD) — inclusion in buyback sizing not decided | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge | TBC during detailed engineering | Datasheet (Conditions); Specification REQ-5, REQ-13 | PROPOSAL: defer to DE outcome; carry as open item at acceptance | TBD |
| CONFLICT-3 | Acceptance-basis document availability | _CONTEXT.md / decomposition expects DEL-071-01/02/03 as acceptance basis | PKG-071 1_Working folder shows DEL-071-01/02/03 currently OPEN (not yet drafted) | All requirements REQ-1 through REQ-4 | PROPOSAL: hold acceptance execution until sibling deliverables reach INITIALIZED at minimum | TBD |
