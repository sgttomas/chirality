import { describe, it, expect } from 'vitest';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
import { deriveNativeProgress } from '../../lib/shell/native-progress';
import { deriveSubagentActivity } from '../../lib/shell/harness-event-views';
import { deriveTurnActivityFromEvents } from '../../lib/shell/turn-activity';
const e = (id: string, method: string, params: Record<string, unknown>): HarnessEvent => ({ schemaVersion: 1, eventId: id, sessionId: 'session', turnId: 'runtime-parent', timestamp: '2026-09-12T00:00:00Z', type: 'codex.notification', data: { method, params, codex: { providerThreadId: 'parent', providerTurnId: 'parent-turn' } } });
const scope = { threadId: 'parent', turnId: 'native-turn' };
describe('native progress replay', () => {
  it('replaces the checklist, keeps empty revisions and isolates actual child turn identity', () => {
    const events = [e('1', 'turn/plan/updated', { ...scope, plan: [{ step: 'Read', status: 'pending' }] }),
      e('2', 'turn/plan/updated', { ...scope, plan: [{ step: 'Read', status: 'completed' }, { step: 'Write', status: 'inProgress' }] }),
      e('3', 'turn/plan/updated', { threadId: 'child', turnId: 'child-turn', plan: [] })];
    expect(deriveNativeProgress(events).checklists).toMatchObject([{ steps: [{ status: 'completed' }, { status: 'inProgress' }] }, { steps: [] }]);
    expect(deriveTurnActivityFromEvents(events)).toEqual(deriveTurnActivityFromEvents(JSON.parse(JSON.stringify(events))));
  });
  it('reconciles indexed summaries and excludes hidden reasoning content', () => {
    const events = [e('1', 'item/reasoning/summaryTextDelta', { ...scope, itemId: 'r', summaryIndex: 0, delta: 'Checking' }),
      e('2', 'item/reasoning/summaryTextDelta', { ...scope, itemId: 'r', summaryIndex: 0, delta: ' the file' }),
      e('3', 'item/completed', { ...scope, item: { id: 'r', type: 'reasoning', summary: ['Checked the file'], content: ['Never display this'] } })];
    expect(deriveNativeProgress(events).summaries.map(row => row.text)).toEqual(['Checked the file']);
    expect(JSON.stringify(deriveTurnActivityFromEvents(events))).not.toContain('Never display this');
  });
  it('does not mistake completed spawn calls or the parent completion for child completion', () => {
    const events = [e('1', 'item/completed', { ...scope, item: { id: 'spawn', type: 'collabAgentToolCall', status: 'completed', receiverThreadIds: ['child-a', 'child-b'], prompt: 'Review the patch', agentsStates: { 'child-a': { status: 'running' }, 'child-b': { status: 'pendingInit' } } } }),
      e('2', 'turn/completed', { threadId: 'parent', turn: { id: 'native-turn', status: 'completed' } }),
      e('3', 'item/completed', { threadId: 'child-a', turnId: 'child-turn', item: { type: 'agentMessage', id: 'answer', text: 'Found one issue.' } }),
      e('4', 'turn/completed', { threadId: 'child-a', turn: { id: 'child-turn', status: 'failed' } })];
    expect(deriveSubagentActivity(events)).toMatchObject([{ status: 'failed', description: 'Review the patch', summary: 'Found one issue.' }, { status: 'waiting' }]);
  });
});
it('records the explicit child observation boundary without declaring the task completed', () => {
  const events = [e('spawn', 'item/completed', { ...scope, item: { type: 'collabAgentToolCall', receiverThreadIds: ['child'], agentsStates: { child: { status: 'running' } } } }),
    e('limit', 'chirality/nativeChildren/observationEnded', { ...scope, agentThreadIds: ['child'], reason: 'parentTurnEnded', message: 'Later child activity is not recorded here.' })];
  expect(deriveSubagentActivity(events)[0]).toMatchObject({ status: 'running', observationEnded: 'Later child activity is not recorded here.' });
  expect(deriveTurnActivityFromEvents(events).running).toBe(0);
});
