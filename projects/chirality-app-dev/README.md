# Chirality App development

**Plan your work. Iterate.**

Chirality App is a desktop workspace for professional knowledge work. Work with Help Human to understand a task, plan and execute it, then turn a useful plan into a workflow you can reuse and adapt.

**v3.0.0 is released** for Apple Silicon Macs running macOS 15 or newer. To use it, [download the App](https://github.com/sgttomas/chirality-app/releases/latest) and sign in with your ChatGPT account. This directory is for developing the App.

[Product overview](https://chirality.ai/app) · [User issue tracker](https://github.com/sgttomas/chirality-app/issues) · [Main repository](../../README.md)

## What is here

The UI uses React and Next.js inside Electron. Electron starts an App-owned Runtime service, which hosts the stock Codex App Server. Ordinary users do not install or start a separate daemon. Codex is the engine shipped in v3; local-model integration remains future work.

The App presents continuing conversations, native Plan Mode, model and reasoning choices, attachments, file previews, workflow selection, questions and approvals, and delegated-agent activity. Workflows are created and revised through chat. Skills work in the background.

| Location | Purpose |
| --- | --- |
| [frontend/src/](frontend/src/) | Conversation UI, document panels, and App HTTP routes |
| [frontend/electron/](frontend/electron/) | Desktop lifecycle, native integration, and Runtime hosting |
| [frontend/scripts/](frontend/scripts/) | Development, packaging, and verification commands |
| [instructions/AGENTS.md](instructions/AGENTS.md) | Default shared product guidance, editable through App Settings |
| [Runtime source](../chirality-runtime/) | Service, protocol contracts, sessions, and Codex integration |
| [Root roles](../../agents/) and [workflows](../../workflows/) | Instruction sources bundled with the App |
| [docs/](docs/README.md) | Architecture, requirements, validation, and release documentation |
| [execution/](execution/) | Development decisions, reviews, and historical evidence |

The App supplies shared product guidance and the active role automatically. Codex also discovers applicable user and project instructions. The repository's [AGENTS.md](AGENTS.md) governs development here; it serves a different purpose from the editable product guidance.

## Run from source

Use the full [chirality repository](https://github.com/sgttomas/chirality). Node.js 22.19 or newer is required; CI uses Node 24. The desktop release target is macOS on Apple Silicon.

From the repository root:

```sh
cd projects/chirality-runtime
npm ci
npm run build

cd ../chirality-app-dev/frontend
npm ci
npm run dev
```

The Runtime build produces the local packages the frontend consumes. The development command starts Next.js on port 3000 and the Electron App. Use a separate working folder for development trials.

## Checks and packaging

Run checks appropriate to the change:

| Working directory | Command | Purpose |
| --- | --- | --- |
| `projects/chirality-runtime` | `npm run build` | Compile Runtime packages consumed by the App |
| `projects/chirality-runtime` | `npm test` | Runtime tests |
| `projects/chirality-app-dev/frontend` | `npm run typecheck` | UI and Electron typechecks |
| `projects/chirality-app-dev/frontend` | `npm test` | Frontend tests, including Runtime integration |

Rebuild Runtime after changing it and before running frontend integration tests. Stop the development server before a production build or package rewrites its output.

See [Build and Release](docs/BUILD_AND_RELEASE.md#8-packaging-procedure) for packaging, and [frontend/package.json](frontend/package.json) for executable scripts and current requirements. Signing, notarization, and public distribution are separate from running a development build.

For agent-assisted changes, read the root [AGENTS.md](../../AGENTS.md) and the [project instructions](AGENTS.md). Keep review and validation proportional to the actual change. Historical trial procedures are evidence of earlier work, not instructions to repeat every trial for each repair.

## License

See the repository [MIT License](../../LICENSE.md) and the licences of bundled dependencies.
