import { access } from 'node:fs/promises';
import { spawn } from 'node:child_process';
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

async function inspectBundle() {
  await access(bundlePath);
  await access(asarCli);

  const requiredPresent = new Set();
  const forbiddenPresent = new Set();
  let localPackageEntries = 0;

  const child = spawn(asarCli, ['list', bundlePath], {
    cwd: frontendRoot,
    stdio: ['ignore', 'pipe', 'inherit']
  });
  const lines = readline.createInterface({ input: child.stdout });

  for await (const entry of lines) {
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

  const summary = {
    status: failures.length === 0 ? 'PASS' : 'FAIL',
    bundlePath,
    localPackageEntries,
    forbiddenDevelopmentPackagesPresent: [...forbiddenPresent].sort(),
    requiredPackagesPresent: [...requiredPresent].sort(),
    failures
  };
  console.log(JSON.stringify(summary, null, 2));

  if (failures.length > 0) {
    throw new Error(failures.join('; '));
  }
}

await inspectBundle();
