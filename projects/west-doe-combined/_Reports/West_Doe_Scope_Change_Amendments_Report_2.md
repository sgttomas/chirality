# West Doe — Scope Change Amendments Report

**Report date:** 2026-05-14
**Facilities covered:** West Doe Compressor Station & Liquids Hub (3-25); West Doe Deepcut Expansion (4-25)
**Source roots:**
- `domain-test/domains/West_Doe_Comp_and_Liquids_DBM/_ScopeChange/`
- `domain-test/domains/West_Doe_Deepcut_DBM/_ScopeChange/`
**Amendment range:** SCA-001 through SCA-006 in each project (2026-04-14 through 2026-04-22)
**Current pointer:** Both `_LATEST.md` files point to SCA-006.

This report describes what changed in the design and scope of each facility under each Scope Change Amendment (SCA). Engineering substance is reported first; governance artifacts are mentioned only where they substantiate the engineering claim.

---

## Project A — West Doe Compressor Station & Liquids Hub (3-25)

Source: `West_Doe_Comp_and_Liquids_DBM/_ScopeChange/`

### SCA-001 — Value Engineering Closure (2026-04-14)
**Folder:** `SCA-001_2026-04-14_0000/`

Application of 8 Value Engineering proposals from the TOU/MLE VE workshop plus two Gate 1 scope clarifications.

Engineering changes:
- **Condensate dehydration removed from 3-25** (VE-20). The entire dehydration unit (KTY-04-10) and its seven child subjects (HBK-0141–0147) move from IN to OUT. Plot space is left for a possible future addition.
- **Condensate treating switched from regenerative to non-regenerative** (VE-19). SUB-04-09-01 process selection changed; SUB-04-09-08 *Caustic Regeneration* (HBK-0134) retired. VE-8 (regen utility consolidation) is superseded by this decision.
- **Incinerator confirmed IN, located physically at 3-25, services 4-25** (ISS-006-001 closed). SUB-04-09-09 (HBK-0135) promoted TBD→IN.
- **LACT confirmed OUT.** SUB-04-11-12 *Condensate LACT Units* (HBK-0159) retired (TBD→OUT). The existing SUB-12-04-05 *Transformers* content is updated to specify a 480 V dry-type transformer at the NRM LACT interface (VE-38).
- **Inlet compressor starting strategy** (VE-34): SUB-04-05-04 changed to *Starting VFD* on KM-2150 / KM-2250 per TOU direction.
- **Electrical revisions:** sync-bus capacitor banks removed on MCC-8200 (VE-37, SUB-12-04-04); 13.8 kV / 3 MW generator replaced by TOU typical LV standby gens on the LV MCC (VE-39, KTY-05-07 / SUB-12-04-03).
- **Shared utilities expanded between 3-25 and 4-25** (VE-7, extended at Gate 1): fuel gas (KTY-05-01), instrument air (KTY-05-02), and power (KTY-12-04) all marked SHARED.

Action ledger: 20 atomic actions in `Amendment_Actions.csv` (10 REMOVE, 10 MODIFY). The TBD→IN status promotion on SUB-04-09-09 *Incinerator* is recorded as MODIFY, not REMOVE — the Brief's "11 REMOVE / 9 MODIFY" tally counts it as a removal of the TBD state and is one over the CSV. Pre/post counts (319 total units): IN 308→301, TBD 7→5, OUT 4→13; active KTYs 88→87. Open issues ISS-006-001 and ISS-006-002 closed. Three new vocabulary terms added: *Non-regenerative Caustic Treating*, *Starting VFD*, *Shared Utility (3-25/4-25)*.

### SCA-002 — Cross-Facility Coordination After Deepcut SCA-001 (2026-04-14)
**Folder:** `SCA-002_2026-04-14_0000/`

Cascading scope changes flowing into 3-25 from the Deepcut (4-25) facility's SCA-001, which consolidated stabilization and SOC compression onto 4-25.

