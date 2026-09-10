#!/usr/bin/env node
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { installHostedReleaseAnchorV2 } from '@chirality/runtime-daemon/hosted-release-provisioner';

const USAGE = 'Usage: provision-hosted-release-anchor-v2 --app <canonical .app> --runtime-directory <canonical path> --accepted-governance-root <canonical path> --expected-outer-inventory-sha256 <digest> --login-activation-id <value> --worker-activation-id <value> --worker-gate-identity <value>';
const FLAGS = Object.freeze([
  '--app', '--runtime-directory', '--accepted-governance-root', '--expected-outer-inventory-sha256',
  '--login-activation-id', '--worker-activation-id', '--worker-gate-identity'
]);

export function parseProvisionHostedReleaseArguments(argv) {
  if (!Array.isArray(argv) || argv.length !== FLAGS.length * 2) throw new Error(USAGE);
  const values = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    const flag = argv[index], value = argv[index + 1];
    if (!FLAGS.includes(flag) || values.has(flag) || typeof value !== 'string' || value.length === 0) throw new Error(USAGE);
    values.set(flag, value);
  }
  const canonical = value => path.isAbsolute(value) && path.resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);
  const app = values.get('--app'), runtimeDirectory = values.get('--runtime-directory'), acceptedGovernanceRoot = values.get('--accepted-governance-root');
  if (!canonical(app) || !app.endsWith('.app') || !canonical(runtimeDirectory) || !canonical(acceptedGovernanceRoot)) throw new Error(USAGE);
  return Object.freeze({
    runtimeDirectory,
    resourcesRoot: path.join(app, 'Contents', 'Resources'),
    acceptedGovernanceRoot,
    expectedOuterInventorySha256: values.get('--expected-outer-inventory-sha256'),
    login: Object.freeze({ activationId: values.get('--login-activation-id'), gateIdentity: 'D36' }),
    worker: Object.freeze({ activationId: values.get('--worker-activation-id'), gateIdentity: values.get('--worker-gate-identity') })
  });
}

export async function runProvisionHostedReleaseAnchorV2(argv, install = installHostedReleaseAnchorV2) {
  return install(parseProvisionHostedReleaseArguments(argv));
}

const isMain = process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url;
if (isMain) {
  try {
    const installed = await runProvisionHostedReleaseAnchorV2(process.argv.slice(2));
    process.stdout.write(`${JSON.stringify(installed)}\n`);
  } catch (error) {
    const message = error instanceof Error ? error.message : 'unknown error';
    process.stderr.write(`Hosted release provisioning failed: ${message}\n`);
    process.exitCode = 1;
  }
}
