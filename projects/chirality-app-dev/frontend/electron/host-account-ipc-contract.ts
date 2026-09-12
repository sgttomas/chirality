import type {
  HostedBootstrapLoginStartResponse,
  HostedBootstrapStatus
} from '@chirality/runtime-contracts';

export const HOST_ACCOUNT_CHANNEL = 'chirality:host-account';

/**
 * The one coarse transport/authority failure string. The renderer's retry
 * ladder treats exactly this message as transient; every other `error` is a
 * final answer from the daemon and is never retried.
 */
export const HOST_ACCOUNT_UNAVAILABLE = 'Hosted account service is unavailable.';

export type HostAccountDesktopOperation =
  | 'status'
  | 'grant-provider-network-consent'
  | 'start-login'
  | 'cancel-login'
  | 'sign-out';

export type HostAccountDesktopValue =
  | { registration: 'required' }
  | { registration: 'registered'; projectId: string; status: HostedBootstrapStatus }
  | HostedBootstrapLoginStartResponse;

export type HostAccountDesktopResult =
  | { ok: true; value: HostAccountDesktopValue }
  | { ok: false; error: typeof HOST_ACCOUNT_UNAVAILABLE }
  /**
   * The daemon answered and rejected the operation. `error` is a short operator
   * string that already carries the reason code in parentheses; `reason` is that
   * same code (`details.reason`, else `details.daemonCode`) for callers that
   * want it structurally.
   */
  | { ok: false; error: string; reason?: string };