Engineering changes:
- **Inlet stabilizer (KTY-04-03)** retired entirely — 11 subjects (HBK-0060–0070) move IN→OUT. Stabilization function now lives at 4-25.
- **Stabilizer Overhead Compressor — SOC (KTY-04-04)** retired entirely — 14 subjects (HBK-0071–0084) move IN→OUT.
- **Heat Medium System (KTY-05-03)** retired entirely — 9 subjects (HBK-0187–0195) move IN→OUT. Justification: no reboiler load remains on 3-25 once the stabilizers are gone.
- **Vapour Recovery Unit (KTY-04-14)** rerouted: VRU now discharges into the 4-25 SOC suction rather than into local stabilizer feed (VE-4).
- **Inlet separators (KTY-04-02)** sized as **twin 9 ft × 40 ft horizontal 3-phase** units (VE-21), with plot for a third.
- **Inlet compressors (KTY-04-05)**: discharge pressure fixed at 800 psig with 4,880 HP (VE-28); revised from the source's 650–800 psig range.
- **Future condensate dehydration plot space cancelled** (VE-28). The plot-space reservation made for retired KTY-04-10 in SCA-001 is revoked; no future condensate dehydration unit is to be installed at 3-25.
- **Instrument air (KTY-05-02)** clarified: 3-25 receives I/A from 4-25 only; no local compressors retained (reconciles VE-7 with VE-29).
- **OBJ-004** statement rewritten to remove the stabilization/SOC objectives.

Action ledger: 9 atomic actions in `Amendment_Actions.csv` (3 REMOVE — all KTY-level, with child-subject closure cascading to 34 retired subjects; 6 MODIFY — five KTYs and one objective). Pre/post counts: IN 301→267 (−34, from the retired subjects of the three removed KTYs), OUT 13→47, active KTYs 87→84, active subjects 306→272 (319 total preserved).

### SCA-003 — Remediation Phase 5: Terminology & Authority Alignment (2026-04-19)
**Folder:** `SCA-003_2026-04-19_0900/`

Phase 5 of the West Doe Two-Root DBM Remediation campaign, governed by the frozen cleaned source authority package at `West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/` and the `plans/Authority_Allocation_Matrix.csv` (20 in-scope rows for 3-25).

Engineering rulings recorded as decomposition truth:
- **Flare boundary resolved.** Five handbook units HBK-0201–0205 move TBD→IN. 3-25 local flare infrastructure is in scope; the dual flare stack and incinerator are shared interfaces with 4-25.
- **Incinerator framing corrected** from "services 4-25 only" to "located at 3-25, shared with 4-25" (HBK-0135 note correction).
- **Excluded-scope note corrected** on HBK-0014.
- **LACT routing confirmed:** one NRM LACT routes to the NRM NEBC Connector; SUB-04-11-12 OUT status from SCA-001 preserved.
- **Inlet compressor horsepower** fixed at 5,200 hp per §5.1 (governs over conflicting upstream values).
- **NRM NEBC Connector** named as the canonical pipeline destination (resolves CONFLICT-01).
- **KTY-05-08 LPG** verified not applicable to 3-25.

Action ledger: 17 direct write actions, including category-count reconciliation (CAT-004: 14→11 KTYs, 141→107 subjects; CAT-005: 8→7 KTYs, 35→27 subjects), four retired-KTY objective-map cleanups, and a vocabulary expansion of 22 entries (21 new + 1 update) bringing the map to 38 terms. Counts post-amendment: IN 272, TBD 0, OUT 47 (5 TBD→IN closing all remaining open issues). Phase 6 downstream regeneration of 23 KTYs and a domain-hypergraph snapshot (972 nodes / 1,046 edges) follow as derivative work.

### SCA-004 — Add Mechanical Package Structure Knowledge Type (2026-04-19)
**Folder:** `SCA-004_2026-04-19_1400/`

Structural addition introducing a new Knowledge Type under CAT-007 Plant Design Requirements to capture the mechanical package roster and per-package line-item structure for 3-25.

Engineering content added:
- **KTY-07-07 _Mechanical-Package-Structure_** — new Knowledge Type.
- **SUB-07-07-01 _Package-Summary_** — the package roster.
- **SUB-07-07-02 _Package-Line-Items_** — line-item detail.
- **HBK-0320 / HBK-0321** — two derived-singleton handbook units (not a row-level explosion of every package).
- Mapped to **OBJ-006** Plant Design Objectives; CAT-007 counts updated 6→7 KTYs / 15→17 subjects / 15→17 IN units.

