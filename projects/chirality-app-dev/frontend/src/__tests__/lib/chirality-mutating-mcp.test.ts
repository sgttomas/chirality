import { mkdir, mkdtemp, readFile, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { serializeDependencyRegister } from '../../lib/dependencies/register-writer';
import type { DependencyRegisterRow } from '../../lib/dependencies/schema';
import {
  dependenciesWriteTool,
  statusTransitionTool
} from '../../lib/harness/mcp/read-tools';
import { replayHarnessEvents } from '../../lib/harness/session-events';
import { writeAmendmentRecords } from './amendment-records-fixture';

const INITIALIZED_STATUS_DOCUMENT = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** INITIALIZED
**Last Updated:** 2026-02-22

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
`;

const IN_PROGRESS_STATUS_DOCUMENT = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** IN_PROGRESS
**Last Updated:** 2026-02-24

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)
`;

type FixtureContext = {
  tmpRoot: string;
  projectRoot: string;
  deliverablePath: string;
};

let fixture: FixtureContext;
const sessionId = 'sess_chirality_mutating_mcp';

function makeDependencyRow(overrides: Partial<DependencyRegisterRow> = {}): DependencyRegisterRow {
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
    SatisfactionStatus: 'IN_PROGRESS',
    Confidence: 'HIGH',
    Origin: 'EXTRACTED',
    FirstSeen: '2026-02-22',
    LastSeen: '2026-02-22',
    Status: 'ACTIVE',
    Notes: '',
    ...overrides
  };
}

function parseJsonToolResult<T>(
  result: Awaited<ReturnType<typeof statusTransitionTool>>
): T {
  const first = result.content[0];
  if (!first || first.type !== 'text') {
    throw new Error('Expected text MCP result');
  }
  return JSON.parse(first.text) as T;
}

beforeEach(async () => {
  const tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-mutating-mcp-'));
  const projectRoot = path.join(tmpRoot, 'project-root');
  const deliverablePath = path.join(
    projectRoot,
    'PKG-05_Filesystem_Execution_Model',
    '1_Working',
    'DEL-05-03_Lifecycle_State_Handling'
  );

  await mkdir(deliverablePath, { recursive: true });
  await writeFile(path.join(deliverablePath, '_STATUS.md'), INITIALIZED_STATUS_DOCUMENT, 'utf8');
  await writeFile(
    path.join(deliverablePath, 'Dependencies.csv'),
    serializeDependencyRegister([makeDependencyRow()], { hostDeliverableId: 'DEL-05-03' }).csv,
    'utf8'
  );

  fixture = {
    tmpRoot,
    projectRoot,
    deliverablePath
  };
  process.env.CHIRALITY_SESSION_ROOT = path.join(tmpRoot, 'sessions');
});

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  await rm(fixture.tmpRoot, { recursive: true, force: true });
});

