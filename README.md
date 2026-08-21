# Chirality

Chirality is an open environment for organizing sustained work between humans and AI agents.

It lets people express agents as durable roles—not merely one-time prompts—and gives those agents explicit responsibilities, methods, tools, context, permissions, and relationships to other agents. Work is preserved in ordinary files so that it can be inspected, reviewed, resumed, and revised without depending on a model’s memory or a particular chat session.

Chirality is intended for technical and professional work where evidence, scope, accountability, and continuity matter: engineering, design, construction, research, technical publishing, project delivery, and complex software development.

Its purpose is not to make AI authoritative. Its purpose is to make AI useful while keeping the basis for human judgment visible.

> Agents propose and produce drafts.\
> Deterministic tools compute and check.\
> Humans decide what is accepted and what may be relied upon.

## Why Chirality exists

AI agents can produce a remarkable amount of plausible work. Plausibility alone is not enough for consequential decisions.

Technical work often requires answers to questions that ordinary agent interfaces do not preserve well:

- What was the agent asked to do?
- Which sources and project state did it use?
- What was observed directly, inferred, proposed, or left unknown?
- What was the agent permitted to change?
- Which work depended on which earlier decisions?
- What was checked deterministically?
- What did a human actually accept?
- Can another person or agent resume the work without relying on hidden chat context?
- If an input changes, which conclusions and deliverables need to be revisited?

Chirality treats these as architectural questions rather than matters of prompting etiquette.

The shared record is the filesystem. Project structures, scopes, dependencies, evidence, decisions, working notes, review findings, snapshots, and handoffs are stored in human-readable, version-controlled files. If an important decision or state change has not been recorded there, it does not exist for purposes of later reliance.

Git records versions and transports changes. A commit is not, by itself, professional acceptance or a lifecycle approval.

## The basic workflow

Most Chirality workflows follow the same broad pattern:

```text
Human intent and source material
        ↓
Structured decomposition
        ↓
Bounded work packages and briefs
        ↓
Agent execution and deterministic checks
        ↓
Review, conflict resolution, and human decisions
        ↓
Accepted snapshots and explicit handoffs
```

### 1. Understand and decompose

The source may be a project scope, a product idea, a body of technical literature, an existing design, or a software repository.

Chirality normalizes that material into stable, reviewable units. It then organizes those units into bounded areas of responsibility:

- projects are divided into packages and deliverables;
- software products are divided into packages and implementation deliverables;
- knowledge domains are divided into categories and knowledge types.

The decomposition is reviewed at human gates. Missing information remains visible as `TBD`; ambiguity is not silently filled with an agent’s best guess.

### 2. Define bounded work

A manager prepares a brief that states:

- the objective;
- the accepted input state;
- the files and context that may be read;
- the files that may be written;
- the tools and methods that may be used;
- the expected outputs;
- the required checks;
- and the conditions that require escalation.

This turns a broad intention into a task that can be executed and independently reviewed.

### 3. Execute through agents, skills, and tools

Agents perform work requiring interpretation and judgment within their assigned boundaries.

Skills provide reusable methods for recurring task shapes, such as source extraction, research, scope writing, decomposition review, software diagnosis, or deliverable consistency checking.

Tools perform deterministic operations such as:

- validating schemas and identifiers;
- calculating dependency closure;
- extracting structured data;
- comparing snapshots;
- checking path containment;
- assembling reports;
- routing affected tests;
- and verifying that required evidence exists.

A tool does not acquire judgment merely because an agent invokes it. An agent does not acquire authority merely because it can call a tool.

### 4. Review and decide

Agent output remains candidate work until it passes the appropriate review and human decision gates.

Conflicting sources are surfaced rather than silently reconciled. Consequential decisions remain with the human project authority or responsible professional.

### 5. Preserve the result

Important phase boundaries end in durable records:

- accepted source or decomposition snapshots;
- decision records;
- review findings and dispositions;
- regenerated derivative packages;
- unresolved blockers;
- rerun requirements;
- and a handoff naming the next responsible party.

The objective is for work to remain understandable after the originating agent session has ended.

## Humans and agents

Chirality uses a small hierarchy of responsibility:

```text
Human ↔ Supervising Architect → Manager → Specialist
```

