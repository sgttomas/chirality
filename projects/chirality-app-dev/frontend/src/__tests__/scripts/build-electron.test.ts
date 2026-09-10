import path from 'node:path';
import { describe, expect, it } from 'vitest';

import {
  resolveNativeAdmissionSource,
  resolveHostedRuntimeSource,
  resolveHostedRuntimePathsSource,
  resolveRuntimeContractsSource
} from '../../../scripts/build-electron.mjs';

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

  it('resolves native admission from the Runtime package source', () => {
    expect(resolveNativeAdmissionSource()).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/native-admission/src/index.ts')
    );
  });

  it('resolves hosted path helpers without importing the daemon barrel', () => {
    expect(resolveHostedRuntimePathsSource()).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/daemon/src/hosted-paths.ts')
    );
  });

  it('resolves the dedicated hosted daemon entry for Electron private bootstrap wiring', () => {
    expect(resolveHostedRuntimeSource()).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/daemon/src/hosted.ts')
    );
  });
});
