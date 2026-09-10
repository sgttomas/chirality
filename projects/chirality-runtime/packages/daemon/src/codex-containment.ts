import { createHash } from 'node:crypto';
import { constants } from 'node:fs';
import { mkdtemp, readdir, realpath, rm, stat, lstat, writeFile, open } from 'node:fs/promises';
import { join, relative, isAbsolute, dirname, resolve } from 'node:path';
import { CHIRALITY_ROLE_NAMES } from '@chirality/runtime-contracts';
import { compareRuntimeUtf8V2, runtimeConformanceInstructionBundleDigest, verifyPackagedRuntimeBasisV2, type RuntimeConformanceArtifactInventorySelection } from '@chirality/runtime-core';
import { digestCodexPolicyInstanceV2, inspectCodexPolicyInstanceV2, type CodexPolicyInstanceV2, type RuntimePackagedPolicyBasisV2 } from './runtime-conformance-v2-admission.js';

export interface TrustedRuntimeReadRootBinding {
  path: string;
  readPaths: readonly string[];
  contentDigest: string;
  artifactInventory: RuntimeConformanceArtifactInventorySelection;
}
export interface TrustedRuntimeReadRootBindingV2 {
  path: string;
  readPaths: readonly string[];
  contentDigest: string;
  artifactInventory: RuntimePackagedPolicyBasisV2;
}
export interface CodexContainmentOptionsV2 extends Omit<CodexContainmentOptions, 'trustedRuntimeReadRoots' | 'purpose'> {
  trustedRuntimeReadRoots: readonly TrustedRuntimeReadRootBindingV2[];
}

export interface CodexContainmentOptions {
  /** Internal auth-only purpose. Never populated from worker or client input. */
  purpose?: "worker" | "trusted-login" | "trusted-supplier";
  canonicalRoot: string;
  codexHome: string;
  privateDirectory: string;
  /** Trusted operator configuration only. Never populate from an RPC/client request.
   * This is a provenance record, not an authentication mechanism. */
  providerNetworkConsent?: { approvedBy: string; approvalReference: string };
  /** Host-selected bundle/tool roots revalidated by Runtime conformance before work. */
  trustedRuntimeReadRoots?: readonly TrustedRuntimeReadRootBinding[];
}

