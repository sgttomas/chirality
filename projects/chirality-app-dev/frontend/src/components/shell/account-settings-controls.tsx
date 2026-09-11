'use client';

import React from 'react';

import type { AccountConsentSettingsViewProps } from '../settings/account-consent-settings';
import { describeAccountIdentity } from '../../lib/consent/hosted-engine-consent-port';
import type { RuntimeSettingsViewProps } from '../settings/runtime-settings-controller';

export function accountTitle(account: AccountConsentSettingsViewProps): string {
  const snapshot = account.snapshot;
  if (!snapshot) return 'Account unavailable';
  return snapshot.account.status === 'loggedIn'
    ? `Account ${describeAccountIdentity(snapshot.account.identity)}` : 'Sign in';
}

/** Daemon and residency reports do not attest external oMLX server health. */
export function LocalModelStatus(): JSX.Element {
  return <span title="The existing runtime connection does not report oMLX server availability.">
    <span data-local-model-status="unknown" aria-hidden="true" />Local model · unknown
  </span>;
}

export function DaemonQuickControl({ runtime, onSetup, showLocalModelStatus = true }: {
  runtime: RuntimeSettingsViewProps; onSetup: () => void;
  showLocalModelStatus?: boolean;
}): JSX.Element {
  const status = runtime.daemonStatus;
  const available = runtime.bridgeAvailable && status !== null;
  return <>
    {showLocalModelStatus ? <p>oMLX server status unknown.</p> : null}
    {!available ? <p className="api-key-hint">{runtime.bridgeAvailable ? 'Runtime daemon status unavailable.' : 'Runtime controls are available only in Chirality Desktop.'}</p> :
      !status.launchAgent.installed ? <button type="button" onClick={onSetup}>Set up runtime…</button> :
        <button type="button" role="switch" aria-label="Chirality runtime daemon" aria-checked={status.launchAgent.loaded}
          disabled={runtime.busyAction !== null}
          onClick={() => runtime.onDaemonAction(status.launchAgent.loaded ? 'stop' : 'start')}>
          {status.launchAgent.loaded ? 'Stop runtime daemon' : 'Start runtime daemon'}
        </button>}
    {!available ? <button type="button" role="switch" aria-label="Chirality runtime daemon" aria-checked={false} disabled title="Runtime daemon controls unavailable">Runtime daemon unavailable</button> : null}
    {runtime.error ? <p role="alert">{runtime.error}</p> : null}
  </>;
}
