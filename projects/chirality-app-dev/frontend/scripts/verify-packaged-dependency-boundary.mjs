import { access, lstat, mkdtemp, readFile, realpath, rm } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { tmpdir } from 'node:os';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const ELECTRON_OUTPUT_DIRECTORY_ENV = 'CHIRALITY_ELECTRON_OUTPUT_DIRECTORY';
export function resolvePackagedDependencyBundlePath(env = process.env) {
  let outputDirectory = path.join(frontendRoot, 'dist');
  if (Object.prototype.hasOwnProperty.call(env, ELECTRON_OUTPUT_DIRECTORY_ENV)) {
    const candidate = env[ELECTRON_OUTPUT_DIRECTORY_ENV];
    if (typeof candidate !== 'string' || candidate.length === 0 || candidate.includes('\0')
      || !path.isAbsolute(candidate) || path.normalize(candidate) !== candidate) {
      throw new Error(`${ELECTRON_OUTPUT_DIRECTORY_ENV} must be a normalized absolute path`);
    }
    outputDirectory = candidate;
  }
  return path.join(outputDirectory, 'mac-arm64', 'Chirality.app', 'Contents', 'Resources', 'app.asar');
}
const bundlePath = path.resolve(
  process.argv[2] ?? resolvePackagedDependencyBundlePath()
);
const asarCli = path.join(frontendRoot, 'node_modules', '.bin', 'asar');
const resourcesRoot = path.dirname(bundlePath);
const packagedCliPath = path.join(resourcesRoot, 'runtime-cli', 'chirality-cli.mjs');
const packagedCliSourceMapPath = `${packagedCliPath}.map`;
const nativeAdmissionAssetName = 'chirality_native_admission.node';

const requiredPackages = ['next'];
const forbiddenLegacyRuntimePackages = [
  '@anthropic-ai/claude-agent-sdk',
  '@anthropic-ai/sdk',
  '@earendil-works/pi-agent-core',
  '@earendil-works/pi-ai',
  '@earendil-works/pi-coding-agent',
  '@earendil-works/pi-tui'
];
const claudePlatformPackagePattern =
  /(?:^|\/)node_modules\/(@anthropic-ai\/claude-agent-sdk-[^/]+)(?:\/|$)/;
const forbiddenDevelopmentPackages = [
  'concurrently',
  'electron-builder',
  'esbuild',
  'shell-quote',
  'typescript',
  'vite',
  'vitest',
  'wait-on'
];

function containsPackage(entry, packageName) {
  const marker = `/node_modules/${packageName}`;
  return entry === marker || entry.startsWith(`${marker}/`) || entry.includes(`${marker}/`);
}

export function findForbiddenLegacyRuntimePackage(entry) {
  for (const packageName of forbiddenLegacyRuntimePackages) {
    if (containsPackage(entry, packageName)) return packageName;
  }
  return normalizeSourcePath(entry).match(claudePlatformPackagePattern)?.[1] ?? null;
}

function normalizeSourcePath(source) {
  return source.replaceAll('\\', '/');
}

function hasSource(sources, suffix) {
  const normalizedSuffix = normalizeSourcePath(suffix);
  return sources.some((source) => normalizeSourcePath(source).endsWith(normalizedSuffix));
}

export async function verifyPackagedNativeAdmissionAsset({ resourcesRoot: candidateRoot }) {
  const failures = [];
  const fallbackPath =
    typeof candidateRoot === 'string'
      ? path.join(path.resolve(candidateRoot), 'native', nativeAdmissionAssetName)
      : null;
  if (
    typeof candidateRoot !== 'string' ||
    candidateRoot.length === 0 ||
    candidateRoot.includes('\0') ||
    !path.isAbsolute(candidateRoot) ||
    path.normalize(candidateRoot) !== candidateRoot
  ) {
    return {
      status: 'FAIL',
      path: fallbackPath,
      canonicalResourcesRoot: null,
      failures: ['Resources root must be a normalized absolute path']
    };
  }

  let canonicalResourcesRoot;
  try {
    canonicalResourcesRoot = await realpath(candidateRoot);
  } catch (error) {
    return {
      status: 'FAIL',
      path: fallbackPath,
      canonicalResourcesRoot: null,
      failures: [`Unable to resolve packaged Resources root: ${error.message}`]
    };
  }

  const nativeDirectory = path.join(canonicalResourcesRoot, 'native');
  const assetPath = path.join(nativeDirectory, nativeAdmissionAssetName);
  try {
    const directoryStat = await lstat(nativeDirectory);
    if (!directoryStat.isDirectory() || directoryStat.isSymbolicLink()) {
      failures.push('Packaged native directory must be a regular non-symlink directory');
    } else if ((await realpath(nativeDirectory)) !== nativeDirectory) {
      failures.push('Packaged native directory resolves outside its exact Resources path');
    }
  } catch (error) {
    failures.push(`Unable to inspect packaged native directory: ${error.message}`);
  }

  try {
    const assetStat = await lstat(assetPath);
    if (!assetStat.isFile() || assetStat.isSymbolicLink()) {
      failures.push('Packaged native-admission asset must be a regular non-symlink file');
    } else if ((await realpath(assetPath)) !== assetPath) {
      failures.push('Packaged native-admission asset resolves outside its exact Resources path');
    } else {
      await readFile(assetPath);
    }
  } catch (error) {
    failures.push(`Unable to read packaged native-admission asset: ${error.message}`);
  }

  return {
    status: failures.length === 0 ? 'PASS' : 'FAIL',
    path: assetPath,
    canonicalResourcesRoot,
    failures
  };
}

