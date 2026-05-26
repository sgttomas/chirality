# Guidance — DEL-072-03 Construction Work Package (Truck Product Loading Unit 4-25)

## Purpose

This Construction Work Package (CWP) exists because `PKG-072` (Truck Product Loading Unit 4-25) is a mandatory Gate-5 EPC anchor deliverable. It is the single integrating document that the EPC Integrator uses to plan, sequence, and turn over the physical installation, tie-in, and inspection of the truck loading station scope at the 04-25 Deep Cut Gas Plant in coordination with the 03-25 Liquids Hub interface. (Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-072-03; `4-25_Deepcut_DBM.md` site definition.)

## Principles

- **EPC Integrator owns the build sequence.** Vendor delivers the package; EPC integrates it. The CWP is the boundary document that translates vendor design data into field execution work. (`_CONTEXT.md` ResponsibleParty; `26020-Package_Requirements.docx` Vendor Engineering Deliverables section establishes the vendor data baseline.)
- **Construct to the interface summary, not to assumed scope.** Where the package's Physical Interface Summary marks an interface "Yes", the CWP must include design, install, test, and turnover steps for it; where "No", the CWP must not add work without a documented scope change. (`26020-Package_Requirements.docx` Physical Interface Summary.)
- **Hold separation distances as hard gates.** API 2510 separation distances around pressurized bullets and the truck loading station are inviolable layout constraints; resolve any layout conflict before foundations work begins. (`4-25_Deepcut_DBM.md` lines 257-258.)
- **Source > narrative.** Where a value or rule is in `26020-Package_Requirements.docx` or `4-25_Deepcut_DBM.md`, prefer the source over decomposition prose; where the source is silent, prefer `TBD` to invention.

## Considerations

- **LACT scope ambiguity** at the 04-25 plant level (`4-25_Deepcut_DBM.md` lines 62, 82, 171) may affect truck-loading metering interfaces. The CWP should not lock fabricated metering tie-in geometry until LACT ownership and inclusion are confirmed.
- **Permitting amendment for the truck rack** must be tracked; the CWP execution sequence should hold any work that depends on truck-rack permit closure until the amendment is in place. (`4-25_Deepcut_DBM.md` line 133.)
- **Site off-loading responsibility.** The 04-25 DBM identifies off-loading of modules and equipment at site as Tourmaline field construction scope (`4-25_Deepcut_DBM.md` line 112). The EPC Integrator should confirm whether truck loading station modules fall under that delineation or under the package vendor's shipping plan (PRQ-013).
- **Source data quality** — see Conflict Table below: the `26020-Package_Requirements.docx` section heading `26020-01-PT-23-001 — Condensate Truck Loading Stations` contains "Basic Scope / Major Included Equipment" prose that describes a Low-Pressure Fuel Gas Skid, not a truck loading station. The interface summary and vendor deliverable list at the bottom of the section are still applicable to truck loading; the equipment-level prose must be sourced from the correct vendor RFQ for truck loading stations.
- **NGL truck distribution is not planned** from 04-25 (`4-25_Deepcut_DBM.md` line 446). The 4-25 Truck Product Loading scope is therefore expected to be condensate-focused, consistent with the section title "Condensate Truck Loading Stations". Confirm during detailed engineering.
- **Common truck-out connection** at condensate tanks (`4-25_Deepcut_DBM.md` line 1661) implies a shared tie-in geometry the CWP must coordinate with the tank-farm CWPs.

## Trade-offs

- **Single mobilization vs. staged build.** Concentrating civil, structural, piping, electrical, and I&C work into a single mobilization minimizes rework but increases sensitivity to vendor data delays (MEC-016/017, STR-006/013, INS-005/006). Staging the work allows earlier permit/LACT issues to be resolved but extends schedule.
- **Tie-in via temporary spool vs. final geometry.** Where the LACT/metering decision is open, temporary spools may protect schedule at the cost of a future hot-tap or recut.
- **Use vendor IOM (MEC-025) verbatim vs. site-adapted procedures.** Vendor procedures are authoritative for warranty; site-adapted procedures may better fit cold-weather or co-located work. The CWP should default to vendor IOM unless a site engineering memo authorizes deviation.

## Examples

- The CWP should reference STR-006 Foundation Drawings and STR-013 Anchor Bolt / Embedment Drawings as the geometric authority for the loading station foundation footprint and anchor pattern. (`26020-Package_Requirements.docx` Vendor Engineering Deliverables, Structural section.)
- The CWP should reference TSF-004 Fire and Gas Detector Layout Drawings as the authority for F&G detector placement around the truck loading station. (Same source, Fire & Gas section.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-072-03-01 | Section `26020-01-PT-23-001 — Condensate Truck Loading Stations` "Basic Scope" / "Major Included Equipment" prose describes a Low-Pressure Fuel Gas Skid, not a truck loading station. | `26020-Package_Requirements.docx` (Truck Loading Stations section body) | `26020-Package_Requirements.docx` (Truck Loading Stations section title + Location/Status + interface summary) | Datasheet Attributes, Specification Requirements | Treat the section title, Location/Status line, Physical Interface Summary, and Vendor Engineering Deliverables list as authoritative for truck loading; treat the misplaced prose as a source error and request the correct truck-loading RFQ (`location TBD`). | TBD |
| CFL-072-03-02 | Vendor Source Basis line names `26020-01-PT-RFQ-23-001_FG_Skid_2.docx`, which is inconsistent with a Condensate Truck Loading Stations package. | `26020-Package_Requirements.docx` (Truck Loading Stations section Source Basis line) | Section title and interface scope | Datasheet References | Request the correct truck-loading RFQ; record current source as `location TBD`. | TBD |
| CFL-072-03-03 | "No truck or rail distribution is planned for NGL product from 04-25" but PKG-072 is named "Truck Product Loading Unit 4-25". | `4-25_Deepcut_DBM.md` line 446 | `_CONTEXT.md` PackageName; `26020-Package_Requirements.docx` section title (Condensate Truck Loading Stations) | Specification Scope, Datasheet Service | Scope is condensate truck loading (not NGL); confirm with detailed engineering. | TBD |
| CFL-072-03-04 | LACT scope/ownership is "TBD" at the 04-25 DBM level; may affect truck-loading metering tie-ins. | `4-25_Deepcut_DBM.md` lines 62, 82, 171 | `26020-Package_Requirements.docx` Loading/Metering Package section (INS-015 Metering Package Specification) | Specification REQ-072-03-12 | Hold metering tie-in geometry until LACT decision is documented. | TBD |
| CFL-072-03-05 | Site off-loading of modules listed as Tourmaline field construction scope, vs. EPC Integrator ownership of CWP. | `4-25_Deepcut_DBM.md` line 112 | `_CONTEXT.md` ResponsibleParty = EPC Integrator | Specification Scope (Includes); Procedure Step 1 | Confirm off-loading responsibility for truck-loading modules specifically. | TBD |
