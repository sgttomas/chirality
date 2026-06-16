import { mkdtemp, readFile, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { persistToolResultArtifact } from '../../lib/harness/tool-result-artifacts';
import { getHarnessToolDescriptor } from '../../lib/harness/tool-descriptor';

let tmpDir = '';

beforeEach(async () => {
  tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-tool-artifacts-'));
  process.env.CHIRALITY_SESSION_ROOT = path.join(tmpDir, 'sessions');
});

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  delete process.env.CHIRALITY_ANTHROPIC_API_KEY;
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

describe('tool result artifacts', () => {
  it('skips persistence for inline-sized results', async () => {
    await expect(
      persistToolResultArtifact({
        sessionId: 'sess_artifact',
        toolUseId: 'tool_read',
        toolName: 'Read',
        descriptor: getHarnessToolDescriptor('Read'),
        result: {
          content: [{ type: 'text', text: 'small result' }]
        }
      })
    ).resolves.toBeUndefined();
  });

  it('persists over-inline results as redacted artifact files', async () => {
    process.env.CHIRALITY_ANTHROPIC_API_KEY = 'sk-test-secret';

    const metadata = await persistToolResultArtifact({
      sessionId: 'sess_artifact',
      toolUseId: 'tool_read',
      toolName: 'Read',
      descriptor: getHarnessToolDescriptor('Read'),
      result: {
        content: [{ type: 'text', text: `${'x'.repeat(70 * 1024)} sk-test-secret` }]
      }
    });

    expect(metadata).toMatchObject({
      artifactRelativePath: path.join('sess_artifact', 'artifacts', 'tools', 'tool_read-Read.json'),
      redacted: true,
      truncated: false,
      originalByteLength: expect.any(Number),
      artifactByteLength: expect.any(Number)
    });

    const artifact = await readFile(metadata?.artifactPath as string, 'utf8');
    expect(artifact).not.toContain('sk-test-secret');
    expect(artifact).toContain('[REDACTED_API_KEY]');
  });

  it('truncates results that exceed the artifact budget', async () => {
    const metadata = await persistToolResultArtifact({
      sessionId: 'sess_artifact',
      toolUseId: 'tool_huge',
      toolName: 'Read',
      descriptor: getHarnessToolDescriptor('Read'),
      result: {
        content: [{ type: 'text', text: 'x'.repeat(3 * 1024 * 1024) }]
      }
    });

    expect(metadata).toMatchObject({
      redacted: true,
      truncated: true
    });
    const artifact = await readFile(metadata?.artifactPath as string, 'utf8');
    expect(artifact).toContain('"truncated": true');
    expect(artifact.length).toBeLessThan(128 * 1024);
  });
});
