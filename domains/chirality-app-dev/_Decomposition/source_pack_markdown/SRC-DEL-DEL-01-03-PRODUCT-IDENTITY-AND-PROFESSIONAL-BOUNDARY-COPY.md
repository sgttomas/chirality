# Source Pack: SRC-DEL-DEL-01-03-PRODUCT-IDENTITY-AND-PROFESSIONAL-BOUNDARY-COPY

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/Datasheet.md

### Datasheet: DEL-01-03 Product Identity and Professional Boundary Copy

#### Identification

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-03 |
| DeliverableName | Product Identity and Professional Boundary Copy |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | S |
| Current lifecycle state at drafting | OPEN |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary product identity | Chirality desktop harness and bundled agent operating system | `docs/DIRECTIVE.md` header; `docs/PRD.md` header |
| Product posture | Local-first governed desktop harness for running AI agents against a user-selected filesystem workspace | `docs/DIRECTIVE.md` Section 1; `docs/PRD.md` Section 2 |
| Identity boundary | User-facing text must identify the product as Chirality, not Claude Code, Anthropic, a vendor CLI, or a feature-parity target | `docs/DIRECTIVE.md` Section 2.11; `docs/CONTRACT.md` K-SDK-4; `docs/PRD.md` Section 3.2 |
| Professional authority posture | Agents propose; humans approve and retain binding decision rights | `docs/DIRECTIVE.md` Section 3; `docs/CONTRACT.md` K-AUTH-1 through K-GATE-1 |
| Draft status of agent outputs | Agent outputs are drafts and decision support until accepted by an accountable human | `docs/DIRECTIVE.md` Section 3.1 and Section 3.4; `docs/PRD.md` Section 2 |
| Reliance-boundary posture | Product-critical boundaries must be documented, implemented, and tested in Chirality terms; prompt text alone is insufficient | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 and K-RELIANCE-2 |
| Domain-engine boundary posture | Domain engines own domain truth; Chirality governs interaction, proposals, records, and human gates | `docs/CONTRACT.md` K-DOMAIN-1 through K-DOMAIN-4; `docs/SPEC.md` Section 18 |

#### Conditions

| Condition | Required treatment | Source |
|---|---|---|
| UI, documentation, packaging, runtime messages, and future domain notices mention the product | Use Chirality-owned product language; do not imply the product is Claude Code or an Anthropic product | `_CONTEXT.md` Deliverable Scope; `docs/DIRECTIVE.md` Section 2.11; `docs/PRD.md` FR-127 |
| Agent output, runtime event, validator result, SDK transcript, or domain-adapter output is presented to a user | Preserve draft/non-binding wording unless a human approval record exists | `docs/DIRECTIVE.md` Sections 2.3 and 3; `docs/CONTRACT.md` K-BIND-1 |
| Copy refers to approval, certification, code compliance, external validation, issuance, signature, seal, transmittal, or release for reliance | Reserve the action for accountable humans; do not attribute it to Chirality, agents, SDKs, tools, validators, runtime events, or domain adapters | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-PROF-1 |
| Copy refers to SDK integration | Describe SDK use as implementation/provider detail behind Chirality-owned contracts, not as product identity or governance authority | `docs/DIRECTIVE.md` Sections 2.8 and 2.11; `docs/CONTRACT.md` K-ENGINE-3 |
| Copy refers to future domain engines | State that domain-operation acceptance is human-gated and domain outputs are not Chirality-owned solver truth | `docs/PRD.md` Section 8.17; `docs/SPEC.md` Section 18 |

#### Construction

The deliverable is a documentation and copy-boundary package. Anticipated artifacts from `_CONTEXT.md` are:

- UI copy guidelines.
- Release review checklist.
- Boundary notice examples.

ASSUMPTION: These artifacts may be implemented as sections or downstream documents, but no final target file paths are specified in the available sources. Target file paths remain TBD until a human or later deliverable assigns them.

