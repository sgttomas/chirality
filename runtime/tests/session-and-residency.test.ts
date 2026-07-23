import { mkdtemp, readFile, writeFile, mkdir, realpath } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import type { OmlxControlPort, OmlxModelStatus } from "@chirality/runtime-contracts";
import { ProjectRegistry, ResidencyCoordinator, SessionStore } from "@chirality/runtime-core";
import { createProjectFixture } from "./helpers.js";

class FakeOmlx implements OmlxControlPort {
  models: OmlxModelStatus[] = [
    { id: "model-a", kind: "llm", loaded: true, loading: false },
    { id: "model-b", kind: "llm", loaded: false, loading: false },
    { id: "embed", kind: "embedding", loaded: true, loading: false }
  ];
  failLoad = false;
  unloads: string[] = [];

  async listStatus() {
    return this.models;
  }
  async load(modelId: string) {
    if (this.failLoad) throw new Error("memory");
    this.models = this.models.map((model) =>
      model.id === modelId ? { ...model, loaded: true } : model
    );
  }
  async unload(modelId: string) {
    this.unloads.push(modelId);
    this.models = this.models.map((model) =>
      model.id === modelId ? { ...model, loaded: false } : model
    );
  }
}

describe("central sessions", () => {
  it("lazily copies a legacy record without modifying the source", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-session-"));
    const { manifestPath } = await createProjectFixture(root);
    const legacyId = "legacy-one";
    await mkdir(join(root, "legacy-sessions", legacyId));
    const legacyPath = join(root, "legacy-sessions", legacyId, "session.json");
    const legacySource = JSON.stringify({
      sessionId: legacyId,
      projectRoot: root,
      persona: "HELP_HUMAN",
      mode: "direct",
      model: "claude",
      createdAt: "2026-01-01T00:00:00.000Z",
      updatedAt: "2026-01-01T00:00:00.000Z"
    });
    await writeFile(legacyPath, legacySource, "utf8");
    const runtime = join(root, "user-data", "runtime");
    const projects = new ProjectRegistry(runtime);
    await projects.register(manifestPath, {
      approvedBy: "test",
      approvalReference: "D-TEST"
    });
    const sessions = new SessionStore(runtime, projects);
    const migrated = await sessions.get("fixture", legacyId);
    expect(migrated.legacy?.sourcePath).toBe(await realpath(legacyPath));
    expect(await readFile(legacyPath, "utf8")).toBe(legacySource);
    expect(migrated.persona).toBe("HELP_HUMAN");
  });
});

describe("model residency", () => {
  it("drains without force and enters NO_MODEL after a post-unload load failure", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-residency-"));
    const control = new FakeOmlx();
    const coordinator = new ResidencyCoordinator(control, root, {
      drainTimeoutMs: 15,
      totalTimeoutMs: 1_000,
      pollIntervalMs: 2
    });
    const ready = await coordinator.activate("model-a", "D-TEST");
    expect(ready.managedModelId).toBe("model-a");
    const release = await coordinator.admitTurn("model-a");
    await expect(coordinator.activate("model-b", "D-TEST")).rejects.toMatchObject({
      code: "RESIDENCY_DRAIN_TIMEOUT"
    });
    expect((await coordinator.status()).managedModelId).toBe("model-a");
    release();
    control.failLoad = true;
    await expect(coordinator.activate("model-b", "D-TEST")).rejects.toBeDefined();
    const failed = await coordinator.status();
    expect(failed.phase).toBe("NO_MODEL");
    expect(failed.managedModelId).toBeUndefined();
    expect(control.unloads).toEqual(["model-a"]);
    expect(control.models.find((model) => model.id === "embed")?.loaded).toBe(true);
  });
});
