import type { HarnessEventType } from './event-schema';

export const HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v1.descriptor-only';

export type ClaudeAgentSdkToolName =
  | 'Read'
  | 'Glob'
  | 'Grep'
  | 'LS'
  | 'Write'
  | 'Edit'
  | 'MultiEdit'
  | 'NotebookEdit'
  | 'Bash'
  | 'WebFetch'
  | 'WebSearch'
  | 'Agent';

export type HarnessToolPermission =
  | 'read'
  | 'workspace-write'
  | 'network'
  | 'shell'
  | 'subagent'
  | 'danger';

export type HarnessToolPathScope =
  | 'none'
  | 'project-root-read'
  | 'project-root-write'
  | 'instruction-root-read'
  | 'external-network';

export type HarnessToolIdempotence = 'idempotent' | 'input-dependent' | 'mutating';
export type HarnessToolConcurrency = 'safe' | 'serialized-by-path' | 'exclusive';
export type HarnessToolInterruptBehavior = 'cancel' | 'block' | 'not-applicable';
export type HarnessToolSurface = 'claude-agent-sdk-builtin' | 'chirality-mcp' | 'reserved';

export type HarnessToolHumanGate =
  | {
      required: false;
    }
  | {
      required: true;
      gate: 'interactive-confirmation' | 'approval-sha' | 'future-policy';
      reason: string;
    };

export type HarnessToolResultBudget = {
  inlineByteLimit: number;
  artifactByteLimit: number;
  overflow: 'artifact' | 'deny' | 'summarize';
};

export type HarnessToolProvenance = {
  emits: readonly HarnessEventType[];
  storeInput: 'metadata' | 'redacted' | 'none';
  storeOutput: 'inline-or-artifact' | 'metadata' | 'none';
  recordsDiff: boolean;
};

export type HarnessToolRuntimeSupport = {
  exposedToModel: false;
  reason: string;
};

export type HarnessToolDescriptor = {
  name: string;
  aliases: readonly string[];
  description: string;
  surface: HarnessToolSurface;
  permissions: readonly HarnessToolPermission[];
  pathScope: HarnessToolPathScope;
  idempotence: HarnessToolIdempotence;
  concurrency: HarnessToolConcurrency;
  interruptBehavior: HarnessToolInterruptBehavior;
  resultBudget: HarnessToolResultBudget;
  provenance: HarnessToolProvenance;
  humanGate: HarnessToolHumanGate;
  adapter: {
    claudeAgentSdk?: {
      toolName: ClaudeAgentSdkToolName;
    };
  };
  inputSchema: Record<string, unknown>;
  outputSchema?: Record<string, unknown>;
  runtime: HarnessToolRuntimeSupport;
};

export type HarnessToolResolutionIssue =
  | {
      type: 'UNKNOWN_TOOL';
      toolName: string;
      message: string;
      knownTools: readonly string[];
    }
  | {
      type: 'DENIED_BY_CURRENT_PHASE';
      toolName: string;
      descriptorName: string;
      message: string;
    };

export type HarnessToolPoolResolution = {
  registryVersion: typeof HARNESS_TOOL_REGISTRY_VERSION;
  mode: string;
  requestedTools: readonly string[];
  requestedDescriptors: readonly HarnessToolDescriptor[];
  allowedToolNames: readonly ClaudeAgentSdkToolName[];
  disallowedToolNames: readonly ClaudeAgentSdkToolName[];
  deniedTools: readonly HarnessToolResolutionIssue[];
  unknownTools: readonly HarnessToolResolutionIssue[];
  issues: readonly HarnessToolResolutionIssue[];
};

const TOOL_EVENTS = [
  'tool.permission',
  'tool.started',
  'tool.completed',
  'tool.failed'
] as const satisfies readonly HarnessEventType[];

const DESCRIPTOR_ONLY_RUNTIME: HarnessToolRuntimeSupport = {
  exposedToModel: false,
  reason:
    'Tool execution remains disabled until the permission overlay, hooks, result storage, and tool loop are implemented.'
};

const READ_RESULT_BUDGET: HarnessToolResultBudget = {
  inlineByteLimit: 64 * 1024,
  artifactByteLimit: 2 * 1024 * 1024,
  overflow: 'artifact'
};

const WRITE_RESULT_BUDGET: HarnessToolResultBudget = {
  inlineByteLimit: 16 * 1024,
  artifactByteLimit: 512 * 1024,
  overflow: 'artifact'
};

