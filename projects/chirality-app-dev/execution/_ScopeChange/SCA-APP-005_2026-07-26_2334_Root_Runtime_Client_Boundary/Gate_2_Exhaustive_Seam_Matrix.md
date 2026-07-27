# Gate 2 Exhaustive Runtime-Seam Matrix

**Amendment:** `SCA-APP-005`
**Status:** `REVISION_2_RECONCILED_PENDING_OWNER_EXPANSION_RULING`
**Basis:** `main@fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`
**Authority basis:** D-GOV-20, D-GOV-28 / Root PRD O-11, accepted Root
decomposition revision 1.1, D-APP-73
**Effect:** read-only impact classification; no authoritative amendment

## Boundary rule used for classification

Root owns generic runtime semantics and the generic runtime's operational
state: contracts, orchestration, daemon, client and CLI protocols, safe
adapters, engines, credentials, sessions, delegation, tools, turn locks,
interruption, model residency, and associated operational records.

App remains a client and retains its separately governed responsibilities:
Electron daemon-mode packaging and safeStorage boundary participation,
project-specific adapter and deterministic acts, project identity and
checkout-contained authority/evidence, client integration and compatibility,
user presentation, human gates, client-side conformance, and acceptance
evidence. A Root transport or daemon operation does not acquire App or project
authority.

This matrix classifies ownership language. It does not decide the exact
credential, adapter, event-record, or delegation/tool partition where the
ruled sources do not yet supply one unambiguous sentence.

## Eight-seam coverage

| Generic runtime seam | Direct decomposition impact | Preserved App-side boundary | Residual |
|---|---|---|---|
| Engines | Client/adapter/conformance wording in PKG-03 and PKG-04 | provider-specific client integration, compatibility, evidence | U2 |
| Credentials | PKG-04 credential and settings wording | Electron daemon-mode safeStorage boundary participation and UI | U1 |
| Sessions | PKG-03/05 lifecycle, persistence, migration, and linkage wording | client projection, compatibility, project evidence | U3 |
| Delegation | PKG-08 execution and child-record wording | project authority, briefs, gates, AgentRun evidence | U4 |
| Tools | PKG-06/08 generic mediation and execution wording | project-specific deterministic acts, policy inputs, human gates | U4 |
| Turn locks | PKG-03 lifecycle/lock wording | client request/observation and conformance | none |
| Interruption | PKG-03 lifecycle/terminal wording | client signal forwarding, presentation, evidence | none |
| Model residency | PKG-04 activation/status/settings wording | client request/status presentation and conformance | U2 |

The Root-only CLI seam was also checked. It introduces no App product scope;
see U5.

## Complete direct `MODIFY` set

### Scope items — 31

`SOW-009`, `SOW-010`, `SOW-011`, `SOW-012`, `SOW-014`, `SOW-015`,
`SOW-016`, `SOW-018`, `SOW-019`, `SOW-020`, `SOW-021`, `SOW-037`,
`SOW-038`, `SOW-039`, `SOW-041`, `SOW-044`, `SOW-045`, `SOW-046`,
`SOW-047`, `SOW-049`, `SOW-051`, `SOW-052`, `SOW-053`, `SOW-055`,
`SOW-056`, `SOW-057`, `SOW-058`, `SOW-059`, `SOW-061`, `SOW-062`,
`SOW-063`.

Each modification is limited to distinguishing Root-owned generic runtime
semantics/operations from App-owned client, adapter, project-authority,
presentation, conformance, and acceptance-evidence duties. Status and mappings
do not change.

### Packages — 5

`PKG-03`, `PKG-04`, `PKG-05`, `PKG-06`, `PKG-08`.

The package descriptions and scopes require an explicit client boundary so
their unchanged member deliverables cannot be read as transferring generic
runtime ownership to App.

### Deliverables — 17

- `DEL-03-01`, `DEL-03-02`, `DEL-03-04`
- `DEL-04-01`, `DEL-04-02`, `DEL-04-03`, `DEL-04-05`
- `DEL-05-01`, `DEL-05-02`, `DEL-05-03`, `DEL-05-05`
- `DEL-06-01`, `DEL-06-02`, `DEL-06-05`, `DEL-06-06`
- `DEL-08-04`, `DEL-08-05`

The deliverable IDs, mappings, context envelopes, and lifecycle state remain
unchanged. Only their expected work-product boundary is qualified.

### Objectives — 5

`OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-007`.

The objective mappings remain unchanged; wording is qualified so the
objectives describe App client, adapter, authority, conformance, and evidence
outcomes rather than ownership of generic runtime semantics.

### Cross-cutting decomposition prose

The disposition is row-specific. Contiguous line ranges are not an
authorization to edit unaffected rows.

