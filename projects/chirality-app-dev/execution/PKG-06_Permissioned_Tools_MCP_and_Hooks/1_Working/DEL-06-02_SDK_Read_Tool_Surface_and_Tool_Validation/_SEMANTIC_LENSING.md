# Semantic Lensing Register: DEL-06-02 SDK Read Tool Surface and Tool Validation

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS — validate_lens_register.py

**Inputs Read:**
- _CONTEXT.md — `_CONTEXT.md#Identity`
- _STATUS.md — `_STATUS.md#History`
- _SEMANTIC.md — `_SEMANTIC.md`
- Datasheet.md — `Datasheet.md`
- Specification.md — `Specification.md`
- Guidance.md — `Guidance.md`
- Procedure.md — `Procedure.md`
- _REFERENCES.md — `_REFERENCES.md#Authoritative Source Corpus` (metadata only; external paths not followed)

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Current ADQ-11 Note (2026-06-21)

This generated 2026-05-20 lens is not regenerated here, but ADQ-11/D-APP-43 retires the active
source-state and runtime-fingerprint findings for current review. REF-006 `docs/PRD.md` is `MATCH`
under the D-APP-38 authority corpus v2, satisfying the source-state portions of `A-001`, `D-002`, and
`E-002`; `frontend/src/lib/harness/runtime-fingerprint.ts`,
`frontend/src/app/api/harness/session/boot/route.ts`, and the route tests satisfy `E-001` for the
runtime fingerprint path. Historical `HASH_MISMATCH` and path-`TBD` text below remains generation
provenance unless separately listed as still open in the active assessment.

## Summary

- Total warranted items: 12
- By document:
  - Datasheet: 0
  - Specification: 3
  - Guidance: 2
  - Procedure: 4
  - Multi: 3
  - NA: 0
- By matrix:
  - A: 1
  - B: 2
  - C: 2
  - F: 2
  - D: 2
  - X: 1
  - E: 2
- By type:
  - Conflict: 1
  - VerificationGap: 3
  - MissingSlot: 4
  - WeakStatement: 0
  - RationaleGap: 1
  - Normalization: 1
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A — Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Lens `prescriptive direction` was checked against scoped production text for normative / guiding without a separate enrichment input. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | Lens `mandatory practice` was checked against scoped production text for normative / applying without a separate enrichment input. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Lens `compliance determination` was checked against scoped production text for normative / judging without a separate enrichment input. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Lens `regulatory audit` surfaces 1 warranted register item(s) for normative / reviewing evidence. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Lens `procedural direction` was checked against scoped production text for operative / guiding without a separate enrichment input. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Lens `practical execution` was checked against scoped production text for operative / applying without a separate enrichment input. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Lens `performance assessment` was checked against scoped production text for operative / judging without a separate enrichment input. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Lens `process audit` was checked against scoped production text for operative / reviewing without a separate enrichment input. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Lens `value orientation` was checked against scoped production text for evaluative / guiding without a separate enrichment input. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Lens `merit application` was checked against scoped production text for evaluative / applying without a separate enrichment input. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Lens `worth determination` was checked against scoped production text for evaluative / judging without a separate enrichment input. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Lens `quality appraisal` was checked against scoped production text for evaluative / reviewing without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Keep PRD-derived claims warning-qualified until REF-006 hash state is reconciled. | The production set relies on PRD sections while `_REFERENCES.md` marks REF-006 as HASH_MISMATCH. The conflict table already leaves the human ruling open, so the register should preserve the unresolved source-state decision. | _REFERENCES.md; Guidance.md; Specification.md | _REFERENCES.md#Authoritative Source Corpus; Guidance.md#Conflict Table (for human ruling); Specification.md#Documentation | _REFERENCES.md#REF-006 HASH_MISMATCH; Guidance.md#Conflict Table (for human ruling); Specification.md#Scope PRD citations | PROPOSAL | TBD |

