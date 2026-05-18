# Plan: Author West Doe Deep Cut (04-25) DBM from Governed KA Content

## Objective

Author a new West Doe Deep Cut Gas Plant (04-25) Design Basis Memorandum from current governed KTY/KA content in FULL_ENGINEERING_DBM mode. Reuse structural/deterministic publication artifacts after alignment checks. Do not reuse any prior DBM prose, section outputs, review outputs, or package text. Write fresh section bodies, assemble a publication package with closeout artifacts, and generate a final .docx.

## Admitted Inputs

All paths relative to `domain-test/domains/West_Doe_Deepcut_DBM/`.

### Structural / Planning Inputs

| Artifact | Role |
|----------|------|
| `_Publication/DBM/_Planning/Publication_Schema.md` | 16-section structure definition |
| `_Publication/DBM/_Planning/Publication_Rules.md` | Style, completeness standard, naming, supersession policy |
| `_Publication/DBM/_Planning/Section_Map.csv` | KA-to-section mapping (selector) |
| `_Decomposition/DeepCut_DOMAIN_DECOMP_FINAL_v4.md` | Domain decomposition authority |
| `_Decomposition/DeepCut_*_v4.csv` | Decomposition companion registers (Category, KTY, Subject, Objective, Vocabulary, Scope Boundary, Open Issues, Domain Ledger, Node Summary, Standalone Subject Coverage) |

### Publication-Admission Inputs

| Artifact | Role |
|----------|------|
| `_ScopeChange/_LATEST.md` | Active scope-change pointer |
| `_ScopeChange/SCA-006_2026-04-22_0100/Supersession_Map.csv` | Active supersession bindings (35 rows) |
| `_ScopeChange/SCA-006_2026-04-22_0100/Handoff_State.md` | Closure status, remaining blockers |
| `_ScopeChange/SCA-006_2026-04-22_0100/Decision_Log.md` | Admission decisions |
| `_Reconciliation/DecompCoverage/_LATEST.md` | Audit evidence pointer |
| Resolved audit snapshot and QA report (path from pointer) | Frozen audit evidence |

### Reference / Provenance Inputs

| Artifact | Role |
|----------|------|
| `_Sources/W235633-PRC-DBM-000001-001_(4-25_Doe)_DBM.md` | Source DBM for conflict checking |
| `_Sources/TOC_Deepcut.md` | Source table of contents |
| `_Sources/west_doe_process_design_basis_clean/` | Shared clean source package |

### KTY-Local Authoring Corpus (selected by Section_Map.csv)

| Artifact Type | Role |
|---------------|------|
| `KA-*.md` files at exact paths mapped by Section_Map.csv | Section-writing inputs |
| `Scoping.md` in each section-relevant KTY | Scope and decomposition context |
| `_STATUS.md` in each section-relevant KTY | Lifecycle state and readiness |

Section_Map.csv is the selector. The KA files, Scoping.md, and _STATUS.md it points to are the actual authoring inputs.

### Mapped-Row Role Handling

| Section_Map.csv Role | Treatment |
|----------------------|-----------|
| PRIMARY | Body-authoring authority — directly supports engineering prose |
| SUPPORTING | Constraints, qualifiers, interfaces, exclusions, corroboration — governs but does not become main narrative source |
| CONTEXT_ONLY | Framing, limitations, caveats, readiness — usually not body prose unless clearly needed |

### Not Admitted

- Prior `Rewritten_DBM.md` from any package run (including accepted RUN-20260422-030000/ and latest RUN-20260423-REVIEWER-B-ENGINEERING-DBM/)
- Prior section bodies (`sections/SEC-##/SEC-##.md`)
- Prior package QA, readiness, open-items, or concordance outputs
- Prior review artifacts
- Prior dispatch outputs

## Alignment Checks (pass / patch / regenerate)

