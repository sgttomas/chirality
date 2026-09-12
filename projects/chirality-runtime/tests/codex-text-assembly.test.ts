import { describe, expect, it } from "vitest";
import { CodexTextAssembly } from "../packages/daemon/src/codex-text-assembly.js";
import { deriveTranscriptView } from "../packages/contracts/src/harness/transcript-replay.js";

describe("native item text projection", () => {
  it("preserves split words and orders interleaved messages with a single paragraph boundary", () => {
    const assembly = new CodexTextAssembly();
    const items = new Map([["a", { text: "Hel", completed: false }], ["b", { text: "Final", completed: true }]]);
    const deltas = [assembly.flush(items)];
    items.get("a")!.text += "lo"; deltas.push(assembly.flush(items));
    items.get("a")!.completed = true; deltas.push(assembly.flush(items));
    deltas.push(assembly.flush(items, true));
    expect(deltas).toEqual(["Hel", "lo", "\n\nFinal", ""]);
    expect(assembly.text).toBe(deltas.join(""));
  });
  it("flushes interrupted partial and completed-only items while ignoring empty items", () => {
    const assembly = new CodexTextAssembly();
    const items = new Map([["empty", { text: "", completed: true }], ["a", { text: "Partial", completed: false }], ["b", { text: "Done", completed: true }]]);
    expect(assembly.flush(items)).toBe("Partial");
    expect(assembly.flush(items, true)).toBe("\n\nDone");
    expect(assembly.flush(items, true)).toBe("");
  });
  it("omits marked bootstrap input while retaining a literal operator bootstrap message", () => {
    const events = [true, false].map((boot, i) => ({ schemaVersion: 1, eventId: `event-${i}`, sessionId: "s", turnId: `turn-${i}`, timestamp: "2026-09-11T00:00:00Z", type: "turn.accepted", data: { message: "bootstrap", ...(boot ? { boot: true } : {}) } }));
    const view = deriveTranscriptView([...events, { ...events[0], eventId: "assistant-boot", type: "assistant.delta", data: { text: "hidden boot output" } }] as any);
    expect(view.items.some(item => item.text === "hidden boot output")).toBe(false);
    expect(view.items.filter(item => item.role === "user").map(item => item.turnId)).toEqual(["turn-1"]);
  });
});