## Matrix B — Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | Lens `essential fact` was checked against scoped production text for data / necessity without a separate enrichment input. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Lens `adequate evidence` was checked against scoped production text for data / sufficiency without a separate enrichment input. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | Lens `comprehensive record` surfaces 1 warranted register item(s) for data / completeness evidence. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | Lens `reliable measurement` was checked against scoped production text for data / consistency without a separate enrichment input. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Lens `essential signal` was checked against scoped production text for information / necessity without a separate enrichment input. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | Lens `adequate context` was checked against scoped production text for information / sufficiency without a separate enrichment input. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | Lens `comprehensive account` was checked against scoped production text for information / completeness without a separate enrichment input. |
| B:[information]:[consistency] | information | consistency | coherent message | 1 | HAS_ITEMS | Lens `coherent message` surfaces 1 warranted register item(s) for information / consistency evidence. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Lens `fundamental understanding` was checked against scoped production text for knowledge / necessity without a separate enrichment input. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Lens `competent expertise` was checked against scoped production text for knowledge / sufficiency without a separate enrichment input. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Lens `thorough mastery` was checked against scoped production text for knowledge / completeness without a separate enrichment input. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Lens `coherent understanding` was checked against scoped production text for knowledge / consistency without a separate enrichment input. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Lens `essential discernment` was checked against scoped production text for wisdom / necessity without a separate enrichment input. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Lens `adequate judgment` was checked against scoped production text for wisdom / sufficiency without a separate enrichment input. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Lens `holistic insight` was checked against scoped production text for wisdom / completeness without a separate enrichment input. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Lens `principled reasoning` was checked against scoped production text for wisdom / consistency without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[completeness] | MissingSlot | Multi | TBD | Assign exact implementation, registry, resolver, metadata, and test fixture paths when implementation ownership is known. | The production documents repeatedly mark implementation file paths, registry path, metadata path, and test paths as TBD. Those absences affect the comprehensive record needed for later implementation and audit. | Datasheet.md; Procedure.md; Specification.md | Datasheet.md#Construction; Procedure.md#Records; Specification.md#Verification |  | PROPOSAL | TBD |
| B-002 | B:[information]:[consistency] | Normalization | Multi | Guidance | Normalize usage of read-first, read-only, and readOnly so mode posture and sequencing remain distinguishable. | The scoped documents use read-first sequencing language, read-only capability language, and the `readOnly` mode token in adjacent contexts. A later pass should keep these terms intentionally distinct rather than letting them collapse. | Datasheet.md; Specification.md; Guidance.md; Procedure.md | Datasheet.md#Conditions; Specification.md#Requirements; Guidance.md#Read-First Surface; Procedure.md#Steps |  | PROPOSAL | TBD |

