import { createHmac, timingSafeEqual, randomUUID } from "node:crypto";
import type { RuntimeAdmissionLease } from "@chirality/runtime-core";

export type Sequence20 = string;
export const AUTHORITY_CONTRACT = "chirality-local-supplier-admission-authority/1";
export const ZERO_TRANSCRIPT_MAC = "A".repeat(43);
export const FIRST_SEQUENCE = "00000000000000000001";
const MAX_SEQUENCE = 18446744073709551615n;
const ASCII = /^[\x21-\x7e]+$/;
const MAC = /^[A-Za-z0-9_-]{43}$/;
const DIGEST = /^[a-f0-9]{64}$/;
const UUID = /^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/;
export type AuthorityErrorReason = "authority-unavailable"|"authority-revoked"|"generation-mismatch"|"sequence-invalid"|"transcript-invalid"|"snapshot-stale"|"lease-busy"|"lease-unknown"|"lease-state-invalid"|"request-malformed"|"internal-failure";
export type AuthorityRequest =
  | {kind:"request";op:"chirality/admissionAcquire";requestId:string;operationId:string;v4:{supplierGeneration:string;identityGeneration:string;snapshotDigest:string}}
  | {kind:"request";op:"chirality/admissionRelease";requestId:string;leaseId:string;disposition:"worker-accepted"}
  | {kind:"request";op:"chirality/admissionAbort";requestId:string;leaseId:string;disposition:"worker-not-accepted"};
export type AuthorityResult =
  | {kind:"result";op:"chirality/admissionAcquire";state:"acquired";requestId:string;operationId:string;leaseId:string;supplierGeneration:string;identityGeneration:string;snapshotDigest:string}
  | {kind:"result";op:"chirality/admissionRelease";state:"released";requestId:string;leaseId:string;disposition:"worker-accepted"}
  | {kind:"result";op:"chirality/admissionAbort";state:"aborted";requestId:string;leaseId:string;disposition:"worker-not-accepted"}
  | {kind:"result";op:"error";state:"error";requestId:string|null;class:"unavailable"|"authorization"|"protocol"|"stale"|"busy"|"malformed"|"internal";reason:AuthorityErrorReason};
export type AuthorityNotification =
  | {kind:"notification";op:"chirality/admissionAcquired";requestId:string;operationId:string;leaseId:string;supplierGeneration:string;identityGeneration:string;snapshotDigest:string}
  | {kind:"notification";op:"chirality/admissionReleased";requestId:string;leaseId:string;disposition:"worker-accepted"}
  | {kind:"notification";op:"chirality/admissionAborted";requestId:string;leaseId:string;disposition:"worker-not-accepted"}
  | {kind:"notification";op:"chirality/admissionRevoked";reason:"authority-revoked"|"identity-transition"|"supplier-shutdown"|"protocol-failure";revokedThroughRuntimeSequence:Sequence20};
