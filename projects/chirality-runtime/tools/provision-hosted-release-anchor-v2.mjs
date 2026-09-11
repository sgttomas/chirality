#!/usr/bin/env node
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { constants } from 'node:fs';
import { mkdir, open, readFile, realpath, rm, stat } from 'node:fs/promises';
import { installHostedReleaseAnchorV2, observeHostedReleaseTrialSealV1, prepareHostedReleaseGovernanceV2 } from '@chirality/runtime-daemon/hosted-release-provisioner';
import { accountFreeLoginObservationFailure, accountFreeLoginStartupDiagnostic, diagnoseCodexAccountFreeLoginStartupV1, observeCodexAccountFreeLoginPurposeV2 } from '@chirality/runtime-daemon/account-free-login-observation';

const USAGE = 'Usage: provision-hosted-release-anchor-v2 --app <canonical .app> --runtime-directory <canonical path> --accepted-governance-root <canonical path> --expected-outer-inventory-sha256 <digest> --login-activation-id <value> --worker-activation-id <value> --worker-gate-identity <value> [--trial-observation <canonical path> --expected-trial-observation-sha256 <digest> --trial-executable <canonical path>]';
const BASE_FLAGS = Object.freeze([
  '--app', '--runtime-directory', '--accepted-governance-root', '--expected-outer-inventory-sha256',
  '--login-activation-id', '--worker-activation-id', '--worker-gate-identity'
]);
const TRIAL_FLAGS = Object.freeze(['--trial-observation', '--expected-trial-observation-sha256', '--trial-executable']);
const FLAGS = Object.freeze([...BASE_FLAGS, ...TRIAL_FLAGS]);
const OBSERVE_USAGE = 'Usage: provision-hosted-release-anchor-v2 observe-trial-seal --app <canonical .app>';
const PREPARE_USAGE = 'Usage: provision-hosted-release-anchor-v2 prepare-governance --recipe <canonical JSON path> --output <canonical absent directory>';
const ACCOUNT_FREE_EVIDENCE_FLAGS = Object.freeze(['--signature-evidence', '--source-correspondence-evidence', '--xpc-record', '--grouped-record']);
const ACCOUNT_FREE_USAGE = 'Usage: provision-hosted-release-anchor-v2 observe-account-free-login --runtime-directory <canonical private path> --resources-root <canonical candidate Resources path> --recipe <canonical owner-private JSON path> --signature-evidence <canonical path> --source-correspondence-evidence <canonical path> --xpc-record <canonical path> --grouped-record <canonical path>';

export function parseObserveHostedReleaseTrialSealArguments(argv) {
  if (!Array.isArray(argv) || argv.length !== 2 || argv[0] !== '--app' || typeof argv[1] !== 'string') throw new Error(OBSERVE_USAGE);
  const app = argv[1];
  if (!path.isAbsolute(app) || path.resolve(app) !== app || !app.endsWith('.app') || /[\x00-\x1f\x7f]/u.test(app)) throw new Error(OBSERVE_USAGE);
  return Object.freeze({ resourcesRoot: path.join(app, 'Contents', 'Resources'), executablePath: path.join(app, 'Contents', 'MacOS', 'Chirality') });
}

export async function runObserveHostedReleaseTrialSealV1(argv, observe = observeHostedReleaseTrialSealV1) {
  return observe(parseObserveHostedReleaseTrialSealArguments(argv));
}

export function parseObserveAccountFreeLoginArguments(argv) {
  if (!Array.isArray(argv) || argv.length !== 14) throw new Error(ACCOUNT_FREE_USAGE);
  const values = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    const flag = argv[index], value = argv[index + 1];
    if (!['--runtime-directory', '--resources-root', '--recipe', ...ACCOUNT_FREE_EVIDENCE_FLAGS].includes(flag) || values.has(flag) || typeof value !== 'string') throw new Error(ACCOUNT_FREE_USAGE);
    values.set(flag, value);
  }
  const canonical = value => typeof value === 'string' && path.isAbsolute(value) && path.resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);
  const runtimeDirectory = values.get('--runtime-directory'), resourcesPath = values.get('--resources-root'), recipePath = values.get('--recipe');
  const evidencePaths = Object.freeze({ signatureEvidenceSha256: values.get('--signature-evidence'), sourceCorrespondenceEvidenceSha256: values.get('--source-correspondence-evidence'), xpcRecordSha256: values.get('--xpc-record'), groupedRecordSha256: values.get('--grouped-record') });
  if (![runtimeDirectory, resourcesPath, recipePath, ...Object.values(evidencePaths)].every(canonical)) throw new Error(ACCOUNT_FREE_USAGE);
  return Object.freeze({ runtimeDirectory, resourcesPath, recipePath, evidencePaths });
}

