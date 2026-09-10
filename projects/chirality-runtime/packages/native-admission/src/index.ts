import { createRequire } from "node:module";
import { isAbsolute, normalize } from "node:path";
import { Readable, Writable } from "node:stream";
import type { RuntimeAdmissionLease } from "@chirality/runtime-core";

export type NativeUnavailableReason = "platform-unsupported" | "api-unavailable" | "filesystem-unqualified" | "path-unsafe" | "lock-contended" | "inode-mismatch" | "descriptor-closure-unqualified" | "spawn-failed" | "wait-unavailable" | "native-package-unqualified" | "host-xpc-unavailable" | "host-xpc-requirement-invalid" | "host-xpc-config-invalid" | "host-xpc-frame-invalid" | "host-xpc-closed" | "host-xpc-busy";
export type NativeAuthorityResult<T> = { state: "available"; value: T } | { state: "unavailable"; reason: NativeUnavailableReason };
export interface NativeSupplierExit { exitCode: number | null; signal: number | null }
interface RawLease { device: bigint; inode: bigint; held: boolean; created: boolean; close(): void }
interface RawChild {
  pid?: number; read(): Promise<Buffer>; write(bytes: Buffer): Promise<void>; closeInput(): void;
  terminate(): void; kill(): void; wait(): Promise<NativeSupplierExit>;
  observeLeader?(): Promise<NativeSupplierExit>; reapLeader?(): Promise<NativeSupplierExit>; groupRetired?(): boolean;
}
type RawHostEvent = { type: "admitted"|"invalidated"|"open"|"finish"|"ping"|"challenge"|"grant"|"pong"|"closed"; connectionId?: string; requestId?: string; reason?: string; replyToken?: bigint; generation?: string; sequence?: bigint; ok?: boolean; challenge?: Buffer; hostNonce?: Buffer; proof?: Buffer; bearer?: Buffer };
interface RawHostPort { serverChallenge(token: bigint,requestId: string,challenge: Buffer,generation: string): void;serverGrant(token: bigint,requestId: string,bearer: Buffer,generation: string): void;clientPong(token: bigint,requestId: string,sequence: bigint): void;clientOpen(requestId: string): void;clientFinish(requestId: string,hostNonce: Buffer,proof: Buffer): void;serverPing(connectionId:string,requestId: string,sequence: bigint): void;closeConnection(connectionId: string): void;close(): Promise<void> }
interface Binding { acquire(directory: string, name: string): RawLease; spawnSupplier(executable: string, args: readonly string[], secret: Buffer, cwd?: string, environment?: readonly string[], processGroup?: boolean): RawChild; createHostXpcPort?(server:boolean,peerRequirement:string,expectedEuid:number,onEvent:(event:RawHostEvent)=>void):RawHostPort;hostXpcService?:string }
export interface NativeSupplierSpawnOptions { cwd: string; environment: Readonly<Record<"HOME" | "CODEX_HOME" | "TMPDIR" | "PATH" | "LANG", string>>; processGroup: true }
interface NativeSupplierPipes { readonly stdin: Writable; readonly stdout: Readable; terminate(): void; kill(): void; closeInput(): void }
export interface NativeSupplierChild extends NativeSupplierPipes { readonly pid?: number; wait(): Promise<NativeSupplierExit> }
export interface NativeGroupedSupplierChild extends NativeSupplierPipes { readonly pid: number; observeLeader(): Promise<NativeSupplierExit>; reapLeader(): Promise<NativeSupplierExit>; groupRetired(): boolean }
export interface NativeAdmissionBinding {
  acquire(directory: string): NativeAuthorityResult<RuntimeAdmissionLease>;
  /** Historical non-grouped transport retained for controlled probes. */
  spawnSupplier(executable: string, args: readonly string[], secret: Buffer): NativeAuthorityResult<NativeSupplierChild>;
  /** Production candidate transport with explicit cwd, closed env and owned group. */
  spawnGroupedSupplier(executable: string, args: readonly string[], secret: Buffer, options: NativeSupplierSpawnOptions): NativeAuthorityResult<NativeGroupedSupplierChild>;
  createHostXpcServer(config: HostXpcServerConfig): NativeAuthorityResult<HostXpcServerPort>;
  createHostXpcClient(config: HostXpcClientConfig): NativeAuthorityResult<HostXpcClientPort>;
}

