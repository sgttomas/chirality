# Semantic Lensing Register: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-05_Dependencies_csv_v3_1_Reader_Writer_and_Linter
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py returned VALID
**Warnings:** [WARNING] PRD_HASH_MISMATCH: _REFERENCES.md REF-006 records docs/PRD.md HASH_MISMATCH; [WARNING] IMPLEMENTATION_SURFACES_TBD: module names, API handler names, fixture paths, payload type names, and warning taxonomy remain unresolved implementation choices.

**Inputs Read:**
- _CONTEXT.md - deliverable identity, package scope, traceability
- _STATUS.md - Current State INITIALIZED; read only
- _SEMANTIC.md - primary Result tables for A, B, C, F, D, X, E
- Datasheet.md - identification, attributes, conditions, construction, references
- Specification.md - scope, requirements, standards, verification, documentation
- Guidance.md - purpose, principles, considerations, trade-offs, examples, conflict table
- Procedure.md - prerequisites, steps, verification, records
- _REFERENCES.md - metadata only; external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 4
- By document:
  - Datasheet: 0
  - Specification: 1
  - Guidance: 1
  - Procedure: 1
  - Multi: 1
  - NA: 0
- By matrix:
  - A: 0
  - B: 0
  - C: 1
  - F: 1
  - D: 1
  - X: 1
  - E: 0
