'use client';

import React from 'react';

import { useEffect, useRef } from 'react';
import { AccountConsentSettingsView, type AccountConsentSettingsViewProps } from './account-consent-settings';
import { RuntimeSettingsView } from './runtime-settings';
import type { RuntimeSettingsViewProps } from './runtime-settings-controller';
import { ApiKeySettings } from './api-key-settings';
import { ThemeControl } from '../shell/theme-control';
import styles from './settings-view.module.css';
import type { HostedBootstrapController } from './hosted-bootstrap-controller';
import { HostedBootstrapView } from './hosted-bootstrap-view';

export function SettingsView({ account, runtime, folder, target, hosted }: {
  account: AccountConsentSettingsViewProps; runtime: RuntimeSettingsViewProps; folder: string | null;
  hosted?: HostedBootstrapController;
  target?: { group?: 'folder' | 'local-model'; sequence: number } | null;
}): JSX.Element {
  const root = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!target?.group) { root.current?.focus(); return; }
    const group = root.current?.querySelector<HTMLElement>(`[data-settings-group="${target.group}"]`);
    group?.scrollIntoView?.({ block: 'start' });
    group?.focus();
  }, [target]);
  return <div ref={root} tabIndex={-1} aria-label="Settings" className={styles.settings}>
    <section data-settings-group="account">{hosted ? <HostedBootstrapView controller={hosted} /> : <><AccountConsentSettingsView {...account} presentation="account" />{account.snapshot ? <p>Preview account · simulated state. Sign-in currently applies to the selected folder.</p> : null}</>}</section>
    {!hosted && folder ? <section tabIndex={-1} data-settings-group="folder"><h2 title={folder}>This folder · {folder.split('/').filter(Boolean).pop() || folder}</h2><AccountConsentSettingsView {...account} presentation="folder" /></section> : null}
    {hosted ? <section tabIndex={-1} data-settings-group="runtime"><RuntimeSettingsView {...runtime} showLocalModels={false} /></section> : null}
    {!hosted ? <section tabIndex={-1} data-settings-group="local-model"><h2>Local model</h2><p>oMLX server status unknown.</p><RuntimeSettingsView {...runtime} /></section> : null}
    <section data-settings-group="api-keys"><h2>API keys</h2><ApiKeySettings /></section>
    <section data-settings-group="appearance"><h2>Appearance</h2><ThemeControl /></section>
    <p className={styles.footer}>{hosted ? 'OpenAI sign-in and provider-network consent apply to the selected project.' : 'Opt-in Preview · account is presented once; consent and permissions are per folder.'}</p>
  </div>;
}
