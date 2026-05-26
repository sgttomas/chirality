# Procedure — DEL-085-04 Vendor Engineered Equipment Package (Flare Stack, High Pressure)

## Purpose

Describe the procedural path by which the Package Vendor produces the Vendor Engineered Equipment Package for PKG-085 (Flare Stack, High Pressure), from receipt of the EPC anchor inputs through issuance of the vendor engineered physical equipment package and supporting vendor design basis and datasheet set (source: `_CONTEXT.md` scope statement; DELIVERABLE_REGISTER.csv).

This procedure covers steps to *produce* the deliverable artifact; operational/use procedures for the flare stack itself are governed by `DEL-085-03` (Construction Work Package), `DEL-085-05` (Vendor Document Turnover Package), and `DEL-085-06` (EPC Vendor Package Review and Acceptance).

## Prerequisites

- Accepted upstream PROJECT_DECOMP snapshot: GATE-07_Final_Published_2026-05-24 (source: `_REFERENCES.md`).
- EPC SOW deliverable (`DEL-085-01`) issued and accessible to vendor (declared upstream of vendor package: TBD — no upstream dependencies declared in `_DEPENDENCIES.md`).
- EPC Package Datasheet deliverable (`DEL-085-02`) issued and accessible to vendor (same TBD).
- Locally accessible source basis: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Site environmental and geotechnical data (final geotechnical report) for foundation/anchorage design (source: 3-25 DBM Foundations).
- Final flare studies status known (source: 3-25 DBM, "blowdown and relief basis require final flare studies"). Where final flare studies are not yet issued, the procedure runs against the current source basis and flags reissue triggers.

## Steps

1. **Receive and confirm EPC anchor inputs.** Vendor reads `DEL-085-01` (EPC SOW) and `DEL-085-02` (EPC Package Datasheet). Vendor logs deviations between EPC inputs and the project DBM source basis and raises clarifications to the EPC Integrator before drafting begins.
2. **Establish vendor design basis.** Vendor drafts the vendor package design basis using the EPC anchor inputs as primary and the project DBM (3-25 and 4-25) as background, including:
   - HP flare service definition (source: 3-25 DBM Flare and Blowdown);
   - HP relief header sizing of 508 mm (20 in) at the package interface (source: 3-25 DBM);
   - HP/Cryo sonic flare stack envelope (660 mm OD x 60,957 mm tall) and LP stack envelope (OD TBD) (source: 3-25 DBM);
   - HP KO drum arrangement (V-4100-2, V-4150-2; 1 x 100% transfer pumps each: P-4100-2, P-4150-2) (source: 3-25 DBM);
   - Thermal-radiation and spacing limits (source: 4-25 Deepcut DBM Flare and Incinerator Spacing);
   - Site environmental loads and foundation basis (source: 3-25 DBM Foundations).
3. **Identify open interface items.** Vendor records the shared 03-25 / 04-25 service split as an open interface item and proposes ownership in the interface register; does not unilaterally resolve (source: 3-25 DBM Utilities narrative).
4. **Develop vendor datasheet set.** Vendor issues vendor datasheets for the flare stack, KO drums (within vendor scope), transfer pumps (within vendor scope), pilot/ignition/purge systems, instrumentation, controls, and structural/foundation interface points. Each datasheet cites the source slice supporting its values; TBD entries are kept rather than guessed.
5. **Engineering and design.** Vendor performs:
   - Stack thermal-radiation modelling against the kW/m² limits;
   - Flare load reconciliation (HP relief/blowdown loads from inlet separators, MPFF, stabilizer flash/feed and tower, SOC, pig receiver vent, contactor blowdown — source: 4-25 Deepcut DBM, 3-25 DBM);
   - Mechanical design (stack, KO drums and internals within vendor scope, structural connections);
   - Controls and detection interfaces (LEL, H2S, methyl mercaptan, fire detection coordination — source: 3-25 DBM Detection);
   - Civil/structural interface to foundations and anchorage (source: 3-25 DBM Foundations);
   - Spacing layout check against the cited minima (source: 4-25 Deepcut DBM).
6. **Fabrication and supply.** Vendor fabricates and supplies the engineered physical equipment package, including bulks and ancillaries within vendor battery limits as set by `DEL-085-01`/`DEL-085-02`. Vendor maintains records sufficient to support `DEL-085-05` (Vendor Document Turnover Package).
7. **Integration review participation.** Vendor participates in EPC Integrator integration review (source: `_CONTEXT.md` ResponsibleParty statement) and supports `DEL-085-06` review and acceptance.
8. **Reissue triggers.** Vendor reissues affected design basis, datasheet, or package items when:
   - Final flare studies establish revised relief/blowdown loads (source: 3-25 DBM);
   - EPC Integrator issues a SOW or Package Datasheet revision;
   - Shared 03-25 / 04-25 allocation is resolved (source: 3-25 DBM Utilities);
   - External regulatory references (OGPFR, OGAOM, API 2510) are reconciled with locally accessible text.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| EPC anchor compliance | Cross-walk of vendor design basis against `DEL-085-01` and `DEL-085-02` | All EPC requirements addressed or marked TBD with referenced ruling needed |
| Flare service coverage | Compare vendor inlet manifold and KO routing against tributary services list in 4-25 Deepcut DBM and 3-25 DBM | All listed HP flare services accommodated or recorded as out-of-scope with rationale |
| Thermal radiation flux | Vendor flux model results vs. 9 kW/m² (inside) and 5 kW/m² (outside) | Model demonstrates compliance at the package boundary |
| Spacing | Layout check against 4-25 Deepcut DBM spacing table | Every minimum distance met or variance documented |
| Foundation/anchorage | Civil/structural calculation against geotechnical report and 3-25 DBM Foundations basis | Calculations sealed by responsible discipline |
| Detection coverage | Detection coordination memo or interface drawing | Coverage accepted by EPC Integrator |
| Open interface items | Interface log entries for shared 03-25/04-25 service split | All open items captured with owner and target ruling date |

## Records

- Vendor design basis document (anticipated artifact: vendor package design basis and datasheet set).
- Vendor datasheet set for stack, KO drums, transfer pumps, pilot/ignition/purge, instrumentation, controls (anticipated artifact).
- Vendor engineering calculations: thermal radiation, flare loads, mechanical, structural/foundation interface, spacing layout check.
- Fabrication records: material test reports, weld records, NDE records, inspection releases (per vendor QC plan; specifics TBD).
- Vendor engineered physical equipment package delivery record (anticipated artifact).
- Interface and integration review participation records (feeds `DEL-085-06`).
- Reissue/change-control records when reissue triggers fire.