const contained = (root: string, candidate: string): boolean => {
  const rel = relative(root, candidate);
  return rel === '' || (!rel.startsWith('..' + '/') && rel !== '..' && !isAbsolute(rel));
};
const quote = (value: string): string => {
  if (/[\x00-\x1f\x7f]/u.test(value)) throw new Error('Sandbox path contains control characters');
  return JSON.stringify(value);
};
async function trustedRootContentDigest(root:string,readPaths:readonly string[]):Promise<string>{
  const rootBefore=await lstat(root,{bigint:true});
  const records:{path:string;sha256:string;size:number}[]=[];let count=0,total=0;
  const walk=async(path:string):Promise<void>=>{if(++count>50_000)throw new Error('Trusted Runtime read root is too large');
    const info=await lstat(path);if(info.isSymbolicLink()||await realpath(path)!==path)throw new Error('Trusted Runtime read root contains an alias');
    if(info.isDirectory()){if((info.mode&0o022)!==0)throw new Error('Trusted Runtime read root is publicly writable');for(const name of(await readdir(path)).sort())await walk(join(path,name));return;}
    if(!info.isFile()||(info.mode&0o022)!==0)throw new Error('Trusted Runtime read root contains an unsafe entry');
    const file=await open(path,constants.O_RDONLY|constants.O_NOFOLLOW);try{const before=await file.stat({bigint:true});if(!before.isFile())throw new Error('Trusted Runtime read root entry changed');const bytes=await file.readFile();const after=await file.stat({bigint:true}),current=await lstat(path,{bigint:true});for(const key of ['dev','ino','size','mtimeNs','ctimeNs','mode','uid','nlink'] as const)if(before[key]!==after[key]||before[key]!==current[key])throw new Error('Trusted Runtime read root entry changed');if(await realpath(path)!==path||BigInt(bytes.length)!==before.size)throw new Error('Trusted Runtime read root entry changed');total+=bytes.length;if(total>1_073_741_824)throw new Error('Trusted Runtime read root is too large');records.push({path:relative(root,path).split('\\').join('/'),sha256:createHash('sha256').update(bytes).digest('hex'),size:bytes.length});}finally{await file.close();}};
  for(const path of readPaths)await walk(path);
  const rootAfter=await lstat(root,{bigint:true});for(const key of ['dev','ino','size','mtimeNs','ctimeNs','mode','uid','nlink'] as const)if(rootBefore[key]!==rootAfter[key])throw new Error('Trusted Runtime read root changed');
  if(await realpath(root)!==root)throw new Error('Trusted Runtime read root changed');
  return createHash('sha256').update(JSON.stringify(records)).digest('hex');
}
export async function bindTrustedRuntimeReadRoot(path:string,artifactInventory:RuntimeConformanceArtifactInventorySelection):Promise<TrustedRuntimeReadRootBinding>{
  if(!isAbsolute(path)||resolve(path)!==path||await realpath(path)!==path)throw new Error('Trusted Runtime read root must be canonical');
  if(artifactInventory.kind!=='packaged-resources')throw new Error('Trusted Runtime instruction reads require a reviewed packaged artifact inventory');
  const inventoryRoot=join(artifactInventory.resourcesRoot,'instruction-root');
  if(path!==inventoryRoot)throw new Error('Trusted Runtime read root is outside the selected artifact inventory');
  const readPaths=[path];
  const expected=await runtimeConformanceInstructionBundleDigest(artifactInventory),observed=await trustedRootContentDigest(path,readPaths);
  if(observed!==expected||await runtimeConformanceInstructionBundleDigest(artifactInventory)!==expected)throw new Error('Trusted Runtime read root differs from its accepted inventory');
  return Object.freeze({path,readPaths:Object.freeze(readPaths),contentDigest:expected,artifactInventory:structuredClone(artifactInventory)});
}
export async function assertTrustedRuntimeReadRoot(binding:TrustedRuntimeReadRootBinding):Promise<void>{
  if(!binding||!/^[a-f0-9]{64}$/.test(binding.contentDigest))throw new Error('Trusted Runtime read root binding is invalid');
  const rebound=await bindTrustedRuntimeReadRoot(binding.path,binding.artifactInventory);
  if(rebound.contentDigest!==binding.contentDigest||JSON.stringify(rebound.readPaths)!==JSON.stringify(binding.readPaths))throw new Error('Trusted Runtime read root content changed');
}

/** macOS host boundary. Fail closed on unsupported hosts; never fall back to raw spawn.
 * Exact supply verification and trusted operator consent verification belong to the caller.
 * Provider-enabled network is inherited by subprocesses: Codex config below is not a
 * mechanism-proven subprocess network boundary in that mode. */
