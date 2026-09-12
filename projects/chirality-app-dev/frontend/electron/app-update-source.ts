/**
 * Where a release feed would come from, if this build had one.
 *
 * It does not. `sgttomas/chirality` publishes no releases, `pack-electron.mjs`
 * passes `--publish never`, and BUILD_AND_RELEASE.md leaves publication as an
 * open owner decision. Under CONTRACT.md K-NET-1 outbound network is
 * deny-by-default, so this module ships unconfigured and the checker fails
 * closed with `no-release-source`.
 *
 * Configuring a source later is a governed act, not a code edit here alone:
 * the feed host must be named in a K-NET-1 amendment and added to
 * `APP_UPDATE_ALLOWED_FEED_HOSTS`, and the contract pins on `electron/main.ts`
 * revisited. A source whose host is not allowlisted still fails closed with
 * `policy`; the allowlist is the enforcement point, this resolver only names
 * the candidate.
 */

export type AppUpdateSource = {
  /** Absolute https URL of a JSON feed with the `AppUpdateFeed` shape. */
  feedUrl: string;
  /** User-facing description of where checks go. */
  description: string;
};

/** Feed hosts a check may contact. Empty: no host is authorized today. */
export const APP_UPDATE_ALLOWED_FEED_HOSTS: readonly string[] = [];

export const UNCONFIGURED_RELEASE_SOURCE_DESCRIPTION =
  'No release source is configured for this build.';

/** The release source for this build, or `null` when none is configured. */
export function resolveAppUpdateSource(): AppUpdateSource | null {
  return null;
}

/** User-facing summary of the source for the renderer state object. */
export function describeAppUpdateSource(
  source: AppUpdateSource | null
): { configured: boolean; description: string } {
  return source
    ? { configured: true, description: source.description }
    : { configured: false, description: UNCONFIGURED_RELEASE_SOURCE_DESCRIPTION };
}

export function isAllowlistedFeedHost(
  hostname: string,
  allowedHosts: readonly string[] = APP_UPDATE_ALLOWED_FEED_HOSTS
): boolean {
  const normalized = hostname.trim().toLowerCase();
  return normalized.length > 0 && allowedHosts.some((host) => host.toLowerCase() === normalized);
}
