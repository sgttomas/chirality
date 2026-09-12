/**
 * Guard for the daemon's spawn-a-GUI-on-`activate` behaviour.
 *
 * macOS delivers `activate` to the headless LaunchAgent daemon whenever the
 * bundle is opened, including when a GUI is *already* running (a second Dock
 * click, a Finder double-click on the bundle). Spawning then is harmful twice
 * over: the second GUI exits at once on "Saved renderer port … is already
 * occupied", and the daemon retires itself regardless, leaving the running GUI
 * without a runtime for the reconnect window and discarding in-memory hosted
 * consent. The decision logic lives here, free of `electron` imports, in the
 * same shape as `runtime-autostart.ts`, so the evidence matrix is checkable in
 * a unit test rather than only in a packaged run.
 *
 * Evidence. The daemon has no view of the GUI's account-host lease (that lives
 * inside Runtime's `HostAccountAuthority` and is not exposed on the host
 * handle), and the control socket cannot tell a GUI client from a CLI one. What
 * the daemon *can* observe, sharing the GUI's userData directory, is the
 * renderer port record the packaged GUI persists (`renderer-server-port.ts`)
 * and whether that loopback port currently accepts a connection. A packaged GUI
 * binds exactly that port for its lifetime and nothing else in the app does, so
 * "saved port is listening" is the same fact the doomed second GUI would have
 * discovered the expensive way.
 *
 * Only that positive fact blocks the spawn. Every other state — no record
 * (development, or a GUI that has never run), a record whose port refuses the
 * connection (the GUI is gone), a record that cannot be read or validated, or a
 * probe that does not settle — keeps the pre-existing V-D4 behaviour and spawns,
 * so a genuine launch can never be swallowed by a stale or damaged file. Each
 * outcome carries the evidence so the log states why.
 */

import { connect as connectTcp } from 'node:net';
import { readRendererPortRecord, rendererPortRecordPath } from './renderer-server-port';

/** Upper bound on the loopback probe; a listening socket answers in microseconds. */
export const GUI_LIVENESS_PROBE_TIMEOUT_MS = 500;

export type RendererPortEvidence =
  /** No record: nothing has ever bound a stable renderer port for this userData. */
  | { kind: 'absent' }
  /** The record failed validation; its port is not trusted. */
  | { kind: 'unreadable'; error: string }
  /** A connection to the saved port was accepted. */
  | { kind: 'listening'; port: number }
  /** A connection to the saved port was refused. */
  | { kind: 'closed'; port: number; error: string }
  /** The probe neither connected nor failed within the timeout. */
  | { kind: 'unknown'; port: number };

export type DaemonActivateDecision =
  | { action: 'spawn'; evidence: RendererPortEvidence }
  | { action: 'ignore'; reason: 'gui-running'; port: number };

/**
 * The one rule: a GUI is alive if and only if its saved renderer port is
 * listening. Anything less than that positive evidence spawns.
 */
export function decideDaemonActivate(evidence: RendererPortEvidence): DaemonActivateDecision {
  if (evidence.kind === 'listening') {
    return { action: 'ignore', reason: 'gui-running', port: evidence.port };
  }
  return { action: 'spawn', evidence };
}

export type LoopbackProbeResult = 'listening' | 'closed' | 'unknown';

/**
 * Try one TCP connection to `127.0.0.1:port` and close it immediately. No bytes
 * are sent; the renderer server never sees a request.
 */
export function probeLoopbackPort(
  port: number,
  timeoutMs = GUI_LIVENESS_PROBE_TIMEOUT_MS
): Promise<{ result: LoopbackProbeResult; error?: string }> {
  return new Promise((resolve) => {
    let settled = false;
    const socket = connectTcp({ host: '127.0.0.1', port });
    const finish = (result: LoopbackProbeResult, error?: string): void => {
      if (settled) return;
      settled = true;
      socket.destroy();
      resolve(error === undefined ? { result } : { result, error });
    };
    socket.setTimeout(timeoutMs, () => finish('unknown'));
    socket.once('connect', () => finish('listening'));
    socket.once('error', (error: NodeJS.ErrnoException) =>
      finish('closed', error.code ?? error.message));
  });
}

export type GuiLivenessDependencies = {
  /** `app.getPath('userData')` — the same directory the GUI persists its record in. */
  userDataDirectory: string;
  readRecord?: typeof readRendererPortRecord;
  probe?: typeof probeLoopbackPort;
};

/** Gather the renderer-port evidence; never throws. */
export async function observeRendererPortEvidence(
  deps: GuiLivenessDependencies
): Promise<RendererPortEvidence> {
  const readRecord = deps.readRecord ?? readRendererPortRecord;
  const probe = deps.probe ?? probeLoopbackPort;
  let port: number;
  try {
    const record = await readRecord(rendererPortRecordPath(deps.userDataDirectory));
    if (record === null) return { kind: 'absent' };
    port = record.port;
  } catch (error) {
    return { kind: 'unreadable', error: error instanceof Error ? error.message : String(error) };
  }
  const probed = await probe(port);
  if (probed.result === 'listening') return { kind: 'listening', port };
  if (probed.result === 'closed') return { kind: 'closed', port, error: probed.error ?? 'refused' };
  return { kind: 'unknown', port };
}
