# DBM Publication Full-DBM Remediation Plan

Status: DRAFT - not approved  
Date: 2026-04-22  
Scope: Global DBM publication agent/skill contracts first; West Doe Deepcut and West Doe Comp & Liquids validation runs second.

## 1. Problem Statement

The current DBM publication workflow produced governed packages that are traceable and structurally coherent, but too brief to function as full Design Basis Memoranda. The observed Deepcut package reads closer to a current-state digest than a governing engineering DBM. The same pattern appears in the other West Doe project, which indicates a workflow calibration problem rather than an isolated worker failure.

The fix is not to patch the existing `Rewritten_DBM.md` files. The intended correction is to revise the publication contracts, then run fresh DBM publication from the accepted upstream DOMAIN/SCA state.

## 2. Research Findings

The failure mode is rooted in the publication contracts:

- `AGENT_DBM_PUBLISHER.md` correctly says the output is a rewritten DBM and includes a strong engineering prose standard, but it does not define a full-DBM body completeness standard.
- The generated `Publication_Rules.md` for Deepcut instructs high-count sections to summarize stable system-level design basis and rely on trace appendices for line-level provenance.
- `dbm-section-publish` has skeletal default section templates. They are good outlines, but they do not require complete engineering basis treatment.
- `dbm-section-publish` requires every PRIMARY mapped KTY to contribute at least one material design-basis statement unless skipped with a reason. One statement per KTY is too weak for full DBM publication.
- `dbm-publish` validates deterministic assembly, traceability, concordance, open items, source supersession, and readiness, but it does not block a package for being underdeveloped as a DBM body.
- The deterministic assembler is doing its job: it assembles and checks package structure. It is not a semantic content-depth validator.
- Traceability was moved out of body prose as intended, but engineering detail was compressed along with trace detail. That is the core optimization error.
- The Comp & Liquids package shows a second symptom: QA and trace scaffolding leaked into the DBM body. Sections used containers such as mapped assertions, caveat inventories, and reference blocks as the primary body shape instead of DBM-native engineering narrative, tables, and design-basis subsections.
- The body was not sufficiently standalone. A reader often needed to reopen KA files or trace artifacts to recover core engineering basis that should have appeared in the DBM body.

The current workflow optimized against hallucination, repetition, and artifact dumping. Those are valid constraints, but the missing counterweight was a DBM completeness requirement.

## 3. Policy Decisions From Review

The remediation will use these decisions:

- The default DBM publisher output must be a full EPC-style engineering DBM, not a digest.
- A digest or executive current-state summary may exist only as an explicit output mode, not as the default DBM publication output.
- Global agent/skill contracts are repaired first because both West Doe projects were affected in the same way.
- Tabular engineering data belongs in the DBM body when it is part of the design basis. Provenance and trace tables remain in appendices.
- The existing short packages will not be repaired in place. New publication runs will start from scratch after the contract updates.

## 4. Root Cause Analysis

### 4.1 Missing Output Mode Distinction

The workflow treats "rewritten DBM" and "current-state publication package" as the same thing. That allowed a concise governed summary to pass as the DBM body.

Required correction: introduce explicit output modes:

- `FULL_ENGINEERING_DBM` - default; full body treatment of engineering basis, tables, limits, interfaces, assumptions, TBDs, and design constraints.
- `DBM_DIGEST` - optional; concise current-state summary, not acceptable as the governing DBM unless the human explicitly requests a digest.

### 4.2 Overcompression Rule

The planning rules encouraged summarization for large sections. This made sense for provenance and line-level traceability, but it was over-applied to engineering content.

Required correction: split "trace detail" from "engineering detail."

- Trace detail: appendix and QA.
- Engineering detail: body.
- Source quotation and provenance mechanics: appendix.
- Design-basis values, capacities, tables, operating conditions, limits, equipment lists, material decisions, and open design requirements: body.

### 4.3 Weak Section Completeness Contract

