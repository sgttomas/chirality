import {
  chmod,
  mkdir,
  mkdtemp,
  readFile,
  realpath,
  rename,
  rm,
  symlink,
  writeFile
} from 'node:fs/promises';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  EVIDENCE_SCHEMA,
  MACOS_UNIX_SOCKET_PATH_MAX_BYTES,
  PREFLIGHT_SCHEMA,
  SESSION_SCHEMA,
  SUMMARY_SCHEMA,
  assertPrepareRuntimeSocketPathSupported,
  main,
  parseCleanupLaunchctlJob
} from '../../../scripts/run-packaged-launchagent-login-proof.mjs';

const roots: string[] = [];

async function fixture() {
  const root = await realpath(await mkdtemp('/tmp/chirality-login-proof-'));
  roots.push(root);
  const home = path.join(root, 'home');
  const appPath = path.join(root, 'dist', 'mac-arm64', 'Chirality.app');
  const executablePath = path.join(appPath, 'Contents', 'MacOS', 'Chirality');
  const cliEntry = path.join(appPath, 'Contents', 'Resources', 'runtime-cli', 'chirality-cli.mjs');
  const launchAgentsDirectory = path.join(home, 'Library', 'LaunchAgents');
  const sessionRoot = path.join(root, 'session');
  const label = 'com.chirality.ci.runatload.login.fixture';
  const plistPath = path.join(launchAgentsDirectory, `${label}.plist`);
  const defaultLabel = 'com.chirality.runtime';
  const defaultPlistPath = path.join(launchAgentsDirectory, `${defaultLabel}.plist`);
  const state = {
    loaded: false,
    defaultJobLoaded: true,
    changeDefaultJobOnBootout: false,
    sessionId: 1001,
    consoleUsername: 'fixture-user',
    consoleUid: 501,
    securityUid: 501,
    securityAsid: undefined as number | undefined,
    domainType: 'login',
    domainSession: 'Aqua',
    consoleOutput: undefined as string | undefined,
    domainOutput: undefined as string | undefined,
    statExitCode: 0,
    statSignal: undefined as string | undefined,
    statStderr: '',
    domainExitCode: 0,
    domainSignal: undefined as string | undefined,
    domainStderr: '',
    loadedService: `gui/501/${label}`,
    loadedState: 'running',
    loadedProgram: executablePath as string | undefined,
    loadedArguments: [executablePath, '--runtime-daemon'] as string[] | undefined,
    loadedOutput: undefined as string | undefined,
    runs: 16,
    lastExitCode: 1 as number | string,
    authToken: 'fixture-runtime-auth-token',
    stdoutLog: 'fixture daemon stdout\n',
    stderrLog: 'fixture daemon stderr\n',
    processExecutables: [executablePath] as string[],
    processInspections: 0,
    processInspectionError: undefined as Error | undefined,
    installError: undefined as Error | undefined,
    installedPlist: undefined as string | undefined,
    processAlive: false,
    pid: 8123 as number | undefined,
    bootoutExitCode: 0,
    bootoutRemovesJob: true,
    bootoutStopsProcess: true,
    commands: [] as Array<{ executable: string; args: string[]; env?: Record<string, string> }>
  };

  await mkdir(path.dirname(executablePath), { recursive: true });
  await mkdir(path.dirname(cliEntry), { recursive: true });
  await mkdir(launchAgentsDirectory, { recursive: true });
  await writeFile(executablePath, 'packaged executable\n');
  await chmod(executablePath, 0o700);
  await writeFile(cliEntry, 'export const packaged = true;\n');
  await writeFile(defaultPlistPath, 'operator plist\n');

  const notFound = (target: string) => ({
    exitCode: 113,
    stdout: '',
    stderr: `Bad request.\nCould not find service "${target}" in domain for user gui: 501`
  });
  const runCommand = async (input: {
    executable: string;
    args: string[];
    env?: Record<string, string>;
  }) => {
    const entry = { executable: input.executable, args: [...input.args], env: input.env };
    state.commands.push(entry);
    if (input.executable === '/usr/bin/stat') {
      return {
        exitCode: state.statExitCode,
        signal: state.statSignal,
        stdout: state.consoleOutput ?? `${state.consoleUsername}:${state.consoleUid}\n`,
        stderr: state.statStderr
      };
    }
    if (input.executable === executablePath) {
      await writeFile(
        plistPath,
        state.installedPlist ?? `<plist><dict>
<key>Label</key><string>${label}</string>
<key>ProgramArguments</key><array><string>${executablePath}</string><string>--runtime-daemon</string></array>
<key>RunAtLoad</key><true/>
</dict></plist>\n`
      );
      const runtimeDirectory = path.join(sessionRoot, 'runtime-data', 'runtime');
      await mkdir(path.join(runtimeDirectory, 'logs'), { recursive: true });
      await mkdir(path.join(runtimeDirectory, 'auth', 'tokens'), { recursive: true });
      await writeFile(path.join(runtimeDirectory, 'logs', 'daemon.stdout.log'), state.stdoutLog);
      await writeFile(path.join(runtimeDirectory, 'logs', 'daemon.stderr.log'), state.stderrLog);
      await writeFile(
        path.join(runtimeDirectory, 'auth', 'tokens', 'operator.token'),
        `${state.authToken}\n`
      );
      if (state.installError) throw state.installError;
      return { exitCode: 0, stdout: '', stderr: '' };
    }
    if (input.executable !== '/bin/launchctl') throw new Error(`Unexpected ${input.executable}`);
    if (input.args[0] === 'print') {
      const service = input.args[1];
      if (service === 'gui/501') {
        const asid = state.securityAsid ?? state.sessionId;
        return {
          exitCode: state.domainExitCode,
          signal: state.domainSignal,
          stdout:
            state.domainOutput ??
            `gui/501 = {
\ttype = ${state.domainType}
\thandle = ${state.sessionId}
\tactive count = 12
\tsession = ${state.domainSession}
\tsecurity context = {
\t\tuid = ${state.securityUid}
\t\tasid = ${asid}
\t}
\tservices = {
\t\thandle = 999999
\t}
}\n`,
          stderr: state.domainStderr
        };
      }
      if (service.endsWith('/com.chirality.runtime')) {
        if (!state.defaultJobLoaded) return notFound(defaultLabel);
        return { exitCode: 0, stdout: 'state = running\nprogram = /operator\npid = 77\n', stderr: '' };
      }
      if (!state.loaded) return notFound(label);
      return {
        exitCode: 0,
        stdout:
          state.loadedOutput ??
          `${state.loadedService} = {\n\tstate = ${state.loadedState}\n${
            state.loadedProgram === undefined ? '' : `\tprogram = ${state.loadedProgram}\n`
          }${
            state.loadedArguments
              ? `\targuments = {\n${state.loadedArguments.map((value) => `\t\t${value}`).join('\n')}\n\t}\n`
              : ''
          }\truns = ${state.runs}\n\tlast exit code = ${state.lastExitCode}\n${
            state.pid === undefined ? '' : `\tpid = ${state.pid}\n`
          }}\n`,
        stderr: ''
      };
    }
    if (input.args[0] === 'bootout') {
      if (state.bootoutExitCode === 0 && state.bootoutRemovesJob) state.loaded = false;
      if (state.bootoutExitCode === 0 && state.bootoutStopsProcess) state.processAlive = false;
      if (state.changeDefaultJobOnBootout) state.defaultJobLoaded = false;
      return { exitCode: state.bootoutExitCode, stdout: '', stderr: '' };
    }
    throw new Error(`Unexpected launchctl call ${input.args.join(' ')}`);
  };
  const deps = {
    platform: 'darwin',
    environment: { HOME: home },
    userInfo: () => ({ homedir: home, uid: 501, username: 'fixture-user' }),
    uid: () => 501,
    now: () => new Date(state.loaded ? '2026-08-22T14:00:00.000Z' : '2026-08-21T14:00:00.000Z'),
    randomId: () => 'fixture',
    runCommand,
    processAlive: (pid: number) => pid === state.pid && state.processAlive,
    inspectProcessExecutables: async () => {
      state.processInspections += 1;
      if (state.processInspectionError) throw state.processInspectionError;
      return state.processExecutables;
    },
    beforeFailureLogSnapshot: undefined as (() => void | Promise<void>) | undefined,
    removePassFailureLogs: undefined as ((failedLogsRoot: string) => Promise<void>) | undefined
  };
  return { root, home, appPath, executablePath, sessionRoot, label, plistPath, state, deps };
}

