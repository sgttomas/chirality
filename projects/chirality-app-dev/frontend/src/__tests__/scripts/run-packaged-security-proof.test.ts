import { describe, expect, it } from 'vitest';
import { EGRESS_LAYER_PROBE_URL } from '../../../electron/renderer-window-policy';
import {
  EGRESS_PROBE_DECOY_URL,
  EGRESS_PROBE_URL,
  credentialProviderIsolation,
  descendantProcessIds,
  evaluateCredentialEvidence,
  inspectPackagedPolicyMarkers,
  packagedProofPass,
  parseArgs,
  parseLsofOutbound,
  sensitiveMaterialFindings,
  summarizeNetworkEvidence,
  summarizeRendererSecurityEvidence
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

  it('expects exactly the egress-probe destination the app fixes, and sets only a loopback decoy in the environment', () => {
    // DEL-09-06-V3-05: the app never reads the probe URL from the environment;
    // the proof's expectation must be byte-equal to the app's constant.
    expect(EGRESS_PROBE_URL).toBe(EGRESS_LAYER_PROBE_URL);
    const destination = new URL(EGRESS_PROBE_URL);
    expect(destination.hostname).toBe('api.anthropic.com');
    expect(destination.port).toBe('8443');
    // The decoy is a destination the egress policy would allow (loopback) but that
    // refuses the connection on the host itself: nothing can leave the machine
    // even if a regression made the app honour the variable again.
    const decoy = new URL(EGRESS_PROBE_DECOY_URL);
    expect(decoy.hostname).toBe('127.0.0.1');
    expect(decoy.port).toBe('9');
    expect(EGRESS_PROBE_DECOY_URL).not.toBe(EGRESS_PROBE_URL);
  });

  it('requires blocked diagnostics, all three probes, and zero non-allowlisted TCP', () => {
    const egressPayload = '{"policy":"REQ-NET-001","destination":{"protocol":"https:","hostname":"api.anthropic.com","port":"8443"},"outcome":"rejected","error":"net::ERR_BLOCKED_BY_CLIENT"}';
    const logText = [
      'Blocked renderer outbound request by network policy { destination: redacted }\n',
      "Blocked renderer outbound request by network policy { reason: 'anthropic_port_not_allowlisted:8443' }\n",
      '[network-policy-probe] {"policy":"REQ-NET-001","results":[',
      '{"url":"https://example.com/chirality-packaged-security-blocked","ok":false},',
      '{"url":"http://127.0.0.1:9/chirality-packaged-security-loopback","ok":false}]}\n',
      `[egress-layer-probe] ${egressPayload}`
    ].join('');
    const snapshots = [
      { pids: [10, 11], endpoints: [{ endpoint: '127.0.0.1:6000', host: '127.0.0.1', class: 'loopback', line: 'fixture' }] }
    ];
    const summary = summarizeNetworkEvidence(logText, snapshots);

    expect(summary.pass).toBe(true);
    expect(summary.egressLayerDiagnostics).toBe(1);
    expect(summary.egressProbeObserved).toBe(true);
    expect(summary.egressProbeUnexpectedDestinations).toEqual([]);
    expect(summary.nonAllowlistedOutboundTcp).toEqual([]);

    // The egress layer must be observed on its own, from the main-process
    // probe: a CSP-only block of the example.com probe is not enough, and a
    // probe that got a response means the egress layer let it through.
    const cspOnly = logText.replace(
      "Blocked renderer outbound request by network policy { reason: 'anthropic_port_not_allowlisted:8443' }\n",
      ''
    );
    expect(summarizeNetworkEvidence(cspOnly, snapshots).pass).toBe(false);
    const responded = logText.replace('"outcome":"rejected"', '"outcome":"response","status":200');
    expect(summarizeNetworkEvidence(responded, snapshots).egressProbeObserved).toBe(false);
    expect(summarizeNetworkEvidence(responded, snapshots).pass).toBe(false);

    // The probe destination is fixed in the app (DEL-09-06-V3-05): a payload for the
    // allowlisted port, for a destination without the port, or for any other
    // destination (the loopback decoy the proof sets in the environment) is not
    // the expected observation and fails the proof.
    const allowlistedPort = logText.replace('"port":"8443"', '"port":"443"');
    expect(summarizeNetworkEvidence(allowlistedPort, snapshots).egressProbeObserved).toBe(false);
    expect(summarizeNetworkEvidence(allowlistedPort, snapshots).egressProbeUnexpectedDestinations).toEqual([
      { protocol: 'https:', hostname: 'api.anthropic.com', port: '443' }
    ]);
    expect(summarizeNetworkEvidence(allowlistedPort, snapshots).pass).toBe(false);
    const portless = logText.replace(',"port":"8443"', '');
    expect(summarizeNetworkEvidence(portless, snapshots).egressProbeObserved).toBe(false);
    expect(summarizeNetworkEvidence(portless, snapshots).pass).toBe(false);
    const decoyFollowed = logText.replace(
      '{"protocol":"https:","hostname":"api.anthropic.com","port":"8443"}',
      '{"protocol":"http:","hostname":"127.0.0.1","port":"9"}'
    );
    const decoySummary = summarizeNetworkEvidence(decoyFollowed, snapshots);
    expect(decoySummary.egressProbeObserved).toBe(false);
    expect(decoySummary.egressProbeUnexpectedDestinations).toEqual([
      { protocol: 'http:', hostname: '127.0.0.1', port: '9' }
    ]);
    expect(decoySummary.pass).toBe(false);
    // An extra payload for another destination fails even beside the expected one.
    const extraDestination = `${logText}\n[egress-layer-probe] {"policy":"REQ-NET-001","destination":{"protocol":"http:","hostname":"127.0.0.1","port":"9"},"outcome":"rejected","error":"net::ERR_CONNECTION_REFUSED"}`;
    const extraSummary = summarizeNetworkEvidence(extraDestination, snapshots);
    expect(extraSummary.egressProbeObserved).toBe(true);
    expect(extraSummary.egressProbeUnexpectedDestinations).toHaveLength(1);
    expect(extraSummary.pass).toBe(false);
  });

  it('requires the renderer hardening evidence from the packaged page', () => {
    const csp = "default-src 'self'; script-src 'self' 'unsafe-inline'; connect-src 'self'; frame-src 'none'; object-src 'none'";
    const payload = {
      policy: 'G-CSP',
      cspHeader: csp,
      windowOpen: { returned: 'null' },
      violations: [
        { blockedURI: 'https://example.com', effectiveDirective: 'connect-src', disposition: 'enforce' }
      ],
      navigationAttempted: 'https://example.com/chirality-renderer-security-navigation'
    };
    const logText = [
      `[renderer-security-probe] ${JSON.stringify(payload)}`,
      '[chirality-desktop] [warn] renderer.window_open.denied {"destination":{"protocol":"https:","hostname":"example.com"}}',
      '[chirality-desktop] [warn] renderer.navigation.denied {"event":"will-navigate","reason":"ORIGIN_NOT_RENDERER"}'
    ].join('\n');

    const summary = summarizeRendererSecurityEvidence(logText);
    expect(summary).toMatchObject({
      cspHeaderPresent: true,
      cspViolationObserved: true,
      unexpectedViolations: [],
      windowOpenReturnedNull: true,
      windowOpenDeniedLogged: true,
      navigationAttempted: true,
      navigationDeniedLogged: true,
      pass: true
    });

    expect(summarizeRendererSecurityEvidence(logText.replace('renderer.navigation.denied', 'x')).pass).toBe(false);
    expect(summarizeRendererSecurityEvidence(logText.replace('"returned":"null"', '"returned":"object"')).pass).toBe(false);
    expect(summarizeRendererSecurityEvidence(logText.replace("'unsafe-inline'", "'unsafe-inline' 'unsafe-eval'")).pass).toBe(false);
    // Exact directives only: the superseded port-wildcard form must not pass.
    const wildcard = summarizeRendererSecurityEvidence(
      logText.replace("connect-src 'self';", "connect-src 'self' https://api.anthropic.com:*;")
    );
    expect(wildcard.cspHeaderPresent).toBe(false);
    expect(wildcard.pass).toBe(false);
    expect(summarizeRendererSecurityEvidence(logText.replace("connect-src 'self';", "connect-src 'self' https://example.com;")).cspHeaderPresent).toBe(false);
    expect(summarizeRendererSecurityEvidence(logText.replace("frame-src 'none';", "frame-src 'self';")).cspHeaderPresent).toBe(false);
    const ownResourceViolation = JSON.stringify({
      ...payload,
      violations: [...payload.violations, { blockedURI: 'http://127.0.0.1:41234/_next/static/x.js', effectiveDirective: 'script-src-elem' }]
    });
    const withOwnViolation = summarizeRendererSecurityEvidence(logText.replace(JSON.stringify(payload), ownResourceViolation));
    expect(withOwnViolation.unexpectedViolations).toHaveLength(1);
    expect(withOwnViolation.pass).toBe(false);
    expect(summarizeRendererSecurityEvidence('no probe at all').pass).toBe(false);
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
      'ATTACHMENT_FAILURE',
      'Content-Security-Policy',
      'renderer.window_open.denied',
      'renderer.navigation.denied'
    ].join('\n');
    expect(inspectPackagedPolicyMarkers(packagedMain).allPresent).toBe(true);
    expect(inspectPackagedPolicyMarkers(packagedMain.replace('renderer.navigation.denied', '')).allPresent).toBe(false);

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
      rendererSecurityProofPass: true,
      metadataLeakFindingCount: 0
    };

    expect(packagedProofPass({ ...otherwisePassing, cleanupPass: true })).toBe(true);
    expect(packagedProofPass({ ...otherwisePassing, cleanupPass: false })).toBe(false);
  });
});
