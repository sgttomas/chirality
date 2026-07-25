import { spawn } from "node:child_process";
import { chmod, mkdir, open, rename, unlink } from "node:fs/promises";
import { basename, dirname, join, resolve } from "node:path";

export const RUNTIME_LAUNCH_AGENT_LABEL = "com.chirality.runtime";

export interface CommandResult {
  exitCode: number;
  stdout: string;
  stderr: string;
}

export type CommandRunner = (
  executable: string,
  args: readonly string[]
) => Promise<CommandResult>;

export interface LaunchAgentPaths {
  launchAgentsDirectory: string;
  runtimeDirectory: string;
}

export interface LaunchAgentStatus {
  installed: boolean;
  loaded: boolean;
  detail?: string;
}

/**
 * launchd restart posture for the managed job.
 *
 * - `"crash-only"` renders `KeepAlive = { SuccessfulExit: false }`: launchd
 *   relaunches the job only when it exited non-zero. A job that exits 0 is held
 *   down by launchd's `successful exit` semaphore and stays dead until an
 *   operator intervenes.
 * - `"always"` renders `KeepAlive = true`: launchd relaunches the job after
 *   *any* exit, including a clean `exit(0)`. Use this when a clean exit is
 *   itself an unwanted outcome (for example an externally induced quit).
 * - `"never"` omits `KeepAlive` entirely: the job runs once per load.
 *
 * `KeepAlive` interacts with `launchctl` verbs in ways that are easy to get
 * wrong, so callers should note:
 * - `launchctl bootout <service>` *unloads* the job from the domain, which
 *   removes the KeepAlive contract with it. Stop semantics therefore keep
 *   working under `"always"`; the daemon stays stopped until it is bootstrapped
 *   again. (`launchctl stop`, by contrast, would be immediately undone by
 *   `KeepAlive = true` — this module deliberately never uses `stop`.)
 * - `launchctl kickstart -k` kills a running instance and starts a fresh one.
 *   Under `"always"` launchd would also relaunch the killed instance on its
 *   own, so `-k` is a redundant-but-harmless restart rather than the only
 *   restart path. `ThrottleInterval` bounds how fast those relaunches occur.
 */
export type LaunchAgentKeepAlivePolicy = "always" | "crash-only" | "never";

export interface RuntimeLaunchAgentOptions {
  /** Job label; also names the plist file and the `gui/<uid>/<label>` service. */
  label?: string;
  /** launchd restart posture. Defaults to `"crash-only"`. */
  keepAlive?: LaunchAgentKeepAlivePolicy;
  /** Whether launchd starts the job as soon as it is loaded. Defaults to `true`. */
  runAtLoad?: boolean;
  /** Minimum seconds between successive launches. Defaults to `10`. */
  throttleIntervalSeconds?: number;
  /**
   * Environment pinned into the job. launchd jobs inherit almost nothing from
   * an interactive shell, so any variable the program needs must be declared
   * here explicitly.
   */
  environmentVariables?: Readonly<Record<string, string>>;
}

const DEFAULT_KEEP_ALIVE: LaunchAgentKeepAlivePolicy = "crash-only";
const DEFAULT_THROTTLE_INTERVAL_SECONDS = 10;

/**
 * Environment variables that configure the managed job's posture.
 *
 * These exist so a *caller* — the desktop app's generated launcher, an isolated
 * verification run, an operator shell — can select the posture without this
 * package carrying any project-specific constant (D-GOV-20). Every name belongs
 * to this package; nothing here knows about a particular app.
 *
 * `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL` is the load-bearing one for safety: it
 * governs the plist filename, the plist `Label`, and the `gui/<uid>/<label>`
 * service name that `bootstrap`/`kickstart`/`bootout`/`print` address. Without it
 * every CLI invocation resolves to the default label, so a fully isolated
 * environment (own `HOME`, own `CHIRALITY_USER_DATA`) still reported — and could
 * have booted out or deleted — an operator's real job, because the launchd
 * domain is per-uid and honours neither `HOME` nor `CHIRALITY_USER_DATA`.
 */
