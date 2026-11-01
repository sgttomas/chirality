# Chirality

**Purposeful, accountable work with AI agents.**

Chirality is a body of principles and practice for turning agent capability into
work whose reasons and consequences people can still understand and correct. It
asks what should guide work shared between people and agents, and it supplies the
means to carry that work out: roles, methods, tools and artifacts, kept open to
revision as experience shows what serves the work and what does not.

[Website](https://chirality.ai) · [Thesis](docs/thesis/README.md) · [Project Management Manual](docs/alignment-manual/README.md#project-management-manual)

<a id="the-shared-library"></a>
<a id="obtain-and-use-the-library"></a>

## Use the library

**New here? Start with the [Project Management Manual](docs/alignment-manual/README.md#project-management-manual).**
It explains how a person and their agent can organize, examine and carry work
through. Read it yourself or give its Markdown source to your agent along with
your actual problem, context and intended result. The manual index links both
readable and agent-friendly forms; a manual supplies a method, not authority.

To contribute to this repository, use [Develop and contribute](#develop-and-contribute).
The steps below are for using library material in your own work or project.

### 1. Choose a version

Use [Chirality library 1.0.0](https://github.com/sgttomas/chirality/releases/tag/library-v1.0.0),
the current published source edition. Its release page provides the download,
checksum, change account and limitations. You can also
[browse that edition on GitHub](https://github.com/sgttomas/chirality/tree/library-v1.0.0)
without installing anything.

Published editions identify fixed source revisions. This README's relative links
open material in the version you are viewing: switch to the published tag or
use its downloaded archive to stay within that edition. Following `main` is an
explicit choice to use ongoing development. A merge or an old application release
is not a new library edition.

### 2. Choose what you need

| I want to… | Start here | How to use it |
| --- | --- | --- |
| Organize work with my agent | [Project Management Manual](docs/alignment-manual/README.md#project-management-manual) | Read the current edition or supply its Markdown source to your agent; apply it to a concrete undertaking. |
| Learn the reasoning | [Thesis](docs/thesis/README.md) and [courses](docs/human-team-courses/README.md) | Read the foundations or follow the learning material for people. |
| Choose an agent's contribution | [Roles](agents/) | Read the relevant role: HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS or TASK. |
| Use a repeatable method | [Workflow guide](workflows/README.md) | Select a workflow and retain its complete package and required resources. |
| Run a library tool | [Workflow resolver](tools/workflow_runtime/README.md), [deliverable queries](tools/deliverables/README.md), or [other tools](tools/) | Follow the selected tool's guide for commands, dependencies, outputs and limits. |
| Understand a shared contract | [Product boundaries](docs/PRODUCT_BOUNDARIES.md), [agent/workflow interface](docs/AGENT_WORKFLOW_RUNTIME.md), [compatibility formats](docs/COMPATIBILITY_FORMATS.md) | Check the reference's applicability before adopting it in your project. |

Read on GitHub, download the source archive from the release, or clone the
repository. Reading alone needs no Git installation. Tools have their own
prerequisites; the workflow resolver selects instruction files and reports source
identity, but does not launch an agent or grant host permissions.

When copying material, keep its original relative paths, required resources and
applicable [license notices](LICENSE.md). Record the selected tag or full source
revision alongside your project's existing instructions or source record, and
mark local adaptations. You can use selected material without adopting the whole
library. Your project keeps its own authority and operating instructions;
Root's `AGENTS.md` and execution rules govern work on this repository.

### 3. Stay informed

Choose whichever route suits you:

- **GitHub notifications:** sign in, open [this repository](https://github.com/sgttomas/chirality),
  select **Watch → Custom → Releases → Apply**. If you already watch it, the
  button may show your current notification setting. Delivery follows your
  [GitHub notification settings](https://github.com/settings/notifications).
- **Feed reader:** subscribe to the [releases Atom feed](https://github.com/sgttomas/chirality/releases.atom).
- **Check manually:** visit the [Releases page](https://github.com/sgttomas/chirality/releases)
  and read the edition's notes and source identity.

These routes announce repository releases; check the release subject for the
library edition you need. Notifications do not update your files or adopt changes.

<a id="inspect-changes-before-adopting-them"></a>

### 4. Decide whether to update

Keep using your selected edition until you choose to change it. Read the new
release notes, compare the material and resources your project uses with your
current basis, and address applicable dependencies or migration steps. Make and
check the update through your own change process. For an unpublished development
revision, use its merged PR description as the change account.

GitHub's comparison view or `git diff` can show the differences. A failed comparison
is not “no change”; a path-limited comparison says nothing about other material.
Historical sources and editions remain discoverable through
[Frozen products](projects/FROZEN.md) and the [manual index](docs/alignment-manual/README.md).

<details>
<summary>Optional command-line discovery and comparison</summary>

List recent publications with the GitHub CLI:

```sh
gh release list --repo sgttomas/chirality --limit 20
```

An empty successful listing means no releases were returned; a failed query does
not establish absence. In an existing clone, fetch source references without
adopting their content, then compare available tags or full commits:

```sh
git fetch origin
git diff <old-basis> <candidate-basis> -- <selected-paths>
```

Polling can repeat these checks. Keep your interests and last examined basis
locally. Scheduling or external delivery requires your own configured operator
and authority; the library provides no subscription service or automatic adoption.

</details>

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

The [Library PRD](docs/PRD.md) defines the accepted library scope.
For agent-assisted work in this repository, start from [AGENTS.md](AGENTS.md).
To work on an application, use that application's repository and its instructions.

This repository contains ongoing development and historical evidence as well as
the current library.

[Discuss changes](https://github.com/sgttomas/chirality/issues) · [Work with us](https://chirality.ai/contact)

## License

[MIT License](LICENSE.md), except where a component or project supplies its own licence. Copyright © 2026 Ryan Tufts.
