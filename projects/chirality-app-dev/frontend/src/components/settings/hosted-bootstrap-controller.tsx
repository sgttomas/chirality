'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import {
  cancelHostedBootstrapLogin,
  getHostedBootstrapStatus,
  grantHostedProviderNetworkConsent,
  initializeHostedBootstrapProject,
  hydrateHostedBootstrapProject,
  signOutHostedBootstrapProject,
  startHostedBootstrapLogin
} from '../../lib/harness/hosted-bootstrap-client';

export type HostedBootstrapStatusResult = Awaited<ReturnType<typeof getHostedBootstrapStatus>>;
type RegisteredBootstrap = Extract<HostedBootstrapStatusResult, { registration: 'registered' }>;

export type HostedBootstrapController = {
  projectRoot: string | null;
  snapshot: HostedBootstrapStatusResult | null;
  loading: boolean;
  busyAction: 'setup' | 'consent' | 'login' | 'cancel' | 'logout' | null;
  error: string | null;
  signOutUncertain: boolean;
  authUrl: string | null;
  onSetup: () => void;
  onGrantConsent: () => void;
  onStartLogin: () => void;
  onCancelLogin: () => void;
  onSignOut: () => void;
};

function messageFrom(error: unknown): string {
  return error instanceof Error ? error.message : 'The OpenAI account request could not be completed.';
}

function withStatus(current: HostedBootstrapStatusResult | null, status: RegisteredBootstrap['status']): HostedBootstrapStatusResult | null {
  return current?.registration === 'registered' ? { ...current, status } : current;
}

