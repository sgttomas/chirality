# Launch brief — H1 G4 diff-mode CI wiring

- Parent: `HELP_HUMAN`, run `ROOT_FOUR_LANES_2026-08-02`, plan v1.
- Role: `HELPS_HUMANS`; load `agents/AGENT_HELPS_HUMANS.md` in full.
- Human-ruled objective: wire the existing G4 diff-mode manifest validator
  into the canonical governed CI path so an applicable instruction-surface
  diff lacking a required manifest fails.
- Preserve: existing manifest schema validation, current manifest discipline,
  and unrelated CI behavior.
- Writes: exact CI workflow, existing validator/test surfaces needed for the
  wiring, and this instance's return/evidence only. Do not touch agents,
  runtime, project loops, registers, or product authority.
- Verification: identify the canonical base/range; prove a positive case and
  a missing-manifest negative case; run focused tests and applicable harness
  validation; record authoritative CI rerun requirements.
- Return: changed paths, rationale, commands/results, negative proof, risks,
  and validated readiness for fan-in.
