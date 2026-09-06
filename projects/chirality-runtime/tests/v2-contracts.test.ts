import { describe, expect, it } from "vitest";
import { HARNESS_V2_TERMINALS, projectRuntimeEventV2, validateHarnessEventV2 } from "../packages/contracts/src/v2-events.js";
import type { RuntimeEvent } from "../packages/contracts/src/events.js";
const envelope = { schemaVersion: 2, eventId: "e", sequence: 1, timestamp: "2026-09-06T00:00:00.000Z", projectId: "p", sessionId: "s", turnId: "t" };
const runtime = (type: RuntimeEvent["type"], data: unknown): RuntimeEvent => ({ schemaVersion: "chirality.event/v1", id: "e", sequence: 1, timestamp: envelope.timestamp, projectId: "p", sessionId: "s", turnId: "t", type, data });
describe("closed additive v2 wire schema", () => {
  it("accepts exactly four terminal identifiers with discriminated payloads", () => {
    expect(HARNESS_V2_TERMINALS).toEqual(["turn.completed", "turn.failed", "turn.interrupted", "turn.cancelled"]);
    for (const type of HARNESS_V2_TERMINALS) {
      const data = type === "turn.failed" ? { code: "FAILED", message: "failure" } : { outcome: type.slice(5) };
      expect(validateHarnessEventV2({ ...envelope, type, data })).toBe(true);
      expect(validateHarnessEventV2({ ...envelope, type, data: { outcome: "arbitrary" } })).toBe(false);
    }
    for (const type of ["turn.finished", "turn.success", "vendor.notification", "toString", "constructor"]) expect(validateHarnessEventV2({ ...envelope, type, data: {} })).toBe(false);
  });
  it.each([
    ["session.created", { role: "task" }], ["session.resumed", { resumed: true }],
    ["turn.accepted", { message: "hello" }], ["turn.started", { started: true }],
    ["message.started", { messageId: "m" }], ["message.delta", { text: "hello" }], ["message.completed", { messageId: "m" }],
    ["model.request.started", { requestId: "r", model: "actual-model" }], ["model.delta", { requestId: "r", text: "token" }], ["model.completed", { requestId: "r" }],
    ["approval.requested", { approvalId: "a", actorId: "actor", host: "example.invalid", protocol: "https", groupingCaveat: "May unblock queued requests to the same destination" }],
    ["approval.decided", { approvalId: "a", actorId: "owner", decision: "acceptForSession", explicitUserAct: true }]
  ])("validates minimal %s and rejects arbitrary extension", (type, data) => {
    expect(validateHarnessEventV2({ ...envelope, type, data })).toBe(true);
    expect(validateHarnessEventV2({ ...envelope, type, data: { ...data, vendorSecret: "secret" } })).toBe(false);
    expect(validateHarnessEventV2({ ...envelope, type, data: {} })).toBe(false);
  });
  it("rejects missing attribution, implicit session approval and schema drift", () => {
    const approval = { ...envelope, type: "approval.decided", data: { approvalId: "a", actorId: "", decision: "acceptForSession", explicitUserAct: true } };
    expect(validateHarnessEventV2(approval)).toBe(false);
    expect(validateHarnessEventV2({ ...approval, data: { ...approval.data, actorId: "a", explicitUserAct: false } })).toBe(false);
    const valid = { ...envelope, type: "message.delta", data: { text: "hi" } };
    for (const mutation of [{ schemaVersion: 1 }, { sequence: -1 }, { timestamp: "yesterday" }, { turnId: "" }, { vendor: {} }, { attribution: { model: "m" } }]) expect(validateHarnessEventV2({ ...valid, ...mutation })).toBe(false);
  });
  it("projects all four runtime terminal identities explicitly", () => {
    for (const type of HARNESS_V2_TERMINALS) {
      const source = { ...runtime("turn.completed", type === "turn.failed" ? { code: "FAILED", message: "failure" } : {}), type };
      expect(projectRuntimeEventV2(source)).toMatchObject({ kind: "event", event: { type } });
    }
  });
  it("projects only safe fields and quarantines unknown notifications without echo", () => {
    const projected = projectRuntimeEventV2(runtime("message.delta", { text: "safe", credential: "secret" }));
    expect(projected).toMatchObject({ kind: "event", event: { schemaVersion: 2, data: { text: "safe" } } });
    expect(JSON.stringify(projected)).not.toContain("secret");
    expect(projectRuntimeEventV2(runtime("compaction", { credential: "secret" }))).toEqual({ kind: "quarantined", reason: "unsupported_event" });
    expect(projectRuntimeEventV2(runtime("message.delta", { delta: "vendor-shaped" }))).toEqual({ kind: "quarantined", reason: "invalid_payload" });
    expect(projectRuntimeEventV2({ ...runtime("turn.completed", {}), schemaVersion: "vendor/v1" } as unknown as RuntimeEvent)).toEqual({ kind: "quarantined", reason: "invalid_envelope" });
  });
});
