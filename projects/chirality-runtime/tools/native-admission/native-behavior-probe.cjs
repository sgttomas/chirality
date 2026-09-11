"use strict";

const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const { parseExactArgs, runtimeEvidence, assertElectronRuntime, sameIdentity, verifyRegularFileIdentity } = require("./native-load-probe.cjs");

const EXPECTED_PATH = "/usr/bin:/bin:/usr/sbin:/sbin";
const EXPECTED_LANG = "en_US.UTF-8";
const SECRET = Buffer.alloc(32, 0x5a);

function deadline(promise, milliseconds, label) {
  let timer;
  return Promise.race([
    promise,
    new Promise((_, reject) => { timer = setTimeout(() => reject(new Error(`timeout:${label}`)), milliseconds); }),
  ]).finally(() => clearTimeout(timer));
}

function decodeHex(value) {
  if (typeof value !== "string" || value.length % 2 || !/^[a-f0-9]*$/.test(value)) throw new Error("invalid-fixture-hex");
  return Buffer.from(value, "hex").toString("utf8");
}

function createRecordReader(child) {
  let buffered = "";
  let ended = false;
  async function next(label) {
    for (;;) {
      const newline = buffered.indexOf("\n");
      if (newline >= 0) {
        const line = buffered.slice(0, newline);
        buffered = buffered.slice(newline + 1);
        return JSON.parse(line);
      }
      if (ended) return null;
      const bytes = await deadline(child.read(), 6000, label);
      if (!Buffer.isBuffer(bytes)) throw new Error("invalid-native-read");
      if (bytes.length === 0) { ended = true; continue; }
      buffered += bytes.toString("utf8");
      if (buffered.length > 1024 * 1024) throw new Error("fixture-output-too-large");
    }
  }
  return { next };
}

function expectThrow(fn, label) {
  try { fn(); } catch { return; }
  throw new Error(`accepted-malformed:${label}`);
}

function expectAllThrow(entries) {
  const accepted = [];
  for (const [label, invoke] of entries) {
    try { invoke(); accepted.push(label); } catch {}
  }
  if (accepted.length) throw new Error(`accepted-malformed:${accepted.join(",")}`);
}

function resultRecorder(cleanup) {
  const cases = [];
  return {
    cases,
    async run(name, fn) {
      try { const evidence = await fn(); cases.push({ name, result: "PASS", ...(evidence || {}) }); }
      catch (error) { cases.push({ name, result: "FAIL", reason: error instanceof Error ? error.message : "unknown-failure" }); }
      try { await cleanup(); }
      catch (error) { cases.push({ name: `${name}:cleanup`, result: "FAIL", reason: error instanceof Error ? error.message : "unknown-cleanup-failure" }); }
    },
    incomplete(name, reason, evidence) { cases.push({ name, result: "NOT_RUN", reason, ...(evidence || {}) }); },
  };
}

function makeEnvironment(runRoot) {
  return [
    `CODEX_HOME=${path.join(runRoot, "codex-home")}`,
    `HOME=${path.join(runRoot, "home")}`,
    `LANG=${EXPECTED_LANG}`,
    `PATH=${EXPECTED_PATH}`,
    `TMPDIR=${path.join(runRoot, "tmp")}`,
  ];
}

function prepareRunRoot(runRoot) {
  if (!path.isAbsolute(runRoot) || path.normalize(runRoot) !== runRoot) throw new Error("unsafe-run-root");
  try { fs.lstatSync(runRoot); throw new Error("run-root-already-exists"); }
  catch (error) { if (error && error.message === "run-root-already-exists") throw error; if (!error || error.code !== "ENOENT") throw error; }
  fs.mkdirSync(runRoot, { mode: 0o700 });
  if (fs.realpathSync.native(runRoot) !== runRoot) throw new Error("noncanonical-run-root");
  if ((fs.statSync(runRoot).mode & 0o777) !== 0o700) throw new Error("run-root-mode");
  for (const name of ["home", "codex-home", "tmp", "cwd"]) fs.mkdirSync(path.join(runRoot, name), { mode: 0o700 });
}

async function collectToEof(reader, label) {
  const records = [];
  for (;;) {
    const record = await reader.next(label);
    if (record === null) return records;
    records.push(record);
  }
}

