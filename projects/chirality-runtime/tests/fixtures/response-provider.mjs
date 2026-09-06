/** Deterministic loopback Responses peer. It never emulates the App Server. */
import { createServer } from 'node:http';
import { createHash } from 'node:crypto';
import { gunzipSync } from 'node:zlib';
const hash = value => createHash('sha256').update(JSON.stringify(value)).digest('hex');
const quote = value => "'" + value.replaceAll("'", "'\\''") + "'";
const events = (id, item) => {
  const response = { id, object: 'response', created_at: 0, model: 'runtime-deterministic', status: 'completed', output: [item], usage: { input_tokens: 1, output_tokens: 1, total_tokens: 2 } };
  const frames = [
    { type: 'response.created', response: { ...response, status: 'in_progress', output: [] } },
    { type: 'response.output_item.added', output_index: 0, item: { ...item, ...(item.type === 'function_call' ? { arguments: '' } : item.type === 'custom_tool_call' ? { input: '' } : item.type === 'tool_search_call' ? {} : { content: [] }) } },
    ...(item.type === 'function_call' ? [{ type: 'response.function_call_arguments.delta', item_id: item.id, output_index: 0, delta: item.arguments }, { type: 'response.function_call_arguments.done', item_id: item.id, output_index: 0, arguments: item.arguments }] : []),
    ...(item.type === 'custom_tool_call' ? [{ type: 'response.custom_tool_call_input.delta', item_id: item.id, call_id: item.call_id, output_index: 0, delta: item.input }] : []),
    { type: 'response.output_item.done', output_index: 0, item },
    { type: 'response.completed', response },
  ];
  return frames.map((frame, sequence_number) => `event: ${frame.type}\ndata: ${JSON.stringify({ ...frame, sequence_number, response_id: id })}\n\n`).join('');
};
function toolByName(tools, names) {
  const functions = tools.flatMap(tool => tool.type === 'namespace' && Array.isArray(tool.tools) ? tool.tools.map(member => ({ ...member, namespace: tool.name })) : [tool]);
  const tool = functions.find(tool => tool.type === 'function' && names.includes(tool.name));
  if (!tool || !tool.parameters || typeof tool.parameters !== 'object') throw new Error(`Required advertised function absent: ${names.join(',')}`);
  return tool;
}
function checkedArguments(tool, supplied) {
  const properties = tool.parameters.properties ?? {};
  for (const name of tool.parameters.required ?? []) if (!(name in supplied)) throw new Error(`Unmapped required property ${tool.name}.${name}`);
  for (const [name, value] of Object.entries(supplied)) {
    const schema = properties[name];
    if (!schema || (schema.type === 'string' && typeof value !== 'string') || (schema.type === 'array' && !Array.isArray(value))) throw new Error(`Argument differs from observed schema ${tool.name}.${name}`);
  }
  return supplied;
}
export function discoveredTools(input, issued) {
  return input.filter(item => item.type === 'tool_search_output' && issued.get(item.call_id)?.kind.startsWith('search-') && item.execution === 'client' && item.status === 'completed' && Array.isArray(item.tools)).flatMap(item => item.tools).slice(0, 64);
}
export function nativeSearch(advertised, issued, who, kind, count) {
  if (!advertised.some(tool => tool.type === 'tool_search' && tool.execution === 'client')) throw new Error('Actual client tool_search advertisement absent');
  if ([...issued.values()].some(call => call.who === who && call.kind === `search-${kind}`)) throw new Error('Deferred native tool absent after one bounded search');
  const call_id = `fixture_search_${count}`; issued.set(call_id, { who, kind: `search-${kind}` });
  return { type: 'tool_search_call', call_id, execution: 'client', arguments: { query: kind === 'spawn' ? 'spawn agent' : 'wait agent', limit: 1 } };
}
/** Headers and full prompts are never retained. Only schemas and issued-call results. */
export async function startResponseProvider({ projectRoot, foreignCanary, brokerCanary, mode = 'exercise', managedMarker = 'CHIRALITY_PI_BOUNDED_READ_7D3E' }) {
  let count = 0;
  const records = [], issued = new Map(), failures = [];
  const command = who => `printf ${quote(who)} > ${quote(`${projectRoot}/${who}.txt`)}; if /bin/cat ${quote(foreignCanary)} >/dev/null 2>&1; then printf FOREIGN_LEAK; else printf FOREIGN_DENIED; fi; if /bin/cat ${quote(brokerCanary)} >/dev/null 2>&1; then printf BROKER_LEAK; else printf BROKER_DENIED; fi`;
  const sockets = new Set();
  const server = createServer(async (request, response) => {
    try {
      if (request.method !== 'POST' || request.url !== '/v1/responses' || request.headers.authorization) throw new Error('Only unauthenticated local Responses requests are allowed');
      const chunks = []; let size = 0;
      for await (const chunk of request) { size += chunk.length; if (size > 2_000_000) throw new Error('Request bound exceeded'); chunks.push(chunk); }
      let bytes = Buffer.concat(chunks);
      if (request.headers['content-encoding'] === 'gzip') bytes = gunzipSync(bytes, { maxOutputLength: 4_000_000 });
      else if (request.headers['content-encoding'] && request.headers['content-encoding'] !== 'identity') throw new Error('Unsupported request encoding');
      const body = JSON.parse(bytes.toString());
      if (body.stream !== true || !Array.isArray(body.tools) || !Array.isArray(body.input) || ++count > 32) throw new Error('Unexpected bounded Responses shape');
      // Deferred tools are authoritative only when actually returned for this peer's search.
      const discovered = discoveredTools(body.input, issued);
      const tools = [...body.tools, ...discovered];
      const userMessages = body.input.filter(item => item.role === 'user');
      const lastUser = JSON.stringify(userMessages.at(-1)?.content ?? '');
      const who = lastUser.includes('DETERMINISTIC_CHILD_ONLY') ? 'child' : 'primary';
      const outputs = body.input.filter(item => ['function_call_output', 'custom_tool_call_output'].includes(item.type) && issued.has(item.call_id)).map(item => ({ callId: item.call_id, issued: issued.get(item.call_id), output: typeof item.output === 'string' ? item.output.slice(0, 16_384) : JSON.stringify(item.output).slice(0, 16_384) }));
      records.push({ request: count, who, toolSchemaSha256: hash(tools), tools, outputs, inputItemTypes: body.input.map(item => item.type ?? item.role), inputSha256: hash(body.input) });
      const call = (tool, args, kind) => {
        const call_id = `fixture_call_${count}`; issued.set(call_id, { who, kind });
        return { type: 'function_call', id: `fc_${count}`, call_id, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(checkedArguments(tool, args)), status: 'completed' };
      };
      const discoverNative = kind => nativeSearch(body.tools, issued, who, kind, count);
      const text = value => ({ type: 'message', id: `msg_${count}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: value, annotations: [] }] });
      let item;
      const own = outputs.filter(output => output.issued.who === who);
      if (mode === 'discover' || lastUser.includes('DETERMINISTIC_RESUME_ONLY')) item = text('DETERMINISTIC_DISCOVERY_COMPLETE');
      else if (mode === 'file-change') {
        const custom = tools.flatMap(tool => tool.type === 'namespace' && Array.isArray(tool.tools) ? tool.tools.map(member => ({ ...member, namespace: tool.name })) : [tool]).find(tool => tool.type === 'custom' && tool.name === 'apply_patch');
        if (!custom) throw new Error('Actual advertised freeform apply_patch absent');
        if (!own.some(output => output.issued.kind === 'patch') || !own.some(output => output.issued.kind === 'patch-denied')) {
          const denied = own.some(output => output.issued.kind === 'patch');
          const call_id = `fixture_call_${count}`; issued.set(call_id, { who, kind: denied ? 'patch-denied' : 'patch' });
          const patch = denied ? `*** Begin Patch\n*** Update File: ${foreignCanary}\n@@\n-DETERMINISTIC_FOREIGN_SENTINEL\n+UNAUTHORIZED_PATCH\n*** End Patch` : `*** Begin Patch\n*** Add File: ${who}-patch.txt\n+${who}-patch-marker\n*** End Patch`;
          item = { type: 'custom_tool_call', id: `ctc_${count}`, call_id, name: custom.name, ...(custom.namespace ? { namespace: custom.namespace } : {}), input: patch, status: 'completed' };
        } else if (who === 'child') item = text('DETERMINISTIC_CHILD_COMPLETE');
        else if (!own.some(output => output.issued.kind === 'spawn')) {
          let tool; try { tool = toolByName(tools, ['spawn_agent']); } catch { /* discover below */ }
          if (tool) item = call(tool, { message: 'DETERMINISTIC_CHILD_ONLY: perform the supplied deterministic file-change canary and finish.' }, 'spawn');
          else item = discoverNative('spawn');
        }
        else if (!own.some(output => output.issued.kind === 'wait')) {
          const returned = JSON.parse(own.find(output => output.issued.kind === 'spawn').output), agentId = returned.agent_id ?? returned.id;
          if (typeof agentId !== 'string') throw new Error('Native descendant identity absent');
          let tool; try { tool = toolByName(tools, ['wait_agent', 'wait']); } catch { /* discover below */ }
          if (tool) item = call(tool, { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [agentId] }, 'wait');
          else item = discoverNative('wait');
        } else item = text('DETERMINISTIC_FILE_CHANGE_COMPLETE');
      }
      else if (mode === 'managed-pi') {
        const delegated = own.find(output => output.issued.kind === 'managed-delegate');
        const reviewed = own.find(output => output.issued.kind === 'managed-review');
        if (!delegated) {
          item = call(toolByName(tools, ['delegate_agent']), { sealedBrief: 'Call read_file with {} to read the one authorized file. Return exactly its contents; do not guess. Do not call any other tool.' }, 'managed-delegate');
        } else {
          // App Server converts host inputText content into the Responses function output.
          // Decode only the known callback JSON; no authority follows from arbitrary prose.
          let result;
          try {
            result = JSON.parse(delegated.output);
            if (Array.isArray(result)) {
              const part = result.find(value => value && (value.type === 'input_text' || value.type === 'inputText') && typeof value.text === 'string');
              result = part ? JSON.parse(part.text) : null;
            }
          } catch { throw new Error('Managed delegate result is not the known bounded JSON result'); }
          if (!result || typeof result.childSessionId !== 'string' || !/^[A-Za-z0-9._-]{1,128}$/.test(result.childSessionId) || typeof result.returnText !== 'string' || !result.returnText.includes(managedMarker)) throw new Error('Managed child result did not establish bounded read marker and identity');
          if (!reviewed) item = call(toolByName(tools, ['review']), { childSessionId: result.childSessionId, decision: 'accepted', rationale: 'The actual delegated child returned the expected bounded read marker.' }, 'managed-review');
          else {
            if (!reviewed.output.includes('"reviewed":true')) throw new Error('Managed review callback did not acknowledge completion');
            item = text(`DETERMINISTIC_MANAGED_PI_COMPLETE ${managedMarker}`);
          }
        }
      }
      else if (mode === 'dynamic') {
        if (!own.some(output => output.issued.kind === 'dynamic')) {
          const tool = toolByName(tools, ['review']);
          item = call(tool, { text: 'DETERMINISTIC_DYNAMIC_INPUT' }, 'dynamic');
        } else {
          const returned = own.find(output => output.issued.kind === 'dynamic');
          if (!returned.output.includes('DETERMINISTIC_DYNAMIC_REVIEWED')) throw new Error('Dynamic tool did not return the expected harmless marker');
          item = text('DETERMINISTIC_DYNAMIC_COMPLETE');
        }
      }
      else if (!own.some(output => output.issued.kind === 'baseline') || !own.some(output => output.issued.kind === 'shell')) {
        const baseline = !own.some(output => output.issued.kind === 'baseline');
        const tool = toolByName(tools, ['exec_command', 'shell_command']);
        const properties = tool.parameters.properties ?? {};
        const args = { [tool.name === 'exec_command' ? 'cmd' : 'command']: baseline ? `/bin/sh -c ${quote(`printf BASELINE_SHELL_OK > ${quote(`${projectRoot}/${who}-baseline.txt`)}; /bin/cat ${quote(`${projectRoot}/${who}-baseline.txt`)}`)}` : command(who) };
        if ('workdir' in properties) args.workdir = projectRoot;
        if ('login' in properties) args.login = false;
        if ('shell' in properties) args.shell = '/bin/sh';
        item = call(tool, args, baseline ? 'baseline' : 'shell');
      } else if (who === 'child') item = text('DETERMINISTIC_CHILD_COMPLETE');
      else if (!own.some(output => output.issued.kind === 'spawn')) {
        const tool = toolByName(tools, ['spawn_agent']);
        item = call(tool, { message: 'DETERMINISTIC_CHILD_ONLY: perform the supplied deterministic canary exercise and finish.' }, 'spawn');
      } else if (!own.some(output => output.issued.kind === 'wait')) {
        const spawn = own.find(output => output.issued.kind === 'spawn');
        let value; try { value = JSON.parse(spawn.output); } catch { throw new Error('Spawn result is not observed JSON; inspect schema before adapting'); }
        const agentId = value.agent_id ?? value.id;
        if (typeof agentId !== 'string') throw new Error('Native descendant identity absent');
        const tool = toolByName(tools, ['wait_agent', 'wait']);
        item = call(tool, { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [agentId] }, 'wait');
      } else item = text('DETERMINISTIC_PARENT_COMPLETE');
      response.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' }); response.end(events(`resp_${count}`, item));
    } catch (error) {
      failures.push(error.message); response.writeHead(400, { 'Content-Type': 'application/json' }); response.end(JSON.stringify({ error: { message: error.message, type: 'invalid_request_error' } }));
    }
  });
  server.on('connection', socket => { sockets.add(socket); socket.once('close', () => sockets.delete(socket)); });
  server.requestTimeout = 10_000;
  await new Promise((resolve, reject) => { server.once('error', reject); server.listen(0, '127.0.0.1', resolve); });
  return { baseUrl: `http://127.0.0.1:${server.address().port}/v1`, records, failures,
    async close() { for (const socket of sockets) socket.destroy(); await new Promise(resolve => server.close(resolve)); } };
}
