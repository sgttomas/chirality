import { createHash } from 'node:crypto';
import { constants } from 'node:fs';
import { mkdtemp, realpath, rm, stat, lstat, writeFile, open } from 'node:fs/promises';
import { join, relative, isAbsolute, dirname, resolve } from 'node:path';

export interface CodexContainmentOptions {
  canonicalRoot: string;
  codexHome: string;
  privateDirectory: string;
  /** Trusted operator configuration only. Never populate from an RPC/client request.
   * This is a provenance record, not an authentication mechanism. */
  providerNetworkConsent?: { approvedBy: string; approvalReference: string };
}

const contained = (root: string, candidate: string): boolean => {
  const rel = relative(root, candidate);
  return rel === '' || (!rel.startsWith('..' + '/') && rel !== '..' && !isAbsolute(rel));
};
const quote = (value: string): string => {
  if (/[\x00-\x1f\x7f]/u.test(value)) throw new Error('Sandbox path contains control characters');
  return JSON.stringify(value);
};

/** macOS host boundary. Fail closed on unsupported hosts; never fall back to raw spawn.
 * Exact supply verification and trusted operator consent verification belong to the caller.
 * Provider-enabled network is inherited by subprocesses: Codex config below is not a
 * mechanism-proven subprocess network boundary in that mode. */
export async function prepareCodexContainment(options: CodexContainmentOptions) {
  if (process.platform !== 'darwin') throw new Error('Codex containment requires macOS sandbox-exec');
  await stat('/usr/bin/sandbox-exec');
  const root = await realpath(options.canonicalRoot);
  if (root !== options.canonicalRoot || root === '/') throw new Error('Project root must be canonical and bounded');
  const privateDirectory = await realpath(options.privateDirectory);
  const codexHome = await realpath(options.codexHome);
  if (privateDirectory !== options.privateDirectory || codexHome !== options.codexHome || !contained(privateDirectory, codexHome)) {
    throw new Error('CODEX_HOME must be canonical and inside the private directory');
  }
  for (const dir of [privateDirectory, codexHome]) {
    const metadata = await stat(dir);
    if (!metadata.isDirectory() || (metadata.mode & 0o077) !== 0 || metadata.uid !== process.getuid?.()) {
      throw new Error('Private directories must be owned by this user and inaccessible to other users');
    }
  }
  if (contained(privateDirectory, root)) throw new Error('Private directory must not enclose the project');
  const consent = options.providerNetworkConsent;
  if (consent && (!consent.approvedBy.trim() || !consent.approvalReference.trim())) {
    throw new Error('Provider network requires an explicit trusted operator consent record');
  }
  const sessionDirectory = await mkdtemp(join(privateDirectory, 'containment-'));
  const sandboxProfilePath = join(sessionDirectory, 'launch.sb');
  const readable = ['/System', '/usr', '/bin', '/sbin', '/Library/Apple', '/private/var/db/dyld', root, privateDirectory];
  const profile = [
    '(version 1)', '(allow default)',
    `(deny file-read-data (require-not (require-any (literal "/") ${readable.map(path => `(subpath ${quote(path)})`).join(' ')} (literal "/dev/null") (literal "/dev/urandom") (literal "/dev/random"))))`,
    `(deny file-write* (require-not (require-any (subpath ${quote(root)}) (subpath ${quote(privateDirectory)}) (literal "/dev/null"))))`,
    '(deny mach-lookup (global-name "com.apple.securityd"))',
    ...(consent ? [] : ['(deny network*)']),
    '',
  ].join('\n');
  try { await writeFile(sandboxProfilePath, profile, { mode: 0o600, flag: 'wx' }); }
  catch (error) { await rm(sessionDirectory, { recursive: true, force: true }); throw error; }
  const config = {
    sandbox_mode: 'workspace-write',
    sandbox_workspace_write: { writable_roots: [root], network_access: false, exclude_slash_tmp: true, exclude_tmpdir_env_var: true },
    approval_policy: 'never',
    features: { plugins: false },
    allow_login_shell: false,
    cli_auth_credentials_store: 'file',
    check_for_update_on_startup: false,
    web_search: 'disabled',
    analytics: { enabled: false },
    feedback: { enabled: false },
  } as const;
  return {
    sandboxProfilePath,
    args: ['-f', sandboxProfilePath],
    /** Caller verifies the supply digest/signature before calling this path gate. */
    launchArguments: async (verifiedExecutablePath: string): Promise<string[]> => {
      const executable = await realpath(verifiedExecutablePath);
      if (executable !== verifiedExecutablePath || (!contained(root, executable) && !contained(privateDirectory, executable)) || !(await stat(executable)).isFile()) {
        throw new Error('Verified Codex executable must be canonical and within the project or private directory');
      }
      return ['-f', sandboxProfilePath, executable];
    },
    environment: {
      HOME: privateDirectory, CODEX_HOME: codexHome, TMPDIR: sessionDirectory,
      PATH: '/usr/bin:/bin:/usr/sbin:/sbin', LANG: 'en_US.UTF-8',
    } satisfies NodeJS.ProcessEnv,
    config,
    providerNetworkEnabled: Boolean(consent),
    commandNetworkBoundary: consent ? 'configuration-only' as const : 'outer-sandbox-denied' as const,
    /** Only our fresh session directory is removed; supplied account/private files survive. */
    cleanup: async () => { await rm(sessionDirectory, { recursive: true, force: true }); },
  };
}