| Check | Criteria | Pass | Patch | Regenerate |
|-------|----------|------|-------|------------|
| Active SCA pointer | `_LATEST.md` points to SCA-006 | Confirmed | N/A | Fail run |
| Section_Map.csv paths | All PRIMARY artifact paths resolve | All resolve | Exclude missing rows, log | Fail if >5% missing |
| Retired KTY exclusion | No RETIRED/TOMBSTONED rows admitted as active body inputs (KTY-04-18 Depropanizer is retired) | None present as PRIMARY body authority | Exclude retired rows, log | N/A |
| Schema alignment | Publication_Schema.md defines 16-section FULL_ENGINEERING_DBM | Matches | N/A | Structural mismatch → fail |
| Rules basis currency | Publication_Rules.md current-state-basis references SCA-006 | Current | Patch stale refs → SCA-006 | N/A |
| Handoff closure | Handoff_State.md has no blocking items for publication | No blockers | N/A | Blockers → fail |
| Audit evidence | Pointer resolves to snapshot with QA report | Snapshot + QA exist | N/A | Missing → document as limitation |

## Authoring

16 section-writing agents (opus), one per section. Each agent:
- Reads exact mapped artifact paths from Section_Map.csv for its section
- Applies mapping role semantics (PRIMARY / SUPPORTING / CONTEXT_ONLY)
- Reads Scoping.md and _STATUS.md in each relevant KTY for lifecycle context
- Reads relevant supersession bindings from Supersession_Map.csv
- Writes one section body per Publication_Rules.md voice and form
- Writes output to `_Publication/DBM/sections/SEC-##/SEC-##.md`

Engineering facts come from KA files read at authoring time, not from this plan.

If dispatch limits force batching, split into two waves (SEC-01 through SEC-08, then SEC-09 through SEC-16). Each section remains independently re-runnable with its own agent brief.

### Section Summary

| SectionID | Title | Type | Key Content Areas |
|-----------|-------|------|-------------------|
| SEC-01 | Project and Document Basis | OVERVIEW | Facility identity, scope boundary, objectives, construction, terminology |
| SEC-02 | Site, Layout, and Spacing Basis | DISCIPLINE_BASIS | Site parameters, plot plan, spacing tables |
| SEC-03 | Feed, Product, Waste, and Metering Basis | DATA_REFERENCE | Inlet feed, products, wastes, storage, metering data interface |
| SEC-04 | Inlet, Separation, Stabilization, and Stabilizer Overheads Basis | PROCESS_BASIS | Inlet pipeline, separation, MPFF, stabilizer, SOC |
| SEC-05 | Compression and Acid Gas Handling Basis | PROCESS_BASIS | Inlet/sales compression, booster, acid-gas injection/disposal |
| SEC-06 | Treating, Dehydration, and Cryogenic Recovery Basis | PROCESS_BASIS | Amine treating, TEG dehy, mol-sieve dehy, UltraTEF cryogenic |
| SEC-07 | Sales Gas, NGL Treating, Product Handling, and Vapor Recovery Basis | PROCESS_BASIS | Sales-gas delivery, NGL treating/dehy, product storage, VRU, retired depropanizer |
| SEC-08 | Utilities and Support Systems Basis | DISCIPLINE_BASIS | Fuel gas, instrument air, heat medium, drains, flare, lube oil, emergency power, analyzers |
| SEC-09 | Energy, Prime Movers, and Emissions Basis | DATA_REFERENCE | Prime mover inventory, emissions summary |
| SEC-10 | Plant Design Philosophy and Mechanical Requirements | PHILOSOPHY | Sparing, margins, isolation, vessel/exchanger rules, package structure |
| SEC-11 | Civil, Buildings, and Miscellaneous Facilities Basis | DISCIPLINE_BASIS | Miscellaneous facilities, civil general, geotechnical, drainage, roads, foundations, buildings |
| SEC-12 | Electrical Basis | DISCIPLINE_BASIS | Codes, area classification, power system, buildings, grounding, cabling, lighting, heat tracing |
| SEC-13 | Controls System Basis | DISCIPLINE_BASIS | Architecture, topology, networks, servers, VMs, consoles, systems, configuration |
| SEC-14 | Instrumented Protection Basis | DISCIPLINE_BASIS | Fire/gas/H2S detection, ESD pushbuttons, shutdown interfaces |
| SEC-15 | Regulatory, Codes, and Standards Basis | REGULATORY | BC environmental, consultation, waste management, codes/specs/standards |
| SEC-16 | Appendices and External Deliverable Register | DATA_REFERENCE | Appendix status, navigation records, external deliverable register |