## Matrix C — Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | registry mandate | 0 | NO_ITEMS | Lens `registry mandate` was checked against scoped production text for normative / necessity without a separate enrichment input. |
| C:[normative]:[sufficiency] | normative | sufficiency | validation threshold | 0 | NO_ITEMS | Lens `validation threshold` was checked against scoped production text for normative / sufficiency without a separate enrichment input. |
| C:[normative]:[completeness] | normative | completeness | exposure coverage | 1 | HAS_ITEMS | Lens `exposure coverage` surfaces 1 warranted register item(s) for normative / completeness evidence. |
| C:[normative]:[consistency] | normative | consistency | policy coherence | 0 | NO_ITEMS | Lens `policy coherence` was checked against scoped production text for normative / consistency without a separate enrichment input. |
| C:[operative]:[necessity] | operative | necessity | resolver prerequisite | 0 | NO_ITEMS | Lens `resolver prerequisite` was checked against scoped production text for operative / necessity without a separate enrichment input. |
| C:[operative]:[sufficiency] | operative | sufficiency | surface evidence | 1 | HAS_ITEMS | Lens `surface evidence` surfaces 1 warranted register item(s) for operative / sufficiency evidence. |
| C:[operative]:[completeness] | operative | completeness | ordering discipline | 0 | NO_ITEMS | Lens `ordering discipline` was checked against scoped production text for operative / completeness without a separate enrichment input. |
| C:[operative]:[consistency] | operative | consistency | runtime stability | 0 | NO_ITEMS | Lens `runtime stability` was checked against scoped production text for operative / consistency without a separate enrichment input. |
| C:[evaluative]:[necessity] | evaluative | necessity | boundary rationale | 0 | NO_ITEMS | Lens `boundary rationale` was checked against scoped production text for evaluative / necessity without a separate enrichment input. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | adequacy warrant | 0 | NO_ITEMS | Lens `adequacy warrant` was checked against scoped production text for evaluative / sufficiency without a separate enrichment input. |
| C:[evaluative]:[completeness] | evaluative | completeness | governance insight | 0 | NO_ITEMS | Lens `governance insight` was checked against scoped production text for evaluative / completeness without a separate enrichment input. |
| C:[evaluative]:[consistency] | evaluative | consistency | exposure appraisal | 0 | NO_ITEMS | Lens `exposure appraisal` was checked against scoped production text for evaluative / consistency without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[completeness] | VerificationGap | Specification | Specification | Tie exposure coverage requirements to concrete implementation evidence once file and fixture paths exist. | Specification requires resolver evidence, registry evidence, deterministic ordering fixtures, and read-first tests, but exact evidence locations remain TBD. The exposure-coverage lens makes the missing verification anchors salient. | Specification.md; Procedure.md | Specification.md#Documentation; Procedure.md#Records |  | PROPOSAL | TBD |
| C-002 | C:[operative]:[sufficiency] | MissingSlot | Procedure | Procedure | Define the exact structured validation error type and fixture assertion shape for unknown tool names. | Guidance and Procedure require structured validation errors for unknown tools, but the exact error type is still TBD. Without that slot, surface evidence for unknown-tool rejection is incomplete. | Guidance.md; Procedure.md | Guidance.md#Resolver Shape; Procedure.md#Steps |  | PROPOSAL | TBD |

## Matrix F — Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | authority registry | 0 | NO_ITEMS | Lens `authority registry` was checked against scoped production text for normative / necessity without a separate enrichment input. |
| F:[normative]:[sufficiency] | normative | sufficiency | evidence gate | 0 | NO_ITEMS | Lens `evidence gate` was checked against scoped production text for normative / sufficiency without a separate enrichment input. |
| F:[normative]:[completeness] | normative | completeness | coverage closure | 0 | NO_ITEMS | Lens `coverage closure` was checked against scoped production text for normative / completeness without a separate enrichment input. |
| F:[normative]:[consistency] | normative | consistency | coherence rule | 0 | NO_ITEMS | Lens `coherence rule` was checked against scoped production text for normative / consistency without a separate enrichment input. |
| F:[operative]:[necessity] | operative | necessity | input precondition | 1 | HAS_ITEMS | Lens `input precondition` surfaces 1 warranted register item(s) for operative / necessity evidence. |
| F:[operative]:[sufficiency] | operative | sufficiency | context warrant | 0 | NO_ITEMS | Lens `context warrant` was checked against scoped production text for operative / sufficiency without a separate enrichment input. |
| F:[operative]:[completeness] | operative | completeness | fixture coverage | 1 | HAS_ITEMS | Lens `fixture coverage` surfaces 1 warranted register item(s) for operative / completeness evidence. |
| F:[operative]:[consistency] | operative | consistency | ordering control | 0 | NO_ITEMS | Lens `ordering control` was checked against scoped production text for operative / consistency without a separate enrichment input. |
| F:[evaluative]:[necessity] | evaluative | necessity | boundary basis | 0 | NO_ITEMS | Lens `boundary basis` was checked against scoped production text for evaluative / necessity without a separate enrichment input. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment threshold | 0 | NO_ITEMS | Lens `judgment threshold` was checked against scoped production text for evaluative / sufficiency without a separate enrichment input. |
| F:[evaluative]:[completeness] | evaluative | completeness | integrity review | 0 | NO_ITEMS | Lens `integrity review` was checked against scoped production text for evaluative / completeness without a separate enrichment input. |
| F:[evaluative]:[consistency] | evaluative | consistency | rationale discipline | 0 | NO_ITEMS | Lens `rationale discipline` was checked against scoped production text for evaluative / consistency without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[necessity] | TBD_Question | Procedure | Procedure | What runtime option/interface shape supplies `opts.tools`, session/persona/mode, SDK version, MCP server set, and permission policy to the resolver? | Procedure names the required context inputs for deterministic exposure, while Guidance says the exact interface shape is TBD. The input-precondition lens requires that open interface question to remain explicit. | Guidance.md; Procedure.md | Guidance.md#Resolver Shape; Procedure.md#Steps |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[completeness] | MissingSlot | Procedure | Procedure | Name the unknown-tool, deterministic-ordering, and read-first sequencing test paths or fixture identifiers. | Procedure lists these records as TBD even though the Specification requires the tests. Fixture coverage cannot close until the concrete test locations are recorded. | Procedure.md; Specification.md | Procedure.md#Records; Specification.md#Verification |  | PROPOSAL | TBD |

