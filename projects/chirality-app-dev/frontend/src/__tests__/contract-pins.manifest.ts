/**
 * Contract-pin manifest (ORN-01 consolidation pattern).
 *
 * Each entry pins governed byte-level invariants of one target file. These
 * pins were relocated verbatim from six previously separate pin-test files:
 *
 *   - src/__tests__/scripts/harness-premerge-workflow.test.ts   (deleted)
 *   - src/__tests__/scripts/build-network-policy.test.ts        (deleted)
 *   - src/__tests__/scripts/dmg-packaging-policy.test.ts        (pin bodies removed)
 *   - src/__tests__/scripts/validate-harness-section9.test.ts   (pin bodies removed)
 *   - src/__tests__/docs/reliance-boundary-register.test.ts     (pin bodies removed)
 *   - src/__tests__/lib/domain-profile-registry.test.ts         (byte-sync pins removed)
 *
 * Only the mechanism moved; every pinned string is preserved. Structural
 * (non-substring) assertions remain in their original files.
 *
 * Pin kinds:
 *   contains / notContains  raw substring presence/absence in the file bytes
 *   notMatches              regex must not match the file bytes
 *   jsonPathContains        parse file as JSON, walk jsonPath; strings use
 *                           substring containment, arrays use membership
 *   jsonPathEquals          parse file as JSON, walk jsonPath, strict equality
 */

export type ContractPin =
  | { kind: 'contains'; value: string }
  | { kind: 'notContains'; value: string }
  | { kind: 'notMatches'; pattern: string }
  | { kind: 'jsonPathContains'; jsonPath: string[]; value: string }
  | { kind: 'jsonPathEquals'; jsonPath: string[]; value: string };

export type ContractPinTarget = {
  /** Target file path, relative to the frontend workspace root. */
  file: string;
  /** What contract these pins hold and where they came from. */
  description: string;
  /**
   * Skip this target (with a logged warning) instead of failing when the
   * file does not exist — for monorepo-level files that are absent when the
   * frontend is hosted outside the monorepo.
   */
  allowMissing?: boolean;
  pins: ContractPin[];
};

