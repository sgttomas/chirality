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

// Explanations live on the action they qualify (hover / accessible description)
// so the surface reads as one status line plus one action.
const SETUP_EXPLANATION = (folder: string | null | undefined) => `Use ${folder ?? 'this folder'} as the Chirality project. This writes one minimal chirality.project.json configuration if it is missing. Existing malformed or conflicting configuration is never replaced.`;
const CONSENT_EXPLANATION = 'Allow this project to contact the OpenAI provider over HTTPS for sign-in and Codex work.';
const PENDING_EXPLANATION = 'Complete sign-in with OpenAI. Chirality is waiting for the provider to finish.';

function signedInExplanation(admission: 'unavailable' | 'establishing' | 'ready', busy: boolean): string {
  if (busy) return 'Signing out of this project…';
  if (admission === 'ready') return 'Codex is ready for this project.';
  if (admission === 'establishing') return 'Your account is signed in. Codex is still preparing for this project.';
  return 'Your account is signed in, but Codex is not yet ready for project work.';
}

export function HostedBootstrapView({ controller, compact = false }: { controller: HostedBootstrapController; compact?: boolean }): JSX.Element {
  const { projectRoot, snapshot, loading, busyAction, error, authUrl, signOutUncertain } = controller;
  const status = snapshot?.registration === 'registered' ? snapshot.status : null;
  const folderName = projectRoot?.split('/').filter(Boolean).pop() || projectRoot;
  return <section className="hosted-bootstrap" aria-label="OpenAI account" data-bootstrap-registration={snapshot?.registration ?? 'unknown'} data-bootstrap-ceremony={status?.ceremony ?? 'unknown'} data-bootstrap-admission={status?.admission ?? 'unavailable'}>
    {!compact ? <h3>OpenAI account</h3> : null}
    <p className="api-key-status"><strong>{hostedBootstrapSummary(controller)}</strong></p>
    {!projectRoot || loading ? null : snapshot?.registration !== 'registered' ?
      <button type="button" disabled={busyAction !== null} title={SETUP_EXPLANATION(folderName)} onClick={controller.onSetup}>{busyAction === 'setup' ? 'Setting up…' : 'Use this folder'}</button>
    : status?.ceremony === 'consent-required' ?
      <button type="button" disabled={busyAction !== null} title={CONSENT_EXPLANATION} onClick={controller.onGrantConsent}>{busyAction === 'consent' ? 'Allowing…' : 'Allow provider network'}</button>
    : status?.ceremony === 'pending' ? <>
      {authUrl ? <a href={authUrl} target="_blank" rel="noreferrer" title={PENDING_EXPLANATION}>Continue to OpenAI</a> : null}
      <button type="button" className="button-muted" disabled={busyAction !== null} title={PENDING_EXPLANATION} onClick={controller.onCancelLogin}>{busyAction === 'cancel' ? 'Cancelling…' : 'Cancel sign-in'}</button>
    </> : status?.ceremony === 'signed-in' ?
      <button type="button" className="button-muted" disabled={busyAction !== null} title={signedInExplanation(status.admission, busyAction === 'logout')} onClick={controller.onSignOut}>{busyAction === 'logout' ? 'Signing out…' : 'Sign out of this project'}</button>
    : <>
      {status?.ceremony === 'failed' && !signOutUncertain ? <p role="alert">Sign-in failed. You can start a new sign-in attempt.</p> : null}
      {status?.ceremony === 'cancelled' ? <p>The previous sign-in was cancelled.</p> : null}
      <button type="button" disabled={busyAction !== null || !status?.canStartLogin} onClick={controller.onStartLogin}>{busyAction === 'login' ? 'Starting sign-in…' : 'Sign in'}</button>
    </>}
    {error ? <p role="alert">{error}</p> : null}
  </section>;
}
