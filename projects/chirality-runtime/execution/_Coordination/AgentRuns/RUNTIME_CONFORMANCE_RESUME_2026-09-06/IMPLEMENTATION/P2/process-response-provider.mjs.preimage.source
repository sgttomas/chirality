/** P2 deterministic model peer; actual App Server executes every advertised tool. */
import { createServer } from 'node:http';
import { gunzipSync } from 'node:zlib';
import { nativeSearch, discoveredTools } from './response-provider.mjs';
const quote = value => "'" + value.replaceAll("'", "'\\''") + "'";
export function processProbe(root, siblingPid, who, lifetime = false) {
  if (!Number.isSafeInteger(siblingPid) || siblingPid <= 0 || !['primary', 'child'].includes(who)) throw new Error('Invalid owned fixture identity');
  if (lifetime) return `printf PROCESS_STARTED; /bin/sleep 7 & fixture_child=$!; printf '%s\\n' "$fixture_child" > ${quote(`${root}/${who}.pid`)}; printf PROCESS_READY; wait "$fixture_child"; printf PROCESS_FINISHED`;
  return `printf PROCESS_STARTED; /bin/sh -c 'printf FOREGROUND_CHILD_DONE'; if kill -USR1 ${siblingPid} 2>/dev/null; then printf SIGNAL_BREACH; else printf SIGNAL_DENIED; fi; printf PROCESS_FINISHED`;
}
const flatten = tools => tools.flatMap(tool => tool.type === 'namespace' ? (tool.tools ?? []).map(item => ({ ...item, namespace: tool.name })) : [tool]);
const find = (tools, names) => flatten(tools).find(tool => tool.type === 'function' && names.includes(tool.name));
function frames(item, index) {
  const response = { id: `process_response_${index}`, object: 'response', model: 'runtime-deterministic', status: 'completed', output: [item], usage: { input_tokens: 1, output_tokens: 1, total_tokens: 2 } };
  return [
    { type: 'response.created', response: { ...response, status: 'in_progress', output: [] } },
    { type: 'response.output_item.added', output_index: 0, item: { ...item, ...(item.type === 'function_call' ? { arguments: '' } : {}) } },
    ...(item.type === 'function_call' ? [{ type: 'response.function_call_arguments.delta', item_id: item.id, output_index: 0, delta: item.arguments }, { type: 'response.function_call_arguments.done', item_id: item.id, output_index: 0, arguments: item.arguments }] : []),
    { type: 'response.output_item.done', output_index: 0, item }, { type: 'response.completed', response },
  ].map((frame, sequence_number) => `event: ${frame.type}\ndata: ${JSON.stringify({ ...frame, sequence_number })}\n\n`).join('');
}
export async function startProcessProvider({ projectRoot, siblingPid, scenario }) {
  if (!['normal', 'cancel-primary', 'cancel-child', 'timeout-primary', 'timeout-child'].includes(scenario)) throw new Error('Unknown bounded process scenario');
  processProbe(projectRoot, siblingPid, 'primary');
  const issued = new Map(), records = [], failures = [], sockets = new Set(); let count = 0;
  const server = createServer(async (request, response) => {
    try {
      if (request.method !== 'POST' || request.url !== '/v1/responses' || request.headers.authorization) throw new Error('Only unauthenticated local Responses allowed');
      const chunks = []; let bytes = 0;
      for await (const chunk of request) { bytes += chunk.length; if (bytes > 2_000_000) throw new Error('Request bound'); chunks.push(chunk); }
      let buffer = Buffer.concat(chunks);
      if (request.headers['content-encoding'] === 'gzip') buffer = gunzipSync(buffer, { maxOutputLength: 4_000_000 });
      else if (request.headers['content-encoding'] && request.headers['content-encoding'] !== 'identity') throw new Error('Unsupported compression');
      const body = JSON.parse(buffer.toString());
      if (!body.stream || !Array.isArray(body.tools) || !Array.isArray(body.input) || ++count > 20) throw new Error('Unexpected response shape/bound');
      const who = JSON.stringify(body.input.filter(item => item.role === 'user').at(-1)?.content).includes('PROCESS_CHILD_ONLY') ? 'child' : 'primary';
      const tools = [...body.tools, ...discoveredTools(body.input, issued)];
      const outputs = body.input.filter(item => item.type === 'function_call_output' && issued.has(item.call_id)).map(item => ({ issued: issued.get(item.call_id), output: typeof item.output === 'string' ? item.output.slice(0, 16384) : JSON.stringify(item.output).slice(0, 16384) }));
      const own = outputs.filter(output => output.issued.who === who);
      records.push({ request: count, who, outputs, receivedAt: Date.now() });
      const call = (tool, args, kind) => {
        if (!tool?.parameters?.properties) throw new Error('Required actual function advertisement absent');
        for (const key of tool.parameters.required ?? []) if (!(key in args)) throw new Error(`Unmapped required ${key}`);
        for (const key of Object.keys(args)) if (!(key in tool.parameters.properties)) throw new Error(`Unadvertised ${key}`);
        const call_id = `process_call_${count}`; issued.set(call_id, { who, kind, issuedAt: Date.now() });
        return { type: 'function_call', id: `process_fc_${count}`, call_id, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(args), status: 'completed' };
      };
      const targetChild = scenario.endsWith('-child');
      let item;
      if ((scenario === 'normal' || who === (targetChild ? 'child' : 'primary')) && !own.some(output => output.issued.kind === 'probe')) {
        const tool = find(tools, ['exec_command']);
        const args = { cmd: processProbe(projectRoot, siblingPid, who, scenario !== 'normal') };
        if (tool?.parameters?.properties.shell) args.shell = '/bin/sh';
        if (tool?.parameters?.properties.login) args.login = false;
        if (tool?.parameters?.properties.yield_time_ms) args.yield_time_ms = 10000;
        item = call(tool, args, 'probe');
      } else if (who === 'primary' && (scenario === 'normal' || targetChild) && !own.some(output => output.issued.kind === 'spawn')) {
        const tool = find(tools, ['spawn_agent']);
        item = tool ? call(tool, { message: 'PROCESS_CHILD_ONLY: execute the deterministic process probe and finish.' }, 'spawn') : nativeSearch(body.tools, issued, who, 'spawn', count);
      } else if (who === 'primary' && (scenario === 'normal' || targetChild) && !own.some(output => output.issued.kind === 'wait')) {
        const result = JSON.parse(own.find(output => output.issued.kind === 'spawn').output); const id = result.agent_id ?? result.id;
        if (typeof id !== 'string') throw new Error('Actual descendant identity absent');
        const tool = find(tools, ['wait_agent', 'wait']);
        item = tool ? call(tool, { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [id] }, 'wait') : nativeSearch(body.tools, issued, who, 'wait', count);
      } else item = { type: 'message', id: `process_msg_${count}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: 'PROCESS_PROFILE_COMPLETE', annotations: [] }] };
      response.writeHead(200, { 'Content-Type': 'text/event-stream' }); response.end(frames(item, count));
    } catch (error) { failures.push(String(error)); response.writeHead(400); response.end(JSON.stringify({ error: 'bounded process fixture rejected request' })); }
  });
  server.on('connection', socket => { sockets.add(socket); socket.on('close', () => sockets.delete(socket)); });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  return { get issuedCalls() { return [...issued.entries()].map(([callId, value]) => ({ callId, ...value })); }, baseUrl: `http://127.0.0.1:${server.address().port}/v1`, records, failures, close: async () => { for (const socket of sockets) socket.destroy(); await new Promise(resolve => server.close(resolve)); } };
}
