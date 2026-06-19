import { mkdtemp, mkdir, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import {
  isDirectChatPersona,
  listAgentRoster,
  selectDirectChatPersonas
} from '../../lib/harness/agent-roster';

let tmpRoot = '';
let instructionRoot = '';
let agentsDir = '';

async function writeAgent(name: string, body: string): Promise<void> {
  await writeFile(path.join(agentsDir, `AGENT_${name}.md`), body, 'utf8');
}

beforeEach(async () => {
  tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-agent-roster-'));
  instructionRoot = path.join(tmpRoot, 'instruction-root');
  agentsDir = path.join(instructionRoot, 'agents');
  await mkdir(agentsDir, { recursive: true });

  await writeAgent('WORKING_ITEMS', 'AGENT_TYPE: 1\nAGENT_CLASS: PERSONA\n');
  await writeAgent('HELPS_HUMANS', 'AGENT_TYPE: 0\nAGENT_CLASS: PERSONA\n');
  await writeAgent('TASK', 'AGENT_TYPE: 2\nAGENT_CLASS: TASK\n');
  await writeAgent(
    'EVALUATION_DEPENDENCY_AUDIT',
    '| **AGENT_TYPE** | TYPE 2 |\n| **AGENT_CLASS** | TASK |\n'
  );
  await writeAgent('NO_TYPE', '# no governance markers here\n');
  // Non-agent files in the dir must be ignored.
  await writeFile(path.join(agentsDir, 'README.md'), '# not an agent\n', 'utf8');
});

afterEach(async () => {
  if (tmpRoot) {
    await rm(tmpRoot, { recursive: true, force: true });
  }
  tmpRoot = '';
  instructionRoot = '';
  agentsDir = '';
});

describe('listAgentRoster', () => {
  it('enumerates AGENT_*.md, strips prefix/suffix, parses type/class, sorts by name', async () => {
    const roster = await listAgentRoster(instructionRoot);

    expect(roster.map((entry) => entry.name)).toEqual([
      'EVALUATION_DEPENDENCY_AUDIT',
      'HELPS_HUMANS',
      'NO_TYPE',
      'TASK',
      'WORKING_ITEMS'
    ]);

    const byName = new Map(roster.map((entry) => [entry.name, entry]));
    expect(byName.get('WORKING_ITEMS')).toEqual({
      name: 'WORKING_ITEMS',
      type: 1,
      class: 'PERSONA'
    });
    expect(byName.get('HELPS_HUMANS')).toEqual({
      name: 'HELPS_HUMANS',
      type: 0,
      class: 'PERSONA'
    });
    expect(byName.get('TASK')).toEqual({ name: 'TASK', type: 2, class: 'TASK' });
    expect(byName.get('EVALUATION_DEPENDENCY_AUDIT')).toEqual({
      name: 'EVALUATION_DEPENDENCY_AUDIT',
      type: 2,
      class: 'TASK'
    });
  });

  it('tolerates agents missing governance markers (type/class undefined)', async () => {
    const roster = await listAgentRoster(instructionRoot);
    const noType = roster.find((entry) => entry.name === 'NO_TYPE');
    expect(noType).toEqual({ name: 'NO_TYPE', type: undefined, class: undefined });
  });

  it('ignores non-AGENT files in the directory', async () => {
    const roster = await listAgentRoster(instructionRoot);
    expect(roster.some((entry) => entry.name === 'README')).toBe(false);
  });
});

describe('selectDirectChatPersonas (D-APP-24: restrict to Type-0/Type-1)', () => {
  it('keeps Type-0/Type-1 personas and excludes Type-2 + untyped', async () => {
    const roster = await listAgentRoster(instructionRoot);
    const direct = selectDirectChatPersonas(roster);

    expect(direct.map((entry) => entry.name)).toEqual(['HELPS_HUMANS', 'WORKING_ITEMS']);
    expect(direct.some((entry) => entry.type === 2)).toBe(false);
    expect(direct.some((entry) => entry.type === undefined)).toBe(false);
  });

  it('isDirectChatPersona predicate gates on type 0/1 only', () => {
    expect(isDirectChatPersona({ name: 'A', type: 0, class: 'PERSONA' })).toBe(true);
    expect(isDirectChatPersona({ name: 'B', type: 1, class: 'PERSONA' })).toBe(true);
    expect(isDirectChatPersona({ name: 'C', type: 2, class: 'TASK' })).toBe(false);
    expect(isDirectChatPersona({ name: 'D', type: undefined, class: undefined })).toBe(false);
  });
});
