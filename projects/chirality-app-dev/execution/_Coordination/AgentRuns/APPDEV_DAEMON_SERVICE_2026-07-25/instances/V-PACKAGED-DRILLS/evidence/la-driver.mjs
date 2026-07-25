// Isolated LaunchAgent driver. Mirrors frontend createDesktopDaemonLifecycle()
// (keepAlive 'always', runAtLoad true, EnvironmentVariables.CHIRALITY_USER_DATA)
// but with the parameterized test label + a test-home LaunchAgents directory.
// Used because the bundled CLI's createDefaultCliDependencies() constructs
// LaunchAgentManager with NO options -> it cannot address an isolated label.
import path from 'node:path';
import { LaunchAgentManager } from '/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/runtime/packages/cli/dist/src/launch-agent.js';

const [action] = process.argv.slice(2);
const userData = process.env.CHIRALITY_USER_DATA;
const launchAgents = process.env.TEST_LAUNCH_AGENTS_DIR;
const label = process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL;
const executable = process.env.TEST_DESKTOP_EXECUTABLE;
if (!userData || !launchAgents || !label || !executable) {
  throw new Error('need CHIRALITY_USER_DATA, TEST_LAUNCH_AGENTS_DIR, CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL, TEST_DESKTOP_EXECUTABLE');
}
const manager = new LaunchAgentManager(
  { launchAgentsDirectory: launchAgents, runtimeDirectory: path.join(userData, 'runtime') },
  undefined,
  undefined,
  { label, keepAlive: 'always', runAtLoad: true, environmentVariables: { CHIRALITY_USER_DATA: userData } }
);
if (action === 'plistpath') { console.log(manager.plistPath); }
else if (action === 'install') { await manager.install(executable); console.log(JSON.stringify({ installed: true, plistPath: manager.plistPath, label: manager.label })); }
else if (action === 'start') { await manager.start(); console.log(JSON.stringify({ started: true })); }
else if (action === 'stop') { await manager.stop(); console.log(JSON.stringify({ stopped: true })); }
else if (action === 'status') { console.log(JSON.stringify(await manager.status(), null, 2)); }
else if (action === 'uninstall') { await manager.uninstall(); console.log(JSON.stringify({ uninstalled: true })); }
else { throw new Error(`unknown action ${action}`); }
