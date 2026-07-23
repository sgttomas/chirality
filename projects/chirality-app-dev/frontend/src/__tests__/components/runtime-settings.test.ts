import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import {
  RuntimeSettings,
  RuntimeSettingsView,
  type RuntimeSettingsViewProps
} from '../../components/settings/runtime-settings';

const baseProps: RuntimeSettingsViewProps = {
  bridgeAvailable: true,
  daemonStatus: {
    launchAgent: { installed: true, loaded: true },
    daemon: { running: true, pid: 4242 }
  },
  residency: {
    phase: 'READY',
    managedModelId: 'Qwen-local-exact',
    epoch: {
      epochId: 'epoch-1',
      modelId: 'Qwen-local-exact',
      activatedAt: '2026-07-22T00:00:00.000Z'
    },
    activeTurns: 0,
    acceptingLocalTurns: true,
    models: [
      {
        id: 'Qwen-local-exact',
        kind: 'llm',
        loaded: true,
        loading: false
      },
      {
        id: 'embedding-helper',
        kind: 'embedding',
        loaded: true,
        loading: false
      }
    ]
  },
  selectedModel: 'Qwen-local-exact',
  busyAction: null,
  error: null,
  onDaemonAction: () => undefined,
  onRefresh: () => undefined,
  onSelectedModelChange: () => undefined,
  onActivateModel: () => undefined
};

function renderView(overrides: Partial<RuntimeSettingsViewProps> = {}): string {
  return renderToStaticMarkup(
    createElement(RuntimeSettingsView, { ...baseProps, ...overrides })
  );
}

describe('RuntimeSettings rendering', () => {
  it('server-renders a Desktop-only fallback without invoking the bridge', () => {
    const html = renderToStaticMarkup(createElement(RuntimeSettings));

    expect(html).toContain('Shared Runtime');
    expect(html).toContain('Checking...');
    expect(html).toContain('available only in Chirality Desktop');
  });

  it('shows daemon lifecycle controls and exact managed-model attribution', () => {
    const html = renderView();

    expect(html).toContain('Running (PID 4242)');
    expect(html).toContain('Stop');
    expect(html).toContain('Uninstall');
    expect(html).toContain('Residency:');
    expect(html).toContain('Qwen-local-exact');
    expect(html).toContain('Activate Explicitly');
    expect(html).not.toContain('embedding-helper');
  });

  it('shows install when the LaunchAgent is absent', () => {
    const html = renderView({
      daemonStatus: {
        launchAgent: { installed: false, loaded: false },
        daemon: { running: false }
      },
      residency: null
    });

    expect(html).toContain('Not installed');
    expect(html).toContain('Install');
    expect(html).not.toContain('Uninstall');
    expect(html).not.toContain('Activate Explicitly');
  });

  it('shows start for an installed stopped daemon and renders errors', () => {
    const html = renderView({
      daemonStatus: {
        launchAgent: { installed: true, loaded: false },
        daemon: { running: false }
      },
      residency: null,
      error: 'Daemon failed closed'
    });

    expect(html).toContain('Installed and stopped');
    expect(html).toContain('Start');
    expect(html).toContain('Daemon failed closed');
  });

  it('disables explicit activation for the already managed model', () => {
    const html = renderView();
    const activationButton = html.match(
      /<button[^>]*disabled=""[^>]*>Activate Explicitly<\/button>/
    );

    expect(activationButton).not.toBeNull();
    expect(html).toContain('Activation never occurs automatically');
  });
});
