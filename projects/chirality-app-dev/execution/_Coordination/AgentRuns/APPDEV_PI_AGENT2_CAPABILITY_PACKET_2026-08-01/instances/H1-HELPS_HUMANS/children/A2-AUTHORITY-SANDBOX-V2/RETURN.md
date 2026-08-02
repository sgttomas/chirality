# Agent 2 Return V2 — Authority and Sandbox Classification

Status: `COMPLETE / READ_ONLY`

Basis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc` plus the live Revision 2
proposal worktree

This record persists the read-only child's terminal return at manager fan-in.
The child changed no file.

## Findings

- Agent 0/1/2 are authority and responsibility contracts; a sandbox applies to
  one concrete instance/run and may narrow but never widen its role authority.
  Agent 0 delegates only Agent 1, Agent 1 delegates only Agent 2, and Agent 2
  never delegates.
- Reusing a Pi implementation primitive is compatible only behind
  Chirality-owned identity/schema, registration, exposure policy,
  authorization, path/shell enforcement, result/evidence, canonical event,
  interruption, and audit contracts. Pi-native permission defaults, ambient
  resources, subagents/delegation, provider discovery, credentials, settings,
  prompts, extensions, and skills cannot become authority by availability.
- Root doctrine presently requires explicit project-root read/write scope and
  serialized integration ownership for a Bash-bearing managed child. A real
  sandbox may add defense in depth, but narrow mounts do not replace that rule
  without a separate Root owner-class ruling and its governed amendments.
- A target where mechanically enforced narrow mounts replace the full-root and
  unconditional-serialization rule must be routed through Root HELPS_HUMANS,
  Root SCOPE_CHANGE, explicit doctrine/runtime rulings, and Root DEL-02-06.
  D-APP-84 may express an App affected-client preference but cannot create the
  Root successor.
- Uniform sandbox semantics across tool-executing Agent 0/1/2 instances are a
  Root-wide owner-class design. A conforming recommendation uses a separate
  role/run-specific sandbox for each instance, never one shared sandbox or one
  copied capability set.

No authority, implementation, or lifecycle selection was made.