Current section templates are too thin. They tell a worker what kinds of paragraphs to write, but not what a DBM section must contain.

Required correction: section workers need a DBM adequacy checklist based on engineering content classes, not a generic prose outline.

Each section must decide whether mapped inputs contain:

- governing design criteria,
- capacities, rates, loads, compositions, emissions, or utility demands,
- equipment and package configuration,
- operating modes and design cases,
- controls, safeguards, shutdowns, relief, alarms, or permissives,
- materials, standards, codes, environmental limits, or regulatory constraints,
- interfaces with other systems, areas, facilities, or disciplines,
- assumptions, TBDs, exclusions, and design-development requirements,
- tabular data that is part of the design basis.

If any applicable class is omitted, the section QA must say why. Unsupported omission becomes a package blocker.

### 4.4 No Fullness Gate

The package gate can pass a short DBM if it is internally consistent. That is exactly what happened.

Required correction: add a package-level DBM content adequacy gate. This should not be a crude word-count gate. It should be a structured semantic review backed by deterministic smoke-test signals.

The agent should decide adequacy, but it must explain that decision against a stable checklist. Quantitative signals should flag anomalies, not replace engineering judgment.

### 4.5 Broad Section Mapping

Some sections collect many KTYs under broad headings. Without subsections and required tables, broad sections naturally compress.

Required correction: schema design must be DBM-native. Gate 3 should require section/subsection structure detailed enough to carry the source basis without collapsing multiple systems into short summary paragraphs.

### 4.6 QA Scaffold Became Body Shape

The generated section bodies used publication QA/reporting structures as if they were DBM structures. `Mapped Design Basis`, `Controlled Assertions`, raw current-state caveat lists, and reference inventories are useful companion artifacts, but they are not a satisfactory body outline for a full DBM.

Required correction: full DBM sections must be written in DBM-native form. QA assertions, detailed trace, and extracted caveat inventories should remain in QA outputs or appendices. TBDs, assumptions, and design-development requirements should be integrated into the relevant engineering subsections and summarized in a dedicated open-items/design-development section when needed.

## 5. Remediation Workstreams

### Workstream A - Global Contract Updates

Update `agents/AGENT_DBM_PUBLISHER.md`:

- Add `DBM_OUTPUT_MODE`, default `FULL_ENGINEERING_DBM`.
- State that `FULL_ENGINEERING_DBM` is the default and that `DBM_DIGEST` requires explicit human selection.
- Add a non-negotiable invariant: DBM body completeness is a publication requirement equal to traceability and concordance.
- Clarify that appendices remove provenance clutter from the body, not engineering facts from the body.
- Require Gate 3 to freeze a body completeness standard as part of `Publication_Rules.md`.
- Require Gate 3 schema approval to evaluate whether sections are too broad and need subdivision.
- Require clean restart after quality-limited runs unless the human explicitly authorizes targeted reuse.

Update `skills/dbm-section-publish/SKILL.md`:

- Replace skeletal section expectations with DBM adequacy expectations by section type.
- Require workers to preserve source tables or reconstruct equivalent body tables when tables contain design-basis values.
- Add a `Table Treatment` QA record: included, consolidated, split, omitted with reason, or trace-only.
- Add a `Design Basis Content Coverage` QA record against the engineering content classes listed above.
- Strengthen PRIMARY KTY contribution expectations: one sentence is insufficient when the KTY contains multiple material design-basis facts or tables.
- Require section workers to emit an `UNDERDEVELOPED_SECTION` finding when mapped active material cannot be represented adequately within the approved section design.
- Prohibit repeated QA/export artifact structure as the default body outline in `FULL_ENGINEERING_DBM` mode. Normal DBM headings such as References, Design Notes, Design Criteria, and Design Development Items remain allowed when used as engineering sections. The prohibited pattern is per-section assertion registers, raw caveat dumps, path inventories, or trace scaffolds standing in for the DBM body.
- Require each section body to be usable for the core engineering design basis without opening KA files. This does not mean every provenance detail belongs in the body; KA/source references support provenance and auditability, but they must not be the only place where material design-basis content appears.

