import { rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { build } from 'esbuild';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repositoryRoot = path.resolve(frontendRoot, '..', '..', '..');
const runtimeRoot = path.join(repositoryRoot, 'projects', 'chirality-runtime');
const outputRoot = path.join(frontendRoot, 'out', 'controlled-ci');

function contractSource(subpath = '') {
  if (!subpath) return path.join(runtimeRoot, 'packages', 'contracts', 'src', 'index.ts');
  if (subpath === 'v3') return path.join(runtimeRoot, 'packages', 'contracts', 'src', 'v3.ts');
  return path.join(runtimeRoot, 'packages', 'contracts', 'src', 'harness', `${subpath}.ts`);
}

const entries = {
  '@chirality/runtime-contracts': contractSource(),
  '@chirality/runtime-core': path.join(runtimeRoot, 'packages', 'core', 'src', 'index.ts'),
  '@chirality/runtime-daemon': path.join(runtimeRoot, 'packages', 'daemon', 'src', 'index.ts'),
  '@chirality/runtime-client': path.join(runtimeRoot, 'packages', 'client', 'src', 'index.ts'),
  '@chirality/runtime-cli': path.join(runtimeRoot, 'packages', 'cli', 'src', 'index.ts')
};

const runtimeSources = {
  name: 'chirality-controlled-ci-runtime-sources',
  setup(api) {
    api.onResolve({ filter: /^@chirality\/runtime-contracts(?:\/(.+))?$/ }, (args) => ({
      path: contractSource(args.path.slice('@chirality/runtime-contracts'.length + 1))
    }));
    for (const [name, source] of Object.entries(entries)) {
      if (name === '@chirality/runtime-contracts') continue;
      api.onResolve({ filter: new RegExp(`^${name.replaceAll('/', '\\/')}$`) }, (args) => ({
        path: name === '@chirality/runtime-daemon' && args.importer.endsWith('controlled-ci-runtime.ts')
          ? path.join(runtimeRoot, 'packages', 'daemon', 'src', 'runtime-daemon.ts')
          : source
      }));
    }
  }
};

const forbiddenControlledSources = [
  '/electron/main.ts',
  '/electron/runtime-host',
  '/engine-pi-omlx/',
  '/engine-claude/',
  '/hosted-private-',
  '/native-admission/',
  '/codex-'
];

function assertControlledGraph(metafile) {
  const sources = Object.keys(metafile.inputs).map((item) => item.replaceAll('\\', '/'));
  for (const fragment of forbiddenControlledSources) {
    if (sources.some((source) => source.includes(fragment))) {
      throw new Error(`Controlled CI graph includes forbidden production source fragment '${fragment}'.`);
    }
  }
  for (const required of ['scripts/controlled-ci-runtime.ts', 'daemon/src/runtime-daemon.ts', 'core/src/runtime-service.ts', 'src/lib/harness/agent-sdk-manager.ts']) {
    if (!sources.some((source) => source.includes(required))) {
      throw new Error(`Controlled CI graph is missing required source fragment '${required}'.`);
    }
  }
}

export async function buildControlledCiRuntime() {
  await rm(outputRoot, { recursive: true, force: true });
  const controlled = await build({
    entryPoints: [path.join(frontendRoot, 'scripts', 'controlled-ci-runtime.ts')],
    outfile: path.join(outputRoot, 'controlled-runtime.mjs'),
    bundle: true,
    platform: 'node',
    target: 'node24',
    format: 'esm',
    banner: { js: "import { createRequire as __controlledCreateRequire } from 'node:module'; const require = __controlledCreateRequire(import.meta.url);" },
    sourcemap: true,
    metafile: true,
    plugins: [runtimeSources],
    logLevel: 'silent'
  });
  assertControlledGraph(controlled.metafile);
  const cli = await build({
    entryPoints: [path.join(runtimeRoot, 'packages', 'cli', 'src', 'bin.ts')],
    outfile: path.join(outputRoot, 'chirality-cli.mjs'),
    bundle: true,
    platform: 'node',
    target: 'node24',
    format: 'esm',
    banner: { js: "import { createRequire as __controlledCreateRequire } from 'node:module'; const require = __controlledCreateRequire(import.meta.url);" },
    sourcemap: true,
    metafile: true,
    plugins: [runtimeSources],
    logLevel: 'silent'
  });
  await writeFile(path.join(outputRoot, 'controlled-runtime.meta.json'), `${JSON.stringify(controlled.metafile, null, 2)}\n`);
  await writeFile(path.join(outputRoot, 'chirality-cli.meta.json'), `${JSON.stringify(cli.metafile, null, 2)}\n`);
  return { outputRoot, controlledMetafile: controlled.metafile, cliMetafile: cli.metafile };
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  await buildControlledCiRuntime();
}
