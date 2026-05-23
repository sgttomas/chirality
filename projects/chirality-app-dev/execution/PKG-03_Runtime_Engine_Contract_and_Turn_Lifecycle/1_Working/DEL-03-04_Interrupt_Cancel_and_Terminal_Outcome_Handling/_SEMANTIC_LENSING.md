# Semantic Lensing Register: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-04_Interrupt_Cancel_and_Terminal_Outcome_Handling
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - validate_lens_register.py completed successfully after generation.
**Warnings:** REF-006 PRD HASH_MISMATCH remains unresolved; interruption taxonomy and exact implementation paths remain TBD.

**Inputs Read:**
- _CONTEXT.md - _CONTEXT.md#Context:-DEL-03-04-Interrupt-Cancel-and-Terminal-Outcome-Handling
- _STATUS.md - _STATUS.md#Status:-DEL-03-04; lifecycle state read only as INITIALIZED
- _SEMANTIC.md - _SEMANTIC.md#Semantic-Lens:-DEL-03-04-Interrupt,-Cancel,-and-Terminal-Outcome-Handling
- Datasheet.md - Datasheet.md#Datasheet:-DEL-03-04-Interrupt,-Cancel,-and-Terminal-Outcome-Handling
- Specification.md - Specification.md#Specification:-DEL-03-04-Interrupt,-Cancel,-and-Terminal-Outcome-Handling
- Guidance.md - Guidance.md#Guidance:-DEL-03-04-Interrupt,-Cancel,-and-Terminal-Outcome-Handling
- Procedure.md - Procedure.md#Procedure:-DEL-03-04-Interrupt,-Cancel,-and-Terminal-Outcome-Handling
- _REFERENCES.md - _REFERENCES.md#References:-DEL-03-04-Interrupt-Cancel-and-Terminal-Outcome-Handling; metadata only, external paths not followed

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 13
- By document:
  - Datasheet: 0
  - Specification: 4
  - Guidance: 2
  - Procedure: 4
  - Multi: 3
  - NA: 0
- By matrix:
  - A: 1
  - B: 2
  - C: 1
  - F: 2
  - D: 1
  - X: 3
  - E: 3
- By type:
  - Conflict: 1
  - VerificationGap: 5
  - MissingSlot: 2
  - WeakStatement: 1
  - RationaleGap: 1
  - Normalization: 1
  - TBD_Question: 2
  - MatrixError: 0
- Notable conflicts: 1
- Matrix parse errors: 0

## Matrix A - Orientation (3x4) - Canonical

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | Reviewed prescriptive direction against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | Reviewed mandatory practice against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | Reviewed compliance determination against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Registers 1 warranted item(s) where regulatory audit exposes a later enrichment need for terminal outcome handling. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | Reviewed procedural direction against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | Reviewed practical execution against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | Reviewed performance assessment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Reviewed process audit against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | Reviewed value orientation against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | Reviewed merit application against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | Reviewed worth determination against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | Reviewed quality appraisal against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Carry unresolved interruption taxonomy conflict into later enrichment. | Guidance records a human-ruling conflict because interruption is required as a durable terminal outcome while SPEC/TYPES initial categories omit turn.interrupted. | Guidance.md; Specification.md | Guidance.md#Conflict-Table-(for-human-ruling); Specification.md#Requirements | Guidance.md#Conflict-Table-(for-human-ruling); Specification.md#Documentation | PROPOSAL | TBD |

## Matrix B - Conceptualization (4x4) - Canonical

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 1 | HAS_ITEMS | Registers 1 warranted item(s) where essential fact exposes a later enrichment need for terminal outcome handling. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | Reviewed adequate evidence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 0 | NO_ITEMS | Reviewed comprehensive record against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | Reviewed reliable measurement against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | Reviewed essential signal against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 1 | HAS_ITEMS | Registers 1 warranted item(s) where adequate context exposes a later enrichment need for terminal outcome handling. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 0 | NO_ITEMS | Reviewed comprehensive account against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | Reviewed coherent message against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | Reviewed fundamental understanding against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | Reviewed competent expertise against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | Reviewed thorough mastery against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | Reviewed coherent understanding against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | Reviewed essential discernment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | Reviewed adequate judgment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | Reviewed holistic insight against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | Reviewed principled reasoning against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[data]:[necessity] | MissingSlot | Multi | TBD | Populate exact interrupt test, cancel cleanup test, mapper, and helper paths. | Datasheet construction targets and Procedure verification steps repeatedly mark exact implementation/test/module paths as TBD. | Datasheet.md; Procedure.md; Specification.md | Datasheet.md#Construction; Procedure.md#Steps; Specification.md#Documentation |  | PROPOSAL | TBD |
| B-002 | B:[information]:[sufficiency] | WeakStatement | Specification | Specification | Define observable cleanup hook or state API for REQ-014 before implementation closure. | REQ-014 requires testable cleanup observability but leaves the exact hook or state API as TBD, which weakens acceptance evidence. | Specification.md | Specification.md#Requirements; Specification.md#Verification |  | PROPOSAL | TBD |