async function prepareCodexContainmentVersion(options: CodexContainmentOptions | (CodexContainmentOptionsV2 & { purpose: 'trusted-supplier' }), identityVersion: 1 | 2) {
  if (options.purpose !== undefined && options.purpose !== 'worker' && options.purpose !== 'trusted-login' && options.purpose !== 'trusted-supplier') throw new Error('Unsupported containment purpose');
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
  const trustedReads = [...(options.trustedRuntimeReadRoots ?? [])].sort((left, right) => identityVersion === 2 ? compareRuntimeUtf8V2(left.path, right.path) : left.path.localeCompare(right.path));
  for (const entry of trustedReads) {
    if (!entry || !/^[a-f0-9]{64}$/.test(entry.contentDigest) || !isAbsolute(entry.path) || resolve(entry.path) !== entry.path
      || await realpath(entry.path) !== entry.path || contained(root, entry.path) || contained(entry.path, root)
      || contained(privateDirectory, entry.path) || contained(entry.path, privateDirectory)) throw new Error('Trusted Runtime read root is not a disjoint conformance-bound path');
    const metadata = await stat(entry.path);
    if ((!metadata.isDirectory() && !metadata.isFile()) || (metadata.mode & 0o022) !== 0) throw new Error('Trusted Runtime read root must be a stable non-publicly-writable file or directory');
    if (identityVersion === 2) await assertTrustedRuntimeReadRootV2(entry as TrustedRuntimeReadRootBindingV2);
    else await assertTrustedRuntimeReadRoot(entry as TrustedRuntimeReadRootBinding);
  }
  const sessionDirectory = await mkdtemp(join(privateDirectory, 'containment-'));
  const sandboxProfilePath = join(sessionDirectory, 'launch.sb');
  const readable = ['/System', '/usr', '/bin', '/sbin', '/Library/Apple', '/private/var/db/dyld', root, privateDirectory, ...trustedReads.flatMap(entry => entry.readPaths)];
  const profile = [
    '(version 1)', '(allow default)',
    `(deny file-read-data (require-not (require-any (literal "/") ${readable.map(path => `(subpath ${quote(path)})`).join(' ')} (literal "/dev/null") (literal "/dev/urandom") (literal "/dev/random"))))`,
    `(deny file-write* (require-not (require-any (subpath ${quote(root)}) (subpath ${quote(privateDirectory)}) (literal "/dev/null"))))`,
    ...((options.purpose === 'trusted-login' || options.purpose === 'trusted-supplier') ? [] : ['(deny mach-lookup (global-name "com.apple.securityd"))']),
    ...(consent ? [] : ['(deny network*)']),
    '',
  ].join('\n');
  try { await writeFile(sandboxProfilePath, profile, { mode: 0o600, flag: 'wx' }); }
  catch (error) { await rm(sessionDirectory, { recursive: true, force: true }); throw error; }
  const preparedDirectory = identityVersion === 2 ? await lstat(sessionDirectory, { bigint: true }) : undefined;
  const preparedProfile = identityVersion === 2 ? await lstat(sandboxProfilePath, { bigint: true }) : undefined;
  const config = {
    sandbox_mode: 'workspace-write',
    sandbox_workspace_write: { writable_roots: [root], network_access: false, exclude_slash_tmp: true, exclude_tmpdir_env_var: true },
    approval_policy: 'never',
    features: { plugins: false, shell_snapshot: false },
    allow_login_shell: false,
    cli_auth_credentials_store: (options.purpose === 'trusted-login' || options.purpose === 'trusted-supplier') ? 'keyring' : 'file',
    check_for_update_on_startup: false,
    web_search: 'disabled',
    analytics: { enabled: false },
    feedback: { enabled: false },
  } as const;
  const outerPolicyDigest = createHash('sha256').update(JSON.stringify({
    schema: `chirality-codex-outer-policy/v${identityVersion}`, purpose: options.purpose ?? 'worker', root, privateDirectory, codexHome,
    trustedReads, profile, config, providerNetworkEnabled: Boolean(consent)
  })).digest('hex');
  return {
    sandboxProfilePath,
    args: ['-f', sandboxProfilePath],
    /** Caller verifies the supply digest/signature before calling this path gate. */
    launchArguments: async (verifiedExecutablePath: string): Promise<string[]> => {
      if (identityVersion === 2) {
        const directory = await lstat(sessionDirectory, { bigint: true }), profile = await lstat(sandboxProfilePath, { bigint: true });
        if (await realpath(sessionDirectory) !== sessionDirectory || await realpath(sandboxProfilePath) !== sandboxProfilePath
          || ['dev', 'ino', 'mode', 'uid'].some(key => directory[key as 'dev'] !== preparedDirectory![key as 'dev'])
          || ['dev', 'ino', 'mode', 'uid', 'size', 'mtimeNs', 'ctimeNs'].some(key => profile[key as 'dev'] !== preparedProfile![key as 'dev'])) throw new Error('Prepared outer allocation changed');
      }
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
    outerPolicyDigest,
    providerNetworkEnabled: Boolean(consent),
    commandNetworkBoundary: consent ? 'configuration-only' as const : 'outer-sandbox-denied' as const,
    /** Only our fresh session directory is removed; supplied account/private files survive. */
    cleanup: async () => { await rm(sessionDirectory, { recursive: true, force: true }); },
  };
}
/** Ordered projection of the closed login compiler config; the same values are
 * hashed and passed to App Server. Arrays remain TOML values, not path aliases. */
export function codexLoginConfigOverridesV2(config: Awaited<ReturnType<typeof prepareCodexContainmentV2>>['config']): readonly string[] {
  const entries: string[] = [];
  const visit = (value: unknown, key: string): void => {
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      for (const [name, item] of Object.entries(value)) visit(item, key ? `${key}.${name}` : name);
    } else entries.push(`${key}=${JSON.stringify(value)}`);
  };
  visit(config, '');
  return Object.freeze(entries);
}
export function prepareCodexContainment(options: CodexContainmentOptions) { return prepareCodexContainmentVersion(options, 1); }
export function prepareCodexContainmentV2(options: CodexContainmentOptions) { return prepareCodexContainmentVersion(options, 2); }