Source authority: `_Sources/Packages_3-25_1.csv` (24 data rows) and `_Sources/Line-Items_3-25_1.csv` (49 non-empty rows). Action ledger: 7 atomic actions (5 ADD, 2 MODIFY). Post-amendment totals: 274 IN, 0 TBD, 47 OUT; HBK count 319→321; active KTYs 84→85.

Source observations recorded but not reconciled per the source-interpretation rule (`ALLOW_RENUMBERING=false`): the Packages CSV has 24 rows where the plan stated 23; the Line-Items CSV has 49 non-empty rows where the plan stated 60; the package "Filters/Strainers" appears under "Tank Farm Pump Building 1" in one CSV; "Vapour Recovery Unit 1" appears only in Line-Items.

### SCA-005 — KTY Content Disposition Formalization (2026-04-21)
**Folder:** `SCA-005_2026-04-21_1627/`

Pre-publication content remediation: stop retired KTY content from leaking into publication factual-use surfaces, and produce the first formal `KTY_Remediation_Manifest.csv` (28 rows) covering the cumulative SCA-001 through SCA-004 amendments.

Engineering content actions:
- **Four retired KTYs archived and tombstoned** with placeholder stubs in place of any active-looking content files. 45 files in total move to `.Archive/SCA-005_RETIRE/`:
  - KTY-04-10 *Condensate Dehydration Unit* (8 files) — retired in SCA-001.
  - KTY-04-03 *Inlet Stabilizer* (12 files) — retired in SCA-002.
  - KTY-04-04 *Stabilizer Overhead Compressor – SOC* (15 files) — retired in SCA-002.
  - KTY-05-03 *Heat Medium System* (10 files) — retired in SCA-002.
- **KTY-04-09 content regenerated** to remove residual references to the now-retired SUB-04-09-08 *Caustic Regeneration*: KA-08 tombstoned; the Scoping.md artifact plan corrected; cross-references in KA-04, KA-12, and KA-14 cleaned.
- **22 active KTYs verified** for content disposition completeness (all verified clean).
- **KTY-07-07** acknowledged as already correctly initialized in SCA-004 (NO_ACTION).

No structural count changes: 272 IN, 0 TBD, 47 OUT preserved. The amendment's main deliverable is the manifest itself, which becomes the governance input for the DBM publication pipeline's input-allowlist scanner.

### SCA-006 — Instrument Air Supersession Formalization (2026-04-22)
**Folder:** `SCA-006_2026-04-22_0900/`

Narrow amendment confined to `KTY-05-02_Instrument-Air`. Records the 2026-04-22 human ruling on the consolidated 4-25 Instrument Air package and the cross-facility demand basis.

Engineering content recorded:
- **Compressor configuration finalized: 2 × 100% lead-lag at the 4-25 consolidated I/A package with provision for a future 3rd 100% unit.** The earlier W242510 §5.2.2.8 wording "3 × 50% compressors" is formally superseded as a source anomaly. The equipment table at W242510 §1 line 867 (`Instrument Air Unit c/w 2× 100% Compressors and Air Dryer Unit`) is taken as governing on configuration.
- **3-25 demand: 393 SCFM (TBC)** per W242510 §5.2.1 Table 5-9, bound to SUB-05-02-01.
- **4-25 demand: 720 SCFM (TBC)** per W235633 §5.2.1 Table 5-14, bound to SUB-05-02-01.
- **Combined arithmetic demand: 1,113 SCFM (TBC)** delivered by the consolidated 4-25 package.
- Final combined sizing, distribution losses, contingency, and the 3-25 booster compressor requirement are preserved as detailed-engineering confirmations.
- Authority chain bound to Deepcut SCA-001 `patches/KTY-05-02_patch.md` VE-29 and the TOU C-60 Gundy drawing.

Action ledger: 3 MODIFY actions (KTY-05-02, SUB-05-02-01, SUB-05-02-02). No new category/KTY/subject/objective. Supersession map expands from 20 to 24 data rows (4 new bindings). Counts preserved: 272 IN, 0 TBD, 47 OUT.

---

## Project B — West Doe Deepcut Expansion (4-25)

Source: `West_Doe_Deepcut_DBM/_ScopeChange/`

### SCA-001 — VE Workshop Closure: Remove Depropanizer, Activate NGL (2026-04-14)
**Folder:** `SCA-001_2026-04-14_1430/`