async function accountFreeLoginInput(argv) {
  if (process.versions.electron !== undefined) throw new Error('Account-free observation requires the external owner Node tool');
  const { runtimeDirectory, resourcesPath, recipePath, evidencePaths } = parseObserveAccountFreeLoginArguments(argv);
  let recipe;
  try { recipe = JSON.parse((await readOwnerAct(recipePath)).toString('utf8')); }
  catch (error) { throw new Error('Account-free observation recipe is invalid', { cause: error }); }
  return { runtimeDirectory, resourcesPath, evidencePaths, recipe };
}

export async function runObserveAccountFreeLoginV2(argv, observe = observeCodexAccountFreeLoginPurposeV2) {
  return observe(await accountFreeLoginInput(argv));
}

export async function runDiagnoseAccountFreeLoginStartupV1(argv, diagnose = diagnoseCodexAccountFreeLoginStartupV1) {
  return diagnose(await accountFreeLoginInput(argv));
}

export function accountFreeLoginFailureOutput(error) {
  const projection = accountFreeLoginObservationFailure(error);
  return projection ? `${JSON.stringify({ schema: 'chirality-account-free-login-observation-failure-output/v1', failure: projection })}\n` : undefined;
}

export function accountFreeLoginStartupDiagnosticOutput(error) {
  const diagnostic = accountFreeLoginStartupDiagnostic(error);
  return diagnostic ? `${JSON.stringify({ schema: 'chirality-account-free-login-startup-diagnostic-output/v1', diagnostic })}\n` : undefined;
}

export function parsePrepareHostedReleaseGovernanceArguments(argv) {
  if (!Array.isArray(argv) || argv.length !== 4) throw new Error(PREPARE_USAGE);
  const values=new Map();for(let index=0;index<argv.length;index+=2){if(!['--recipe','--output'].includes(argv[index])||values.has(argv[index]))throw new Error(PREPARE_USAGE);values.set(argv[index],argv[index+1]);}
  const recipePath=values.get('--recipe'),outputDirectory=values.get('--output'),canonical=value=>typeof value==='string'&&path.isAbsolute(value)&&path.resolve(value)===value&&!/[\x00-\x1f\x7f]/u.test(value);
  if(!canonical(recipePath)||!canonical(outputDirectory))throw new Error(PREPARE_USAGE);return Object.freeze({recipePath,outputDirectory});
}

async function syncDirectory(directory){const handle=await open(directory,'r');try{await handle.sync();}finally{await handle.close();}}
async function readOwnerAct(sourcePath){if(typeof sourcePath!=='string'||!path.isAbsolute(sourcePath)||path.resolve(sourcePath)!==sourcePath||await realpath(sourcePath)!==sourcePath)throw new Error('Owner act path is not canonical');const handle=await open(sourcePath,constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);try{const before=await handle.stat({bigint:true});if(!before.isFile()||before.nlink!==1n||before.uid!==BigInt(process.getuid?.()??-1)||(before.mode&0o777n)!==0o600n||before.size<1n||before.size>1_048_576n)throw new Error('Owner act custody is invalid');const declared=Number(before.size),buffer=Buffer.alloc(declared+1);let total=0;while(total<buffer.length){const{bytesRead}=await handle.read(buffer,total,buffer.length-total,total);if(!bytesRead)break;total+=bytesRead;}const after=await handle.stat({bigint:true}),current=await stat(sourcePath,{bigint:true});for(const key of ['dev','ino','size','mtimeNs','ctimeNs','mode','uid','nlink'])if(before[key]!==after[key]||before[key]!==current[key])throw new Error('Owner act changed while reading');if(total!==declared||await realpath(sourcePath)!==sourcePath)throw new Error('Owner act changed while reading');return buffer.subarray(0,total);}finally{await handle.close();}}
export async function runPrepareHostedReleaseGovernanceV2(argv, prepare = prepareHostedReleaseGovernanceV2) {
  const {recipePath,outputDirectory}=parsePrepareHostedReleaseGovernanceArguments(argv);if(await realpath(recipePath)!==recipePath)throw new Error('Governance recipe path is not canonical');
  const source=JSON.parse((await readOwnerAct(recipePath)).toString('utf8'));if(!source||typeof source!=='object'||Array.isArray(source))throw new Error('Governance recipe must be an object');
  const recipe={...source,login:{...source.login,ownerAct:await readOwnerAct(source.login?.ownerActPath)},worker:{...source.worker,ownerAct:await readOwnerAct(source.worker?.ownerActPath)}};delete recipe.login.ownerActPath;delete recipe.worker.ownerActPath;
  const files=prepare(recipe);let created=false;
  const parent=path.dirname(outputDirectory),parentInfo=await stat(parent);if(await realpath(parent)!==parent||!parentInfo.isDirectory()||parentInfo.uid!==(process.getuid?.()??-1)||(parentInfo.mode&0o077)!==0)throw new Error('Governance output parent is not private');
  try{await mkdir(outputDirectory,{mode:0o700});created=true;await syncDirectory(parent);for(const [name,value]of Object.entries(files)){const handle=await open(path.join(outputDirectory,name),'wx',0o600);try{await handle.writeFile(value.bytes);await handle.sync();}finally{await handle.close();}}await syncDirectory(outputDirectory);return Object.freeze({outputDirectory,files:Object.fromEntries(Object.entries(files).map(([name,value])=>[name,{sha256:value.sha256,size:value.bytes.length}]))});}
  catch(error){if(created){await rm(outputDirectory,{recursive:true,force:true});await syncDirectory(parent);}throw error;}
}

