import {
  chmod,
  mkdir,
  mkdtemp,
  readFile,
  realpath,
  rm,
  symlink,
  writeFile
} from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  DEFAULT_LAUNCH_AGENT_LABEL,
  assertExactRuntimeArguments,
  inspectInstalledPlist,
  isExactLaunchctlNotFound,
  main,
  parseLaunchctlJob,
  validateProofLabel
} from '../../../scripts/run-packaged-launchagent-runatload-proof.mjs';

const tempRoots: string[] = [];

type HarnessOptions = {
  ambiguousIdentity?: boolean;
  bootoutFailures?: number;
  bootoutLeavesJobLoaded?: boolean;
  cleanupPrintFailure?: { exitCode: number; stdout: string; stderr: string };
  defaultPrintFailure?: { exitCode: number; stdout: string; stderr: string };
  defaultLoaded?: boolean;
  homeMismatch?: boolean;
  identityChangesAfterTerm?: boolean;
  installFailure?: boolean;
  loadedArguments?: string[] | null;
  loadedProgram?: string;
  omitLoadedPid?: boolean;
  plistArguments?: string[];
  replacePidOnTerminate?: boolean;
  sigkillPostChecks?: number;
  sigtermLeavesProcessAlive?: boolean;
  uniquePreflightFailure?: { exitCode: number; stdout: string; stderr: string };
};

