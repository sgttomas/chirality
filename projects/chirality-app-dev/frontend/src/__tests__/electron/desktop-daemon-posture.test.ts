import { describe, expect, it } from 'vitest';
import {
  RUNTIME_INSTRUCTION_ROOT_ENV,
  resolveRuntimeLaunchAgentOptions,
  renderRuntimeLaunchAgent,
  RUNTIME_LAUNCH_AGENT_ENV
} from '@chirality/runtime-cli';
import {
  daemonPostureEnvironment,
  DESKTOP_KEEP_ALIVE_POLICY,
  resolveDesktopDaemonPosture
} from '../../../electron/desktop-daemon-posture';

const USER_DATA = '/Users/example/Library/Application Support/chirality-frontend';

describe('electron/desktop-daemon-posture', () => {
  it('defaults to the real label and the always-restart contract', () => {
    const posture = resolveDesktopDaemonPosture({}, USER_DATA);

    expect(posture).toEqual({
      label: 'com.chirality.runtime',
      keepAlive: 'always',
      runAtLoad: true,
      userDataDirectory: USER_DATA
    });
    expect(DESKTOP_KEEP_ALIVE_POLICY).toBe('always');
  });

  it('honors a label override so an isolated run addresses its own job', () => {
    const posture = resolveDesktopDaemonPosture(
      { [RUNTIME_LAUNCH_AGENT_ENV.label]: ' com.chirality.runtime.tranchetest ' },
      USER_DATA
    );

    expect(posture.label).toBe('com.chirality.runtime.tranchetest');
  });

  it('falls back to the default label when the override is blank', () => {
    const posture = resolveDesktopDaemonPosture(
      { [RUNTIME_LAUNCH_AGENT_ENV.label]: '   ' },
      USER_DATA
    );

    expect(posture.label).toBe('com.chirality.runtime');
  });

  it('does not let the environment weaken the restart contract', () => {
    const posture = resolveDesktopDaemonPosture(
      { [RUNTIME_LAUNCH_AGENT_ENV.keepAlive]: 'crash-only' },
      USER_DATA
    );

    expect(posture.keepAlive).toBe('always');
  });

  it('exports exactly what a CLI invocation needs to reproduce the posture', () => {
    const environment = daemonPostureEnvironment(resolveDesktopDaemonPosture({}, USER_DATA));

    expect(environment).toEqual({
      CHIRALITY_USER_DATA: USER_DATA,
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime',
      CHIRALITY_RUNTIME_KEEP_ALIVE: 'always'
    });
  });

  it('pins the resolved instruction root for launcher and LaunchAgent installs', () => {
    const instructionRoot = '/Applications/Chirality.app/Contents/Resources';
    const environment = daemonPostureEnvironment(
      resolveDesktopDaemonPosture(
        { [RUNTIME_INSTRUCTION_ROOT_ENV]: instructionRoot },
        USER_DATA
      )
    );

    expect(environment.CHIRALITY_INSTRUCTION_ROOT).toBe(instructionRoot);
  });

  // The V-D2 acceptance, expressed as a test: a shell holding only the values the
  // generated launcher exports must make the generic CLI render the same plist the
  // in-app install renders. Before the fix the CLI rendered crash-only with no
  // pinned environment, silently reinstating the corrected root cause.
  it('round-trips through the generic CLI resolver into the intended plist', () => {
    const launcherExports = daemonPostureEnvironment(
      resolveDesktopDaemonPosture({}, USER_DATA)
    );

    const options = resolveRuntimeLaunchAgentOptions(
      launcherExports,
      launcherExports.CHIRALITY_USER_DATA
    );
    const plist = renderRuntimeLaunchAgent({
      ...options,
      executablePath: '/Applications/Chirality.app/Contents/MacOS/Chirality',
      runtimeDirectory: `${USER_DATA}/runtime`
    });

    expect(options.label).toBe('com.chirality.runtime');
    expect(options.keepAlive).toBe('always');
    expect(plist).toContain('<key>KeepAlive</key>\n  <true/>');
    expect(plist).toContain('<key>RunAtLoad</key>\n  <true/>');
    expect(plist).toContain('<key>CHIRALITY_USER_DATA</key>');
    expect(plist).toContain(`<string>${USER_DATA}</string>`);
    expect(plist).toContain('<string>com.chirality.runtime</string>');
    // The defect this closes: never the crash-only semaphore on the CLI path.
    expect(plist).not.toContain('SuccessfulExit');
  });

  // The invariant behind V-D2: whichever surface installs the job, the job's
  // environment block must come out the same. If these two ever drift again, the
  // in-app install and `chirality daemon install` are producing different daemons.
  it('renders the same job environment as the generic CLI resolver', () => {
    for (const label of [undefined, 'com.chirality.runtime.tranchetest']) {
      const environment = label ? { [RUNTIME_LAUNCH_AGENT_ENV.label]: label } : {};
      const fromApp = daemonPostureEnvironment(
        resolveDesktopDaemonPosture(environment, USER_DATA)
      );
      const fromCli = resolveRuntimeLaunchAgentOptions(
        { ...environment, [RUNTIME_LAUNCH_AGENT_ENV.keepAlive]: DESKTOP_KEEP_ALIVE_POLICY },
        USER_DATA
      ).environmentVariables;

      expect(fromApp).toEqual(fromCli);
    }
  });

  it('round-trips an isolated label without naming the default job', () => {
    const launcherExports = daemonPostureEnvironment(
      resolveDesktopDaemonPosture(
        { [RUNTIME_LAUNCH_AGENT_ENV.label]: 'com.chirality.runtime.tranchetest' },
        '/tmp/isolated/userdata'
      )
    );

    const options = resolveRuntimeLaunchAgentOptions(
      launcherExports,
      launcherExports.CHIRALITY_USER_DATA
    );
    const plist = renderRuntimeLaunchAgent({
      ...options,
      executablePath: '/Applications/Chirality.app/Contents/MacOS/Chirality',
      runtimeDirectory: '/tmp/isolated/userdata/runtime'
    });

    expect(options.label).toBe('com.chirality.runtime.tranchetest');
    expect(plist).toContain('<string>com.chirality.runtime.tranchetest</string>');
    expect(plist).not.toContain('<string>com.chirality.runtime</string>');
  });
});