/** Reject supplier plaintext credential persistence in its private keyring home.
 * Call before launch and again after login/status transitions. */
export async function assertCodexKeyringHomeHasNoPlaintextCredentials(codexHome: string): Promise<void> {
  if (!isAbsolute(codexHome) || resolve(codexHome) !== codexHome || await realpath(codexHome) !== codexHome) throw new Error('Codex keyring home must be canonical');
  const metadata = await stat(codexHome);
  if (!metadata.isDirectory() || (metadata.mode & 0o077) !== 0 || metadata.uid !== process.getuid?.()) throw new Error('Codex keyring home must be owner-private');
  const credentialName = /^(?:\.?auth(?:[._-][^/]*)?\.json(?:[._-][^/]*)?|\.?auth\.json(?:[._-][^/]*)?)$/iu;
  for (const entry of await readdir(codexHome, { withFileTypes: true })) {
    if (credentialName.test(entry.name)) throw new Error('Plaintext Codex credential artifact is forbidden in keyring home');
  }
}

/** Trusted authenticated App Server outer boundary. Model-reachable shell and
 * file effects still require the separately bound native tool policy. */
export async function prepareCodexTrustedSupplierContainment(options: Omit<CodexContainmentOptions, 'purpose'>) {
  return prepareCodexContainment({ ...options, purpose: 'trusted-supplier' });
}
export async function prepareCodexTrustedSupplierContainmentV2(options: CodexContainmentOptionsV2) {
  return prepareCodexContainmentVersion({ ...options, purpose: 'trusted-supplier' }, 2);
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

function globSegmentMatches(pattern: string, value: string): boolean {
  let expression = '^';
  for (let index = 0; index < pattern.length; index++) {
    const character = pattern[index]!;
    if (character === '*') expression += '.*';
    else if (character === '?') expression += '.';
    else if (character === '[') {
      const end = pattern.indexOf(']', index + 1);
      if (end < 0) expression += '\\[';
      else { expression += pattern.slice(index, end + 1); index = end; }
    } else expression += character.replace(/[\\^$+?.()|{}]/g, '\\$&');
  }
  return new RegExp(expression + '$', 'u').test(value);
}

export interface CodexNativePolicyOptions extends CodexContainmentOptions {
  commandNetworkPosture?: 'off' | 'ask-per-destination' | 'on';
  /** Existing canonical system-code files or directories. Enumeration is provisional until G-SBX. */
  immutableReadRoots: string[];
  /** Canonical project subtrees that provider file tools may read but may not write. */
  readOnlyProjectPaths?: string[];
  /** Includes broker control root plus canonical project literals/native deny patterns. */
  protectedPaths: string[];
  nativeRoleConfiguration?: { digest: string; configOverrides: readonly string[] };
}

/** Compile a named native action policy for a trusted exact App Server host.
 * This function performs no vendor execution and provides no kernel-proof claim.
 * Caller authenticates provider consent and verifies exact supply, effective config,
 * and the selected profile on every thread/turn. Never expose args to client override. */
export async function prepareCodexNativePolicy(options: CodexNativePolicyOptions) {
  if (options.purpose !== undefined && options.purpose !== "worker") throw new Error("Native workers cannot select the trusted login purpose");
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
  const projectReads = [...new Set(options.readOnlyProjectPaths ?? [])].sort();
  for (const path of projectReads) {
    quote(path);
    if (/[*?\[\]{}]/u.test(path) || path === root || !contained(root, path) || await canonicalProtectedLiteral(path) !== path) {
      throw new Error('Read-only project paths must be canonical literal subtrees of the project');
    }
    for (const rule of denied) {
      if (!/[\*?\[\]]/u.test(rule)) {
        if (contained(rule, path) || contained(path, rule)) throw new Error('Read-only project paths overlap protected control paths');
        continue;
      }
      const segments = rule.slice(root.length + 1).split('/');
      const firstGlob = segments.findIndex(segment => /[\*?\[\]]/u.test(segment));
      const prefix = firstGlob <= 0 ? root : join(root, ...segments.slice(0, firstGlob));
      const overlaps = prefix === root
        ? globSegmentMatches(segments[0]!, relative(root, path).split('/')[0]!)
        : contained(prefix, path) || contained(path, prefix);
      if (overlaps) throw new Error('Read-only project paths overlap protected control patterns');
    }
  }
  const trustedRuntimeReads = [...(options.trustedRuntimeReadRoots ?? [])].sort((left, right) => left.path.localeCompare(right.path));
  for (const entry of trustedRuntimeReads) {
    if (!entry || !/^[a-f0-9]{64}$/.test(entry.contentDigest) || await realpath(entry.path) !== entry.path) throw new Error('Trusted Runtime read root is not conformance-bound');
    await assertTrustedRuntimeReadRoot(entry);
    const metadata = await stat(entry.path);
    if ((!metadata.isDirectory() && !metadata.isFile()) || (metadata.mode & 0o022) !== 0 || contained(root, entry.path) || contained(entry.path, root)
      || contained(privateDirectory, entry.path) || contained(entry.path, privateDirectory)) throw new Error('Trusted Runtime read root overlaps project/private custody or is writable by other users');
    for (const readPath of entry.readPaths) for (const deniedPath of denied) if (!/[\*?\[\]]/u.test(deniedPath) && (contained(deniedPath, readPath) || contained(readPath, deniedPath))) throw new Error('Trusted Runtime read root overlaps a deny path');
  }
  const nativeRoles = options.nativeRoleConfiguration;
  if (nativeRoles !== undefined) {
    const expectedPrefix = ['agents.enabled=true', 'features.multi_agent=true', 'features.multi_agent_v2=false', 'agents.max_depth=2'];
    if (!/^[a-f0-9]{64}$/.test(nativeRoles.digest) || !Array.isArray(nativeRoles.configOverrides)
      || nativeRoles.configOverrides.length !== expectedPrefix.length + CHIRALITY_ROLE_NAMES.length * 2
      || expectedPrefix.some((value, index) => nativeRoles.configOverrides[index] !== value)) throw new Error('Invalid trusted native role configuration');
    let index = expectedPrefix.length;
    for (const roleId of CHIRALITY_ROLE_NAMES) {
      const descriptionPrefix = `agents.${roleId}.description=`, filePrefix = `agents.${roleId}.config_file=`;
      const description = nativeRoles.configOverrides[index++]!, file = nativeRoles.configOverrides[index++]!;
      if (!description.startsWith(descriptionPrefix) || !file.startsWith(filePrefix)) throw new Error('Invalid trusted native role configuration');
      let parsedDescription: unknown, parsedFile: unknown;
      try { parsedDescription = JSON.parse(description.slice(descriptionPrefix.length)); parsedFile = JSON.parse(file.slice(filePrefix.length)); } catch { throw new Error('Invalid trusted native role configuration'); }
      if (typeof parsedDescription !== 'string' || !parsedDescription.trim() || Buffer.byteLength(parsedDescription) > 4096
        || typeof parsedFile !== 'string' || !isAbsolute(parsedFile) || resolve(parsedFile) !== parsedFile || !contained(privateDirectory, parsedFile)) throw new Error('Invalid trusted native role configuration');
    }
  }
  // A deterministic profile identity excludes ephemeral scratch names: scratch is
  // covered only by the canonical project grant, never by a global temp exception.
  const identity = { version: 9, shellSnapshot: false, approvalsReviewer: 'user', canonicalRoot: root, reads, projectReads, trustedRuntimeReads, immutableFiles, denied, commandNetworkPosture, networkProxyFeature: commandNetworkPosture !== 'off', network, approvalPolicy, commandNetwork: commandNetworkEnabled, includePlatformDefaults: false, loginShell: false,
    nativeRoles: nativeRoles === undefined ? null : { digest: nativeRoles.digest, configOverrides: [...nativeRoles.configOverrides] } };
  const policyDigest = createHash('sha256').update(JSON.stringify(identity)).digest('hex');
  const profileId = `chirality_${policyDigest.slice(0, 24)}`;
  const scratchDirectory = await mkdtemp(join(root, '.chirality-scratch-'));
  try { await writeFile(join(scratchDirectory, '.gitignore'), '*\n', { mode: 0o600, flag: 'wx' }); }
  catch (error) { await rm(scratchDirectory, { recursive: true, force: true }); throw error; }
  const expectedPermissions = { filesystem: Object.fromEntries([...reads.map(path => [path, 'read']), ...trustedRuntimeReads.flatMap(entry => entry.readPaths.map(path=>[path,'read'] as const)), [root, 'write'], ...projectReads.map(path => [path, 'read']), ...denied.map(path => [path, 'deny'])]), network };
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
    ['cli_auth_credentials_store', 'keyring'], ['check_for_update_on_startup', false], ['web_search', 'disabled'],
    ['sandbox_workspace_write.writable_roots', [root]], ['sandbox_workspace_write.network_access', commandNetworkEnabled],
    ['sandbox_workspace_write.exclude_slash_tmp', true], ['sandbox_workspace_write.exclude_tmpdir_env_var', true],
    ['features.network_proxy', commandNetworkPosture !== 'off'],
    // Snapshot creation launches its own login shell before tool sandboxing.
    ['features.shell_snapshot', false],
    ['features.plugins', false], ['features.remote_plugin', false], ['analytics.enabled', false], ['feedback.enabled', false],
    ['projects', { [root]: { trust_level: 'trusted' } }],
    ['permissions', { [profileId]: expectedPermissions }],
  ];
  const configOverrides = entries.map(([key, value]) => `${key}=${inlineToml(value)}`);
  if (nativeRoles) configOverrides.push(...nativeRoles.configOverrides);
  const args = configOverrides.flatMap(value => ['-c', value]);
  const configToml = configOverrides.join('\n') + '\n';
  return {
    profileId, permissionProfile: profileId, policyDigest, configToml, configOverrides, args, scratchDirectory,
    expectedPermissions, approvalPolicy, immutableFiles,
    commandNetworkPosture, nativeRoleConfiguration: nativeRoles === undefined ? undefined : Object.freeze({ digest: nativeRoles.digest, configOverrides: Object.freeze([...nativeRoles.configOverrides]) }),
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

export interface CodexNativePolicyOptionsV2 extends Omit<CodexNativePolicyOptions, 'trustedRuntimeReadRoots' | 'purpose'> {
  purpose: 'worker';
  executablePath: string;
  nativeAddonPath: string;
  trustedRuntimeReadRoots: readonly TrustedRuntimeReadRootBindingV2[];
  toolRuntime: { codexSelfExecutablePath: string; requiresSandboxedFileSystem: true; requiresSandboxedFileStreaming: true };
}

async function assertTrustedRuntimeReadRootV2(binding: TrustedRuntimeReadRootBindingV2): Promise<void> {
  const inventory = binding.artifactInventory;
  if (!inventory || inventory.schema !== 'chirality-runtime-packaged-basis/v2' || binding.path !== join(inventory.resourcesRoot, 'instruction-root')
    || binding.readPaths.length < 1 || binding.readPaths.length > 32 || !binding.readPaths.every(path => path === binding.path || contained(binding.path, path))) throw new Error('Trusted Runtime v2 read root is outside its packaged basis');
  const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot: inventory.resourcesRoot });
  if (verified.inventoryPath !== inventory.inventoryPath || verified.payloadManifestPath !== inventory.payloadManifestPath
    || verified.inventorySha256 !== inventory.outerInventorySha256 || verified.payloadDigest !== inventory.payloadDigest) throw new Error('Trusted Runtime v2 packaged basis changed');
  const records = verified.payload.entries.filter((entry): entry is Extract<typeof entry, {type:'file'}> => entry.type === 'file' && entry.relativePath.startsWith('instruction-root/'))
    .map(entry => ({ path: entry.relativePath.slice('instruction-root/'.length), sha256: entry.sha256, size: entry.size }));
  const observed = createHash('sha256').update(`${JSON.stringify(records)}\n`).digest('hex');
  if (observed !== binding.contentDigest) throw new Error('Trusted Runtime v2 instruction content changed');
}
export async function bindTrustedRuntimeReadRootV2(path: string, artifactInventory: RuntimePackagedPolicyBasisV2): Promise<TrustedRuntimeReadRootBindingV2> {
  const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot: artifactInventory.resourcesRoot });
  if (path !== join(verified.resourcesRoot, 'instruction-root') || verified.inventoryPath !== artifactInventory.inventoryPath || verified.payloadManifestPath !== artifactInventory.payloadManifestPath
    || verified.inventorySha256 !== artifactInventory.outerInventorySha256 || verified.payloadDigest !== artifactInventory.payloadDigest) throw new Error('Trusted Runtime v2 packaged basis changed');
  const records = verified.payload.entries.filter((entry): entry is Extract<typeof entry, {type:'file'}> => entry.type === 'file' && entry.relativePath.startsWith('instruction-root/'))
    .map(entry => ({ path: entry.relativePath.slice('instruction-root/'.length), sha256: entry.sha256, size: entry.size }));
  const binding = Object.freeze({ path, readPaths: Object.freeze([path]), contentDigest: createHash('sha256').update(`${JSON.stringify(records)}\n`).digest('hex'), artifactInventory: structuredClone(artifactInventory) });
  await assertTrustedRuntimeReadRootV2(binding);
  return binding;
}