| Artifact | Current location in this deliverable | Final destination path | Source |
|---|---|---|---|
| UI copy guidelines | `Guidance.md` Principles, Considerations, Trade-offs, and Examples | TBD | `_CONTEXT.md` Anticipated Artifacts; decomposition DEL-01-03 AnticipatedArtifacts |
| Release review checklist | `Procedure.md` Verification and Release Review Evidence Template | TBD | `_CONTEXT.md` Anticipated Artifacts; `docs/DIRECTIVE.md` Sections 2.4 and 3.2 |
| Boundary notice examples | `Guidance.md` Examples | TBD | `_CONTEXT.md` Anticipated Artifacts; `docs/CONTRACT.md` K-AUTH-1 and K-DOMAIN-4 |
| Review notes | `Procedure.md` Review Note Record Template | TBD | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |

#### References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Founding intent, product identity, professional responsibility, evidence posture |
| REF-002 | `docs/CONTRACT.md` | Binding invariants for authority, identity, reliance boundaries, domain boundaries |
| REF-003 | `docs/SPEC.md` | Physical structures, persona composer professional-boundary reminders, domain future boundary |
| REF-004 | `docs/TYPES.md` | Stable identifiers, project truth, artifact vocabulary, human approval authority |
| REF-005 | `docs/PLAN.md` | Product identity and release/local-check posture |
| REF-006 | `docs/PRD.md` | Product requirements and accepted vNext runtime direction; hash mismatch treated as source warning per dispatch |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context; no copy requirements extracted |

## Component: execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/Guidance.md

### Guidance: DEL-01-03 Product Identity and Professional Boundary Copy

#### Purpose

This deliverable gives product and release writers a conservative boundary for Chirality copy. Its purpose is to preserve Chirality identity and human-only professional authority across UI, documentation, packaging, runtime messages, and future domain notices.

The governing posture is:

- Chirality is a governed desktop harness, not a vendor CLI wrapper.
- The SDK may be privileged as implementation substrate, but Chirality owns product semantics, runtime contracts, audit posture, permission policy, professional-boundary language, and user-facing product identity.
- Agents, tools, SDKs, validators, transcripts, and runtime events assist; accountable humans decide what can be relied upon.

Sources: `docs/DIRECTIVE.md` Sections 1, 2.8, 2.11, and 3; `docs/CONTRACT.md` K-AUTH-1, K-ENGINE-3, K-SDK-4.

#### Principles

| Principle | Guidance | Source |
|---|---|---|
| Name Chirality first | Use "Chirality" for product identity. Mention external SDK/provider details only when useful and only as implementation detail. | `docs/DIRECTIVE.md` Section 2.11 |
| Keep assistance non-binding | Prefer "draft", "proposal", "decision support", "review", "evidence", and "human acceptance" over "approved", "certified", "issued", or "validated" unless referring to a human approval record. | `docs/DIRECTIVE.md` Section 3; `docs/CONTRACT.md` K-BIND-1 |
| Preserve human gates | Copy should make clear that humans approve reliance-affecting transitions, release actions, issue actions, residual risk, and professional judgments. | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-GATE-1 |
| Avoid prompt-only safety claims | Do not describe prompt text, model instruction, or SDK default behavior as sufficient enforcement for product-critical boundaries. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-2 |
| Separate runtime evidence from approval | Runtime events and transcripts explain what happened; they do not approve work. | `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-BIND-1 |
| Keep domain truth separate | Future domain-engine copy should distinguish Chirality interaction governance from domain-engine truth and professional review. | `docs/CONTRACT.md` K-DOMAIN-1 through K-DOMAIN-4 |

#### Considerations

- Copy can disclose SDK usage when it improves transparency, diagnostics, implementation context, or release evidence. It risks product-identity drift when the SDK brand becomes the subject of the product claim, appears to own governance semantics, or makes Chirality look like Claude Code, an Anthropic product, a vendor CLI, or a feature-parity target.
- Professional-boundary copy should be visible where a user could confuse output generation, validation, event logging, or domain-engine results with approval.
- Release review should include UI labels, empty states, permission prompts, status-transition messages, runtime/session summaries, documentation, packaging metadata, and domain-engine future notices. The checked-surface inventory for a given release remains TBD until the release owner identifies the affected surfaces.
- ASSUMPTION: "Boundary notice examples" will be used as reusable copy snippets, not as a substitute for implementation enforcement. This is inferred from the deliverable scope and the reliance-boundary requirements.

#### Trade-offs

| Trade-off | Preferred posture |
|---|---|
| Transparent SDK disclosure vs. product identity drift | Disclose SDK use where appropriate, but keep Chirality as the product and contract owner. |
| Concise UI copy vs. professional-boundary clarity | Use concise language, but do not remove human-review and non-binding qualifiers where reliance confusion is plausible. For very short UI strings, pair concise labels with nearby help text, tooltip text, empty-state copy, or release notes when the label alone cannot carry the boundary without becoming misleading. |
| Friendly automation language vs. authority confusion | Prefer "helps draft", "organizes", "records", "checks", and "proposes" over "approves", "certifies", "issues", or "validates for reliance". |
| Future domain-engine capability vs. current scope | Present domain engines as future-boundary scope until governed amendment and implementation evidence exist. |

#### Term Normalization

| Term | Copy treatment | Source basis |
|---|---|---|
| Draft | Non-binding working output that requires accountable human acceptance before reliance. | `docs/DIRECTIVE.md` Section 3.1; `docs/CONTRACT.md` K-BIND-1 |
| Proposal | A suggested change, operation, or copy treatment requiring review or acceptance. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-GATE-1 |
| Decision support | Assistance that informs judgment but does not replace accountable human decision rights. | `docs/DIRECTIVE.md` Section 3.4 |
| Summary | Non-authoritative condensation unless imported into governed project files and accepted. | `docs/DIRECTIVE.md` Sections 2.5 and 2.6 |
| Transcript | Runtime or SDK record used for diagnosis/review, not an approval record. | `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-SDK-3 |
| Runtime event | Audit evidence of what happened during a turn; not approval, issuance, code compliance, external validation, or reliance clearance. | `docs/DIRECTIVE.md` Section 2.3 |
| Validator result | Deterministic check evidence; not professional approval or external validation. | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 |
| Approval record | Human-authored binding evidence tied to specific content, normally a git SHA. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |

