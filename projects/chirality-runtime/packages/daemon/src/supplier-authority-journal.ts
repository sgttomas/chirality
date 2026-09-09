import { constants } from "node:fs";
import { open, rename } from "node:fs/promises";
import { dirname } from "node:path";
import { createHash, randomUUID } from "node:crypto";
import type { RuntimeAdmissionLease } from "@chirality/runtime-core";
import { parseAuthorityJson, strictKeys, SupplierAuthorityController, type SupplierAuthorityProjection } from "./supplier-authority-controller.js";

export const AUTHORITY_JOURNAL_EVENTS=["LOCK_ACQUIRED","STARTING","PROVING","ACTIVE","REVOKING","UNCLEAN_PREDECESSOR_RECOVERY","AUTHORITY_FENCED","SUPPLIER_RETIRING","SUPPLIER_RETIRED","CUSTODY_BLOCKED_AMBIGUOUS"] as const;
export type AuthorityJournalEvent=typeof AUTHORITY_JOURNAL_EVENTS[number];
export interface AuthorityJournalRecord {schema:"chirality.runtime.supplier-authority-journal/v1";sequence:string;event:AuthorityJournalEvent;runtimeProcessIncarnationId:string;supplierGeneration:string|null;lockIdentity:{device:string;inode:string}|null;priorDigest:string;details:Record<string,never>;digest:string}
const ZERO="0".repeat(64),HEX=/^[a-f0-9]{64}$/,DEC=/^(0|[1-9][0-9]*)$/;
function validate(value:unknown):AuthorityJournalRecord {
  strictKeys(value,["schema","sequence","event","runtimeProcessIncarnationId","supplierGeneration","lockIdentity","priorDigest","details","digest"]);
  if(value.schema!=="chirality.runtime.supplier-authority-journal/v1"||typeof value.sequence!=="string"||!DEC.test(value.sequence)||BigInt(value.sequence)<1n||!AUTHORITY_JOURNAL_EVENTS.includes(value.event as AuthorityJournalEvent)||typeof value.runtimeProcessIncarnationId!=="string"||!/^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/.test(value.runtimeProcessIncarnationId)||!(value.supplierGeneration===null||(typeof value.supplierGeneration==="string"&&/^[\x21-\x7e]{1,128}$/.test(value.supplierGeneration)))||typeof value.priorDigest!=="string"||!HEX.test(value.priorDigest)||typeof value.digest!=="string"||!HEX.test(value.digest))throw new Error("authority-journal-corrupt");
  if(value.lockIdentity!==null){strictKeys(value.lockIdentity,["device","inode"]);for(const v of Object.values(value.lockIdentity))if(typeof v!=="string"||!DEC.test(v))throw new Error("authority-journal-corrupt");}
  // Lifecycle events disclose no free-form context. An incomplete prefix is bound by priorDigest.
  strictKeys(value.details,[]);return value as unknown as AuthorityJournalRecord;
}
function recordDigest(record:Omit<AuthorityJournalRecord,"digest">):string {return createHash("sha256").update(JSON.stringify(record)).digest("hex");}
function transition(previous:AuthorityJournalRecord|undefined,next:AuthorityJournalRecord):void {
  if(!previous){if(next.event!=="LOCK_ACQUIRED"||!next.lockIdentity)throw new Error("authority-journal-order");return;}
  if(!next.lockIdentity||JSON.stringify(previous.lockIdentity)!==JSON.stringify(next.lockIdentity))throw new Error("authority-journal-lock-identity");
  if(previous.runtimeProcessIncarnationId!==next.runtimeProcessIncarnationId){if(next.event!=="UNCLEAN_PREDECESSOR_RECOVERY"||next.supplierGeneration!==null)throw new Error("authority-journal-order");return;}
  const allowed:Record<AuthorityJournalEvent,readonly AuthorityJournalEvent[]>={LOCK_ACQUIRED:["STARTING","REVOKING"],STARTING:["PROVING","REVOKING"],PROVING:["ACTIVE","REVOKING"],ACTIVE:["REVOKING"],REVOKING:["SUPPLIER_RETIRING","CUSTODY_BLOCKED_AMBIGUOUS"],UNCLEAN_PREDECESSOR_RECOVERY:["AUTHORITY_FENCED"],AUTHORITY_FENCED:["SUPPLIER_RETIRED","CUSTODY_BLOCKED_AMBIGUOUS"],SUPPLIER_RETIRING:["SUPPLIER_RETIRED","CUSTODY_BLOCKED_AMBIGUOUS"],SUPPLIER_RETIRED:["AUTHORITY_FENCED","LOCK_ACQUIRED"],CUSTODY_BLOCKED_AMBIGUOUS:[]};
  if(!allowed[previous.event].includes(next.event))throw new Error("authority-journal-order");
  if(next.event!=="STARTING"&&previous.supplierGeneration!==next.supplierGeneration)throw new Error("authority-journal-generation");
}
export class SupplierAuthorityJournal {
  private prior=ZERO;private next=1n;private last?:AuthorityJournalRecord;private ready=false;private serial:Promise<void>=Promise.resolve();
  constructor(readonly path:string){}
  async recover():Promise<readonly AuthorityJournalRecord[]>{
    let file;try{file=await open(this.path,constants.O_RDONLY|constants.O_NOFOLLOW);}catch(error){if((error as NodeJS.ErrnoException).code==="ENOENT"){this.ready=true;return[];}throw error;}
    let text:string;try{const s=await file.stat();if(!s.isFile()||s.uid!==process.getuid?.()||(s.mode&0o777)!==0o600||s.nlink!==1)throw new Error("authority-journal-unsafe");text=await file.readFile("utf8");}finally{await file.close();}
    const records:AuthorityJournalRecord[]=[];let prior=ZERO,next=1n;
    try{if(text!==""&&!text.endsWith("\n"))throw new Error("authority-journal-torn");for(const line of text.split("\n").slice(0,-1)){const r=validate(parseAuthorityJson(line));const {digest,...base}=r;if(r.priorDigest!==prior||r.sequence!==String(next)||recordDigest(base)!==digest)throw new Error("authority-journal-corrupt");transition(records.at(-1),r);records.push(r);prior=digest;next++;}}
    catch{this.ready=false;await rename(this.path,`${this.path}.quarantine-${randomUUID()}`);const directory=await open(dirname(this.path),constants.O_RDONLY|constants.O_DIRECTORY);try{await directory.sync();}finally{await directory.close();}throw new Error("authority-blocked-ambiguous");}
    this.prior=prior;this.next=next;this.last=records.at(-1);this.ready=true;return records;
  }
  append(input:Pick<AuthorityJournalRecord,"event"|"runtimeProcessIncarnationId"|"supplierGeneration"|"lockIdentity">):Promise<AuthorityJournalRecord>{
    const run=this.serial.then(async()=>{if(!this.ready)throw new Error("authority-journal-not-recovered");const base:Omit<AuthorityJournalRecord,"digest">={schema:"chirality.runtime.supplier-authority-journal/v1",sequence:String(this.next),event:input.event,runtimeProcessIncarnationId:input.runtimeProcessIncarnationId,supplierGeneration:input.supplierGeneration,lockIdentity:input.lockIdentity,priorDigest:this.prior,details:{}};const record=validate({...base,digest:recordDigest(base)});transition(this.last,record);
      const f=await open(this.path,constants.O_WRONLY|constants.O_APPEND|constants.O_CREAT|constants.O_NOFOLLOW,0o600);try{const s=await f.stat();if(!s.isFile()||s.uid!==process.getuid?.()||(s.mode&0o777)!==0o600||s.nlink!==1)throw new Error("authority-journal-unsafe");await f.writeFile(JSON.stringify(record)+"\n");await f.sync();}catch(error){this.ready=false;throw error;}finally{await f.close();}
      const directory=await open(dirname(this.path),constants.O_RDONLY|constants.O_DIRECTORY);try{await directory.sync();}finally{await directory.close();}this.prior=record.digest;this.next++;this.last=record;return record;});this.serial=run.then(()=>{},()=>{});return run;
  }
}
/** Runtime acceptance fencing and D-GOV-36 supplier cleanup are separate durable decisions. */
export class SupplierAuthorityLifecycle {
  private lease?:RuntimeAdmissionLease;private incarnation?:string;private generation?:string;private controller?:SupplierAuthorityController;private blocked=false;private started=false;private closing?:Promise<void>;
  constructor(private readonly options:{journal:SupplierAuthorityJournal;acquire:()=>Promise<RuntimeAdmissionLease>;establish:(context:{lease:RuntimeAdmissionLease;runtimeProcessIncarnationId:string;supplierGeneration:string;spawned:()=>Promise<void>;durableRevoke:()=>Promise<void>})=>Promise<SupplierAuthorityController>;retire:()=>Promise<{retired:boolean;cleanupVerified:boolean}>}){}
  projection():SupplierAuthorityProjection{return this.blocked?{state:"unavailable",reason:"blocked"}:this.started?this.controller!.projection():{state:"unavailable",reason:"starting"};}
  get authority():SupplierAuthorityController {if(!this.controller||this.blocked||!this.started)throw new Error("authority-unavailable");return this.controller;}
  private async record(event:AuthorityJournalEvent):Promise<void>{if(!this.incarnation)throw new Error("authority-unavailable");await this.options.journal.append({event,runtimeProcessIncarnationId:this.incarnation,supplierGeneration:this.generation??null,lockIdentity:this.lease?{device:String(this.lease.device),inode:String(this.lease.inode)}:null});}
  async start(incarnation:string):Promise<void>{if(this.incarnation)throw new Error("authority-unavailable");this.incarnation=incarnation;
    try{const records=await this.options.journal.recover();this.lease=await this.options.acquire();if(!this.lease.held)throw new Error("authority-unavailable");const last=records.at(-1);const identity=last?.lockIdentity;
      if(identity&&(identity.device!==String(this.lease.device)||identity.inode!==String(this.lease.inode)))throw new Error("inode-mismatch");
      if(!last&&!this.lease.created)throw new Error("authority-blocked-ambiguous");
      if(last){if(!identity)throw new Error("authority-blocked-ambiguous");await this.record("UNCLEAN_PREDECESSOR_RECOVERY");await this.record("AUTHORITY_FENCED");const cleanup=await this.options.retire();if(!cleanup.retired||!cleanup.cleanupVerified){await this.record("CUSTODY_BLOCKED_AMBIGUOUS");throw new Error("authority-blocked-ambiguous");}await this.record("SUPPLIER_RETIRED");}
      await this.record("LOCK_ACQUIRED");this.generation=randomUUID();await this.record("STARTING");let spawned=false;
      this.controller=await this.options.establish({lease:this.lease,runtimeProcessIncarnationId:incarnation,supplierGeneration:this.generation,spawned:async()=>{if(spawned)throw new Error("authority-unavailable");spawned=true;await this.record("PROVING");},durableRevoke:()=>this.record("REVOKING")});
      if(!spawned||this.controller.projection().state!=="ready")throw new Error("authority-unavailable");await this.record("ACTIVE");this.started=true;
    }catch(error){this.blocked=true;await this.controller?.revoke().catch(()=>{});throw error;}
  }
  close():Promise<void>{return this.closing??=(async()=>{this.blocked=true;await this.controller?.revoke();await this.controller?.close();if(!this.controller&&this.lease)await this.record("REVOKING");await this.record("SUPPLIER_RETIRING");const cleanup=await this.options.retire();if(!cleanup.retired||!cleanup.cleanupVerified){await this.record("CUSTODY_BLOCKED_AMBIGUOUS");throw new Error("authority-blocked-ambiguous");}await this.record("SUPPLIER_RETIRED");await this.record("AUTHORITY_FENCED");if(this.lease?.held)this.lease.close();})();}
}
