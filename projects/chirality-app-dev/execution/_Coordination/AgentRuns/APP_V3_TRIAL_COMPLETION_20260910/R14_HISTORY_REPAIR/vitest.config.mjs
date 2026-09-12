import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('../../../../../../..', import.meta.url));
export default { resolve: { alias: {
  '@chirality/runtime-contracts/transcript-replay': `${root}/projects/chirality-runtime/packages/contracts/src/harness/transcript-replay.ts`,
  '@chirality/runtime-core': `${root}/projects/chirality-runtime/packages/core/src/index.ts`
} }, test: { testTimeout: 20000 } };
