// Round-2 isolated LaunchAgent driver.
//
// Derived from Stage V's evidence/la-driver.mjs. It now goes through the SAME
// generic env resolver the fixed CLI uses (resolveRuntimeLaunchAgentOptions), so
// what it installs is what `chirality daemon install` installs — the V-D2 gap was
// exactly that these two diverged. Extra isolation-only pins (HOME,
// CHIRALITY_SKIP_CLI_LAUNCHER) are added to the job environment so a GUI the
// daemon spawns for drill (iii) inherits the test HOME and cannot rewrite the
// operator's ~/.local/bin/chirality.
import path from 'node:path';
import {
  LaunchAgentManager,
  resolveRuntimeLaunchAgentOptions
} from '/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/runtime/packages/cli/dist/src/launch-agent.js';

const [action] = process.argv.slice(2);
const userData = process.env.CHIRALITY_USER_DATA;
const launchAgents = process.env.TEST_LAUNCH_AGENTS_DIR;
const executable = process.env.TEST_DESKTOP_EXECUTABLE;
const testHome = process.env.TEST_HOME;
if (!userData || !launchAgents || !executable || !testHome) {
  throw new Error('need CHIRALITY_USER_DATA, TEST_LAUNCH_AGENTS_DIR, TEST_DESKTOP_EXECUTABLE, TEST_HOME');
}
const resolved = resolveRuntimeLaunchAgentOptions(process.env, userData);
if (!resolved.label || resolved.label === 'com.chirality.runtime') {
  throw new Error(`refusing to drive the default label (${resolved.label})`);
}
const options = {
  ...resolved,
  environmentVariables: {
    ...resolved.environmentVariables,
    HOME: testHome,
    CHIRALITY_SKIP_CLI_LAUNCHER: '1'
  }
};
const manager = new LaunchAgentManager(
  { launchAgentsDirectory: launchAgents, runtimeDirectory: path.join(userData, 'runtime') },
  undefined,
  undefined,
  options
);
if (manager.plistPath.startsWith(`${process.env.REAL_HOME}/Library/LaunchAgents`)) {
  throw new Error(`refusing to write into the operator LaunchAgents dir: ${manager.plistPath}`);
}
const out = (v) => console.log(JSON.stringify(v, null, 2));
if (action === 'plistpath') out({ plistPath: manager.plistPath, label: manager.label });
else if (action === 'options') out(options);
else if (action === 'install') { await manager.install(executable); out({ installed: true, plistPath: manager.plistPath, label: manager.label }); }
else if (action === 'start') { const t0 = Date.now(); await manager.start(); out({ started: true, elapsedMs: Date.now() - t0 }); }
else if (action === 'stop') { const t0 = Date.now(); await manager.stop(); out({ stopped: true, elapsedMs: Date.now() - t0 }); }
else if (action === 'status') out(await manager.status());
else if (action === 'uninstall') { await manager.uninstall(); out({ uninstalled: true }); }
else throw new Error(`unknown action ${action}`);