export const CONTRACT_PIN_MANIFEST: ContractPinTarget[] = [
  {
    file: '../../../.github/workflows/harness-premerge.yml',
    description:
      'ORN-01 gate set: repo-root harness premerge workflow runs on pull requests without provider secrets (from harness-premerge-workflow.test.ts)',
    pins: [
      { kind: 'contains', value: 'pull_request:' },
      { kind: 'contains', value: 'CHIRALITY_HARNESS_PROVIDER: stub' },
      {
        kind: 'contains',
        value:
          'echo "HARNESS_PROJECT_ROOT=${RUNNER_TEMP}/chirality-harness-workroot" >> "${GITHUB_ENV}"'
      },
      { kind: 'contains', value: 'runtime/package-lock.json' },
      { kind: 'contains', value: 'working-directory: runtime' },
      { kind: 'contains', value: 'npm run build' },
      { kind: 'contains', value: 'dist-electron/main.js --runtime-daemon' },
      { kind: 'contains', value: '--no-sandbox' },
      { kind: 'contains', value: 'dist-runtime/chirality-cli.mjs' },
      {
        kind: 'contains',
        value: '--manifest "${GITHUB_WORKSPACE}/projects/chirality-app-dev/chirality.project.json"'
      },
      { kind: 'contains', value: 'echo "CHIRALITY_RUNTIME_TOKEN_FILE=${project_token}"' },
      {
        kind: 'contains',
        value: 'echo "HARNESS_PROJECT_ROOT=${GITHUB_WORKSPACE}/projects/chirality-app-dev"'
      },
      { kind: 'notContains', value: '${{ runner.temp }}' },
      { kind: 'contains', value: 'mkdir -p "${HARNESS_PROJECT_ROOT}"' },
      { kind: 'contains', value: '"${REPO_ROOT}/AGENTS.md" "${REPO_ROOT}/CLAUDE.md"' },
      { kind: 'contains', value: 'npm run instruction-root:integrity --' },
      { kind: 'contains', value: 'run: npm run validate:release-quality' },
      { kind: 'contains', value: 'artifacts/harness/section8/latest/summary.json' },
      { kind: 'contains', value: 'artifacts/harness/release-quality/latest/summary.json' },
      {
        kind: 'contains',
        value: 'artifacts/harness/instruction-root-integrity/latest/summary.json'
      },
      { kind: 'notContains', value: 'secrets.ANTHROPIC_API_KEY' },
      { kind: 'notContains', value: 'command -v claude' }
    ]
  },
  {
    file: 'scripts/validate-release-quality-evidence.mjs',
    description:
      'ORN-01 enforcement point: the release-quality wrapper runs the full test suite and typecheck as evidence commands, and validates the Section 9 manifest (from harness-premerge-workflow.test.ts and validate-harness-section9.test.ts). If the test/typecheck commands leave the wrapper, the premerge workflow must regain standalone steps.',
    pins: [
      {
        kind: 'contains',
        value: "runCommand({ id: 'full_test', args: ['run', 'test', '--', '--testTimeout=15000'] })"
      },
      { kind: 'contains', value: "runCommand({ id: 'typecheck', args: ['run', 'typecheck'] })" },
      { kind: 'contains', value: 'SECTION9_MANIFEST_PATH' },
      {
        kind: 'contains',
        value: 'Section 9 manifest must contain the exact governed 16-ID inventory.'
      },
      { kind: 'contains', value: "'sourceReferences', 'evidenceFiles'" },
      { kind: 'contains', value: "'warnings', 'blockers'" }
    ]
  },
  {
    file: 'scripts/validate-harness-section9.mjs',
    description:
      'Section 9 runner emits the stable manifest artifact and enforces the governed inventory (from validate-harness-section9.test.ts)',
    pins: [
      { kind: 'contains', value: "'manifest.json'" },
      { kind: 'contains', value: 'HARNESS_SECTION9_MANIFEST_PATH=' },
      { kind: 'contains', value: 'exact governed 16-ID inventory' }
    ]
  },
  {
    file: 'package.json',
    description:
      'Build/packaging policy pins: telemetry disabled, unsigned desktop packaging, proof commands registered, monorepo symlinks excluded (from build-network-policy.test.ts and dmg-packaging-policy.test.ts)',
    pins: [
      { kind: 'jsonPathContains', jsonPath: ['scripts', 'dev:next'], value: 'NEXT_TELEMETRY_DISABLED=1' },
      { kind: 'jsonPathContains', jsonPath: ['scripts', 'build'], value: 'NEXT_TELEMETRY_DISABLED=1' },
      {
        kind: 'jsonPathEquals',
        jsonPath: ['scripts', 'proof:secret-scan'],
        value: 'node ./scripts/scan-secret-evidence.mjs'
      },
      {
        kind: 'jsonPathEquals',
        jsonPath: ['scripts', 'proof:packaged-security'],
        value: 'node ./scripts/run-packaged-security-proof.mjs'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'desktop:pack'],
        value: 'CSC_IDENTITY_AUTO_DISCOVERY=false'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'desktop:dist'],
        value: 'CSC_IDENTITY_AUTO_DISCOVERY=false'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'desktop:pack'],
        value: 'desktop:verify-dependencies'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'desktop:dist'],
        value: 'desktop:verify-dependencies'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'desktop:verify-dependencies'],
        value: 'verify-packaged-dependency-boundary.mjs'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'harness:validate:agentsdk-packaged-proof'],
        value: 'verify-packaged-agent-sdk-runtime.mjs'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'pi:lock-integrity'],
        value: 'normalize-pi-lock-integrity.mjs'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'pi:supply-chain'],
        value: 'verify-pi-supply-chain.mjs'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['scripts', 'harness:validate:pi-packaged-proof'],
        value: 'run-packaged-pi-runtime-proof.mjs'
      },
      {
        kind: 'jsonPathContains',
        jsonPath: ['build', 'files'],
        value: '!node_modules/@chirality/**'
      }
    ]
  },
  {
    file: 'electron/main.ts',
    description:
      'Renderer network-policy hardening: no auto-update or GitHub release checks; fail-closed egress allowlist interception with redacted diagnostics (from build-network-policy.test.ts)',
    pins: [
      { kind: 'notMatches', pattern: '\\bautoUpdater\\b' },
      { kind: 'notContains', value: 'releases/latest' },
      { kind: 'notContains', value: 'api.github.com/repos' },
      { kind: 'contains', value: 'session.webRequest.onBeforeRequest' },
      { kind: 'contains', value: "RUNTIME_NETWORK_POLICY_ID = 'REQ-NET-001'" },
      { kind: 'contains', value: "'NETWORK_POLICY_VIOLATION'" },
      { kind: 'contains', value: "'INVALID_URL'" },
      { kind: 'contains', value: "['http://*/*', 'https://*/*', 'ws://*/*', 'wss://*/*']" },
      { kind: 'contains', value: "'api.anthropic.com'" },
      { kind: 'contains', value: "'localhost'" },
      { kind: 'contains', value: "'127.0.0.1'" },
      { kind: 'contains', value: "'[::1]'" },
      { kind: 'contains', value: 'Blocked renderer outbound request by network policy' },
      { kind: 'contains', value: 'destination: summarizeRendererRequestDestination(details.url)' },
      { kind: 'contains', value: 'hostname: parsed.hostname' },
      { kind: 'contains', value: 'port: parsed.port || null' },
      { kind: 'contains', value: 'protocol: parsed.protocol' },
      { kind: 'notContains', value: 'url: details.url' }
    ]
  },
  {
    file: 'electron/main.ts',
    description:
      'G-CSP renderer hardening (DEL-09-06-V3-01): every window is created from the hardening policy (asserted context isolation, no Node integration, sandbox), the egress policy and the window policy (window-open denial, navigation containment, CSP) are installed per window, the packaged renderer server sets the CSP at the source, and every privileged IPC module receives the exact renderer origin',
    pins: [
      { kind: 'contains', value: "webPreferences: rendererWebPreferences({ preload: path.join(__dirname, 'preload.js') })" },
      { kind: 'notContains', value: 'contextIsolation: false' },
      { kind: 'notContains', value: 'nodeIntegration: true' },
      { kind: 'notContains', value: 'sandbox: false' },
      { kind: 'notContains', value: 'webSecurity: false' },
      { kind: 'notContains', value: 'allowRunningInsecureContent' },
      { kind: 'notContains', value: 'nodeIntegrationInWorker' },
      { kind: 'notContains', value: 'nodeIntegrationInSubFrames' },
      { kind: 'notContains', value: 'enableRemoteModule' },
      { kind: 'notContains', value: 'webviewTag' },
      { kind: 'contains', value: 'registerRendererEgressPolicy(window);' },
      { kind: 'contains', value: 'installRendererWindowPolicy(window, {' },
      { kind: 'contains', value: 'openExternal: (url) => shell.openExternal(url)' },
      { kind: 'contains', value: "mode: app.isPackaged ? 'packaged' : 'development'" },
      { kind: 'contains', value: 'res.setHeader(CONTENT_SECURITY_POLICY_HEADER, contentSecurityPolicy);' },
      { kind: 'contains', value: 'const rendererOrigin = new URL(rendererUrl).origin;' },
      { kind: 'contains', value: 'registerApiKeyHandlers(runtimeClient, {' },
      { kind: 'contains', value: 'registerRuntimeControlHandlers({' }
    ]
  },
  {
    file: 'electron/renderer-window-policy.ts',
    description:
      'Renderer window hardening policy (DEL-09-06-V3-01): explicit web preferences, deny-all window-open, renderer-origin-only navigation on both navigation events, CSP without eval outside development and closed to frames/objects/embedding',
    pins: [
      { kind: 'contains', value: 'contextIsolation: true,' },
      { kind: 'contains', value: 'nodeIntegration: false,' },
      { kind: 'contains', value: 'sandbox: true' },
      { kind: 'contains', value: "return { action: 'deny' };" },
      { kind: 'contains', value: "return { action: 'deny', external: false, reason: 'SCHEME_NOT_HTTP' };" },
      { kind: 'contains', value: "['will-navigate', 'will-redirect'] as const" },
      { kind: 'contains', value: 'event.preventDefault();' },
      { kind: 'contains', value: "parsed.origin === 'null' || parsed.origin !== rendererOrigin" },
      { kind: 'contains', value: "\"default-src 'self'\"" },
      { kind: 'contains', value: "`script-src 'self' 'unsafe-inline'${development ? \" 'unsafe-eval'\" : ''}`" },
      { kind: 'contains', value: "\"frame-src 'none'\"" },
      { kind: 'contains', value: "\"object-src 'none'\"" },
      { kind: 'contains', value: "\"frame-ancestors 'none'\"" },
      { kind: 'contains', value: "\"base-uri 'self'\"" },
      { kind: 'contains', value: "\"form-action 'self'\"" },
      { kind: 'contains', value: "const connectSources = [\"'self'\"];" },
      { kind: 'notContains', value: 'api.anthropic.com:*' },
      { kind: 'contains', value: "callback(responseHeaders === null ? {} : { responseHeaders });" },
      { kind: 'contains', value: 'window.webContents.session' },
      { kind: 'contains', value: "CHIRALITY_EGRESS_LAYER_PROBE_URL" },
      { kind: 'contains', value: "parsed.protocol !== 'http:' && parsed.protocol !== 'https:'" },
      { kind: 'contains', value: 'webRequest.onHeadersReceived(' },
      { kind: 'notContains', value: 'unsafe-hashes' },
      { kind: 'notContains', value: "'*'" }
    ]
  },
  {
    file: 'electron/api-key-ipc.ts',
    description:
      'Credential IPC sender authorization (DEL-09-06-V3-01): all six channels adopt the shared origin policy and deny with a typed, secret-free result',
    pins: [
      { kind: 'contains', value: "from './ipc-sender-policy'" },
      { kind: 'contains', value: 'isAuthorizedSender(event, rendererOrigin)' },
      { kind: 'contains', value: "'Credential request was denied'" },
      { kind: 'contains', value: 'if (denied(event, API_KEY_STORE_CHANNEL))' },
      { kind: 'contains', value: 'if (denied(event, API_KEY_REMOVE_CHANNEL))' },
      { kind: 'contains', value: 'if (denied(event, API_KEY_STATUS_CHANNEL))' },
      { kind: 'contains', value: 'if (denied(event, PROVIDER_API_KEY_STORE_CHANNEL))' },
      { kind: 'contains', value: 'if (denied(event, PROVIDER_API_KEY_REMOVE_CHANNEL))' },
      { kind: 'contains', value: 'if (denied(event, PROVIDER_API_KEY_STATUS_CHANNEL))' },
      { kind: 'contains', value: 'sender: describeIpcSender(event)' },
      { kind: 'notContains', value: 'senderFrame.url' }
    ]
  },
  {
    file: 'electron/runtime-control-ipc.ts',
    description:
      'Runtime-control IPC keeps the shared sender policy (no private copy that could drift)',
    pins: [
      { kind: 'contains', value: "from './ipc-sender-policy'" },
      { kind: 'contains', value: 'isAuthorizedSender(event, deps.rendererOrigin)' },
      { kind: 'notContains', value: 'function isAuthorizedSender' }
    ]
  },
  {
    file: 'electron/api-key-storage.ts',
    description:
      'Typed safeStorage states are non-destructive (DEL-04-05-V3-01): a failed read never rewrites, truncates, or deletes the blob, and never falls back to another store',
    pins: [
      { kind: 'contains', value: "return { state: 'storageUnavailable' };" },
      { kind: 'contains', value: "return { state: 'decryptFailed' };" },
      { kind: 'contains', value: "return { state: 'missing' };" },
      { kind: 'contains', value: "return { state: 'available', value: decrypted };" },
      { kind: 'contains', value: 'Preserve corrupted blobs for operator investigation.' },
      { kind: 'notContains', value: 'writeFileSync' },
      { kind: 'notContains', value: 'keytar' }
    ]
  },
  {
    file: 'scripts/run-network-policy-proof.mjs',
    description:
      'Scripted agentSdk network proof mode exists without broadening egress (from build-network-policy.test.ts)',
    pins: [
      { kind: 'contains', value: "'--provider'" },
      { kind: 'contains', value: "'--scripted-agent-sdk'" },
      { kind: 'contains', value: 'CHIRALITY_HARNESS_PROVIDER' },
      { kind: 'contains', value: 'CHIRALITY_AGENTSDK_SCRIPTED_PROOF' },
      {
        kind: 'contains',
        value: "endpoint.class !== 'loopback' && endpoint.class !== 'allowlisted'"
      },
      { kind: 'contains', value: "'api.anthropic.com'" }
    ]
  },
  {
    file: 'scripts/run-packaged-security-proof.mjs',
    description:
      'Packaged artifact proof identity-binds real bundle bytes, exercises isolated safeStorage, and captures fail-closed renderer egress',
    pins: [
      { kind: 'contains', value: "schema: 'chirality-packaged-security-proof/v1'" },
      { kind: 'contains', value: "CHIRALITY_USER_DATA: userDataRoot" },
      { kind: 'contains', value: "CHIRALITY_SKIP_CLI_LAUNCHER: '1'" },
      { kind: 'contains', value: "client.storeCredential('anthropic', fixtureCredential)" },
      { kind: 'contains', value: 'nonAllowlistedOutboundTcp' },
      { kind: 'contains', value: 'retainedMetadataLeakFindings' },
      { kind: 'contains', value: "CHIRALITY_RENDERER_SECURITY_PROBE: '1'" },
      { kind: 'contains', value: 'CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_URL' },
      { kind: 'contains', value: 'rendererSecurityProofPass === true' },
      { kind: 'contains', value: "'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'" },
      { kind: 'contains', value: "'[egress-layer-probe]'" },
      { kind: 'notContains', value: 'CSC_LINK' },
      { kind: 'notContains', value: 'APPLE_ID' }
    ]
  },
  {
    file: 'scripts/scan-secret-evidence.mjs',
    description: 'Secret-scan proof stays redacted (from build-network-policy.test.ts)',
    pins: [
      { kind: 'contains', value: 'valueSha256' },
      { kind: 'contains', value: 'rawSecretValuesWritten' },
      { kind: 'contains', value: 'actual_environment_secret_value' },
      {
        kind: 'contains',
        value:
          'environmentSecretInputs: envSecrets.map(({ variants: _variants, ...entry }) => entry)'
      }
    ]
  },
  {
    file: '../docs/harness/reliance_boundary_register.md',
    description:
      'Reliance boundary register keeps the governed schema, boundary inventory, Section 9 index, and PEC evidence framing (from reliance-boundary-register.test.ts)',
    pins: [
      { kind: 'contains', value: '| BoundaryID |' },
      { kind: 'contains', value: '| BoundaryCategory |' },
      { kind: 'contains', value: '| ProductSemantic |' },
      { kind: 'contains', value: '| SourceRefs |' },
      { kind: 'contains', value: '| EnforcementOwner |' },
      { kind: 'contains', value: '| EnforcementSurface |' },
      { kind: 'contains', value: '| ValidationID |' },
      { kind: 'contains', value: '| ResidualRisk |' },
      { kind: 'contains', value: '| DecisionStatus |' },
      { kind: 'contains', value: '| RB-ENGINE |' },
      { kind: 'contains', value: '| RB-AUDIT |' },
      { kind: 'contains', value: '| RB-PERMISSION |' },
      { kind: 'contains', value: '| RB-FILESYSTEM |' },
      { kind: 'contains', value: '| RB-LIFECYCLE |' },
      { kind: 'contains', value: '| RB-TRANSCRIPT |' },
      { kind: 'contains', value: '| RB-SETTINGS |' },
      { kind: 'contains', value: '| RB-SUBAGENT |' },
      { kind: 'contains', value: '| RB-HUMAN-GATE |' },
      { kind: 'contains', value: '| RB-TOOL-SURFACE |' },
      { kind: 'contains', value: '| RB-HOOKS |' },
      { kind: 'contains', value: '| RB-REDACTION |' },
      { kind: 'contains', value: '| RB-FALLBACK |' },
      { kind: 'contains', value: '| `section9.reliance_boundary_register` |' },
      { kind: 'contains', value: '| `section9.sdk_session_link_resume` |' },
      { kind: 'contains', value: '| `section9.domain_profile_validation` |' },
      { kind: 'contains', value: 'does not authorize apply behavior' },
      { kind: 'notContains', value: 'Not implemented in the current Section 9 script' },
      {
        kind: 'contains',
        value: 'docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md'
      },
      { kind: 'contains', value: 'projects/pec/docs/PRD.md' }
    ]
  },
  {
    // The registry's marker byte strings are themselves pinned against
    // DOMAIN_ENGINE_PROFILE_REGISTRY in domain-profile-registry.test.ts; these
    // entries pin the same byte strings against the LIVE profile files so
    // fixture drift can never mask a V-9-class defect (the byte-sync guard
    // formerly in domain-profile-registry.test.ts). allowMissing preserves
    // that guard's skip-when-not-in-monorepo behavior.
    file: '../../../_DomainEngines/profiles/open_pipe_stress.yaml',
    description:
      'Live open_pipe_stress profile keeps the D-APP-51 registry identity and deterministic-tool markers (byte-sync guard from domain-profile-registry.test.ts)',
    allowMissing: true,
    pins: [
      { kind: 'contains', value: 'id: "open_pipe_stress"' },
      { kind: 'contains', value: '- id: "completeness_checker"' },
      { kind: 'contains', value: '- id: "rule_check_runner"' },
      { kind: 'contains', value: '- id: "headless_runner"' }
    ]
  },
  {
    file: '../../../_DomainEngines/profiles/pec.yaml',
    description:
      'Live pec profile keeps the D-APP-51 registry identity marker (byte-sync guard from domain-profile-registry.test.ts)',
    allowMissing: true,
    pins: [{ kind: 'contains', value: 'id: "pec"' }]
  }
];
