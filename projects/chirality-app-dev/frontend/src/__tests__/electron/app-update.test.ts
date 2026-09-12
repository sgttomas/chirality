import { describe, expect, it, vi } from 'vitest';
import {
  checkForAppUpdate,
  compareSemver,
  createAppUpdateController,
  createPolicyGuardedFetch,
  evaluateAppUpdateSourcePolicy,
  parseAppUpdateFeed,
  parseSemver,
  type AppUpdateFetch,
  type AppUpdateFetchResponse
} from '../../../electron/app-update';
import {
  APP_UPDATE_ALLOWED_FEED_HOSTS,
  describeAppUpdateSource,
  resolveAppUpdateSource,
  type AppUpdateSource
} from '../../../electron/app-update-source';
import {
  APP_ABOUT_SHOW_CHANNEL,
  APP_UPDATE_CHANGED_CHANNEL,
  APP_UPDATE_CHECK_CHANNEL,
  APP_UPDATE_GET_CHANNEL,
  APP_UPDATE_OPEN_DOWNLOAD_CHANNEL,
  type AppUpdateState
} from '../../../electron/app-update-ipc-contract';

/**
 * The checker is exercised with a fake `fetchImpl` only: no test here, and no
 * production path today, issues a network request. The configured-source cases
 * use a hypothetical allowlist passed explicitly, because the shipped allowlist
 * is empty and must stay that way until a K-NET-1 amendment names a host.
 */

const FEED_HOST = 'releases.example.test';
const FEED_URL = `https://${FEED_HOST}/chirality/feed.json`;
const CONFIGURED: AppUpdateSource = { feedUrl: FEED_URL, description: 'Example feed' };
const ALLOW = [FEED_HOST];
const CURRENT = '3.0.0-rc.1';
const CLOCK = () => new Date('2026-09-12T10:00:00.000Z');

function response(body: string, init: { ok?: boolean; status?: number } = {}): AppUpdateFetchResponse {
  return { ok: init.ok ?? true, status: init.status ?? 200, text: async () => body };
}

function feedWith(version: string, extra: Record<string, unknown> = {}): string {
  return JSON.stringify({ version, downloadUrl: 'https://releases.example.test/Chirality.dmg', ...extra });
}

const neverFetch: AppUpdateFetch = vi.fn(async () => {
  throw new Error('fetch must not be called');
});

describe('app-update contract', () => {
  it('pins the channel names the preload and renderer are coded against', () => {
    expect(APP_UPDATE_GET_CHANNEL).toBe('chirality:app-update-get');
    expect(APP_UPDATE_CHECK_CHANNEL).toBe('chirality:app-update-check');
    expect(APP_UPDATE_OPEN_DOWNLOAD_CHANNEL).toBe('chirality:app-update-open-download');
    expect(APP_UPDATE_CHANGED_CHANNEL).toBe('chirality:app-update-changed');
    expect(APP_ABOUT_SHOW_CHANNEL).toBe('chirality:app-about-show');
  });
});

describe('release source (shipped unconfigured)', () => {
  it('resolves no source and allowlists no host', () => {
    expect(resolveAppUpdateSource()).toBeNull();
    expect(APP_UPDATE_ALLOWED_FEED_HOSTS).toEqual([]);
    expect(describeAppUpdateSource(null)).toEqual({
      configured: false,
      description: 'No release source is configured for this build.'
    });
    expect(describeAppUpdateSource(CONFIGURED)).toEqual({ configured: true, description: 'Example feed' });
  });

  it('fails the policy gate for a missing, non-https, malformed or non-allowlisted source', () => {
    expect(evaluateAppUpdateSourcePolicy(null)).toMatchObject({ allowed: false, failure: { code: 'no-release-source' } });
    expect(evaluateAppUpdateSourcePolicy(CONFIGURED)).toMatchObject({ allowed: false, failure: { code: 'policy' } });
    expect(evaluateAppUpdateSourcePolicy({ ...CONFIGURED, feedUrl: `http://${FEED_HOST}/feed.json` }, ALLOW)).toMatchObject({
      allowed: false,
      failure: { code: 'policy' }
    });
    expect(evaluateAppUpdateSourcePolicy({ ...CONFIGURED, feedUrl: 'not a url' }, ALLOW)).toMatchObject({
      allowed: false,
      failure: { code: 'policy' }
    });
    expect(evaluateAppUpdateSourcePolicy(CONFIGURED, ALLOW)).toEqual({ allowed: true, feedUrl: FEED_URL, hostname: FEED_HOST });
    expect(evaluateAppUpdateSourcePolicy(CONFIGURED, ['RELEASES.EXAMPLE.TEST'])).toMatchObject({ allowed: true });
  });
});

