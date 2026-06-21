# Semantic Lensing Register: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract`
**Warnings:** Existing deliverable files include pre-run dirty or untracked changes outside this task scope; this run did not edit them. `_SEMANTIC.md` Matrix A and Matrix B are canonical direct tables rather than `### Result` subsections; they were parsed as primary canonical result tables for coverage.

**Inputs Read:**
- _CONTEXT.md — deliverable identity, scope, traceability, and source authority
- _STATUS.md — current lifecycle state and history; read only
- _SEMANTIC.md — primary/canonical tables for matrices A, B, C, F, D, X, E
- Datasheet.md — identification, attributes, conditions, construction, references
- Specification.md — scope, requirements, standards, verification, documentation
- Guidance.md — purpose, principles, considerations, trade-offs, examples, conflict table
- Procedure.md — purpose, prerequisites, steps, verification, records
- _REFERENCES.md — metadata only; external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 7
- By document:
  - Datasheet: 0
  - Specification: 1
  - Guidance: 1
  - Procedure: 2
  - Multi: 3
  - NA: 0
- By matrix:
  - A: 0
  - B: 1
  - C: 1
  - F: 2
  - D: 1
  - X: 1
  - E: 1
- By type:
  - Conflict: 1
  - VerificationGap: 1
  - MissingSlot: 2
  - WeakStatement: 1
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Prescriptive direction is represented by the sourced alias and matrix vocabulary rules; no additional direction gap surfaced. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | Mandatory practice is covered by explicit MUST requirements for aliases, rows, columns, route destinations, and persona lookup. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Compliance determination is present through requirement-level verification rows and no separate judging slot is missing. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | Review posture is represented by source-warning preservation and conflict surfacing guidance without requiring a new item here. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Procedural direction is stated in Procedure steps for source extraction, fixture construction, and TBD handling. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Practical execution is assigned to later tests and fixtures, and detailed gaps are captured under fixture-specific matrices. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Performance assessment is expressed through verification checks for aliases, matrix vocabulary, route destination, and persona lookup. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Process audit is represented by Procedure verification and source-warning checks; no separate audit edit is warranted. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Value orientation is covered by Guidance principles that restrict aliases and preserve WORKBENCH versus PIPELINE boundaries. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Merit application is covered by explicit criteria for sourced aliases, row destinations, and unknown-key warning behavior. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Worth determination has no standalone missing slot beyond the recorded TBDs for implementation evidence. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Quality appraisal is represented by the conflict table posture and verification checks without an added item. |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | Essential alias, row, column, and route facts are listed in Datasheet attributes and Specification requirements. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Evidence sources are cited per requirement, with the PRD warning handled as a separate coherence item. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | The five aliases, three rows, four columns, and three row destinations are enumerated without a missing data row. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | Reliable measurement surfaces an ambiguity in unknown alias behavior that affects repeatable alias tests. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Essential signals for WORKBENCH and PIPELINE routing are present in Specification scope and Guidance considerations. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | Context for alias, matrix, route, and persona behavior is adequate for later implementation planning. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | The production documents give a complete high-level account of aliases, row routing, persona lookup, and fallback. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | Messaging consistently separates WORKBENCH persona routing from PIPELINE operative category routing. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Fundamental understanding is supplied through the scope exclusions and source-governed vocabulary principles. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Competent implementation knowledge is deferred only where file paths and concrete fixtures remain TBD. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Thorough mastery is not expected at document-draft stage; known implementation unknowns are tracked elsewhere. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Coherent understanding is maintained across Datasheet construction, Specification requirements, and Guidance principles. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Essential discernment appears in the no-invention principle for aliases and persona names. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Adequate judgment is documented by applying D-APP-38 for source state and ADQ-12 for the loop-first persona contract. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Holistic insight is covered by the deliverable's explicit boundary against SDK adapter and full pipeline dispatch work. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Principled reasoning is visible in Guidance trade-offs for strict aliases, matrix fixtures, and pipeline distinction. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | Resolved | Multi | TBD | Unknown non-empty personas pass through normalized and fail later at instruction-file lookup if absent. | ADQ-12 records the deterministic fallback behavior in Specification, Guidance, Procedure, Datasheet, and persona-resolution tests. | Specification.md; Guidance.md | Specification Verification; Guidance Examples |  | ADQ-12 | ADQ-12 accepted fallback semantics |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | source mandate | 0 | NO_ITEMS | Source mandate is explicit for TYPES vocabulary, PRD routing, SPEC fallback, and CONTRACT no-invention rules. |
| C:[normative]:[sufficiency] | normative | sufficiency | evidence threshold | 0 | NO_ITEMS | Evidence threshold is described through per-requirement source citations and standards applicability. |
| C:[normative]:[completeness] | normative | completeness | coverage obligation | 0 | NO_ITEMS | Coverage obligation is represented by requirements for all sourced aliases, matrix rows, columns, route destinations, and persona lookup. |
| C:[normative]:[consistency] | normative | consistency | rule coherence | 1 | HAS_ITEMS | Rule coherence recorded the former REF-006 source-state conflict; ADQ-12 marks it resolved by D-APP-38. |
| C:[operative]:[necessity] | operative | necessity | route trigger | 0 | NO_ITEMS | Route trigger is captured by the row-based WORKBENCH and PIPELINE requirements. |
| C:[operative]:[sufficiency] | operative | sufficiency | fixture adequacy | 0 | NO_ITEMS | Fixture adequacy gaps are better tracked under routing proof and fixture coverage lenses. |
| C:[operative]:[completeness] | operative | completeness | workflow coverage | 0 | NO_ITEMS | Workflow coverage is described from source extraction through tests and fixtures in Procedure steps. |
| C:[operative]:[consistency] | operative | consistency | behavior stability | 0 | NO_ITEMS | Behavior stability is protected by strict sourced aliases and stable route shape constraints. |
| C:[evaluative]:[necessity] | evaluative | necessity | boundary basis | 0 | NO_ITEMS | Boundary basis is explicit in the deliverable scope and out-of-scope statements. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | criteria warrant | 0 | NO_ITEMS | Criteria warrant is grounded in Guidance principles and the verification table. |
| C:[evaluative]:[completeness] | evaluative | completeness | review coverage | 0 | NO_ITEMS | Review coverage is represented by source warning, dependency deferral, and no-invention checks. |
| C:[evaluative]:[consistency] | evaluative | consistency | rationale coherence | 0 | NO_ITEMS | Rationale coherence is maintained across preferred directions and examples without a distinct C-matrix edit. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[consistency] | Resolved | Multi | NA | Former PRD source-state warning is resolved under D-APP-38. | `_REFERENCES.md` now records REF-006 as `MATCH`; ADQ-12 keeps source-state proof separate from implementation proof. | Specification.md; Guidance.md; _REFERENCES.md | Specification Requirements and Standards; Guidance Principles and Trade-offs; _REFERENCES.md REF-006 | Specification.md#Requirements; _REFERENCES.md#REF-006 | D-APP-38 | D-APP-38 accepted current authority corpus |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | authority basis | 0 | NO_ITEMS | Authority basis is stated for TYPES, PRD, SPEC, CONTRACT, and DIRECTIVE sources. |
| F:[normative]:[sufficiency] | normative | sufficiency | proof standard | 0 | NO_ITEMS | Proof standard is expressed through unit, fixture, route-state, and runtime option tests. |
| F:[normative]:[completeness] | normative | completeness | source coverage | 0 | NO_ITEMS | Source coverage spans aliases, matrix vocabulary, route destinations, workbench context, persona lookup, and fallback. |
| F:[normative]:[consistency] | normative | consistency | trace coherence | 0 | NO_ITEMS | Trace coherence is intact under D-APP-38 and ADQ-12 source-state updates. |
| F:[operative]:[necessity] | operative | necessity | dispatch trigger | 0 | NO_ITEMS | Dispatch trigger is covered by OPERATIVE to PIPELINE and NORMATIVE/EVALUATIVE to WORKBENCH requirements. |
| F:[operative]:[sufficiency] | operative | sufficiency | routing proof | 1 | HAS_ITEMS | Routing proof is underspecified until implementation-local module, fixture, and test paths are selected. |
| F:[operative]:[completeness] | operative | completeness | fixture coverage | 0 | NO_ITEMS | Fixture coverage is listed across alias resolver, matrix mapping, route fixtures, and persona resolver tests. |
| F:[operative]:[consistency] | operative | consistency | route stability | 0 | NO_ITEMS | Route stability is protected by the route shape constraint and row destination requirements. |
| F:[evaluative]:[necessity] | evaluative | necessity | appraisal basis | 0 | NO_ITEMS | Appraisal basis is the sourced routing and persona contract, not broader SDK or prompt composition behavior. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | review standard | 1 | HAS_ITEMS | Review standard needs concrete evidence capture for the later test and fixture artifacts. |
| F:[evaluative]:[completeness] | evaluative | completeness | assessment coverage | 0 | NO_ITEMS | Assessment coverage is broad enough once implementation path and evidence slots are added. |
| F:[evaluative]:[consistency] | evaluative | consistency | judgment coherence | 0 | NO_ITEMS | Judgment coherence is maintained by warning-based source handling and no-invention constraints. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[sufficiency] | MissingSlot | Procedure | Procedure | Add the selected module paths and fixture/test file paths for alias resolver, matrix mapping, route fixtures, and persona resolver when implementation begins. | Datasheet and Specification both mark exact implementation file paths as TBD, while Procedure prerequisites depend on knowing those paths before executable routing proof can be sufficient. | Datasheet.md; Specification.md; Procedure.md | Datasheet Construction; Specification Documentation; Procedure Prerequisites |  | PROPOSAL | TBD |
| F-002 | F:[evaluative]:[sufficiency] | VerificationGap | Specification | Specification | Define the evidence artifact names or command outputs that prove alias, matrix, route, workbench-context, persona, and fallback checks passed. | Specification lists required verification artifacts, but the records section does not yet identify concrete result files or command output locations for later audit. | Specification.md; Procedure.md | Specification Verification; Procedure Records |  | PROPOSAL | TBD |

