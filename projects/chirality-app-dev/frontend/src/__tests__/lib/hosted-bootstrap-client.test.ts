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

describe('hosted bootstrap renderer client', () => {
  it('keeps status read-only and encodes the selected project root', async () => {
    const result = { registration: 'required' };
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(JSON.stringify(result), { status: 200 })
    );
    vi.stubGlobal('fetch', fetchMock);

    await expect(getHostedBootstrapStatus('/project one')).resolves.toEqual(result);
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/harness/hosted-bootstrap/status?projectRoot=%2Fproject+one',
      { signal: undefined }
    );
  });

  it('sends initialization, consent, start, cancel, and project sign-out as explicit POST actions', async () => {
    const status = {
      schema: 'chirality-hosted-bootstrap-status/v1',
      projectId: 'project-one',
      ceremony: 'ready-to-start',
      admission: 'unavailable',
      canStartLogin: true
    };
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(new Response(JSON.stringify({
        registration: 'registered', projectId: 'project-one', status
      }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify(status), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({
        loginId: 'login-1', authUrl: 'https://example.test/login'
      }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({
        ...status, ceremony: 'cancelled'
      }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({
        ...status, ceremony: 'consent-required', canStartLogin: false
      }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);

    await initializeHostedBootstrapProject('/project');
    await grantHostedProviderNetworkConsent('/project');
    await startHostedBootstrapLogin('/project');
    await cancelHostedBootstrapLogin('/project');
    const controller = new AbortController();
    await signOutHostedBootstrapProject('/project', controller.signal);

    expect(fetchMock.mock.calls.map(([url]) => url)).toEqual([
      '/api/harness/hosted-bootstrap/project/initialize',
      '/api/harness/hosted-bootstrap/provider-network-consent',
      '/api/harness/hosted-bootstrap/login/start',
      '/api/harness/hosted-bootstrap/login/cancel',
      '/api/harness/hosted-bootstrap/logout'
    ]);
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({
      projectRoot: '/project'
    });
    expect(JSON.parse(fetchMock.mock.calls[1][1].body)).toEqual({
      projectRoot: '/project', consent: true
    });
    expect(JSON.parse(fetchMock.mock.calls[2][1].body)).toEqual({
      projectRoot: '/project'
    });
    expect(JSON.parse(fetchMock.mock.calls[3][1].body)).toEqual({
      projectRoot: '/project'
    });
    expect(JSON.parse(fetchMock.mock.calls[4][1].body)).toEqual({
      projectRoot: '/project'
    });
    expect(fetchMock.mock.calls[4][1].signal).toBe(controller.signal);
  });
});
