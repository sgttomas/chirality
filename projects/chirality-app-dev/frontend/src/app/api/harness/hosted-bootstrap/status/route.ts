import { NextResponse } from 'next/server';
import { errorResponse, requireNonEmptyString } from '../../../../../lib/harness/http';
import { getHostedBootstrapPort } from '../../../../../lib/runtime-client/daemon-harness-port';

/**
 * Read-only registration probe. This route never returns hosted account
 * status: the daemon requires the Desktop account-host proof for account
 * reads, which only the main-process IPC path can supply.
 */
export async function GET(request: Request): Promise<Response> {
  try {
    const projectRoot = requireNonEmptyString(
      new URL(request.url).searchParams.get('projectRoot'),
      'projectRoot'
    );
    const result = await getHostedBootstrapPort().getStatus(projectRoot, {
      signal: request.signal
    });
    return NextResponse.json(result, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
