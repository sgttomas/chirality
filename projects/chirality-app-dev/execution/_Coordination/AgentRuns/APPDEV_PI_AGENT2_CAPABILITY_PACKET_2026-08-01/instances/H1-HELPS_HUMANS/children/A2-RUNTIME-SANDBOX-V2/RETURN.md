# Agent 2 Return V2 — Runtime and Sandbox Seams

Status: `COMPLETE / READ_ONLY`

Basis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc` plus the live Revision 2
proposal worktree

This record persists the read-only child's terminal return at manager fan-in.
The child changed no file.

## Verified current state

- Pi's `createAgentSession`, model/session loop, resource loader, event
  subscription, prompt, interruption, compaction-facing behavior, and custom
  tool binding execute in the Electron runtime-daemon process. Model inference
  is served separately by authenticated literal-loopback oMLX.
- The adapter disables Pi built-ins with `noTools: 'all'` and suppresses
  extensions, skills, prompt templates, themes, context/AGENTS files, settings,
  credentials, and ambient resources. Chirality definitions are adapted into
  Pi tool definitions; the callbacks execute in-process today.
- No Chirality-owned per-run OS sandbox contains Agent 0, Agent 1, Agent 2, or
  their tool effects. `BrowserWindow`'s Chromium `sandbox: true` protects the
  GUI renderer only; the headless daemon does not create that window.
- Descriptor/permission/path/shell policy and lexical shell inspection are
  controls, not an OS containment backend. `cwd` is context, not confinement.
- Pi durable resume is not implemented; the descriptors declare
  `durableResume: false` and canonical event replay does not hydrate a fresh Pi
  session.
- App dependency bytes and the Root engine descriptor name Pi `0.82.0`, while
  App governing authority remains pinned to `0.80.10`.

## Feasible seam, not implementation authority

A trusted daemon can retain authorization, identity, credentials, provider
brokerage, policy, evidence, and audit while each tool-executing agent run uses
a separate role/run-specific worker sandbox. Pi's session/tool loop can remain
inside the Pi Agent 2 worker. Effectful tools can run inside that worker or a
narrower authenticated executor, provided no native primitive can bypass
Chirality pre-execution policy and post-execution evidence/audit.

No backend, primitive, capability, or role expansion was selected.