Validators and runtime events cannot be treated as external validation or approval records because the sources separate evidence from human authority. They can show what was checked or what happened, but gate-relevant decisions still require versioned project files and accountable human acceptance.

#### Examples

Acceptable examples, grounded in source posture:

| Context | Example copy | Source basis |
|---|---|---|
| Product description | "Chirality is a governed desktop harness for AI-assisted project work over local files." | `docs/DIRECTIVE.md` Section 1 |
| Draft output notice | "This output is draft assistance. An accountable human must review and accept it before reliance." | `docs/DIRECTIVE.md` Section 3.1 |
| SDK disclosure | "This runtime may use an SDK-backed engine behind Chirality-owned contracts and audit records." | `docs/DIRECTIVE.md` Sections 2.8 and 2.10 |
| Runtime event notice | "Runtime events record what happened during the turn; they are not approval records." | `docs/DIRECTIVE.md` Section 2.3 |
| Domain notice | "Domain-engine results require human review and do not represent Chirality-owned solver truth or professional approval." | `docs/CONTRACT.md` K-DOMAIN-4; `docs/PRD.md` FR-115 |
| Validator result notice | "This validator result is check evidence, not external validation or professional approval." | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 |

Avoid examples:

| Context | Avoid | Reason |
|---|---|---|
| Product identity | "Chirality is Claude Code for professional workflows." | Violates product identity boundary. |
| Approval | "The agent approved this deliverable." | Violates human-only approval boundary. |
| Validation | "Chirality certifies this result as code-compliant." | Violates professional-boundary and domain-truth boundaries. |
| Reliance boundary | "The prompt prevents unsafe writes." | Prompt text alone is not a sufficient safety boundary. |

#### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | Dispatch path used `PKG-01_Governance_and_Product_Boundaries`, but the matching folder on disk is `PKG-01_Product_Governance_and_Reliance_Boundaries`. | User dispatch path | `_CONTEXT.md` PackageName and actual folder path | Run record; final report | Treat actual matching DEL-01-03 folder as resolved scope; preserve stable PackageID/DeliverableID. | TBD |
| CT-002 | `docs/PRD.md` hash differs from `_REFERENCES.md` expected hash. | `_REFERENCES.md` REF-006 expected/actual hash | User dispatch override says mismatch is source warning, not blocker | All PRD-sourced requirements | Use PRD as accessible source with warning; do not treat mismatch as blocker. | TBD |

