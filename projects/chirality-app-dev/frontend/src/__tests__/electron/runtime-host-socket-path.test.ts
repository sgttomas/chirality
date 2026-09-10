import path from 'node:path';
import { mkdtemp, rm, writeFile } from 'node:fs/promises';
import { describe, expect, it, vi } from 'vitest';
import {
  readHostedPrivateBootstrapConfiguration,
  startControlledHostedPrivateBootstrapRuntimeHostForTests
} from '@chirality/runtime-daemon/hosted';

import {
  MACOS_UNIX_SOCKET_PATH_MAX_BYTES,
  assertRuntimeSocketPathSupported,
  configuredPackagedRuntimeBootInput,
  startControlledRuntimeHostForTests
} from '../../../electron/runtime-host';

const inventory = {
  kind: 'packaged-resources' as const,
  resourcesRoot: '/Applications/Chirality.app/Contents/Resources',
  manifestPath: '/Applications/Chirality.app/Contents/Resources/runtime-artifact-inventory.json'
};

const input = {
  runtimeDirectory: '/runtime',
  daemonSocket: 'control.sock' as const,
  instructionRoot: '/Applications/Chirality.app/Contents/Resources/instruction-root',
  supplierExecutablePath: '/Applications/Chirality.app/Contents/Resources/supplier/codex',
  nativeAddonPath: '/Applications/Chirality.app/Contents/Resources/native/chirality_native_admission.node',
  artifactInventory: inventory
};

const host = {
  socketPath: '/runtime/control.sock',
  runtimeDirectory: '/runtime',
  bootstrapTokenFile: '/runtime/auth/tokens/hosted-bootstrap-host.token',
  stop: vi.fn(async () => {})
};

function privateConfiguration(supplierExecutablePath = input.supplierExecutablePath) {
  return {
    schema: 'chirality.hosted-private-runtime/v1',
    privateComposition: {
      runtimeDirectory: input.runtimeDirectory,
      supplierExecutablePath,
      nativeAddonPath: input.nativeAddonPath,
      instructionRoot: input.instructionRoot,
      model: 'gpt-test',
      managedAuth: {
        backend: 'keyring',
        binding: {
          schema: 'chirality-hosted-account-binding/v1',
          state: 'unavailable',
          reason: 'canonical-identity-producer-unavailable'
        }
      },
      compatibility: {
        compatibilityIdentity: 'root-runtime-1',
        contractBasisSha256: 'a'.repeat(64)
      },
      conformance: {
        recordPath: '/accept/record',
        acceptancePath: '/accept/acceptance',
        ownerActPath: '/accept/owner',
        ownerActSha256: 'b'.repeat(64),
        activationId: 'activation',
        gateIdentity: 'G4',
        artifactInventory: inventory
      },
      loginPurposeRelease: {
        recordPath: '/accept/login-record',
        acceptancePath: '/accept/login-acceptance',
        ownerActPath: '/accept/login-owner',
        ownerActSha256: 'd'.repeat(64),
        activationId: 'login-activation',
        gateIdentity: 'D36',
        artifactInventory: inventory
      },
      configDigest: 'c'.repeat(64),
      consentVersion: 'consent-v1',
      commandNetworkPosture: 'off',
      commandNetworkConsent: {
        approvedBy: 'owner',
        approvedAt: '2026-09-10T00:00:00.000Z',
        explicitUserAct: true
      },
      protectedPaths: ['/runtime'],
      immutableReadRoots: ['/usr']
    }
  };
}

function pathWithBytes(targetBytes: number, unicode = false): string {
  const prefix = '/tmp/';
  const remaining = targetBytes - Buffer.byteLength(prefix, 'utf8');
  const tail = unicode ? `${'a'.repeat(remaining - 2)}é` : 'a'.repeat(remaining);
  const value = `${prefix}${tail}`;
  expect(Buffer.byteLength(value, 'utf8')).toBe(targetBytes);
  return value;
}

