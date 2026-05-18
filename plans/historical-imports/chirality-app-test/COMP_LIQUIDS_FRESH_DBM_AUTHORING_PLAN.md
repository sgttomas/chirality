# Plan: Author West Doe Comp & Liquids (03-25) DBM from Governed KA Content

## Objective

Author a new West Doe Compressor Station and Liquids Hub (03-25) Design Basis Memorandum from current governed KTY/KA content in FULL_ENGINEERING_DBM mode. Reuse structural/deterministic publication artifacts after alignment checks. Do not reuse any prior DBM prose, section outputs, review outputs, or package text. Write fresh section bodies, assemble a publication package with closeout artifacts, and generate a final .docx.

## Admitted Inputs

All paths relative to `domain-test/domains/West_Doe_Comp_and_Liquids_DBM/`.

### Structural / Planning Inputs

| Artifact | Role |
|----------|------|
| `_Publication/DBM/_Planning/Publication_Schema.md` | 16-section structure definition |
| `_Publication/DBM/_Planning/Publication_Rules.md` | Style, completeness standard, naming, supersession policy |
| `_Publication/DBM/_Planning/Section_Map.csv` | KA-to-section mapping (selector) |
| `_Decomposition/WEST_DOE_DOMAIN_DECOMPOSITION.md` | Domain decomposition authority |
| `_Decomposition/annex_*.csv` | Decomposition companion registers |

### Publication-Admission Inputs

| Artifact | Role |
|----------|------|
| `_ScopeChange/_LATEST.md` | Active scope-change pointer |
| `_ScopeChange/SCA-006_2026-04-22_0900/Supersession_Map.csv` | Active supersession bindings |
| `_ScopeChange/SCA-006_2026-04-22_0900/Handoff_State.md` | Closure status, remaining blockers |
| `_ScopeChange/SCA-006_2026-04-22_0900/Decision_Log.md` | Admission decisions |
| `_Reconciliation/DecompCoverage/_LATEST.md` | Audit evidence pointer |
| Resolved audit snapshot and QA report (path from pointer) | Frozen audit evidence |

### Reference / Provenance Inputs

| Artifact | Role |
|----------|------|
| `_Sources/W242510-PRC-DBM-000001-001_(3-25_Doe)_DBM.md` | Source DBM for conflict checking |
| `_Sources/TOC_Compression_Liquids.md` | Source table of contents |
| Shared clean source package (`West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/`) | Cross-facility reference |

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

- Prior `Rewritten_DBM.md` from any package run
- Prior section bodies (`sections/SEC-##/SEC-##.md`)
- Prior package QA, readiness, open-items, or concordance outputs
- Prior review artifacts
- Prior dispatch outputs

## Alignment Checks (pass / patch / regenerate)

| Check | Criteria | Pass | Patch | Regenerate |
|-------|----------|------|-------|------------|
| Active SCA pointer | `_LATEST.md` points to SCA-006 | Confirmed | N/A | Fail run |
| Section_Map.csv paths | All PRIMARY artifact paths resolve | All resolve | Exclude missing rows, log | Fail if >5% missing |
| Retired KTY exclusion | No RETIRED/TOMBSTONED rows admitted as active body inputs | None present | Exclude retired rows, log | N/A |
| Schema alignment | Publication_Schema.md defines 16-section FULL_ENGINEERING_DBM | Matches | N/A | Structural mismatch → fail |
| Rules basis currency | Publication_Rules.md current-state-basis references SCA-006 | Current | Patch stale SCA-005 refs → SCA-006 | N/A |
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
    RUN-20260423-FRESH-DBM/
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