### Human

The human establishes purpose, scope, priorities, constraints, and decision rights. Humans resolve consequential conflicts and decide what is accepted.

Professional responsibility remains personal and non-transferable. No agent may certify, seal, approve, or issue professional work for reliance.

### Supervising Architect — Agent 0

`HELP_HUMAN` coordinates work that crosses several managers or packages. It aligns the work with the human, maintains the overall work graph, routes discoveries between managers, and validates their combined return.

It is an optional supervisory layer, not a mandatory gateway.

### Managers — Agent 1

Managers own complete workflows such as:

- project, software, or domain decomposition;
- package-level production;
- research;
- scope change;
- review and evaluation;
- source conversion;
- drawing or equation extraction;
- publication;
- reconciliation;
- and controlled Git change.

A human may work directly with any appropriate manager.

### Specialists — Agent 2

A specialist performs one bounded objective from a sealed brief. It may use a reusable skill or operate as a purpose-specific generalist. It does not create another delegation hierarchy.

This structure is about responsibility and authority, not about pretending that different model sessions are different people.

The live agent index and runtime rules are in [`AGENTS.md`](AGENTS.md).

## Evidence and uncertainty

Chirality does not treat all statements as equally warranted.

Non-trivial claims should make their status visible:

- **FACT** — directly supported by identified evidence;
- **ASSUMPTION** — a reasoned inference that still requires validation;
- **PROPOSAL** — a suggested course of action requiring a decision;
- **TBD** — information that is missing or cannot yet be justified.

When sources disagree, the disagreement is recorded with the competing evidence and routed for human resolution.

When information is missing, the gap is preserved. Agents should not silently invent values merely to make a document appear complete.

These mechanisms do not prove that a claim is correct. They make its basis and limitations visible so that a qualified person can review it efficiently.

## Working roots and instruction roots

Chirality separates the rules governing agents from the material on which they work.

The **instruction root** contains the shared agent system:

- agent roles;
- skills;
- deterministic tools;
- governance;
- runtime contracts;
- and validation machinery.

A **working root** contains the state of a particular project or knowledge domain:

- source material;
- decomposition;
- deliverables;
- research;
- decisions;
- execution records;
- and accepted snapshots.

Working roots may live inside this repository or in separately versioned repositories. Sensitive or proprietary domain knowledge can remain private while using the public Chirality instruction system.

A `chirality.project.json` manifest identifies the working root, instruction root, available project overlays, execution location, and enabled runtime capabilities.

All writes must remain inside the declared working root and the scope granted for the active task.

## Domain knowledge

A Chirality domain pack is more than a document collection and is not model training data.

It is a governed knowledge workspace that can contain:

- admitted source material and source hashes;
- audited text, equations, figures, and tables;
- stable source and section identifiers;
- atomic knowledge statements;
- vocabulary and synonym maps;
- categories and knowledge types;
- coverage and validation registers;
- research packets;
- retrieval indexes;
- review decisions;
- and immutable snapshots.

The intended progression is:

```text
Source material
→ audited extraction
→ accepted decomposition
→ evidence-grounded research
→ project deliverables
→ human review and decision
```

Source documents remain distinguishable from decomposition truth. Research and publications derived from a domain must identify the accepted snapshots on which they depend.

## What Chirality can support

The current system includes methods and tools for work such as:

- decomposing project scopes and product requirements;
- defining packages, deliverables, dependencies, and context boundaries;
- decomposing technical literature into governed knowledge structures;
- researching across admitted sources and accepted domain knowledge;
- preparing scopes of work, technical documents, estimates, and proposals;
- extracting and reviewing PDFs, equations, drawings, tables, and equipment data;
- planning and executing bounded software changes;
- testing and reviewing software components;
- assessing change impacts;
- reconciling claims across deliverables;
- auditing completeness, provenance, dependency closure, and governance;
- and publishing evidence-backed technical material.

Not every workflow is equally mature, and not every task requires the full governance depth. The appropriate rigor should reflect the stakes, uncertainty, and consequences of the work.

## Current proof cases

Chirality is being developed through real projects rather than isolated demonstrations.

### Chirality runtime and desktop application

