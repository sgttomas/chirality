import path from 'node:path';

import { RuntimeClient } from '/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/node_modules/.chirality-runtime-workspace/packages/client/dist/src/index.js';

const [userData, action, ...args] = process.argv.slice(2);
if (!userData || !path.isAbsolute(userData)) {
  throw new Error('First argument must be an absolute isolated userData path');
}

const runtimeDirectory = path.join(userData, 'runtime');
const client = new RuntimeClient({
  socketPath: path.join(runtimeDirectory, 'control.sock'),
  tokenFile: path.join(runtimeDirectory, 'auth', 'tokens', 'operator.token')
});

const projectId = 'chirality-app-dev';

async function createFixture() {
  const session = await client.createSession(projectId, {
    projectId,
    role: 'agent1',
    engineSelection: { adapterId: 'stub', providerId: 'stub' },
    persona: 'WORKING_ITEMS',
    mode: 'readOnly',
    approvalRef: 'D-APP-86'
  });
  const stream = await client.turnSession(projectId, session.sessionId, {
    message: 'D-APP-86 post-helper parity fixture transcript item.',
    opts: {
      model: 'stub-parity',
      tools: [],
      maxTurns: 1,
      persona: 'WORKING_ITEMS',
      mode: 'readOnly'
    }
  });
  const frames = [];
  for await (const frame of stream) frames.push(frame);
  const replay = await client.replaySession(projectId, session.sessionId);
  return { session, frames, replay };
}

let result;
if (action === 'status') {
  result = await client.daemonStatus();
} else if (action === 'register') {
  result = await client.registerProject({
    manifestPath: path.resolve(args[0]),
    approvedBy: 'A2-PKG02-PARITY-EXECUTOR-01',
    approvalReference: 'D-APP-86 Option A mandatory helper rerun'
  });
} else if (action === 'fixture') {
  result = await createFixture();
} else if (action === 'sessions') {
  result = await client.listSessions(projectId);
} else if (action === 'replay') {
  result = await client.replaySession(projectId, args[0]);
} else {
  throw new Error(`Unknown action: ${action}`);
}

process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