type CodexNativePolicyProjectionBase = Pick<Awaited<ReturnType<typeof prepareCodexNativePolicy>>, 'immutableFiles' | 'expectedPermissions' | 'approvalPolicy' | 'configOverrides'>;

/** Deterministic native-10 projection used after the filesystem compiler has
 * established its base permissions and immutable-file observations. */
export function compileCodexNativePolicyProjectionV2(policyValue: CodexPolicyInstanceV2, base: CodexNativePolicyProjectionBase) {
  const policyInstance = inspectCodexPolicyInstanceV2(policyValue);
  const entries = Object.entries(base.expectedPermissions.filesystem).map(([path, permission]) => [path, permission] as [string, typeof permission]);
  for (const binding of policyInstance.trustedRuntimeReadRoots) for (const path of binding.readPaths) entries.push([path, 'read']);
  entries.sort((left, right) => compareRuntimeUtf8V2(left[0], right[0]));
  if (entries.some((entry, index) => index > 0 && entries[index - 1]![0] === entry[0])) throw new Error('Native v2 permission mapping collides');
  const expectedPermissions = { filesystem: Object.fromEntries(entries), network: structuredClone(base.expectedPermissions.network) };
  const nativeIdentity = { version: 10, policyInstance, immutableFiles: structuredClone(base.immutableFiles), expectedPermissions, approvalPolicy: base.approvalPolicy };
  const policyDigest = createHash('sha256').update(`${JSON.stringify(nativeIdentity)}\n`).digest('hex');
  const profileId = `chirality_${policyDigest.slice(0, 24)}`;
  const inlineToml = (value: unknown): string => {
    if (typeof value === 'string' || typeof value === 'boolean') return JSON.stringify(value);
    if (Array.isArray(value)) return `[${value.map(inlineToml).join(',')}]`;
    if (value && typeof value === 'object') return `{${Object.entries(value).map(([key, item]) => `${JSON.stringify(key)}=${inlineToml(item)}`).join(',')}}`;
    throw new Error('Unsupported native configuration value');
  };
  const configOverrides = [...base.configOverrides];
  const permissionIndex = configOverrides.findIndex(value => value.startsWith('permissions='));
  if (permissionIndex < 0) throw new Error('Native v2 permissions configuration is unavailable');
  configOverrides[permissionIndex] = `permissions=${inlineToml({ [profileId]: expectedPermissions })}`;
  return Object.freeze({ profileId, permissionProfile: profileId, policyDigest, policyInstance, policyInstanceDigest: digestCodexPolicyInstanceV2(policyInstance),
    expectedPermissions: Object.freeze(expectedPermissions), configOverrides: Object.freeze(configOverrides), args: Object.freeze(configOverrides.flatMap(value => ['-c', value])), configToml: `${configOverrides.join('\n')}\n` });
}