describe('runtime-host macOS socket-path boundary', () => {
  it('accepts 103 bytes, rejects 104 bytes, and counts UTF-8 bytes', () => {
    expect(
      assertRuntimeSocketPathSupported(
        pathWithBytes(MACOS_UNIX_SOCKET_PATH_MAX_BYTES),
        'darwin'
      )
    ).toEqual({ measuredBytes: 103, maximumBytes: 103 });
    for (const socketPath of [pathWithBytes(104), pathWithBytes(104, true)]) {
      expect(() => assertRuntimeSocketPathSupported(socketPath, 'darwin')).toThrow(
        'Runtime control socket path is 104 UTF-8 bytes; macOS maximum is 103 bytes'
      );
    }
    expect(() => assertRuntimeSocketPathSupported(pathWithBytes(104), 'linux')).not.toThrow();
  });

  it('rejects an oversized macOS control socket before reading configuration or starting Runtime', async () => {
    const readConfiguration = vi.fn();
    const startHost = vi.fn();
    const platform = vi.spyOn(process, 'platform', 'get').mockReturnValue('darwin');
    try {
      await expect(startControlledRuntimeHostForTests({
        runtimeDirectory: `/tmp/${'x'.repeat(100)}`,
        daemonSocket: 'control.sock',
        instructionRoot: '/instructions'
      }, { readConfiguration, startHost })).rejects.toThrow('macOS maximum is 103 bytes');
      expect(readConfiguration).not.toHaveBeenCalled();
      expect(startHost).not.toHaveBeenCalled();
    } finally {
      platform.mockRestore();
    }
  });

  it('maps the packaged resource basis to the fixed supplier, native, and inventory paths', () => {
    expect(configuredPackagedRuntimeBootInput({
      runtimeDirectory: '/runtime',
      daemonSocket: 'control.sock',
      instructionRoot: '/registered/project/instructions',
      configFile: '/private/config/hosted.json',
      resourcesRoot: inventory.resourcesRoot
    })).toEqual({
      ...input,
      hostedPrivateConfigFile: '/private/config/hosted.json'
    });
  });

  it('starts an unbound bootstrap without selecting native or supplier composition', async () => {
    const createBindings = vi.fn();
    const startHost = vi.fn(async () => host);
    await startControlledRuntimeHostForTests(input, {
      readConfiguration: readHostedPrivateBootstrapConfiguration,
      startHost: (configuration) => startControlledHostedPrivateBootstrapRuntimeHostForTests(
        configuration,
        { createBindings, startHost }
      )
    });
    expect(createBindings).not.toHaveBeenCalled();
    expect(startHost).toHaveBeenCalledWith({
      enabled: true,
      runtimeDirectory: '/runtime',
      daemonSocket: 'control.sock',
      instructionRoot: input.instructionRoot
    });
  });

  it('passes a matching strict carrier through the real Runtime reader and private entry', async () => {
    const directory = await mkdtemp('/private/tmp/app-private-runtime-');
    try {
      const configFile = path.join(directory, 'hosted.json');
      await writeFile(configFile, JSON.stringify(privateConfiguration()), { mode: 0o600 });
      const bindings = { createCeremony: vi.fn() };
      const createBindings = vi.fn(async () => bindings);
      const startHost = vi.fn(async () => host);
      await startControlledRuntimeHostForTests(
        { ...input, hostedPrivateConfigFile: configFile },
        {
          readConfiguration: readHostedPrivateBootstrapConfiguration,
          startHost: (configuration) => startControlledHostedPrivateBootstrapRuntimeHostForTests(
            configuration,
            { createBindings, startHost }
          )
        }
      );
      expect(createBindings).toHaveBeenCalledWith(expect.objectContaining({
        supplierExecutablePath: input.supplierExecutablePath,
        nativeAddonPath: input.nativeAddonPath
      }));
      expect(startHost).toHaveBeenCalledWith(expect.objectContaining({
        nativeAddonPath: input.nativeAddonPath,
        artifactInventory: inventory
      }), bindings);
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  });

  it('does not start a host when the real Runtime reader rejects a mismatched carrier', async () => {
    const directory = await mkdtemp('/private/tmp/app-private-runtime-');
    try {
      const configFile = path.join(directory, 'hosted.json');
      await writeFile(configFile, JSON.stringify(privateConfiguration('/wrong/supplier')), {
        mode: 0o600
      });
      const startHost = vi.fn(async () => host);
      await expect(startControlledRuntimeHostForTests(
        { ...input, hostedPrivateConfigFile: configFile },
        { readConfiguration: readHostedPrivateBootstrapConfiguration, startHost }
      )).rejects.toMatchObject({ code: 'ENGINE_UNAVAILABLE' });
      expect(startHost).not.toHaveBeenCalled();
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  });

  it.each(['', '   ', ' /private/config/hosted.json '])(
    'passes an explicitly present invalid carrier %j to Runtime without starting the host',
    async (hostedPrivateConfigFile) => {
      const startHost = vi.fn(async () => host);
      await expect(startControlledRuntimeHostForTests(
        { ...input, hostedPrivateConfigFile },
        { readConfiguration: readHostedPrivateBootstrapConfiguration, startHost }
      )).rejects.toMatchObject({ code: 'ENGINE_UNAVAILABLE' });
      expect(startHost).not.toHaveBeenCalled();
    }
  );
});