async function main(argv = process.argv.slice(2)) {
  const output = {
    schemaVersion: "chirality.native-behavior-probe/v1",
    scope: "synthetic native-admission fixture only; no supplier, account, credential, Plan, packaging, or release qualification",
    runtime: runtimeEvidence(), addon: null, fixture: null, runRoot: null, cases: [], result: "FAIL", reason: null,
  };
  let createdRunRoot = false;
  try {
    const args = parseExactArgs(argv, ["--addon", "--addon-sha256", "--fixture", "--fixture-sha256", "--run-root"]);
    const addonIdentity = verifyRegularFileIdentity(args["--addon"], args["--addon-sha256"]);
    const fixtureIdentity = verifyRegularFileIdentity(args["--fixture"], args["--fixture-sha256"]);
    fs.accessSync(fixtureIdentity.path, fs.constants.X_OK);
    output.addon = { path: addonIdentity.path, sha256: addonIdentity.sha256 };
    output.fixture = { path: fixtureIdentity.path, sha256: fixtureIdentity.sha256 };
    assertElectronRuntime(output.runtime);
    prepareRunRoot(args["--run-root"]);
    createdRunRoot = true;
    output.runRoot = args["--run-root"];
    const binding = require(addonIdentity.path);
    const afterLoad = verifyRegularFileIdentity(addonIdentity.path, addonIdentity.sha256);
    if (!sameIdentity(addonIdentity, afterLoad)) throw new Error("addon-identity-changed-during-load");
    if (!binding || typeof binding.acquire !== "function" || typeof binding.spawnSupplier !== "function") throw new Error("addon-api-mismatch");
    const runRoot = output.runRoot;
    const environment = makeEnvironment(runRoot);
    const cwd = path.join(runRoot, "cwd");
    const active = new Map();
    const activeLeases = new Set();
    const acquire = (directory) => {
      const lease = binding.acquire(directory, "runtime-admission-authority.lock");
      activeLeases.add(lease);
      return lease;
    };
    const spawn = (fixtureArgs, secret = SECRET, selectedCwd = cwd, selectedEnvironment = environment, group = true) => {
      const currentFixture = verifyRegularFileIdentity(fixtureIdentity.path, fixtureIdentity.sha256);
      if (!sameIdentity(fixtureIdentity, currentFixture)) throw new Error("fixture-identity-changed-before-spawn");
      const child = binding.spawnSupplier(fixtureIdentity.path, fixtureArgs, secret, selectedCwd, selectedEnvironment, group);
      if (!child || !Number.isSafeInteger(child.pid) || child.pid <= 0 || ["read", "write", "observeLeader", "reapLeader", "groupRetired", "closeInput", "terminate", "kill"].some((name) => typeof child[name] !== "function")) throw new Error("invalid-native-child");
      active.set(child, { observed: null, observePromise: null, reaped: false, reapPromise: null });
      return child;
    };
    const unexpectedRaw = (...rawArgs) => {
      const child = binding.spawnSupplier(...rawArgs);
      if (child && Number.isSafeInteger(child.pid) && child.pid > 0 && ["observeLeader", "reapLeader", "groupRetired", "closeInput", "terminate", "kill"].every((name) => typeof child[name] === "function")) active.set(child, { observed: null, observePromise: null, reaped: false, reapPromise: null });
      return child;
    };
    const observeOwned = async (child, milliseconds, label) => {
      const state = active.get(child);
      if (!state) throw new Error("untracked-native-child");
      state.observePromise ||= child.observeLeader();
      state.observed = await deadline(state.observePromise, milliseconds, label);
      return state.observed;
    };
    const reapOwned = async (child, milliseconds, label) => {
      const state = active.get(child);
      if (!state || !state.observed) throw new Error("leader-not-observed");
      state.reapPromise ||= child.reapLeader();
      const result = await deadline(state.reapPromise, milliseconds, label);
      state.reaped = true;
      return result;
    };
    const confirmRetired = async (child, label) => {
      for (let attempt = 0; attempt < 40; attempt++) {
        if (child.groupRetired()) return;
        await new Promise((resolve) => setTimeout(resolve, 25));
      }
      throw new Error(`group-not-retired:${label}`);
    };
    const finishOwned = async (child, milliseconds, label) => {
      const observed = await observeOwned(child, milliseconds, `${label}-observe`);
      const reaped = await reapOwned(child, milliseconds, `${label}-reap`);
      if (JSON.stringify(observed) !== JSON.stringify(reaped)) throw new Error(`leader-result-changed:${label}`);
      await confirmRetired(child, label);
      return reaped;
    };
    const cleanup = async () => {
      const failures = [];
      for (const [child, state] of active) {
        if (!state.reaped) {
          try { child.closeInput(); } catch {}
          const observing = observeOwned(child, 3000, "failure-observe");
          try { child.terminate(); } catch {}
          try { child.kill(); } catch {}
          try {
            await observing;
            await reapOwned(child, 3000, "failure-reap");
            await confirmRetired(child, "failure-cleanup");
          }
          catch (error) { failures.push(error instanceof Error ? error.message : "unknown-cleanup-failure"); }
        }
        active.delete(child);
      }
      for (const lease of activeLeases) {
        try { if (lease.held) lease.close(); } catch {}
        activeLeases.delete(lease);
      }
      if (failures.length) throw new Error(`native-child-cleanup:${failures.join(",")}`);
    };
    const record = resultRecorder(cleanup);

    await record.run("lock-owner-mode-inode-and-contention", async () => {
      const lockRoot = path.join(runRoot, "lock-valid"); fs.mkdirSync(lockRoot, { mode: 0o700 });
      const first = acquire(lockRoot);
      const lockPath = path.join(lockRoot, "runtime-admission-authority.lock");
      const stat = fs.lstatSync(lockPath);
      if (!first.held || typeof first.device !== "bigint" || typeof first.inode !== "bigint" || stat.uid !== process.geteuid() || (stat.mode & 0o777) !== 0o600 || stat.nlink !== 1 || BigInt(stat.dev) !== first.device || BigInt(stat.ino) !== first.inode) throw new Error("lock-invariant-failed");
      expectThrow(() => acquire(lockRoot), "contention");
      first.close();
      const second = acquire(lockRoot);
      second.close();
      return { created: first.created, device: first.device.toString(), inode: first.inode.toString() };
    });

    await record.run("lock-path-failures", async () => {
      const wrong = path.join(runRoot, "lock-wrong-mode"); fs.mkdirSync(wrong, { mode: 0o755 }); fs.chmodSync(wrong, 0o755);
      expectThrow(() => acquire(wrong), "wrong-mode");
      const target = path.join(runRoot, "lock-target"); fs.mkdirSync(target, { mode: 0o700 });
      const symlink = path.join(runRoot, "lock-symlink"); fs.symlinkSync(target, symlink);
      expectThrow(() => acquire(symlink), "symlink-directory");
      const hard = path.join(runRoot, "lock-hardlink"); fs.mkdirSync(hard, { mode: 0o700 });
      const source = path.join(hard, "source"); fs.writeFileSync(source, "x", { mode: 0o600 });
      fs.linkSync(source, path.join(hard, "runtime-admission-authority.lock"));
      expectThrow(() => acquire(hard), "hardlink");
      const fileSymlinkRoot = path.join(runRoot, "lock-file-symlink"); fs.mkdirSync(fileSymlinkRoot, { mode: 0o700 });
      fs.symlinkSync(source, path.join(fileSymlinkRoot, "runtime-admission-authority.lock"));
      expectThrow(() => acquire(fileSymlinkRoot), "symlink-file");
      const fileModeRoot = path.join(runRoot, "lock-file-mode"); fs.mkdirSync(fileModeRoot, { mode: 0o700 });
      fs.writeFileSync(path.join(fileModeRoot, "runtime-admission-authority.lock"), "x", { mode: 0o644 }); fs.chmodSync(path.join(fileModeRoot, "runtime-admission-authority.lock"), 0o644);
      expectThrow(() => acquire(fileModeRoot), "wrong-file-mode");
    });
    record.incomplete("lock-pathname-swap-race", "a deterministic concurrent pathname-swap coordinator is not present in the bounded fixture; native pre/post inode checks are source-inspected only", { qualificationBlocking: false, coverageLimit: true });

    await record.run("strict-spawn-inspection", async () => {
      const lockRoot = path.join(runRoot, "spawn-lock"); fs.mkdirSync(lockRoot, { mode: 0o700 });
      const lease = acquire(lockRoot);
      const sentinelPath = path.join(runRoot, "parent-sentinel"); fs.writeFileSync(sentinelPath, "synthetic", { mode: 0o600 });
      const sentinelFd = fs.openSync(sentinelPath, "r");
      let child, observation, eof, waited;
      try {
        child = spawn(["inspect"]); const reader = createRecordReader(child);
        observation = await reader.next("inspect-record");
        eof = await reader.next("inspect-eof");
        waited = await finishOwned(child, 6000, "inspect");
      } finally { fs.closeSync(sentinelFd); }
      lease.close();
      if (!observation || observation.event !== "inspect" || eof !== null || waited.exitCode !== 0 || waited.signal !== null) throw new Error("inspect-completion");
      if (observation.pid !== child.pid || observation.pgrp !== child.pid || observation.bootstrapLength !== 32 || decodeHex(observation.bootstrapHex) !== SECRET.toString("utf8")) throw new Error("bootstrap-or-group");
      if (decodeHex(observation.cwdHex) !== cwd) throw new Error("cwd-mismatch");
      const observedEnvironment = observation.environmentHex.map(decodeHex).sort();
      if (observation.environmentCount !== 5 || JSON.stringify(observedEnvironment) !== JSON.stringify([...environment].sort())) throw new Error("environment-mismatch");
      if (observation.fdEnumeration !== "PROC_PIDLISTFDS" || JSON.stringify([...observation.openFds].sort((a, b) => a - b)) !== JSON.stringify([0, 1, 2, 3])) throw new Error("descriptor-closure-unqualified");
      return { pid: child.pid, pgrp: observation.pgrp, fdCoverage: observation.fdEnumeration, openFds: observation.openFds, parentSentinelFd: sentinelFd, heldLockExcluded: true };
    });

    await record.run("stdin-stdout-eof-and-exit", async () => {
      const child = spawn(["echo"]); const reader = createRecordReader(child); const payload = Buffer.from("synthetic-echo\n");
      await deadline(child.write(payload), 3000, "echo-write"); child.closeInput();
      const bytes = await deadline(child.read(), 3000, "echo-read");
      const eof = await deadline(child.read(), 3000, "echo-eof");
      const waited = await finishOwned(child, 3000, "echo");
      if (!bytes.equals(payload) || eof.length !== 0 || waited.exitCode !== 0 || waited.signal !== null) throw new Error("echo-mismatch");
      const exiting = spawn(["exit", "23"]); const exitResult = await finishOwned(exiting, 3000, "known-exit");
      if (exitResult.exitCode !== 23 || exitResult.signal !== null) throw new Error("exit-mismatch");
    });

    await record.run("strict-argument-rejection", async () => {
      expectAllThrow([
        ["executable-relative", () => unexpectedRaw("relative", [], SECRET, cwd, environment, true)],
        ["executable-symlink", () => { const alias = path.join(runRoot, "fixture-alias"); fs.symlinkSync(fixtureIdentity.path, alias); return unexpectedRaw(alias, [], SECRET, cwd, environment, true); }],
        ["argc-seven", () => unexpectedRaw(fixtureIdentity.path, ["exit", "0"], SECRET, cwd, environment, true, "extra")],
        ["secret-31", () => spawn(["exit", "0"], Buffer.alloc(31))],
        ["secret-33", () => spawn(["exit", "0"], Buffer.alloc(33))],
        ["argv-control", () => spawn(["bad\narg"])],
        ["cwd-relative", () => spawn(["exit", "0"], SECRET, "relative")],
        ["cwd-missing", () => spawn(["exit", "0"], SECRET, path.join(runRoot, "missing"))],
        ["group-false", () => spawn(["exit", "0"], SECRET, cwd, environment, false)],
        ["env-missing", () => spawn(["exit", "0"], SECRET, cwd, environment.slice(1))],
        ["env-duplicate", () => spawn(["exit", "0"], SECRET, cwd, [environment[0], environment[0], ...environment.slice(2)])],
        ["env-extra", () => spawn(["exit", "0"], SECRET, cwd, [...environment.slice(0, 4), "USER=blocked"])],
        ["env-order", () => spawn(["exit", "0"], SECRET, cwd, [environment[1], environment[0], ...environment.slice(2)])],
        ["env-path-value", () => spawn(["exit", "0"], SECRET, cwd, environment.map((item) => item.startsWith("PATH=") ? "PATH=/untrusted" : item))],
        ["env-lang-value", () => spawn(["exit", "0"], SECRET, cwd, environment.map((item) => item.startsWith("LANG=") ? "LANG=C" : item))],
        ["env-home-symlink", () => { const alias = path.join(runRoot, "home-alias"); fs.symlinkSync(path.join(runRoot, "home"), alias); return spawn(["exit", "0"], SECRET, cwd, environment.map((item) => item.startsWith("HOME=") ? `HOME=${alias}` : item)); }],
      ]);
    });

    await record.run("raw-canonical-cwd-rejection", async () => {
      const alias = path.join(runRoot, "cwd-alias"); fs.symlinkSync(cwd, alias);
      expectThrow(() => spawn(["inspect"], SECRET, alias), "symlink-cwd");
    });

    await record.run("process-group-term", async () => {
      const child = spawn(["hold"]); const reader = createRecordReader(child); const ready = await reader.next("term-ready");
      if (!ready || ready.pgrp !== child.pid) throw new Error("term-group-mismatch");
      child.closeInput(); const observing = observeOwned(child, 3000, "term-observe"); child.terminate();
      await collectToEof(reader, "term-eof"); const waited = await observing; await reapOwned(child, 3000, "term-reap"); await confirmRetired(child, "term");
      if (waited.exitCode !== null || waited.signal !== 15) throw new Error("term-result-mismatch");
    });

    await record.run("process-group-kill-with-descendant", async () => {
      const child = spawn(["descendant"]); const reader = createRecordReader(child);
      const records = [await reader.next("kill-ready-1"), await reader.next("kill-ready-2")];
      if (!records.some((item) => item && item.event === "leader-ready") || !records.some((item) => item && item.event === "descendant-ready")) throw new Error("descendant-not-ready");
      child.closeInput(); const observing = observeOwned(child, 3000, "kill-observe"); child.kill();
      const waited = await observing;
      const remaining = await collectToEof(reader, "kill-eof");
      if (waited.exitCode !== null || waited.signal !== 9 || remaining.length !== 0) throw new Error("kill-group-not-retired");
      await reapOwned(child, 3000, "kill-reap"); await confirmRetired(child, "kill");
      return { leaderPid: child.pid, observedPipeEof: true };
    });

    await record.run("term-resistant-descendant-observation", async () => {
      const child = spawn(["descendant"]); const reader = createRecordReader(child);
      const ready = [await reader.next("survival-ready-1"), await reader.next("survival-ready-2")];
      if (!ready.some((item) => item && item.event === "leader-ready") || !ready.some((item) => item && item.event === "descendant-ready")) throw new Error("descendant-not-ready");
      child.closeInput(); const observing = observeOwned(child, 3000, "survival-observe"); child.terminate();
      const survived = await reader.next("survival-term-record");
      if (!survived || survived.event !== "descendant-term-survived") throw new Error("descendant-survival-not-observed");
      child.kill();
      const later = await collectToEof(reader, "survival-kill-eof");
      const waited = await observing;
      if (waited.exitCode !== null || waited.signal !== 15 || later.length !== 0) throw new Error("descendant-retirement-not-observed");
      await reapOwned(child, 3000, "survival-reap"); await confirmRetired(child, "survival");
      return { leaderPid: child.pid, descendantSurvivedTerm: true, killedBeforeLeaderReap: true, observedPipeEof: true };
    });

    output.cases = record.cases;
    output.result = output.cases.some((item) => item.result === "FAIL") ? "FAIL" : output.cases.some((item) => item.result === "NOT_RUN" && item.qualificationBlocking) ? "INCOMPLETE" : "PASS";
  } catch (error) {
    output.reason = error instanceof Error ? error.message : "unknown-failure";
  }
  if (createdRunRoot && output.runRoot) {
    try { fs.writeFileSync(path.join(output.runRoot, "native-behavior-result.json"), `${JSON.stringify(output, null, 2)}\n`, { flag: "wx", mode: 0o600 }); }
    catch (error) { output.result = "FAIL"; output.reason = `evidence-write:${error instanceof Error ? error.message : "unknown"}`; }
  }
  process.stdout.write(`${JSON.stringify(output)}\n`);
  return output.result === "PASS" ? 0 : 1;
}

module.exports = { collectToEof, createRecordReader, deadline, decodeHex, makeEnvironment, prepareRunRoot, resultRecorder };

if (require.main === module) void main().then((code) => { process.exitCode = code; }, (error) => {
  process.stdout.write(`${JSON.stringify({ schemaVersion: "chirality.native-behavior-probe/v1", result: "FAIL", reason: error instanceof Error ? error.message : "unknown-failure" })}\n`);
  process.exitCode = 1;
});