function sessionRootWithSocketBytes(anchor: string, targetBytes: number, unicode = false): string {
  const suffix = `${path.sep}runtime-data${path.sep}runtime${path.sep}control.sock`;
  const prefix = `${anchor}${path.sep}`;
  const fixedBytes = Buffer.byteLength(`${prefix}${suffix}`, 'utf8');
  const remaining = targetBytes - fixedBytes;
  if (remaining < (unicode ? 2 : 1)) throw new Error('Anchor is too long for requested fixture');
  const segment = unicode ? `${'a'.repeat(remaining - 2)}é` : 'a'.repeat(remaining);
  const sessionRoot = path.join(anchor, segment);
  expect(Buffer.byteLength(path.join(sessionRoot, 'runtime-data', 'runtime', 'control.sock'), 'utf8')).toBe(
    targetBytes
  );
  return sessionRoot;
}

afterEach(async () => {
  await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

async function expectPreflightFailureWithoutMutation(
  harness: Awaited<ReturnType<typeof fixture>>
) {
  let result: Awaited<ReturnType<typeof main>> | undefined;
  let failure: unknown;
  try {
    result = await main(['preflight'], harness.deps);
  } catch (error) {
    failure = error;
  }

  expect(failure).toBeInstanceOf(Error);
  expect(result).toBeUndefined();
  expect(harness.state.commands.some((entry) => entry.executable === harness.executablePath)).toBe(
    false
  );
  expect(
    harness.state.commands
      .filter((entry) => entry.executable === '/bin/launchctl')
      .every(
        (entry) =>
          entry.args.length === 2 && entry.args[0] === 'print' && entry.args[1] === 'gui/501'
      )
  ).toBe(true);
  await expect(realpath(harness.sessionRoot)).rejects.toThrow();
}

describe('cleanup launchctl parser', () => {
  const realService =
    'gui/501/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b';

  it('parses the verified R19 never-exited fixture exactly', async () => {
    const source = await readFile(
      new URL('./fixtures/launchctl-print-r19-never-exited.txt', import.meta.url),
      'utf8'
    );

    expect(parseCleanupLaunchctlJob(source, realService)).toMatchObject({
      state: 'running',
      pid: 34924,
      runs: 1,
      lastExitCode: undefined,
      neverExited: true
    });
  });

  it('preserves integer parsing and rejects every other noninteger last-exit form', async () => {
    const source = await readFile(
      new URL('./fixtures/launchctl-print-r19-never-exited.txt', import.meta.url),
      'utf8'
    );
    expect(
      parseCleanupLaunchctlJob(source.replace('(never exited)', '-9'), realService)
    ).toMatchObject({ lastExitCode: -9, neverExited: false });
    for (const malformed of ['', '   ', 'never exited', '(still running)', '1.5', '0x0']) {
      expect(() =>
        parseCleanupLaunchctlJob(source.replace('(never exited)', malformed), realService)
      ).toThrow('Loaded cleanup job last exit code is invalid');
    }
  });
});

describe('macOS login-session identity preflight', () => {
  it('accepts live-shaped Aqua login-domain output without raw identity or mutation', async () => {
    const harness = await fixture();
    const first = await main(['preflight'], harness.deps);
    if (!('identitySha256' in first)) throw new Error('Expected preflight result');

    expect(first).toMatchObject({
      schema: PREFLIGHT_SCHEMA,
      status: 'PASS',
      mode: 'READ_ONLY_PREFLIGHT',
      inspections: {
        consoleOwnerMetadata: true,
        topLevelGuiLoginDomain: true,
        serviceOrJobInspection: false
      },
      validation: {
        currentAccountMatchesConsoleOwner: true,
        uidConsistent: true,
        loginDomain: true,
        aquaSession: true,
        identifierConsistent: true
      },
      mutationsPerformed: false,
      sessionRootCreated: false
    });
    expect(first.identitySha256).toMatch(/^[0-9a-f]{64}$/u);
    expect(JSON.stringify(first)).not.toContain('fixture-user');
    expect(JSON.stringify(first)).not.toContain('1001');
    expect(harness.state.commands).toEqual([
      { executable: '/usr/bin/stat', args: ['-f', '%Su:%u', '/dev/console'], env: undefined },
      { executable: '/bin/launchctl', args: ['print', 'gui/501'], env: undefined }
    ]);
    expect(harness.state.commands.some((entry) => entry.executable === '/usr/bin/osascript')).toBe(
      false
    );
    expect(
      harness.state.commands.some(
        (entry) =>
          entry.executable === '/bin/launchctl' &&
          (entry.args.length !== 2 || entry.args[0] !== 'print' || entry.args[1] !== 'gui/501')
      )
    ).toBe(false);
    await expect(realpath(harness.sessionRoot)).rejects.toThrow();

    harness.state.sessionId += 1;
    harness.state.commands.length = 0;
    const second = await main(['preflight'], harness.deps);
    if (!('identitySha256' in second)) throw new Error('Expected preflight result');
    expect(second.identitySha256).not.toBe(first.identitySha256);
  });

  it('refuses every option before inspection and does not create a proof root', async () => {
    for (const option of [
      ['--session-root', '/tmp/forbidden'],
      ['--app-path', '/Applications/Chirality.app'],
      ['--label', 'com.chirality.ci.runatload.login.forbidden'],
      ['--source-revision', 'forbidden']
    ]) {
      const harness = await fixture();
      await expect(main(['preflight', ...option], harness.deps)).rejects.toThrow(
        'Preflight accepts no options'
      );
      expect(harness.state.commands).toHaveLength(0);
      await expect(realpath(harness.sessionRoot)).rejects.toThrow();
    }
  });

  it.each([
    ['non-Darwin platform', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.deps.platform = 'linux';
    }],
    ['root process UID', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.deps.uid = () => 0;
    }],
    ['process/account UID mismatch', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.deps.userInfo = () => ({
        homedir: harness.home,
        uid: 502,
        username: 'fixture-user'
      });
    }],
    ['invalid current-account username root', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.deps.userInfo = () => ({ homedir: harness.home, uid: 501, username: 'root' });
    }],
    ['invalid current-account username loginwindow', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.deps.userInfo = () => ({ homedir: harness.home, uid: 501, username: 'loginwindow' });
    }],
    ['invalid current-account username _mbsetupuser', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.deps.userInfo = () => ({ homedir: harness.home, uid: 501, username: '_mbsetupuser' });
    }]
  ])('fails closed on %s before inspection', async (_caseName, mutate) => {
    const harness = await fixture();
    mutate(harness);
    await expectPreflightFailureWithoutMutation(harness);
  });

  it.each([
    ['malformed console output', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.consoleOutput = 'fixture-user:501\nsecond-record:501\n';
    }],
    ['loginwindow console owner', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.consoleUsername = 'loginwindow';
    }],
    ['setup console owner', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.consoleUsername = '_mbsetupuser';
    }],
    ['wrong console user', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.consoleUsername = 'another-user';
    }],
    ['wrong console UID', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.consoleUid = 502;
    }],
    ['console command failure', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.statExitCode = 1;
    }],
    ['signaled console command', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.statSignal = 'SIGTERM';
    }],
    ['console stderr-bearing success', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.statStderr = 'partial warning\n';
    }]
  ])('fails closed on %s', async (_caseName, mutate) => {
    const harness = await fixture();
    mutate(harness);
    await expectPreflightFailureWithoutMutation(harness);
  });

  it.each([
    ['malformed domain output', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = 'not a login domain\n';
    }],
    ['wrong domain identifier UID', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/502 = {
\ttype = login
\thandle = 1001
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
\t}
}\n`;
    }],
    ['wrong security UID', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.securityUid = 502;
    }],
    ['non-login domain', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainType = 'user';
    }],
    ['non-Aqua session', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainSession = 'Background';
    }],
    ['mismatched handle and asid', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.securityAsid = 1002;
    }],
    ['unsafe-integer handle and asid', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/501 = {
\ttype = login
\thandle = 9007199254740992
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 9007199254740992
\t}
}\n`;
    }],
    ['duplicate handle', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/501 = {
\ttype = login
\thandle = 1001
\thandle = 1001
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
\t}
}\n`;
    }],
    ['ambiguous security contexts', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/501 = {
\ttype = login
\thandle = 1001
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
\t}
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
\t}
}\n`;
    }],
    ['trailing top-level domain output', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/501 = {
\ttype = login
\thandle = 1001
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
\t}
}
trailing output
`;
    }],
    ['unclosed top-level domain brace', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/501 = {
\ttype = login
\thandle = 1001
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
\t}
`;
    }],
    ['unclosed security-context braces', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainOutput = `gui/501 = {
\ttype = login
\thandle = 1001
\tsession = Aqua
\tsecurity context = {
\t\tuid = 501
\t\tasid = 1001
`;
    }],
    ['launchctl command failure', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainExitCode = 113;
    }],
    ['signaled top-level launchctl command', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainSignal = 'SIGTERM';
    }],
    ['launchctl stderr-bearing success', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.domainStderr = 'partial warning\n';
    }]
  ])('fails closed on %s', async (_caseName, mutate) => {
    const harness = await fixture();
    mutate(harness);
    await expectPreflightFailureWithoutMutation(harness);
  });
});

