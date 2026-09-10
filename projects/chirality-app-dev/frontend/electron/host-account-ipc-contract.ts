import type {
  HostedBootstrapLoginStartResponse,
  HostedBootstrapStatus
} from '@chirality/runtime-contracts';

export const HOST_ACCOUNT_CHANNEL = 'chirality:host-account';

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
  | { ok: false; error: 'Hosted account service is unavailable.' };
