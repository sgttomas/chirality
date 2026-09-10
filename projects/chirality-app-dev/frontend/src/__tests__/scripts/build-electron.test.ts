import path from 'node:path';
import { describe, expect, it } from 'vitest';

import { resolveRuntimeContractsSource } from '../../../scripts/build-electron.mjs';

describe('build Electron Runtime contract aliases', () => {
  it('resolves the v3 package export from the contracts source root', () => {
    expect(resolveRuntimeContractsSource('v3')).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/contracts/src/v3.ts')
    );
  });

  it('keeps established Harness subpath exports under the Harness source directory', () => {
    expect(resolveRuntimeContractsSource('errors')).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/contracts/src/harness/errors.ts')
    );
  });
});
