import { NextResponse } from 'next/server';
import {
  errorResponse,
  readJsonBody,
  requireNonEmptyString
} from '../../../../lib/harness/http';
import { getHarnessRuntime } from '../../../../lib/harness/runtime';
import { getPermissionBroker } from '../../../../lib/harness/permission-broker';
import { InterruptRequest } from '@chirality/harness-contract/types';

export async function POST(request: Request): Promise<Response> {
  try {
    const body = await readJsonBody<InterruptRequest>(request);
    const sessionId = requireNonEmptyString(body.sessionId, 'sessionId');

    // Release any approval the turn is suspended on so the interrupt can land.
    getPermissionBroker().clearSession(sessionId, 'deny');

    const runtime = getHarnessRuntime();
    await runtime.turnEngine.interrupt(sessionId);

    return NextResponse.json({ ok: true }, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
