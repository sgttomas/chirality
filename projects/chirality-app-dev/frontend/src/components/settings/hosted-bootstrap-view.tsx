'use client';

import React from 'react';
import type { HostedBootstrapController } from './hosted-bootstrap-controller';

export function hostedBootstrapTitle(controller: HostedBootstrapController): string {
  const status = controller.snapshot?.registration === 'registered' ? controller.snapshot.status : null;
  return status?.ceremony === 'signed-in' ? 'OpenAI signed in' : 'OpenAI';
}

export function hostedBootstrapSummary(controller: HostedBootstrapController): string {
  if (!controller.projectRoot) return 'Choose a folder to get started';
  if (controller.loading) return 'Checking this project…';
  if (controller.snapshot?.registration !== 'registered') return 'Project setup required';
  const { ceremony, admission } = controller.snapshot.status;
  if (ceremony === 'signed-in' && admission === 'ready') return 'Signed in · Ready to work';
  if (ceremony === 'signed-in') return admission === 'establishing' ? 'Signed in · Preparing engine' : 'Signed in · Engine unavailable';
  if (ceremony === 'pending') return 'Sign-in pending';
  if (ceremony === 'consent-required') return 'Provider network consent required';
  return 'Sign in required';
}

export function HostedBootstrapView({ controller, compact = false }: { controller: HostedBootstrapController; compact?: boolean }): JSX.Element {
  const { projectRoot, snapshot, loading, busyAction, error, authUrl, signOutUncertain } = controller;
  const status = snapshot?.registration === 'registered' ? snapshot.status : null;
  const folderName = projectRoot?.split('/').filter(Boolean).pop() || projectRoot;
  return <section className="hosted-bootstrap" aria-label="OpenAI account" data-bootstrap-registration={snapshot?.registration ?? 'unknown'} data-bootstrap-ceremony={status?.ceremony ?? 'unknown'} data-bootstrap-admission={status?.admission ?? 'unavailable'}>
    {!compact ? <><h3>OpenAI account</h3><p className="api-key-hint">Connect this project to Codex with explicit provider-network consent.</p></> : null}
    <p className="api-key-status"><strong>{hostedBootstrapSummary(controller)}</strong></p>
    {!projectRoot ? <p>Choose a folder before setting up the project.</p> : loading ? null : snapshot?.registration !== 'registered' ? <>
      <p>Use {folderName} as the Chirality project. This writes one minimal <code>chirality.project.json</code> configuration if it is missing. Existing malformed or conflicting configuration is never replaced.</p>
      <button type="button" disabled={busyAction !== null} onClick={controller.onSetup}>{busyAction === 'setup' ? 'Setting up…' : 'Use this folder'}</button>
    </> : status?.ceremony === 'consent-required' ? <>
      <p>Allow this project to contact the OpenAI provider over HTTPS for sign-in and Codex work.</p>
      <button type="button" disabled={busyAction !== null} onClick={controller.onGrantConsent}>{busyAction === 'consent' ? 'Allowing…' : 'Allow provider network'}</button>
    </> : status?.ceremony === 'pending' ? <>
      <p>Complete sign-in with OpenAI. Chirality is waiting for the provider to finish.</p>
      {authUrl ? <a href={authUrl} target="_blank" rel="noreferrer">Continue to OpenAI</a> : null}
      <button type="button" className="button-muted" disabled={busyAction !== null} onClick={controller.onCancelLogin}>{busyAction === 'cancel' ? 'Cancelling…' : 'Cancel sign-in'}</button>
    </> : status?.ceremony === 'signed-in' ? <>
      <p>{busyAction === 'logout' ? 'Signing out of this project…' : status.admission === 'ready' ? 'Codex is ready for this project.' : status.admission === 'establishing' ? 'Your account is signed in. Codex is still preparing for this project.' : 'Your account is signed in, but Codex is not yet ready for project work.'}</p>
      <button type="button" className="button-muted" disabled={busyAction !== null} onClick={controller.onSignOut}>{busyAction === 'logout' ? 'Signing out…' : 'Sign out of this project'}</button>
    </> : <>
      {status?.ceremony === 'failed' && !signOutUncertain ? <p role="alert">Sign-in failed. You can start a new sign-in attempt.</p> : null}
      {status?.ceremony === 'cancelled' ? <p>The previous sign-in was cancelled.</p> : null}
      <button type="button" disabled={busyAction !== null || !status?.canStartLogin} onClick={controller.onStartLogin}>{busyAction === 'login' ? 'Starting sign-in…' : 'Sign in'}</button>
    </>}
    {error ? <p role="alert">{error}</p> : null}
  </section>;
}
