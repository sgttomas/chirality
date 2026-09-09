'use client';

import React from 'react';

import type { AccountConsentSettingsViewProps } from '../settings/account-consent-settings';
import type { RuntimeSettingsViewProps } from '../settings/runtime-settings-controller';
import { accountTitle, DaemonQuickControl } from './account-settings-controls';
import { ThemeControl } from './theme-control';
import styles from './account-controls.module.css';
import { version } from '../../../package.json';

export type AccountPopoverProps = {
  account: AccountConsentSettingsViewProps;
  runtime: RuntimeSettingsViewProps;
  folder: string | null;
  legacyHref: string;
  onOpenSettings: (group?: 'folder' | 'local-model') => void;
};

export function AccountPopover({ account, runtime, folder, legacyHref, onOpenSettings }: AccountPopoverProps): JSX.Element {
  void legacyHref;
  return <>
    <section className={styles.group} aria-label="OpenAI account">
      <strong>{accountTitle(account)}</strong>
      <p>{account.snapshot ? 'Preview account · simulated state' : 'Account service unavailable in this build.'}</p>
      {account.snapshot ? <button type="button" disabled={account.busy} onClick={account.snapshot.account.status === 'loggedIn' ? account.onLogout : account.onLogin}>
        {account.snapshot.account.status === 'loggedIn' ? 'Sign out' : 'Sign in'}
      </button> : null}
      {folder ? <><p>Consent for {folder.split('/').filter(Boolean).pop() || folder}: {account.snapshot?.consent.status ?? 'unavailable'}</p><button type="button" onClick={() => onOpenSettings('folder')}>This folder…</button></> : null}
      {account.error ? <p role="alert">{account.error}</p> : null}
    </section>
    <section className={styles.group} aria-label="Local model"><strong>Local model</strong><DaemonQuickControl runtime={runtime} onSetup={() => onOpenSettings('local-model')} /></section>
    <section className={styles.group} aria-label="App controls">
      <button type="button" className={styles.menuAction} onClick={() => onOpenSettings()}>Settings…</button>
      <details><summary>Appearance</summary><ThemeControl /></details>
      <details><summary>About Chirality</summary><p>Chirality {version} · Opt-in Preview</p></details>
    </section>
  </>;
}
