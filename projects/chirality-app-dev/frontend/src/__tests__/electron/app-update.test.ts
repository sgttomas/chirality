import { describe, expect, it, vi } from 'vitest';
import { checkForAppUpdate, compareSemver, createAppUpdateController, createPolicyGuardedFetch,
  evaluateAppUpdateSourcePolicy, parseAppUpdateFeed, parseSemver, type AppUpdateFetchResponse } from '../../../electron/app-update';
import { APP_UPDATE_FEED_URL, APP_UPDATE_RELEASE_ROOT, resolveAppUpdateSource } from '../../../electron/app-update-source';

const source = resolveAppUpdateSource()!;
function release(version = '3.0.0', overrides: Record<string, unknown> = {}) {
  return { tag_name: `v${version}`, draft: false, prerelease: false,
    html_url: `${APP_UPDATE_RELEASE_ROOT}/tag/v${version}`, published_at: '2026-09-12T10:00:00Z',
    assets: [{ name: `Chirality-${version}-arm64.dmg`, state: 'uploaded',
      browser_download_url: `${APP_UPDATE_RELEASE_ROOT}/download/v${version}/Chirality-${version}-arm64.dmg` }], ...overrides };
}
const response = (body: unknown = release(), status = 200): AppUpdateFetchResponse => ({
  ok: status === 200, status, text: async () => JSON.stringify(body)
});
const check = (body: unknown = release(), currentVersion = '3.0.0-rc.1') => checkForAppUpdate({
  source, currentVersion, platform: 'darwin', arch: 'arm64', fetchImpl: async () => response(body)
});

describe('semver precedence', () => {
  const order = (a: string, b: string): number => compareSemver(parseSemver(a)!, parseSemver(b)!);

  it('parses release and prerelease identities and rejects malformed ones', () => {
    expect(parseSemver('3.0.0-rc.1')).toEqual({ major: 3, minor: 0, patch: 0, prerelease: ['rc', 1] });
    expect(parseSemver('v3.0.0+build.7')).toEqual({ major: 3, minor: 0, patch: 0, prerelease: [] });
    for (const bad of ['3.0', '03.0.0', '3.0.0-', 'latest', '', '3.0.0-rc..1', '3.0.0-01']) {
      expect(parseSemver(bad), bad).toBeNull();
    }
  });

  it('orders prereleases below the release and numerically within a prerelease', () => {
    expect(order('3.0.0-rc.1', '3.0.0')).toBeLessThan(0);
    expect(order('3.0.0', '3.0.0-rc.1')).toBeGreaterThan(0);
    expect(order('3.0.0-rc.1', '3.0.0-rc.2')).toBeLessThan(0);
    expect(order('3.0.0-rc.10', '3.0.0-rc.9')).toBeGreaterThan(0);
    expect(order('3.0.0-alpha', '3.0.0-alpha.1')).toBeLessThan(0);
    expect(order('3.0.0-alpha.1', '3.0.0-beta')).toBeLessThan(0);
    expect(order('3.0.0-1', '3.0.0-alpha')).toBeLessThan(0);
    expect(order('3.0.0-rc.1', '3.0.0-rc.1')).toBe(0);
    expect(order('3.0.0-rc.1+a', '3.0.0-rc.1+b')).toBe(0);
    expect(order('3.0.1-rc.1', '3.0.0')).toBeGreaterThan(0);
    expect(order('2.9.9', '3.0.0-rc.1')).toBeLessThan(0);
    expect(order('999999999999999999.0.0', '999999999999999998.0.0')).toBeGreaterThan(0);
    expect(order('3.0.0-999999999999999999', '3.0.0-999999999999999998')).toBeGreaterThan(0);
  });
});


describe('public release source and validation', () => {
  it('allows only the exact public latest endpoint, even with a broader host allowlist', () => {
    expect(evaluateAppUpdateSourcePolicy(source)).toMatchObject({ allowed: true, feedUrl: APP_UPDATE_FEED_URL });
    expect(evaluateAppUpdateSourcePolicy(null)).toMatchObject({ allowed: false });
    for (const feedUrl of [APP_UPDATE_FEED_URL + '?token=x', APP_UPDATE_FEED_URL + '#x',
      APP_UPDATE_FEED_URL.replace('https://', 'https://user:pass@'),
      APP_UPDATE_FEED_URL.replace('chirality-app', 'other'), APP_UPDATE_FEED_URL.replace('https:', 'http:'),
      APP_UPDATE_FEED_URL.replace('api.github.com', 'foreign.test')]) {
      expect(evaluateAppUpdateSourcePolicy({ ...source, feedUrl }, ['api.github.com', 'foreign.test'])).toMatchObject({ allowed: false });
    }
  });
  it('accepts published stable releases and chooses only matching architecture assets', () => {
    const body = JSON.stringify(release());
    expect(parseAppUpdateFeed(body, 'darwin', 'arm64')).toMatchObject({ ok: true, feed: { downloadUrl: release().assets[0].browser_download_url } });
    for (const [platform, arch] of [['darwin', 'x64'], ['linux', 'arm64'], ['win32', 'x64']]) {
      expect(parseAppUpdateFeed(body, platform, arch)).toMatchObject({ ok: true, feed: { downloadUrl: release().html_url } });
    }
    expect(parseAppUpdateFeed(JSON.stringify(release('3.0.0', { assets: [] })))).toMatchObject({ ok: true, feed: { downloadUrl: release().html_url } });
  });
  it('rejects drafts, prereleases, malformed bodies and foreign/credentialed/redirect-shaped URLs', () => {
    for (const overrides of [{ draft: true }, { prerelease: true }, { tag_name: '3.0.0-rc.2' },
      { published_at: null }, { assets: null }, { html_url: 'https://github.com/foreign/repo/releases/tag/v3.0.0' },
      { html_url: release().html_url + '?redirect=bad' },
      { html_url: release().html_url.replace('https://', 'https://u:p@') },
      { assets: [{ ...release().assets[0], browser_download_url: 'https://foreign.test/a.dmg' }] }]) {
      expect(parseAppUpdateFeed(JSON.stringify(release('3.0.0', overrides)))).toMatchObject({ ok: false });
    }
    for (const body of ['not json', 'null', '[]', '{}']) expect(parseAppUpdateFeed(body)).toMatchObject({ ok: false });
  });
});