Update `skills/dbm-publish/SKILL.md`:

- Add package-level `DBM Content Adequacy Review`.
- Add readiness blockers:
  - `UNDERDEVELOPED_SECTION`
  - `UNJUSTIFIED_TABLE_OMISSION`
  - `PRIMARY_KTY_COLLAPSED`
  - `MISSING_DESIGN_BASIS_CLASS`
  - `DIGEST_MODE_USED_FOR_FULL_DBM`
  - `QA_SCAFFOLD_BODY_LEAKAGE`
- Add a mandatory content-adequacy gate record for `FULL_ENGINEERING_DBM` mode. Preferred package artifact: `Publication_Content_Adequacy.md`; acceptable low-friction alternative: a mandatory fixed-schema `DBM Content Adequacy` section inside `Publication_Readiness.md`. The gate record must be lean and bounded, not a prose mini-audit.
- The package gate assembles the adequacy record from section QA outputs, deterministic content-profile smoke-test signals, and direct package review. Section workers must not author the package adequacy artifact from scratch.
- Keep `READY_WITH_MAJOR_NOTES` for residual non-blocking quality issues, but make materially underdeveloped body content blocking for full DBM mode.

Minimum `Publication_Content_Adequacy.md` schema:

1. `Package Verdict`
   - `AdequacyVerdict`: `PASS | PASS_WITH_NOTES | BLOCKED`
   - `DBMOutputMode`
   - `BlockingFindingCount`
   - short blocker list, if any
2. `Section Adequacy Matrix`
   - `SectionID`
   - `SectionTitle`
   - `CoreBasisStandalone`: `YES | NO`
   - `DBMNativeStructure`: `YES | NO`
   - `SourceDBMGeometry`: `PRESERVED | INTENTIONALLY_REDESIGNED | NOT_AVAILABLE | FAIL`
   - `DesignBasisTablesHandled`: `INCLUDED | CONSOLIDATED | OMITTED_WITH_RATIONALE | DEFERRED_UPSTREAM_MISSING | NONE_APPLICABLE`
   - `PrimaryKTYsMateriallyUsed`: `YES | NO`
   - `QAScaffoldLeakage`: `NONE | WARNING | BLOCKER`
   - `UnderdevelopedSection`: `NO | YES`
   - `SectionVerdict`: `PASS | PASS_WITH_NOTES | BLOCKED`
3. `Table Treatment Summary`
   - design-basis tables only; exclude trace, index, provenance, and reference tables
   - summarize included, consolidated/redesigned, omitted with rationale, and deferred because upstream truth is missing
4. `Blockers`
   - fixed finding-code list only: `UNDERDEVELOPED_SECTION`, `UNJUSTIFIED_TABLE_OMISSION`, `PRIMARY_KTY_COLLAPSED`, `MISSING_DESIGN_BASIS_CLASS`, `QA_SCAFFOLD_BODY_LEAKAGE`, `NON_STANDALONE_CORE_BASIS`, `DIGEST_MODE_USED_FOR_FULL_DBM`
5. `Human Review Notes`
   - only issues requiring human judgment; no general commentary or duplicate QA narrative

Update publication helper tooling only where useful:

- Add deterministic content-profile signals, either by extending existing helpers or adding a new helper such as `tools/publication/profile_publication_content.py`.
- Suggested signals: body word count by section, body table count by section, classified source table count, design-basis table count versus body table count, mapped PRIMARY KTY count, section QA table-treatment findings, PRIMARY KTY zero-contribution count, source-to-body design-basis table omission candidates, and caveat/reference-to-body ratios that may indicate QA scaffold leakage.
- Table metrics must classify source tables before comparison. Design-basis tables should drive body inclusion or intentional redesign; trace, index, provenance, and reference tables should not force artificial table inflation in the body.
- Add a forbidden/repeated scaffold-heading smoke test for `FULL_ENGINEERING_DBM` mode. It should flag repeated body use of headings or structures such as `Mapped Design Basis`, `Controlled Assertions`, raw `Current-State Caveats`, and full file-path reference inventories.
- Treat these as smoke tests. They flag likely underdevelopment for agent review; they do not define adequacy alone.

