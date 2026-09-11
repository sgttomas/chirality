import React from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, expect, it, vi } from 'vitest';

const api = vi.hoisted(() => ({ get: vi.fn(), initialize: vi.fn(), consent: vi.fn(), start: vi.fn(), cancel: vi.fn(), signOut: vi.fn() }));
vi.mock('../../lib/harness/hosted-bootstrap-client', () => ({
  hydrateHostedBootstrapProject: (root: string, _onBound: unknown, signal: AbortSignal) => api.get(root, signal),
  getHostedBootstrapStatus: api.get,
  initializeHostedBootstrapProject: api.initialize,
  grantHostedProviderNetworkConsent: api.consent,
  startHostedBootstrapLogin: api.start,
  cancelHostedBootstrapLogin: api.cancel,
  signOutHostedBootstrapProject: api.signOut
}));

import { useHostedBootstrapController, type HostedBootstrapController } from '../../components/settings/hosted-bootstrap-controller';
import { HostedBootstrapView, hostedBootstrapSummary } from '../../components/settings/hosted-bootstrap-view';

const root = '/projects/example';
const status = (ceremony: 'consent-required' | 'ready-to-start' | 'pending' | 'signed-in' | 'failed' | 'cancelled', admission: 'unavailable' | 'establishing' | 'ready' = 'unavailable') => ({
  schema: 'chirality-hosted-bootstrap-status/v1' as const,
  projectId: 'example', ceremony, admission,
  canStartLogin: ['ready-to-start', 'failed', 'cancelled'].includes(ceremony)
});
const registered = (ceremony: Parameters<typeof status>[0], admission?: Parameters<typeof status>[1]) => ({ registration: 'registered' as const, projectId: 'example', status: status(ceremony, admission) });
function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>(done => { resolve = done; });
  return { promise, resolve };
}

let tree: ReactTestRenderer;
let latest!: HostedBootstrapController;
function Fixture({ projectRoot = root, refresh = () => {} }: { projectRoot?: string | null; refresh?: () => void }): JSX.Element {
  latest = useHostedBootstrapController(projectRoot, refresh);
  return <HostedBootstrapView controller={latest} />;
}
const text = (): string => JSON.stringify(tree.toJSON());
const button = (label: string) => tree.root.findAllByType('button').find(node => node.children.join('') === label)!;

beforeEach(() => {
  vi.clearAllMocks();
  vi.stubGlobal('window', { setInterval: (...args: Parameters<typeof globalThis.setInterval>) => globalThis.setInterval(...args), clearInterval: (timer: ReturnType<typeof globalThis.setInterval>) => globalThis.clearInterval(timer) });
  api.get.mockResolvedValue({ registration: 'required' });
});
afterEach(() => { tree?.unmount(); vi.useRealTimers(); vi.unstubAllGlobals(); });