## Matrix D — Design

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | governed registry | 0 | NO_ITEMS | Lens `governed registry` was checked against scoped production text for normative / guiding without a separate enrichment input. |
| D:[normative]:[applying] | normative | applying | binding validation | 0 | NO_ITEMS | Lens `binding validation` was checked against scoped production text for normative / applying without a separate enrichment input. |
| D:[normative]:[judging] | normative | judging | acceptance boundary | 0 | NO_ITEMS | Lens `acceptance boundary` was checked against scoped production text for normative / judging without a separate enrichment input. |
| D:[normative]:[reviewing] | normative | reviewing | audit posture | 0 | NO_ITEMS | Lens `audit posture` was checked against scoped production text for normative / reviewing without a separate enrichment input. |
| D:[operative]:[guiding] | operative | guiding | resolver pathway | 0 | NO_ITEMS | Lens `resolver pathway` was checked against scoped production text for operative / guiding without a separate enrichment input. |
| D:[operative]:[applying] | operative | applying | controlled exposure | 1 | HAS_ITEMS | Lens `controlled exposure` surfaces 1 warranted register item(s) for operative / applying evidence. |
| D:[operative]:[judging] | operative | judging | validation finding | 0 | NO_ITEMS | Lens `validation finding` was checked against scoped production text for operative / judging without a separate enrichment input. |
| D:[operative]:[reviewing] | operative | reviewing | process assurance | 0 | NO_ITEMS | Lens `process assurance` was checked against scoped production text for operative / reviewing without a separate enrichment input. |
| D:[evaluative]:[guiding] | evaluative | guiding | boundary rationale | 0 | NO_ITEMS | Lens `boundary rationale` was checked against scoped production text for evaluative / guiding without a separate enrichment input. |
| D:[evaluative]:[applying] | evaluative | applying | merit standard | 0 | NO_ITEMS | Lens `merit standard` was checked against scoped production text for evaluative / applying without a separate enrichment input. |
| D:[evaluative]:[judging] | evaluative | judging | risk closure | 0 | NO_ITEMS | Lens `risk closure` was checked against scoped production text for evaluative / judging without a separate enrichment input. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality signal | 1 | HAS_ITEMS | Lens `quality signal` surfaces 1 warranted register item(s) for evaluative / reviewing evidence. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[operative]:[applying] | VerificationGap | Specification | Specification | Add verification evidence that `allowedTools` cannot bypass deny policy and that implementation availability alone cannot expose tools. | The requirements and procedure state these permission boundaries, but the implementation evidence is still future-facing. Controlled exposure needs explicit tests or fixtures before closure. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Verification |  | PROPOSAL | TBD |
| D-002 | D:[evaluative]:[reviewing] | RationaleGap | Guidance | Guidance | Capture the review rationale for continuing to use PRD-derived details while REF-006 remains HASH_MISMATCH. | Guidance notes that PRD content aligns with matching sources but requires review after reconciliation. The quality-signal lens makes the basis for that interim use worth preserving. | Guidance.md; _REFERENCES.md | Guidance.md#PRD Hash Warning; _REFERENCES.md#Authoritative Source Corpus |  | PROPOSAL | TBD |

