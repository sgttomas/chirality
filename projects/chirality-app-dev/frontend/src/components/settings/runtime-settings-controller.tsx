'use client';

import { useCallback, useEffect, useState } from 'react';
import { useRuntimeEpoch } from '../shell/runtime-connectivity-provider';

export type RuntimeDaemonAction = 'install' | 'start' | 'stop' | 'status' | 'uninstall';

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

export function useRuntimeSettingsController({ localModels = true }: { localModels?: boolean } = {}): RuntimeSettingsViewProps {
  const [daemonStatus, setDaemonStatus] = useState<RuntimeDaemonStatus | null>(null);
  const [residency, setResidency] = useState<RuntimeResidencyStatus | null>(null);
  const [selectedModel, setSelectedModel] = useState('');
  const [busyAction, setBusyAction] = useState<RuntimeDaemonAction | 'models' | null>(
    null
  );
  const [error, setError] = useState<string | null>(null);
  const [bridgeAvailable, setBridgeAvailable] = useState(false);
  const runtimeEpoch = useRuntimeEpoch();

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
      setDaemonStatus(null);
      setResidency(null);
      return;
    }

    setBridgeAvailable(true);
    setBusyAction('status');
    setError(null);
    setDaemonStatus(null);
    setResidency(null);
    try {
      const daemonResult = await bridge.daemon.status();
      if (!daemonResult.ok) {
        setError(daemonResult.error);
        return;
      }
      setDaemonStatus(daemonResult);

      if (!daemonResult.daemon.running || !localModels) {
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
  }, [applyResidency, localModels]);

  // Re-probed on reconnect as well as on mount: this panel's whole content is a
  // claim about the daemon ("not running", "no models"), and a claim captured
  // while the client was unbound is exactly the one the operator opens it to
  // check after the daemon comes back.
  useEffect(() => {
    void refresh();
  }, [refresh, runtimeEpoch]);

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
      } else if (localModels) {
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
    if (!bridge || !localModels || !selectedModel) return;
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

  return { bridgeAvailable, daemonStatus, residency, selectedModel, busyAction, error,
    onDaemonAction: (action) => void runDaemonAction(action),
    onRefresh: () => void refresh(), onSelectedModelChange: setSelectedModel,
    onActivateModel: () => void activateModel() };
}