### Workstream B - Planning Artifact Standard

Revise the expected contents of generated `Publication_Rules.md`:

- Explicitly set `DBM_OUTPUT_MODE = FULL_ENGINEERING_DBM`.
- Include a "Body Completeness Standard" section.
- Include a "Tabular Data Policy" section.
- Include a "Trace vs Engineering Detail" section.
- Include a "Body vs QA Artifact Boundary" section.
- Include a "Standalone Body Usability" section.
- Include a "Section Underdevelopment Policy" section.
- Include a "Digest Output Prohibition" statement unless the human has selected digest mode.

Revise generated `Publication_Schema.md` expectations:

- Require each section to state expected body components, not only purpose and output shape.
- Require section designers to identify likely required tables before dispatch, preferably by subsection.
- Require each dispatched section to have a DBM-native section/subsection outline, not only a broad section title.
- Preserve the original DBM-native section/subsection geometry where available, or intentionally redesign it with rationale when the accepted current-state basis requires a different structure.
- Require subdivision when a section maps many systems or KTYs that cannot be represented as a coherent DBM section.
- Prefer DBM-native sections and subsections over broad compressed category summaries.

Revise section dispatch briefs:

- Include the body completeness standard.
- Include expected tables and data classes.
- Include section-specific adequacy risks from the context packet.
- Include instruction that body brevity is acceptable only when source material is genuinely sparse.
- Include explicit instruction not to use mapped-assertion lists, controlled-assertion registers, raw caveat dumps, or reference inventories as the main body structure.

### Workstream C - Validation Strategy Before Full West Doe Reruns

Before rerunning both complete West Doe DBMs, run a small contract validation pass:

1. Select one high-density section from Deepcut, preferably Utilities or Process Basis.
2. Select one high-density section from Comp & Liquids, preferably Utilities or a compressor/liquids process section.
3. Run section publication under the revised section contract.
4. Review whether the outputs now include real DBM body content: design values, tables, operating basis, package configuration, interfaces, caveats, and TBDs.
5. Revise global contracts once if the pilot still overcompresses or becomes an artifact dump.

This pilot is not a governed package acceptance step. It is a calibration check for the new global contracts.

### Workstream D - Project-Specific Clean Restart Runs

After global contract updates and pilot validation:

1. Deepcut DBM publication:
   - Start with Gate 1 `CLEAN_RESTART`.
   - Do not use the prior short package as body-authoring authority.
   - Consume the accepted upstream DOMAIN/SCA state, including latest scope-change pointers.
   - Regenerate `_Planning`, dispatch, sections, package, readiness, and pointers only after human acceptance.

2. Comp & Liquids DBM publication:
   - Same clean restart procedure.
   - Ensure shared-system facts align with Deepcut where accepted SCA/concordance state requires it.
   - Carry cross-facility facts through concordance register rather than duplicated ad hoc prose.

3. Prior packages:
   - Retain as historical publication packages.
   - Do not repair them in place.
   - Do not treat them as full DBM governed output after the new approach is adopted.
   - Only update accepted/latest pointers after the successor package is accepted by the human.

### Workstream E - SCOPE_CHANGE Boundary

The brevity problem itself is not a decomposition scope change. It is a publication workflow defect.

Run `SCOPE_CHANGE` only when the new full-DBM publication process reveals that accepted decomposition truth needs amendment. Examples:

- a design-basis fact is missing from the decomposition/KTY layer,
- a new human ruling changes accepted current-state content,
- source/reference material must be incorporated into governed KTY truth before publication,
- a shared-system or cross-facility relation is not represented in decomposition state.

