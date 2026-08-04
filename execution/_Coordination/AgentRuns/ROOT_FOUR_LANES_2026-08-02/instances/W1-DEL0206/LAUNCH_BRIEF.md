# Launch brief — W1 DEL-02-06 accepted-turn recovery

- Parent: `HELP_HUMAN`, run `ROOT_FOUR_LANES_2026-08-02`, plan v1.
- Role: `WORKING_ITEMS`; load `agents/AGENT_WORKING_ITEMS.md` in full.
- Objective: take TM-ROOT-108 into the DEL-02-06 amendment/activation lane.
- Accepted constraint: DEL-02-06 is `INITIALIZED`, not previously activated;
  its accepted first activation is limited by REQ-027 to specification,
  read-only consumer inventory, evidence-matrix design, and change planning.
- Exact concern: persisted `turn.accepted` records lacking terminal evidence
  must be reconciled idempotently on restart before new admission or model
  activation, with eventual restart/replay, drain-accounting, and
  exactly-one-terminal proof.
- Writes: deliverable-local run records only. No runtime/client source,
  lifecycle state, contract repin, App/Piping surface, register, or release
  write without a later sealed authorization.
- Coordination: discovery/planning may proceed in parallel; hold executable
  amendment on applicable S1 and later activation gates.
- Return: validated manager work graph, exact requirements and affected
  surfaces, proposed implementation/evidence plan, current activation verdict,
  next human gate, blockers, and rerun requirements.
