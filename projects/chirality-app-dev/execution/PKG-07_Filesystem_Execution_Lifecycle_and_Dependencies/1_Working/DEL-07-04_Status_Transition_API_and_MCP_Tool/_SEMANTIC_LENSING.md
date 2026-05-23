# Semantic Lensing Register: DEL-07-04 Status Transition API and MCP Tool

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-04_Status_Transition_API_and_MCP_Tool
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py passed after generation
**Warnings:** docs/PRD.md is listed as HASH_MISMATCH in _REFERENCES.md; PRD-derived acceptance details remain warned source material.

**Inputs Read:**
- _CONTEXT.md - read
- _STATUS.md - read
- _SEMANTIC.md - read
- Datasheet.md - read
- Specification.md - read
- Guidance.md - read
- Procedure.md - read
- _REFERENCES.md - read

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 12
- By document:
  - Datasheet: 0
  - Specification: 4
  - Guidance: 3
  - Procedure: 4
  - Multi: 1
  - NA: 0
- By matrix:
  - A: 0
  - B: 2
  - C: 1
  - F: 2
  - D: 2
  - X: 2
  - E: 3
- By type:
  - Conflict: 0
  - VerificationGap: 4
  - MissingSlot: 4
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 1
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 0
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | reliable measurement lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for comprehensive account. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for coherent understanding. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[information]:[completeness] | MissingSlot | Specification | Specification | Define exact status read and transition request/response payload schemas. | Specification names the API endpoints and records the exact payload schemas as TBD, leaving the information-completeness lens open for implementation. | Specification.md | Documentation |  | PROPOSAL | TBD |
| B-002 | B:[knowledge]:[consistency] | MissingSlot | Specification | Specification | Define the runtime actor identity enum or mapping used for transition authorization. | Specification requires actor authorization but keeps the exact actor identity enum or policy mapping as TBD, creating a consistency gap between rule and implementation surface. | Specification.md | Documentation |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding rationale | 0 | NO_ITEMS | binding rationale lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[normative]:[sufficiency] | normative | sufficiency | adequate warrant | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for adequate warrant. |
| C:[normative]:[completeness] | normative | completeness | integral record | 0 | NO_ITEMS | integral record lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[normative]:[consistency] | normative | consistency | coherent standard | 0 | NO_ITEMS | coherent standard lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[operative]:[necessity] | operative | necessity | required action | 0 | NO_ITEMS | required action lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[operative]:[sufficiency] | operative | sufficiency | sufficient context | 0 | NO_ITEMS | sufficient context lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[operative]:[completeness] | operative | completeness | complete procedure | 0 | NO_ITEMS | complete procedure lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[operative]:[consistency] | operative | consistency | stable execution | 0 | NO_ITEMS | stable execution lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[evaluative]:[necessity] | evaluative | necessity | discerning criterion | 0 | NO_ITEMS | discerning criterion lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | balanced judgment | 0 | NO_ITEMS | balanced judgment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[evaluative]:[completeness] | evaluative | completeness | holistic appraisal | 0 | NO_ITEMS | holistic appraisal lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| C:[evaluative]:[consistency] | evaluative | consistency | principled coherence | 0 | NO_ITEMS | principled coherence lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[sufficiency] | RationaleGap | Guidance | Guidance | Record how alternate immutable approval evidence would be authorized if not using a git SHA-like token. | Guidance prefers strict SHA-like validation but allows deliberate policy extension for alternate immutable evidence without naming the approval path for that extension. | Guidance.md | Trade-offs |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | enforceable prerequisite | 0 | NO_ITEMS | enforceable prerequisite lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[normative]:[sufficiency] | normative | sufficiency | justified mandate | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for justified mandate. |
| F:[normative]:[completeness] | normative | completeness | comprehensive control | 0 | NO_ITEMS | comprehensive control lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[normative]:[consistency] | normative | consistency | stable obligation | 0 | NO_ITEMS | stable obligation lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[operative]:[necessity] | operative | necessity | actionable prerequisite | 0 | NO_ITEMS | actionable prerequisite lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[operative]:[sufficiency] | operative | sufficiency | contextual capability | 0 | NO_ITEMS | contextual capability lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[operative]:[completeness] | operative | completeness | complete workflow | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for complete workflow. |
| F:[operative]:[consistency] | operative | consistency | reliable practice | 0 | NO_ITEMS | reliable practice lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[evaluative]:[necessity] | evaluative | necessity | value threshold | 0 | NO_ITEMS | value threshold lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | reasoned adequacy | 0 | NO_ITEMS | reasoned adequacy lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[evaluative]:[completeness] | evaluative | completeness | holistic criterion | 0 | NO_ITEMS | holistic criterion lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| F:[evaluative]:[consistency] | evaluative | consistency | principled alignment | 0 | NO_ITEMS | principled alignment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Add an acceptance check that PRD HASH_MISMATCH is reconciled before PRD-derived SHA criteria are final. | Specification retains PRD-derived approval SHA requirements while warning that the PRD source hash is mismatched, so the warrant for final acceptance needs an explicit reconciliation check. | Specification.md | Source Warning |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[completeness] | VerificationGap | Procedure | Procedure | Add verification coverage for exact request/response schema fixtures after schemas are accepted. | Procedure requires API route behavior and structured outcomes, but exact response schema remains TBD, leaving complete workflow verification under-specified. | Procedure.md | Steps |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governed direction | 0 | NO_ITEMS | governed direction lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[normative]:[applying] | normative | applying | enforceable practice | 0 | NO_ITEMS | enforceable practice lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[normative]:[judging] | normative | judging | binding determination | 0 | NO_ITEMS | binding determination lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[normative]:[reviewing] | normative | reviewing | accountable review | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for accountable review. |
| D:[operative]:[guiding] | operative | guiding | actionable direction | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for actionable direction. |
| D:[operative]:[applying] | operative | applying | disciplined execution | 0 | NO_ITEMS | disciplined execution lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[operative]:[judging] | operative | judging | measured performance | 0 | NO_ITEMS | measured performance lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[operative]:[reviewing] | operative | reviewing | process oversight | 0 | NO_ITEMS | process oversight lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[evaluative]:[guiding] | evaluative | guiding | value compass | 0 | NO_ITEMS | value compass lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[evaluative]:[applying] | evaluative | applying | merit enactment | 0 | NO_ITEMS | merit enactment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[evaluative]:[judging] | evaluative | judging | reasoned judgment | 0 | NO_ITEMS | reasoned judgment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality scrutiny | 0 | NO_ITEMS | quality scrutiny lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[guiding] | TBD_Question | Procedure | Procedure | Implementation owner must identify the module path for working-root deliverable APIs and Chirality MCP tools. | Procedure starts with locating the implementation area and records implementation module location as TBD, so actionable direction is not yet closed. | Procedure.md | Prerequisites |  | PROPOSAL | TBD |
| D-002 | D:[normative]:[reviewing] | VerificationGap | Guidance | Guidance | Define review evidence proving runtime/event records are not treated as human approval records. | Guidance states runtime and event records are not substitutes for human approval, but does not define the review evidence for that accountable review. | Guidance.md | Considerations |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | directive threshold | 0 | NO_ITEMS | directive threshold lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | evidentiary warrant | 0 | NO_ITEMS | evidentiary warrant lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[guiding]:[completeness] | guiding | completeness | coverage frame | 0 | NO_ITEMS | coverage frame lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[guiding]:[consistency] | guiding | consistency | reliability posture | 0 | NO_ITEMS | reliability posture lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[applying]:[necessity] | applying | necessity | practice threshold | 0 | NO_ITEMS | practice threshold lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[applying]:[sufficiency] | applying | sufficiency | contextual readiness | 0 | NO_ITEMS | contextual readiness lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[applying]:[completeness] | applying | completeness | workflow coverage | 0 | NO_ITEMS | workflow coverage lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[applying]:[consistency] | applying | consistency | execution coherence | 0 | NO_ITEMS | execution coherence lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[judging]:[necessity] | judging | necessity | decision threshold | 0 | NO_ITEMS | decision threshold lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[judging]:[sufficiency] | judging | sufficiency | assessment warrant | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for assessment warrant. |
| X:[judging]:[completeness] | judging | completeness | determination coverage | 0 | NO_ITEMS | determination coverage lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[judging]:[consistency] | judging | consistency | appraisal coherence | 0 | NO_ITEMS | appraisal coherence lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit threshold | 0 | NO_ITEMS | audit threshold lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | evidence readiness | 0 | NO_ITEMS | evidence readiness lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| X:[reviewing]:[completeness] | reviewing | completeness | review coverage | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for review coverage. |
| X:[reviewing]:[consistency] | reviewing | consistency | audit coherence | 0 | NO_ITEMS | audit coherence lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Add test assertion shape for denial reasons: invalid state, backward transition, unauthorized actor, missing/invalid approval SHA, policy/path denial, and malformed status file. | Guidance calls for structured denial information across these cases while Specification verification lists coverage at a higher level, leaving assessment warrant details open. | Guidance.md; Specification.md | Guidance.md#Considerations; Specification.md#Verification |  | PROPOSAL | TBD |
| X-002 | X:[reviewing]:[completeness] | MissingSlot | Procedure | Procedure | Record audit evidence expectations for permission, hook, path, redaction, and event logging policy on MCP status operations. | Procedure requires MCP status tools to route through shared policy overlays, but record artifacts for proving each overlay are only described generally. | Procedure.md | Records |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | directive facts | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for directive facts. |
| E:[guiding]:[information] | guiding | information | signal warrant | 0 | NO_ITEMS | signal warrant lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding frame | 0 | NO_ITEMS | understanding frame lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[guiding]:[wisdom] | guiding | wisdom | discerning rationale | 0 | NO_ITEMS | discerning rationale lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[applying]:[data] | applying | data | practice facts | 0 | NO_ITEMS | practice facts lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[applying]:[information] | applying | information | context readiness | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for context readiness. |
| E:[applying]:[knowledge] | applying | knowledge | expertise workflow | 0 | NO_ITEMS | expertise workflow lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[applying]:[wisdom] | applying | wisdom | judgment enactment | 0 | NO_ITEMS | judgment enactment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[judging]:[data] | judging | data | decision evidence | 0 | NO_ITEMS | decision evidence lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[judging]:[information] | judging | information | message assessment | 0 | NO_ITEMS | message assessment lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[judging]:[knowledge] | judging | knowledge | mastery determination | 0 | NO_ITEMS | mastery determination lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[judging]:[wisdom] | judging | wisdom | reasoning appraisal | 0 | NO_ITEMS | reasoning appraisal lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[reviewing]:[data] | reviewing | data | audit record | 0 | NO_ITEMS | audit record lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[reviewing]:[information] | reviewing | information | message oversight | 1 | HAS_ITEMS | Register records 1 warranted enrichment item(s) for message oversight. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery scrutiny | 0 | NO_ITEMS | mastery scrutiny lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | insight appraisal | 0 | NO_ITEMS | insight appraisal lens was checked against status parser, lifecycle, API, MCP, and approval-gate documents with no distinct warranted register item. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[data] | Normalization | Multi | Guidance | Normalize decomposition variant spelling between SOFTWARE and SOFTWARE_DECOMP in generated and production artifacts. | The runtime override uses DECOMP_VARIANT=SOFTWARE while Datasheet identification records DecompositionVariant as SOFTWARE_DECOMP; this can confuse downstream tools if not normalized as context versus runtime token. | Datasheet.md; _SEMANTIC_LENSING.md | Datasheet.md#Identification; register header |  | PROPOSAL | TBD |
| E-002 | E:[applying]:[information] | MissingSlot | Procedure | Procedure | Define caller-facing transition success and denial payload fields once API/MCP schema is accepted. | Procedure asks for structured success and denial outcomes but leaves exact request/response schemas as TBD, limiting context readiness for implementers. | Procedure.md | Steps |  | PROPOSAL | TBD |
| E-003 | E:[reviewing]:[information] | TBD_Question | Guidance | Guidance | Human or implementation owner should decide whether PRD HASH_MISMATCH blocks implementation, final acceptance, or only PRD-specific acceptance claims. | Multiple documents preserve the hash mismatch warning but do not state its governance effect, leaving message oversight unresolved. | Datasheet.md; Specification.md; Guidance.md; Procedure.md | Source Warning / Conditions |  | PROPOSAL | TBD |
