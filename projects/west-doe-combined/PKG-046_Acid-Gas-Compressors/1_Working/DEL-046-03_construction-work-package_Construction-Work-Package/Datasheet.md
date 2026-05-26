# Datasheet: DEL-046-03 — Construction Work Package (Acid Gas Compressors)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-046-03_construction-work-package` |
| Deliverable Name | Construction Work Package |
| Parent Package | `PKG-046` — Acid Gas Compressors |
| Facility | 04-25 West Doe Deepcut Gas Plant Expansion (Tourmaline) |
| Discipline | Mechanical (with multi-discipline construction interfaces: Civil, Structural, E&I, Controls) |
| Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Field Construction Authority | Tourmaline Oil Corporation (assigned in `4-25_Deepcut_DBM.md` SEC-01, Construction Responsibility) |
| Document Status | INITIALIZED (Pass 1/2) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package service | Acid gas injection compression for amine-regenerator acid gas | `4-25_Deepcut_DBM.md` SEC-05, Acid Gas Injection Compression Basis |
| Compressor configuration | Two 100% acid gas compressor packages plus one spare compressor; 3 x 50% alternative remains TBD | `4-25_Deepcut_DBM.md` SEC-05 Acid Gas Compressor Design Conditions |
| Compressor type | Ariel KBT/6, five-stage separable reciprocating compressor (conflicting KBK/6 reference remains TBD) | `4-25_Deepcut_DBM.md` SEC-05 Acid Gas Compressor Design Conditions |
| Driver | 969 kW (1,300 hp) induction motor, 8-pole, 900 rpm on VFD, minimum 3:1 speed turndown | `4-25_Deepcut_DBM.md` SEC-05 Acid Gas Compressor Design Conditions |
| Cooler arrangement | Common forced-draft motor-driven air cooler per stage; louver control, warm-air recirculation, freeze-prevention heat medium | `4-25_Deepcut_DBM.md` SEC-05 |
| Module count and split | TBD (to be defined by vendor packaging design and shipping logistics) | ASSUMPTION; not stated in accessible sources |
| Number of shipped-loose components | TBD | TBD; relevant to field installation scope (Step 4d) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service fluid | Wet acid gas from amine regenerator (H2S/CO2/H2O/light hydrocarbons; design 72.95 mol% H2S, 21.29 mol% CO2) | `4-25_Deepcut_DBM.md` SEC-05 Acid Gas Composition Basis |
| 1st-stage suction pressure | 7 psig normal; 3.8 psig low | `4-25_Deepcut_DBM.md` SEC-05 |
| 5th-stage discharge pressure | 1,200 psig normal; 1,500 psig design-discharge reference unresolved | `4-25_Deepcut_DBM.md` SEC-05 |
| Stage MAWPs / design temperatures | Range 197–1,551 psig MAWP / 300–350 deg F design temperature across 5 stages (see SEC-05 table) | `4-25_Deepcut_DBM.md` SEC-05 |
| Site location | LSD 03-25-80-15 W6M north of Dawson Creek, BC; elevation 673 m AMSL | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Site Location |
| Climatic / seismic / geotechnical basis | Per DBM SEC-02 (final geotechnical report governs foundation construction criteria; values are placeholders until accepted) | `3-25_Comp_and_Liquids_DBM.md` SEC-02 |
| Hazardous-area classification | TBD; to be set by electrical area classification deliverable; sour H2S service requires sour-service materials and venting controls | TBD |

## Construction

| Item | Basis |
|---|---|
| Modular shop assembly | Acid gas compressor packages assumed modularized and field-installed; module split count TBD | ASSUMPTION (consistent with sibling inlet compressor packaging in `3-25_Comp_and_Liquids_DBM.md` SEC-05) |
| Foundations and piling | Tourmaline field construction scope | `4-25_Deepcut_DBM.md` SEC-01 Construction Responsibility |
| Shipping and off-loading | Tourmaline field construction scope | `4-25_Deepcut_DBM.md` SEC-01 |
| Setting modules and equipment | Tourmaline field construction scope | `4-25_Deepcut_DBM.md` SEC-01 |
| Mechanical hookup and interconnecting piping | Tourmaline field construction scope | `4-25_Deepcut_DBM.md` SEC-01 |
| Installation of shipped-loose instruments / valves | Tourmaline field construction scope | `4-25_Deepcut_DBM.md` SEC-01 |
| Home-run cabling and electrical terminations | Tourmaline field construction scope | `4-25_Deepcut_DBM.md` SEC-01 |
| Interconnecting piping to ISBL/OSBL tie-ins | External interface responsibility — to be confirmed per tie-in | `4-25_Deepcut_DBM.md` SEC-01 |
| Acid gas injection pipeline interface | Assumed 3 in. NPS per Tourmaline; final sizing TBD; downstream of disposal well by others | `4-25_Deepcut_DBM.md` SEC-05 Acid Gas Disposal Well Interface |
| Joint planning for tie-ins | Required; tie-in timing to be established as project progresses | `4-25_Deepcut_DBM.md` SEC-01 |

## References

- `4-25_Deepcut_DBM.md` — sections SEC-01 (Construction Responsibility) and SEC-05 (Compression and Acid Gas Handling Basis) — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- `3-25_Comp_and_Liquids_DBM.md` — sections SEC-02 (Site-Specific Design Data) and SEC-05 (Inlet Compression context for compressor packaging convention) — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `26020-Package_Requirements.docx` — package heading 1 — location: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — **content TBD (binary not text-extracted in this scope)**
- Decomposition row: `DELIVERABLE_REGISTER.csv` GATE-07 snapshot
