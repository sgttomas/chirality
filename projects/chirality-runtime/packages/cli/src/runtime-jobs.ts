import { dirname, isAbsolute, join, normalize, relative } from "node:path";

export interface RuntimeJobCommand {
  label: string;
  executablePath: string;
  /** Exact non-secret arguments supported by the trusted executable. Never caller input. */
  args: readonly string[];
  socketPath: string;
}
export interface RuntimeJobsInput {
  privateDirectory: string;
  daemon: RuntimeJobCommand;
  supervisor: RuntimeJobCommand;
}
export interface RenderedRuntimeJob {
  label: string;
  programArguments: readonly string[];
  socketPath: string;
  plist: string;
}
export interface RenderedRuntimeJobs {
  mode: "render-only";
  transport: "unix";
  supervisorExposure: "daemon-only";
  daemon: RenderedRuntimeJob;
  supervisor: RenderedRuntimeJob;
  requirements: { directoryMode: 0o700; socketMode: 0o600; credentialExchange: "runtime-only" };
}
function exactKeys(value: object, keys: string[]): void {
  if (Object.keys(value).some(key => !keys.includes(key))) throw new Error("unsupported configuration field; credentials and exposure overrides are forbidden");
}
function absolute(value: string): void {
  if (typeof value !== "string" || !isAbsolute(value) || normalize(value) !== value || /[\x00-\x1f]/.test(value)) throw new Error("expected normalized absolute path");
}
function xml(value: string): string {
  return value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&apos;");
}
function render(command: RuntimeJobCommand, privateDirectory: string): RenderedRuntimeJob {
  const programArguments = [command.executablePath, ...command.args];
  const plist = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>${xml(command.label)}</string>
  <key>ProgramArguments</key><array>${programArguments.map(value => `<string>${xml(value)}</string>`).join("")}</array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><dict><key>SuccessfulExit</key><false/></dict>
  <key>ThrottleInterval</key><integer>10</integer>
  <key>Umask</key><integer>63</integer>
  <key>StandardOutPath</key><string>${xml(join(privateDirectory, `${command.label}.stdout.log`))}</string>
  <key>StandardErrorPath</key><string>${xml(join(privateDirectory, `${command.label}.stderr.log`))}</string>
</dict>
</plist>
`;
  return { label: command.label, programArguments, socketPath: command.socketPath, plist };
}
/**
 * Pure launch-plan rendering, not installation or proof that an arbitrary runner
 * honors this topology. Callers provide real supported executable/argument pairs;
 * no supervisor switch or environment variable is invented here. A separate
 * launcher must privately provision directories, pass socket configuration by its
 * supported interface and exchange epoch credentials at runtime. The daemon is
 * the sole public broker; the supervisor capability must never reach its clients.
 * Credentials must not appear in arguments; obvious secret/network flags are
 * rejected, but trusted command review is still required for arbitrary programs.
 */
export function renderRuntimeJobs(input: RuntimeJobsInput): RenderedRuntimeJobs {
  exactKeys(input, ["privateDirectory", "daemon", "supervisor"]);
  absolute(input.privateDirectory);
  if (dirname(input.privateDirectory) === input.privateDirectory) throw new Error("root is not a private runtime directory");
  for (const command of [input.daemon, input.supervisor]) {
    exactKeys(command, ["label", "executablePath", "args", "socketPath"]);
    if (!/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(command.label)) throw new Error("invalid job label");
    absolute(command.executablePath); absolute(command.socketPath);
    const path = relative(input.privateDirectory, command.socketPath);
    if (!path || path === ".." || path.startsWith("../") || isAbsolute(path)) throw new Error("socket must be inside private directory");
    if (!Array.isArray(command.args) || command.args.length > 128 || command.args.some(arg => typeof arg !== "string" || arg.length > 4096 || /[\x00-\x1f]/.test(arg))) throw new Error("invalid exact arguments");
    if (command.args.some(arg => /(?:token|password|secret|credential|authorization)|(?:^|=)(?:https?|tcp|ws|wss):\/\/|^--(?:host|port|listen|bind)(?:=|$)/i.test(arg))) throw new Error("credential or public network arguments forbidden");
  }
  if (input.daemon.label === input.supervisor.label || input.daemon.socketPath === input.supervisor.socketPath) throw new Error("jobs require distinct labels and sockets");
  return { mode: "render-only", transport: "unix", supervisorExposure: "daemon-only", daemon: render(input.daemon, input.privateDirectory), supervisor: render(input.supervisor, input.privateDirectory), requirements: { directoryMode: 0o700, socketMode: 0o600, credentialExchange: "runtime-only" } };
}