const SHELL_RESULT_BUDGET: HarnessToolResultBudget = {
  inlineByteLimit: 16 * 1024,
  artifactByteLimit: 2 * 1024 * 1024,
  overflow: 'artifact'
};

function readOnlyDescriptor(input: {
  name: string;
  aliases: readonly string[];
  description: string;
  sdkToolName: ClaudeAgentSdkToolName;
  inputSchema: Record<string, unknown>;
}): HarnessToolDescriptor {
  return {
    name: input.name,
    aliases: input.aliases,
    description: input.description,
    surface: 'claude-agent-sdk-builtin',
    permissions: ['read'],
    pathScope: 'project-root-read',
    idempotence: 'idempotent',
    concurrency: 'safe',
    interruptBehavior: 'cancel',
    resultBudget: READ_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'metadata',
      storeOutput: 'inline-or-artifact',
      recordsDiff: false
    },
    humanGate: {
      required: false
    },
    adapter: {
      claudeAgentSdk: {
        toolName: input.sdkToolName
      }
    },
    inputSchema: input.inputSchema,
    runtime: DESCRIPTOR_ONLY_RUNTIME
  };
}

export const HARNESS_TOOL_DESCRIPTORS = [
  readOnlyDescriptor({
    name: 'read_file',
    aliases: ['read', 'Read', 'sdk.read'],
    description: 'Read one project-root-contained file.',
    sdkToolName: 'Read',
    inputSchema: {
      type: 'object',
      required: ['file_path'],
      properties: {
        file_path: {
          type: 'string'
        }
      }
    }
  }),
  readOnlyDescriptor({
    name: 'find_files',
    aliases: ['glob', 'Glob', 'sdk.glob'],
    description: 'Find project files by glob pattern.',
    sdkToolName: 'Glob',
    inputSchema: {
      type: 'object',
      required: ['pattern'],
      properties: {
        pattern: {
          type: 'string'
        }
      }
    }
  }),
  readOnlyDescriptor({
    name: 'search_files',
    aliases: ['grep', 'Grep', 'search', 'sdk.grep'],
    description: 'Search project files for text patterns.',
    sdkToolName: 'Grep',
    inputSchema: {
      type: 'object',
      required: ['pattern'],
      properties: {
        pattern: {
          type: 'string'
        },
        path: {
          type: 'string'
        }
      }
    }
  }),
  readOnlyDescriptor({
    name: 'list_files',
    aliases: ['list', 'ls', 'LS', 'sdk.ls'],
    description: 'List files and directories inside the project root.',
    sdkToolName: 'LS',
    inputSchema: {
      type: 'object',
      required: ['path'],
      properties: {
        path: {
          type: 'string'
        }
      }
    }
  }),
  {
    name: 'write_file',
    aliases: ['write', 'Write', 'sdk.write'],
    description: 'Write a project-root-contained file after policy approval.',
    surface: 'claude-agent-sdk-builtin',
    permissions: ['workspace-write'],
    pathScope: 'project-root-write',
    idempotence: 'mutating',
    concurrency: 'serialized-by-path',
    interruptBehavior: 'block',
    resultBudget: WRITE_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'metadata',
      storeOutput: 'metadata',
      recordsDiff: true
    },
    humanGate: {
      required: true,
      gate: 'interactive-confirmation',
      reason: 'Workspace writes require an accepted permission policy and human gate.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'Write'
      }
    },
    inputSchema: {
      type: 'object',
      required: ['file_path', 'content'],
      properties: {
        file_path: {
          type: 'string'
        },
        content: {
          type: 'string'
        }
      }
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'edit_file',
    aliases: ['edit', 'Edit', 'sdk.edit'],
    description: 'Apply an exact project-root-contained file edit after policy approval.',
    surface: 'claude-agent-sdk-builtin',
    permissions: ['workspace-write'],
    pathScope: 'project-root-write',
    idempotence: 'mutating',
    concurrency: 'serialized-by-path',
    interruptBehavior: 'block',
    resultBudget: WRITE_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'metadata',
      storeOutput: 'metadata',
      recordsDiff: true
    },
    humanGate: {
      required: true,
      gate: 'interactive-confirmation',
      reason: 'File edits require path containment, diff provenance, and permission policy.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'Edit'
      }
    },
    inputSchema: {
      type: 'object',
      required: ['file_path', 'old_string', 'new_string'],
      properties: {
        file_path: {
          type: 'string'
        },
        old_string: {
          type: 'string'
        },
        new_string: {
          type: 'string'
        }
      }
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'multi_edit_file',
    aliases: ['multi_edit', 'MultiEdit', 'sdk.multiedit'],
    description: 'Apply multiple exact project-root-contained edits after policy approval.',
    surface: 'claude-agent-sdk-builtin',
    permissions: ['workspace-write'],
    pathScope: 'project-root-write',
    idempotence: 'mutating',
    concurrency: 'serialized-by-path',
    interruptBehavior: 'block',
    resultBudget: WRITE_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'metadata',
      storeOutput: 'metadata',
      recordsDiff: true
    },
    humanGate: {
      required: true,
      gate: 'interactive-confirmation',
      reason: 'Multi-file edits require same-file serialization and accepted write policy.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'MultiEdit'
      }
    },
    inputSchema: {
      type: 'object',
      required: ['file_path', 'edits'],
      properties: {
        file_path: {
          type: 'string'
        },
        edits: {
          type: 'array'
        }
      }
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'notebook_edit',
    aliases: ['NotebookEdit', 'notebook_edit', 'sdk.notebookedit'],
    description: 'Reserved SDK notebook mutation surface; not part of the current Chirality runtime.',
    surface: 'reserved',
    permissions: ['workspace-write', 'danger'],
    pathScope: 'project-root-write',
    idempotence: 'mutating',
    concurrency: 'serialized-by-path',
    interruptBehavior: 'block',
    resultBudget: WRITE_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'metadata',
      storeOutput: 'metadata',
      recordsDiff: true
    },
    humanGate: {
      required: true,
      gate: 'future-policy',
      reason: 'Notebook mutation is reserved until a product policy accepts notebook support.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'NotebookEdit'
      }
    },
    inputSchema: {
      type: 'object'
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'shell',
    aliases: ['bash', 'Bash', 'shell', 'sdk.bash'],
    description: 'Run a shell command after explicit shell policy, timeout, and audit controls exist.',
    surface: 'claude-agent-sdk-builtin',
    permissions: ['shell', 'danger'],
    pathScope: 'none',
    idempotence: 'input-dependent',
    concurrency: 'exclusive',
    interruptBehavior: 'cancel',
    resultBudget: SHELL_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'metadata',
      storeOutput: 'inline-or-artifact',
      recordsDiff: false
    },
    humanGate: {
      required: true,
      gate: 'interactive-confirmation',
      reason: 'Shell execution is denied until timeout, audit, packaging, and permission controls exist.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'Bash'
      }
    },
    inputSchema: {
      type: 'object',
      required: ['command'],
      properties: {
        command: {
          type: 'string'
        }
      }
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'web_fetch',
    aliases: ['WebFetch', 'web_fetch', 'sdk.webfetch'],
    description: 'Reserved network fetch surface outside the current Anthropic-only runtime policy.',
    surface: 'reserved',
    permissions: ['network'],
    pathScope: 'external-network',
    idempotence: 'input-dependent',
    concurrency: 'safe',
    interruptBehavior: 'cancel',
    resultBudget: READ_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'redacted',
      storeOutput: 'inline-or-artifact',
      recordsDiff: false
    },
    humanGate: {
      required: true,
      gate: 'future-policy',
      reason: 'Non-Anthropic network access requires a future governed scope amendment.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'WebFetch'
      }
    },
    inputSchema: {
      type: 'object'
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'web_search',
    aliases: ['WebSearch', 'web_search', 'sdk.websearch'],
    description: 'Reserved network search surface outside the current Anthropic-only runtime policy.',
    surface: 'reserved',
    permissions: ['network'],
    pathScope: 'external-network',
    idempotence: 'input-dependent',
    concurrency: 'safe',
    interruptBehavior: 'cancel',
    resultBudget: READ_RESULT_BUDGET,
    provenance: {
      emits: TOOL_EVENTS,
      storeInput: 'redacted',
      storeOutput: 'inline-or-artifact',
      recordsDiff: false
    },
    humanGate: {
      required: true,
      gate: 'future-policy',
      reason: 'Non-Anthropic network access requires a future governed scope amendment.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'WebSearch'
      }
    },
    inputSchema: {
      type: 'object'
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  },
  {
    name: 'agent',
    aliases: ['Agent', 'subagent', 'sdk.agent'],
    description: 'Invoke a governed subagent after Type 2 allowlist and parent-child audit policy exist.',
    surface: 'claude-agent-sdk-builtin',
    permissions: ['subagent'],
    pathScope: 'none',
    idempotence: 'input-dependent',
    concurrency: 'exclusive',
    interruptBehavior: 'cancel',
    resultBudget: READ_RESULT_BUDGET,
    provenance: {
      emits: ['tool.permission', 'subagent.started', 'subagent.completed', 'subagent.failed'],
      storeInput: 'metadata',
      storeOutput: 'inline-or-artifact',
      recordsDiff: false
    },
    humanGate: {
      required: true,
      gate: 'future-policy',
      reason: 'Subagent execution requires SDK agent definitions and fail-closed governance hooks.'
    },
    adapter: {
      claudeAgentSdk: {
        toolName: 'Agent'
      }
    },
    inputSchema: {
      type: 'object',
      required: ['agent'],
      properties: {
        agent: {
          type: 'string'
        }
      }
    },
    runtime: DESCRIPTOR_ONLY_RUNTIME
  }
] as const satisfies readonly HarnessToolDescriptor[];

