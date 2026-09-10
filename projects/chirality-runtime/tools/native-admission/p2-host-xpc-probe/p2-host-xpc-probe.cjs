"use strict";

const { execFileSync, spawn, spawnSync } = require("node:child_process");
const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const { parseExactArgs, runtimeEvidence, assertElectronRuntime, verifyRegularFileIdentity } = require("../native-load-probe.cjs");

const SERVICE = "com.chirality.app.runtime.account-host";

function deadline(promise, milliseconds, label) {
  let timer;
  return Promise.race([promise, new Promise((_, reject) => { timer = setTimeout(() => reject(new Error(`timeout:${label}`)), milliseconds); })])
    .finally(() => clearTimeout(timer));
}

function xml(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&apos;");
}

function launchAgentPlist({ label, programArguments, stdout, stderr, environment = {} }) {
  const args = programArguments.map((value) => `<string>${xml(value)}</string>`).join("");
  const variables = Object.entries(environment).sort(([left], [right]) => left.localeCompare(right))
    .map(([key, value]) => `<key>${xml(key)}</key><string>${xml(value)}</string>`).join("");
  return `<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0"><dict><key>Label</key><string>${xml(label)}</string><key>ProgramArguments</key><array>${args}</array><key>MachServices</key><dict><key>${SERVICE}</key><true/></dict><key>RunAtLoad</key><true/><key>KeepAlive</key><false/><key>ProcessType</key><string>Interactive</string><key>StandardOutPath</key><string>${xml(stdout)}</string><key>StandardErrorPath</key><string>${xml(stderr)}</string><key>EnvironmentVariables</key><dict>${variables}</dict></dict></plist>\n`;
}

function fixedServiceUnoccupied(domainText) {
  return !domainText.includes(SERVICE);
}

function exactOwnedJob(jobText, { label, expiringExec, serverHost }) {
  return jobText.includes(label) && jobText.includes(expiringExec) && jobText.includes(serverHost);
}

function readRecords(file) {
  if (!fs.existsSync(file)) return [];
  return fs.readFileSync(file, "utf8").split("\n").filter(Boolean).map((line) => JSON.parse(line));
}

function sha256File(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}

async function waitForRecord(file, predicate, label) {
  let timer;
  return deadline(new Promise((resolve) => {
    const poll = () => {
      const found = readRecords(file).find(predicate);
      if (found) resolve(found); else timer = setTimeout(poll, 25);
    };
    poll();
  }), 5000, label).finally(() => clearTimeout(timer));
}

async function waitForJobAbsent(target) {
  let timer;
  return deadline(new Promise((resolve, reject) => {
    const poll = () => {
      try {
        const result = spawnSync("/bin/launchctl", ["print", target], { encoding: "utf8", maxBuffer: 1024 * 1024 });
        if (result.error) throw result.error;
        if (result.status === 0) {
          timer = setTimeout(poll, 25);
          return;
        }
        const diagnostic = `${result.stdout ?? ""}\n${result.stderr ?? ""}`;
        if (!/Could not find service|service not found/u.test(diagnostic)) throw new Error("owned-job-retirement-unreadable");
        resolve();
      } catch (error) {
        reject(error);
      }
    };
    poll();
  }), 5000, "owned-job-retirement").finally(() => clearTimeout(timer));
}

async function waitForServiceAbsent(domain) {
  let timer;
  return deadline(new Promise((resolve, reject) => {
    const poll = () => {
      try {
        const state = execFileSync("/bin/launchctl", ["print", domain], { encoding: "utf8", maxBuffer: 16 * 1024 * 1024 });
        if (fixedServiceUnoccupied(state)) resolve(); else timer = setTimeout(poll, 25);
      } catch (error) {
        reject(error);
      }
    };
    poll();
  }), 5000, "fixed-service-retirement").finally(() => clearTimeout(timer));
}

