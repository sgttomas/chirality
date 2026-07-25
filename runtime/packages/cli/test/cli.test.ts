import { mkdtemp, readFile, rm, stat, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { RuntimeStream } from "@chirality/runtime-client";
import type { RuntimeSseFrame } from "@chirality/runtime-contracts";
import {
  LaunchAgentManager,
  RUNTIME_LAUNCH_AGENT_LABEL,
  renderRuntimeLaunchAgent,
  resolveRuntimeLaunchAgentOptions
} from "../src/launch-agent.js";
import {
  runCli,
  type CliDependencies,
  type CliIo,
  type RuntimeCliClient,
  type RuntimeLaunchAgent
} from "../src/cli.js";

const temporaryDirectories: string[] = [];

function stream(events: readonly RuntimeSseFrame[]): RuntimeStream {
  return {
    async *[Symbol.asyncIterator]() {
      yield* events;
    },
    cancel() {}
  };
}

function fakeClient(
  overrides: Partial<RuntimeCliClient> = {}
): RuntimeCliClient {
  const unexpected = async (): Promise<never> => {
    throw new Error("Unexpected fake client method");
  };
  return {
    daemonStatus: unexpected,
    registerProject: unexpected,
    listProjects: unexpected,
    projectStatus: unexpected,
    listModels: unexpected,
    activateModel: unexpected,
    createSession: unexpected,
    listSessions: unexpected,
    replaySession: unexpected,
    turnSession: unexpected,
    interruptSession: unexpected,
    runAgent1: unexpected,
    ...overrides
  };
}

function fakeLaunchAgent(
  overrides: Partial<RuntimeLaunchAgent> = {}
): RuntimeLaunchAgent {
  return {
    async install() {},
    async start() {},
    async stop() {},
    async status() {
      return { installed: false, loaded: false };
    },
    async uninstall() {},
    ...overrides
  };
}

function io(stdin = ""): {
  io: CliIo;
  stdout: string[];
  stderr: string[];
} {
  const stdout: string[] = [];
  const stderr: string[] = [];
  return {
    stdout,
    stderr,
    io: {
      stdout(text) {
        stdout.push(text);
      },
      stderr(text) {
        stderr.push(text);
      },
      async readStdin() {
        return stdin;
      }
    }
  };
}

function dependencies(
  client: RuntimeCliClient,
  launchAgent: RuntimeLaunchAgent = fakeLaunchAgent()
): CliDependencies {
  return {
    client,
    launchAgent,
    paths: {
      userData: "/tmp/chirality-test",
      runtimeDirectory: "/tmp/chirality-test/runtime",
      socketPath: "/tmp/chirality-test/runtime/control.sock",
      tokenFile: "/tmp/chirality-test/runtime/operator.token",
      launchAgentsDirectory: "/tmp/chirality-test/LaunchAgents"
    },
    executablePath: "/Applications/Chirality.app/Contents/MacOS/Chirality",
    readTextFile: (path) => readFile(path, "utf8")
  };
}

afterEach(async () => {
  await Promise.all(
    temporaryDirectories.splice(0).map((directory) =>
      rm(directory, { recursive: true, force: true })
    )
  );
  vi.restoreAllMocks();
});

describe("chirality CLI", () => {
  it("runs an Agent 1 request from a brief file and emits UIEvent NDJSON", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-cli-run-"));
    temporaryDirectories.push(root);
    const briefFile = join(root, "brief.md");
    await writeFile(briefFile, "Inspect the bounded fixture.\n");
    const runAgent1 = vi.fn(async () =>
      stream([
        { type: "chat:delta", data: { text: "evidence" } },
        { type: "session:complete", data: {} },
        { type: "process:exit", data: { exitCode: 0 } }
      ])
    );
    const output = io();

    const exitCode = await runCli(
      [
        "run",
        "--project",
        "app-dev",
        "--agent",
        "WORKING_ITEMS",
        "--brief-file",
        briefFile,
        "--local-model",
        "mlx-community/model",
        "--json"
      ],
      output.io,
      dependencies(fakeClient({ runAgent1 }))
    );

    expect(exitCode).toBe(0);
    expect(runAgent1).toHaveBeenCalledWith("app-dev", {
      brief: "Inspect the bounded fixture.",
      agentId: "WORKING_ITEMS",
      approvalReference: "cli-agent1:WORKING_ITEMS",
      localModel: "mlx-community/model",
      readOnlyTool: {
        name: "read_file",
        relativePath: "chirality.project.json"
      }
    });
    expect(output.stdout.map((line) => JSON.parse(line))).toEqual([
      { type: "chat:delta", data: { text: "evidence" } },
      { type: "session:complete", data: {} },
      { type: "process:exit", data: { exitCode: 0 } }
    ]);
  });

  it("accepts a session-turn request through stdin and keeps human output non-JSON", async () => {
    const turnSession = vi.fn(async () =>
      stream([
        { type: "chat:delta", data: { text: "local text" } },
        { type: "process:exit", data: { exitCode: 0 } }
      ])
    );
    const output = io("prompt from stdin\n");

    const exitCode = await runCli(
      [
        "session",
        "turn",
        "--project",
        "app-dev",
        "--session",
        "sess-1"
      ],
      output.io,
      dependencies(fakeClient({ turnSession }))
    );

    expect(exitCode).toBe(0);
    expect(turnSession).toHaveBeenCalledWith("app-dev", "sess-1", {
      prompt: "prompt from stdin"
    });
    expect(output.stdout.join("")).toBe("local text[process:exit]\n");
  });

  it("propagates a failed session turn process exit", async () => {
    const turnSession = vi.fn(async () =>
      stream([
        {
          type: "turn:error",
          data: {
            phase: "mid-stream",
            errorType: "SDK_FAILURE",
            message: "manager failed",
            status: 502,
            severity: "error",
            fatal: true
          }
        },
        { type: "process:exit", data: { exitCode: 7, error: "manager failed" } }
      ])
    );
    const output = io("prompt\n");

    const exitCode = await runCli(
      [
        "session",
        "turn",
        "--project",
        "app-dev",
        "--session",
        "sess-failed"
      ],
      output.io,
      dependencies(fakeClient({ turnSession }))
    );

    expect(exitCode).toBe(7);
    expect(output.stderr.join("")).toContain("SDK_FAILURE: manager failed");
    expect(output.stderr.join("")).toContain("process exited 7");
  });

  it("rejects an Agent 1 stream that ends without process:exit", async () => {
    const runAgent1 = vi.fn(async () =>
      stream([
        { type: "chat:delta", data: { text: "partial" } },
        { type: "session:complete", data: {} }
      ])
    );
    const output = io("bounded brief\n");

    const exitCode = await runCli(
      ["run", "--project", "app-dev", "--agent", "WORKING_ITEMS"],
      output.io,
      dependencies(fakeClient({ runAgent1 }))
    );

    expect(exitCode).toBe(1);
    expect(output.stderr.join("")).toContain(
      "INTERNAL_FAILURE: Runtime stream ended without terminal process:exit"
    );
  });

  it("has no credential command surface", async () => {
    const output = io();
    const client = fakeClient({ listProjects: vi.fn() });

    const exitCode = await runCli(
      ["credential", "set"],
      output.io,
      dependencies(client)
    );

    expect(exitCode).toBe(2);
    expect(output.stderr.join("")).toContain("Unknown command");
    expect(client.listProjects).not.toHaveBeenCalled();
  });

  it("does not reject ordinary request paths or model IDs containing credential-like words", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-cli-token-named-file-"));
    temporaryDirectories.push(root);
    const briefFile = join(root, "api-key-token-analysis.md");
    await writeFile(briefFile, "Analyze naming without handling credentials.\n");
    const runAgent1 = vi.fn(async () =>
      stream([{ type: "process:exit", data: { exitCode: 0 } }])
    );
    const output = io();

    const exitCode = await runCli(
      [
        "run",
        "--project",
        "app-dev",
        "--agent",
        "WORKING_ITEMS",
        "--brief-file",
        briefFile,
        "--local-model",
        "mlx-community/token-counter"
      ],
      output.io,
      dependencies(fakeClient({ runAgent1 }))
    );

    expect(exitCode).toBe(0);
    expect(runAgent1).toHaveBeenCalledOnce();
  });

  it("renders and installs a private opt-in LaunchAgent without a model argument", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-launch-agent-"));
    temporaryDirectories.push(root);
    const launchAgentsDirectory = join(root, "LaunchAgents");
    const runtimeDirectory = join(root, "user-data", "runtime");
    const calls: Array<{ executable: string; args: readonly string[] }> = [];
    const manager = new LaunchAgentManager(
      { launchAgentsDirectory, runtimeDirectory },
      async (executable, args) => {
        calls.push({ executable, args });
        return { exitCode: 0, stdout: "ok", stderr: "" };
      },
      501
    );
    const executablePath = "/Applications/Chirality.app/Contents/MacOS/Chirality";

    await manager.install(executablePath);
    const source = await readFile(manager.plistPath, "utf8");
    const metadata = await stat(manager.plistPath);
    const runtimeMetadata = await stat(runtimeDirectory);
    const logsMetadata = await stat(join(runtimeDirectory, "logs"));
    expect(metadata.mode & 0o777).toBe(0o600);
    expect(runtimeMetadata.mode & 0o777).toBe(0o700);
    expect(logsMetadata.mode & 0o777).toBe(0o700);
    expect(source).toContain(`<string>${RUNTIME_LAUNCH_AGENT_LABEL}</string>`);
    expect(source).toContain("<string>--runtime-daemon</string>");
    expect(source).toContain("<key>RunAtLoad</key>");
    expect(source).toContain("<key>KeepAlive</key>");
    expect(source).toContain("<key>SuccessfulExit</key>");
    expect(source).toContain("<false/>");
    expect(source).toContain("<key>ThrottleInterval</key>");
    expect(source).not.toMatch(/model|activate|omlx/iu);

    // `bootstrap` on a fresh job already starts it under RunAtLoad, so no
    // kickstart follows: a second launch inside ThrottleInterval would stall the
    // call for the rest of the window and double the job's launch count.
    await manager.start();
    expect(calls).toEqual([
      {
        executable: "launchctl",
        args: ["bootstrap", "gui/501", manager.plistPath]
      }
    ]);
  });

  it("escapes executable and log paths in the LaunchAgent plist", () => {
    const source = renderRuntimeLaunchAgent({
      executablePath: "/Applications/A&B<Dev>.app/Chirality",
      runtimeDirectory: "/tmp/A&B"
    });
    expect(source).toContain("A&amp;B&lt;Dev&gt;");
    expect(source).toContain("/tmp/A&amp;B/logs");
  });

  it("renders KeepAlive=true so launchd also restarts after a clean exit", () => {
    const source = renderRuntimeLaunchAgent({
      executablePath: "/Applications/Chirality.app/Chirality",
      runtimeDirectory: "/tmp/keep-alive-always",
      keepAlive: "always"
    });
    expect(source).toContain("<key>KeepAlive</key>\n  <true/>");
    // The crash-only semaphore must be gone: it is precisely what suppressed a
    // relaunch after an externally induced `exit(0)`.
    expect(source).not.toContain("<key>SuccessfulExit</key>");
  });

  it("omits KeepAlive entirely when restarts are not wanted", () => {
    const source = renderRuntimeLaunchAgent({
      executablePath: "/Applications/Chirality.app/Chirality",
      runtimeDirectory: "/tmp/keep-alive-never",
      keepAlive: "never"
    });
    expect(source).not.toContain("<key>KeepAlive</key>");
  });

  it("pins EnvironmentVariables, RunAtLoad and ThrottleInterval when supplied", () => {
    const source = renderRuntimeLaunchAgent({
      executablePath: "/Applications/Chirality.app/Chirality",
      runtimeDirectory: "/tmp/env-pinning",
      runAtLoad: false,
      throttleIntervalSeconds: 4,
      environmentVariables: {
        CHIRALITY_USER_DATA: "/tmp/A&B/user-data",
        OTHER: "value"
      }
    });
    expect(source).toContain("<key>RunAtLoad</key>\n  <false/>");
    expect(source).toContain("<key>ThrottleInterval</key>\n  <integer>4</integer>");
    expect(source).toContain("<key>EnvironmentVariables</key>");
    expect(source).toContain("<key>CHIRALITY_USER_DATA</key>");
    // Values reach the plist through the same XML escaping as every other path.
    expect(source).toContain("<string>/tmp/A&amp;B/user-data</string>");
    expect(source).toContain("<key>OTHER</key>");
  });

  it("omits the EnvironmentVariables block when no variables are pinned", () => {
    const source = renderRuntimeLaunchAgent({
      executablePath: "/Applications/Chirality.app/Chirality",
      runtimeDirectory: "/tmp/no-env"
    });
    expect(source).not.toContain("<key>EnvironmentVariables</key>");
  });

  it("keeps the historical plist as the default so existing callers are unchanged", () => {
    const source = renderRuntimeLaunchAgent({
      executablePath: "/Applications/Chirality.app/Chirality",
      runtimeDirectory: "/tmp/defaults"
    });
    expect(source).toContain(`<string>${RUNTIME_LAUNCH_AGENT_LABEL}</string>`);
    expect(source).toContain("<key>RunAtLoad</key>\n  <true/>");
    expect(source).toContain("<key>KeepAlive</key>\n  <dict>");
    expect(source).toContain("<key>SuccessfulExit</key>");
    expect(source).toContain("<key>ThrottleInterval</key>\n  <integer>10</integer>");
  });

  it("routes an overridden label through the plist path, service name and plist body", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-launch-agent-label-"));
    temporaryDirectories.push(root);
    const calls: Array<{ executable: string; args: readonly string[] }> = [];
    const manager = new LaunchAgentManager(
      {
        launchAgentsDirectory: join(root, "LaunchAgents"),
        runtimeDirectory: join(root, "user-data", "runtime")
      },
      async (executable, args) => {
        calls.push({ executable, args });
        return { exitCode: 0, stdout: "ok", stderr: "" };
      },
      501,
      {
        label: "com.chirality.runtime.isolated",
        keepAlive: "always",
        environmentVariables: { CHIRALITY_USER_DATA: join(root, "user-data") }
      }
    );

    expect(manager.label).toBe("com.chirality.runtime.isolated");
    expect(manager.plistPath).toBe(
      join(root, "LaunchAgents", "com.chirality.runtime.isolated.plist")
    );

    await manager.install("/Applications/Chirality.app/Contents/MacOS/Chirality");
    const source = await readFile(manager.plistPath, "utf8");
    expect(source).toContain("<string>com.chirality.runtime.isolated</string>");
    expect(source).toContain("<key>KeepAlive</key>\n  <true/>");
    expect(source).toContain("<key>CHIRALITY_USER_DATA</key>");
    expect(source).not.toContain(`<string>${RUNTIME_LAUNCH_AGENT_LABEL}</string>`);

    // An isolated job must be startable and stoppable without ever naming the
    // default service, which is what keeps a verification run off a real agent.
    await manager.start();
    await manager.stop();
    expect(calls.map((call) => call.args)).toEqual([
      ["bootstrap", "gui/501", manager.plistPath],
      ["bootout", "gui/501/com.chirality.runtime.isolated"]
    ]);
  });

  it("kickstarts only when bootstrap did not itself start the job", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-launch-agent-kickstart-"));
    temporaryDirectories.push(root);
    const paths = {
      launchAgentsDirectory: join(root, "LaunchAgents"),
      runtimeDirectory: join(root, "user-data", "runtime")
    };

    // Case 1: already loaded. `bootstrap` fails with launchctl's already-loaded
    // signal, so a kickstart is the only thing that can (re)start the job.
    const alreadyLoadedCalls: Array<readonly string[]> = [];
    const alreadyLoaded = new LaunchAgentManager(
      paths,
      async (_executable, args) => {
        alreadyLoadedCalls.push(args);
        return args[0] === "bootstrap"
          ? { exitCode: 5, stdout: "", stderr: "Bootstrap failed: 5: Input/output error" }
          : { exitCode: 0, stdout: "ok", stderr: "" };
      },
      501
    );
    await alreadyLoaded.start();
    expect(alreadyLoadedCalls).toEqual([
      ["bootstrap", "gui/501", alreadyLoaded.plistPath],
      ["kickstart", "-k", "gui/501/com.chirality.runtime"]
    ]);

    // Case 2: RunAtLoad off. A fresh bootstrap loads the job but launchd will not
    // run it, so the kickstart is genuinely required.
    const manualCalls: Array<readonly string[]> = [];
    const manual = new LaunchAgentManager(
      paths,
      async (_executable, args) => {
        manualCalls.push(args);
        return { exitCode: 0, stdout: "ok", stderr: "" };
      },
      501,
      { runAtLoad: false }
    );
    await manual.start();
    expect(manualCalls).toEqual([
      ["bootstrap", "gui/501", manual.plistPath],
      ["kickstart", "-k", "gui/501/com.chirality.runtime"]
    ]);
  });

  it("still fails loudly when bootstrap fails for a reason other than already-loaded", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-launch-agent-bootstrap-fail-"));
    temporaryDirectories.push(root);
    const manager = new LaunchAgentManager(
      {
        launchAgentsDirectory: join(root, "LaunchAgents"),
        runtimeDirectory: join(root, "user-data", "runtime")
      },
      async () => ({ exitCode: 1, stdout: "", stderr: "Operation not permitted" }),
      501
    );

    await expect(manager.start()).rejects.toThrow("Operation not permitted");
  });
});

