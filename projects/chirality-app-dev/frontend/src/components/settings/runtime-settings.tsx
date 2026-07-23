'use client';

import React, { useCallback, useEffect, useMemo, useState } from 'react';
import type { ChangeEvent } from 'react';

type RuntimeDaemonAction = 'install' | 'start' | 'stop' | 'status' | 'uninstall';

export type RuntimeDaemonStatus = {
  launchAgent: {
    installed: boolean;
    loaded: boolean;
  };
  daemon: {
    running: boolean;
    pid?: number;
    startedAt?: string;
  };
};

export type RuntimeModel = {
  id: string;
  kind: 'llm' | 'embedding' | 'reranker' | 'helper' | 'unknown';
  loaded: boolean;
  loading: boolean;
  managed?: boolean;
};

export type RuntimeResidencyStatus = {
  phase: 'NO_MODEL' | 'READY' | 'DRAINING' | 'UNLOADING' | 'LOADING';
  managedModelId?: string;
  epoch?: {
    epochId: string;
    modelId: string;
    activatedAt: string;
  };
  activeTurns: number;
  acceptingLocalTurns: boolean;
  models: readonly RuntimeModel[];
};

type RuntimeDaemonControlResult =
  | ({ ok: true } & RuntimeDaemonStatus)
  | { ok: false; error: string };

type RuntimeModelStatusResult =
  | { ok: true; residency: RuntimeResidencyStatus }
  | { ok: false; error: string };

type ChiralityRuntimeBridge = {
  daemon: Record<
    RuntimeDaemonAction,
    () => Promise<RuntimeDaemonControlResult>
  >;
  models: {
    status: () => Promise<RuntimeModelStatusResult>;
    activate: (modelId: string) => Promise<RuntimeModelStatusResult>;
  };
};

type RuntimeWindow = typeof window & {
  chirality?: {
    runtime?: ChiralityRuntimeBridge;
  };
};

export type RuntimeSettingsViewProps = {
  bridgeAvailable: boolean;
  daemonStatus: RuntimeDaemonStatus | null;
  residency: RuntimeResidencyStatus | null;
  selectedModel: string;
  busyAction: RuntimeDaemonAction | 'models' | null;
  error: string | null;
  onDaemonAction: (action: RuntimeDaemonAction) => void;
  onRefresh: () => void;
  onSelectedModelChange: (modelId: string) => void;
  onActivateModel: () => void;
};

function getRuntimeBridge(): ChiralityRuntimeBridge | undefined {
  if (typeof window === 'undefined') {
    return undefined;
  }
  return (window as RuntimeWindow).chirality?.runtime;
}

export function RuntimeSettings(): JSX.Element {
  const [daemonStatus, setDaemonStatus] = useState<RuntimeDaemonStatus | null>(null);
  const [residency, setResidency] = useState<RuntimeResidencyStatus | null>(null);
  const [selectedModel, setSelectedModel] = useState('');
  const [busyAction, setBusyAction] = useState<RuntimeDaemonAction | 'models' | null>(
    null
  );
  const [error, setError] = useState<string | null>(null);
  const [bridgeAvailable, setBridgeAvailable] = useState(false);

  const applyResidency = useCallback((next: RuntimeResidencyStatus) => {
    setResidency(next);
    setSelectedModel((current) => {
      if (current && next.models.some((model) => model.id === current)) {
        return current;
      }
      return next.managedModelId ?? next.models.find((model) => model.kind === 'llm')?.id ??
        next.models.find((model) => model.kind === 'unknown')?.id ?? '';
    });
  }, []);

  const refresh = useCallback(async () => {
    const bridge = getRuntimeBridge();
    if (!bridge) {
      setBridgeAvailable(false);
      return;
    }

    setBridgeAvailable(true);
    setBusyAction('status');
    setError(null);
    try {
      const daemonResult = await bridge.daemon.status();
      if (!daemonResult.ok) {
        setError(daemonResult.error);
        return;
      }
      setDaemonStatus(daemonResult);

      if (!daemonResult.daemon.running) {
        setResidency(null);
        return;
      }

      const modelResult = await bridge.models.status();
      if (!modelResult.ok) {
        setError(modelResult.error);
        return;
      }
      applyResidency(modelResult.residency);
    } catch {
      setError('Unable to contact the Chirality runtime');
    } finally {
      setBusyAction(null);
    }
  }, [applyResidency]);

  useEffect(() => {
    void refresh();
  }, [refresh]);

  async function runDaemonAction(action: RuntimeDaemonAction): Promise<void> {
    const bridge = getRuntimeBridge();
    if (!bridge) return;
    if (
      action === 'uninstall' &&
      !window.confirm(
        'Uninstall the Chirality runtime LaunchAgent? Existing sessions and credentials are retained.'
      )
    ) {
      return;
    }

    setBusyAction(action);
    setError(null);
    try {
      const result = await bridge.daemon[action]();
      if (!result.ok) {
        setError(result.error);
        return;
      }
      setDaemonStatus(result);
      if (!result.daemon.running) {
        setResidency(null);
      } else {
        const modelResult = await bridge.models.status();
        if (modelResult.ok) {
          applyResidency(modelResult.residency);
        }
      }
    } catch {
      setError(`Unable to ${action} the Chirality runtime daemon`);
    } finally {
      setBusyAction(null);
    }
  }

  async function activateModel(): Promise<void> {
    const bridge = getRuntimeBridge();
    if (!bridge || !selectedModel) return;
    if (
      !window.confirm(
        `Activate the exact oMLX model “${selectedModel}”? Active local turns will be drained before a model switch.`
      )
    ) {
      return;
    }

    setBusyAction('models');
    setError(null);
    try {
      const result = await bridge.models.activate(selectedModel);
      if (!result.ok) {
        setError(result.error);
        return;
      }
      applyResidency(result.residency);
    } catch {
      setError('Unable to activate the selected oMLX model');
    } finally {
      setBusyAction(null);
    }
  }

  return (
    <RuntimeSettingsView
      bridgeAvailable={bridgeAvailable}
      daemonStatus={daemonStatus}
      residency={residency}
      selectedModel={selectedModel}
      busyAction={busyAction}
      error={error}
      onDaemonAction={(action) => void runDaemonAction(action)}
      onRefresh={() => void refresh()}
      onSelectedModelChange={setSelectedModel}
      onActivateModel={() => void activateModel()}
    />
  );
}

