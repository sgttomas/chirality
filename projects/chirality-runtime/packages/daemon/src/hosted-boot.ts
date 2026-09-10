import { resolve, isAbsolute } from "node:path";
import { CHIRALITY_INSTRUCTION_ROOT_ENV, RuntimeError, type NativePlanAdapterQualification, type RuntimeCompatibilityIdentity, type WorkerContinuity } from "@chirality/runtime-contracts";
import { ProjectRegistry } from "@chirality/runtime-core";
import { CodexSupervisor } from "./codex-supervisor.js";
import { readHostedStandaloneConfig, startHostedStandaloneJob, startHostedStandaloneJobWithControlledSupervisorForTests, type StandaloneJob, type StandaloneRuntimeBindings } from "./hosted-standalone.js";

export type HostedRuntimeBootInput =
  | { enabled?: false }
  | {
    enabled: true;
    configPath: string;
    nativeAddonPath: string;
    instructionRoot?: string;
    selectedProject: {
      projectId: string;
      canonicalRoot: string;
      identity: WorkerContinuity;
      compatibility: RuntimeCompatibilityIdentity;
    };
    nativePlanQualification?: NativePlanAdapterQualification;
  };

export interface HostedRuntimeHost {
  socketPath: string;
  runtimeDirectory: string;
  stop(): Promise<void>;
}

type ReadyInput = Extract<HostedRuntimeBootInput, { enabled: true }>;
type JobStarter = (role: "daemon" | "supervisor", configPath: string, bindings: StandaloneRuntimeBindings) => Promise<StandaloneJob>;
const invalid = (message: string) => new RuntimeError("INVALID_REQUEST", message);
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);

function exactAbsolutePath(value: string, label: string): void {
  if (typeof value !== "string" || !isAbsolute(value) || resolve(value) !== value || /[\x00-\x1f]/.test(value)) throw invalid(`${label} must be a normalized absolute path`);
}

async function validateReadyInput(input: ReadyInput) {
  exactAbsolutePath(input.configPath, "Hosted configuration path");
  exactAbsolutePath(input.nativeAddonPath, "Native admission add-on path");
  if (input.instructionRoot !== undefined) exactAbsolutePath(input.instructionRoot, "Runtime instruction root");
  exactAbsolutePath(input.selectedProject.canonicalRoot, "Selected project root");
  const config = await readHostedStandaloneConfig(input.configPath);
  if (config.mode !== "hosted-validation") throw unavailable("Hosted runtime boot requires an explicit hosted-validation configuration");
  if (config.supplierAuthority === undefined || config.supplierAuthority.enabled !== false) throw unavailable("Hosted runtime supplier authority must remain explicitly disabled until native admission is qualified");
  const selected = input.selectedProject;
  if (selected.canonicalRoot !== selected.identity.canonicalRoot || selected.identity.cwd !== selected.canonicalRoot) throw invalid("Selected project continuity does not bind its canonical root");
  const sameIdentity = (["canonicalRoot", "cwd", "accountId", "accountEpoch", "policyDigest"] as const)
    .every(key => config.project.identity[key] === selected.identity[key]);
  const sameCompatibility = config.project.compatibility.compatibilityIdentity === selected.compatibility.compatibilityIdentity
    && config.project.compatibility.contractBasisSha256 === selected.compatibility.contractBasisSha256;
  if (config.project.projectId !== selected.projectId || config.project.identity.canonicalRoot !== selected.canonicalRoot
    || !sameIdentity || !sameCompatibility) {
    throw invalid("Hosted configuration does not exactly match the explicitly selected project and trusted continuity");
  }
  const projects = new ProjectRegistry(config.runtimeDirectory, input.instructionRoot === undefined ? {} : { [CHIRALITY_INSTRUCTION_ROOT_ENV]: input.instructionRoot });
  const registered = await projects.requireAuthorized(selected.projectId);
  if (registered.canonicalRoot !== selected.canonicalRoot) throw invalid("Selected project root differs from its explicit authorization");
  await projects.roots(selected.projectId);
  return config;
}

async function composeHostedRuntimeHost(input: HostedRuntimeBootInput | undefined, start: JobStarter): Promise<HostedRuntimeHost> {
  if (input?.enabled !== true) throw unavailable("Hosted runtime is not ready until an authorized project and trusted hosted configuration are selected");
  const config = await validateReadyInput(input);
  const bindings: StandaloneRuntimeBindings = { nativeAddonPath: input.nativeAddonPath, ...(input.instructionRoot === undefined ? {} : { instructionRoot: input.instructionRoot }), ...(input.nativePlanQualification === undefined ? {} : { nativePlanQualification: input.nativePlanQualification }) };
  const supervisor = await start("supervisor", input.configPath, bindings);
  let daemon: StandaloneJob;
  try { daemon = await start("daemon", input.configPath, bindings); }
  catch (error) { try { await supervisor.close(); } catch { /* Preserve the primary daemon startup failure. */ } throw error; }
  let stopping: Promise<void> | undefined;
  return {
    socketPath: daemon.socketPath,
    runtimeDirectory: config.runtimeDirectory,
    stop() {
      return stopping ??= (async () => {
        let failure: unknown;
        try { await daemon.close(); } catch (error) { failure = error; }
        try { await supervisor.close(); } catch (error) { failure ??= error; }
        if (failure !== undefined) throw failure;
      })();
    }
  };
}

/** Default-off Electron/host composition. All trusted project and continuity inputs must be explicit. */
export function startHostedRuntimeHost(input?: HostedRuntimeBootInput): Promise<HostedRuntimeHost> {
  return composeHostedRuntimeHost(input, startHostedStandaloneJob);
}

/** Controlled-provider test seam. It does not alter or serialize the production worker configuration. */
export function startControlledHostedRuntimeHostForTests(input: ReadyInput, supervisor: CodexSupervisor): Promise<HostedRuntimeHost> {
  return composeHostedRuntimeHost(input, (role, configPath, bindings) => startHostedStandaloneJobWithControlledSupervisorForTests(role, configPath, supervisor, bindings));
}
