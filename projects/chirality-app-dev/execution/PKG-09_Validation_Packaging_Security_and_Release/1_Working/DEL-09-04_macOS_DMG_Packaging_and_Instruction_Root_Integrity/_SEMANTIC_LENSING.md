# Semantic Lensing Register: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

**Generated:** 2026-05-20
**DECOMP_VARIANT:** SOFTWARE
**Deliverable Folder:** /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
**Warnings:** REF-006 PRD hash mismatch treated as source warning only per deliverable-local guidance; production documents were not edited.

**Inputs Read:**
- _CONTEXT.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_CONTEXT.md#identity
- _STATUS.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md#history
- _SEMANTIC.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_SEMANTIC.md#semantic-lens
- Datasheet.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Datasheet.md#attributes
- Specification.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Specification.md#requirements
- Guidance.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Guidance.md#principles
- Procedure.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Procedure.md#steps
- _REFERENCES.md - /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_REFERENCES.md#authoritative-source-corpus

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.

## Summary

- Total warranted items: 13
- By document:
  - Datasheet: 0
  - Specification: 4
  - Guidance: 3
  - Procedure: 5
  - Multi: 1
  - NA: 0
- By matrix:
  - A: 1
  - B: 2
  - C: 2
  - F: 2
  - D: 2
  - X: 2
  - E: 2
- By type:
  - Conflict: 2
  - VerificationGap: 6
  - MissingSlot: 2
  - WeakStatement: 1
  - RationaleGap: 1
  - Normalization: 0
  - TBD_Question: 1
  - MatrixError: 0
- Notable conflicts: 2
- Matrix parse errors: 0

## Matrix A - Orientation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| A:[normative]:[guiding] | normative | guiding | prescriptive direction | 0 | NO_ITEMS | normative guiding orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[normative]:[applying] | normative | applying | mandatory practice | 0 | NO_ITEMS | normative applying orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[normative]:[judging] | normative | judging | compliance determination | 0 | NO_ITEMS | normative judging orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[normative]:[reviewing] | normative | reviewing | regulatory audit | 1 | HAS_ITEMS | Conflict item recorded for this lens: Retain PRD hash mismatch as a source warning only for this run while keeping PRD-backed draft requirements traceable. |
| A:[operative]:[guiding] | operative | guiding | procedural direction | 0 | NO_ITEMS | operative guiding orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[operative]:[applying] | operative | applying | practical execution | 0 | NO_ITEMS | operative applying orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[operative]:[judging] | operative | judging | performance assessment | 0 | NO_ITEMS | operative judging orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[operative]:[reviewing] | operative | reviewing | process audit | 0 | NO_ITEMS | operative reviewing orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[evaluative]:[guiding] | evaluative | guiding | value orientation | 0 | NO_ITEMS | evaluative guiding orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[evaluative]:[applying] | evaluative | applying | merit application | 0 | NO_ITEMS | evaluative applying orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[evaluative]:[judging] | evaluative | judging | worth determination | 0 | NO_ITEMS | evaluative judging orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |
| A:[evaluative]:[reviewing] | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | evaluative reviewing orientation is represented in the deliverable role split; no extra item beyond package-readiness evidence gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[normative]:[reviewing] | Conflict | Multi | NA | Retain PRD hash mismatch as a source warning only for this run while keeping PRD-backed draft requirements traceable. | Guidance records assignment override for REF-006, while _REFERENCES.md marks REF-006 as HASH_MISMATCH; this needs human ruling before the warning can become accepted source policy. | Guidance.md; _REFERENCES.md | Guidance.md#conflict-table-for-human-ruling; _REFERENCES.md#authoritative-source-corpus | Guidance.md#conflict-table-for-human-ruling; _REFERENCES.md#authoritative-source-corpus | PROPOSAL | TBD |

