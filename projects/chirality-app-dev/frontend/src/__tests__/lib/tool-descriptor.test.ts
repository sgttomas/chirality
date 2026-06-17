import { describe, expect, it } from 'vitest';
import {
  createDescriptorLookup,
  getCurrentTrancheDisallowedToolNames,
  getHarnessToolDescriptor,
  HARNESS_TOOL_REGISTRY_VERSION,
  listHarnessToolDescriptors,
  resolveHarnessToolPool,
  type ClaudeAgentSdkToolName,
  type HarnessToolDescriptor
} from '../../lib/harness/tool-descriptor';
import { buildChiralityMcpTools } from '../../lib/harness/mcp/read-tools';
import {
  CHIRALITY_MCP_ALLOWED_TOOL_NAMES,
  type ChiralityMcpAllowedToolName
} from '../../lib/harness/mcp/tool-names';

function normalizeLookupKey(toolName: string): string {
  return toolName.trim().toLowerCase();
}

function descriptorLookupKeys(descriptor: HarnessToolDescriptor): Array<{
  rawKey: string;
  kind: string;
}> {
  return [
    { rawKey: descriptor.name, kind: 'name' },
    ...descriptor.aliases.map((alias) => ({ rawKey: alias, kind: 'alias' })),
    ...(descriptor.adapter.claudeAgentSdk?.toolName
      ? [
          {
            rawKey: descriptor.adapter.claudeAgentSdk.toolName,
            kind: 'adapter.claudeAgentSdk.toolName'
          }
        ]
      : [])
  ];
}

function toRawChiralityMcpToolName(toolName: ChiralityMcpAllowedToolName): string {
  return toolName.replace(/^mcp__chirality__/, '');
}

