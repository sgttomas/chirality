// Isolated LaunchAgent driver for F1-SERVICE-SIGNAL.
//
// Derived from V-PACKAGED-DRILLS/evidence/la-driver.mjs, with two additions:
//  * the job environment also pins CHIRALITY_SKIP_CLI_LAUNCHER=1 and the label,
//    so a GUI spawned by the daemon cannot rewrite the operator's
//    ~/.local/bin/chirality and cannot address the operator's real job;
//  * TEST_DESKTOP_EXECUTABLE is free to point at either the app's own binary or
//    the nested runtime bundle's binary, which is the S2 arm.
//
// Hard guards: refuses the default label and refuses to write into the
// operator's ~/Library/LaunchAgents.
import path from 'node:path';
import os from 'node:os';
import { LaunchAgentManager } from '/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/runtime/packages/cli/dist/src/launch-agent.js';

const [action] = process.argv.slice(2);
const userData = process.env.CHIRALITY_USER_DATA;
const launchAgents = process.env.TEST_LAUNCH_AGENTS_DIR;
const label = process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL;
const executable = process.env.TEST_DESKTOP_EXECUTABLE;
if (!userData || !launchAgents || !label || !executable) {
  throw new Error(
    'need CHIRALITY_USER_DATA, TEST_LAUNCH_AGENTS_DIR, CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL, TEST_DESKTOP_EXECUTABLE'
  );
}
if (label === 'com.chirality.runtime' || !label.includes('f1test')) {
  throw new Error(`refusing to operate on non-isolated label: ${label}`);
}
const ownerLaunchAgents = path.join(os.homedir(), 'Library', 'LaunchAgents');
if (path.resolve(launchAgents) === path.resolve(ownerLaunchAgents)) {
  throw new Error(`refusing to write into the operator LaunchAgents directory: ${launchAgents}`);
}

const manager = new LaunchAgentManager(
  { launchAgentsDirectory: launchAgents, runtimeDirectory: path.join(userData, 'runtime') },
  undefined,
  undefined,
  {
    label,
    keepAlive: 'always',
    runAtLoad: true,
    environmentVariables: {
      CHIRALITY_USER_DATA: userData,
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: label,
      CHIRALITY_SKIP_CLI_LAUNCHER: '1'
    }
  }
);

if (action === 'plistpath') console.log(manager.plistPath);
else if (action === 'install') {
  await manager.install(executable);
  console.log(JSON.stringify({ installed: true, plistPath: manager.plistPath, executable }));
} else if (action === 'start') {
  const t = Date.now();
  await manager.start();
  console.log(JSON.stringify({ started: true, ms: Date.now() - t }));
} else if (action === 'stop') {
  const t = Date.now();
  await manager.stop();
  console.log(JSON.stringify({ stopped: true, ms: Date.now() - t }));
} else if (action === 'status') console.log(JSON.stringify(await manager.status(), null, 2));
else if (action === 'uninstall') {
  await manager.uninstall();
  console.log(JSON.stringify({ uninstalled: true }));
} else throw new Error(`unknown action ${action}`);
