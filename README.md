# Chirality

**Purposeful, accountable work with AI agents.**

Chirality is a body of principles and practice for turning agent capability into
work whose reasons and consequences people can still understand and correct. It
asks what should guide work shared between people and agents, and it supplies the
means to carry that work out: roles, methods, tools and artifacts, kept open to
revision as experience shows what serves the work and what does not.

[Website](https://chirality.ai) · [Theses](docs/thesis/README.md) · [Alignment manual](docs/alignment-manual/README.md)

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
longer serve them. The [theses](docs/thesis/README.md) develop the argument.

## The shared library

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

## Built with Chirality

Applications built on these principles live in their own repositories, each with
its own instructions, releases and support:

- [Chirality App](https://github.com/sgttomas/chirality-app): the workflow-authoring
  application, where a person works with Help Human to plan, carry out and reuse
  their work. Downloads and App issue reports live there.
- [SWBPIPE](https://github.com/sgttomas/SWBPIPE): an analysis-grade piping design
  engine and stress-model authoring environment.

Earlier products (App v3, Runtime and PEC) are archived; [Frozen products](projects/FROZEN.md)
explains how to recover their source.

## Develop and contribute

For agent-assisted work in this repository, start from [AGENTS.md](AGENTS.md).
To work on an application, use that application's repository and its instructions.

This repository contains ongoing development and historical evidence as well as
the current library.

[Discuss changes](https://github.com/sgttomas/chirality/issues) · [Work with us](https://chirality.ai/contact)

## License

[MIT License](LICENSE.md), except where a component or project supplies its own licence. Copyright © 2026 Ryan Tufts.