function captureChild({ command, args, environment, evidenceRoot, caseId, timeoutMs = 12000 }) {
  fs.mkdirSync(evidenceRoot, { mode: 0o700, recursive: true });
  const stdoutPath = path.join(evidenceRoot, `${caseId}.stdout`);
  const stderrPath = path.join(evidenceRoot, `${caseId}.stderr`);
  const metadataPath = path.join(evidenceRoot, `${caseId}.process.json`);
  const stdoutFd = fs.openSync(stdoutPath, "wx", 0o600);
  const stderrFd = fs.openSync(stderrPath, "wx", 0o600);
  const started = Date.now();
  const state = { stdoutBytes: 0, stderrBytes: 0, stdoutRetained: 0, stderrRetained: 0, overflow: false, spawnError: null, exitCode: null, signal: null, exitObserved: false, stdoutClosed: false, stderrClosed: false, closeObserved: false, timedOut: false, events: [] };
  let timer;
  return new Promise((resolve) => {
    let settled = false;
    const retain = (fd, field, retainedField, chunk) => {
      if (settled) return;
      state[field] += chunk.length;
      const remaining = 65536 - state[retainedField];
      if (remaining > 0) {
        const bytes = chunk.subarray(0, remaining);
        fs.writeSync(fd, bytes);
        state[retainedField] += bytes.length;
      }
      if (chunk.length > remaining) state.overflow = true;
    };
    const finish = () => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      fs.closeSync(stdoutFd); fs.closeSync(stderrFd);
      const metadata = {
        schemaVersion: "chirality.p2-host-xpc-child-process/v1", caseId, command, args, environment,
        ...state, elapsedMs: Date.now() - started, stdoutPath, stderrPath,
        stdoutSha256: sha256File(stdoutPath), stderrSha256: sha256File(stderrPath)
      };
      fs.writeFileSync(metadataPath, `${JSON.stringify(metadata, null, 2)}\n`, { flag: "wx", mode: 0o600 });
      resolve({ ...metadata, metadataPath });
    };
    let child;
    try { child = spawn(command, args, { shell: false, stdio: ["ignore", "pipe", "pipe"], env: environment }); state.events.push({ phase: "spawned", elapsedMs: Date.now() - started }); }
    catch (error) { state.spawnError = error instanceof Error ? error.message : "spawn-failed"; state.events.push({ phase: "spawn-failed", elapsedMs: Date.now() - started }); finish(); return; }
    child.stdout.on("data", (chunk) => retain(stdoutFd, "stdoutBytes", "stdoutRetained", chunk));
    child.stderr.on("data", (chunk) => retain(stderrFd, "stderrBytes", "stderrRetained", chunk));
    child.stdout.once("close", () => { state.stdoutClosed = true; state.events.push({ phase: "stdout-closed", elapsedMs: Date.now() - started }); });
    child.stderr.once("close", () => { state.stderrClosed = true; state.events.push({ phase: "stderr-closed", elapsedMs: Date.now() - started }); });
    child.once("error", (error) => { state.spawnError = error.message; state.events.push({ phase: "spawn-error", elapsedMs: Date.now() - started }); });
    child.once("exit", (code, signal) => { state.exitObserved = true; state.exitCode = code; state.signal = signal; state.events.push({ phase: "exit", elapsedMs: Date.now() - started }); });
    child.once("close", (code, signal) => { state.closeObserved = true; state.exitCode = code; state.signal = signal; state.events.push({ phase: "close", elapsedMs: Date.now() - started }); setImmediate(finish); });
    timer = setTimeout(() => { state.timedOut = true; state.events.push({ phase: "observation-timeout", elapsedMs: Date.now() - started }); finish(); }, timeoutMs);
  });
}

function assessClientCapture(capture) {
  if (capture.spawnError) throw Object.assign(new Error(`client-spawn:${capture.spawnError}`), { caseEvidence: capture });
  if (capture.timedOut || !capture.closeObserved || !capture.stdoutClosed || !capture.stderrClosed) throw Object.assign(new Error("client-observation-timeout"), { caseEvidence: capture });
  if (capture.overflow) throw Object.assign(new Error("client-output-too-large"), { caseEvidence: capture });
  let records;
  try { records = fs.readFileSync(capture.stdoutPath, "utf8").split("\n").filter(Boolean).map((line) => JSON.parse(line)); }
  catch { throw Object.assign(new Error("malformed-client-output"), { caseEvidence: capture }); }
  const detail = records.length === 1 ? records[0] : null;
  const evidence = { ...capture, resultRecord: detail };
  if (capture.exitCode !== 0 || capture.signal !== null || records.length !== 1 || detail?.result !== "PASS") {
    const reason = detail?.result === "FAIL" && typeof detail.reason === "string" ? detail.reason : `client-exit:${capture.exitCode}:${capture.signal ?? "none"}`;
    throw Object.assign(new Error(reason), { caseEvidence: evidence });
  }
  return evidence;
}