## Matrix D — Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | canonical direction | 0 | NO_ITEMS | Canonical direction is supplied by TYPES vocabulary and the no-invention rule for aliases and persona names. |
| D:[normative]:[applying] | normative | applying | mandatory proof | 0 | NO_ITEMS | Mandatory proof is present as MUST requirements with verification methods. |
| D:[normative]:[judging] | normative | judging | coverage ruling | 0 | NO_ITEMS | Coverage ruling is represented by enumerated alias and matrix vocabulary checks. |
| D:[normative]:[reviewing] | normative | reviewing | trace audit | 0 | NO_ITEMS | Trace audit is supported by source citations and the D-APP-38 REF-006 MATCH state. |
| D:[operative]:[guiding] | operative | guiding | dispatch direction | 0 | NO_ITEMS | Dispatch direction is clear for row-to-surface routing and pipeline distinction. |
| D:[operative]:[applying] | operative | applying | fixture execution | 1 | HAS_ITEMS | Fixture execution is supported by ADQ-12 route-state, matrix launch, and persona-resolution tests. |
| D:[operative]:[judging] | operative | judging | routing assessment | 0 | NO_ITEMS | Routing assessment is defined by expected destinations and persona lookup outcomes. |
| D:[operative]:[reviewing] | operative | reviewing | process review | 0 | NO_ITEMS | Process review is represented in the Procedure verification table and source-warning check. |
| D:[evaluative]:[guiding] | evaluative | guiding | boundary orientation | 0 | NO_ITEMS | Boundary orientation is explicit in the in-scope and out-of-scope lists. |
| D:[evaluative]:[applying] | evaluative | applying | criteria application | 0 | NO_ITEMS | Criteria application is reflected in strict alias use, visible unsupported options, and unknown-key warnings. |
| D:[evaluative]:[judging] | evaluative | judging | quality determination | 0 | NO_ITEMS | Quality determination is deferred to tests and fixtures without a separate document edit. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | rationale appraisal | 0 | NO_ITEMS | Rationale appraisal is already recorded in Guidance trade-offs and examples. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | WeakStatement | Multi | TBD | Replace generic "route state or query parameters" wording with the actual context keys once implementation chooses them. | Specification requires selected agent, row, and column context preservation, but Guidance and Specification leave exact query-param names open; later tests need fixed keys or a cited adapter boundary. | Specification.md; Guidance.md | Specification Requirements DEL-08-02-REQ-011; Guidance Trade-offs |  | PROPOSAL | TBD |

