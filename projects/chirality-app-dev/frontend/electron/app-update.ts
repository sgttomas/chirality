/**
 * App-update checking: a pure feed checker plus the main-process state owner
 * the IPC handlers and the application menu drive.
 *
 * Scope is deliberately narrow. A check reads one JSON feed, compares its
 * version with the running one, and reports; opening the download hands an
 * https URL to the system browser. Nothing downloads, installs or restarts.
 *
 * Fail-closed by construction (CONTRACT.md K-NET-1): with no configured
 * source the check reports `no-release-source` without touching the network;
 * with a source whose host is not allowlisted it reports `policy`, again
 * without a request. Only a configured and allowlisted https source is ever
 * fetched, and today none exists (`app-update-source.ts`).
 *
 * Kept free of `electron` imports so it can be unit-tested under plain Node,
 * mirroring `runtime-connectivity.ts`.
 */

import {
  APP_UPDATE_ALLOWED_FEED_HOSTS,
  describeAppUpdateSource,
  isAllowlistedFeedHost,
  type AppUpdateSource
} from './app-update-source';
import type {
  AppUpdateAvailable,
  AppUpdateFailure,
  AppUpdateOpenDownloadResult,
  AppUpdateState
} from './app-update-ipc-contract';

/** Minimal fetch-like response the checker needs. `Response` satisfies it. */
export type AppUpdateFetchResponse = {
  ok: boolean;
  status: number;
  text: () => Promise<string>;
};

export type AppUpdateFetch = (url: string) => Promise<AppUpdateFetchResponse>;

/** Published feed shape. Only `version` and an https `downloadUrl` are required. */
export type AppUpdateFeed = {
  version: string;
  downloadUrl: string;
  releaseNotesUrl?: string;
  publishedAt?: string;
};

export type AppUpdateCheckResult =
  | { status: 'up-to-date'; checkedAt: string }
  | { status: 'update-available'; checkedAt: string; available: AppUpdateAvailable }
  | { status: 'failed'; checkedAt: string; failure: AppUpdateFailure };

export type AppUpdateCheckOptions = {
  source: AppUpdateSource | null;
  currentVersion: string;
  fetchImpl: AppUpdateFetch;
  allowedHosts?: readonly string[];
  now?: () => Date;
};

// ---------------------------------------------------------------------------
// Semantic versions (semver 2.0.0 precedence, build metadata ignored)
// ---------------------------------------------------------------------------

export type ParsedSemver = {
  major: number;
  minor: number;
  patch: number;
  prerelease: Array<string | number>;
};

const SEMVER_PATTERN =
  /^v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/u;

export function parseSemver(value: string): ParsedSemver | null {
  const match = SEMVER_PATTERN.exec(value.trim());
  if (!match) return null;
  const prerelease = (match[4] ?? '')
    .split('.')
    .filter((part) => part.length > 0)
    .map((part) => (/^(0|[1-9]\d*)$/u.test(part) ? Number(part) : part));
  return {
    major: Number(match[1]),
    minor: Number(match[2]),
    patch: Number(match[3]),
    prerelease
  };
}

function comparePrereleaseIdentifier(a: string | number, b: string | number): number {
  if (typeof a === 'number' && typeof b === 'number') return a === b ? 0 : a < b ? -1 : 1;
  // Numeric identifiers always have lower precedence than alphanumeric ones.
  if (typeof a === 'number') return -1;
  if (typeof b === 'number') return 1;
  return a === b ? 0 : a < b ? -1 : 1;
}

