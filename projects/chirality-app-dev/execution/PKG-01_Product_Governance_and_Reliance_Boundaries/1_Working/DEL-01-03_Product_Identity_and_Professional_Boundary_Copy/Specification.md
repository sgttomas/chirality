# Specification: DEL-01-03 Product Identity and Professional Boundary Copy

## Scope

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

## Requirements

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

## Standards

| Standard / authority | Status | Application |
|---|---|---|
| `docs/DIRECTIVE.md` | Accessible | Governs intent, product identity, professional responsibility, evidence posture |
| `docs/CONTRACT.md` | Accessible | Governs binding copy invariants |
| `docs/SPEC.md` | Accessible | Governs runtime/document structures and future domain specification boundary |
| `docs/TYPES.md` | Accessible | Governs vocabulary for project truth, artifacts, stable IDs, and authority |
| `docs/PLAN.md` | Accessible | Governs roadmap/release copy checks |
| `docs/PRD.md` | Accessible with hash mismatch warning | Governs product requirements and accepted vNext direction; dispatch says mismatch is warning, not blocker |

## Verification

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

## Documentation

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