export const HOST_XPC_SERVICE = "com.chirality.app.runtime.account-host" as const;
export const HOST_XPC_MAX_FRAME_BYTES = 4096 as const;
export type HostXpcInvalidationReason = "peer-invalidated"|"peer-interrupted"|"peer-requirement-rejected"|"protocol-invalid"|"lease-closed"|"delivery-unavailable";
export interface HostXpcChallenge { requestId:string;challenge:Buffer;generation:string }
export interface HostXpcFinish { connectionId:string;requestId:string;hostNonce:Buffer;proof:Buffer }
export interface HostXpcGrant { requestId:string;bearer:Buffer;generation:string;scopes:readonly ["account:read","account:control"] }
export interface HostXpcServerConfig { peerRequirement:string;expectedEuid:number;onAdmitted(connectionId:string):void;onInvalidated(connectionId:string,reason:HostXpcInvalidationReason):void;onCeremonyOpen(input:{connectionId:string;requestId:string}):Promise<HostXpcChallenge>|HostXpcChallenge;onCeremonyFinish(input:HostXpcFinish):Promise<HostXpcGrant>|HostXpcGrant }
export interface HostXpcClientConfig { peerRequirement:string;expectedEuid:number;onInvalidated(reason:HostXpcInvalidationReason):void;onPing(input:{requestId:string;sequence:bigint}):Promise<{requestId:string;sequence:bigint}>|{requestId:string;sequence:bigint} }
export interface HostXpcServerPort { readonly service:typeof HOST_XPC_SERVICE;ping(connectionId:string,input:{requestId:string;sequence:bigint}):Promise<{requestId:string;sequence:bigint}>;closeConnection(connectionId:string,reason:HostXpcInvalidationReason):Promise<void>;close():Promise<void> }
export interface HostXpcClientPort { readonly service:typeof HOST_XPC_SERVICE;provision(input:{requestId:string;onChallenge(challenge:HostXpcChallenge):Promise<{requestId:string;hostNonce:Buffer;proof:Buffer}>|{requestId:string;hostNonce:Buffer;proof:Buffer}}):Promise<HostXpcGrant>;close():Promise<void> }

