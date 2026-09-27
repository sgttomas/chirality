import { describe, expect, it } from 'vitest';
import { CHIRALITY_ROLES } from '@chirality/runtime-contracts/v3';
import { DEFAULT_PERSONA, PERSONA_ALIASES, resolvePersona } from '../../lib/shell/persona-resolution';

describe('resolvePersona', () => {
  it('defaults new chats to HELP_HUMAN', () => {
    expect([null, undefined, '', '   '].map(resolvePersona)).toEqual(Array(4).fill('HELP_HUMAN'));
    expect(DEFAULT_PERSONA).toBe('HELP_HUMAN');
  });

  it('accepts exactly the three direct-entry roles', () => {
    expect(resolvePersona('help_human')).toBe('HELP_HUMAN');
    expect(resolvePersona(' helps_humans ')).toBe('HELPS_HUMANS');
    expect(resolvePersona('working_items')).toBe('WORKING_ITEMS');
    expect(resolvePersona('TASK')).toBe('HELP_HUMAN');
  });

  it('keeps bounded legacy display aliases without reviving retired roles', () => {
    expect(PERSONA_ALIASES).toEqual({ HELP: 'HELP_HUMAN', AGENTS: 'HELPS_HUMANS' });
    expect(resolvePersona('ORCHESTRATE')).toBe('HELP_HUMAN');
    expect(resolvePersona('RESEARCH')).toBe('HELP_HUMAN');
    expect(resolvePersona('CHANGE')).toBe('HELP_HUMAN');
  });

  // Ported by SCA-APP-012 from the retired agent-matrix-cells.test.ts (case 1).
  it('derives exactly the three direct-entry choices from the shared role registry', () => {
    expect(CHIRALITY_ROLES.filter(role => role.directEntry).map(role => role.id)).toEqual([
      'HELP_HUMAN',
      'HELPS_HUMANS',
      'WORKING_ITEMS'
    ]);
    expect(CHIRALITY_ROLES.find(role => role.defaultForNewChat)?.id).toBe('HELP_HUMAN');
    expect(CHIRALITY_ROLES.find(role => role.id === 'TASK')?.directEntry).toBe(false);
  });

  // DEL-08-02-REQ-004: historical RECONCILING and the TYPES §4 matrix labels
  // stay replay metadata and never become execution roles.
  it('resolves RECONCILING and the TYPES §4 matrix row and column labels to HELP_HUMAN without aliasing them', () => {
    const historicalLabels = [
      'RECONCILING',
      'NORMATIVE',
      'OPERATIVE',
      'EVALUATIVE',
      'GUIDING',
      'APPLYING',
      'JUDGING',
      'REVIEWING'
    ];
    for (const label of historicalLabels) {
      expect(resolvePersona(label)).toBe('HELP_HUMAN');
      expect(resolvePersona(label.toLowerCase())).toBe('HELP_HUMAN');
      expect(Object.keys(PERSONA_ALIASES)).not.toContain(label);
    }
  });
});
