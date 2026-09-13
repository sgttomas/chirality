# Chirality

**Plan your work. Iterate.**

Chirality helps professional knowledge workers turn complex tasks into methods they can reuse and adapt. Start a conversation with Help Human, the assistant in Chirality App. Work out what you need, make a plan when it helps, and carry out the work together. Turn a useful plan into a workflow for next time.

[Download Chirality App](https://github.com/sgttomas/chirality-app/releases/latest) · [Website](https://chirality.ai) · [Release announcement](https://chirality.ai/announcements)

## Use the App

**Version 3.0.0 is available.** It runs on Apple Silicon Macs with macOS 15 or newer and uses Codex through your ChatGPT account. Local-model support is planned for a later release.

Bring a task such as a monthly update, a proposal, an investigation, or a review. Help Human can organize references, prepare work, and help you check it. You can select a workflow from the library or ask it to turn your plan into one. Return to the conversation to reuse and refine the method as your work changes.

Saved plans, workflows, references, and outputs are ordinary files in your folders. Plans stay in conversation history unless you choose to save them to a file. You can keep and use them outside the App. Task content needed by the model is sent to OpenAI using your account; Chirality AI Ltd does not proxy or retain that content. See [installation and data handling](https://chirality.ai/deployment).

You direct the work and decide what is ready to rely on. Use review appropriate to its consequences.

## Why Chirality

Every project should give the next one a better starting point. Often, the understanding stays with the person who did the work, even when the finished document survives.

Chirality makes more of that understanding available for reuse: the method, its references, and the checks that help someone evaluate the result. Some work becomes a repeatable workflow. Some leads to a purpose-built tool that no longer needs an agent to run it.

## This repository

This is the main source and development repository for Chirality App, its Runtime, agent instructions, reusable methods, and related projects. Downloads and user issue reports live in [chirality-app](https://github.com/sgttomas/chirality-app).

| Location | Purpose |
| --- | --- |
| [App development](projects/chirality-app-dev/README.md) | Desktop source, local setup, and development documentation |
| [Runtime](projects/chirality-runtime/README.md) | The App-owned service and Codex integration |
| [Agents](agents/) | Four roles: HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS, and TASK |
| [Workflows](workflows/README.md) | Reusable instructions for coordinating and completing work |
| [Skills](.agents/skills/) | Bounded methods used by agents during their work |
| [Tools](tools/) | Deterministic utilities and checks |
| [Projects](projects/) | Product and integration work, including SWB Piping Designer |
| [Design documentation](docs/) | Design basis, standards, and contracts |

A role describes how an agent participates. A workflow describes how work is organized and carried through. Skills supply contextual methods; tools perform deterministic operations. The App loads the active role and brings in methods as needed.

## Develop and contribute

For application development, start with the [App README](projects/chirality-app-dev/README.md). For agent-assisted work in this repository, read [AGENTS.md](AGENTS.md) and the instructions in the project you are changing.

The repository contains ongoing development and historical evidence as well as released source. Consult the [release notes](https://github.com/sgttomas/chirality-app/releases) for what ships in a particular App version.

[Report an App issue](https://github.com/sgttomas/chirality-app/issues/new/choose) · [Discuss source changes](https://github.com/sgttomas/chirality/issues) · [Work with us](https://chirality.ai/contact)

## License

[MIT License](LICENSE.md), except where a component or project supplies its own licence. Copyright © 2026 Ryan Tufts.