## Component: execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/Procedure.md

### Procedure: DEL-01-03 Product Identity and Professional Boundary Copy

#### Purpose

This procedure describes how to produce and use product-identity and professional-boundary copy for DEL-01-03 without inventing unsupported claims or weakening Chirality's governance posture.

#### Prerequisites

- Read `_CONTEXT.md` for deliverable identity, scope, artifacts, and `ResponsibleParty: TBD`.
- Read `_REFERENCES.md` for the authoritative source corpus and hash status.
- Read `_DEPENDENCIES.md` and `Dependencies.csv`; dependency extraction has produced active rows, but satisfaction status remains `TBD` pending downstream FULL_GRAPH/cycle checks and human closure decisions.
- Read relevant source slices from:
  - `docs/DIRECTIVE.md`
  - `docs/CONTRACT.md`
  - `docs/SPEC.md`
  - `docs/TYPES.md`
  - `docs/PLAN.md`
  - `docs/PRD.md` with hash mismatch warning
  - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`

#### Steps

1. Confirm stable identity.
   - Use `DEL-01-03`, `PKG-01`, and the canonical deliverable name from `_CONTEXT.md`.
   - Keep `ResponsibleParty` as `TBD` until a human assigns ownership.

2. Establish source authority.
   - Use `docs/DIRECTIVE.md` for intent, product identity, professional responsibility, evidence posture, and source hierarchy.
   - Use `docs/CONTRACT.md` for binding invariants.
   - Use `docs/PRD.md` for accepted vNext product requirements, while preserving the recorded hash-mismatch warning.

3. Draft or review product identity copy.
   - Confirm the surface names Chirality as the product.
   - Confirm SDK/provider references are implementation detail, not product identity.
   - Remove or flag copy that makes Chirality appear to be Claude Code, Anthropic, a vendor CLI, or a feature-parity target.

4. Draft or review professional-boundary copy.
   - State that agent outputs are drafts, proposals, or decision support until accepted by an accountable human.
   - Reserve approval, certification, signature, seal, issue, transmittal, release for reliance, residual-risk acceptance, and professional judgment for humans.
   - Flag copy that conflates runtime events, transcripts, validators, or generated artifacts with approval records.

5. Draft or review reliance-boundary copy.
   - Confirm product-critical boundaries are described as Chirality-owned or verified through concrete enforcement surfaces.
   - Flag statements that rely on prompt text, model behavior, or opaque SDK defaults alone for safety or authority.

6. Draft or review future domain-engine notices.
   - State that domain engines own authoritative domain truth where applicable.
   - State that Chirality governs interaction, proposals, records, and human gates.
   - State that domain-engine outputs are not Chirality-owned solver truth, code compliance, external validation, or professional approval.

7. Preserve uncertainty.
   - Mark missing target paths, owner assignments, and unsupported implementation details as `TBD`.
   - Mark inferred guidance as `ASSUMPTION`.
   - Add conflicts requiring judgment to the Conflict Table in `Guidance.md`.

8. Prepare release review evidence.
   - Record the surfaces checked.
   - Record source sections used.
   - Record any `TBD`, `ASSUMPTION`, or human-ruling-needed item.
   - Record reviewer name or role, review date, pass/fail result, findings, proposed copy, and human ruling status.
   - Include PRD hash-mismatch handling and Conflict Table status as explicit evidence checkpoints.

9. Route authority-sensitive wording.
   - If copy uses approve, certify, sign, seal, issue, transmit, release, externally validate, code-compliant, solver truth, or safe for reliance, record the exact phrase and route it to the accountable human or human review body.
   - If no accountable role has been assigned, record `TBD` rather than approving the wording.
   - Do not close the item until the human ruling or deferral is recorded.

#### Verification

| Check | Pass condition | Evidence fields |
|---|---|---|
| Identity check | Product-facing copy names Chirality and does not present the app as Claude Code, Anthropic, or a vendor CLI. | Surface; copy excerpt; source section; pass/fail; finding ID |
| SDK framing check | SDK references are implementation/provider detail behind Chirality-owned contracts. | Surface; SDK phrase; source section; pass/fail; finding ID |
| Human authority check | No copy claims automated approval, certification, issue, signature, seal, external validation, code compliance, or release for reliance. | Surface; authority-sensitive phrase; routed-to human role; ruling status |
| Binding-record check | Drafts, proposals, summaries, transcripts, runtime events, and validator results are not described as approval records. | Record type; proposed label; source section; pass/fail |
| Reliance-boundary check | Product-critical boundaries are not described as prompt-only or SDK-default-only. | Boundary; enforcement surface if known; unsupported claims marked `TBD` |
| Domain-boundary check | Domain-engine notices preserve human acceptance and do not assign solver truth or professional approval to Chirality. | Domain surface; notice text; human-gate statement; pass/fail |
| Uncertainty check | Unsupported facts remain `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, or human-ruling-needed. | Item; label used; owner/ruling field; closure status |
| Source-status check | PRD hash mismatch and Conflict Table status are visible in review evidence. | REF-006 warning status; CT-001 status; CT-002 status; human ruling status |