Do not use `SCOPE_CHANGE` to make the publication body longer. Use it only to amend upstream truth.

## 6. Acceptance Criteria

Global remediation is complete when:

- `AGENT_DBM_PUBLISHER.md` distinguishes full DBM output from digest output.
- `dbm-section-publish` contains a DBM body adequacy contract.
- `dbm-publish` contains a package-level content adequacy gate.
- Planning artifact requirements include body completeness, table treatment, and underdevelopment policy.
- A pilot section run demonstrates that engineering detail remains in the body while traceability remains in appendices.

West Doe remediation is complete when:

- Deepcut and Comp & Liquids each complete a fresh DBM publication run from current accepted upstream state.
- Each run uses `FULL_ENGINEERING_DBM` mode.
- Each package passes assembly, concordance, source/supersession validation where applicable, semantic verification, and content adequacy review.
- The body includes design-basis tables where source/KTY material supports them.
- Any omitted tables or source-heavy content have explicit QA rationale.
- A fixed-schema content-adequacy gate record is emitted for each `FULL_ENGINEERING_DBM` run, preferably as `Publication_Content_Adequacy.md`, and records package verdict, section adequacy matrix, design-basis table treatment, blockers, and human-review notes.
- The DBM body can be read as the governing core engineering design basis without chasing KA files for core values, capacities, configurations, interfaces, assumptions, and TBDs. Provenance details and audit mechanics remain in appendices or companion artifacts.
- The human accepts the successor package and only then updates publication pointers.

## 7. Risks and Controls

Risk: The new workflow may swing too far and produce artifact dumps.
Control: Keep provenance in appendices, require engineering prose synthesis, and require section QA to distinguish included design basis from trace material.

Risk: The new workflow may keep QA/checklist structures in the body while merely adding more words.
Control: Require DBM-native body outlines and keep assertion registers, detailed caveat inventories, and trace mechanics in companion artifacts or appendices.

Risk: Quantitative fullness gates may create perverse incentives.
Control: Use quantitative metrics as smoke tests, not as adequacy definitions. The blocking decision remains a structured engineering judgment against the DBM adequacy checklist.

Risk: Broad sections may remain too compressed.  
Control: Gate 3 must force schema subdivision or subsection planning before dispatch.

Risk: Rerunning from scratch costs time.  
Control: Use the existing publication workflow and updated contracts rather than inventing a reconstruction workflow for the short packages.

Risk: Project-specific content defects may be discovered during publication.  
Control: Route true upstream truth changes through narrow `SCOPE_CHANGE`; do not patch them directly in publication outputs.

## 8. Proposed Execution Order After Approval

1. Patch global contract files.
2. Add or update deterministic content-profile helper if needed.
3. Update QA/checklist files for affected skills.
4. Run focused tests or smoke checks on modified tooling.
5. Run two pilot section publications for calibration.
6. Revise contracts if the pilot indicates overcompression or artifact dumping.
7. Start clean Deepcut full-DBM publication run.
8. Start clean Comp & Liquids full-DBM publication run.
9. Review successor packages with human.
10. Update publication pointers only after acceptance.

## 9. Open Review Items

- Confirm whether the mandatory content-adequacy gate record should be a separate package artifact named `Publication_Content_Adequacy.md` or a fixed-schema section inside `Publication_Readiness.md`. The plan recommends the separate artifact for audit clarity, but the gate is more important than the filename.
- Decide whether content-profile tooling should be mandatory in v1 or introduced first as advisory.
- Decide whether pilot section outputs should be written under a scratch/calibration folder or a normal publication run folder marked non-governed.
- Decide whether the prior accepted-with-major-notes packages need an explicit status note, pointer annotation, or handoff note saying they are historical digest-like outputs and not the accepted full DBM successor.

## 10. Revision Log

- 2026-04-22: Draft created from research of `AGENT_DBM_PUBLISHER`, `dbm-section-publish`, `dbm-publish`, Deepcut planning artifacts, and observed short package output.
