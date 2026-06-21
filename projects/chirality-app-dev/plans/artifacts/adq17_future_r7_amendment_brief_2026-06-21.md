# ADQ-17 Future R7 Amendment Brief

**Status:** Draft brief for future human ruling.
**Date:** 2026-06-21
**Queue item:** ADQ-17
**Scope:** Documentation only. This brief does not activate R7, implement domain-engine endpoints,
write protected domain paths, create domain MCP tools, apply domain operations, issue PKG-10
deliverables, or make professional, code-compliance, external-validation, solver-truth, release, or
certification claims.

## 1. Purpose

Prepare a concise future-amendment brief for R7: Domain Engine Profiles and Operation Proposals. The
brief packages the existing PKG-10 future-boundary work into a decision-ready structure so a later
human authority can decide whether, when, and how to open R7 implementation.

Current queue authority permits this document-only preparation. R7 implementation remains a hard fence.

## 2. Authority Basis

| Source | R7-relevant rule |
|---|---|
| `docs/PLAN.md` R7 | Domain profiles and operation proposals are future-amendment work after core harness stability. |
| `docs/PRD.md` R7 / FR-106..FR-115 | Future profiles, protected paths, proposal paths, operation proposal records, human gates, and boundary notices. |
| `docs/SPEC.md` Section 18 | `/api/domain/*` families are provisional future platform interfaces and must not be implemented as current-release scope. |
| `docs/CONTRACT.md` K-DOMAIN-1..4 | Domain engines own domain truth; protected paths are write-quarantined; operations require proposal records and human acceptance; no professional/code/external/solver-truth overclaims. |
| `docs/ISSUE_READINESS_PROFILES.md` Section 5 | PKG-10 uses the future-boundary/doc-only acceptance profile; doc-only acceptance does not activate R7. |
| `plans/PLAN_2026-06-20_autonomous_development_queue.md` | R7 amendment brief is eligible doc work; R7 implementation is fenced. |

## 3. Current PKG-10 Posture

PKG-10 contains five future-boundary deliverables:

| Deliverable | Current usable content | Main unresolved implementation blocker |
|---|---|---|
| DEL-10-01 `DomainEngineProfile` Contract Draft | Generic profile field contract, deterministic validation requirement, boundary-notice rule. | Operation descriptor and manifest-rule schemas remain TBD. |
| DEL-10-02 Protected Path and Proposal Path Policy | Protected/proposal path semantics and write-quarantine policy. | Concrete path syntax, profile policy enforcement, and fail-closed tests remain TBD. |
| DEL-10-03 `OperationProposal` Record and Human Gate Workflow | Proposal shape, status vocabulary, review checklist concepts. | Human acceptance evidence schema, deterministic-check payloads, and apply semantics remain TBD. |
| DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture | Future validator/fixture requirements and OpenPipeStress-as-fixture boundary. | No validator, negative fixture suite, or accepted fixture profile exists. |
| DEL-10-05 Domain Boundary Notices and Solver Truth Separation | Future copy/checklist rules separating domain truth, Chirality records, and human acceptance. | No selected future UI/API/event/profile surfaces or accepted notice artifact locations exist. |

INSP-03 found the package coherent as future-boundary documentation but not executable R7
implementation evidence. D-APP-37 established the doc-only profile. No `_STATUS.md` state transition
is authorized by this brief.

## 4. Required Human Rulings Before R7 Opens

| Ruling need | Decision question |
|---|---|
| R7 activation | Open no implementation, open doc-only refinement, or authorize a bounded implementation program? |
| Responsible owner | Who owns future domain-engine profile and operation-proposal governance? |
| First fixture | Use no fixture, OpenPipeStress as a read-only fixture profile, or another fixture? |
| Profile contract | Which `DomainEngineProfile` fields and manifest rules are accepted as machine-validated schema? |
| Protected/proposal paths | What path syntax, protected roots, proposal roots, and path-policy enforcement are accepted? |
| Operation proposal records | What proposal ID, status transitions, deterministic check payloads, and evidence paths are accepted? |
| Human acceptance | What actor/authority/timestamp/proposal-binding artifact is sufficient before an operation can be applied? |
| Apply semantics | Is operation application in scope at all, or only proposal drafting and validation? |
| Tool/API surface | Are `/api/domain/*`, `mcp__chirality__domain_*`, or UI surfaces in scope, and with what permissions? |
| Boundary notices | What notice text and review checklist are required on each selected surface? |

