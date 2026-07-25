import path from 'node:path';
import { RuntimeClient } from '/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/runtime/packages/client/dist/src/index.js';
const userData = process.env.CHIRALITY_USER_DATA;
const runtimeDir = path.join(userData, 'runtime');
const client = new RuntimeClient({
  socketPath: path.join(runtimeDir, 'control.sock'),
  tokenFile: path.join(runtimeDir, 'auth', 'tokens', 'operator.token')
});
const [action, ...rest] = process.argv.slice(2);
const out = (v) => console.log(JSON.stringify(v, null, 2));
try {
  if (action === 'daemon-status') out(await client.daemonStatus());
  else if (action === 'cred-status') out(await client.credentialStatus(rest[0] ?? 'anthropic'));
  else if (action === 'cred-set') out(await client.storeCredential(rest[0], rest[1]));
  else if (action === 'cred-remove') out(await client.removeCredential(rest[0]));
  else if (action === 'projects') out(await client.listProjects());
  else if (action === 'register') out(await client.requestJson('/v1/projects/register', { method: 'POST', body: { manifestPath: rest[0], approvedBy: rest[1] ?? 'V-PACKAGED-DRILLS', approvalReference: rest[2] ?? 'TRB-APPDEV-DAEMON-SERVICE-2026-07-25/StageV' } }));
  else if (action === 'models') out(await client.listModels());
  else if (action === 'sessions') out(await client.listSessions(rest[0]));
  else if (action === 'session-create') out(await client.createSession(rest[0], JSON.parse(rest[1])));
  else if (action === 'raw') out(await client.requestJson(rest[0], rest[1] ? { method: 'POST', body: JSON.parse(rest[1]) } : {}));
  else throw new Error(`unknown action ${action}`);
} catch (e) {
  console.error(`ERR ${e?.constructor?.name}: ${e?.code ?? ''} ${e?.message}`);
  process.exitCode = 1;
}