## Matrix C - Formulation (3x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | policy trigger basis | 0 | NO_ITEMS | Reviewed policy trigger basis against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[normative]:[sufficiency] | normative | sufficiency | compliance proof | 0 | NO_ITEMS | Reviewed compliance proof against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[normative]:[completeness] | normative | completeness | rule coverage | 0 | NO_ITEMS | Reviewed rule coverage against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[normative]:[consistency] | normative | consistency | control coherence | 1 | HAS_ITEMS | Registers 1 warranted item(s) where control coherence exposes a later enrichment need for terminal outcome handling. |
| C:[operative]:[necessity] | operative | necessity | execution trigger | 0 | NO_ITEMS | Reviewed execution trigger against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[operative]:[sufficiency] | operative | sufficiency | cleanup proof | 0 | NO_ITEMS | Reviewed cleanup proof against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[operative]:[completeness] | operative | completeness | lifecycle coverage | 0 | NO_ITEMS | Reviewed lifecycle coverage against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[operative]:[consistency] | operative | consistency | signal stability | 0 | NO_ITEMS | Reviewed signal stability against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[evaluative]:[necessity] | evaluative | necessity | judgment basis | 0 | NO_ITEMS | Reviewed judgment basis against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | outcome warrant | 0 | NO_ITEMS | Reviewed outcome warrant against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[evaluative]:[completeness] | evaluative | completeness | assurance coverage | 0 | NO_ITEMS | Reviewed assurance coverage against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| C:[evaluative]:[consistency] | evaluative | consistency | quality rationale | 0 | NO_ITEMS | Reviewed quality rationale against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[consistency] | Normalization | Multi | Guidance | Normalize interruption vocabulary across terminal outcome, cancellation reason, and process:exit usage. | Documents use interruption as terminal outcome while also allowing turn.cancelled with reason=interrupted; later enrichment needs consistent terms before schema closure. | Datasheet.md; Guidance.md; Procedure.md | Datasheet.md#Conditions; Guidance.md#Trade-offs; Procedure.md#Steps |  | PROPOSAL | TBD |

## Matrix F - Requirements (3x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | terminal mandate | 1 | HAS_ITEMS | Registers 1 warranted item(s) where terminal mandate exposes a later enrichment need for terminal outcome handling. |
| F:[normative]:[sufficiency] | normative | sufficiency | rule evidence | 0 | NO_ITEMS | Reviewed rule evidence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[normative]:[completeness] | normative | completeness | compliance record | 0 | NO_ITEMS | Reviewed compliance record against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[normative]:[consistency] | normative | consistency | policy alignment | 0 | NO_ITEMS | Reviewed policy alignment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[operative]:[necessity] | operative | necessity | cleanup prerequisite | 1 | HAS_ITEMS | Registers 1 warranted item(s) where cleanup prerequisite exposes a later enrichment need for terminal outcome handling. |
| F:[operative]:[sufficiency] | operative | sufficiency | execution evidence | 0 | NO_ITEMS | Reviewed execution evidence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[operative]:[completeness] | operative | completeness | recovery account | 0 | NO_ITEMS | Reviewed recovery account against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[operative]:[consistency] | operative | consistency | lifecycle stability | 0 | NO_ITEMS | Reviewed lifecycle stability against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[evaluative]:[necessity] | evaluative | necessity | assurance basis | 0 | NO_ITEMS | Reviewed assurance basis against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | judgment context | 0 | NO_ITEMS | Reviewed judgment context against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[evaluative]:[completeness] | evaluative | completeness | outcome insight | 0 | NO_ITEMS | Reviewed outcome insight against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| F:[evaluative]:[consistency] | evaluative | consistency | quality reasoning | 0 | NO_ITEMS | Reviewed quality reasoning against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[normative]:[necessity] | VerificationGap | Specification | Specification | Add explicit acceptance rule for aborting active provider/model requests without leaking SDK semantics. | REQ-002 states provider abort behavior and REQ-007 preserves Chirality-owned semantics, but the verification table does not define how adapter-boundary proof avoids SDK-shaped public contracts. | Specification.md | Specification.md#Requirements; Specification.md#Verification |  | PROPOSAL | TBD |
| F-002 | F:[operative]:[necessity] | VerificationGap | Procedure | Procedure | Make lock-release proof cover interrupt, disconnect, provider failure, and cancellation in one terminal trigger matrix. | Procedure asks for a terminal trigger matrix and tests each path, but the current records do not yet bind all terminal paths to a single lock-release evidence artifact. | Procedure.md | Procedure.md#Steps; Procedure.md#Verification |  | PROPOSAL | TBD |

