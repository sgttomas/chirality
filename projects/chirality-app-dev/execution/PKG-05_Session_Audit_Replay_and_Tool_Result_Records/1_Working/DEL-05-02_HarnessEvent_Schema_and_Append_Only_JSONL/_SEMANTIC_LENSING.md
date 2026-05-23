# Semantic Lensing Register: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py completed successfully
**Warnings:** none

**Inputs Read:**
- _CONTEXT.md - _CONTEXT.md#identity
- _STATUS.md - _STATUS.md#history
- _SEMANTIC.md - _SEMANTIC.md
- Datasheet.md - Datasheet.md#attributes
- Specification.md - Specification.md#requirements
- Guidance.md - Guidance.md#principles
- Procedure.md - Procedure.md#steps
- _REFERENCES.md - _REFERENCES.md#authoritative-source-corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 7
- By document:
  - Datasheet: 0
  - Specification: 2
  - Guidance: 1
  - Procedure: 3
  - Multi: 0
  - NA: 1
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
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/guiding. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | mandatory practice was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/applying. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/judging. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/reviewing. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/guiding. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | practical execution was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/applying. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/judging. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | process audit was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/reviewing. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/guiding. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | merit application was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/applying. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/judging. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/reviewing. |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | essential fact was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for data/necessity. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for data/sufficiency. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for data/completeness. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to reliable measurement. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | essential signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for information/necessity. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for information/sufficiency. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for information/completeness. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | coherent message was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for information/consistency. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for knowledge/necessity. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for knowledge/sufficiency. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for knowledge/completeness. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for knowledge/consistency. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for wisdom/necessity. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for wisdom/sufficiency. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for wisdom/completeness. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for wisdom/consistency. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[consistency] | Conflict | Multi | NA | Resolve whether PRD-derived runtime requirements remain corroborating-only until REF-006 hash mismatch is reconciled. | The production set uses PRD text only where aligned with matching SPEC/CONTRACT/TYPES evidence, while _REFERENCES records REF-006 as HASH_MISMATCH; the source-state warning is a governance conflict that remains human-ruled. | _REFERENCES.md; Guidance.md | _REFERENCES.md#authoritative-source-corpus; Guidance.md#conflict-table-for-human-ruling | _REFERENCES.md#REF-006; Guidance.md#SOURCE-WARN-001 | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | binding audit basis | 0 | NO_ITEMS | binding audit basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/necessity. |
| C:[normative]:[sufficiency] | normative | sufficiency | enforceable evidence frame | 0 | NO_ITEMS | enforceable evidence frame was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/sufficiency. |
| C:[normative]:[completeness] | normative | completeness | complete control record | 0 | NO_ITEMS | complete control record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/completeness. |
| C:[normative]:[consistency] | normative | consistency | coherent governance signal | 0 | NO_ITEMS | coherent governance signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/consistency. |
| C:[operative]:[necessity] | operative | necessity | execution readiness basis | 0 | NO_ITEMS | execution readiness basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/necessity. |
| C:[operative]:[sufficiency] | operative | sufficiency | adequate workflow evidence | 0 | NO_ITEMS | adequate workflow evidence was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/sufficiency. |
| C:[operative]:[completeness] | operative | completeness | complete runtime account | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to complete runtime account. |
| C:[operative]:[consistency] | operative | consistency | stable process message | 0 | NO_ITEMS | stable process message was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/consistency. |
| C:[evaluative]:[necessity] | evaluative | necessity | value evidence basis | 0 | NO_ITEMS | value evidence basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/necessity. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | justified appraisal context | 0 | NO_ITEMS | justified appraisal context was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/sufficiency. |
| C:[evaluative]:[completeness] | evaluative | completeness | complete merit account | 0 | NO_ITEMS | complete merit account was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/completeness. |
| C:[evaluative]:[consistency] | evaluative | consistency | coherent quality rationale | 0 | NO_ITEMS | coherent quality rationale was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/consistency. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[operative]:[completeness] | MissingSlot | Procedure | Procedure | Record accepted upstream and downstream dependency edges once dependency extraction is accepted. | Procedure prerequisites currently state both declared upstream and downstream dependencies are TBD, leaving the runtime account incomplete for phase handoff and replay sequencing. | Procedure.md | Procedure.md#prerequisites |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | obligatory record criteria | 0 | NO_ITEMS | obligatory record criteria was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/necessity. |
| F:[normative]:[sufficiency] | normative | sufficiency | sufficient control proof | 0 | NO_ITEMS | sufficient control proof was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/sufficiency. |
| F:[normative]:[completeness] | normative | completeness | complete compliance dossier | 0 | NO_ITEMS | complete compliance dossier was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/completeness. |
| F:[normative]:[consistency] | normative | consistency | consistent governance rationale | 0 | NO_ITEMS | consistent governance rationale was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/consistency. |
| F:[operative]:[necessity] | operative | necessity | required execution evidence | 0 | NO_ITEMS | required execution evidence was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/necessity. |
| F:[operative]:[sufficiency] | operative | sufficiency | sufficient runtime context | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to sufficient runtime context. |
| F:[operative]:[completeness] | operative | completeness | complete process trace | 0 | NO_ITEMS | complete process trace was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/completeness. |
| F:[operative]:[consistency] | operative | consistency | consistent workflow account | 0 | NO_ITEMS | consistent workflow account was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/consistency. |
| F:[evaluative]:[necessity] | evaluative | necessity | required appraisal basis | 0 | NO_ITEMS | required appraisal basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/necessity. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | sufficient judgment context | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to sufficient judgment context. |
| F:[evaluative]:[completeness] | evaluative | completeness | complete quality rationale | 0 | NO_ITEMS | complete quality rationale was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/completeness. |
| F:[evaluative]:[consistency] | evaluative | consistency | consistent merit argument | 0 | NO_ITEMS | consistent merit argument was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/consistency. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[sufficiency] | TBD_Question | Procedure | Procedure | Identify owner and accepted threshold source for large payload artifact references before implementation tests assert a numeric limit. | Procedure and Guidance require large payloads to be stored as artifacts, but defer threshold and storage policy to DEL-05-05 unless already established. | Procedure.md; Guidance.md | Procedure.md#steps; Guidance.md#considerations |  | PROPOSAL | TBD |
| F-002 | F:[evaluative]:[sufficiency] | TBD_Question | Specification | Specification | Identify which redaction helper or fixture contract DEL-05-03 will provide for secret-safety verification. | Specification verification labels detailed redaction helper tests as owned by DEL-05-03, so sufficiency of the judgment context depends on an adjacent deliverable contract. | Specification.md | Specification.md#verification |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | binding direction closure | 0 | NO_ITEMS | binding direction closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/guiding. |
| D:[normative]:[applying] | normative | applying | enforceable practice closure | 0 | NO_ITEMS | enforceable practice closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/applying. |
| D:[normative]:[judging] | normative | judging | compliance verdict closure | 0 | NO_ITEMS | compliance verdict closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/judging. |
| D:[normative]:[reviewing] | normative | reviewing | audit assurance closure | 0 | NO_ITEMS | audit assurance closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for normative/reviewing. |
| D:[operative]:[guiding] | operative | guiding | procedural readiness closure | 0 | NO_ITEMS | procedural readiness closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/guiding. |
| D:[operative]:[applying] | operative | applying | execution control closure | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to execution control closure. |
| D:[operative]:[judging] | operative | judging | performance evidence closure | 0 | NO_ITEMS | performance evidence closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/judging. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance closure | 0 | NO_ITEMS | process assurance closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for operative/reviewing. |
| D:[evaluative]:[guiding] | evaluative | guiding | value alignment closure | 0 | NO_ITEMS | value alignment closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/guiding. |
| D:[evaluative]:[applying] | evaluative | applying | merit practice closure | 0 | NO_ITEMS | merit practice closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/applying. |
| D:[evaluative]:[judging] | evaluative | judging | worth judgment closure | 0 | NO_ITEMS | worth judgment closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/judging. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality assurance closure | 0 | NO_ITEMS | quality assurance closure was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for evaluative/reviewing. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | MissingSlot | Procedure | Procedure | Mark event-type-specific payload schemas as TBD until accepted source or implementation defines each category payload. | Procedure directs unresolved implementation choices to mark event payload schemas by type as TBD, which is an explicit missing slot for execution closure. | Procedure.md | Procedure.md#steps |  | PROPOSAL | TBD |