export const RUNTIME_LAUNCH_AGENT_ENV = {
  label: "CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL",
  keepAlive: "CHIRALITY_RUNTIME_KEEP_ALIVE",
  runAtLoad: "CHIRALITY_RUNTIME_RUN_AT_LOAD",
  throttleIntervalSeconds: "CHIRALITY_RUNTIME_THROTTLE_INTERVAL_SECONDS"
} as const;

/** Variable pinned into the job so the daemon shares the caller's runtime directory. */
export const RUNTIME_USER_DATA_ENV = "CHIRALITY_USER_DATA";

function parseBoolean(value: string): boolean | undefined {
  const normalized = value.trim().toLowerCase();
  if (["1", "true", "yes", "on"].includes(normalized)) {
    return true;
  }
  if (["0", "false", "no", "off"].includes(normalized)) {
    return false;
  }
  return undefined;
}

function parseKeepAlive(value: string): LaunchAgentKeepAlivePolicy | undefined {
  const normalized = value.trim().toLowerCase();
  return normalized === "always" || normalized === "crash-only" || normalized === "never"
    ? normalized
    : undefined;
}

/**
 * Build job options from the environment, pinning `userDataDirectory`.
 *
 * Unrecognised or blank values are *omitted* rather than rejected, so each
 * option falls back to the documented default and a typo can never stop the CLI
 * from managing a job. `userDataDirectory` is always pinned because launchd jobs
 * inherit almost nothing: an unpinned daemon resolves its own default, which for
 * an Electron bundle is not the same directory this CLI resolves — the exact
 * mismatch the pin exists to remove.
 */
export function resolveRuntimeLaunchAgentOptions(
  environment: Readonly<Record<string, string | undefined>>,
  userDataDirectory: string
): RuntimeLaunchAgentOptions {
  const options: RuntimeLaunchAgentOptions = {
    environmentVariables: { [RUNTIME_USER_DATA_ENV]: resolve(userDataDirectory) }
  };

  const label = environment[RUNTIME_LAUNCH_AGENT_ENV.label]?.trim();
  if (label) {
    options.label = label;
  }

  const keepAliveRaw = environment[RUNTIME_LAUNCH_AGENT_ENV.keepAlive];
  const keepAlive = keepAliveRaw === undefined ? undefined : parseKeepAlive(keepAliveRaw);
  if (keepAlive !== undefined) {
    options.keepAlive = keepAlive;
  }

  // The job's environment describes the job. Pinning the effective label and
  // restart posture — not just the runtime directory — makes the installed job
  // self-describing, so a process the daemon starts (see the GUI spawned on
  // `activate`) inherits the *same* label instead of falling back to the default.
  // Without this, an isolated run driven through the CLI would install an
  // isolated job whose children silently addressed the operator's job.
  options.environmentVariables = {
    ...options.environmentVariables,
    [RUNTIME_LAUNCH_AGENT_ENV.label]: options.label ?? RUNTIME_LAUNCH_AGENT_LABEL,
    [RUNTIME_LAUNCH_AGENT_ENV.keepAlive]: options.keepAlive ?? DEFAULT_KEEP_ALIVE
  };

  const runAtLoadRaw = environment[RUNTIME_LAUNCH_AGENT_ENV.runAtLoad];
  const runAtLoad = runAtLoadRaw === undefined ? undefined : parseBoolean(runAtLoadRaw);
  if (runAtLoad !== undefined) {
    options.runAtLoad = runAtLoad;
  }

  const throttleRaw = environment[RUNTIME_LAUNCH_AGENT_ENV.throttleIntervalSeconds]?.trim();
  if (throttleRaw) {
    const throttle = Number.parseInt(throttleRaw, 10);
    if (Number.isFinite(throttle) && throttle >= 0) {
      options.throttleIntervalSeconds = throttle;
    }
  }

  return options;
}

