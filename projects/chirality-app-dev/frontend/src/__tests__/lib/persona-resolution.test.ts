import { describe, expect, it } from 'vitest';
import {
  DEFAULT_PERSONA,
  PERSONA_ALIASES,
  resolvePersona
} from '../../lib/shell/persona-resolution';

describe('resolvePersona', () => {
  it('defaults to WORKING_ITEMS for empty / missing input', () => {
    expect(resolvePersona(null)).toBe(DEFAULT_PERSONA);
    expect(resolvePersona(undefined)).toBe(DEFAULT_PERSONA);
    expect(resolvePersona('')).toBe(DEFAULT_PERSONA);
    expect(resolvePersona('   ')).toBe(DEFAULT_PERSONA);
    expect(DEFAULT_PERSONA).toBe('WORKING_ITEMS');
  });

  it('normalizes case and trims before resolving', () => {
    expect(resolvePersona('working_items')).toBe('WORKING_ITEMS');
    expect(resolvePersona('  change  ')).toBe('CHANGE');
  });

  it('maps display-label aliases to persona ids', () => {
    expect(resolvePersona('HELP')).toBe('HELP_HUMAN');
    expect(resolvePersona('ORCHESTRATE')).toBe('PROJECT_SETUP');
    expect(resolvePersona('AGENTS')).toBe('HELPS_HUMANS');
  });

  it('no longer aliases the re-pointed matrix cells; their personas resolve directly', () => {
    // NORMATIVE/REVIEWING re-pointed AGGREGATE->AGGREGATION (Type-2 TASK) to the
    // Type-1 REVIEW persona; EVALUATIVE/REVIEWING re-pointed
    // RECONCILING->RECONCILIATION to the Type-1 RESEARCH persona.
    expect(PERSONA_ALIASES.AGGREGATE).toBeUndefined();
    expect(PERSONA_ALIASES.RECONCILING).toBeUndefined();
    expect(resolvePersona('REVIEW')).toBe('REVIEW');
    expect(resolvePersona('RESEARCH')).toBe('RESEARCH');
    expect(resolvePersona('AGGREGATE')).toBe('AGGREGATE');
    expect(resolvePersona('RECONCILING')).toBe('RECONCILING');
  });

  it('fixes the broken EVALUATIVE/APPLYING cell: DEPENDENCIES -> EVALUATION (Type-1 persona)', () => {
    // There is no AGENT_DEPENDENCIES.md; the cell previously resolved to the
    // bogus persona id "DEPENDENCIES" and 404'd. EVALUATION is the Type-1
    // persona for the evaluative valley.
    expect(PERSONA_ALIASES.DEPENDENCIES).toBe('EVALUATION');
    expect(resolvePersona('DEPENDENCIES')).toBe('EVALUATION');
    expect(resolvePersona('dependencies')).toBe('EVALUATION');
  });

  it('passes unknown personas through normalized (no alias, no route gating)', () => {
    expect(resolvePersona('RESEARCH')).toBe('RESEARCH');
    expect(resolvePersona('CHANGE')).toBe('CHANGE');
    // EVALUATIVE/JUDGING cell already loaded AGENT_CHANGE.md correctly.
  });
});
