import { NextResponse } from 'next/server';
import { HarnessError } from '@chirality/harness-contract/errors';
import { errorResponse, readJsonBody, requireNonEmptyString } from '../../../../lib/harness/http';
import { getPermissionBroker, type PermissionVerdict } from '../../../../lib/harness/permission-broker';

type PermissionDecisionRequest = {
  sessionId?: unknown;
  toolUseId?: unknown;
  verdict?: unknown;
};

function requireVerdict(value: unknown): PermissionVerdict {
  if (value === 'allow' || value === 'deny') {
    return value;
  }
  throw new HarnessError('INVALID_REQUEST', 400, "Field 'verdict' must be 'allow' or 'deny'");
}

export async function POST(request: Request): Promise<Response> {
  try {
    const body = await readJsonBody<PermissionDecisionRequest>(request);
    const sessionId = requireNonEmptyString(body.sessionId, 'sessionId');
    const toolUseId = requireNonEmptyString(body.toolUseId, 'toolUseId');
    const verdict = requireVerdict(body.verdict);

    const decided = getPermissionBroker().decide({ sessionId, toolUseId, verdict });

    // `decided: false` means no matching pending request (already resolved, timed
    // out, or never paused) — not an error; the UI reconciles from the event stream.
    return NextResponse.json({ ok: true, decided }, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
