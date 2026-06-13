import { describe, expect, it } from 'vitest';
import {
  getCurrentTrancheDisallowedToolNames,
  getHarnessToolDescriptor,
  HARNESS_TOOL_REGISTRY_VERSION,
  listHarnessToolDescriptors,
  resolveHarnessToolPool
} from '../../lib/harness/tool-descriptor';

describe('tool descriptor registry', () => {
  it('defines provider-neutral metadata before any tools are exposed', () => {
    const descriptors = listHarnessToolDescriptors();

    expect(descriptors.map((descriptor) => descriptor.name)).toEqual([
      'read_file',
      'find_files',
      'search_files',
      'list_files',
      'write_file',
      'edit_file',
      'multi_edit_file',
      'notebook_edit',
      'shell',
      'web_fetch',
      'web_search',
      'agent'
    ]);
    expect(descriptors.every((descriptor) => descriptor.runtime.exposedToModel === false)).toBe(
      true
    );

    const readFile = getHarnessToolDescriptor('read');
    expect(readFile?.permissions).toEqual(['read']);
    expect(readFile?.pathScope).toBe('project-root-read');
    expect(readFile?.humanGate.required).toBe(false);

    const writeFile = getHarnessToolDescriptor('Write');
    expect(writeFile?.permissions).toEqual(['workspace-write']);
    expect(writeFile?.pathScope).toBe('project-root-write');
    expect(writeFile?.humanGate.required).toBe(true);

    const bash = getHarnessToolDescriptor('bash');
    expect(bash?.permissions).toEqual(['shell', 'danger']);
    expect(bash?.humanGate.required).toBe(true);
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
    expect(resolution.allowedToolNames).toEqual([]);
    expect(resolution.disallowedToolNames).toEqual(getCurrentTrancheDisallowedToolNames());
    expect(resolution.unknownTools).toEqual([
      expect.objectContaining({
        type: 'UNKNOWN_TOOL',
        toolName: 'mystery',
        knownTools: expect.arrayContaining(['read_file', 'list_files'])
      })
    ]);
    expect(resolution.deniedTools.map((issue) => issue.type)).toEqual([
      'DENIED_BY_CURRENT_PHASE',
      'DENIED_BY_CURRENT_PHASE',
      'DENIED_BY_CURRENT_PHASE'
    ]);
  });

  it('keeps the descriptor-only SDK deny list broad enough to preserve no-tool exposure', () => {
    expect(getCurrentTrancheDisallowedToolNames()).toEqual([
      'Read',
      'Glob',
      'Grep',
      'LS',
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
