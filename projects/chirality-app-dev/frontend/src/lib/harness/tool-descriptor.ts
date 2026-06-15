import type { HarnessEventType } from './event-schema';
import {
  resolveHarnessPermissionDecision,
  type HarnessPermissionDecision
} from './permission-overlay';
import {
  toChiralityMcpAllowedToolName,
  type ChiralityMcpAllowedToolName,
  type ChiralityMcpReadToolName
} from './mcp/tool-names';

export const HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v5.bash';

export type ClaudeAgentSdkBuiltinToolName =
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

export type ClaudeAgentSdkToolName = ClaudeAgentSdkBuiltinToolName | ChiralityMcpAllowedToolName;

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

export type HarnessToolRuntimeSupport =
  | {
      exposedToModel: true;
      reason: string;
    }
  | {
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
  permissionDecisions: readonly HarnessPermissionDecision[];
  allowedToolNames: readonly ClaudeAgentSdkToolName[];
  disallowedToolNames: readonly ClaudeAgentSdkToolName[];
  deniedTools: readonly HarnessToolResolutionIssue[];
  unknownTools: readonly HarnessToolResolutionIssue[];
  issues: readonly HarnessToolResolutionIssue[];
};

const TOOL_EVENTS = [
  'tool.permission',
  'tool.started',
  'tool.progress',
  'tool.completed',
  'tool.failed'
] as const satisfies readonly HarnessEventType[];

const SDK_READ_RUNTIME: HarnessToolRuntimeSupport = {
  exposedToModel: true,
  reason:
    'Read-class SDK built-ins are exposed behind Chirality permission overlay and hard-deny policy.'
};

const CHIRALITY_READ_MCP_RUNTIME: HarnessToolRuntimeSupport = {
  exposedToModel: true,
  reason:
    'Read-only Chirality MCP tools are exposed behind descriptor resolution and permission overlay policy.'
};

const SDK_WRITE_RUNTIME: HarnessToolRuntimeSupport = {
  exposedToModel: true,
  reason:
    'Write/Edit SDK built-ins are exposed only in workspaceWrite mode after descriptor resolution, permission overlay, and Chirality write hooks.'
};

const SDK_SHELL_RUNTIME: HarnessToolRuntimeSupport = {
  exposedToModel: true,
  reason:
    'Bash is exposed only in workspaceWrite mode after descriptor resolution, permission overlay, timeout policy, and Chirality shell hooks.'
};

const DESCRIPTOR_ONLY_RUNTIME: HarnessToolRuntimeSupport = {
  exposedToModel: false,
  reason:
    'This tool is not exposed until its permission overlay, hooks, result storage, and validation tranche land.'
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
    runtime: SDK_READ_RUNTIME
  };
}