describe('semver precedence', () => {
  const order = (a: string, b: string): number => compareSemver(parseSemver(a)!, parseSemver(b)!);

  it('parses release and prerelease identities and rejects malformed ones', () => {
    expect(parseSemver('3.0.0-rc.1')).toEqual({ major: 3, minor: 0, patch: 0, prerelease: ['rc', 1] });
    expect(parseSemver('v3.0.0+build.7')).toEqual({ major: 3, minor: 0, patch: 0, prerelease: [] });
    for (const bad of ['3.0', '03.0.0', '3.0.0-', 'latest', '', '3.0.0-rc..1']) {
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
  });
});

describe('feed parsing', () => {
  it('accepts the published shape and rejects every malformed variant', () => {
    expect(parseAppUpdateFeed(feedWith('3.0.0', { releaseNotesUrl: 'https://x.test/notes', publishedAt: '2026-09-12' }))).toEqual({
      ok: true,
      feed: { version: '3.0.0', downloadUrl: 'https://releases.example.test/Chirality.dmg', releaseNotesUrl: 'https://x.test/notes', publishedAt: '2026-09-12' }
    });
    expect(parseAppUpdateFeed('not json')).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed('[]')).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed('null')).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed(JSON.stringify({ downloadUrl: 'https://x.test/a' }))).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed(JSON.stringify({ version: 'latest', downloadUrl: 'https://x.test/a' }))).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed(JSON.stringify({ version: '3.0.0' }))).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed(JSON.stringify({ version: '3.0.0', downloadUrl: 'http://x.test/a' }))).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed(JSON.stringify({ version: '3.0.0', downloadUrl: 'https://x.test/a', releaseNotesUrl: 'ftp://x' }))).toMatchObject({ ok: false });
    expect(parseAppUpdateFeed(JSON.stringify({ version: '3.0.0', downloadUrl: 'https://x.test/a', publishedAt: 7 }))).toMatchObject({ ok: false });
  });
});

describe('checkForAppUpdate', () => {
  it('fails closed with no-release-source and never fetches when no source is configured', async () => {
    const result = await checkForAppUpdate({ source: null, currentVersion: CURRENT, fetchImpl: neverFetch, now: CLOCK });
    expect(result).toEqual({
      status: 'failed',
      checkedAt: '2026-09-12T10:00:00.000Z',
      failure: { code: 'no-release-source', message: 'No release source is configured for this build.' }
    });
    expect(neverFetch).not.toHaveBeenCalled();
  });

  it('fails closed with policy and never fetches when the source host is not allowlisted', async () => {
    const result = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl: neverFetch, now: CLOCK });
    expect(result).toMatchObject({ status: 'failed', failure: { code: 'policy' } });
    expect(neverFetch).not.toHaveBeenCalled();
    // The shipped allowlist is the default: passing nothing is the same as passing it.
    const shipped = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl: neverFetch, allowedHosts: APP_UPDATE_ALLOWED_FEED_HOSTS });
    expect(shipped).toMatchObject({ status: 'failed', failure: { code: 'policy' } });
  });

  it('reports network when the fetch rejects or answers non-2xx, with no URL in the message', async () => {
    const rejecting: AppUpdateFetch = async () => {
      throw new Error(`getaddrinfo ENOTFOUND ${FEED_HOST} while fetching ${FEED_URL}?token=abc`);
    };
    const rejected = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl: rejecting, allowedHosts: ALLOW });
    expect(rejected).toMatchObject({ status: 'failed', failure: { code: 'network' } });
    expect(rejected.status === 'failed' && rejected.failure.message).not.toContain('token=abc');
    expect(rejected.status === 'failed' && rejected.failure.message).not.toContain('https://');

    const notFound = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl: async () => response('', { ok: false, status: 404 }), allowedHosts: ALLOW });
    expect(notFound).toMatchObject({ status: 'failed', failure: { code: 'network', message: 'The release feed request failed with HTTP 404.' } });
  });

  it('reports invalid-feed for a malformed body', async () => {
    for (const body of ['<html>', '{}', feedWith('3.0.0').replace('https://', 'http://')]) {
      const result = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl: async () => response(body), allowedHosts: ALLOW });
      expect(result, body).toMatchObject({ status: 'failed', failure: { code: 'invalid-feed' } });
    }
  });

  it('reports invalid-feed when the installed version cannot be compared, without fetching', async () => {
    const result = await checkForAppUpdate({ source: CONFIGURED, currentVersion: 'dev', fetchImpl: neverFetch, allowedHosts: ALLOW });
    expect(result).toMatchObject({ status: 'failed', failure: { code: 'invalid-feed' } });
    expect(neverFetch).not.toHaveBeenCalled();
  });

  it('fetches exactly the configured feed URL and reports update-available with the feed details', async () => {
    const fetchImpl = vi.fn(async () => response(feedWith('3.0.0', { releaseNotesUrl: 'https://releases.example.test/notes', publishedAt: '2026-10-01T00:00:00.000Z' })));
    const result = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl, allowedHosts: ALLOW, now: CLOCK });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
    expect(fetchImpl).toHaveBeenCalledWith(FEED_URL);
    expect(result).toEqual({
      status: 'update-available',
      checkedAt: '2026-09-12T10:00:00.000Z',
      available: {
        version: '3.0.0',
        downloadUrl: 'https://releases.example.test/Chirality.dmg',
        releaseNotesUrl: 'https://releases.example.test/notes',
        publishedAt: '2026-10-01T00:00:00.000Z'
      }
    });
  });

  it('reports up-to-date for an equal or older feed version, including prerelease ordering', async () => {
    for (const version of ['3.0.0-rc.1', '3.0.0-rc.0', '3.0.0-beta.9', '2.9.9']) {
      const result = await checkForAppUpdate({ source: CONFIGURED, currentVersion: CURRENT, fetchImpl: async () => response(feedWith(version)), allowedHosts: ALLOW, now: CLOCK });
      expect(result, version).toEqual({ status: 'up-to-date', checkedAt: '2026-09-12T10:00:00.000Z' });
    }
    const release = await checkForAppUpdate({ source: CONFIGURED, currentVersion: '3.0.0', fetchImpl: async () => response(feedWith('3.0.0-rc.2')), allowedHosts: ALLOW });
    expect(release).toMatchObject({ status: 'up-to-date' });
  });
});

