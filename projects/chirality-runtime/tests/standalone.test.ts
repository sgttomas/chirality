import { createServer } from "node:http";
import { spawn, execFile, type ChildProcessWithoutNullStreams } from "node:child_process";
import { chmod, lstat, mkdir, mkdtemp, readFile, realpath, rm, symlink, writeFile } from "node:fs/promises";
import { promisify } from "node:util";
import { prepareCodexContainment } from "../packages/daemon/src/codex-containment.js";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { afterEach, describe, expect, it } from "vitest";
import { AuthRegistry, ProjectRegistry } from "@chirality/runtime-core";
import { RuntimeClient } from "@chirality/runtime-client";
import { readStandaloneConfig, type DelegatedStandaloneConfig } from "../packages/daemon/src/standalone.js";
import { SupervisorClient } from "../packages/daemon/src/supervisor-server.js";
import { createProjectFixture } from "./helpers.js";

const cleanup: (() => Promise<unknown>)[] = [];
afterEach(async () => { for (const action of cleanup.splice(0).reverse()) await action(); });
const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "a".repeat(64) };
async function fixture(register = true) {
  const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "sj-")));
  cleanup.push(() => rm(root, { recursive: true, force: true }));
  const runtimeDirectory = join(root, "r"); await mkdir(runtimeDirectory, { mode: 0o700 });
  const projectRoot = join(root, "project");
  const { manifestPath } = await createProjectFixture(projectRoot, "project");
  let tokenFile = "";
  if (register) {
    await new ProjectRegistry(runtimeDirectory, {}).register(manifestPath, { approvedBy: "fixture", approvalReference: "fixture-only" }, "fixture-client");
    tokenFile = (await new AuthRegistry(runtimeDirectory).issueClient("fixture-client", ["runtime:read", "sessions:read", "sessions:write"], "project")).tokenFile;
  }
  const config: DelegatedStandaloneConfig = {
    schema: "chirality-standalone/v1", mode: "controlled-worker", runtimeDirectory,
    daemonSocket: "d.sock", supervisorSocket: "s/s.sock", supervisorCredential: "s/credential.json",
    project: { projectId: "project", identity: { canonicalRoot: projectRoot, cwd: projectRoot, accountId: "fixture-account", accountEpoch: 1, policyDigest: "fixture-policy" }, compatibility, codexHome: "homes/project", retirementDirectory: "journals/project" },
    worker: { executablePath: await realpath(process.execPath), args: [await realpath(resolve("tests/fixtures/delegated-worker.mjs"))], maxRunMs: 3000 }
  };
  const configPath = join(runtimeDirectory, "config.json");
  const save = async () => writeFile(configPath, JSON.stringify(config), { mode: 0o600 }); await save();
  return { root, config, configPath, save, tokenFile };
}
async function launch(role: string, configPath: string, expectReady = true) {
  const child: ChildProcessWithoutNullStreams = spawn(process.execPath, [resolve("packages/daemon/dist/standalone-bin.js"), role, "--config", configPath], { env: {}, stdio: "pipe" });
  let stdout = "", stderr = "";
  child.stdout.on("data", value => { stdout += value; }); child.stderr.on("data", value => { stderr += value; });
  let exited = false;
  const exit = new Promise<{ code: number | null; signal: NodeJS.Signals | null }>(resolveExit => child.once("exit", (code, signal) => { exited = true; resolveExit({ code, signal }); }));
  async function stop() {
    if (!exited) child.kill("SIGTERM");
    let timer: ReturnType<typeof setTimeout> | undefined;
    try { return await Promise.race([exit, new Promise<never>((_, reject) => { timer = setTimeout(() => { child.kill("SIGKILL"); reject(new Error(`job failed graceful shutdown: ${stderr}`)); }, 5000); })]); }
    finally { clearTimeout(timer); }
  }
  cleanup.push(stop);
  if (expectReady) {
    await new Promise<void>((resolveReady, reject) => {
      const timer = setTimeout(() => { clearInterval(interval); reject(new Error(`job readiness timeout: ${stderr}`)); }, 5000);
      const interval = setInterval(() => {
        if (stdout.includes('"ready":true')) { clearInterval(interval); clearTimeout(timer); resolveReady(); }
        else if (exited) { clearInterval(interval); clearTimeout(timer); reject(new Error(`job exited before readiness: ${stderr}`)); }
      }, 10);
    });
  }
  return { child, stop, exit, output: () => ({ stdout, stderr }) };
}

