# Chirality

Chirality is a macOS workspace for professional knowledge work with AI agents.
Work with project files, develop a plan, carry it out, review the results, and
save a useful method as a workflow. Reuse that workflow with new inputs and
refine it as the work changes. People remain responsible for what they accept
and rely on.

## Download Chirality for macOS

Download the signed and notarized installer from the
[latest GitHub release](https://github.com/sgttomas/chirality-app/releases/latest).
These instructions describe published releases; a local build is not evidence
of signing or notarization.

System requirements:

- Apple Silicon (`arm64`)
- macOS 15 or newer

The release contains:

- `Chirality-<version>-arm64.dmg`
- `Chirality-<version>-arm64.dmg.sha256`

To verify the download, place both files in the same directory and run:

```sh
shasum -a 256 -c Chirality-*-arm64.dmg.sha256
```

Then open the DMG, drag Chirality to Applications, and launch it normally.
Published installers are signed with a Developer ID certificate, accepted by
Apple notarization, and distributed with a stapled notarization ticket.

## Start Working

Chirality v3 uses Codex as its sole agent engine. Sign in with your ChatGPT
account through the Codex sign-in flow, then choose a folder for your work and
start a conversation. Describe the result you need, the files to use, and any
constraints. Your available models and usage follow your Codex account.

Use Plan mode to work through an approach, answer questions, and revise the
plan before execution. Review the resulting files and give corrections in the
conversation. When a method is useful, ask to save it as a project or personal
workflow so you can use it again and improve it over successive runs.

Four roles organize the work: HELP_HUMAN coordinates with you, HELPS_HUMANS
designs methods and instructions, WORKING_ITEMS manages production work, and
TASK carries out bounded assignments. Workflows provide reusable methods;
skills remain available to agents in the background. You do not need to browse
or manage skills to begin a conversation.

Chirality checks public release metadata at startup and every six hours while
running. When an update is available, it shows a download option. Downloading
opens your browser; you choose when to quit Chirality, install the replacement,
and reopen it. Chirality does not install updates automatically. You can also
check manually in About Chirality.

## Repository Contents

This repository is the curated Chirality desktop release projection.

| Path | Contents |
| --- | --- |
| `runtime/` | Runtime service, contracts, client, CLI, engine adapters, and tests |
| `agents/` | Instructions for the four agent roles |
| `workflows/` | Reusable workflow library and its supporting resources |
| `.agents/skills/` | Seven selected skills available to agents in the background |
| `tools/` | Utilities and validation tools |
| `docs/` | Architecture, contracts, specifications, and governance |
| `init/` | Public session bootstrap guidance |

The desktop application source is not currently included in this release
projection. It lives in the public
[canonical Chirality source repository](https://github.com/sgttomas/chirality).
Published desktop installers are distributed here as release assets. This
repository excludes credentials, local runtime data, machine registration
state, downloaded models, non-release project workspaces, and private domain
repositories.

## Working with the Public Runtime

Runtime development requires Node.js 22.19 or newer:

```sh
cd runtime
npm ci
npm run typecheck
npm test
npm run build
```

These commands validate and build the Runtime. They do not build the desktop
application. Runtime compatibility code does not establish support for another
engine in Chirality v3.

See [`runtime/README.md`](runtime/README.md) for architecture and development
details, and [`AGENTS.md`](AGENTS.md) for the agent roles and instruction model.

## Professional and Security Boundary

Generated content must be reviewed against the project record, applicable
standards, and your acceptance criteria. Chirality does not transfer
professional responsibility to an AI system.

Sign-in state and runtime sessions are local operational data. They are not
part of this repository and do not replace your project files or records.

## License

MIT License. See [`LICENSE.md`](LICENSE.md).

Copyright (c) 2026 Ryan Tufts
