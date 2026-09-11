import { describe, expect, it, vi } from 'vitest';
import { mkdtemp, realpath, rm, symlink } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { tmpdir } from 'node:os';

import { RuntimeError, type RuntimeSessionRecord } from '@chirality/runtime-contracts';
import type { RuntimeClient, RuntimeStream } from '@chirality/runtime-client';
import type { UIEvent } from '@chirality/runtime-contracts/types';

import {
  RuntimeDaemonHarnessPort,
  RuntimeHostedBootstrapPort,
  createRuntimeDaemonHarnessPortFromEnvironment
} from '../../lib/runtime-client/runtime-daemon-harness-port';

const project = {
  projectId: 'chirality-app-dev',
  displayName: 'Chirality App Development',
  canonicalRoot: '/repo/projects/chirality-app-dev',
  manifestPath: '/repo/projects/chirality-app-dev/chirality.project.json',
  manifestHash: 'abc123',
  registeredAt: '2026-07-22T00:00:00.000Z',
  approval: {
    approvedBy: 'owner',
    approvalReference: 'D-APP-73'
  },
  clientId: 'desktop-chirality-app-dev',
  enabledAdapterIds: ['claude-agent-sdk', 'pi'],
  legacySessionRoots: ['frontend/.chirality/sessions']
} as const;

const session: RuntimeSessionRecord = {
  schemaVersion: 'chirality.session/v2',
  projectId: project.projectId,
  projectRoot: project.canonicalRoot,
  sessionId: 'sess-1',
  createdAt: '2026-07-22T00:00:00.000Z',
  updatedAt: '2026-07-22T00:00:00.000Z',
  role: 'agent1',
  persona: 'WORKING_ITEMS',
  mode: 'chat',
  engineSelection: {
    adapterId: 'claude-agent-sdk',
    providerId: 'anthropic',
    model: 'configured-by-daemon'
  },
  status: 'idle'
};

function client(overrides: Partial<RuntimeClient> = {}): RuntimeClient {
  return {
    resolveProjectByRoot: vi.fn().mockResolvedValue(project),
    createSession: vi.fn().mockResolvedValue(session),
    resolveSessionOwner: vi.fn().mockResolvedValue({ project, session }),
    listSessions: vi.fn().mockResolvedValue([session]),
    getSession: vi.fn().mockResolvedValue(session),
    deleteSession: vi.fn().mockResolvedValue({
      deleted: true,
      sessionId: session.sessionId
    }),
    requestJson: vi.fn(),
    bootSession: vi.fn(),
    replaySession: vi.fn(),
    turnSession: vi.fn(),
    interruptSession: vi.fn().mockResolvedValue({
      interrupted: true,
      sessionId: session.sessionId
    }),
    decidePermission: vi.fn().mockResolvedValue({
      accepted: true,
      requestId: 'tool-1',
      decision: 'allow'
    }),
    projectStatus: vi.fn().mockResolvedValue({
      project,
      manifestDrift: false,
      adaptersEnabled: true
    }),
    listProjects: vi.fn().mockResolvedValue([
      {
        project,
        manifestDrift: false,
        adaptersEnabled: true
      }
    ]),
    listRoles: vi.fn().mockResolvedValue({
      schemaVersion: 'chirality.roles/v3',
      defaultRole: 'HELP_HUMAN',
      roles: [
        { id: 'HELP_HUMAN', agentType: 0, directEntry: true, defaultForNewChat: true, description: 'help', instruction: 'agents/AGENT_HELP_HUMAN.md' },
        { id: 'WORKING_ITEMS', agentType: 1, directEntry: true, defaultForNewChat: false, description: 'work', instruction: 'agents/AGENT_WORKING_ITEMS.md' },
        { id: 'TASK', agentType: 2, directEntry: false, defaultForNewChat: false, description: 'task', instruction: 'agents/AGENT_TASK.md' }
      ]
    }),
    scaffold: vi.fn(),
    ...overrides
  } as unknown as RuntimeClient;
}

