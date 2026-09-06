import React from 'react';
import { act, create } from 'react-test-renderer';
import { expect, it, vi } from 'vitest';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
const state = vi.hoisted(() => ({ events: [] as HarnessEvent[] }));
vi.mock('../../components/workspace/harness-events-provider', () => ({ useHarnessEvents: () => ({ events: state.events }) }));
import { ActivityView, ActivityStrip } from '../../components/woven-dialogue/activity-shelf';
import { ToolStreamList } from '../../components/shell/tool-stream-view';
function event(eventId: string, type: HarnessEvent['type'], data: Record<string, unknown>, sessionId = 'one'): HarnessEvent {
  return { schemaVersion: 1, eventId, sessionId, turnId: 'turn', timestamp: '2026-09-06T01:00:00Z', type, data };
}
it('filters completed projections and clears only observed versions without changing the shared event buffer', () => {
  state.events = [event('start', 'tool.started', { toolUseId: 'tool', toolName: 'read_file' }), event('end', 'tool.completed', { toolUseId: 'tool' })];
  const original = JSON.stringify(state.events);
  const tree = create(<ActivityView />);
  act(() => tree.root.findByProps({ 'aria-label': 'Filter activity' }).props.onChange({ target: { value: 'read_file' } }));
  expect(tree.root.findByType(ToolStreamList).props.rows).toMatchObject([{ toolName: 'read_file', status: 'completed' }]);
  act(() => tree.root.findAllByType('button').find(button => button.children.includes('Clear view'))!.props.onClick());
  expect(tree.root.findByType(ToolStreamList).props.rows).toEqual([]);
  expect(JSON.stringify(state.events)).toBe(original);
  act(() => tree.root.findByProps({ 'aria-label': 'Filter activity' }).props.onChange({ target: { value: '' } }));
  state.events = [...state.events, event('start', 'tool.started', { toolUseId: 'tool', toolName: 'write_file' }, 'two')];
  act(() => tree.update(<ActivityView />));
  expect(tree.root.findByType(ToolStreamList).props.rows).toMatchObject([{ toolName: 'write_file', status: 'running' }]);
  state.events = [event('start', 'tool.started', { toolUseId: 'tool', toolName: 'updated_tool' }), ...state.events.slice(1)];
  act(() => tree.update(<ActivityView />));
  expect(tree.root.findByType(ToolStreamList).props.rows[0].status).toBe('completed');
  expect(tree.root.findByType(ToolStreamList).props.rows.map((row: { toolName: string }) => row.toolName)).toEqual(['updated_tool', 'write_file']);
  act(() => tree.unmount());
});

it('keeps matching tool IDs in different sessions distinct and reveals a later completion after clear', () => {
  state.events = [event('start', 'tool.started', { toolUseId: 'same', toolName: 'read_file' }, 'one'), event('start', 'tool.started', { toolUseId: 'same', toolName: 'read_file' }, 'two')];
  const tree = create(<ActivityView />);
  expect(tree.root.findByType(ToolStreamList).props.rows).toHaveLength(2);
  const strip = create(<ActivityStrip events={state.events} running onOpenDetails={() => {}} />);
  expect(JSON.stringify(strip.toJSON())).toContain('2 actions');
  act(() => tree.root.findAllByType('button').find(button => button.children.includes('Clear view'))!.props.onClick());
  expect(tree.root.findByType(ToolStreamList).props.rows).toEqual([]);
  const completion = event('end', 'tool.completed', { toolUseId: 'same' }, 'one');
  state.events = [...state.events, completion];
  act(() => tree.update(<ActivityView />));
  expect(tree.root.findByType(ToolStreamList).props.rows).toMatchObject([{ key: 'one:same', status: 'completed' }]);
  expect(state.events).toHaveLength(3); expect(state.events[2]).toBe(completion);
  act(() => { tree.unmount(); strip.unmount(); });
});
