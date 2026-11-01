# Chirality

**Purposeful, accountable work with AI agents.**

Chirality is a body of principles and practice for turning agent capability into
work whose reasons and consequences people can still understand and correct. It
asks what should guide work shared between people and agents, and it supplies the
means to carry that work out: roles, methods, tools and artifacts, kept open to
revision as experience shows what serves the work and what does not.

[Website](https://chirality.ai) · [Thesis](docs/thesis/README.md) · [Alignment manual](docs/alignment-manual/README.md)

## Why Chirality

Every project should give the next one a better starting point. Often, the
understanding stays with the person who did the work, even when the finished
document survives.

Chirality makes more of that understanding available for reuse: the method, its
references, and the checks that help someone evaluate the result. Some work
becomes a repeatable workflow. Some leads to a purpose-built tool that no longer
needs an agent to run it.

## What it holds to

- **Useful work.** Work begins with something that matters, and its result is
  judged by its use in the world it serves.
- **Inspectable reasons.** Why a result looks the way it does, and what it rests
  on, stays available to the people who rely on it.
- **Understandable authority.** It is clear who may decide what, and agents act
  within the authority given to them.
- **A person who answers for the work.** Accountability, acceptance and reliance
  remain human acts.
- **Attention to consequences.** Review is proportionate to what depends on the
  result.

The particular mechanisms, such as roles, sequences of review and record formats,
are design choices in service of these commitments, and are revised when they no
longer serve them. The [thesis](docs/thesis/README.md) develops the argument.

## The shared library

The accepted [Library PRD](docs/PRD.md) defines the current development scope.

This repository is the library that Chirality projects draw on:

| Part | What it provides |
| --- | --- |
| [Roles](agents/) | Four ways an agent participates: HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS and TASK |
| [Workflows](workflows/README.md) | Reusable methods for organizing and carrying work through, selected by name and source |
| [Tools](tools/) | Deterministic utilities and checks |
| [Design documentation](docs/) | Shared references: product boundaries, the agent and workflow runtime, compatibility formats |
| [Alignment manual](docs/alignment-manual/README.md) | How to organize, check and carry work forward across projects |

A role describes how an agent participates. A workflow describes how work is
organized and carried through. Tools perform deterministic operations. A project
names the library in its own `AGENTS.md`, keeps its own authority, holds and
product decisions, and adds methods and tools of its own where it needs them.

## Obtain and use the library

The current owner-published source edition is [Chirality library 1.0.0](https://github.com/sgttomas/chirality/releases/tag/library-v1.0.0),
from `fc73de583d25bf792d5c3abb3bf1ac8e0c38f7d6`. Its release supplies the source archive,
checksum, change account, dependencies and qualification limits.

Select the material and its source basis for the work you intend to do. Use an
owner-published library version when one is available for that purpose. Following
`main` is an explicit development choice; a merge, an archive tag or an old App
release does not establish a published library edition.

You can read files on GitHub, download a source archive for the selected tag or
commit, or clone this repository. Reading the material requires no Git
installation. An archive is available at
`https://github.com/sgttomas/chirality/archive/<tag-or-full-commit>.zip`.
Keep the selected identity with your project's entry or existing source record;
the archive's lack of a `.git` directory does not make its origin unknown when
you obtained it from an identified revision. A selected-file copy should retain
its original path and basis, required resources and applicable license notices.
The repository's [LICENSE.md](LICENSE.md) provides the MIT notice; retain any
component-specific license that applies to the material you take.

Read a holding's purpose, applicability and limits before relying on it. For a
workflow, preserve its complete package and the resources its method needs;
the [workflow guide](workflows/README.md) explains selection and package form.
Each tool's README gives its dependencies and usage contract. A prose method can
be read without running the [workflow resolver](tools/workflow_runtime/README.md),
which selects requested instruction files and reports their source identity.
Its result does not launch an agent or grant host permissions.

Your project chooses its own entry instructions, authority and methods. Root's
`AGENTS.md`, session init prompt and execution entry govern work on this
repository. Copying library material does not adopt those Root operating rules.
Keep adaptations distinguishable from their source; a product's packaged inputs
remain at its selected basis until that product deliberately adopts a change.

## Inspect changes before adopting them

Compare the basis you use with the particular version you are considering.
Read its release or change account and the affected source diff. For an integrated
development revision without a release, use the merged PR description as the
change account. Then follow the inputs and uses that matter to your project.
Include linked resources and
explanatory editions where their meaning changed. GitHub's comparison view or
ordinary Git can supply the source differences:

```sh
git diff <old-basis> <candidate-basis> -- <selected-paths>
```

Confirm that both revisions are available and the selected paths cover the
claim. A failed comparison is not “no change”; a path-limited comparison says
nothing about unexamined material. Inspecting a newer source does not adopt it.
Update your selected basis only through your own change process, with applicable
checks and any migration or compatibility conditions addressed.

To discover publications, inspect this repository's Releases page and each
candidate's stated subject and source. The optional GitHub CLI offers the same
bounded listing with `gh release list --repo sgttomas/chirality --limit 20`.
An empty successful listing means no releases were returned; a failed query does
not establish absence. In a clone, `git fetch origin` obtains available source
references without adopting their content into your work. Select the particular
tag or full commit before comparing it with your retained basis.

Polling can repeat that discovery and comparison. Keep your interests and last examined basis locally.
Any scheduled check or external notification needs an actual configured operator
and authority; the library provides no subscriber registry or automatic adoption.
Historical source and edition recovery is described in
[Frozen products](projects/FROZEN.md) and the
[manual index](docs/alignment-manual/README.md).

## Built with Chirality

Applications built on these principles live in their own repositories, each with
its own instructions, releases and support:

- [Chirality App](https://github.com/sgttomas/chirality-app): the workflow-authoring
  application, where a person works with Help Human to plan, carry out and reuse
  their work. Downloads and App issue reports live there.
- [SWBPIPE](https://github.com/sgttomas/SWBPIPE): an analysis-grade piping design
  engine and stress-model authoring environment.

Earlier products (App v3 and Runtime) are archived; [Frozen products](projects/FROZEN.md)
explains how to recover their source.

## Develop and contribute

For agent-assisted work in this repository, start from [AGENTS.md](AGENTS.md).
To work on an application, use that application's repository and its instructions.

This repository contains ongoing development and historical evidence as well as
the current library.

[Discuss changes](https://github.com/sgttomas/chirality/issues) · [Work with us](https://chirality.ai/contact)

## License

[MIT License](LICENSE.md), except where a component or project supplies its own licence. Copyright © 2026 Ryan Tufts.
