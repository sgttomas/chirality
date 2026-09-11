import { afterEach, describe, expect, it, vi } from 'vitest';

import {
  bindHostedBootstrapProject,
  cancelHostedBootstrapLogin,
  getHostedBootstrapStatus,
  grantHostedProviderNetworkConsent,
  hydrateHostedBootstrapProject,
  initializeHostedBootstrapProject,
  signOutHostedBootstrapProject,
  startHostedBootstrapLogin
} from '../../lib/harness/hosted-bootstrap-client';

afterEach(() => {
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

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
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(new Response(JSON.stringify({
        registration: 'registered', projectId: 'project-one'
      }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({
        registration: 'registered', projectId: 'project-one', status
      }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const bridge = installDesktopAccountBridge();
    bridge.grantProviderNetworkConsent.mockResolvedValue({ registration: 'registered', projectId: 'project-one', status });
    bridge.startLogin.mockResolvedValue({ loginId: 'login-1', authUrl: 'https://example.test/login' });
    bridge.cancelLogin.mockResolvedValue({ registration: 'registered', projectId: 'project-one', status: { ...status, ceremony: 'cancelled' } });
    bridge.signOut.mockResolvedValue({ registration: 'registered', projectId: 'project-one', status: { ...status, ceremony: 'consent-required', canStartLogin: false } });

    await bindHostedBootstrapProject('/project');
    await initializeHostedBootstrapProject('/project');
    await grantHostedProviderNetworkConsent('/project');
    await startHostedBootstrapLogin('/project');
    await cancelHostedBootstrapLogin('/project');
    await signOutHostedBootstrapProject('/project');

    expect(fetchMock).toHaveBeenCalledTimes(2);
    expect(fetchMock).toHaveBeenNthCalledWith(
      1,
      '/api/harness/hosted-bootstrap/project/bind',
      expect.objectContaining({ method: 'POST' })
    );
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      '/api/harness/hosted-bootstrap/project/initialize',
      expect.objectContaining({ method: 'POST' })
    );
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({ projectRoot: '/project' });
    expect(JSON.parse(fetchMock.mock.calls[1][1].body)).toEqual({ projectRoot: '/project' });
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

  it('publishes a recovered binding before an independent account-status failure', async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({
      registration: 'registered', projectId: 'restart-project'
    }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const bridge = installDesktopAccountBridge({
      status: vi.fn().mockRejectedValue(new Error('account unavailable'))
    });
    const onBound = vi.fn();

    await expect(hydrateHostedBootstrapProject('/project', onBound))
      .rejects.toThrow('account unavailable');
    expect(onBound).toHaveBeenCalledWith({
      registration: 'registered',
      projectId: 'restart-project'
    });
    expect(bridge.status).toHaveBeenCalledWith('/project');
  });

  it('retries transient account startup failures without repeating the project bind', async () => {
    vi.useFakeTimers();
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({
      registration: 'registered', projectId: 'restart-project'
    }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const recovered = {
      registration: 'registered' as const,
      projectId: 'restart-project',
      status: {
        schema: 'chirality-hosted-bootstrap-status/v1' as const,
        projectId: 'restart-project',
        ceremony: 'consent-required' as const,
        admission: 'unavailable' as const,
        canStartLogin: false
      }
    };
    const unavailable = new Error('Hosted account service is unavailable.');
    const bridge = installDesktopAccountBridge({
      status: vi.fn()
        .mockRejectedValueOnce(unavailable)
        .mockRejectedValueOnce(unavailable)
        .mockRejectedValueOnce(unavailable)
        .mockResolvedValueOnce(recovered)
    });

    const operation = hydrateHostedBootstrapProject('/project', vi.fn());
    await vi.advanceTimersByTimeAsync(250);
    await vi.advanceTimersByTimeAsync(1_000);
    await vi.advanceTimersByTimeAsync(5_000);

    await expect(operation).resolves.toEqual(recovered);
    expect(fetchMock).toHaveBeenCalledOnce();
    expect(bridge.status).toHaveBeenCalledTimes(4);
  });

  it('aborts a pending account startup retry and clears its timer', async () => {
    vi.useFakeTimers();
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify({
      registration: 'registered', projectId: 'restart-project'
    }), { status: 200 })));
    const bridge = installDesktopAccountBridge({
      status: vi.fn().mockRejectedValue(new Error('Hosted account service is unavailable.'))
    });
    const controller = new AbortController();
    const operation = hydrateHostedBootstrapProject('/project', vi.fn(), controller.signal);
    await vi.advanceTimersByTimeAsync(0);

    controller.abort(new DOMException('cancelled', 'AbortError'));

    await expect(operation).rejects.toMatchObject({ name: 'AbortError' });
    expect(bridge.status).toHaveBeenCalledOnce();
    expect(vi.getTimerCount()).toBe(0);
  });
});
