'use client';

import React from 'react';
import type { HostedBootstrapController } from './hosted-bootstrap-controller';

/**
 * The account row's neutral label. Authentication state never leaks into the
 * label itself; it is reported by the summary line and the popover detail.
 */
export function hostedBootstrapTitle(_controller: HostedBootstrapController): string {
  return 'Account';
}

export type HostedBootstrapAuthState = 'signed-in' | 'pending' | 'failed' | 'cancelled' | 'signed-out' | 'setup-required' | 'no-folder' | 'checking';
export type HostedBootstrapReadinessState = 'ready' | 'establishing' | 'unavailable' | 'not-applicable';

/** Authentication and Runtime readiness, kept separate so the UI never blends them. */
export function hostedBootstrapStates(controller: HostedBootstrapController): { auth: HostedBootstrapAuthState; readiness: HostedBootstrapReadinessState } {
  if (!controller.projectRoot) return { auth: 'no-folder', readiness: 'not-applicable' };
  if (controller.loading) return { auth: 'checking', readiness: 'not-applicable' };
  if (controller.snapshot?.registration !== 'registered') return { auth: 'setup-required', readiness: 'not-applicable' };
  const { ceremony, admission } = controller.snapshot.status;
  if (ceremony === 'signed-in') return { auth: 'signed-in', readiness: admission };
  if (ceremony === 'pending') return { auth: 'pending', readiness: 'not-applicable' };
  // An unconfirmed sign-out leaves the ceremony `failed` without a failed sign-in attempt; report it as signed out.
  if (ceremony === 'failed') return { auth: controller.signOutUncertain ? 'signed-out' : 'failed', readiness: 'not-applicable' };
  if (ceremony === 'cancelled') return { auth: 'cancelled', readiness: 'not-applicable' };
  return { auth: 'signed-out', readiness: 'not-applicable' };
}

export function authStateLabel(auth: HostedBootstrapAuthState): string {
  switch (auth) {
    case 'signed-in': return 'Signed in';
    case 'pending': return 'Waiting for sign-in…';
    case 'failed': return 'Sign-in failed';
    case 'cancelled': return 'Sign-in cancelled';
    case 'signed-out': return 'Not signed in';
    case 'setup-required': return 'Project setup required';
    case 'no-folder': return 'No folder chosen';
    default: return 'Checking…';
  }
}

export function readinessStateLabel(readiness: HostedBootstrapReadinessState): string {
  switch (readiness) {
    case 'ready': return 'Ready to work';
    case 'establishing': return 'Preparing engine';
    case 'unavailable': return 'Engine unavailable';
    default: return 'Not ready';
  }
}

/** One line for the account row: authentication, then readiness when it applies. */
export function hostedBootstrapSummary(controller: HostedBootstrapController): string {
  const { auth, readiness } = hostedBootstrapStates(controller);
  if (auth === 'no-folder') return 'Choose a folder to get started';
  if (auth === 'checking') return 'Checking this project…';
  if (auth === 'setup-required') return 'Project setup required';
  if (auth === 'signed-in') return `Signed in · ${readinessStateLabel(readiness)}`;
  if (auth === 'pending') return 'Waiting for sign-in…';
  if (auth === 'failed') return 'Sign-in failed';
  if (auth === 'cancelled') return 'Sign-in cancelled';
  return 'Sign in required';
}

// Explanations live on the action they qualify (hover / accessible description)
// so the surface reads as one status line plus one action.
const SETUP_EXPLANATION = (folder: string | null | undefined) => `Use ${folder ?? 'this folder'} as the Chirality project. This writes one minimal chirality.project.json configuration if it is missing. Existing malformed or conflicting configuration is never replaced.`;
const PENDING_EXPLANATION = 'Finish signing in with your ChatGPT account in the browser. Chirality is waiting for OpenAI to confirm.';
const SIGN_IN_EXPLANATION = 'Opens the OpenAI sign-in page in your browser. Codex keeps the credentials; Chirality only waits for the result.';

function signedInExplanation(admission: 'unavailable' | 'establishing' | 'ready', busy: boolean): string {
  if (busy) return 'Signing out of Codex in Chirality…';
  if (admission === 'ready') return 'Codex is ready. Signing out affects only Chirality; other Codex clients keep their own sign-in.';
  if (admission === 'establishing') return 'Your account is signed in. Codex is still preparing.';
  return 'Your account is signed in, but Codex is not yet ready for work.';
}

export function HostedBootstrapView({ controller, compact = false }: { controller: HostedBootstrapController; compact?: boolean }): JSX.Element {
  const { projectRoot, snapshot, loading, busyAction, error, authUrl, signOutUncertain } = controller;
  const status = snapshot?.registration === 'registered' ? snapshot.status : null;
  const folderName = projectRoot?.split('/').filter(Boolean).pop() || projectRoot;
  const states = hostedBootstrapStates(controller);
  const showReadiness = states.auth === 'signed-in';
  return <section className="hosted-bootstrap" aria-label="Account" data-bootstrap-registration={snapshot?.registration ?? 'unknown'} data-bootstrap-ceremony={status?.ceremony ?? 'unknown'} data-bootstrap-admission={status?.admission ?? 'unavailable'}>
    {!compact ? <h3>Account</h3> : null}
    {compact
      ? <dl className="hosted-bootstrap-states">
          <div><dt>Sign-in</dt><dd data-auth-state={states.auth}>{authStateLabel(states.auth)}</dd></div>
          {showReadiness ? <div><dt>Runtime</dt><dd data-readiness-state={states.readiness}>{readinessStateLabel(states.readiness)}</dd></div> : null}
        </dl>
      : <p className="api-key-status"><strong>{hostedBootstrapSummary(controller)}</strong></p>}
    {!projectRoot || loading ? null : snapshot?.registration !== 'registered' ?
      <button type="button" disabled={busyAction !== null} title={SETUP_EXPLANATION(folderName)} onClick={controller.onSetup}>{busyAction === 'setup' ? 'Setting up…' : 'Use this folder'}</button>
    : status?.ceremony === 'pending' ? <>
      <p className="hosted-bootstrap-pending" role="status">{PENDING_EXPLANATION}</p>
      <div className="hosted-bootstrap-actions">
        {authUrl ? <button type="button" className="button-muted" disabled={busyAction !== null} title="Open the same OpenAI sign-in page again in your browser." onClick={controller.onReopenLogin}>Open sign-in page again</button> : null}
        <button type="button" className="button-muted" disabled={busyAction !== null} title="Stop waiting and cancel this sign-in attempt." onClick={controller.onCancelLogin}>{busyAction === 'cancel' ? 'Cancelling…' : 'Cancel'}</button>
      </div>
    </> : status?.ceremony === 'signed-in' ?
      <button type="button" className="button-muted" disabled={busyAction !== null} title={signedInExplanation(status.admission, busyAction === 'logout')} onClick={controller.onSignOut}>{busyAction === 'logout' ? 'Signing out…' : 'Sign out'}</button>
    : <>
      {status?.ceremony === 'failed' && !signOutUncertain ? <p role="alert">Sign-in failed. You can start a new sign-in attempt.</p> : null}
      {status?.ceremony === 'cancelled' ? <p>The previous sign-in was cancelled.</p> : null}
      <button type="button" disabled={busyAction !== null || !status?.canStartLogin} title={SIGN_IN_EXPLANATION} onClick={controller.onStartLogin}>{busyAction === 'login' ? 'Opening sign-in…' : 'Sign in with your ChatGPT account'}</button>
    </>}
    {error ? <p role="alert">{error}</p> : null}
  </section>;
}