function normalizeToolName(toolName: string): string {
  return toolName.trim().toLowerCase();
}

function createDescriptorLookup(): Map<string, HarnessToolDescriptor> {
  const lookup = new Map<string, HarnessToolDescriptor>();
  for (const descriptor of HARNESS_TOOL_DESCRIPTORS) {
    lookup.set(normalizeToolName(descriptor.name), descriptor);
    for (const alias of descriptor.aliases) {
      lookup.set(normalizeToolName(alias), descriptor);
    }
    const sdkToolName = descriptor.adapter.claudeAgentSdk?.toolName;
    if (sdkToolName) {
      lookup.set(normalizeToolName(sdkToolName), descriptor);
    }
  }
  return lookup;
}

const DESCRIPTOR_LOOKUP = createDescriptorLookup();

function uniqueValues<T>(values: readonly T[]): T[] {
  return Array.from(new Set(values));
}

export function listHarnessToolDescriptors(): HarnessToolDescriptor[] {
  return [...HARNESS_TOOL_DESCRIPTORS];
}

export function getHarnessToolDescriptor(toolName: string): HarnessToolDescriptor | undefined {
  return DESCRIPTOR_LOOKUP.get(normalizeToolName(toolName));
}

export function getKnownHarnessToolNames(): string[] {
  return HARNESS_TOOL_DESCRIPTORS.map((descriptor) => descriptor.name);
}

