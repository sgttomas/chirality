/**
 * Persona resolution for the harness shell.
 *
 * Extracted from `chat-panel` and **decoupled from the route** in Phase 5. The
 * prior implementation honored `?agent=` only on `/workbench` and hardcoded
 * `WORKING_ITEMS` everywhere else; the persona picker / direct-chat / loop-first
 * surfaces need any picked persona to resolve regardless of route. Resolution is
 * now a pure function of the requested agent string, unit-testable in the
 * node-env test runner.
 */

export const DEFAULT_PERSONA = 'WORKING_ITEMS';

/**
 * Display-label → persona-id aliases. Matrix cells (and pickers) carry a human
 * label that is not always the on-disk persona file name; this maps the label to
 * the `AGENT_<id>.md` stem consumed by `buildSystemPrompt`.
 *
 * `DEPENDENCIES → EVALUATION` fixes the broken EVALUATIVE/APPLYING matrix cell
 * (D-APP-23): there is no `AGENT_DEPENDENCIES.md`. Its three EVALUATIVE siblings
 * all resolve to Type-0/Type-1 personas (AGENTS→HELPS_HUMANS, CHANGE,
 * RECONCILING→RECONCILIATION); EVALUATION is the Type-1 persona for the
 * evaluative valley. The Type-2 `EVALUATION_DEPENDENCY_AUDIT` task agent is
 * deliberately NOT used here — task agents run via orchestration, not as a
 * `/workbench` persona session.
 *
 * The former `AGGREGATE → AGGREGATION` alias was removed: AGGREGATION is a
 * Type-2 TASK agent, so the NORMATIVE/REVIEWING matrix cell was re-pointed at
 * the Type-1 REVIEW persona (which resolves directly, no alias). The
 * `agent-matrix-cells.test.ts` guard now enforces that every `/workbench`
 * matrix target resolves to a Type-0/Type-1 persona.
 */
export const PERSONA_ALIASES: Record<string, string> = {
  HELP: 'HELP_HUMAN',
  ORCHESTRATE: 'ORCHESTRATOR',
  RECONCILING: 'RECONCILIATION',
  AGENTS: 'HELPS_HUMANS',
  DEPENDENCIES: 'EVALUATION'
};

/**
 * Resolve a requested agent label (from `?agent=`, a picker selection, etc.) to
 * a persona id. Empty / missing → the default persona. No route gating.
 */
export function resolvePersona(rawAgent: string | null | undefined): string {
  const candidate = rawAgent?.trim();
  if (!candidate) {
    return DEFAULT_PERSONA;
  }

  const normalized = candidate.toUpperCase();
  return PERSONA_ALIASES[normalized] ?? normalized;
}