export function verifyPackagedRuntimeSources({
  desktopSources,
  cliSources,
  packagedEntries
}) {
  const requiredDesktopSources = [
    'electron/main.ts',
    'electron/runtime-host.ts',
    'chirality-runtime/packages/client/src/client.ts',
    'chirality-runtime/packages/daemon/src/runtime-daemon.ts',
    'chirality-runtime/packages/daemon/src/hosted-bootstrap.ts',
    'chirality-runtime/packages/daemon/src/hosted-paths.ts'
  ];
  const requiredCodexDesktopSources = [
    'chirality-runtime/packages/daemon/src/hosted-boot.ts',
    'chirality-runtime/packages/daemon/src/hosted-standalone.ts',
    'chirality-runtime/packages/daemon/src/hosted-private-composition.ts',
    'chirality-runtime/packages/daemon/src/hosted-private-entry.ts',
    'chirality-runtime/packages/daemon/src/codex-admitted-launcher.ts',
    'chirality-runtime/packages/daemon/src/codex-authenticated-transport.ts',
    'chirality-runtime/packages/daemon/src/codex-supervisor.ts',
    'chirality-runtime/packages/core/src/delegated-engine-adapter.ts',
    'chirality-runtime/packages/native-admission/src/index.ts'
  ];
  const forbiddenLegacyDesktopSources = [
    'electron/runtime-host-legacy.ts',
    'src/lib/harness/anthropic-agent-sdk-manager.ts',
    'src/lib/harness/claude-agent-sdk-manager.ts',
    'src/lib/harness/pi-agent-engine-adapter.ts',
    'chirality-runtime/packages/engine-claude/src/index.ts',
    'chirality-runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts'
  ];
  const requiredCliSources = [
    'chirality-runtime/packages/cli/src/bin.ts',
    'chirality-runtime/packages/cli/src/cli.ts',
    'chirality-runtime/packages/client/src/client.ts'
  ];
  const forbiddenCliSources = [
    // Reject stale pre-migration server sources as well as the current project.
    'runtime/packages/daemon/src/runtime-daemon.ts',
    'runtime/packages/engine-claude/src/index.ts',
    'runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts',
    'chirality-runtime/packages/daemon/src/runtime-daemon.ts',
    'chirality-runtime/packages/engine-claude/src/index.ts',
    'chirality-runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts',
    'electron/runtime-host.ts'
  ];
  const requiredPackagedEntries = ['/dist-electron/main.js', '/dist-electron/main.js.map'];
  const failures = [];

  for (const suffix of requiredDesktopSources) {
    if (!hasSource(desktopSources, suffix)) {
      failures.push(`desktop bundle is missing source ${suffix}`);
    }
  }
  for (const suffix of requiredCodexDesktopSources) {
    if (!hasSource(desktopSources, suffix)) {
      failures.push(`desktop bundle is missing Codex production source ${suffix}`);
    }
  }
  for (const suffix of forbiddenLegacyDesktopSources) {
    if (hasSource(desktopSources, suffix)) {
      failures.push(`Codex-only desktop bundle unexpectedly embeds legacy engine source ${suffix}`);
    }
  }
  for (const suffix of requiredCliSources) {
    if (!hasSource(cliSources, suffix)) {
      failures.push(`CLI bundle is missing source ${suffix}`);
    }
  }
  for (const suffix of forbiddenCliSources) {
    if (hasSource(cliSources, suffix)) {
      failures.push(`CLI client bundle unexpectedly embeds server source ${suffix}`);
    }
  }
  for (const entry of requiredPackagedEntries) {
    if (!packagedEntries.has(entry)) {
      failures.push(`app.asar is missing ${entry}`);
    }
  }

  return {
    failures,
    requiredDesktopSources,
    requiredCodexDesktopSources,
    forbiddenLegacyDesktopSources,
    requiredCliSources,
    forbiddenCliSources,
    requiredPackagedEntries
  };
}

function parseSourceMapSources(sourceMap, sourceMapPath) {
  const parsed = JSON.parse(sourceMap);
  if (!Array.isArray(parsed.sources) || !parsed.sources.every((source) => typeof source === 'string')) {
    throw new Error(`Invalid source map sources: ${sourceMapPath}`);
  }
  return parsed.sources;
}