/** Negative when `a` precedes `b`, positive when it follows, zero when equal. */
export function compareSemver(a: ParsedSemver, b: ParsedSemver): number {
  if (a.major !== b.major) return a.major < b.major ? -1 : 1;
  if (a.minor !== b.minor) return a.minor < b.minor ? -1 : 1;
  if (a.patch !== b.patch) return a.patch < b.patch ? -1 : 1;
  // A version without a prerelease has higher precedence than one with.
  if (a.prerelease.length === 0 && b.prerelease.length === 0) return 0;
  if (a.prerelease.length === 0) return 1;
  if (b.prerelease.length === 0) return -1;
  const length = Math.min(a.prerelease.length, b.prerelease.length);
  for (let index = 0; index < length; index += 1) {
    const order = comparePrereleaseIdentifier(a.prerelease[index], b.prerelease[index]);
    if (order !== 0) return order;
  }
  // A larger set of prerelease fields has higher precedence when the prefix matches.
  return a.prerelease.length === b.prerelease.length
    ? 0
    : a.prerelease.length < b.prerelease.length
      ? -1
      : 1;
}

// ---------------------------------------------------------------------------
// Feed validation
// ---------------------------------------------------------------------------

function isHttpsUrl(value: unknown): value is string {
  if (typeof value !== 'string' || value.trim().length === 0) return false;
  try {
    return new URL(value).protocol === 'https:';
  } catch {
    return false;
  }
}

/** Parse the feed body. Returns the reason when the shape is not the published one. */
export function parseAppUpdateFeed(
  body: string
): { ok: true; feed: AppUpdateFeed } | { ok: false; reason: string } {
  let parsed: unknown;
  try {
    parsed = JSON.parse(body);
  } catch {
    return { ok: false, reason: 'The release feed is not valid JSON.' };
  }
  if (typeof parsed !== 'object' || parsed === null || Array.isArray(parsed)) {
    return { ok: false, reason: 'The release feed is not a JSON object.' };
  }
  const candidate = parsed as Record<string, unknown>;
  if (typeof candidate.version !== 'string' || parseSemver(candidate.version) === null) {
    return { ok: false, reason: 'The release feed has no valid semantic version.' };
  }
  if (!isHttpsUrl(candidate.downloadUrl)) {
    return { ok: false, reason: 'The release feed download URL is missing or is not https.' };
  }
  if (candidate.releaseNotesUrl !== undefined && !isHttpsUrl(candidate.releaseNotesUrl)) {
    return { ok: false, reason: 'The release feed notes URL is not https.' };
  }
  if (candidate.publishedAt !== undefined && typeof candidate.publishedAt !== 'string') {
    return { ok: false, reason: 'The release feed publication date is not a string.' };
  }
  const feed: AppUpdateFeed = {
    version: candidate.version,
    downloadUrl: candidate.downloadUrl
  };
  if (candidate.releaseNotesUrl !== undefined) feed.releaseNotesUrl = candidate.releaseNotesUrl;
  if (candidate.publishedAt !== undefined) feed.publishedAt = candidate.publishedAt;
  return { ok: true, feed };
}

// ---------------------------------------------------------------------------
// Policy gate on the feed source
// ---------------------------------------------------------------------------

/**
 * The single decision point for whether a source may be contacted: configured,
 * https, and its host on the allowlist. Shared by the checker and the
 * production fetch guard so the two cannot disagree.
 */
export function evaluateAppUpdateSourcePolicy(
  source: AppUpdateSource | null,
  allowedHosts: readonly string[] = APP_UPDATE_ALLOWED_FEED_HOSTS
): { allowed: true; feedUrl: string; hostname: string } | { allowed: false; failure: AppUpdateFailure } {
  if (!source) {
    return {
      allowed: false,
      failure: {
        code: 'no-release-source',
        message: 'No release source is configured for this build.'
      }
    };
  }
  let parsed: URL;
  try {
    parsed = new URL(source.feedUrl);
  } catch {
    return {
      allowed: false,
      failure: { code: 'policy', message: 'The configured release feed URL is not valid.' }
    };
  }
  if (parsed.protocol !== 'https:') {
    return {
      allowed: false,
      failure: { code: 'policy', message: 'The configured release feed is not an https URL.' }
    };
  }
  if (!isAllowlistedFeedHost(parsed.hostname, allowedHosts)) {
    return {
      allowed: false,
      failure: {
        code: 'policy',
        message: `The release feed host "${parsed.hostname}" is not allowlisted for outbound network access.`
      }
    };
  }
  return { allowed: true, feedUrl: parsed.toString(), hostname: parsed.hostname };
}