Application of 16 VE proposals from the TOU/MLE workshop. The dominant engineering decision is the elimination of the LPG product line; treating and dehydration are re-pointed at NGL as current scope.

Engineering changes:
- **Depropanizer line eliminated** (VE-14). KTY-04-18 *Depropanizer* retired in full, plus 9 child subjects + SUB-03-02-02 + SUB-04-19-06. 281 ledger rows move to RETIRED (HBK-3921–4132, HBK-1351–1380, HBK-4237–4275).
- **NGL scope activated.** KTY-04-16 and KTY-04-17 are renamed from LPG-FUTURE to NGL current scope (IDs preserved). 295 ledger rows in those KTYs are rewritten LPG→NGL. SUB-11-04-03 becomes *NGL Storage Area*.
- **Mercaptan treating** confirmed non-regenerative under the NGL framing (VE-8).
- **TEG contactor** (VE-3): 1 × 100% configuration.
- **Stabilizer consolidation** (VE-4): 3-25 stabilizers consolidated onto 4-25 (the mirror side of C&L SCA-002).
- **Inlet separator sizing** (VE-21): 2 × 9 ft × 40 ft, plot for a third.
- **New inlet-separator HEX** (VE-23): SUB-04-02-15 created between the inlet sep and MPFF preheat.
- **Heat medium single-loop** (VE-26): 220 °C supply; regen-gas heater split out.
- **Mole sieve** (VE-27): 3A type, 8 ft × 20 ft vertical regen tower, future mercury-removal plot space.
- **Instrument air consolidation** (VE-29): 2 × 100% on 4-25 serving both 3-25 and 4-25 (subsumes VE-7).
- **Inlet compressor starting strategy** (VE-34): Starting VFD on KM-2150 / KM-2250 (mirrors C&L SCA-001).
- **Electrical revisions:** sync-bus cap banks removed at MCC-8200 (VE-37); 480 V dry-type LACT transformer (VE-38); LV-MCC standby generators with transfer switch (VE-39).
- VE-6 (regen compressors) rejected — stay with 2 × 100% regen compressors. VE-28 (3-25 dehy) is 3-25-only and not applied here.

Action ledger: 34 atomic actions in `Amendment_Actions.csv` (3 REMOVE, 3 ADD, 28 MODIFY). The Brief.md tally of "3 REMOVE / 2 ADD / 29 MODIFY" treats the Decision-Log creation (DEC-010) as a MODIFY; the CSV records it as an ADD, giving 3 ADDs total (SUB-04-02-15, vocab term *NGL*, DEC-010). Pre/post counts: IN 5,243→4,962, RETIRED 0→281; active KTYs 98→97; active subjects 443→432; vocabulary +1 (*NGL*). Open issues 593→564. Many design-parameter rewrites are flagged as deferred to TASK agents — see RUN_SUMMARY §"Pending actions". The folder also contains ad-hoc Python helper scripts (`apply_amendment.py`, `apply_patches.py`, `fix_md_ledger.py`, `refresh_derivatives.py`) and a duplicate of the VE tracker CSV co-located with the governance artifacts.

### SCA-002 — 3-25 Interface Coordination Acknowledgment (2026-04-14)
**Folder:** `SCA-002_2026-04-14_1510/`

Cross-facility acknowledgment of changes made by the 3-25 SCA-001. Equipment located on 3-25 but serving 4-25 needs its content basis rewritten on the 4-25 side; shared fuel gas and shared power coordination items are added as open coordination notes.

Engineering changes:
- **Incinerator feed redefined** (SUB-04-16-09 / HBK-3782): "caustic regeneration overheads" replaced with "spent caustic tank vapours + disulphide-oil off-gas" (consequence of the 3-25 switch to non-regenerative treating).
- **Incinerator location annotated** (HBK-3783): "physically located at 3-25 facility" with interface reference. The asset is shared, not 4-25 local.
- **Incinerator flow basis** (HBK-3786): the 0.6 MMSCFD caustic-regen basis is superseded; flow becomes TBD pending detailed engineering.
- **Scope tables (HBK-0803, HBK-0804)** updated: LPG→NGL, "Future" dropped, 3-25 physical location added.
- **Three new open coordination items added** (HBK-5974–5976): incinerator operational responsibility, shared fuel gas, shared power.
- LACT excluded (NRM scope) — explicitly not part of this amendment.
- Shared Instrument Air already covered by SCA-001 VE-29 — no further action.