## Matrix B - Conceptualization

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| B:[data]:[necessity] | data | necessity | essential fact | 0 | NO_ITEMS | data necessity concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[data]:[sufficiency] | data | sufficiency | adequate evidence | 0 | NO_ITEMS | data sufficiency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[data]:[completeness] | data | completeness | comprehensive record | 1 | HAS_ITEMS | MissingSlot item recorded for this lens: Record dependency-edge extraction status before closure or cite the accepted no-edge ruling. |
| B:[data]:[consistency] | data | consistency | reliable measurement | 0 | NO_ITEMS | data consistency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[information]:[necessity] | information | necessity | essential signal | 0 | NO_ITEMS | information necessity concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[information]:[sufficiency] | information | sufficiency | adequate context | 0 | NO_ITEMS | information sufficiency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[information]:[completeness] | information | completeness | comprehensive account | 1 | HAS_ITEMS | MissingSlot item recorded for this lens: Add explicit owner or routing placeholder for release evidence bundle custody once assigned. |
| B:[information]:[consistency] | information | consistency | coherent message | 0 | NO_ITEMS | information consistency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[knowledge]:[necessity] | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | knowledge necessity concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[knowledge]:[sufficiency] | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | knowledge sufficiency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[knowledge]:[completeness] | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | knowledge completeness concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[knowledge]:[consistency] | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | knowledge consistency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[wisdom]:[necessity] | wisdom | necessity | essential discernment | 0 | NO_ITEMS | wisdom necessity concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[wisdom]:[sufficiency] | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | wisdom sufficiency concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[wisdom]:[completeness] | wisdom | completeness | holistic insight | 0 | NO_ITEMS | wisdom completeness concept is present through attributes, requirements, guidance, or records unless separately itemized. |
| B:[wisdom]:[consistency] | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | wisdom consistency concept is present through attributes, requirements, guidance, or records unless separately itemized. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | B:[information]:[completeness] | MissingSlot | Procedure | Procedure | Add explicit owner or routing placeholder for release evidence bundle custody once assigned. | Procedure names Required records but ResponsibleParty remains TBD, so the comprehensive account lacks an accountable records owner. | Procedure.md; _CONTEXT.md | Procedure.md#records; _CONTEXT.md#identity |  | PROPOSAL | TBD |
| B-002 | B:[data]:[completeness] | MissingSlot | Procedure | Procedure | Record dependency-edge extraction status before closure or cite the accepted no-edge ruling. | Procedure prerequisites state declared upstream dependencies are TBD, leaving the comprehensive record incomplete for dependency-aware closure. | Procedure.md | Procedure.md#prerequisites |  | PROPOSAL | TBD |

## Matrix C - Formulation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| C:[normative]:[necessity] | normative | necessity | release mandate basis | 0 | NO_ITEMS | release mandate basis is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[normative]:[sufficiency] | normative | sufficiency | package proof frame | 1 | HAS_ITEMS | VerificationGap item recorded for this lens: Require integrity summary evidence to state pass result or enumerate blockers before release readiness. |
| C:[normative]:[completeness] | normative | completeness | compliance evidence corpus | 0 | NO_ITEMS | compliance evidence corpus is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[normative]:[consistency] | normative | consistency | coherent control posture | 0 | NO_ITEMS | coherent control posture is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[operative]:[necessity] | operative | necessity | release execution path | 0 | NO_ITEMS | release execution path is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[operative]:[sufficiency] | operative | sufficiency | build evidence basis | 1 | HAS_ITEMS | VerificationGap item recorded for this lens: Capture SDK subprocess package-layout probe command, expected result, and failure recording rule. |
| C:[operative]:[completeness] | operative | completeness | package workflow record | 0 | NO_ITEMS | package workflow record is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[operative]:[consistency] | operative | consistency | stable process posture | 0 | NO_ITEMS | stable process posture is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[evaluative]:[necessity] | evaluative | necessity | readiness value rationale | 0 | NO_ITEMS | readiness value rationale is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[evaluative]:[sufficiency] | evaluative | sufficiency | acceptance evidence balance | 0 | NO_ITEMS | acceptance evidence balance is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[evaluative]:[completeness] | evaluative | completeness | release appraisal corpus | 0 | NO_ITEMS | release appraisal corpus is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |
| C:[evaluative]:[consistency] | evaluative | consistency | quality rationale posture | 0 | NO_ITEMS | quality rationale posture is generally reflected in scope and verification text; only sufficiency lenses produced itemized gaps. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | C:[normative]:[sufficiency] | VerificationGap | Specification | Specification | Require integrity summary evidence to state pass result or enumerate blockers before release readiness. | Specification requires the summary JSON but the current text allows existence plus blocker recording; sufficiency depends on an explicit pass/blocker verdict. | Specification.md; Procedure.md | Specification.md#verification; Procedure.md#verification |  | PROPOSAL | TBD |
| C-002 | C:[operative]:[sufficiency] | VerificationGap | Specification | Procedure | Capture SDK subprocess package-layout probe command, expected result, and failure recording rule. | Specification requires package-layout executability, and Procedure asks to run or review the probe, but no concrete probe artifact shape is defined. | Specification.md; Procedure.md | Specification.md#requirements; Procedure.md#steps |  | PROPOSAL | TBD |