/**
 * Production fetch for the controller: refuses (rejects, which the checker
 * reports as `network`) unless a source is configured and allowlisted, and
 * only then delegates to the real fetch. With `app-update-source.ts`
 * unconfigured this never issues a request. Redirects are refused so a feed
 * cannot bounce a check to a host outside the allowlist.
 */
export function createPolicyGuardedFetch(options: {
  source: AppUpdateSource | null;
  allowedHosts?: readonly string[];
  fetchImpl?: AppUpdateFetch;
}): AppUpdateFetch {
  const delegate: AppUpdateFetch =
    options.fetchImpl ??
    ((url) => globalThis.fetch(url, { redirect: 'error', cache: 'no-store' }));
  return async (url) => {
    const policy = evaluateAppUpdateSourcePolicy(options.source, options.allowedHosts);
    if (!policy.allowed) {
      throw new Error('Release feed fetch refused: no configured, allowlisted release source.');
    }
    if (url !== policy.feedUrl) {
      throw new Error('Release feed fetch refused: URL is not the configured feed.');
    }
    return delegate(url);
  };
}

// ---------------------------------------------------------------------------
// One check
// ---------------------------------------------------------------------------

export async function checkForAppUpdate(options: AppUpdateCheckOptions): Promise<AppUpdateCheckResult> {
  const now = options.now ?? (() => new Date());
  const finish = (): string => now().toISOString();
  const fail = (failure: AppUpdateFailure): AppUpdateCheckResult => ({
    status: 'failed',
    checkedAt: finish(),
    failure
  });

  const policy = evaluateAppUpdateSourcePolicy(options.source, options.allowedHosts);
  if (!policy.allowed) return fail(policy.failure);

  const current = parseSemver(options.currentVersion);
  if (!current) {
    return fail({
      code: 'invalid-feed',
      message: `The installed version "${options.currentVersion}" is not a valid semantic version, so the feed cannot be compared.`
    });
  }

  let body: string;
  try {
    const response = await options.fetchImpl(policy.feedUrl);
    if (!response.ok) {
      return fail({
        code: 'network',
        message: `The release feed request failed with HTTP ${response.status}.`
      });
    }
    body = await response.text();
  } catch (error) {
    return fail({
      code: 'network',
      message: describeError(error, 'The release feed could not be reached.')
    });
  }

  const feed = parseAppUpdateFeed(body);
  if (!feed.ok) return fail({ code: 'invalid-feed', message: feed.reason });

  const published = parseSemver(feed.feed.version);
  if (!published) return fail({ code: 'invalid-feed', message: 'The release feed has no valid semantic version.' });

  if (compareSemver(published, current) > 0) {
    return { status: 'update-available', checkedAt: finish(), available: { ...feed.feed } };
  }
  return { status: 'up-to-date', checkedAt: finish() };
}

// ---------------------------------------------------------------------------
// State owner
// ---------------------------------------------------------------------------

export type AppUpdateLogLevel = 'info' | 'warn' | 'error';

export type AppUpdateControllerOptions = {
  appVersion: string;
  source: AppUpdateSource | null;
  fetchImpl: AppUpdateFetch;
  openExternal: (url: string) => Promise<void>;
  allowedHosts?: readonly string[];
  now?: () => Date;
  log?: (level: AppUpdateLogLevel, event: string, detail?: unknown) => void;
};

export type AppUpdateController = {
  getState: () => AppUpdateState;
  /** Run a check, or join the one already in flight. Resolves with the settled state. */
  check: () => Promise<AppUpdateState>;
  /** Open the reported download in the system browser (https only). */
  openDownload: () => Promise<AppUpdateOpenDownloadResult>;
  /** Called on every state change. Returns the unsubscribe function. */
  subscribe: (listener: (state: AppUpdateState) => void) => () => void;
};

