import { mkdtemp, mkdir, rm, stat, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { serializeDependencyRegister } from '../../lib/dependencies/register-writer';
import type { DependencyRegisterRow } from '../../lib/dependencies/schema';
import {
  createChiralityReadMcpServers,
  dependenciesReadTool,
  scaffoldPreviewTool,
  scopeScanTool,
  statusReadTool
} from '../../lib/harness/mcp/read-tools';

const STATUS_DOCUMENT = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** INITIALIZED
**Last Updated:** 2026-02-22

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
`;

const DECOMPOSITION_DOCUMENT = `# Example System - Software Decomposition

## Packages

| PackageID | Package Name | Description |
|---|---|---|
| PKG-05 | Filesystem Execution Model | Runtime filesystem |

## Deliverables

### PKG-05 - Filesystem Execution Model

| DeliverableID | Name | Type |
|---|---|---|
| DEL-05-03 | Lifecycle State Handling | RUNTIME |
`;

type FixtureContext = {
  tmpRoot: string;
  projectRoot: string;
  deliverablePath: string;
  decompositionPath: string;
};

let fixture: FixtureContext;

function makeDependencyRow(): DependencyRegisterRow {
  return {
    RegisterSchemaVersion: 'v3.1',
    DependencyID: 'DEP-05-03-001',
    FromPackageID: 'PKG-05',
    FromDeliverableID: 'DEL-05-03',
    FromDeliverableName: 'Lifecycle State Handling',
    DependencyClass: 'EXECUTION',
    AnchorType: 'NOT_APPLICABLE',
    Direction: 'UPSTREAM',
    DependencyType: 'PREREQUISITE',
    TargetType: 'DELIVERABLE',
    TargetPackageID: 'PKG-05',
    TargetDeliverableID: 'DEL-05-02',
    TargetRefID: '',
    TargetName: 'Execution Root Scaffolding',
    TargetLocation: '',
    Statement: 'Requires scaffolding baseline before lifecycle transitions',
    EvidenceFile: 'Specification.md',
    SourceRef: 'Specification.md#REQ-01',
    EvidenceQuote: 'Ensure lifecycle is represented by _STATUS.md.',
    Explicitness: 'EXPLICIT',
    RequiredMaturity: 'IN_PROGRESS',
    ProposedMaturity: 'IN_PROGRESS',
    SatisfactionStatus: 'PENDING',
    Confidence: 'HIGH',
    Origin: 'EXTRACTED',
    FirstSeen: '2026-02-22',
    LastSeen: '2026-02-22',
    Status: 'ACTIVE',
    Notes: ''
  };
}

function parseJsonToolResult<T>(result: Awaited<ReturnType<typeof statusReadTool>>): T {
  const first = result.content[0];
  if (!first || first.type !== 'text') {
    throw new Error('Expected text MCP result');
  }
  return JSON.parse(first.text) as T;
}

beforeEach(async () => {
  const tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-read-mcp-'));
  const projectRoot = path.join(tmpRoot, 'project-root');
  const deliverablePath = path.join(
    projectRoot,
    'PKG-05_Filesystem_Execution_Model',
    '1_Working',
    'DEL-05-03_Lifecycle_State_Handling'
  );
  const decompositionDirectory = path.join(projectRoot, '_Decomposition');
  const decompositionPath = path.join(decompositionDirectory, 'decomposition.md');

  await mkdir(deliverablePath, { recursive: true });
  await mkdir(decompositionDirectory, { recursive: true });
  await writeFile(path.join(deliverablePath, '_STATUS.md'), STATUS_DOCUMENT, 'utf8');
  await writeFile(
    path.join(deliverablePath, 'Dependencies.csv'),
    serializeDependencyRegister([makeDependencyRow()], { hostDeliverableId: 'DEL-05-03' }).csv,
    'utf8'
  );
  await writeFile(decompositionPath, DECOMPOSITION_DOCUMENT, 'utf8');

  fixture = {
    tmpRoot,
    projectRoot,
    deliverablePath,
    decompositionPath
  };
});

afterEach(async () => {
  await rm(fixture.tmpRoot, { recursive: true, force: true });
});

describe('Chirality read MCP tools', () => {
  it('reads parsed lifecycle status and dependency register output', async () => {
    const context = { projectRoot: fixture.projectRoot };
    const statusResult = parseJsonToolResult<{
      status: { currentState: string };
      statusFilePath: string;
    }>(
      await statusReadTool(context, {
        deliverablePath: fixture.deliverablePath
      })
    );
    const dependencyResult = parseJsonToolResult<{
      rows: Array<{ DependencyID: string; SatisfactionStatus: string }>;
      warnings: string[];
    }>(
      await dependenciesReadTool(context, {
        deliverablePath: fixture.deliverablePath
      })
    );

    expect(statusResult.status.currentState).toBe('INITIALIZED');
    expect(statusResult.statusFilePath.endsWith('DEL-05-03_Lifecycle_State_Handling/_STATUS.md')).toBe(
      true
    );
    expect(dependencyResult.rows).toHaveLength(1);
    expect(dependencyResult.rows[0]).toMatchObject({
      DependencyID: 'DEP-05-03-001',
      SatisfactionStatus: 'PENDING'
    });
    expect(dependencyResult.warnings).toEqual([]);
  });

  it('scans project scopes without reading document bodies', async () => {
    const result = parseJsonToolResult<{
      projectRoot: string;
      deliverables: Array<{ id: string; path: string }>;
      knowledgeTypes: unknown[];
    }>(await scopeScanTool({ projectRoot: fixture.projectRoot }));

    expect(result.projectRoot).toBe(fixture.projectRoot);
    expect(result.deliverables).toEqual([
      expect.objectContaining({
        id: 'DEL-05-03',
        path: fixture.deliverablePath
      })
    ]);
  });

  it('previews scaffold paths without creating execution-root files', async () => {
    const executionRoot = path.join(fixture.projectRoot, 'execution-preview');
    const result = parseJsonToolResult<{
      executionRoot: string;
      packageCount: number;
      planned: { files: string[] };
    }>(
      await scaffoldPreviewTool(
        { projectRoot: fixture.projectRoot },
        {
          executionRoot,
          decompositionPath: fixture.decompositionPath
        }
      )
    );

    expect(result.executionRoot).toBe(executionRoot);
    expect(result.packageCount).toBe(1);
    expect(result.planned.files).toContain(path.join(executionRoot, 'INIT.md'));
    await expect(stat(executionRoot)).rejects.toMatchObject({ code: 'ENOENT' });
  });

  it('rejects scaffold preview paths outside the active project root', async () => {
    await expect(
      scaffoldPreviewTool(
        { projectRoot: fixture.projectRoot },
        {
          executionRoot: path.join(fixture.tmpRoot, 'outside-project'),
          decompositionPath: fixture.decompositionPath
        }
      )
    ).rejects.toMatchObject({
      type: 'INVALID_REQUEST',
      message: expect.stringContaining('executionRoot must resolve inside projectRoot')
    });
  });

  it('attaches the SDK MCP server only when a read MCP tool is explicitly allowed', () => {
    expect(
      createChiralityReadMcpServers({
        context: { projectRoot: fixture.projectRoot },
        allowedToolNames: []
      })
    ).toEqual({});

    expect(
      createChiralityReadMcpServers({
        context: { projectRoot: fixture.projectRoot },
        allowedToolNames: ['mcp__chirality__status_read']
      })
    ).toMatchObject({
      chirality: {
        type: 'sdk',
        name: 'chirality'
      }
    });
  });
});
