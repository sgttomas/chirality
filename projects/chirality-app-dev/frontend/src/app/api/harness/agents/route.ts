import { NextResponse } from 'next/server';
import {
  listAgentRoster,
  selectDirectChatPersonas
} from '../../../../lib/harness/agent-roster';
import { errorResponse } from '../../../../lib/harness/http';

/**
 * GET /api/harness/agents — enumerate the agent roster (name + parsed
 * type/class) for the persona picker. `?directChat=1` restricts the result to
 * Type-0/Type-1 personas (D-APP-24), so the picker can never surface a Type-2
 * task agent for ad-hoc direct chat.
 */
export async function GET(request: Request): Promise<Response> {
  try {
    const url = new URL(request.url);
    const directChatOnly = url.searchParams.get('directChat') === '1';

    const roster = await listAgentRoster();
    const agents = directChatOnly ? selectDirectChatPersonas(roster) : roster;

    return NextResponse.json({ agents }, { status: 200 });
  } catch (error) {
    return errorResponse(error);
  }
}
