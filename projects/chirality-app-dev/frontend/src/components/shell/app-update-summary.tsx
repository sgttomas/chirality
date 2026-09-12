'use client';

import React from 'react';
import { useAppUpdate } from './app-update-provider';

/** Human wording for each update state. Never claims availability that was not checked. */
export function appUpdateStatusText(state: { status: string; available?: { version: string }; failure?: { message: string }; releaseSource: { configured: boolean; description: string } } | null, bridgeAvailable: boolean): string {
  if (!bridgeAvailable || !state) return 'Update checks are available in Chirality Desktop.';
  switch (state.status) {
    case 'checking': return 'Checking for updates…';
    case 'up-to-date': return 'Chirality is up to date.';
    case 'update-available': return `Version ${state.available?.version ?? ''} is available.`.replace('  ', ' ');
    case 'failed': return state.failure?.message ?? 'The update check did not complete.';
    default: return state.releaseSource.configured ? 'Not checked yet.' : state.releaseSource.description;
  }
}

/**
 * Check for Updates… plus the resulting state, shared by the account menu and
 * the About panel. Checking and download access only: no automatic install.
 */
export function AppUpdateControls({ compact = false }: { compact?: boolean }): JSX.Element {
  const { state, bridgeAvailable, check, openDownload } = useAppUpdate();
  const checking = state?.status === 'checking';
  return <div className="app-update-controls" data-update-status={state?.status ?? 'unavailable'}>
    <button type="button" disabled={!bridgeAvailable || checking} onClick={() => { void check(); }} title={bridgeAvailable ? 'Ask the release source whether a newer Chirality is available.' : 'Update checks run only in Chirality Desktop.'}>{checking ? 'Checking…' : 'Check for Updates…'}</button>
    <p role="status" className={compact ? 'app-update-status app-update-status--compact' : 'app-update-status'}>{appUpdateStatusText(state, bridgeAvailable)}</p>
    {state?.status === 'update-available' && state.available ? <button type="button" onClick={() => { void openDownload(); }} title={`Open the download for Chirality ${state.available.version} in your browser.`}>Download {state.available.version}</button> : null}
  </div>;
}
