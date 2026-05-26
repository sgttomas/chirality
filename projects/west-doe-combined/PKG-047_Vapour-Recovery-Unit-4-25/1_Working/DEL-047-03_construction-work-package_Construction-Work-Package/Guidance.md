# Guidance — Construction Work Package (VRU 4-25)

DeliverableID: `DEL-047-03_construction-work-package`
ParentPackageID: `PKG-047`

## Purpose

Provide the EPC Integrator's construction execution view of the VRU 4-25 package. The Construction Work Package is the bridge between vendor-supplied compressor trains and the operating 04-25 facility: it answers how the package is received at site, set, tied in, electrically connected, mechanically completed, and turned over to commissioning. It is the Gate 5 EPC anchor for this package (per `_CONTEXT.md` and the decomposition deliverable register).

## Principles

1. **Vendor designs; EPC integrates.** Per OBJ-004 and SOW-0253, package engineering/design/equipment/documentation belong to the Package Vendor. The Construction Work Package authority is bounded to installation, tie-in, integration, and turnover.
2. **Sour service governs construction discipline.** The VRU process envelope is sour (H2S 0.3557 mol%, CO2 0.9434 mol% per DBM and SOW-0255). NACE designation, weld procedures, NDE, and post-install testing follow sour-service rules without exception.
3. **Tie-ins routed by the DBM, not improvised on site.** Inlet collection, discharge to SOC first-stage suction, and primary seal vent to LP flare are explicit DBM routings; the construction package implements them, it does not reinterpret them.
4. **Carry source conflicts forward, do not silently resolve.** Conflicts between SOW-0254/0256 and the DBM body (motor voltage, building count, dewpoint values) are explicitly captured in the Conflict Table below for human ruling; do not let a construction crew pick the value.
5. **Mechanical completion is evidence-bearing.** Every R6 turnover line must be supported by a signed record. Verbal sign-off is not acceptable for sour-service tie-ins or for VFD/motor commissioning.

## Considerations

- **"By others" scope is the EPC scope.** SOW-0256's "By others" list (shipping, piles, tie-in piping, electrical connections, mounting platform and stairs) is precisely the EPC Integrator's construction scope. The wording is from the vendor's perspective; the responsibility flips when read from the EPC perspective.
- **Two units, lead-lag.** SOW-0254 and the DBM both call for 2 x 100% in lead-lag operation. Construction must ensure both trains can run independently and that the standby unit can be brought online without taking the lead unit down — relevant to isolation valving, drains, and electrical sectionalizing.
- **Condensation risk at 1st-stage cooler.** DBM notes the first-stage cooler discharge temperature (48.9 C) is below dewpoint (52.7 C in DBM, 45.6 C in SOW), so condensation is expected. Construction must ensure the suction scrubber upstream of the second stage is correctly oriented, drains free, and is reachable for inspection. (DBM VRU Scrubbing/Cooling section.)
- **Both 04-25 and 03-25 VRUs discharge to 04-25 SOC.** The 03-25 VRU tie-in interface to the 04-25 SOC suction header is a cross-facility interface and may have a different construction owner; coordinate with the 03-25 construction scope and confirm interface custody before tie-in. (DBM VRU section.)
- **Pre-commissioning purge regime.** First gas-in on a sour service package requires inerting (typically N2) and a controlled purge to fuel-gas blanket, governed by facility procedures referenced in DBM SEC-14/SEC-15 (not extracted locally for this deliverable).
- **VFD / 600 V vs 4,000 V conflict (CFL-1).** Until ruled, construction cannot finalize cable sizing, conduit/tray, motor pad layout, or local disconnect rating. Hold electrical detail downstream of this ruling.
- **One building vs two buildings conflict (CFL-2).** Until ruled, civil layout, HVAC scope, gas detection coverage, and electrical room siting cannot be fixed. Hold civil/building detail downstream of this ruling.

## Trade-offs

- **Single-building consolidation (SOW-0254)** reduces civil footprint and may simplify HVAC and electrical-room sharing, but concentrates fire/gas risk and complicates maintenance isolation between trains.
- **Two-building separation (DBM)** preserves train independence and isolation but increases civil, electrical, and HVAC scope. The DBM body is the higher-authority technical document; SOW is the vendor package extract. Default toward DBM unless a human ruling reverses it.
- **VFD-ready 600 V (SOW-0256)** matches typical 200 HP industrial drives and aligns with the SOW package; **4,000 V (DBM)** is normally reserved for larger motors. The 200 HP / 600 V combination is more internally consistent than 200 HP / 4,000 V; recommend a directional PROPOSAL toward the SOW values, but the call is a human ruling.

## Examples

(Sources do not include illustrative examples; section retained per default schema. **TBD**.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-1 | Motor voltage and power | SOW-0256: 200 HP, 600 V, 3-phase, 60 Hz, VFD-ready | 4-25_Deepcut_DBM.md VRU Configuration table: 4,000 V; motor power TBD with 200 hp TBC and 300 hp conflict noted | Datasheet Attributes; Specification R4; Procedure electrical steps | PROPOSAL: SOW-0256 (200 HP / 600 V); 200 HP / 4,000 V is internally inconsistent | TBD |
| CFL-2 | Building count and arrangement | SOW-0254: both trains housed in one building | 4-25_Deepcut_DBM.md VRU Configuration: "Each VRU is installed in an individual building with associated utilities" | Datasheet Attributes (Housing); Specification R5; Procedure civil/building steps | PROPOSAL: DBM (two buildings) — DBM body is the higher-authority technical document for facility layout | TBD |
| CFL-3 | First-stage dewpoint | SOW-0256: 1st stage dewpoint 45.6 C | 4-25_Deepcut_DBM.md cooler table: 1st-stage dewpoint 52.7 C | Datasheet Attributes; Specification (condensation handling implied) | PROPOSAL: defer to DBM cooler-table value (52.7 C) for sizing; both indicate condensation is expected at 48.9 C cooler-discharge, so practical construction implication is the same | TBD |
| CFL-4 | Second-stage dewpoint | SOW-0256: 53.2 C | 4-25_Deepcut_DBM.md cooler table: 55.8 C | Datasheet Attributes | PROPOSAL: DBM value (55.8 C) | TBD |
| CFL-5 | DBM intra-source motor power conflict | DBM VRU table itself: "Motor power: TBD; 200 hp TBC and 300 hp conflict requires ruling" | (intra-source) | Specification R4 | PROPOSAL: 200 HP if CFL-1 resolves toward SOW | TBD |

## Objective Association (PACKAGE_HEURISTIC — ASSUMPTION)

Per `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`, OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 are directionally relevant context for this deliverable (recorded as ASSUMPTION pending human confirmation; explicit mapping in DELIVERABLE_REGISTER.csv row DEL-047-03 confirms this list, so the heuristic and the explicit mapping agree).

The construction scope most directly serves:
- OBJ-004 (vendor/EPC responsibility split) — the very reason this deliverable exists.
- OBJ-008 (civil/structural/site/construction support) — pile foundations, mounting platform, stairs.
- OBJ-005 (electrical) — VFD-ready motor terminations.
- OBJ-009 (sour-service safety, regulatory, codes) — sour-service construction discipline.
- OBJ-007 (utilities, flare, drains) — LP flare tie-in for primary seal vent.