Action ledger: 8 atomic actions (5 MODIFY, 3 ADD). Post-state: 5,961 ledger rows (+3), 4,965 IN / 701 OUT / 14 TBD / 281 RETIRED; DeferredConfirmation open items 138→141.

### SCA-003 — Remediation Phase 3: Two-Root DBM Authority Alignment (2026-04-19)
**Folder:** `SCA-003_2026-04-19_0900/`

Alignment of the Deepcut decomposition to the same frozen source-authority package that governs the 3-25 root, scoped to 20 of 26 rows in the Authority Allocation Matrix (6 DEEPCUT_ONLY, 11 SHARED_INTERFACE owning, 3 SHARED_INTERFACE secondary).

Engineering substance corrected:
- **NGL mercaptan treating returned to non-regenerative basis** under KTY-04-16 — the regenerative wording introduced earlier was incorrect against the frozen source. HBK-3626 / 3627 / 3628 / 3629 corrected. Human arbitration ruled in favour of source-frozen non-regenerative caustic.
- **Scope-table content** under KTY-01-04 normalized: LPG→NGL, future→current, capacity updated.
- **Waste-stream framing** under KTY-03-03: disulphide oil (DSO) and spent caustic streams reclassified future→current.
- **KTY-04-06 SOC gas sources** updated: "Future / LPG" replaced with current-scope NGL.
- **OBJ-002 erroneous `[RETIRED]` tag on KTY-04-20** removed.
- **Cross-cutting reference cleanup** across KTY-01-01, KTY-01-03, KTY-03-03, KTY-04-14, KTY-04-16 (LPG / future tokens normalized in non-retired KTYs).

Action ledger: 24 actions (21 MODIFY + 3 VERIFY_ONLY); 32 ledger-row corrections across 34 unique KTYs. Vocabulary map expanded from 13 to 48 terms (35 new, all `SHARED_INTERFACE` SharedTermSet rows). Revision v4.3-SCA-003. The Phase 4 downstream rerun is recorded as: TASK + domain-documents for 34 KTYs (all SUCCESS), DOMAIN_HYPERGRAPH snapshot 1,002 nodes / 1,427 edges (36 non-structural QA blockers from discovery-script ID qualification, accepted for handoff), AUDIT_DECOMP 0 blockers / 100% coverage, terminology QA with no blocking contradictions.

### SCA-004 — Add Mechanical Package Structure Knowledge Type (2026-04-19)
**Folder:** `SCA-004_2026-04-19_1525/`

Parallel structural addition to the 3-25 SCA-004. Same Knowledge Type identity, subjects, schema, and descriptive wording, but with 4-25 source authority and a different objective mapping.

Engineering content added:
- **KTY-07-07 _Mechanical-Package-Structure_** under CAT-007 Plant Design Requirements.
- **SUB-07-07-01 _Package-Summary_** — the package roster.
- **SUB-07-07-02 _Package-Line-Items_** — line-item detail.
- **HBK-5978 / HBK-5979** — two derived-singleton handbook units.
- Mapped to **OBJ-004** (vs OBJ-006 on the 3-25 side); CAT-007 counts updated KTYs 6→7 / subjects 15→17 / IN units 178→180.

Source authority: `_Sources/Packages_4-25_1.csv` (34 packages) and `_Sources/Line-Items_4-25_1.csv` (61 data rows). Action ledger: 7 atomic actions (5 ADD, 2 MODIFY). Post-amendment counts: 98 KTYs (+1), 434 subjects (+2), 5,692 IN units (+2); OBJ-004 mapped-unit count 641→643. AUDIT_DECOMP COV_SCA004_POST snapshot issued two cosmetic warnings (stale inline ledger summary counts and telemetry JSON row counts), both corrected post-snapshot with human-accepted no-rerun closure. DOMAIN_HYPERGRAPH HG_SCA004 snapshot: 0 blockers, 9/9 PASS. Pre-existing source-table discrepancy (VRU2 in line-items only) recorded as non-blocking.

