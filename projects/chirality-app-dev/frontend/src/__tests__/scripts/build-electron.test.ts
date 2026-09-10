import path from 'node:path';
import { describe, expect, it } from 'vitest';

import {
  resolveNativeAdmissionSource,
  resolveHostedRuntimeSource,
  resolveHostedRuntimePathsSource,
  resolveProtectedRuntimeCliSource,
  resolveRuntimeContractsSource,
  resolveRuntimeConformanceV2Source
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

  it('resolves the v2 conformance subpath from the same Runtime source graph', () => {
    expect(resolveRuntimeConformanceV2Source()).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/core/src/runtime-conformance-v2.ts')
    );
  });

  it('pins the protected in-ASAR CLI closure to Runtime CLI source', () => {
    expect(resolveProtectedRuntimeCliSource()).toBe(
      path.resolve(process.cwd(), '../../chirality-runtime/packages/cli/src/cli.ts')
    );
  });
});
