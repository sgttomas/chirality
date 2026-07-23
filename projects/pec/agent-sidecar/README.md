# @pec/agent-sidecar — deterministic project adapter

Under D-T0-23/D-PEC-56 this package no longer owns an LLM, credential-provider,
conversation, session, delegation, interruption, or model-residency loop. Its
production entrypoint is a loopback-only deterministic PEC project adapter for
the root Chirality runtime.

The package name is retained for one migration cycle. The backend's historical
`/api/projects/:pid/agent/*` route now proxies to the shared daemon, not to this
process.

## Retained authority boundary

The adapter logs in as an owner-provisioned PEC agent person and invokes PEC
only through the existing RBAC HTTP API:

- the person must be non-admin and must not hold `import.accept`;
- all reads remain limited to that person's project membership and visibility;
- deterministic proposal, own-withdrawal, bounded triage, report, and read acts
  retain their previous guards;
- accept/apply, reject-of-others, `force`, approval/decision/check outcomes,
  waiver, issue, access change, attestation, and consequence closure are absent
  from the adapter dispatch table;
- the low-level client denylist, payload guards, and PEC server RBAC provide
  independent defense in depth.

The shared runtime decides which adapter acts, if any, a governed session
receives. The first local-agent pilot remains read-only and scratch/demo-only.

## HTTP surface

The process listens on `127.0.0.1` only:

```text
GET  /adapter/health
POST /adapter/execute  { "pid": 1, "act": "intake.summary", "input": {} }
```

The retired `/agent/health` and `/agent/messages` paths return
`410 AGENT_RUNTIME_MIGRATED`; they never start a second execution loop.

Declared deterministic acts:

```text
import.propose       import.refresh       import.withdraw
import.status        intake.triage        intake.summary
screen.read          read.overview        read.register
read.history         read.explain         read.report
report.draftDocx
```

Human-only acts are intentionally not declared.

## Environment

```text
PEC_BASE_URL=http://127.0.0.1:4810
PEC_ADAPTER_PORT=4812
PEC_ADAPTER_TOKEN_FILE=/absolute/path/to/mode-0600/adapter.token
PEC_AGENT_EMAIL=...
PEC_AGENT_PASSWORD=...
PEC_AGENT_ACCESS=enumerated|broad
```

`PEC_BASE_URL` must be loopback. Every `/adapter/*` request requires the bearer
credential loaded from `PEC_ADAPTER_TOKEN_FILE`; the server process uses the
same file through `PEC_PROJECT_ADAPTER_TOKEN_FILE`. The file must be a regular
mode-`0600` file containing at least 32 non-whitespace characters. Credentials remain local environment values,
are never returned by health, and establish the person-bound PEC session only.
`enumerated` remains the default data-egress clamp; `broad` remains an explicit
owner launch choice and never expands the human-act boundary.

The historical `PEC_AGENT_ENGINE`, `PEC_AGENT_MODEL`, and `PEC_AGENT_SESSION`
knobs are not read by the production adapter.

## Run and integration

From `projects/pec`:

```text
npm run dev:agent
```

Despite the temporary script name, this starts the deterministic adapter.
The PEC backend calls the authenticated deterministic adapter first to obtain
RBAC-filtered project context, then invokes the project-scoped shared-runtime
client for the governed Agent 1 stream. The browser receives neither
credential and there is no production fallback to the historical agent loop.

Historical stub/SDK loop sources and their regression harness remain isolated
in `src/legacy-agent-test-harness.ts` for the migration cycle. The production
entrypoint does not import that module and must never use it as fallback.