## Matrix D - Objectives (3x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | terminal obligation | 0 | NO_ITEMS | Reviewed terminal obligation against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[normative]:[applying] | normative | applying | cleanup practice | 0 | NO_ITEMS | Reviewed cleanup practice against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[normative]:[judging] | normative | judging | conformance decision | 0 | NO_ITEMS | Reviewed conformance decision against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[normative]:[reviewing] | normative | reviewing | lifecycle audit | 0 | NO_ITEMS | Reviewed lifecycle audit against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[operative]:[guiding] | operative | guiding | recovery direction | 0 | NO_ITEMS | Reviewed recovery direction against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[operative]:[applying] | operative | applying | cleanup execution | 0 | NO_ITEMS | Reviewed cleanup execution against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[operative]:[judging] | operative | judging | terminal performance | 0 | NO_ITEMS | Reviewed terminal performance against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | Reviewed process audit against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[evaluative]:[guiding] | evaluative | guiding | assurance orientation | 0 | NO_ITEMS | Reviewed assurance orientation against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[evaluative]:[applying] | evaluative | applying | judgment practice | 0 | NO_ITEMS | Reviewed judgment practice against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[evaluative]:[judging] | evaluative | judging | outcome worth | 0 | NO_ITEMS | Reviewed outcome worth against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 1 | HAS_ITEMS | Registers 1 warranted item(s) where quality appraisal exposes a later enrichment need for terminal outcome handling. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[evaluative]:[reviewing] | RationaleGap | Guidance | Guidance | State decision criteria for fail-closed versus retry/fallback behavior when terminal event writes fail. | Guidance identifies event log write strictness as a trade-off but leaves exact retry or fallback behavior TBD, so later closure needs rationale. | Guidance.md | Guidance.md#Trade-offs |  | PROPOSAL | TBD |

## Matrix X - Verification (4x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | contract basis | 0 | NO_ITEMS | Reviewed contract basis against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | evidence threshold | 0 | NO_ITEMS | Reviewed evidence threshold against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[guiding]:[completeness] | guiding | completeness | coverage map | 0 | NO_ITEMS | Reviewed coverage map against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[guiding]:[consistency] | guiding | consistency | compatibility alignment | 0 | NO_ITEMS | Reviewed compatibility alignment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[applying]:[necessity] | applying | necessity | practice trigger | 0 | NO_ITEMS | Reviewed practice trigger against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[applying]:[sufficiency] | applying | sufficiency | execution proof | 1 | HAS_ITEMS | Registers 1 warranted item(s) where execution proof exposes a later enrichment need for terminal outcome handling. |
| X:[applying]:[completeness] | applying | completeness | recovery record | 0 | NO_ITEMS | Reviewed recovery record against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[applying]:[consistency] | applying | consistency | stream coherence | 0 | NO_ITEMS | Reviewed stream coherence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[judging]:[necessity] | judging | necessity | decision basis | 0 | NO_ITEMS | Reviewed decision basis against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[judging]:[sufficiency] | judging | sufficiency | conformance proof | 1 | HAS_ITEMS | Registers 1 warranted item(s) where conformance proof exposes a later enrichment need for terminal outcome handling. |
| X:[judging]:[completeness] | judging | completeness | outcome record | 0 | NO_ITEMS | Reviewed outcome record against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[judging]:[consistency] | judging | consistency | audit coherence | 0 | NO_ITEMS | Reviewed audit coherence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit basis | 0 | NO_ITEMS | Reviewed audit basis against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | closure proof | 0 | NO_ITEMS | Reviewed closure proof against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| X:[reviewing]:[completeness] | reviewing | completeness | assurance record | 1 | HAS_ITEMS | Registers 1 warranted item(s) where assurance record exposes a later enrichment need for terminal outcome handling. |
| X:[reviewing]:[consistency] | reviewing | consistency | taxonomy coherence | 0 | NO_ITEMS | Reviewed taxonomy coherence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[applying]:[sufficiency] | VerificationGap | Procedure | Procedure | Specify how SSE disconnect tests prove cleanup when no final browser event can be delivered. | Procedure recognizes client disconnect can prevent final browser delivery, but verification needs evidence criteria for cleanup and cancellation persistence without an SSE terminal event. | Procedure.md; Guidance.md | Procedure.md#Steps; Procedure.md#Verification; Guidance.md#Examples |  | PROPOSAL | TBD |
| X-002 | X:[judging]:[sufficiency] | VerificationGap | Specification | Specification | Add redaction assertions for terminal failure/error payloads including provider error surfaces. | Specification requires redaction and has a redaction test row, but later enrichment should ensure provider errors, runtime events, logs, and tool artifacts are all covered by concrete assertions. | Specification.md; Procedure.md | Specification.md#Requirements; Specification.md#Verification; Procedure.md#Verification |  | PROPOSAL | TBD |
| X-003 | X:[reviewing]:[completeness] | TBD_Question | Procedure | TBD | Which upstream deliverables provide accepted lock, route, event-writer, and replay seams for final DEL-03-04 closure? | Procedure lists DEL-03-01, DEL-03-02, DEL-03-03, and DEL-05-02 as assumed prerequisites while _DEPENDENCIES.md reports no accepted upstream edges yet. | Procedure.md; _DEPENDENCIES.md | Procedure.md#Prerequisites; _DEPENDENCIES.md#Dependencies-DEL-03-04-Interrupt-Cancel-and-Terminal-Outcome-Handling |  | PROPOSAL | TBD |

