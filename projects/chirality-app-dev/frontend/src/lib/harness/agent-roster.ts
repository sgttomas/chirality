import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import { parseAgentClass, parseAgentType, type AgentClass } from './agent-instruction';
import { assertInstructionRootReadable } from './instruction-root';

/**
 * One enumerated agent from the instruction-root `agents/` directory, carrying
 * the parsed governance classification (`AGENT_TYPE` / `AGENT_CLASS`). `name` is
 * the persona id consumed by `resolvePersona` / `buildSystemPrompt` — the
 * `AGENT_` prefix and `.md` suffix are stripped, hyphens left as-authored.
 */
export type AgentRosterEntry = {
  name: string;
  type: number | undefined;
  class: AgentClass | undefined;
};

const AGENT_FILE_PATTERN = /^AGENT_(.+)\.md$/;

/**
 * Enumerate the agent roster from `<instructionRoot>/agents/AGENT_*.md`, parsing
 * the type/class of each. This is the source of truth the Phase 5 persona picker
 * filters on — no such enumerator existed before (subagent-governance only
 * *validated* delegated candidates, it never listed the roster). Server-only.
 *
 * `instructionRootOverride` is resolved directly (no scaffold assertion) so tests
 * can point at a bare `agents/` fixture; the default path goes through
 * `assertInstructionRootReadable` like every other instruction-root reader.
 */
export async function listAgentRoster(
  instructionRootOverride?: string
): Promise<AgentRosterEntry[]> {
  const instructionRoot = instructionRootOverride
    ? path.resolve(instructionRootOverride)
    : await assertInstructionRootReadable();
  const agentsDir = path.join(instructionRoot, 'agents');

  const entries = await readdir(agentsDir);
  const roster: AgentRosterEntry[] = [];

  for (const entry of entries) {
    const match = AGENT_FILE_PATTERN.exec(entry);
    if (!match) {
      continue;
    }

    let content = '';
    try {
      content = await readFile(path.join(agentsDir, entry), 'utf8');
    } catch {
      // Skip entries that disappear or are unreadable mid-traversal rather than
      // failing the whole roster.
      continue;
    }

    roster.push({
      name: match[1],
      type: parseAgentType(content),
      class: parseAgentClass(content)
    });
  }

  roster.sort((a, b) => a.name.localeCompare(b.name));
  return roster;
}

/**
 * The direct-chat picker is restricted to Type-0/Type-1 personas (D-APP-24):
 * Type-2 task agents are governed to run only via the orchestrated/INIT path,
 * never ad-hoc direct chat. This pure predicate is the enforcement point.
 */
export function isDirectChatPersona(entry: AgentRosterEntry): boolean {
  return entry.type === 0 || entry.type === 1;
}

export function selectDirectChatPersonas(
  roster: readonly AgentRosterEntry[]
): AgentRosterEntry[] {
  return roster.filter(isDirectChatPersona);
}
