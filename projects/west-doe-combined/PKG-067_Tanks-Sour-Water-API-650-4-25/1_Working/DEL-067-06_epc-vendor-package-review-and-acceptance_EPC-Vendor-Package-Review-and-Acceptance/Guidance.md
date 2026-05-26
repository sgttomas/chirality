# Guidance — DEL-067-06 EPC Vendor Package Review and Acceptance

## Purpose

Provide the EPC Integrator's reviewer / acceptance team with the rationale, principles, and trade-off considerations needed to apply the Specification (`Specification.md`) effectively to the Tanks, Sour Water (API 650) 4-25 package (`PKG-067`, `26020-01-PT-19-005`). This deliverable is the EPC-side acceptance record for `DEL-067-04` (Vendor Engineered Equipment Package) and `DEL-067-05` (Vendor Document Turnover), evaluated against `DEL-067-01..03` anchors.

Source basis: `DELIVERABLE_REGISTER.csv` row `DEL-067-06`; `_CONTEXT.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Produced Water.

## Principles

- **Sour-service caution drives acceptance margin.** The DBM (line 524) explicitly flags that "tank isolation philosophy must be reviewed in the context of potential sour vapours." Acceptance must not treat the package as a benign atmospheric storage installation: blanket-gas, VRU, PVRV/EPRV, and isolation logic warrant explicit review.
- **Modified API 650 with 16 oz test pressure is the design anchor.** Vendor deviation from this design anchor (line 518) is a flag for human review.
- **Coating, insulation, heating, and skim are not optional appurtenances at 04-25.** The DBM (line 524) prescribes Devchem 253 (floor/walls/roof), external insulation, electric heating, and Kennilworth-type hydrocarbon skim float system; absence in vendor submittals is a non-conformance, not a value-engineering opportunity, unless an approved deviation exists.
- **Storage-basis sizing is the EPC's traceability link.** The 2 × 2,000 bbl / 380 bbl/d / 8.9-day basis (line 493) defines the operational intent the EPC Integrator must reconcile with vendor capacity claims.
- **Fluid characterization remains incomplete.** The DBM (line 508) labels the fluid composition list as "not comprehensive and is to be confirmed." Acceptance must explicitly carry this incompleteness — not silently treat the vendor's assumed composition as confirmed.
- **The downstream produced-water pipeline is out of scope.** Per DBM line 506, the pipeline is "designed and installed by others"; the EPC Integrator's acceptance terminates at the pipeline riser at the gas plant facility boundary.

## Considerations

- **Open-items posture.** The DBM lists several explicit TBCs/TBDs relevant to acceptance: produced-water transfer pumps suction arrangement (line 521), filtration requirement (line 522), tank design SG (line 508), EPRV sizing (line 524), tank isolation philosophy (line 524), MAWP / route / elevation / outlet condition of the downstream pipeline (line 564). Acceptance should not "close" these silently.
- **Interface coverage breadth.** PKG-067 carries nine `YES` interface marks in `INTERFACE_REGISTER.csv` (Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports). Acceptance must walk down each interface; partial coverage is a failure mode.
- **Spacing constraints are project-specific.** NFPA 30 and OGAOM 9.6.15 spacing values from the DBM (lines 261-297) drive plot-plan acceptance; reviewers must check the as-built dimensions, not just the IFC plot plan.
- **Pressure-equipment registration jurisdiction is not stated.** The accessible sources do not pin down whether the registration regime is ABSA (Alberta) or BC equivalent; this is a `HRR` candidate (see Conflict Table).
- **Analog basis acknowledged in decomposition.** `PACKAGE_REGISTER.csv` row `PKG-067` notes the scope is built on "Analog basis from 26020-03-PT-19-007_Tanks_Sour_Water" with no direct package-folder brief / DOCX / PDF for 4-25 found. Acceptance criteria derived from analogous scope are inherently `ASSUMPTION`-flavored until the vendor's actual scope statement is on file.

## Trade-offs

- **Strict design-basis adherence vs. vendor standard product offering.** Vendors with standardized tank designs may push back on Kennilworth skim, Devchem 253 specifics, or 16 oz test pressure. The EPC Integrator should resist value-engineering substitutions absent an explicit, technically equivalent deviation accepted by the Owner / Engineer.
- **EPRV sizing detail vs. acceptance throughput.** EPRV sizing is flagged for detailed-engineering review (DBM line 524). The acceptance can either hold the package until EPRV sizing is closed or accept with a documented carryover. The latter is faster but increases handoff risk to commissioning.
- **Provincial registration timing.** Pressure-equipment registration acceptance may lag fabrication completion. Accepting on the basis of an "in-flight" registration package is common practice but creates a turnover dependency; the acceptance log should make this explicit.
- **Composition assumptions vs. operational reality.** Tightening fluid-composition assumptions for materials selection (e.g., NACE compliance) trades extra vendor cost for reduced risk of in-service degradation; given the incomplete composition list (DBM line 508), accepting conservative material selection is preferred.

## Examples

- A vendor submittal proposes uncoated tank floors with cathodic protection in lieu of Devchem 253 internal coating: reject without explicit deviation per DBM line 524.
- A vendor proposes a single PVRV per tank pair (shared header) instead of "at least one PVRV per tank": flag as a non-conformance and require either per-tank PVRV or an accepted relief-philosophy deviation.
- A vendor's pressure-test record uses 24 oz test pressure: acceptable (exceeds 16 oz basis); record the higher value in the acceptance log.
- Vendor data sheet uses tank design SG = 1.20: reconcile against the DBM "1.25 (TBC)" basis; either accept with a documented Owner ruling or push the vendor to align.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| `CONF-067-06-01` | Tank capacity basis: DBM specifies 2 × 2,000 bbl for produced water at 04-25, while the `PACKAGE_REGISTER.csv` row `PKG-067` calls out a 4-25 tank pair "matching the 4-25 tank pair identified in the 3-25 sour water analog" without a numeric capacity, and other 4-25 PKGs (PKG-098) reference 3,800 bbl tanks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 493 (2 × 2,000 bbl) | `PACKAGE_REGISTER.csv` row `PKG-067` (analog basis, capacity unstated); `ARTIFACT_REGISTER.csv` `ART-340A371C42` etc. (3,800 bbl tanks elsewhere) | Datasheet "Storage basis"; Spec `R-067-06-05` | Use DBM 2 × 2,000 bbl unless `DEL-067-02` Package Datasheet has been re-baselined; flag for confirmation. | TBD |
| `CONF-067-06-02` | Provincial pressure-equipment registration jurisdiction (ABSA vs. BC equivalent) is not stated in accessible sources. | Spec `R-067-06-12` (ASSUMPTION) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 133 (BC ER permitting for 03-25, no statement for tank registration) | Spec Standards table; Spec `R-067-06-12` | Treat as BC jurisdiction by default pending Owner ruling. | TBD |
| `CONF-067-06-03` | Sour-service material-selection code citation (NACE / MR-0175) is not explicit for PKG-067 in accessible sources; analogous PKG-096 row explicitly cites "NACE compliant". | `ARTIFACT_REGISTER.csv` `ART-5AF4728A78` (no NACE clause for PKG-067) | `ARTIFACT_REGISTER.csv` `ART-BE664573F5` (PKG-096 sour service NACE) | Spec Standards table | Adopt NACE MR-0175 as governing for sour-service materials by analogy, with explicit ASSUMPTION label. | TBD |
| `CONF-067-06-04` | The accessible source set does not include a directly readable rendering of `26020-Package_Requirements.docx` Heading 22; clause-level acceptance must rely on `PACKAGE_REGISTER.csv` and `ARTIFACT_REGISTER.csv` summaries plus the DBM. | `_REFERENCES.md` (Missing / Deferred References) | `_Sources/26020-Package_Requirements.docx` (binary, not extracted to Markdown) | All four production documents | Accept register/DBM-derived basis with "location TBD at clause level"; surface for the next pass to ingest the DOCX. | TBD |
