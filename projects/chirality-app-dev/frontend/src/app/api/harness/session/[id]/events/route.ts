import { NextResponse } from 'next/server';
import { HarnessError } from '@chirality/harness-contract/errors';
import { errorResponse, requireNonEmptyString } from '../../../../../../lib/harness/http';
import { getHarnessRuntime } from '../../../../../../lib/harness/runtime';
import { replayHarnessEvents } from '../../../../../../lib/harness/session-events';
import { deriveTranscriptView } from '@chirality/harness-contract/transcript-replay';

type RouteContext = {
  params: {
    id: string;
  };
};

/**
 * GET /api/harness/session/[id]/events — replay a session's persisted
 * `events.jsonl` (D-APP-22 hydrate-on-open). Returns the parsed events plus the
 * honest `malformedLineCount` and a summary; reuses `replayHarnessEvents` (no
 * forked parser). A missing log yields an empty replay, not an error.
 */
export async function GET(_request: Request, context: RouteContext): Promise<Response> {
  try {
    const sessionId = requireNonEmptyString(context.params.id, 'id');
    // The id is joined into an on-disk events path; reject separators / `..`
    // so a crafted id can never traverse outside the session store.
    if (sessionId.includes('/') || sessionId.includes('\\') || sessionId.includes('..')) {
      throw new HarnessError('INVALID_REQUEST', 400, `Invalid session id '${sessionId}'`);
    }

    const runtime = getHarnessRuntime();
    const session = await runtime.sessionManager.getById(sessionId);
    const replay = await replayHarnessEvents(sessionId);
    const transcript = deriveTranscriptView(replay.events, session);
    return NextResponse.json({ ...replay, session, transcript }, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