#### Records

Create or maintain these records as applicable:

- UI copy guidelines: target path TBD.
- Release review checklist: target path TBD.
- Boundary notice examples: target path TBD.
- Review notes with checked surfaces and source sections: target path TBD.
- Human rulings for Conflict Table entries: TBD.
- `Dependencies.csv` satisfaction closure notes: TBD.

##### Release Review Evidence Template

| Field | Value |
|---|---|
| Review ID | TBD |
| Reviewer / accountable role | TBD |
| Review date | TBD |
| Release or surface set | TBD |
| Surfaces checked | TBD |
| Source sections used | TBD |
| PRD hash-mismatch treatment | REF-006 warning acknowledged; human ruling TBD |
| Conflict Table status | CT-001 TBD; CT-002 TBD |
| Overall result | TBD |

##### Review Note Record Template

| Field | Value |
|---|---|
| Checked surface | TBD |
| Source basis | TBD |
| Issue type | Identity / SDK framing / human authority / binding record / reliance boundary / domain boundary / uncertainty / source status |
| Current copy excerpt | TBD |
| Proposed copy | TBD |
| Finding | TBD |
| Human ruling | TBD |

## Component: execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/Specification.md

### Specification: DEL-01-03 Product Identity and Professional Boundary Copy

#### Scope

This deliverable specifies copy requirements for preserving Chirality product identity and human-only professional authority across UI, documentation, packaging, runtime messages, and future domain notices.

Included:

- Product identity language for Chirality-owned surfaces.
- Professional-boundary language for draft output, human approval, reliance, and release.
- Boundary notice requirements for future domain-engine surfaces.
- Release-review checks for identity and professional-boundary copy.

Excluded:

- Runtime implementation details except where copy must reflect product-owned boundaries.
- Dependency satisfaction closure; `Dependencies.csv` exists, but its rows remain `SatisfactionStatus=TBD` pending downstream FULL_GRAPH/cycle checks and any human closure decisions.
- Final assignment of `ResponsibleParty`; it remains TBD.
- Current-release domain operation implementation.

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-01 | User-facing copy MUST identify the product as Chirality and describe Chirality's governed-work posture. | `docs/DIRECTIVE.md` Section 2.11; `docs/PLAN.md` Section 6.5 |
| REQ-02 | User-facing copy MUST NOT make Chirality appear to be Claude Code, an Anthropic product, a vendor CLI, or a feature-parity target. | `docs/DIRECTIVE.md` Section 2.11; `docs/PRD.md` Section 3.2; `docs/CONTRACT.md` K-SDK-4 |
| REQ-03 | SDK references, when needed, MUST be framed as implementation/provider detail behind Chirality-owned contracts. | `docs/DIRECTIVE.md` Sections 2.8 and 2.10; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-4 |
| REQ-04 | Copy MUST state or preserve that agent outputs are drafts or decision support until accepted by an accountable human through a governed process. | `docs/DIRECTIVE.md` Sections 3.1 and 3.4; `docs/PRD.md` Section 2 |
| REQ-05 | Copy MUST NOT state or imply that an AI system, agent, tool, SDK, transcript, runtime event, deterministic validator, or domain adapter can approve, certify, sign, seal, issue, transmit, externally validate, or release professional work for reliance. | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-AUTH-1; `docs/PRD.md` Section 3.2 |
| REQ-06 | Copy MUST distinguish non-binding records such as drafts, proposals, summaries, and runtime transcripts from binding approval records. | `docs/CONTRACT.md` K-BIND-1; `docs/DIRECTIVE.md` Sections 2.3 and 3 |
| REQ-07 | Copy that describes reliance boundaries MUST NOT imply prompt text or opaque SDK defaults are sufficient enforcement for product-critical safety, audit, filesystem, lifecycle, transcript, settings, subagent, or human-gate semantics. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-2; `docs/PRD.md` FR-124 and FR-125 |
| REQ-08 | Future domain-engine notices MUST state that domain engines own authoritative domain truth and Chirality does not own solver truth, code compliance, external validation, or professional approval. | `docs/CONTRACT.md` K-DOMAIN-1 and K-DOMAIN-4; `docs/SPEC.md` Section 18; `docs/PRD.md` FR-115 |
| REQ-09 | Copy for future domain operations MUST preserve explicit human acceptance before any domain operation is applied. | `docs/CONTRACT.md` K-DOMAIN-3; `docs/SPEC.md` Section 18; `docs/PRD.md` FR-113 |
| REQ-10 | Copy and review artifacts MUST preserve explicit uncertainty when source support is missing; unknowns remain `TBD`, assumptions are labeled, and conflicts are surfaced. | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |

#### Standards

| Standard / authority | Status | Application |
|---|---|---|
| `docs/DIRECTIVE.md` | Accessible | Governs intent, product identity, professional responsibility, evidence posture |
| `docs/CONTRACT.md` | Accessible | Governs binding copy invariants |
| `docs/SPEC.md` | Accessible | Governs runtime/document structures and future domain specification boundary |
| `docs/TYPES.md` | Accessible | Governs vocabulary for project truth, artifacts, stable IDs, and authority |
| `docs/PLAN.md` | Accessible | Governs roadmap/release copy checks |
| `docs/PRD.md` | Accessible with hash mismatch warning | Governs product requirements and accepted vNext direction; dispatch says mismatch is warning, not blocker |

#### Verification

| Requirement | Verification approach |
|---|---|
| REQ-01, REQ-02 | Review UI labels, empty states, permission prompts, status-transition messages, runtime/session summaries, documentation, packaging metadata, release notes, and future domain notices for Chirality-owned identity and absence of Claude Code/Anthropic product-identity claims. |
| REQ-03 | Review SDK-related copy for implementation-detail framing and Chirality-owned contract language. |
| REQ-04 through REQ-06 | Review copy for draft/non-binding language and human-only approval language. |
| REQ-07 | Review reliance-boundary copy for non-prompt-only enforcement language and concrete ownership references. |
| REQ-08, REQ-09 | Review future domain notices for domain-truth separation and explicit human acceptance. |
| REQ-10 | Review deliverable and downstream copy for `TBD`, `ASSUMPTION`, `PROPOSAL`, and conflict labeling where source support is incomplete. |

Closure evidence before downstream production copy updates:

- `ResponsibleParty` assigned by an accountable human: TBD.
- Final destination paths for UI copy guidelines, release review checklist, boundary notice examples, and review notes: TBD.
- `Dependencies.csv` satisfaction and any project-level FULL_GRAPH/cycle checks closed or explicitly deferred by a human: TBD.
- Conflict Table CT-001 and CT-002 human rulings recorded: TBD.
- Release review evidence record completed for the checked surfaces and source sections: TBD.

#### Documentation

Required or anticipated artifacts:

- UI copy guidelines.
- Release review checklist.
- Boundary notice examples.

TBD:

- Final destination path for UI copy guidelines.
- Final destination path for release review checklist.
- Final destination path for boundary notice examples.
- Final destination path for review notes.
- Human assignment of `ResponsibleParty`.
- Human closure decision for `Dependencies.csv` rows whose `SatisfactionStatus` remains `TBD`.
