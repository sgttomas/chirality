import { beforeEach, expect, it, vi } from 'vitest';
const mocks = vi.hoisted(() => ({ exposed: undefined as unknown, invoke: vi.fn<(...args: unknown[]) => Promise<unknown>>(async () => ({ ok: true })), on: vi.fn(), removeListener: vi.fn(), getPathForFile: vi.fn() }));
vi.mock('electron', () => ({ contextBridge: { exposeInMainWorld: (_name: string, value: unknown) => { mocks.exposed = value; } }, ipcRenderer: { invoke: mocks.invoke, on: mocks.on, removeListener: mocks.removeListener }, webUtils: { getPathForFile: mocks.getPathForFile } }));
import '../../../electron/preload';
type Bridge = {
  folders: { registerRecent: (path: string) => Promise<unknown>; pathForFile: (file: File) => string; subscribeOpen: (listener: (intent: unknown) => void) => () => void };
  document: { inlinePdfPreview: boolean };
  runtime: { service: { restart: () => Promise<unknown> }; hostedAccount?: unknown; daemon?: unknown; models?: unknown };
};
beforeEach(() => vi.clearAllMocks());
it('exposes inline PDF preview as unavailable for the desktop MVP fallback', () => {
  expect((mocks.exposed as Bridge).document.inlinePdfPreview).toBe(false);
});
it('exposes the owned-service restart and none of the retired daemon, model or hosted-account bridges', async () => {
  const runtime = (mocks.exposed as Bridge).runtime;
  expect(runtime.hostedAccount).toBeUndefined(); expect(runtime.daemon).toBeUndefined(); expect(runtime.models).toBeUndefined();
  const result = { ok: true, service: { status: 'ready' } };
  mocks.invoke.mockResolvedValueOnce(result);
  await expect(runtime.service.restart()).resolves.toBe(result);
  expect(mocks.invoke).toHaveBeenLastCalledWith('chirality:runtime-service-restart');
});
it('forwards only the folder path for registration and uses Electron file extraction without inventing paths', async () => {
  const bridge = (mocks.exposed as Bridge).folders;
  await bridge.registerRecent('/chosen'); expect(mocks.invoke).toHaveBeenCalledWith('chirality:folder-register-recent', '/chosen');
  const file = {} as File; mocks.getPathForFile.mockReturnValue('/native/folder'); expect(bridge.pathForFile(file)).toBe('/native/folder'); expect(mocks.getPathForFile).toHaveBeenCalledWith(file);
  mocks.getPathForFile.mockImplementation(() => { throw new TypeError('Not a File'); }); expect(bridge.pathForFile(null as unknown as File)).toBe('');
  mocks.getPathForFile.mockReturnValue(''); expect(bridge.pathForFile(file)).toBe('');
});
it('delivers only the intent payload, registers readiness after listening and unsubscribes the exact listener', () => {
  const listener = vi.fn(); const stop = (mocks.exposed as Bridge).folders.subscribeOpen(listener);
  expect(mocks.on).toHaveBeenCalledWith('chirality:folder-open-intent', expect.any(Function));
  expect(mocks.invoke).toHaveBeenCalledWith('chirality:folder-open-ready');
  expect(mocks.on.mock.invocationCallOrder[0]).toBeLessThan(mocks.invoke.mock.invocationCallOrder[0]);
  const handler = mocks.on.mock.calls[0][1]; const privileged = { sender: 'privileged' }; const intent = { path: '/chosen' };
  handler(privileged, intent); expect(listener).toHaveBeenCalledTimes(1); expect(listener).toHaveBeenCalledWith(intent);
  stop(); expect(mocks.removeListener).toHaveBeenCalledWith('chirality:folder-open-intent', handler);
  handler(privileged, { path: '/later' }); expect(listener).toHaveBeenCalledTimes(1);
});
it('forwards only the project root to the attachment picker channel and returns the fixed result shape', async () => {
  const bridge = (mocks.exposed as Bridge & { attachments: { selectFiles: (request: { projectRoot: string }) => Promise<unknown> } }).attachments;
  const selected = { cancelled: false, paths: ['/project/notes.md'] };
  mocks.invoke.mockResolvedValueOnce(selected);
  await expect(bridge.selectFiles({ projectRoot: '/project', extra: 'ignored' } as { projectRoot: string })).resolves.toBe(selected);
  expect(mocks.invoke).toHaveBeenLastCalledWith('chirality:attachments-select-files', { projectRoot: '/project' });
});