function chiralityReadMcpDescriptor(input: {
  name: string;
  aliases: readonly string[];
  description: string;
  mcpToolName: ChiralityMcpReadToolName;
  inputSchema: Record<string, unknown>;
  outputSchema?: Record<string, unknown>;
}): HarnessToolDescriptor {
  return {
    name: input.name,
    aliases: [
      ...input.aliases,
      input.mcpToolName,
      toChiralityMcpAllowedToolName(input.mcpToolName)
    ],
    description: input.description,
    surface: 'chirality-mcp',
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
        toolName: toChiralityMcpAllowedToolName(input.mcpToolName)
      }
    },
    inputSchema: input.inputSchema,
    outputSchema: input.outputSchema,
    runtime: CHIRALITY_READ_MCP_RUNTIME
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
  chiralityReadMcpDescriptor({
    name: 'status_read',
    aliases: ['status', 'mcp.status_read'],
    description: 'Read parsed lifecycle state from a project-root-contained deliverable _STATUS.md.',
    mcpToolName: 'status_read',
    inputSchema: {
      type: 'object',
      required: ['deliverablePath'],
      properties: {
        deliverablePath: {
          type: 'string'
        }
      }
    },
    outputSchema: {
      type: 'object',
      required: ['projectRoot', 'deliverablePath', 'statusFilePath', 'status']
    }
  }),
  chiralityReadMcpDescriptor({
    name: 'dependency_read',
    aliases: ['dependencies', 'deps', 'deps_read', 'mcp.deps_read'],
    description: 'Read parsed dependency rows and warnings from a deliverable Dependencies.csv.',
    mcpToolName: 'deps_read',
    inputSchema: {
      type: 'object',
      required: ['deliverablePath'],
      properties: {
        deliverablePath: {
          type: 'string'
        }
      }
    },
    outputSchema: {
      type: 'object',
      required: ['projectRoot', 'deliverablePath', 'dependenciesFilePath', 'headers', 'rows', 'warnings']
    }
  }),
  chiralityReadMcpDescriptor({
    name: 'scope_scan',
    aliases: ['scope', 'mcp.scope_scan'],
    description: 'Scan deliverable and knowledge-type scopes inside the selected project root.',
    mcpToolName: 'scope_scan',
    inputSchema: {
      type: 'object',
      properties: {}
    },
    outputSchema: {
      type: 'object',
      required: ['projectRoot', 'deliverables', 'knowledgeTypes', 'truncated']
    }
  }),
  chiralityReadMcpDescriptor({
    name: 'scaffold_preview',
    aliases: ['scaffold_dry_run', 'mcp.scaffold_preview'],
    description: 'Preview execution-root scaffold paths from decomposition markdown without writing files.',
    mcpToolName: 'scaffold_preview',
    inputSchema: {
      type: 'object',
      required: ['executionRoot', 'decompositionPath'],
      properties: {
        executionRoot: {
          type: 'string'
        },
        decompositionPath: {
          type: 'string'
        },
        projectName: {
          type: 'string'
        },
        coordinationMode: {
          type: 'string'
        }
      }
    },
    outputSchema: {
      type: 'object',
      required: ['executionRoot', 'decompositionPath', 'planned', 'packages']
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
    runtime: SDK_WRITE_RUNTIME
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
    runtime: SDK_WRITE_RUNTIME
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
    description: 'Run a project-root-contained shell command after shell policy and audit controls pass.',
    surface: 'claude-agent-sdk-builtin',
    permissions: ['shell', 'workspace-write', 'danger'],
    pathScope: 'project-root-write',
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
      reason: 'Shell execution requires governed workspace mode, timeout, hook, and audit policy.'
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
        },
        timeout: {
          type: 'number'
        },
        description: {
          type: 'string'
        },
        run_in_background: {
          type: 'boolean'
        },
        dangerouslyDisableSandbox: {
          type: 'boolean'
        }
      }
    },
    runtime: SDK_SHELL_RUNTIME
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

function getSdkToolName(descriptor: HarnessToolDescriptor): ClaudeAgentSdkToolName | undefined {
  return descriptor.adapter.claudeAgentSdk?.toolName;
}

export function getCurrentTrancheDisallowedToolNames(
  allowedToolNames: readonly ClaudeAgentSdkToolName[] = []
): ClaudeAgentSdkToolName[] {
  const allowed = new Set(allowedToolNames);
  return uniqueValues(
    HARNESS_TOOL_DESCRIPTORS.flatMap((descriptor) => {
      const sdkToolName = getSdkToolName(descriptor);
      return sdkToolName && !allowed.has(sdkToolName) ? [sdkToolName] : [];
    })
  );
}

export function resolveHarnessToolPool(input: {
  sessionId?: string;
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
  const permissionDecisions: HarnessPermissionDecision[] = [];
  const allowedToolNames: ClaudeAgentSdkToolName[] = [];
  const seenDescriptors = new Set<string>();
  const knownTools = getKnownHarnessToolNames();

  for (const toolName of requestedTools) {
    const descriptor = getHarnessToolDescriptor(toolName);
    if (!descriptor) {
      permissionDecisions.push(
        resolveHarnessPermissionDecision({
          sessionId: input.sessionId,
          toolName,
          mode: input.mode,
          source: 'chirality-policy'
        })
      );
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
      const decision = resolveHarnessPermissionDecision({
        sessionId: input.sessionId,
        toolName,
        mode: input.mode,
        descriptor,
        source: 'chirality-policy'
      });
      permissionDecisions.push(decision);

      const sdkToolName = getSdkToolName(descriptor);
      if (decision.decision === 'allow' && descriptor.runtime.exposedToModel && sdkToolName) {
        allowedToolNames.push(sdkToolName);
      } else {
        deniedTools.push({
          type: 'DENIED_BY_CURRENT_PHASE',
          toolName,
          descriptorName: descriptor.name,
          message: descriptor.runtime.exposedToModel ? decision.reason : descriptor.runtime.reason
        });
      }
    }
  }

  return {
    registryVersion: HARNESS_TOOL_REGISTRY_VERSION,
    mode: input.mode ?? 'default',
    requestedTools,
    requestedDescriptors,
    permissionDecisions,
    allowedToolNames: uniqueValues(allowedToolNames),
    disallowedToolNames: getCurrentTrancheDisallowedToolNames(allowedToolNames),
    deniedTools,
    unknownTools,
    issues: [...unknownTools, ...deniedTools]
  };
}
