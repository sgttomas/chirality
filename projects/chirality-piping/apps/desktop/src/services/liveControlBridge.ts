import { invoke } from "@tauri-apps/api/core";
import { isTauriRuntime } from "./nativeMenu";
import type { LiveControlController } from "../features/workspace/liveControlController";
import type { LiveRequest } from "../features/workspace/liveControlTypes";
type Registration = { enabled: boolean; app_instance_id: string | null; registration_id: string | null; controller_session_id: string };
type Cancellation = Pick<LiveRequest, "registration_id" | "controller_session_id" | "dispatch_id" | "request_id"> & { reason: string };
// Serialize asynchronous unregister/register across StrictMode effect replacement.
let lifecycle: Promise<void> = Promise.resolve();
export function startLiveControlBridge(controller: LiveControlController): () => void {
  if (!isTauriRuntime()) return () => {};
  let disposed = false;
  let registration: Registration | null = null;
  let unlisteners: (() => void)[] = [];
  const early: ({ kind: "request"; payload: LiveRequest } | { kind: "cancel"; payload: Cancellation })[] = [];
  const pending = new Map<string, { requestId: string; abort: AbortController }>();
  const matches = (event: Pick<LiveRequest, "registration_id" | "controller_session_id">) => !disposed && registration?.enabled && event.registration_id === registration.registration_id && event.controller_session_id === controller.sessionId;
  const dispatch = (payload: LiveRequest) => {
    if (!matches(payload) || payload.app_instance_id !== registration?.app_instance_id || pending.has(payload.dispatch_id)) return;
    const abort = new AbortController();
    pending.set(payload.dispatch_id, { requestId: payload.request_id, abort });
    void controller.request(payload, abort.signal).then(async response => {
      if (!matches(payload)) return;
      await invoke("live_control_reply", { registrationId: payload.registration_id, dispatchId: payload.dispatch_id, response });
    }).catch(() => { /* Native expiry owns failed delivery; history stays in controller. */ }).finally(() => pending.delete(payload.dispatch_id));
  };
  const cancel = (payload: Cancellation) => {
    if (!matches(payload)) return;
    const entry = pending.get(payload.dispatch_id);
    if (entry?.requestId === payload.request_id) entry.abort.abort();
  };
  const setup = lifecycle.then(async () => {
    if (disposed) return;
    const { listen } = await import("@tauri-apps/api/event");
    if (disposed) return;
    unlisteners.push(await listen<LiveRequest>("piping-live-control-request", ({ payload }) => {
      if (!registration && !disposed && payload.controller_session_id === controller.sessionId) {
        if (early.length < 32) early.push({ kind: "request", payload });
      } else dispatch(payload);
    }));
    unlisteners.push(await listen<Cancellation>("piping-live-control-cancel", ({ payload }) => {
      if (!registration && !disposed && payload.controller_session_id === controller.sessionId) {
        if (early.length < 32) early.push({ kind: "cancel", payload });
      } else cancel(payload);
    }));
    if (disposed) return;
    registration = await invoke<Registration>("live_control_register", { controllerSessionId: controller.sessionId });
    if (!disposed && registration.enabled && registration.app_instance_id) {
      controller.bind(registration.app_instance_id);
      for (const event of early) event.kind === "request" ? dispatch(event.payload) : cancel(event.payload);
    }
    early.length = 0;
  });
  lifecycle = setup.catch(() => {
    early.length = 0;
    for (const unlisten of unlisteners) unlisten();
    unlisteners = [];
  });
  return () => {
    disposed = true;
    controller.retire();
    for (const entry of pending.values()) entry.abort.abort();
    lifecycle = setup.catch(() => {}).then(async () => {
      for (const unlisten of unlisteners) unlisten();
      unlisteners = [];
      if (registration?.enabled && registration.registration_id) await invoke("live_control_unregister", { registrationId: registration.registration_id });
    }).catch(() => {});
  };
}
