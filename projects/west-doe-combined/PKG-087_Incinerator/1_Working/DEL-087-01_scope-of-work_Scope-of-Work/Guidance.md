# Guidance — DEL-087-01 Scope of Work (PKG-087 Incinerator)

> Pass: P1_P2. Directional guidance and rationale for the EPC Scope of Work. Where source authority is mixed or absent, items are surfaced as `TBD` or as Conflict Table rows for human ruling.

## Purpose

The Scope of Work is the EPC Integrator's anchor artifact for the Incinerator package. It binds the vendor-supplied package (knockout drum, knockout drum transfer pump, low-pressure flare stack, and blower per `PACKAGE_REGISTER.csv` row 64) into the wider process facility by establishing what the package is, what it does, what the EPC owns, and where the package meets the facility. Downstream deliverables (`DEL-087-02` Package Datasheet, `DEL-087-03` Construction Work Package, `DEL-087-06` EPC Vendor Package Review and Acceptance) rely on this Scope of Work as the controlling identity and boundary definition.

## Principles

P-01. **Source fidelity over restatement.** Where source language exists (`PACKAGE_REGISTER.csv` row 64; `DBM-Deepcut`; `DBM-Comp_and_Liquids`), the Scope of Work uses it verbatim or by faithful summary. Decomposition narrative routes; sources determine content.

P-02. **EPC/Vendor split is non-negotiable.** Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (`PACKAGE_REGISTER.csv` row 64). The Scope of Work shall not absorb vendor scope and shall not delegate integration scope.

P-03. **Open items are open items.** Where the DBM marks supplemental fuel gas rate, incinerator flow basis, and 03-25/04-25 operational responsibility as `TBD` (`DBM-Deepcut` line 1572), and dilution/enrichment gas as `TBC` (`DBM-Deepcut` line 1890), the Scope of Work mirrors that status rather than asserting closure. The package is sourced and integrated under those open items as constraints, not under invented values.

P-04. **Spacing and layout act on EPC scope.** The 25 m (82 ft) minimum spacing rules (`DBM-Deepcut` lines 280, 296, citing OGAOM Sec. 9.6.15) bind the EPC Integrator's plot-plan and constructability decisions and shall propagate to `DEL-087-03`.

P-05. **Backflash-protection facts bound the inlet interface.** The spent caustic tank and DSO storage tank vent through flame arrestors to the incinerator header (`DBM-Comp_and_Liquids` line 402; `DBM-Deepcut` lines 1562, 1564). The Scope of Work locates these protections on the contributing tank packages and does not duplicate them onto the incinerator package itself.

## Considerations

C-01. **Cross-facility service split (03-25 vs 04-25).** `DBM-Comp_and_Liquids` line 56 records the incinerator as a shared-interface system governed by the current 03-25/04-25 allocation, with the exact service split and owner interface carried as an open interface item. `DBM-Deepcut` line 1570 says the incinerator is physically located at the 3-25 facility and services the 4-25 NGL mercaptan treating system, while `PACKAGE_REGISTER.csv` row 64 lists `PKG-087` Incinerator under WBS 02 (Deepcut, 4-25). This conflict is recorded in the Conflict Table below.

C-02. **Tag-to-equipment mapping.** `DBM-Deepcut` Tag-Detail row 32 lists four tags (`B-6920-1`, `FL-6920-1`, `P-6900-1`, `V-6900-1`) but does not provide per-tag descriptors. The Datasheet maps each tag to one of the four vendor-supplied items by name match (`V-6900-1` → knockout drum; `P-6900-1` → knockout drum transfer pump). The mapping to blower/stack (`B-6920-1`, `FL-6920-1`) is an `ASSUMPTION` and needs vendor or EPC confirmation.

C-03. **Emissions basis is future scope.** Incinerator emissions in the source emissions tables are flagged as future scope with a current non-regenerative-caustic basis `TBD` (`DBM-Deepcut` lines 2244-2246, 2295). The Scope of Work does not commit to emissions values; downstream permitting work must close this gap independently.

C-04. **Bid documents and Word package section not locally accessible.** `26020-Package_Requirements.docx` package heading 40 and `26020-01-PT-RFQ-25-003_Incinerator.docx` are listed in `_REFERENCES.md` but not locally available in markdown form for this run. Section-level requirements that depend solely on those documents remain `TBD` here.

## Trade-offs

T-01. **Tighter sourcing vs. coverage.** Listing only source-grounded requirements yields a smaller but auditable Scope of Work. The alternative — folding in decomposition narrative as if it were source — would broaden coverage but violate authority hierarchy and would over-state vendor obligations. The Scope of Work prefers tighter sourcing.

T-02. **Shared-incinerator service allocation.** If the incinerator physically resides at 03-25 (`DBM-Deepcut` line 1570) but is registered under `PKG-087` at facility 04-25 (`PACKAGE_REGISTER.csv` row 64), the EPC Integrator absorbs a cross-facility interface inside an intra-facility package definition. The trade-off is between rewriting the package identity (out of scope here) and carrying the cross-facility allocation as an open interface item bound to this Scope of Work (preferred).

## Examples

Example tag and supplied-item line (Datasheet §Attributes):

```
| V-6900-1 | Incinerator knockout drum | PACKAGE_REGISTER.csv row 64; DBM-Deepcut Tag-Detail row 32 |
```

Example responsibility-assignment row (the EPC/Vendor split — `PACKAGE_REGISTER.csv` row 64 verbatim):

> Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Incinerator facility location and service ownership: DBM-Deepcut says the incinerator is physically located at 3-25 and services the 4-25 NGL mercaptan treating system; the package register lists `PKG-087` under WBS 02 / facility 4-25 (Deepcut). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1570 ("Incinerator Interface" section) | `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 64 | Datasheet §Identification; Specification R-06; Guidance C-01, T-02; Procedure step 4 | Treat `PACKAGE_REGISTER.csv` row 64 as the package-identity authority (Gate-7 accepted snapshot), and carry the 03-25/04-25 service split as an open interface item bound to this Scope of Work | `TBD` |
| CONF-02 | Supplied-item-to-tag mapping for `B-6920-1` (blower) and `FL-6920-1` (low-pressure flare stack) is not explicit in the DBM tag list. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Tag-Detail row 32 | `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 64 supplied-items list | Datasheet §Attributes; Datasheet §Construction items 3-4 | Confirm tag-to-item mapping with Package Vendor at RFQ clarification | `TBD` |