describe('manual release checks', () => {
  it('offers newer stable versions and never downgrades the 3.0.0 candidate to public 2.0.0', async () => {
    expect(await check()).toMatchObject({ status: 'update-available', available: { version: '3.0.0' } });
    expect(await check(release('2.0.0'))).toMatchObject({ status: 'up-to-date' });
    expect(await check(release(), '3.0.0+build.9')).toMatchObject({ status: 'up-to-date' });
    expect(await check(release(), '4.0.0')).toMatchObject({ status: 'up-to-date' });
    expect(await check({}, 'dev')).toMatchObject({ status: 'failed', failure: { code: 'invalid-feed' } });
    expect(await check({})).toMatchObject({ status: 'failed', failure: { code: 'invalid-feed' } });
  });
  it('truthfully reports no release, rate limits, network and redirects', async () => {
    for (const [status, message] of [[404, /No published stable release/], [403, /rate-limited/], [429, /rate-limited/], [500, /HTTP 500/]] as const) {
      expect(await checkForAppUpdate({ source, currentVersion: '3.0.0', fetchImpl: async () => response({}, status) })).toMatchObject({ status: 'failed', failure: { message } });
    }
    for (const extra of [{ redirected: true }, { url: 'https://foreign.test/feed' }]) {
      expect(await checkForAppUpdate({ source, currentVersion: '3.0.0', fetchImpl: async () => ({ ...response(), ...extra }) })).toMatchObject({ status: 'failed', failure: { message: /redirected/ } });
    }
  });
  it('bounds stalled headers and body and aborts the request', async () => {
    for (const bodyStalls of [false, true]) {
      let signal: AbortSignal | null | undefined;
      const result = await checkForAppUpdate({ source, currentVersion: '3.0.0', timeoutMs: 5,
        fetchImpl: async (_, init) => { signal = init?.signal; return bodyStalls
          ? { ...response(), text: () => new Promise(() => undefined) } : new Promise(() => undefined); } });
      expect(result).toMatchObject({ status: 'failed', failure: { message: /timed out/ } });
      expect(signal?.aborted).toBe(true);
    }
  });
  it('production fetch omits credentials, refuses redirects and cannot be retargeted', async () => {
    const fetchImpl = vi.fn(async () => response());
    const guarded = createPolicyGuardedFetch({ source, fetchImpl });
    await expect(guarded('https://foreign.test')).rejects.toThrow(/not the configured/);
    expect(fetchImpl).not.toHaveBeenCalled();
    await guarded(APP_UPDATE_FEED_URL, { headers: { Authorization: 'secret' }, credentials: 'include', redirect: 'follow' });
    expect(fetchImpl).toHaveBeenCalledWith(APP_UPDATE_FEED_URL, expect.objectContaining({ credentials: 'omit', redirect: 'error',
      headers: { Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' } }));
  });
});

describe('controller browser-mediated UX', () => {
  it('deduplicates checks, clears stale updates, and opens only the validated release URL', async () => {
    let body: unknown = release();
    let finish!: () => void;
    const fetchImpl = vi.fn(async () => { await new Promise<void>(resolve => { finish = resolve; }); return response(body); });
    const openExternal = vi.fn(async () => undefined);
    const controller = createAppUpdateController({ source, appVersion: '3.0.0-rc.1', platform: 'darwin', arch: 'arm64', fetchImpl, openExternal });
    expect(await controller.openDownload()).toMatchObject({ ok: false });
    const first = controller.check();
    expect(controller.check()).toBe(first);
    expect(controller.getState().status).toBe('checking');
    finish(); await first;
    expect(openExternal).not.toHaveBeenCalled();
    expect(await controller.openDownload()).toEqual({ ok: true });
    expect(openExternal).toHaveBeenCalledWith(release().assets[0].browser_download_url);
    controller.getState().available!.downloadUrl = 'https://foreign.test/file';
    expect(await controller.openDownload()).toMatchObject({ ok: false });
    body = {};
    const next = controller.check();
    expect(controller.getState().available).toBeUndefined();
    finish(); await next;
    expect(controller.getState()).toMatchObject({ status: 'failed' });
    expect(fetchImpl).toHaveBeenCalledTimes(2);
  });
});