| Section | `MODIFY` | `NO_CHANGE` |
|---|---|---|
| Intake | accepted-basis lines 85 and 87 | line 83, section heading, and separators |
| Hard constraints | lines 94, 96, 107 | lines 91–93, 95, 97–106, 108–110 |
| Vocabulary | `Runtime Audit Mirror`; `AgentEnginePort`; `EngineAdapter`; `Provider Adapter`; `Pi Adapter`; `oMLX Provider`; `Capability Policy`; `TurnEngine`; `HarnessEvent`; `SdkOptionsBuilder`; `ChiralityPermissionOverlay`; `Hook`; `ToolResultStore`; `SubagentGovernanceBridge`; `SessionRecord`; `HarnessSubagentRun`; `SDK built-in tool`; `canUseTool` | `Chirality App`; `Instruction Root`; `Working Root`; `Project Truth`; `SDK Transcript`; `Pi Pattern Corpus`; `Explicit Deny Precedence`; `UIEvent`; `PersonaComposer`; `Chirality MCP Tool`; `HarnessPermissionDecision`; `allowedTools`; `disallowedTools`; `Epistemic Label`; `CoordinationRepresentation`; `DomainEngineProfile`; `OperationProposal`; `OpenPipeStress fixture` |
| Invariant-family coverage | `K-PRD/K-HIER/K-ID/K-PATH/K-FS/K-GIT/K-NOMEM` row at 506 only as to PKG-05 session/event state; `K-CORE/K-ENGINE/K-RELIANCE/K-SDK` at 509; `K-EVENT` at 510; `K-PERM/K-TOOL/K-MCP/K-HOOK/K-PATH/K-BASH` at 511; `K-WRITE/K-SEAL/K-GHOST/K-SUBAGENT` at 513 | rows 507, 508, 512, 514, 515 |
| Binding/roadmap notes | SPEC note at 519; TYPES note at 523; PLAN overlay at 527 | headings and unaffected explanatory prose |
| Acceptance checklist | SPEC conformance at 542; TYPES conformance at 543 | rows 535–541 and 544–546, including PLAN sequencing at 544 |
| Open issues | `OI-002`, `OI-006`, `OI-007` | `OI-001`, `OI-003`, `OI-004`, `OI-005` |
| Downstream notes | accepted-basis lines 607 and 611 | every other downstream note |
| Decision/history | add `DEC-021` and a dated SCA-APP-005 change-log entry | preserve `DEC-005`, `DEC-017`, `DEC-018`, `DEC-019`, `DEC-020`, and all historical change-log entries |

Line references identify accepted-basis anchors; exact Gate-3 prose must use
semantic anchors and a deterministic concordance check rather than relying on
line numbers after edits.

## Complete direct `NO_CHANGE` set

### Scope items — 37

`SOW-002`, `SOW-005`, `SOW-006`, `SOW-007`, `SOW-008`, `SOW-013`,
`SOW-017`, `SOW-022`, `SOW-024`, `SOW-025`, `SOW-026`, `SOW-027`,
`SOW-028`, `SOW-029`, `SOW-030`, `SOW-031`, `SOW-032`, `SOW-033`,
`SOW-034`, `SOW-035`, `SOW-036`,
`SOW-040`, `SOW-042`, `SOW-043`, `SOW-048`, `SOW-050`, `SOW-054`,
`SOW-060`, `SOW-064`, `SOW-065`, `SOW-072`, `SOW-073`, `SOW-074`,
`SOW-075`, `SOW-076`, `SOW-077`, `SOW-078`.

These already state an App presentation, project-specific deterministic act,
client compatibility, human-authority, validation, or boundary duty; or they
are unaffected mappings/constraints. Their unchanged text is governed by the
clarified package boundary and does not transfer generic runtime ownership.

### Deliverables

- `DEL-01-02`
- `DEL-02-02`, `DEL-02-04`, `DEL-02-05`
- `DEL-03-03`
- `DEL-04-04`
- `DEL-05-04`
- `DEL-06-03`, `DEL-06-04`
- all PKG-07 deliverables
- `DEL-08-01`, `DEL-08-02`, `DEL-08-03`
- all PKG-09 deliverables

PKG-07 remains App/project-owned because its filesystem, dependency, and
lifecycle tools are project-specific deterministic acts constrained by Root
transport, not generic runtime tools. PKG-09 remains validation and evidence,
not generic runtime implementation ownership.

## Context metadata parity — 25 files

Update package-scope metadata in every existing `_CONTEXT.md` under:

- all 4 PKG-03 deliverables;
- all 5 PKG-04 deliverables;
- all 5 PKG-05 deliverables;
- all 6 PKG-06 deliverables;
- all 5 PKG-08 deliverables.

