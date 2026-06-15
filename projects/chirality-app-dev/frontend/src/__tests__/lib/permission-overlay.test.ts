import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import {
  createHarnessCanUseTool,
  HARNESS_PERMISSION_POLICY_VERSION,
  permissionDecisionToSdkResult,
  resolveHarnessPermissionDecision
} from '../../lib/harness/permission-overlay';
import { replayHarnessEvents } from '../../lib/harness/session-events';
import { getHarnessToolDescriptor } from '../../lib/harness/tool-descriptor';

const sessionId = 'sess_permission_overlay';
let tmpDir = '';

async function useTempSessionRoot(): Promise<void> {
  tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-permission-overlay-'));
  process.env.CHIRALITY_SESSION_ROOT = path.join(tmpDir, 'sessions');
}

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

function decisionFor(toolName: string, mode: string, explicitDeny = false) {
  return resolveHarnessPermissionDecision({
    sessionId,
    toolName,
    mode,
    descriptor: getHarnessToolDescriptor(toolName),
    explicitDeny,
    explicitDenyReason: explicitDeny ? 'Test hard deny.' : undefined
  });
}

describe('permission overlay', () => {
  it('allows read-class tools at the abstract policy layer', () => {
    const decision = decisionFor('Read', 'readOnly');

    expect(decision).toMatchObject({
      sessionId,
      toolName: 'Read',
      decision: 'allow',
      source: 'chirality-policy',
      reason: expect.stringContaining('allowed')
    });
    expect(decision.safeMetadata).toMatchObject({
      policyVersion: HARNESS_PERMISSION_POLICY_VERSION,
      mode: 'readOnly',
      descriptorName: 'read_file',
      adapterToolName: 'Read',
      allowClass: 'read'
    });
  });

  it('requires application approval for governed write surfaces in ask mode', () => {
    const decision = decisionFor('Write', 'ask');

    expect(decision).toMatchObject({
      decision: 'ask',
      reason: expect.stringContaining('requires interactive approval')
    });
    expect(decision.safeMetadata).toMatchObject({
      mode: 'ask',
      descriptorName: 'write_file',
      requiresHumanApproval: true
    });

    expect(permissionDecisionToSdkResult(decision, 'tool_1')).toMatchObject({
      behavior: 'deny',
      message: expect.stringContaining('requires application approval'),
      toolUseID: 'tool_1'
    });
  });

  it('lets explicit hard denies override abstract allow and ask decisions', () => {
    const readDecision = decisionFor('Read', 'readOnly', true);
    const writeDecision = decisionFor('Write', 'ask', true);

    expect(readDecision).toMatchObject({
      decision: 'deny',
      reason: 'Test hard deny.'
    });
    expect(readDecision.safeMetadata).toMatchObject({ hardDeny: true });
    expect(writeDecision).toMatchObject({
      decision: 'deny',
      reason: 'Test hard deny.'
    });
    expect(writeDecision.safeMetadata).toMatchObject({ hardDeny: true });
  });

  it('denies unapproved write, shell, network, subagent, and unknown tools in dontAsk mode', () => {
    const decisions = ['Write', 'Bash', 'WebFetch', 'Agent', 'mystery'].map((toolName) =>
      decisionFor(toolName, 'dontAsk')
    );

    expect(decisions.map((decision) => decision.decision)).toEqual([
      'deny',
      'deny',
      'deny',
      'deny',
      'deny'
    ]);
    expect(decisions.map((decision) => decision.safeMetadata?.denyClass)).toEqual([
      'workspace-write',
      'danger',
      'reserved-tool',
      'subagent',
      'unknown-tool'
    ]);
  });

  it('keeps bypass mode subject to Chirality hard-deny rules', () => {
    const safeRead = decisionFor('Read', 'bypass');
    const shell = decisionFor('Bash', 'bypass');
    const explicit = decisionFor('Read', 'bypass', true);

    expect(safeRead.decision).toBe('allow');
    expect(shell).toMatchObject({
      decision: 'deny',
      reason: expect.stringContaining('danger-class capability')
    });
    expect(explicit).toMatchObject({
      decision: 'deny',
      reason: 'Test hard deny.'
    });
  });

  it('hard-denies path-bearing read callbacks outside the active project root', async () => {
    await useTempSessionRoot();
    const canUseTool = createHarnessCanUseTool({
      sessionId,
      mode: 'readOnly',
      projectRoot: '/tmp/project',
      resolveDescriptor: getHarnessToolDescriptor
    });

    await expect(
      canUseTool(
        'Read',
        { file_path: '../outside.md' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_outside'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'deny',
      message: expect.stringContaining('outside the active project root'),
      toolUseID: 'tool_outside'
    });

    await expect(
      canUseTool(
        'LS',
        { path: 'PKG-01' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_inside'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'allow',
      toolUseID: 'tool_inside'
    });

    const replay = await replayHarnessEvents(sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'tool.permission',
      'tool.permission'
    ]);
    expect(replay.events[0]).toMatchObject({
      sessionId,
      type: 'tool.permission',
      data: {
        behavior: 'deny',
        decisionId: expect.stringMatching(/^perm_/),
        descriptorName: 'read_file',
        adapterToolName: 'Read',
        mode: 'readOnly',
        surface: 'claude-agent-sdk-builtin'
      }
    });
    expect(replay.events[0].data.safeMetadata).toMatchObject({
      inputMetadata: {
        inputKeys: ['file_path'],
        pathFields: {
          file_path: '../outside.md'
        }
      },
      denyClass: 'path-containment'
    });
    expect(replay.events[1]).toMatchObject({
      type: 'tool.permission',
      data: {
        behavior: 'allow',
        descriptorName: 'list_files',
        adapterToolName: 'LS'
      }
    });
  });
});
