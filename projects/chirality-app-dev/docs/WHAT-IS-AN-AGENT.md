# What Is an Agent?

```text
agent = LLM + instructions + declared files/context + tools + permissions
```

That definition is operational, not metaphysical. An AI agent is not a
responsible professional or bearer of duty. It contributes claims and actions
inside a governed workflow; the human decides what to accept or rely on.

## The runtime hierarchy

```text
Human ↔ Agent 0 → Agent 1 → Agent 2
```

| Layer | Name | Role |
|---|---|---|
| Agent 0 | Supervising Architect | Aligns the human and workflow, supervises managers, and brokers cross-package decisions. HELP_HUMAN is the sole canonical Agent 0. |
| Agent 1 | Manager | Owns a bounded management scope, derives a work graph, delegates specialists, coordinates evidence, and validates fan-in. |
| Agent 2 | Specialist | Executes one sealed objective and returns outputs plus evidence. It does not delegate. |

The human may start an untyped session, HELP_HUMAN, or any Agent 1 directly.
Agent 2 is not a top-level chat role. Standards constrain all three layers but
are not themselves agents.

Agent 2 may be TASK plus a skill and brief, an ephemeral generalist with no
persistent role file, or a dedicated specialist approved after HELPS_HUMANS
demonstrates that TASK and ephemeral forms are inadequate.

## Multi-agent orchestration

The hierarchy controls delegation and communication authority. The work graph
may combine sequential and concurrent action as dependencies require.

Terminal fan-out/fan-in dispatches independent children, waits for their final
returns, validates the complete set, and continues only from accepted fan-in.

Supervised many-to-many agency allows active children to report typed notices
to their parent. Agent 0 brokers between Agent 1 instances; Agent 1 brokers
between Agent 2 instances. Parents may relay, amend, hold, replan, route, or
escalate. Siblings do not bypass the parent.

The runtime persists plans, graphs, launch briefs, status, returns, notices,
updates, amendments, and acknowledgments under
`execution/_Coordination/AgentRuns/<RunID>/`. These control-plane records make
coordination inspectable but do not become decomposition or deliverable truth.

## Package-level development

HELP_HUMAN may launch multiple WORKING_ITEMS Agent 1 instances, one per
activated package. Each WORKING_ITEMS instance coordinates deliverable-scoped
Agent 2 work inside that package and reports cross-package information upward.
Software work uses WORKING_ITEMS plus a project software profile, `software-*`
TASK skills, and deterministic tools. A separate SOFTWARE_DEV manager remains
deferred until trials show stable semantics that this arrangement cannot carry.

## Professional boundary

Agents propose; humans approve. No agent issues, signs, seals, certifies, or
accepts professional reliance. Failure isolation, sealed context, explicit
write ownership, versioned amendments, and validated fan-in make delegated
work legible enough for meaningful human supervision.

The canonical doctrine is the instruction-root `AGENTS.md`; this document is a
product-facing explanation and defers to that source on disagreement.