describe("actual two-job standalone runtime", () => {
  it("retires an eager process generation promptly and permanently rejects later capture", async () => {
    const moduleUrl = pathToFileURL(resolve("packages/core/dist/runtime-conformance.js")).href;
    const script = `const m=await import(${JSON.stringify(moduleUrl)}); const start=performance.now(); await Promise.all([m.retireRuntimeConformanceGeneration(),m.retireRuntimeConformanceGeneration()]); let denied=0; for(let i=0;i<2;i++){try{await m.captureRuntimeConformanceGeneration()}catch{denied++}} if(denied!==2)throw Error("retired generation reopened"); console.log(JSON.stringify({denied,retirementMs:performance.now()-start}));`;
    const { stdout } = await promisify(execFile)(process.execPath, ["--input-type=module", "-e", script], { env: {}, timeout: 2000 });
    const result = JSON.parse(stdout); expect(result.denied).toBe(2); expect(result.retirementMs).toBeLessThan(1000);
  });
  it("executes client consent and turn through two separate jobs and cleans SIGTERM sockets", async () => {
    const f = await fixture();
    const supervisor = await launch("supervisor", f.configPath);
    const daemon = await launch("daemon", f.configPath);
    expect(supervisor.child.pid).not.toBe(daemon.child.pid);
    const credentialPath = join(f.config.runtimeDirectory, f.config.supervisorCredential);
    const secret = JSON.parse(await readFile(credentialPath, "utf8")).credential.token;
    expect((await lstat(credentialPath)).mode & 0o777).toBe(0o600);
    const client = new RuntimeClient({ socketPath: join(f.config.runtimeDirectory, f.config.daemonSocket), tokenFile: f.tokenFile });
    expect(await client.listSessions("project")).toEqual([]);
    expect(await client.delegatedCapabilities("project")).toMatchObject({ approvalRecordsAvailable: true, approvalForwardingSupported: false });
    await client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
    expect(await client.runDelegatedTurn("project", compatibility, { turnId: "standalone", prompt: "hello" })).toMatchObject({ output: "controlled:hello", evidenceClass: "controlled-worker", terminal: { outcome: "completed" } });
    expect(JSON.stringify(supervisor.output()) + JSON.stringify(daemon.output())).not.toContain(secret);
    expect(await daemon.stop()).toMatchObject({ code: 0, signal: null });
    expect(await supervisor.stop()).toMatchObject({ code: 0, signal: null });
    await expect(lstat(join(f.config.runtimeDirectory, f.config.daemonSocket))).rejects.toMatchObject({ code: "ENOENT" });
    await expect(lstat(join(f.config.runtimeDirectory, f.config.supervisorSocket))).rejects.toMatchObject({ code: "ENOENT" });
    await expect(lstat(credentialPath)).rejects.toMatchObject({ code: "ENOENT" });
  });
  it("rotates credentials across supervisor jobs and starts the daemon with the new generation", async () => {
    const f = await fixture();
    const first = await launch("supervisor", f.configPath);
    const credentialPath = join(f.config.runtimeDirectory, f.config.supervisorCredential);
    const old = JSON.parse(await readFile(credentialPath, "utf8"));
    await first.stop();
    const next = await launch("supervisor", f.configPath);
    const fresh = JSON.parse(await readFile(credentialPath, "utf8"));
    expect(fresh.credential.epoch).not.toBe(old.credential.epoch); expect(fresh.credential.token).not.toBe(old.credential.token);
    await expect(new SupervisorClient({ socketPath: fresh.socketPath, credential: old.credential }).inventory()).rejects.toThrow();
    const daemon = await launch("daemon", f.configPath);
    const client = new RuntimeClient({ socketPath: join(f.config.runtimeDirectory, f.config.daemonSocket), tokenFile: f.tokenFile });
    await client.grantDelegatedConsent("project", compatibility, { posture: "off", approvedBy: "fixture-owner", explicitUserAct: true });
    expect((await client.runDelegatedTurn("project", compatibility, { turnId: "new-generation", prompt: "again" })).terminal.outcome).toBe("completed");
    await daemon.stop(); await next.stop();
  });
  it("refuses a forged or nonprivate supervisor credential at daemon startup", async () => {
    const f = await fixture(); await launch("supervisor", f.configPath);
    const path = join(f.config.runtimeDirectory, f.config.supervisorCredential);
    const original = await readFile(path, "utf8");
    const forged = JSON.parse(original); forged.credential.token = "a".repeat(64);
    await writeFile(path, JSON.stringify(forged), { mode: 0o600 });
    const rejected = await launch("daemon", f.configPath, false);
    expect(await rejected.exit).toMatchObject({ code: 1 });
    await writeFile(path, original, { mode: 0o600 }); await chmod(path, 0o644);
    const nonprivate = await launch("daemon", f.configPath, false);
    expect(await nonprivate.exit).toMatchObject({ code: 1 });
    await chmod(path, 0o600);
  });
  it("does not rotate a live supervisor credential when a duplicate job is refused", async () => {
    const f = await fixture(); await launch("supervisor", f.configPath);
    const path = join(f.config.runtimeDirectory, f.config.supervisorCredential);
    const original = await readFile(path, "utf8");
    const duplicate = await launch("supervisor", f.configPath, false);
    expect(await duplicate.exit).toMatchObject({ code: 1 });
    expect(await readFile(path, "utf8")).toBe(original);
  });
  it("does not implicitly register the configured project", async () => {
    const f = await fixture(false); await launch("supervisor", f.configPath);
    const daemon = await launch("daemon", f.configPath, false);
    expect(await daemon.exit).toMatchObject({ code: 1 });
    await expect(lstat(join(f.config.runtimeDirectory, "projects", "registry.json"))).rejects.toMatchObject({ code: "ENOENT" });
  });
  it("refuses a credential symlink before opening the daemon", async () => {
    const f = await fixture(); await launch("supervisor", f.configPath);
    const path = join(f.config.runtimeDirectory, f.config.supervisorCredential), target = join(f.config.runtimeDirectory, "copied.json");
    await writeFile(target, await readFile(path), { mode: 0o600 }); await rm(path); await symlink(target, path);
    const daemon = await launch("daemon", f.configPath, false);
    expect(await daemon.exit).toMatchObject({ code: 1 });
    // Restore so the supervisor can perform its own epoch-checked teardown.
    await rm(path); await writeFile(path, await readFile(target), { mode: 0o600 });
  });
  it("seats hosted-validation only with a dedicated worker-private subtree", async () => {
    const f = await fixture();
    const privateDirectory = join(f.config.runtimeDirectory, "worker"); await mkdir(privateDirectory, { mode: 0o700 });
    const executablePath = join(privateDirectory, "fixture-not-vendor"); await writeFile(executablePath, "#!/bin/sh\nexit 0\n", { mode: 0o700 });
    const hosted = { ...f.config, mode: "hosted-validation" as const, project: { ...f.config.project, codexHome: "worker/codex" },
      worker: { executablePath, privateDirectory: "worker", model: "explicit-model", authBindingSha256: "a".repeat(64), providerNetworkConsent: { approvedBy: "fixture", approvalReference: "validation-only-no-account-use" } } };
    await writeFile(f.configPath, JSON.stringify(hosted), { mode: 0o600 });
    expect((await readStandaloneConfig(f.configPath)).mode).toBe("hosted-validation");
    const conformance = { recordPath: "conformance/record.json", acceptancePath: "conformance/acceptance.json", ownerActPath: f.configPath, ownerActSha256: "a".repeat(64), activationId: "mechanical-fixture", gateIdentity: "fixture-G4" };
    await writeFile(f.configPath, JSON.stringify({ ...hosted, worker: { ...hosted.worker, conformance } }));
    expect((await readStandaloneConfig(f.configPath)).mode).toBe("hosted-validation");
    await writeFile(f.configPath, JSON.stringify({ ...hosted, worker: { ...hosted.worker, conformance: { ...conformance, recordPath: "worker/forbidden-record.json" } } }));
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await writeFile(f.configPath, JSON.stringify({ ...hosted, worker: { ...hosted.worker, privateDirectory: "auth" } }), { mode: 0o600 });
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await writeFile(f.configPath, JSON.stringify({ ...hosted, project: { ...hosted.project, retirementDirectory: "worker/journal" } }), { mode: 0o600 });
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await writeFile(f.configPath, JSON.stringify({ ...hosted, worker: { ...hosted.worker, args: ["--unsafe"] } }), { mode: 0o600 });
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
  it.runIf(process.platform === "darwin")("actual sandbox cannot read or write sibling broker credentials", async () => {
    const f = await fixture();
    const worker = join(f.config.runtimeDirectory, "worker"), home = join(worker, "codex"); await mkdir(home, { recursive: true, mode: 0o700 });
    const secret = join(f.config.runtimeDirectory, "auth", "broker-secret"); await writeFile(secret, "fixture-private-value", { mode: 0o600 });
    const containment = await prepareCodexContainment({ canonicalRoot: f.config.project.identity.canonicalRoot, privateDirectory: worker, codexHome: home });
    try {
      await expect(promisify(execFile)("/usr/bin/sandbox-exec", [...containment.args, "/bin/cat", secret], { env: containment.environment })).rejects.toThrow();
      await expect(promisify(execFile)("/usr/bin/sandbox-exec", [...containment.args, "/bin/sh", "-c", 'printf changed > "$1"', "fixture", secret], { env: containment.environment })).rejects.toThrow();
      expect(await readFile(secret, "utf8")).toBe("fixture-private-value");
    } finally { await containment.cleanup(); }
  });
  it("refuses unknown public-network or production-mode configuration", async () => {
    const f = await fixture();
    await writeFile(f.configPath, JSON.stringify({ ...f.config, host: "0.0.0.0", port: 8000 }), { mode: 0o600 });
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await writeFile(f.configPath, JSON.stringify({ ...f.config, mode: "provider-observed" }), { mode: 0o600 });
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("rejects unsafe config mode, symlink aliases and escaping storage", async () => {
    const f = await fixture(); await chmod(f.configPath, 0o644);
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await chmod(f.configPath, 0o600);
    const alias = join(f.config.runtimeDirectory, "alias.json"); await symlink(f.configPath, alias);
    await expect(readStandaloneConfig(alias)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await rm(alias);
    f.config.supervisorSocket = "../outside.sock"; await f.save();
    await expect(readStandaloneConfig(f.configPath)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });
});

it("starts a real local-only daemon job without any Codex supervisor credential", async () => {
  const f = await fixture();
  const server = createServer((_req, res) => { res.setHeader("content-type", "application/json"); res.end(JSON.stringify({ models: [{ id: "local-fixture", kind: "llm", loaded: true }] })); });
  await new Promise<void>(resolve => server.listen(0, "127.0.0.1", resolve));
  cleanup.push(() => new Promise<void>(resolve => { server.closeAllConnections(); server.close(() => resolve()); }));
  await writeFile(join(f.config.runtimeDirectory, "local-secret.json"), JSON.stringify({ providerId: "omlx", credential: "synthetic-secret" }), { mode: 0o600 });
  await writeFile(f.configPath, JSON.stringify({ schema: "chirality-standalone/v1", mode: "local-engine-only", runtimeDirectory: f.config.runtimeDirectory, daemonSocket: "local.sock", project: { projectId: "project", canonicalRoot: f.config.project.identity.canonicalRoot }, engine: { baseUrl: `http://127.0.0.1:${(server.address() as { port: number }).port}/v1`, model: { id: "local-fixture", contextWindow: 8192, maxTokens: 512 }, credentialFile: "local-secret.json", approvalReference: "synthetic-selection" } }), { mode: 0o600 });
  const daemon = await launch("daemon", f.configPath);
  expect(daemon.output().stdout).toContain('"mode":"local-engine-only"');
  const client = new RuntimeClient({ socketPath: join(f.config.runtimeDirectory, "local.sock"), tokenFile: f.tokenFile });
  expect(await client.listSessions("project")).toEqual([]);
  expect(await daemon.stop()).toMatchObject({ code: 0 });
  await expect(lstat(join(f.config.runtimeDirectory, f.config.supervisorCredential))).rejects.toMatchObject({ code: "ENOENT" });
});
