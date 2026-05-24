# Semantic Lensing Register: DEL-08-04 Type 2 Subagent Governance Bridge

**Generated:** 2026-05-20
**Deliverable Folder:** `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge`
**DECOMP_VARIANT:** SOFTWARE
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS - `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_lens_register.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge`
**Purpose:** Matrix-organized lensing register generated from `_SEMANTIC.md` primary Result tables and deliverable-local production documents.

**Inputs Read:**
- `_CONTEXT.md` - local identity and scope metadata
- `_STATUS.md` - read only; no status edits made
- `_SEMANTIC.md` - primary Result tables for matrices A, B, C, F, D, X, and E
- `Datasheet.md` - production evidence
- `Specification.md` - production evidence
- `Guidance.md` - production evidence
- `Procedure.md` - production evidence
- `_REFERENCES.md` - metadata only; external paths not followed
- `_DEPENDENCIES.md` - read only local dependency context

**Warnings:**
- [WARNING] SOURCE_STATE: `_REFERENCES.md` records REF-006 `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived delegation behavior remains warning-qualified.
- [WARNING] TBD_IMPLEMENTATION_CONTRACTS: module/file targets, governance decision shape, approval reference format, SDK probe readiness, and DEL-08-05 handoff boundary remain TBD in local production documents.
- [WARNING] DEPENDENCY_STATE: `_DEPENDENCIES.md` contains extracted ACTIVE dependency rows while Procedure still says declared upstream dependencies are TBD and dependency extraction remains deferred.

## Summary

Total warranted items: 11

By matrix:
- A: 1
- B: 1
- C: 2
- F: 2
- D: 2
- X: 2
- E: 1

By type:
- MissingSlot: 3
- WeakStatement: 1
- Conflict: 0
- VerificationGap: 4
- RationaleGap: 1
- Normalization: 1
- TBD_Question: 1
- MatrixError: 0

By document:
- Datasheet.md: 2
- Specification.md: 7
- Guidance.md: 7
- Procedure.md: 9
- _REFERENCES.md: 1
- _DEPENDENCIES.md: 4

## Matrix A

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `A:[normative]:[guiding]` | normative | guiding | prescriptive direction | 0 | NO_ITEMS | prescriptive direction is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[normative]:[applying]` | normative | applying | mandatory practice | 1 | HAS_ITEMS | Mandatory practice exposes unresolved implementation module and hook target names. |
| `A:[normative]:[judging]` | normative | judging | compliance determination | 0 | NO_ITEMS | compliance determination is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[normative]:[reviewing]` | normative | reviewing | regulatory audit | 0 | NO_ITEMS | regulatory audit is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[operative]:[guiding]` | operative | guiding | procedural direction | 0 | NO_ITEMS | procedural direction is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[operative]:[applying]` | operative | applying | practical execution | 0 | NO_ITEMS | practical execution is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[operative]:[judging]` | operative | judging | performance assessment | 0 | NO_ITEMS | performance assessment is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[operative]:[reviewing]` | operative | reviewing | process audit | 0 | NO_ITEMS | process audit is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[evaluative]:[guiding]` | evaluative | guiding | value orientation | 0 | NO_ITEMS | value orientation is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[evaluative]:[applying]` | evaluative | applying | merit application | 0 | NO_ITEMS | merit application is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[evaluative]:[judging]` | evaluative | judging | worth determination | 0 | NO_ITEMS | worth determination is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |
| `A:[evaluative]:[reviewing]` | evaluative | reviewing | quality appraisal | 0 | NO_ITEMS | quality appraisal is represented by fail-closed delegation framing, approval evidence, and child-boundary controls in the local docs. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | `A:[normative]:[applying]` | MissingSlot | Procedure.md | Procedure.md | Name the TypeScript module/file targets for the bridge, SDK agent-definition builder, and Agent hook before implementation closure. | Procedure and Guidance leave exact module/file names as TBD while the mandatory practice lens requires an executable ownership surface for the bridge and hook. | Procedure.md; Guidance.md | Prerequisites; Records; Open Items | NA | PROPOSAL | TBD |

