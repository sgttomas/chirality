#!/usr/bin/env node

import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const frontendRoot = path.resolve(__dirname, '..');
const contractSrc = path.join(frontendRoot, 'packages', 'harness-contract', 'src');
const forbiddenSpecifiers = [
  /^node:/,
  /^react($|\/)/,
  /^react-dom($|\/)/,
  /^next($|\/)/,
  /^electron($|\/)/,
  /^@anthropic-ai\//
];
const allowedFacadeSpecifiers = [/^@chirality\/runtime-contracts(?:$|\/)/];

async function listSourceFiles(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await listSourceFiles(fullPath)));
      continue;
    }
    if (entry.isFile() && fullPath.endsWith('.ts')) {
      files.push(fullPath);
    }
  }
  return files;
}

function importSpecifiers(source) {
  const specifiers = [];
  const importExportPattern =
    /\b(?:import|export)\s+(?:type\s+)?(?:[^'"]*?\s+from\s+)?['"]([^'"]+)['"]/g;
  const dynamicImportPattern = /\bimport\s*\(\s*['"]([^'"]+)['"]\s*\)/g;
  for (const pattern of [importExportPattern, dynamicImportPattern]) {
    let match;
    while ((match = pattern.exec(source)) !== null) {
      specifiers.push(match[1]);
    }
  }
  return specifiers;
}

function resolveRelativeImport(filePath, specifier) {
  const resolved = path.resolve(path.dirname(filePath), specifier);
  return path.extname(resolved) ? resolved : `${resolved}.ts`;
}

const failures = [];
for (const filePath of await listSourceFiles(contractSrc)) {
  const source = await readFile(filePath, 'utf8');
  for (const specifier of importSpecifiers(source)) {
    if (forbiddenSpecifiers.some((pattern) => pattern.test(specifier))) {
      failures.push(`${path.relative(frontendRoot, filePath)} imports forbidden ${specifier}`);
      continue;
    }
    if (specifier.startsWith('.')) {
      const resolved = resolveRelativeImport(filePath, specifier);
      if (!resolved.startsWith(`${contractSrc}${path.sep}`)) {
        failures.push(
          `${path.relative(frontendRoot, filePath)} escapes contract package via ${specifier}`
        );
      }
      continue;
    }
    if (allowedFacadeSpecifiers.some((pattern) => pattern.test(specifier))) {
      continue;
    }
    failures.push(`${path.relative(frontendRoot, filePath)} imports external package ${specifier}`);
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    console.error(failure);
  }
  process.exitCode = 1;
} else {
  console.log('harness contract dependency lint passed');
}
