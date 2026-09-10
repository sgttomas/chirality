import React from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, expect, it, vi } from 'vitest';
import { createDefaultWovenWorkspaceState } from '../../lib/woven-dialogue/woven-workspace-state';

const mocks = vi.hoisted(() => ({ list: vi.fn() }));
vi.mock('../../lib/harness/method-selection-client', async importOriginal => ({
  ...await importOriginal<typeof import('../../lib/harness/method-selection-client')>(),
  listMethods: mocks.list
}));
vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: '/project' })
}));
vi.mock('../../components/woven-dialogue/activity-shelf', () => ({ ActivityView: () => null }));
vi.mock('../../components/shell/file-tree-panel', () => ({ FileTreePanel: () => null }));
vi.mock('../../components/shell/document-view', () => ({ DocumentView: () => null, handoffDocument: vi.fn() }));

import { RightPanel } from '../../components/woven-dialogue/right-panel';

afterEach(() => vi.clearAllMocks());

it('retries an unavailable method catalog through the panel Refresh action', async () => {
  mocks.list.mockRejectedValueOnce(new Error('Daemon was unavailable')).mockResolvedValue({
    schemaVersion: 'chirality.methods/v3', methods: [], malformedPackages: []
  });
  let tree!: ReactTestRenderer;
  await act(async () => {
    tree = create(<RightPanel
      state={{ ...createDefaultWovenWorkspaceState(), rightPanelView: 'workflows' }}
      sessionOpen={false}
      onView={() => {}}
      onOpenFile={() => {}}
      onClose={() => {}}
      onExpand={() => {}}
      coordination={null}
    />);
  });
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  expect(JSON.stringify(tree.toJSON())).toContain('Daemon was unavailable');
  expect(JSON.stringify(tree.toJSON())).toContain('Workflows');
  const refresh = tree.root.findAllByType('button').find(node => node.children.includes('Refresh'))!;
  await act(async () => refresh.props.onClick());
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  expect(mocks.list).toHaveBeenCalledTimes(2);
  act(() => tree.unmount());
});
