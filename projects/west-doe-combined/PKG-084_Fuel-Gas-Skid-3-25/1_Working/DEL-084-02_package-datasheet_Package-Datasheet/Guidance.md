# Guidance — DEL-084-02 Package Datasheet (PKG-084 Fuel Gas Skid 3-25)

> Directional guidance on how to read, complete, and use this Package Datasheet, including trade-offs, rationale, and a Conflict Table where source authority disagrees.

## Purpose

This deliverable is the EPC Integrator technical handoff datasheet for the LP Fuel Gas Skid (PKG-084). Its purpose is to give a third-party vendor — or an internal discipline-engineering team — the minimum package data set required to engineer, design, fabricate, and supply the skid while remaining traceable to the project's source-of-truth documents.

The Datasheet is intentionally **package-level, not vendor-level**: it does not specify cylinder dimensions, instrument tag tables, or P&IDs. Those follow under DEL-084-04 Vendor Engineered Equipment Package once the package is in vendor scope.

Per `_CONTEXT.md` Notes: this deliverable is a mandatory Gate 5 EPC anchor, and interface facts are intentionally carried here as evidence rather than as separate deliverables.

## Principles

1. **Source-grounded.** Every non-trivial value in `Datasheet.md` is either traceable to a source slice (DBM, package register, workbook row, or Word source basis) or marked `TBD`. Inferences are labeled `ASSUMPTION`.
2. **Authority hierarchy.** Source materials (locally accessible DBM source slices) are authoritative over decomposition prose. Where they disagree, surface in the Conflict Table — do not silently reconcile (`four-documents/SKILL.md` Authority hierarchy).
3. **Package boundary first.** Datasheet content stops at the package boundary (skid edge or first flange). Whole-facility integration (e.g., shared 03-25/04-25 fuel-gas allocation) is recorded for context, not designed here.
4. **Conservative TBDs.** Where source slices are silent (heater duty, scrubber design pressure, area classification), prefer `TBD` over guessing.
5. **One package, two facility tag-numbers.** The DBMs use V-3210-1 (Deepcut basis) and V-3210-2 (Comp_and_Liquids basis) for the LP fuel gas scrubber. PKG-084 is a single skid; CF-02 records the apparent tag-number duplication for owner ruling.

## Considerations

### Why this package is shared across facilities

The Comp_and_Liquids DBM (L452) places the fuel gas building "at or associated with 04-25" serving the 04-25 gas plant, 03-25 liquids hub, and 03-25 compressor station. The package register entry (PKG-084) is owned within the 3-25 workbook tag (`26020-02-PT-23-001 - Fuel Gas Skid`) but describes service to "the West Doe Deep Cut Facility." This is consistent with a single shared LP fuel gas package physically located at/associated with 04-25 but procured and tracked under the 3-25 workbook. The package datasheet treats the skid as a single shared utility and defers location-of-record to owner ruling (CF-01).

### Heater technology choice

The DBM mandates an electric resistance / SCR-controlled heater (no fired heater), consistent with the facility electrification posture (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L533, electric-drive compressors). This avoids fired-heater siting constraints (OGAOM Sec. 9.6.15 cited at L295-298 in Deepcut DBM for fired heaters) and the associated 25 m / 50 ft spacing rules — these spacing rules do not apply to an electric heater in the same way. However, the area classification of the heater enclosure remains TBD and shall be confirmed by the EPC area-classification deliverable.

### Scrubber K-factor (0.35) rationale

K = 0.35 Imperial with operating-pressure derating is conservative for a low-liquid-load service downstream of sales-gas / dehydration. The DBM (L1874) explicitly notes "minimal liquid is expected." This K value should be retained as a sizing ceiling; vendor may not exceed it without engineering justification.

### Pressure envelope

The supply MAWP cited (9,928 kPag / 1,440 psig) is well above normal supply pressure (5,171–5,516 kPag). The package design pressure must envelop either (a) the full MAWP — robust but possibly costly — or (b) a lower value backed by upstream pressure protection (PSV / regulator failure-mode analysis). This is a project-level pressure-protection ruling, not a vendor decision; it shall be resolved before the package is issued for RFQ.

### Emergency buyback

Sources disagree on whether the emergency buyback fuel-gas tie-in is part of the package (see CF-03). Buyback affects heater sizing ("sized for … winter ambient buyback gas conditions," L1872) and regulator independence (L1878). The current datasheet captures heater sizing basis from the Deepcut DBM but flags buyback inclusion as `NEEDS_HUMAN_RULING` to avoid pre-judging.