function unavailable<T>(reason: NativeUnavailableReason): NativeAuthorityResult<T> { return { state: "unavailable", reason }; }
const reasons: readonly string[] = ["platform-unsupported", "api-unavailable", "filesystem-unqualified", "path-unsafe", "lock-contended", "inode-mismatch", "descriptor-closure-unqualified", "spawn-failed", "wait-unavailable", "native-package-unqualified", "host-xpc-unavailable", "host-xpc-requirement-invalid", "host-xpc-config-invalid", "host-xpc-frame-invalid", "host-xpc-closed", "host-xpc-busy"];
function translate<T>(fn: () => T): NativeAuthorityResult<T> { try { return { state: "available", value: fn() }; } catch (error) { const reason = error && typeof error === "object" && "code" in error ? error.code : undefined; return unavailable(typeof reason === "string" && reasons.includes(reason) ? reason as NativeUnavailableReason : "native-package-unqualified"); } }
function path(value: unknown): asserts value is string { if (typeof value !== "string" || !isAbsolute(value) || normalize(value) !== value || Buffer.byteLength(value) > 4095 || /[\x00-\x1f]/.test(value)) throw Object.assign(new Error("invalid-native-path"), { code: "path-unsafe" }); }
function spawnOptions(value: NativeSupplierSpawnOptions): { cwd: string; environment: string[] } {
  if (!value || typeof value !== "object" || Array.isArray(value) || Object.keys(value).sort().join(",") !== "cwd,environment,processGroup" || value.processGroup !== true) throw new Error("invalid-native-bootstrap");
  path(value.cwd);
  const environment = value.environment;
  const keys = ["CODEX_HOME", "HOME", "LANG", "PATH", "TMPDIR"] as const;
  if (!environment || typeof environment !== "object" || Array.isArray(environment) || Object.keys(environment).sort().join(",") !== keys.join(",")) throw new Error("invalid-native-bootstrap");
  for (const key of ["CODEX_HOME", "HOME", "TMPDIR"] as const) path(environment[key]);
  if (environment.PATH !== "/usr/bin:/bin:/usr/sbin:/sbin" || environment.LANG !== "en_US.UTF-8") throw new Error("invalid-native-bootstrap");
  return { cwd: value.cwd, environment: keys.map(key => `${key}=${environment[key]}`) };
}
function validateExit(result: NativeSupplierExit): NativeSupplierExit {
  if (!result || Object.keys(result).sort().join(",") !== "exitCode,signal" || !(result.exitCode === null || Number.isInteger(result.exitCode)) || !(result.signal === null || Number.isInteger(result.signal)) || (result.exitCode === null) === (result.signal === null)) throw new Error("wait-unavailable");
  return result;
}
function pipes(child: RawChild): NativeSupplierPipes {
  let reading = false;
  const stdout = new Readable({ read() { if (reading) return; reading = true; void child.read().then(bytes => { reading = false; if (!Buffer.isBuffer(bytes)) throw new Error("invalid-native-read"); this.push(bytes.length ? bytes : null); }, () => { reading = false; this.destroy(new Error("native-read-unavailable")); }); } });
  const stdin = new Writable({ write(chunk: Buffer, _encoding, callback) { void child.write(Buffer.from(chunk)).then(() => callback(), () => callback(new Error("native-write-unavailable"))); }, final(callback) { try { child.closeInput(); callback(); } catch { callback(new Error("native-input-unavailable")); } } });
  return { stdin, stdout, closeInput: () => { stdin.end(); }, terminate: () => child.terminate(), kill: () => child.kill() };
}
function hostId(value:unknown): asserts value is string { if(typeof value!=="string"||value.length<1||value.length>96||Buffer.byteLength(value)>96||!/^[\x21-\x7e]+$/.test(value)) throw Object.assign(new Error("invalid-host-frame"),{code:"host-xpc-frame-invalid"}); }
function secret(value:unknown): asserts value is Buffer { if(!Buffer.isBuffer(value)||value.length!==32) throw Object.assign(new Error("invalid-host-secret"),{code:"host-xpc-frame-invalid"}); }
function generation(value:unknown): asserts value is bigint { if(typeof value!=="bigint"||value<0n) throw Object.assign(new Error("invalid-host-counter"),{code:"host-xpc-frame-invalid"}); }
function daemonGeneration(value:unknown): asserts value is string { if(typeof value!=="string"||!/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/.test(value))throw Object.assign(new Error("invalid-daemon-generation"),{code:"host-xpc-frame-invalid"}); }
function hostConfig(value:{peerRequirement:string;expectedEuid:number}) { if(!value||typeof value!=="object"||typeof value.peerRequirement!=="string"||!value.peerRequirement.length||Buffer.byteLength(value.peerRequirement)>4096||/[\x00-\x1f]/.test(value.peerRequirement)||!Number.isSafeInteger(value.expectedEuid)||value.expectedEuid<0||value.expectedEuid>0xffffffff) throw Object.assign(new Error("invalid-host-config"),{code:"host-xpc-config-invalid"}); }
const invalidationReasons:readonly HostXpcInvalidationReason[]=["peer-invalidated","peer-interrupted","peer-requirement-rejected","protocol-invalid","lease-closed","delivery-unavailable"];
function supportedReason(value:unknown):HostXpcInvalidationReason|undefined{return typeof value==="string"&&invalidationReasons.includes(value as HostXpcInvalidationReason)?value as HostXpcInvalidationReason:undefined;}
function supportedReplyReason(value:unknown):HostXpcInvalidationReason|undefined{const why=supportedReason(value);return why!=="lease-closed"&&why!=="delivery-unavailable"?why:undefined;}
function reason(value:unknown):HostXpcInvalidationReason { return supportedReason(value)??"peer-invalidated"; }
function deferred<T>(){let resolve!:(value:T)=>void,reject!:(error:Error)=>void;const promise=new Promise<T>((a,b)=>{resolve=a;reject=b;});return{promise,resolve,reject};}
function redactedError(code="host-xpc-unavailable"){return Object.assign(new Error("Host XPC unavailable"),{code});}