## Matrix E - Evaluation (4x4)

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | runtime facts | 0 | NO_ITEMS | Reviewed runtime facts against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[guiding]:[information] | guiding | information | signal evidence | 0 | NO_ITEMS | Reviewed signal evidence against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[guiding]:[knowledge] | guiding | knowledge | contract understanding | 0 | NO_ITEMS | Reviewed contract understanding against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[guiding]:[wisdom] | guiding | wisdom | policy discernment | 0 | NO_ITEMS | Reviewed policy discernment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[applying]:[data] | applying | data | cleanup facts | 0 | NO_ITEMS | Reviewed cleanup facts against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[applying]:[information] | applying | information | execution context | 0 | NO_ITEMS | Reviewed execution context against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[applying]:[knowledge] | applying | knowledge | mapper expertise | 1 | HAS_ITEMS | Registers 1 warranted item(s) where mapper expertise exposes a later enrichment need for terminal outcome handling. |
| E:[applying]:[wisdom] | applying | wisdom | terminal judgment | 0 | NO_ITEMS | Reviewed terminal judgment against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[judging]:[data] | judging | data | decision facts | 0 | NO_ITEMS | Reviewed decision facts against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[judging]:[information] | judging | information | conformance context | 0 | NO_ITEMS | Reviewed conformance context against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[judging]:[knowledge] | judging | knowledge | outcome mastery | 0 | NO_ITEMS | Reviewed outcome mastery against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[judging]:[wisdom] | judging | wisdom | audit reasoning | 1 | HAS_ITEMS | Registers 1 warranted item(s) where audit reasoning exposes a later enrichment need for terminal outcome handling. |
| E:[reviewing]:[data] | reviewing | data | source facts | 1 | HAS_ITEMS | Registers 1 warranted item(s) where source facts exposes a later enrichment need for terminal outcome handling. |
| E:[reviewing]:[information] | reviewing | information | closure context | 0 | NO_ITEMS | Reviewed closure context against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | assurance mastery | 0 | NO_ITEMS | Reviewed assurance mastery against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | taxonomy reasoning | 0 | NO_ITEMS | Reviewed taxonomy reasoning against interrupt, cancellation, terminal outcome, cleanup, SSE, replay, and source-state material; this lens adds no separate item beyond the specific registered gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[applying]:[knowledge] | MissingSlot | Procedure | Procedure | Record terminal mapper fixture cases for completion, failure, cancellation, and interruption-adjacent signals. | Procedure calls for mapper tests across terminal signals, but exact fixture cases and module path remain TBD. | Procedure.md; Specification.md | Procedure.md#Steps; Specification.md#Verification |  | PROPOSAL | TBD |
| E-002 | E:[judging]:[wisdom] | TBD_Question | Guidance | NA | Human ruling required: add turn.interrupted or encode interruption as turn.cancelled with reason metadata? | Guidance presents both taxonomy options and explicitly leaves terminal interruption event type pending conflict resolution. | Guidance.md | Guidance.md#Trade-offs; Guidance.md#Conflict-Table-(for-human-ruling) |  | PROPOSAL | TBD |
| E-003 | E:[reviewing]:[data] | VerificationGap | Specification | Specification | Tie malformed trailing JSONL replay tolerance to terminal outcome persistence evidence. | Specification covers terminal outcome replay and malformed trailing lines, but later validation should prove these together for failure or cancellation after turn.accepted. | Specification.md; Procedure.md | Specification.md#Verification; Procedure.md#Verification |  | PROPOSAL | TBD |
