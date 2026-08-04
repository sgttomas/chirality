# Facts that must be supplied or independently established

Status: `FACT REQUEST INVENTORY — NOT A DECISION FORM`

No answer is requested through this carrier. These facts are grouped so later
acquisition work does not silently infer them.

## Accountable owner / product facts

- deployment and process topology considered in scope;
- supported OS versions, architectures, packaging channels, and lifecycle;
- acceptable isolation/cost tradeoff and sandbox lifetime posture;
- grant issuer, policy authority, evaluator trust, and trust anchors;
- acceptable replay/expiry/revocation and evidence-tamper posture;
- protected-data classes, access roles, retention/deletion/legal-hold rules;
- acceptable interruption and cleanup latency caps by tool/effect class;
- budget maxima, truncation/data-loss, artifact, and continuation posture;
- permitted test-only fixture posture;
- implementation-family membership and affected-client acceptance owners;
- compatibility/migration window and cryptographic-agility posture.

## Vendor / provider facts

- documented interruption/cancellation acknowledgement and cleanup guarantees;
- native-tool process/resource ownership and force behavior;
- SDK/tool schema/version stability and supported platforms;
- credential/channel isolation guarantees;
- receipt/event authenticity and ordering guarantees, if relied upon;
- licensing, redistribution, support, and security-update commitments for any
  backend component.

## Platform / packaging facts

- backend API availability in signed, entitled, notarized, installed, and
  managed execution contexts;
- exact rights expressibility and known unsupported resource classes;
- symlink/path-race, process-tree, IPC/device/network, and credential behavior;
- unsupported OS/backend-pair failure behavior;
- CI or physical-host evidence for each intended platform cell;
- architecture-specific and OS-version-specific differences.

The Phase-1 host probe supplies none of these facts beyond one local negative
observation: `sandbox-exec` is present but cannot apply the `no-network` named
profile in the current managed environment.
