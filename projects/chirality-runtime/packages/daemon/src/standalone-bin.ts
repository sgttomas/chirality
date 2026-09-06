#!/usr/bin/env node
import { retireRuntimeConformanceGeneration } from "@chirality/runtime-core";
import { RuntimeError } from "@chirality/runtime-contracts";
import { startStandaloneJob, type StandaloneJob } from "./standalone.js";

process.umask(0o077);
let job: StandaloneJob | undefined;
let stopping = false;
let finish!: () => void;
const stopped = new Promise<void>(resolve => { finish = resolve; });
async function stop(): Promise<void> {
  if (stopping) return;
  stopping = true;
  try { await job?.close(); } catch { process.stderr.write("Standalone shutdown failed\n"); process.exitCode = 1; }
  finally { finish(); }
}
const signal = () => { void stop(); };
process.on("SIGTERM", signal);
process.on("SIGINT", signal);
try {
  const [role, flag, configPath, ...extra] = process.argv.slice(2);
  if ((role !== "daemon" && role !== "supervisor") || flag !== "--config" || !configPath || extra.length !== 0) throw new RuntimeError("INVALID_REQUEST", "Usage: chirality-runtime-service daemon|supervisor --config <absolute-private-json>");
  job = await startStandaloneJob(role, configPath);
  if (stopping) await job.close();
  else {
    process.stdout.write(`${JSON.stringify({ ready: true, role: job.role, socketPath: job.socketPath, mode: job.mode })}\n`);
    await stopped;
  }
} catch (error) {
  process.stderr.write(`${error instanceof RuntimeError ? `${error.code}: ${error.message}` : `Standalone startup failed (${typeof (error as NodeJS.ErrnoException)?.code === "string" ? (error as NodeJS.ErrnoException).code : "unknown"})`}\n`);
  process.exitCode = 1;
} finally {
  await retireRuntimeConformanceGeneration();
  process.off("SIGTERM", signal); process.off("SIGINT", signal);
}
