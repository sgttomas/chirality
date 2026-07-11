import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

const REGISTER_PATH = path.resolve(
  process.cwd(),
  '..',
  'docs',
  'harness',
  'reliance_boundary_register.md'
);

const REQUIRED_BOUNDARIES = [
  'RB-ENGINE',
  'RB-AUDIT',
  'RB-PERMISSION',
  'RB-FILESYSTEM',
  'RB-LIFECYCLE',
  'RB-TRANSCRIPT',
  'RB-SETTINGS',
  'RB-SUBAGENT',
  'RB-HUMAN-GATE',
  'RB-TOOL-SURFACE',
  'RB-HOOKS',
  'RB-REDACTION',
  'RB-FALLBACK'
];

describe('reliance boundary register', () => {
  it('retains the governed schema, boundary inventory, and implemented Section 9 index', async () => {
    const register = await readFile(REGISTER_PATH, 'utf8');

    for (const field of [
      'BoundaryID',
      'BoundaryCategory',
      'ProductSemantic',
      'SourceRefs',
      'EnforcementOwner',
      'EnforcementSurface',
      'ValidationID',
      'ResidualRisk',
      'DecisionStatus'
    ]) {
      expect(register).toContain(`| ${field} |`);
    }
    for (const boundary of REQUIRED_BOUNDARIES) {
      expect(register).toContain(`| ${boundary} |`);
    }
    for (const id of [
      'section9.reliance_boundary_register',
      'section9.sdk_session_link_resume',
      'section9.domain_profile_validation'
    ]) {
      expect(register).toContain(`| \`${id}\` |`);
    }

    expect(register).toContain('does not authorize apply behavior');
    expect(register).not.toContain('Not implemented in the current Section 9 script');
  });
});
