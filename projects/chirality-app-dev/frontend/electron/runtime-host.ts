import type { RuntimeConformanceArtifactInventorySelection } from '@chirality/runtime-core';
import path from 'node:path';
import {
  loadPackagedHostedReleaseBasis,
  readHostedPrivateBootstrapConfiguration,
  startHostedBootstrapRuntimeHost,
  startHostedPackagedPrivateBootstrapRuntimeHost,
  startHostedPrivateBootstrapRuntimeHost,
  type EmbeddedRuntimeVersionsV2,
  type HostedBootstrapRuntimeHost,
  type HostedPackagedReleaseLoadResult,
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

export type DesktopPackagedRuntimeBootInput = {
  runtimeDirectory: string;
  daemonSocket: 'control.sock';
  resourcesRoot: string;
  embeddedRuntime: EmbeddedRuntimeVersionsV2;
};

export type DesktopRuntimeBootInput =
  | DesktopRuntimeBootstrap
  | DesktopHostedPrivateBootInput
  | DesktopPackagedRuntimeBootInput;

type RuntimeHostEntry = {
  readConfiguration(
    input: HostedPrivateBootstrapConfigurationReadInput
  ): Promise<HostedPrivateBootstrapHostInput>;
  startHost(input: HostedPrivateBootstrapHostInput): Promise<RuntimeHost>;
};

type PackagedRuntimeHostEntry = {
  loadReleaseBasis(input: {
    resourcesRoot: string;
    runtimeDirectory: string;
    embeddedRuntime: EmbeddedRuntimeVersionsV2;
  }): Promise<HostedPackagedReleaseLoadResult>;
  startPackagedHost(
    input: Parameters<typeof startHostedPackagedPrivateBootstrapRuntimeHost>[0]
  ): Promise<RuntimeHost>;
  startUnboundHost(
    input: Parameters<typeof startHostedBootstrapRuntimeHost>[0]
  ): Promise<RuntimeHost>;
};

const productionEntry: RuntimeHostEntry = Object.freeze({
  readConfiguration: readHostedPrivateBootstrapConfiguration,
  startHost: startHostedPrivateBootstrapRuntimeHost
});

const packagedProductionEntry: PackagedRuntimeHostEntry = Object.freeze({
  loadReleaseBasis: loadPackagedHostedReleaseBasis,
  startPackagedHost: startHostedPackagedPrivateBootstrapRuntimeHost,
  startUnboundHost: startHostedBootstrapRuntimeHost
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
  input: DesktopRuntimeBootstrap | DesktopHostedPrivateBootInput,
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

async function connectPackagedRuntimeHost(
  input: DesktopPackagedRuntimeBootInput,
  entry: PackagedRuntimeHostEntry
): Promise<RuntimeHost> {
  assertRuntimeSocketPathSupported(path.join(input.runtimeDirectory, input.daemonSocket));
  const release = await entry.loadReleaseBasis({
    resourcesRoot: input.resourcesRoot,
    runtimeDirectory: input.runtimeDirectory,
    embeddedRuntime: input.embeddedRuntime
  });
  if (release.status === 'ready') {
    return entry.startPackagedHost({
      bootstrap: {
        enabled: true,
        runtimeDirectory: input.runtimeDirectory,
        daemonSocket: input.daemonSocket,
        instructionRoot: release.basis.instructionRoot,
        nativeAddonPath: release.basis.nativeAddonPath
      },
      basis: release.basis
    });
  }
  // All loader failures have the same Desktop behavior and disclosure: the
  // setup/bootstrap daemon remains usable, while private hosted work remains
  // unavailable. Runtime owns the detailed reason and never supplies a basis.
  return entry.startUnboundHost({
    enabled: true,
    runtimeDirectory: input.runtimeDirectory,
    daemonSocket: input.daemonSocket,
    instructionRoot: path.join(input.resourcesRoot, 'instruction-root')
  });
}

export function packagedRuntimeBootInput(input: {
  runtimeDirectory: string;
  daemonSocket: 'control.sock';
  resourcesRoot: string;
  embeddedRuntime: EmbeddedRuntimeVersionsV2;
}): DesktopPackagedRuntimeBootInput {
  return {
    runtimeDirectory: input.runtimeDirectory,
    daemonSocket: input.daemonSocket,
    resourcesRoot: path.resolve(input.resourcesRoot),
    embeddedRuntime: { ...input.embeddedRuntime }
  };
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
  if ('embeddedRuntime' in input) {
    return connectPackagedRuntimeHost(input, packagedProductionEntry);
  }
  return connectRuntimeHost(input, productionEntry);
}

/** Native-free seam for checking the App-to-Runtime production input mapping. */
export function startControlledRuntimeHostForTests(
  input: DesktopRuntimeBootstrap | DesktopHostedPrivateBootInput,
  entry: RuntimeHostEntry
): Promise<RuntimeHost> {
  return connectRuntimeHost(input, entry);
}


/** Native-free adapter seam for checking Desktop's packaged input and fallback mapping. */
export function startControlledPackagedRuntimeHostForTests(
  input: DesktopPackagedRuntimeBootInput,
  entry: PackagedRuntimeHostEntry
): Promise<RuntimeHost> {
  return connectPackagedRuntimeHost(input, entry);
}