export function parseProvisionHostedReleaseArguments(argv) {
  if (!Array.isArray(argv) || ![BASE_FLAGS.length * 2, FLAGS.length * 2].includes(argv.length)) throw new Error(USAGE);
  const values = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    const flag = argv[index], value = argv[index + 1];
    if (!FLAGS.includes(flag) || values.has(flag) || typeof value !== 'string' || value.length === 0) throw new Error(USAGE);
    values.set(flag, value);
  }
  const canonical = value => path.isAbsolute(value) && path.resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);
  const app = values.get('--app'), runtimeDirectory = values.get('--runtime-directory'), acceptedGovernanceRoot = values.get('--accepted-governance-root');
  if (!canonical(app) || !app.endsWith('.app') || !canonical(runtimeDirectory) || !canonical(acceptedGovernanceRoot)) throw new Error(USAGE);
  const trialValues = TRIAL_FLAGS.map(flag => values.get(flag));
  if (trialValues.some(Boolean) && (!trialValues.every(Boolean) || !canonical(trialValues[0]) || !canonical(trialValues[2]))) throw new Error(USAGE);
  return Object.freeze({
    runtimeDirectory,
    resourcesRoot: path.join(app, 'Contents', 'Resources'),
    acceptedGovernanceRoot,
    expectedOuterInventorySha256: values.get('--expected-outer-inventory-sha256'),
    login: Object.freeze({ activationId: values.get('--login-activation-id'), gateIdentity: 'D36' }),
    worker: Object.freeze({ activationId: values.get('--worker-activation-id'), gateIdentity: values.get('--worker-gate-identity') }),
    ...(trialValues.every(Boolean) ? { trial: Object.freeze({ observationPath: trialValues[0], expectedObservationSha256: trialValues[1], executablePath: trialValues[2] }) } : {})
  });
}

export async function runProvisionHostedReleaseAnchorV2(argv, install = installHostedReleaseAnchorV2) {
  return install(parseProvisionHostedReleaseArguments(argv));
}

const isMain = process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url;
if (isMain) {
  try {
    const argv = process.argv.slice(2);
    if (argv[0] === 'observe-trial-seal') {
      const observed = await runObserveHostedReleaseTrialSealV1(argv.slice(1));
      process.stdout.write(observed.bytes);
    } else if (argv[0] === 'observe-account-free-login') {
      const observed = await runObserveAccountFreeLoginV2(argv.slice(1));
      process.stdout.write(`${JSON.stringify(observed)}\n`);
    } else if (argv[0] === 'diagnose-account-free-login-startup') {
      const diagnosed = await runDiagnoseAccountFreeLoginStartupV1(argv.slice(1));
      process.stdout.write(`${JSON.stringify(diagnosed)}\n`);
    } else if (argv[0] === 'prepare-governance') {
      const prepared = await runPrepareHostedReleaseGovernanceV2(argv.slice(1));
      process.stdout.write(`${JSON.stringify(prepared)}\n`);
    } else {
      const installed = await runProvisionHostedReleaseAnchorV2(argv);
      process.stdout.write(`${JSON.stringify(installed)}\n`);
    }
  } catch (error) {
    const projection = accountFreeLoginStartupDiagnosticOutput(error) ?? accountFreeLoginFailureOutput(error);
    if (projection) process.stderr.write(projection);
    const message = error instanceof Error ? error.message : 'unknown error';
    process.stderr.write(`Hosted release provisioning failed: ${message}\n`);
    process.exitCode = 1;
  }
}
