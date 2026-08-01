import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import {
  HARNESS_EVENT_TYPES,
  HarnessError,
  PUBLIC_UI_EVENT_NAMES,
  RUNTIME_ROUTES
} from "@chirality/runtime-contracts";
import { HarnessError as SubpathHarnessError } from "@chirality/runtime-contracts/errors";
import { ProjectRegistry, SessionStore } from "@chirality/runtime-core";
import { createProjectFixture } from "./helpers.js";

describe("standalone promoted contracts", () => {
  it("preserves existing values and identities while adding daemon routes", () => {
    expect(HarnessError).toBe(SubpathHarnessError);
    expect(HARNESS_EVENT_TYPES).toContain("turn.interrupted");
    expect(PUBLIC_UI_EVENT_NAMES).toEqual(
      expect.arrayContaining(["session:init", "harness:event", "process:exit"])
    );
    expect(RUNTIME_ROUTES.sessionTurn("p", "s")).toBe("/v1/projects/p/sessions/s/turn");
  });
});

describe("project registry", () => {
  it("allows profile references under a distinct declared instruction root and detects drift", async () => {
    const repository = await mkdtemp(join(tmpdir(), "chirality-project-"));
    const project = join(repository, "projects", "pec");
    const profile = join(repository, "_DomainEngines", "profiles");
    const { mkdir } = await import("node:fs/promises");
    await mkdir(project, { recursive: true });
    await mkdir(profile, { recursive: true });
    await mkdir(join(project, "execution"));
    await writeFile(join(profile, "pec.yaml"), "id: pec\n", "utf8");
    const manifestPath = join(project, "chirality.project.json");
    await writeFile(
      manifestPath,
      JSON.stringify({
        schemaVersion: "chirality.project/v1",
        projectId: "pec",
        displayName: "PEC",
        workingRoot: ".",
        instructionRoot: "../..",
        defaultExecutionRoot: "execution",
        profiles: {
          domain: ["../../_DomainEngines/profiles/pec.yaml"],
          capability: [],
          dataBoundary: []
        },
        enabledAdapterIds: ["pi"],
        embeddedUi: { declared: false },
        legacySessionRoots: []
      }),
      "utf8"
    );
    const registry = new ProjectRegistry(join(repository, "user-data", "runtime"));
    await registry.register(manifestPath, {
      approvedBy: "test",
      approvalReference: "D-TEST"
    });
    expect((await registry.status("pec")).manifestDrift).toBe(false);
    await writeFile(manifestPath, `${await readFile(manifestPath, "utf8")}\n`, "utf8");
    expect((await registry.status("pec")).manifestDrift).toBe(true);
    await expect(registry.requireAuthorized("pec")).rejects.toMatchObject({
      code: "PROJECT_MANIFEST_DRIFT"
    });
  });

  it("registers a manifest whose referenced paths all exist", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-existing-"));
    const { manifestPath } = await createProjectFixture(root, "existing");
    const registry = new ProjectRegistry(join(root, "user-data", "runtime"));
    const record = await registry.register(manifestPath, {
      approvedBy: "test",
      approvalReference: "D-TEST"
    });
    expect(record.projectId).toBe("existing");
    expect((await registry.status("existing")).manifestDrift).toBe(false);
  });

  it("rejects a missing defaultExecutionRoot with a typed manifest error naming label and path", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-missing-exec-"));
    const { manifest, manifestPath } = await createProjectFixture(root, "missing-exec");
    manifest.defaultExecutionRoot = "missing-execution";
    await writeFile(manifestPath, JSON.stringify(manifest), "utf8");
    const registry = new ProjectRegistry(join(root, "user-data", "runtime"));
    await expect(
      registry.register(manifestPath, { approvedBy: "test", approvalReference: "D-TEST" })
    ).rejects.toMatchObject({
      name: "RuntimeError",
      code: "PROJECT_MANIFEST_INVALID",
      message: "defaultExecutionRoot references a path that does not exist: missing-execution"
    });
  });

  it("rejects a missing workingRoot with a typed manifest error naming label and path", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-missing-root-"));
    const { manifest, manifestPath } = await createProjectFixture(root, "missing-root");
    manifest.workingRoot = "no-such-root";
    await writeFile(manifestPath, JSON.stringify(manifest), "utf8");
    const registry = new ProjectRegistry(join(root, "user-data", "runtime"));
    await expect(
      registry.register(manifestPath, { approvedBy: "test", approvalReference: "D-TEST" })
    ).rejects.toMatchObject({
      code: "PROJECT_MANIFEST_INVALID",
      message: "workingRoot references a path that does not exist: no-such-root"
    });
  });

  it("tolerates an absent legacySessionRoots entry and lists no legacy sessions from it", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-legacy-absent-"));
    const { manifest, manifestPath } = await createProjectFixture(root, "legacy-absent");
    manifest.legacySessionRoots = ["frontend/.chirality/sessions"];
    await writeFile(manifestPath, JSON.stringify(manifest), "utf8");
    const runtimeDirectory = join(root, "user-data", "runtime");
    const registry = new ProjectRegistry(runtimeDirectory);
    const record = await registry.register(manifestPath, {
      approvedBy: "test",
      approvalReference: "D-TEST"
    });
    expect(record.legacySessionRoots).toEqual(["frontend/.chirality/sessions"]);
    const sessions = new SessionStore(runtimeDirectory, registry);
    await expect(sessions.list("legacy-absent")).resolves.toEqual([]);
  });

  it("still rejects a legacySessionRoots entry that exists but escapes the declared roots", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-legacy-escape-"));
    const { manifest, manifestPath } = await createProjectFixture(root, "legacy-escape");
    const { mkdir } = await import("node:fs/promises");
    await mkdir(join(root, "..", "outside-sessions"), { recursive: true });
    manifest.legacySessionRoots = ["../outside-sessions"];
    await writeFile(manifestPath, JSON.stringify(manifest), "utf8");
    const registry = new ProjectRegistry(join(root, "user-data", "runtime"));
    await expect(
      registry.register(manifestPath, { approvedBy: "test", approvalReference: "D-TEST" })
    ).rejects.toMatchObject({
      code: "PROJECT_MANIFEST_INVALID",
      message: "legacySessionRoots escapes the declared working and instruction roots"
    });
  });

  it("rejects symlink/path escapes outside both declared roots", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-escape-"));
    const { manifest, manifestPath } = await createProjectFixture(root, "escape");
    manifest.profiles.domain = ["../outside.yaml"];
    await writeFile(join(root, "..", "outside.yaml"), "outside\n", "utf8");
    await writeFile(manifestPath, JSON.stringify(manifest), "utf8");
    const registry = new ProjectRegistry(join(root, "user-data", "runtime"));
    await expect(
      registry.register(manifestPath, {
        approvedBy: "test",
        approvalReference: "D-TEST"
      })
    ).rejects.toBeDefined();
  });
});