async function runClient(expiringExec, executable, driver, common, { requestId, mode, environment, evidenceRoot }) {
  fs.mkdirSync(evidenceRoot, { mode: 0o700, recursive: true });
  if (!fs.statSync(evidenceRoot).isDirectory() || (fs.statSync(evidenceRoot).mode & 0o777) !== 0o700) throw new Error("unsafe-client-evidence-root");
  const diagnostic = path.join(evidenceRoot, `${requestId}.diagnostic.jsonl`);
  fs.writeFileSync(diagnostic, "", { flag: "wx", mode: 0o600 });
  const args = ["10", executable, driver, ...common, "--role", "client", "--request-id", requestId, "--mode", mode, "--diagnostic", diagnostic];
  const capture = await captureChild({ command: expiringExec, args, environment, evidenceRoot, caseId: requestId });
  let diagnosticEvidence;
  try { diagnosticEvidence = { diagnosticPath: diagnostic, diagnosticSha256: sha256File(diagnostic), milestones: readRecords(diagnostic) }; }
  catch { throw Object.assign(new Error("malformed-client-diagnostic"), { caseEvidence: { ...capture, diagnosticPath: diagnostic, diagnosticSha256: sha256File(diagnostic) } }); }
  let evidence;
  try { evidence = assessClientCapture(capture); }
  catch (error) { error.caseEvidence = { ...(error.caseEvidence ?? capture), ...diagnosticEvidence }; throw error; }
  Object.assign(evidence, diagnosticEvidence);
  return evidence;
}

function assertWrongPeerEvidence(evidence) {
  const events = new Set(evidence.milestones.map((record) => record.event));
  for (const required of ["load-started", "load-completed", "client-binding-loaded", "client-created", "provision-invoked", "close-completed"]) {
    if (!events.has(required)) throw new Error(`wrong-peer-missing-${required}`);
  }
  if (events.has("challenge-observed") || events.has("grant-observed")) throw new Error("wrong-peer-client-ceremony-observed");
  const result = evidence.resultRecord;
  if (!result || result.mode !== "wrong-peer" || result.requestId !== "wrong-peer" || !["remote-terminal", "observation-expired-local-close"].includes(result.disposition)) throw new Error("wrong-peer-disposition-invalid");
  if (result.disposition === "remote-terminal" && !["peer-invalidated", "peer-interrupted", "peer-requirement-rejected"].includes(result.invalidation)) throw new Error("wrong-peer-terminal-invalid");
}

function assertNoWrongServerEvents(before, after, requestId) {
  const added = after.slice(before.length);
  if (added.some((record) => record.event === "admitted" || ((record.event === "open" || record.event === "finish") && record.requestId === requestId))) {
    throw new Error("wrong-peer-reached-server");
  }
}

function pressureTerminalEvidence(cases) {
  const result = cases.find((entry) => entry.name === "bounded-terminal-delivery-pressure")?.evidence?.resultRecord;
  return Number.isSafeInteger(result?.terminallyRejected) && result.terminallyRejected > 0;
}

function applyFinalWrongServerCheck(output, records) {
  const wrongCase = output.cases.find((entry) => entry.name === "wrong-peer-bounded-nonadmission");
  if (!wrongCase || !records.some((record) => record.requestId === "wrong-peer" && (record.event === "open" || record.event === "finish"))) return true;
  wrongCase.result = "FAIL";
  wrongCase.reason = "wrong-peer-late-server-ceremony";
  output.result = "FAIL";
  if (output.primaryFailure === null) output.primaryFailure = "wrong-peer-late-server-ceremony";
  output.reason = output.primaryFailure;
  return false;
}

function assertCodeRequirement(executable, requirement, shouldMatch) {
  let matched = true;
  try { execFileSync("/usr/bin/codesign", ["--verify", `-R=${requirement}`, executable], { stdio: "pipe" }); }
  catch { matched = false; }
  if (matched !== shouldMatch) throw new Error(shouldMatch ? "signed-driver-requirement-mismatch" : "wrong-driver-satisfied-correct-requirement");
}