describe('createPolicyGuardedFetch (production wiring)', () => {
  it('rejects without delegating unless a source is configured and allowlisted', async () => {
    const delegate = vi.fn<AppUpdateFetch>(async () => response(feedWith('3.0.0')));
    await expect(createPolicyGuardedFetch({ source: null, fetchImpl: delegate })(FEED_URL)).rejects.toThrow(/refused/u);
    await expect(createPolicyGuardedFetch({ source: CONFIGURED, fetchImpl: delegate })(FEED_URL)).rejects.toThrow(/refused/u);
    await expect(createPolicyGuardedFetch({ source: CONFIGURED, allowedHosts: ALLOW, fetchImpl: delegate })('https://releases.example.test/other.json')).rejects.toThrow(/not the configured feed/u);
    expect(delegate).not.toHaveBeenCalled();
    await expect(createPolicyGuardedFetch({ source: CONFIGURED, allowedHosts: ALLOW, fetchImpl: delegate })(FEED_URL)).resolves.toMatchObject({ ok: true });
    expect(delegate).toHaveBeenCalledWith(FEED_URL);
  });

  it('surfaces through the checker as a network failure with the shipped (empty) source', async () => {
    const result = await checkForAppUpdate({
      source: CONFIGURED,
      currentVersion: CURRENT,
      allowedHosts: ALLOW,
      fetchImpl: createPolicyGuardedFetch({ source: resolveAppUpdateSource(), allowedHosts: APP_UPDATE_ALLOWED_FEED_HOSTS })
    });
    expect(result).toMatchObject({ status: 'failed', failure: { code: 'network' } });
  });
});

type ControllerHarness = {
  states: AppUpdateState[];
  logs: Array<{ level: string; event: string; detail?: unknown }>;
  openExternal: ReturnType<typeof vi.fn>;
  controller: ReturnType<typeof createAppUpdateController>;
};

function harness(options: { source?: AppUpdateSource | null; fetchImpl?: AppUpdateFetch; openExternal?: (url: string) => Promise<void> } = {}): ControllerHarness {
  const states: AppUpdateState[] = [];
  const logs: ControllerHarness['logs'] = [];
  const openExternal = vi.fn(options.openExternal ?? (async () => undefined));
  const controller = createAppUpdateController({
    appVersion: CURRENT,
    source: options.source ?? null,
    fetchImpl: options.fetchImpl ?? neverFetch,
    allowedHosts: ALLOW,
    openExternal,
    now: CLOCK,
    log: (level, event, detail) => logs.push({ level, event, detail })
  });
  controller.subscribe((state) => states.push(state));
  return { states, logs, openExternal, controller };
}

