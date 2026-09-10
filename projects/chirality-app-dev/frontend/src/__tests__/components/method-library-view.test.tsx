import React from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { beforeEach, expect, it, vi } from 'vitest';

const mocks = vi.hoisted(() => ({ list: vi.fn(), inspect: vi.fn() }));
vi.mock('../../lib/harness/method-selection-client', async importOriginal => ({
  ...await importOriginal<typeof import('../../lib/harness/method-selection-client')>(),
  listMethods: mocks.list,
  inspectMethod: mocks.inspect
}));
import { MethodLibraryView } from '../../components/woven-dialogue/method-library-view';

const descriptor = (name: string, sourceRootId: string) => ({
  qualifiedId: `${sourceRootId}/skill/${name}`,
  sourceRootId,
  source: 'project' as const,
  kind: 'skill' as const,
  name,
  description: `${name} description`,
  central: false,
  compatibility: 'canonical' as const,
  executionRoleIds: ['TASK'] as const,
  resources: []
});
const response = (methods: ReturnType<typeof descriptor>[]) => ({ schemaVersion: 'chirality.methods/v3' as const, methods, malformedPackages: [] });
function deferred<T>() { let resolve!: (value: T) => void; const promise = new Promise<T>(done => { resolve = done; }); return { promise, resolve }; }

beforeEach(() => vi.clearAllMocks());

it('does not let an aborted project catalog overwrite the current project', async () => {
  const oldResult = deferred<ReturnType<typeof response>>();
  const nextResult = deferred<ReturnType<typeof response>>();
  mocks.list.mockImplementation((root: string) => root === '/old' ? oldResult.promise : nextResult.promise);
  let tree!: ReactTestRenderer;
  await act(async () => { tree = create(<MethodLibraryView projectRoot="/old" selected={[]} onSelectedChange={() => {}} />); });
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  await act(async () => { tree.update(<MethodLibraryView projectRoot="/next" selected={[]} onSelectedChange={() => {}} />); });
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  await act(async () => nextResult.resolve(response([descriptor('current-method', 'next-root')])));
  await act(async () => oldResult.resolve(response([descriptor('stale-method', 'old-root')])));
  const text = JSON.stringify(tree.toJSON());
  expect(text).toContain('current-method');
  expect(text).not.toContain('stale-method');
  expect(tree.root.findAllByProps({ role: 'alert' })).toHaveLength(0);
});

it('keeps only the newest inspection result', async () => {
  const a = descriptor('method-a', 'root-a');
  const b = descriptor('method-b', 'root-b');
  mocks.list.mockResolvedValue(response([a, b]));
  const inspectA = deferred<any>(); const inspectB = deferred<any>();
  mocks.inspect.mockImplementation((_root: string, method: { name: string }) => method.name === 'method-a' ? inspectA.promise : inspectB.promise);
  let tree!: ReactTestRenderer;
  await act(async () => { tree = create(<MethodLibraryView projectRoot="/project" selected={[]} onSelectedChange={() => {}} />); });
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  const inspectButtons = tree.root.findAllByType('button').filter(button => button.children.includes('Inspect'));
  await act(async () => inspectButtons[0].props.onClick());
  await act(async () => inspectButtons[1].props.onClick());
  await act(async () => inspectB.resolve({ schemaVersion: 'chirality.method-inspection/v3', method: b, entrypoint: { content: 'B instructions', sha256: 'b'.repeat(64) }, resources: [] }));
  await act(async () => inspectA.resolve({ schemaVersion: 'chirality.method-inspection/v3', method: a, entrypoint: { content: 'A instructions', sha256: 'a'.repeat(64) }, resources: [] }));
  const text = JSON.stringify(tree.toJSON());
  expect(text).toContain('B instructions');
  expect(text).not.toContain('A instructions');
});

it('reloads the catalog when the panel requests a refresh', async () => {
  mocks.list.mockRejectedValueOnce(new Error('Daemon was unavailable'))
    .mockResolvedValue(response([descriptor('available-again', 'project-root')]));
  let tree!: ReactTestRenderer;
  await act(async () => { tree = create(<MethodLibraryView projectRoot="/project" selected={[]} onSelectedChange={() => {}} refresh={0} />); });
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  expect(JSON.stringify(tree.toJSON())).toContain('Daemon was unavailable');
  await act(async () => { tree.update(<MethodLibraryView projectRoot="/project" selected={[]} onSelectedChange={() => {}} refresh={1} />); });
  await act(async () => { await new Promise(resolve => setTimeout(resolve, 0)); });
  expect(mocks.list).toHaveBeenCalledTimes(2);
  expect(JSON.stringify(tree.toJSON())).toContain('available-again');
});