export function getCurrentTrancheDisallowedToolNames(): ClaudeAgentSdkToolName[] {
  return uniqueValues(
    HARNESS_TOOL_DESCRIPTORS.flatMap((descriptor) => {
      const sdkToolName = descriptor.adapter.claudeAgentSdk?.toolName;
      return sdkToolName ? [sdkToolName] : [];
    })
  );
}

export function resolveHarnessToolPool(input: {
  requestedTools?: readonly string[];
  mode?: string;
}): HarnessToolPoolResolution {
  const requestedTools = uniqueValues(
    (input.requestedTools ?? [])
      .map((toolName) => toolName.trim())
      .filter((toolName) => toolName.length > 0)
  );
  const requestedDescriptors: HarnessToolDescriptor[] = [];
  const deniedTools: HarnessToolResolutionIssue[] = [];
  const unknownTools: HarnessToolResolutionIssue[] = [];
  const seenDescriptors = new Set<string>();
  const knownTools = getKnownHarnessToolNames();

  for (const toolName of requestedTools) {
    const descriptor = getHarnessToolDescriptor(toolName);
    if (!descriptor) {
      unknownTools.push({
        type: 'UNKNOWN_TOOL',
        toolName,
        message: `Unknown harness tool '${toolName}'.`,
        knownTools
      });
      continue;
    }

    if (!seenDescriptors.has(descriptor.name)) {
      seenDescriptors.add(descriptor.name);
      requestedDescriptors.push(descriptor);
      deniedTools.push({
        type: 'DENIED_BY_CURRENT_PHASE',
        toolName,
        descriptorName: descriptor.name,
        message: descriptor.runtime.reason
      });
    }
  }

  return {
    registryVersion: HARNESS_TOOL_REGISTRY_VERSION,
    mode: input.mode ?? 'default',
    requestedTools,
    requestedDescriptors,
    allowedToolNames: [],
    disallowedToolNames: getCurrentTrancheDisallowedToolNames(),
    deniedTools,
    unknownTools,
    issues: [...unknownTools, ...deniedTools]
  };
}
