# PEC demo launch runbook

> **Epistemic status: coordination runbook — owner-adopted 2026-07-07 (item
> B-1 of `_DomainEngines/proposals/pec/BRIEF_2026-07-07_workflow_simplification.md`).**
> Doc-only: this page changes no default and no behavior. On any disagreement
> the env-var read sites govern (`agent-sidecar/src/config.ts`,
> `agent-sidecar/src/engine/sdk.ts`, `server/src/agent-proxy.ts`,
> `server/src/index.ts`). Secrets are referenced by name only — never write a
> value into this file.

All shapes run from `projects/pec/`. Set `PEC_DB` **first, every time** — the
one recorded launch failure (Receipt 50, 2026-07-07) was a launch without it:
the server came up on the non-demo `pec.db` and the sidecar failed clean at
login (401). One root script starts all three processes (server :4810,
sidecar :4812, web :4811).

**Common preface (every shape):**

```sh
cd projects/pec
export PEC_DB="$PWD/pec-demo.db"            # absolute; must contain "scratch" or "demo" (seed guard)
source ~/.secrets/pec-agent-person.env      # sets PEC_AGENT_EMAIL / PEC_AGENT_PASSWORD
```

## A — demo, stub engine (no key, no model egress)

```sh
npm run dev
```

## B — demo, SDK engine (hermetic session, enumerated access — the defaults)

```sh
export PEC_AGENT_ENGINE=sdk
export ANTHROPIC_API_KEY=...                # from your keychain; never committed
npm run dev
```

## C — demo, SDK + broad access (D-T0-21 O-B per-launch act)

Shape B, plus:

```sh
export PEC_AGENT_ACCESS=broad
```

## D — demo, SDK + broad + open session profile (D-T0-22 per-launch act)

Shape C, plus:

```sh
export PEC_AGENT_SESSION=open
```

**Optional knobs (any SDK shape):** `PEC_AGENT_MODEL` (default: the SDK's
default model), `PEC_AGENT_MAX_ACTS` (default 8), and server-side
`PEC_AGENT_MESSAGE_TIMEOUT_MS` (default 300000).

## Post-launch check (every shape)

```sh
curl -s http://127.0.0.1:4812/agent/health
```

Expect `engine`, `access`, and `session` to match the shape you launched, and
`configured: true`. `configured: false` means credentials are unset or login
was refused — the sidecar still serves browsing, but agent messages return
503 (`agent-sidecar/README.md` covers provisioning). Accept/apply/`force`
remain your screen acts in every shape.