## Matrix B

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `B:[data]:[necessity]` | data | necessity | essential fact | 0 | NO_ITEMS | essential fact is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[data]:[sufficiency]` | data | sufficiency | adequate evidence | 0 | NO_ITEMS | adequate evidence is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[data]:[completeness]` | data | completeness | comprehensive record | 0 | NO_ITEMS | comprehensive record is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[data]:[consistency]` | data | consistency | reliable measurement | 1 | HAS_ITEMS | Reliable measurement is limited by TBD decision-object and approval-reference vocabulary. |
| `B:[information]:[necessity]` | information | necessity | essential signal | 0 | NO_ITEMS | essential signal is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[information]:[sufficiency]` | information | sufficiency | adequate context | 0 | NO_ITEMS | adequate context is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[information]:[completeness]` | information | completeness | comprehensive account | 0 | NO_ITEMS | comprehensive account is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[information]:[consistency]` | information | consistency | coherent message | 0 | NO_ITEMS | coherent message is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[knowledge]:[necessity]` | knowledge | necessity | fundamental understanding | 0 | NO_ITEMS | fundamental understanding is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[knowledge]:[sufficiency]` | knowledge | sufficiency | competent expertise | 0 | NO_ITEMS | competent expertise is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[knowledge]:[completeness]` | knowledge | completeness | thorough mastery | 0 | NO_ITEMS | thorough mastery is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[knowledge]:[consistency]` | knowledge | consistency | coherent understanding | 0 | NO_ITEMS | coherent understanding is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[wisdom]:[necessity]` | wisdom | necessity | essential discernment | 0 | NO_ITEMS | essential discernment is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[wisdom]:[sufficiency]` | wisdom | sufficiency | adequate judgment | 0 | NO_ITEMS | adequate judgment is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[wisdom]:[completeness]` | wisdom | completeness | holistic insight | 0 | NO_ITEMS | holistic insight is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |
| `B:[wisdom]:[consistency]` | wisdom | consistency | principled reasoning | 0 | NO_ITEMS | principled reasoning is addressed through the local gate inputs, denial scenarios, source warnings, and bounded child execution records. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-001 | `B:[data]:[consistency]` | Normalization | Guidance.md | Specification.md | Normalize the serialized governance decision object fields, denial reason vocabulary, and approval-reference representation used by tests and audit handoff. | Guidance marks the decision object and approval reference as TBD, while Specification requires denial, unknown-value, and handoff behavior that needs consistent measurement. | Guidance.md; Specification.md | Open Items; Requirements DEL-08-04-R02, R10, R11; Verification | NA | PROPOSAL | TBD |

## Matrix C

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `C:[normative]:[necessity]` | normative | necessity | Binding Gate Premise | 0 | NO_ITEMS | Binding Gate Premise is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[normative]:[sufficiency]` | normative | sufficiency | Sufficient Control Warrant | 0 | NO_ITEMS | Sufficient Control Warrant is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[normative]:[completeness]` | normative | completeness | Complete Control Frame | 0 | NO_ITEMS | Complete Control Frame is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[normative]:[consistency]` | normative | consistency | Consistent Gate Logic | 1 | HAS_ITEMS | Consistent gate logic remains warning-qualified by the REF-006 PRD hash mismatch. |
| `C:[operative]:[necessity]` | operative | necessity | Required Execution Basis | 0 | NO_ITEMS | Required Execution Basis is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[operative]:[sufficiency]` | operative | sufficiency | Adequate Runtime Basis | 1 | HAS_ITEMS | Adequate runtime basis is weakened by TBD SDK probe readiness evidence. |
| `C:[operative]:[completeness]` | operative | completeness | Complete Runtime Frame | 0 | NO_ITEMS | Complete Runtime Frame is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[operative]:[consistency]` | operative | consistency | Consistent Runtime Logic | 0 | NO_ITEMS | Consistent Runtime Logic is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[evaluative]:[necessity]` | evaluative | necessity | Essential Assurance Basis | 0 | NO_ITEMS | Essential Assurance Basis is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[evaluative]:[sufficiency]` | evaluative | sufficiency | Sufficient Assurance Warrant | 0 | NO_ITEMS | Sufficient Assurance Warrant is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[evaluative]:[completeness]` | evaluative | completeness | Complete Assurance Frame | 0 | NO_ITEMS | Complete Assurance Frame is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |
| `C:[evaluative]:[consistency]` | evaluative | consistency | Consistent Assurance Logic | 0 | NO_ITEMS | Consistent Assurance Logic is supported by source-cited governance bridge framing without adding authority beyond the local evidence. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-001 | `C:[normative]:[consistency]` | RationaleGap | Guidance.md | Guidance.md | Carry REF-006 PRD hash mismatch as an explicit warning until a human refreshes or waives the accepted PRD snapshot. | The production set cites PRD Section 8.15 for multiple requirements while _REFERENCES.md and local conflict tables record REF-006 as HASH_MISMATCH; proceeding is justified only as warning-qualified. | _REFERENCES.md; Specification.md; Guidance.md; Datasheet.md | Authoritative Source Corpus REF-006; Conflict Table; Conditions | NA | PROPOSAL | TBD |
| C-002 | `C:[operative]:[sufficiency]` | WeakStatement | Procedure.md | Procedure.md | Replace current SDK probe readiness TBD with a concrete accepted probe reference or a blocking prerequisite before claiming executable runtime sufficiency. | Procedure says SDK agents capability verified by R0/R1 probes is required but current probe status is TBD; operative sufficiency cannot be assessed from an unspecified probe state. | Procedure.md; _DEPENDENCIES.md | Prerequisites; Extracted Dependency Register DEP-08-04-005 | NA | PROPOSAL | TBD |

## Matrix F

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `F:[normative]:[necessity]` | normative | necessity | Mandatory Gate Requirement | 0 | NO_ITEMS | Mandatory Gate Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[normative]:[sufficiency]` | normative | sufficiency | Traceable Approval Requirement | 1 | HAS_ITEMS | Traceable approval requirement lacks an accepted approval-reference format. |
| `F:[normative]:[completeness]` | normative | completeness | Complete Governance Requirement | 0 | NO_ITEMS | Complete Governance Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[normative]:[consistency]` | normative | consistency | Uniform Denial Requirement | 0 | NO_ITEMS | Uniform Denial Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[operative]:[necessity]` | operative | necessity | Failclosed Execution Requirement | 0 | NO_ITEMS | Failclosed Execution Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[operative]:[sufficiency]` | operative | sufficiency | Bounded Runtime Requirement | 1 | HAS_ITEMS | Bounded runtime requirement lacks a serialized governance decision contract. |
| `F:[operative]:[completeness]` | operative | completeness | Complete Execution Requirement | 0 | NO_ITEMS | Complete Execution Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[operative]:[consistency]` | operative | consistency | Predictable Runtime Requirement | 0 | NO_ITEMS | Predictable Runtime Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[evaluative]:[necessity]` | evaluative | necessity | Essential Safety Requirement | 0 | NO_ITEMS | Essential Safety Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[evaluative]:[sufficiency]` | evaluative | sufficiency | Auditable Assurance Requirement | 0 | NO_ITEMS | Auditable Assurance Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[evaluative]:[completeness]` | evaluative | completeness | Complete Assurance Requirement | 0 | NO_ITEMS | Complete Assurance Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |
| `F:[evaluative]:[consistency]` | evaluative | consistency | Principled Assurance Requirement | 0 | NO_ITEMS | Principled Assurance Requirement is described as a requirement family for delegation gates, restricted runtime, and assurance behavior. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F-001 | `F:[normative]:[sufficiency]` | MissingSlot | Guidance.md | Guidance.md | Define the exact approval reference format and minimum traceability fields accepted by evaluateSubagentGovernance. | Traceable approval is a normative requirement, but Guidance leaves the exact approval reference format TBD and examples only state absent references must deny. | Guidance.md; Specification.md; Procedure.md | Principles; Open Items; Requirements DEL-08-04-R02; Steps 2-3 | NA | PROPOSAL | TBD |
| F-002 | `F:[operative]:[sufficiency]` | MissingSlot | Specification.md | Specification.md | Define the serialized governance decision object, including allow/deny, human-ruling-needed, denial reason, audit-safe metadata, and DEL-08-05 handoff fields. | Bounded runtime proof depends on a stable decision object, but Guidance records the serialized shape as TBD and Specification requires tests and downstream handoff. | Guidance.md; Specification.md; Procedure.md | Open Items; Requirements DEL-08-04-R10, R11; Steps 9-10 | NA | PROPOSAL | TBD |

## Matrix D

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `D:[normative]:[guiding]` | normative | guiding | Authorized Delegation Aim | 0 | NO_ITEMS | Authorized Delegation Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[normative]:[applying]` | normative | applying | Evidenced Permission Aim | 0 | NO_ITEMS | Evidenced Permission Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[normative]:[judging]` | normative | judging | Governed Decision Aim | 0 | NO_ITEMS | Governed Decision Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[normative]:[reviewing]` | normative | reviewing | Auditable Denial Aim | 0 | NO_ITEMS | Auditable Denial Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[operative]:[guiding]` | operative | guiding | Failclosed Runtime Aim | 0 | NO_ITEMS | Failclosed Runtime Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[operative]:[applying]` | operative | applying | Restricted Capability Aim | 1 | HAS_ITEMS | Restricted capability aim needs concrete implementation paths and test commands. |
| `D:[operative]:[judging]` | operative | judging | Verified Execution Aim | 0 | NO_ITEMS | Verified Execution Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[operative]:[reviewing]` | operative | reviewing | Repeatable Guard Aim | 1 | HAS_ITEMS | Repeatable guard audit exposes unresolved dependency-state reconciliation. |
| `D:[evaluative]:[guiding]` | evaluative | guiding | Safety Priority Aim | 0 | NO_ITEMS | Safety Priority Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[evaluative]:[applying]` | evaluative | applying | Assurance Evidence Aim | 0 | NO_ITEMS | Assurance Evidence Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[evaluative]:[judging]` | evaluative | judging | Confidence Judgment Aim | 0 | NO_ITEMS | Confidence Judgment Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |
| `D:[evaluative]:[reviewing]` | evaluative | reviewing | Principled Review Aim | 0 | NO_ITEMS | Principled Review Aim is framed as an objective for authorized delegation, restricted capability, and reviewable denial behavior. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | `D:[operative]:[applying]` | VerificationGap | Procedure.md | Procedure.md | Provide concrete implementation paths and final test commands for bridge invocation, hook fail-closed behavior, Type 2 eligibility, context sealing, approval reference, and child tool/cwd restriction. | Procedure lists expected artifacts and tests but does not name implementation files or commands; restricted capability execution cannot close without runnable evidence. | Procedure.md; Specification.md | Steps 1-12; Records; Verification | NA | PROPOSAL | TBD |
| D-002 | `D:[operative]:[reviewing]` | TBD_Question | Procedure.md | Procedure.md | Reconcile Procedure prerequisite text that declared upstream dependencies are TBD with _DEPENDENCIES.md active extracted prerequisites for source corpus, governance contract, hook infrastructure, SDK probe, and DEL-08-05 handoff. | Procedure still says dependency extraction is deferred and declared upstream dependencies are TBD, while _DEPENDENCIES.md now records six active rows; workflow audit needs a current-state ruling without treating extracted rows as accepted declarations. | Procedure.md; _DEPENDENCIES.md | Prerequisites; Records; Declared Upstream; Extracted Dependency Register | NA | PROPOSAL | TBD |

## Matrix X

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `X:[guiding]:[necessity]` | guiding | necessity | Permission Gate Check | 0 | NO_ITEMS | Permission Gate Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[guiding]:[sufficiency]` | guiding | sufficiency | Approval Evidence Check | 0 | NO_ITEMS | Approval Evidence Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[guiding]:[completeness]` | guiding | completeness | Authorization Coverage Check | 0 | NO_ITEMS | Authorization Coverage Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[guiding]:[consistency]` | guiding | consistency | Stable Permission Check | 0 | NO_ITEMS | Stable Permission Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[applying]:[necessity]` | applying | necessity | Evidence Requirement Check | 0 | NO_ITEMS | Evidence Requirement Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[applying]:[sufficiency]` | applying | sufficiency | Bounded Scope Check | 1 | HAS_ITEMS | Bounded scope check lacks fixture paths and passing command evidence. |
| `X:[applying]:[completeness]` | applying | completeness | Capability Coverage Check | 0 | NO_ITEMS | Capability Coverage Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[applying]:[consistency]` | applying | consistency | Restriction Alignment Check | 0 | NO_ITEMS | Restriction Alignment Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[judging]:[necessity]` | judging | necessity | Decision Basis Check | 0 | NO_ITEMS | Decision Basis Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[judging]:[sufficiency]` | judging | sufficiency | Decision Evidence Check | 0 | NO_ITEMS | Decision Evidence Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[judging]:[completeness]` | judging | completeness | Decision Coverage Check | 0 | NO_ITEMS | Decision Coverage Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[judging]:[consistency]` | judging | consistency | Decision Stability Check | 0 | NO_ITEMS | Decision Stability Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[reviewing]:[necessity]` | reviewing | necessity | Denial Audit Check | 0 | NO_ITEMS | Denial Audit Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[reviewing]:[sufficiency]` | reviewing | sufficiency | Review Evidence Check | 1 | HAS_ITEMS | Review evidence check needs audit-safe denial-reason tests. |
| `X:[reviewing]:[completeness]` | reviewing | completeness | Review Coverage Check | 0 | NO_ITEMS | Review Coverage Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |
| `X:[reviewing]:[consistency]` | reviewing | consistency | Review Stability Check | 0 | NO_ITEMS | Review Stability Check is represented by the planned verification categories for gate, scope, decision, and audit behavior. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X-001 | `X:[applying]:[sufficiency]` | VerificationGap | Specification.md | Specification.md | Attach concrete fixture paths and passing test names for missing metadata, missing approval reference, unsealed context, non-allowlisted candidate, non-Type-2 candidate, hook error, broad child capability request, and allowed restricted execution. | Specification and Procedure describe verification categories, but no concrete fixture paths or command outputs are present for sufficiency of applying-level validation evidence. | Specification.md; Procedure.md | Verification; Records | NA | PROPOSAL | TBD |
| X-002 | `X:[reviewing]:[sufficiency]` | VerificationGap | Specification.md | Specification.md | Test that denial reasons are audit-suitable and do not leak sensitive prompt or environment data while still preserving enough detail for review. | Guidance requires audit-suitable denial reasons without sensitive leakage, but the exact decision object and test expectations remain TBD. | Guidance.md; Specification.md; Procedure.md | Considerations; Requirements DEL-08-04-R09, R10; Steps 9 and 12 | NA | PROPOSAL | TBD |

## Matrix E

### Lens Coverage

| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| `E:[guiding]:[data]` | guiding | data | Permission Fact Value | 0 | NO_ITEMS | Permission Fact Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[guiding]:[information]` | guiding | information | Permission Signal Value | 0 | NO_ITEMS | Permission Signal Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[guiding]:[knowledge]` | guiding | knowledge | Permission Rationale Value | 0 | NO_ITEMS | Permission Rationale Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[guiding]:[wisdom]` | guiding | wisdom | Permission Judgment Value | 0 | NO_ITEMS | Permission Judgment Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[applying]:[data]` | applying | data | Restriction Fact Value | 0 | NO_ITEMS | Restriction Fact Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[applying]:[information]` | applying | information | Restriction Signal Value | 0 | NO_ITEMS | Restriction Signal Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[applying]:[knowledge]` | applying | knowledge | Restriction Rationale Value | 0 | NO_ITEMS | Restriction Rationale Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[applying]:[wisdom]` | applying | wisdom | Restriction Judgment Value | 0 | NO_ITEMS | Restriction Judgment Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[judging]:[data]` | judging | data | Decision Fact Value | 0 | NO_ITEMS | Decision Fact Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[judging]:[information]` | judging | information | Decision Signal Value | 0 | NO_ITEMS | Decision Signal Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[judging]:[knowledge]` | judging | knowledge | Decision Rationale Value | 0 | NO_ITEMS | Decision Rationale Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[judging]:[wisdom]` | judging | wisdom | Decision Judgment Value | 0 | NO_ITEMS | Decision Judgment Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[reviewing]:[data]` | reviewing | data | Audit Fact Value | 1 | HAS_ITEMS | Audit fact value needs a verified DEL-08-05 handoff interface boundary. |
| `E:[reviewing]:[information]` | reviewing | information | Audit Signal Value | 0 | NO_ITEMS | Audit Signal Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[reviewing]:[knowledge]` | reviewing | knowledge | Audit Rationale Value | 0 | NO_ITEMS | Audit Rationale Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |
| `E:[reviewing]:[wisdom]` | reviewing | wisdom | Audit Judgment Value | 0 | NO_ITEMS | Audit Judgment Value is carried as an evaluation perspective over permission, restriction, decision, and audit outcomes. |

### Warranted Items

| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | `E:[reviewing]:[data]` | VerificationGap | Procedure.md | Procedure.md | Verify the DEL-08-05 handoff interface carries child lifecycle metadata and output artifact-path hooks without DEL-08-04 owning persistence. | Datasheet, Specification, Guidance, and Procedure all reserve full child-record persistence for DEL-08-05, but the exact interface boundary remains TBD and needs reviewable evidence. | Datasheet.md; Specification.md; Guidance.md; Procedure.md; _DEPENDENCIES.md | Conditions; Requirements DEL-08-04-R11; Trade-offs; Verification; DEP-08-04-006 | NA | PROPOSAL | TBD |