## Matrix F - Requirements

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| F:[normative]:[necessity] | normative | necessity | binding readiness premise | 0 | NO_ITEMS | binding readiness premise is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[normative]:[sufficiency] | normative | sufficiency | sufficient control evidence | 0 | NO_ITEMS | sufficient control evidence is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[normative]:[completeness] | normative | completeness | integrated compliance basis | 0 | NO_ITEMS | integrated compliance basis is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[normative]:[consistency] | normative | consistency | stable release rule | 0 | NO_ITEMS | stable release rule is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[operative]:[necessity] | operative | necessity | actionable build premise | 0 | NO_ITEMS | actionable build premise is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[operative]:[sufficiency] | operative | sufficiency | sufficient execution proof | 0 | NO_ITEMS | sufficient execution proof is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[operative]:[completeness] | operative | completeness | complete workflow basis | 0 | NO_ITEMS | complete workflow basis is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[operative]:[consistency] | operative | consistency | reliable process pattern | 1 | HAS_ITEMS | VerificationGap item recorded for this lens: Add a repeatable evidence form for architecture, minimum OS, signing posture, resource inclusion, network policy, and SDK execution checks. |
| F:[evaluative]:[necessity] | evaluative | necessity | priority acceptance premise | 1 | HAS_ITEMS | TBD_Question item recorded for this lens: Who can rule whether SDK-backed turn start after R1 is a DEL-09-04 blocker or deferred packaged-app validation? |
| F:[evaluative]:[sufficiency] | evaluative | sufficiency | balanced readiness basis | 0 | NO_ITEMS | balanced readiness basis is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[evaluative]:[completeness] | evaluative | completeness | comprehensive appraisal frame | 0 | NO_ITEMS | comprehensive appraisal frame is addressed by requirements and procedure checks except the listed consistency or boundary questions. |
| F:[evaluative]:[consistency] | evaluative | consistency | stable quality judgment | 0 | NO_ITEMS | stable quality judgment is addressed by requirements and procedure checks except the listed consistency or boundary questions. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | F:[operative]:[consistency] | VerificationGap | Procedure | Procedure | Add a repeatable evidence form for architecture, minimum OS, signing posture, resource inclusion, network policy, and SDK execution checks. | Procedure lists manual verification notes but does not normalize their format, which risks inconsistent release evidence between local runs. | Procedure.md | Procedure.md#records |  | PROPOSAL | TBD |
| F-002 | F:[evaluative]:[necessity] | TBD_Question | Guidance | NA | Who can rule whether SDK-backed turn start after R1 is a DEL-09-04 blocker or deferred packaged-app validation? | Procedure step 9 includes SDK-backed turn start after R1, but the deliverable scope is packaging integrity and SDK subprocess posture; the closure boundary needs human confirmation. | Procedure.md; _CONTEXT.md | Procedure.md#steps; _CONTEXT.md#deliverable-scope |  | PROPOSAL | TBD |

