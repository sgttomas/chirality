import { describe, expect, it } from "vitest";
import { spawn } from "node:child_process";
import { mkdtemp, readFile, realpath, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createHash } from "node:crypto";
import { CodexLogin, createControlledCodexLoginForTests } from "../packages/daemon/src/codex-login.js";
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
   if(mode!=='failed')require('node:fs').writeFileSync(process.env.CODEX_HOME+'/auth.json',JSON.stringify({fixture:'not-a-real-credential'}),{mode:mode==='unsafe'?0o644:0o600});
   send({method:'account/login/completed',params:{loginId:mode==='mismatch'?'other':'login1',success:mode!=='failed',error:null}});
  },20);return;
 }
 if(r.method==='account/read'){if(r.params.refreshToken!==false)process.exit(8);send({id:r.id,result:{account:{fixture:true},requiresOpenaiAuth:true}});return;}
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
  it("waits for actual completion and binds private persisted auth without exposing it", async () => {
    const f = await fixture();
    try {
      expect(await f.login.startLogin()).toEqual({ loginId: "login1", authUrl: "https://auth.openai.com/authorize?state=fixture" });
      await expect.poll(async () => (await f.login.status()).state).toBe("completed");
      const bytes = await readFile(join(f.codexHome, "auth.json")); const status = await f.login.status();
      expect(status.authBindingSha256).toBe(createHash("sha256").update(bytes).digest("hex")); expect(status.hasAccount).toBe(true); expect(status.evidenceClass).toBe("controlled-fixture");
      expect(JSON.stringify(status)).not.toContain("not-a-real-credential");
      await f.login.close(); expect(await readFile(join(f.codexHome, "auth.json"))).toEqual(bytes);
    } finally { await f.close(); }
  });
  it("rejects nonofficial origins, plain HTTP and URL credentials", async () => {
    for (const url of ["https://auth.openai.com.evil.example/login", "http://auth.openai.com/login", "https://user:pass@auth.openai.com/login", "https://auth.openai.com:8443/login"]) {
      const f = await fixture("pending", url);
      try { await expect(f.login.startLogin()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
      finally { await f.close(); }
    }
  });
  it("fails for unsafe auth-file mode, mismatched completion, provider failure and clean exit", async () => {
    for (const mode of ["unsafe", "mismatch", "failed", "exit"]) {
      const f = await fixture(mode);
      try { await f.login.startLogin(); await expect.poll(async () => (await f.login.status()).state).toBe("failed"); expect((await f.login.status()).authBindingSha256).toBeUndefined(); }
      finally { await f.close(); }
    }
  });
  it("cancels pending login and prevents double start without clearing persisted home", async () => {
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