describe('packaged LaunchAgent login-session proof preparation', () => {
  it('enforces the exact macOS socket-path byte boundary before prepare mutation', async () => {
    const accepted = await fixture();
    accepted.sessionRoot = sessionRootWithSocketBytes(
      accepted.root,
      MACOS_UNIX_SOCKET_PATH_MAX_BYTES
    );
    expect(
      assertPrepareRuntimeSocketPathSupported(accepted.sessionRoot, 'darwin')
    ).toEqual({ measuredBytes: 103, maximumBytes: 103 });
    await expect(
      main(
        [
          'prepare',
          '--app-path',
          accepted.appPath,
          '--session-root',
          accepted.sessionRoot,
          '--label',
          accepted.label,
          '--source-revision',
          'fixture-sha'
        ],
        accepted.deps
      )
    ).resolves.toMatchObject({ status: 'PREPARED', proofClaimed: false });

    const asciiRejected = await fixture();
    const unicodeRejected = await fixture();
    const rejectedCases = [
      {
        name: '104-byte ASCII path',
        harness: asciiRejected,
        sessionRoot: sessionRootWithSocketBytes(asciiRejected.root, 104),
        expectedBytes: 104,
        inspectRootAbsence: true
      },
      {
        name: '104-byte Unicode path',
        harness: unicodeRejected,
        sessionRoot: sessionRootWithSocketBytes(unicodeRejected.root, 104, true),
        expectedBytes: 104,
        inspectRootAbsence: true
      },
      {
        name: 'R16 path',
        harness: await fixture(),
        sessionRoot:
          '/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20',
        expectedBytes: 119,
        inspectRootAbsence: false
      },
      {
        name: 'R13 path',
        harness: await fixture(),
        sessionRoot:
          '/private/tmp/chirality-login-proof-owner-2a38b15f-07de-48c4-87ef-ccd246bd92fa',
        expectedBytes: 111,
        inspectRootAbsence: false
      }
    ];
    for (const { name, harness: rejected, sessionRoot, expectedBytes, inspectRootAbsence } of rejectedCases) {
      const absentHome = path.join(rejected.root, 'guard-rejection-home');
      rejected.deps.environment.HOME = absentHome;
      rejected.deps.userInfo = () => ({ homedir: absentHome, uid: 501, username: 'fixture-user' });
      expect(
        Buffer.byteLength(path.join(sessionRoot, 'runtime-data', 'runtime', 'control.sock'), 'utf8'),
        name
      ).toBe(expectedBytes);
      await expect(
        main(
          [
            'prepare',
            '--app-path',
            rejected.appPath,
            '--session-root',
            sessionRoot,
            '--label',
            rejected.label,
            '--source-revision',
            'fixture-sha'
          ],
          rejected.deps
        )
      ).rejects.toThrow(
        `Proof runtime control socket path is ${expectedBytes} UTF-8 bytes; macOS maximum is 103 bytes`
      );
      expect(rejected.state.commands, name).toHaveLength(0);
      await expect(realpath(absentHome), name).rejects.toThrow();
      if (inspectRootAbsence) {
        await expect(realpath(sessionRoot), name).rejects.toThrow();
      }
    }
  });

  it('prepares without bootstrap, kickstart, launcher mutation, or a proof claim', async () => {
    const harness = await fixture();
    const result = await main(
      [
        'prepare',
        '--app-path',
        harness.appPath,
        '--session-root',
        harness.sessionRoot,
        '--label',
        harness.label,
        '--source-revision',
        'fixture-sha'
      ],
      harness.deps
    );

    expect(result).toMatchObject({ status: 'PREPARED', proofClaimed: false });
    const prepared = JSON.parse(
      await readFile(path.join(harness.sessionRoot, 'prepared.json'), 'utf8')
    );
    expect(prepared).toMatchObject({
      schema: SESSION_SCHEMA,
      status: 'PREPARED',
      sourceRevision: 'fixture-sha',
      bootstrapInvoked: false,
      kickstartInvoked: false,
      proofClaimed: false
    });
    expect(prepared).toMatchObject({
      plist: `~/Library/LaunchAgents/${harness.label}.plist`,
      app: { path: '<packaged-app>' },
      runtimeData: '<proof-session>/runtime-data',
      preparedJobAbsent: true
    });
    expect(JSON.stringify(prepared)).not.toContain(harness.root);
    expect(JSON.stringify(prepared)).not.toContain(harness.home);
    expect(prepared.prepareMutations).toEqual(['packaged-cli-install']);
    expect(await readFile(harness.plistPath, 'utf8')).toContain('<key>RunAtLoad</key><true/>');
    expect(harness.state.commands.map((entry) => entry.args[0])).not.toContain('bootstrap');
    expect(harness.state.commands.map((entry) => entry.args[0])).not.toContain('kickstart');
    const install = harness.state.commands.find((entry) => entry.executable === harness.executablePath);
    expect(install?.env).toMatchObject({
      CHIRALITY_SKIP_CLI_LAUNCHER: '1',
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: harness.label,
      CHIRALITY_RUNTIME_RUN_AT_LOAD: 'true'
    });
  });

  it('rejects missing and placeholder source revisions before prepare mutates owner state', async () => {
    for (const revision of [undefined, '   ', 'unknown']) {
      const harness = await fixture();
      const args = [
        'prepare',
        '--app-path',
        harness.appPath,
        '--session-root',
        harness.sessionRoot,
        '--label',
        harness.label
      ];
      if (revision !== undefined) args.push('--source-revision', revision);

      await expect(main(args, harness.deps)).rejects.toThrow(/Source revision.*(required|placeholder)/u);
      expect(
        harness.state.commands.some((entry) => entry.executable === harness.executablePath)
      ).toBe(false);
      await expect(realpath(harness.sessionRoot)).rejects.toThrow();
    }
  });

  it('cleans proof-owned side effects when packaged install times out after writing the plist', async () => {
    const harness = await fixture();
    harness.state.installError = new Error('Command exceeded 60000ms: packaged install');

    await expect(
      main(
        ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
        harness.deps
      )
    ).rejects.toThrow(
      /Command exceeded 60000ms.*install-attempt cleanup complete \(job=absent, job-mutation-refused=false, plist=absent, runtime-data=absent\)/u
    );
    await expect(readFile(harness.plistPath, 'utf8')).rejects.toThrow();
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).rejects.toThrow();
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it('cleans proof-owned side effects when post-install plist validation fails', async () => {
    const harness = await fixture();
    harness.state.installedPlist = '<plist><dict><key>Label</key><string>wrong.label</string></dict></plist>\n';

    await expect(
      main(
        ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
        harness.deps
      )
    ).rejects.toThrow(
      /Installed plist.*install-attempt cleanup complete \(job=absent, job-mutation-refused=false, plist=absent, runtime-data=absent\)/u
    );
    await expect(readFile(harness.plistPath, 'utf8')).rejects.toThrow();
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).rejects.toThrow();
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it('captures a login-discovered job in one invocation, packages evidence, and cleans up', async () => {
    const harness = await fixture();
    await main(
      [
        'prepare',
        '--app-path',
        harness.appPath,
        '--session-root',
        harness.sessionRoot,
        '--label',
        harness.label,
        '--source-revision',
        'fixture-sha'
      ],
      harness.deps
    );

    // The test models the owner-controlled session boundary. The harness itself
    // has no logout/login or launch mutation API.
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    const summary = await main(
      ['capture', '--session-root', harness.sessionRoot],
      harness.deps
    );

    expect(summary).toMatchObject({
      schema: SUMMARY_SCHEMA,
      status: 'PASS',
      launchAgent: {
        preparedJobAbsent: true,
        bootstrapInvoked: false,
        kickstartInvoked: false,
        loginDiscoveredJobObserved: true,
        loadedProgramMatches: true,
        loadedArgumentsMatch: true
      },
      process: { pidObserved: true, executableIdentityMatches: true },
      loginSession: { identityTransitionObserved: true },
      cleanup: {
        processAbsent: true,
        jobAbsent: true,
        plistAbsent: true,
        runtimeDataRemoved: true
      },
      proofBoundary: {
        ownerLogoutLoginActRequired: true,
        harnessPerformedLogoutLogin: false,
        preparationClaimedProof: false
      }
    });
    const evidence = JSON.parse(
      await readFile(path.join(harness.sessionRoot, 'evidence-package.json'), 'utf8')
    );
    expect(evidence).toMatchObject({ schema: EVIDENCE_SCHEMA, status: 'PASS' });
    expect(evidence.files).toEqual(['prepared.json', 'summary.json']);
    await expect(readFile(harness.plistPath, 'utf8')).rejects.toThrow();
    expect(JSON.stringify(summary)).not.toContain(harness.home);
    for (const evidenceFile of evidence.files) {
      expect(await readFile(path.join(harness.sessionRoot, evidenceFile), 'utf8')).not.toContain(
        harness.root
      );
    }
    expect(harness.state.commands.map((entry) => entry.args[0])).not.toContain('bootstrap');
    expect(harness.state.commands.map((entry) => entry.args[0])).not.toContain('kickstart');
    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow('already consumed');
  });

  it('boots out an exact-owned running PID with runs 1 and never-exited state', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.state.runs = 1;
    harness.state.lastExitCode = '(never exited)';

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).resolves.toMatchObject({
      status: 'PASS',
      cleanup: {
        processAbsent: true,
        jobAbsent: true,
        destructiveCleanupRefused: false,
        plistAbsent: true,
        runtimeDataRemoved: true
      }
    });
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(true);
  });

  it('keeps final PASS irrevocable when PASS-only failed-log deletion fails', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.deps.removePassFailureLogs = async () => {
      throw new Error('deterministic PASS-only deletion failure');
    };

    const summary = await main(['capture', '--session-root', harness.sessionRoot], harness.deps);
    expect(summary).toMatchObject({
      status: 'PASS',
      cleanup: {
        failureLogsCopied: null,
        passOnlyFailureLogCleanup: 'INDETERMINATE_RETAINED_OR_PARTIAL',
        runtimeDataRemoved: true
      }
    });
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stdout.log'), 'utf8')
    ).resolves.toBe('fixture daemon stdout\n');
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stderr.log'), 'utf8')
    ).resolves.toBe('fixture daemon stderr\n');
  });

  it('fails closed and removes prepared state when the login session did not discover the job', async () => {
    const harness = await fixture();
    await main(
      [
        'prepare',
        '--app-path',
        harness.appPath,
        '--session-root',
        harness.sessionRoot,
        '--label',
        harness.label,
        '--source-revision',
        'fixture-sha'
      ],
      harness.deps
    );
    harness.state.sessionId += 1;
    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow('not discovered');
    const summary = JSON.parse(
      await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8')
    );
    expect(summary.status).toBe('FAIL');
    expect(summary.launchAgent.loginDiscoveredJobObserved).toBe(false);
    expect(summary.cleanup).toMatchObject({
      jobAbsent: true,
      destructiveCleanupRefused: false,
      failureLogsCopied: true,
      plistAbsent: true,
      runtimeDataRemoved: true
    });
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stdout.log'), 'utf8')
    ).resolves.toBe('fixture daemon stdout\n');
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stderr.log'), 'utf8')
    ).resolves.toBe('fixture daemon stderr\n');
    expect(summary.proofBoundary.harnessPerformedLogoutLogin).toBe(false);
  });

  it('copies neither log and retains private runtime logs when either contains the auth token', async () => {
    const harness = await fixture();
    harness.state.stdoutLog = `before ${harness.state.authToken} after\n`;
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.sessionId += 1;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow(
      'not discovered'
    );
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      failureLogsCopied: false,
      failureLogsPrivateOnly: true,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors).toContain(
      'Runtime auth token was detected; retained failure logs only in private runtime data'
    );
    await expect(realpath(path.join(harness.sessionRoot, 'failed-logs'))).rejects.toThrow();
    await expect(
      readFile(
        path.join(harness.sessionRoot, 'runtime-data', 'runtime', 'logs', 'daemon.stdout.log'),
        'utf8'
      )
    ).resolves.toBe(harness.state.stdoutLog);
    expect(JSON.stringify(summary)).not.toContain(harness.state.authToken);
  });

  it('fails closed with private-only retention when both capture logs are missing', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    const logsRoot = path.join(harness.sessionRoot, 'runtime-data', 'runtime', 'logs');
    await rm(path.join(logsRoot, 'daemon.stdout.log'));
    await rm(path.join(logsRoot, 'daemon.stderr.log'));
    harness.state.sessionId += 1;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow(
      'not discovered'
    );
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      failureLogsCopied: false,
      failureLogsPrivateOnly: true,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors).toContain(
      'Required failure logs are missing; retained only in private runtime data'
    );
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).resolves.toBe(
      path.join(harness.sessionRoot, 'runtime-data')
    );
  });

  it('fails closed with private-only retention when one log is missing before later default failure', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    await rm(
      path.join(
        harness.sessionRoot,
        'runtime-data',
        'runtime',
        'logs',
        'daemon.stderr.log'
      )
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.state.changeDefaultJobOnBootout = true;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.defaultProtection.jobLoadedStateUnchanged).toBe(false);
    expect(summary.cleanup).toMatchObject({
      failureLogsCopied: false,
      failureLogsPrivateOnly: true,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors).toContain(
      'Required failure logs are missing; retained only in private runtime data'
    );
  });

  it.each(['logs', 'auth', 'tokens'])('rejects a symlinked %s ancestor without copying logs', async (ancestor) => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    const runtimeDirectory = path.join(harness.sessionRoot, 'runtime-data', 'runtime');
    const target =
      ancestor === 'logs'
        ? path.join(runtimeDirectory, 'logs')
        : ancestor === 'auth'
          ? path.join(runtimeDirectory, 'auth')
          : path.join(runtimeDirectory, 'auth', 'tokens');
    const replacement = path.join(harness.root, `replacement-${ancestor}`);
    if (ancestor === 'logs') {
      await mkdir(replacement);
      await writeFile(path.join(replacement, 'daemon.stdout.log'), harness.state.stdoutLog);
      await writeFile(path.join(replacement, 'daemon.stderr.log'), harness.state.stderrLog);
    } else if (ancestor === 'auth') {
      await mkdir(path.join(replacement, 'tokens'), { recursive: true });
      await writeFile(path.join(replacement, 'tokens', 'operator.token'), `${harness.state.authToken}\n`);
    } else {
      await mkdir(replacement);
      await writeFile(path.join(replacement, 'operator.token'), `${harness.state.authToken}\n`);
    }
    await rm(target, { recursive: true });
    await symlink(replacement, target, 'dir');
    harness.state.sessionId += 1;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      failureLogsCopied: false,
      failureLogsPrivateOnly: true,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors[0]).toContain('Failure-log identity or auth snapshot is unsafe');
    await expect(realpath(path.join(harness.sessionRoot, 'failed-logs'))).rejects.toThrow();
  });

  it('rejects final-file substitution after identity inspection', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    const stdoutPath = path.join(
      harness.sessionRoot,
      'runtime-data',
      'runtime',
      'logs',
      'daemon.stdout.log'
    );
    const originalPath = `${stdoutPath}.original`;
    harness.deps.beforeFailureLogSnapshot = async () => {
      await rename(stdoutPath, originalPath);
      await symlink(originalPath, stdoutPath);
    };
    harness.state.sessionId += 1;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      failureLogsCopied: false,
      failureLogsPrivateOnly: true,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors[0]).toContain('Failure-log identity or auth snapshot is unsafe');
    await expect(realpath(path.join(harness.sessionRoot, 'failed-logs'))).rejects.toThrow();
  });

  it('retains pre-removal log copies when final default protection fails later', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.state.changeDefaultJobOnBootout = true;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow(
      'Capture or cleanup incomplete'
    );
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.status).toBe('FAIL');
    expect(summary.defaultProtection.jobLoadedStateUnchanged).toBe(false);
    expect(summary.cleanup).toMatchObject({
      failureLogsCopied: true,
      runtimeDataRemoved: true
    });
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stdout.log'), 'utf8')
    ).resolves.toBe('fixture daemon stdout\n');
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stderr.log'), 'utf8')
    ).resolves.toBe('fixture daemon stderr\n');
  });

  it('requires a different completed GUI login session than preparation', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.processAlive = true;

    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow('same session');
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.loginSession.identityTransitionObserved).toBe(false);
    expect(summary.launchAgent.loginDiscoveredJobObserved).toBe(false);
  });

  it('fails closed when launchctl omits the loaded daemon argument vector', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.loadedArguments = undefined;
    harness.state.processAlive = true;

    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow('arguments are missing');
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.launchAgent.loadedArgumentsAvailable).toBe(false);
    expect(summary.status).toBe('FAIL');
    expect(summary.cleanup).toMatchObject({
      jobAbsent: false,
      jobMutationRefused: true,
      destructiveCleanupRefused: true,
      failureLogsCopied: true,
      plistAbsent: false,
      runtimeDataRemoved: false
    });
    await expect(readFile(harness.plistPath, 'utf8')).resolves.toContain(harness.label);
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).resolves.toBe(
      path.join(harness.sessionRoot, 'runtime-data')
    );
    expect(harness.state.loaded).toBe(true);
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it('boots out and cleans an exact proof-owned pid-less crash-loop job without lsof', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.loadedState = 'spawn scheduled';
    harness.state.sessionId += 1;
    harness.state.pid = undefined;

    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow('Loaded job has ambiguous process identity');
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary).toMatchObject({
      status: 'FAIL',
      error: 'Loaded job has ambiguous process identity',
      cleanup: {
        jobAbsent: true,
        jobMutationRefused: false,
        plistAbsent: true,
        runtimeDataRemoved: true
      }
    });
    expect(harness.state.processInspections).toBe(0);
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(true);
  });

  it('refuses cleanup of a PID-bearing job whose state is not running', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.loadedState = 'spawn scheduled';
    harness.state.sessionId += 1;
    harness.state.processAlive = true;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.status).toBe('FAIL');
    expect(summary.cleanup).toMatchObject({ jobAbsent: false, jobMutationRefused: true });
    expect(harness.state.processInspections).toBe(0);
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it('refuses cleanup of a pid-less job whose state is running', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.loadedState = 'running';
    harness.state.sessionId += 1;
    harness.state.pid = undefined;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.status).toBe('FAIL');
    expect(summary.cleanup).toMatchObject({ jobAbsent: false, jobMutationRefused: true });
    expect(harness.state.processInspections).toBe(0);
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it('preserves plist and runtime diagnostics when exact-owned bootout is refused', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.state.bootoutExitCode = 5;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      processAbsent: false,
      jobAbsent: false,
      destructiveCleanupRefused: true,
      failureLogsCopied: true,
      plistAbsent: false,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors).toContain(
      'Refusing destructive cleanup while proof state is unsafe (job=present-or-unknown, process=alive, job-mutation-refused=false)'
    );
    await expect(readFile(harness.plistPath, 'utf8')).resolves.toContain(harness.label);
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).resolves.toBe(
      path.join(harness.sessionRoot, 'runtime-data')
    );
  });

  it('preserves plist and runtime diagnostics when a process remains alive after bootout', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.state.bootoutStopsProcess = false;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      processAbsent: false,
      jobAbsent: true,
      destructiveCleanupRefused: true,
      failureLogsCopied: true,
      plistAbsent: false,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors).toContain(
      'Refusing destructive cleanup while proof state is unsafe (job=absent, process=alive, job-mutation-refused=false)'
    );
    await expect(readFile(harness.plistPath, 'utf8')).resolves.toContain(harness.label);
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).resolves.toBe(
      path.join(harness.sessionRoot, 'runtime-data')
    );
  });

  it('preserves diagnostics when successful bootout leaves the job loaded but process absent', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    harness.state.bootoutRemovesJob = false;

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.cleanup).toMatchObject({
      processAbsent: true,
      jobAbsent: false,
      destructiveCleanupRefused: true,
      failureLogsCopied: true,
      plistAbsent: false,
      runtimeDataRemoved: false
    });
    expect(summary.cleanupErrors).toContain(
      'Refusing destructive cleanup while proof state is unsafe (job=present-or-unknown, process=absent, job-mutation-refused=false)'
    );
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(true);
    await expect(readFile(harness.plistPath, 'utf8')).resolves.toContain(harness.label);
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stdout.log'), 'utf8')
    ).resolves.toBe('fixture daemon stdout\n');
    await expect(
      readFile(path.join(harness.sessionRoot, 'failed-logs', 'daemon.stderr.log'), 'utf8')
    ).resolves.toBe('fixture daemon stderr\n');
    await expect(realpath(path.join(harness.sessionRoot, 'runtime-data'))).resolves.toBe(
      path.join(harness.sessionRoot, 'runtime-data')
    );
  });

  it.each([
    ['missing launchctl program', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.loadedProgram = undefined;
    }],
    ['mismatched launchctl service', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.loadedService = `gui/501/${harness.label}.foreign`;
    }],
    ['ambiguous launchctl arguments', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.loadedOutput = `${harness.state.loadedService} = {\n\tstate = spawn scheduled\n\tprogram = ${harness.executablePath}\n\targuments = {\n\t\t${harness.executablePath}\n\t\t--runtime-daemon\n\t}\n\targuments = {\n\t\t${harness.executablePath}\n\t\t--runtime-daemon\n\t}\n}\n`;
    }],
    ['mismatched proof plist label', async (harness: Awaited<ReturnType<typeof fixture>>) => {
      await writeFile(
        harness.plistPath,
        (await readFile(harness.plistPath, 'utf8')).replace(harness.label, `${harness.label}.foreign`)
      );
    }],
    ['mismatched proof plist arguments', async (harness: Awaited<ReturnType<typeof fixture>>) => {
      await writeFile(
        harness.plistPath,
        (await readFile(harness.plistPath, 'utf8')).replace('--runtime-daemon', '--foreign-daemon')
      );
    }],
    ['mismatched proof plist RunAtLoad', async (harness: Awaited<ReturnType<typeof fixture>>) => {
      await writeFile(
        harness.plistPath,
        (await readFile(harness.plistPath, 'utf8')).replace('<true/>', '<false/>')
      );
    }],
    ['ambiguous proof plist label', async (harness: Awaited<ReturnType<typeof fixture>>) => {
      await writeFile(
        harness.plistPath,
        (await readFile(harness.plistPath, 'utf8')).replace(
          '</dict>',
          `<key>Label</key><string>${harness.label}</string></dict>`
        )
      );
    }]
  ])('refuses pid-less proof-job cleanup with %s', async (_name, mutateIdentity) => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.loadedState = 'spawn scheduled';
    harness.state.sessionId += 1;
    harness.state.pid = undefined;
    await mutateIdentity(harness);

    await expect(main(['capture', '--session-root', harness.sessionRoot], harness.deps)).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.status).toBe('FAIL');
    expect(summary.cleanup).toMatchObject({ jobAbsent: false, jobMutationRefused: true });
    expect(harness.state.loaded).toBe(true);
    expect(harness.state.processInspections).toBe(0);
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it.each([
    ['program mismatch', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.loadedProgram = path.join(harness.root, 'foreign', 'Chirality');
    }],
    ['argument mismatch', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.loadedArguments = [harness.executablePath, '--foreign-daemon'];
    }],
    ['ambiguous launchctl process identity', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.loadedProgram = `${harness.executablePath}\nprogram = ${harness.executablePath}`;
    }],
    ['executable inspection failure', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.processInspectionError = new Error('Unable to inspect process executable');
    }],
    ['ambiguous executable identity', (harness: Awaited<ReturnType<typeof fixture>>) => {
      harness.state.processExecutables = [
        harness.executablePath,
        path.join(harness.root, 'other', 'Chirality.app', 'Contents', 'MacOS', 'Chirality')
      ];
    }]
  ])('does not boot out a loaded same-label service with %s', async (_caseName, mutateIdentity) => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    harness.state.loaded = true;
    harness.state.sessionId += 1;
    harness.state.processAlive = true;
    mutateIdentity(harness);

    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow();
    const summary = JSON.parse(await readFile(path.join(harness.sessionRoot, 'summary.json'), 'utf8'));
    expect(summary.status).toBe('FAIL');
    expect(summary.cleanup).toMatchObject({ jobAbsent: false, jobMutationRefused: true });
    expect(harness.state.loaded).toBe(true);
    expect(harness.state.commands.some((entry) => entry.args[0] === 'bootout')).toBe(false);
  });

  it('binds the redacted prepared manifest and refuses unsafe cleanup state', async () => {
    const harness = await fixture();
    await main(
      ['prepare', '--app-path', harness.appPath, '--session-root', harness.sessionRoot, '--label', harness.label, '--source-revision', 'fixture-sha'],
      harness.deps
    );
    const preparedPath = path.join(harness.sessionRoot, 'prepared.json');
    const prepared = JSON.parse(await readFile(preparedPath, 'utf8'));
    prepared.sourceRevision = 'tampered';
    await writeFile(preparedPath, `${JSON.stringify(prepared)}\n`);
    await expect(
      main(['capture', '--session-root', harness.sessionRoot], harness.deps)
    ).rejects.toThrow('bound capture state');

    const second = await fixture();
    await main(
      ['prepare', '--app-path', second.appPath, '--session-root', second.sessionRoot, '--label', second.label, '--source-revision', 'fixture-sha'],
      second.deps
    );
    const statePath = path.join(second.sessionRoot, '.capture-state.json');
    const privateState = JSON.parse(await readFile(statePath, 'utf8'));
    privateState.runtimeRoot = second.home;
    await writeFile(statePath, `${JSON.stringify(privateState)}\n`);
    await expect(
      main(['capture', '--session-root', second.sessionRoot], second.deps)
    ).rejects.toThrow('inconsistent');
    await expect(realpath(second.home)).resolves.toBe(second.home);
  });

  it('refuses unsafe labels and reused session roots before owner-state mutation', async () => {
    const harness = await fixture();
    await expect(
      main(
        [
          'prepare',
          '--app-path',
          harness.appPath,
          '--session-root',
          harness.sessionRoot,
          '--label',
          'com.chirality.runtime',
          '--source-revision',
          'fixture-sha'
        ],
        harness.deps
      )
    ).rejects.toThrow('default');
    expect(harness.state.commands.some((entry) => entry.executable === harness.executablePath)).toBe(false);

    const second = await fixture();
    await mkdir(second.sessionRoot);
    await expect(
      main(
        [
          'prepare',
          '--app-path',
          second.appPath,
          '--session-root',
          second.sessionRoot,
          '--label',
          second.label,
          '--source-revision',
          'fixture-sha'
        ],
        second.deps
      )
    ).rejects.toThrow('already exists');
  });
});