The 17 directly modified deliverables receive deliverable-specific boundary
wording. The other 8 receive package-boundary parity only. No lifecycle,
dependency, provenance, estimate, or task-state field changes.

## Unresolved clauses for the Gate-3 candidate

| ID | Clause requiring exact treatment | Required Gate-3 posture |
|---|---|---|
| U1 | Credential ownership and the Electron safeStorage boundary | Transcribe D-GOV-20 items 2–3; do not invent a Root-contract/App-storage split. Surface any remaining presentation/custody ambiguity as `PROPOSED`. |
| U2 | Generic runtime adapter ownership versus private/project provider-adapter contribution, including model residency | Preserve Root ownership of generic adapters and residency; state App client integration/conformance duties. Any private-adapter contribution rule not already ruled is `PROPOSED`. |
| U3 | Daemon operational event/session records versus checkout-contained project authority and acceptance evidence | Preserve daemon operational records and App/project canonical authority/evidence. Do not call either the other's canonical record. |
| U4 | Daemon execution of delegation/tools versus App/project authorization, deterministic acts, human gates, and child-run evidence | Preserve generic execution in Root and authority in the project/App. Do not let transport grant authority or let App claim generic execution. |
| U5 | Root CLI | Record `NO_CHANGE` for App scope. The Root CLI does not create an App deliverable or implementation duty. |

Exact Gate-3 amendment prose may be drafted only after this envelope passes an
independent eight-seam backcheck and the owner accepts the expansion.

## Independent backcheck

A first read-only adversarial pass confirmed the initial envelope:

- the then-listed 29 direct scope-item modifications;
- the five package modifications;
- the then-listed 15 direct deliverable modifications;
- all five objective modifications;
- all 25 context-parity writes;
- the complete `NO_CHANGE` sets; and
- U1–U5 as unresolved clauses that Gate 3 must preserve rather than decide.

The fresh independent backcheck found bounded corrections. `SOW-054` remains
`NO_CHANGE` as the checkout-contained structured approval/evidence record.
`SOW-056` is `MODIFY` because its unqualified `tool.permission` persistence
crosses daemon operational events and checkout-contained App/project
approval evidence. `SOW-062` is `MODIFY` because it combines daemon-owned
generic Bash execution, interruption, and operational audit with App/project
policy and human authorization. Consequently `DEL-05-03` and `DEL-06-05`
also require direct boundary wording. Revision 2 also replaces blanket
cross-cutting ranges with the row-level dispositions above and completes the
PKG-07/08/09 `NO_CHANGE` inventory.

A final adversarial reconciliation agreed with those corrections using the
accepted source:

- D-GOV-20 line 21 assigns generic tools, interruption, sessions, and runtime
  operations to the daemon; line 24 classifies daemon state as operational
  while keeping approvals and acceptance evidence checkout-contained; and
  lines 44–45 preserve project-specific deterministic acts and human gates.
- App SOW rows 216/440 require `tool.permission` persistence, so `SOW-056`
  must distinguish daemon operational events from App/project approval
  evidence.
- App SOW rows 222/446 and `DEL-06-05` combine Bash timeout, capture,
  interruption, and audit with policy; they therefore require a client/policy
  boundary while generic execution stays with the daemon.
- `DEL-05-03` currently claims redaction into generic runtime records and
  therefore requires App-side source/presentation/conformance wording under
  Root's continuing security stewardship.
- Intake line 83 and acceptance row 544 remain `NO_CHANGE`: they state App
  identity/evidence posture and sequencing, not generic runtime ownership.
- `SessionRecord` is `MODIFY`; `Explicit Deny Precedence` is `NO_CHANGE`.

The reconciled Revision 2 envelope supersedes the earlier 29-SOW/15-deliverable
gate. That earlier count remains visible here only as review lineage.

## Topology and lifecycle invariants

- 78 scope items, 10 packages, 51 deliverables, and 10 objectives.
- No stable ID, status, mapping, context envelope, lifecycle state, package
  membership, or deliverable membership changes.
- No scope item, package, deliverable, or objective is added or removed.
- All authoritative decomposition registers remain unchanged until Gate 5.

## Deferred surfaces

This SCA does not modify ScopeOfWork contracts, statuses, dependencies, pins,
implementation, Root or App PRDs, source corpora, D-APP-48/49 evidence,
APP-HOLD-1, compatibility-retirement state, method standards, or UI/API
semantic-parity work. Those remain separately governed downstream work.

Boundary notices to Root, Tier-0, and PEC are propagation outputs of this SCA.
They are coordination only: they convey what changed and route follow-on work
without adopting scope or authority in the receiving loop.