## Matrix X — Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | source anchor | 0 | NO_ITEMS | Source anchor is present through the standards table and reference metadata. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | direction proof | 0 | NO_ITEMS | Direction proof is covered by cited requirements and Guidance principles. |
| X:[guiding]:[completeness] | guiding | completeness | direction coverage | 0 | NO_ITEMS | Direction coverage includes aliases, matrix vocabulary, routing destinations, workbench context, and persona behavior. |
| X:[guiding]:[consistency] | guiding | consistency | contract coherence | 0 | NO_ITEMS | Contract coherence is generally maintained, with PRD hash handling tracked as a separate conflict/rationale issue. |
| X:[applying]:[necessity] | applying | necessity | fixture anchor | 0 | NO_ITEMS | Fixture anchor is present through anticipated artifacts and required verification artifacts. |
| X:[applying]:[sufficiency] | applying | sufficiency | fixture proof | 0 | NO_ITEMS | Fixture proof is represented by required tests, with concrete evidence naming captured under F. |
| X:[applying]:[completeness] | applying | completeness | fixture coverage | 1 | HAS_ITEMS | Fixture coverage is affected by unresolved dependency extraction and accepted upstream/downstream edge status. |
| X:[applying]:[consistency] | applying | consistency | behavior coherence | 0 | NO_ITEMS | Behavior coherence is protected by deterministic fallback and unknown-key warning requirements. |
| X:[judging]:[necessity] | judging | necessity | decision basis | 0 | NO_ITEMS | Decision basis is present in expected route destinations and persona outcomes. |
| X:[judging]:[sufficiency] | judging | sufficiency | coverage proof | 0 | NO_ITEMS | Coverage proof is sufficient at document level once concrete fixture evidence is later produced. |
| X:[judging]:[completeness] | judging | completeness | decision coverage | 0 | NO_ITEMS | Decision coverage spans alias, matrix, route, workbench, persona, fallback, unknown-key, and visibility checks. |
| X:[judging]:[consistency] | judging | consistency | evidence coherence | 0 | NO_ITEMS | Evidence coherence is maintained by matching verification labels across Specification and Procedure. |
| X:[reviewing]:[necessity] | reviewing | necessity | trace basis | 0 | NO_ITEMS | Trace basis is supported by _REFERENCES metadata and per-requirement source columns. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | review proof | 0 | NO_ITEMS | Review proof is adequate for document drafting; execution proof is separately tracked. |
| X:[reviewing]:[completeness] | reviewing | completeness | review record | 0 | NO_ITEMS | Review record includes the conflict table, PRD warning, and dependency deferral notes. |
| X:[reviewing]:[consistency] | reviewing | consistency | review coherence | 0 | NO_ITEMS | Review coherence keeps warnings, TBDs, and deferred dependency extraction visible. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[applying]:[completeness] | MissingSlot | Multi | TBD | Populate accepted dependency edges or record an explicit no-edge ruling after the authorized dependency-extract phase. | Specification defers dependency extraction and Procedure says declared upstream dependencies are TBD, so closure cannot rely on a complete dependency picture yet. | Specification.md; Procedure.md | Specification Out of scope; Procedure Prerequisites and Step 14 |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | source evidence | 0 | NO_ITEMS | Source evidence is enumerated in Datasheet references and Specification standards. |
| E:[guiding]:[information] | guiding | information | route signal | 0 | NO_ITEMS | Route signal is clear for NORMATIVE, OPERATIVE, and EVALUATIVE row destinations. |
| E:[guiding]:[knowledge] | guiding | knowledge | contract understanding | 0 | NO_ITEMS | Contract understanding is sufficient for the persona alias and matrix routing slice. |
| E:[guiding]:[wisdom] | guiding | wisdom | direction judgment | 0 | NO_ITEMS | Direction judgment is represented by no-invention, visible unsupported options, and warning-based source handling. |
| E:[applying]:[data] | applying | data | fixture record | 0 | NO_ITEMS | Fixture record expectations are named, with concrete file paths tracked under F. |
| E:[applying]:[information] | applying | information | route context | 0 | NO_ITEMS | Route context is covered by preserving selected agent, row, and column, with key names tracked under D. |
| E:[applying]:[knowledge] | applying | knowledge | behavior understanding | 0 | NO_ITEMS | Behavior understanding is captured for aliases, row routing, persona lookup, and fallback. |
| E:[applying]:[wisdom] | applying | wisdom | fixture judgment | 0 | NO_ITEMS | Fixture judgment has no separate gap beyond evidence artifact naming. |
| E:[judging]:[data] | judging | data | proof record | 0 | NO_ITEMS | Proof record is planned through required verification artifacts and future implementation records. |
| E:[judging]:[information] | judging | information | decision signal | 0 | NO_ITEMS | Decision signal is explicit for WORKBENCH, PIPELINE, and `PERSONA_NOT_FOUND` outcomes. |
| E:[judging]:[knowledge] | judging | knowledge | judgment understanding | 0 | NO_ITEMS | Judgment understanding aligns with source-governed vocabulary and route-surface distinction. |
| E:[judging]:[wisdom] | judging | wisdom | coverage judgment | 0 | NO_ITEMS | Coverage judgment is documented by complete alias and matrix enumeration. |
| E:[reviewing]:[data] | reviewing | data | review record | 0 | NO_ITEMS | Review record includes current warnings and TBDs without requiring a new data item. |
| E:[reviewing]:[information] | reviewing | information | review signal | 1 | HAS_ITEMS | Review signal recorded the former REF-006 transition question; ADQ-12 marks it resolved by D-APP-38. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | trace understanding | 0 | NO_ITEMS | Trace understanding is supported by reference metadata and warning labels. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | review judgment | 0 | NO_ITEMS | Review judgment remains with the human for PRD hash acceptance and unknown behavior rulings. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[information] | Resolved | Guidance | Guidance | REF-006 transition path is resolved by D-APP-38. | Current guidance records PRD-backed checks as source-current while implementation proof remains separate. | Guidance.md; _REFERENCES.md | Guidance Trade-offs and Conflict Table; _REFERENCES.md REF-006 |  | D-APP-38 | D-APP-38 accepted current authority corpus |