async function extractPackagedFile(entry) {
  const extractionRoot = await mkdtemp(path.join(tmpdir(), 'chirality-asar-extract-'));
  try {
    const child = spawn(asarCli, ['extract-file', bundlePath, entry], {
      cwd: extractionRoot,
      stdio: ['ignore', 'ignore', 'inherit']
    });
    const exitCode = await new Promise((resolve, reject) => {
      child.once('error', reject);
      child.once('close', (code) => resolve(code ?? 1));
    });
    if (exitCode !== 0) {
      throw new Error(`asar extract-file exited with status ${exitCode}`);
    }
    return readFile(path.join(extractionRoot, path.basename(entry)), 'utf8');
  } finally {
    await rm(extractionRoot, { recursive: true, force: true });
  }
}

async function inspectBundle() {
  await access(bundlePath);
  await access(asarCli);
  await access(packagedCliPath);
  await access(packagedCliSourceMapPath);
  const nativeAdmissionAsset = await verifyPackagedNativeAdmissionAsset({ resourcesRoot });

  const requiredPresent = new Set();
  const forbiddenPresent = new Set();
  const forbiddenLegacyRuntimePresent = new Set();
  let localPackageEntries = 0;
  const packagedEntries = new Set();

  const child = spawn(asarCli, ['list', bundlePath], {
    cwd: frontendRoot,
    stdio: ['ignore', 'pipe', 'inherit']
  });
  const lines = readline.createInterface({ input: child.stdout });

  for await (const entry of lines) {
    packagedEntries.add(normalizeSourcePath(entry));
    if (entry.includes('/node_modules/@chirality/')) {
      localPackageEntries += 1;
    }
    for (const packageName of requiredPackages) {
      if (containsPackage(entry, packageName)) {
        requiredPresent.add(packageName);
      }
    }
    for (const packageName of forbiddenDevelopmentPackages) {
      if (containsPackage(entry, packageName)) {
        forbiddenPresent.add(packageName);
      }
    }
    const forbiddenLegacyPackage = findForbiddenLegacyRuntimePackage(entry);
    if (forbiddenLegacyPackage) forbiddenLegacyRuntimePresent.add(forbiddenLegacyPackage);
  }

  const exitCode = await new Promise((resolve, reject) => {
    child.once('error', reject);
    child.once('close', (code) => resolve(code ?? 1));
  });
  if (exitCode !== 0) {
    throw new Error(`asar list exited with status ${exitCode}`);
  }

  const missingRequired = requiredPackages.filter(
    (packageName) => !requiredPresent.has(packageName)
  );
  const failures = [];
  failures.push(...nativeAdmissionAsset.failures);
  if (localPackageEntries > 0) {
    failures.push(`found ${localPackageEntries} monorepo-only @chirality package entries`);
  }
  if (forbiddenPresent.size > 0) {
    failures.push(
      `found development-only packages: ${[...forbiddenPresent].sort().join(', ')}`
    );
  }
  if (forbiddenLegacyRuntimePresent.size > 0) {
    failures.push(
      `found legacy runtime packages in Codex-only artifact: ${[...forbiddenLegacyRuntimePresent].sort().join(', ')}`
    );
  }
  if (missingRequired.length > 0) {
    failures.push(`missing runtime packages: ${missingRequired.join(', ')}`);
  }
  const desktopSources = parseSourceMapSources(
    await extractPackagedFile('dist-electron/main.js.map'),
    `${bundlePath}:dist-electron/main.js.map`
  );
  const cliSources = parseSourceMapSources(
    await readFile(packagedCliSourceMapPath, 'utf8'),
    packagedCliSourceMapPath
  );
  const runtimeSourceProof = verifyPackagedRuntimeSources({
    desktopSources,
    cliSources,
    packagedEntries
  });
  failures.push(...runtimeSourceProof.failures);

  const summary = {
    status: failures.length === 0 ? 'PASS' : 'FAIL',
    bundlePath,
    localPackageEntries,
    forbiddenDevelopmentPackagesPresent: [...forbiddenPresent].sort(),
    forbiddenLegacyRuntimePackagesPresent: [...forbiddenLegacyRuntimePresent].sort(),
    runtimeProfile: 'codex-only',
    nativeAdmissionAsset,
    requiredPackagesPresent: [...requiredPresent].sort(),
    packagedRuntimeSourceProof: {
      status: runtimeSourceProof.failures.length === 0 ? 'PASS' : 'FAIL',
      desktopSourceCount: desktopSources.length,
      cliSourceCount: cliSources.length,
      requiredDesktopSources: runtimeSourceProof.requiredDesktopSources,
      requiredCodexDesktopSources: runtimeSourceProof.requiredCodexDesktopSources,
      requiredCliSources: runtimeSourceProof.requiredCliSources
    },
    failures
  };
  console.log(JSON.stringify(summary, null, 2));

  if (failures.length > 0) {
    throw new Error(failures.join('; '));
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await inspectBundle();
}
