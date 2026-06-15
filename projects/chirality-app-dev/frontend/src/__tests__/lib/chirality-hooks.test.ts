import { mkdir, mkdtemp, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { createChiralityToolHooks } from '../../lib/harness/chirality-hooks';
import { replayHarnessEvents } from '../../lib/harness/session-events';
import { getHarnessToolDescriptor } from '../../lib/harness/tool-descriptor';

const sessionId = 'sess_chirality_hooks';
let tmpDir = '';
let projectRoot = '';
let instructionRoot = '';

beforeEach(async () => {
  tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-hooks-'));
  projectRoot = path.join(tmpDir, 'project');
  instructionRoot = path.join(projectRoot, 'instruction-root');
  await mkdir(projectRoot, { recursive: true });
  await mkdir(instructionRoot, { recursive: true });
  process.env.CHIRALITY_SESSION_ROOT = path.join(tmpDir, 'sessions');
  process.env.CHIRALITY_INSTRUCTION_ROOT = instructionRoot;
});

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  delete process.env.CHIRALITY_INSTRUCTION_ROOT;
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

function getHooks() {
  return createChiralityToolHooks({
    sessionId,
    projectRoot,
    instructionRoot,
    resolveDescriptor: getHarnessToolDescriptor
  });
}

describe('Chirality write hooks', () => {
  it('allows project-root-contained Write and records post-write provenance metadata', async () => {
    const hooks = getHooks();
    const preToolUse = hooks.PreToolUse?.[0]?.hooks[0];
    const postToolUse = hooks.PostToolUse?.[0]?.hooks[0];
    expect(preToolUse).toBeTypeOf('function');
    expect(postToolUse).toBeTypeOf('function');

    const preResult = await preToolUse?.(
      {
        hook_event_name: 'PreToolUse',
        tool_name: 'Write',
        tool_input: {
          file_path: 'notes.md',
          content: 'after'
        },
        tool_use_id: 'tool_write'
      } as never,
      'tool_write',
      { signal: new AbortController().signal }
    );

    expect(preResult).toMatchObject({
      continue: true,
      hookSpecificOutput: {
        hookEventName: 'PreToolUse',
        permissionDecision: 'allow'
      }
    });

    await writeFile(path.join(projectRoot, 'notes.md'), 'after', 'utf8');

    const postResult = await postToolUse?.(
      {
        hook_event_name: 'PostToolUse',
        tool_name: 'Write',
        tool_input: {
          file_path: 'notes.md'
        },
        tool_response: {
          ok: true
        },
        tool_use_id: 'tool_write',
        duration_ms: 7
      } as never,
      'tool_write',
      { signal: new AbortController().signal }
    );

    expect(postResult).toMatchObject({
      continue: true,
      hookSpecificOutput: {
        hookEventName: 'PostToolUse'
      }
    });

    const replay = await replayHarnessEvents(sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'hook.started',
      'hook.completed',
      'hook.started',
      'hook.completed'
    ]);
    expect(replay.events[1].data).toMatchObject({
      hookName: 'chirality.write.pre_tool_use',
      decision: 'approve',
      descriptorName: 'write_file',
      pathMetadata: {
        rawPath: 'notes.md',
        resolvedPath: path.join(projectRoot, 'notes.md'),
        pathScope: 'project-root-write'
      },
      beforeState: {
        exists: false
      },
      recordsDiff: true
    });
    expect(replay.events[3].data).toMatchObject({
      hookName: 'chirality.write.post_tool_use',
      descriptorName: 'write_file',
      beforeState: {
        exists: false
      },
      afterState: {
        exists: true,
        kind: 'file',
        byteLength: 5,
        sha256: expect.any(String)
      },
      resultMetadata: {
        rawOutputPersisted: false
      },
      recordsDiff: true
    });
  });

  it('blocks outside-root, instruction-root, and symlink write attempts', async () => {
    const externalRoot = path.join(tmpDir, 'external');
    await mkdir(externalRoot, { recursive: true });
    await writeFile(path.join(externalRoot, 'target.md'), 'outside', 'utf8');
    await symlink(externalRoot, path.join(projectRoot, 'linked'));

    const preToolUse = getHooks().PreToolUse?.[0]?.hooks[0];

    const outside = await preToolUse?.(
      {
        hook_event_name: 'PreToolUse',
        tool_name: 'Write',
        tool_input: {
          file_path: '../outside.md',
          content: 'outside'
        },
        tool_use_id: 'tool_outside'
      } as never,
      'tool_outside',
      { signal: new AbortController().signal }
    );
    const instruction = await preToolUse?.(
      {
        hook_event_name: 'PreToolUse',
        tool_name: 'Edit',
        tool_input: {
          file_path: path.join(instructionRoot, 'AGENT.md'),
          old_string: 'a',
          new_string: 'b'
        },
        tool_use_id: 'tool_instruction'
      } as never,
      'tool_instruction',
      { signal: new AbortController().signal }
    );
    const symlinked = await preToolUse?.(
      {
        hook_event_name: 'PreToolUse',
        tool_name: 'Write',
        tool_input: {
          file_path: 'linked/target.md',
          content: 'through symlink'
        },
        tool_use_id: 'tool_symlink'
      } as never,
      'tool_symlink',
      { signal: new AbortController().signal }
    );

    expect(outside).toMatchObject({
      continue: false,
      decision: 'block',
      hookSpecificOutput: {
        permissionDecision: 'deny'
      }
    });
    expect(JSON.stringify(outside)).toContain('outside the active project root');
    expect(instruction).toMatchObject({
      continue: false,
      decision: 'block',
      hookSpecificOutput: {
        permissionDecision: 'deny'
      }
    });
    expect(JSON.stringify(instruction)).toContain('instruction root');
    expect(symlinked).toMatchObject({
      continue: false,
      decision: 'block',
      hookSpecificOutput: {
        permissionDecision: 'deny'
      }
    });
    expect(JSON.stringify(symlinked)).toContain('symbolic link');

    const replay = await replayHarnessEvents(sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'hook.started',
      'hook.completed',
      'hook.started',
      'hook.completed',
      'hook.started',
      'hook.completed'
    ]);
    expect(replay.events[1].data.safeMetadata).toMatchObject({
      denyClass: 'path-containment'
    });
    expect(replay.events[3].data.safeMetadata).toMatchObject({
      denyClass: 'instruction-root'
    });
    expect(replay.events[5].data.safeMetadata).toMatchObject({
      denyClass: 'symlink-write'
    });
  });
});