## Trade-offs

| Trade-off | Option A | Option B | Recommendation |
|---|---|---|---|
| Package physical location of record | 04-25 (per DBM physical placement) | 3-25 (per package register workbook ownership) | Defer to owner ruling (CF-01); current datasheet preserves both citations |
| Design pressure | Envelop full supply MAWP 9,928 kPag | Lower value backed by upstream pressure protection | Defer to project pressure-protection philosophy; carry as TBD with ASSUMPTION |
| Heater duty TBD vs ASSUMPTION | Hold heater duty TBD until vendor sizing | Provide an EPC-side ASSUMPTION duty | Hold TBD — sizing depends on buyback case which is itself unresolved (CF-03) |
| Single tag (one skid, one scrubber tag) | Use V-3210 (no facility suffix) | Carry both V-3210-1 and V-3210-2 | Defer to owner ruling (CF-02); datasheet carries both for now |
| Relief routing (HP vs LP flare) | Route scrubber PSV to LP flare | Route to HP flare | Defer; depends on facility flare allocation (DBM L497 et seq); carry TBD |

## Examples

### Example — How a vendor reads this datasheet

A package vendor receiving this datasheet (alongside `26020-02-PT-RFQ-23-001_FG_Skid_1.docx`) should:

1. Treat the Identification and Equipment List blocks as fixed.
2. Use the Service / Process Attributes block (flow, supply pressures, MAWP) as binding design inputs.
3. Treat the Construction Attributes block: each value marked `TBD` is open for vendor proposal subject to EPC review; cited values (K = 0.35, electric/SCR, skin-T override) are fixed.
4. Use the Interface Requirements Matrix to scope skid tie-in points and request EPC tag-level interface data before final P&ID issue.
5. Surface back to EPC any TBD that materially affects skid sizing, especially heater duty (OI-01) and the buyback ruling (OI-04).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-01 | Package physical location: 04-25 vs Deep Cut Facility | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Utility Integration Basis L452 (fuel gas building at/associated with 04-25) | `PACKAGE_REGISTER.csv` row PKG-084 description ("serve the low-pressure fuel gas system for the West Doe Deep Cut Facility"); package tracked under 3-25 workbook | Datasheet Identification; Package Identity; Interface routing | PROPOSAL: physical location 04-25; package procured and tracked under 3-25 workbook (consistent with both sources) | TBD |
| CF-02 | LP fuel gas scrubber tag: V-3210-1 (Deepcut DBM L1874) vs V-3210-2 (Comp_and_Liquids DBM L463) | `DBM-Deepcut/4-25_Deepcut_DBM.md` L1874 (V-3210-1; slop TK-9130-1) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 (V-3210-2; slop TK-9130-2) | Datasheet Equipment List; Construction; relief/drain routing | PROPOSAL: facility-specific suffix duplication for a single shared scrubber; adopt one canonical tag (e.g., V-3210) once owner confirms facility location | TBD |
| CF-03 | Emergency buyback fuel gas inclusion | W242510 indicates not required (cited at `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L465) | Process_DBM_fixed includes emergency buyback in 04-25 utility package (cited at L465); `DBM-Deepcut/4-25_Deepcut_DBM.md` L1876-1878 describes buyback regulator design | Heater sizing basis; regulator scope; package scope boundary | PROPOSAL: hold inclusion until human authority ruling per L465; carry buyback heater sizing basis (winter ambient) as conditional | TBD (NEEDS_HUMAN_RULING) |
| CF-04 | Relief / blowdown routing (HP vs LP flare allocation) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Flare L497 et seq. (HP/Cryo + LP dual flare stack shared 03-25/04-25; specific allocation carried as open interface items) | `DBM-Deepcut/4-25_Deepcut_DBM.md` Utility table row "Fuel gas" L1830 (facility-boundary isolation etc. remain TBD/TBC) | Scrubber/heater PSV routing; package interface declaration | PROPOSAL: defer to facility flare allocation ruling; carry datasheet entry as TBD | TBD |
| CF-05 | LP fuel gas design flow (>1.5 MMSCFD per source vs precise value TBC) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L463 (normal 1.382 MMSCFD; design >1.5 MMSCFD, TBC) | (no contradicting source in accessible set) | Heater duty; scrubber sizing | PROPOSAL: use 1.5 MMSCFD as a sizing floor and explicitly call out TBC | TBD |