describe('createAppUpdateController', () => {
  it('starts idle with the current version and the unconfigured source description', () => {
    const { controller } = harness();
    expect(controller.getState()).toEqual({
      currentVersion: CURRENT,
      status: 'idle',
      releaseSource: { configured: false, description: 'No release source is configured for this build.' }
    });
  });

  it('publishes checking then failed/no-release-source for the shipped build, with a checkedAt', async () => {
    const { controller, states } = harness();
    const settled = await controller.check();
    expect(states.map((state) => state.status)).toEqual(['checking', 'failed']);
    expect(states[0]).toEqual({ currentVersion: CURRENT, status: 'checking', checkedAt: undefined, releaseSource: settled.releaseSource });
    expect(settled).toEqual({
      currentVersion: CURRENT,
      status: 'failed',
      checkedAt: '2026-09-12T10:00:00.000Z',
      failure: { code: 'no-release-source', message: 'No release source is configured for this build.' },
      releaseSource: { configured: false, description: 'No release source is configured for this build.' }
    });
    expect(controller.getState()).toBe(settled);
  });

  it('shares one in-flight check between concurrent callers and runs a fresh one afterwards', async () => {
    let release: (() => void) | undefined;
    const fetchImpl = vi.fn(async () => {
      await new Promise<void>((resolve) => { release = resolve; });
      return response(feedWith('3.0.0'));
    });
    const { controller, states } = harness({ source: CONFIGURED, fetchImpl });
    const first = controller.check();
    const second = controller.check();
    expect(second).toBe(first);
    expect(controller.getState().status).toBe('checking');
    release?.();
    const [a, b] = await Promise.all([first, second]);
    expect(a).toBe(b);
    expect(a).toMatchObject({ status: 'update-available', available: { version: '3.0.0' } });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
    expect(states.map((state) => state.status)).toEqual(['checking', 'update-available']);

    const third = controller.check();
    expect(third).not.toBe(first);
    release?.();
    await third;
    expect(fetchImpl).toHaveBeenCalledTimes(2);
  });

  it('clears a stale outcome while checking and keeps the last checkedAt', async () => {
    let body = feedWith('3.0.0');
    const { controller } = harness({ source: CONFIGURED, fetchImpl: async () => response(body) });
    await controller.check();
    expect(controller.getState().available).toBeDefined();
    body = '<html>';
    const pending = controller.check();
    expect(controller.getState()).toEqual({
      currentVersion: CURRENT,
      status: 'checking',
      checkedAt: '2026-09-12T10:00:00.000Z',
      releaseSource: { configured: true, description: 'Example feed' }
    });
    const settled = await pending;
    expect(settled.available).toBeUndefined();
    expect(settled).toMatchObject({ status: 'failed', failure: { code: 'invalid-feed' } });
  });

  it('opens only an https download, and reports why otherwise', async () => {
    const none = harness();
    await expect(none.controller.openDownload()).resolves.toEqual({ ok: false, error: 'No update download is available to open.' });
    expect(none.openExternal).not.toHaveBeenCalled();

    const some = harness({ source: CONFIGURED, fetchImpl: async () => response(feedWith('3.0.0')) });
    await some.controller.check();
    await expect(some.controller.openDownload()).resolves.toEqual({ ok: true });
    expect(some.openExternal).toHaveBeenCalledWith('https://releases.example.test/Chirality.dmg');

    const failing = harness({ source: CONFIGURED, fetchImpl: async () => response(feedWith('3.0.0')), openExternal: async () => { throw new Error('launch services refused https://releases.example.test/Chirality.dmg?sig=1'); } });
    await failing.controller.check();
    const refused = await failing.controller.openDownload();
    expect(refused.ok).toBe(false);
    expect(refused.error).not.toContain('sig=1');
  });

  it('never logs a URL or an @ and unsubscribes cleanly', async () => {
    const { controller, logs, states } = harness({
      source: CONFIGURED,
      fetchImpl: async () => { throw new Error(`refused for user@example.test at ${FEED_URL}?k=v`); }
    });
    const stop = controller.subscribe(() => undefined);
    stop();
    await controller.check();
    const serialized = JSON.stringify(logs);
    expect(serialized).not.toContain('http');
    expect(serialized).not.toContain('@');
    expect(logs.map((entry) => entry.event)).toEqual(['app_update.check.started', 'app_update.check.completed']);
    expect(logs[1]).toMatchObject({ level: 'warn', detail: { status: 'failed', failureCode: 'network' } });
    expect(states).toHaveLength(2);
  });
});
