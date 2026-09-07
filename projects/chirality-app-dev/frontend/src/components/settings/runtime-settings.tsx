'use client';

import React, { useMemo, type ChangeEvent } from 'react';
import { useRuntimeSettingsController, type RuntimeSettingsViewProps } from './runtime-settings-controller';
export type { RuntimeSettingsViewProps, RuntimeDaemonStatus, RuntimeModel, RuntimeResidencyStatus } from './runtime-settings-controller';

export function RuntimeSettings({ controller }: { controller?: RuntimeSettingsViewProps } = {}): JSX.Element {
  return controller ? <RuntimeSettingsView {...controller} /> : <StandaloneRuntimeSettings />;
}

function StandaloneRuntimeSettings(): JSX.Element {
  const controller = useRuntimeSettingsController();
  return <RuntimeSettingsView {...controller} />;
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
