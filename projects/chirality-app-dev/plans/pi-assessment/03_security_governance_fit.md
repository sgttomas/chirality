# Pi Security And Governance Fit

Date: 2026-06-13

Pi source baseline: `/Users/ryan/ai-env/projects/pi` at commit `9e9fc7947871a913946f727854ae0a57fbce1863`.

## Scope

Assess Pi's trust, filesystem, tool, extension, and sandbox assumptions against Chirality's governed professional-work requirements.

Primary sources:

- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/containerization.md`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/extensions.md`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/path-utils.ts`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/write.ts`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/edit.ts`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/bash.ts`

## Findings

Pi is explicit about its security boundary. Its security docs say it is a local coding agent that runs with the permissions of the user account that starts it (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:1`). Project trust controls loading project-local settings, resources, packages, and extensions, but "is not a sandbox" and does not restrict what model-requested tools can do after the session starts (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:5`).

Pi has no built-in sandbox. Its built-in tools can read, write, edit, and run shell commands with the process user's permissions, and extensions are TypeScript modules running with the same permissions (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:31`). Pi's docs intentionally push real isolation to OS, VM, container, or policy-controlled sandbox boundaries (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:35`).

The containerization docs confirm that Pi runs with all permissions by default and recommend either running the whole process inside isolation or routing tool execution into isolation (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/containerization.md:1`). That is a useful operational pattern, but it is not a built-in guarantee.

## Tool Behavior

Pi's path resolution is ergonomic, not restrictive. `resolveToCwd()` handles absolute paths and home expansion relative to cwd, but it does not enforce project-root containment (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/path-utils.ts:44`).

The write tool accepts relative or absolute paths, creates parent directories, and overwrites files (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/write.ts:14` and `/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/write.ts:181`). The edit tool resolves the requested path and writes the final content after exact replacements (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/edit.ts:287`). The bash tool executes arbitrary shell commands in the current working directory and streams/truncates output (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/src/core/tools/bash.ts:269`).

Those mechanics are appropriate for a monitored developer coding workbench. They are not acceptable as the unwrapped primitive for Chirality's engineering-domain product runtime.

## Borrowable Governance Patterns

Pi still has useful patterns:

- Be explicit that project trust is input-loading control, not a sandbox.
- Use operation interfaces to route read/write/edit/bash into a policy service or VM.
- Serialize same-file mutations to prevent edit/write races.
- Preserve exact-edit behavior, diff generation, BOM/line-ending preservation, and result details as future Chirality tool ideas.
- Use tool-call interception as a runtime policy hook, not just prompt text.
- Use container or VM routing for high-risk execution where a user genuinely needs coding-agent behavior.

Pi's extension docs show lifecycle subscriptions, custom tools, event interception, UI prompts, commands, session persistence, and custom rendering (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/extensions.md:3`). That is a useful extension vocabulary, but Chirality should rehouse it as product-owned MCP/tools/hooks rather than accepting arbitrary project-loaded TypeScript extensions.

## Governance Gap Register

| Gap | Pi posture | Chirality requirement | Required wrapper |
| --- | --- | --- | --- |
| Sandbox | None in-process | Deny-first runtime boundaries | OS/container/VM or Chirality policy layer |
| Filesystem containment | Paths may be absolute/home-relative | Working-root containment, instruction-root block | Mandatory path gate before every tool |
| Writes | Direct write/edit | Proposal paths or approved workspace writes | Human/mode gates plus provenance |
| Bash | Arbitrary shell | Default denied; timeout/audit required | Explicit mode gate plus sandbox |
| Extensions | Arbitrary TypeScript code | Release-managed, trusted capabilities | Disable or curate; no project auto-load |
| Project trust | Resource loading only | Not a safety boundary | Treat as advisory only |
| Sessions | User-writable JSONL | Audit mirror plus git-tracked truth | Chirality-owned event log and snapshots |
| Prompt injection | Expected local-agent risk | Must not alter protected state | Tool policy and deterministic adapters |

## Recommendation

Verdict: **Pi's coding shell should not be embedded directly into production Chirality engineering-domain workflows.**

Borrow the patterns, not the assumptions. If Pi is used for coding work, run it outside the product or behind an isolated execution boundary. For Chirality's embedded engineering apps, all tools must be typed, allowlisted, path-contained, auditable, and routed through Chirality-owned human gates.
