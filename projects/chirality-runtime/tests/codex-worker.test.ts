import { describe, expect, it } from "vitest";
import { mkdtemp, readdir, rm, realpath, symlink } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { probeExactCodexWorker, runControlledCodexProbeForTests } from "../packages/daemon/src/codex-worker.js";

async function fixture(code: string) {
  const privateDirectory = await mkdtemp(join(await realpath(tmpdir()), "codex-probe-"));
  const executablePath = await realpath(process.execPath);
  return { input: { executablePath, privateDirectory, args: ["-e", code] }, async close() { await rm(privateDirectory, { recursive: true, force: true }); } };
}
const normal = `
const readline=require('node:readline'); const fs=require('node:fs');
const methods=['initialize','initialized','config/read','configRequirements/read','experimentalFeature/list','account/read'];let i=0;
readline.createInterface({input:process.stdin}).on('line',line=>{
 const r=JSON.parse(line);if(r.method!==methods[i++])process.exit(9);
 if(r.method==='initialized')return;
 if(r.method==='account/read' && (r.params.refreshToken!==false || !fs.readFileSync(process.env.CODEX_HOME+'/config.toml','utf8').includes('network_access = false')))process.exit(8);
 const result=r.method==='account/read'?{account:null,requiresOpenaiAuth:true}:{};
 process.stdout.write(JSON.stringify({id:r.id,result})+'\\n');
});`;
describe("offline Codex readiness adapter", () => {
  it("runs only fixed observed methods in an isolated home and returns sanitized fixture evidence", async () => {
    const f = await fixture(normal);
    try {
      const result = await runControlledCodexProbeForTests(f.input);
      expect(result.evidenceClass).toBe("controlled-fixture"); expect(result.supply).toBeUndefined();
      expect(result.protocolChecks).toEqual(["initialize", "config/read", "configRequirements/read", "experimentalFeature/list", "account/read"].map(method => ({ method, status: "passed" })));
      expect(result.authRequired).toBe(true); expect(result.hostedTurnAvailable).toBe(false);
      expect(JSON.stringify(result)).not.toContain("account:null"); expect(result.exitCode).toBe(0);
      expect(await readdir(f.input.privateDirectory)).toEqual([]);
    } finally { await f.close(); }
  });
  it("does not accept the fixture executable through the production supply verifier", async () => {
    const f = await fixture(normal);
    try { await expect(probeExactCodexWorker(f.input)).rejects.toThrow(); expect(await readdir(f.input.privateDirectory)).toEqual([]); }
    finally { await f.close(); }
  });
  it("stops at a protocol rejection without inferring authentication or readiness", async () => {
    const f = await fixture(`process.stdin.once('data',()=>process.stdout.write(JSON.stringify({id:1,error:{message:'fixture rejection'}})+'\\n'));`);
    try { const result = await runControlledCodexProbeForTests(f.input); expect(result.protocolChecks).toEqual([{ method: "initialize", status: "rejected" }]); expect(result.authRequired).toBeUndefined(); expect(result.hostedTurnAvailable).toBe(false); }
    finally { await f.close(); }
  });
  it("rejects unsolicited responses, malformed messages and output floods then cleans up", async () => {
    for (const output of ['{"id":99,"result":{}}\n', 'not-json\n', 'x'.repeat(300000)]) {
      const f = await fixture(`process.stdin.once('data',()=>process.stdout.write(${JSON.stringify(output)}));`);
      try { await expect(runControlledCodexProbeForTests(f.input)).rejects.toThrow(); expect(await readdir(f.input.privateDirectory)).toEqual([]); }
      finally { await f.close(); }
    }
  });
  it("rejects aliases and bounds a silent process", async () => {
    const f = await fixture('setInterval(()=>{},1000)');
    try {
      const alias = join(f.input.privateDirectory, "alias"); await symlink(f.input.executablePath, alias);
      await expect(runControlledCodexProbeForTests({ ...f.input, executablePath: alias })).rejects.toThrow("aliases");
      await expect(runControlledCodexProbeForTests(f.input)).rejects.toThrow("timed out");
      expect(await readdir(f.input.privateDirectory)).toEqual(["alias"]);
    } finally { await f.close(); }
  }, 8000);
});
