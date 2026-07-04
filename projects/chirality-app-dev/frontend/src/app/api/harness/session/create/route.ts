import { NextResponse } from 'next/server';
import { assertDirectChatPersona } from '../../../../../lib/harness/agent-roster';
import {
  errorResponse,
  readJsonBody,
  requireNonEmptyString
} from '../../../../../lib/harness/http';
import { getHarnessRuntime } from '../../../../../lib/harness/runtime';
import { SessionCreateRequest } from '@chirality/harness-contract/types';
import { CHAT_SECTION } from '../../../../../lib/shell/loop-first';

export async function POST(request: Request): Promise<Response> {
  try {
    const body = await readJsonBody<SessionCreateRequest>(request);
    const projectRoot = requireNonEmptyString(body.projectRoot, 'projectRoot');

    // D-APP-24: the direct-chat surface is restricted to Type-0/Type-1 personas.
    // Enforce it server-side (not only in the picker) so a hand-edited
    // `/chat?agent=<Type-2>` URL cannot boot a task agent as a top-level persona.
    const persona = typeof body.persona === 'string' ? body.persona.trim() : '';
    if (body.mode === CHAT_SECTION && persona) {
      await assertDirectChatPersona(persona);
    }

    const runtime = getHarnessRuntime();
    const session = await runtime.sessionManager.create({
      projectRoot,
      persona: body.persona,
      mode: body.mode
    });

    return NextResponse.json({ session }, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