describe('Chirality mutating MCP tools', () => {
  it('applies a status transition in workspaceWrite and records metadata-only evidence', async () => {
    const result = parseJsonToolResult<{
      transition: { from: string; to: string; actor: string };
      status: { currentState: string; historyLength: number };
    }>(
      await statusTransitionTool(
        { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' },
        {
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        }
      )
    );

    expect(result.transition).toEqual({
      from: 'INITIALIZED',
      to: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS'
    });
    expect(result.status).toMatchObject({
      currentState: 'IN_PROGRESS',
      historyLength: 3
    });
    await expect(readFile(path.join(fixture.deliverablePath, '_STATUS.md'), 'utf8')).resolves.toContain(
      '**Current State:** IN_PROGRESS'
    );

    const replay = await replayHarnessEvents(sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'tool.started',
      'tool.permission',
      'tool.completed'
    ]);
    expect(replay.events[1].data).toMatchObject({
      behavior: 'allow',
      toolName: 'mcp__chirality__status_transition',
      descriptorName: 'status_transition',
      mode: 'workspaceWrite'
    });
    expect(replay.events[2].data).toMatchObject({
      source: 'chirality-mcp',
      toolName: 'status_transition',
      adapterToolName: 'mcp__chirality__status_transition',
      fileEvidence: {
        before: {
          exists: true,
          sha256: expect.any(String),
          byteLength: expect.any(Number)
        },
        after: {
          exists: true,
          sha256: expect.any(String),
          byteLength: expect.any(Number)
        },
        diffSummary: {
          shaChanged: true
        }
      }
    });
    expect(JSON.stringify(replay.events[2].data)).not.toContain('State set to IN_PROGRESS');
  });

  it('requires workspaceWrite for mutating status transitions', async () => {
    await expect(
      statusTransitionTool(
        { projectRoot: fixture.projectRoot, sessionId, mode: 'readOnly' },
        {
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        }
      )
    ).rejects.toMatchObject({
      type: 'INVALID_REQUEST',
      status: 403,
      message: expect.stringContaining('denied in readOnly mode')
    });

    await expect(readFile(path.join(fixture.deliverablePath, '_STATUS.md'), 'utf8')).resolves.toContain(
      '**Current State:** INITIALIZED'
    );
  });

  it('allows HUMAN approvalSha transitions through the lifecycle engine', async () => {
    await writeFile(path.join(fixture.deliverablePath, '_STATUS.md'), IN_PROGRESS_STATUS_DOCUMENT, 'utf8');

    const result = parseJsonToolResult<{
      transition: { from: string; to: string; actor: string };
      status: { currentState: string };
    }>(
      await statusTransitionTool(
        { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' },
        {
          deliverablePath: fixture.deliverablePath,
          targetState: 'CHECKING',
          actor: 'HUMAN',
          date: '2026-02-25',
          approvalSha: 'abc1234'
        }
      )
    );

    expect(result.transition).toEqual({
      from: 'IN_PROGRESS',
      to: 'CHECKING',
      actor: 'HUMAN'
    });
    expect(result.status.currentState).toBe('CHECKING');
    await expect(readFile(path.join(fixture.deliverablePath, '_STATUS.md'), 'utf8')).resolves.toContain(
      '**Checking Approval SHA:** abc1234'
    );
  });

  it('applies the human-ruled CHECKING reversal only with the full human-gate evidence', async () => {
    const checking = IN_PROGRESS_STATUS_DOCUMENT.replace(
      '**Current State:** IN_PROGRESS',
      '**Current State:** CHECKING'
    ).concat('- 2026-02-25 - State set to CHECKING (HUMAN)\n');
    const statusPath = path.join(fixture.deliverablePath, '_STATUS.md');
    await writeFile(statusPath, checking, 'utf8');
    await mkdir(path.join(fixture.projectRoot, '_DECISIONS'), { recursive: true });
    await writeFile(path.join(fixture.projectRoot, '_DECISIONS', 'D-001.md'), '# Ruling\n', 'utf8');
    const context = { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' as const };
    const base = {
      deliverablePath: fixture.deliverablePath,
      targetState: 'IN_PROGRESS',
      date: '2026-02-26'
    };

    // The tool rejects the reversal for HUMAN with neither SHA nor ruling, with a
    // ruling but no SHA, with a SHA but no ruling, and for an agent actor. The
    // actor is caller-asserted: HUMAN with a well-formed SHA and a real ruling file
    // passes (App SPEC §4.3 known limit).
    for (const [args, code] of [
      [{ ...base, actor: 'HUMAN' }, 'APPROVAL_SHA_REQUIRED'],
      [{ ...base, actor: 'HUMAN', ruling: '_DECISIONS/D-001.md' }, 'APPROVAL_SHA_REQUIRED'],
      [{ ...base, actor: 'HUMAN', approvalSha: 'abc1234' }, 'RULING_REQUIRED'],
      [
        { ...base, actor: 'WORKING_ITEMS', approvalSha: 'abc1234', ruling: '_DECISIONS/D-001.md' },
        'UNAUTHORIZED_ACTOR'
      ]
    ] as const) {
      await expect(statusTransitionTool(context, args)).rejects.toMatchObject({ code });
      await expect(readFile(statusPath, 'utf8')).resolves.toBe(checking);
    }

    const result = parseJsonToolResult<{
      transition: { from: string; to: string; actor: string };
      status: { currentState: string };
    }>(
      await statusTransitionTool(context, {
        ...base,
        actor: 'HUMAN',
        approvalSha: 'abc1234',
        ruling: '_DECISIONS/D-001.md'
      })
    );

    expect(result.transition).toEqual({ from: 'CHECKING', to: 'IN_PROGRESS', actor: 'HUMAN' });
    await expect(readFile(statusPath, 'utf8')).resolves.toContain(
      '[reversal from CHECKING; ruling: _DECISIONS/D-001.md; approval SHA: abc1234]'
    );
  });

  it('keeps ISSUED -> IN_PROGRESS rejected through the MCP tool', async () => {
    const issued = IN_PROGRESS_STATUS_DOCUMENT.replace(
      '**Current State:** IN_PROGRESS',
      '**Current State:** ISSUED'
    ).concat('- 2026-02-25 - State set to ISSUED (HUMAN)\n');
    const statusPath = path.join(fixture.deliverablePath, '_STATUS.md');
    await writeFile(statusPath, issued, 'utf8');
    await mkdir(path.join(fixture.projectRoot, '_DECISIONS'), { recursive: true });
    await writeFile(path.join(fixture.projectRoot, '_DECISIONS', 'D-001.md'), '# Ruling\n', 'utf8');

    await expect(
      statusTransitionTool(
        { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' },
        {
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'HUMAN',
          date: '2026-02-26',
          approvalSha: 'abc1234',
          ruling: '_DECISIONS/D-001.md'
        }
      )
    ).rejects.toMatchObject({ code: 'BACKWARD_TRANSITION' });
    await expect(readFile(statusPath, 'utf8')).resolves.toBe(issued);
  });

  it('reopens ISSUED -> IN_PROGRESS through the MCP tool only with a HUMAN actor and an admitted amendment', async () => {
    const issued = IN_PROGRESS_STATUS_DOCUMENT.replace(
      '**Current State:** IN_PROGRESS',
      '**Current State:** ISSUED'
    ).concat('- 2026-02-25 - State set to ISSUED (HUMAN)\n');
    const statusPath = path.join(fixture.deliverablePath, '_STATUS.md');
    await writeFile(statusPath, issued, 'utf8');
    await writeAmendmentRecords({
      scopeChangeRoot: path.join(fixture.projectRoot, '_ScopeChange'),
      manifestBase: fixture.projectRoot,
      rows: [
        { AmendmentID: 'SCA-001', ActionSeq: '1', ActionType: 'MODIFY', EntityType: 'DELIVERABLE', EntityID: 'DEL-05-03', ScopeChanging: 'NO' }
      ]
    });
    const context = { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' as const };
    const base = {
      deliverablePath: fixture.deliverablePath,
      targetState: 'IN_PROGRESS',
      date: '2026-02-26',
      approvalSha: 'abc1234'
    };

    for (const [args, code] of [
      [{ ...base, actor: 'WORKING_ITEMS', amendment: 'SCA-001' }, 'UNAUTHORIZED_ACTOR'],
      [{ ...base, actor: 'HUMAN', amendment: 'SCA-002' }, 'AMENDMENT_NOT_ADMITTED'],
      [{ ...base, actor: 'HUMAN' }, 'BACKWARD_TRANSITION']
    ] as const) {
      await expect(statusTransitionTool(context, args)).rejects.toMatchObject({ code });
      await expect(readFile(statusPath, 'utf8')).resolves.toBe(issued);
    }

    const result = parseJsonToolResult<{ transition: { from: string; to: string } }>(
      await statusTransitionTool(context, { ...base, actor: 'HUMAN', amendment: 'SCA-001' })
    );
    expect(result.transition).toMatchObject({ from: 'ISSUED', to: 'IN_PROGRESS' });
    await expect(readFile(statusPath, 'utf8')).resolves.toContain(
      '[reopened from ISSUED; amendment: SCA-001 (_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26); ' +
        'action: _ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv ActionSeq 1 MODIFY;'
    );
  });

  it('refuses gate-evidence metadata from an agent actor through the MCP tool', async () => {
    const statusPath = path.join(fixture.deliverablePath, '_STATUS.md');
    const before = await readFile(statusPath, 'utf8');
    const context = { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' as const };
    const base = { deliverablePath: fixture.deliverablePath, targetState: 'IN_PROGRESS', date: '2026-02-26' };

    await expect(
      statusTransitionTool(context, {
        ...base,
        actor: 'WORKING_ITEMS',
        metadata: { 'Authorization Basis': 'agent-asserted ruling' }
      })
    ).rejects.toMatchObject({ code: 'INVALID_METADATA' });
    await expect(readFile(statusPath, 'utf8')).resolves.toBe(before);

    await statusTransitionTool(context, {
      ...base,
      actor: 'HUMAN',
      metadata: { 'Authorization Basis': 'owner ruling D-001' }
    });
    await expect(readFile(statusPath, 'utf8')).resolves.toContain('**Authorization Basis:** owner ruling D-001');
  });

  it('writes Dependencies.csv through v3.1 writer semantics without event row payloads', async () => {
    const nextRow = makeDependencyRow({
      SatisfactionStatus: 'SATISFIED',
      LastSeen: '2026-02-23'
    });

    const result = parseJsonToolResult<{
      rowCount: number;
      warningCount: number;
      warnings: string[];
    }>(
      await dependenciesWriteTool(
        { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' },
        {
          deliverablePath: fixture.deliverablePath,
          rows: [nextRow]
        }
      )
    );

    expect(result).toMatchObject({
      rowCount: 1,
      warningCount: 1,
      warnings: ['ANCHOR_IMPLEMENTS_NODE_COUNT_NOT_ONE']
    });
    await expect(
      readFile(path.join(fixture.deliverablePath, 'Dependencies.csv'), 'utf8')
    ).resolves.toContain('SATISFIED');

    const replay = await replayHarnessEvents(sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'tool.started',
      'tool.permission',
      'tool.completed'
    ]);
    expect(replay.events[2].data).toMatchObject({
      source: 'chirality-mcp',
      toolName: 'dependency_write',
      adapterToolName: 'mcp__chirality__deps_write',
      resultSummary: {
        rowCount: 1,
        warningCount: 1
      }
    });
    expect(JSON.stringify(replay.events[2].data)).not.toContain('DEP-05-03-001');
    expect(JSON.stringify(replay.events[2].data)).not.toContain('SATISFIED');
  });

  it('denies symlink target writes before the lifecycle engine runs', async () => {
    const outsideStatusPath = path.join(fixture.tmpRoot, 'outside-status.md');
    await writeFile(outsideStatusPath, INITIALIZED_STATUS_DOCUMENT, 'utf8');
    await rm(path.join(fixture.deliverablePath, '_STATUS.md'));
    await symlink(outsideStatusPath, path.join(fixture.deliverablePath, '_STATUS.md'));

    await expect(
      statusTransitionTool(
        { projectRoot: fixture.projectRoot, sessionId, mode: 'workspaceWrite' },
        {
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        }
      )
    ).rejects.toMatchObject({
      type: 'INVALID_REQUEST',
      status: 403,
      message: expect.stringContaining('crosses symbolic link')
    });

    await expect(readFile(outsideStatusPath, 'utf8')).resolves.toContain(
      '**Current State:** INITIALIZED'
    );
  });
});