async function createHarness(options: HarnessOptions = {}) {
  const root = await realpath(
    await mkdtemp(path.join(os.tmpdir(), 'chirality-runatload-test-'))
  );
  tempRoots.push(root);
  const home = path.join(root, 'home');
  const accountHome = options.homeMismatch ? path.join(root, 'account-home') : home;
  const launchAgentsDirectory = path.join(home, 'Library', 'LaunchAgents');
  const appPath = path.join(root, 'dist', 'mac-arm64', 'Chirality.app');
  const executablePath = path.join(appPath, 'Contents', 'MacOS', 'Chirality');
  const cliEntry = path.join(
    appPath,
    'Contents',
    'Resources',
    'runtime-cli',
    'chirality-cli.mjs'
  );
  const outputRoot = path.join(root, 'evidence');
  const label = 'com.chirality.ci.runatload.test-123';
  const plistPath = path.join(launchAgentsDirectory, `${label}.plist`);
  const defaultPlistPath = path.join(
    launchAgentsDirectory,
    `${DEFAULT_LAUNCH_AGENT_LABEL}.plist`
  );

  await mkdir(path.dirname(executablePath), { recursive: true });
  await mkdir(path.dirname(cliEntry), { recursive: true });
  await mkdir(launchAgentsDirectory, { recursive: true });
  await mkdir(accountHome, { recursive: true });
  await writeFile(executablePath, 'packaged-app-bytes\n', 'utf8');
  await chmod(executablePath, 0o700);
  await writeFile(cliEntry, 'export const packaged = true;\n', 'utf8');
  await writeFile(defaultPlistPath, 'protected-default-plist\n', 'utf8');

  const state = {
    bootoutAttempted: false,
    bootoutAttempts: 0,
    loaded: false,
    processAlive: false,
    signals: [] as string[],
    signalPids: [] as number[],
    pidHistory: [4242] as number[],
    identityInspections: 0,
    signalIdentityInspections: [] as number[],
    postSigkillChecks: 0,
    sigkillPendingChecks: 0,
    mutations: [] as Array<{
      executable: string;
      args: string[];
      env?: Record<string, string>;
    }>,
    pid: 4242
  };

  const notFound = (targetLabel: string) => ({
    exitCode: 113,
    stdout: '',
    stderr: `Bad request.\nCould not find service "${targetLabel}" in domain for user gui: 501`
  });

  const runCommand = async (input: {
    executable: string;
    args: string[];
    env?: Record<string, string>;
  }) => {
    const args = [...input.args];
    if (input.executable === executablePath) {
      state.mutations.push({ executable: input.executable, args, env: input.env });
      if (options.installFailure) return { exitCode: 1, stdout: '', stderr: 'install failed' };
      const plistArguments = options.plistArguments ?? [executablePath, '--runtime-daemon'];
      await writeFile(
        plistPath,
        `<?xml version="1.0"?>
<plist version="1.0"><dict>
<key>Label</key><string>${label}</string>
<key>ProgramArguments</key><array>${plistArguments.map((argument) => `<string>${argument}</string>`).join('')}</array>
<key>RunAtLoad</key><true/>
</dict></plist>\n`,
        'utf8'
      );
      return { exitCode: 0, stdout: '', stderr: '' };
    }
    if (input.executable !== '/bin/launchctl') {
      throw new Error(`Unexpected executable: ${input.executable}`);
    }
    if (args[0] === 'bootstrap') {
      state.mutations.push({ executable: input.executable, args });
      state.loaded = true;
      state.processAlive = true;
      return { exitCode: 0, stdout: '', stderr: '' };
    }
    if (args[0] === 'bootout') {
      state.mutations.push({ executable: input.executable, args });
      state.bootoutAttempted = true;
      state.bootoutAttempts += 1;
      if (state.bootoutAttempts <= (options.bootoutFailures ?? 0)) {
        return { exitCode: 5, stdout: '', stderr: 'transient bootout failure' };
      }
      if (!options.bootoutLeavesJobLoaded) {
        state.loaded = false;
        state.processAlive = false;
      }
      return { exitCode: 0, stdout: '', stderr: '' };
    }
    if (args[0] === 'print') {
      if (args[1]?.endsWith(`/${DEFAULT_LAUNCH_AGENT_LABEL}`)) {
        if (options.defaultPrintFailure) return options.defaultPrintFailure;
        return options.defaultLoaded
          ? {
              exitCode: 0,
              stdout: 'state = running\nprogram = /protected/default\npid = 91\n',
              stderr: ''
            }
          : notFound(DEFAULT_LAUNCH_AGENT_LABEL);
      }
      if (!state.loaded) {
        if (!state.bootoutAttempted && options.uniquePreflightFailure) {
          return options.uniquePreflightFailure;
        }
        if (state.bootoutAttempted && options.cleanupPrintFailure) {
          return options.cleanupPrintFailure;
        }
        return notFound(label);
      }
      const loadedArguments =
        options.loadedArguments === undefined
          ? [executablePath, '--runtime-daemon']
          : options.loadedArguments;
      const argumentsBlock =
        loadedArguments === null
          ? ''
          : `arguments = {\n${loadedArguments.map((argument) => `\t${argument}`).join('\n')}\n}\n`;
      return {
        exitCode: 0,
        stdout: `state = running\nprogram = ${options.loadedProgram ?? executablePath}\n${argumentsBlock}${options.omitLoadedPid ? '' : `pid = ${state.pid}\n`}`,
        stderr: ''
      };
    }
    throw new Error(`Unexpected launchctl arguments: ${args.join(' ')}`);
  };

  return {
    root,
    home,
    accountHome,
    appPath,
    executablePath,
    outputRoot,
    label,
    plistPath,
    defaultPlistPath,
    state,
    deps: {
      platform: 'darwin',
      environment: { HOME: home },
      userInfo: () => ({ homedir: accountHome }),
      uid: () => 501,
      tempDirectory: () => root,
      randomId: () => 'fixture-id',
      now: () => new Date('2026-08-20T18:00:00.000Z'),
      runCommand,
      cleanupSignalTimeoutMs: 1,
      processAlive: (pid: number) => {
        if (pid !== state.pid || !state.processAlive) return false;
        if (state.sigkillPendingChecks > 0) {
          state.postSigkillChecks += 1;
          state.sigkillPendingChecks -= 1;
          return true;
        }
        if (options.sigkillPostChecks !== undefined && state.postSigkillChecks > 0) {
          state.postSigkillChecks += 1;
          state.processAlive = false;
          return false;
        }
        return true;
      },
      terminateProcess: async (pid: number, signal: string) => {
        if (pid === state.pid) {
          state.signals.push(signal);
          state.signalPids.push(pid);
          state.signalIdentityInspections.push(state.identityInspections);
          if (signal === 'SIGTERM' && options.sigtermLeavesProcessAlive) return;
          if (signal === 'SIGKILL' && options.sigkillPostChecks !== undefined) {
            state.sigkillPendingChecks = options.sigkillPostChecks;
            return;
          }
          state.processAlive = false;
          if (signal === 'SIGTERM' && options.replacePidOnTerminate && state.loaded) {
            state.pid += 1;
            state.pidHistory.push(state.pid);
            state.processAlive = true;
          }
        }
      },
      inspectProcessExecutables: async () => {
        state.identityInspections += 1;
        if (options.ambiguousIdentity) {
          return [
            executablePath,
            path.join(root, 'other', 'Other.app', 'Contents', 'MacOS', 'Chirality')
          ];
        }
        if (options.identityChangesAfterTerm && state.signals.includes('SIGTERM')) {
          return [path.join(root, 'other', 'Other.app', 'Contents', 'MacOS', 'Chirality')];
        }
        return [executablePath];
      }
    }
  };
}