- By type:
  - Conflict: 1
  - VerificationGap: 1
  - MissingSlot: 1
  - WeakStatement: 0
  - RationaleGap: 0
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | A lens normative/guiding (prescriptive direction) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | A lens normative/applying (mandatory practice) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | A lens normative/judging (compliance determination) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | A lens normative/reviewing (regulatory audit) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | A lens operative/guiding (procedural direction) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | A lens operative/applying (practical execution) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | A lens operative/judging (performance assessment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | A lens operative/reviewing (process audit) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | A lens evaluative/guiding (value orientation) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | A lens evaluative/applying (merit application) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | A lens evaluative/judging (worth determination) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | A lens evaluative/reviewing (quality appraisal) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | B lens data/necessity (essential fact) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | B lens data/sufficiency (adequate evidence) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | B lens data/completeness (comprehensive record) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | B lens data/consistency (reliable measurement) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | B lens information/necessity (essential signal) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | B lens information/sufficiency (adequate context) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | B lens information/completeness (comprehensive account) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | B lens information/consistency (coherent message) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | B lens knowledge/necessity (fundamental understanding) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | B lens knowledge/sufficiency (competent expertise) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | B lens knowledge/completeness (thorough mastery) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | B lens knowledge/consistency (coherent understanding) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | B lens wisdom/necessity (essential discernment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | B lens wisdom/sufficiency (adequate judgment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | B lens wisdom/completeness (holistic insight) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | B lens wisdom/consistency (principled reasoning) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding rationale | 0 | NO_ITEMS | C lens normative/necessity (binding rationale) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate warrant | 0 | NO_ITEMS | C lens normative/sufficiency (adequate warrant) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[normative]:[completeness] | normative | completeness | integral record | 0 | NO_ITEMS | C lens normative/completeness (integral record) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[normative]:[consistency] | normative | consistency | coherent standard | 0 | NO_ITEMS | C lens normative/consistency (coherent standard) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[operative]:[necessity] | operative | necessity | required action | 0 | NO_ITEMS | C lens operative/necessity (required action) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[operative]:[sufficiency] | operative | sufficiency | sufficient context | 0 | NO_ITEMS | C lens operative/sufficiency (sufficient context) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[operative]:[completeness] | operative | completeness | complete procedure | 0 | NO_ITEMS | C lens operative/completeness (complete procedure) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[operative]:[consistency] | operative | consistency | stable execution | 1 | HAS_ITEMS | Select a stable warning code or category taxonomy for dependency reader, writer, linter, API, and MCP warning output. |
| C:[evaluative]:[necessity] | evaluative | necessity | discerning criterion | 0 | NO_ITEMS | C lens evaluative/necessity (discerning criterion) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | balanced judgment | 0 | NO_ITEMS | C lens evaluative/sufficiency (balanced judgment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[evaluative]:[completeness] | evaluative | completeness | holistic appraisal | 0 | NO_ITEMS | C lens evaluative/completeness (holistic appraisal) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| C:[evaluative]:[consistency] | evaluative | consistency | principled coherence | 0 | NO_ITEMS | C lens evaluative/consistency (principled coherence) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[consistency] | TBD_Question | Multi | TBD | Select a stable warning code or category taxonomy for dependency reader, writer, linter, API, and MCP warning output. | Specification requires structured warnings and Guidance says warning categories should be stable once selected, while Procedure records the warning code taxonomy as TBD. Stable execution cannot be fully tested until the vocabulary is chosen. | Specification.md; Guidance.md; Procedure.md | Specification.md#Scope; Specification.md#Requirements; Guidance.md#Considerations; Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | enforceable prerequisite | 0 | NO_ITEMS | F lens normative/necessity (enforceable prerequisite) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[normative]:[sufficiency] | normative | sufficiency | justified mandate | 0 | NO_ITEMS | F lens normative/sufficiency (justified mandate) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[normative]:[completeness] | normative | completeness | comprehensive control | 0 | NO_ITEMS | F lens normative/completeness (comprehensive control) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[normative]:[consistency] | normative | consistency | stable obligation | 1 | HAS_ITEMS | Resolve or explicitly preserve the PRD hash-mismatch warning before accepting PRD-derived dependency warning and lifecycle language. |
| F:[operative]:[necessity] | operative | necessity | actionable prerequisite | 0 | NO_ITEMS | F lens operative/necessity (actionable prerequisite) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[operative]:[sufficiency] | operative | sufficiency | contextual capability | 0 | NO_ITEMS | F lens operative/sufficiency (contextual capability) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[operative]:[completeness] | operative | completeness | complete workflow | 0 | NO_ITEMS | F lens operative/completeness (complete workflow) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[operative]:[consistency] | operative | consistency | reliable practice | 0 | NO_ITEMS | F lens operative/consistency (reliable practice) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[evaluative]:[necessity] | evaluative | necessity | value threshold | 0 | NO_ITEMS | F lens evaluative/necessity (value threshold) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | reasoned adequacy | 0 | NO_ITEMS | F lens evaluative/sufficiency (reasoned adequacy) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[evaluative]:[completeness] | evaluative | completeness | holistic criterion | 0 | NO_ITEMS | F lens evaluative/completeness (holistic criterion) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| F:[evaluative]:[consistency] | evaluative | consistency | principled alignment | 0 | NO_ITEMS | F lens evaluative/consistency (principled alignment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[consistency] | Conflict | Guidance | NA | Resolve or explicitly preserve the PRD hash-mismatch warning before accepting PRD-derived dependency warning and lifecycle language. | Guidance records that PRD Section 8.9 is used for acceptance language while _REFERENCES.md marks docs/PRD.md as HASH_MISMATCH. The register can surface the reliance conflict, but the task cannot decide accepted source truth. | Guidance.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governed direction | 0 | NO_ITEMS | D lens normative/guiding (governed direction) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[normative]:[applying] | normative | applying | enforceable practice | 0 | NO_ITEMS | D lens normative/applying (enforceable practice) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[normative]:[judging] | normative | judging | binding determination | 0 | NO_ITEMS | D lens normative/judging (binding determination) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[normative]:[reviewing] | normative | reviewing | accountable review | 0 | NO_ITEMS | D lens normative/reviewing (accountable review) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[operative]:[guiding] | operative | guiding | actionable direction | 1 | HAS_ITEMS | Record selected implementation module names, API handler names, fixture paths, and test paths once local code ownership chooses them. |
| D:[operative]:[applying] | operative | applying | disciplined execution | 0 | NO_ITEMS | D lens operative/applying (disciplined execution) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[operative]:[judging] | operative | judging | measured performance | 0 | NO_ITEMS | D lens operative/judging (measured performance) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[operative]:[reviewing] | operative | reviewing | process oversight | 0 | NO_ITEMS | D lens operative/reviewing (process oversight) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[evaluative]:[guiding] | evaluative | guiding | value compass | 0 | NO_ITEMS | D lens evaluative/guiding (value compass) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[evaluative]:[applying] | evaluative | applying | merit enactment | 0 | NO_ITEMS | D lens evaluative/applying (merit enactment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[evaluative]:[judging] | evaluative | judging | reasoned judgment | 0 | NO_ITEMS | D lens evaluative/judging (reasoned judgment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality scrutiny | 0 | NO_ITEMS | D lens evaluative/reviewing (quality scrutiny) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[guiding] | MissingSlot | Procedure | Procedure | Record selected implementation module names, API handler names, fixture paths, and test paths once local code ownership chooses them. | Specification and Procedure both leave concrete module, handler, fixture, and payload naming as TBD. The action pathway is defined, but later execution evidence needs a placement slot for the selected paths. | Specification.md; Procedure.md | Specification.md#Verification; Specification.md#Documentation; Procedure.md#Steps; Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | directive threshold | 0 | NO_ITEMS | X lens guiding/necessity (directive threshold) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | evidentiary warrant | 0 | NO_ITEMS | X lens guiding/sufficiency (evidentiary warrant) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[guiding]:[completeness] | guiding | completeness | coverage frame | 0 | NO_ITEMS | X lens guiding/completeness (coverage frame) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[guiding]:[consistency] | guiding | consistency | reliability posture | 0 | NO_ITEMS | X lens guiding/consistency (reliability posture) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[applying]:[necessity] | applying | necessity | practice threshold | 0 | NO_ITEMS | X lens applying/necessity (practice threshold) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[applying]:[sufficiency] | applying | sufficiency | contextual readiness | 0 | NO_ITEMS | X lens applying/sufficiency (contextual readiness) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[applying]:[completeness] | applying | completeness | workflow coverage | 0 | NO_ITEMS | X lens applying/completeness (workflow coverage) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[applying]:[consistency] | applying | consistency | execution coherence | 0 | NO_ITEMS | X lens applying/consistency (execution coherence) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[judging]:[necessity] | judging | necessity | decision threshold | 0 | NO_ITEMS | X lens judging/necessity (decision threshold) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[judging]:[sufficiency] | judging | sufficiency | assessment warrant | 1 | HAS_ITEMS | Add acceptance evidence mapping for API/MCP dependency read-write payloads and governed write-hook behavior after concrete surfaces are selected. |
| X:[judging]:[completeness] | judging | completeness | determination coverage | 0 | NO_ITEMS | X lens judging/completeness (determination coverage) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[judging]:[consistency] | judging | consistency | appraisal coherence | 0 | NO_ITEMS | X lens judging/consistency (appraisal coherence) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit threshold | 0 | NO_ITEMS | X lens reviewing/necessity (audit threshold) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | evidence readiness | 0 | NO_ITEMS | X lens reviewing/sufficiency (evidence readiness) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[reviewing]:[completeness] | reviewing | completeness | review coverage | 0 | NO_ITEMS | X lens reviewing/completeness (review coverage) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| X:[reviewing]:[consistency] | reviewing | consistency | audit coherence | 0 | NO_ITEMS | X lens reviewing/consistency (audit coherence) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Add acceptance evidence mapping for API/MCP dependency read-write payloads and governed write-hook behavior after concrete surfaces are selected. | Specification requires API tests, MCP/tool integration tests, and hook/containment verification, but exact payload type names and local code surfaces remain TBD. Evidence sufficiency is therefore pending a concrete mapping. | Specification.md; Procedure.md | Specification.md#Verification; Specification.md#Documentation; Procedure.md#Steps; Procedure.md#Verification |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | directive facts | 0 | NO_ITEMS | E lens guiding/data (directive facts) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[guiding]:[information] | guiding | information | signal warrant | 0 | NO_ITEMS | E lens guiding/information (signal warrant) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding frame | 0 | NO_ITEMS | E lens guiding/knowledge (understanding frame) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[guiding]:[wisdom] | guiding | wisdom | discerning rationale | 0 | NO_ITEMS | E lens guiding/wisdom (discerning rationale) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[applying]:[data] | applying | data | practice facts | 0 | NO_ITEMS | E lens applying/data (practice facts) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[applying]:[information] | applying | information | context readiness | 0 | NO_ITEMS | E lens applying/information (context readiness) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[applying]:[knowledge] | applying | knowledge | expertise workflow | 0 | NO_ITEMS | E lens applying/knowledge (expertise workflow) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[applying]:[wisdom] | applying | wisdom | judgment enactment | 0 | NO_ITEMS | E lens applying/wisdom (judgment enactment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[judging]:[data] | judging | data | decision evidence | 0 | NO_ITEMS | E lens judging/data (decision evidence) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[judging]:[information] | judging | information | message assessment | 0 | NO_ITEMS | E lens judging/information (message assessment) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[judging]:[knowledge] | judging | knowledge | mastery determination | 0 | NO_ITEMS | E lens judging/knowledge (mastery determination) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[judging]:[wisdom] | judging | wisdom | reasoning appraisal | 0 | NO_ITEMS | E lens judging/wisdom (reasoning appraisal) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[reviewing]:[data] | reviewing | data | audit record | 0 | NO_ITEMS | E lens reviewing/data (audit record) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[reviewing]:[information] | reviewing | information | message oversight | 0 | NO_ITEMS | E lens reviewing/information (message oversight) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery scrutiny | 0 | NO_ITEMS | E lens reviewing/knowledge (mastery scrutiny) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | insight appraisal | 0 | NO_ITEMS | E lens reviewing/wisdom (insight appraisal) left schema, lifecycle, provenance, target-resolution, and tool-surface text aligned for this setup pass. |
