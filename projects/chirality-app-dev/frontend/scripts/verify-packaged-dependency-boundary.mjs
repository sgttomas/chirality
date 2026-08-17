import { access, mkdtemp, readFile, rm } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { tmpdir } from 'node:os';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const bundlePath = path.resolve(
  process.argv[2] ??
    path.join(
      frontendRoot,
      'dist',
      'mac-arm64',
      'Chirality.app',
      'Contents',
      'Resources',
      'app.asar'
    )
);
const asarCli = path.join(frontendRoot, 'node_modules', '.bin', 'asar');
const resourcesRoot = path.dirname(bundlePath);
const packagedCliPath = path.join(resourcesRoot, 'runtime-cli', 'chirality-cli.mjs');
const packagedCliSourceMapPath = `${packagedCliPath}.map`;

const requiredPackages = [
  '@anthropic-ai/claude-agent-sdk',
  '@earendil-works/pi-coding-agent',
  'next'
];
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

function normalizeSourcePath(source) {
  return source.replaceAll('\\', '/');
}

function hasSource(sources, suffix) {
  const normalizedSuffix = normalizeSourcePath(suffix);
  return sources.some((source) => normalizeSourcePath(source).endsWith(normalizedSuffix));
}

export function verifyPackagedRuntimeSources({
  desktopSources,
  cliSources,
  packagedEntries
}) {
  const requiredDesktopSources = [
    'electron/main.ts',
    'electron/runtime-host.ts',
    'runtime/packages/client/src/client.ts',
    'runtime/packages/daemon/src/runtime-daemon.ts',
    'runtime/packages/engine-claude/src/index.ts',
    'runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts'
  ];
  const requiredCliSources = [
    'runtime/packages/cli/src/bin.ts',
    'runtime/packages/cli/src/cli.ts',
    'runtime/packages/client/src/client.ts'
  ];
  const forbiddenCliSources = [
    'runtime/packages/daemon/src/runtime-daemon.ts',
    'runtime/packages/engine-claude/src/index.ts',
    'runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts',
    'electron/runtime-host.ts'
  ];
  const requiredPackagedEntries = ['/dist-electron/main.js', '/dist-electron/main.js.map'];
  const failures = [];

  for (const suffix of requiredDesktopSources) {
    if (!hasSource(desktopSources, suffix)) {
      failures.push(`desktop bundle is missing source ${suffix}`);
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

  const requiredPresent = new Set();
  const forbiddenPresent = new Set();
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
  if (localPackageEntries > 0) {
    failures.push(`found ${localPackageEntries} monorepo-only @chirality package entries`);
  }
  if (forbiddenPresent.size > 0) {
    failures.push(
      `found development-only packages: ${[...forbiddenPresent].sort().join(', ')}`
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
    requiredPackagesPresent: [...requiredPresent].sort(),
    packagedRuntimeSourceProof: {
      status: runtimeSourceProof.failures.length === 0 ? 'PASS' : 'FAIL',
      desktopSourceCount: desktopSources.length,
      cliSourceCount: cliSources.length,
      requiredDesktopSources: runtimeSourceProof.requiredDesktopSources,
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
