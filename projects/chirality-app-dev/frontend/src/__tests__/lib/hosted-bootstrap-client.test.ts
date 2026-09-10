import { afterEach, describe, expect, it, vi } from 'vitest';

import {
  cancelHostedBootstrapLogin,
  getHostedBootstrapStatus,
  grantHostedProviderNetworkConsent,
  initializeHostedBootstrapProject,
  signOutHostedBootstrapProject,
  startHostedBootstrapLogin
} from '../../lib/harness/hosted-bootstrap-client';

afterEach(() => vi.unstubAllGlobals());

function installDesktopAccountBridge(overrides: Record<string, ReturnType<typeof vi.fn>> = {}) {
  const hostedAccount = {
    status: vi.fn(),
    grantProviderNetworkConsent: vi.fn(),
    startLogin: vi.fn(),
    cancelLogin: vi.fn(),
    signOut: vi.fn(),
    ...overrides
  };
  vi.stubGlobal('window', { chirality: { runtime: { hostedAccount } } });
  return hostedAccount;
}

describe('hosted bootstrap renderer client', () => {
  it('routes status through the fixed desktop bridge with only the selected project root', async () => {
    const result = { registration: 'required' };
    const bridge = installDesktopAccountBridge({ status: vi.fn().mockResolvedValue(result) });
    await expect(getHostedBootstrapStatus('/project one')).resolves.toEqual(result);
    expect(bridge.status).toHaveBeenCalledWith('/project one');
  });

  it('keeps initialization on Next and routes account effects through the fixed bridge', async () => {
    const status = {
      schema: 'chirality-hosted-bootstrap-status/v1',
      projectId: 'project-one',
      ceremony: 'ready-to-start',
      admission: 'unavailable',
      canStartLogin: true
    };
    const fetchMock = vi.fn().mockResolvedValueOnce(new Response(JSON.stringify({
      registration: 'registered', projectId: 'project-one', status
    }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const bridge = installDesktopAccountBridge();
    bridge.grantProviderNetworkConsent.mockResolvedValue({ registration: 'registered', projectId: 'project-one', status });
    bridge.startLogin.mockResolvedValue({ loginId: 'login-1', authUrl: 'https://example.test/login' });
    bridge.cancelLogin.mockResolvedValue({ registration: 'registered', projectId: 'project-one', status: { ...status, ceremony: 'cancelled' } });
    bridge.signOut.mockResolvedValue({ registration: 'registered', projectId: 'project-one', status: { ...status, ceremony: 'consent-required', canStartLogin: false } });

    await initializeHostedBootstrapProject('/project');
    await grantHostedProviderNetworkConsent('/project');
    await startHostedBootstrapLogin('/project');
    await cancelHostedBootstrapLogin('/project');
    await signOutHostedBootstrapProject('/project');

    expect(fetchMock).toHaveBeenCalledOnce();
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/harness/hosted-bootstrap/project/initialize',
      expect.objectContaining({ method: 'POST' })
    );
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({ projectRoot: '/project' });
    expect(bridge.grantProviderNetworkConsent).toHaveBeenCalledWith('/project');
    expect(bridge.startLogin).toHaveBeenCalledWith('/project');
    expect(bridge.cancelLogin).toHaveBeenCalledWith('/project');
    expect(bridge.signOut).toHaveBeenCalledWith('/project');
  });

  it('settles cancellation locally without forwarding an AbortSignal through IPC', async () => {
    const pending = new Promise<never>(() => undefined);
    const bridge = installDesktopAccountBridge({ signOut: vi.fn(() => pending) });
    const controller = new AbortController();
    const operation = signOutHostedBootstrapProject('/project', controller.signal);
    controller.abort(new DOMException('cancelled', 'AbortError'));
    await expect(operation).rejects.toMatchObject({ name: 'AbortError' });
    expect(bridge.signOut).toHaveBeenCalledWith('/project');
  });
});