describe('RuntimeDaemonHarnessPort', () => {
  it('fails closed when the Desktop host omits daemon authentication paths', () => {
    expect(() => createRuntimeDaemonHarnessPortFromEnvironment({})).toThrowError(
      expect.objectContaining({
        type: 'ENGINE_UNAVAILABLE',
        status: 503
      })
    );
  });

  it('requires a fixed app-dev project ID and root in the Desktop environment', () => {
    expect(() =>
      createRuntimeDaemonHarnessPortFromEnvironment({
        CHIRALITY_RUNTIME_SOCKET_PATH: '/runtime/control.sock',
        CHIRALITY_RUNTIME_TOKEN_FILE: '/runtime/project.token',
        CHIRALITY_RUNTIME_PROJECT_ID: 'pec',
        CHIRALITY_RUNTIME_PROJECT_ROOT: project.canonicalRoot
      })
    ).toThrowError(expect.objectContaining({ type: 'ENGINE_UNAVAILABLE' }));

    expect(() =>
      createRuntimeDaemonHarnessPortFromEnvironment({
        CHIRALITY_RUNTIME_SOCKET_PATH: '/runtime/control.sock',
        CHIRALITY_RUNTIME_TOKEN_FILE: '/runtime/auth/tokens/operator.token',
        CHIRALITY_RUNTIME_PROJECT_ID: project.projectId,
        CHIRALITY_RUNTIME_PROJECT_ROOT: project.canonicalRoot
      })
    ).toThrowError(expect.objectContaining({ type: 'ENGINE_UNAVAILABLE' }));

    expect(() =>
      createRuntimeDaemonHarnessPortFromEnvironment({
        CHIRALITY_RUNTIME_SOCKET_PATH: '/runtime/control.sock',
        CHIRALITY_RUNTIME_TOKEN_FILE: '/runtime/project.token',
        CHIRALITY_RUNTIME_PROJECT_ID: project.projectId
      })
    ).toThrowError(expect.objectContaining({ type: 'ENGINE_UNAVAILABLE' }));

    expect(() =>
      createRuntimeDaemonHarnessPortFromEnvironment({
        CHIRALITY_RUNTIME_SOCKET_PATH: '/runtime/control.sock',
        CHIRALITY_RUNTIME_TOKEN_FILE: '/runtime/auth/tokens/project-app-dev.token',
        CHIRALITY_RUNTIME_PROJECT_ID: project.projectId,
        CHIRALITY_RUNTIME_PROJECT_ROOT: project.canonicalRoot
      })
    ).not.toThrow();
  });

  it('resolves the registered project and leaves engine defaults to the daemon', async () => {
    const runtimeClient = client();
    const port = new RuntimeDaemonHarnessPort(runtimeClient);

    await expect(
      port.createSession({
        projectRoot: project.canonicalRoot,
        persona: 'WORKING_ITEMS',
        mode: 'chat'
      })
    ).resolves.toEqual({ session });
    expect(runtimeClient.createSession).toHaveBeenCalledWith(
      project.projectId,
      {
        projectId: project.projectId,
        persona: 'WORKING_ITEMS',
        mode: 'chat'
      },
      undefined
    );
    expect(runtimeClient.resolveProjectByRoot).not.toHaveBeenCalled();
  });

  it('passes declared context and write-target tri-state through to Runtime session creation', async () => {
    const runtimeClient = client();
    const port = new RuntimeDaemonHarnessPort(runtimeClient);

    await port.createSession({
      projectRoot: project.canonicalRoot,
      persona: 'WORKING_ITEMS',
      declaredContext: [],
      allowedWriteTargets: []
    });
    expect(runtimeClient.createSession).toHaveBeenLastCalledWith(
      project.projectId,
      expect.objectContaining({
        declaredContext: [],
        allowedWriteTargets: []
      }),
      undefined
    );

    const declaredContext = [`${project.canonicalRoot}/execution/PKG-01`];
    const allowedWriteTargets = [`${project.canonicalRoot}/execution/PKG-01/output.md`];
    await port.createSession({
      projectRoot: project.canonicalRoot,
      persona: 'WORKING_ITEMS',
      declaredContext,
      allowedWriteTargets
    });
    expect(runtimeClient.createSession).toHaveBeenLastCalledWith(
      project.projectId,
      expect.objectContaining({ declaredContext, allowedWriteTargets }),
      undefined
    );

    await port.createSession({
      projectRoot: project.canonicalRoot,
      persona: 'WORKING_ITEMS'
    });
    const finalRequest = vi.mocked(runtimeClient.createSession).mock.calls.at(-1)?.[1];
    expect(finalRequest).not.toHaveProperty('declaredContext');
    expect(finalRequest).not.toHaveProperty('allowedWriteTargets');
  });

  it('forwards the session-fixed modelSelection to Runtime createSession and keeps reasoningEffort on returned records', async () => {
    const created: RuntimeSessionRecord = {
      ...session,
      engineSelection: { adapterId: 'codex-app-server', providerId: 'openai', model: 'gpt-alt' },
      reasoningEffort: 'low'
    };
    const runtimeClient = client({
      createSession: vi.fn().mockResolvedValue(created),
      replaySession: vi.fn().mockResolvedValue({ session: created, events: [], malformedLineCount: 0 })
    });
    const port = new RuntimeDaemonHarnessPort(runtimeClient);

    const modelSelection = { model: 'gpt-alt', reasoningEffort: 'low' };
    await expect(port.createSession({
      projectRoot: project.canonicalRoot,
      persona: 'WORKING_ITEMS',
      roleId: 'WORKING_ITEMS',
      mode: 'chat',
      modelSelection
    })).resolves.toEqual({ session: created });
    expect(runtimeClient.createSession).toHaveBeenLastCalledWith(
      project.projectId,
      {
        projectId: project.projectId,
        roleId: 'WORKING_ITEMS',
        persona: 'WORKING_ITEMS',
        mode: 'chat',
        modelSelection
      },
      undefined
    );

    await port.createSession({ projectRoot: project.canonicalRoot, persona: 'WORKING_ITEMS' });
    expect(vi.mocked(runtimeClient.createSession).mock.calls.at(-1)?.[1]).not.toHaveProperty('modelSelection');

    // Replay keeps the additive field: the App renders it in the lens.
    await expect(port.replaySession('sess-1')).resolves.toMatchObject({
      session: { engineSelection: { model: 'gpt-alt' }, reasoningEffort: 'low' }
    });
  });

  it('maps legacy dontAsk creation to canonical readOnly unless permissionMode is explicit', async () => {
    const runtimeClient = client();
    const port = new RuntimeDaemonHarnessPort(runtimeClient);

    await port.createSession({
      projectRoot: project.canonicalRoot,
      persona: 'HELP_HUMAN',
      mode: 'dontAsk'
    });
    expect(runtimeClient.createSession).toHaveBeenLastCalledWith(
      project.projectId,
      expect.objectContaining({ mode: 'dontAsk', permissionMode: 'readOnly' }),
      undefined
    );

    await port.createSession({
      projectRoot: project.canonicalRoot,
      persona: 'HELP_HUMAN',
      mode: 'dontAsk',
      permissionMode: 'bypass'
    });
    expect(runtimeClient.createSession).toHaveBeenLastCalledWith(
      project.projectId,
      expect.objectContaining({ mode: 'dontAsk', permissionMode: 'bypass' }),
      undefined
    );
  });

  it('preserves canonical UI events and interrupts the owned session on cancel', async () => {
    const event: UIEvent = {
      type: 'chat:delta',
      data: { text: 'local evidence' }
    };
    const cancel = vi.fn();
    const stream: RuntimeStream = {
      async *[Symbol.asyncIterator]() {
        yield event;
      },
      cancel
    };
    const runtimeClient = client({
      turnSession: vi.fn().mockResolvedValue(stream)
    });
    const port = new RuntimeDaemonHarnessPort(runtimeClient);
    const running = await port.turn({
      sessionId: session.sessionId,
      message: 'inspect',
      opts: { tools: ['read_file'] },
      attachments: ['/repo/fixture.txt']
    });

    const received: UIEvent[] = [];
    for await (const item of running.events) received.push(item);
    expect(received).toEqual([event]);
    expect(runtimeClient.turnSession).toHaveBeenCalledWith(
      project.projectId,
      session.sessionId,
      {
        message: 'inspect',
        opts: { tools: ['read_file'] },
        attachments: ['/repo/fixture.txt']
      },
      undefined
    );

    await running.cancel();
    expect(cancel).toHaveBeenCalledOnce();
    expect(runtimeClient.interruptSession).toHaveBeenCalledWith(
      project.projectId,
      session.sessionId
    );
  });

  it('maps permission IDs and filters Type-2 agents from direct chat', async () => {
    const runtimeClient = client();
    const port = new RuntimeDaemonHarnessPort(runtimeClient);

    await expect(
      port.decidePermission({
        sessionId: session.sessionId,
        toolUseId: 'tool-1',
        verdict: 'allow'
      })
    ).resolves.toEqual({ ok: true, decided: true });
    expect(runtimeClient.decidePermission).toHaveBeenCalledWith(
      project.projectId,
      session.sessionId,
      {
        requestId: 'tool-1',
        decision: 'allow'
      },
      undefined
    );

    await expect(port.listAgents({ directChatOnly: true })).resolves.toEqual({
      agents: [
        { name: 'HELP_HUMAN', type: 0, class: 'PERSONA' },
        { name: 'WORKING_ITEMS', type: 1, class: 'PERSONA' }
      ]
    });
  });

  it('passes native Plan clarification reads and replies through the fixed project binding', async () => {
    const clarificationResponse = {
      schemaVersion: 'chirality.native-plan-clarifications/v3' as const,
      status: 'qualified' as const,
      qualification: {
        adapterId: 'codex-app-server',
        providerId: 'openai',
        qualificationId: 'native-plan-v3',
        admissionSha256: 'a'.repeat(64),
        evidenceClass: 'native-adapter-qualified' as const
      },
      clarifications: [{
        clientTurnId: 'client-turn-1',
        providerThreadId: 'thread-1',
        providerTurnId: 'turn-1',
        requestId: 17,
        itemId: 'item-1',
        questions: [{
          id: 'scope',
          header: 'Scope',
          question: 'Which scope?',
          options: [{ label: 'Current', description: 'Use the current scope.' }],
          isOther: true,
          isSecret: false
        }],
        isBlocking: true,
        autoResolutionMs: null
      }]
    };
    const replyResponse = {
      schemaVersion: 'chirality.native-plan-clarification-reply/v3' as const,
      sessionId: session.sessionId,
      requestId: 17,
      sent: true as const
    };
    const listNativePlanClarifications = vi.fn().mockResolvedValue(clarificationResponse);
    const replyNativePlanClarification = vi.fn().mockResolvedValue(replyResponse);
    const runtimeClient = client({
      listNativePlanClarifications,
      replyNativePlanClarification
    });
    const port = new RuntimeDaemonHarnessPort(
      runtimeClient,
      project.projectId,
      project.canonicalRoot
    );
    const abortController = new AbortController();

    await expect(
      port.listNativePlanClarifications(session.sessionId, {
        signal: abortController.signal
      })
    ).resolves.toEqual(clarificationResponse);
    expect(listNativePlanClarifications).toHaveBeenCalledWith(
      project.projectId,
      session.sessionId,
      abortController.signal
    );

    const answers = { scope: { answers: ['Current'] } };
    await expect(
      port.replyNativePlanClarification(
        session.sessionId,
        17,
        answers,
        { signal: abortController.signal }
      )
    ).resolves.toEqual(replyResponse);
    expect(replyNativePlanClarification).toHaveBeenCalledWith(
      project.projectId,
      session.sessionId,
      { requestId: 17, answers },
      abortController.signal
    );
    expect(runtimeClient.projectStatus).toHaveBeenCalledTimes(2);
  });

  it('keeps restart binding and hosted status read-only when the selected folder is unregistered', async () => {
    const projectRoot = await realpath(process.cwd());
    const initializeHostedBootstrapProject = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({
        resolveProjectByRoot: vi.fn().mockRejectedValue(
          new RuntimeError('PROJECT_NOT_FOUND', 'not registered', 404)
        ),
        initializeHostedBootstrapProject
      }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock'
    });

    await expect(port.bindProject(projectRoot)).resolves.toEqual({
      registration: 'required'
    });
    await expect(port.getStatus(projectRoot)).resolves.toEqual({ registration: 'required' });
    expect(initializeHostedBootstrapProject).not.toHaveBeenCalled();
  });

  it('rehydrates an existing project binding without consulting hosted account status', async () => {
    const projectRoot = await realpath(process.cwd());
    const registered = {
      ...project,
      projectId: 'restart-project',
      canonicalRoot: projectRoot,
      manifestPath: join(projectRoot, 'chirality.project.json'),
      manifestHash: 'restart-manifest',
      clientId: 'hosted-project-restart-project'
    };
    const healthy = { project: registered, manifestDrift: false, adaptersEnabled: true };
    const hostedBootstrapStatus = vi.fn();
    const scopedClient = client({
      projectStatus: vi.fn().mockResolvedValue(healthy),
      hostedBootstrapStatus
    });
    const installBoundPort = vi.fn();
    const bootstrapClient = client({
      resolveProjectByRoot: vi.fn().mockResolvedValue(registered),
      projectStatus: vi.fn().mockResolvedValue(healthy)
    });
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient,
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: () => scopedClient,
      installBoundPort
    });

    await expect(port.bindProject(projectRoot)).resolves.toEqual({
      registration: 'registered',
      projectId: registered.projectId
    });
    expect(bootstrapClient.resolveProjectByRoot).toHaveBeenCalledWith(projectRoot, undefined);
    expect(installBoundPort).toHaveBeenCalledWith(
      expect.any(RuntimeDaemonHarnessPort),
      { projectId: registered.projectId, projectRoot },
      false
    );
    expect(scopedClient.projectStatus).toHaveBeenCalledOnce();
    expect(hostedBootstrapStatus).not.toHaveBeenCalled();
  });

  it('does not install a restart binding when the registered project has drifted', async () => {
    const projectRoot = await realpath(process.cwd());
    const registered = {
      ...project,
      projectId: 'drifted-restart-project',
      canonicalRoot: projectRoot,
      manifestPath: join(projectRoot, 'chirality.project.json'),
      clientId: 'hosted-project-drifted-restart-project'
    };
    const installBoundPort = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({
        resolveProjectByRoot: vi.fn().mockResolvedValue(registered),
        projectStatus: vi.fn().mockResolvedValue({
          project: registered,
          manifestDrift: true,
          adaptersEnabled: true
        })
      }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: vi.fn(),
      installBoundPort
    });

    await expect(port.bindProject(projectRoot)).rejects.toMatchObject({
      type: 'WORKING_ROOT_CONFLICT',
      status: 409
    });
    expect(installBoundPort).not.toHaveBeenCalled();
  });

  it('initializes explicitly, verifies both principals, and installs an arbitrary project binding', async () => {
    const projectRoot = await realpath(process.cwd());
    const registered = {
      ...project,
      projectId: 'user-project',
      canonicalRoot: projectRoot,
      manifestPath: join(projectRoot, 'chirality.project.json'),
      manifestHash: 'hosted-manifest',
      clientId: 'hosted-project-user-project'
    };
    const registration = {
      projectId: registered.projectId,
      manifestHash: registered.manifestHash
    };
    // The ordinary scoped client carries no account-host proof; a real daemon
    // with an account host rejects this read with 401. The port must never
    // reach it on any App path.
    const hostedBootstrapStatus = vi.fn().mockRejectedValue(
      new RuntimeError('UNAUTHORIZED', 'Complete App account host proof is required', 401)
    );
    const bootstrapClient = client({
      initializeHostedBootstrapProject: vi.fn().mockResolvedValue(registration),
      hostedBootstrapStatus,
      projectStatus: vi.fn().mockResolvedValue({
        project: registered,
        manifestDrift: false,
        adaptersEnabled: true
      })
    });
    const scopedClient = client({
      projectStatus: vi.fn().mockResolvedValue({
        project: registered,
        manifestDrift: false,
        adaptersEnabled: true
      }),
      hostedBootstrapStatus
    });
    const createScopedClient = vi.fn().mockReturnValue(scopedClient);
    const installBoundPort = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient,
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient,
      installBoundPort
    });

    const initialized = await port.initializeProject(projectRoot);
    expect(initialized).toEqual({
      registration: 'registered',
      projectId: registered.projectId
    });
    expect(initialized).not.toHaveProperty('status');
    await expect(port.getStatus(projectRoot)).resolves.toEqual({
      registration: 'registered',
      projectId: registered.projectId
    });
    await expect(port.bindProject(projectRoot)).resolves.toEqual({
      registration: 'registered',
      projectId: registered.projectId
    });
    expect(hostedBootstrapStatus).not.toHaveBeenCalled();
    expect(bootstrapClient.initializeHostedBootstrapProject).toHaveBeenCalledWith(
      { projectRoot },
      undefined
    );
    expect(createScopedClient).toHaveBeenCalledWith({
      socketPath: '/runtime/control.sock',
      tokenFile: '/runtime/auth/tokens/hosted-project-user-project.token'
    });
    expect(installBoundPort).toHaveBeenCalledWith(
      expect.any(RuntimeDaemonHarnessPort),
      { projectId: registered.projectId, projectRoot },
      true
    );

    await expect(port.getStatus(dirname(projectRoot))).rejects.toMatchObject({
      type: 'WORKING_ROOT_CONFLICT',
      status: 409
    });
    expect(installBoundPort).toHaveBeenCalledOnce();
  });

  it('rejects a late project initialization before it can replace the newer binding', async () => {
    const temporaryA = await mkdtemp(join(tmpdir(), 'chirality-hosted-a-'));
    const temporaryB = await mkdtemp(join(tmpdir(), 'chirality-hosted-b-'));
    const rootA = await realpath(temporaryA);
    const rootB = await realpath(temporaryB);
    let resolveA!: (value: { projectId: string; manifestHash: string }) => void;
    let resolveB!: (value: { projectId: string; manifestHash: string }) => void;
    const initializationA = new Promise<{ projectId: string; manifestHash: string }>(resolve => { resolveA = resolve; });
    const initializationB = new Promise<{ projectId: string; manifestHash: string }>(resolve => { resolveB = resolve; });
    const projects = new Map([
      ['project-a', { ...project, projectId: 'project-a', canonicalRoot: rootA, manifestPath: join(rootA, 'chirality.project.json'), manifestHash: 'manifest-a', clientId: 'hosted-project-project-a' }],
      ['project-b', { ...project, projectId: 'project-b', canonicalRoot: rootB, manifestPath: join(rootB, 'chirality.project.json'), manifestHash: 'manifest-b', clientId: 'hosted-project-project-b' }]
    ]);
    const bootstrapClient = client({
      initializeHostedBootstrapProject: vi.fn().mockImplementation(({ projectRoot }: { projectRoot: string }) => projectRoot === rootA ? initializationA : initializationB),
      projectStatus: vi.fn().mockImplementation((projectId: string) => Promise.resolve({ project: projects.get(projectId)!, manifestDrift: false, adaptersEnabled: true }))
    });
    const scopedClients = new Map([...projects].map(([projectId, registered]) => [projectId, client({
      projectStatus: vi.fn().mockResolvedValue({ project: registered, manifestDrift: false, adaptersEnabled: true }),
      hostedBootstrapStatus: vi.fn()
    })]));
    const installBoundPort = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient,
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: ({ tokenFile }) => scopedClients.get(tokenFile.includes('project-a') ? 'project-a' : 'project-b')!,
      installBoundPort
    });

    try {
      const requestA = port.initializeProject(rootA);
      const requestB = port.initializeProject(rootB);
      resolveB({ projectId: 'project-b', manifestHash: 'manifest-b' });
      await expect(requestB).resolves.toEqual({ registration: 'registered', projectId: 'project-b' });
      resolveA({ projectId: 'project-a', manifestHash: 'manifest-a' });
      await expect(requestA).rejects.toMatchObject({ type: 'WORKING_ROOT_CONFLICT', status: 409 });
      expect(installBoundPort).toHaveBeenCalledTimes(1);
      expect(installBoundPort).toHaveBeenCalledWith(expect.any(RuntimeDaemonHarnessPort), { projectId: 'project-b', projectRoot: rootB }, true);
      await expect(port.getStatus(rootB)).resolves.toEqual({ registration: 'registered', projectId: 'project-b' });
      for (const scoped of scopedClients.values()) expect(scoped.hostedBootstrapStatus).not.toHaveBeenCalled();
    } finally {
      await rm(temporaryA, { recursive: true, force: true });
      await rm(temporaryB, { recursive: true, force: true });
    }
  });

  it('lets a newer explicit selection commit while a consent mutation finishes on the captured old binding', async () => {
    const temporaryA = await mkdtemp(join(tmpdir(), 'chirality-hosted-selected-a-'));
    const temporaryB = await mkdtemp(join(tmpdir(), 'chirality-hosted-selected-b-'));
    const rootA = await realpath(temporaryA);
    const rootB = await realpath(temporaryB);
    const registeredA = { ...project, projectId: 'selected-a', canonicalRoot: rootA, manifestPath: join(rootA, 'chirality.project.json'), manifestHash: 'selected-manifest-a', clientId: 'hosted-project-selected-a' };
    const registeredB = { ...project, projectId: 'selected-b', canonicalRoot: rootB, manifestPath: join(rootB, 'chirality.project.json'), manifestHash: 'selected-manifest-b', clientId: 'hosted-project-selected-b' };
    const registrationA = { projectId: 'selected-a', manifestHash: 'selected-manifest-a' };
    const registrationB = { projectId: 'selected-b', manifestHash: 'selected-manifest-b' };
    const consentA = { schema: 'chirality-hosted-bootstrap-status/v1' as const, projectId: 'selected-a', ceremony: 'ready-to-start' as const, admission: 'unavailable' as const, canStartLogin: true };
    let resolveB!: (value: typeof registrationB) => void;
    const pendingB = new Promise<typeof registrationB>(resolve => { resolveB = resolve; });
    const bootstrapClient = client({
      initializeHostedBootstrapProject: vi.fn().mockImplementation(({ projectRoot }: { projectRoot: string }) => projectRoot === rootA ? Promise.resolve(registrationA) : pendingB),
      projectStatus: vi.fn().mockImplementation((projectId: string) => Promise.resolve({ project: projectId === 'selected-a' ? registeredA : registeredB, manifestDrift: false, adaptersEnabled: true }))
    });
    const scopedA = client({
      projectStatus: vi.fn().mockResolvedValue({ project: registeredA, manifestDrift: false, adaptersEnabled: true }),
      hostedBootstrapStatus: vi.fn(),
      grantHostedProviderNetworkConsent: vi.fn().mockResolvedValue(consentA)
    });
    const scopedB = client({
      projectStatus: vi.fn().mockResolvedValue({ project: registeredB, manifestDrift: false, adaptersEnabled: true }),
      hostedBootstrapStatus: vi.fn()
    });
    const installBoundPort = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient,
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: ({ tokenFile }) => tokenFile.includes('selected-a') ? scopedA : scopedB,
      installBoundPort
    });

    try {
      await port.initializeProject(rootA);
      const selectionB = port.initializeProject(rootB);
      const lateBindingA = port.getStatus(rootA);
      const lateConsentA = port.grantProviderNetworkConsent(rootA);
      await expect(lateBindingA).resolves.toEqual({ registration: 'registered', projectId: 'selected-a' });
      await expect(lateConsentA).resolves.toEqual(consentA);
      resolveB(registrationB);
      await expect(selectionB).resolves.toEqual({ registration: 'registered', projectId: 'selected-b' });
      await expect(port.getStatus(rootB)).resolves.toEqual({ registration: 'registered', projectId: 'selected-b' });
      await expect(port.getStatus(rootA)).rejects.toMatchObject({ type: 'WORKING_ROOT_CONFLICT', status: 409 });
      expect(installBoundPort).toHaveBeenCalledTimes(2);
      expect(installBoundPort).toHaveBeenLastCalledWith(expect.any(RuntimeDaemonHarnessPort), { projectId: 'selected-b', projectRoot: rootB }, true);
      expect(scopedA.hostedBootstrapStatus).not.toHaveBeenCalled();
      expect(scopedB.hostedBootstrapStatus).not.toHaveBeenCalled();
    } finally {
      await rm(temporaryA, { recursive: true, force: true });
      await rm(temporaryB, { recursive: true, force: true });
    }
  });

  it('allows a verified normal daemon port to serve a non-app-dev project ID', async () => {
    const projectRoot = await realpath(process.cwd());
    const registered = {
      ...project,
      projectId: 'user-project',
      canonicalRoot: projectRoot
    };
    const listRoles = vi.fn().mockResolvedValue({
      schemaVersion: 'chirality.roles/v3',
      defaultRole: 'HELP_HUMAN',
      roles: []
    });
    const runtimeClient = client({
      projectStatus: vi.fn().mockResolvedValue({
        project: registered,
        manifestDrift: false,
        adaptersEnabled: true
      }),
      listRoles
    });
    const port = new RuntimeDaemonHarnessPort(
      runtimeClient,
      registered.projectId,
      projectRoot
    );

    await port.listRoles(projectRoot);
    expect(listRoles).toHaveBeenCalledWith(registered.projectId, undefined);
  });

  it('revalidates a cached hosted binding before a consent mutation', async () => {
    const projectRoot = await realpath(process.cwd());
    const registered = {
      ...project,
      projectId: 'drift-project',
      canonicalRoot: projectRoot,
      manifestHash: 'before',
      clientId: 'hosted-project-drift-project'
    };
    const healthy = {
      project: registered,
      manifestDrift: false,
      adaptersEnabled: true
    };
    const bootstrapProjectStatus = vi.fn().mockResolvedValue(healthy);
    const scopedProjectStatus = vi.fn().mockResolvedValue(healthy);
    const scopedClient = client({
      projectStatus: scopedProjectStatus,
      hostedBootstrapStatus: vi.fn(),
      grantHostedProviderNetworkConsent: vi.fn()
    });
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({
        resolveProjectByRoot: vi.fn().mockResolvedValue(registered),
        projectStatus: bootstrapProjectStatus
      }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: () => scopedClient
    });
    await port.getStatus(projectRoot);
    bootstrapProjectStatus.mockResolvedValueOnce({
      ...healthy,
      project: { ...registered, manifestHash: 'after' }
    });

    await expect(
      port.grantProviderNetworkConsent(projectRoot)
    ).rejects.toMatchObject({ type: 'WORKING_ROOT_CONFLICT', status: 409 });
    expect(scopedClient.grantHostedProviderNetworkConsent).not.toHaveBeenCalled();
    expect(scopedClient.hostedBootstrapStatus).not.toHaveBeenCalled();
  });

  it('revalidates and preserves the selected binding for project-local sign-out', async () => {
    const projectRoot = await realpath(process.cwd());
    const registered = {
      ...project,
      projectId: 'logout-project',
      canonicalRoot: projectRoot,
      manifestHash: 'logout-manifest',
      clientId: 'hosted-project-logout-project'
    };
    const healthy = { project: registered, manifestDrift: false, adaptersEnabled: true };
    const signedOut = {
      schema: 'chirality-hosted-bootstrap-status/v1' as const,
      projectId: registered.projectId,
      ceremony: 'consent-required' as const,
      admission: 'unavailable' as const,
      canStartLogin: false
    };
    const signOutHostedProject = vi.fn().mockResolvedValue(signedOut);
    const scopedClient = client({
      projectStatus: vi.fn().mockResolvedValue(healthy),
      hostedBootstrapStatus: vi.fn(),
      signOutHostedProject
    });
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({
        resolveProjectByRoot: vi.fn().mockResolvedValue(registered),
        projectStatus: vi.fn().mockResolvedValue(healthy)
      }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: () => scopedClient
    });
    await port.getStatus(projectRoot);
    const controller = new AbortController();
    await expect(port.signOut(projectRoot, { signal: controller.signal })).resolves.toEqual(signedOut);
    expect(signOutHostedProject).toHaveBeenCalledWith(registered.projectId, controller.signal);
    expect(scopedClient.hostedBootstrapStatus).not.toHaveBeenCalled();
  });

  it('rejects a symlink alias before explicit hosted project initialization', async () => {
    const fixtureRoot = await mkdtemp(join(tmpdir(), 'chirality-hosted-root-'));
    const alias = `${fixtureRoot}-alias`;
    await symlink(fixtureRoot, alias);
    const initializeHostedBootstrapProject = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({ initializeHostedBootstrapProject }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock'
    });

    try {
      await expect(port.initializeProject(alias)).rejects.toMatchObject({
        type: 'INVALID_REQUEST',
        status: 400
      });
      expect(initializeHostedBootstrapProject).not.toHaveBeenCalled();
    } finally {
      await rm(alias);
      await rm(fixtureRoot, { recursive: true, force: true });
    }
  });

  it('does not install a normal port when Runtime returns a conflicting registration', async () => {
    const projectRoot = await realpath(process.cwd());
    const registration = { projectId: 'project-one', manifestHash: 'expected' };
    const installBoundPort = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({
        initializeHostedBootstrapProject: vi.fn().mockResolvedValue(registration),
        projectStatus: vi.fn().mockResolvedValue({
          project: {
            ...project,
            projectId: registration.projectId,
            canonicalRoot: projectRoot,
            manifestHash: 'conflicting'
          },
          manifestDrift: false,
          adaptersEnabled: true
        })
      }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: vi.fn(),
      installBoundPort
    });

    await expect(port.initializeProject(projectRoot)).rejects.toMatchObject({
      type: 'WORKING_ROOT_CONFLICT',
      status: 409
    });
    expect(installBoundPort).not.toHaveBeenCalled();
  });

  it('does not install a normal port when Runtime rejects project initialization', async () => {
    const projectRoot = await realpath(process.cwd());
    const installBoundPort = vi.fn();
    const port = new RuntimeHostedBootstrapPort({
      bootstrapClient: client({
        initializeHostedBootstrapProject: vi.fn().mockRejectedValue(
          new RuntimeError('INVALID_REQUEST', 'Malformed existing manifest', 400)
        )
      }),
      runtimeDirectory: '/runtime',
      socketPath: '/runtime/control.sock',
      createScopedClient: vi.fn(),
      installBoundPort
    });

    await expect(port.initializeProject(projectRoot)).rejects.toMatchObject({
      type: 'INVALID_REQUEST',
      status: 400,
      message: 'Malformed existing manifest'
    });
    expect(installBoundPort).not.toHaveBeenCalled();
  });

  it('uses only the fixed app-dev project for contained scaffold requests', async () => {
    const scaffoldResult = {
      executionRoot: `${project.canonicalRoot}/execution/demo`,
      decompositionPath: `${project.canonicalRoot}/execution/demo/decomposition.json`,
      copiedDecompositionPath: `${project.canonicalRoot}/execution/demo/decomposition.json`,
      projectName: 'demo',
      coordinationMode: 'HYBRID' as const,
      packageCount: 0,
      deliverableCount: 0,
      created: { directories: [], files: [] },
      layoutValidation: {
        valid: true,
        executionRoot: { path: 'execution/demo', valid: true, missing: [] },
        packages: [],
        deliverables: []
      },
      preparationCompatibility: {
        ready: true,
        deliverablesChecked: 0,
        issueCount: 0,
        deliverables: []
      }
    };
    const runtimeClient = client({
      scaffold: vi.fn().mockResolvedValue(scaffoldResult)
    });
    const port = new RuntimeDaemonHarnessPort(runtimeClient);

    await expect(
      port.scaffold({
        executionRoot: scaffoldResult.executionRoot,
        decompositionPath: scaffoldResult.decompositionPath,
        coordinationMode: 'HYBRID'
      })
    ).resolves.toEqual(scaffoldResult);
    expect(runtimeClient.scaffold).toHaveBeenCalledWith(
      project.projectId,
      {
        executionRoot: scaffoldResult.executionRoot,
        decompositionPath: scaffoldResult.decompositionPath,
        coordinationMode: 'HYBRID'
      },
      undefined
    );
    expect(runtimeClient.listProjects).not.toHaveBeenCalled();
  });

  it('translates daemon failures into the legacy route error vocabulary', async () => {
    const port = new RuntimeDaemonHarnessPort(
      client({
        turnSession: vi
          .fn()
          .mockRejectedValue(
            new RuntimeError('SESSION_TURN_IN_PROGRESS', 'turn locked', 409)
          )
      })
    );

    await expect(
      port.turn({ sessionId: session.sessionId, message: 'blocked' })
    ).rejects.toEqual(
      expect.objectContaining({
        type: 'TURN_IN_PROGRESS',
        status: 409,
        message: 'turn locked'
      })
    );
  });

  it('never enumerates projects or session owners, even with an operator-capable client', async () => {
    const runtimeClient = client({
      resolveProjectByRoot: vi.fn(() => {
        throw new Error('must not enumerate projects');
      }),
      resolveSessionOwner: vi.fn(() => {
        throw new Error('must not enumerate session owners');
      }),
      listProjects: vi.fn(() => {
        throw new Error('must not list projects');
      })
    });
    const port = new RuntimeDaemonHarnessPort(
      runtimeClient,
      project.projectId,
      project.canonicalRoot
    );

    await expect(port.getSession('foreign-looking-session-id')).resolves.toEqual({
      session
    });
    expect(runtimeClient.getSession).toHaveBeenCalledWith(
      project.projectId,
      'foreign-looking-session-id',
      undefined
    );
    expect(runtimeClient.resolveSessionOwner).not.toHaveBeenCalled();
    expect(runtimeClient.listProjects).not.toHaveBeenCalled();
  });

  it('rejects a session payload attributed to another project', async () => {
    const port = new RuntimeDaemonHarnessPort(
      client({
        getSession: vi.fn().mockResolvedValue({
          ...session,
          projectId: 'pec'
        })
      }),
      project.projectId,
      project.canonicalRoot
    );

    await expect(port.getSession(session.sessionId)).rejects.toMatchObject({
      type: 'PROVIDER_AUTH_FAILURE',
      status: 403
    });
  });

  it('rejects paths and registrations outside the fixed app-dev root', async () => {
    const runtimeClient = client();
    const port = new RuntimeDaemonHarnessPort(
      runtimeClient,
      project.projectId,
      project.canonicalRoot
    );

    await expect(
      port.createSession({
        projectRoot: '/repo/projects/pec',
        persona: 'WORKING_ITEMS',
        mode: 'chat'
      })
    ).rejects.toMatchObject({
      type: 'WORKING_ROOT_INACCESSIBLE',
      status: 404
    });
    expect(runtimeClient.createSession).not.toHaveBeenCalled();

    const mismatched = new RuntimeDaemonHarnessPort(
      client({
        projectStatus: vi.fn().mockResolvedValue({
          project: { ...project, canonicalRoot: '/repo/projects/pec' },
          manifestDrift: false,
          adaptersEnabled: true
        })
      }),
      project.projectId,
      project.canonicalRoot
    );
    await expect(mismatched.listSessions(project.canonicalRoot)).rejects.toMatchObject({
      type: 'WORKING_ROOT_CONFLICT',
      status: 409
    });
  });
});
