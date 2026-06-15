import { Buffer } from 'node:buffer';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { redactJsonLike } from './run-logger';
import type { HarnessToolDescriptor } from './tool-descriptor';

export type ToolResultArtifactMetadata = {
  artifactPath: string;
  artifactRelativePath: string;
  artifactByteLength: number;
  originalByteLength: number;
  redacted: true;
  truncated: boolean;
};

function getSessionRootDirectory(): string {
  return process.env.CHIRALITY_SESSION_ROOT ?? path.join(process.cwd(), '.chirality', 'sessions');
}

function safePathSegment(value: string | undefined, fallback: string): string {
  const candidate = value?.replace(/[^A-Za-z0-9_.-]/g, '_').slice(0, 80);
  return candidate && candidate.length > 0 ? candidate : fallback;
}

function byteLength(value: string): number {
  return Buffer.byteLength(value, 'utf8');
}

export async function persistToolResultArtifact(input: {
  sessionId: string;
  toolUseId?: string;
  toolName?: string;
  descriptor?: HarnessToolDescriptor;
  result: unknown;
}): Promise<ToolResultArtifactMetadata | undefined> {
  const budget = input.descriptor?.resultBudget;
  if (!budget || budget.overflow !== 'artifact') {
    return undefined;
  }

  const redactedResult = redactJsonLike(input.result);
  const serialized = `${JSON.stringify(
    {
      schemaVersion: 1,
      toolName: input.toolName,
      descriptorName: input.descriptor?.name,
      adapterToolName: input.descriptor?.adapter.claudeAgentSdk?.toolName,
      redacted: true,
      result: redactedResult
    },
    null,
    2
  )}\n`;
  const originalByteLength = byteLength(serialized);
  if (originalByteLength <= budget.inlineByteLimit) {
    return undefined;
  }

  const truncated = originalByteLength > budget.artifactByteLimit;
  const content = truncated
    ? `${JSON.stringify(
        {
          schemaVersion: 1,
          toolName: input.toolName,
          descriptorName: input.descriptor?.name,
          adapterToolName: input.descriptor?.adapter.claudeAgentSdk?.toolName,
          redacted: true,
          truncated: true,
          originalByteLength,
          preview: serialized.slice(0, budget.inlineByteLimit)
        },
        null,
        2
      )}\n`
    : serialized;

  const artifactRelativePath = path.join(
    input.sessionId,
    'artifacts',
    'tools',
    `${safePathSegment(input.toolUseId, 'tool-result')}-${safePathSegment(
      input.toolName,
      'tool'
    )}.json`
  );
  const artifactPath = path.join(getSessionRootDirectory(), artifactRelativePath);
  await mkdir(path.dirname(artifactPath), { recursive: true });
  await writeFile(artifactPath, content, 'utf8');

  return {
    artifactPath,
    artifactRelativePath,
    artifactByteLength: byteLength(content),
    originalByteLength,
    redacted: true,
    truncated
  };
}
