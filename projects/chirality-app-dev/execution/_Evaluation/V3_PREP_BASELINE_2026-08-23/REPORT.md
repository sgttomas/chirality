# V3 Preparation-Lane Baseline — 2026-08-23

## Status and boundary

- Evaluation basis: `3af765222bbd4f43a52dcbe17bd151c13942e5ac`.
- Frozen reference: `origin/main` at the same commit.
- Basis frontend tree: `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- Scope: evidence-only baseline for the v3 preparation lane. This report changes
  no code, contract, register, lifecycle, pointer, or frontend byte.
- Epistemic status: observations below reproduce exact basis bytes. The AT
  mappings identify later evidence obligations they feed; they are neither
  conformance findings nor owner acceptance, release, or lifecycle authority.
- Citation convention: each citation gives `path:line` or `path:start-end` and
  the SHA-256 of the complete file's exact Git blob bytes at the basis. The
  following indented block is the verbatim output of
  `git show origin/main:<path> | sed -n '<range>p'`.

## 1. Electron identity and frozen distribution supply

### 1.1 Executable pin and the 43.1.1 historical reference

The executable manifest and its lockfile both pin Electron `43.2.0`.

`projects/chirality-app-dev/frontend/package.json:68`
blob SHA-256 `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc`

```text
    "electron": "43.2.0",
```

`projects/chirality-app-dev/frontend/package-lock.json:40`
blob SHA-256 `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458`

```text
        "electron": "43.2.0",
```

D-APP-72 named `43.1.1` as the desktop prerequisite.

`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-72_RULING_2026-07-21.md:23-26`
blob SHA-256 `c7dcbb5aaa0f82481fb76825c7099c4e355c4ada80232c51f3a3cf6ba2076577`

```text
The owner authorizes the bounded Pi/oMLX second-engine tranche described by SCA-APP-002:

- upgrade the desktop prerequisite to Electron `43.1.1` with its embedded Node `24.18.0`, electron-builder `26.15.3`, and project Node floor `>=22.19.0` before Pi integration;
- pin `@earendil-works/pi-coding-agent` `0.80.10` and run it in-process as an opt-in second adapter;
```

The later App ruling records `43.2.0` as current App authority and explicitly
classifies D-APP-72's `43.1.1` reference as historical. Therefore this report
does not describe `43.1.1` as current App dependency authority.

`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-98_RULING_ELECTRON_AUTHORITY_2026-08-17.md:16-18`
blob SHA-256 `71dfc1ae6369acea1e49f71d68e45aaf9da8f14c5f6a77733845c43f3ee7c020`

```text
**C2 — Electron authority disposition, TM-APP-041.**

Electron `43.2.0`, as pinned in `frontend/package.json` on `main`, is the App's recorded Electron authority and the D-APP-72 successor for that single fact. D-APP-72's `43.1.1` reference is historical. Future Electron changes are made by amending the pin and recording a successor disposition in the same tranche; no separate packet is required for patch/minor upgrades that pass the registered checks and the packaged-artifact proofs of the release-preparation phase. TM-APP-041 is resolved by this ruling. No dependency, product, or lock-file byte changes in the recording tranche.
```

The Revision 3.1 plan nevertheless retains the cross-loop TM-ROOT-122
comparison as a prerequisite-versus-observed drift to resolve before AT-039.
That is a named preparation blocker, not a pin change in this report.

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:671-675`
blob SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`

```text
        <h3>8.4 Pre-existing defects to resolve or explicitly isolate</h3>
        <ul>
          <li>TM-ROOT-106 / PI082-F07: governed Pi/oMLX pin <code>0.80.10</code> versus shipped adapter <code>0.82.0</code>; resolve or isolate before G1.</li>
          <li>TM-ROOT-122: Electron <code>43.1.1</code> governed prerequisite versus observed <code>43.2.0</code>; resolve before AT-039 identity freeze.</li>
          <li>Route Task Management candidates for practitioner-harness advisory treatment of uncatalogued <code>K-*</code>, K-EVENT-4’s live legacy path, and DEL-09-04 source-completeness/staged-identity remediation.</li>