function hostServer(binding:Binding,config:HostXpcServerConfig):HostXpcServerPort {
  hostConfig(config);if(typeof binding.createHostXpcPort!=="function"||binding.hostXpcService!==HOST_XPC_SERVICE)throw redactedError();let closed:Promise<void>|undefined,live=true;const epochs=new Map<string,number>(),ceremonyGenerations=new Map<string,string>(),pongs=new Map<string,{connectionId:string;pending:ReturnType<typeof deferred<{requestId:string;sequence:bigint}>>}>();
  let raw!:RawHostPort;const onEvent=(event:RawHostEvent)=>{void(async()=>{try{
    if(event.type==="closed"){live=false;epochs.clear();ceremonyGenerations.clear();for(const value of pongs.values())value.pending.reject(redactedError("delivery-unavailable"));pongs.clear();return;}
    if(event.type==="admitted"){hostId(event.connectionId);if(!live)return;epochs.set(event.connectionId,0);config.onAdmitted(event.connectionId);return;}
    if(event.type==="invalidated"){hostId(event.connectionId);epochs.delete(event.connectionId);ceremonyGenerations.delete(event.connectionId);for(const [id,value] of pongs)if(value.connectionId===event.connectionId){value.pending.reject(redactedError());pongs.delete(id);}config.onInvalidated(event.connectionId,reason(event.reason));return;}
    if(event.type==="open"){hostId(event.connectionId);hostId(event.requestId);generation(event.replyToken);const epoch=epochs.get(event.connectionId);if(!live||epoch===undefined)return;const output=await config.onCeremonyOpen({connectionId:event.connectionId,requestId:event.requestId});if(!live||epochs.get(event.connectionId)!==epoch)return;hostId(output.requestId);if(output.requestId!==event.requestId)throw redactedError("host-xpc-frame-invalid");secret(output.challenge);daemonGeneration(output.generation);ceremonyGenerations.set(event.connectionId,output.generation);const copy=Buffer.from(output.challenge);try{raw.serverChallenge(event.replyToken,output.requestId,copy,output.generation);}finally{copy.fill(0);}return;}
    if(event.type==="finish"){hostId(event.connectionId);hostId(event.requestId);generation(event.replyToken);secret(event.hostNonce);secret(event.proof);const epoch=epochs.get(event.connectionId);if(!live||epoch===undefined)return;const nonce=Buffer.from(event.hostNonce),proof=Buffer.from(event.proof);event.hostNonce.fill(0);event.proof.fill(0);let output:HostXpcGrant;try{output=await config.onCeremonyFinish({connectionId:event.connectionId,requestId:event.requestId,hostNonce:nonce,proof});}finally{nonce.fill(0);proof.fill(0);}if(!live||epochs.get(event.connectionId)!==epoch)return;hostId(output.requestId);secret(output.bearer);daemonGeneration(output.generation);if(output.requestId!==event.requestId||output.generation!==ceremonyGenerations.get(event.connectionId)||output.scopes.length!==2||output.scopes[0]!=="account:read"||output.scopes[1]!=="account:control")throw redactedError("host-xpc-frame-invalid");const bearer=Buffer.from(output.bearer);try{raw.serverGrant(event.replyToken,output.requestId,bearer,output.generation);ceremonyGenerations.delete(event.connectionId);}finally{bearer.fill(0);}return;}
    if(event.type==="pong"){hostId(event.requestId);const entry=pongs.get(event.requestId);if(!entry)throw redactedError("host-xpc-frame-invalid");pongs.delete(event.requestId);if(event.ok!==true){entry.pending.reject(redactedError());return;}generation(event.sequence);entry.pending.resolve({requestId:event.requestId,sequence:event.sequence});}
  }catch{if(event.connectionId)try{raw.closeConnection(event.connectionId);}catch{}}})();};
  raw=binding.createHostXpcPort(true,config.peerRequirement,config.expectedEuid,onEvent);return Object.freeze({service:HOST_XPC_SERVICE,async ping(connectionId:string,input:{requestId:string;sequence:bigint}){hostId(connectionId);hostId(input.requestId);generation(input.sequence);if(!live||!epochs.has(connectionId))throw redactedError("host-xpc-closed");if(pongs.has(input.requestId))throw redactedError("host-xpc-busy");const pending=deferred<{requestId:string;sequence:bigint}>();pongs.set(input.requestId,{connectionId,pending});try{raw.serverPing(connectionId,input.requestId,input.sequence);return await pending.promise;}catch(error){pongs.delete(input.requestId);throw error;}},async closeConnection(connectionId:string,closeReason:HostXpcInvalidationReason){hostId(connectionId);reason(closeReason);if(!live||!epochs.has(connectionId))throw redactedError("host-xpc-closed");epochs.delete(connectionId);ceremonyGenerations.delete(connectionId);for(const [id,value] of pongs)if(value.connectionId===connectionId){value.pending.reject(redactedError());pongs.delete(id);}raw.closeConnection(connectionId);},close(){if(!closed){live=false;epochs.clear();ceremonyGenerations.clear();for(const value of pongs.values())value.pending.reject(redactedError());pongs.clear();closed=Promise.resolve(raw.close());}return closed;}});
}
function hostClient(binding:Binding,config:HostXpcClientConfig):HostXpcClientPort {
  hostConfig(config);if(typeof binding.createHostXpcPort!=="function"||binding.hostXpcService!==HOST_XPC_SERVICE)throw redactedError();let closed:Promise<void>|undefined,active:string|undefined,live=true,epoch=0;const expectedGenerations=new Map<string,string>(),challenges=new Map<string,ReturnType<typeof deferred<HostXpcChallenge>>>(),grants=new Map<string,ReturnType<typeof deferred<HostXpcGrant>>>();
  const failAll=(why:HostXpcInvalidationReason|"host-xpc-closed"="host-xpc-closed")=>{const error=redactedError(why);for(const pending of [...challenges.values(),...grants.values()])pending.reject(error);challenges.clear();grants.clear();expectedGenerations.clear();active=undefined;};const invalidateOnce=(why:HostXpcInvalidationReason)=>{if(!live)return;live=false;epoch++;failAll(why);try{config.onInvalidated(why);}catch{}};let raw!:RawHostPort;
  const onEvent=(event:RawHostEvent)=>{try{if(event.type==="invalidated"){invalidateOnce(supportedReason(event.reason)??"protocol-invalid");return;}if(event.type==="closed"){invalidateOnce("delivery-unavailable");return;}if(!live)return;hostId(event.requestId);if(event.type==="ping"){generation(event.replyToken);generation(event.sequence);const observed=epoch;void Promise.resolve(config.onPing({requestId:event.requestId,sequence:event.sequence})).then(output=>{if(!live||epoch!==observed)return;hostId(output.requestId);generation(output.sequence);if(output.requestId!==event.requestId||output.sequence!==event.sequence)throw redactedError("host-xpc-frame-invalid");raw.clientPong(event.replyToken!,output.requestId,output.sequence);}).catch(()=>invalidateOnce("delivery-unavailable"));return;}if(event.type!=="challenge"&&event.type!=="grant")throw redactedError("host-xpc-frame-invalid");if(event.ok!==true){const why=event.ok===false?supportedReplyReason(event.reason):undefined,pending=event.type==="challenge"?challenges.get(event.requestId):grants.get(event.requestId);if(!why||!pending)throw redactedError("host-xpc-frame-invalid");invalidateOnce(why);return;}if(event.type==="challenge"){secret(event.challenge);daemonGeneration(event.generation);const pending=challenges.get(event.requestId);if(!pending)throw redactedError("host-xpc-frame-invalid");challenges.delete(event.requestId);expectedGenerations.set(event.requestId,event.generation);const copy=Buffer.from(event.challenge);event.challenge.fill(0);pending.resolve({requestId:event.requestId,challenge:copy,generation:event.generation});}else{secret(event.bearer);daemonGeneration(event.generation);const pending=grants.get(event.requestId);if(!pending||event.generation!==expectedGenerations.get(event.requestId))throw redactedError("host-xpc-frame-invalid");grants.delete(event.requestId);expectedGenerations.delete(event.requestId);pending.resolve({requestId:event.requestId,bearer:Buffer.from(event.bearer),generation:event.generation,scopes:["account:read","account:control"]});event.bearer.fill(0);active=undefined;}}catch{invalidateOnce("protocol-invalid");}};
  raw=binding.createHostXpcPort(false,config.peerRequirement,config.expectedEuid,onEvent);return Object.freeze({service:HOST_XPC_SERVICE,async provision(input:{requestId:string;onChallenge(challenge:HostXpcChallenge):Promise<{requestId:string;hostNonce:Buffer;proof:Buffer}>|{requestId:string;hostNonce:Buffer;proof:Buffer}}){hostId(input.requestId);if(!live)throw redactedError("host-xpc-closed");if(active)throw redactedError("host-xpc-busy");active=input.requestId;const observed=epoch,challenge=deferred<HostXpcChallenge>();challenges.set(input.requestId,challenge);try{raw.clientOpen(input.requestId);const received=await challenge.promise;if(!live||epoch!==observed)throw redactedError("host-xpc-closed");let response:{requestId:string;hostNonce:Buffer;proof:Buffer};try{response=await input.onChallenge(received);}finally{received.challenge.fill(0);}if(!live||epoch!==observed)throw redactedError("host-xpc-closed");hostId(response.requestId);secret(response.hostNonce);secret(response.proof);if(response.requestId!==input.requestId)throw redactedError("host-xpc-frame-invalid");const nonce=Buffer.from(response.hostNonce),proof=Buffer.from(response.proof),grant=deferred<HostXpcGrant>();grants.set(input.requestId,grant);try{raw.clientFinish(input.requestId,nonce,proof);}finally{nonce.fill(0);proof.fill(0);}return await grant.promise;}catch(error){challenges.delete(input.requestId);grants.delete(input.requestId);expectedGenerations.delete(input.requestId);active=undefined;throw error;}},close(){if(!closed){live=false;epoch++;failAll();closed=Promise.resolve(raw.close());}return closed;}});
}

