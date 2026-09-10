import { describe, expect, it } from "vitest";
import { spawn } from "node:child_process";
import { mkdtemp, readdir, realpath, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { PassThrough } from "node:stream";
import { CodexLogin, createControlledCodexLoginForTests, inspectCodexLoginPurposeReleaseRecord } from "../packages/daemon/src/codex-login.js";
async function fixture(mode = "success", authUrl = "https://auth.openai.com/authorize?state=fixture", timeoutMs = 1000) {
  const codexHome = await mkdtemp(join(await realpath(tmpdir()), "login-fixture-"));
  const code = `
const mode=${JSON.stringify(mode)}, authUrl=${JSON.stringify(authUrl)};
const send=x=>process.stdout.write(JSON.stringify(x)+'\\n');
require('node:readline').createInterface({input:process.stdin}).on('line',line=>{
 const r=JSON.parse(line);
 if(r.method==='initialize'){send({id:r.id,result:{}});return;}
 if(r.method==='initialized')return;
 if(r.method==='account/login/start'){
  if(r.params.type!=='chatgpt')process.exit(7);
  send({id:r.id,result:{type:'chatgpt',loginId:'login1',authUrl}});
  if(mode==='exit'){setTimeout(()=>process.exit(0),20);return;}
  if(mode==='pending')return;
  setTimeout(()=>{
   send({method:'account/login/completed',params:{loginId:mode==='mismatch'?'other':'login1',success:mode!=='failed',error:null}});
  },20);return;
 }
 if(r.method==='account/read'){if(r.params.refreshToken!==false)process.exit(8);send({id:r.id,result:{account:{type:'apiKey'},requiresOpenaiAuth:true}});return;}
 if(r.method==='account/login/cancel'){send({id:r.id,result:{}});send({method:'account/login/completed',params:{loginId:'login1',success:false,error:'canceled'}});return;}
 process.exit(9);
});`;
  const child = spawn(process.execPath, ["-e", code], { env: { CODEX_HOME: codexHome }, stdio: "pipe", detached: process.platform !== "win32" });
  child.stderr.resume(); const closed = new Promise<void>(resolve => child.once("close", () => resolve()));
  const transport = { stdin: child.stdin, stdout: child.stdout, async close() { if (child.pid) { try { process.kill(process.platform === "win32" ? child.pid : -child.pid, "SIGKILL"); } catch { /* exited */ } } await closed; } };
  const login = createControlledCodexLoginForTests({ transport, codexHome, timeoutMs });
  return { login, codexHome, child, async close() { await login.close(); expect(child.exitCode !== null || child.signalCode !== null).toBe(true); await rm(codexHome, { recursive: true, force: true }); } };
}
describe("operator-only sign-in component (controlled fixture)", () => {
  it("accepts only an exact account-free observed login-purpose record", () => {
    const bindings = { bindingDigest:"a".repeat(64), outerPolicyDigest:"b".repeat(64), sourceDigest:"c".repeat(64), packageDigest:"d".repeat(64), activationId:"release-1", gateIdentity:"D36", consentDigest:"e".repeat(64) };
    const supply = { sha256:"f".repeat(64), size:123, version:"0.149.0" };
    const limbs = Object.fromEntries(["exact-supplier","keyring-backend","plaintext-fallback-absent","process-containment","storage-isolation","provider-network","bounded-protocol-purpose","retirement"].map(name=>[name,{attempted:true,passed:true,evidenceSha256:"1".repeat(64)}]));
    const record = { schema:"chirality-codex-login-purpose-release/v1", evidenceClass:"exact-login-purpose-observed", bindings, supply,
      backend:{credentialStore:"keyring",plaintextFallback:false},purpose:{modelExecution:false,methods:["account/login/start","account/login/cancel","account/read"]},issuedAt:"2026-01-01T00:00:00.000Z",expiresAt:"2027-01-01T00:00:00.000Z",limbs };
    expect(inspectCodexLoginPurposeReleaseRecord(record,{...bindings,supply},Date.parse("2026-06-01T00:00:00.000Z"))).toMatchObject({evidenceClass:"exact-login-purpose-observed",backend:{credentialStore:"keyring",plaintextFallback:false}});
    expect(()=>inspectCodexLoginPurposeReleaseRecord({...record,backend:{credentialStore:"auto",plaintextFallback:false}},{...bindings,supply},Date.parse("2026-06-01T00:00:00.000Z"))).toThrow("backend");
    expect(()=>inspectCodexLoginPurposeReleaseRecord({...record,purpose:{...record.purpose,modelExecution:true}},{...bindings,supply},Date.parse("2026-06-01T00:00:00.000Z"))).toThrow("protocol");
    expect(()=>inspectCodexLoginPurposeReleaseRecord({...record,limbs:{...limbs,retirement:{attempted:true,passed:false,evidenceSha256:"1".repeat(64)}}},{...bindings,supply},Date.parse("2026-06-01T00:00:00.000Z"))).toThrow("incomplete");
    expect(()=>inspectCodexLoginPurposeReleaseRecord({...record,bindings:{...bindings,gateIdentity:"other"}},{...bindings,gateIdentity:"other",supply},Date.parse("2026-06-01T00:00:00.000Z"))).toThrow("gate");
  });
  it("reports completed ceremony with unavailable identity and never creates credential files", async () => {
    const f = await fixture();
    try {
      expect(await f.login.startLogin()).toEqual({ loginId: "login1", authUrl: "https://auth.openai.com/authorize?state=fixture" });
      await expect.poll(async () => (await f.login.status()).state).toBe("completed");
      const status = await f.login.status();
      expect(status).toEqual({ schema: "chirality-hosted-login-status/v2", state: "completed", loginId: "login1", hasAccount: true,
        evidenceClass: "controlled-fixture", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" }, hostedReady: false });
      expect(await readdir(f.codexHome)).toEqual([]);
      await f.login.close(); expect(await readdir(f.codexHome)).toEqual([]);
    } finally { await f.close(); }
  });
  it("rejects nonofficial origins, plain HTTP and URL credentials", async () => {
    for (const url of ["https://auth.openai.com.evil.example/login", "http://auth.openai.com/login", "https://user:pass@auth.openai.com/login", "https://auth.openai.com:8443/login"]) {
      const f = await fixture("pending", url);
      try { await expect(f.login.startLogin()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
      finally { await f.close(); }
    }
  });
  it("fails for mismatched completion, provider failure and clean exit", async () => {
    for (const mode of ["mismatch", "failed", "exit"]) {
      const f = await fixture(mode);
      try { await f.login.startLogin(); await expect.poll(async () => (await f.login.status()).state).toBe("failed"); expect(await f.login.status()).toMatchObject({ binding: { state: "unavailable" }, hostedReady: false }); }
      finally { await f.close(); }
    }
  });
  it("cancels pending login and prevents double start without creating account state", async () => {
    const f = await fixture("pending");
    try { await f.login.startLogin(); expect((await f.login.status()).state).toBe("pending"); await expect(f.login.startLogin()).rejects.toThrow("single-use"); await f.login.cancel(); expect((await f.login.status()).state).toBe("failed"); }
    finally { await f.close(); }
  });
  it("honors close racing with startup without continuing the ceremony", async () => {
    const f = await fixture("pending");
    try { const starting = f.login.startLogin(); await f.login.close(); await expect(starting).rejects.toThrow("closed during startup"); }
    finally { await f.close(); }
  });
  it("bounds a pending ceremony and denies production launch absent operator consent", async () => {
    // The ceremony budget includes a real child startup on contended CI workers.
    const f = await fixture("pending", undefined, 1000);
    try { await f.login.startLogin(); expect((await f.login.status()).state).toBe("pending"); await expect.poll(async () => (await f.login.status()).state, { timeout: 2000 }).toBe("failed"); }
    finally { await f.close(); }
    const login = new CodexLogin({ executablePath: "/invalid", canonicalRoot: "/invalid", codexHome: "/invalid/home", privateDirectory: "/invalid", providerNetworkConsent: { approvedBy: "", approvalReference: "" } });
    await expect(login.startLogin()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); await login.close();
  });
});


it.each(["close", "cancel"] as const)("custody %s during account projection cannot revive completed login", async action => {
  const stdin = new PassThrough(), stdout = new PassThrough();
  let accountRequest!: number; let entered!: () => void;
  const reading = new Promise<void>(resolve => { entered = resolve; });
  const send = (value: unknown) => stdout.write(JSON.stringify(value) + "\n");
  stdin.on("data", bytes => {
    for (const line of bytes.toString().trim().split("\n")) {
      const r = JSON.parse(line);
      if (r.method === "initialize") send({ id: r.id, result: {} });
      else if (r.method === "account/login/start") {
        send({ id: r.id, result: { type: "chatgpt", loginId: "race", authUrl: "https://auth.openai.com/fixture" } });
        send({ method: "account/login/completed", params: { loginId: "race", success: true } });
      } else if (r.method === "account/read") { accountRequest = r.id; entered(); }
      else if (r.method !== "initialized") throw new Error("Unexpected synthetic method");
    }
  });
  const login = createControlledCodexLoginForTests({ codexHome: "/synthetic/never-opened", transport: { stdin, stdout, async close() {} }, timeoutMs: 1000 });
  try {
    await login.startLogin(); const projection = login.status(); await reading;
    await login[action]();
    send({ id: accountRequest, result: { account: { type: "apiKey" }, requiresOpenaiAuth: true } });
    expect(await projection).toMatchObject({ state: "failed", binding: { state: "unavailable" }, hostedReady: false });
    expect(await login.status()).toMatchObject({ state: "failed", hostedReady: false });
  } finally { await login.close(); stdin.destroy(); stdout.destroy(); }
});