afterEach(async () => {
  await Promise.all(tempRoots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

describe('packaged LaunchAgent RunAtLoad proof', () => {
  it('accepts only a bounded non-default proof label', () => {
    expect(validateProofLabel('com.chirality.ci.runatload.run-123')).toBe(
      'com.chirality.ci.runatload.run-123'
    );
    expect(() => validateProofLabel(DEFAULT_LAUNCH_AGENT_LABEL)).toThrow('default');
    expect(() => validateProofLabel('com.example.unsafe')).toThrow('Unsafe');
    expect(() => validateProofLabel('com.chirality.ci.runatload.bad/target')).toThrow('Unsafe');
  });

  it('recognizes only the exact supported launchctl not-found result', () => {
    const service = 'gui/501/com.chirality.ci.runatload.fixture';
    const exact = {
      exitCode: 113,
      stdout: '',
      stderr:
        'Bad request.\nCould not find service "com.chirality.ci.runatload.fixture" in domain for user gui: 501'
    };
    expect(isExactLaunchctlNotFound(exact, service)).toBe(true);
    expect(isExactLaunchctlNotFound({ ...exact, exitCode: 1 }, service)).toBe(false);
    expect(
      isExactLaunchctlNotFound({ ...exact, stderr: 'Operation not permitted' }, service)
    ).toBe(false);
    expect(
      isExactLaunchctlNotFound({ ...exact, stderr: 'Could not find service' }, service)
    ).toBe(false);
  });

  it('requires the exact two-entry packaged runtime daemon plist vector', () => {
    const executable = '/Applications/Chirality.app/Contents/MacOS/Chirality';
    const render = (args: string[]) => `<key>Label</key><string>fixture</string>
<key>ProgramArguments</key><array>${args.map((argument) => `<string>${argument}</string>`).join('')}</array>
<key>RunAtLoad</key><true/>`;
    const exact = inspectInstalledPlist(render([executable, '--runtime-daemon']));
    expect(() =>
      assertExactRuntimeArguments(exact.programArguments, executable, 'Installed plist')
    ).not.toThrow();
    for (const invalid of [
      [executable],
      [executable, '--wrong-mode'],
      [executable, '--runtime-daemon', '--extra']
    ]) {
      const parsed = inspectInstalledPlist(render(invalid));
      expect(() =>
        assertExactRuntimeArguments(parsed.programArguments, executable, 'Installed plist')
      ).toThrow('exactly match');
    }
  });

  it('rejects ambiguous plist and loaded-process identities', () => {
    expect(() =>
      inspectInstalledPlist(`
        <key>Label</key><string>a</string>
        <key>Label</key><string>b</string>
        <key>ProgramArguments</key><array><string>/app</string></array>
        <key>RunAtLoad</key><true/>
      `)
    ).toThrow('ambiguous');
    expect(() =>
      parseLaunchctlJob('state = running\nprogram = /app/a\nprogram = /app/b\npid = 1\n')
    ).toThrow('ambiguous');
  });

  it('selects only top-level job state from realistic nested coalition output', () => {
    const source = `gui/501/com.chirality.ci.runatload.fixture = {
\tactive count = 5
\ttype = LaunchAgent
\tstate = running

\tprogram = /Applications/Chirality.app/Contents/MacOS/Chirality
\targuments = {
\t\t/Applications/Chirality.app/Contents/MacOS/Chirality
\t\t--runtime-daemon
\t}

\tpid = 2928
\tdynamic endpoints = {
\t\t"com.chirality.fixture" = {
\t\t\tactive = 1
\t\t}
\t}

\tresource coalition = {
\t\tID = 34125
\t\ttype = resource
\t\tstate = active
\t}

\tjetsam coalition = {
\t\tID = 34126
\t\ttype = jetsam
\t\tstate = active
\t}
\tjob state = running
}`;

    expect(parseLaunchctlJob(source)).toEqual({
      state: 'running',
      program: '/Applications/Chirality.app/Contents/MacOS/Chirality',
      pid: 2928,
      programArguments: [
        '/Applications/Chirality.app/Contents/MacOS/Chirality',
        '--runtime-daemon'
      ]
    });
  });

  it('proves automatic packaged launch and verifies fail-closed cleanup/default protection', async () => {
    const harness = await createHarness({ defaultLoaded: true });
    const summary = await main(
      [
        '--app-path',
        harness.appPath,
        '--output-root',
        harness.outputRoot,
        '--label',
        harness.label,
        '--source-revision',
        'fixture-sha'
      ],
      harness.deps
    );

    expect(summary.status).toBe('PASS');
    expect(summary.launchAgent).toMatchObject({
      runAtLoad: true,
      bootstrapOnly: true,
      automaticLaunchObserved: true,
      loadedProgramMatches: true,
      loadedArgumentsAvailable: true,
      loadedArgumentsMatch: true
    });
    expect(summary.process).toMatchObject({
      pidObserved: true,
      executableIdentityMatches: true
    });
    expect(summary.cleanup).toMatchObject({
      processAbsent: true,
      jobAbsent: true,
      plistAbsent: true,
      runtimeDataRemoved: true
    });
    expect(summary.defaultProtection).toMatchObject({
      plistUnchanged: true,
      jobLoadedStateUnchanged: true,
      mutationTargetsExcluded: true
    });
    expect(await readFile(harness.defaultPlistPath, 'utf8')).toBe('protected-default-plist\n');
    expect(harness.state.mutations).toHaveLength(3);
    expect(harness.state.mutations[0]?.executable).toBe(harness.executablePath);
    expect(harness.state.mutations.slice(1).map((call) => call.args[0])).toEqual([
      'bootstrap',
      'bootout'
    ]);
    expect(harness.state.mutations[0]?.env).toMatchObject({
      HOME: harness.home,
      CHIRALITY_LAUNCH_AGENTS_DIRECTORY: path.join(
        harness.home,
        'Library',
        'LaunchAgents'
      ),
      CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: harness.label
    });
    expect(JSON.stringify(harness.state.mutations)).not.toContain(DEFAULT_LAUNCH_AGENT_LABEL);
    expect(JSON.stringify(harness.state.mutations)).not.toContain('kickstart');

    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.status).toBe('PASS');
    expect(JSON.stringify(retained)).not.toContain(harness.home);
  });

  it('fails before mutation when HOME is not the account home', async () => {
    const harness = await createHarness({ homeMismatch: true });
    await expect(
      main(
        ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
        harness.deps
      )
    ).rejects.toThrow('HOME does not resolve');
    expect(harness.state.mutations).toEqual([]);
  });

  it('invalidates seeded stale PASS evidence before platform, uid, HOME, and label failures', async () => {
    const cases = [
      {
        name: 'platform',
        deps: (harness: Awaited<ReturnType<typeof createHarness>>) => ({
          ...harness.deps,
          platform: 'linux'
        }),
        label: (harness: Awaited<ReturnType<typeof createHarness>>) => harness.label
      },
      {
        name: 'uid',
        deps: (harness: Awaited<ReturnType<typeof createHarness>>) => ({
          ...harness.deps,
          uid: () => 0
        }),
        label: (harness: Awaited<ReturnType<typeof createHarness>>) => harness.label
      },
      {
        name: 'HOME',
        deps: (harness: Awaited<ReturnType<typeof createHarness>>) => ({
          ...harness.deps,
          environment: {}
        }),
        label: (harness: Awaited<ReturnType<typeof createHarness>>) => harness.label
      },
      {
        name: 'label',
        deps: (harness: Awaited<ReturnType<typeof createHarness>>) => harness.deps,
        label: () => DEFAULT_LAUNCH_AGENT_LABEL
      }
    ];

    for (const testCase of cases) {
      const harness = await createHarness();
      await mkdir(harness.outputRoot, { recursive: true });
      await writeFile(
        path.join(harness.outputRoot, 'summary.json'),
        '{"schema":"stale","status":"PASS"}\n',
        'utf8'
      );
      await expect(
        main(
          [
            '--app-path',
            harness.appPath,
            '--output-root',
            harness.outputRoot,
            '--label',
            testCase.label(harness)
          ],
          testCase.deps(harness)
        )
      ).rejects.toThrow();
      const retained = JSON.parse(
        await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
      );
      expect(retained.status, testCase.name).toBe('FAIL');
      expect(retained.schema, testCase.name).not.toBe('stale');
    }
  });

  it('invalidates seeded stale PASS evidence before unknown-argument and missing-value failures', async () => {
    for (const suffix of [['--unknown', 'value'], ['--source-revision']]) {
      const harness = await createHarness();
      await mkdir(harness.outputRoot, { recursive: true });
      await writeFile(
        path.join(harness.outputRoot, 'summary.json'),
        '{"schema":"stale","status":"PASS"}\n',
        'utf8'
      );
      await expect(
        main(
          [
            '--app-path',
            harness.appPath,
            '--output-root',
            harness.outputRoot,
            '--label',
            harness.label,
            ...suffix
          ],
          harness.deps
        )
      ).rejects.toThrow();
      const retained = JSON.parse(
        await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
      );
      expect(retained.status).toBe('FAIL');
      expect(retained.schema).not.toBe('stale');
    }
  });

  it('rejects a missing packaged app before launchd mutation', async () => {
    const harness = await createHarness();
    await expect(
      main(
        [
          '--app-path',
          path.join(harness.root, 'missing', 'Chirality.app'),
          '--output-root',
          harness.outputRoot,
          '--label',
          harness.label
        ],
        harness.deps
      )
    ).rejects.toThrow();
    expect(harness.state.mutations).toEqual([]);
    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.status).toBe('FAIL');
    expect(retained.error).not.toContain(harness.home);
  });

  it('fails closed on permission/domain/transient launchctl print failures', async () => {
    const failures = [
      {
        options: {
          uniquePreflightFailure: {
            exitCode: 1,
            stdout: '',
            stderr: 'Operation not permitted'
          }
        },
        expected: 'Unexpected launchctl print failure',
        jobAbsent: false
      },
      {
        options: {
          defaultPrintFailure: {
            exitCode: 125,
            stdout: '',
            stderr: 'Domain does not support specified action'
          }
        },
        expected: 'Unexpected launchctl print failure',
        jobAbsent: true
      },
      {
        options: {
          cleanupPrintFailure: {
            exitCode: 5,
            stdout: '',
            stderr: 'Input/output error'
          }
        },
        expected: 'Cleanup verification failed',
        jobAbsent: false
      }
    ];

    for (const failure of failures) {
      const harness = await createHarness(failure.options);
      await expect(
        main(
          ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
          harness.deps
        )
      ).rejects.toThrow(failure.expected);
      const retained = JSON.parse(
        await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
      );
      expect(retained.status).toBe('FAIL');
      expect(retained.cleanup.jobAbsent).toBe(failure.jobAbsent);
    }
  });

  it('rejects wrong or extra loaded argument identity and allows an unavailable block', async () => {
    for (const suffix of [['--wrong-mode'], ['--runtime-daemon', '--extra']]) {
      const options: HarnessOptions = { loadedArguments: [] };
      const amended = await createHarness(options);
      options.loadedArguments = [amended.executablePath, ...suffix];
      await expect(
        main(
          ['--app-path', amended.appPath, '--output-root', amended.outputRoot, '--label', amended.label],
          amended.deps
        )
      ).rejects.toThrow('Loaded job arguments');
    }

    const unavailable = await createHarness({ loadedArguments: null });
    const summary = await main(
      [
        '--app-path',
        unavailable.appPath,
        '--output-root',
        unavailable.outputRoot,
        '--label',
        unavailable.label
      ],
      unavailable.deps
    );
    expect(summary.launchAgent.loadedArgumentsAvailable).toBe(false);
    expect(summary.launchAgent.loadedArgumentsMatch).toBeNull();
  });

  it('cleans its job and plist after ambiguous process identity fails', async () => {
    const harness = await createHarness({ ambiguousIdentity: true });
    await expect(
      main(
        ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
        harness.deps
      )
    ).rejects.toThrow('ambiguous');

    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.status).toBe('FAIL');
    expect(retained.cleanup).toMatchObject({ processAbsent: true, jobAbsent: true, plistAbsent: true });
    expect(retained.defaultProtection).toMatchObject({
      plistUnchanged: true,
      jobLoadedStateUnchanged: true,
      mutationTargetsExcluded: true
    });
  });

  it('retries a transient bootout until the service reaches exact not-found', async () => {
    const harness = await createHarness({ bootoutFailures: 1 });
    const summary = await main(
      ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
      harness.deps
    );

    expect(summary.status).toBe('PASS');
    expect(summary.cleanup).toMatchObject({ processAbsent: true, jobAbsent: true });
    expect(harness.state.bootoutAttempts).toBe(2);
  });

  it('tracks KeepAlive replacement PIDs before retrying bootout', async () => {
    const harness = await createHarness({
      bootoutFailures: 2,
      replacePidOnTerminate: true
    });
    const summary = await main(
      ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
      harness.deps
    );

    expect(summary.status).toBe('PASS');
    expect(harness.state.bootoutAttempts).toBe(3);
    expect(harness.state.pidHistory).toEqual([4242, 4243, 4244]);
    expect(harness.state.signalPids).toEqual([4242, 4243]);
    expect(summary.cleanup).toMatchObject({ processAbsent: true, jobAbsent: true });
  });

  it('waits for confirmed process absence after SIGKILL', async () => {
    const harness = await createHarness({
      bootoutFailures: 1,
      sigtermLeavesProcessAlive: true,
      sigkillPostChecks: 1
    });
    const summary = await main(
      ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
      harness.deps
    );

    expect(summary.status).toBe('PASS');
    expect(harness.state.signals).toEqual(['SIGTERM', 'SIGKILL']);
    expect(harness.state.signalIdentityInspections).toEqual([2, 3]);
    expect(harness.state.postSigkillChecks).toBeGreaterThanOrEqual(2);
    expect(summary.cleanup.processAbsent).toBe(true);
  });

  it('refuses SIGKILL and fails closed when executable identity changes after SIGTERM', async () => {
    const harness = await createHarness({
      bootoutFailures: 1,
      identityChangesAfterTerm: true,
      sigtermLeavesProcessAlive: true
    });
    await expect(
      main(
        ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
        harness.deps
      )
    ).rejects.toThrow('refused to SIGKILL');

    expect(harness.state.signals).toEqual(['SIGTERM']);
    expect(harness.state.identityInspections).toBeGreaterThanOrEqual(3);
    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.status).toBe('FAIL');
  });

  it('fails closed after the bounded cleanup loop cannot reclaim the service', async () => {
    const harness = await createHarness({ bootoutLeavesJobLoaded: true });
    await expect(
      main(
        ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
        harness.deps
      )
    ).rejects.toThrow('LaunchAgent service remained loaded after 5 cleanup attempts');

    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.status).toBe('FAIL');
    expect(retained.cleanup.jobAbsent).toBe(false);
    expect(harness.state.bootoutAttempts).toBe(5);
  });

  it('captures PID before a later identity failure and performs bounded cleanup', async () => {
    const harness = await createHarness({
      loadedProgram: '/wrong/Other.app/Contents/MacOS/Chirality',
      bootoutLeavesJobLoaded: true
    });
    await expect(
      main(
        ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
        harness.deps
      )
    ).rejects.toThrow('Loaded job program does not match');

    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.process.pidObserved).toBe(true);
    expect(retained.cleanup.processAbsent).toBe(true);
    expect(retained.cleanup.jobAbsent).toBe(false);
    expect(harness.state.signals).toEqual(['SIGTERM']);
  });

  it('never reports an unknown PID as proven absent', async () => {
    const harness = await createHarness({ omitLoadedPid: true });
    await expect(
      main(
        ['--app-path', harness.appPath, '--output-root', harness.outputRoot, '--label', harness.label],
        harness.deps
      )
    ).rejects.toThrow('ambiguous process identity');
    const retained = JSON.parse(
      await readFile(path.join(harness.outputRoot, 'summary.json'), 'utf8')
    );
    expect(retained.process.pidObserved).toBe(false);
    expect(retained.cleanup.processAbsent).toBe(false);
  });

  it('does not write evidence into the actual LaunchAgents directory', async () => {
    const harness = await createHarness();
    await expect(
      main(
        [
          '--app-path',
          harness.appPath,
          '--output-root',
          path.join(harness.home, 'Library', 'LaunchAgents', 'unsafe-evidence'),
          '--label',
          harness.label
        ],
        harness.deps
      )
    ).rejects.toThrow('overlaps');
    expect(harness.state.mutations).toEqual([]);
  });

  it('rejects output-root symlink ancestors targeting LaunchAgents or the packaged app', async () => {
    for (const targetName of ['launch-agents', 'packaged-app']) {
      const harness = await createHarness();
      const target =
        targetName === 'launch-agents'
          ? path.join(harness.home, 'Library', 'LaunchAgents')
          : harness.appPath;
      const link = path.join(harness.root, `${targetName}-link`);
      await symlink(target, link);
      await expect(
        main(
          [
            '--app-path',
            harness.appPath,
            '--output-root',
            path.join(link, 'unsafe-evidence'),
            '--label',
            harness.label
          ],
          harness.deps
        )
      ).rejects.toThrow('symbolic-link ancestor');
      expect(harness.state.mutations).toEqual([]);
    }
  });
});
