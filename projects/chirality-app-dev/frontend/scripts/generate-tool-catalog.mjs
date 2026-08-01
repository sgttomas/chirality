#!/usr/bin/env node

import { createRequire } from 'node:module';
import path from 'node:path';
import { readFileSync } from 'node:fs';
import { mkdir, writeFile } from 'node:fs/promises';

const require = createRequire(import.meta.url);
const ts = require('typescript');
const repoRelativeCatalogPath = path.join('docs', 'harness', 'tool_catalog.md');
const catalogPath = path.resolve(process.cwd(), repoRelativeCatalogPath);

require.extensions['.ts'] = function loadTypeScriptModule(module, filename) {
  const source = readFileSync(filename, 'utf8');
  const output = ts.transpileModule(source, {
    compilerOptions: {
      target: ts.ScriptTarget.ES2022,
      module: ts.ModuleKind.CommonJS,
      esModuleInterop: true,
      isolatedModules: true
    },
    fileName: filename
  });
  module._compile(output.outputText, filename);
};

// Catalog-vs-descriptor drift is owned by a single check:
// src/__tests__/lib/tool-catalog.test.ts (runs in CI through the
// release-quality wrapper's full_test evidence command). The former
// `--check` mode here duplicated that exact equality assertion and had no
// CI or package.json caller, so this script is now write-only.
async function main() {
  const { renderHarnessToolCatalog } = require(
    '../packages/harness-contract/src/tool-catalog.ts'
  );
  const rendered = renderHarnessToolCatalog();

  await mkdir(path.dirname(catalogPath), { recursive: true });
  await writeFile(catalogPath, rendered, 'utf8');
  process.stdout.write(`wrote ${repoRelativeCatalogPath}\n`);
}

main().catch((error) => {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(`${message}\n`);
  process.exitCode = 1;
});