function xml(value: string): string {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");
}

function renderKeepAlive(policy: LaunchAgentKeepAlivePolicy): string {
  if (policy === "never") {
    return "";
  }
  if (policy === "always") {
    return `  <key>KeepAlive</key>
  <true/>
`;
  }
  return `  <key>KeepAlive</key>
  <dict>
    <key>SuccessfulExit</key>
    <false/>
  </dict>
`;
}

function renderEnvironmentVariables(
  environmentVariables: Readonly<Record<string, string>> | undefined
): string {
  const entries = Object.entries(environmentVariables ?? {});
  if (entries.length === 0) {
    return "";
  }
  const body = entries
    .map(
      ([name, value]) =>
        `    <key>${xml(name)}</key>\n    <string>${xml(value)}</string>`
    )
    .join("\n");
  return `  <key>EnvironmentVariables</key>
  <dict>
${body}
  </dict>
`;
}

export function renderRuntimeLaunchAgent(
  input: {
    executablePath: string;
    runtimeDirectory: string;
  } & RuntimeLaunchAgentOptions
): string {
  const logs = join(input.runtimeDirectory, "logs");
  const label = input.label ?? RUNTIME_LAUNCH_AGENT_LABEL;
  const runAtLoad = input.runAtLoad ?? true;
  const throttleInterval =
    input.throttleIntervalSeconds ?? DEFAULT_THROTTLE_INTERVAL_SECONDS;
  return `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${xml(label)}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${xml(resolve(input.executablePath))}</string>
    <string>--runtime-daemon</string>
  </array>
  <key>RunAtLoad</key>
  <${runAtLoad ? "true" : "false"}/>
${renderKeepAlive(input.keepAlive ?? DEFAULT_KEEP_ALIVE)}${renderEnvironmentVariables(
    input.environmentVariables
  )}  <key>ThrottleInterval</key>
  <integer>${Math.trunc(throttleInterval)}</integer>
  <key>StandardOutPath</key>
  <string>${xml(join(logs, "daemon.stdout.log"))}</string>
  <key>StandardErrorPath</key>
  <string>${xml(join(logs, "daemon.stderr.log"))}</string>
</dict>
</plist>
`;
}

async function defaultCommandRunner(
  executable: string,
  args: readonly string[]
): Promise<CommandResult> {
  return new Promise((resolveResult, reject) => {
    const child = spawn(executable, [...args], {
      stdio: ["ignore", "pipe", "pipe"]
    });
    let stdout = "";
    let stderr = "";
    child.stdout.setEncoding("utf8");
    child.stderr.setEncoding("utf8");
    child.stdout.on("data", (chunk: string) => {
      stdout += chunk;
    });
    child.stderr.on("data", (chunk: string) => {
      stderr += chunk;
    });
    child.once("error", reject);
    child.once("exit", (code) => {
      resolveResult({ exitCode: code ?? 1, stdout, stderr });
    });
  });
}

async function atomicWrite(filePath: string, content: string): Promise<void> {
  await mkdir(dirname(filePath), { recursive: true });
  const temporary = join(
    dirname(filePath),
    `.${basename(filePath)}.${process.pid}.${Date.now()}.tmp`
  );
  let committed = false;
  try {
    const handle = await open(temporary, "wx", 0o600);
    try {
      await handle.writeFile(content, "utf8");
      await handle.sync();
    } finally {
      await handle.close();
    }
    await rename(temporary, filePath);
    await chmod(filePath, 0o600);
    committed = true;
  } finally {
    if (!committed) {
      await unlink(temporary).catch((error: NodeJS.ErrnoException) => {
        if (error.code !== "ENOENT") throw error;
      });
    }
  }
}

async function ensurePrivateDirectory(path: string): Promise<void> {
  await mkdir(path, { recursive: true, mode: 0o700 });
  await chmod(path, 0o700);
}

