# Chapter 8 — Implementation and Validation

---

## 8.1 Introduction

Root's shared instructions, roles, methods, queries and integration paths are
examined at repository revision `a602024416ace9652f61bb2043889c307fd4e09d`.

The historical record has a boundary. Original January–April repositories were
deleted during migration. The owner's account describes January–March as a move
from controlling LLM outputs to having agents build code, and April as largely
quiet. Surviving migrated Git history starts with the May 18 snapshot. The
account of earlier intent is testimony, not reconstructed commit evidence.

From that basis the case shows repeated adjustment of production means. July
separated roles, methods, tools and deliverable content. August reconsidered
delegation and the separation of private knowledge from public mechanics.
September reduced specialist roles and supplier wrappers. October removed
administrative duties and their enforcement together. These changes matter to
Root because its artifacts shape the conditions under which later artifacts
are produced.

---

## 8.2 Agent Suite

### 8.2.1 Type Distribution

The current repository has four general role files:

| Role | Contribution |
|---|---|
| HELP_HUMAN | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | Make intent, methods and designs concrete |
| WORKING_ITEMS | Own implementation, assignments and integration |
| TASK | Carry one bounded assignment through its ordinary repairs; do not delegate |

The agent working with the owner holds Agent 0's responsibilities regardless
of its entry role. Other roles are available contributions. They are not
mandatory staffing positions or sequential approval stops. The role files
and [repository instructions](../../AGENTS.md) establish this distinction;
[PR #1223](https://github.com/sgttomas/chirality/pull/1223) contains the
corresponding role, workflow and resolver changes.

### 8.2.2 Responsibility and Write Scope

A role describes responsibility. Its name does not itself grant tools,
credentials or write authority. Those depend on the authorized assignment
and the host's actual permission boundary.

The earlier registry made HELP_HUMAN read-only. The revised repository
resolver retains authorized write targets for that role while denying
unauthorized targets and respecting a read-only host. Boundary tests in
PR #1223 cover absent authorization and escaping targets, including symlink
escapes. These tests establish behaviour of that resolver under the checked
conditions. They do not establish that every host or App product applies
the same policy. App v4's own role configuration remains a product contract.

This distinction matters for fault containment. An instruction to respect a
scope is an instruction; a tested path check is a mechanical control; an
operating-system sandbox has its own coverage. None should be reported as
another merely because all concern write boundaries.

### 8.2.3 Navigation and the Historical Matrix

The [Root entry](../../execution/_Coordination/LOOP_INIT.md) starts from the
shared component and its affected consumers. It does not require a global census
or a product deliverable for each tooling change. An active project entry instead
locates the affected product commitments. This division keeps shared production
work and project scope from becoming competing authorities.

Earlier App versions offered a 3×4 matrix of epistemic postures and functions.
That matrix was a navigation design, not evidence that work requires twelve
positions. It is historical product material. The present role framework
does not impose it as an execution hierarchy.

Current navigation begins with the authorized undertaking and the relevant
project or Root component. Methods are loaded when needed. This reduces
required reading without claiming that omitted context is irrelevant: an
agent must still investigate the requirements and interfaces implicated by
its work.

### 8.2.4 Decomposition and Deliverable Sources

Decomposition remains a method for making scope, interfaces and intended
results intelligible. Its output need not force all implementation through
one fixed sequence of gates. A person retains reserved commitment and
acceptance decisions; ordinary work proceeds within the authority already
given.

Active project deliverables use `execution/PKG-nn/DEL-nn-nn/` with:

- `ScopeOfWork.md` for commitments and acceptance criteria;
- `Design/` for useful technical detail;
- `deliverable.yaml` for consumer-stated needs, conditions and relevant
  code/check pointers.

Lifecycle status files and Working/Checking/Issued phase folders were
removed. The consumer declares its need once; tools derive reverse links.
The migrations preserved distinct conditions instead of collapsing every
pair of deliverables into a single readiness label. Their accounting and
baseline comparisons are in
[App v4 PR #1213](https://github.com/sgttomas/chirality/pull/1213) and
[Piping PR #1216](https://github.com/sgttomas/chirality/pull/1216).

### 8.2.5 Coordination and Continuity

The [coordinated-knowledge-work workflow](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
describes responsibility for purpose, integration, contributions and review.
One agent can perform several contributions. Delegation is justified by the
work, and TASK remains a non-delegating bounded executor.

Independent work need not wait for an unrelated unresolved branch. Shared
writes, uncertain interfaces, memory limits and integration capacity can
still justify sequencing. A dependency query discovers candidate
relationships; absence of a recorded edge does not prove independence.

Continuity comes from the conversation, current authoritative artifacts,
tool queries and Git/PR history. A replaceable recovery note is appropriate
where these do not suffice. Routine receipts, handoff chains and authored
progress graphs are no longer required. This removes repeated
representations while leaving integration ownership explicit.

### 8.2.6 Examination and Review

Review is a contribution selected for its purpose, not a permanent audit
subsystem that every change must traverse. The repository calls for
targeted regressions and independent scrutiny for consequential numerical,
persistence, permission and destructive changes. Routine reversible work
may need inspection or direct exercise only.

The person retains judgment in the thesis's committed, world-involving
sense. Agents can perform extensive reckoning, including inference,
criticism and comparison of evidence. An independent agent's examination can
improve the grounds for reliance without performing the person's act of
reliance.

### 8.2.7 Methods and Skills

Reusable methods are indexed in `workflows/index.json`; skills supply additional
selected methods. Role files do not reproduce the library. The Root
[resolver contract](../../tools/workflow_runtime/README.md) describes ordered
method selection, explicit resources and source identities. Missing or escaping
selected resources fail resolution. Omitted resources are not read.

The resolver returns hashes for the inputs it read. Those hashes identify tool
inputs; they do not prove that a host delivered that context to an agent. This
is an important Root boundary: resolving a source, delivering it, interpreting
it and applying its method are different events.

A workflow edit also has a concrete consumer path. The package supplies index
metadata; [the index builder](../../tools/validation/build_workflow_index.py)
rebuilds the catalog. Adopted App resources can be affected separately. Root's
instructions require updating actual consumers of a changed source, not sending
notices to every project or automatically synchronizing independent product text.
The useful evidence is the saved source, selected identity, affected consumer and
appropriate check of that connection.

---

## 8.3 Deterministic Tools

### 8.3.1 Query and Validation Operations

The current [deliverable CLI](../../tools/deliverables/README.md) exposes
`neighborhood`, `impact`, `touches`, `dag-diff` and `check`. It reports source
locations and the basis observed, including working-tree changes. It writes
no generated project register.

`neighborhood` exposes direct inputs and consumers; `impact` follows
downstream relationships; `touches` maps a change to relevant deliverables;
`dag-diff` compares declarations with an identified baseline. Code mappings
indicate relevance, not exclusive ownership. Missing mappings remain visible.

`check` rejects malformed data and invalid or escaping identities/paths.
Unresolved suppliers, planned paths and cycles are reported without being
treated as automatic execution failures. Non-gating relationships may form
cycles legitimately. The checker does not decide whether an input is suitable.

### 8.3.2 The Boundary of Mechanical Evidence

Deterministic operations can traverse files, compare revisions, resolve
paths, calculate numerical results and check defined predicates. Their
outputs remain bounded by the inputs and predicates. A present file is not
a fulfilled need; a merged PR is not acceptance; a green suite is not
engineering approval.

Agents use these facts in reckoning about meaning, suitability and next
actions. A person exercises judgment in setting the purpose and deciding
what to stand behind. Neither activity is replaced by adding another status
column.

### 8.3.3 Tool Development by Demonstrated Need

The former list of future tools assumed that every declared lifecycle rule
should eventually become automated. That is no longer the development
principle. A tool is justified by a current consumer, a useful operation or
a consequential failure it can detect. Retiring an unnecessary duty can be
better than implementing its remaining validator.

This does not preclude more automation. It changes the burden of argument:
the proposed mechanism must have a benefit in actual work, including its
maintenance and attention costs.

---

## 8.4 Root Consumers and Successive Derivation

### 8.4.1 Architecture and Successive Derivation

The App is Root's first workflow-authoring exemplar. It provides a concrete
setting for working with conversations, requests, methods and returned work.
Its [PRD](../../projects/chirality-app-v4/docs/PRD.md) and
[architecture](../../projects/chirality-app-v4/docs/ARCHITECTURE.md) define the
current adoption; Root's instructions do not automatically become its product
behaviour. The [App thesis](../../projects/chirality-app-v4/docs/thesis/README.md)
examines that application-specific argument.

Earlier Apps and Runtime are recoverable through
[the frozen-product references](../../projects/FROZEN.md), not current
verification targets. [PR #1224](https://github.com/sgttomas/chirality/pull/1224)
removed App v3, Runtime and PEC from the working tree after accounting for
active consumers.

This is a concrete test of re-derivation. Root must permit authors to revisit
implementation while preserving current commitments and useful lessons. The
histories of v2 and v3 include both evolution and redesign; v4 also identifies
reuse candidates. A new PRD and version number do not prove that learning was
retained. Existing tests, native-use findings, interfaces and owner decisions
must be examined for their current relevance.

### 8.4.2 Application Actions and Navigation

App v4 develops conversations, request cards, workflow authoring, trial runs
and inspection of returned work. Those are useful product activities, not
proof of a universal agent organization. Its first reported native witness
exposed role-header accumulation and input-autocorrection defects that were
repaired in [PR #1240](https://github.com/sgttomas/chirality/pull/1240).

That observation supports the value of exercising the actual application.
It does not establish general usability or the absence of other defects.

### 8.4.3 The Domain Application: SWBPIPE

SWBPIPE supplies a domain consumer with substantially different demands. Its
[PRD](../../projects/chirality-piping/docs/PRD.md) distinguishes physical models,
analytical models, analysis runs, comparison and handoff. Those objects are not
created by assigning a Root role or applying a generic workflow. They require
piping-domain definitions, numerical implementation and domain evidence.

The [SWBPIPE thesis](../../projects/chirality-piping/docs/thesis/README.md)
examines that instantiation. The relevance to Root is the transfer question:
can useful methods, discovery and human–agent responsibility relationships be
adopted while the application owns its domain operations and validation? Shared
schemas and repository residence establish neither successful integration nor
professional suitability.

SWBPIPE is therefore a candidate instance of proliferation at the application
category, rather than evidence that a general-purpose Root engine can supply
all domain meaning. Its results must be assessed independently.

### 8.4.4 Host Integration and Human Acts

The [host-integration contract](../../projects/chirality-app-v4/docs/HOST_INTEGRATION.md)
proposes discoverable application capabilities that can support human and
agent access. A shared catalog does not automatically supply good interfaces,
correct domain behaviour, safe recovery or every transport adapter.

The App's process-placement ruling in
[PR #1244](https://github.com/sgttomas/chirality/pull/1244) assigns file and
record writes, supplier interaction and capture of human acts to the Rust
host, while the web view presents and sends human-initiated requests. The
ruling is a product commitment. Its text alone does not establish that all
implementation paths already conform or that a recorded act constitutes
professional authentication.

---

## 8.5 Validation

### 8.5.1 What the Reset Examined

The October reset changed duties and enforcement together. It retired
administrative validators, migrated dependency declarations, relocated live
conditions before archiving records, and accounted for maintained readers.
Independent reviews identified real omissions during that work, including
technical conditions and frozen numerical references that still had consumers.
The repaired PRs are evidence of examination and correction, not proof that
the migration was complete merely because it was scripted.

The key changes are documented in
[PR #1212](https://github.com/sgttomas/chirality/pull/1212),
[PR #1213](https://github.com/sgttomas/chirality/pull/1213),
[PR #1216](https://github.com/sgttomas/chirality/pull/1216), and the archive
batches. Recoverable Git tags preserve the prior material without making
it a current development obligation.

### 8.5.2 Verification Selection and Result Reuse

The [CI selection reference](../CI_SELECTION.md) defines `harness` as the
single required aggregate result for repository checks and selected active
product workflows. Selection and failure propagation are separate concerns:
unrelated jobs can be skipped explicitly, while a selected failed, cancelled
or missing job must prevent the aggregate from passing.

[PR #1214](https://github.com/sgttomas/chirality/pull/1214) revised the checks
according to consequential behaviour and exercised their selection.
Subsequent result reuse distinguishes an exact applicable prior pass from
a dependency/build cache. A reused result states that no new tests executed.
Manual runs can obtain fresh evidence. These are bounded evidence-management
mechanisms, not a general exemption from examination after change.

### 8.5.3 Connecting Evidence and Its Limits

Three source paths illustrate what Root's evidence can establish:

1. **Role and permission change.** PR #1223 coupled HELP_HUMAN's authorized-write
   interpretation with the resolver and boundary tests. It removed one role-name
   restriction without treating absent authorization as unrestricted access.
2. **Dependency migration.** PRs #1213 and #1216 compared source rows with
   migrated conditions and accepted graph bases. Independent review examined
   meaning, not merely the migrator's own counts. This supports preservation on
   the examined basis; it does not turn `check` into a semantic validator.
3. **Archive integration.** Reviews of the archive batches identified live
   technical references and contracts among intended removals. Relocation and
   consumer repair were necessary even though the generated product results were
   already committed. A green product test alone would not establish that the
   next generator invocation remained usable.

App native-use findings in
[PR #1240](https://github.com/sgttomas/chirality/pull/1240) provide a further
limit: Root's production method can yield an assembled product that still
contains defects revealed by actual interaction. The appropriate response was
product repair, not another generic governance layer.

These observations support concrete production and correction. They do not
establish comparative productivity, professional review quality, regulatory
compliance or portability. Their value lies in the identified claim and
consumer, not the volume of artifacts produced.

---

## 8.6 Current State and Implementation Gaps

### 8.6.1 Implemented and Exercised

At the stated basis, repository instructions, four role files, selected
methods, deliverable-local source documents and the query CLI are in use.
The relevant Git and CI paths have been exercised through the reset and
subsequent development. App v4 and SWBPIPE contain working product
increments. The accepted manuals describe the revised working model
([PR #1238](https://github.com/sgttomas/chirality/pull/1238)).

These are identifiable implementations. Their presence should not be
reported as an undifferentiated state of being fully validated.

### 8.6.2 Properties, Mechanisms and Residual Dependence

| Property sought | Current mechanism | What remains to assess |
|---|---|---|
| Authorized writes | Assignment, resolver/path checks and host permissions | Coverage of each actual entry path and host boundary |
| Useful continuity | Current artifacts, conversation, Git and bounded recovery support | Recovery after interruption without lost or duplicated work |
| Relevant context | Consumer needs and on-demand graph queries | Missing declarations and semantic suitability of inputs |
| Dependable integration | Continuing ownership, selected checks and review | Unchecked interactions and common mistaken assumptions |
| Attributable reliance | Human decisions and identified subject/scope where required | Whether the person's engagement is competent and substantive |

The final column is not a list of obligations to build more machinery.
Some limitations call for better product behaviour, others for focused
examination, clearer communication or human practice. No mechanical trace
compels genuine judgment.

### 8.6.3 Candidate Investigations

Root's most relevant investigations concern its connecting paths: whether an
agent finds the governing condition without reconstructing global history;
whether an instruction change reaches the actual resolver or selected method;
whether a reviewer receives the candidate and relevant basis; and whether an
interrupted undertaking resumes without losing work or repeating an uncertain
write.

The outcomes should be assessed against usable work, consequential errors and
total effort, including owner attention. Expanded metadata, another catalog or
another validator is only one possible response to a finding. Retiring an
unnecessary duty or clarifying the current source may be better.

Application-specific product activities and numerical investigations belong to
the App and SWBPIPE research questions. These examples create no standing backlog
or new authority for Root.

### 8.6.4 Summary Assessment

The implementation supports feasibility of several mechanisms and shows
that some earlier mechanisms were dispensable in the examined work. It
does not prove that the surviving arrangement is optimal, that every
contract is mechanically enforced, or that a domain professional can adopt
it without its author's assistance.

The October removal of duties is evidence against their necessity for
every undertaking. Its causal effect cannot be isolated from stronger
models, accumulated product knowledge, work begun earlier and the owner's
continued involvement. File counts, line counts and merged-PR totals are
measures of repository activity or size, not productivity estimates.

---

## 8.7 Summary

The case demonstrates a Root environment that can help produce work and revise
its own production means. Current source documents, queryable needs, selected
methods, assignment-specific authority and continuing integration ownership
replace several earlier repeated representations. Their operation is traceable
to maintained sources and examined changes.

The reset did not make Root an autonomous authority over its applications.
Owners retain judgment and reserved commitments; host permissions remain real
limits; products adopt shared methods according to their own contracts. The
App and SWBPIPE expose different tests of whether the environment serves useful
work.

Historical mechanisms remain evidence about learning, including mistaken claims
of necessity. Root's own method is credible to the extent that contrary findings
can change the current means without erasing the distinctions and responsibilities
that justified them.
