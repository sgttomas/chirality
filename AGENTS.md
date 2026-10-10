# Chirality repository instructions

Work toward the owner's intended result within the authority given in the
conversation. Roles describe contributions; workflows supply methods. The owner
remains accountable for acceptance and reliance.

## Where work happens

| Scope | Entry | Standing |
|---|---|---|
| Root: shared instructions, workflows, skills, tools and CI | `execution/_Coordination/LOOP_INIT.md` | Work as steered |
| App v4: Chirality within applications and the workflow-authoring exemplar | `projects/chirality-app-v4/loop/LOOP_INIT.md` | Active |
| SWBPIPE: piping design and stress-model authoring | `projects/chirality-piping/loop/LOOP_INIT.md` | Active |
| App v3, Runtime, PEC | `archive/pre-docs-cleanup-1` | Frozen; no development or verification without explicit reactivation |
| `_DomainEngines/` | Owning project's instructions | Write only under a steer for that work |

## Working cycle

1. Take the objective, limits and authorization from the conversation. Do not
   reconstruct a standing backlog from archived plans or records.
2. Locate the affected deliverable or shared Root component. Read its current
   commitments and design; consult the PRD and companions for the requirements
   and interfaces this work involves.
3. Query the relevant inputs, consumers and changes. Read what this slice needs;
   do not perform a global state census. Resolve whether an input meets its
   condition from evidence and judgment, not file existence or merge status.
4. Carry authorized work through implementation, proportionate verification and
   integration. Use one coordinator for a shared result, disjoint concurrent
   writes, and owners who stay with their work through repairs.
5. Update the current ScopeOfWork, Design or dependency condition when its meaning
   changes. Apply already-authorized decisions without asking again. Leave
   unchanged declarations alone; Git preserves their history.
6. Return the usable result, checks, material findings and reserved choices.
   Stop when the agreed result is established; do not invent closeout work.

## Deliverables and records

Active project deliverables live in `execution/PKG-nn/DEL-nn-nn/`:
`ScopeOfWork.md` holds commitments and acceptance criteria, `Design/` holds useful
technical detail, and `deliverable.yaml` holds needs, conditions and code/check
pointers. The consumer states its needs; tools derive reverse links and graphs.

From the repository root, use `python3 -m tools.deliverables --project <project>`
with `neighborhood <DEL>`, `impact <DEL>`, `touches <rev|PR:n>` or
`dag-diff <tag>`. `check` reports structural errors and unresolved references.
See `tools/deliverables/README.md` for arguments and limits. Results are facts
and unknowns, not completion or acceptance claims; code paths indicate relevance,
not exclusive ownership. Never hand-maintain derived progress or lifecycle state.

Produce the work and the minimum information needed to review, use or recover
it. A record needs a concrete consumer, acceptance requirement or recovery need.
The PR states what changed, why, what was checked and what remains open; quote
the owner's words for reserved decisions. Decisions edit the text they govern,
not append registers. No routine receipts, notices, run records or handoff
chains. Keep one replaceable recovery note only where continuity needs it.

## Verification and authority

- Routine, reversible changes: inspect or exercise the result.
- Ordinary implementation: run a focused check.
- Numerical meaning, persistence, permissions or destructive operations: use
  targeted regression checks and independent scrutiny by a separate agent.
- Releases: check the actual product; release remains an owner act.

Changing an expected result to silence a failure needs a substantive reason.
Reuse applicable passing evidence; repeat checks when a change or unresolved
concern warrants it, not because work moved between agents or into a PR.

Changes to commitments or acceptance criteria, releases, risk acceptance and
explicit holds are reserved for the owner. Present an unresolved reserved choice
with its consequence. Otherwise continue authorized work; uncertainty alone does
not require another approval. Honor project fences and keep private data out of
this public repository. Required secret and private-term checks still apply.
Model and effort choices come from session steering, not repository doctrine.

### Standing Git grant

For `sgttomas/chirality` only, agents may commit, push, open, update and merge PRs
within authorized work after the verification above and required checks pass on
the exact head. Explicit holds and reserved decisions apply. This grant excludes
protection bypasses, history rewrites, force pushes, permission changes and
releases. Use `.agents/skills/chirality-change/SKILL.md` for Git conventions.

## Current contracts

Product commitments live in the project's PRD and named companions, ScopeOfWork
and Design. Consult these shared references where applicable:

- [Product boundaries](docs/PRODUCT_BOUNDARIES.md): professional accountability,
  domain ownership, protected writes and human acceptance. Frozen Runtime
  contracts apply only upon explicit reactivation.
- [Agent and workflow runtime](docs/AGENT_WORKFLOW_RUNTIME.md): product interface
  reference, only where adopted by the current product; it imports no retired
  Runtime obligations into App v4 or repository development.
- [Compatibility formats](docs/COMPATIBILITY_FORMATS.md): containment and legacy
  formats still consumed by tools.

Omission from these pointers does not supersede a live commitment or hold. If
one is found elsewhere, move it into its current home or add a relevant pointer
in the same change. Historical procedures create no new development duties.

## Roles and workflows

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | 1 | Design workflows, tools and projects with the owner |
| WORKING_ITEMS | 1 | Own implementation, assignments and integration |
| TASK | 2 | Execute one bounded assignment; does not delegate |

The person may work untyped or enter through either manager or HELP_HUMAN.
HELP_HUMAN may coordinate directly or through Type 1 managers; managers may
assign bounded TASK work. Use only the hierarchy the undertaking needs.
Load the active role's `agents/AGENT_<ROLE>.md`; other role, workflow and skill
bodies are on demand. Keep ownership of integration and route returns through
the host's actual mechanisms.

Use `workflows/coordinated-knowledge-work/WORKFLOW.md` when coordinating related
contributions into a usable result. Other methods are indexed in
`workflows/index.json`; load only a selected method and the resources needed for
the stage in hand. Select with `Workflow: <name>` or a source-qualified identity;
retain the selected origin and expose collisions rather than silently switching.
Before creating or revising a reusable workflow, follow `create-workflow`.
Product discovery and registration mechanics live in the interface reference.
