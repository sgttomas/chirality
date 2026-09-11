import path from 'node:path';
import { pathToFileURL } from 'node:url';
import {
  AuthRegistry,
  EngineRegistry,
  ProjectRegistry,
  ResidencyCoordinator,
  RuntimeService,
  SessionStore,
  TurnCoordinator
} from '@chirality/runtime-core';
import type { OmlxControlPort } from '@chirality/runtime-contracts';
import { RuntimeError } from '@chirality/runtime-contracts';
import { RuntimeDaemon } from '@chirality/runtime-daemon';
import { StubAgentSdkManager } from '../src/lib/harness/agent-sdk-manager';
import { LegacyAgentEngineAdapter } from '../src/lib/harness/engine-registry';

export const CONTROLLED_CI_PURPOSE = 'chirality-controlled-ci-runtime/v1';

export type ControlledCiRuntimeOptions = {
  purpose: typeof CONTROLLED_CI_PURPOSE;
  runtimeDirectory: string;
  socketPath: string;
  instructionRoot: string;
};

export async function startControlledCiRuntime(options: ControlledCiRuntimeOptions) {
  if (options.purpose !== CONTROLLED_CI_PURPOSE) {
    throw new Error('The controlled Runtime entry is available only for the declared CI test purpose.');
  }
  for (const [label, value] of Object.entries({
    runtimeDirectory: options.runtimeDirectory,
    socketPath: options.socketPath,
    instructionRoot: options.instructionRoot
  })) {
    if (!path.isAbsolute(value)) throw new Error(`${label} must be an absolute path.`);
  }

  const projects = new ProjectRegistry(options.runtimeDirectory, {
    CHIRALITY_INSTRUCTION_ROOT: options.instructionRoot
  });
  const sessions = new SessionStore(options.runtimeDirectory, projects);
  const engines = new EngineRegistry();
  engines.register(new LegacyAgentEngineAdapter({
    adapterId: 'stub',
    providerId: 'stub',
    capabilities: {
      credentials: false,
      tools: false,
      attachments: true,
      interruption: true,
      durableResume: false,
      compaction: false,
      runtimeControlTools: false
    }
  }, new StubAgentSdkManager()));
  const control: OmlxControlPort = {
    async listStatus() { return []; },
    async load() { throw new RuntimeError('ENGINE_UNAVAILABLE', 'Controlled CI runtime has no model control.', 503); },
    async unload() { throw new RuntimeError('ENGINE_UNAVAILABLE', 'Controlled CI runtime has no model control.', 503); }
  };
  const residency = new ResidencyCoordinator(control, options.runtimeDirectory);
  const auth = new AuthRegistry(options.runtimeDirectory);
  const turns = new TurnCoordinator(projects, sessions, engines, residency);
  const service = new RuntimeService(
    projects,
    sessions,
    engines,
    residency,
    turns,
    auth,
    {
      async get() { return undefined; },
      async status() { return { configured: false }; },
      async set() { throw new RuntimeError('ENGINE_UNAVAILABLE', 'Controlled CI runtime cannot configure credentials.', 503); },
      async remove() { throw new RuntimeError('ENGINE_UNAVAILABLE', 'Controlled CI runtime cannot configure credentials.', 503); }
    },
    undefined,
    undefined,
    undefined,
    {
      async resolve(input) {
        return {
          role: input.agentType === 0 ? 'agent0' as const : 'agent1' as const,
          engineSelection: { adapterId: 'stub', providerId: 'stub', model: 'controlled-ci' }
        };
      }
    }
  );
  const daemon = new RuntimeDaemon({
    runtimeDirectory: options.runtimeDirectory,
    socketPath: options.socketPath,
    service
  });
  const started = await daemon.start();
  return { ...started, daemon, stop: () => daemon.stop() };
}

function requiredAbsoluteEnvironment(name: string): string {
  const value = process.env[name];
  if (!value || !path.isAbsolute(value)) throw new Error(`${name} must be an absolute path.`);
  return value;
}

async function main(): Promise<void> {
  if (process.env.CHIRALITY_CONTROLLED_CI_RUNTIME !== CONTROLLED_CI_PURPOSE) {
    throw new Error(`CHIRALITY_CONTROLLED_CI_RUNTIME must equal ${CONTROLLED_CI_PURPOSE}.`);
  }
  const host = await startControlledCiRuntime({
    purpose: CONTROLLED_CI_PURPOSE,
    runtimeDirectory: requiredAbsoluteEnvironment('CHIRALITY_RUNTIME_DIRECTORY'),
    socketPath: requiredAbsoluteEnvironment('CHIRALITY_RUNTIME_SOCKET_PATH'),
    instructionRoot: requiredAbsoluteEnvironment('CHIRALITY_INSTRUCTION_ROOT')
  });
  process.stdout.write(`${JSON.stringify({
    status: 'ready',
    purpose: CONTROLLED_CI_PURPOSE,
    socketPath: host.socketPath,
    operatorTokenFile: host.operatorTokenFile
  })}\n`);

  let stopping = false;
  const stop = (): void => {
    if (stopping) return;
    stopping = true;
    void host.stop().then(() => process.exit(0), (error) => {
      process.stderr.write(`${error instanceof Error ? error.stack ?? error.message : String(error)}\n`);
      process.exit(1);
    });
  };
  process.once('SIGINT', stop);
  process.once('SIGTERM', stop);
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  await main();
}