### SCA-005 — KTY Corpus Remediation Assessment & Publication Prep (2026-04-21)
**Folder:** `SCA-005_2026-04-21_1400/`

A three-lane remediation campaign closing engineering conflicts, verification failures, and terminology blockers accumulated across SCA-001 through SCA-004 in advance of publication.

Engineering content actions:
- **Inlet-separator HEX subject registered.** SUB-04-02-15 (deferred from SCA-001 Seq 18) is added to the registers; 6 ledger rows already present are normalized.
- **D-007 KTY-04-16 non-regenerative refactor (full).** Caustic treating definitively rewritten as non-regenerative: SUB-04-16-08 *Caustic Regeneration* removed (16 ledger rows retired); 5 SUB-04-16-07 rows retired; 6 ledger rows modified across SUB-04-16-02 / -05 / -09; the Knowledge Type Register entry and the main decomposition document corrected to match.
- **Stale Depropanizer-derivative entries cleaned.** 9 SUB-04-18-* Node Summary rows move IN→RETIRED.
- **TOU C-60 unsupported qualifier removed** (terminology cleanup).
- **DGAP-01 closed** with HBK-5980 added under SUB-04-13-04.
- **Active warranted LPG tokens normalized to NGL** in non-retired KTYs (the converse of the SCA-001 wholesale rename).
- **OBJ-002 and CAT-004 counts** corrected to match the companion CSV authority.

Manifest dispatch: 22 rows covering 22 KTYs.
- 1 ARCHIVE_AND_STUB — KTY-04-18 (Depropanizer).
- 15 REGENERATE_CONTENT — including 8 KTYs escalated from VERIFY after failing verification on D-002 (VE-4a stabilizer), D-007 (non-regen), D-021 (VE-27 mole sieve), D-023 (VFD), and D-004 (Depropanizer cross-refs). Regenerated KTYs include KTY-11-04, KTY-12-05, KTY-04-02, KTY-04-16, KTY-04-06, KTY-04-07, KTY-04-12, KTY-04-13, KTY-04-14, KTY-04-19, KTY-03-02.
- 5 VERIFY_ONLY — KTY-04-04, KTY-04-17, KTY-05-02, KTY-05-03, KTY-05-07 (downgrades approved by human against SCA-003 regeneration evidence).
- 1 NO_ACTION — KTY-07-07 (SCA-004 output already current).
- KRM-022 added during Lane 3 for TERM-BLOCK-001 (KTY-01-01 regenerative-caustic statement vs D-007 non-regen governance).

Action ledger: 35 actions (2 ADD, 2 REMOVE, 31 MODIFY). Net ledger motion: −20 IN rows. Manifest validator and Publication Input Allowlist scan PASS. Non-blocking deferrals recorded: CONF-02 (TEG sparing 1×100% vs 2×50%, awaiting human ruling) and CONF-03 (NGL regen-gas source under non-regen, DeferredConfirmation with TBD flow values).

### SCA-006 — KTY-05-02 Instrument Air Combined Demand (2026-04-22)
**Folder:** `SCA-006_2026-04-22_0100/`

Narrow amendment matching the 3-25 SCA-006 on the same day. Confines its scope to KTY-05-02 *Instrument Air* and SUB-05-02-01 *Instrument-Air-Consumption*.

Engineering content recorded:
- **Consolidated 4-25 Instrument Air package serves both facilities** (cross-facility demand admission, D-028).
- **4-25 facility demand: 720 SCFM (TBC)** per W235633 §5.2.1 Table 5-14.
- **3-25 facility demand: 393 SCFM (TBC)** per W242510 §5.2.1 Table 5-9.
- **Combined arithmetic demand: 1,113 SCFM (TBC)** for the consolidated 4-25 package.
- **Compressor configuration ruling preserved:** 2 × 100% lead-lag at 4-25 with provision for a future 3rd 100% unit. The SCA does not reopen this ruling (D-030).
- **Detailed-engineering confirmations preserved** (D-029): final combined sizing, contingency treatment, cross-facility distribution losses, and the 3-25 booster compressor requirement remain Detailed Engineering items.

