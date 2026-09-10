import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { shouldPreventNativeQuit } from '../../../electron/runtime-shutdown-policy';

const mainSource = readFileSync(new URL('../../../electron/main.ts', import.meta.url), 'utf8');

describe('electron/runtime-daemon signal integration', () => {
  it('installs the shared one-shot binder only through daemon initialization', () => {
    expect(mainSource).toContain(
      "import { installRuntimeDaemonSignalShutdown } from '@chirality/runtime-daemon';"
    );
    expect(mainSource).toContain(
      "if (runtimeDaemonMode) {\n      await initializeDaemon();\n      return;\n    }"
    );

    const initializeDaemon = mainSource.slice(
      mainSource.indexOf('async function initializeDaemon(): Promise<void> {'),
      mainSource.indexOf('/**\n * Release everything this process owns')
    );
    expect(initializeDaemon).toContain('runtimeHost = await startRuntimeHost(');
    expect(initializeDaemon).toContain('installRuntimeDaemonSignalShutdown({');
    expect(initializeDaemon).toContain("stop: () => shutdown(0, 'runtime-daemon-signal')");
    expect(initializeDaemon.indexOf('runtimeHost = await startRuntimeHost(')).toBeLessThan(
      initializeDaemon.indexOf('installRuntimeDaemonSignalShutdown({')
    );
  });

  it('keeps direct process signals GUI-only and preserves the shared shutdown funnel', () => {
    expect(mainSource).toContain(
      "if (!runtimeDaemonMode) {\n  for (const signal of ['SIGINT', 'SIGTERM'] as const)"
    );
    expect(mainSource.match(/process\.once\(signal/g)).toHaveLength(1);
    expect(mainSource.match(/installRuntimeDaemonSignalShutdown\(\{/g)).toHaveLength(1);
    expect(mainSource).toContain("void shutdown(1, 'initialize-failed');");
    expect(mainSource).toContain("void shutdown(0, 'before-quit');");
    expect(mainSource).toContain("void shutdown(0, 'retire-after-gui-spawn');");
  });

  it('keeps bootstrap token custody in host and server process environments', () => {
    expect(mainSource).toContain(
      "import { resolveHostedBootstrapTokenFile } from '@chirality/runtime-daemon/hosted-paths';"
    );
    expect(mainSource).not.toContain('CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE');
    expect(mainSource).toContain('tokenFile: control.bootstrapTokenFile');

    const initializeGui = mainSource.slice(
      mainSource.indexOf('async function initializeGui(): Promise<void> {'),
      mainSource.indexOf('async function initializeDaemon(): Promise<void> {')
    );
    expect(initializeGui).toContain(
      'process.env.CHIRALITY_RUNTIME_DIRECTORY = control.runtimeDirectory;'
    );
    expect(initializeGui).toContain(
      'process.env.CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE = control.bootstrapTokenFile;'
    );
    expect(initializeGui.indexOf('CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE')).toBeLessThan(
      initializeGui.indexOf('startPackagedRendererServer()')
    );

    const initializeDaemon = mainSource.slice(
      mainSource.indexOf('async function initializeDaemon(): Promise<void> {'),
      mainSource.indexOf('/**\n * Release everything this process owns')
    );
    expect(initializeDaemon).toContain(
      'process.env.CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE = runtimeHost.bootstrapTokenFile;'
    );
  });

  it('connects only explicit packaged private configuration to the hosted Runtime entry', () => {
    const initializeGui = mainSource.slice(
      mainSource.indexOf('async function initializeGui(): Promise<void> {'),
      mainSource.indexOf('async function initializeDaemon(): Promise<void> {')
    );
    const initializeDaemon = mainSource.slice(
      mainSource.indexOf('async function initializeDaemon(): Promise<void> {'),
      mainSource.indexOf('/**\n * Release everything this process owns')
    );
    expect(initializeGui).not.toContain('CHIRALITY_HOSTED_PRIVATE_CONFIG_FILE');
    expect(initializeDaemon).toContain(
      'process.env.CHIRALITY_HOSTED_PRIVATE_CONFIG_FILE;'
    );
    expect(initializeDaemon).toContain('hostedPrivateConfigFile !== undefined');
    expect(initializeDaemon).not.toContain('CHIRALITY_HOSTED_PRIVATE_CONFIG_FILE?.trim()');
    expect(initializeDaemon).toContain('configuredPackagedRuntimeBootInput({');
    expect(initializeDaemon).toContain('resourcesRoot: process.resourcesPath');
    expect(initializeDaemon).toContain(
      'Hosted private configuration is unavailable in development until a reviewed source-tree artifact basis is provided.'
    );
  });

  it('prevents binder-first native quit until the owned final exit', () => {
    expect(
      shouldPreventNativeQuit({
        shutdownStarted: true,
        shutdownCompleted: false,
        hasOwnedResources: true
      })
    ).toBe(true);

    expect(
      shouldPreventNativeQuit({
        shutdownStarted: true,
        shutdownCompleted: false,
        hasOwnedResources: false
      })
    ).toBe(true);

    expect(
      shouldPreventNativeQuit({
        shutdownStarted: true,
        shutdownCompleted: true,
        hasOwnedResources: false
      })
    ).toBe(false);
  });

  it('allows an idle native quit when the process owns no runtime resources', () => {
    expect(
      shouldPreventNativeQuit({
        shutdownStarted: false,
        shutdownCompleted: false,
        hasOwnedResources: false
      })
    ).toBe(false);
  });
});