## Matrix D - Objectives

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| D:[normative]:[guiding] | normative | guiding | authoritative closure direction | 0 | NO_ITEMS | authoritative closure direction is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[normative]:[applying] | normative | applying | mandatory proof practice | 1 | HAS_ITEMS | Conflict item recorded for this lens: Surface possible mismatch between policy-level required instruction-root assets and the code-level integrity manifest. |
| D:[normative]:[judging] | normative | judging | compliance readiness verdict | 0 | NO_ITEMS | compliance readiness verdict is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[normative]:[reviewing] | normative | reviewing | regulatory evidence review | 0 | NO_ITEMS | regulatory evidence review is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[operative]:[guiding] | operative | guiding | procedural closure path | 0 | NO_ITEMS | procedural closure path is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[operative]:[applying] | operative | applying | practical package execution | 1 | HAS_ITEMS | WeakStatement item recorded for this lens: Replace or qualify "required pre-packaging checks" with an explicit acceptance rule for non-run evidence. |
| D:[operative]:[judging] | operative | judging | performance readiness verdict | 0 | NO_ITEMS | performance readiness verdict is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[operative]:[reviewing] | operative | reviewing | process evidence review | 0 | NO_ITEMS | process evidence review is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[evaluative]:[guiding] | evaluative | guiding | value closure orientation | 0 | NO_ITEMS | value closure orientation is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[evaluative]:[applying] | evaluative | applying | merit release practice | 0 | NO_ITEMS | merit release practice is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[evaluative]:[judging] | evaluative | judging | worth readiness verdict | 0 | NO_ITEMS | worth readiness verdict is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |
| D:[evaluative]:[reviewing] | evaluative | reviewing | quality evidence review | 0 | NO_ITEMS | quality evidence review is allocated across specification, procedure, and guidance; applying lenses exposed the itemized issue. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | D:[normative]:[applying] | Conflict | Guidance | NA | Surface possible mismatch between policy-level required instruction-root assets and the code-level integrity manifest. | Guidance says a manifest difference must be recorded as conflict or blocker, while Specification requires packaged builds to contain required resources; the accepted source of the asset set is not yet ruled. | Guidance.md; Specification.md | Guidance.md#considerations; Specification.md#requirements | Guidance.md#considerations; Specification.md#requirements | PROPOSAL | TBD |
| D-002 | D:[operative]:[applying] | WeakStatement | Procedure | Procedure | Replace or qualify "required pre-packaging checks" with an explicit acceptance rule for non-run evidence. | Procedure step 2 permits confirming accepted evidence already exists, but the acceptance criteria for substituted evidence are not stated in this deliverable. | Procedure.md | Procedure.md#steps |  | PROPOSAL | TBD |

## Matrix X - Synthesis

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| X:[guiding]:[necessity] | guiding | necessity | release authority proof | 0 | NO_ITEMS | release authority proof has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[guiding]:[sufficiency] | guiding | sufficiency | sufficient mandate evidence | 0 | NO_ITEMS | sufficient mandate evidence has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[guiding]:[completeness] | guiding | completeness | complete readiness basis | 0 | NO_ITEMS | complete readiness basis has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[guiding]:[consistency] | guiding | consistency | coherent review control | 0 | NO_ITEMS | coherent review control has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[applying]:[necessity] | applying | necessity | package practice proof | 0 | NO_ITEMS | package practice proof has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[applying]:[sufficiency] | applying | sufficiency | sufficient execution evidence | 0 | NO_ITEMS | sufficient execution evidence has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[applying]:[completeness] | applying | completeness | complete workflow proof | 0 | NO_ITEMS | complete workflow proof has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[applying]:[consistency] | applying | consistency | reliable practice control | 0 | NO_ITEMS | reliable practice control has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[judging]:[necessity] | judging | necessity | acceptance verdict proof | 1 | HAS_ITEMS | VerificationGap item recorded for this lens: Define verdict evidence needed to pass readiness when instruction-root assets are absent or summary reports failure. |
| X:[judging]:[sufficiency] | judging | sufficiency | sufficient assessment evidence | 0 | NO_ITEMS | sufficient assessment evidence has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[judging]:[completeness] | judging | completeness | complete decision record | 0 | NO_ITEMS | complete decision record has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[judging]:[consistency] | judging | consistency | coherent verdict control | 0 | NO_ITEMS | coherent verdict control has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[reviewing]:[necessity] | reviewing | necessity | audit evidence proof | 0 | NO_ITEMS | audit evidence proof has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[reviewing]:[sufficiency] | reviewing | sufficiency | sufficient review evidence | 1 | HAS_ITEMS | VerificationGap item recorded for this lens: Require audit-ready pointers to command transcript, artifact listing or checksum, summary JSON, and SDK probe output. |
| X:[reviewing]:[completeness] | reviewing | completeness | complete audit basis | 0 | NO_ITEMS | complete audit basis has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |
| X:[reviewing]:[consistency] | reviewing | consistency | reliable review control | 0 | NO_ITEMS | reliable review control has supporting release-evidence language; judging or reviewing lenses identify itemized proof gaps where shown. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | X:[judging]:[necessity] | VerificationGap | Specification | Specification | Define verdict evidence needed to pass readiness when instruction-root assets are absent or summary reports failure. | Specification states missing assets are P0 blockers, but the readiness verdict path should explicitly bind failed integrity evidence to non-closure. | Specification.md; Guidance.md | Specification.md#requirements; Guidance.md#principles |  | PROPOSAL | TBD |
| X-002 | X:[reviewing]:[sufficiency] | VerificationGap | Procedure | Procedure | Require audit-ready pointers to command transcript, artifact listing or checksum, summary JSON, and SDK probe output. | Procedure lists records, but sufficient review evidence needs stable paths or attachment identifiers for the release evidence bundle. | Procedure.md | Procedure.md#records |  | PROPOSAL | TBD |

