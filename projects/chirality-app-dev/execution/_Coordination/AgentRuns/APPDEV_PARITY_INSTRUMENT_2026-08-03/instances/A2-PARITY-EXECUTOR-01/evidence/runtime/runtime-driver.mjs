import path from 'node:path';

import { RuntimeClient } from '/Users/ryan/.codex/worktrees/5bef/chirality/runtime/packages/client/dist/src/index.js';

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
  const manager = await client.createSession(projectId, {
    projectId,
    role: 'agent1',
    engineSelection: { adapterId: 'stub', providerId: 'stub' },
    persona: 'WORKING_ITEMS',
    mode: 'readOnly',
    approvalRef: 'D-APP-86'
  });
  const child = await client.createSession(projectId, {
    projectId,
    role: 'agent2',
    parentSessionId: manager.sessionId,
    engineSelection: { adapterId: 'stub', providerId: 'stub' },
    persona: 'A2-PARITY-FIXTURE',
    mode: 'readOnly',
    approvalRef: 'D-APP-86',
    allowedWriteTargets: []
  });
  const stream = await client.turnSession(projectId, child.sessionId, {
    message: 'D-APP-86 parity fixture transcript item.',
    opts: {
      model: 'stub-parity',
      tools: [],
      maxTurns: 1,
      persona: 'A2-PARITY-FIXTURE',
      mode: 'readOnly'
    }
  });
  const frames = [];
  for await (const frame of stream) {
    frames.push(frame);
  }
  const replay = await client.replaySession(projectId, child.sessionId);
  return { manager, child, frames, replay };
}

async function turnExisting(sessionId) {
  const stream = await client.turnSession(projectId, sessionId, {
    message: 'D-APP-86 parity fixture transcript item.',
    opts: {
      model: 'stub-parity',
      tools: [],
      maxTurns: 1,
      persona: 'WORKING_ITEMS',
      mode: 'readOnly'
    }
  });
  const frames = [];
  for await (const frame of stream) {
    frames.push(frame);
  }
  const replay = await client.replaySession(projectId, sessionId);
  return { sessionId, frames, replay };
}

let result;
if (action === 'status') {
  result = await client.daemonStatus();
} else if (action === 'register') {
  result = await client.registerProject({
    manifestPath: path.resolve(args[0]),
    approvedBy: 'A2-PARITY-EXECUTOR-01',
    approvalReference: 'D-APP-86 Option A'
  });
} else if (action === 'fixture') {
  result = await createFixture();
} else if (action === 'turn-existing') {
  result = await turnExisting(args[0]);
} else if (action === 'sessions') {
  result = await client.listSessions(projectId);
} else if (action === 'agents') {
  result = await client.listAgents(projectId);
} else if (action === 'replay') {
  result = await client.replaySession(projectId, args[0]);
} else {
  throw new Error(`Unknown action: ${action}`);
}

process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