## Matrix X — Review

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | registry warrant | 0 | NO_ITEMS | Lens `registry warrant` was checked against scoped production text for guiding / necessity without a separate enrichment input. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | evidence threshold | 0 | NO_ITEMS | Lens `evidence threshold` was checked against scoped production text for guiding / sufficiency without a separate enrichment input. |
| X:[guiding]:[completeness] | guiding | completeness | coverage rationale | 0 | NO_ITEMS | Lens `coverage rationale` was checked against scoped production text for guiding / completeness without a separate enrichment input. |
| X:[guiding]:[consistency] | guiding | consistency | coherent surface | 0 | NO_ITEMS | Lens `coherent surface` was checked against scoped production text for guiding / consistency without a separate enrichment input. |
| X:[applying]:[necessity] | applying | necessity | practice prerequisite | 0 | NO_ITEMS | Lens `practice prerequisite` was checked against scoped production text for applying / necessity without a separate enrichment input. |
| X:[applying]:[sufficiency] | applying | sufficiency | implementation warrant | 0 | NO_ITEMS | Lens `implementation warrant` was checked against scoped production text for applying / sufficiency without a separate enrichment input. |
| X:[applying]:[completeness] | applying | completeness | complete exposure | 0 | NO_ITEMS | Lens `complete exposure` was checked against scoped production text for applying / completeness without a separate enrichment input. |
| X:[applying]:[consistency] | applying | consistency | stable ordering | 0 | NO_ITEMS | Lens `stable ordering` was checked against scoped production text for applying / consistency without a separate enrichment input. |
| X:[judging]:[necessity] | judging | necessity | decision basis | 0 | NO_ITEMS | Lens `decision basis` was checked against scoped production text for judging / necessity without a separate enrichment input. |
| X:[judging]:[sufficiency] | judging | sufficiency | adequate assessment | 0 | NO_ITEMS | Lens `adequate assessment` was checked against scoped production text for judging / sufficiency without a separate enrichment input. |
| X:[judging]:[completeness] | judging | completeness | closure finding | 0 | NO_ITEMS | Lens `closure finding` was checked against scoped production text for judging / completeness without a separate enrichment input. |
| X:[judging]:[consistency] | judging | consistency | consistent appraisal | 0 | NO_ITEMS | Lens `consistent appraisal` was checked against scoped production text for judging / consistency without a separate enrichment input. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit trigger | 0 | NO_ITEMS | Lens `audit trigger` was checked against scoped production text for reviewing / necessity without a separate enrichment input. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | evidence standard | 0 | NO_ITEMS | Lens `evidence standard` was checked against scoped production text for reviewing / sufficiency without a separate enrichment input. |
| X:[reviewing]:[completeness] | reviewing | completeness | trace coverage | 1 | HAS_ITEMS | Lens `trace coverage` surfaces 1 warranted register item(s) for reviewing / completeness evidence. |
| X:[reviewing]:[consistency] | reviewing | consistency | assurance coherence | 0 | NO_ITEMS | Lens `assurance coherence` was checked against scoped production text for reviewing / consistency without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[reviewing]:[completeness] | MissingSlot | Procedure | Procedure | Complete trace records for tool resolver implementation, registry, error contract, fixtures, sequencing tests, and PRD warning note. | Procedure Records holds all trace evidence paths as TBD. The trace-coverage lens requires these records before audit or review can verify artifact closure. | Procedure.md | Procedure.md#Records |  | PROPOSAL | TBD |