describe("resolveRuntimeLaunchAgentOptions", () => {
  const userData = "/Users/example/Library/Application Support/chirality-frontend";

  it("pins a self-describing job environment: runtime directory, label and posture", () => {
    // launchd inherits almost nothing, and an unpinned Electron daemon resolves a
    // different default userData than this CLI does — the mismatch the pin removes.
    // Label and posture are pinned too so a process the daemon starts inherits the
    // same job identity rather than falling back to the default label.
    expect(resolveRuntimeLaunchAgentOptions({}, userData)).toEqual({
      environmentVariables: {
        CHIRALITY_USER_DATA: userData,
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: "com.chirality.runtime",
        CHIRALITY_RUNTIME_KEEP_ALIVE: "crash-only"
      }
    });
  });

  it("pins the isolated label into the job so children cannot escape isolation", () => {
    const options = resolveRuntimeLaunchAgentOptions(
      {
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: "com.chirality.runtime.tranchetest",
        CHIRALITY_RUNTIME_KEEP_ALIVE: "always"
      },
      userData
    );

    expect(options.environmentVariables).toEqual({
      CHIRALITY_USER_DATA: userData,
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: "com.chirality.runtime.tranchetest",
      CHIRALITY_RUNTIME_KEEP_ALIVE: "always"
    });
  });

  it("resolves a relative runtime directory so a plist never carries one", () => {
    const options = resolveRuntimeLaunchAgentOptions({}, "relative/user-data");
    expect(options.environmentVariables?.CHIRALITY_USER_DATA).toBe(
      resolve("relative/user-data")
    );
  });

  it("reads the full posture from the environment", () => {
    expect(
      resolveRuntimeLaunchAgentOptions(
        {
          CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: " com.chirality.runtime.tranchetest ",
          CHIRALITY_RUNTIME_KEEP_ALIVE: "ALWAYS",
          CHIRALITY_RUNTIME_RUN_AT_LOAD: "yes",
          CHIRALITY_RUNTIME_THROTTLE_INTERVAL_SECONDS: "30"
        },
        userData
      )
    ).toEqual({
      label: "com.chirality.runtime.tranchetest",
      keepAlive: "always",
      runAtLoad: true,
      throttleIntervalSeconds: 30,
      environmentVariables: {
        CHIRALITY_USER_DATA: userData,
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: "com.chirality.runtime.tranchetest",
        CHIRALITY_RUNTIME_KEEP_ALIVE: "always"
      }
    });
  });

  it("accepts the documented false spellings for RunAtLoad", () => {
    for (const value of ["0", "false", "no", "OFF"]) {
      expect(
        resolveRuntimeLaunchAgentOptions({ CHIRALITY_RUNTIME_RUN_AT_LOAD: value }, userData)
          .runAtLoad
      ).toBe(false);
    }
  });

  it("omits unrecognised or blank values so each option keeps its default", () => {
    // A typo must never stop the CLI from managing a job.
    const options = resolveRuntimeLaunchAgentOptions(
      {
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: "   ",
        CHIRALITY_RUNTIME_KEEP_ALIVE: "sometimes",
        CHIRALITY_RUNTIME_RUN_AT_LOAD: "perhaps",
        CHIRALITY_RUNTIME_THROTTLE_INTERVAL_SECONDS: "soon"
      },
      userData
    );

    expect(options).not.toHaveProperty("label");
    expect(options).not.toHaveProperty("keepAlive");
    expect(options).not.toHaveProperty("runAtLoad");
    expect(options).not.toHaveProperty("throttleIntervalSeconds");
  });

  it("rejects a negative throttle interval", () => {
    expect(
      resolveRuntimeLaunchAgentOptions(
        { CHIRALITY_RUNTIME_THROTTLE_INTERVAL_SECONDS: "-5" },
        userData
      )
    ).not.toHaveProperty("throttleIntervalSeconds");
  });

  it("renders the intended plist end to end from environment alone", () => {
    const options = resolveRuntimeLaunchAgentOptions(
      {
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: "com.chirality.runtime",
        CHIRALITY_RUNTIME_KEEP_ALIVE: "always"
      },
      userData
    );
    const source = renderRuntimeLaunchAgent({
      ...options,
      executablePath: "/Applications/Chirality.app/Contents/MacOS/Chirality",
      runtimeDirectory: `${userData}/runtime`
    });

    expect(source).toContain("<key>KeepAlive</key>\n  <true/>");
    expect(source).toContain("<key>RunAtLoad</key>\n  <true/>");
    expect(source).toContain("<key>CHIRALITY_USER_DATA</key>");
    expect(source).not.toContain("<key>SuccessfulExit</key>");
  });
});
