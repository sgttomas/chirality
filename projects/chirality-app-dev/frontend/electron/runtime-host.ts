import type { RuntimeConformanceArtifactInventorySelection } from '@chirality/runtime-core';
import path from 'node:path';
import {
  readHostedPrivateBootstrapConfiguration,
  startHostedPrivateBootstrapRuntimeHost,
  type HostedBootstrapRuntimeHost,
  type HostedPrivateBootstrapConfigurationReadInput,
  type HostedPrivateBootstrapHostInput
} from '@chirality/runtime-daemon/hosted';

export const MACOS_UNIX_SOCKET_PATH_MAX_BYTES = 103;

export type RuntimeHost = HostedBootstrapRuntimeHost;
type DesktopRuntimeBootstrap = {
  runtimeDirectory: string;
  daemonSocket: 'control.sock';
  instructionRoot: string;
};

type DesktopHostedPrivateBootInput = DesktopRuntimeBootstrap & {
  hostedPrivateConfigFile: string;
  supplierExecutablePath: string;
  nativeAddonPath: string;
  artifactInventory: RuntimeConformanceArtifactInventorySelection;
};

export type DesktopRuntimeBootInput =
  | DesktopRuntimeBootstrap
  | DesktopHostedPrivateBootInput;

type RuntimeHostEntry = {
  readConfiguration(
    input: HostedPrivateBootstrapConfigurationReadInput
  ): Promise<HostedPrivateBootstrapHostInput>;
  startHost(input: HostedPrivateBootstrapHostInput): Promise<RuntimeHost>;
};

const productionEntry: RuntimeHostEntry = Object.freeze({
  readConfiguration: readHostedPrivateBootstrapConfiguration,
  startHost: startHostedPrivateBootstrapRuntimeHost
});

export function assertRuntimeSocketPathSupported(
  socketPath: string,
  platform: NodeJS.Platform = process.platform
): { measuredBytes: number; maximumBytes: number } {
  const measuredBytes = Buffer.byteLength(socketPath, 'utf8');
  if (platform === 'darwin' && measuredBytes > MACOS_UNIX_SOCKET_PATH_MAX_BYTES) {
    throw new Error(
      `Runtime control socket path is ${measuredBytes} UTF-8 bytes; macOS maximum is ${MACOS_UNIX_SOCKET_PATH_MAX_BYTES} bytes`
    );
  }
  return { measuredBytes, maximumBytes: MACOS_UNIX_SOCKET_PATH_MAX_BYTES };
}

async function connectRuntimeHost(
  input: DesktopRuntimeBootInput,
  entry: RuntimeHostEntry
): Promise<RuntimeHost> {
  assertRuntimeSocketPathSupported(path.join(input.runtimeDirectory, input.daemonSocket));
  const bootstrap = {
    enabled: true as const,
    runtimeDirectory: input.runtimeDirectory,
    daemonSocket: input.daemonSocket,
    instructionRoot: input.instructionRoot
  };
  if (!('hostedPrivateConfigFile' in input)) {
    return entry.startHost({ bootstrap });
  }
  const configuredBootstrap = {
    ...bootstrap,
    nativeAddonPath: input.nativeAddonPath,
    artifactInventory: input.artifactInventory
  };
  const configuration = await entry.readConfiguration({
    configFile: input.hostedPrivateConfigFile,
    bootstrap: configuredBootstrap,
    packaged: {
      supplierExecutablePath: input.supplierExecutablePath,
      nativeAddonPath: input.nativeAddonPath,
      instructionRoot: input.instructionRoot,
      artifactInventory: input.artifactInventory
    }
  });
  return entry.startHost(configuration);
}

export function configuredPackagedRuntimeBootInput(input: DesktopRuntimeBootstrap & {
  configFile: string;
  resourcesRoot: string;
}): DesktopHostedPrivateBootInput {
  const resourcesRoot = path.resolve(input.resourcesRoot);
  const instructionRoot = path.join(resourcesRoot, 'instruction-root');
  return {
    runtimeDirectory: input.runtimeDirectory,
    daemonSocket: input.daemonSocket,
    instructionRoot,
    hostedPrivateConfigFile: input.configFile,
    supplierExecutablePath: path.join(resourcesRoot, 'supplier', 'codex'),
    nativeAddonPath: path.join(resourcesRoot, 'native', 'chirality_native_admission.node'),
    artifactInventory: {
      kind: 'packaged-resources',
      resourcesRoot,
      manifestPath: path.join(resourcesRoot, 'runtime-artifact-inventory.json')
    }
  };
}

/** Read the owner-private carrier, then start Runtime's hosted bootstrap composition. */
export function startRuntimeHost(input: DesktopRuntimeBootInput): Promise<RuntimeHost> {
  return connectRuntimeHost(input, productionEntry);
}

/** Native-free seam for checking the App-to-Runtime production input mapping. */
export function startControlledRuntimeHostForTests(
  input: DesktopRuntimeBootInput,
  entry: RuntimeHostEntry
): Promise<RuntimeHost> {
  return connectRuntimeHost(input, entry);
}