/** Test injection proves wrapper behavior only; it never establishes native qualification. */
export function wrapNativeAdmissionBinding(raw: unknown): NativeAdmissionBinding {
  const binding = raw as Binding;
  const spawn = (executable: string, args: readonly string[], secret: Buffer, options?: NativeSupplierSpawnOptions): NativeAuthorityResult<NativeSupplierChild | NativeGroupedSupplierChild> => translate(() => {
    path(executable);
    if (!Array.isArray(args) || args.length > 128 || args.some(value => typeof value !== "string" || Buffer.byteLength(value) > 4096 || /[\x00-\x1f]/.test(value)) || !Buffer.isBuffer(secret) || secret.length !== 32 || typeof binding?.spawnSupplier !== "function") throw new Error("invalid-native-bootstrap");
    const strict = options === undefined ? undefined : spawnOptions(options);
    const child = strict ? binding.spawnSupplier(executable, args, secret, strict.cwd, strict.environment, true) : binding.spawnSupplier(executable, args, secret);
    const required = ["read", "write", "closeInput", "terminate", "kill", ...(strict ? ["observeLeader", "reapLeader", "groupRetired"] : ["wait"])];
    if (!child || required.some(key => typeof (child as unknown as Record<string, unknown>)[key] !== "function") || (strict && (!Number.isSafeInteger(child.pid) || child.pid! <= 0))) throw new Error("invalid-native-child");
    const streams = pipes(child);
    if (strict) {
      let observed: Promise<NativeSupplierExit> | undefined, reaped: Promise<NativeSupplierExit> | undefined;
      return Object.freeze({ pid: child.pid!, ...streams, observeLeader: () => observed ??= child.observeLeader!().then(validateExit), reapLeader: () => reaped ??= child.reapLeader!().then(validateExit), groupRetired: () => child.groupRetired!() === true });
    }
    let waited: Promise<NativeSupplierExit> | undefined;
    return Object.freeze({ ...streams, ...(child.pid === undefined ? {} : { pid: child.pid }), wait: () => waited ??= child.wait().then(validateExit, () => { throw new Error("wait-unavailable"); }) });
  });
  return {
    acquire(directory) { return translate(() => { path(directory); if (!binding || typeof binding.acquire !== "function") throw new Error("invalid-native-binding"); const lease = binding.acquire(directory, "runtime-admission-authority.lock"); if (!lease || typeof lease.device !== "bigint" || lease.device < 0n || typeof lease.inode !== "bigint" || lease.inode < 0n || lease.held !== true || typeof lease.created !== "boolean" || typeof lease.close !== "function") throw new Error("invalid-native-lease"); let closed = false; return Object.freeze({ device: lease.device, inode: lease.inode, created: lease.created, get held() { return !closed && lease.held === true; }, close() { if (closed) throw new Error("native-lease-already-closed"); closed = true; lease.close(); } }); }); },
    spawnSupplier(executable, args, secret) { return spawn(executable, args, secret) as NativeAuthorityResult<NativeSupplierChild>; },
    spawnGroupedSupplier(executable, args, secret, options) { return spawn(executable, args, secret, options) as NativeAuthorityResult<NativeGroupedSupplierChild>; },
    createHostXpcServer(config) { return translate(()=>hostServer(binding,config)); },
    createHostXpcClient(config) { return translate(()=>hostClient(binding,config)); }
  };
}

/** Importing the package never loads the addon. A later qualified composition must inject its trusted absolute packaged path. */
export function loadNativeAdmissionBinding(enabled: boolean, addonPath?: string): NativeAuthorityResult<NativeAdmissionBinding> {
  if (!enabled) return unavailable("native-package-unqualified");
  if (addonPath === undefined) return unavailable("native-package-unqualified");
  try { path(addonPath); } catch { return unavailable("path-unsafe"); }
  if (process.platform !== "darwin" || !["arm64", "x64"].includes(process.arch)) return unavailable("platform-unsupported");
  return translate(() => wrapNativeAdmissionBinding(createRequire(addonPath)(addonPath)));
}