// Resolve a not-yet-created protected literal without admitting symlink aliases.
async function canonicalProtectedLiteral(path: string): Promise<string> {
  if (!isAbsolute(path) || resolve(path) !== path) throw new Error('Protected literal must be normalized and absolute');
  let ancestor = path;
  while (true) {
    try {
      const metadata = await lstat(ancestor);
      if (await realpath(ancestor) !== ancestor || (ancestor !== path && !metadata.isDirectory())) throw new Error('Protected literal has an aliased or non-directory ancestor');
      return path;
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code !== 'ENOENT') throw error;
      // A dangling symlink is an existing entry, not a safe future literal.
      try { await lstat(ancestor); throw new Error('Protected literal has a dangling alias'); }
      catch (probe) { if ((probe as NodeJS.ErrnoException).code !== 'ENOENT') throw probe; }
      const parent = dirname(ancestor);
      if (parent === ancestor) throw new Error('Protected literal has no canonical ancestor');
      ancestor = parent;
    }
  }
}
// Preserve deny patterns for the exact native matcher; do not expand a snapshot
// into an expressible subset. Exact parser acceptance and action probes are gates.
async function canonicalProtectedRule(root: string, rule: string): Promise<string> {
  if (!/[\*?\[\]]/u.test(rule)) return canonicalProtectedLiteral(rule);
  if (!isAbsolute(rule) || resolve(rule) !== rule || !rule.startsWith(root + '/')) throw new Error('Protected pattern must be normalized inside canonical project');
  const relativeRule = rule.slice(root.length + 1);
  const segments = relativeRule.split('/');
  const firstGlob = segments.findIndex(segment => /[\*?\[\]]/u.test(segment));
  const prefix = firstGlob === 0 ? root : join(root, ...segments.slice(0, firstGlob));
  await canonicalProtectedLiteral(prefix);
  return rule;
}

export interface CodexNativePolicyOptions extends CodexContainmentOptions {
  commandNetworkPosture?: 'off' | 'ask-per-destination' | 'on';
  /** Existing canonical system-code files or directories. Enumeration is provisional until G-SBX. */
  immutableReadRoots: string[];
  /** Includes broker control root plus canonical project literals/native deny patterns. */
  protectedPaths: string[];
}

/** Compile a named native action policy for a trusted exact App Server host.
 * This function performs no vendor execution and provides no kernel-proof claim.
 * Caller authenticates provider consent and verifies exact supply, effective config,
 * and the selected profile on every thread/turn. Never expose args to client override. */
