import { describe, expect, it } from 'vitest';
import { createRequire } from 'node:module';
import { chmodSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const require = createRequire(import.meta.url);
const { applyFinalWrongServerCheck, assessClientCapture, assertNoWrongServerEvents, assertWrongPeerEvidence, captureChild, exactOwnedJob, fixedServiceUnoccupied, launchAgentPlist, pressureTerminalEvidence, runClient } = require('../tools/native-admission/p2-host-xpc-probe/p2-host-xpc-probe.cjs');

describe('P2 host XPC probe custody helpers', () => {
  it('treats the fixed Mach service as occupied regardless of the owning job label', () => {
    expect(fixedServiceUnoccupied('services = { "com.example.other" => active }')).toBe(true);
    expect(fixedServiceUnoccupied('job = com.unrelated.owner\nMachServices = { "com.chirality.app.runtime.account-host" => active }')).toBe(false);
  });

  it('permits cleanup only when the unique job still names both owned executables', () => {
    const owned = { label: 'com.chirality.probe.123', expiringExec: '/stage/expiring', serverHost: '/stage/correct/Electron' };
    const state = `${owned.label}\nprogram = ${owned.expiringExec}\narguments = { ${owned.serverHost} }`;
    expect(exactOwnedJob(state, owned)).toBe(true);
    expect(exactOwnedJob(state.replace(owned.serverHost, '/Applications/Chirality.app'), owned)).toBe(false);
    expect(exactOwnedJob(state.replace(owned.label, 'com.someone.else'), owned)).toBe(false);
  });

  it('renders a non-restarting fixed-service job through the expiring executable', () => {
    const plist = launchAgentPlist({
      label: 'com.chirality.probe.123',
      programArguments: ['/stage/expiring', '45', '/stage/correct/Electron', '/stage/driver.mjs', '--peer-requirement', 'anchor & identity'],
      stdout: '/stage/run/server.jsonl', stderr: '/stage/run/server.stderr'
    });
    expect(plist).toContain('<key>com.chirality.app.runtime.account-host</key><true/>');
    expect(plist).toContain('<key>KeepAlive</key><false/>');
    expect(plist).toContain('<key>RunAtLoad</key><true/>');
    expect(plist).toContain('<string>/stage/expiring</string><string>45</string><string>/stage/correct/Electron</string>');
    expect(plist).toContain('anchor &amp; identity');
  });

  it('retains a nonzero child JSON failure after stdout and stderr close', async () => {
    const root = mkdtempSync(join(tmpdir(), 'chirality-p2-child-'));
    try {
      const capture = await captureChild({
        command: process.execPath,
        args: ['-e', 'process.stdout.write(JSON.stringify({result:"FAIL",reason:"precise-child-failure"})+"\\n");process.stderr.write("detail\\n");process.exitCode=7'],
        environment: { PATH: process.env.PATH ?? '' }, evidenceRoot: root, caseId: 'failure', timeoutMs: 2000
      });
      expect(capture).toMatchObject({ exitCode: 7, stdoutClosed: true, stderrClosed: true, closeObserved: true, timedOut: false, overflow: false });
      expect(readFileSync(capture.stderrPath, 'utf8')).toBe('detail\n');
      expect(() => assessClientCapture(capture)).toThrow('precise-child-failure');
      expect(JSON.parse(readFileSync(capture.metadataPath, 'utf8'))).toMatchObject({ args: capture.args, environment: capture.environment, closeObserved: true });
    } finally { rmSync(root, { recursive: true, force: true }); }
  });

  it('retains spawn and observation-timeout failures without interpreting them as transport results', async () => {
    const root = mkdtempSync(join(tmpdir(), 'chirality-p2-child-'));
    try {
      const missing = await captureChild({ command: join(root, 'absent-command'), args: [], environment: {}, evidenceRoot: root, caseId: 'spawn', timeoutMs: 100 });
      expect(missing.spawnError).toBeTruthy();
      expect(() => assessClientCapture(missing)).toThrow('client-spawn:');
      const timedOut = await captureChild({ command: process.execPath, args: ['-e', 'setTimeout(()=>{},50)'], environment: {}, evidenceRoot: root, caseId: 'timeout', timeoutMs: 5 });
      expect(timedOut).toMatchObject({ timedOut: true, closeObserved: false });
      expect(() => assessClientCapture(timedOut)).toThrow('client-observation-timeout');
      await new Promise((resolve) => setTimeout(resolve, 100));
    } finally { rmSync(root, { recursive: true, force: true }); }
  });

  it('creates the private evidence directory before the first real client launch', async () => {
    const root = mkdtempSync(join(tmpdir(), 'chirality-p2-client-'));
    const launcher = join(root, 'controlled-launcher');
    const evidenceRoot = join(root, 'not-created-yet');
    writeFileSync(launcher, `#!${process.execPath}\nconst fs=require('node:fs');const a=process.argv.slice(2);const d=a[a.indexOf('--diagnostic')+1];for(const event of ['load-started','load-completed','client-binding-loaded','client-created','provision-invoked','close-completed'])fs.appendFileSync(d,JSON.stringify({event})+'\\n');process.stdout.write(JSON.stringify({result:'PASS',mode:'client-close'})+'\\n');\n`);
    chmodSync(launcher, 0o700);
    try {
      const evidence = await runClient(launcher, '/synthetic/host', '/synthetic/driver', [], {
        requestId: 'first-client', mode: 'client-close', environment: { PATH: process.env.PATH ?? '' }, evidenceRoot
      });
      expect(evidence.resultRecord).toMatchObject({ result: 'PASS', mode: 'client-close' });
      expect(evidence.milestones.map(({ event }: { event: string }) => event)).toContain('provision-invoked');
    } finally { rmSync(root, { recursive: true, force: true }); }
  });

  it('rejects malformed and overflowed child output while retaining bounded raw evidence', async () => {
    const root = mkdtempSync(join(tmpdir(), 'chirality-p2-child-'));
    try {
      const malformed = await captureChild({ command: process.execPath, args: ['-e', 'process.stdout.write("not-json\\n")'], environment: {}, evidenceRoot: root, caseId: 'malformed', timeoutMs: 2000 });
      expect(() => assessClientCapture(malformed)).toThrow('malformed-client-output');
      const overflow = await captureChild({ command: process.execPath, args: ['-e', 'process.stdout.write("x".repeat(70000))'], environment: {}, evidenceRoot: root, caseId: 'overflow', timeoutMs: 2000 });
      expect(overflow).toMatchObject({ stdoutBytes: 70000, stdoutRetained: 65536, overflow: true });
      expect(() => assessClientCapture(overflow)).toThrow('client-output-too-large');
    } finally { rmSync(root, { recursive: true, force: true }); }
  });

  it('requires complete wrong-peer attempt and close evidence without client ceremony', () => {
    const evidence = {
      resultRecord: { mode: 'wrong-peer', requestId: 'wrong-peer', disposition: 'observation-expired-local-close' },
      milestones: ['load-started', 'load-completed', 'client-binding-loaded', 'client-created', 'provision-invoked', 'close-completed'].map((event) => ({ event }))
    };
    expect(() => assertWrongPeerEvidence(evidence)).not.toThrow();
    expect(() => assertWrongPeerEvidence({ ...evidence, milestones: [...evidence.milestones, { event: 'challenge-observed' }] })).toThrow('wrong-peer-client-ceremony-observed');
    expect(() => assertWrongPeerEvidence({ ...evidence, milestones: evidence.milestones.filter(({ event }) => event !== 'provision-invoked') })).toThrow('wrong-peer-missing-provision-invoked');
  });

  it('rejects any admission in the isolated wrong-client interval and late matching ceremony', () => {
    const before = [{ event: 'pong', requestId: 'ping-control' }];
    expect(() => assertNoWrongServerEvents(before, [...before, { event: 'invalidated' }], 'wrong-peer')).not.toThrow();
    expect(() => assertNoWrongServerEvents(before, [...before, { event: 'admitted', connectionId: 'opaque' }], 'wrong-peer')).toThrow('wrong-peer-reached-server');
    expect(() => assertNoWrongServerEvents(before, [...before, { event: 'open', requestId: 'wrong-peer' }], 'wrong-peer')).toThrow('wrong-peer-reached-server');
  });

  it('reads terminal pressure evidence from the retained child result record', () => {
    const nested = [{ name: 'bounded-terminal-delivery-pressure', evidence: { resultRecord: { terminallyRejected: 1 } } }];
    expect(pressureTerminalEvidence(nested)).toBe(true);
    expect(pressureTerminalEvidence([{ name: 'bounded-terminal-delivery-pressure', evidence: { terminallyRejected: 1 } }])).toBe(false);
  });

  it('reverses the wrong-peer and overall PASS when the closed server log reveals late ceremony', () => {
    const output = {
      result: 'PASS', reason: null, primaryFailure: null,
      cases: [{ name: 'wrong-peer-bounded-nonadmission', result: 'PASS', evidence: { resultRecord: { disposition: 'observation-expired-local-close' } } }]
    };
    expect(applyFinalWrongServerCheck(output, [{ event: 'closed' }])).toBe(true);
    expect(applyFinalWrongServerCheck(output, [{ event: 'open', requestId: 'wrong-peer' }, { event: 'closed' }])).toBe(false);
    expect(output).toMatchObject({ result: 'FAIL', reason: 'wrong-peer-late-server-ceremony', primaryFailure: 'wrong-peer-late-server-ceremony' });
    expect(output.cases[0]).toMatchObject({ result: 'FAIL', reason: 'wrong-peer-late-server-ceremony' });
  });
});