it('requires an explicit project setup, consent, and sign-in before exposing the validated provider URL', async () => {
  const refresh = vi.fn();
  await act(async () => { tree = create(<Fixture refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  expect(text()).toContain('Use this folder');
  expect(text()).toContain('one minimal');
  expect(tree.root.findAllByType('a')).toHaveLength(0);

  api.initialize.mockResolvedValue(registered('consent-required'));
  await act(async () => { button('Use this folder').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(refresh).toHaveBeenCalledTimes(1);
  expect(text()).toContain('Allow provider network');

  api.consent.mockResolvedValue(status('ready-to-start'));
  await act(async () => { button('Allow provider network').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Sign in');
  api.start.mockResolvedValue({ loginId: 'login-1', authUrl: 'https://auth.openai.example/login-1' });
  api.get.mockResolvedValue(registered('pending', 'establishing'));
  await act(async () => { button('Sign in').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  const link = tree.root.findByType('a');
  expect(link.props).toMatchObject({ href: 'https://auth.openai.example/login-1', target: '_blank', rel: 'noreferrer' });
  expect(text()).toContain('Cancel sign-in');

  api.cancel.mockResolvedValue(status('cancelled'));
  await act(async () => { button('Cancel sign-in').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(tree.root.findAllByType('a')).toHaveLength(0);
  expect(text()).toContain('previous sign-in was cancelled');
});

it('keeps setup available after a binding conflict and surfaces the error without changing files implicitly', async () => {
  api.get.mockRejectedValue(new Error('Another working root is currently bound'));
  await act(async () => { tree = create(<Fixture />); });
  await act(async () => { await Promise.resolve(); });
  expect(text()).toContain('Another working root is currently bound');
  expect(text()).toContain('Use this folder');
  expect(api.initialize).not.toHaveBeenCalled();
});

it('does not restart hydration when the caller supplies a new refresh callback', async () => {
  await act(async () => { tree = create(<Fixture refresh={() => {}} />); });
  await act(async () => { await Promise.resolve(); });
  expect(api.get).toHaveBeenCalledOnce();

  await act(async () => { tree.update(<Fixture refresh={() => {}} />); });
  await act(async () => { await Promise.resolve(); });
  expect(api.get).toHaveBeenCalledOnce();
});

it('distinguishes signed-in state from readiness and publishes the ready transition once', async () => {
  vi.useFakeTimers();
  const refresh = vi.fn();
  api.get.mockResolvedValue(registered('signed-in', 'establishing'));
  await act(async () => { tree = create(<Fixture refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  expect(hostedBootstrapSummary(latest)).toBe('Signed in · Preparing engine');
  expect(text()).toContain('still preparing');
  expect(refresh).toHaveBeenCalledTimes(1);

  api.get.mockResolvedValue(registered('signed-in', 'ready'));
  await act(async () => { await vi.advanceTimersByTimeAsync(1000); });
  expect(hostedBootstrapSummary(latest)).toBe('Signed in · Ready to work');
  expect(text()).toContain('Codex is ready for this project');
  expect(refresh).toHaveBeenCalledTimes(2);
});

it('never exposes identity, private paths, or digests in hosted status presentation', async () => {
  api.get.mockResolvedValue(registered('signed-in', 'ready'));
  await act(async () => { tree = create(<Fixture />); });
  await act(async () => { await Promise.resolve(); });
  expect(text()).not.toMatch(/email|token|digest|CODEX_HOME|\.codex/i);
});

it('rejects a late A result across an A to B to A root cycle', async () => {
  const firstA = deferred<ReturnType<typeof registered>>();
  let actionSignal!: AbortSignal;
  api.initialize.mockImplementation((_projectRoot: string, signal: AbortSignal) => { actionSignal = signal; return firstA.promise; });
  const refresh = vi.fn();
  await act(async () => { tree = create(<Fixture projectRoot="/projects/a" refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => button('Use this folder').props.onClick());
  await act(async () => tree.update(<Fixture projectRoot="/projects/b" refresh={refresh} />));
  await act(async () => tree.update(<Fixture projectRoot="/projects/a" refresh={refresh} />));
  await act(async () => { await Promise.resolve(); });
  expect(text()).toContain('Use this folder');
  await act(async () => { firstA.resolve(registered('signed-in', 'ready')); await Promise.resolve(); await Promise.resolve(); });
  expect(actionSignal.aborted).toBe(true);
  expect(text()).toContain('Use this folder');
  expect(text()).not.toContain('Ready to work');
  expect(refresh).not.toHaveBeenCalled();
});

it('aborts a pending action on unmount without publishing its late result', async () => {
  const setup = deferred<ReturnType<typeof registered>>();
  let actionSignal!: AbortSignal;
  api.initialize.mockImplementation((_projectRoot: string, signal: AbortSignal) => { actionSignal = signal; return setup.promise; });
  const refresh = vi.fn();
  await act(async () => { tree = create(<Fixture refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => button('Use this folder').props.onClick());
  await act(async () => tree.unmount());
  expect(actionSignal.aborted).toBe(true);
  await act(async () => { setup.resolve(registered('consent-required')); await Promise.resolve(); });
  expect(refresh).not.toHaveBeenCalled();
});

it('does not let an in-flight pending poll overwrite a completed cancellation', async () => {
  vi.useFakeTimers();
  const poll = deferred<ReturnType<typeof registered>>();
  let pollSignal!: AbortSignal;
  api.get.mockResolvedValueOnce(registered('pending', 'establishing')).mockImplementationOnce((_root: string, signal: AbortSignal) => {
    pollSignal = signal;
    return poll.promise;
  });
  api.cancel.mockResolvedValue(status('cancelled'));
  await act(async () => { tree = create(<Fixture />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => { vi.advanceTimersByTime(1000); await Promise.resolve(); });
  await act(async () => { button('Cancel sign-in').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(pollSignal.aborted).toBe(true);
  expect(text()).toContain('previous sign-in was cancelled');
  await act(async () => { poll.resolve(registered('pending', 'establishing')); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('previous sign-in was cancelled');
  expect(text()).not.toContain('Sign-in pending');
});

it('resumes pending status polling after cancellation fails', async () => {
  vi.useFakeTimers();
  const refresh = vi.fn();
  api.get.mockResolvedValueOnce(registered('pending', 'establishing')).mockResolvedValue(registered('signed-in', 'ready'));
  api.cancel.mockRejectedValue(new Error('Cancellation transport failed'));
  await act(async () => { tree = create(<Fixture refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => { button('Cancel sign-in').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Cancellation transport failed');
  expect(text()).toContain('Sign-in pending');
  await act(async () => { await vi.advanceTimersByTimeAsync(1000); });
  expect(text()).toContain('Signed in · Ready to work');
  expect(text()).not.toContain('Cancellation transport failed');
  expect(refresh).toHaveBeenCalledTimes(2);
});

it('keeps the login link, cancellation, and polling when status reconciliation fails after start', async () => {
  vi.useFakeTimers();
  api.get
    .mockResolvedValueOnce(registered('ready-to-start'))
    .mockRejectedValueOnce(new Error('Status reconciliation failed'))
    .mockResolvedValue(registered('signed-in', 'ready'));
  api.start.mockResolvedValue({ loginId: 'login-recovery', authUrl: 'https://auth.openai.example/login-recovery' });
  await act(async () => { tree = create(<Fixture />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => { button('Sign in').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Sign-in pending');
  expect(text()).toContain('Status reconciliation failed');
  expect(latest.snapshot?.registration === 'registered' ? latest.snapshot.status.admission : null).toBe('unavailable');
  expect(button('Cancel sign-in')).toBeDefined();
  expect(tree.root.findByType('a').props.href).toBe('https://auth.openai.example/login-recovery');
  expect(tree.root.findAllByType('button').some(node => node.children.join('') === 'Sign in')).toBe(false);

  await act(async () => { await vi.advanceTimersByTimeAsync(1000); });
  expect(text()).toContain('Signed in · Ready to work');
  expect(text()).not.toContain('Status reconciliation failed');
  expect(tree.root.findAllByType('a')).toHaveLength(0);
});

it('signs out only this project and republishes readiness after explicit consent and sign-in', async () => {
  const refresh = vi.fn();
  api.get.mockResolvedValueOnce(registered('signed-in', 'ready'));
  const signedOut = deferred<ReturnType<typeof status>>();
  api.signOut.mockReturnValue(signedOut.promise);
  await act(async () => { tree = create(<Fixture refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  expect(button('Sign out of this project')).toBeDefined();
  expect(refresh).toHaveBeenCalledTimes(1);

  await act(async () => button('Sign out of this project').props.onClick());
  expect(text()).toContain('Signing out of this project');
  expect(button('Signing out…').props.disabled).toBe(true);
  expect(refresh).toHaveBeenCalledTimes(1);
  await act(async () => { signedOut.resolve(status('consent-required')); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Allow provider network');
  expect(refresh).toHaveBeenCalledTimes(2);

  api.consent.mockResolvedValue(status('ready-to-start'));
  await act(async () => { button('Allow provider network').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  api.start.mockResolvedValue({ loginId: 'again', authUrl: 'https://auth.openai.example/again' });
  api.get.mockResolvedValue(registered('signed-in', 'ready'));
  await act(async () => { button('Sign in').props.onClick(); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Signed in · Ready to work');
  expect(refresh).toHaveBeenCalledTimes(3);
});

it('keeps sign-out uncertainty unavailable, refreshes after reconciliation, and does not claim success', async () => {
  const refresh = vi.fn();
  api.get.mockResolvedValueOnce(registered('signed-in', 'ready')).mockResolvedValueOnce(registered('failed', 'unavailable'));
  api.signOut.mockRejectedValue(new Error('transport detail'));
  await act(async () => { tree = create(<Fixture refresh={refresh} />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => { button('Sign out of this project').props.onClick(); await Promise.resolve(); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Sign-out could not be confirmed');
  expect(text()).not.toContain('Sign-in failed');
  expect(text()).not.toContain('Ready to work');
  expect(latest.snapshot?.registration === 'registered' ? latest.snapshot.status.admission : null).toBe('unavailable');
  expect(refresh).toHaveBeenCalledTimes(2);
});

it('rejects a late sign-out result across an A to B to A root cycle', async () => {
  const late = deferred<ReturnType<typeof status>>();
  let signal!: AbortSignal;
  api.get.mockResolvedValueOnce({ registration: 'registered', projectId: 'a', status: { ...status('signed-in', 'ready'), projectId: 'a' } }).mockResolvedValue({ registration: 'required' });
  api.signOut.mockImplementation((_root: string, actionSignal: AbortSignal) => { signal = actionSignal; return late.promise; });
  await act(async () => { tree = create(<Fixture projectRoot="/projects/a" />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => button('Sign out of this project').props.onClick());
  await act(async () => tree.update(<Fixture projectRoot="/projects/b" />));
  await act(async () => tree.update(<Fixture projectRoot="/projects/a" />));
  await act(async () => { await Promise.resolve(); });
  await act(async () => { late.resolve(status('consent-required')); await Promise.resolve(); await Promise.resolve(); });
  expect(signal.aborted).toBe(true);
  expect(text()).toContain('Use this folder');
});

it('does not let an in-flight readiness poll restore ready after sign-out starts', async () => {
  vi.useFakeTimers();
  const poll = deferred<ReturnType<typeof registered>>();
  const logout = deferred<ReturnType<typeof status>>();
  api.get.mockResolvedValueOnce(registered('signed-in', 'establishing')).mockReturnValueOnce(poll.promise);
  api.signOut.mockReturnValue(logout.promise);
  await act(async () => { tree = create(<Fixture />); });
  await act(async () => { await Promise.resolve(); });
  await act(async () => { await vi.advanceTimersByTimeAsync(1000); });
  await act(async () => button('Sign out of this project').props.onClick());
  await act(async () => { poll.resolve(registered('signed-in', 'ready')); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Signing out of this project');
  expect(text()).not.toContain('Ready to work');
  await act(async () => { logout.resolve(status('consent-required')); await Promise.resolve(); await Promise.resolve(); });
  expect(text()).toContain('Allow provider network');
});
