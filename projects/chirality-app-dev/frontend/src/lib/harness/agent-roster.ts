import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import {
  parseAgentClass,
  parseAgentType,
  readAgentInstruction,
  type AgentClass
} from './agent-instruction';
import { HarnessError } from '@chirality/runtime-contracts/errors';
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
export const UNTYPED_PERSONA = 'UNTYPED';
export const GENERALIST_AGENT2_PERSONA = 'GENERALIST_AGENT2';

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

/**
 * Server-side enforcement of the direct-chat Type-0/Type-1 restriction
 * (D-APP-24). The picker only *offers* Type-0/Type-1 personas, but the
 * session-boot path has no inherent type gate — so a hand-edited
 * `/chat?agent=<Type-2>` URL could otherwise boot a task agent as a top-level
 * persona session, bypassing subagent governance (which engages only on
 * *delegated* subagents). Call this when creating a direct-chat session: it
 * throws an `INVALID_REQUEST` if the persona is not Type-0/Type-1. The picker
 * and the server thus share one enforcement predicate (`isDirectChatPersona`).
 */
export async function assertDirectChatPersona(
  persona: string,
  instructionRootOverride?: string
): Promise<void> {
  if (persona.trim().toUpperCase() === UNTYPED_PERSONA) {
    return;
  }
  const instruction = await readAgentInstruction(persona, instructionRootOverride);
  const entry: AgentRosterEntry = {
    name: persona,
    type: parseAgentType(instruction.content),
    class: parseAgentClass(instruction.content)
  };

  if (!isDirectChatPersona(entry)) {
    throw new HarnessError(
      'INVALID_REQUEST',
      400,
      `Persona '${persona}' is not available for direct chat; only Type-0/Type-1 personas may run a direct-chat session (Type-2 task agents run via orchestration).`,
      { persona, type: entry.type }
    );
  }
}
