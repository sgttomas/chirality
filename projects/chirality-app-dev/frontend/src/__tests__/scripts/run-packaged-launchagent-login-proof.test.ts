import { chmod, mkdir, mkdtemp, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  EVIDENCE_SCHEMA,
  SESSION_SCHEMA,
  SUMMARY_SCHEMA,
  main
} from '../../../scripts/run-packaged-launchagent-login-proof.mjs';

const roots: string[] = [];

async function fixture() {
  const root = await realpath(await mkdtemp(path.join(os.tmpdir(), 'chirality-login-proof-')));
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
    sessionId: 1001,
    loadedProgram: executablePath,
    loadedArguments: [executablePath, '--runtime-daemon'] as string[] | undefined,
    processExecutables: [executablePath] as string[],
    processInspectionError: undefined as Error | undefined,
    installError: undefined as Error | undefined,
    installedPlist: undefined as string | undefined,
    processAlive: false,
    pid: 8123,
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
    if (input.executable === '/usr/bin/osascript') {
      return {
        exitCode: 0,
        stdout: JSON.stringify({
          kCGSSessionIDKey: state.sessionId,
          kCGSessionUserIDKey: 501,
          kCGSessionOnConsoleKey: true,
          kCGSessionLoginDoneKey: true
        }),
        stderr: ''
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
      if (state.installError) throw state.installError;
      return { exitCode: 0, stdout: '', stderr: '' };
    }
    if (input.executable !== '/bin/launchctl') throw new Error(`Unexpected ${input.executable}`);
    if (input.args[0] === 'print') {
      const service = input.args[1];
      if (service.endsWith('/com.chirality.runtime')) {
        return { exitCode: 0, stdout: 'state = running\nprogram = /operator\npid = 77\n', stderr: '' };
      }
      if (!state.loaded) return notFound(label);
      return {
        exitCode: 0,
        stdout: `state = running\nprogram = ${state.loadedProgram}\n${
          state.loadedArguments
            ? `arguments = {\n${state.loadedArguments.join('\n')}\n}\n`
            : ''
        }pid = ${state.pid}\n`,
        stderr: ''
      };
    }
    if (input.args[0] === 'bootout') {
      state.loaded = false;
      state.processAlive = false;
      return { exitCode: 0, stdout: '', stderr: '' };
    }
    throw new Error(`Unexpected launchctl call ${input.args.join(' ')}`);
  };
  const deps = {
    platform: 'darwin',
    environment: { HOME: home },
    userInfo: () => ({ homedir: home }),
    uid: () => 501,
    now: () => new Date(state.loaded ? '2026-08-22T14:00:00.000Z' : '2026-08-21T14:00:00.000Z'),
    randomId: () => 'fixture',
    runCommand,
    processAlive: (pid: number) => pid === state.pid && state.processAlive,
    inspectProcessExecutables: async () => {
      if (state.processInspectionError) throw state.processInspectionError;
      return state.processExecutables;
    }
  };
  return { root, home, appPath, executablePath, sessionRoot, label, plistPath, state, deps };
}

afterEach(async () => {
  await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

describe('packaged LaunchAgent login-session proof preparation', () => {
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
    expect(summary.cleanup).toMatchObject({ jobAbsent: true, plistAbsent: true, runtimeDataRemoved: true });
    expect(summary.proofBoundary.harnessPerformedLogoutLogin).toBe(false);
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
    expect(summary.cleanup).toMatchObject({ jobAbsent: false, jobMutationRefused: true });
    expect(harness.state.loaded).toBe(true);
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