## Matrix X - Verification

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | directive evidence basis | 0 | NO_ITEMS | directive evidence basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/necessity. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | adequate direction proof | 0 | NO_ITEMS | adequate direction proof was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/sufficiency. |
| X:[guiding]:[completeness] | guiding | completeness | complete guidance record | 0 | NO_ITEMS | complete guidance record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/completeness. |
| X:[guiding]:[consistency] | guiding | consistency | coherent direction signal | 0 | NO_ITEMS | coherent direction signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/consistency. |
| X:[applying]:[necessity] | applying | necessity | practice evidence basis | 0 | NO_ITEMS | practice evidence basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/necessity. |
| X:[applying]:[sufficiency] | applying | sufficiency | adequate execution proof | 0 | NO_ITEMS | adequate execution proof was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/sufficiency. |
| X:[applying]:[completeness] | applying | completeness | complete practice record | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to complete practice record. |
| X:[applying]:[consistency] | applying | consistency | coherent application signal | 0 | NO_ITEMS | coherent application signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/consistency. |
| X:[judging]:[necessity] | judging | necessity | verdict evidence basis | 0 | NO_ITEMS | verdict evidence basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/necessity. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate assessment proof | 0 | NO_ITEMS | adequate assessment proof was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/sufficiency. |
| X:[judging]:[completeness] | judging | completeness | complete judgment record | 0 | NO_ITEMS | complete judgment record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/completeness. |
| X:[judging]:[consistency] | judging | consistency | coherent verdict signal | 0 | NO_ITEMS | coherent verdict signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/consistency. |
| X:[reviewing]:[necessity] | reviewing | necessity | assurance evidence basis | 0 | NO_ITEMS | assurance evidence basis was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/necessity. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | adequate audit proof | 0 | NO_ITEMS | adequate audit proof was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/sufficiency. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete review record | 0 | NO_ITEMS | complete review record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/completeness. |
| X:[reviewing]:[consistency] | reviewing | consistency | coherent assurance signal | 0 | NO_ITEMS | coherent assurance signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/consistency. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[applying]:[completeness] | VerificationGap | Specification | Specification | Add fixture coverage plan for later tool, hook, compaction, subagent, and SDK mirror event categories when their owning deliverables mature. | Datasheet lists later event categories and Procedure keeps them representable, but current required artifacts focus on initial categories and do not define later-category fixtures. | Datasheet.md; Procedure.md; Specification.md | Datasheet.md#attributes; Procedure.md#steps; Specification.md#documentation |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | directive fact record | 0 | NO_ITEMS | directive fact record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/data. |
| E:[guiding]:[information] | guiding | information | contextual direction signal | 0 | NO_ITEMS | contextual direction signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/information. |
| E:[guiding]:[knowledge] | guiding | knowledge | understood guidance model | 0 | NO_ITEMS | understood guidance model was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for guiding/knowledge. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled direction rationale | 1 | HAS_ITEMS | This lens surfaces 1 warranted item(s) tied to principled direction rationale. |
| E:[applying]:[data] | applying | data | practice fact record | 0 | NO_ITEMS | practice fact record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/data. |
| E:[applying]:[information] | applying | information | contextual execution signal | 0 | NO_ITEMS | contextual execution signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/information. |
| E:[applying]:[knowledge] | applying | knowledge | understood practice model | 0 | NO_ITEMS | understood practice model was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/knowledge. |
| E:[applying]:[wisdom] | applying | wisdom | principled application rationale | 0 | NO_ITEMS | principled application rationale was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for applying/wisdom. |
| E:[judging]:[data] | judging | data | verdict fact record | 0 | NO_ITEMS | verdict fact record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/data. |
| E:[judging]:[information] | judging | information | contextual assessment signal | 0 | NO_ITEMS | contextual assessment signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/information. |
| E:[judging]:[knowledge] | judging | knowledge | understood judgment model | 0 | NO_ITEMS | understood judgment model was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/knowledge. |
| E:[judging]:[wisdom] | judging | wisdom | principled verdict rationale | 0 | NO_ITEMS | principled verdict rationale was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for judging/wisdom. |
| E:[reviewing]:[data] | reviewing | data | assurance fact record | 0 | NO_ITEMS | assurance fact record was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/data. |
| E:[reviewing]:[information] | reviewing | information | contextual audit signal | 0 | NO_ITEMS | contextual audit signal was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/information. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | understood review model | 0 | NO_ITEMS | understood review model was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/knowledge. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled assurance rationale | 0 | NO_ITEMS | principled assurance rationale was checked against the deliverable documents; no distinct gap, conflict, or TBD beyond recorded items was found for reviewing/wisdom. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[wisdom] | RationaleGap | Guidance | Guidance | Explain why append-only JSONL is sufficient for interrupted-write recovery beyond malformed-tail tolerance. | Guidance states malformed-tail tolerance matters but does not give the decision rationale connecting append-only writes, diagnostics, and replay recovery boundaries. | Guidance.md | Guidance.md#considerations |  | PROPOSAL | TBD |

