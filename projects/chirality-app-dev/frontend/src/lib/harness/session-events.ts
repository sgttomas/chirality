import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { HarnessEvent } from './event-schema';
import { redactJsonLike } from './run-logger';

function getSessionRootDirectory(): string {
  return process.env.CHIRALITY_SESSION_ROOT ?? path.join(process.cwd(), '.chirality', 'sessions');
}

function getSessionEventFilePath(sessionId: string): string {
  return path.join(getSessionRootDirectory(), sessionId, 'events.jsonl');
}

export async function appendHarnessEvent(event: HarnessEvent): Promise<string> {
  const filePath = getSessionEventFilePath(event.sessionId);
  await mkdir(path.dirname(filePath), { recursive: true });
  await writeFile(filePath, `${JSON.stringify(redactJsonLike(event))}\n`, {
    encoding: 'utf8',
    flag: 'a'
  });
  return filePath;
}

export async function replayHarnessEvents(sessionId: string): Promise<{
  events: HarnessEvent[];
  malformedLineCount: number;
}> {
  const filePath = getSessionEventFilePath(sessionId);
  let raw = '';
  try {
    raw = await readFile(filePath, 'utf8');
  } catch {
    return { events: [], malformedLineCount: 0 };
  }

  const events: HarnessEvent[] = [];
  let malformedLineCount = 0;
  for (const line of raw.split('\n')) {
    if (line.trim().length === 0) {
      continue;
    }
    try {
      events.push(JSON.parse(line) as HarnessEvent);
    } catch {
      malformedLineCount += 1;
    }
  }

  return { events, malformedLineCount };
}