async function main(argv = process.argv.slice(2)) {
  const output = {
    schemaVersion: "chirality.p2-host-xpc-probe/v1",
    scope: "isolated signed synthetic XPC drivers; not packaged App, account, supplier, model, or release qualification",
    runtime: runtimeEvidence(), cases: [], result: "FAIL", reason: null, primaryFailure: null, cleanupFailure: null
  };
  let ownJob = null;
  try {
    const args = parseExactArgs(argv, [
      "--addon", "--addon-sha256", "--wrapper", "--wrapper-sha256", "--driver", "--driver-sha256",
      "--expiring-exec", "--expiring-exec-sha256", "--server-host", "--server-host-sha256",
      "--correct-client-host", "--correct-client-host-sha256", "--wrong-client-host", "--wrong-client-host-sha256",
      "--correct-requirement", "--wrong-requirement", "--run-root"
    ]);
    assertElectronRuntime(output.runtime);
    const identities = Object.fromEntries([
      ["addon", "--addon"], ["wrapper", "--wrapper"], ["driver", "--driver"], ["expiringExec", "--expiring-exec"],
      ["serverHost", "--server-host"], ["correctClientHost", "--correct-client-host"], ["wrongClientHost", "--wrong-client-host"]
    ].map(([key, flag]) => [key, verifyRegularFileIdentity(args[flag], args[`${flag}-sha256`])]));
    const runRoot = args["--run-root"];
    if (!path.isAbsolute(runRoot) || path.normalize(runRoot) !== runRoot || fs.existsSync(runRoot)) throw new Error("unsafe-run-root");
    fs.mkdirSync(runRoot, { mode: 0o700 });
    if (fs.realpathSync.native(runRoot) !== runRoot || (fs.statSync(runRoot).mode & 0o777) !== 0o700) throw new Error("unsafe-run-root");
    const home = path.join(runRoot, "home"), tmp = path.join(runRoot, "tmp");
    fs.mkdirSync(home, { mode: 0o700 }); fs.mkdirSync(tmp, { mode: 0o700 });
    const driverEnvironment = { ELECTRON_RUN_AS_NODE: "1", HOME: home, LANG: "en_US.UTF-8", PATH: "/usr/bin:/bin:/usr/sbin:/sbin", TMPDIR: tmp };
    const evidenceRoot = path.join(runRoot, "clients");
    assertCodeRequirement(identities.serverHost.path, args["--correct-requirement"], true);
    assertCodeRequirement(identities.correctClientHost.path, args["--correct-requirement"], true);
    assertCodeRequirement(identities.wrongClientHost.path, args["--wrong-requirement"], true);
    assertCodeRequirement(identities.wrongClientHost.path, args["--correct-requirement"], false);
    const domain = `gui/${process.geteuid()}`;
    const domainState = execFileSync("/bin/launchctl", ["print", domain], { encoding: "utf8", maxBuffer: 16 * 1024 * 1024 });
    if (!fixedServiceUnoccupied(domainState)) throw new Error("fixed-mach-service-occupied");
    const label = `com.chirality.probe.${crypto.randomUUID()}`;
    const log = path.join(runRoot, "server.jsonl"), stderr = path.join(runRoot, "server.stderr"), plist = path.join(runRoot, "server.plist");
    fs.writeFileSync(log, "", { flag: "wx", mode: 0o600 });
    fs.writeFileSync(stderr, "", { flag: "wx", mode: 0o600 });
    const common = ["--addon", identities.addon.path, "--addon-sha256", identities.addon.sha256, "--wrapper", identities.wrapper.path, "--wrapper-sha256", identities.wrapper.sha256, "--peer-requirement", args["--correct-requirement"]];
    const programArguments = [identities.expiringExec.path, "45", identities.serverHost.path, identities.driver.path, ...common, "--role", "server", "--log", log];
    fs.writeFileSync(plist, launchAgentPlist({ label, programArguments, stdout: log, stderr, environment: driverEnvironment }), { flag: "wx", mode: 0o600 });
    execFileSync("/bin/launchctl", ["bootstrap", domain, plist], { stdio: "pipe" });
    ownJob = { domain, label, expiringExec: identities.expiringExec.path, serverHost: identities.serverHost.path, log };
    await waitForRecord(log, (record) => record.event === "ready", "server-ready");

    const correctBefore = await runClient(identities.expiringExec.path, identities.correctClientHost.path, identities.driver.path, common, { requestId: "correct-replacement", mode: "client-close", environment: driverEnvironment, evidenceRoot });
    await waitForRecord(log, (record) => record.event === "pong" && record.requestId === "ping-correct-replacement", "control-before-pong");
    output.cases.push({ name: "correct-control-before", result: "PASS", evidence: correctBefore });
    const serverBeforeWrong = readRecords(log);
    const wrongPeerEvidence = await runClient(identities.expiringExec.path, identities.wrongClientHost.path, identities.driver.path, common, { requestId: "wrong-peer", mode: "wrong-peer", environment: driverEnvironment, evidenceRoot });
    assertWrongPeerEvidence(wrongPeerEvidence);
    assertNoWrongServerEvents(serverBeforeWrong, readRecords(log), "wrong-peer");
    const correctAfter = await runClient(identities.expiringExec.path, identities.correctClientHost.path, identities.driver.path, common, { requestId: "correct-close", mode: "server-close", environment: driverEnvironment, evidenceRoot });
    await waitForRecord(log, (record) => record.event === "pong" && record.requestId === "ping-correct-close", "correct-pong");
    if (readRecords(log).some((record) => record.requestId === "wrong-peer" && (record.event === "open" || record.event === "finish"))) throw new Error("wrong-peer-late-server-ceremony");
    output.cases.push({ name: "wrong-peer-bounded-nonadmission", result: "PASS", evidence: wrongPeerEvidence });
    output.cases.push({ name: "correct-control-after-server-close", result: "PASS", evidence: correctAfter });
    output.cases.push({ name: "pending-close-late-callback-fenced", result: "PASS", evidence: await runClient(identities.expiringExec.path, identities.correctClientHost.path, identities.driver.path, common, { requestId: "late-callback", mode: "pending-close", environment: driverEnvironment, evidenceRoot }) });
    if (readRecords(log).some((record) => record.requestId === "late-callback" && record.event === "finish")) throw new Error("late-callback-resurrected");
    output.cases.push({ name: "bounded-terminal-delivery-pressure", result: "PASS", evidence: await runClient(identities.expiringExec.path, identities.correctClientHost.path, identities.driver.path, common, { requestId: "pressure", mode: "pressure", environment: driverEnvironment, evidenceRoot }) });
    output.result = "PASS";
  } catch (error) {
    output.primaryFailure = error instanceof Error ? error.message : "unknown-failure";
    output.reason = output.primaryFailure;
    if (error?.caseEvidence) output.cases.push({ name: "failed-client-case", result: "FAIL", evidence: error.caseEvidence });
  } finally {
    if (ownJob) {
      try {
        const target = `${ownJob.domain}/${ownJob.label}`;
        const state = execFileSync("/bin/launchctl", ["print", target], { encoding: "utf8", maxBuffer: 1024 * 1024 });
        if (!exactOwnedJob(state, ownJob)) throw new Error("owned-launchagent-identity-changed");
        execFileSync("/bin/launchctl", ["kill", "SIGTERM", target], { stdio: "pipe" });
        let terminalError;
        try { await waitForRecord(ownJob.log, (record) => record.event === "closed" || record.event === "close-failed", "server-terminal"); }
        catch (error) { terminalError = error; }
        const retained = execFileSync("/bin/launchctl", ["print", target], { encoding: "utf8", maxBuffer: 1024 * 1024 });
        if (!exactOwnedJob(retained, ownJob)) throw new Error("owned-launchagent-identity-changed-before-bootout");
        execFileSync("/bin/launchctl", ["bootout", target], { stdio: "pipe" });
        await waitForJobAbsent(target);
        await waitForServiceAbsent(ownJob.domain);
        const terminal = readRecords(ownJob.log);
        applyFinalWrongServerCheck(output, terminal);
        const closeFailure = terminal.find((record) => record.event === "close-failed");
        const pressureTerminal = pressureTerminalEvidence(output.cases);
        const observedTerminal = terminal.some((record) => record.event === "closed")
          || (pressureTerminal && closeFailure?.reason === "delivery-unavailable");
        if (terminalError || !observedTerminal || (closeFailure && closeFailure.reason !== "delivery-unavailable")) throw new Error("owned-launchagent-terminal-delivery-unproved");
      } catch (error) {
        output.result = "FAIL";
        output.cleanupFailure = error instanceof Error ? error.message : "unknown";
        if (output.primaryFailure === null) output.reason = `cleanup:${output.cleanupFailure}`;
      }
    }
    process.stdout.write(`${JSON.stringify(output)}\n`);
  }
  return output.result === "PASS" ? 0 : 1;
}

module.exports = { applyFinalWrongServerCheck, assessClientCapture, assertNoWrongServerEvents, assertWrongPeerEvidence, captureChild, exactOwnedJob, fixedServiceUnoccupied, launchAgentPlist, main, pressureTerminalEvidence, runClient };
if (require.main === module) main().then((code) => { process.exitCode = code; });