describe('tool descriptor registry', () => {
  it('fails closed on duplicate descriptor lookup keys', () => {
    const [readFile] = listHarnessToolDescriptors();
    const duplicate: HarnessToolDescriptor = {
      ...readFile,
      name: 'duplicate_read_file',
      aliases: ['duplicate_read'],
      adapter: {
        claudeAgentSdk: {
          toolName: 'Read'
        }
      }
    };

    expect(() => createDescriptorLookup([readFile, duplicate])).toThrow(
      /Duplicate harness tool descriptor key "Read"/
    );
  });

  it('keeps descriptor names, aliases, and adapter tool names collision-free across descriptors', () => {
    const registrations = new Map<
      string,
      { descriptorName: string; rawKey: string; kind: string }
    >();

    for (const descriptor of listHarnessToolDescriptors()) {
      for (const key of descriptorLookupKeys(descriptor)) {
        const normalized = normalizeLookupKey(key.rawKey);
        const existing = registrations.get(normalized);
        if (existing) {
          expect(existing.descriptorName).toBe(descriptor.name);
          continue;
        }
        registrations.set(normalized, {
          descriptorName: descriptor.name,
          rawKey: key.rawKey,
          kind: key.kind
        });
      }
    }
  });

  it('keeps built-in SDK tool names disjoint from Chirality MCP adapter names', () => {
    const descriptors = listHarnessToolDescriptors();
    const builtinToolNames = descriptors
      .filter((descriptor) => descriptor.surface !== 'chirality-mcp')
      .map((descriptor) => descriptor.adapter.claudeAgentSdk?.toolName)
      .filter((toolName): toolName is ClaudeAgentSdkToolName => Boolean(toolName));
    const chiralityMcpToolNames = descriptors
      .filter((descriptor) => descriptor.surface === 'chirality-mcp')
      .map((descriptor) => descriptor.adapter.claudeAgentSdk?.toolName)
      .filter((toolName): toolName is ChiralityMcpAllowedToolName =>
        Boolean(toolName?.startsWith('mcp__chirality__'))
      );

    expect(new Set(chiralityMcpToolNames)).toEqual(new Set(CHIRALITY_MCP_ALLOWED_TOOL_NAMES));
    expect(builtinToolNames.filter((toolName) => toolName.startsWith('mcp__chirality__'))).toEqual(
      []
    );
    expect(
      builtinToolNames.filter((toolName) => chiralityMcpToolNames.includes(toolName as ChiralityMcpAllowedToolName))
    ).toEqual([]);
  });

  it('keeps live Chirality MCP tool registrations in parity with descriptor metadata', () => {
    const liveToolNames = buildChiralityMcpTools({
      context: { projectRoot: '/tmp/chirality-project', sessionId: 'sess_descriptor_parity' },
      mode: 'workspaceWrite',
      allowedToolNames: CHIRALITY_MCP_ALLOWED_TOOL_NAMES
    }).map((definition) => (definition as { name: string }).name);
    const descriptorToolNames = listHarnessToolDescriptors()
      .filter((descriptor) => descriptor.surface === 'chirality-mcp')
      .map((descriptor) => descriptor.adapter.claudeAgentSdk?.toolName)
      .filter((toolName): toolName is ChiralityMcpAllowedToolName => Boolean(toolName))
      .map(toRawChiralityMcpToolName);

    expect(liveToolNames).toEqual(descriptorToolNames);
  });

  it('exposes read-class tools plus bounded Write/Edit descriptors for the current tranche', () => {
    const descriptors = listHarnessToolDescriptors();

    expect(descriptors.map((descriptor) => descriptor.name)).toEqual([
      'read_file',
      'find_files',
      'search_files',
      'list_files',
      'status_read',
      'dependency_read',
      'scope_scan',
      'scaffold_preview',
      'status_transition',
      'dependency_write',
      'write_file',
      'edit_file',
      'multi_edit_file',
      'notebook_edit',
      'shell',
      'web_fetch',
      'web_search',
      'agent'
    ]);
    expect(
      descriptors
        .filter((descriptor) => descriptor.permissions.includes('read'))
        .map((descriptor) => descriptor.name)
    ).toEqual([
      'read_file',
      'find_files',
      'search_files',
      'list_files',
      'status_read',
      'dependency_read',
      'scope_scan',
      'scaffold_preview'
    ]);
    expect(
      descriptors
        .filter((descriptor) => descriptor.permissions.includes('read'))
        .every((descriptor) => descriptor.runtime.exposedToModel === true)
    ).toBe(true);
    expect(
      descriptors
        .filter((descriptor) => ['write_file', 'edit_file'].includes(descriptor.name))
        .every((descriptor) => descriptor.runtime.exposedToModel === true)
    ).toBe(true);
    expect(
      descriptors
        .filter(
          (descriptor) =>
            !descriptor.permissions.includes('read') &&
            ![
              'status_transition',
              'dependency_write',
              'write_file',
              'edit_file',
              'shell'
            ].includes(descriptor.name)
        )
        .every((descriptor) => descriptor.runtime.exposedToModel === false)
    ).toBe(true);

    const readFile = getHarnessToolDescriptor('read');
    expect(readFile?.permissions).toEqual(['read']);
    expect(readFile?.pathScope).toBe('project-root-read');
    expect(readFile?.humanGate.required).toBe(false);

    const writeFile = getHarnessToolDescriptor('Write');
    expect(writeFile?.permissions).toEqual(['workspace-write']);
    expect(writeFile?.pathScope).toBe('project-root-write');
    expect(writeFile?.humanGate.required).toBe(true);

    const bash = getHarnessToolDescriptor('bash');
    expect(bash?.permissions).toEqual(['shell', 'workspace-write', 'danger']);
    expect(bash?.pathScope).toBe('project-root-write');
    expect(bash?.humanGate.required).toBe(true);
    expect(bash?.runtime.exposedToModel).toBe(true);
  });

  it('resolves Write/Edit/Bash only in workspaceWrite mode', () => {
    const resolution = resolveHarnessToolPool({
      requestedTools: ['read', 'write', 'Edit', 'multi_edit', 'bash'],
      mode: 'workspaceWrite'
    });

    expect(resolution.allowedToolNames).toEqual(['Read', 'Write', 'Edit', 'Bash']);
    expect(resolution.disallowedToolNames).toEqual([
      'Glob',
      'Grep',
      'LS',
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read',
      'mcp__chirality__scope_scan',
      'mcp__chirality__scaffold_preview',
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write',
      'MultiEdit',
      'NotebookEdit',
      'WebFetch',
      'WebSearch',
      'Agent'
    ]);
    expect(resolution.deniedTools).toEqual([
      expect.objectContaining({
        toolName: 'multi_edit',
        descriptorName: 'multi_edit_file'
      })
    ]);

    const askResolution = resolveHarnessToolPool({
      requestedTools: ['write', 'Edit'],
      mode: 'ask'
    });
    expect(askResolution.allowedToolNames).toEqual([]);
    expect(askResolution.disallowedToolNames).toContain('Write');
    expect(askResolution.disallowedToolNames).toContain('Edit');
  });

  it('resolves read-only Chirality MCP descriptors without opening write or shell tools', () => {
    const resolution = resolveHarnessToolPool({
      requestedTools: ['status_read', 'deps_read', 'scope_scan', 'scaffold_preview'],
      mode: 'readOnly'
    });

    expect(resolution.requestedDescriptors.map((descriptor) => descriptor.name)).toEqual([
      'status_read',
      'dependency_read',
      'scope_scan',
      'scaffold_preview'
    ]);
    expect(resolution.allowedToolNames).toEqual([
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read',
      'mcp__chirality__scope_scan',
      'mcp__chirality__scaffold_preview'
    ]);
    expect(resolution.deniedTools).toEqual([]);
    expect(resolution.disallowedToolNames).toEqual([
      'Read',
      'Glob',
      'Grep',
      'LS',
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write',
      'Write',
      'Edit',
      'MultiEdit',
      'NotebookEdit',
      'Bash',
      'WebFetch',
      'WebSearch',
      'Agent'
    ]);
  });

  it('resolves mutating Chirality MCP descriptors only in workspaceWrite mode', () => {
    const resolution = resolveHarnessToolPool({
      requestedTools: ['status_transition', 'deps_write'],
      mode: 'workspaceWrite'
    });

    expect(resolution.requestedDescriptors.map((descriptor) => descriptor.name)).toEqual([
      'status_transition',
      'dependency_write'
    ]);
    expect(resolution.allowedToolNames).toEqual([
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write'
    ]);
    expect(resolution.deniedTools).toEqual([]);
    expect(resolution.disallowedToolNames).not.toContain('mcp__chirality__status_transition');
    expect(resolution.disallowedToolNames).not.toContain('mcp__chirality__deps_write');

    const readOnly = resolveHarnessToolPool({
      requestedTools: ['status_transition', 'deps_write'],
      mode: 'readOnly'
    });

    expect(readOnly.allowedToolNames).toEqual([]);
    expect(readOnly.disallowedToolNames).toContain('mcp__chirality__status_transition');
    expect(readOnly.disallowedToolNames).toContain('mcp__chirality__deps_write');
    expect(readOnly.deniedTools).toEqual([
      expect.objectContaining({
        toolName: 'status_transition',
        descriptorName: 'status_transition'
      }),
      expect.objectContaining({
        toolName: 'deps_write',
        descriptorName: 'dependency_write'
      })
    ]);
  });

  it('resolves aliases deterministically and reports structured unknown tool issues', () => {
    const resolution = resolveHarnessToolPool({
      requestedTools: ['Read', 'read', 'bash', 'mystery', 'LS'],
      mode: 'readOnly'
    });

    expect(resolution.registryVersion).toBe(HARNESS_TOOL_REGISTRY_VERSION);
    expect(resolution.requestedTools).toEqual(['Read', 'read', 'bash', 'mystery', 'LS']);
    expect(resolution.requestedDescriptors.map((descriptor) => descriptor.name)).toEqual([
      'read_file',
      'shell',
      'list_files'
    ]);
    expect(
      resolution.permissionDecisions.map((decision) => ({
        toolName: decision.toolName,
        decision: decision.decision
      }))
    ).toEqual([
      { toolName: 'Read', decision: 'allow' },
      { toolName: 'bash', decision: 'deny' },
      { toolName: 'mystery', decision: 'deny' },
      { toolName: 'LS', decision: 'allow' }
    ]);
    expect(resolution.allowedToolNames).toEqual(['Read', 'LS']);
    expect(resolution.disallowedToolNames).toEqual(getCurrentTrancheDisallowedToolNames(['Read', 'LS']));
    expect(resolution.unknownTools).toEqual([
      expect.objectContaining({
        type: 'UNKNOWN_TOOL',
        toolName: 'mystery',
        knownTools: expect.arrayContaining(['read_file', 'list_files'])
      })
    ]);
    expect(resolution.deniedTools).toEqual([
      expect.objectContaining({
        type: 'DENIED_BY_CURRENT_PHASE',
        toolName: 'bash',
        descriptorName: 'shell'
      })
    ]);
  });

  it('keeps denied and unrequested tools out of the model context', () => {
    expect(getCurrentTrancheDisallowedToolNames()).toEqual([
      'Read',
      'Glob',
      'Grep',
      'LS',
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read',
      'mcp__chirality__scope_scan',
      'mcp__chirality__scaffold_preview',
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write',
      'Write',
      'Edit',
      'MultiEdit',
      'NotebookEdit',
      'Bash',
      'WebFetch',
      'WebSearch',
      'Agent'
    ]);
    expect(getCurrentTrancheDisallowedToolNames(['Read', 'Grep'])).toEqual([
      'Glob',
      'LS',
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read',
      'mcp__chirality__scope_scan',
      'mcp__chirality__scaffold_preview',
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write',
      'Write',
      'Edit',
      'MultiEdit',
      'NotebookEdit',
      'Bash',
      'WebFetch',
      'WebSearch',
      'Agent'
    ]);
  });
});
