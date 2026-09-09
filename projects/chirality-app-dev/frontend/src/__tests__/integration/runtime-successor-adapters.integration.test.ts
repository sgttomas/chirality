import { mkdir, mkdtemp, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import {
  AuthRegistry,
  EngineRegistry,
  ProjectRegistry,
  ResidencyCoordinator,
  RuntimeService,
  SessionStore,
  TurnCoordinator
} from '@chirality/runtime-core';
import type { AgentEnginePort, OmlxControlPort, UIEvent } from '@chirality/runtime-contracts';
import { ClaudeAgentSdkManager } from '../../lib/harness/claude-agent-sdk-manager';
import { AnthropicAgentSdkManager } from '../../lib/harness/anthropic-agent-sdk-manager';
import { PiAgentEngineAdapter } from '../../lib/harness/pi-agent-engine-adapter';
import { LegacyAgentEngineAdapter } from '../../lib/harness/engine-registry';

const roots: string[] = [];

afterEach(async () => {
  await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

async function drain(source: AsyncIterable<UIEvent>): Promise<void> {
  for await (const _event of source) { /* exhaust */ }
}

function adapters(): readonly AgentEnginePort[] {
  return [
    new ClaudeAgentSdkManager(undefined, async () => 'unused'),
    new LegacyAgentEngineAdapter({
      adapterId: 'anthropic-direct', providerId: 'anthropic',
      capabilities: { credentials: true, tools: false, attachments: true, interruption: true, durableResume: true, compaction: false }
    }, new AnthropicAgentSdkManager()),
    new PiAgentEngineAdapter({
      resolveProvider: async () => ({
        baseUrl: 'http://127.0.0.1:1/v1', apiKey: 'unused',
        model: { id: 'unused', contextWindow: 1, maxTokens: 1 }
      }),
      buildSystemPrompt: async () => 'unused',
      customTools: []
    })
  ];
}

async function exerciseRuntimeSuccessor(actual: AgentEnginePort): Promise<void> {
  const directory = await mkdtemp(path.join(os.tmpdir(), 'chirality-app-successor-'));
  roots.push(directory);
  const projectRoot = path.join(directory, 'project');
  const runtimeRoot = path.join(directory, 'runtime');
  await mkdir(path.join(projectRoot, '.chirality', 'workflows', 'next-method'), { recursive: true });
  await writeFile(path.join(projectRoot, 'AGENTS.md'), '# Controlled App successor project\n');
  await writeFile(path.join(projectRoot, '.chirality', 'workflows', 'next-method', 'WORKFLOW.md'), [
    '---', 'name: next-method', 'description: Runtime-to-App successor contract fixture.', '---', '', '# Next method', 'CURRENT_METHOD_BODY'
  ].join('\n'));
  await writeFile(path.join(projectRoot, '.chirality', 'workflows', 'next-method', 'execution.json'), `${JSON.stringify({ schema_version: 1, compatible_roles: ['HELP_HUMAN'] })}\n`);
  const projectId = `app-successor-${actual.descriptor.adapterId}`;
  const manifestPath = path.join(projectRoot, 'chirality.project.json');
  await writeFile(manifestPath, `${JSON.stringify({
    schemaVersion: 'chirality.project/v2', projectId, displayName: 'App successor fixture', workingRoot: '.',
    instructionRoot: { mode: 'runtime' }, defaultExecutionRoot: '.', profiles: { domain: [], capability: [], dataBoundary: [] },
    enabledAdapterIds: [actual.descriptor.adapterId], embeddedUi: { declared: false }
  })}\n`);

  const projects = new ProjectRegistry(runtimeRoot, {
    CHIRALITY_INSTRUCTION_ROOT: path.resolve(process.cwd(), '../../..')
  });
  const sessions = new SessionStore(runtimeRoot, projects);
  const engines = new EngineRegistry();
  const controlled: AgentEnginePort = {
    descriptor: actual.descriptor,
    subject: actual.subject,
    async preflight() {},
    async *startTurn(input) {
      yield { type: 'session:init', data: {
        engineSessionId: `predecessor-${actual.descriptor.adapterId}`,
        adapterId: actual.descriptor.adapterId,
        providerId: actual.descriptor.providerId,
        model: input.opts.model
      } };
      yield { type: 'chat:complete', data: { text: 'prior assistant response' } };
      yield { type: 'process:exit', data: { exitCode: 0 } };
    },
    async interrupt() {},
    prepareContextSuccessor: actual.prepareContextSuccessor?.bind(actual),
    cancelContextSuccessor: actual.cancelContextSuccessor?.bind(actual)
  };
  engines.register(controlled);
  const control: OmlxControlPort = { async listStatus() { return []; }, async load() {}, async unload() {} };
  const residency = new ResidencyCoordinator(control, runtimeRoot);
  const service = new RuntimeService(
    projects, sessions, engines, residency,
    new TurnCoordinator(projects, sessions, engines, residency),
    new AuthRegistry(runtimeRoot),
    { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} },
    undefined, undefined, undefined,
    { async resolve() { return { role: 'agent0' as const, engineSelection: {
      adapterId: actual.descriptor.adapterId, providerId: actual.descriptor.providerId, model: 'controlled'
    } }; } }
  );
  await service.registerProject(manifestPath, 'test', 'app-successor-contract');
  const session = await service.createSession({ projectId, selectedMethods: [] });
  await drain(service.runSessionTurn(projectId, session.sessionId, { message: 'prior human request' }));
  const methods = await service.listMethods(projectId);
  const next = methods.methods.find((method) => method.name === 'next-method');
  expect(next).toBeDefined();
  const replaced = await service.replaceSelectedMethods(projectId, session.sessionId, {
    expectedRevision: 0, boundaryConfirmed: true,
    methods: [{ sourceRootId: next!.sourceRootId, source: next!.source, kind: next!.kind, name: next!.name }]
  });
  if (actual.descriptor.capabilities.durableResume) {
    expect(replaced.transition).toMatchObject({ status: 'prepared', successorAvailable: true });
  } else {
    // Pi starts a fresh provider identity for each turn, so Runtime does not
    // need to prepare a replacement span. Its callable preparation seam still
    // uses the same canonical reference if Runtime qualifies resume later.
    expect(replaced.transition).toMatchObject({ status: 'unchanged', successorAvailable: true });
    const preview = replaced.basisPreview;
    const prepared = await actual.prepareContextSuccessor?.({
      sessionId: session.sessionId,
      predecessorEngineSessionId: `predecessor-${actual.descriptor.adapterId}`,
      fromBasisId: session.instructionBasisId!,
      toBasisPreview: preview,
      continuationContext: { transcript: '[]', sha256: '0'.repeat(64), priorBasisRefs: [] }
    });
    expect(prepared?.targetReference).toBe(`${preview.id}:${preview.sha256}`);
  }
}

describe('RuntimeService to production App successor preparation', () => {
  for (const adapter of adapters()) {
    it(`accepts the canonical target reference from ${adapter.descriptor.adapterId}`, async () => {
      await exerciseRuntimeSuccessor(adapter);
    });
  }
});
