import type { ChildProcess } from "node:child_process";
import { RuntimeError } from "@chirality/runtime-contracts";
import type { CodexSessionTransport } from "./codex-session.js";

export const CODEX_TRANSPORT_CLOSE_BOUNDS_MS = Object.freeze({ eof: 1000, term: 500, finalClose: 2000 });
/** Transport closure is cleanup evidence only; it never proves authority fencing. */
export const CODEX_TRANSPORT_AUTHORITY_EVIDENCE = "NONE" as const;
export interface CodexTransportLifecycleEvent {
  phase: "close-requested" | "stdin-eof" | "stdin-eof-finished" | "stdin-error" | "eof-grace-expired" | "term-grace-expired" | "signal" | "signal-error" | "exit" | "close" | "spawn-error" | "process-error" | "stderr-overflow" | "close-deadline" | "pipes-disposed";
  at: number;
  signal?: NodeJS.Signals;
  code?: string;
  deadlineAt?: number;
}

/** Owns only the supplied detached ChildProcess and its original group, never census PIDs. */
export function createCodexTransportLifecycle(child: ChildProcess, options: {
  observe?: (event: CodexTransportLifecycleEvent) => void;
} = {}): CodexSessionTransport {
  const { stdin, stdout, stderr } = child;
  if (!stdin || !stdout || !stderr) throw new RuntimeError("ENGINE_UNAVAILABLE", "Codex transport requires owned pipes", 503);
  const originalPid = child.pid;
  let exited = child.exitCode !== null || child.signalCode !== null;
  let didClose = false, spawnFailed = false, stderrBytes = 0, stderrOverflow = false;
  let closing: Promise<void> | undefined;
  let inputFailure: unknown;
  let closedAt: number | undefined;
  const emit = (event: Omit<CodexTransportLifecycleEvent, "at">) => {
    // Diagnostics must not break cleanup or acquire signal authority.
    try { options.observe?.({ ...event, at: Date.now() }); } catch {}
  };
  const code = (error: unknown) => {
    const value = (error as NodeJS.ErrnoException)?.code;
    return typeof value === "string" && /^[A-Z0-9_]{1,64}$/.test(value) ? value : "UNCLASSIFIED";
  };
  let resolveClosed!: () => void;
  const closed = new Promise<void>(resolve => { resolveClosed = resolve; });
  child.once("exit", () => { exited = true; emit({ phase: "exit" }); });
  child.once("close", () => { closedAt = performance.now(); didClose = true; exited = true; emit({ phase: "close" }); resolveClosed(); });
  child.on("error", error => { if (originalPid === undefined) spawnFailed = true; emit({ phase: spawnFailed ? "spawn-error" : "process-error", code: code(error) }); });
  const inputError = (error: unknown) => {
    emit({ phase: "stdin-error", code: code(error) });
    // A failure while the owner is alive cannot become success merely because
    // fallback later closes it. EPIPE after known exit is a different race.
    if (!exited && !didClose && !spawnFailed && child.exitCode === null && child.signalCode === null) inputFailure ??= error;
  };
  stdin.on("error", inputError);
  stdin.once("finish", () => emit({ phase: "stdin-eof-finished" }));
  const signal = (value: NodeJS.Signals) => {
    if (!originalPid || exited || didClose || spawnFailed || child.exitCode !== null || child.signalCode !== null) return;
    emit({ phase: "signal", signal: value });
    try { process.kill(-originalPid, value); }
    catch (error) { emit({ phase: "signal-error", signal: value, code: code(error) }); if (code(error) !== "ESRCH") throw error; }
  };
  stderr.on("data", (bytes: Buffer | string) => {
    stderrBytes += Buffer.byteLength(bytes);
    if (stderrBytes > 65536 && !stderrOverflow) {
      stderrOverflow = true;
      emit({ phase: "stderr-overflow" });
      try { signal("SIGKILL"); } catch { /* close/reconciliation still has to establish cleanup. */ }
    }
  });
  const waitClosed = async (deadlineAt: number) => {
    if (didClose) return closedAt! <= deadlineAt;
    const ms = Math.max(0, deadlineAt - performance.now());
    if (ms === 0) return false;
    let timer: ReturnType<typeof setTimeout> | undefined;
    try { return await Promise.race([closed.then(() => closedAt! <= deadlineAt), new Promise<false>(resolve => { timer = setTimeout(() => resolve(false), ms); })]); }
    finally { clearTimeout(timer); }
  };
  const close = () => {
    if (closing) return closing;
    const requestedAt = performance.now();
    const requestedWallAt = Date.now();
    const eofDeadline = requestedAt + CODEX_TRANSPORT_CLOSE_BOUNDS_MS.eof;
    const termDeadline = eofDeadline + CODEX_TRANSPORT_CLOSE_BOUNDS_MS.term;
    const closeDeadline = termDeadline + CODEX_TRANSPORT_CLOSE_BOUNDS_MS.finalClose;
    closing = Promise.resolve().then(async () => {
      emit({ phase: "close-requested", deadlineAt: requestedWallAt + closeDeadline - requestedAt });
      // Drain without detaching the session parser; a child may flush its shutdown response.
      stdout.resume();
      if (!didClose && !exited && !spawnFailed) {
        emit({ phase: "stdin-eof" });
        try {
          if (stdin.destroyed) inputError(new RuntimeError("ENGINE_UNAVAILABLE", "Codex stdin unavailable before shutdown", 503, { reason: "CODEX_TRANSPORT_STDIN_UNAVAILABLE" }));
          else if (!stdin.writableEnded) stdin.end();
        }
        catch (error) { inputError(error); }
      }
      if (await waitClosed(eofDeadline)) { if (inputFailure) throw inputFailure; return; }
      emit({ phase: "eof-grace-expired" });
      let signalFailure: unknown;
      try { signal("SIGTERM"); } catch (error) { signalFailure = error; }
      if (await waitClosed(termDeadline)) {
        if (inputFailure) throw inputFailure;
        if (signalFailure) throw signalFailure;
        return;
      }
      emit({ phase: "term-grace-expired" });
      try { signal("SIGKILL"); } catch (error) { signalFailure ??= error; }
      if (!(await waitClosed(closeDeadline))) {
        emit({ phase: "close-deadline" });
        // Dispose our pipe handles even if an inherited remote end never closes.
        // This never grants signal authority over that process or resolves retirement.
        stdin.destroy(); stdout.destroy(); stderr.destroy(); emit({ phase: "pipes-disposed" });
        const failure = new RuntimeError("ENGINE_UNAVAILABLE", "Codex transport close deadline exceeded", 503, {
          reason: "CODEX_TRANSPORT_CLOSE_TIMEOUT", inputFailure: inputFailure ? code(inputFailure) : undefined,
          signalFailure: signalFailure ? code(signalFailure) : undefined
        });
        failure.cause = inputFailure ?? signalFailure;
        throw failure;
      }
      if (inputFailure) throw inputFailure;
      if (signalFailure) throw signalFailure;
    });
    return closing;
  };
  return { stdin, stdout, close };
}

/** A deadline bounds cleanup only. Completion requires the exact child's wait result. */
export async function retireNativeSupplier(child:{closeInput():void;terminate():void;kill():void;wait():Promise<unknown>},deadline:(phase:"eof"|"term"|"kill")=>Promise<void>=()=>new Promise(resolve=>setTimeout(resolve,1000))):Promise<void>{
  const waited=child.wait().then(()=>true);void waited.catch(()=>{});child.closeInput();
  if(await Promise.race([waited,deadline("eof").then(()=>false)]))return;
  child.terminate();if(await Promise.race([waited,deadline("term").then(()=>false)]))return;
  child.kill();if(await Promise.race([waited,deadline("kill").then(()=>false)]))return;
  throw new Error("Supplier retirement remains unverified");
}