## Matrix E - Evaluation

### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| E:[guiding]:[data] | guiding | data | authoritative evidence signal | 0 | NO_ITEMS | authoritative evidence signal is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[guiding]:[information] | guiding | information | contextual authority message | 0 | NO_ITEMS | contextual authority message is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[guiding]:[knowledge] | guiding | knowledge | expert release basis | 0 | NO_ITEMS | expert release basis is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[guiding]:[wisdom] | guiding | wisdom | principled readiness rationale | 1 | HAS_ITEMS | RationaleGap item recorded for this lens: Explain why unsigned/adhoc local-builder DMG remains acceptable for this release target. |
| E:[applying]:[data] | applying | data | practical package evidence | 1 | HAS_ITEMS | VerificationGap item recorded for this lens: Add checksum or deterministic artifact identity expectation for the DMG when package evidence is captured. |
| E:[applying]:[information] | applying | information | contextual execution signal | 0 | NO_ITEMS | contextual execution signal is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[applying]:[knowledge] | applying | knowledge | skilled package basis | 0 | NO_ITEMS | skilled package basis is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[applying]:[wisdom] | applying | wisdom | reasoned practice rationale | 0 | NO_ITEMS | reasoned practice rationale is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[judging]:[data] | judging | data | verdict evidence signal | 0 | NO_ITEMS | verdict evidence signal is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[judging]:[information] | judging | information | contextual assessment proof | 0 | NO_ITEMS | contextual assessment proof is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[judging]:[knowledge] | judging | knowledge | expert acceptance basis | 0 | NO_ITEMS | expert acceptance basis is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[judging]:[wisdom] | judging | wisdom | principled verdict rationale | 0 | NO_ITEMS | principled verdict rationale is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[reviewing]:[data] | reviewing | data | audit evidence signal | 0 | NO_ITEMS | audit evidence signal is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[reviewing]:[information] | reviewing | information | contextual review proof | 0 | NO_ITEMS | contextual review proof is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[reviewing]:[knowledge] | reviewing | knowledge | expert audit basis | 0 | NO_ITEMS | expert audit basis is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |
| E:[reviewing]:[wisdom] | reviewing | wisdom | principled appraisal rationale | 0 | NO_ITEMS | principled appraisal rationale is supported by current evidence roles; selected data and rationale lenses need the listed refinements. |

### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | E:[guiding]:[wisdom] | RationaleGap | Guidance | Guidance | Explain why unsigned/adhoc local-builder DMG remains acceptable for this release target. | Guidance names the trade-off but does not state the release rationale beyond current scope, leaving principled readiness rationale thin. | Guidance.md | Guidance.md#trade-offs |  | PROPOSAL | TBD |
| E-002 | E:[applying]:[data] | VerificationGap | Specification | Procedure | Add checksum or deterministic artifact identity expectation for the DMG when package evidence is captured. | Specification requires confirming the DMG exists, but release evidence would be stronger with stable artifact identity rather than existence alone. | Specification.md; Procedure.md | Specification.md#verification; Procedure.md#records |  | PROPOSAL | TBD |