## Matrix E — Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | factual warrant | 0 | NO_ITEMS | Lens `factual warrant` was checked against scoped production text for guiding / data without a separate enrichment input. |
| E:[guiding]:[information] | guiding | information | signal rationale | 0 | NO_ITEMS | Lens `signal rationale` was checked against scoped production text for guiding / information without a separate enrichment input. |
| E:[guiding]:[knowledge] | guiding | knowledge | understanding frame | 0 | NO_ITEMS | Lens `understanding frame` was checked against scoped production text for guiding / knowledge without a separate enrichment input. |
| E:[guiding]:[wisdom] | guiding | wisdom | discernment path | 0 | NO_ITEMS | Lens `discernment path` was checked against scoped production text for guiding / wisdom without a separate enrichment input. |
| E:[applying]:[data] | applying | data | fact practice | 0 | NO_ITEMS | Lens `fact practice` was checked against scoped production text for applying / data without a separate enrichment input. |
| E:[applying]:[information] | applying | information | context enactment | 0 | NO_ITEMS | Lens `context enactment` was checked against scoped production text for applying / information without a separate enrichment input. |
| E:[applying]:[knowledge] | applying | knowledge | expertise method | 0 | NO_ITEMS | Lens `expertise method` was checked against scoped production text for applying / knowledge without a separate enrichment input. |
| E:[applying]:[wisdom] | applying | wisdom | judgment practice | 0 | NO_ITEMS | Lens `judgment practice` was checked against scoped production text for applying / wisdom without a separate enrichment input. |
| E:[judging]:[data] | judging | data | evidence decision | 0 | NO_ITEMS | Lens `evidence decision` was checked against scoped production text for judging / data without a separate enrichment input. |
| E:[judging]:[information] | judging | information | message assessment | 0 | NO_ITEMS | Lens `message assessment` was checked against scoped production text for judging / information without a separate enrichment input. |
| E:[judging]:[knowledge] | judging | knowledge | mastery appraisal | 0 | NO_ITEMS | Lens `mastery appraisal` was checked against scoped production text for judging / knowledge without a separate enrichment input. |
| E:[judging]:[wisdom] | judging | wisdom | reasoned finding | 1 | HAS_ITEMS | Lens `reasoned finding` surfaces 1 warranted register item(s) for judging / wisdom evidence. |
| E:[reviewing]:[data] | reviewing | data | record audit | 1 | HAS_ITEMS | Lens `record audit` surfaces 1 warranted register item(s) for reviewing / data evidence. |
| E:[reviewing]:[information] | reviewing | information | account review | 0 | NO_ITEMS | Lens `account review` was checked against scoped production text for reviewing / information without a separate enrichment input. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | mastery assurance | 0 | NO_ITEMS | Lens `mastery assurance` was checked against scoped production text for reviewing / knowledge without a separate enrichment input. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled appraisal | 0 | NO_ITEMS | Lens `principled appraisal` was checked against scoped production text for reviewing / wisdom without a separate enrichment input. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[reviewing]:[data] | VerificationGap | Specification | Specification | Define safe metadata or boot-fingerprint evidence path for resolved SDK names, versions, and MCP identifiers. | REQ-012 requires safe runtime metadata or boot fingerprints, but both Specification and Procedure leave the exact metadata path TBD. Record-audit coverage needs a concrete evidence target. | Specification.md; Procedure.md | Specification.md#Requirements; Procedure.md#Records |  | PROPOSAL | TBD |
| E-002 | E:[judging]:[wisdom] | TBD_Question | Guidance | NA | Who rules whether PRD HASH_MISMATCH blocks closure or remains a warning-qualified residual risk? | The conflict table leaves the human ruling as TBD. The reasoned-finding lens requires the unresolved authority decision to remain visible rather than being silently absorbed into implementation guidance. | Guidance.md; _REFERENCES.md | Guidance.md#Conflict Table (for human ruling); _REFERENCES.md#Authoritative Source Corpus |  | PROPOSAL | TBD |
