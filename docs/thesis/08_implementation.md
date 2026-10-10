# Chapter 8 — Implementation and Validation

---

## 8.1 Introduction

Chirality is a developing family of implementations, not one completed agent
operating system. This chapter examines what the repository demonstrates,
which mechanisms changed, and what remains a design intention. The account
is bounded by the repository at `510f4a9abc` on 2026-10-10. Later product work
must be assessed on its own candidate and evidence.

Three kinds of statement must remain distinct:

| Kind | Example | What would support it |
|---|---|---|
| Normative commitment | A person retains responsibility for acceptance and reliance | The declared allocation of authority and its justification |
| Design hypothesis | Current artifacts and on-demand queries reduce contradictory descriptions of work | An implemented arrangement and examination of its failure modes |
| Empirical finding | A particular native-use exercise exposed a particular interface defect | The identified exercise, result and repair |

Implementation establishes that a mechanism can be built. A passing test
supports a bounded claim about its behaviour. Neither establishes that the
whole framework improves professional practice or satisfies a regulator.

The development history also has an evidential boundary. The original
January–April repositories were deleted during migration. The owner's
retrospective account describes January–March as a move from building code
to control LLM outputs toward having agents build code, with April largely
quiet. Surviving migrated Git history begins with the May 18 snapshot. The
earlier account is testimony about intent and sequence, not reconstructed
commit evidence.

The surviving history shows successive revisions rather than a steady
accumulation of controls: July separated standards, roles, methods and tools;
August reconsidered delegation authority and the separation of private
domain knowledge from public mechanics; September simplified roles and
supplier integration and established the App v4 direction; October retired
administrative duties together with the mechanisms enforcing them. The
current implementation therefore differs materially from the historical
mechanisms catalogued in Appendix A.

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

Reusable methods are indexed in `workflows/index.json`; repository skills
have their own selected entry points. Roles do not have to reproduce the
method library. The separation lets one bounded executor use different
methods, and lets a manager work directly when delegation adds no value.

This is an implemented information-access arrangement, not evidence that
all methods are useful or that every agent selects them correctly. Their
value must be examined in the undertakings that consume them.

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

## 8.4 Desktop Application

### 8.4.1 Architecture and Successive Derivation

App v4 is the workflow-authoring exemplar for Chirality within applications.
Its current [PRD](../../projects/chirality-app-v4/docs/PRD.md) and
[architecture](../../projects/chirality-app-v4/docs/ARCHITECTURE.md) select
Tauri/React and direct App-owned hosting of a pinned stock Codex App Server.
They distinguish shared interface meanings from shared process topology.

Earlier Apps and Runtime remain recoverable through
[the frozen-product references](../../projects/FROZEN.md). They are not
current validation targets.
[PR #1224](https://github.com/sgttomas/chirality/pull/1224) removed the
App v3, Runtime and PEC working trees after accounting for active consumers.

The succession illustrates re-derivation from requirements and accumulated
learning. It is not deterministic compilation from a PRD. The histories of
v2 and v3 include both redesign and evolution; v4 also identifies reuse
candidates. Requirements, observed behaviour, supplier capabilities and
owner interpretation jointly inform each implementation.

### 8.4.2 Application Actions and Navigation

App v4 develops conversations, request cards, workflow authoring, trial runs
and inspection of returned work. Those are useful product activities, not
proof of a universal agent organization. Its first reported native witness
exposed role-header accumulation and input-autocorrection defects that were
repaired in [PR #1240](https://github.com/sgttomas/chirality/pull/1240).

That observation supports the value of exercising the actual application.
It does not establish general usability or the absence of other defects.

### 8.4.3 The Domain Application: SWBPIPE

SWBPIPE is an analysis-grade piping design engine and stress-model
authoring environment. Its
[PRD](../../projects/chirality-piping/docs/PRD.md) distinguishes the physical
model, analytical model, analysis run, comparison and handoff. Human and
agent routes are intended to reach common validated operations.

This is a stronger domain test than workflow authoring alone. Numerical
meaning, units, geometry, persistence and private data introduce concrete
constraints. A common operation engine can reduce divergence between human
and agent paths; the receiving interfaces and connected activity must still
be implemented and examined. Product development is not evidence of
professional qualification or code-compliance certification.

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

### 8.5.3 Project Evidence and Its Limits

The repository contains substantial App and SWBPIPE implementation,
independent reviews, regression checks and repairs. Three observations are
especially informative:

1. The role/write-policy change in PR #1223 coupled instructions with the
   resolver and tested both useful authorization and refusal boundaries.
2. The native App exercise in PR #1240 found defects through use of the
   assembled product.
3. [PR #1245](https://github.com/sgttomas/chirality/pull/1245) implemented
   the first phase of workflow-trial support; it did not establish delivery
   of every remaining trial interaction.

These observations demonstrate concrete production and correction. Earlier
example project trees similarly demonstrate that methods were exercised.
Neither type of evidence establishes comparative professional review
quality, regulatory compliance, portability or sustained productivity gains.

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

Useful next investigations follow observed needs: complete product
activities; reliable discovery of current conditions; recovery from actual
interruptions; avoidable build and numerical-check waits; and one connected
SWBPIPE operation through human and agent routes. Domain retrieval should
be examined against a concrete engineering question and its source limits.

These are research and development candidates, not a standing backlog
created by this thesis. Current product authorization remains elsewhere.

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

The case demonstrates a revisable implementation of the framework's four
questions. Relevant objects and relationships are represented in current
artifacts; tools expose bounded facts; agents perform substantial reckoning
and action within authority; people retain situated judgment and reserved
commitments. Continuing ownership connects production to repair and use.

The historical mechanisms are useful evidence about design, including its
costs and failed assumptions. Their retirement does not erase the learning.
It shows why a framework for accountable work must permit its own means to
be examined and replaced.
