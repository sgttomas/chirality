import { mkdir, mkdtemp, realpath, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import type { AgentEnginePort, OmlxControlPort, UIEvent } from '@chirality/runtime-contracts';
import {
  createPiOmlxEngineAdapter,
  PI_CODING_AGENT_PACKAGE_NAME,
  PI_CODING_AGENT_PACKAGE_VERSION
} from '@chirality/engine-pi-omlx';
import {
  AuthRegistry,
  EngineRegistry,
  ProjectRegistry,
  ResidencyCoordinator,
  RuntimeService,
  SessionStore,
  TurnCoordinator
} from '@chirality/runtime-core';
import { RuntimeClient } from '@chirality/runtime-client';
import { RuntimeDaemon } from '@chirality/runtime-daemon';
import { PiAgentEngineAdapter } from '../../lib/harness/pi-agent-engine-adapter';
import { createBoundedReadToolDefinitions } from '../../lib/harness/chirality-tool-bridge';
import { bindChiralityToolsForPi } from '../../lib/harness/pi-tool-binder';
import {
  requireOmlxModel,
  resolveOmlxProviderConfig
} from '../../lib/harness/omlx-provider-config';
import { RuntimeDaemonHarnessPort } from '../../lib/runtime-client/runtime-daemon-harness-port';
import { resolvePackagedDaemonInstructionRoot } from '../../../electron/daemon-instruction-root';
import {
  startFakeOpenAiLoopback,
  type FakeOpenAiLoopback
} from './fake-openai-loopback';

const activeDaemons: RuntimeDaemon[] = [];
const tempRoots: string[] = [];
const providers: FakeOpenAiLoopback[] = [];
let previousSessionRoot: string | undefined;
let sessionRootOverridden = false;

afterEach(async () => {
  await Promise.all(
    activeDaemons.splice(0).map(async (daemon) => daemon.stop().catch(() => undefined))
  );
  await Promise.all(providers.splice(0).map(async (provider) => provider.close()));
  await Promise.all(
    tempRoots.splice(0).map(async (root) => rm(root, { recursive: true, force: true }))
  );
  if (sessionRootOverridden) {
    if (previousSessionRoot === undefined) delete process.env.CHIRALITY_SESSION_ROOT;
    else process.env.CHIRALITY_SESSION_ROOT = previousSessionRoot;
    sessionRootOverridden = false;
  }
});

async function collect(source: AsyncIterable<UIEvent>): Promise<UIEvent[]> {
  const events: UIEvent[] = [];
  try {
    for await (const event of source) {
      events.push(event);
      // Drain the public SSE stream so cancellation and terminal persistence settle.
    }
  } catch {
    // Cancellation may reject the client stream after yielding attributed events.
  }
  return events;
}

async function createProjectFixture(root: string, instructionRoot = '.'): Promise<string> {
  const resolvedInstructionRoot = join(root, instructionRoot);
  await mkdir(join(resolvedInstructionRoot, 'agents'), { recursive: true });
  await mkdir(join(root, 'execution'), { recursive: true });
  await mkdir(join(root, 'legacy-sessions'), { recursive: true });
  await writeFile(
    join(resolvedInstructionRoot, 'agents', 'AGENT_HELP_HUMAN.md'),
    '[[DOC:AGENT_INSTRUCTIONS]]\n# HELP_HUMAN\nAGENT_TYPE: 0\nAGENT_CLASS: SUPERVISING\n',
    'utf8'
  );
  const manifestPath = join(root, 'chirality.project.json');
  await writeFile(
    manifestPath,
    `${JSON.stringify(
      {
        schemaVersion: 'chirality.project/v1',
        projectId: 'chirality-app-dev',
        displayName: 'Chirality App Dev Fixture',
        workingRoot: '.',
        instructionRoot,
        agentsOverlay: join(instructionRoot, 'agents', 'AGENT_HELP_HUMAN.md'),
        defaultExecutionRoot: 'execution',
        profiles: { domain: [], capability: [], dataBoundary: [] },
        enabledAdapterIds: ['pi'],
        embeddedUi: { declared: false },
        legacySessionRoots: ['legacy-sessions']
      },
      null,
      2
    )}\n`,
    'utf8'
  );
  return manifestPath;
}

async function createRuntime(
  root: string,
  engine?: AgentEnginePort,
  model = 'fixture-model',
  controlOverride?: OmlxControlPort,
  activateModel = true
) {
  const runtimeDirectory = join(root, 'runtime');
  const projects = new ProjectRegistry(runtimeDirectory);
  const sessions = new SessionStore(runtimeDirectory, projects);
  const engines = new EngineRegistry();
  const control: OmlxControlPort = controlOverride ?? {
    async listStatus() {
      return [{ id: model, kind: 'llm' as const, loaded: true, loading: false }];
    },
    async load() {},
    async unload() {}
  };
  const residency = new ResidencyCoordinator(control, runtimeDirectory);
  const auth = new AuthRegistry(runtimeDirectory);
  const credentials = {
    async get() {
      return undefined;
    },
    async status() {
      return { configured: false };
    },
    async set() {},
    async remove() {}
  };
  const turns = new TurnCoordinator(projects, sessions, engines, residency);
  if (engine) {
    engines.register(engine);
    if (activateModel) {
      await residency.activate(model, 'D-APP-85-C04-C16');
    }
  }
  const service = new RuntimeService(
    projects,
    sessions,
    engines,
    residency,
    turns,
    auth,
    credentials,
    undefined,
    undefined,
    undefined,
    {
      async resolve() {
        return {
          role: 'agent0' as const,
          engineSelection: { adapterId: 'pi', providerId: 'omlx', model }
        };
      }
    }
  );
  return { runtimeDirectory, service, projects };
}

function createPiAdapter(input: {
  provider: FakeOpenAiLoopback;
  apiKey: string;
  projectRoot: string;
  model: string;
}): AgentEnginePort {
  const runtime = new PiAgentEngineAdapter({
    turnTimeoutMs: 5_000,
    resolveProvider: async (runInput) => {
      const config = resolveOmlxProviderConfig({
        baseUrl: input.provider.baseUrl,
        apiKey: input.apiKey
      });
      await requireOmlxModel(runInput.opts.model, config);
      return {
        ...config,
        model: { id: runInput.opts.model, contextWindow: 32768, maxTokens: 4096 }
      };
    },
    buildSystemPrompt: async () => 'Use only read_file for the sealed task.',
    resolveCustomTools: async (runInput) =>
      bindChiralityToolsForPi(
        createBoundedReadToolDefinitions({
          context: {
            projectRoot: input.projectRoot,
            sessionId: runInput.session.sessionId,
            turnId: runInput.turnId,
            mode: 'readOnly',
            allowedReadScopes: [input.projectRoot],
            allowedWriteTargets: []
          },
          allowedToolNames: ['read_file']
        })
      )
  });
  return createPiOmlxEngineAdapter({
    credentials: {
      async get(providerId) {
        return providerId === 'omlx' ? input.apiKey : undefined;
      },
      async status(providerId) {
        return { configured: providerId === 'omlx' };
      }
    },
    runtime: {
      preflight: (runInput) => runtime.preflight(runInput),
      startTurn: (runInput) => runtime.startTurn(runInput),
      interrupt: (sessionId) => runtime.interrupt(sessionId)
    },
    transcriptRootFor: (sessionId) => join(input.projectRoot, 'adapter-events', sessionId),
    isExactlyResident: async (modelId) => modelId === input.model
  });
}

describe('Desktop and CLI shared runtime daemon', () => {
  it('shares one daemon, project credential, and session across both public clients', async () => {
    const root = await mkdtemp(join(tmpdir(), 'chirality-desktop-cli-'));
    tempRoots.push(root);
    const { runtimeDirectory, service, projects } = await createRuntime(root);
    const socketPath = join(runtimeDirectory, 'control.sock');
    const daemon = new RuntimeDaemon({ runtimeDirectory, socketPath, service });
    activeDaemons.push(daemon);
    await daemon.start();
    const competingDaemon = new RuntimeDaemon({ runtimeDirectory, socketPath, service });
    await expect(competingDaemon.start()).rejects.toMatchObject({
      code: 'RESIDENCY_TRANSITION_IN_PROGRESS'
    });

    const projectRoot = join(root, 'chirality-app-dev');
    const manifestPath = await createProjectFixture(projectRoot, '..');
    const registration = await service.registerProject(manifestPath, 'test', 'D-APP-85-C04-C16');
    const canonicalProjectRoot = await realpath(projectRoot);
    const canonicalInstructionRoot = await realpath(root);

    const desktopClient = new RuntimeClient({
      socketPath,
      tokenFile: registration.tokenFile
    });
    const cliClient = new RuntimeClient({
      socketPath,
      tokenFile: registration.tokenFile
    });
    const desktop = new RuntimeDaemonHarnessPort(
      desktopClient,
      'chirality-app-dev',
      canonicalProjectRoot
    );

    const [desktopDaemon, cliDaemon] = await Promise.all([
      desktopClient.daemonStatus(),
      cliClient.daemonStatus()
    ]);
    expect(desktopDaemon).toEqual(cliDaemon);
    expect(desktopDaemon.socketPath).toBe(socketPath);

    const [desktopProject, cliProject] = await Promise.all([
      desktopClient.projectStatus('chirality-app-dev'),
      cliClient.projectStatus('chirality-app-dev')
    ]);
    expect(desktopProject).toEqual(cliProject);
    expect(desktopProject.project.projectId).toBe('chirality-app-dev');

    const packagedResourcesPath = join(root, 'packaged-resources');
    const daemonInstructionRoot = await resolvePackagedDaemonInstructionRoot({
      projectId: 'chirality-app-dev',
      packagedResourcesPath,
      resolveProjectRoots: (projectId) => projects.roots(projectId)
    });
    expect(daemonInstructionRoot).toEqual({
      instructionRoot: canonicalInstructionRoot,
      source: 'registered-project-manifest'
    });
    expect(daemonInstructionRoot.instructionRoot).not.toBe(packagedResourcesPath);

    const created = await desktop.createSession({
      projectRoot: canonicalProjectRoot,
      persona: 'HELP_HUMAN',
      mode: 'direct'
    });
    const [desktopSession, cliSession] = await Promise.all([
      desktop.getSession(created.session.sessionId),
      cliClient.getSession('chirality-app-dev', created.session.sessionId)
    ]);
    expect(desktopSession.session).toEqual(cliSession);
    await expect(cliClient.listSessions('chirality-app-dev')).resolves.toEqual([cliSession]);
  });

  it('persists exactly one terminal outcome when daemon restart interrupts an in-flight model drain', async () => {
    const root = await mkdtemp(join(tmpdir(), 'ch-md-'));
    tempRoots.push(root);
    const projectRoot = join(root, 'chirality-app-dev');
    const manifestPath = await createProjectFixture(projectRoot);
    const currentModel = 'model-drain-current';
    const replacementModel = 'model-drain-replacement';
    const loadedModels = new Set([currentModel]);
    const residencyCalls: string[] = [];
    const control: OmlxControlPort = {
      async listStatus() {
        return [currentModel, replacementModel].map((id) => ({
          id,
          kind: 'llm' as const,
          loaded: loadedModels.has(id),
          loading: false
        }));
      },
      async unload(modelId) {
        residencyCalls.push(`unload:${modelId}`);
        loadedModels.delete(modelId);
      },
      async load(modelId) {
        residencyCalls.push(`load:${modelId}`);
        loadedModels.add(modelId);
      }
    };
    let markEngineStarted!: () => void;
    let releaseEngine!: () => void;
    const engineStarted = new Promise<void>((resolve) => {
      markEngineStarted = resolve;
    });
    const engineReleased = new Promise<void>((resolve) => {
      releaseEngine = resolve;
    });
    let interrupts = 0;
    const engine: AgentEnginePort = {
      descriptor: {
        adapterId: 'pi',
        providerId: 'omlx',
        capabilities: {
          credentials: false,
          tools: false,
          attachments: false,
          interruption: true,
          durableResume: false,
          compaction: false
        }
      },
      subject: 'pi',
      async preflight() {},
      async *startTurn(input) {
        yield {
          type: 'session:init',
          data: {
            engineSessionId: `engine-${input.session.sessionId}`,
            adapterId: 'pi',
            providerId: 'omlx',
            model: input.opts.model
          }
        };
        markEngineStarted();
        await engineReleased;
      },
      async interrupt() {
        interrupts += 1;
        releaseEngine();
      }
    };
    const firstRuntime = await createRuntime(root, engine, currentModel, control);
    const registration = await firstRuntime.service.registerProject(
      manifestPath,
      'test',
      'D-APP-85-C04-C16'
    );
    const socketPath = join(firstRuntime.runtimeDirectory, 'control.sock');
    const firstDaemon = new RuntimeDaemon({
      runtimeDirectory: firstRuntime.runtimeDirectory,
      socketPath,
      service: firstRuntime.service
    });
    activeDaemons.push(firstDaemon);
    const firstDaemonStart = await firstDaemon.start();
    const projectClient = new RuntimeClient({
      socketPath,
      tokenFile: registration.tokenFile
    });
    const operatorClient = new RuntimeClient({
      socketPath,
      tokenFile: firstDaemonStart.operatorTokenFile
    });
    const session = await projectClient.createSession('chirality-app-dev', {
      projectId: 'chirality-app-dev',
      persona: 'HELP_HUMAN',
      mode: 'direct'
    });
    const turnId = 'model-drain-restart-turn';
    const turn = await projectClient.turnSession('chirality-app-dev', session.sessionId, {
      turnId,
      message: 'Hold model work in flight while residency drains.',
      opts: { model: currentModel, tools: [], maxTurns: 1, persona: 'HELP_HUMAN', mode: 'direct' }
    });
    const turnEvents = collect(turn).catch(() => undefined);
    await engineStarted;

    const activation = operatorClient.activateModel(
      replacementModel,
      'D-APP-85-C04-C16'
    );
    let draining = await projectClient.listModels();
    for (let attempt = 0; attempt < 100 && draining.phase !== 'DRAINING'; attempt += 1) {
      await new Promise((resolve) => setTimeout(resolve, 5));
      draining = await projectClient.listModels();
    }
    expect(draining).toMatchObject({
      phase: 'DRAINING',
      activeTurns: 1,
      acceptingLocalTurns: false,
      managedModelId: currentModel
    });

    await Promise.all([firstDaemon.stop(), activation, turnEvents]);
    expect(interrupts).toBe(1);
    expect(residencyCalls).toEqual([
      `unload:${currentModel}`,
      `load:${replacementModel}`
    ]);

    const restartedRuntime = await createRuntime(
      root,
      engine,
      replacementModel,
      control,
      false
    );
    const restartedDaemon = new RuntimeDaemon({
      runtimeDirectory: restartedRuntime.runtimeDirectory,
      socketPath,
      service: restartedRuntime.service
    });
    activeDaemons.push(restartedDaemon);
    await restartedDaemon.start();
    const restartedClient = new RuntimeClient({
      socketPath,
      tokenFile: registration.tokenFile
    });
    const replay = await restartedClient.replaySession(
      'chirality-app-dev',
      session.sessionId
    );
    const terminalTypes = new Set([
      'turn.completed',
      'turn.failed',
      'turn.cancelled',
      'turn.interrupted'
    ]);
    const acceptedForTurn = replay.events.filter(
      (event) => event.turnId === turnId && event.type === 'turn.accepted'
    );
    const terminalForTurn = replay.events.filter(
      (event) => event.turnId === turnId && terminalTypes.has(event.type)
    );

    expect(acceptedForTurn).toHaveLength(1);
    expect(terminalForTurn).toHaveLength(1);
    expect(terminalForTurn[0]?.type).toBe('turn.interrupted');
    expect(replay.session).toMatchObject({
      status: 'interrupted',
      engineSelection: { adapterId: 'pi', providerId: 'omlx', model: currentModel }
    });
    await expect(restartedClient.listModels()).resolves.toMatchObject({
      phase: 'READY',
      managedModelId: replacementModel,
      activeTurns: 0,
      acceptingLocalTurns: true
    });
  });

  it('rejects a CLI turn with the typed shared-session lock while Desktop is active', async () => {
    const root = await mkdtemp(join(tmpdir(), 'chirality-desktop-cli-lock-'));
    tempRoots.push(root);
    const projectRoot = join(root, 'chirality-app-dev');
    const manifestPath = await createProjectFixture(projectRoot);
    const canonicalProjectRoot = await realpath(projectRoot);
    previousSessionRoot = process.env.CHIRALITY_SESSION_ROOT;
    process.env.CHIRALITY_SESSION_ROOT = join(root, 'app-harness-sessions');
    sessionRootOverridden = true;
    const apiKey = 'desktop-cli-lock-key';
    const model = 'desktop-cli-lock-model';
    let providerStarted!: () => void;
    let secondProviderStarted!: () => void;
    let thirdProviderStarted!: () => void;
    const started = new Promise<void>((resolve) => {
      providerStarted = resolve;
    });
    const secondStarted = new Promise<void>((resolve) => {
      secondProviderStarted = resolve;
    });
    const thirdStarted = new Promise<void>((resolve) => {
      thirdProviderStarted = resolve;
    });
    const provider = await startFakeOpenAiLoopback({
      apiKey,
      models: { kind: 'json', body: { data: [{ id: model }] } },
      completions: [
        { kind: 'hang', started: providerStarted },
        { kind: 'hang', started: secondProviderStarted },
        { kind: 'hang', started: thirdProviderStarted }
      ]
    });
    providers.push(provider);
    const adapter = createPiAdapter({ provider, apiKey, projectRoot: canonicalProjectRoot, model });
    expect(adapter.descriptor).toMatchObject({
      adapterId: 'pi',
      providerId: 'omlx',
      packageName: PI_CODING_AGENT_PACKAGE_NAME,
      packageVersion: PI_CODING_AGENT_PACKAGE_VERSION
    });
    const { runtimeDirectory, service } = await createRuntime(root, adapter, model);
    const registration = await service.registerProject(manifestPath, 'test', 'D-APP-85-C04-C16');
    const session = await service.sessions.create({
      projectId: 'chirality-app-dev',
      role: 'agent2',
      engineSelection: { adapterId: 'pi', providerId: 'omlx', model },
      persona: 'TASK',
      mode: 'readOnly',
      parentSessionId: 'desktop-parent',
      approvalRef: 'D-APP-85-C04-C16',
      allowedWriteTargets: []
    });
    const socketPath = join(runtimeDirectory, 'control.sock');
    const daemon = new RuntimeDaemon({ runtimeDirectory, socketPath, service });
    activeDaemons.push(daemon);
    await daemon.start();
    const desktopClient = new RuntimeClient({ socketPath, tokenFile: registration.tokenFile });
    const cliClient = new RuntimeClient({ socketPath, tokenFile: registration.tokenFile });
    const desktop = new RuntimeDaemonHarnessPort(
      desktopClient,
      'chirality-app-dev',
      canonicalProjectRoot
    );

    const desktopTurn = await desktop.turn({
      sessionId: session.sessionId,
      message: 'Keep the shared Desktop turn active.',
      opts: { model, tools: ['read_file'], maxTurns: 1, persona: 'TASK', mode: 'readOnly' }
    });
    const desktopEvents = collect(desktopTurn.events).catch(() => undefined);
    await started;
    await expect(
      cliClient.turnSession('chirality-app-dev', session.sessionId, {
        message: 'Competing CLI turn.',
        opts: { model, tools: ['read_file'], maxTurns: 1, persona: 'TASK', mode: 'readOnly' }
      })
    ).rejects.toMatchObject({ code: 'SESSION_TURN_IN_PROGRESS' });
    await desktopTurn.cancel();
    const emittedDesktopEvents = await desktopEvents;
    expect(emittedDesktopEvents).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          type: 'session:init',
          data: expect.objectContaining({ adapterId: 'pi', providerId: 'omlx', model })
        })
      ])
    );

    let replay = await cliClient.replaySession('chirality-app-dev', session.sessionId);
    for (let attempt = 0; attempt < 100 && replay.session.status !== 'interrupted'; attempt += 1) {
      await new Promise((resolve) => setTimeout(resolve, 10));
      replay = await cliClient.replaySession('chirality-app-dev', session.sessionId);
    }
    const terminalTypes = new Set([
      'turn.completed',
      'turn.failed',
      'turn.cancelled',
      'turn.interrupted'
    ]);
    expect(replay.session.status).toBe('interrupted');
    expect(replay.events.filter((event) => terminalTypes.has(event.type))).toHaveLength(1);

    const secondSession = await service.sessions.create({
      projectId: 'chirality-app-dev',
      role: 'agent2',
      engineSelection: { adapterId: 'pi', providerId: 'omlx', model },
      persona: 'TASK',
      mode: 'readOnly',
      parentSessionId: 'desktop-parent',
      approvalRef: 'D-APP-85-C04-C16',
      allowedWriteTargets: []
    });
    const thirdSession = await service.sessions.create({
      projectId: 'chirality-app-dev',
      role: 'agent2',
      engineSelection: { adapterId: 'pi', providerId: 'omlx', model },
      persona: 'TASK',
      mode: 'readOnly',
      parentSessionId: 'cli-parent',
      approvalRef: 'D-APP-85-C04-C16',
      allowedWriteTargets: []
    });
    const secondDesktopTurn = await desktop.turn({
      sessionId: secondSession.sessionId,
      message: 'Keep the second Desktop session active.',
      opts: { model, tools: ['read_file'], maxTurns: 1, persona: 'TASK', mode: 'readOnly' }
    });
    const secondDesktopEvents = collect(secondDesktopTurn.events).catch(() => undefined);
    await secondStarted;
    const thirdCliTurn = await cliClient.turnSession('chirality-app-dev', thirdSession.sessionId, {
      message: 'Run the distinct CLI session concurrently.',
      opts: { model, tools: ['read_file'], maxTurns: 1, persona: 'TASK', mode: 'readOnly' }
    });
    const thirdCliEvents = collect(thirdCliTurn).catch(() => undefined);
    await thirdStarted;
    expect(provider.completionCount()).toBe(3);

    await secondDesktopTurn.cancel();
    thirdCliTurn.cancel();
    await cliClient.interruptSession('chirality-app-dev', thirdSession.sessionId);
    await Promise.all([secondDesktopEvents, thirdCliEvents]);
    for (const concurrentSession of [secondSession, thirdSession]) {
      let stored = await cliClient.getSession('chirality-app-dev', concurrentSession.sessionId);
      for (let attempt = 0; attempt < 100 && stored.status !== 'interrupted'; attempt += 1) {
        await new Promise((resolve) => setTimeout(resolve, 10));
        stored = await cliClient.getSession('chirality-app-dev', concurrentSession.sessionId);
      }
      expect(stored.status).toBe('interrupted');
    }
  });
});
