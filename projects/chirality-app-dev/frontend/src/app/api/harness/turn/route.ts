import {
  errorResponse,
  formatSseEvent,
  readJsonBody
} from '../../../../lib/harness/http';
import { getHarnessRuntime } from '../../../../lib/harness/runtime';
import { TurnRequest } from '../../../../lib/harness/types';

export async function POST(request: Request): Promise<Response> {
  try {
    const body = await readJsonBody<TurnRequest>(request);
    const runtime = getHarnessRuntime();
    const runningTurn = await runtime.turnEngine.runTurn(body);

    const encoder = new TextEncoder();
    const stream = new ReadableStream<Uint8Array>({
      async start(controller): Promise<void> {
        try {
          for await (const event of runningTurn.events) {
            controller.enqueue(encoder.encode(formatSseEvent(event.type, event.data)));
          }
        } finally {
          try {
            controller.close();
          } catch {
            // Stream may already be closed/cancelled.
          }
        }
      },
      async cancel(): Promise<void> {
        await runningTurn.cancel();
      }
    });

    return new Response(stream, {
      status: 200,
      headers: {
        'Content-Type': 'text/event-stream; charset=utf-8',
        'Cache-Control': 'no-cache, no-transform',
        Connection: 'keep-alive'
      }
    });
  } catch (error) {
    return errorResponse(error);
  }
}
