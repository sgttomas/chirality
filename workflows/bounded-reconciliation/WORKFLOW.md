---
name: bounded-reconciliation
description: Reconcile a completed portion of software work with the contents of its affected deliverable folders, updating their scope descriptions, remaining work, dependencies and evidence within the assignment.
---
# Bounded reconciliation

Bring the documents in named deliverable folders into an accurate relationship
with a bounded portion of the code and its evidence. The documents must make
clear what is intended, what is implemented, what has been verified and what
remains. They may legitimately describe future work; a difference from current
code is not automatically a documentation error.

Use this separate method as a small node during local work graph traversal.
A TASK can execute it without delegation while independent implementation
continues. Its primary output is the warranted deliverable-document changes,
with unresolved differences returned to the graph. A report alone does not
complete an assignment that authorizes those document changes.

## 1. Name the deliverables and the work being reconciled

From the graph node, establish the completed capability, repair, investigation
or design decision; its affected deliverable IDs and folders; and the code,
tests and evidence to compare. Identify the stable source revision or exact
candidate, the relevant user direction, and the permitted document write scope.
Label unmerged or partially verified work accurately.

If the deliverable mapping is unclear, inspect the decomposition and local
scope to resolve it. Return an explicit mapping question when it cannot be
resolved; do not settle for a generic code-review report. Keep the assignment
small enough to inspect the affected statements and their implementation.
One deliverable or a small connected group is a useful unit; split an oversized
assignment through its parent.

## 2. Read the affected deliverable contents

Use the files that are actually current in the folder. Read the controlling
amendments before relying on older statements. Follow references needed for the
bounded comparison; avoid a whole-project documentation sweep.

| Deliverable file | What to inspect and reconcile |
|---|---|
| `ScopeOfWork.md` | The actual description of the deliverable: purpose and objective links; defined behavior and outputs; requirements and completion criteria; production/verification method; decisions, constraints and the output/evaluation matrix. Locate the specific sections or claim IDs affected by the code or newly established details. |
| Active legacy `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md` | Inspect the equivalent definition, requirements, procedure and rationale where the project still uses these files. Many deliverables consolidate them in `ScopeOfWork.md`; do not recreate retired files or update archived copies as current documents. |
| `_STATUS.md` | Compare `Remaining` items and their removal conditions with the actual result. Correct completed, partial, blocked and newly exposed remaining work. Lifecycle state and `Checking Approval SHA` retain their separate authority requirements. |
| `Dependencies.csv` and `_DEPENDENCIES.md` | Check affected prerequisite/interface claims, their target identities, satisfaction evidence and unresolved conditions. Keep both representations consistent for permitted updates; preserve stable IDs and the owning project's dependency semantics. |
| `MEMORY.md` | Read relevant decisions and prior results. Add a short material explanation or activity row when needed to preserve what changed, why and what remains; retain dated history. |
| `_REFERENCES.md` | Check sources and evidence used by the affected statements. Correct or add warranted references within scope; do not silently repin an accepted authority corpus to eliminate drift. |
| `_CONTEXT.md` | Verify deliverable identity, scope and traceability. It is not a routine progress log; amendments to its identity or decomposition basis need the corresponding authority. |

Inspect other affected review or derived files when referenced. Preserve signed,
accepted or historical records, and identify any required downstream refresh.
Reconciliation does not require touching every file in the folder.

## 3. Compare the documents with the code in both directions

First follow the affected document statements into the implementation and its
checks. Does the code provide the described behavior, enforce the constraint,
use the stated interface, and have the claimed evidence? Distinguish missing
implementation from missing verification. Identify exact sections and source
locations, rather than relying on another agent's completion summary.

Then follow the bounded code change back into the deliverable documents. Look
for new behavior, resolved design details or TBDs, changed interfaces, discovered
limitations and dependency consequences that the documents do not yet reflect.
Check relevant earlier decisions before treating a difference as a new choice.

Keep deliverable statements at the level of requirements and stable scope.
Apply the owning claim-granularity rules (Root's
`docs/DELIVERABLE_CONCORDANCE_METHOD.md` §3.1 for Chirality): a statement belongs
as a claim when changing it requires a decision, an interface relies on it, or
named verification can check it. Mechanism detail that meets none of these tests
belongs in code, tests or developer documentation, and may be cited as evidence.
For stale mechanism-level wording, prefer lifting the statement to that claim
level and moving the mechanism into evidence; a mechanism-level rewrite needs
the owning ruling's reason. Preserve decision-bound mechanisms and return
borderline classifications for the owning decision. The test does not itself
authorize a requirement change.

For each material difference, decide what follows:

- **Documentation has fallen behind:** update the current description, resolved
  details, verification account or Remaining item using the code and evidence.
- **Implementation has fallen short:** preserve the requirement and record the
  specific gap or failure as remaining work. Route code repair through the graph.
- **An adopted decision changes the intended design:** apply that decision to the
  affected sections within the assignment, retaining its basis and residual work.
- **An unapproved departure or uncertain result is discovered:** describe it
  accurately and return the precise decision, investigation or proposed edit.

Do not replace a requirement with whatever the code happens to do. Equally, do
not leave obsolete setup-only descriptions or resolved TBDs untouched merely
because they once expressed future intent. Correct the affected current text
while preserving still-unimplemented obligations and explicitly historical text.

## 4. Make and verify the warranted document changes

Edit the affected deliverable sections within the assignment. Keep scope text,
completion/evidence descriptions, Remaining items and dependency statements
consistent about the bounded result. Preserve identifiers and citations needed
to trace the change. Use the folder's existing history convention; a short
Markdown activity row can link the code revision, evidence and graph node.
Avoid repeating the same narrative across memory, status and a separate report.

A fulfilled Remaining item can be removed only when its stated condition is
supported. Record dependency satisfaction when the assignment and owning rules
permit it; a local update does not silently rebuild or amend the accepted project
DAG. Scope, lifecycle, acceptance or pinned-basis changes outside the assignment
return as precise proposals. Routine authorized factual updates need no new
human approval. Code repair is a separate work node unless explicitly included.

Before saving, compare the target with the version inspected and preserve other
contributors' edits. If the code basis changed, recheck the affected comparison
or return it as stale. Read the edited documents together, verify links and
applicable formats, and check that they neither overclaim completion nor lose
future scope. Apply required independent checking; reconciliation is not a
substitute for the implementation's review or verification.

## 5. Return the deliverable changes and remaining consequences

Return the changed files and concise supporting evidence. Where useful, use
one small table in the graph's result location or the deliverable's activity
record; no separate claim ledger is mandatory.

| Deliverable / section | Code or evidence basis | Document change | Remaining consequence |
|---|---|---|---|
| <ID, file and section> | <revision; behavior and check> | <applied edit, no change needed, or precise proposal> | <gap, dependency, decision or next graph node> |

The node completes when its bounded document comparison and permitted edits are
checked, or a supported no-change result is established, and every material
residual has a disposition. Where writes were not authorized, return the exact
proposed changes and leave their application outstanding in the graph. Missing
inputs or blocked inspection leave the affected reconciliation incomplete.
Completion of this node does not imply completion of the deliverable itself.

On interruption, inspect the actual document diff and pinned code basis before
continuing; check partial edits rather than repeating or discarding them. Return
stale evidence, owner holds and the next safe action to the graph maintainer,
who integrates the result and any follow-on nodes without overwriting concurrent
work. Keep required execution attribution separate from the document findings.