Any answer that authorizes implementation must be recorded as a ruling before code, endpoint, MCP,
path-policy, operation-store, adapter, or UI work begins.

## 5. Suggested Future Amendment Shape

If a human authority opens R7 later, use a bounded amendment with these sections:

1. **Scope and fences:** explicitly name what remains out of scope, especially professional approval,
   code compliance, external validation, solver-truth ownership, direct protected-path writes, and any
   current-release claim.
2. **Accepted profile schema:** define fields, required/optional status, manifest-rule structure,
   deterministic validation errors, and versioning.
3. **Protected/proposal path policy:** define path syntax, path normalization, write-quarantine
   behavior, proposal-write allowance, and test fixtures.
4. **Operation proposal record:** define `OperationProposal` schema, status transitions, deterministic
   check results, risk fields, expected outputs, and evidence storage.
5. **Human gate:** define acceptance artifact, required actor/authority, timestamp, proposal binding,
   and rejected/accepted/applied semantics.
6. **Fixture posture:** decide whether OpenPipeStress or any other engine is a fixture profile only,
   and keep engine-specific assumptions out of core runtime.
7. **Surface inventory:** list any API, MCP, UI, event, docs, and artifact surfaces selected for the
   first tranche.
8. **Validation plan:** define static, unit, integration, browser, security, and claims-review evidence.
9. **Handoff state:** record accepted upstream snapshot, derivative-package status, current blockers,
   and any deferred implementation.

## 6. Non-Implementation Work Packages For A Future Plan

These work packages are future planning units, not current authorization:

| Future package | Output | Entry condition |
|---|---|---|
| R7-A Profile schema packet | Accepted machine-readable profile schema and negative cases. | Human ruling opens profile-schema work. |
| R7-B Protected/proposal path packet | Path-policy fixture matrix and enforcement expectations. | Human ruling defines profile path syntax. |
| R7-C Operation proposal packet | Proposal record schema, status semantics, and review checklist. | Human ruling defines whether proposals are in scope. |
| R7-D Boundary notice packet | Surface-specific notice text and claims checklist. | Human ruling selects future surfaces. |
| R7-E Fixture packet | Read-only fixture profile and deterministic validation expectations. | Human ruling selects OpenPipeStress or another fixture. |

Implementation packages would require a separate ruling and are intentionally not scoped here.

## 7. Minimum Validation Bar If R7 Is Later Authorized

| Surface | Minimum evidence |
|---|---|
| Profile schema | Deterministic pass/fail tests for required fields, invalid fields, manifest rules, and version handling. |
| Protected paths | Tests proving direct protected writes fail closed and proposal-path writes remain non-binding. |
| Operation proposals | Schema tests, status transition tests, deterministic-check payload tests, and human-gate artifact binding tests. |
| API/MCP/UI surfaces | Permission overlay, hook, event, redaction, and claims-review tests before exposure. |
| Fixture profile | Negative fixtures for missing notices, overlapping paths, incomplete operations, and core-runtime coupling. |
| Boundary notices | Copy review proving no professional approval, code compliance, external validation, certification, sealing, authentication, or Chirality-owned solver-truth claim. |

If authority documents change during a later R7 amendment, run the D-APP-38 corpus `status`, then
`bump` and `apply` as required.

## 8. Stop Conditions

Stop and require a human ruling if future work would:

- implement or expose `/api/domain/*` endpoints;
- expose `mcp__chirality__domain_*` tools;
- write path hooks or policies for protected domain paths;
- create a domain operation store or apply workflow;
- add OpenPipeStress or another domain engine as a runtime dependency;
- mutate protected domain-engine truth;
- claim professional approval, code compliance, external validation, solver ownership, signing,
  sealing, certification, authentication, release readiness, publication, or distribution.

## 9. Handoff State

| Field | Value |
|---|---|
| Accepted upstream basis | Current governed docs plus PKG-10 local-kit documents and INSP-03 assessments. |
| Derivative status | This brief is derivative planning evidence, not authoritative decomposition truth. |
| Closure verdict | ADQ-17 doc-only brief complete; R7 implementation remains closed/fenced. |
| Rerun requirements | Rerun source/reference checks and D-APP-38 status before any future amendment packet changes authority docs. |
| Remaining blockers | Human rulings listed in Section 4; D-APP-40/41/42 remain unrelated active runtime decisions. |