export function useHostedBootstrapController(projectRoot: string | null, onBindingChanged: () => void): HostedBootstrapController {
  const [observed, setObserved] = useState<{ projectRoot: string | null; snapshot: HostedBootstrapStatusResult | null }>({ projectRoot, snapshot: null });
  const snapshot = observed.projectRoot === projectRoot ? observed.snapshot : null;
  const [loading, setLoading] = useState(Boolean(projectRoot));
  const [busyAction, setBusyAction] = useState<HostedBootstrapController['busyAction']>(null);
  const [error, setError] = useState<string | null>(null);
  const [authUrl, setAuthUrl] = useState<string | null>(null);
  const [signOutUncertain, setSignOutUncertain] = useState(false);
  const rootRef = useRef(projectRoot);
  const snapshotRef = useRef(snapshot);
  const onBindingChangedRef = useRef(onBindingChanged);
  const publishedBindingKeys = useRef(new Set<string>());
  const operationGeneration = useRef(0);
  const actionController = useRef<AbortController | null>(null);
  const pollController = useRef<AbortController | null>(null);
  rootRef.current = projectRoot;
  snapshotRef.current = snapshot;
  onBindingChangedRef.current = onBindingChanged;

  const load = useCallback(async (root: string, generation: number, signal?: AbortSignal): Promise<void> => {
    const result = await hydrateHostedBootstrapProject(
      root,
      (binding) => {
        if (
          !signal?.aborted &&
          operationGeneration.current === generation &&
          rootRef.current === root
        ) {
          const key = `${root}:${binding.projectId}:registered`;
          if (!publishedBindingKeys.current.has(key)) {
            publishedBindingKeys.current.add(key);
            onBindingChangedRef.current();
          }
        }
      },
      signal
    );
    if (!signal?.aborted && operationGeneration.current === generation && rootRef.current === root) {
      setObserved({ projectRoot: root, snapshot: result });
      setError(null);
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    const generation = ++operationGeneration.current;
    actionController.current?.abort();
    pollController.current?.abort();
    publishedBindingKeys.current.clear();
    setObserved({ projectRoot, snapshot: null });
    setAuthUrl(null);
    setError(null);
    setSignOutUncertain(false);
    setBusyAction(null);
    if (!projectRoot) { setLoading(false); return; }
    setLoading(true);
    const controller = new AbortController();
    void load(projectRoot, generation, controller.signal).catch(reason => {
      if (!controller.signal.aborted && operationGeneration.current === generation && rootRef.current === projectRoot) {
        setError(messageFrom(reason));
        setLoading(false);
      }
    });
    return () => {
      ++operationGeneration.current;
      controller.abort();
      actionController.current?.abort();
      pollController.current?.abort();
    };
  }, [projectRoot, load]);

  useEffect(() => {
    if (!projectRoot || snapshot?.registration !== 'registered') return;
    const keys = [`${projectRoot}:${snapshot.projectId}:registered`];
    if (snapshot.status.admission === 'ready') keys.push(`${projectRoot}:${snapshot.projectId}:ready`);
    let publish = false;
    for (const key of keys) {
      if (publishedBindingKeys.current.has(key)) continue;
      publishedBindingKeys.current.add(key);
      publish = true;
    }
    if (publish) onBindingChanged();
    if (['signed-in', 'failed', 'cancelled'].includes(snapshot.status.ceremony)) setAuthUrl(null);
  }, [projectRoot, snapshot, onBindingChanged]);

  useEffect(() => {
    if (!projectRoot || busyAction || snapshot?.registration !== 'registered') return;
    const status = snapshot.status;
    if (status.ceremony !== 'pending' && status.admission !== 'establishing') return;
    const controller = new AbortController();
    pollController.current = controller;
    const generation = operationGeneration.current;
    let active = false;
    const poll = (): void => {
      if (active || controller.signal.aborted) return;
      active = true;
      void load(projectRoot, generation, controller.signal).catch(reason => {
        if (!controller.signal.aborted && operationGeneration.current === generation && rootRef.current === projectRoot) setError(messageFrom(reason));
      }).finally(() => { active = false; });
    };
    const timer = window.setInterval(poll, 1000);
    return () => {
      controller.abort();
      if (pollController.current === controller) pollController.current = null;
      window.clearInterval(timer);
    };
  }, [projectRoot, snapshot, busyAction, load]);

  const perform = useCallback(async (
    action: NonNullable<HostedBootstrapController['busyAction']>,
    run: (root: string, signal: AbortSignal, generation: number) => Promise<void>
  ): Promise<void> => {
    const root = rootRef.current;
    if (!root || busyAction) return;
    const generation = ++operationGeneration.current;
    actionController.current?.abort();
    pollController.current?.abort();
    const controller = new AbortController();
    actionController.current = controller;
    setBusyAction(action);
    setError(null);
    if (action !== 'logout') setSignOutUncertain(false);
    try { await run(root, controller.signal, generation); }
    catch (reason) {
      if (!controller.signal.aborted && operationGeneration.current === generation && rootRef.current === root) setError(messageFrom(reason));
    } finally {
      if (actionController.current === controller) actionController.current = null;
      if (!controller.signal.aborted && operationGeneration.current === generation && rootRef.current === root) setBusyAction(null);
    }
  }, [busyAction]);

  return {
    projectRoot, snapshot, loading, busyAction, error, authUrl, signOutUncertain,
    onSetup: () => void perform('setup', async (root, signal, generation) => {
      const result = await initializeHostedBootstrapProject(root, signal);
      if (signal.aborted || operationGeneration.current !== generation || rootRef.current !== root) return;
      setObserved({ projectRoot: root, snapshot: result });
      setAuthUrl(null);
    }),
    onGrantConsent: () => void perform('consent', async (root, signal, generation) => {
      const status = await grantHostedProviderNetworkConsent(root, signal);
      if (!signal.aborted && operationGeneration.current === generation && rootRef.current === root) setObserved(current => ({ projectRoot: root, snapshot: withStatus(current.projectRoot === root ? current.snapshot : null, status) }));
    }),
    onStartLogin: () => void perform('login', async (root, signal, generation) => {
      const result = await startHostedBootstrapLogin(root, signal);
      if (signal.aborted || operationGeneration.current !== generation || rootRef.current !== root) return;
      setAuthUrl(result.authUrl);
      setObserved(current => ({
        projectRoot: root,
        snapshot: current.projectRoot === root && current.snapshot?.registration === 'registered'
          ? { ...current.snapshot, status: { ...current.snapshot.status, ceremony: 'pending', canStartLogin: false } }
          : current.snapshot
      }));
      await load(root, generation, signal);
    }),
    onCancelLogin: () => void perform('cancel', async (root, signal, generation) => {
      const status = await cancelHostedBootstrapLogin(root, signal);
      if (signal.aborted || operationGeneration.current !== generation || rootRef.current !== root) return;
      setAuthUrl(null);
      setObserved(current => ({ projectRoot: root, snapshot: withStatus(current.projectRoot === root ? current.snapshot : null, status) }));
    }),
    onSignOut: () => void perform('logout', async (root, signal, generation) => {
      const currentSnapshot = snapshotRef.current;
      if (currentSnapshot?.registration === 'registered') {
        publishedBindingKeys.current.delete(`${root}:${currentSnapshot.projectId}:ready`);
      }
      setAuthUrl(null);
      setSignOutUncertain(false);
      setObserved(current => {
        if (current.projectRoot !== root || current.snapshot?.registration !== 'registered') return current;
        return { projectRoot: root, snapshot: withStatus(current.snapshot, { ...current.snapshot.status, admission: 'unavailable' }) };
      });
      try {
        const status = await signOutHostedBootstrapProject(root, signal);
        if (signal.aborted || operationGeneration.current !== generation || rootRef.current !== root) return;
        setObserved(current => ({ projectRoot: root, snapshot: withStatus(current.projectRoot === root ? current.snapshot : null, status) }));
        onBindingChanged();
      } catch {
        if (signal.aborted || operationGeneration.current !== generation || rootRef.current !== root) return;
        setSignOutUncertain(true);
        try {
          const reconciled = await getHostedBootstrapStatus(root, signal);
          if (!signal.aborted && operationGeneration.current === generation && rootRef.current === root) {
            setObserved({
              projectRoot: root,
              snapshot: reconciled.registration === 'registered'
                ? { ...reconciled, status: { ...reconciled.status, admission: 'unavailable' } }
                : reconciled
            });
          }
        } catch {}
        if (!signal.aborted && operationGeneration.current === generation && rootRef.current === root) onBindingChanged();
        throw new Error('Sign-out could not be confirmed. Check this project’s status before signing in again.');
      }
    })
  };
}