Action ledger: 3 MODIFY actions in `Amendment_Actions.csv` — one against KTY-05-02 *Instrument-Air* content (the rewrite that appends six new ledger rows, HBK-5981 through HBK-5986, under SUB-05-02-01), one OTHER entry recording the supersession binding, and one OTHER entry updating the `_LATEST.md` scope-change pointer. No category / KTY / subject / objective / identity changes. Domain Integrity Report clean (0 critical / 0 major / 0 minor findings); KTY remediation manifest validation PASS (KRM-001 VERIFY_ONLY). The publication package was accepted as `RUN-20260422-030000` with major notes; AUDIT_DECOMP and DOMAIN_HYPERGRAPH reruns are recommended before later-phase consumption.

---

## Appendix A — Non-Timestamped `SCA-001/` Folder

Each project's `_ScopeChange/` tree contains a non-timestamped `SCA-001/` folder *in addition to* the timestamped SCA-001 snapshot. These are **source-authority folders, not amendment snapshots:**

- `West_Doe_Comp_and_Liquids_DBM/_ScopeChange/SCA-001/Value_Engineering_Tracker.csv` — the 8 VE proposals (workshop with TOU direction notes) that drove the 3-25 SCA-001 amendment.
- `West_Doe_Deepcut_DBM/_ScopeChange/SCA-001/Value_Engineering_Tracker.csv` — the 16 VE proposals (TOU / MLE workshop) that drove the 4-25 SCA-001 amendment.

They are referenced as the originating governance input by the timestamped SCA-001 Brief.md files. They are immutable source records; do not conflate with the executed amendment snapshots. The 4-25 timestamped SCA-001 folder also carries a duplicate copy of this CSV next to its governance artifacts.

---

## Appendix B — Evidence Index per Amendment

For each amendment the primary evidence files used in this report are:

| Project | Amendment | Brief | RUN_SUMMARY | Decision Log | Impact Assessment | Other |
|---|---|---|---|---|---|---|
| 3-25 | SCA-001 | ✓ | ✓ | ✓ | ✓ | Amendment_Actions.csv; Supersession_Delta.csv |
| 3-25 | SCA-002 | — | ✓ | — | — | Amendment_Actions.csv; Supersession_Delta.csv (no Brief / no Impact_Assessment) |
| 3-25 | SCA-003 | ✓ | ✓ | ✓ | ✓ | Propagation_Plan.md |
| 3-25 | SCA-004 | ✓ | ✓ | ✓ | ✓ | Handoff_State.md; Supersession_Map.csv |
| 3-25 | SCA-005 | ✓ | ✓ | ✓ | ✓ | KTY_Remediation_Manifest.csv; Evidence/; Handoff_State.md |
| 3-25 | SCA-006 | ✓ | ✓ | ✓ | ✓ | Validation_Report.md; Validation_Findings.csv; Supersession_Map.csv; Handoff_State.md |
| 4-25 | SCA-001 | ✓ | ✓ | ✓ | ✓ | apply_amendment.py / apply_patches.py / fix_md_ledger.py / refresh_derivatives.py; patches/; Value_Engineering_Tracker.csv (duplicated copy) |
| 4-25 | SCA-002 | — | ✓ | ✓ | — | apply_amendment.py; Supersession_Delta.csv |
| 4-25 | SCA-003 | ✓ | ✓ | ✓ | ✓ | apply_ledger_corrections.py; ledger_correction_log.json; Propagation_Plan.md |
| 4-25 | SCA-004 | ✓ | ✓ | ✓ | ✓ | Handoff_State.md; Supersession_Map.csv; Reconciliation_Ledger.csv |
| 4-25 | SCA-005 | ✓ | ✓ | ✓ | ✓ | KTY_Remediation_Manifest.csv; Manifest_Validation_Findings.csv; Publication_Input_Allowlist.csv / Exclusions.csv / Report.md; Evidence/; Handoff_State.md |
| 4-25 | SCA-006 | ✓ | ✓ | ✓ | ✓ | Domain_Integrity_Report.md / Findings.csv; KTY_Remediation_Manifest.csv / Manifest_Validation_Findings.csv; Supersession_Map.csv / Findings.csv; Evidence/; Handoff_State.md |

Two amendments (the SCA-002 in each project) do not carry a `Brief.md` or `Impact_Assessment.md`; their governance is captured in `RUN_SUMMARY.md` + `Decision_Log.md` (4-25) or `RUN_SUMMARY.md` alone (3-25).
