/** Test-only deterministic model peer; exact vendor remains the executor. */
import { createServer } from 'node:http';
import { gunzipSync } from 'node:zlib';
import { discoveredTools, nativeSearch } from './response-provider.mjs';
function toolByName(tools, names) {
  const flattened = tools.flatMap(tool => tool.type === 'namespace' && Array.isArray(tool.tools) ? tool.tools.map(member => ({ ...member, namespace: tool.name })) : [tool]);
  const found = flattened.find(tool => tool.type === 'function' && names.includes(tool.name));
  if (!found?.parameters?.properties) return undefined;
  return found;
}
export function summarizeBoundaryOutput(output, who) {
  const started = new RegExp(`^BOUNDARY_${who}_START\\r?$`, 'm').test(output);
  const finished = new RegExp(`^BOUNDARY_${who}_FINISH\\r?$`, 'm').test(output);
  const values = Object.fromEntries(output.split('\n').map(line => /^BOUNDARY_([A-Z_]+):([0-9]{1,3}|PASS|FAIL|ABSENT|PRESENT)\r?$/.exec(line)).filter(Boolean).map(match => [match[1], match[2]]));
  return { started, finished, values };
}
export async function startBoundaryResponseProvider({ root, commandFor }) {
  let count = 0; const issued = new Map(), records = [], failures = [];
  const server = createServer(async (request, response) => {
    try {
      if (request.url !== '/v1/responses' || request.method !== 'POST' || request.headers.authorization) throw new Error('Unexpected owned model request');
      const chunks = []; let size = 0;
      for await (const part of request) { size += part.length; if (size > 2000000) throw new Error('Request bound'); chunks.push(part); }
      const raw = Buffer.concat(chunks); const body = JSON.parse((request.headers['content-encoding'] === 'gzip' ? gunzipSync(raw, { maxOutputLength: 4000000 }) : raw).toString());
      if (++count > 24 || !Array.isArray(body.input) || !Array.isArray(body.tools)) throw new Error('Unexpected model shape');
      const who = JSON.stringify(body.input.filter(item => item.role === 'user').at(-1)?.content ?? '').includes('BOUNDARY_NATIVE_CHILD_ONLY') ? 'child' : 'primary';
      const tools = [...body.tools, ...discoveredTools(body.input, issued)];
      const own = body.input.filter(item => item.type === 'function_call_output' && issued.get(item.call_id)?.who === who).map(item => ({ ...item, issued: issued.get(item.call_id) }));
      for (const item of own) if (item.issued.kind === 'probe' && !records.some(record => record.callId === item.call_id)) {
        const text = typeof item.output === 'string' ? item.output : JSON.stringify(item.output);
        records.push({ who, callId: item.call_id, elapsedMs: Date.now() - item.issued.startedAt, summary: summarizeBoundaryOutput(text, who), supplierFailure: /^exec_command failed(?: for |:)/.test(text) ? text.slice(0, 2048) : null });
      }
      const call = (tool, args, kind) => {
        if ((tool.parameters.required ?? []).some(key => !(key in args))) throw new Error('Unmapped tool argument');
        const call_id = `boundary_${count}`; issued.set(call_id, { who, kind, startedAt: Date.now() });
        return { type: 'function_call', id: `fc_${count}`, call_id, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(args), status: 'completed' };
      };
      const message = text => ({ type: 'message', id: `msg_${count}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text, annotations: [] }] });
      let item;
      if (!own.some(item => item.issued.kind === 'probe')) {
        if ([...issued.values()].some(item => item.who === who && item.kind === 'probe')) throw new Error('No probe resend without output');
        const tool = toolByName(tools, ['exec_command']); if (!tool) throw new Error('Actual exec tool absent');
        item = call(tool, { cmd: commandFor(who), ...(tool.parameters.properties.workdir ? { workdir: root } : {}), ...(tool.parameters.properties.login ? { login: false } : {}), ...(tool.parameters.properties.yield_time_ms ? { yield_time_ms: 1000 } : {}) }, 'probe');
      } else if (who === 'child') item = message('BOUNDARY_CHILD_COMPLETE');
      else if (!own.some(item => item.issued.kind === 'spawn')) {
        const tool = toolByName(tools, ['spawn_agent']); item = tool ? call(tool, { message: 'BOUNDARY_NATIVE_CHILD_ONLY: execute the exact deterministic probe once and finish.' }, 'spawn') : nativeSearch(body.tools, issued, who, 'spawn', count);
      } else if (!own.some(item => item.issued.kind === 'wait')) {
        const output = own.find(item => item.issued.kind === 'spawn'); const value = JSON.parse(output.output); const id = value.agent_id ?? value.id;
        if (typeof id !== 'string') throw new Error('Actual native child identity missing');
        const tool = toolByName(tools, ['wait_agent', 'wait']); item = tool ? call(tool, { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [id] }, 'wait') : nativeSearch(body.tools, issued, who, 'wait', count);
      } else item = message('BOUNDARY_PRIMARY_COMPLETE');
      const result = { id: `resp_${count}`, object: 'response', model: 'runtime-deterministic', status: 'completed', output: [item], usage: { input_tokens: 1, output_tokens: 1, total_tokens: 2 } };
      const frames = [{ type: 'response.created', response: { ...result, status: 'in_progress', output: [] } }, { type: 'response.output_item.added', output_index: 0, item: { ...item, ...(item.type === 'function_call' ? { arguments: '' } : {}) } }, ...(item.type === 'function_call' ? [{ type: 'response.function_call_arguments.delta', item_id: item.id, output_index: 0, delta: item.arguments }, { type: 'response.function_call_arguments.done', item_id: item.id, output_index: 0, arguments: item.arguments }] : []), { type: 'response.output_item.done', output_index: 0, item }, { type: 'response.completed', response: result }];
      response.writeHead(200, { 'Content-Type': 'text/event-stream' }).end(frames.map((frame, sequence_number) => `event: ${frame.type}\ndata: ${JSON.stringify({ ...frame, sequence_number, response_id: result.id })}\n\n`).join(''));
    } catch { failures.push('BOUNDED_MODEL_FIXTURE_FAILURE'); response.writeHead(400).end('{}'); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  return { baseUrl: `http://127.0.0.1:${server.address().port}/v1`, records, failures, async close() { server.closeAllConnections(); await new Promise(resolve => server.close(resolve)); } };
}