### Key Supersession Context

| Amendment | Key Supersessions |
|-----------|-------------------|
| SCA-001 | TEG dehy contactor sizing (VE-3); stabilizer count and provisions (VE-4a); SOC suction from 03-25 VRU (VE-4b); depropanizer removal (VE-14); NGL caustic regenerative → non-regenerative (VE-8); inlet separator 3rd provision (VE-21); heat medium single-loop 220C (VE-26); molecular sieve 3A/regen tower (VE-27); I/A consolidation at 04-25 2x100%+3rd (VE-8/29); inlet compressor starting VFD (VE-34a); LV standby generators on LV MCC (VE-39a/39b) |
| SCA-002 | Incinerator feed basis and caustic changes; incinerator location at 03-25, shared coordination; coordination open items (HBK-5974/5975/5976) |
| SCA-006 | 04-25 I/A demand 720 SCFM (TBC) extended to include 03-25 cross-facility 393 SCFM; combined basis 1,113 SCFM (TBC) |

### Retired / Special-Treatment KTYs

| KTY | Treatment |
|-----|-----------|
| KTY-04-18_Depropanizer | Retired — not active process body authority; context/open-item only in SEC-07 |
| KTY-04-16_LPG-Mercaptan-Treating-FUTURE | Current NGL scope after SCA cleanup; obsolete LPG/FUTURE framing is not current-state |
| KTY-04-17_LPG-Molecular-Seive-MS-Dehydration-FUTURE | Current NGL scope after SCA cleanup; obsolete LPG/FUTURE framing is not current-state |

### Key Open Items to Surface

| Item | Type | Sections |
|------|------|----------|
| CONF-02 | Human ruling | SEC-06 — TEG contactor sparing remains TBD |
| CONF-03 | Deferred confirmation | SEC-07 — NGL regen-gas/vapour source existence TBD |
| Metering schematic | External deliverable gap | SEC-03 |
| Plot plan | External deliverable gap | SEC-02 |
| Appendix bodies | External deliverable gap | SEC-16 |

## Package Assembly and Closeout

After all 16 sections are written:

1. Assemble `Rewritten_DBM.md` from the 16 section files with front matter
2. Produce closeout artifacts:
   - `Publication_Open_Items.md` — TBDs, TBCs, assumptions, deferred confirmations
   - `Publication_Content_Adequacy.md` — completeness against Publication_Schema.md and Publication_Rules.md
   - `Publication_Readiness.md` — readiness verdict with evidence
3. Generate `Rewritten_DBM.docx` from the final assembled package DBM

## Output Topology

```
_Publication/DBM/
  _Planning/
    Publication_Input_Manifest.md       (new — admitted inputs and alignment check results)
  sections/
    SEC-01/SEC-01.md
    SEC-02/SEC-02.md
    ...
    SEC-16/SEC-16.md
  package/
    RUN-20260423-FRESH-DEEPCUT-DBM/
      Rewritten_DBM.md
      Rewritten_DBM.docx
      Publication_Open_Items.md
      Publication_Content_Adequacy.md
      Publication_Readiness.md
      Input_Manifest.md                 (copy for package immutability)
```

## Success Criteria

- All 16 sections present in assembled DBM
- Headings follow `# SEC-NN - <Title>` per Publication_Rules.md
- TBD/TBC preserved where upstream carries uncertainty
- Active SCA-006 supersession bindings applied
- Mapped-row roles respected (PRIMARY/SUPPORTING/CONTEXT_ONLY)
- No source file names or KTY mechanics in body prose
- No prior prose reused — all section content sourced from KA reads
- .docx contains inline formatted tables with header rows
- Completeness documented in Publication_Content_Adequacy.md
- Open items documented in Publication_Open_Items.md
- Readiness verdict documented in Publication_Readiness.md
- Each section is independently re-runnable
- Retired KTY-04-18 (Depropanizer) not used as active body authority
- NGL treating KTYs (04-16, 04-17) use current-state framing, not obsolete LPG/FUTURE terminology
- Combined instrument air demand basis (1,113 SCFM TBC) correctly represented
