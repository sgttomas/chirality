import { rm } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { build } from 'esbuild';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repositoryRoot = path.resolve(frontendRoot, '..', '..', '..');
const runtimeRoot = path.join(repositoryRoot, 'runtime');

const runtimeEntries = {
  '@chirality/runtime-contracts': path.join(
    runtimeRoot,
    'packages',
    'contracts',
    'src',
    'index.ts'
  ),
  '@chirality/runtime-core': path.join(runtimeRoot, 'packages', 'core', 'src', 'index.ts'),
  '@chirality/runtime-daemon': path.join(
    runtimeRoot,
    'packages',
    'daemon',
    'src',
    'index.ts'
  ),
  '@chirality/runtime-client': path.join(
    runtimeRoot,
    'packages',
    'client',
    'src',
    'index.ts'
  ),
  '@chirality/runtime-cli': path.join(runtimeRoot, 'packages', 'cli', 'src', 'index.ts'),
  '@chirality/engine-pi-omlx': path.join(
    runtimeRoot,
    'packages',
    'engine-pi-omlx',
    'src',
    'index.ts'
  )
};

const runtimePackagePlugin = {
  name: 'chirality-runtime-workspace',
  setup(buildApi) {
    buildApi.onResolve(
      { filter: /^@chirality\/runtime-contracts(?:\/(.+))?$/ },
      (args) => {
        const subpath = args.path.slice('@chirality/runtime-contracts'.length + 1);
        return {
          path:
            subpath.length === 0
              ? runtimeEntries['@chirality/runtime-contracts']
              : path.join(runtimeRoot, 'packages', 'contracts', 'src', 'harness', `${subpath}.ts`)
        };
      }
    );
    for (const [packageName, entry] of Object.entries(runtimeEntries)) {
      if (packageName === '@chirality/runtime-contracts') continue;
      buildApi.onResolve(
        { filter: new RegExp(`^${packageName.replaceAll('/', '\\/')}$`) },
        () => ({ path: entry })
      );
    }
  }
};

await rm(path.join(frontendRoot, 'dist-electron'), { recursive: true, force: true });
await rm(path.join(frontendRoot, 'dist-runtime'), { recursive: true, force: true });

await build({
  entryPoints: [path.join(frontendRoot, 'electron', 'main.ts')],
  outfile: path.join(frontendRoot, 'dist-electron', 'main.js'),
  bundle: true,
  platform: 'node',
  target: 'node24',
  format: 'cjs',
  sourcemap: true,
  plugins: [runtimePackagePlugin],
  external: [
    'electron',
    'next',
    '@anthropic-ai/claude-agent-sdk',
    '@anthropic-ai/claude-agent-sdk/*',
    '@anthropic-ai/sdk',
    '@anthropic-ai/sdk/*',
    '@earendil-works/pi-coding-agent',
    '@earendil-works/pi-coding-agent/*'
  ],
  logLevel: 'info'
});

await build({
  entryPoints: [path.join(frontendRoot, 'electron', 'preload.ts')],
  outfile: path.join(frontendRoot, 'dist-electron', 'preload.js'),
  bundle: true,
  platform: 'node',
  target: 'node24',
  format: 'cjs',
  sourcemap: true,
  external: ['electron'],
  logLevel: 'info'
});

await build({
  entryPoints: [path.join(runtimeRoot, 'packages', 'cli', 'src', 'bin.ts')],
  outfile: path.join(frontendRoot, 'dist-runtime', 'chirality-cli.mjs'),
  bundle: true,
  platform: 'node',
  target: 'node24',
  format: 'esm',
  sourcemap: true,
  plugins: [runtimePackagePlugin],
  logLevel: 'info'
});