The shared runtime provides provider-neutral contracts, project and session management, governed delegation, authenticated local clients, engine adapters, interruption, turn coordination, and local-model residency.

The desktop application and command-line interfaces are clients of this runtime.

### OpenPipeStress

OpenPipeStress is a pre-release, open-mechanics piping flexibility and stress-analysis platform being developed through Chirality.

It is both a real engineering software product and the principal proof case for the human-agent operating model. Its development includes physical modeling, numerical solvers, units, loads, stress recovery, nonlinear restraints, reporting, model operations, external-tool handoffs, validation evidence, and a packaged desktop interface.

OpenPipeStress is intended to open the mechanics while keeping protected standards data under user control. Results remain engineering decision-support information; professional judgment and acceptance remain with the responsible engineer.

Its verification and validation program distinguishes analytical checks, machine-readable hand calculations, invented benchmarks, regression evidence, and correlation against accepted external solvers.

OpenPipeStress is currently a technical preview, not a released engineering product.

### PEC

PEC is an optional coordination plane that projects governed file state into faster discovery and status views.

It is deliberately rebuildable and non-authoritative. Removing PEC may reduce convenience or throughput, but it must not change project truth or prevent work from continuing through the underlying files.

## Repository guide

| Path | Purpose |
| --- | --- |
| `AGENTS.md` and `agents/` | Agent responsibilities, authority, delegation, and workflow contracts |
| `skills/` | Reusable methods executed through bounded specialist tasks |
| `tools/` | Deterministic transformations, validators, and analysis utilities |
| `docs/` | Founding principles, contracts, standards, types, specifications, and design basis |
| `runtime/` | Provider-neutral runtime contracts, core, daemon, client, CLI, and engine adapters |
| `projects/` | Explicitly governed project working roots |
| `_DomainEngines/` | Project-specific profiles and controlled domain integrations |
| `execution/` | Chirality’s own governed product-development working state |
| `exports/` | Curated public release profiles and packaging rules |
| `init/` | Human and agent entry points |
| `plans/` | Planning and historical design material; not automatically current authority |

## Where to start

### For a human

To understand the system:

1. Read [`docs/DIRECTIVE.md`](docs/DIRECTIVE.md) for the underlying purpose and principles.
2. Read [`AGENTS.md`](AGENTS.md) for the live agent organization.
3. Read [`docs/SPEC.md`](docs/SPEC.md) and [`docs/TYPES.md`](docs/TYPES.md) when you need the physical structures and vocabulary.
4. Read [`docs/CONTRACT.md`](docs/CONTRACT.md) for the binding invariants.
5. Enter a specific project through its `chirality.project.json`, local instructions, and current coordination or handoff state.

You do not need to understand every agent or artifact before beginning a bounded workflow.

### For an agent

Before acting:

1. Resolve the active instruction root and working root.
2. Read the applicable root and project instruction files.
3. Identify the current accepted state, active handoff, and decision surface.
4. Distinguish authoritative truth from candidates, derivatives, and historical records.
5. Confirm the objective, scope, write boundary, expected output, and human gates.
6. Preserve unknowns and conflicts rather than silently resolving them.
7. Validate the result and leave an explicit handoff when work continues elsewhere.

Do not infer authority from an old plan, a chat transcript, a generated report, or the existence of a Git commit.

## Validation

Common repository-level checks include:

```sh
python3 tools/validation/validate_agent_instructions.py agents
python3 tools/validation/validate_skill_metadata.py skills
python3 tools/validation/discover_test_surfaces.py . --text
python3 tools/run_affected_tests.py --base origin/main
```

The shared runtime can be checked independently:

```sh
cd runtime
npm ci
npm run typecheck
npm test
npm run build
```

Project working roots may define additional validation profiles and evidence requirements.

## Maturity

Chirality is an active research and development system with an emerging runtime and product surface.

Its governance, decomposition, and evidence methods are extensive. Its runtime, application interfaces, and project integrations continue to evolve as the human-agent interface itself evolves.

Internal acceptance records establish the project’s own governed state. They are not external certification, regulatory approval, professional authentication, or evidence of general fitness for every use.

## License

Chirality is available under the MIT License. See [`LICENSE.md`](LICENSE.md).

Copyright © 2026 Ryan Tufts.
