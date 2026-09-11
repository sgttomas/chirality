import {describe,expect,it} from "vitest";
import {mkdtemp,rm,realpath} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join} from "node:path";
import {startSupervisorServer,SupervisorClient,assertNoPrivateAuthoritySurface,validateSupplierAuthorityProjection} from "../packages/daemon/src/supervisor-server.js";
import {validateStandaloneSupplierAuthority} from "../packages/daemon/src/standalone.js";
describe("supplier private public-surface denial",()=>{
 for(const name of ["authoritySecret","runtimeProcessIncarnationId","supplierGeneration","identityGeneration","snapshotDigest","leaseId","transcriptMac","previousTranscriptMac","runtimeChallenge","supplierChallenge","exactSupplyDigest"]){it(`denies exact private ${name} names in objects and nested JSON input`,()=>{expect(()=>assertNoPrivateAuthoritySurface({nested:{[name]:"x"}})).toThrow();expect(()=>assertNoPrivateAuthoritySurface({input:JSON.stringify({[name]:"x"})})).toThrow();expect(()=>assertNoPrivateAuthoritySurface({[name+"Documentation"]:"safe"})).not.toThrow();});}
 it("rejects every private method and notification payload",()=>{for(const suffix of ["Acquire","Release","Abort","Acquired","Released","Aborted","Revoked"])expect(()=>assertNoPrivateAuthoritySurface({method:"chirality/admission"+suffix})).toThrow();});
 it("permits only the closed coarse projections",()=>{for(const value of [{state:"disabled"},{state:"ready"},... ["not-configured","starting","revoking","retiring","blocked"].map(reason=>({state:"unavailable",reason}))])expect(validateSupplierAuthorityProjection(value)).toEqual(value);for(const value of [{state:"ready",leaseId:"x"},{state:"unavailable",reason:"custom"},{state:"ready",extra:1}])expect(()=>validateSupplierAuthorityProjection(value)).toThrow();});
 it("rejects private outgoing supervisor responses and incoming client payloads over the actual server boundary",async()=>{const d=await realpath(await mkdtemp(join(tmpdir(),"authority-server-")));try{let calls=0;const server=await startSupervisorServer({socketPath:join(d,"socket"),supervisor:{inventory:async()=>[{leaseId:"must-not-escape"}],acquire:async()=>{calls++;return{};}} as any});try{const client=new SupervisorClient({socketPath:join(d,"socket"),credential:server.credential});await expect(client.inventory()).rejects.toThrow("rejected");await expect(client.acquire("w",JSON.stringify({supplierGeneration:"x"}))).rejects.toThrow("private");expect(calls).toBe(0);}finally{await server.close();}}finally{await rm(d,{recursive:true,force:true});}});
 it("keeps standalone absent/disabled and validates the exact explicit schema",()=>{expect(validateStandaloneSupplierAuthority(undefined,"/private/tmp")).toBeUndefined();expect(validateStandaloneSupplierAuthority({enabled:false},"/private/tmp")).toEqual({enabled:false});const enabled={schema:"chirality-standalone-supplier-authority/v1",enabled:true,authorityDirectory:"authority",supplierExecutable:"/private/supplier",supplierArgs:[],nativeBindingSha256:"a".repeat(64),exactSupplyDigest:"b".repeat(64)};expect(validateStandaloneSupplierAuthority(enabled,"/private/tmp")).toEqual(enabled);for(const value of [{...enabled,enabled:false},{...enabled,extra:true},{...enabled,authorityDirectory:"../escape"},{...enabled,supplierArgs:["x\u0000y"]},{enabled:true}])expect(()=>validateStandaloneSupplierAuthority(value,"/private/tmp")).toThrow();});
});


it.each([true, false])("routes bounded interruption separately when supported (native=%s)", async native => {
  const root = await realpath(await mkdtemp(join(tmpdir(), "interrupt-server-")));
  const calls: string[] = [];
  const supervisor = {
    ...(native ? { interrupt: async (workerId: string, generation: string) => { calls.push(`interrupt:${workerId}:${generation}`); } } : {}),
    retire: async (workerId: string, generation: string) => { calls.push(`retire:${workerId}:${generation}`); }
  };
  const server = await startSupervisorServer({ socketPath: join(root, "socket"), supervisor: supervisor as any });
  try {
    const client = new SupervisorClient({ socketPath: join(root, "socket"), credential: server.credential });
    await client.interrupt("worker", "generation");
    expect(calls).toEqual([`${native ? "interrupt" : "retire"}:worker:generation`]);
    await expect(client.interrupt("worker", "")).rejects.toThrow("rejected");
    expect(calls).toHaveLength(1);
  } finally { await server.close(); await rm(root, { recursive: true, force: true }); }
});
