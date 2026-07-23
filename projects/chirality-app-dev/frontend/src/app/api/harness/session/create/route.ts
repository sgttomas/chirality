import { NextResponse } from 'next/server';
import {
  errorResponse,
  readJsonBody,
  requireNonEmptyString
} from '../../../../../lib/harness/http';
import { getDaemonHarnessPort } from '../../../../../lib/runtime-client/daemon-harness-port';
import { SessionCreateRequest } from '@chirality/harness-contract/types';

export async function POST(request: Request): Promise<Response> {
  try {
    const body = await readJsonBody<SessionCreateRequest>(request);
    const projectRoot = requireNonEmptyString(body.projectRoot, 'projectRoot');

    const result = await getDaemonHarnessPort().createSession(
      {
        projectRoot,
        persona: body.persona,
        mode: body.mode
      },
      { signal: request.signal }
    );
    return NextResponse.json(result, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