export function RuntimeSettingsView({
  bridgeAvailable,
  daemonStatus,
  residency,
  selectedModel,
  busyAction,
  error,
  onDaemonAction,
  onRefresh,
  onSelectedModelChange,
  onActivateModel
}: RuntimeSettingsViewProps): JSX.Element {
  const selectableModels = useMemo(
    () =>
      residency?.models.filter(
        (model) => model.kind === 'llm' || model.kind === 'unknown'
      ) ?? [],
    [residency]
  );
  const selected = selectableModels.find((model) => model.id === selectedModel);
  const modelBusy =
    busyAction === 'models' ||
    residency?.phase === 'DRAINING' ||
    residency?.phase === 'UNLOADING' ||
    residency?.phase === 'LOADING';
  const daemonLabel = !daemonStatus
    ? 'Checking...'
    : daemonStatus.daemon.running
      ? `Running${daemonStatus.daemon.pid ? ` (PID ${daemonStatus.daemon.pid})` : ''}`
      : daemonStatus.launchAgent.loaded
        ? 'LaunchAgent loaded; daemon unavailable'
        : daemonStatus.launchAgent.installed
          ? 'Installed and stopped'
          : 'Not installed';

  return (
    <section className="runtime-settings" aria-labelledby="runtime-settings-title">
      <h3 className="api-key-settings-title" id="runtime-settings-title">
        Shared Runtime
      </h3>
      <p
        className="runtime-status"
        data-running={daemonStatus?.daemon.running ? 'true' : 'false'}
      >
        {daemonLabel}
      </p>

      {bridgeAvailable ? (
        <>
          <div className="runtime-control-row">
            {!daemonStatus?.launchAgent.installed ? (
              <button
                type="button"
                onClick={() => onDaemonAction('install')}
                disabled={busyAction !== null}
              >
                {busyAction === 'install' ? 'Installing...' : 'Install'}
              </button>
            ) : null}
            {daemonStatus?.launchAgent.installed && !daemonStatus.launchAgent.loaded ? (
              <button
                type="button"
                onClick={() => onDaemonAction('start')}
                disabled={busyAction !== null}
              >
                {busyAction === 'start' ? 'Starting...' : 'Start'}
              </button>
            ) : null}
            {daemonStatus?.launchAgent.loaded ? (
              <button
                type="button"
                onClick={() => onDaemonAction('stop')}
                disabled={busyAction !== null}
              >
                {busyAction === 'stop' ? 'Stopping...' : 'Stop'}
              </button>
            ) : null}
            <button
              type="button"
              className="button-muted"
              onClick={onRefresh}
              disabled={busyAction !== null}
            >
              Refresh
            </button>
            {daemonStatus?.launchAgent.installed ? (
              <button
                type="button"
                className="button-muted runtime-uninstall"
                onClick={() => onDaemonAction('uninstall')}
                disabled={busyAction !== null}
              >
                {busyAction === 'uninstall' ? 'Uninstalling...' : 'Uninstall'}
              </button>
            ) : null}
          </div>

          {daemonStatus?.daemon.running ? (
            <div className="runtime-model-controls">
              <p className="runtime-model-status">
                Residency: <strong>{residency?.phase ?? 'Checking'}</strong>
                {residency?.managedModelId
                  ? ` · ${residency.managedModelId}`
                  : ' · no managed model'}
                {residency ? ` · ${residency.activeTurns} active turn(s)` : ''}
              </p>
              <div className="runtime-control-row">
                <select
                  aria-label="Exact oMLX model"
                  value={selectedModel}
                  onChange={(event: ChangeEvent<HTMLSelectElement>) =>
                    onSelectedModelChange(event.target.value)
                  }
                  disabled={modelBusy || selectableModels.length === 0}
                >
                  {selectableModels.length === 0 ? (
                    <option value="">No oMLX LLMs reported</option>
                  ) : null}
                  {selectableModels.map((model) => (
                    <option key={model.id} value={model.id}>
                      {model.id}
                      {model.loaded ? ' (loaded)' : ''}
                    </option>
                  ))}
                </select>
                <button
                  type="button"
                  onClick={onActivateModel}
                  disabled={
                    modelBusy ||
                    !selectedModel ||
                    selected?.id === residency?.managedModelId
                  }
                >
                  {busyAction === 'models' ? 'Activating...' : 'Activate Explicitly'}
                </button>
              </div>
              <p className="api-key-hint">
                Activation never occurs automatically. A switch drains active local turns before
                unloading the managed model.
              </p>
            </div>
          ) : null}
        </>
      ) : (
        <p className="api-key-hint">
          Runtime controls are available only in Chirality Desktop.
        </p>
      )}

      {error ? <p className="api-key-error">{error}</p> : null}
    </section>
  );
}
