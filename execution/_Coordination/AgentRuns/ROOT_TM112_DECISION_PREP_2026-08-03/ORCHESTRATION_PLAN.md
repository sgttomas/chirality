# Orchestration plan — TM-ROOT-112 investigation and later decision preparation

RunID: `ROOT_TM112_DECISION_PREP_2026-08-03`
Selection authority: `HUMAN`
Posture: `MIXED`
Frozen revision: `88e7590d3664d4f1daf91bed2a8899bda0748b92`
Frozen remote basis: `origin/main` at the same revision

## Objective

Execute the human-prioritized serial work graph. This manager dispatch owns N1
only: a bounded, evidence-producing reproduction or disproof investigation of
TM-ROOT-112. N2 (root handoff count repair) and N3 (owner-decision
preparation) remain held until HELP_HUMAN validates N1.

## Authority and artifact classes

- Authority inputs: the live Root register row `TM-ROOT-112`; the human steer;
  accepted Root source at the frozen revision.
- Coordination input: the App-surface notice
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md`,
  SHA-256 `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`.
- This run package is derivative inquiry evidence. It does not define runtime
  semantics, alter source, update Task Management, or accept App work.

## N1 method

1. Bind the repository, source, notice, environment, tools, and dependencies.
2. Inspect `RuntimeDaemon.stop()`, SSE routing, and existing daemon tests.
3. Run controlled Unix-socket stop cases with explicit timeouts:
   idle server, active ordinary keep-alive client, and a live long-lived/SSE
   response using the same Node `Server.close()` primitive.
4. Preserve timestamped raw output, fixture source, process/connection/socket
   and cleanup observations, and distinguish direct execution from static
   inference.
5. Assess the App hypothesis, current/intended contract evidence, warranted
   scope, owning gate, coverage gaps, and next bounded diagnostic seam.
6. Validate containment and return N1 to HELP_HUMAN without modifying source,
   tests, register, lifecycle, Git state, App/Piping content, or root handoff.

## Stop conditions

Stop and escalate if the investigation requires a source/test/runtime repair,
semantic contract selection, cross-loop write, register change, lifecycle or
release change, or Git action. No Agent 2 is dispatched in N1; HELPS_HUMANS
executes the bounded inquiry directly.