/** Additive native-10 compiler. The v1 compiler above remains byte-for-byte compatible. */
export async function prepareCodexNativePolicyV2(options: CodexNativePolicyOptionsV2) {
  const ordered = (values: readonly string[]) => values.every((value, index) => index === 0 || compareRuntimeUtf8V2(values[index - 1]!, value) < 0);
  if (options.purpose !== 'worker' || options.toolRuntime.codexSelfExecutablePath !== options.executablePath
    || options.toolRuntime.requiresSandboxedFileSystem !== true || options.toolRuntime.requiresSandboxedFileStreaming !== true
    || !ordered(options.immutableReadRoots) || !ordered(options.protectedPaths) || !ordered(options.readOnlyProjectPaths ?? [])
    || options.trustedRuntimeReadRoots.length !== 1 || !ordered(options.trustedRuntimeReadRoots[0]!.readPaths)) throw new Error('Native v2 policy inputs are not exact and canonically ordered');
  for (const binding of options.trustedRuntimeReadRoots) await assertTrustedRuntimeReadRootV2(binding);
  const legacy = await prepareCodexNativePolicy({
    purpose: 'worker', canonicalRoot: options.canonicalRoot, privateDirectory: options.privateDirectory, codexHome: options.codexHome,
    providerNetworkConsent: options.providerNetworkConsent, commandNetworkPosture: options.commandNetworkPosture,
    immutableReadRoots: [...options.immutableReadRoots], protectedPaths: [...options.protectedPaths], readOnlyProjectPaths: options.readOnlyProjectPaths === undefined ? undefined : [...options.readOnlyProjectPaths],
    nativeRoleConfiguration: options.nativeRoleConfiguration
  });
  try {
    const policyInstance = inspectCodexPolicyInstanceV2({
      schema: 'chirality-codex-policy-instance/v2', outerPurpose: 'trusted-supplier', nativePurpose: 'worker',
      canonicalRoot: options.canonicalRoot, privateDirectory: options.privateDirectory, codexHome: options.codexHome,
      executablePath: options.executablePath, nativeAddonPath: options.nativeAddonPath,
      providerNetworkConsent: structuredClone(options.providerNetworkConsent!), commandNetworkPosture: options.commandNetworkPosture ?? 'off',
      immutableReadRoots: [...options.immutableReadRoots], protectedPaths: [...options.protectedPaths], readOnlyProjectPaths: [...(options.readOnlyProjectPaths ?? [])],
      trustedRuntimeReadRoots: structuredClone(options.trustedRuntimeReadRoots), toolRuntime: structuredClone(options.toolRuntime),
      nativeRoleConfiguration: options.nativeRoleConfiguration === undefined ? null : structuredClone(options.nativeRoleConfiguration)
    });
    const scratchIdentity = await lstat(legacy.scratchDirectory, { bigint: true });
    return Object.freeze({ ...legacy, ...compileCodexNativePolicyProjectionV2(policyInstance, legacy),
      async revalidateScratch(): Promise<void> {
        const current = await lstat(legacy.scratchDirectory, { bigint: true });
        if (await realpath(legacy.scratchDirectory) !== legacy.scratchDirectory || ['dev', 'ino', 'mode', 'uid'].some(key => current[key as 'dev'] !== scratchIdentity[key as 'dev'])) throw new Error('Prepared native allocation changed');
      }
    });
  } catch (error) { await legacy.cleanup(); throw error; }
}