export class LaunchAgentManager {
  readonly plistPath: string;
  readonly label: string;
  private readonly domain: string;
  private readonly service: string;
  private readonly options: RuntimeLaunchAgentOptions;

  constructor(
    private readonly paths: LaunchAgentPaths,
    private readonly runCommand: CommandRunner = defaultCommandRunner,
    userId = process.getuid?.() ?? 0,
    options: RuntimeLaunchAgentOptions = {}
  ) {
    this.options = options;
    this.label = options.label ?? RUNTIME_LAUNCH_AGENT_LABEL;
    this.plistPath = join(
      resolve(paths.launchAgentsDirectory),
      `${this.label}.plist`
    );
    this.domain = `gui/${userId}`;
    this.service = `${this.domain}/${this.label}`;
  }

  async install(executablePath: string): Promise<void> {
    await ensurePrivateDirectory(this.paths.runtimeDirectory);
    await ensurePrivateDirectory(join(this.paths.runtimeDirectory, "logs"));
    await atomicWrite(
      this.plistPath,
      renderRuntimeLaunchAgent({
        ...this.options,
        label: this.label,
        executablePath,
        runtimeDirectory: this.paths.runtimeDirectory
      })
    );
  }

  /**
   * Load the job and make sure it is running.
   *
   * `bootstrap` on a not-yet-loaded job already starts it when `RunAtLoad` is
   * set, so the follow-up `kickstart -k` is not merely redundant: it is a
   * *second* launch inside `ThrottleInterval`, which makes launchd hold the
   * request for the remainder of the window (measured at 10.07 s for the default
   * 10 s interval) and doubles the job's launch count. `kickstart` is therefore
   * reserved for the two cases that genuinely need it — an already-loaded job
   * (this is the restart path) and a job whose `RunAtLoad` is off.
   */
  async start(): Promise<void> {
    const bootstrap = await this.runCommand("launchctl", [
      "bootstrap",
      this.domain,
      this.plistPath
    ]);
    const freshlyLoaded = bootstrap.exitCode === 0;
    if (
      !freshlyLoaded &&
      !/already loaded|service already loaded|bootstrap failed: 5/iu.test(
        `${bootstrap.stdout}\n${bootstrap.stderr}`
      )
    ) {
      throw new Error(bootstrap.stderr.trim() || "Unable to bootstrap runtime LaunchAgent");
    }
    if (freshlyLoaded && (this.options.runAtLoad ?? true)) {
      return;
    }
    const start = await this.runCommand("launchctl", ["kickstart", "-k", this.service]);
    if (start.exitCode !== 0) {
      throw new Error(start.stderr.trim() || "Unable to start runtime LaunchAgent");
    }
  }

  async stop(): Promise<void> {
    const result = await this.runCommand("launchctl", ["bootout", this.service]);
    if (
      result.exitCode !== 0 &&
      !/could not find service|no such process|not found/iu.test(
        `${result.stdout}\n${result.stderr}`
      )
    ) {
      throw new Error(result.stderr.trim() || "Unable to stop runtime LaunchAgent");
    }
  }

  async status(): Promise<LaunchAgentStatus> {
    const installed = await import("node:fs/promises").then(({ stat }) =>
      stat(this.plistPath).then(
        () => true,
        () => false
      )
    );
    const result = await this.runCommand("launchctl", ["print", this.service]);
    return {
      installed,
      loaded: result.exitCode === 0,
      ...(result.exitCode === 0
        ? { detail: result.stdout.trim() }
        : result.stderr.trim()
          ? { detail: result.stderr.trim() }
          : {})
    };
  }

  async uninstall(): Promise<void> {
    await this.stop();
    await unlink(this.plistPath).catch((error: NodeJS.ErrnoException) => {
      if (error.code !== "ENOENT") throw error;
    });
  }
}