const CREDENTIALISH_PATTERN = /(?:Bearer|token|credential|api[_ -]?key)\s+\S+/giu;
const URL_PATTERN = /\bhttps?:\/\/\S+/giu;

/**
 * Error text for state and log: credential-shaped fragments and any URL are
 * removed, so a query string or a user-info segment never reaches a log line.
 */
function describeError(error: unknown, fallback: string): string {
  const message =
    error instanceof Error && error.message.trim() ? error.message.trim() : fallback;
  return message.replaceAll(CREDENTIALISH_PATTERN, '[redacted]').replaceAll(URL_PATTERN, '[url]');
}

export function createAppUpdateController(options: AppUpdateControllerOptions): AppUpdateController {
  const now = options.now ?? (() => new Date());
  const log = options.log ?? (() => undefined);
  const listeners = new Set<(state: AppUpdateState) => void>();
  const appVersion = options.appVersion;

  let state: AppUpdateState = {
    currentVersion: appVersion,
    status: 'idle',
    releaseSource: describeAppUpdateSource(options.source)
  };
  let inFlight: Promise<AppUpdateState> | undefined;

  const publish = (next: AppUpdateState): void => {
    state = next;
    for (const listener of listeners) {
      try {
        listener(state);
      } catch (error) {
        log('warn', 'app_update.listener_failed', { reason: describeError(error, 'listener threw') });
      }
    }
  };

  const runCheck = async (): Promise<AppUpdateState> => {
    // Checking clears the previous outcome: a stale "update available" must
    // not stay on screen while a fresh answer is in flight.
    publish({
      currentVersion: appVersion,
      status: 'checking',
      checkedAt: state.checkedAt,
      releaseSource: state.releaseSource
    });
    log('info', 'app_update.check.started', {
      currentVersion: appVersion,
      sourceConfigured: state.releaseSource.configured
    });
    const result = await checkForAppUpdate({
      source: options.source,
      currentVersion: appVersion,
      fetchImpl: options.fetchImpl,
      allowedHosts: options.allowedHosts,
      now
    });
    const next: AppUpdateState = {
      currentVersion: appVersion,
      status: result.status,
      checkedAt: result.checkedAt,
      releaseSource: state.releaseSource
    };
    if (result.status === 'failed') next.failure = result.failure;
    if (result.status === 'update-available') next.available = result.available;
    publish(next);
    log(result.status === 'failed' ? 'warn' : 'info', 'app_update.check.completed', {
      status: result.status,
      failureCode: result.status === 'failed' ? result.failure.code : null,
      availableVersion: result.status === 'update-available' ? result.available.version : null
    });
    return state;
  };

  return {
    getState: () => state,
    check(): Promise<AppUpdateState> {
      if (inFlight) return inFlight;
      inFlight = runCheck().finally(() => {
        inFlight = undefined;
      });
      return inFlight;
    },
    async openDownload(): Promise<AppUpdateOpenDownloadResult> {
      const available = state.available;
      if (!available) {
        return { ok: false, error: 'No update download is available to open.' };
      }
      if (!isHttpsUrl(available.downloadUrl)) {
        log('warn', 'app_update.open_download.refused', { reason: 'not-https' });
        return { ok: false, error: 'The update download URL is not https, so it was not opened.' };
      }
      try {
        await options.openExternal(available.downloadUrl);
        log('info', 'app_update.open_download.opened', { version: available.version });
        return { ok: true };
      } catch (error) {
        const reason = describeError(error, 'The system browser could not be opened.');
        log('warn', 'app_update.open_download.failed', { reason });
        return { ok: false, error: reason };
      }
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => {
        listeners.delete(listener);
      };
    }
  };
}
