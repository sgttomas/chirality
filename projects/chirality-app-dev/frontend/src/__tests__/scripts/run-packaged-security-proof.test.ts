import { describe, expect, it } from 'vitest';
import {
  credentialProviderIsolation,
  descendantProcessIds,
  evaluateCredentialEvidence,
  inspectPackagedPolicyMarkers,
  packagedProofPass,
  parseArgs,
  parseLsofOutbound,
  sensitiveMaterialFindings,
  summarizeNetworkEvidence
} from '../../../scripts/run-packaged-security-proof.mjs';

describe('run-packaged-security-proof script', () => {
  it('normalizes explicit packaged proof inputs', () => {
    const args = parseArgs([
      '--app-path',
      './dist/mac-arm64/Chirality.app',
      '--output-root',
      './artifacts/proof',
      '--source-revision',
      'abc123',
      '--capture-seconds',
      '9'
    ]);

    expect(args.appPath).toContain('/dist/mac-arm64/Chirality.app');
    expect(args.outputRoot).toContain('/artifacts/proof');
    expect(args.sourceRevision).toBe('abc123');
    expect(args.captureSeconds).toBe(9);
  });

  it('captures the complete packaged descendant process tree', () => {
    expect(
      descendantProcessIds(
        [
          { pid: 10, ppid: 1, command: 'packaged-gui' },
          { pid: 11, ppid: 10, command: 'renderer' },
          { pid: 12, ppid: 11, command: 'network-service' },
          { pid: 99, ppid: 1, command: 'unrelated' }
        ],
        [10]
      )
    ).toEqual([10, 11, 12]);
  });

  it('fails closed on non-loopback TCP while accepting isolated loopback traffic', () => {
    const parsed = parseLsofOutbound([
      'Chirality 10 user 20u IPv4 TCP 127.0.0.1:5000->127.0.0.1:6000 (ESTABLISHED)',
      'Chirality 11 user 21u IPv4 TCP 127.0.0.1:5001->203.0.113.4:443 (SYN_SENT)'
    ].join('\n'));

    expect(parsed.map((entry: { class: string }) => entry.class)).toEqual([
      'loopback',
      'external-non-allowlisted'
    ]);
  });

  it('requires blocked diagnostics, both probes, and zero non-allowlisted TCP', () => {
    const logText = [
      'Blocked renderer outbound request by network policy { destination: redacted }',
      '[network-policy-probe] {"policy":"REQ-NET-001","results":[',
      '{"url":"https://example.com/chirality-packaged-security-blocked","ok":false},',
      '{"url":"http://127.0.0.1:9/chirality-packaged-security-loopback","ok":false}]}'
    ].join('');
    const summary = summarizeNetworkEvidence(logText, [
      { pids: [10, 11], endpoints: [{ endpoint: '127.0.0.1:6000', host: '127.0.0.1', class: 'loopback', line: 'fixture' }] }
    ]);

    expect(summary.pass).toBe(true);
    expect(summary.nonAllowlistedOutboundTcp).toEqual([]);
  });

  it('requires every packaged security marker and reports only hashes for fixture leaks', () => {
    const packagedMain = [
      'REQ-NET-001',
      'api.anthropic.com',
      'anthropic_protocol_not_allowlisted',
      'anthropic_port_not_allowlisted',
      'host_not_allowlisted',
      'Blocked renderer outbound request by network policy',
      'Attachment exceeds per-file size limit',
      'Attachment exceeds per-turn size budget',
      'symbolic links are rejected',
      'ATTACHMENT_FAILURE'
    ].join('\n');
    expect(inspectPackagedPolicyMarkers(packagedMain).allPresent).toBe(true);

    const findings = sensitiveMaterialFindings('log has proof-key-value', [
      { label: 'fixture', value: 'proof-key-value' }
    ]);
    expect(findings).toHaveLength(1);
    expect(findings[0]).toEqual({
      label: 'fixture',
      sha256: expect.stringMatching(/^[a-f0-9]{64}$/)
    });
    expect(JSON.stringify(findings)).not.toContain('proof-key-value');
  });

  it('fails credential evidence when an operation-time stream leaks the fixture', () => {
    const fixture = 'packaged-proof-fixture-not-a-secret';
    const findings = evaluateCredentialEvidence(fixture, {
      beforeOperations: 'clean',
      completeDaemonStream: `credential stored: ${fixture}`,
      completeGuiStream: 'clean after stream closure'
    });

    expect(findings).toHaveLength(1);
    expect(findings[0].label).toBe('fixture-credential:completeDaemonStream');
    expect(JSON.stringify(findings)).not.toContain(fixture);
  });

  it('fails provider isolation when Anthropic mutation changes oMLX', () => {
    expect(
      credentialProviderIsolation({
        beforeOmlx: { configured: false },
        afterStoreOmlx: { configured: true },
        afterRemoveOmlx: { configured: false }
      })
    ).toBe(false);
  });

  it('requires confirmed cleanup in the final PASS predicate', () => {
    const otherwisePassing = {
      identityPresent: true,
      packagedPolicyPass: true,
      credentialProofPass: true,
      networkProofPass: true,
      metadataLeakFindingCount: 0
    };

    expect(packagedProofPass({ ...otherwisePassing, cleanupPass: true })).toBe(true);
    expect(packagedProofPass({ ...otherwisePassing, cleanupPass: false })).toBe(false);
  });
});
