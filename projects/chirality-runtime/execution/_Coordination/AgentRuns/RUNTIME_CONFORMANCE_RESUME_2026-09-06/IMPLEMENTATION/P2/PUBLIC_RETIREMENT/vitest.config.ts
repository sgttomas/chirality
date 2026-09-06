import { defineConfig } from 'vitest/config';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
const root = fileURLToPath(new URL("../../../../../../../", import.meta.url));
export default defineConfig({ root, resolve: { alias: [
  { find: /^@chirality\/runtime-core$/, replacement: join(root, 'packages/core/src/index.ts') },
  { find: /^@chirality\/runtime-contracts$/, replacement: join(root, 'packages/contracts/src/index.ts') },
  { find: /^@chirality\/runtime-client$/, replacement: join(root, 'packages/client/src/index.ts') },
] }, test: { include: ['tests/exact-process-runtime-conformance.test.ts'] } });