export type AuthorityBody = AuthorityRequest|AuthorityResult|AuthorityNotification;
export interface AuthorityEnvelope<T = AuthorityBody> {contract:string;runtimeProcessIncarnationId:string;supplierGeneration:string;direction:"runtime-to-supplier"|"supplier-to-runtime";sequence:Sequence20;previousTranscriptMac:string;body:T;transcriptMac:string}
export function strictKeys(value:unknown, names:readonly string[]): asserts value is Record<string,unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value) || Object.getPrototypeOf(value) !== Object.prototype || Object.keys(value).length !== names.length || names.some(k=>!Object.hasOwn(value,k))) throw new Error("request-malformed");
}
function boundedId(value:unknown): asserts value is string { if(typeof value!=="string"||value.length>128||!ASCII.test(value))throw new Error("request-malformed"); }
function digest(value:unknown): asserts value is string {if(typeof value!=="string"||!DIGEST.test(value))throw new Error("request-malformed");}
function mac(value:unknown): asserts value is string {if(typeof value!=="string"||!MAC.test(value)||Buffer.from(value,"base64url").toString("base64url")!==value)throw new Error("transcript-invalid");}
/** Detect duplicate keys on the original JSON bytes, including escaped key aliases. */
export function parseAuthorityJson(raw:string|Uint8Array): unknown {
  const text=typeof raw==="string"?raw:new TextDecoder("utf-8",{fatal:true}).decode(raw);
  if(Buffer.byteLength(text)>1048576)throw new Error("request-malformed");
  let i=0;const ws=()=>{while(/[\x20\t\r\n]/.test(text[i]??"x"))i++;};
  const string=():string=>{const start=i++;while(i<text.length){if(text[i]==="\\"){i+=2;continue;}if(text[i++]==='"')return JSON.parse(text.slice(start,i)) as string;}throw new Error("request-malformed");};
  const value=(depth:number):void=>{if(depth>32)throw new Error("request-malformed");ws();if(text[i]==='"'){string();return;}if(text[i]==='{'){i++;ws();const keys=new Set<string>();if(text[i]==='}'){i++;return;}while(true){ws();if(text[i]!== '"')throw new Error("request-malformed");const k=string();if(keys.has(k))throw new Error("request-malformed");keys.add(k);ws();if(text[i++]!==':')throw new Error("request-malformed");value(depth+1);ws();if(text[i]==='}'){i++;return;}if(text[i++]!==',')throw new Error("request-malformed");}}if(text[i]==='['){i++;ws();if(text[i]===']'){i++;return;}while(true){value(depth+1);ws();if(text[i]===']'){i++;return;}if(text[i++]!==',')throw new Error("request-malformed");}}const start=i;while(i<text.length&&!/[\x20\t\r\n,}\]]/.test(text[i]!))i++;if(start===i)throw new Error("request-malformed");const v:unknown=JSON.parse(text.slice(start,i));if(typeof v==='number'&&!Number.isFinite(v))throw new Error("request-malformed");};
  value(0);ws();if(i!==text.length)throw new Error("request-malformed");return JSON.parse(text) as unknown;
}
export function parseSequence20(value:unknown):bigint {if(typeof value!=="string"||!/^[0-9]{20}$/.test(value))throw new Error("sequence-invalid");const n=BigInt(value);if(n<1n||n>MAX_SEQUENCE)throw new Error("sequence-invalid");return n;}
export function nextSequence20(value:Sequence20):Sequence20 {const n=parseSequence20(value);if(n===MAX_SEQUENCE)throw new Error("sequence-invalid");return(n+1n).toString().padStart(20,"0");}
const errorPairs:Record<AuthorityErrorReason,string>={"authority-unavailable":"unavailable","authority-revoked":"authorization","generation-mismatch":"protocol","sequence-invalid":"protocol","transcript-invalid":"protocol","snapshot-stale":"stale","lease-busy":"busy","lease-unknown":"malformed","lease-state-invalid":"malformed","request-malformed":"malformed","internal-failure":"internal"};
export function decodeAuthorityBody(value:unknown):AuthorityBody {
  if(!value||typeof value!=="object"||Array.isArray(value))throw new Error("request-malformed");
  const b=value as Record<string,unknown>, kind=b.kind,op=b.op;
  const fields=kind==="request"&&op==="chirality/admissionAcquire"?["kind","op","requestId","operationId","v4"]:
    kind==="request"&&(op==="chirality/admissionRelease"||op==="chirality/admissionAbort")?["kind","op","requestId","leaseId","disposition"]:
    kind==="result"&&op==="error"?["kind","op","state","requestId","class","reason"]:
    kind==="notification"&&op==="chirality/admissionRevoked"?["kind","op","reason","revokedThroughRuntimeSequence"]:
    kind==="result"&&op==="chirality/admissionAcquire"?["kind","op","state","requestId","operationId","leaseId","supplierGeneration","identityGeneration","snapshotDigest"]:
    kind==="notification"&&op==="chirality/admissionAcquired"?["kind","op","requestId","operationId","leaseId","supplierGeneration","identityGeneration","snapshotDigest"]:
    kind==="result"&&(op==="chirality/admissionRelease"||op==="chirality/admissionAbort")?["kind","op","state","requestId","leaseId","disposition"]:
    kind==="notification"&&(op==="chirality/admissionReleased"||op==="chirality/admissionAborted")?["kind","op","requestId","leaseId","disposition"]:undefined;
  if(!fields)throw new Error("request-malformed");strictKeys(b,fields);
  for(const field of ["requestId","operationId","leaseId","supplierGeneration","identityGeneration"]){if(field in b&&!(op==="error"&&field==="requestId"&&b[field]===null))boundedId(b[field]);}
  if("snapshotDigest"in b)digest(b.snapshotDigest);
  if("v4"in b){strictKeys(b.v4,["supplierGeneration","identityGeneration","snapshotDigest"]);boundedId(b.v4.supplierGeneration);boundedId(b.v4.identityGeneration);digest(b.v4.snapshotDigest);}
  if(op==="error"){if(b.state!=="error"||typeof b.reason!=="string"||!Object.hasOwn(errorPairs,b.reason)||errorPairs[b.reason as AuthorityErrorReason]!==b.class)throw new Error("request-malformed");}
  else if(op==="chirality/admissionRevoked"){if(!["authority-revoked","identity-transition","supplier-shutdown","protocol-failure"].includes(String(b.reason)))throw new Error("request-malformed");parseSequence20(b.revokedThroughRuntimeSequence);}
  else {const acquired=op==="chirality/admissionAcquire"||op==="chirality/admissionAcquired";const release=op==="chirality/admissionRelease"||op==="chirality/admissionReleased";if(kind==="result"&&b.state!==(acquired?"acquired":release?"released":"aborted"))throw new Error("request-malformed");if(!acquired&&b.disposition!==(release?"worker-accepted":"worker-not-accepted"))throw new Error("request-malformed");}
  return b as unknown as AuthorityBody;
}
function ascii(value:string):Buffer {if(!ASCII.test(value))throw new Error("request-malformed");return Buffer.from(value,"ascii");}
function u32(n:number):Buffer {if(!Number.isSafeInteger(n)||n<0||n>0xffffffff)throw new Error("request-malformed");const b=Buffer.alloc(4);b.writeUInt32BE(n);return b;}
function lp(value:Buffer):Buffer{return Buffer.concat([u32(value.length),value]);}
export type CanonField={type:"ascii";value:string}|{type:"sequence";value:Sequence20};
export const asciiField=(value:string):CanonField=>({type:"ascii",value});
export const sequenceField=(value:Sequence20):CanonField=>({type:"sequence",value});
export function canonicalBytes(domain:string,fields:readonly CanonField[]):Buffer {return Buffer.concat([Buffer.from("chirality-local-admission-mac\0","ascii"),Buffer.from([1]),lp(ascii(domain)),u32(fields.length),...fields.map(f=>{if(f.type==="ascii")return lp(ascii(f.value));const b=Buffer.alloc(8);b.writeBigUInt64BE(parseSequence20(f.value));return lp(b);})]);}
export function bodyFields(input:AuthorityBody):CanonField[]{
  const b=decodeAuthorityBody(input),a=asciiField;
  if(b.kind==="request"&&b.op==="chirality/admissionAcquire")return[b.kind,b.op,b.requestId,b.operationId,b.v4.supplierGeneration,b.v4.identityGeneration,b.v4.snapshotDigest].map(a);
  if(b.kind==="result"&&b.op==="error")return[b.kind,b.op,b.state,b.requestId??"null",b.class,b.reason].map(a);
  if(b.kind==="notification"&&b.op==="chirality/admissionRevoked")return[a(b.kind),a(b.op),a(b.reason),sequenceField(b.revokedThroughRuntimeSequence)];
  const prefix=[b.kind,b.op,...(b.kind==="result"?[b.state]:[]),b.requestId];
  if((b.kind==="result"&&b.op==="chirality/admissionAcquire")||(b.kind==="notification"&&b.op==="chirality/admissionAcquired"))return[...prefix,b.operationId,b.leaseId,b.supplierGeneration,b.identityGeneration,b.snapshotDigest].map(a);
  return [...prefix,b.leaseId,b.disposition].map(a);
}
export function transcriptMac(secret:Buffer,envelope:Omit<AuthorityEnvelope,"transcriptMac">):string {if(secret.length!==32)throw new Error("request-malformed");return createHmac("sha256",secret).update(canonicalBytes(`transcript/${envelope.direction}`,[asciiField(envelope.contract),asciiField(envelope.runtimeProcessIncarnationId),asciiField(envelope.supplierGeneration),asciiField(envelope.direction),sequenceField(envelope.sequence),asciiField(envelope.previousTranscriptMac),...bodyFields(envelope.body)])).digest("base64url");}
export interface InitializationProofInput {contract:string;runtimeProcessIncarnationId:string;supplierGeneration:string;runtimeChallenge:string;supplierChallenge:string;exactSupplyDigest:string;descriptor:{capability:string;contract:string;major:number;minor:number};v4Descriptor:{capability:string;contract:string;major:number;minor:number;method:string}}
export function initializationProof(secret:Buffer,input:InitializationProofInput):string {if(secret.length!==32)throw new Error("request-malformed");const integer=(n:number)=>{if(!Number.isSafeInteger(n)||n<0)throw new Error("request-malformed");return String(n);};return createHmac("sha256",secret).update(canonicalBytes("initialize-proof",[input.contract,input.runtimeProcessIncarnationId,input.supplierGeneration,input.runtimeChallenge,input.supplierChallenge,input.exactSupplyDigest,input.descriptor.capability,input.descriptor.contract,integer(input.descriptor.major),integer(input.descriptor.minor),input.v4Descriptor.capability,input.v4Descriptor.contract,integer(input.v4Descriptor.major),integer(input.v4Descriptor.minor),input.v4Descriptor.method].map(asciiField))).digest("base64url");}
export function verifyProof(expected:string,actual:unknown):void {mac(actual);mac(expected);if(!timingSafeEqual(Buffer.from(expected,"base64url"),Buffer.from(actual,"base64url")))throw new Error("transcript-invalid");}
export function verifyTranscriptMac(secret:Buffer,envelope:AuthorityEnvelope):void {verifyProof(transcriptMac(secret,envelope),envelope.transcriptMac);}
export function decodeAuthorityEnvelope(value:unknown):AuthorityEnvelope {strictKeys(value,["contract","runtimeProcessIncarnationId","supplierGeneration","direction","sequence","previousTranscriptMac","body","transcriptMac"]);if(value.contract!==AUTHORITY_CONTRACT||typeof value.runtimeProcessIncarnationId!=="string"||!UUID.test(value.runtimeProcessIncarnationId)||!["runtime-to-supplier","supplier-to-runtime"].includes(String(value.direction)))throw new Error("request-malformed");boundedId(value.supplierGeneration);parseSequence20(value.sequence);mac(value.previousTranscriptMac);mac(value.transcriptMac);const body=decodeAuthorityBody(value.body);if((value.direction==="runtime-to-supplier")!==(body.kind==="request"))throw new Error("request-malformed");return value as unknown as AuthorityEnvelope;}
/** A direction owns its own exact sequence and chain. Exhaustion never wraps. */
export class AuthorityTranscript {
  private next:Sequence20|undefined=FIRST_SEQUENCE;private previous=ZERO_TRANSCRIPT_MAC;
  constructor(private readonly secret:Buffer,private readonly identity:{runtimeProcessIncarnationId:string;supplierGeneration:string},private readonly direction:AuthorityEnvelope["direction"]){if(secret.length!==32)throw new Error("request-malformed");}
  encode(body:AuthorityBody):AuthorityEnvelope {if(!this.next)throw new Error("sequence-invalid");const frame={contract:AUTHORITY_CONTRACT,...this.identity,direction:this.direction,sequence:this.next,previousTranscriptMac:this.previous,body,transcriptMac:""};frame.transcriptMac=transcriptMac(this.secret,frame);decodeAuthorityEnvelope(frame);this.advance(frame);return frame;}
  accept(raw:string|Uint8Array):AuthorityBody {const f=decodeAuthorityEnvelope(parseAuthorityJson(raw));if(f.runtimeProcessIncarnationId!==this.identity.runtimeProcessIncarnationId||f.supplierGeneration!==this.identity.supplierGeneration)throw new Error("generation-mismatch");if(f.direction!==this.direction||f.sequence!==this.next||f.previousTranscriptMac!==this.previous)throw new Error("sequence-invalid");verifyTranscriptMac(this.secret,f);this.advance(f);return f.body;}
  private advance(f:AuthorityEnvelope):void {this.previous=f.transcriptMac;this.next=parseSequence20(f.sequence)===MAX_SEQUENCE?undefined:nextSequence20(f.sequence);}
}
export interface AuthorityTransport {send(frame:AuthorityEnvelope<AuthorityRequest>):Promise<void>;subscribe(frame:(raw:string|Uint8Array)=>void,failed:()=>void):()=>void;close():Promise<void>}
export type SupplierAuthorityProjection={state:"disabled"}|{state:"unavailable";reason:"not-configured"|"starting"|"revoking"|"retiring"|"blocked"}|{state:"ready"};
interface Pending {request:AuthorityRequest;result?:AuthorityResult;resolve:(result:AuthorityResult)=>void;reject:(error:Error)=>void}
export class SupplierAuthorityController {
  private state:"disabled"|"active"|"revoking"="disabled";private heldOperation?:string;private heldLeaseId?:string;private pending?:Pending;private guard:Promise<void>=Promise.resolve();private outgoing?:AuthorityTranscript;private incoming?:AuthorityTranscript;private revocation?:Promise<void>;private detach?:()=>void;private lastSent?:Sequence20;
  constructor(private readonly options:{enabled:boolean;kernelLease?:RuntimeAdmissionLease;transport?:AuthorityTransport;authoritySecret?:Buffer;runtimeProcessIncarnationId?:string;supplierGeneration?:string;identityGeneration?:string;snapshotDigest?:string;durableRevoke?:()=>Promise<void>;refreshSnapshot?:()=>Promise<{supplierGeneration:string;identityGeneration:string;snapshotDigest:string}>}){
    if(!options.enabled)return;
    if(!options.kernelLease?.held||!options.transport||!options.authoritySecret||!options.runtimeProcessIncarnationId||!options.supplierGeneration||!options.identityGeneration||!options.snapshotDigest)return;
    boundedId(options.identityGeneration);digest(options.snapshotDigest);const identity={runtimeProcessIncarnationId:options.runtimeProcessIncarnationId,supplierGeneration:options.supplierGeneration};
    this.outgoing=new AuthorityTranscript(options.authoritySecret,identity,"runtime-to-supplier");this.incoming=new AuthorityTranscript(options.authoritySecret,identity,"supplier-to-runtime");this.state="active";
    this.detach=options.transport.subscribe(raw=>{try{this.receive(raw);}catch{void this.revoke();}},()=>{void this.revoke();});
  }
  projection():SupplierAuthorityProjection{return this.state==="active"&&this.options.kernelLease?.held?{state:"ready"}:this.options.enabled?{state:"unavailable",reason:this.state==="revoking"?"revoking":"starting"}:{state:"disabled"};}
  runGuarded<T>(fn:()=>Promise<T>):Promise<T>{const run=this.guard.then(fn,fn);this.guard=run.then(()=>{},()=>{});return run;}
  assertCommit(operationId:string):void {if(this.state!=="active"||!this.options.kernelLease?.held||this.heldOperation!==operationId||!this.heldLeaseId)throw new Error("authority-unavailable");}
  private receive(raw:string|Uint8Array):void {
    if(this.state!=="active"||!this.incoming)throw new Error("authority-revoked");const body=this.incoming.accept(raw);
    if(body.kind==="notification"&&body.op==="chirality/admissionRevoked"){if(!this.lastSent||parseSequence20(body.revokedThroughRuntimeSequence)>parseSequence20(this.lastSent))throw new Error("sequence-invalid");void this.revoke();return;}
    const p=this.pending;if(!p)throw new Error("transcript-invalid");
    if(!p.result){if(body.kind!=="result"||body.requestId!==p.request.requestId)throw new Error("transcript-invalid");if(body.op==="error"){this.pending=undefined;p.reject(new Error(body.reason));void this.revoke();return;}if(body.op!==p.request.op)throw new Error("transcript-invalid");p.result=body;return;}
    const r=p.result;const expected=r.op==="chirality/admissionAcquire"?"chirality/admissionAcquired":r.op==="chirality/admissionRelease"?"chirality/admissionReleased":"chirality/admissionAborted";
    if(body.kind!=="notification"||body.op!==expected)throw new Error("transcript-invalid");for(const [key,value]of Object.entries(r)){if(!["kind","op","state"].includes(key)&&(body as unknown as Record<string,unknown>)[key]!==value)throw new Error("transcript-invalid");}
    this.pending=undefined;p.resolve(r);
  }
  private async exchange(request:AuthorityRequest):Promise<AuthorityResult>{if(this.state!=="active"||!this.options.kernelLease?.held||!this.outgoing||!this.options.transport||this.pending)throw new Error("authority-unavailable");const frame=this.outgoing.encode(request) as AuthorityEnvelope<AuthorityRequest>;this.lastSent=frame.sequence;let resolve!:(result:AuthorityResult)=>void,reject!:(e:Error)=>void;const result=new Promise<AuthorityResult>((ok,no)=>{resolve=ok;reject=no;});this.pending={request,resolve,reject};void result.catch(()=>{});try{await this.options.transport.send(frame);return await result;}catch{await this.revoke();throw new Error("authority-unavailable");}}
  async acquire(operationId:string):Promise<{leaseId:string}>{boundedId(operationId);if(this.heldLeaseId)throw new Error("lease-busy");try{if(this.options.refreshSnapshot){const snapshot=await this.options.refreshSnapshot();if(snapshot.supplierGeneration!==this.options.supplierGeneration)throw new Error("generation-mismatch");boundedId(snapshot.identityGeneration);digest(snapshot.snapshotDigest);this.options.identityGeneration=snapshot.identityGeneration;this.options.snapshotDigest=snapshot.snapshotDigest;}const r=await this.exchange({kind:"request",op:"chirality/admissionAcquire",requestId:randomUUID(),operationId,v4:{supplierGeneration:this.options.supplierGeneration!,identityGeneration:this.options.identityGeneration!,snapshotDigest:this.options.snapshotDigest!}});if(r.op!=="chirality/admissionAcquire"||r.operationId!==operationId||r.supplierGeneration!==this.options.supplierGeneration||r.identityGeneration!==this.options.identityGeneration||r.snapshotDigest!==this.options.snapshotDigest||this.state!=="active")throw new Error("transcript-invalid");this.heldOperation=operationId;this.heldLeaseId=r.leaseId;return{leaseId:r.leaseId};}catch(error){await this.revoke();throw error;}}
  async release(operationId:string):Promise<void>{return this.finish(operationId,true);}
  async abort(operationId:string):Promise<void>{return this.finish(operationId,false);}
  private async finish(operationId:string,committed:boolean):Promise<void>{this.assertCommit(operationId);const leaseId=this.heldLeaseId!;this.heldLeaseId=undefined;this.heldOperation=undefined;try{const requestId=randomUUID();const r=await this.exchange(committed?{kind:"request",op:"chirality/admissionRelease",requestId,leaseId,disposition:"worker-accepted"}:{kind:"request",op:"chirality/admissionAbort",requestId,leaseId,disposition:"worker-not-accepted"});if(r.op!==(committed?"chirality/admissionRelease":"chirality/admissionAbort")||!("leaseId"in r)||r.leaseId!==leaseId)throw new Error("transcript-invalid");}catch(error){await this.revoke();throw error;}}
  revoke():Promise<void>{if(this.revocation)return this.revocation;this.state="revoking";this.heldLeaseId=undefined;this.heldOperation=undefined;const pending=this.pending;this.pending=undefined;pending?.reject(new Error("authority-revoked"));this.detach?.();this.revocation=(async()=>{await this.options.durableRevoke?.();await this.options.transport?.close();})();void this.revocation.catch(()=>{});return this.revocation;}
  async close():Promise<void>{await this.runGuarded(async()=>{await this.revoke();});}
}
