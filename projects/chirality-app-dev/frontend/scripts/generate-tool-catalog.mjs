#!/usr/bin/env node

import { createRequire } from 'node:module';
import path from 'node:path';
import { readFileSync } from 'node:fs';
import { mkdir, readFile, writeFile } from 'node:fs/promises';

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

function parseArgs(argv) {
  return {
    check: argv.includes('--check')
  };
}

async function main() {
  const { check } = parseArgs(process.argv.slice(2));
  const { renderHarnessToolCatalog } = require('../src/lib/harness/tool-catalog.ts');
  const rendered = renderHarnessToolCatalog();

  if (check) {
    const current = await readFile(catalogPath, 'utf8');
    if (current !== rendered) {
      throw new Error(
        `${repoRelativeCatalogPath} is out of date. Run npm run harness:generate-tool-catalog.`
      );
    }
    process.stdout.write(`tool catalog is current: ${repoRelativeCatalogPath}\n`);
    return;
  }

  await mkdir(path.dirname(catalogPath), { recursive: true });
  await writeFile(catalogPath, rendered, 'utf8');
  process.stdout.write(`wrote ${repoRelativeCatalogPath}\n`);
}

main().catch((error) => {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(`${message}\n`);
  process.exitCode = 1;
});
