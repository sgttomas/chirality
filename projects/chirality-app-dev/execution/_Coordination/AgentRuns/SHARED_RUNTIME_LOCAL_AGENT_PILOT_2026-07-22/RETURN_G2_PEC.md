# G2 Return — PEC Adapter Migration

Status: `COMPLETED`

PEC now uses one injected shared-runtime client path for agent execution while
retaining deterministic PEC acts, RBAC, reporting, and domain tools in the
project adapter. The compatibility endpoint preserves canonical UIEvent SSE
without constructing a second production LLM/session loop.

Browser-selected model/path routing, operator/permissive/symlink tokens,
credential-bearing redirects, production data paths, file proposal attachment
execution, and human-only acts fail closed.

Validation: PEC typecheck passed; 74 core, 172 server, and 110 adapter tests
passed. The web build passed.