```

### 1.2 Frozen `electronDist` posture

The R18/Tranche-A supply verifier pins version, archive name, exact byte size,
SHA-256, the verbatim official checksum line, and its source URL.

`projects/chirality-app-dev/frontend/scripts/verify-electron-dist.mjs:8-16`
blob SHA-256 `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`

```text
export const ELECTRON_SUPPLY_PIN = Object.freeze({
  version: '43.2.0',
  filename: 'electron-v43.2.0-darwin-arm64.zip',
  size: 122090802,
  sha256: 'ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28',
  officialLine:
    'ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28 *electron-v43.2.0-darwin-arm64.zip',
  sourceUrl: 'https://github.com/electron/electron/releases/download/v43.2.0/SHASUMS256.txt'
});
```

The verifier fail-closes on package-version drift, non-regular/symlink archive,
size mismatch, and digest mismatch.

`projects/chirality-app-dev/frontend/scripts/verify-electron-dist.mjs:65-74`
blob SHA-256 `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`

```text
  let packageJson;
  try {
    packageJson = JSON.parse(await readFile(packageJsonPath, 'utf8'));
  } catch (error) {
    throw new Error(`Unable to read frontend package.json: ${error.message}`);
  }
  if (packageJson.devDependencies?.electron !== ELECTRON_SUPPLY_PIN.version) {
    throw new Error(
      `Electron devDependency must equal ${ELECTRON_SUPPLY_PIN.version}`
    );
```

`projects/chirality-app-dev/frontend/scripts/verify-electron-dist.mjs:86-107`
blob SHA-256 `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`

```text
  const archivePath = path.join(resolvedDirectory, ELECTRON_SUPPLY_PIN.filename);
  if (path.dirname(archivePath) !== resolvedDirectory) {
    throw new Error('Electron archive path escapes the distribution directory');
  }
  const archiveStat = await lstat(archivePath);
  if (!archiveStat.isFile() || archiveStat.isSymbolicLink()) {
    throw new Error('Electron archive must be a regular non-symlink file');
  }
  if (archiveStat.size !== ELECTRON_SUPPLY_PIN.size) {
    throw new Error(
      `Electron archive size mismatch: expected ${ELECTRON_SUPPLY_PIN.size}, received ${archiveStat.size}`
    );
  }
  const canonicalArchive = await realpath(archivePath);
  if (canonicalArchive !== path.join(canonicalDirectory, ELECTRON_SUPPLY_PIN.filename)) {
    throw new Error('Electron archive resolves outside the distribution directory');
  }

  const digest = await hashArchive(archivePath);
  if (digest !== ELECTRON_SUPPLY_PIN.sha256) {
    throw new Error('Electron archive SHA-256 mismatch');
  }
```

The packaging wrapper first verifies the directory and then passes it to
electron-builder via the directory-form `electronDist` configuration while
pinning macOS arm64, directory output, no publishing, and disabled signing
identity auto-discovery.

`projects/chirality-app-dev/frontend/scripts/pack-electron-with-supply.mjs:5-18`
blob SHA-256 `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db`

```text
import { verifyElectronDist } from './verify-electron-dist.mjs';

export function buildElectronBuilderArgs(electronDistDirectory) {
  if (typeof electronDistDirectory !== 'string' || electronDistDirectory.length === 0) {
    throw new Error('Verified Electron distribution directory is required');
  }
  return [
    '--mac',
    '--arm64',
    '--dir',
    '--publish',
    'never',
    `-c.electronDist=${electronDistDirectory}`
  ];
```

`projects/chirality-app-dev/frontend/scripts/pack-electron-with-supply.mjs:41-55`
blob SHA-256 `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db`

```text
export async function runElectronPack({
  verify = verifyElectronDist,
  spawnProcess = spawn,
  env = process.env
} = {}) {
  const electronDistDirectory = await verify();
  const args = buildElectronBuilderArgs(electronDistDirectory);
  await spawnAndWait(
    'electron-builder',
    args,
    {
      stdio: 'inherit',
      shell: false,
      env: { ...env, CSC_IDENTITY_AUTO_DISCOVERY: 'false' }
    },
```

## 2. Credential storage and release-credential posture

### 2.1 `safeStorage` state collapse

`retrieveProviderApiKey` returns the same `null` result for three distinct
conditions: encryption unavailable, storage read failure (including absence),
and decrypt failure. The last path preserves the corrupted blob but does not
return a distinct typed state. This is the observed null-collapse baseline.

`projects/chirality-app-dev/frontend/electron/api-key-storage.ts:80-106`
blob SHA-256 `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db`

```text
export async function retrieveProviderApiKey(
  providerId: ProviderCredentialId
): Promise<string | null> {
  if (!safeStorage.isEncryptionAvailable()) {
    return null;
  }

  const storagePath = getStoragePath(providerId);
  let encrypted: Buffer;
  try {
    encrypted = await readFile(storagePath);
  } catch {
    return null;
  }

  // Repair credentials stored before the owner-only mode was enforced, so an
  // installation heals on first read rather than only when a key is re-entered.
  await chmod(storagePath, 0o600).catch(() => undefined);
  await chmod(path.dirname(storagePath), 0o700).catch(() => undefined);

  try {
    return safeStorage.decryptString(encrypted);
  } catch {
    // Preserve corrupted blobs for operator investigation.
    return null;
  }
}
```

### 2.2 Unsigned workflow credential hard-fail

The desktop release template fails if common signing/notarization credentials
are present, fails unless signing identity auto-discovery is disabled, and
labels the output unsigned/ad hoc.

`.github/workflows/desktop-release-template.yml:58-70`
blob SHA-256 `3642152e730e3b6c59d48d860cbf1fd49a5c999d25d505deba4112dde62db2dc`

```text
      - name: Verify unsigned build posture
        shell: bash
        run: |
          set -euo pipefail
          if env | grep -Eq '^(CSC_LINK|CSC_KEY_PASSWORD|APPLE_ID|APPLE_APP_SPECIFIC_PASSWORD|APPLE_TEAM_ID)='; then
            echo "::error::Signing or notarization credentials must not be present in this CI-only workflow."
            exit 1
          fi
          if [[ "${CSC_IDENTITY_AUTO_DISCOVERY}" != "false" ]]; then
            echo "::error::Automatic signing identity discovery must remain disabled."
            exit 1
          fi
          echo "This job creates an unsigned/adhoc CI artifact only." >> "${GITHUB_STEP_SUMMARY}"
```

## 3. Packaged CLI and current LaunchAgent shape

The packaged CLI entry resolves from the app's resources under
`runtime-cli/chirality-cli.mjs`.

`projects/chirality-app-dev/frontend/electron/cli-launcher.ts:17-20`
blob SHA-256 `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`

```text
export function resolveBundledCliEntry(): string {
  return app.isPackaged
    ? path.join(process.resourcesPath, 'runtime-cli', 'chirality-cli.mjs')
    : path.resolve(__dirname, '..', 'dist-runtime', 'chirality-cli.mjs');
```

The generated launcher exports `ELECTRON_RUN_AS_NODE=1` before dispatch.

`projects/chirality-app-dev/frontend/electron/cli-launcher.ts:53-59`
blob SHA-256 `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`

```text
  return `#!/bin/zsh
set -eu
desktop_executable=${desktopExecutable}
cli_entry=${cliEntry}
export ELECTRON_RUN_AS_NODE=1
${pinnedExports}
if [[ "\${1:-}" == "daemon" && "\${2:-}" == "install" ]]; then
```

The current runtime CLI LaunchAgent renderer hard-codes
`--runtime-daemon` as the sole argument after the executable. This is the
current one-job program-argument baseline relevant to the later two-job
installer/supervisor work; it does not demonstrate that future work.

`runtime/packages/cli/src/launch-agent.ts:248-255`
blob SHA-256 `1c3992ff3ca595cedfb648c9cae0aebfd557c2bb9b68e620b8b89799ddfcea27`

```text
  <key>Label</key>
  <string>${xml(label)}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${xml(resolve(input.executablePath))}</string>
    <string>--runtime-daemon</string>
  </array>
  <key>RunAtLoad</key>
```

## 4. Secret-evidence scan surface

The scanner's complete text-extension allowlist includes `.json` and
`.ndjson` but does not include `.jsonl`. Because `isTextPath` accepts only set
membership, `.jsonl` is outside this extension-selected scan surface at basis.

`projects/chirality-app-dev/frontend/scripts/scan-secret-evidence.mjs:29-48`
blob SHA-256 `001cb2b7ecc380807e6debf77ce503a71efddf6909083365e4890f0f10981187`

```text
const TEXT_EXTENSIONS = new Set([
  '.cjs',
  '.csv',
  '.css',
  '.html',
  '.js',
  '.json',
  '.jsx',
  '.log',
  '.md',
  '.mjs',
  '.ndjson',
  '.sh',
  '.svg',
  '.ts',
  '.tsx',
  '.txt',
  '.yaml',
  '.yml'
]);
```

`projects/chirality-app-dev/frontend/scripts/scan-secret-evidence.mjs:133-135`
blob SHA-256 `001cb2b7ecc380807e6debf77ce503a71efddf6909083365e4890f0f10981187`

```text
function isTextPath(filePath) {
  return TEXT_EXTENSIONS.has(path.extname(filePath).toLowerCase());
}
```

## 5. Harness permission and path-policy baselines

### 5.1 SDK bypass environment gate

The SDK options builder maps `bypass` to `bypassPermissions` only when
`CHIRALITY_ALLOW_SDK_BYPASS=1`; otherwise it falls through to `default`.

`projects/chirality-app-dev/frontend/src/lib/harness/sdk-options-builder.ts:42-55`
blob SHA-256 `ea5ab431b00a7dd402ac30291891c7d74b050f2e866c7b3d76c33d0e542370f6`

```text
  if (normalizedMode === 'readOnly' || normalizedMode === 'dontAsk') {
    return 'dontAsk';
  }
  if (normalizedMode === 'workspaceWrite') {
    return 'acceptEdits';
  }
  if (
    normalizedMode === 'bypass' &&
    process.env.CHIRALITY_ALLOW_SDK_BYPASS === '1'
  ) {
    return 'bypassPermissions';
  }
  return 'default';
}
```

### 5.2 Tool-path argument-only inspection

The path policy's own extraction surface is a fixed list of primary fields in
the structured `toolInput`; it returns the first non-empty string field.

`projects/chirality-app-dev/frontend/src/lib/harness/tool-path-policy.ts:30-38`
blob SHA-256 `fe707666d7fb528519b9ce358987e198082ad1e6f11132b97eadc435d20e5eaf`

```text
const PRIMARY_PATH_FIELDS = [
  'file_path',
  'path',
  'notebook_path',
  'deliverablePath',
  'executionRoot',
  'decompositionPath',
  'runnerInputRef'
] as const;
```

`projects/chirality-app-dev/frontend/src/lib/harness/tool-path-policy.ts:49-65`
blob SHA-256 `fe707666d7fb528519b9ce358987e198082ad1e6f11132b97eadc435d20e5eaf`

```text
function readPrimaryPathField(toolInput: unknown): { field: string; value: string } | undefined {
  if (!isRecord(toolInput)) {
    return undefined;
  }

  for (const field of PRIMARY_PATH_FIELDS) {
    const value = toolInput[field];
    if (typeof value === 'string' && value.trim().length > 0) {
      return {
        field,
        value: value.trim()
      };
    }
  }

  return undefined;
}
```

For a shell-permission descriptor with no recognized primary path field, the
function returns allowed metadata rather than inspecting command text. This is
the precise basis for the "argument-only inspection" label; it is an observed
implementation boundary, not a conclusion that every caller is exploitable.

`projects/chirality-app-dev/frontend/src/lib/harness/tool-path-policy.ts:199-215`
blob SHA-256 `fe707666d7fb528519b9ce358987e198082ad1e6f11132b97eadc435d20e5eaf`

```text
  const pathField = readPrimaryPathField(input.toolInput);
  const projectRoot = path.resolve(input.projectRoot);
  const managedScopes =
    pathScope === 'project-root-read'
      ? input.allowedReadScopes
      : pathScope === 'project-root-write'
        ? input.allowedWriteTargets
        : undefined;
  if (!pathField) {
    if (input.descriptor?.permissions.includes('shell')) {
      return {
        allowed: true,
        metadata: {
          projectRoot,
          pathScope
        }
      };
```

### 5.3 PEC suffix globs

The PEC profile declares suffix-glob protected write paths including broad
subtrees, `_STATUS.md`, and `ScopeOfWork.md` patterns.

`_DomainEngines/profiles/pec.yaml:34-45`
blob SHA-256 `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`

```text
  protected_write_paths:
    - "_DomainEngines/profiles/pec.yaml"
    - "projects/pec/v2/**"
    - "projects/pec/software-workflow.json"
    - "projects/pec/chirality.project.json"
    - "projects/pec/AGENTS.md"
    - "projects/pec/docs/**"
    - "projects/pec/execution/_Decomposition/**"
    - "projects/pec/execution/_ScopeChange/**"
    - "projects/pec/execution/_Coordination/_DECISIONS/**"
    - "projects/pec/execution/**/_STATUS.md"
    - "projects/pec/execution/**/ScopeOfWork.md"
```

### 5.4 Active-sibling write overlap

Managed delegation enumerates sibling instances, considers only `LAUNCHED` or
`RUNNING` siblings, compares write targets, and rejects undeclared overlap;
an unreadable or malformed sibling record fails closed, while a readable record
whose status is not `LAUNCHED` or `RUNNING` is skipped. This is the current
multi-child write-disjointness baseline, not evidence for native-descendant
topology.

`projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts:467-505`
blob SHA-256 `0a3dec1309bde70548daee39a48b280ece6886f837d8c4d4b40b85f4f6a6d180`

```text
async function assertNoActiveWriteOverlap(
  runRoot: string,
  instanceId: string,
  writeTargets: string[],
  dependencies: string[]
): Promise<void> {
  const instancesRoot = path.join(runRoot, 'instances');
  let entries: string[] = [];
  try {
    entries = await readdir(instancesRoot);
  } catch {
    return;
  }
  for (const siblingId of entries) {
    if (siblingId === instanceId) continue;
    try {
      const status = await readJson(path.join(instancesRoot, siblingId, 'STATUS.json'));
      if (!['LAUNCHED', 'RUNNING'].includes(String(status.status))) continue;
      const siblingTargets = Array.isArray(status.writeTargets)
        ? status.writeTargets.filter((item): item is string => typeof item === 'string')
        : [];
      const overlap = writeTargets.some((target) => siblingTargets.some((other) => pathsOverlap(target, other)));
      if (overlap && !dependencies.includes(siblingId)) {
        throw new HarnessError(
          'INVALID_REQUEST',
          409,
          `Concurrent write overlap with active sibling ${siblingId}`
        );
      }
    } catch (error) {
      if (error instanceof HarnessError) throw error;
      throw new HarnessError(
        'INVALID_REQUEST',
        409,
        `Cannot prove write disjointness because sibling ${siblingId} has an invalid status record`
      );
    }
  }
}
```

## 6. Shared-runtime and packaging doctrine

### 6.1 Release Quality Gates section 13

Section 13 requires preservation of engine behavior; one shared Desktop/CLI
daemon and state/credential/interruption ownership; a protected Unix socket
with recovery and no TCP listener; explicit model-switching rules; App/PEC
evidence; and a generic, credential-free public export. The text explicitly
withholds release and lifecycle authority.

`projects/chirality-app-dev/docs/RELEASE_QUALITY_GATES.md:161-178`
blob SHA-256 `dbfa56aa71ae9934f84247ec115721129e3aac4fb2cedfd5b5cab212c74bc382`

```text
## 13. Shared Runtime Gate

Before SCA-APP-003 closeout, prove:

- runtime-package promotion preserves current Claude/stub/Pi behavior;
- Desktop and CLI use one daemon, session store, lock system, credential
  owner, and interruption state;
- the control plane has correct Unix-socket permissions, project-scoped
  authorization, stale recovery, and no TCP listener;
- model switching obeys explicit activation, drain, timeout, no-force,
  `NO_MODEL`, no-helper-unload, and no-fallback rules;
- the app-dev and PEC pilot paths pass with canonical evidence and
  actual-model attribution;
- public export includes only generic runtime/CLI/contracts/safe adapters and
  excludes credentials, machine state, and private adapters.

This gate is validation evidence only. It grants no release, publication,
signing, notarization, lifecycle, or professional-reliance authority.
```

### 6.2 Current BUILD_AND_RELEASE packaging steps

The current skeleton binds source state, commands, quality gates, integrity,
build/package commands, artifact/checksum evidence, signing/notarization state,
limitations, and human records, then explicitly prohibits publication or
reliance implications. Hosted release concerns remain human-gated.

`projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md:126-146`
blob SHA-256 `903c96dbd72ebc3982c6886c831dd0754c461c9454dbebb119d1af931b39ba0c`

```text
## 8. Packaging Skeleton

A packaging review should:

1. Confirm source revision and working-tree state.
2. Confirm `frontend/package.json` command and `build` configuration are the intended source of package behavior.
3. Run applicable validation gates from `docs/RELEASE_QUALITY_GATES.md`.
4. Run `npm run instruction-root:integrity`.
5. Run `npm run build`.
6. Run `npm run desktop:pack` for app-directory packaging review, or `npm run desktop:dist` for DMG review when in scope.
7. Record generated artifact paths and checksums when a release-candidate review requires them.
8. Record signing and notarization state. Current ordinary output is unsigned and unnotarized.
9. Record known limitations, skipped checks, unresolved decisions, and any human waiver or acceptance record.

No packaging review may imply that the package is published, professionally approved, externally validated, code-compliant, certified, sealed, authenticated, notarized, or suitable for reliance.

## 9. Future CI And Release Mapping

Hosted CI, public/private data handling, release matrix, signing, notarization, publication, and attestation remain future human-gated decisions. When selected, hosted workflows should call the same local command surface or a documented equivalent so local and hosted evidence remain comparable.

Hosted workflows must not receive private project data, API keys, protected professional work, SDK transcripts containing secrets, signing credentials, publishing credentials, or broader network permissions unless a recorded human decision authorizes the handling model.
```

## 7. R20 login-proof harness as a later two-label fixture seed

The harness has explicit prepare/capture/preflight modes, source/session/label
binding, a macOS Unix-socket maximum, and fixed schemas.

`projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs:23-40`
blob SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`

```text
import {
  DEFAULT_LAUNCH_AGENT_LABEL,
  assertExactRuntimeArguments,
  inspectInstalledPlist,
  isExactLaunchctlNotFound,
  parseLaunchctlJob,
  validateProofLabel
} from './run-packaged-launchagent-runatload-proof.mjs';

export const SESSION_SCHEMA = 'chirality-packaged-launchagent-login-proof-session/v1';
const CAPTURE_STATE_SCHEMA = 'chirality-packaged-launchagent-login-proof-capture-state/v1';
export const SUMMARY_SCHEMA = 'chirality-packaged-launchagent-login-proof/v1';
export const EVIDENCE_SCHEMA = 'chirality-packaged-launchagent-login-proof-evidence/v1';
export const PREFLIGHT_SCHEMA = 'chirality-packaged-launchagent-login-proof-preflight/v1';
export const MACOS_UNIX_SOCKET_PATH_MAX_BYTES = 103;

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const defaultAppPath = path.join(frontendRoot, 'dist', 'mac-arm64', 'Chirality.app');
```

Preparation binds one unique proof label/service, refuses pre-existing state,
and snapshots the separate default operator job only for protection.

`projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs:1070-1087`
blob SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`

```text
  const label = validateProofLabel(
    options.label ??
      `com.chirality.ci.runatload.login.${process.pid}.${deps.randomId().replaceAll('-', '').slice(0, 8)}`
  );
  const plistPath = path.join(launchAgentsDirectory, `${label}.plist`);
  const service = `gui/${uid}/${label}`;
  if ((await fileSnapshot(plistPath)).present) {
    throw new Error('Proof plist already exists; refusing to overwrite it');
  }
  if ((await jobState(service, deps)).classification !== 'NOT_FOUND') {
    throw new Error('Proof job already exists; refusing to take ownership');
  }
  const defaultPlistPath = path.join(
    launchAgentsDirectory,
    `${DEFAULT_LAUNCH_AGENT_LABEL}.plist`
  );
  const defaultService = `gui/${uid}/${DEFAULT_LAUNCH_AGENT_LABEL}`;
  const defaultBefore = await protectedState(defaultPlistPath, defaultService, deps);
```

Its prepared record binds revision, label, service, plist digest, executable
digest, login-session identity, and the no-bootstrap/no-kickstart boundary.

`projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs:1123-1148`
blob SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`

```text
    const prepared = {
      schema: SESSION_SCHEMA,
      status: 'PREPARED',
      preparedAt: deps.now().toISOString(),
      sourceRevision,
      label,
      service,
      plist: `~/Library/LaunchAgents/${label}.plist`,
      plistSha256: await sha256File(plistPath),
      app: {
        path: '<packaged-app>',
        executableSha256: await sha256File(executablePath)
      },
      runtimeData: '<proof-session>/runtime-data',
      preparedLoginSessionSha256,
      preparedJobAbsent: true,
      defaultProtection: {
        label: DEFAULT_LAUNCH_AGENT_LABEL,
        plist: `~/Library/LaunchAgents/${DEFAULT_LAUNCH_AGENT_LABEL}.plist`,
        recordedOnly: true
      },
      prepareMutations: ['packaged-cli-install'],
      bootstrapInvoked: false,
      kickstartInvoked: false,
      proofClaimed: false
    };
```

Capture requires a loaded, running job; exact program and arguments; and a
single canonical packaged executable identity.

`projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs:1363-1385`
blob SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`

```text
    const captured = await jobState(captureState.service, deps);
    if (captured.classification !== 'LOADED') {
      throw new Error('Prepared job was not discovered in the current login session');
    }
    const job = parseLaunchctlJob(captured.result.stdout);
    observedPid = job.pid;
    summary.process.pidObserved = true;
    if (job.state !== 'running') throw new Error(`Prepared job state was ${job.state}`);
    if (path.resolve(job.program) !== captureState.executablePath) {
      throw new Error('Loaded job program does not match prepared packaged executable');
    }
    summary.launchAgent.loadedProgramMatches = true;
    summary.launchAgent.loadedArgumentsAvailable = job.programArguments !== undefined;
    if (job.programArguments === undefined) throw new Error('Loaded job arguments are missing');
    assertExactRuntimeArguments(job.programArguments, captureState.executablePath, 'Loaded job');
    summary.launchAgent.loadedArgumentsMatch = true;
    const processExecutables = await canonicalPackagedExecutables(
      await deps.inspectProcessExecutables(observedPid)
    );
    if (processExecutables.length !== 1 || processExecutables[0] !== captureState.executablePath) {
      throw new Error('Launched process executable identity is missing or ambiguous');
    }
    summary.process.executableIdentityMatches = true;
```

PASS requires process/job/plist/runtime-data cleanup plus protected-default
state; the evidence package binds prepared and summary digests.

`projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs:1429-1444`
blob SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`

```text
  const cleanupComplete =
    summary.cleanup.processAbsent &&
    summary.cleanup.jobAbsent &&
    summary.cleanup.plistAbsent &&
    summary.cleanup.runtimeDataRemoved;
  const defaultProtected = Object.values(summary.defaultProtection)
    .filter((value) => typeof value === 'boolean')
    .every(Boolean);
  const finalPass =
    !proofError && cleanup.errors.length === 0 && cleanupComplete && defaultProtected;
  if (finalPass) {
    summary.status = 'PASS';
    try {
      await deps.removePassFailureLogs(cleanup.failedLogsRoot);
      summary.cleanup.failureLogsCopied = false;
      summary.cleanup.passOnlyFailureLogCleanup = 'REMOVED';
```

`projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs:1470-1481`
blob SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`

```text
  const summaryPath = path.join(sessionRoot, 'summary.json');
  await writeJsonAtomic(summaryPath, summary);
  const evidence = {
    schema: EVIDENCE_SCHEMA,
    status: summary.status,
    sourceRevision: summary.sourceRevision,
    preparedManifestSha256: createHash('sha256').update(preparedBytes).digest('hex'),
    summarySha256: await sha256File(summaryPath),
    files: ['prepared.json', 'summary.json']
  };
  await writeJsonAtomic(path.join(sessionRoot, 'evidence-package.json'), evidence);
  if (summary.status !== 'PASS') throw new Error(summary.error ?? 'Login-session proof capture failed');
```

Assessment: these are useful seed primitives for a later G-HELPER two-label
fixture: exact label/service/program/argument identity, launch-session
observation, protected unrelated state, process identity, cleanup, and bound
evidence. The present harness proves one proof service while protecting the
default service; it does **not** prove installation, coexistence, migration, or
rollback of the future daemon-plus-process-supervisor pair.

## 8. AT obligation mapping

The plan describes AT rows as evidence obligations, not current-conformance
claims. The mappings below identify which later obligation each baseline fact
feeds; they do not satisfy any row.

| Baseline fact | Later AT identifiers fed | Why this evidence is relevant |
|---|---|---|
| Electron pin and frozen `electronDist` | AT-038, AT-039, AT-047 | Unsigned build posture, exact dependency/source identity freeze, and packaged nested-byte survival require a stable Electron input and package path. |
| `safeStorage` null-collapse | AT-051, AT-057 | The later gate must distinguish decrypt failure/storage unavailability/missing state and prove identity transitions. |
| Bundled CLI, RunAsNode, hard-coded daemon job | AT-035, AT-048, AT-054, AT-058 | These bytes are the current baseline for two-job migration, Finder activation, installer transactions, and the future Electron-as-Node supervisor. |
| Secret scanner and unsigned credential hard-fail | AT-025, AT-038 | Later evidence must cover `.jsonl` and other sinks while keeping production signing/notary credentials out of preparation. |
| SDK bypass gate | AT-006, AT-018, AT-049 | Environment isolation and actual-turn/package sandbox evidence must show development bypass posture cannot escape into the candidate. |
| Tool primary-field inspection and PEC suffix globs | AT-018, AT-019, AT-031, AT-049 | Later probes must demonstrate actual command/file enforcement, protected-glob round trips, and semantic failure containment. |
| Active-sibling write-overlap check | AT-027, AT-031 | Native topology remains uncapped while Chirality-managed work still must not expand write authority through sibling overlap. |
| RQG section 13 | AT-053 | The governed-basis scenario explicitly requires the Shared Runtime Gate mapping. |
| BUILD_AND_RELEASE steps | AT-038, AT-039, AT-047 | The steps define the evidence chain from source and commands through package identity and explicit unsigned state. |
| R20 harness seed | AT-035, AT-048, AT-054, AT-058 | Existing launchd/process/cleanup identity checks can seed, but cannot substitute for, the later two-label installer/supervisor fixture. |

Verbatim plan rows supporting that mapping follow. All are from
`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, blob
SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`.

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:819`:

```text
            <tr><td class="id">AT-006</td><td>Environment and shell isolation</td><td>Daemon, plist/effective launchd state, supervisor, and worker contain only approved variables; ambient Codex state/credentials are absent; login-shell requests, packaged bypass, and non-positive timeout hatches fail closed; any root-local scratch is <code>0700</code>, ignored, and cleaned.</td><td>G-ENV</td></tr>
```

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:831-832`:

```text
            <tr><td class="id">AT-018</td><td>Actual-turn sandbox sentinel</td><td>Under the exact <code>turn/start</code> policy used by production, deterministic primary/descendant probes cannot read sibling/home canaries or write outside the canonical root, <code>/tmp</code>, or <code>$TMPDIR</code>. Only enumerated immutable runtime read roots work; <code>includePlatformDefaults</code> is false. The probe is not substituted with <code>command/exec</code>, and client-initiated shell/process methods are unreachable.</td><td>G-SBX/G-SENT/G-ENV</td></tr>
            <tr><td class="id">AT-019</td><td>Protected material round trip</td><td>Every declared protected rule—including mid-path globs—compiles and denies read, file change, and shell write for primary and descendants; any unrepresentable rule blocks workspace-write.</td><td>G-PROT/G4</td></tr>
```

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:838,840,844`:

```text
            <tr><td class="id">AT-025</td><td>Secret and ceremony-data scan</td><td>Synthetic bearer/JWT/OAuth/cookie/query-token/API-key values are absent from renderer and every sink. Synthetic <code>userCode</code>/<code>verificationUrl</code> appear only in the live typed login-UI channel and are absent from <code>.jsonl</code>, both SSE hops, persistence, telemetry, replay, event/crash/daemon/supervisor/App Server/launchd logs, screenshots/support bundles, and—after ceremony disposal—the DOM, reachable application state, queued IPC buffers, and captures; the dedicated view is destroyed. No nondeterministic V8 physical-zeroization claim is made.</td><td>G-WIRE</td></tr>
            <tr><td class="id">AT-027</td><td>No Chirality topology cap</td><td>The delegation-capable profile enables exact-pin native multi-agent behavior, leaves concurrency unset, and supplies no Chirality child allowlist, model restriction, or fixed topology; upstream limits remain visible.</td><td>G-ROLE/G4</td></tr>
            <tr><td class="id">AT-031</td><td>Semantic failure containment</td><td>Even a deliberately nonconforming role fixture cannot expand filesystem/network/approval/process authority.</td><td>G4</td></tr>
```

The three quoted rows above are non-contiguous in the source: line 838,
line 840, and line 844 respectively; each line is reproduced independently by
the cited command.

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:848,851-852`:

```text
            <tr><td class="id">AT-035</td><td>v2 data and two-job migration</td><td>Representative v2 data opens without destructive rewrite. The journalled installer transitions from the existing daemon-only plist to daemon plus process-supervisor plists, verifies both effective jobs, and rolls back a failure without orphaning or duplicating either.</td><td>G-HELPER/G5/G7</td></tr>
            <tr><td class="id">AT-038</td><td>Unsigned preparation artifact</td><td>Config explicitly pins no signing identity and disables identity auto-discovery; CI/local artifact is non-distributable, carries no production signing/notary credentials, and passes package fan-in.</td><td>G5</td></tr>
            <tr><td class="id">AT-039</td><td>Release identity freeze</td><td>Source SHA, dependency lock, resolved Electron version, App Server digest, generated schema/config digest, notices/SBOM, procedure, and version bind before signing.</td><td>G6a</td></tr>
```

The quoted rows above are non-contiguous in the source: line 848, then lines
851-852; each range is reproduced independently by the cited command.

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:860-864`:

```text
            <tr><td class="id">AT-047</td><td>Preparation nested-byte survival</td><td><code>desktop:dist</code> preserves accepted App Server and Electron/CLI host bytes and inventories every existing or absent nested signature.</td><td>G5</td></tr>
            <tr><td class="id">AT-048</td><td>Finder activation during work</td><td>After verified two-job migration, Finder activation while a primary/descendant turn runs creates no duplicate worker. If restart/upgrade retires the generation, affected turns terminalize and subsequent work starts fresh; no reattachment claim is tested.</td><td>G-HELPER/G-DUAL/G-SIG</td></tr>
            <tr><td class="id">AT-049</td><td>Packaged sandbox enforcement</td><td>The hardened-runtime, non-App-Sandbox package denies positive escape probes for primary and descendants with <code>includePlatformDefaults: false</code>. Parsed-but-ineffective policy, missing immutable runtime roots, or an incompatible Electron fuse/entitlement fails.</td><td>G-SBX</td></tr>
            <tr><td class="id">AT-050</td><td>Role-profile isolation</td><td>Exact-pin schema and readback prove delegation-capable versus optional explicit-Agent-2 config layering, including <code>features.multi_agent</code>, pin-specific <code>features.multi_agent_v2</code>, and <code>agents.enabled</code> precedence. A failed bounded profile withholds only that explicit entry mode.</td><td>G-ROLE</td></tr>
            <tr><td class="id">AT-051</td><td>Credential signature transition</td><td>App Server keyring and Electron <code>safeStorage</code> survive unsigned/ad hoc→self-signed preparation identity A→B and, in the actual release lane only, Developer ID N→N+1 where safe; otherwise the UI reports a distinguishable non-destructive reauthentication or decrypt-failed state. No plaintext or silent loss occurs.</td><td>G-KEY/G7</td></tr>
```

AT-050 is quoted for neighboring context but is not assigned to a baseline row
in the table above.

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:866-871`:

```text
            <tr><td class="id">AT-053</td><td>Governed basis and shared-runtime gate</td><td>Accepted carriers map every Root/App amendment, held binding, RQG §13 Shared Runtime Gate condition, DEL-02-06 REQ-027/exclusion, D-APP-103 interaction, and open Task Management item without inferring authority or closure.</td><td>G0/G0.5/G1</td></tr>
            <tr><td class="id">AT-054</td><td>Two-job install transaction</td><td>The runtime-control IPC is the only installer entry; sender authorization, staged plists, journal, load/print verification, rollback, upgrade, uninstall, and obsolete-job cleanup are proven for the daemon and Delegated Harness Process Supervisor.</td><td>G-HELPER/G-CSP/G-DUAL</td></tr>
            <tr><td class="id">AT-055</td><td>Retirement failure recovery</td><td>Failure is injected before and after each journal, terminal append, status update, process kill, and cleanup boundary. Recovery is idempotent, never reports false success, and cannot admit root work until closure is backchecked.</td><td>G-SIG</td></tr>
            <tr><td class="id">AT-056</td><td>Private <code>CODEX_HOME</code> lifecycle</td><td>Creation, permissions, backup exclusion, upgrade, root removal, logout, credential-store behavior, and deletion are defined and tested without token copying/symlinking or cross-root project/config exposure.</td><td>G-DUAL/G-ENV/G-KEY</td></tr>
            <tr><td class="id">AT-057</td><td>Credential IPC and typed storage states</td><td>All six credential IPC handlers reject unauthorized senders. Storage returns distinct <code>missing</code>, <code>storageUnavailable</code>, <code>decryptFailed</code>, and <code>available</code> states; preparation identity-transition tests prove UI/remediation behavior without production signing.</td><td>G-CSP/G-KEY</td></tr>
            <tr><td class="id">AT-058</td><td>Signed Electron-as-Node host</td><td>Preparation and exact signed bytes prove the packaged Electron binary can execute the bundled <code>--runtime-supervisor</code> entry under <code>ELECTRON_RUN_AS_NODE=1</code>, preserve required fuses/entitlements, receive launchd signals, maintain its private socket, and terminate worker process groups. Failure invokes a separately approved helper design, not an Electron-spawned workaround.</td><td>G-HELPER/G-SBX/G6b/G7</td></tr>
```

AT-055 and AT-056 are quoted for neighboring context but are not assigned to a
baseline row in the table above. No AT row is claimed passed by this report.
