import { describe, expect, it, vi } from 'vitest';

import { RuntimeError, type RuntimeSessionRecord } from '@chirality/runtime-contracts';
import type { RuntimeClient, RuntimeStream } from '@chirality/runtime-client';
import type { UIEvent } from '@chirality/runtime-contracts/types';

import {
  RuntimeDaemonHarnessPort,
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