export async function prepareCodexNativePolicy(options: CodexNativePolicyOptions) {
  if (process.platform !== 'darwin') throw new Error('Native policy requires macOS Seatbelt verification');
  const commandNetworkPosture = options.commandNetworkPosture ?? 'off';
  if (!['off', 'ask-per-destination', 'on'].includes(commandNetworkPosture)) throw new Error('Unsupported command network posture');
  const commandNetworkEnabled = commandNetworkPosture === 'on';
  const approvalPolicy = commandNetworkPosture === 'ask-per-destination' ? 'on-request' as const : 'never' as const;
  // Exact 0.149.0 requires BOTH the network_proxy feature gate and the named
  // network table; the table alone enables network access without starting a proxy.
  // An empty destination map prompts under on-request; on explicitly permits all
  // destinations through the same proxy. Actual kernel enforcement is a test limb.
  const network = commandNetworkPosture === 'off' ? { enabled: false } : {
    enabled: true, proxy_url: 'http://127.0.0.1:0', enable_socks5: true,
    socks_url: 'http://127.0.0.1:0', enable_socks5_udp: true, allow_upstream_proxy: false,
    dangerously_allow_non_loopback_proxy: false, dangerously_allow_all_unix_sockets: false,
    mode: 'full', domains: commandNetworkPosture === 'on' ? { '*': 'allow' } : {},
    unix_sockets: {}, allow_local_binding: false,
  };
  const root = await realpath(options.canonicalRoot);
  const privateDirectory = await realpath(options.privateDirectory);
  const codexHome = await realpath(options.codexHome);
  if (root !== options.canonicalRoot || root === '/' || privateDirectory !== options.privateDirectory || codexHome !== options.codexHome) {
    throw new Error('Native policy paths must be canonical');
  }
  if (contained(root, privateDirectory) || contained(privateDirectory, root) || !contained(privateDirectory, codexHome)) {
    throw new Error('Native project and private account roots must be disjoint');
  }
  for (const path of [root, privateDirectory, codexHome]) {
    quote(path);
    if (/[\*?\[\]{}]/u.test(path)) throw new Error('Native permission paths may not contain glob syntax');
    const metadata = await stat(path);
    if (!metadata.isDirectory()) throw new Error('Native policy roots must be directories');
    if (path !== root && ((metadata.mode & 0o077) !== 0 || metadata.uid !== process.getuid?.())) {
      throw new Error('Native private directories must be owned and inaccessible to other users');
    }
  }
  if (options.providerNetworkConsent && (!options.providerNetworkConsent.approvedBy.trim() || !options.providerNetworkConsent.approvalReference.trim())) {
    throw new Error('Provider network requires trusted operator consent provenance');
  }
  const permittedSystemRoots = ['/System', '/usr', '/bin', '/sbin', '/Library/Apple', '/private/var/db/dyld'];
  const systemConfigurationLeaves = new Set(['/private/etc/ssl/openssl.cnf']);
  const immutableFiles: Array<{ path: string; sha256: string; size: number; mode: number; uid: number }> = [];
  const reads = [...new Set(options.immutableReadRoots)].sort();
  if (reads.length === 0) throw new Error('Explicit immutable runtime reads are required');
  for (const path of reads) {
    const metadata = await stat(path);
    if ((!permittedSystemRoots.some(base => contained(base, path)) && !systemConfigurationLeaves.has(path)) || await realpath(path) !== path || (!metadata.isDirectory() && !metadata.isFile()) || metadata.uid !== 0 || (metadata.mode & 0o022) !== 0 || (systemConfigurationLeaves.has(path) && !metadata.isFile())) {
      throw new Error('Immutable reads must be canonical enumerated system-code files or directories');
    }
    if (metadata.isFile()) {
      if (metadata.size > 32 * 1024 * 1024) throw new Error('Immutable file exceeds bounded identity read');
      const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
      try {
        const fields = ['ino', 'dev', 'size', 'mtimeMs', 'ctimeMs', 'mode', 'uid'] as const;
        const before = await handle.stat();
        if (!before.isFile() || before.uid !== 0 || (before.mode & 0o022) !== 0 || fields.some(key => before[key] !== metadata[key])) throw new Error('Immutable file changed during policy compilation');
        // Read at most the accepted size plus one byte, even if a privileged
        // updater grows the file during this observation.
        const buffer = Buffer.alloc(before.size + 1); let count = 0;
        while (count < buffer.length) { const read = await handle.read(buffer, count, buffer.length - count, count); if (read.bytesRead === 0) break; count += read.bytesRead; }
        const after = await handle.stat(); const current = await lstat(path);
        if (count !== before.size || !current.isFile() || current.isSymbolicLink() || await realpath(path) !== path || after.uid !== 0 || (after.mode & 0o022) !== 0 || fields.some(key => before[key] !== after[key] || after[key] !== current[key])) throw new Error('Immutable file changed during policy compilation');
        immutableFiles.push({ path, sha256: createHash('sha256').update(buffer.subarray(0, count)).digest('hex'), size: after.size, mode: after.mode, uid: after.uid });
      } finally { await handle.close(); }
    }
    if (contained(path, root) || contained(root, path) || contained(path, privateDirectory)) {
      throw new Error('Immutable reads overlap private or project roots');
    }
  }
  if (!options.protectedPaths.length) throw new Error('Explicit broker protection is required');
  if (!options.protectedPaths.some(path => path !== privateDirectory && contained(path, privateDirectory))) throw new Error('Protected paths must include enclosing broker control root');
  const denied = [...new Set([...options.protectedPaths, privateDirectory, join(root, '.codex')])].sort();
  for (const path of denied) {
    quote(path);
    if (await canonicalProtectedRule(root, path) !== path || contained(path, root)) {
      throw new Error('Protected literals must be canonical and may not enclose the project');
    }
    if (reads.some(read => contained(read, path) || contained(path, read))) {
      throw new Error('Protected control paths overlap immutable read roots');
    }
  }
  // A deterministic profile identity excludes ephemeral scratch names: scratch is
  // covered only by the canonical project grant, never by a global temp exception.
  const identity = { version: 5, approvalsReviewer: 'user', canonicalRoot: root, reads, immutableFiles, denied, commandNetworkPosture, networkProxyFeature: commandNetworkPosture !== 'off', network, approvalPolicy, commandNetwork: commandNetworkEnabled, includePlatformDefaults: false, loginShell: false };
  const policyDigest = createHash('sha256').update(JSON.stringify(identity)).digest('hex');
  const profileId = `chirality_${policyDigest.slice(0, 24)}`;
  const scratchDirectory = await mkdtemp(join(root, '.chirality-scratch-'));
  try { await writeFile(join(scratchDirectory, '.gitignore'), '*\n', { mode: 0o600, flag: 'wx' }); }
  catch (error) { await rm(scratchDirectory, { recursive: true, force: true }); throw error; }
  const expectedPermissions = { filesystem: Object.fromEntries([...reads.map(path => [path, 'read']), [root, 'write'], ...denied.map(path => [path, 'deny'])]), network };
  // Codex's -c key parser splits dotted strings without respecting quoted path
  // segments. Put path-bearing maps inside TOML inline values, never CLI keys.
  const inlineToml = (value: unknown): string => {
    if (typeof value === 'string' || typeof value === 'boolean') return JSON.stringify(value);
    if (Array.isArray(value)) return `[${value.map(inlineToml).join(',')}]`;
    if (value && typeof value === 'object') return `{${Object.entries(value).map(([key, item]) => `${quote(key)}=${inlineToml(item)}`).join(',')}}`;
    throw new Error('Unsupported native configuration value');
  };
  const entries: Array<[string, unknown]> = [
    ['approval_policy', approvalPolicy], ['approvals_reviewer', 'user'], ['sandbox_mode', 'workspace-write'], ['allow_login_shell', false],
    ['cli_auth_credentials_store', 'file'], ['check_for_update_on_startup', false], ['web_search', 'disabled'],
    ['sandbox_workspace_write.writable_roots', [root]], ['sandbox_workspace_write.network_access', commandNetworkEnabled],
    ['sandbox_workspace_write.exclude_slash_tmp', true], ['sandbox_workspace_write.exclude_tmpdir_env_var', true],
    ['features.network_proxy', commandNetworkPosture !== 'off'],
    ['features.plugins', false], ['features.remote_plugin', false], ['analytics.enabled', false], ['feedback.enabled', false],
    ['projects', { [root]: { trust_level: 'trusted' } }],
    ['permissions', { [profileId]: expectedPermissions }],
  ];
  const configOverrides = entries.map(([key, value]) => `${key}=${inlineToml(value)}`);
  const args = configOverrides.flatMap(value => ['-c', value]);
  const configToml = configOverrides.join('\n') + '\n';
  return {
    profileId, permissionProfile: profileId, policyDigest, configToml, configOverrides, args, scratchDirectory,
    expectedPermissions, approvalPolicy, immutableFiles,
    commandNetworkPosture,
    environment: { HOME: privateDirectory, CODEX_HOME: codexHome, TMPDIR: scratchDirectory, PATH: '/usr/bin:/bin:/usr/sbin:/sbin', LANG: 'en_US.UTF-8' } satisfies NodeJS.ProcessEnv,
    enforcementEvidence: 'NOT_PROVEN_G_SBX' as const,
    providerNetworkEnabled: Boolean(options.providerNetworkConsent),
    launchArguments: async (verifiedExecutablePath: string): Promise<string[]> => {
      if (await realpath(verifiedExecutablePath) !== verifiedExecutablePath || !contained(privateDirectory, verifiedExecutablePath) || !(await stat(verifiedExecutablePath)).isFile()) {
        throw new Error('Trusted exact executable must be canonical inside worker-private directory');
      }
      return [verifiedExecutablePath, ...args];
    },
    cleanup: async () => { await rm(scratchDirectory, { recursive: true, force: true }); },
  };
}
