'use client';

import React, { useEffect, useMemo, useState } from 'react';
import { useRouter } from 'next/navigation';
import {
  useDeliverables,
  type DeliverablesScan
} from '../workspace/deliverables-provider';
import { createNavigationIntentScheduler } from '../../lib/workspace/navigation-intent';
import {
  MATRIX_ROWS,
  isMatrixLaunchBlockedByStreaming,
  matrixCellLaunchKind,
  type MatrixCell
} from '../../lib/portal/agent-matrix-cells';
import { resolvePersona } from '../../lib/shell/persona-resolution';
import { useHarnessStreaming } from '../workspace/harness-events-provider';

function focusLiveLoopInput(): void {
  if (typeof window === 'undefined') {
    return;
  }

  window.requestAnimationFrame(() => {
    document.querySelector<HTMLInputElement>('[data-chat-input="primary"]')?.focus();
  });
}

function agentParamFromTarget(target: string): string | null {
  try {
    const url = new URL(target, 'http://chirality.local');
    return url.searchParams.get('agent');
  } catch {
    return null;
  }
}

type AgentMatrixPanelProps = {
  loading: boolean;
  error: string | null;
  scan: DeliverablesScan | null;
  streaming: boolean;
  launchNotice: string | null;
  onFocusLoop: () => void;
  onCellLaunch: (cell: MatrixCell) => void;
  onDeliverableLaunch: (deliverableKey: string) => void;
};

export function AgentMatrixPanel({
  loading,
  error,
  scan,
  streaming,
  launchNotice,
  onFocusLoop,
  onCellLaunch,
  onDeliverableLaunch
}: AgentMatrixPanelProps): JSX.Element {
  const blocked = isMatrixLaunchBlockedByStreaming(streaming);
  const blockedTitle = 'A turn is running; wait for it to finish before changing launch context.';

  return (
    <section className="portal-matrix portal-matrix--sidebar">
      <header className="portal-matrix-header">
        <div className="portal-matrix-heading">
          <h3>Agent Matrix</h3>
          <p>
            Type-0/Type-1 cells focus the mounted live loop. OPERATIVE cells keep the
            governed PIPELINE route until the tertiary form lands.
          </p>
        </div>
        <button
          type="button"
          className="portal-start-session"
          disabled={blocked}
          title={blocked ? blockedTitle : undefined}
          onClick={onFocusLoop}
        >
          Focus live loop
        </button>
      </header>

      {streaming ? (
        <p className="portal-launch-notice" role="status">
          A turn is running. Matrix launches are paused so the mounted loop is not clobbered.
        </p>
      ) : launchNotice ? (
        <p className="portal-launch-notice" role="status">
          {launchNotice}
        </p>
      ) : null}

      <div className="matrix-grid" role="grid" aria-label="Chirality Agent Matrix">
        <div className="matrix-header-cell" />
        <div className="matrix-header-cell">GUIDING</div>
        <div className="matrix-header-cell">APPLYING</div>
        <div className="matrix-header-cell">JUDGING</div>
        <div className="matrix-header-cell">REVIEWING</div>

        {MATRIX_ROWS.map((row) => (
          <div key={row.rowLabel} className="matrix-row-group">
            <div className="matrix-row-label">{row.rowLabel}</div>
            {row.cells.map((cell) => {
              const launchKind = matrixCellLaunchKind(cell);
              return (
                <button
                  key={`${cell.row}-${cell.column}`}
                  type="button"
                  className="matrix-cell"
                  disabled={blocked}
                  title={blocked ? blockedTitle : undefined}
                  onClick={() => {
                    onCellLaunch(cell);
                  }}
                >
                  <span>{cell.label}</span>
                  <small>{launchKind === 'loop-persona' ? 'Loop' : 'Pipeline'}</small>
                </button>
              );
            })}
          </div>
        ))}
      </div>

      <section className="portal-deliverables">
        <header>
          <h4>OPERATIVE Deliverable Rows</h4>
          <p>Select a deliverable row to open PIPELINE `TASK*` with that `pkg::id` pre-selected.</p>
        </header>

        {loading ? (
          <p className="pipeline-note">Loading deliverables from `/api/project/deliverables`...</p>
        ) : error ? (
          <p className="panel-error">{error}</p>
        ) : !scan || scan.deliverables.length === 0 ? (
          <p className="panel-empty">No deliverables found for the selected Working Root.</p>
        ) : (
          <div className="portal-deliverable-grid">
            {scan.deliverables.map((deliverable) => {
              const deliverableKey = deliverable.key;
              return (
                <button
                  key={deliverable.path}
                  type="button"
                  className="portal-deliverable-row"
                  title={blocked ? blockedTitle : deliverable.path}
                  disabled={blocked}
                  onClick={() => {
                    onDeliverableLaunch(deliverableKey);
                  }}
                >
                  <span className="portal-deliverable-key">{deliverableKey}</span>
                  <span className="portal-deliverable-name">{deliverable.name}</span>
                </button>
              );
            })}
          </div>
        )}
      </section>
    </section>
  );
}

export function AgentMatrix(): JSX.Element {
  const router = useRouter();
  const { loading, error, scan } = useDeliverables();
  const streaming = useHarnessStreaming();
  const [launchNotice, setLaunchNotice] = useState<string | null>(null);
  const navigationScheduler = useMemo(
    () =>
      createNavigationIntentScheduler({
        onNavigate: (target) => {
          router.push(target);
        }
      }),
    [router]
  );

  useEffect(() => {
    return () => {
      navigationScheduler.cancel();
    };
  }, [navigationScheduler]);

  function focusLoop(): void {
    if (streaming) {
      setLaunchNotice('A turn is running; wait for it to finish before changing launch context.');
      return;
    }

    setLaunchNotice('Live loop focused.');
    focusLiveLoopInput();
  }

  function launchCell(cell: MatrixCell): void {
    if (streaming) {
      setLaunchNotice('A turn is running; wait for it to finish before changing launch context.');
      return;
    }

    if (matrixCellLaunchKind(cell) === 'loop-persona') {
      const rawAgent = agentParamFromTarget(cell.target);
      const persona = resolvePersona(rawAgent);
      router.replace(cell.target, { scroll: false });
      setLaunchNotice(`${persona} selected in the live loop.`);
      focusLiveLoopInput();
      return;
    }

    navigationScheduler.schedule(cell.target);
  }

  function launchDeliverable(deliverableKey: string): void {
    if (streaming) {
      setLaunchNotice('A turn is running; wait for it to finish before opening PIPELINE.');
      return;
    }

    const params = new URLSearchParams({
      category: 'TASK',
      taskScopeMode: 'DELIVERABLES',
      scopeKey: deliverableKey
    });
    navigationScheduler.schedule(`/pipeline?${params.toString()}`);
  }

  return (
    <AgentMatrixPanel
      loading={loading}
      error={error}
      scan={scan}
      streaming={streaming}
      launchNotice={launchNotice}
      onFocusLoop={focusLoop}
      onCellLaunch={launchCell}
      onDeliverableLaunch={launchDeliverable}
    />
  );
}
