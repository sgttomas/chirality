import { waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
const mocks = vi.hoisted(() => ({ invoke: vi.fn(), listeners: new Map<string, (event: { payload: any }) => void>(), unlisten: vi.fn(), targets: new Map<string, unknown>(), failListen: false }));
vi.mock("@tauri-apps/api/core", () => ({ invoke: mocks.invoke }));
vi.mock("@tauri-apps/api/event", () => ({ listen: vi.fn(async (name: string, handler: (event: { payload: any }) => void, options: unknown) => {
  mocks.targets.set(name, options);
  if (mocks.failListen && name.endsWith("cancel")) throw new Error("listener failed");
  mocks.listeners.set(name, handler); return () => { mocks.unlisten(name); if (mocks.listeners.get(name) === handler) mocks.listeners.delete(name); };
}) }));
import { startLiveControlBridge } from "./liveControlBridge";
import type { LiveControlController } from "../features/workspace/liveControlController";
import type { LiveRequest } from "../features/workspace/liveControlTypes";
const disposers = new Set<() => void>();
const unblockers = new Set<() => Promise<void>>();
function start(controller: ReturnType<typeof fake>) {
  const raw = startLiveControlBridge(controller as unknown as LiveControlController);
  let disposed = false;
  const dispose = () => { if (!disposed) { disposed = true; raw(); } };
  disposers.add(dispose);
  return dispose;
}
function fake() { return { sessionId: "controller-test", bind: vi.fn(), retire: vi.fn(), request: vi.fn(async (_request?: unknown, _signal?: AbortSignal) => ({ result: "observed" })) }; }
const request: LiveRequest = { registration_id: "registration-test", controller_session_id: "controller-test", dispatch_id: "dispatch-test", request_id: "request-test", app_instance_id: "app-test", method: "inspect", params: { scope: "workspace" } };
const registration = { enabled: true, registration_id: "registration-test", controller_session_id: "controller-test", app_instance_id: "app-test" };
afterEach(async () => {
  try {
    // Resolve deliberately held registrations even when a preceding assertion
    // failed, then dispose every bridge and observe its actual listener cleanup.
    try {
      for (const unblock of unblockers) await unblock();
    } finally {
      for (const dispose of disposers) dispose();
      await waitFor(() => expect(mocks.listeners.size).toBe(0));
    }
  } finally {
    disposers.clear(); unblockers.clear(); mocks.invoke.mockReset();
    mocks.unlisten.mockReset(); mocks.targets.clear(); mocks.listeners.clear(); mocks.failListen = false;
    delete (window as unknown as Record<string, unknown>).__TAURI_INTERNALS__;
  }
});
describe("native live bridge lifecycle", () => {
  it("is inert in a browser", async () => {
    const dispose = start(fake()); dispose(); expect(mocks.invoke).not.toHaveBeenCalled();
  });
  it("buffers a request before registration promise completion and installs both listeners first", async () => {
    (window as unknown as Record<string, unknown>).__TAURI_INTERNALS__ = {};
    let release!: (r: typeof registration) => void;
    mocks.invoke.mockImplementation((command: string) => {
      if (command === "live_control_register") {
        expect(mocks.listeners.size).toBe(2);
        expect([...mocks.targets.entries()]).toEqual([
          ["piping-live-control-request", { target: { kind: "WebviewWindow", label: "main" } }],
          ["piping-live-control-cancel", { target: { kind: "WebviewWindow", label: "main" } }]
        ]);
        mocks.listeners.get("piping-live-control-request")!({ payload: request });
        return new Promise(resolve => { release = resolve; });
      }
      return Promise.resolve();
    });
    unblockers.add(async () => { await waitFor(() => expect(release).toBeTypeOf("function")); release(registration); });
    const controller = fake(), dispose = start(controller);
    await waitFor(() => expect(release).toBeTypeOf("function"));
    expect(controller.request).not.toHaveBeenCalled();
    release(registration);
    await waitFor(() => expect(controller.request).toHaveBeenCalledTimes(1));
    expect(controller.bind).toHaveBeenCalledWith("app-test");
    expect(controller.request).toHaveBeenCalledTimes(1);
    await waitFor(() => expect(mocks.invoke).toHaveBeenCalledWith("live_control_reply", { registrationId: "registration-test", dispatchId: "dispatch-test", response: { result: "observed" } }));
    dispose(); await waitFor(() => expect(mocks.unlisten).toHaveBeenCalledTimes(2));
  });
  it("keeps disabled registration inert and cleans listeners on a partial setup failure", async () => {
    (window as unknown as Record<string, unknown>).__TAURI_INTERNALS__ = {};
    mocks.invoke.mockResolvedValue({ ...registration, enabled: false, app_instance_id: null, registration_id: null });
    const controller = fake(), dispose = start(controller);
    await waitFor(() => expect(mocks.invoke).toHaveBeenCalledWith("live_control_register", { controllerSessionId: "controller-test" }));
    mocks.listeners.get("piping-live-control-request")!({ payload: request });
    expect(controller.request).not.toHaveBeenCalled(); expect(controller.bind).not.toHaveBeenCalled();
    dispose(); await waitFor(() => expect(mocks.listeners.size).toBe(0));
    mocks.unlisten.mockClear(); mocks.failListen = true;
    const disposeFailed = start(fake());
    await waitFor(() => expect(mocks.unlisten).toHaveBeenCalledTimes(1)); disposeFailed();
  });
  it("serializes StrictMode retirement and binds cancellation to dispatch and request identity", async () => {
    (window as unknown as Record<string, unknown>).__TAURI_INTERNALS__ = {};
    mocks.invoke.mockResolvedValue(registration);
    const old = fake(), oldDispose = start(old);
    await waitFor(() => expect(old.bind).toHaveBeenCalledWith("app-test")); oldDispose();
    const controller = fake(); let signal: AbortSignal | undefined;
    controller.request.mockImplementation((_request?: unknown, suppliedSignal?: AbortSignal) => { signal = suppliedSignal; return new Promise(() => {}); });
    const dispose = start(controller);
    await waitFor(() => expect(controller.bind).toHaveBeenCalledWith("app-test"));
    const commands = mocks.invoke.mock.calls.map(([command]) => command);
    expect(commands).toEqual(["live_control_register", "live_control_unregister", "live_control_register"]);
    mocks.listeners.get("piping-live-control-request")!({ payload: request });
    mocks.listeners.get("piping-live-control-cancel")!({ payload: { ...request, request_id: "wrong", reason: "disconnect" } });
    expect(signal?.aborted).toBe(false);
    mocks.listeners.get("piping-live-control-cancel")!({ payload: { ...request, reason: "disconnect" } });
    expect(signal?.aborted).toBe(true); dispose();
    await waitFor(() => expect(mocks.listeners.size).toBe(0));
  });
});
