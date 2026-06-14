# Pi Fit For Domain Harness Workflows

Date: 2026-06-13

Pi source baseline: `/Users/ryan/ai-env/projects/pi` at commit `9e9fc7947871a913946f727854ae0a57fbce1863`.

SCA-APP-001 status: historical/reference assessment. Pi is now a pattern corpus and reference source only. D-APP-01 and D-APP-02 rule out a Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, and immediate spike work unless a future human ruling explicitly reverses those boundaries.

## Scope

Assess how Pi concepts translate to Chirality's non-coding, app-embedded engineering-domain workflows.

Primary sources:

- `/Users/ryan/ai-env/projects/chirality/AGENTS.md`
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_ENGINE.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/CONTRACT.md`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/SPEC.md`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/index.md`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md`

## Chirality Domain Model

Chirality's architecture is not just an agent loop. The parent AGENTS index defines governance rules such as derivative-package handling, immutable snapshots, explicit handoff state, closure requirements, and sequencing across accepted snapshots (`/Users/ryan/ai-env/projects/chirality/AGENTS.md:13`). The PRD says Chirality is a desktop harness for governed AI agents over a local filesystem workspace where humans retain authority and project truth lives in git-tracked plain files (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md:21`).

The domain-engine direction is also clear: future domain engines own domain truth, while Chirality governs profiles, proposals, records, and human gates (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/docs/PRD.md:144`). This matters because engineering workflows are not primarily "edit arbitrary files" tasks.

## Workflow Translation

For a piping stress example, the domain workflow should be:

1. Agent drafts an operation proposal under an approved proposal path.
2. A deterministic adapter converts proposal data into a typed domain-engine input or operation.
3. The domain engine performs analysis and emits run artifacts, warnings, checks, and comparison tables.
4. The agent revises proposal text using cited deterministic evidence.
5. Human reviewer accepts, rejects, or requests revision.
6. Accepted state is recorded in versioned files and, where applicable, the domain engine's native accepted state.

Pi can help with the mechanics around this flow, but Pi should not own this flow.

## Pi Concepts That Translate

| Pi concept | Domain translation | Chirality-owned form |
| --- | --- | --- |
| Skill/prompts | Domain task instructions | `TASK + TaskSkill`, governed skill folders |
| Custom tools | Deterministic domain adapters | In-process MCP or domain adapter APIs |
| Tool-call hooks | Path/proposal/human-gate policy | Capability policy with explicit hard-deny precedence |
| Sessions/events | Runtime observability | `.chirality/sessions/<id>/events.jsonl` plus git truth |
| Packages | Curated domain profiles | Release-managed instruction/profile bundles |
| Compaction | Runtime context management | Non-authoritative context mirror events |
| RPC/JSON modes | App integration boundary | Chirality `AgentEnginePort` and typed APIs |

## Pi Concepts That Do Not Translate Directly

Pi is a terminal coding harness. Chirality's domain apps need least privilege, typed domain operations, solver result capture, professional boundary notices, and non-delegable human gates.

Pi's own docs say project trust is not a sandbox and tools run with user-process permissions (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:5` and `/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/security.md:31`). That is acceptable for developer-monitored coding work but not for authoritative engineering state changes.

Pi's flexible package/extension model is also too open for current Chirality domain products. Domain profiles should be release-managed and governed, not arbitrary project-loaded extensions that can execute TypeScript with full process permissions (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/docs/extensions.md:108`).

## Recommendation

Verdict: **Pi is a useful implementation vocabulary for harness mechanics, not the domain workflow engine.**

For engineering-domain apps, Chirality must own:

- Domain profiles and protected path policy.
- Operation proposals and human gates.
- Deterministic adapter manifests and result artifacts.
- Accepted snapshots and handoff state.
- Audit/event records and redaction.
- Professional-boundary posture.

Pi should remain a reference for lightweight harness primitives and possibly a development-time coding assistant. It should not define the production shape of embedded engineering-domain workflows.
